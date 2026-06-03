# GitHub Authentication and Push Guide

This guide helps you publish the local repository to GitHub after the first commit.

Official references:

- GitHub authentication overview: <https://docs.github.com/en/authentication>
- Personal access tokens: <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>
- SSH keys: <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>
- Pushing commits: <https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository>

## Recommended Path for This Project

Use the GitHub web UI to create the public repository, then push from local Git.

This project does not require GitHub CLI. On this machine, `gh` may not be installed, so the default route is:

1. Configure local Git identity.
2. Make the first commit.
3. Create a public GitHub repository in the browser.
4. Add the GitHub repository as `origin`.
5. Push `main`.

## Option A: HTTPS Remote

HTTPS remote format:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/codex-oss-readiness.git
git push -u origin main
```

If Git asks you to authenticate, use the method GitHub supports for command-line Git on your system. This may involve Git Credential Manager, browser login, GitHub CLI, or a personal access token.

Do not use your GitHub account password for command-line Git authentication.

Do not save a token in this repository, README, issue, commit, `.env`, or `private-info.template.md`.

## Option B: SSH Remote

SSH remote format:

```powershell
git remote add origin git@github.com:YOUR_USERNAME/codex-oss-readiness.git
git push -u origin main
```

Use SSH only after you have generated an SSH key and added the public key to your GitHub account.

## Check the Remote

After adding `origin`:

```powershell
git remote -v
```

Expected HTTPS output looks like:

```text
origin  https://github.com/YOUR_USERNAME/codex-oss-readiness.git (fetch)
origin  https://github.com/YOUR_USERNAME/codex-oss-readiness.git (push)
```

Expected SSH output looks like:

```text
origin  git@github.com:YOUR_USERNAME/codex-oss-readiness.git (fetch)
origin  git@github.com:YOUR_USERNAME/codex-oss-readiness.git (push)
```

## If Push Fails

Common causes:

- The GitHub repository was not created yet.
- The remote URL has the wrong username or repository name.
- Authentication was not completed.
- The local branch is not named `main`.
- The remote repository already has files created on GitHub.

Helpful checks:

```powershell
git branch --show-current
git remote -v
git status
```

If the remote repository already has files, stop and ask before merging histories. For this starter project, the cleanest path is to create an empty GitHub repository with no auto-generated README, license, or `.gitignore`.

## After Push

Run:

```powershell
python -m src.codex_oss_readiness --repo . --missing-only
```

Then open the GitHub repository and complete:

- [`repository-settings-checklist.md`](repository-settings-checklist.md)
- [`github-labels.md`](github-labels.md)
- [`first-pr-lab.md`](first-pr-lab.md)

