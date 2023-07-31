#!/usr/bin/env python3
from utils import access_nested_map, memoize
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


my_class = GithubOrgClient('google')
# print(my_class.repos_payload)

payload = [
    load.get("name") for load in TEST_PAYLOAD[0][1]
]
print(payload)
