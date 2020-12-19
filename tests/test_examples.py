from unittest import TestCase

from pymock import PyMock, Is


class Post:
    def get_title(self) -> str:
        pass


class Blog:
    def get_post(self, id: int) -> Post:
        pass


class CustomException(Exception):
    pass


class TestExamples(TestCase):

    def test_return_object(self):
        post = Post()
        with PyMock(Blog) as mock:
            PyMock.setup(mock.get_post(123)).returns(post)

        self.assertEqual(post, mock.get_post(123))

    def test_setup_multiple_values(self):
        post1 = Post()
        post2 = Post()
        with PyMock(Blog) as mock:
            PyMock.setup(mock.get_post(1)).returns(post1)
            PyMock.setup(mock.get_post(2)).returns(post2)

        self.assertEqual(post1, mock.get_post(1))
        self.assertEqual(post2, mock.get_post(2))

    def test_raise_exception(self):
        with PyMock(Blog) as mock:
            PyMock.setup(mock.get_post(1)).raises(CustomException())

        with self.assertRaises(CustomException):
            mock.get_post(1)

    def test_match_instance_type(self):
        post = Post()
        with PyMock(Blog) as mock:
            PyMock.setup(mock.get_post(Is.type(int))).returns(post)

        self.assertEqual(post, mock.get_post(12345))

    def test_recursive_mocking(self):
        with PyMock(Blog) as mock:
            PyMock.setup(mock.get_post(Is.type(int)).get_title()).returns("PyMock is awesome")

        self.assertEqual("PyMock is awesome", mock.get_post(123).get_title())

    def test_mocking_with_fallback_value(self):
        post = Post()
        default = Post()
        with PyMock(Blog) as mock:
            PyMock.setup(mock.get_post(123)).returns(post)
            PyMock.setup(mock.get_post(Is.type(int))).returns(default)

        self.assertEqual(post, mock.get_post(123))
        self.assertEqual(default, mock.get_post(456))
