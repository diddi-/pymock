from unittest import TestCase
from unittest.mock import MagicMock

from pymock import PyMock, Is


class TestExamples(TestCase):

    def test_return_object(self):
        class Person:
            pass
        bob = Person()
        mock = PyMock()
        mock.call("bob").returns(bob)
        person_repository = MagicMock()
        person_repository.get_person.side_effect = mock
        self.assertEqual(bob, person_repository.get_person("bob"))

    def test_call_multiple_values(self):
        mock = PyMock()
        mock.call(1, 1).returns(2)
        mock.call(1, 2).returns(3)
        calculator = MagicMock()
        calculator.add.side_effect = mock

        self.assertEqual(2, calculator.add(1, 1))
        self.assertEqual(3, calculator.add(1, 2))

    def test_raise_exception(self):
        class MyException(Exception):
            pass
        mock = PyMock()
        mock.call("invalid").raises(MyException())
        my_object = MagicMock()
        my_object.method.side_effect = mock

        with self.assertRaises(MyException):
            my_object.method("invalid")

    def test_return_magicmock_when_not_matching_any_calls(self):
        mock = PyMock()
        mock.call("won't match this").returns(1)
        my_object = MagicMock()
        my_object.method.side_effect = mock

        self.assertIsInstance(my_object.method("hello"), MagicMock)

    def test_match_instance_type(self):
        class Date:
            pass
        mock = PyMock()
        mock.call(Is.type(Date)).returns(True)
        calendar = MagicMock()
        calendar.has_events.side_effect = mock

        self.assertEqual(True, calendar.has_events(Date()))
