# GH-Clone-Helper 🚀

version 2.2

A nifty shell function and a Python file to clone GitHub repositories using `curl` instead of the `gh` or `git clone` protocols: a Python script that downloads the tarball instead that never fails, as long as there is some Internet around 🛠️

## Why You'll Love It 👨‍🏭

Tired of `git clone` breaking your heart (and your code) with its fickle ways? 😩 GH-Clone-Helper is your new reliable BFF. It's like a warm hug for your repositories, ensuring a smooth cloning process even when your internet decides to play hard to get. 🌐💔.

More mundanely: Many end-users encounter issues with the standard `git clone` where the cloning process breaks, especially when dealing with large repositories or unstable Internet connections. Common fixes such as increasing `http.postBuffer` or using shallow clones often do not resolve these issues. The `git clone` command can fail due to various reasons, including network timeouts and data transfer interruptions, leading to incomplete clones that cannot be resumed from the point of failure. 
`GH-Clone-Helper` (now at: https://github.com/Manamama/GH-Clone-Helper/) aims to provide a more robust solution by leveraging the GitHub CLI, its `gh clone`, which uses GitHub's API for cloning operations, offering a more stable and reliable cloning process.

## Get Your Token, Get Set, Go! 🏁

To kick things off with GH-Clone-Helper, you'll need a personal access token (PAT) from your sidekick GitHub account. This little golden key 🗝️ will let GH-Clone-Helper step in on your behalf, especially handy when your main account is taking a timeout. 🕒

### Crafting Your Personal Access Token 🛠️

1. Sneak into your secondary GitHub account. 🕵️‍♂️
2. Navigate to your account settings.
3. Hit "Developer settings" like it owes you money. 💰
4. Choose "Personal access tokens" and treat yourself to a "Generate new token" moment.
5. Name your token something memorable, pick the powers you want to bestow upon it (minimum: `repo`), and let the magic happen. ✨
6. **Heads up**: Copy your token now! It's a shy one and won't show itself again. 🙈

### Securing Your Personal Access Token 🔐

1. Pop open a terminal window.
2. Summon a text editor and conjure up a `.ghtoken2` file in your home directory:
   ```sh
   nano ~/.ghtoken2
   ```
   
## Setting Up Shop 🛍️

1. Make sure the GitHub CLI is part of your toolkit and on speaking terms with your secondary token.
2. Cozy up your shell configuration file with the `gh_clone_with_token` function. It's like inviting a friend over. 🏡
3. Give your terminal a quick refresh or just reboot. It's like a spa day for your CLI. 🧖‍♂️

## How to Use It 🤔

When you're ready to bring a new repo into your life, just whisper sweet nothings to the function like so:

```sh
gh_clone_with_token "https://github.com/username/repository.git"
```

And voilà! The script will work its magic, leaving you with a perfectly cloned repo. 🎩✨

PS. Sending a high-five to Microsoft Copilot🤖🦜🦉 (still in the Creative mode) for the assist on this script! 🙌 And remember, keep your tokens close and your repositories closer. 😉🔒
(And MS Copilot wrote most of the above, too.)
```
⬛⬜⬛⬜⬛
⬜⬛⬜⬛⬜
⬛⬜⬛⬜⬛
```

