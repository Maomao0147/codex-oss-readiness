# Codex OSS Readiness

Codex OSS Readiness is a small command-line checklist for people preparing an
open-source repository for the OpenAI Codex for OSS application process.

It checks whether a local project has the basic public-maintenance materials
that reviewers and contributors expect: README, license, contribution guide,
issue templates, pull request template, release notes, and an application draft.
It also checks the first GitHub workflow milestones: local Git setup, first
commit, and a GitHub remote.

## Why this project exists

Applying for an open-source support program is easier when the project already
looks maintainable. This tool turns the preparation work into a visible,
repeatable checklist that can be improved over time through issues and pull
requests.

## Quick start

Run the checker from this repository:

```powershell
python -m src.codex_oss_readiness --repo .
```

Check another project:

```powershell
python -m src.codex_oss_readiness --repo C:\path\to\your\project
```

Show only missing items:

```powershell
python -m src.codex_oss_readiness --repo . --missing-only
```

The output also includes prioritized next actions. For a brand-new learner
repository, the first suggestions should guide you toward the first commit and
GitHub remote setup.
Use `--missing-only` when you want the shortest view of what still needs work.
It hides completed checks and keeps the focus on the next setup gap.

Audit your GitHub learning evidence:

```powershell
python -m src.codex_oss_readiness --repo . --skills-audit --missing-only
```

The skills audit reads `docs/github-skills-matrix.md`. It checks whether each
GitHub skill has both an evidence link or note and a short reflection, so you
can tell the difference between reading a guide and actually practicing the
workflow.

Audit the application workbook and evidence links:

```powershell
python -m src.codex_oss_readiness --repo . --application-audit --missing-only
```

The application audit is allowed to show TODO items while you are still learning.
Use it before submission to confirm that public evidence exists and private
account fields are recorded somewhere safe. It also checks whether the project
eligibility explanation and API credits plan are present and within the
500-character form limit, whether the evidence log records repository identity
and permission evidence, and whether evidence links point to the expected GitHub
issue, pull request, commit, Actions run, and release pages.

## What it checks

- `README.md`
- `LICENSE`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `.gitignore`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/labels.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/ci.yml`
- `.github/RELEASE_TEMPLATE.md`
- `docs/github-4-week-plan.md`
- `docs/application-workbook.md`
- `docs/application-form-walkthrough.md`
- `docs/codex-api-credits-plan.md`
- `docs/release-checklist.md`
- `docs/first-commit-and-publish.md`
- `docs/github-auth-and-push-guide.md`
- `docs/commit-and-branch-guide.md`
- `docs/github-cheatsheet.md`
- `docs/maintenance-backlog.md`
- `docs/issue-triage-guide.md`
- `docs/github-labels.md`
- `docs/pr-review-guide.md`
- `docs/first-release-lab.md`
- `docs/ci-debugging-lab.md`
- `docs/repository-settings-checklist.md`
- `docs/week-by-week-tracker.md`
- `docs/github-skills-matrix.md`
- `docs/first-pr-lab.md`
- `docs/github-profile-checklist.md`
- `docs/application-evidence-log.md`
- `docs/final-application-audit.md`
- `docs/openai-org-id-guide.md`
- `docs/privacy-and-public-repo.md`
- `docs/private-info.template.md`
- local Git repository status
- Git user.name status
- Git user.email status
- main branch status
- first commit status
- GitHub remote status
- privacy ignore rules for private application info

## Four-week learning path

This repository includes a Chinese learning plan in
[`docs/github-4-week-plan.md`](docs/github-4-week-plan.md).

The intended path is:

1. Learn GitHub basics with this repository.
2. Use this repository as the first public OSS candidate project.
3. Practice issue triage, pull requests, releases, and changelog writing.
4. Prepare the final Codex for OSS application draft in
   [`docs/application-workbook.md`](docs/application-workbook.md).
   Keep evidence in [`docs/application-evidence-log.md`](docs/application-evidence-log.md)
   and run the final audit in [`docs/final-application-audit.md`](docs/final-application-audit.md).

If this is your first GitHub project, start with
[`docs/first-commit-and-publish.md`](docs/first-commit-and-publish.md).
Use [`docs/github-auth-and-push-guide.md`](docs/github-auth-and-push-guide.md)
when adding `origin` and pushing to GitHub.
Use [`docs/commit-and-branch-guide.md`](docs/commit-and-branch-guide.md) before
creating the first commit or first pull request branch.
Use [`docs/week-by-week-tracker.md`](docs/week-by-week-tracker.md) to track
your progress during the four weeks.
Use [`docs/github-skills-matrix.md`](docs/github-skills-matrix.md) to confirm
that you can complete the GitHub skills expected before applying.
After publishing the repository, use
[`docs/first-pr-lab.md`](docs/first-pr-lab.md) for your first issue, branch,
pull request, CI check, and merge.
Use [`docs/pr-review-guide.md`](docs/pr-review-guide.md) for review practice
and [`docs/first-release-lab.md`](docs/first-release-lab.md) for the first
public release.
Use [`docs/ci-debugging-lab.md`](docs/ci-debugging-lab.md) when GitHub Actions
fails, and [`docs/repository-settings-checklist.md`](docs/repository-settings-checklist.md)
after creating the public repository.

## Development

Run tests:

```powershell
python -m unittest discover -s tests
```

Run the checker:

```powershell
python -m src.codex_oss_readiness --repo .
```

After this repository is published on GitHub, pull requests run the same tests
through GitHub Actions. Use that CI result as part of your maintenance evidence.

## Contributing

Issues and pull requests are welcome. Good first contributions include:

- improving the checklist wording
- adding examples for beginner GitHub workflows
- translating docs
- adding checks for release notes or project health signals

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## License

MIT
