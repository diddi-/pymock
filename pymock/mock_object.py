from __future__ import annotations

from typing import Type, Dict

from pymock.action.call_action import CallAction
from pymock.action.return_action import ReturnAction


class MockObject(object):
    """ Class that represents a mocked object

    A MockObject operates in two modes, recording and non-recording. Recording mode will cause the
    MockObject to record and save all requests for an attribute (methods, fields, ..).

    In non-recording mode, when accessing an attribute the MockObject will return any previously
    recorded attribute matching the request (field name or method calls with matching arguments).

    The reason for this is to be able to retain the static type hinting support as if it were the
    original mocked type.

    Note: MockObject is not intended to be instantiated manually. It depends on the PyMock context
    manager to instantiate and control the recording modes.
    """

    # All attributes defined here MUST be prefixed with __PyMock__ to ensure they do not conflict
    # with any attribute defined in the mocked type.
    def __init__(self, mocked_type: Type, parent: MockObject = None):
        self.__PyMock__mocked_type = mocked_type
        self.__PyMock__parent = parent
        self.__PyMock__attributes: Dict[str, MockObject] = {}
        self.__PyMock__arguments: Dict[tuple, MockObject] = {}
        if parent:
            self.__PyMock__recording_enabled = parent._MockObject__PyMock__recording_enabled
        else:
            self.__PyMock__recording_enabled = False
        self.__PyMock__action: CallAction = ReturnAction(self)

    def __PyMock__start_recording(self):
        self.__PyMock__recording_enabled = True
        for mock in self.__PyMock__attributes.values():
            mock._MockObject__PyMock__start_recording()
        for mock in self.__PyMock__arguments.values():
            mock._MockObject__PyMock__start_recording()

    def __PyMock__stop_recording(self):
        self.__PyMock__recording_enabled = False
        for mock in self.__PyMock__attributes.values():
            mock._MockObject__PyMock__stop_recording()
        for mock in self.__PyMock__arguments.values():
            mock._MockObject__PyMock__stop_recording()

    def __getattr__(self, item):
        if item in self.__PyMock__attributes.keys():
            return self.__PyMock__attributes[item]

        mock = MockObject(self.__PyMock__mocked_type, self)
        self.__PyMock__attributes[item] = mock
        return mock

    def __call__(self, *args, **kwargs):
        for saved_args, mock in self.__PyMock__arguments.items():
            if args == saved_args:
                if self.__PyMock__recording_enabled:
                    return mock
                return mock._MockObject__PyMock__action.execute()

        mock = MockObject(self.__PyMock__mocked_type, self)
        self.__PyMock__arguments[args] = mock
        if self.__PyMock__recording_enabled:
            return mock
        return mock._MockObject__PyMock__action.execute()

    def __repr__(self):
        return f"<MockObject: {self.__PyMock__mocked_type.__name__}>"
