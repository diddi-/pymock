from typing import Any

from pymock.action.call_action import CallAction


class ReturnAction(CallAction):
    def __init__(self, return_value: Any):
        self.__return_value: Any = return_value

    def execute(self):
        return self.__return_value

    def __eq__(self, other):
        return self.__return_value == other

    def __repr__(self):
        return f"<ReturnAction: {self.__return_value}>"
