# GitHub Repository Settings Checklist

After publishing this project as a public GitHub repository, use this checklist to make the repository easier to inspect, contribute to, and evaluate for Codex for OSS readiness.

## Public Repository Basics

- [ ] Repository visibility is public.
- [ ] Default branch is `main`.
- [ ] Repository description explains the project in one sentence.
- [ ] README is visible and readable on the repository homepage.
- [ ] License is visible in the repository sidebar.

## About Section

Suggested description:

```text
Checklist CLI and learning workspace for GitHub OSS maintenance and Codex for OSS application readiness.
```

Suggested topics:

```text
github
open-source
cli
codex
maintenance
readiness
python
```

## Features

- [ ] Issues are enabled.
- [ ] Pull requests are enabled.
- [ ] Actions are enabled.
- [ ] Releases are available.
- [ ] Discussions are disabled unless you plan to maintain them.

## Branch and PR Settings

For a beginner project, keep the setup simple:

- [ ] Use pull requests for visible maintenance practice.
- [ ] Require yourself to run tests before merge.
- [ ] Check GitHub Actions before merge.
- [ ] Avoid complex branch protection until you understand the workflow.

Optional later:

- [ ] Require status checks before merging.
- [ ] Require a pull request before merging to `main`.
- [ ] Add branch protection after the first few PRs are working.

## Evidence to Record

After setup, record these in `docs/week-by-week-tracker.md`:

- Public repository URL.
- Labels setup.
- First issue.
- First pull request.
- First CI run.
- First release.

