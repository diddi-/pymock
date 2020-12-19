from typing import Generic, TypeVar, Type, cast, Any

from pymock.mock_object import MockObject
from pymock.action_selector import ActionSelector

T = TypeVar("T")


class PyMock(Generic[T]):
    """ PyMock context manager

    When used as a context manager this will control the recording modes of a MockObject and return
    it type-casted to the mocked type. This will make the MockObject _appear_ as if it was of the
    same type as the original mocked type.
    """
    def __init__(self, cls: Type[T]):
        self.__cls = cls
        self.__object = MockObject(cls)

    def __enter__(self):
        self.__object._MockObject__PyMock__start_recording()
        # This cast is purely to help (fool?) IDEs into resolving attributes of the original
        # mocked type.
        return cast(T, self.__object)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__object._MockObject__PyMock__stop_recording()
        pass


    # TODO: Could this be a decorator method to avoid the context manager?
    # Would the decorator fire before the argument call?
    @staticmethod
    def setup(call: Any):
        """ Setup an attribute and its return value

        Example:
            with PyMock(Blog) as mock:
                PyMock.setup(mock.get_post(123)).returns(Post())
        """
        return ActionSelector(call)

    def __repr__(self):
        return f"<PyMock: {self.__cls.__name__}>"
