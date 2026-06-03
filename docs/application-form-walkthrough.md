# Codex for OSS Application Form Walkthrough

Use this walkthrough to map the local preparation files to the official Codex for OSS application form.

Official pages:

- Application form: <https://openai.com/form/codex-for-oss/>
- Program terms: <https://developers.openai.com/codex/codex-for-oss-terms>

Check the official form again on the day you submit. Fields can change.

## Field Mapping

| Form field | Local preparation source | Notes |
| --- | --- | --- |
| Last name | `docs/application-workbook.md` or private notes | Use the name you will submit in the form. |
| First name | `docs/application-workbook.md` or private notes | Keep public privacy preferences in mind. |
| Email associated with ChatGPT account | private notes | Do not commit private email if you do not want it public. |
| GitHub username | `docs/application-workbook.md` | Must match the public maintainer account. |
| Public repository | `docs/application-workbook.md` and `docs/application-evidence-log.md` | Must be a public GitHub repository. |
| Maintainer role | `docs/application-workbook.md` | Use `main maintainer` or `core maintainer` truthfully. |
| Project eligibility explanation | 500-character draft in `docs/application-workbook.md` | Mention project value and real maintenance status. |
| Areas of interest | `docs/application-workbook.md` | Use `Codex Security`, `API credits`, or both. |
| OpenAI Organization ID | private notes or `recorded privately` marker | Do not commit sensitive account details to a public repo. |
| API credits usage plan | 500-character draft and `docs/codex-api-credits-plan.md` | Explain concrete maintenance workflows and human review. |
| Additional information | optional private or public-safe note | Keep to 500 characters if filled. |

## Submission Safety

- Do not invent usage, contributors, downloads, stars, or ecosystem impact.
- Do not claim maintainer status for a repository you do not control.
- Do not include API keys, tokens, passwords, SSH private keys, or private account details.
- Keep AI-assisted maintenance under human review.

## Before Submitting

Run:

```powershell
python -m src.codex_oss_readiness --repo . --application-audit --missing-only
```

Then verify public links manually in a browser:

- Repository URL.
- First issue.
- First merged PR.
- First PR review note.
- First passing CI run.
- First release.

