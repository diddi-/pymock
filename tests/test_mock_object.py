from unittest import TestCase

from pymock.mock_attribute import MockAttribute
from pymock.mock_object import MockObject


class TestMockObject(TestCase):

    def enable_recording(self, mock: MockObject):
        mock._MockObject__PyMock__start_recording()

    def disable_recording(self, mock: MockObject):
        mock._MockObject__PyMock__disable_recording()

    def test_get_field_returns_MockAttribute_when_recording(self):
        mock = MockObject()
        self.assertIsInstance(mock.my_field, MockAttribute)

    def test_get_method_returns_MockAttribute_when_recording(self):
        mock = MockObject()
        self.assertIsInstance(mock.my_method(), MockAttribute)

    def test_get_field_returns_recorded_field_when_not_recording(self):
        mock = MockObject()
        expected = mock.my_field
        self.disable_recording(mock)
        self.assertEqual(expected, mock.my_field)

    def test_get_method_returns_recorded_method_when_not_recording(self):
        mock = MockObject()
        expected = mock.my_method()
        self.disable_recording(mock)
        self.assertEqual(expected, mock.my_method)

    def test_get_same_field_twice_returns_same_MockAttribute_when_recording(self):
        mock = MockObject()
        expected = mock.my_field
        self.assertEqual(expected, mock.my_field)

    def test_get_same_method_twice_returns_same_MockAttribute_when_recording(self):
        mock = MockObject()
        expected = mock.my_method()
        self.assertEqual(expected, mock.my_method())

    def test_get_same_method_twice_with_arguments_returns_same_MockAttribute_when_recording(self):
        mock = MockObject()
        expected = mock.my_method(123)
        self.assertEqual(expected, mock.my_method(123))

    def test_get_methods_with_different_arguments_returns_different_MockAttribute_when_recording(self):
        mock = MockObject()
        expected = mock.my_method(123)
        self.assertNotEqual(expected, mock.my_method("abc"))
