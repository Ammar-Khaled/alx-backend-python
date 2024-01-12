#!/usr/bin/env python3
"""Test client.py functions."""
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import MagicMock, patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class."""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org: str, mocked_get_json: MagicMock) -> None:
        """Test GithubOrgClient.org() method."""
        client = GithubOrgClient(test_org)
        client.org()
        targeted_endpoint = f"https://api.github.com/orgs/{test_org}"
        mocked_get_json.assert_called_once_with(targeted_endpoint)

    def test_public_repos_url(self):
        """Test _public_repos_url."""
        client = GithubOrgClient('google')
        repos_url = "https://api.github.com/orgs/google/repos"
        org_path = 'client.GithubOrgClient.org'
        with patch(org_path, new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = {"repos_url": repos_url}
            self.assertEqual(client._public_repos_url, repos_url)

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """Test public_repos."""
        client = GithubOrgClient('google')
        expected_repos = [{"id": 1936771, "name": "truth"},
                          {"id": 3248531, "name": "autoparse"}]
        mocked_get_json.return_value = expected_repos
        property_path = 'client.GithubOrgClient._public_repos_url'
        with patch(property_path, new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/google/repos"
            self.assertEqual(client.public_repos(), ['truth', 'autoparse'])
            mock_url.assert_called_once()
            mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, result):
        """Test has_license method."""
        client = GithubOrgClient('google')
        self.assertEqual(client.has_license(repo, license_key), result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration Test for client.GithubOrgClient class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Set up the class before tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return MagicMock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.mocked_get = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration Test for GithubOrgClient.public_repos."""
        client = GithubOrgClient('google')
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.mocked_get.assert_called()

    def test_public_repos_with_license(self):
        """Test calling GithubOrgClient.public_repos(license)."""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.assertEqual(client.public_repos('apache-2.0'), self.apache2_repos)
        self.mocked_get.assert_called()

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop get_pathcer."""
        cls.get_patcher.stop()
