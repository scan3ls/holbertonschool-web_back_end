#!/usr/bin/env python3

from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock
import client
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
        foo.assert_called_once()

    def test_public_repos_url(self):
        with patch('client.GithubOrgClient.org') as org:
            org.return_value = 'Known'

            with patch('client.GithubOrgClient._public_repos_url',
                       new_callable=PropertyMock) as foo:
                foo.return_value = org()
                test = GithubOrgClient('name')
                self.assertEqual(test.org(), test._public_repos_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        mock_json.return_value = [
            {'name': 'your choice'},
            {'name': 'my choice'}
        ]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as foo:

            test = GithubOrgClient('Jeff')
            foo.return_value = mock_json

            test.public_repos()
            foo.assert_called_once()
            mock_json.assert_called_once()
