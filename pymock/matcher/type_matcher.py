from pymock.matcher.matcher import Matcher


class TypeMatcher(Matcher):
    def __init__(self, cls):
        self.__cls = cls

    def __eq__(self, other):
        if isinstance(other, self.__cls):
            return True
        return False

    def __hash__(self):
        # TODO: I have literally no idea what I'm doing here
        return hash("TypeMatcher")

    def __repr__(self):
        return f"<TypeMatcher: {self.__cls}>"
