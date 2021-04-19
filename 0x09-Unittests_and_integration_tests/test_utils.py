#!/usr/bin/env python3
""" test module """
from parameterized import parameterized
from nose.tools import assert_equal
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ test suite for AccesNestedMap """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, mapping, sequence, expected):
        """ test access nested map """
        assert_equal(access_nested_map(mapping, sequence), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, mapping, sequence, expected):
        """ test key error raise """
        with self.assertRaises(Exception) as context:
            access_nested_map(mapping, sequence)
        assert_equal(type(context.exception), expected)


class TestGetJson(unittest.TestCase):
    """ test suite for GetJson """

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
            assert_equal(response, test_payload)
