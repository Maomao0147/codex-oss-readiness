# Issue Triage Guide

Issue triage is the habit of turning new reports and ideas into clear next actions. For Codex for OSS preparation, it also creates public evidence that the project is actively maintained.

## Triage Goals

- Understand what the reporter needs.
- Decide whether the issue is valid for this project.
- Add useful labels.
- Ask for missing information when needed.
- Connect accepted issues to a branch, pull request, or release.

## Recommended Labels

Use GitHub labels manually after the repository is public. See [`github-labels.md`](github-labels.md) and `.github/labels.yml` for the canonical label list.

| Label | Meaning | When to use |
| --- | --- | --- |
| `bug` | Something is broken | CLI output is wrong, tests fail, docs are misleading |
| `enhancement` | New or improved behavior | A new check, option, or workflow would help |
| `documentation` | Docs-only work | README, guides, examples, templates |
| `good first issue` | Beginner-friendly | Small scope, clear acceptance criteria |
| `needs info` | Waiting for detail | Reproduction steps, environment, or expected behavior is missing |
| `triaged` | Maintainer has reviewed it | The issue has a clear next step |
| `release` | Release preparation | Changelog, release notes, version checks |

## First Response Template

```markdown
Thanks for opening this. I will triage it against the current checklist and docs.

Current understanding:
- 

Next step:
- 
```

## Triage Checklist

- [ ] Is the issue about this repository?
- [ ] Is it a bug, enhancement, documentation task, or release task?
- [ ] Is the requested outcome clear?
- [ ] Is more information needed?
- [ ] Are acceptance criteria written?
- [ ] Is there a likely test or manual verification step?
- [ ] Is it small enough for a first pull request?

## Decisions

### Accept

Use when the issue is useful and actionable.

Actions:

- Add `triaged`.
- Add the type label.
- Add `good first issue` if the scope is beginner-friendly.
- Write acceptance criteria.

### Needs Info

Use when the issue might be valid but is incomplete.

Actions:

- Add `needs info`.
- Ask one or two specific questions.
- Leave it open until the reporter or maintainer can clarify.

### Close

Use when the issue is unrelated, duplicated, already fixed, or not planned.

Actions:

- Explain the reason briefly.
- Link the duplicate or related issue when possible.
- Keep the tone respectful.

## Weekly Triage Routine

Once the repository is public:

1. Review new issues.
2. Label each issue.
3. Convert one issue into a small branch and pull request.
4. Record useful links in `docs/application-evidence-log.md`.
5. Add release candidates to `docs/release-checklist.md`.

## Evidence to Keep

- Issue with labels and acceptance criteria.
- Pull request linked to an issue.
- Passing CI on the pull request.
- Release notes that mention the issue or PR.
