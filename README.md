# PyMock
PyMock is a set of tools to help with mocking in python.

The typical way of mocking and controlling returned values in python is with `MagicMock` or simply `Mock` (https://docs.python.org/3/library/unittest.mock.html).
```python
def test_something():
    my_object = MagicMock()
    my_object.some_method.side_effect = [val1, val2, val3]
```
A challenge often faced when working in a project is to know exactly how many times the mocked method is called
and in *what order*. For lists, `side_effect` return values one by one for each call to the method which
quickly becomes a game of chance getting that list correct. Sometimes the input arguments to the method is what should
determine which of the values to return which leaves you with the only option of creating another method or function
that `side_effect` can call to retrieve the correct value.

This is where `PyMock` comes in. Instead of fiddling with lists or writing separate functions,
you configure a `PyMock` instance with a set of `calls` and pass it in as a `side_effect`.
PyMock will look at the arguments passed in to the mocked method and return the correct value for you.
No extra code needed!

# Examples
```python
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
```
