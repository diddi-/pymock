from abc import abstractmethod


class CallAction:

    @abstractmethod
    def execute(self):
        pass
