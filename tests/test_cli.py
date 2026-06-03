import unittest

from src.codex_oss_readiness.checks import Check, CheckResult
from src.codex_oss_readiness.application_audit import ApplicationAuditItem
from src.codex_oss_readiness.cli import format_application_audit, format_results, format_skills_audit
from src.codex_oss_readiness.skills_audit import GitHubSkillAuditItem


class CliFormatTests(unittest.TestCase):
    def test_format_results_includes_missing_reason(self):
        output = format_results(
            [
                CheckResult(
                    check=Check("README.md", "README", "Explains the project."),
                    exists=False,
                )
            ]
        )

        self.assertIn("Codex OSS readiness score: 0%", output)
        self.assertIn("[TODO] README: README.md", output)
        self.assertIn("Why: Explains the project.", output)
        self.assertIn("Next actions:", output)

    def test_missing_only_hides_passed_items(self):
        output = format_results(
            [
                CheckResult(
                    check=Check("README.md", "README", "Explains the project."),
                    exists=True,
                ),
                CheckResult(
                    check=Check("LICENSE", "License", "Declares reuse terms."),
                    exists=False,
                ),
            ],
            missing_only=True,
        )

        self.assertNotIn("README.md", output)
        self.assertIn("LICENSE", output)

    def test_format_application_audit_includes_guidance(self):
        output = format_application_audit(
            [
                ApplicationAuditItem(
                    label="Application field: GitHub username",
                    path="docs/application-workbook.md",
                    passed=False,
                    guidance="Use the public GitHub username.",
                )
            ]
        )

        self.assertIn("Codex for OSS application audit score: 0%", output)
        self.assertIn("[TODO] Application field: GitHub username", output)
        self.assertIn("Guidance: Use the public GitHub username.", output)

    def test_format_application_audit_mentions_identity_evidence_next_action(self):
        output = format_application_audit(
            [
                ApplicationAuditItem(
                    label="Evidence identity: Public repository URL",
                    path="docs/application-evidence-log.md",
                    passed=False,
                    guidance="Record the public GitHub repository URL.",
                )
            ],
            missing_only=True,
        )

        self.assertIn("GitHub identity and permission evidence", output)
        self.assertIn("Add real issue, pull request, CI, and release links", output)

    def test_format_skills_audit_includes_next_actions(self):
        output = format_skills_audit(
            [
                GitHubSkillAuditItem(
                    label="GitHub skill: 创建第一次提交",
                    level="第 1 级：本地 Git 基础",
                    passed=False,
                    guidance="Add evidence and reflection.",
                )
            ],
            missing_only=True,
        )

        self.assertIn("GitHub skills audit score: 0%", output)
        self.assertIn("[TODO] GitHub skill: 创建第一次提交", output)
        self.assertIn("Complete one real GitHub operation", output)


if __name__ == "__main__":
    unittest.main()
