# GitHub Beginner Cheatsheet

## Local Git commands

Check what changed:

```powershell
git status
```

Stage changes:

```powershell
git add .
```

Commit changes:

```powershell
git commit -m "Short message"
```

Create a branch:

```powershell
git checkout -b docs/update-readme
```

See history:

```powershell
git log --oneline
```

Check remote:

```powershell
git remote -v
```

Push main branch:

```powershell
git push -u origin main
```

## GitHub workflow

1. Create an issue for the work.
2. Create a branch for that issue.
3. Make a small change.
4. Commit and push the branch.
5. Open a pull request.
6. Review the diff and tests.
7. Merge the pull request.
8. Close or link the issue.

## Publishing

See [`github-auth-and-push-guide.md`](github-auth-and-push-guide.md) before pushing the first public repository.

## Good commit messages

See [`commit-and-branch-guide.md`](commit-and-branch-guide.md) for the full guide.

- `Add release checklist`
- `Fix missing-only CLI output`
- `Improve application workbook`

Avoid vague messages like:

- `update`
- `fix`
- `changes`
