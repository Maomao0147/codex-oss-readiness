# Contributing

Thanks for helping improve Codex OSS Readiness.

## Ways to contribute

- Open an issue for unclear instructions, missing checklist items, or bugs.
- Open a pull request for small improvements to docs or checks.
- Suggest examples that help first-time GitHub users practice real workflows.

## Local setup

1. Fork or clone the repository.
2. Create a new branch:

   ```powershell
   git checkout -b docs/improve-checklist
   ```

3. Run the tests:

   ```powershell
   python -m unittest discover -s tests
   ```

4. Make a focused change.
5. Commit with a short message:

   ```powershell
   git add .
   git commit -m "Improve checklist wording"
   ```

6. Open a pull request and describe what changed.

## Pull request expectations

- Keep pull requests focused on one topic.
- Include tests when changing checker behavior.
- Update docs when changing user-facing behavior.
- Use clear commit messages.

## Maintainer workflow

- Triage new issues at least once per week.
- Label beginner-friendly issues as `good first issue`.
- Prefer pull requests over direct commits for visible maintenance history.
- Keep releases small and understandable.

