from unittest import TestCase

from pymock.matcher.type_matcher import TypeMatcher


class TestTypeMatcher(TestCase):

    def test_string_matches_string_type(self):
        matcher = TypeMatcher(str)
        self.assertEqual(matcher, "string")

    def test_object_matches_its_class_type(self):
        class MyClass:
            pass
        matcher = TypeMatcher(MyClass)
        self.assertEqual(MyClass(), matcher)

    def test_object_matches_its_base_class_type(self):
        class Substring(str):
            pass
        matcher = TypeMatcher(str)
        self.assertEqual(Substring(), matcher)

    def test_integer_does_not_match_str_type(self):
        matcher = TypeMatcher(str)
        self.assertNotEqual(1, matcher)

    def test_object_does_not_match_class_type_it_doesnt_inherit_from(self):
        class MyClass:
            pass
        matcher = TypeMatcher(str)
        self.assertNotEqual(MyClass(), matcher)
