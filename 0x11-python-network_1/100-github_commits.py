#!/usr/bin/python3

""" Please list 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
    You must use the GitHub API, here is the documentation
    https://developer.github.com/v3/repos/commits/
    Print all commits by: `<sha>: <author name>` (one by line)
"""

import sys
import requests


def fetch_commits(repo_name, owner_name):
    '''
        Fetches 10 recent commits of a repository
        Args:
            repo_name: the repository to fetch from
            owner_name: Repository's owner
    '''

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # 10 recent commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            # commit_message = commit['commit']['message']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Failed to fetch commits. Status code:\
              {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(" Usage: python3 script_name.py repository_name owner_name")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_commits(repository_name, owner_name)
