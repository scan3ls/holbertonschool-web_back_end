#!/usr/bin/env python3
""" test module """
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ test for AccesNestedMap """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, mapping, sequence, expected):
        """ test access nested map """
        self.assertEqual(access_nested_map(mapping, sequence), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, mapping, sequence, expected):
        """ test key error raise """
        with self.assertRaises(Exception) as context:
            access_nested_map(mapping, sequence)
        self.assertEqual(type(context.exception), expected)


class TestGetJson(unittest.TestCase):
    """ test for GetJson """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ test get_json """
        request = Mock()
        request.json.return_value = test_payload
        with patch('requests.get', return_value=request):
            response = get_json(test_url)
            request.json.assert_called_once()
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ test memoizaiton """

    def test_memoize(self):
        """ test memoize """

        class TestClass:
            """ class import """
            def a_method(self):
                """ function 42 """
                return 42

            @memoize
            def a_property(self):
                """ memoize function """
                return self.a_method()

        test = TestClass()
        attr = '_a_property'
        self.assertFalse(hasattr(test, attr))

        value = test.a_property
        self.assertTrue(hasattr(test, attr))
        self.assertEqual(getattr(test, attr), value)
