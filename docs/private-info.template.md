# Private Application Info Template

Copy this file to `private/application-info.private.md` before filling in sensitive values.

Do not commit the copied private file. The `private/` directory and `*.private.md` files are ignored by Git.

## Codex for OSS Private Fields

- Last name:
- First name:
- Full name, if useful locally:
- ChatGPT account email:
- OpenAI Organization ID:
- Country or region:
- Application submitted date:
- Application confirmation or notes:

## GitHub Identity

- GitHub username:
- Git commit email:
- GitHub no-reply email:

## Public Repository

- Repository URL:
- First issue:
- First merged PR:
- First passing CI:
- First release:

## Safety Check

Before committing, run:

```powershell
git status --short
```

If `private/application-info.private.md` appears in the output, stop and fix `.gitignore` before committing.
