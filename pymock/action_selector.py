from typing import Any

from pymock.action.raise_action import RaiseAction
from pymock.action.return_action import ReturnAction
from pymock.mock_object import MockObject


class ActionSelector:  # Hmmm need better name for this don't we?
    def __init__(self, mock: MockObject):
        self.__mock = mock

    def returns(self, return_value: Any):
        self.__mock._MockObject__PyMock__internal__value = ReturnAction(return_value)  # type: ignore

    def raises(self, exception: Exception):
        self.__mock._MockObject__PyMock__internal__value = RaiseAction(exception)  # type: ignore
