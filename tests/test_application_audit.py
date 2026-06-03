import tempfile
import unittest
from pathlib import Path

from src.codex_oss_readiness.application_audit import (
    application_audit_score,
    audit_application_docs,
)


class ApplicationAuditTests(unittest.TestCase):
    def test_audit_finds_blank_fields_and_missing_evidence_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            docs = repo / "docs"
            docs.mkdir()
            (docs / "application-workbook.md").write_text(
                "\n".join(
                    [
                        "- Last name:",
                        "- First name:",
                        "- Email associated with ChatGPT account: user@example.com",
                        "- GitHub username:",
                        "- Public repository URL: https://github.com/example/repo",
                        "- OpenAI organization ID: recorded privately",
                        "- Maintainer role: main maintainer / core maintainer",
                        "- ChatGPT account status: active",
                        "- Country or region: US",
                        "- Areas of interest:",
                        "- Additional information:",
                        "",
                        "## 500 字以内项目说明草稿",
                        "",
                        "```text",
                        "A" * 501,
                        "```",
                        "",
                        "## 500 字以内 API credits 使用计划草稿",
                        "",
                        "```text",
                        "Use credits for PR review and release notes with human review.",
                        "```",
                    ]
                ),
                encoding="utf-8",
            )
            (docs / "application-evidence-log.md").write_text(
                "\n".join(
                    [
                        "## 仓库身份",
                        "",
                        "- GitHub username:",
                        "- Public repository URL: https://github.com/example/repo",
                        "- Maintainer role: main maintainer / core maintainer",
                        "- Permission evidence: owner / admin / write access / other",
                        "- First public commit:",
                        "",
                        "| Evidence type | Target | Link | Notes |",
                        "| --- | --- | --- | --- |",
                        "| Issue | First issue |  |  |",
                        "| Pull request | First merged PR | https://github.com/example/repo/pull/1 |  |",
                        "| CI run | First passing CI | https://github.com/example/repo/actions/runs/1 |  |",
                        "| Release | v0.1.0 |  |  |",
                    ]
                ),
                encoding="utf-8",
            )
            (docs / "codex-api-credits-plan.md").write_text(
                "Issue triage\nPull request review\nCI debugging\nRelease workflow\nHuman review\n",
                encoding="utf-8",
            )

            items = audit_application_docs(repo)

        missing_labels = {item.label for item in items if not item.passed}
        self.assertIn("Application field: Last name", missing_labels)
        self.assertIn("Application field: First name", missing_labels)
        self.assertIn("Application field: GitHub username", missing_labels)
        self.assertIn("Application field: Maintainer role", missing_labels)
        self.assertIn("Application field: Areas of interest", missing_labels)
        self.assertIn(
            "Application draft: project eligibility explanation under 500 characters",
            missing_labels,
        )
        self.assertIn("Evidence identity: GitHub username", missing_labels)
        self.assertIn("Evidence identity: Maintainer role", missing_labels)
        self.assertIn("Evidence identity: Permission evidence", missing_labels)
        self.assertIn("Evidence identity: First public commit", missing_labels)
        self.assertIn("Evidence link: First issue", missing_labels)
        self.assertIn("Evidence link: v0.1.0", missing_labels)

    def test_audit_passes_draft_length_checks_when_under_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            docs = repo / "docs"
            docs.mkdir()
            (docs / "application-workbook.md").write_text(
                "\n".join(
                    [
                        "- Last name: Maintainer",
                        "- First name: Example",
                        "- Email associated with ChatGPT account: user@example.com",
                        "- GitHub username: example",
                        "- Public repository URL: https://github.com/example/repo",
                        "- OpenAI organization ID: recorded privately",
                        "- Maintainer role: main maintainer",
                        "- ChatGPT account status: active",
                        "- Country or region: US",
                        "- Areas of interest: API credits",
                        "- Additional information:",
                        "",
                        "## 500 字以内项目说明草稿",
                        "",
                        "```text",
                        "A small checklist CLI for beginner OSS maintainers.",
                        "```",
                        "",
                        "## 500 字以内 API credits 使用计划草稿",
                        "",
                        "```text",
                        "Use credits for issue triage, PR review drafts, and release notes with maintainer review.",
                        "```",
                    ]
                ),
                encoding="utf-8",
            )
            (docs / "application-evidence-log.md").write_text(
                "\n".join(
                    [
                        "## 仓库身份",
                        "",
                        "- GitHub username: example",
                        "- Public repository URL: https://github.com/example/repo",
                        "- Maintainer role: main maintainer",
                        "- Permission evidence: owner",
                        "- First public commit: https://github.com/example/repo/commit/abcdef1",
                        "",
                        "| Evidence type | Target | Link | Notes |",
                        "| --- | --- | --- | --- |",
                        "| Issue | First issue | https://github.com/example/repo/issues/1 |  |",
                        "| Pull request | First merged PR | https://github.com/example/repo/pull/1 |  |",
                        "| Pull request review | First PR review note | https://github.com/example/repo/pull/1 |  |",
                        "| CI run | First passing CI | https://github.com/example/repo/actions/runs/1 |  |",
                        "| Release | v0.1.0 | https://github.com/example/repo/releases/tag/v0.1.0 |  |",
                    ]
                ),
                encoding="utf-8",
            )
            (docs / "codex-api-credits-plan.md").write_text(
                "Issue triage\nPull request review\nCI debugging\nRelease workflow\nHuman review\n",
                encoding="utf-8",
            )

            items = audit_application_docs(repo)

        missing_labels = {item.label for item in items if not item.passed}
        self.assertNotIn("Application draft: project eligibility explanation exists", missing_labels)
        self.assertNotIn(
            "Application draft: project eligibility explanation under 500 characters",
            missing_labels,
        )
        self.assertNotIn("Application draft: API credits plan under 500 characters", missing_labels)
        self.assertEqual(set(), missing_labels)

    def test_audit_rejects_wrong_github_evidence_link_types(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            docs = repo / "docs"
            docs.mkdir()
            (docs / "application-workbook.md").write_text(
                "\n".join(
                    [
                        "- Last name: Maintainer",
                        "- First name: Example",
                        "- Email associated with ChatGPT account: user@example.com",
                        "- GitHub username: example",
                        "- Public repository URL: https://gitlab.com/example/repo",
                        "- OpenAI organization ID: recorded privately",
                        "- Maintainer role: owner",
                        "- ChatGPT account status: expired",
                        "- Country or region: US",
                        "- Areas of interest: stickers",
                        "- Additional information:",
                        "",
                        "## 500 字以内项目说明草稿",
                        "",
                        "```text",
                        "A small checklist CLI for beginner OSS maintainers.",
                        "```",
                        "",
                        "## 500 字以内 API credits 使用计划草稿",
                        "",
                        "```text",
                        "Use credits for issue triage and PR review drafts with maintainer review.",
                        "```",
                    ]
                ),
                encoding="utf-8",
            )
            (docs / "application-evidence-log.md").write_text(
                "\n".join(
                    [
                        "## 仓库身份",
                        "",
                        "- GitHub username: example",
                        "- Public repository URL: https://gitlab.com/example/repo",
                        "- Maintainer role: owner",
                        "- Permission evidence: other",
                        "- First public commit: https://github.com/example/repo/pull/1",
                        "",
                        "| Evidence type | Target | Link | Notes |",
                        "| --- | --- | --- | --- |",
                        "| Issue | First issue | https://github.com/example/repo/pull/1 | wrong type |",
                        "| Pull request | First merged PR | https://github.com/example/repo/issues/1 | wrong type |",
                        "| Pull request review | First PR review note | https://github.com/example/repo/issues/1 | wrong type |",
                        "| CI run | First passing CI | https://github.com/example/repo/actions | wrong type |",
                        "| Release | v0.1.0 | https://github.com/example/repo/releases | wrong type |",
                    ]
                ),
                encoding="utf-8",
            )
            (docs / "codex-api-credits-plan.md").write_text(
                "Issue triage\nPull request review\nCI debugging\nRelease workflow\n",
                encoding="utf-8",
            )

            items = audit_application_docs(repo)

        missing_labels = {item.label for item in items if not item.passed}
        self.assertIn("Application field: Public repository URL is GitHub URL", missing_labels)
        self.assertIn("Application field: Maintainer role is valid", missing_labels)
        self.assertIn("Application field: ChatGPT account status is active", missing_labels)
        self.assertIn("Application field: Areas of interest is valid", missing_labels)
        self.assertIn("API credits plan: Human review", missing_labels)
        self.assertIn("Evidence identity: Public repository URL is GitHub URL", missing_labels)
        self.assertIn("Evidence identity: Maintainer role is valid", missing_labels)
        self.assertIn("Evidence identity: Permission evidence is valid", missing_labels)
        self.assertIn("Evidence identity: First public commit is GitHub commit URL", missing_labels)
        self.assertIn("Evidence link: First issue", missing_labels)
        self.assertIn("Evidence link: First merged PR", missing_labels)
        self.assertIn("Evidence link: First PR review note", missing_labels)
        self.assertIn("Evidence link: First passing CI", missing_labels)
        self.assertIn("Evidence link: v0.1.0", missing_labels)

    def test_application_audit_score_counts_passed_items(self):
        items = [
            type("Item", (), {"passed": True})(),
            type("Item", (), {"passed": False})(),
            type("Item", (), {"passed": True})(),
        ]

        self.assertEqual(application_audit_score(items), 67)


if __name__ == "__main__":
    unittest.main()
