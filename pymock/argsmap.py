from __future__ import annotations
from typing import Dict, TYPE_CHECKING

# We only need to import MockObject to resolve the type checking which would otherwise result in a
# cyclic import error at runtime. Perhaps there is a more elegant way to resolve this but it's good
# for now.
if TYPE_CHECKING:
    from pymock.mock_object import MockObject


class ArgsMap:
    """ Maps a set of function arguments with MockObjects """
    def __init__(self):
        self.__arg_map: Dict[tuple, MockObject] = {}

    def add(self, args: tuple, obj: MockObject):
        self.__arg_map[args] = obj

    def has_args(self, args: tuple):
        return args in list(self.__arg_map.keys())

    def get(self, args: tuple):
        for arg in self.__arg_map.keys():
            if arg == args:
                return self.__arg_map[arg]
        raise ValueError(f"ArgsMap has no mapping for {args}")
