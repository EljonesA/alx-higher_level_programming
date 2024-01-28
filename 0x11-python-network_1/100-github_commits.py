#!/usr/bin/python3

import sys
import requests

def fetch_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10] # 10 recent commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Failed to fetch commits. Status code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(" Usage: python3 script_name.py repository_name owner_name")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_commits(repository_name, owner_name)
