#!/usr/bin/env python3
"""Test client.py functions."""
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import MagicMock, patch


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
