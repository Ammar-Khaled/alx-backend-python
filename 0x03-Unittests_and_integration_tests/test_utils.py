#!/usr/bin/env python3
"""Test utils functions."""
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from unittest import TestCase
from unittest.mock import Mock, patch


class TestAccessNestedMap(TestCase):
    """Test utils.access_nested_map."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """Test access_nested_map method."""
        access_nested_map = __import__('utils').access_nested_map
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """Test access_nested_map exceptions."""
        access_nested_map = __import__('utils').access_nested_map
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Test utils.get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mocked_requests_get: Mock):
        """Test get_json function with a mocked HTTP request."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mocked_requests_get.return_value = mock_response
        get_json = __import__('utils').get_json
        res = get_json(test_url)
        mocked_requests_get.assert_called_once_with(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(TestCase):
    """Test utils.memoize decorator."""
    def test_memoize(self):
        """Test memoize method."""
        memoize = __import__('utils').memoize

        class TestClass:
            """Test Class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mocked.assert_called_once()
