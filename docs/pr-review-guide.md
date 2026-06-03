# Pull Request Review Guide

Pull request review is one of the clearest ways to show active open-source maintenance. Even when you are reviewing your own beginner PRs, practice the same habits you would use for outside contributors.

## Review Goals

- Confirm the PR matches the linked issue or stated goal.
- Check whether the change is small enough to review.
- Verify tests or manual checks.
- Leave clear comments only where they help.
- Merge only after CI passes and the summary is understandable.

## Review Checklist

- [ ] The PR title describes the change.
- [ ] The PR body explains why the change was made.
- [ ] The PR links to an issue when possible.
- [ ] The changed files match the scope.
- [ ] Tests are included or not needed.
- [ ] GitHub Actions CI passes.
- [ ] README or docs are updated when behavior changes.
- [ ] No private information is included.

## Comment Templates

Use short comments. A good review comment names the issue and the next action.

```markdown
Could you add the command you used to verify this? That will make the PR easier to review and preserve as maintenance evidence.
```

```markdown
This looks good to merge after CI passes. The PR is focused, and the README update matches the issue acceptance criteria.
```

```markdown
This change is useful, but it seems broader than the linked issue. Please split the unrelated part into a follow-up issue or PR.
```

## Review Decisions

### Approve

Use when the PR is focused, tested, and understandable.

### Request Changes

Use when the PR has a bug, missing verification, unclear scope, or private information.

### Comment

Use when you need clarification but are not blocking the PR yet.

## Evidence to Record

After a useful review, add the PR link to `docs/application-evidence-log.md`.

Good evidence includes:

- A PR connected to an issue.
- A visible review comment.
- Passing CI.
- A merge commit or squash commit.
- Release notes that mention the change.

## Using Codex or API Credits Later

If selected for Codex for OSS support, API credits could help draft review notes, summarize changed files, suggest missing tests, or draft release notes. The maintainer should still decide what to post, approve, merge, or reject.

