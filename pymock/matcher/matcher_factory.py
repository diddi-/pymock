from pymock.matcher.type_matcher import TypeMatcher


class Is:

    @staticmethod
    def type(value):
        return TypeMatcher(value)
