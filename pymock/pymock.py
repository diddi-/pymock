from typing import TypeVar, Type, cast, Any

from pymock.action_selector import ActionSelector
from pymock.mock_object import MockObject

T = TypeVar("T")


class PyMock:
    @staticmethod
    def create(cls: Type[T]):
        """ Create a new mock instance """
        return cast(T, MockObject())

    @staticmethod
    def setup(obj: Any):
        """ Setup an attribute and its return value

        Example:
                mock = PyMock.create(Blog)
                PyMock.setup(mock.get_post(123)).returns(Post())
        """
        return ActionSelector(obj)
