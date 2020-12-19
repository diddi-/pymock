from abc import abstractmethod


class MockAttribute:

    @abstractmethod
    def enable_recording(self):
        pass

    @abstractmethod
    def disable_recording(self):
        pass
