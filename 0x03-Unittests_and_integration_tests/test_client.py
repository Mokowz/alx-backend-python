#!/usr/bin/env python3
"""Test Client Module"""
import unittest
from unittest import mock
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Org Client class"""
    @parameterized.expand([
      ("google"),
      ("abc"),
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """Test org Test function"""
        ex = GithubOrgClient(org)
        ex_response = ex.org
        self.assertEqual(ex_response, mock_org.return_value)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """Test Public Repo URL"""
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as MockClass:
            MockClass.return_value = {"repos_url": 100}
            ex = GithubOrgClient('Mimi')
            ex_response = ex._public_repos_url
            self.assertEqual(ex_response,
                             MockClass.return_value.get("repos_url"))
            MockClass.assert_called_once()


if __name__ == '__main__':
    unittest.main()
