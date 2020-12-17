from unittest import TestCase

from pymock.action.raise_action import RaiseAction


class TestRaiseAction(TestCase):

    def test_execute_raises_supplied_exception(self):
        action = RaiseAction(ValueError())
        self.assertRaises(ValueError, action.execute)

    def test_execute_raises_supplied_exception_with_message(self):
        action = RaiseAction(ValueError("message"))
        with self.assertRaises(ValueError) as err:
            action.execute()

        self.assertEqual("message", str(err.exception))
