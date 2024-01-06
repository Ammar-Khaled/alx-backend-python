#!/usr/bin/env python3
"""Test client.py functions."""
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import MagicMock, patch, PropertyMock


class TestGithubOrgClient(TestCase):
    """Test GithubOrgClient class."""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org: str, mocked_get_json: MagicMock) -> None:
        """Test GithubOrgClient.org() method."""
        GithubOrgClient = __import__('client').GithubOrgClient
        client = GithubOrgClient(test_org)
        client.org()
        targeted_endpoint = f"https://api.github.com/orgs/{test_org}"
        mocked_get_json.assert_called_once_with(targeted_endpoint)

    def test_public_repos_url(self):
        """Test _public_repos_url."""
        GithubOrgClient = __import__('client').GithubOrgClient
        client = GithubOrgClient('google')
        repos_url = "https://api.github.com/orgs/google/repos"
        org_path = 'client.GithubOrgClient.org'
        with patch(org_path, new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = {"repos_url": repos_url}
            self.assertEqual(client._public_repos_url, repos_url)

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """Test public_repos."""
        GithubOrgClient = __import__('client').GithubOrgClient
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
