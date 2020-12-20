# PyMock
_Mocking in Python made easy!_

![PyMock](https://github.com/diddi-/pymock/workflows/PyMock/badge.svg)

# Install
PyMock can be installed with pip
```bash
$ pip install python-mock
```
**Note**: PyMock require Python version >= 3.7 to work properly.

# How is it different?

The typical way of mocking in Python is with `MagicMock` or simply `Mock` (https://docs.python.org/3/library/unittest.mock.html).
```python
def test_something():
    blog = MagicMock()
    blog.get_post.return_value = Post()
    assert isinstance(blog.get_post(1), Post)
```
While this technically work the syntax can be difficult to remember, provides limited
support for when your return values depend on input arguments and even if you're using a decent IDE
there is no [_type hinting_](https://www.python.org/dev/peps/pep-0484/) available to help with code completion.

`PyMock` attempts to solve all of these issues by offering a simple syntax and full control over how
your mocks should respond in different situations. The same example as above can be written using
PyMock:
```python
def test_something():
    blog = PyMock.create(Blog)
    PyMock.setup(blog.get_post(1)).returns(Post())
    assert isinstance(blog.get_post(1), Post)
```
The benefits here are many, for example
* Just by looking at the first line it's very clear what type of object you intend to mock
* PyMock support setting different return values for different input arguments. In this case
  it's `blog.get_post(1)` that should return an instance of `Post`, not `blog.get_post(2)` or any
  other call to the same method.
* Because PyMock know exactly what the mocked type is, code completion work just as if it were an
object of that type.

![Code completion in action](https://raw.githubusercontent.com/diddi-/pymock/master/docs/img/pymock-type-hinting.png)

# Feedback
PyMock is an early state of development and is likely to contain bugs. Quite possibly lots of them.
Don't let that hold you back from trying it out and [_let me know_](https://github.com/diddi-/pymock) how it works for you!
All kinds of feedback are valuable, good and bad
* Bug reports
* Performance
* Syntax
* Overall experience
* Success stories
* Anything else you want to share :)

# Examples
Below are a few examples on how PyMock can be used.
```python
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
        mock = PyMock.create(Blog)
        PyMock.setup(mock.get_post(123)).returns(post)

        self.assertEqual(post, mock.get_post(123))

    def test_setup_multiple_values(self):
        post1 = Post()
        post2 = Post()
        mock = PyMock.create(Blog)
        PyMock.setup(mock.get_post(1)).returns(post1)
        PyMock.setup(mock.get_post(2)).returns(post2)

        self.assertEqual(post1, mock.get_post(1))
        self.assertEqual(post2, mock.get_post(2))

    def test_raise_exception(self):
        mock = PyMock.create(Blog)
        PyMock.setup(mock.get_post(1)).raises(CustomException())

        with self.assertRaises(CustomException):
            mock.get_post(1)

    def test_match_instance_type(self):
        post = Post()
        mock = PyMock.create(Blog)
        PyMock.setup(mock.get_post(Is.type(int))).returns(post)

        self.assertEqual(post, mock.get_post(12345))

    def test_recursive_mocking(self):
        mock = PyMock.create(Blog)
        PyMock.setup(mock.get_post(123).get_title()).returns("PyMock is awesome")

        self.assertEqual("PyMock is awesome", mock.get_post(123).get_title())

    def test_mock_function(self):
        def my_function():
            pass
        mock = PyMock.create(my_function)
        PyMock.setup(mock()).returns("my_function return value")

        self.assertEqual("my_function return value", mock())
```
