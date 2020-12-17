from unittest import TestCase

from pymock.action.return_action import ReturnAction


class TestReturnAction(TestCase):

    def test_execute_returns_the_supplied_return_value(self):
        action = ReturnAction("string")
        self.assertEqual("string", action.execute())
