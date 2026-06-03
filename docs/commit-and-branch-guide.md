# Commit and Branch Guide

Clear commits and branch names make pull requests easier to review and make the repository history more useful as open-source maintenance evidence.

## Branch Names

Use short names with a type prefix:

| Prefix | Use for | Example |
| --- | --- | --- |
| `docs/` | Documentation-only work | `docs/explain-missing-only` |
| `fix/` | Bug fixes | `fix/missing-only-output` |
| `feature/` | New behavior | `feature/check-release-template` |
| `chore/` | Maintenance | `chore/update-labels` |
| `release/` | Release preparation | `release/v0.1.0` |

Good branch names:

- `docs/improve-readme-quick-start`
- `feature/add-github-remote-check`
- `fix/application-audit-link-format`
- `release/v0.1.0`

Avoid:

- `test`
- `update`
- `my-branch`
- `final`

## Commit Messages

Use a short imperative sentence:

```text
Add first release lab
Fix application audit link validation
Improve README quick start
Document GitHub labels
```

Good commit messages answer:

- What changed?
- Why would a reviewer care?
- Is the scope clear?

Avoid:

- `update`
- `fix`
- `stuff`
- `changes`
- `final final`

## First Commit

For this repository, the first commit can be:

```powershell
git add .
git commit -m "Create Codex OSS readiness starter project"
```

Before committing:

```powershell
git status --short
python -m unittest discover -s tests
python -m src.codex_oss_readiness --repo . --missing-only
```

## Pull Request Commits

For beginner practice, keep each pull request focused:

- One issue.
- One branch.
- One small set of related commits.
- One clear PR summary.

If a PR becomes too large, split the extra work into another issue.

## Evidence Value

Clear branch names and commit messages help prove that maintenance work was intentional, reviewable, and connected to issues, PRs, CI, and releases.

