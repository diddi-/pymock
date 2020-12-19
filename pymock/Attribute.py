from typing import Type


class Attribute:
    def __init__(self, name: str, attribute_type: Type):
        self.__name = name
        self.__type = attribute_type

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    def __eq__(self, other):
        if not isinstance(other, Attribute):
            return False
        return self.__name == other.name and self.__type == other.type

    def __repr__(self):
        return f"<Attribute: {self.__name}     {str(self.__type)}>"
