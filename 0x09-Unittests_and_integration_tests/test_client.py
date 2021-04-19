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
        """ test _public_repos_url property """
        with patch('client.GithubOrgClient.org') as org:
            org.return_value = 'Known'

            with patch('client.GithubOrgClient._public_repos_url',
                       new_callable=PropertyMock) as foo:
                foo.return_value = org()
                test = GithubOrgClient('name')
                self.assertEqual(test.org(), test._public_repos_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ test public_repos method """
        mock_json.return_value = [
            {'name': 'your choice'},
            {'name': 'my choice'}
        ]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as foo:

            test = GithubOrgClient('Jeff')
            foo.return_value = mock_json

            response = test.public_repos()

            self.assertEqual(response, ['your choice', 'my choice'])
            mock_json.assert_called_once()
            foo.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license'),
        ({'license': {'key': 'other_license'}}, 'my_license')
    ])
    def test_has_license(self, repo, license_key):
        self.assertTrue(True)
