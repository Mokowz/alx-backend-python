#!/usr/bin/env python3
"""Test Client Module"""
import unittest
from unittest import mock
from unittest.mock import Mock, patch
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
    "Test org function"
    ex = GithubOrgClient(org)
    response = ex.org
    self.assertEqual(response, mock_org.return_value)
    mock_org.assert_called_once()


if __name__ == '__main__':
  unittest.main()
