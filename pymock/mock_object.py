from typing import Optional

from pymock.action.call_action import CallAction
from pymock.argsmap import ArgsMap


class MockObject:
    def __init__(self):
        self.__PyMock__internal__attributes = {}
        self.__PyMock__internal__calls = ArgsMap()
        self.__PyMock__internal__value: Optional[CallAction] = None

    def __getattr__(self, item):
        if item in self.__PyMock__internal__attributes.keys():
            return self.__PyMock__internal__attributes[item]

        m = MockObject()
        self.__PyMock__internal__attributes[item] = m
        return m

    def __call__(self, *args, **kwargs):
        if self.__PyMock__internal__calls.has_args(args):
            mock = self.__PyMock__internal__calls.get(args)
        else:
            mock = MockObject()
            self.__PyMock__internal__calls.add(args, mock)

        if mock._MockObject__PyMock__internal__value is not None:
            return mock._MockObject__PyMock__internal__value.execute()
        return mock

    def __eq__(self, other):
        if self.__PyMock__internal__value is not None:
            return self.__PyMock__internal__value == other
        if isinstance(other, MockObject):
            return id(self) == id(other)
        return False

    def __str__(self):
        if self.__PyMock__internal__value is not None:
            return str(self.__PyMock__internal__value)
        return f"<MockObject id={id(self)}>"
