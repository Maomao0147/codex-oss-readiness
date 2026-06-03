# CI Debugging Lab

CI debugging is the practice of reading a failed GitHub Actions run, finding the failed command, fixing the branch, and rerunning the check. It is a useful GitHub skill and a strong maintenance signal.

## When to Use This Lab

Use this when a pull request or release commit has a failing GitHub Actions run.

Prerequisites:

- The repository is public on GitHub.
- `.github/workflows/ci.yml` exists.
- A pull request or push has triggered GitHub Actions.

## 1. Open the Failed Run

In GitHub:

1. Open the pull request or repository Actions tab.
2. Select the failed workflow run.
3. Open the failing job.
4. Expand the failing step.

Record:

- Workflow run URL:
- Job name:
- Failing step:
- Failed command:

Expected evidence link format:

```text
https://github.com/OWNER/REPOSITORY/actions/runs/123
```

## 2. Classify the Failure

Use one of these buckets:

- Test failure: a test assertion failed.
- Import or packaging failure: Python cannot import the project.
- Command failure: a command in `ci.yml` is wrong.
- Environment failure: Python version, path, or dependency issue.
- Readiness failure: `python -m src.codex_oss_readiness --repo .` reports a missing item.

## 3. Reproduce Locally

Run the same command locally:

```powershell
python -m unittest discover -s tests
python -m src.codex_oss_readiness --repo .
```

If local Python is unavailable, use the working Python runtime in your environment and record that in the PR testing notes.

## 4. Fix on the Same Branch

Make the smallest change that fixes the failing command.

Then run:

```powershell
git status
git add .
git commit -m "Fix CI failure"
git push
```

## 5. Verify the Rerun

After pushing, GitHub Actions should rerun automatically.

Record:

- Previous failed run:
- Passing rerun:
- What changed:

## 6. Add Evidence

If the run is part of your application evidence, add the passing CI run to `docs/application-evidence-log.md`.

Good CI evidence includes:

- A failing run you investigated.
- A commit or PR that fixes the issue.
- A later passing run.
- A short note explaining what you learned.

