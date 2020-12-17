from __future__ import annotations

from typing import List, Any
from unittest.mock import MagicMock

from pymock.matcher.matcher import Matcher
from pymock.call_mock import CallMock


class PyMock:

    def __init__(self):
        self.__call_mocks: List[CallMock] = []

    def call(self, *matchers: Any) -> CallMock:
        entry = CallMock(matchers)
        self.__call_mocks.append(entry)
        return entry

    def __call__(self, *matchers: Matcher, **kwargs):
        for call in self.__call_mocks:
            if call.has_matchers(matchers):
                return call.execute()

        return MagicMock()

