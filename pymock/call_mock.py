from typing import Optional, Any

from pymock.action.call_action import CallAction
from pymock.action.raise_action import RaiseAction
from pymock.action.return_action import ReturnAction


class CallMock:
    def __init__(self, *arguments):
        self.__arguments = arguments
        self.__action: Optional[CallAction] = None

    def returns(self, return_value: Any):
        self.__action = ReturnAction(return_value)

    def raises(self, exception: Exception):
        self.__action = RaiseAction(exception)

    def execute(self):
        return self.__action.execute()

    def has_matchers(self, *arguments):
        if self.__arguments == arguments:
            return True
        return False
