from typing import Tuple, Optional, Any

from pymock.action.call_action import CallAction
from pymock.action.raise_action import RaiseAction
from pymock.action.return_action import ReturnAction
from pymock.matcher.matcher import Matcher


class CallMock:
    def __init__(self, matchers: Tuple[Any]):
        self.__matchers = matchers
        self.__action: Optional[CallAction] = None

    def returns(self, return_value: Any):
        self.__action = ReturnAction(return_value)

    def raises(self, exception: Exception):
        self.__action = RaiseAction(exception)

    def execute(self):
        return self.__action.execute()

    def has_matchers(self, matchers: Tuple[Matcher]):
        if self.__matchers == matchers:
            return True
        return False
