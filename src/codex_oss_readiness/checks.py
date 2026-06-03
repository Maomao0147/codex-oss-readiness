from __future__ import annotations

import subprocess
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Check:
    path: str
    label: str
    why_it_matters: str
    category: str = "file"


@dataclass(frozen=True)
class CheckResult:
    check: Check
    exists: bool


DEFAULT_CHECKS: tuple[Check, ...] = (
    Check("README.md", "README", "Explains what the project does and how to use it."),
    Check("LICENSE", "License", "Makes reuse terms clear for contributors and users."),
    Check("CONTRIBUTING.md", "Contributing guide", "Shows how people can report, fix, and review work."),
    Check("CHANGELOG.md", "Changelog", "Keeps releases and project history easy to review."),
    Check(".gitignore", "Git ignore file", "Keeps local build and cache files out of commits."),
    Check(
        ".github/ISSUE_TEMPLATE/bug_report.md",
        "Bug report issue template",
        "Makes bug reports easier to reproduce and triage.",
    ),
    Check(
        ".github/ISSUE_TEMPLATE/feature_request.md",
        "Feature request issue template",
        "Keeps new ideas structured and comparable.",
    ),
    Check(
        ".github/ISSUE_TEMPLATE/config.yml",
        "Issue template chooser config",
        "Documents how people should route project issues and support requests.",
    ),
    Check(
        ".github/labels.yml",
        "GitHub label reference",
        "Defines the labels used for issue triage and maintenance evidence.",
    ),
    Check(
        ".github/PULL_REQUEST_TEMPLATE.md",
        "Pull request template",
        "Encourages contributors to explain behavior and tests.",
    ),
    Check(
        ".github/workflows/ci.yml",
        "GitHub Actions CI workflow",
        "Runs tests automatically on pushes and pull requests.",
    ),
    Check(
        ".github/RELEASE_TEMPLATE.md",
        "Release notes template",
        "Makes releases easier to review and repeat.",
    ),
    Check(
        "docs/github-4-week-plan.md",
        "Four-week GitHub plan",
        "Turns learning into a visible maintenance roadmap.",
    ),
    Check(
        "docs/application-workbook.md",
        "Application workbook",
        "Keeps Codex for OSS application answers honest and concrete.",
    ),
    Check(
        "docs/application-form-walkthrough.md",
        "Application form walkthrough",
        "Maps official Codex for OSS form fields to local preparation files.",
    ),
    Check(
        "docs/codex-api-credits-plan.md",
        "Codex API credits usage plan",
        "Explains planned API-assisted maintenance tasks and human review boundaries.",
    ),
    Check(
        "docs/github-profile-checklist.md",
        "GitHub profile checklist",
        "Prepares the public maintainer identity shown in the application.",
    ),
    Check(
        "docs/application-evidence-log.md",
        "Application evidence log",
        "Connects application claims to public GitHub evidence.",
    ),
    Check(
        "docs/final-application-audit.md",
        "Final application audit",
        "Checks eligibility, evidence, and application answers before submission.",
    ),
    Check(
        "docs/openai-org-id-guide.md",
        "OpenAI organization ID guide",
        "Prepares the OpenAI account identifier required by the application form.",
    ),
    Check(
        "docs/privacy-and-public-repo.md",
        "Public repository privacy guide",
        "Explains which application values should not be committed to a public repository.",
    ),
    Check(
        "docs/private-info.template.md",
        "Private application info template",
        "Gives maintainers a safe place to copy sensitive application fields outside Git.",
    ),
    Check(
        "docs/release-checklist.md",
        "Release checklist",
        "Supports repeatable release notes and version history.",
    ),
    Check(
        "docs/first-commit-and-publish.md",
        "First commit and publish guide",
        "Gives first-time GitHub users a concrete path from local repo to public repo.",
    ),
    Check(
        "docs/github-auth-and-push-guide.md",
        "GitHub auth and push guide",
        "Explains HTTPS, SSH, remotes, and safe authentication for the first push.",
    ),
    Check(
        "docs/commit-and-branch-guide.md",
        "Commit and branch guide",
        "Keeps Git history readable and connected to issues, PRs, CI, and releases.",
    ),
    Check(
        "docs/github-cheatsheet.md",
        "GitHub beginner cheatsheet",
        "Keeps common commands close while learning the first workflows.",
    ),
    Check(
        "docs/maintenance-backlog.md",
        "Maintenance backlog",
        "Provides real issue ideas for practicing open-source maintenance.",
    ),
    Check(
        "docs/issue-triage-guide.md",
        "Issue triage guide",
        "Turns new issues into labels, decisions, pull requests, and application evidence.",
    ),
    Check(
        "docs/github-labels.md",
        "GitHub labels guide",
        "Explains how to create and apply the repository label set manually.",
    ),
    Check(
        "docs/week-by-week-tracker.md",
        "Week-by-week tracker",
        "Connects learning tasks to visible GitHub evidence.",
    ),
    Check(
        "docs/github-skills-matrix.md",
        "GitHub skills matrix",
        "Maps GitHub learning milestones to public evidence links and reflections.",
    ),
    Check(
        "docs/first-pr-lab.md",
        "First pull request lab",
        "Gives beginners a concrete issue-to-PR-to-CI workflow to practice.",
    ),
    Check(
        "docs/pr-review-guide.md",
        "Pull request review guide",
        "Turns PR review into visible maintenance evidence and safer merges.",
    ),
    Check(
        "docs/first-release-lab.md",
        "First release lab",
        "Guides the first public release and records release evidence.",
    ),
    Check(
        "docs/ci-debugging-lab.md",
        "CI debugging lab",
        "Teaches how to inspect failing GitHub Actions runs and preserve debugging evidence.",
    ),
    Check(
        "docs/repository-settings-checklist.md",
        "Repository settings checklist",
        "Covers public repository settings that make the project easier to inspect and maintain.",
    ),
)


