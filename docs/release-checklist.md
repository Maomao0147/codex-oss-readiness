# Release Checklist

Use this checklist before creating a GitHub release.

For a guided first release, use [`first-release-lab.md`](first-release-lab.md).

## Before release

- [ ] Tests pass with `python -m unittest discover -s tests`.
- [ ] README examples still work.
- [ ] `python -m src.codex_oss_readiness --repo .` reports expected results.
- [ ] GitHub Actions CI passes on the release commit.
- [ ] Open issues and pull requests are reviewed.
- [ ] Version number is updated if needed.

## Release notes template

```markdown
# v0.1.0

## Added

- Initial readiness checklist CLI.
- GitHub four-week learning plan.
- Codex for OSS application workbook.

## Changed

- None.

## Fixed

- None.

## Next

- Add more checks for repository health.
- Improve examples for beginner GitHub workflows.
```

## After release

- [ ] Create the GitHub release tag.
- [ ] Confirm the release page is public.
- [ ] Paste or adapt `.github/RELEASE_TEMPLATE.md` into the GitHub release notes.
- [ ] Record the release link in `docs/application-evidence-log.md`.
- [ ] Link the release in the README or project notes if useful.
- [ ] Create follow-up issues for the next version.
