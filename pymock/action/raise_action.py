
from pymock.action.call_action import CallAction


class RaiseAction(CallAction):
    def __init__(self, exception: Exception):
        self.__exception = exception

    def execute(self):
        raise self.__exception
