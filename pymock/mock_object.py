from pymock.mock_attribute import MockAttribute


class MockObject:
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
    def __init__(self):
        self.__PyMock__methods = {}

    def __PyMock__start_recording(self):
        for m in self.__PyMock__methods.values():
            m.modifiable = True

    def __PyMock__stop_recording(self):
        for m in self.__PyMock__methods.values():
            m.modifiable = False

    def __getattr__(self, item):
        if item in self.__PyMock__methods.keys():
            return self.__PyMock__methods[item]
        m = MockAttribute(item)
        self.__PyMock__methods[item] = m
        return m

    def __repr__(self):
        return f"<MockObject: {self.__PyMock__object_class.__name__}>"
