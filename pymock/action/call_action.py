from abc import ABC, abstractmethod


class CallAction(ABC):

    @abstractmethod
    def execute(self):
        pass
