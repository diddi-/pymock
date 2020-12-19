from unittest.mock import MagicMock

from pymock.action.call_action import CallAction
from pymock.action.return_action import ReturnAction
from pymock.mock_attribute import MockAttribute


class MockMethod(MockAttribute):
    def __init__(self, name: str):
        self.__name = name
        self.__action: CallAction = ReturnAction(MagicMock())

    @property
    def name(self):
        return self.__name

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value: CallAction):
        self.__action = value

    def return_value(self):
        return self.__action.execute()

    def enable_recording(self):
        pass

    def disable_recording(self):
        pass

    def __repr__(self):
        return f"<MockMethod: {self.__name}>"
