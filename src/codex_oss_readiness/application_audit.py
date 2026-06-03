from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ApplicationAuditItem:
    label: str
    path: str
    passed: bool
    guidance: str


WORKBOOK_FIELDS: tuple[tuple[str, str], ...] = (
    ("Last name", "Record the last name you will use in the form."),
    ("First name", "Record the first name you will use in the form."),
    ("Email associated with ChatGPT account", "Use the email tied to your active ChatGPT account."),
    ("GitHub username", "Use the public GitHub username that owns or maintains the repository."),
    ("Public repository URL", "Use a public GitHub repository URL."),
    ("OpenAI organization ID", "Record privately if the repository will be public."),
    ("Maintainer role", "State main maintainer or core maintainer truthfully."),
    ("ChatGPT account status", "Confirm the account is active before applying."),
    ("Country or region", "Use the country or region requested by the form."),
    ("Areas of interest", "Record Codex Security, API credits, or both according to the form."),
)

MAINTAINER_ROLES = {"main maintainer", "core maintainer"}

PERMISSION_EVIDENCE_VALUES = {"owner", "admin", "write access", "maintain access"}

EVIDENCE_IDENTITY_FIELDS: tuple[tuple[str, str], ...] = (
    ("GitHub username", "Record the public GitHub username that owns or maintains the repository."),
    ("Public repository URL", "Record the public GitHub repository URL you plan to submit."),
    ("Maintainer role", "State main maintainer or core maintainer truthfully."),
    ("Permission evidence", "Record your repository permission level, such as owner, admin, or write access."),
    ("First public commit", "Add a GitHub commit URL after the repository is public."),
)

EVIDENCE_ROWS: tuple[tuple[str, str, str, str], ...] = (
    (
        "First issue",
        "Add a link to the first real GitHub issue.",
        r"^https://github\.com/[^/\s]+/[^/\s]+/issues/\d+/?$",
        "https://github.com/OWNER/REPOSITORY/issues/1",
    ),
    (
        "First merged PR",
        "Add a link to a merged pull request.",
        r"^https://github\.com/[^/\s]+/[^/\s]+/pull/\d+/?$",
        "https://github.com/OWNER/REPOSITORY/pull/1",
    ),
    (
        "First PR review note",
        "Add a link to a pull request where you left a review or merge note.",
        r"^https://github\.com/[^/\s]+/[^/\s]+/pull/\d+/?$",
        "https://github.com/OWNER/REPOSITORY/pull/1",
    ),
    (
        "First passing CI",
        "Add a link to a passing GitHub Actions run.",
        r"^https://github\.com/[^/\s]+/[^/\s]+/actions/runs/\d+/?$",
        "https://github.com/OWNER/REPOSITORY/actions/runs/123",
    ),
    (
        "v0.1.0",
        "Add a link to the first public release.",
        r"^https://github\.com/[^/\s]+/[^/\s]+/releases/tag/[^/\s]+/?$",
        "https://github.com/OWNER/REPOSITORY/releases/tag/v0.1.0",
    ),
)

MAX_FORM_CHARACTERS = 500


def audit_application_docs(repo: Path) -> list[ApplicationAuditItem]:
    repo = repo.expanduser().resolve()
    items: list[ApplicationAuditItem] = []

    workbook_path = repo / "docs" / "application-workbook.md"
    workbook_text = _read_text(workbook_path)
    if workbook_text is None:
        items.append(_missing_file("docs/application-workbook.md"))
    else:
        for field, guidance in WORKBOOK_FIELDS:
            value = _field_value(workbook_text, field)
            items.append(
                ApplicationAuditItem(
                    label=f"Application field: {field}",
                    path="docs/application-workbook.md",
                    passed=_has_value(value),
                    guidance=guidance,
                )
            )
        items.extend(_field_format_items(workbook_text))
        items.extend(_draft_items(workbook_text))

    evidence_path = repo / "docs" / "application-evidence-log.md"
    evidence_text = _read_text(evidence_path)
    if evidence_text is None:
        items.append(_missing_file("docs/application-evidence-log.md"))
    else:
        items.extend(_evidence_identity_items(evidence_text))
        for row_label, guidance, pattern, example in EVIDENCE_ROWS:
            items.append(
                ApplicationAuditItem(
                    label=f"Evidence link: {row_label}",
                    path="docs/application-evidence-log.md",
                    passed=_evidence_link_valid(evidence_text, row_label, pattern),
                    guidance=f"{guidance} Expected format: {example}",
                )
            )

    usage_plan_path = repo / "docs" / "codex-api-credits-plan.md"
    usage_plan_text = _read_text(usage_plan_path)
    if usage_plan_text is None:
        items.append(_missing_file("docs/codex-api-credits-plan.md"))
    else:
        items.extend(_usage_plan_items(usage_plan_text))

    return items


