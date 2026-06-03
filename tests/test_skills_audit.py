import tempfile
import unittest
from pathlib import Path

from src.codex_oss_readiness.skills_audit import audit_github_skills, github_skills_score


class GitHubSkillsAuditTests(unittest.TestCase):
    def test_audit_reports_missing_matrix_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            items = audit_github_skills(Path(tmp))

        self.assertEqual(1, len(items))
        self.assertFalse(items[0].passed)
        self.assertEqual("Missing file: docs/github-skills-matrix.md", items[0].label)

    def test_audit_requires_evidence_and_reflection(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            docs = repo / "docs"
            docs.mkdir()
            (docs / "github-skills-matrix.md").write_text(
                "\n".join(
                    [
                        "## 第 1 级：本地 Git 基础",
                        "",
                        "| Skill | Acceptance evidence | Evidence link or note | Reflection |",
                        "| --- | --- | --- | --- |",
                        "| 查看仓库状态 | 能解释 git status | Ran git status locally | I learned when files are untracked. |",
                        "| 创建第一次提交 | main 分支有 first commit |  |  |",
                    ]
                ),
                encoding="utf-8",
            )

            items = audit_github_skills(repo)

        missing_labels = {item.label for item in items if not item.passed}
        self.assertEqual(50, github_skills_score(items))
        self.assertNotIn("GitHub skill: 查看仓库状态", missing_labels)
        self.assertIn("GitHub skill: 创建第一次提交", missing_labels)

    def test_audit_rejects_placeholder_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            docs = repo / "docs"
            docs.mkdir()
            (docs / "github-skills-matrix.md").write_text(
                "\n".join(
                    [
                        "## 第 2 级：公开仓库基础",
                        "",
                        "| Skill | Acceptance evidence | Evidence link or note | Reflection |",
                        "| --- | --- | --- | --- |",
                        "| 创建 public 仓库 | repository URL 可以访问 | TBD | TODO |",
                    ]
                ),
                encoding="utf-8",
            )

            items = audit_github_skills(repo)

        self.assertEqual(0, github_skills_score(items))
        self.assertFalse(items[0].passed)


if __name__ == "__main__":
    unittest.main()
