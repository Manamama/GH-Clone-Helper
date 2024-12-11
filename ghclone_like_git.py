#!/usr/bin/env python3
'''
ghclone_like_git: Mimics git clone behavior using GitHub API.

What the code does:
- This script mimics the behavior of `git clone` by directly downloading a tarball of the specified GitHub repository.
- It uses the GitHub API to fetch the tarball, ensuring the repository is downloaded and extracted without using the traditional `git clone` command.
- This method is particularly useful in environments where standard Git operations may face network issues or other restrictions.

Note:
- This script uses HTTP to download the repository, as specified.
- The provided URL (even if it is HTTPS) is converted to the HTTP equivalent for compatibility.

ManamaMa, Version 1.1
'''

import os
import re
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='ghclone_like_git: Mimics git clone behavior.')
    parser.add_argument('repository', type=str, help='URL of the repository to clone (e.g., https://github.com/qt/qtbase)')
    return parser.parse_args()

def print_info(repo_url, alternative_method):
    print('''\nghclone_like_git: Mimics git clone behavior using GitHub API.

What the code does:
- This script mimics the behavior of `git clone` by directly downloading a tarball of the specified GitHub repository.
- It uses the GitHub API to fetch the tarball, ensuring the repository is downloaded and extracted without using the traditional `git clone` command.
- This method is particularly useful in environments where standard Git operations may face network issues or other restrictions.

Note:
- This script uses HTTP to download the repository, as specified.
- The provided URL (even if it is HTTPS) is converted to the HTTP equivalent for compatibility.
''')

    print(f"Original URL provided: {repo_url}")
    print(f"\033[34mAlternative method:\033[0m git clone {alternative_method}")

def clone_repository(repo_url):
    print_info(repo_url, repo_url.replace('https://', 'git://'))
    
    # Convert HTTPS to HTTP
    repo_url = repo_url.replace('https://', 'http://')
    print(f"Converted URL to HTTP: {repo_url}")

    # Regex to extract owner and repository from URL
    match = re.match(r'http://github\.com/([^/]+)/([^/]+)', repo_url)
    if not match:
        print("Invalid GitHub URL. Please provide a valid repository URL.")
        return
    
    owner, repo = match.groups()
    tarball_url = f'http://api.github.com/repos/{owner}/{repo}/tarball'
    
    print(f"Cloning repository: {owner}/{repo}")
    print(f"Downloading from: {tarball_url}")
    
    # Download tarball
    print("Downloading tarball...")
    os.system(f'curl -L {tarball_url} -o {repo}.tar.gz')
    
    # Extract tarball
    print("Extracting tarball...")
    os.system(f'tar -xzf {repo}.tar.gz')
    
    print(f"Repository {owner}/{repo} has been cloned successfully.")

def main():
    args = parse_arguments()
    print(f"ghclone_like_git: Cloning repository {args.repository}")
    clone_repository(args.repository)

if __name__ == '__main__':
    main()