PRIVACY_CHECKS: tuple[Check, ...] = (
    Check(
        ".gitignore private/",
        "private directory ignored",
        "Private application notes should stay out of public Git history.",
        "privacy",
    ),
    Check(
        ".gitignore *.private.md",
        "private markdown files ignored",
        "Copied private application files should not be committed accidentally.",
        "privacy",
    ),
    Check(
        ".gitignore .env",
        "environment files ignored",
        "Tokens, keys, and local environment values should not be committed.",
        "privacy",
    ),
)


GIT_CHECKS: tuple[Check, ...] = (
    Check(
        "git repository",
        "Git repository initialized",
        "Git is the local foundation for commits, branches, and pull requests.",
        "git",
    ),
    Check(
        "git user.name",
        "Git user.name configured",
        "Commit history should show the maintainer identity you intend to use.",
        "git",
    ),
    Check(
        "git user.email",
        "Git user.email configured",
        "Commit history should use an email you are comfortable associating with GitHub.",
        "git",
    ),
    Check(
        "main branch",
        "Main branch is named main",
        "GitHub repositories usually use main as the default branch for PRs and releases.",
        "git",
    ),
    Check(
        "first commit",
        "First commit exists",
        "A first commit turns the starter files into reviewable project history.",
        "git",
    ),
    Check(
        "origin remote on GitHub",
        "GitHub remote configured",
        "A public GitHub remote is required before issues, pull requests, and releases can be practiced.",
        "git",
    ),
)


GitRunner = Callable[[Path, list[str]], tuple[bool, str]]


def run_checks(repo: Path, checks: tuple[Check, ...] = DEFAULT_CHECKS) -> list[CheckResult]:
    repo = repo.expanduser().resolve()
    return [CheckResult(check=check, exists=(repo / check.path).exists()) for check in checks]


