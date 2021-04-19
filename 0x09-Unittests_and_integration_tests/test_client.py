#!/usr/bin/env python3

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test client file """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org, foo):
        GithubOrgClient(org).org()
        foo.assert_called_once_with(f'https://api.github.com/orgs/{org}')
