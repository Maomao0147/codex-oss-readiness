# First Release Lab

This lab turns your first public GitHub release into useful maintenance evidence.

Prerequisites:

- The repository is public on GitHub.
- At least one pull request has been merged.
- GitHub Actions CI passed on `main`.
- `docs/application-evidence-log.md` has the first issue, PR, and CI links.
- `docs/repository-settings-checklist.md` has been reviewed.

## 1. Review the Release Checklist

Open [`release-checklist.md`](release-checklist.md) and complete the before-release items.

Run locally:

```powershell
python -m unittest discover -s tests
python -m src.codex_oss_readiness --repo .
python -m src.codex_oss_readiness --repo . --application-audit --missing-only
```

## 2. Update Changelog

Update `CHANGELOG.md` with a short `v0.1.0` section.

Include:

- what was added
- what was changed
- what was verified
- what comes next

## 3. Create a Release Tag

After committing changelog updates on `main`, create a tag:

```powershell
git tag v0.1.0
git push origin v0.1.0
```

## 4. Create the GitHub Release

In GitHub:

1. Open Releases.
2. Choose Draft a new release.
3. Select tag `v0.1.0`.
4. Paste or adapt `.github/RELEASE_TEMPLATE.md`.
5. Publish the release.

## 5. Record Evidence

Add these links to `docs/application-evidence-log.md`:

- First release: `https://github.com/OWNER/REPOSITORY/releases/tag/v0.1.0`
- First passing CI: `https://github.com/OWNER/REPOSITORY/actions/runs/123`

Then rerun:

```powershell
python -m src.codex_oss_readiness --repo . --application-audit --missing-only
```

## 6. Follow-Up

Create one follow-up issue for the next release. Good examples:

- Improve release note examples.
- Add another readiness check.
- Add a bilingual docs section.
