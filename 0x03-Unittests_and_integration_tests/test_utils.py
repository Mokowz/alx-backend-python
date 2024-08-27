#!/usr/bin/env python3
"""Test Utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize, requests
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Test Access Nested Map Class"""
    @parameterized.expand([
      ({"a": 1}, ("a",), 1),
      ({"a": {"b": 2}}, ("a",), {"b": 2}),
      ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test Exception"""
        # with self.assertRaises(KeyError):
        #     access_nested_map(nested_map, path)
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test Get JSON Class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Test get json function
        """
        class Mocked(Mock):
            """Mocked class"""

            def json(self):
                """json function"""
                return payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """test Memoize class"""
    def test_memoize(self):
        """Test memoize function"""
        class TestClass:
            """Test Class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            ex = TestClass()
            ex.a_property
            ex.a_property
            mocked.assert_called_once()


if __name__ == '__main__':
    unittest.main()
