# Codex API Credits Usage Plan

This document expands the short 500-character application answer in `docs/application-workbook.md`. It should stay truthful, public-safe, and tied to real maintenance work.

## Goals

- Reduce maintainer time spent on repetitive triage and review writing.
- Improve documentation quality for beginner contributors.
- Make releases easier to summarize and verify.
- Keep all project decisions under human maintainer review.

## Planned Uses

| Maintenance task | How Codex/API could help | Human review boundary | Evidence to record |
| --- | --- | --- | --- |
| Issue triage | Draft issue summaries, possible labels, and missing-information questions | Maintainer decides labels and final comment | Issue link with labels and triage note |
| Pull request review | Draft review notes, spot missing tests, summarize changed files | Maintainer edits and posts comments; no auto-merge | PR link with review or merge note |
| CI debugging | Summarize failing logs and suggest likely fix areas | Maintainer verifies locally and commits fixes | Actions run and fixing PR |
| Release workflow | Draft release notes from merged PRs and changelog entries | Maintainer edits release notes before publishing | Release link |
| Documentation | Suggest clearer bilingual wording and examples | Maintainer checks accuracy and tone | Docs PR link |

## Non-Goals

- No unattended merging.
- No automatic project decisions.
- No posting AI-generated comments without review.
- No use of private account data or secrets in prompts.
- No claims about users, downloads, or ecosystem impact without evidence.

## Prompt Safety Checklist

Before using API credits on repository maintenance:

- [ ] Remove private values such as ChatGPT email, OpenAI Organization ID, tokens, and `.env` values.
- [ ] Use public issue, PR, or CI text when possible.
- [ ] Ask for suggestions, not final authority.
- [ ] Review every output before posting or committing.
- [ ] Record the public artifact that benefited from the assistance.

## Example Maintenance Prompts

Issue triage:

```text
Summarize this public GitHub issue, suggest one or two labels from the project label list, and list any missing information the maintainer should ask for. Do not invent project usage or user impact.
```

PR review:

```text
Review this public PR diff for documentation clarity, missing tests, and scope creep. Return concise suggestions only; the maintainer will decide what to post.
```

Release workflow:

```text
Draft release notes from these merged PR summaries. Keep the notes factual, avoid marketing language, and separate Added, Changed, Fixed, and Next sections.
```

CI debugging:

```text
Summarize this public GitHub Actions failure log, identify the failing command, and suggest likely next checks. Do not assume dependencies or secrets that are not shown.
```

## Success Criteria

- Issues are triaged faster and more consistently.
- PR review notes become clearer without losing maintainer judgment.
- Release notes are published with less manual summarization effort.
- Application evidence links show human-reviewed maintenance work.

