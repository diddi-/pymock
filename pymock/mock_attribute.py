from typing import Optional
from unittest.mock import MagicMock

from pymock.action.call_action import CallAction
from pymock.action.return_action import ReturnAction


class MockAttribute:
    def __init__(self, name: str):
        self.name = name
        self.args: Optional[tuple]
        self.kwargs: Optional[dict]
        self.action: CallAction = ReturnAction(MagicMock())
        self.modifiable = True

    def __call__(self, *args, **kwargs):
        if self.modifiable:
            self.args = args
            self.kwargs = kwargs
            return self
        else:
            return self.action.execute()

    def __repr__(self):
        return f"<MockAttribute: {self.name}>"
