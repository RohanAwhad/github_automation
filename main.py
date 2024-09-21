import os
import requests
import argparse
import sys

parser = argparse.ArgumentParser(description='Create a new GitHub repository')
parser.add_argument('repo_name', type=str, help='Name of the repository')
parser.add_argument('description', type=str, help='Description of the repository')
parser.add_argument('--is_private', action='store_true', help='Whether the repository should be private')

args = parser.parse_args()

repo_name: str = args.repo_name
description: str = args.description
is_private: bool = args.is_private

access_token: str = os.environ.get('GITHUB_ACCESS_TOKEN')

if access_token is None:
    print("Error: GITHUB_ACCESS_TOKEN environment variable not set.")
    sys.exit(1)

headers: dict[str, str] = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {access_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

r = requests.post(
    "https://api.github.com/user/repos",
    headers=headers,
    json={
        "name": repo_name,
        "description": description,
        "homepage": "https://github.com",
        "private": is_private,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }
)

if r.status_code != 201:
    print(f"Failed to create repository: {r.text}")
    sys.exit(1)

print(f"Successfully created repository: {repo_name}")
print(f'https://github.com/rohanawhad/{repo_name}')