def _usage_plan_items(text: str) -> list[ApplicationAuditItem]:
    required_terms = (
        ("Issue triage", "Include issue triage as an API-assisted maintenance use case."),
        ("Pull request review", "Include pull request review as an API-assisted maintenance use case."),
        ("CI debugging", "Include CI debugging or failing-check summarization as a maintenance use case."),
        ("Release workflow", "Include release workflow or release note drafting as a maintenance use case."),
        ("Human review", "State that maintainers review AI output before posting, committing, or merging."),
    )

    normalized = text.lower()
    return [
        ApplicationAuditItem(
            label=f"API credits plan: {term}",
            path="docs/codex-api-credits-plan.md",
            passed=term.lower() in normalized,
            guidance=guidance,
        )
        for term, guidance in required_terms
    ]


def _field_format_items(text: str) -> list[ApplicationAuditItem]:
    repo_url = _field_value(text, "Public repository URL")
    maintainer_role = _field_value(text, "Maintainer role")
    chatgpt_status = _field_value(text, "ChatGPT account status")
    areas_of_interest = _field_value(text, "Areas of interest")

    return [
        ApplicationAuditItem(
            label="Application field: Public repository URL is GitHub URL",
            path="docs/application-workbook.md",
            passed=not _has_value(repo_url) or _is_github_repo_url(repo_url),
            guidance="Use a URL like https://github.com/OWNER/REPOSITORY.",
        ),
        ApplicationAuditItem(
            label="Application field: Maintainer role is valid",
            path="docs/application-workbook.md",
            passed=not _has_value(maintainer_role) or _normalized_value(maintainer_role) in MAINTAINER_ROLES,
            guidance="Use either main maintainer or core maintainer.",
        ),
        ApplicationAuditItem(
            label="Application field: ChatGPT account status is active",
            path="docs/application-workbook.md",
            passed=not _has_value(chatgpt_status) or _normalized_value(chatgpt_status) in {"active", "valid", "confirmed"},
            guidance="Use active, valid, or confirmed after checking the account.",
        ),
        ApplicationAuditItem(
            label="Application field: Areas of interest is valid",
            path="docs/application-workbook.md",
            passed=not _has_value(areas_of_interest)
            or _normalized_value(areas_of_interest)
            in {"codex security", "api credits", "both", "codex security and api credits", "api credits and codex security"},
            guidance="Use Codex Security, API credits, or both.",
        ),
    ]


def _evidence_identity_items(text: str) -> list[ApplicationAuditItem]:
    repo_url = _field_value(text, "Public repository URL")
    maintainer_role = _field_value(text, "Maintainer role")
    permission_evidence = _field_value(text, "Permission evidence")
    first_public_commit = _field_value(text, "First public commit")

    items = [
        ApplicationAuditItem(
            label=f"Evidence identity: {field}",
            path="docs/application-evidence-log.md",
            passed=_has_value(_field_value(text, field)),
            guidance=guidance,
        )
        for field, guidance in EVIDENCE_IDENTITY_FIELDS
    ]
    items.extend(
        [
            ApplicationAuditItem(
                label="Evidence identity: Public repository URL is GitHub URL",
                path="docs/application-evidence-log.md",
                passed=not _has_value(repo_url) or _is_github_repo_url(repo_url),
                guidance="Use a URL like https://github.com/OWNER/REPOSITORY.",
            ),
            ApplicationAuditItem(
                label="Evidence identity: Maintainer role is valid",
                path="docs/application-evidence-log.md",
                passed=not _has_value(maintainer_role) or _normalized_value(maintainer_role) in MAINTAINER_ROLES,
                guidance="Use either main maintainer or core maintainer.",
            ),
            ApplicationAuditItem(
                label="Evidence identity: Permission evidence is valid",
                path="docs/application-evidence-log.md",
                passed=not _has_value(permission_evidence)
                or _normalized_value(permission_evidence) in PERMISSION_EVIDENCE_VALUES,
                guidance="Use owner, admin, write access, or maintain access.",
            ),
            ApplicationAuditItem(
                label="Evidence identity: First public commit is GitHub commit URL",
                path="docs/application-evidence-log.md",
                passed=not _has_value(first_public_commit) or _is_github_commit_url(first_public_commit),
                guidance="Use a URL like https://github.com/OWNER/REPOSITORY/commit/COMMIT_SHA.",
            ),
        ]
    )
    return items


