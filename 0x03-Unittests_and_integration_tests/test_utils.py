#!/usr/bin/env python3
"""Test utils module with dynamic (parameterized) values"""
from parameterized import parameterized
from typing import (
    Any, Dict, Mapping, Sequence, Tuple, Union
)
import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize
import requests


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Union[Dict, int, Sequence],
                               expected: Any):
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Tuple[str],
        expected: Exception
    ) -> None:
        """test for exception raise"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_obj):
        """Test with patching and parameterization"""
        mock_resp = mock.Mock()
        mock_resp.json = mock.Mock(return_value=test_payload)
        mock_obj.return_value = mock_resp

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        mock_obj.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test memoization class"""

    # @parameterized.expand([
    #     ()
    # ])
    def test_memoize(self):
        """test utils.memoize()"""

        class TestClass:
            """Test class"""

            def a_method(self):
                """method for test"""
                return 42

            @memoize
            def a_property(self):
                """test property"""
                return self.a_method()

        with mock.patch.object(
            TestClass,
            'a_method',
            return_value=lambda: 42
        ) as mock_method:

            test_obj_class = TestClass()
            self.assertEqual(test_obj_class.a_property(), 42)
            self.assertEqual(test_obj_class.a_property(), 42)
            mock_method.assert_called_once()