def run_privacy_checks(repo: Path) -> list[CheckResult]:
    repo = repo.expanduser().resolve()
    gitignore = repo / ".gitignore"
    lines = _normalized_gitignore_lines(gitignore)

    return [
        CheckResult(check=PRIVACY_CHECKS[0], exists="private/" in lines),
        CheckResult(check=PRIVACY_CHECKS[1], exists="*.private.md" in lines),
        CheckResult(check=PRIVACY_CHECKS[2], exists=".env" in lines and ".env.*" in lines),
    ]


def run_git_checks(repo: Path, runner: GitRunner | None = None) -> list[CheckResult]:
    repo = repo.expanduser().resolve()
    runner = runner or _run_git

    is_repo, _ = runner(repo, ["rev-parse", "--is-inside-work-tree"])
    has_user_name, user_name = runner(repo, ["config", "--get", "user.name"])
    has_user_email, user_email = runner(repo, ["config", "--get", "user.email"])
    has_branch, branch_name = runner(repo, ["branch", "--show-current"])
    has_commit, _ = runner(repo, ["rev-parse", "--verify", "HEAD"])
    has_origin, origin_url = runner(repo, ["remote", "get-url", "origin"])
    has_github_origin = has_origin and "github.com" in origin_url.lower()

    return [
        CheckResult(check=GIT_CHECKS[0], exists=is_repo),
        CheckResult(check=GIT_CHECKS[1], exists=has_user_name and bool(user_name.strip())),
        CheckResult(check=GIT_CHECKS[2], exists=has_user_email and bool(user_email.strip())),
        CheckResult(check=GIT_CHECKS[3], exists=has_branch and branch_name.strip() == "main"),
        CheckResult(check=GIT_CHECKS[4], exists=has_commit),
        CheckResult(check=GIT_CHECKS[5], exists=has_github_origin),
    ]


def run_all_checks(repo: Path) -> list[CheckResult]:
    return [*run_checks(repo), *run_privacy_checks(repo), *run_git_checks(repo)]


def readiness_score(results: list[CheckResult]) -> int:
    if not results:
        return 0
    passed = sum(1 for result in results if result.exists)
    return round((passed / len(results)) * 100)


def next_actions(results: list[CheckResult], limit: int = 3) -> list[str]:
    missing = [result for result in results if not result.exists]
    missing_labels = {result.check.label for result in missing}
    actions: list[str] = []

    if "Git repository initialized" in missing_labels:
        actions.append("Initialize Git locally so commits and branches can be practiced.")

    identity_missing = "Git user.name configured" in missing_labels or "Git user.email configured" in missing_labels

    if identity_missing:
        actions.append("Configure Git user.name and user.email for this repository before the first commit.")

    if "Main branch is named main" in missing_labels:
        actions.append("Rename the current branch to main so GitHub PR and release docs match the repository.")

    if "First commit exists" in missing_labels:
        if identity_missing:
            actions.append("Create the first commit after Git identity is configured.")
        else:
            actions.append("Follow docs/first-commit-and-publish.md to create the first commit.")

    if "GitHub remote configured" in missing_labels:
        actions.append(
            "Create a public GitHub repository in the browser, add it as origin, and push the main branch."
        )

    if any(result.check.category == "privacy" for result in missing):
        actions.append("Restore privacy ignore rules before adding application or account notes.")

    for result in missing:
        if result.check.category == "file":
            actions.append(f"Create or restore {result.check.path}: {result.check.why_it_matters}")

    if not actions and results:
        actions.extend(
            [
                "Create real GitHub issues from docs/maintenance-backlog.md.",
                "Handle each issue through a branch and pull request.",
                "Prepare a first release, then complete docs/application-evidence-log.md and docs/final-application-audit.md.",
            ]
        )

    return actions[:limit]


def _run_git(repo: Path, args: list[str]) -> tuple[bool, str]:
    try:
        completed = subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True,
            check=False,
            text=True,
        )
    except FileNotFoundError:
        return False, ""

    output = completed.stdout.strip() or completed.stderr.strip()
    return completed.returncode == 0, output


def _normalized_gitignore_lines(path: Path) -> set[str]:
    if not path.exists():
        return set()

    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
