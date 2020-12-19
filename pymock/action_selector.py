from typing import Any

from pymock.action.raise_action import RaiseAction
from pymock.action.return_action import ReturnAction
from pymock.mock_attribute import MockAttribute


# Hmmm need better name for this don't we?
class ActionSelector:
    def __init__(self, mock: MockAttribute):
        self.__mock = mock

    def returns(self, return_value: Any):
        self.__mock._MockObject__PyMock__action = ReturnAction(return_value)

    def raises(self, exception: Exception):
        self.__mock._MockObject__PyMock__action = RaiseAction(exception)
