from unittest import TestCase

from pymock.argsmap import ArgsMap
from pymock.mock_object import MockObject


class TestArgsMap(TestCase):

    def test_argument_mapping_can_be_added(self):
        args = (1,)
        map = ArgsMap()
        map.add(args, MockObject())
        self.assertTrue(map.has_args(args))

    def test_MockObject_matching_argument_can_be_retrieved(self):
        args = (1,)
        mock = MockObject()
        map = ArgsMap()
        map.add(args, mock)
        self.assertEqual(mock, map.get(args))
