# GH-Clone-Helper

A convenient shell function to clone GitHub repositories via `gh` instead of `git clone`, using the GitHub CLI with authentication support for rate-limited accounts.

## Motivation

Many end-users encounter issues with the standard `git clone` where the cloning process breaks, especially when dealing with large repositories or unstable Internet connections. Common fixes such as increasing `http.postBuffer` or using shallow clones often do not resolve these issues[^1^][1]. The `git clone` command can fail due to various reasons, including network timeouts and data transfer interruptions, leading to incomplete clones that cannot be resumed from the point of failure[^2^][2].

`GH-Clone-Helper` aims to provide a more robust solution by leveraging the GitHub CLI, its `gh clone`, which uses GitHub's API for cloning operations, offering a more stable and reliable cloning process even on connections that are less than ideal.

## Generating and Storing Your Secondary GitHub Token

To use `GH-Clone-Helper` with a secondary GitHub account, you'll need to generate a personal access token (PAT) for that account. This token will allow `GH-Clone-Helper` to authenticate with GitHub on your behalf, which is particularly useful if you've hit rate limits with your primary account.

### Generating a Personal Access Token

1. Log in to your secondary GitHub account.
2. Go to your account settings.
3. Click on "Developer settings."
4. Select "Personal access tokens."
5. Click on "Generate new token."
6. Give your token a descriptive name, select the scopes or permissions you want to grant this token (at a minimum, you'll need `repo` for full control of private repositories), and click "Generate token."
7. **Important**: Make sure to copy your new personal access token now. You won’t be able to see it again!

### Storing the Personal Access Token

1. Open a terminal on your machine.
2. Use a text editor to create a file named `.ghtoken2` in your home directory:
   ```sh
   nano ~/.ghtoken2
   
## Installation

1. Ensure you have the GitHub CLI installed and that it works with the secondary token.
2. Add the `gh_clone_with_token` function, from its .sh file here, to your shell configuration file (e.g., `.bashrc`, `.zshrc`)
3. Source your shell configuration file or restart your terminal session.
   4. Or just paste it to the current terminal, verbatim, within this session. (Not persistent then.)

## Usage

To clone a repository, simply call the function with the repository URL:

```sh
gh_clone_with_token "https://github.com/username/repository.git"
```
The script shall parse the URL to match the `gh clone` syntax. 

PS. Thanks to Microsoft Copilot for coming up with the idea and the script ! 