def _draft_items(text: str) -> list[ApplicationAuditItem]:
    project_draft = _code_block_after_heading(text, "项目说明")
    api_draft = _code_block_after_heading(text, "API credits")
    additional_info = _field_value(text, "Additional information")

    return [
        ApplicationAuditItem(
            label="Application draft: project eligibility explanation exists",
            path="docs/application-workbook.md",
            passed=_has_value(project_draft),
            guidance="Write the 500-character project eligibility explanation before applying.",
        ),
        ApplicationAuditItem(
            label="Application draft: project eligibility explanation under 500 characters",
            path="docs/application-workbook.md",
            passed=_within_form_limit(project_draft),
            guidance="Shorten the project eligibility explanation to 500 characters or fewer.",
        ),
        ApplicationAuditItem(
            label="Application draft: API credits plan exists",
            path="docs/application-workbook.md",
            passed=_has_value(api_draft),
            guidance="Write the 500-character API credits usage plan before applying.",
        ),
        ApplicationAuditItem(
            label="Application draft: API credits plan under 500 characters",
            path="docs/application-workbook.md",
            passed=_within_form_limit(api_draft),
            guidance="Shorten the API credits usage plan to 500 characters or fewer.",
        ),
        ApplicationAuditItem(
            label="Application field: Additional information under 500 characters",
            path="docs/application-workbook.md",
            passed=additional_info is None or not additional_info or _within_form_limit(additional_info),
            guidance="Keep optional additional information to 500 characters or fewer if you fill it in.",
        ),
    ]


def application_audit_score(items: list[ApplicationAuditItem]) -> int:
    if not items:
        return 0
    passed = sum(1 for item in items if item.passed)
    return round((passed / len(items)) * 100)


def _field_value(text: str, field: str) -> str | None:
    pattern = rf"^-[ \t]+{re.escape(field)}:[ \t]*(.*)$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def _has_value(value: str | None) -> bool:
    if not value:
        return False
    normalized = _normalized_value(value)
    return normalized not in {
        "todo",
        "tbd",
        "your_username",
        "your name",
        "n/a",
        "main maintainer / core maintainer",
        "owner / admin / write access / other",
        "codex security / api credits / both",
    }


def _normalized_value(value: str | None) -> str:
    if value is None:
        return ""
    return " ".join(value.strip().lower().split())


def _within_form_limit(value: str | None, limit: int = MAX_FORM_CHARACTERS) -> bool:
    if not _has_value(value):
        return False
    return len(value.strip()) <= limit


def _code_block_after_heading(text: str, heading_keyword: str) -> str | None:
    pattern = rf"^## [^\n]*{re.escape(heading_keyword)}[^\n]*\r?\n(?P<body>.*?)(?=^## |\Z)"
    section = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if not section:
        return None

    code_block = re.search(r"```(?:text)?\s*(.*?)```", section.group("body"), flags=re.DOTALL)
    if not code_block:
        return None

    return code_block.group(1).strip()


def _evidence_link_valid(text: str, row_label: str, pattern: str) -> bool:
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[1] == row_label:
            return bool(cells[2]) and bool(re.match(pattern, cells[2]))
    return False


def _is_github_repo_url(value: str | None) -> bool:
    if not value:
        return False
    return bool(re.match(r"^https://github\.com/[^/\s]+/[^/\s]+/?$", value.strip()))


def _is_github_commit_url(value: str | None) -> bool:
    if not value:
        return False
    return bool(re.match(r"^https://github\.com/[^/\s]+/[^/\s]+/commit/[0-9a-fA-F]{7,40}/?$", value.strip()))


def _missing_file(path: str) -> ApplicationAuditItem:
    return ApplicationAuditItem(
        label=f"Missing file: {path}",
        path=path,
        passed=False,
        guidance="Create this file before running the application audit.",
    )


def _read_text(path: Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")
