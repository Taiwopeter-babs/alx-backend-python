#!/usr/bin/env python3
"""Test client module"""
import requests
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from typing import Dict
import unittest
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test GitHubOrgClient class"""

    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(
        self,
        org_url: str,
        response: Dict,
        mock_get_json: Mock
    ) -> None:
        """Test org method"""
        mock_get_json.return_value = Mock(return_value=response)

        github_client = GithubOrgClient(org_url)

        self.assertEqual(github_client.org(), response)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_url))

    def test_public_repos_url(self) -> None:
        """Test _public_repos_url method"""

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock
                   ) as mock_obj:

            response = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }

            mock_obj.return_value = response

            github_client = GithubOrgClient('google')._public_repos_url

            self.assertEqual(github_client,
                             "https://api.github.com/orgs/google/repos"
                             )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """Test public_repos method"""

        json_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {

                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    }
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    }
                }
            ]
        }

        mock_get_json.return_value = Mock(return_value=json_payload['repos'])

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            response_url = json_payload["repos_url"]

            mock_repos_url.return_value = Mock(return_value=response_url)

            github_client = GithubOrgClient('google').public_repos()

            self.assertEqual(github_client, ["episodes.dart", "cpp-netlib"])

            mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self,
                         repo: Dict,
                         license: str,
                         expected: bool
                         ) -> None:
        """Test has_license method"""

        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


# Integration test payload
test_payload = [load for load in TEST_PAYLOAD[0][1]]


@parameterized_class(test_payload)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration Test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        cls.mock_req_get = patch('requests.get')
        cls.get_patcher = cls.mock_req_get.start()
        cls.get_patcher.side_effect = test_payload

        print('patcher started')

    @classmethod
    def tearDownClass(cls):
        cls.mock_req_get.stop()
        print('patcher stopped')

    def test_patch(self):
        self.assertIs(requests.get, self.get_patcher)
