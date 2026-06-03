from __future__ import annotations

import argparse
from pathlib import Path

from .application_audit import ApplicationAuditItem, application_audit_score, audit_application_docs
from .checks import CheckResult, next_actions, readiness_score, run_all_checks
from .skills_audit import GitHubSkillAuditItem, audit_github_skills, github_skills_score


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codex-oss-readiness",
        description="Check whether an OSS repository is ready for GitHub practice and Codex for OSS preparation.",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Path to the repository to check. Defaults to the current directory.",
    )
    parser.add_argument(
        "--missing-only",
        action="store_true",
        help="Show only missing checklist items.",
    )
    audit_mode = parser.add_mutually_exclusive_group()
    audit_mode.add_argument(
        "--application-audit",
        action="store_true",
        help="Audit application workbook fields and public evidence links.",
    )
    audit_mode.add_argument(
        "--skills-audit",
        action="store_true",
        help="Audit GitHub skills matrix evidence and reflections.",
    )
    return parser


def format_results(results: list[CheckResult], missing_only: bool = False) -> str:
    visible_results = [result for result in results if not result.exists] if missing_only else results
    lines = [f"Codex OSS readiness score: {readiness_score(results)}%"]

    if missing_only and not visible_results:
        lines.append("All checklist items are present.")
        return "\n".join(lines)

    for result in visible_results:
        status = "PASS" if result.exists else "TODO"
        lines.append(f"[{status}] {result.check.label}: {result.check.path}")
        if not result.exists:
            lines.append(f"       Why: {result.check.why_it_matters}")

    actions = next_actions(results)
    if actions:
        lines.append("")
        lines.append("Next actions:")
        for index, action in enumerate(actions, start=1):
            lines.append(f"{index}. {action}")

    return "\n".join(lines)


def format_application_audit(items: list[ApplicationAuditItem], missing_only: bool = False) -> str:
    visible_items = [item for item in items if not item.passed] if missing_only else items
    lines = [f"Codex for OSS application audit score: {application_audit_score(items)}%"]

    if missing_only and not visible_items:
        lines.append("All application audit items are complete.")
        return "\n".join(lines)

    for item in visible_items:
        status = "PASS" if item.passed else "TODO"
        lines.append(f"[{status}] {item.label}: {item.path}")
        if not item.passed:
            lines.append(f"       Guidance: {item.guidance}")

    missing_count = sum(1 for item in items if not item.passed)
    if missing_count:
        lines.append("")
        lines.append("Next actions:")
        lines.append("1. Fill public-safe fields directly in docs/application-workbook.md.")
        lines.append("2. Record sensitive account values privately, then enter them only in the application form.")
        if any(item.label.startswith("Evidence identity:") and not item.passed for item in items):
            lines.append(
                "3. After publishing, fill docs/application-evidence-log.md with GitHub identity and permission evidence."
            )
            lines.append("4. Add real issue, pull request, CI, and release links after publishing to GitHub.")
        else:
            lines.append("3. Add real issue, pull request, CI, and release links after publishing to GitHub.")

    return "\n".join(lines)


def format_skills_audit(items: list[GitHubSkillAuditItem], missing_only: bool = False) -> str:
    visible_items = [item for item in items if not item.passed] if missing_only else items
    lines = [f"GitHub skills audit score: {github_skills_score(items)}%"]

    if missing_only and not visible_items:
        lines.append("All GitHub skills have evidence and reflections.")
        return "\n".join(lines)

    for item in visible_items:
        status = "PASS" if item.passed else "TODO"
        lines.append(f"[{status}] {item.label}: {item.level}")
        if not item.passed:
            lines.append(f"       Guidance: {item.guidance}")

    missing_count = sum(1 for item in items if not item.passed)
    if missing_count:
        lines.append("")
        lines.append("Next actions:")
        lines.append("1. Complete one real GitHub operation from docs/github-skills-matrix.md.")
        lines.append("2. Add the evidence link or note and a short reflection.")
        lines.append("3. Sync the strongest public evidence into docs/application-evidence-log.md.")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    repo = Path(args.repo)

    if not repo.exists():
        parser.error(f"Repository path does not exist: {repo}")

    if args.application_audit:
        items = audit_application_docs(repo)
        print(format_application_audit(items, missing_only=args.missing_only))
        return 0

    if args.skills_audit:
        items = audit_github_skills(repo)
        print(format_skills_audit(items, missing_only=args.missing_only))
        return 0

    results = run_all_checks(repo)
    print(format_results(results, missing_only=args.missing_only))
    return 0
