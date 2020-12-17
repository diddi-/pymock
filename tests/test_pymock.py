from unittest import TestCase
from unittest.mock import MagicMock

from pymock import PyMock


class TestPyMock(TestCase):

    def test_configured_call_is_executed_when_calling_PyMock_object(self):
        mock = PyMock()
        mock.call("arg1", "arg2").returns(1234)
        self.assertEqual(1234, mock("arg1", "arg2"))

    def test_MagicMock_instance_is_returned_when_no_matching_calls_are_found(self):
        mock = PyMock()
        self.assertIsInstance(mock(), MagicMock)
