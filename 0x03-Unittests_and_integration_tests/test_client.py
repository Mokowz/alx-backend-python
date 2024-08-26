#!/usr/bin/env python3
"""Test Client Module"""
import unittest
from unittest import mock
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test Github Org Client class
    """
    @parameterized.expand([
      ("google"),
      ("abc"),
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test TestGithubOrgClient's org method
        """
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

    @patch('client.get_json', return_value=[{'name': 'Hello'},
                                            {'name': 'Haha'}])
    def test_public_repos(self, mock_repo):
        """Test GithubOrgClient's public_repos"""
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as moc:

            test_ex = GithubOrgClient('mimi')
            test_resp = test_ex.public_repos()
            for idx in range(2):
                self.assertIn(mock_repo.return_value[idx]['name'], test_resp)
            mock_repo.assert_called_once()
            moc.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient's has_license method"""
        test_ex = GithubOrgClient('mimi')
        licensee = test_ex.has_license(repo, license_key)
        self.assertEqual(licensee, expected)


def requests_get(*args, **kwargs):
    """Mock requests.get function"""
    class MockResponse:
        """Mock response Class"""

        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == "https://api.github.com/orgs/google":
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class"""
    @classmethod
    def setUpClass(cls):
        """
        Set up function for TestIntegrationGithubOrgClient
        """
        cls.get_patcher = patch('utils.requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down resources set up for class tests.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos func"""
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos func with license"""
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
