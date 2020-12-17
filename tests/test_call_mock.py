from unittest import TestCase

from pymock.call_mock import CallMock


class TestCallMock(TestCase):

    def test_has_arguments_return_Frue_when_arguments_are_same(self):
        mock = CallMock("arg1", 2)
        self.assertTrue(mock.has_matchers("arg1", 2))

    def test_has_arguments_return_False_when_arguments_differs(self):
        mock = CallMock("arg1", 2)
        self.assertFalse(mock.has_matchers(1, 2))

    def test_has_arguments_return_False_when_number_of_arguments_differ(self):
        mock = CallMock(1, 2, 3)
        self.assertFalse(mock.has_matchers(1))
