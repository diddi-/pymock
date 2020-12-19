from typing import Dict

from pymock.mock_attribute import MockAttribute
from pymock.mock_type.mock_method import MockMethod


class AttributeInterceptor(MockMethod):
    def __init__(self, name: str):
        super().__init__(name)
        self.__recording_enabled = True
        self.__attributes: Dict[tuple, MockAttribute] = {}

    def enable_recording(self):
        self.__recording_enabled = True

    def disable_recording(self):
        self.__recording_enabled = False

    def __call__(self, *args, **kwargs):
        if not self.__recording_enabled:
            if args in self.__attributes:
                self.__attributes[args].return_value()
            return MockMethod(self.name).return_value()

        if args in self.__attributes.keys():
            return self.__attributes[args]

        attribute = MockMethod(self.name)
        self.__attributes[args] = attribute
        return attribute

    def __repr__(self):
        if self.__attributes:
            return f"<AttributeInterceptor: {self.name}(...)>"
        return f"<AttributeInterceptor: {self.name}>"
