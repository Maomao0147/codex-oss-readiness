from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GitHubSkillAuditItem:
    label: str
    level: str
    passed: bool
    guidance: str


def audit_github_skills(repo: Path) -> list[GitHubSkillAuditItem]:
    repo = repo.expanduser().resolve()
    matrix_path = repo / "docs" / "github-skills-matrix.md"
    text = _read_text(matrix_path)
    if text is None:
        return [
            GitHubSkillAuditItem(
                label="Missing file: docs/github-skills-matrix.md",
                level="file",
                passed=False,
                guidance="Create docs/github-skills-matrix.md before auditing GitHub learning progress.",
            )
        ]

    return _skill_items(text)


def github_skills_score(items: list[GitHubSkillAuditItem]) -> int:
    if not items:
        return 0
    passed = sum(1 for item in items if item.passed)
    return round((passed / len(items)) * 100)


def _skill_items(text: str) -> list[GitHubSkillAuditItem]:
    items: list[GitHubSkillAuditItem] = []
    current_level = "GitHub skills"

    for line in text.splitlines():
        heading = re.match(r"^##\s+(.+)$", line)
        if heading:
            current_level = heading.group(1).strip()
            continue

        cells = _table_cells(line)
        if not cells:
            continue

        skill, evidence, reflection = cells[0], cells[2], cells[3]
        has_evidence = _has_value(evidence)
        has_reflection = _has_value(reflection)
        items.append(
            GitHubSkillAuditItem(
                label=f"GitHub skill: {skill}",
                level=current_level,
                passed=has_evidence and has_reflection,
                guidance="Add an evidence link or note and a one-sentence reflection in docs/github-skills-matrix.md.",
            )
        )

    return items


def _table_cells(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None

    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if len(cells) < 4:
        return None
    if cells[0].lower() == "skill" or set(cells[0]) <= {"-"}:
        return None

    return cells


def _has_value(value: str | None) -> bool:
    if not value:
        return False
    normalized = " ".join(value.strip().lower().split())
    return normalized not in {"todo", "tbd", "n/a", "none", "-"}


def _read_text(path: Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")
