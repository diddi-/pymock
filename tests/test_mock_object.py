from typing import Any
from unittest import TestCase

from pymock.action.return_action import ReturnAction
from pymock.mock_object import MockObject


class Blog:
    def get_post(self):
        pass


class TestMockObject(TestCase):

    def set_value(self, obj: MockObject, value: Any):
        obj._MockObject__PyMock__internal__value = ReturnAction(value)  # type: ignore

    def test_MockObject_can_be_created(self):
        self.assertIsInstance(MockObject(), MockObject)

    def test_calling_a_method_on_MockObject_returns_new_MockObject(self):
        self.assertIsInstance(MockObject().method(), MockObject)

    def test_getting_data_attribute_on_MockObject_returns_new_MockObject(self):
        self.assertIsInstance(MockObject().data, MockObject)

    def test_calling_same_method_twice_return_same_result(self):
        mock = MockObject()
        self.assertEqual(mock.method(), mock.method())

    def test_calling_same_method_twice_with_arguments_return_same_result(self):
        mock = MockObject()
        self.assertEqual(mock.method(1), mock.method(1))

    def test_calling_same_method_twice_with_different_arguments_return_different_result(self):
        mock = MockObject()
        self.assertNotEqual(mock.method(1), mock.method(2))

    def test_getting_same_data_attribute_twice_return_same_result(self):
        mock = MockObject()
        self.assertEqual(mock.data, mock.data)

    def test_MockObject_with_integer_value_is_equal_to_the_value_itself(self):
        mock = MockObject()
        self.set_value(mock, 2)
        self.assertEqual(2, mock)

    def test_MockObject_with_string_value_is_equal_to_the_value_itself(self):
        mock = MockObject()
        self.set_value(mock, "PyMock")
        self.assertEqual("PyMock", mock)

    def test_setting_value_for_method_call_returns_same_value_on_successive_calls(self):
        mock = MockObject()
        self.set_value(mock.method(123), "PyMock")
        self.assertEqual("PyMock", mock.method(123))

    def test_data_attributes_can_be_set_with_standard_setattr(self):
        mock = MockObject()
        mock.data = 123
        self.assertEqual(123, mock.data)
