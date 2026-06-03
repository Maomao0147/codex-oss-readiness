import tempfile
import unittest
from pathlib import Path

from src.codex_oss_readiness.checks import (
    Check,
    CheckResult,
    next_actions,
    readiness_score,
    run_git_checks,
    run_privacy_checks,
    run_checks,
)


class ReadinessCheckTests(unittest.TestCase):
    def test_run_checks_reports_existing_and_missing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "README.md").write_text("# Demo\n", encoding="utf-8")

            checks = (
                Check("README.md", "README", "Explains the project."),
                Check("LICENSE", "License", "Declares reuse terms."),
            )

            results = run_checks(repo, checks)

        self.assertTrue(results[0].exists)
        self.assertFalse(results[1].exists)

    def test_readiness_score_rounds_percentage(self):
        results = [
            type("Result", (), {"exists": True})(),
            type("Result", (), {"exists": False})(),
            type("Result", (), {"exists": True})(),
        ]

        self.assertEqual(readiness_score(results), 67)

    def test_readiness_score_is_zero_without_checks(self):
        self.assertEqual(readiness_score([]), 0)

    def test_run_privacy_checks_reads_gitignore_rules(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / ".gitignore").write_text(
                "\n".join(["private/", "*.private.md", ".env", ".env.*"]),
                encoding="utf-8",
            )

            results = run_privacy_checks(repo)

        self.assertTrue(all(result.exists for result in results))

    def test_run_privacy_checks_reports_missing_rules(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / ".gitignore").write_text("private/\n", encoding="utf-8")

            results = run_privacy_checks(repo)

        missing_labels = {result.check.label for result in results if not result.exists}
        self.assertIn("private markdown files ignored", missing_labels)
        self.assertIn("environment files ignored", missing_labels)

    def test_run_git_checks_uses_runner_output(self):
        def fake_runner(repo, args):
            outputs = {
                ("rev-parse", "--is-inside-work-tree"): (True, "true"),
                ("config", "--get", "user.name"): (True, "Example Maintainer"),
                ("config", "--get", "user.email"): (True, "example@users.noreply.github.com"),
                ("branch", "--show-current"): (True, "main"),
                ("rev-parse", "--verify", "HEAD"): (True, "abc123"),
                ("remote", "get-url", "origin"): (True, "https://github.com/example/repo.git"),
            }
            return outputs[tuple(args)]

        results = run_git_checks(Path("."), runner=fake_runner)

        self.assertTrue(all(result.exists for result in results))

    def test_run_git_checks_requires_github_origin(self):
        def fake_runner(repo, args):
            outputs = {
                ("rev-parse", "--is-inside-work-tree"): (True, "true"),
                ("config", "--get", "user.name"): (True, "Example Maintainer"),
                ("config", "--get", "user.email"): (True, "example@users.noreply.github.com"),
                ("branch", "--show-current"): (True, "main"),
                ("rev-parse", "--verify", "HEAD"): (True, "abc123"),
                ("remote", "get-url", "origin"): (True, "https://gitlab.com/example/repo.git"),
            }
            return outputs[tuple(args)]

        results = run_git_checks(Path("."), runner=fake_runner)

        self.assertFalse(results[5].exists)

    def test_next_actions_prioritizes_first_commit_before_remote(self):
        results = [
            CheckResult(Check("git repository", "Git repository initialized", "Needed.", "git"), True),
            CheckResult(Check("git user.name", "Git user.name configured", "Needed.", "git"), True),
            CheckResult(Check("git user.email", "Git user.email configured", "Needed.", "git"), True),
            CheckResult(Check("main branch", "Main branch is named main", "Needed.", "git"), True),
            CheckResult(Check("first commit", "First commit exists", "Needed.", "git"), False),
            CheckResult(Check("origin remote on GitHub", "GitHub remote configured", "Needed.", "git"), False),
        ]

        actions = next_actions(results)

        self.assertIn("first commit", actions[0])
        self.assertIn("public GitHub repository", actions[1])

    def test_run_git_checks_reports_missing_identity_and_main_branch(self):
        def fake_runner(repo, args):
            outputs = {
                ("rev-parse", "--is-inside-work-tree"): (True, "true"),
                ("config", "--get", "user.name"): (False, ""),
                ("config", "--get", "user.email"): (False, ""),
                ("branch", "--show-current"): (True, "master"),
                ("rev-parse", "--verify", "HEAD"): (False, ""),
                ("remote", "get-url", "origin"): (False, ""),
            }
            return outputs[tuple(args)]

        results = run_git_checks(Path("."), runner=fake_runner)
        missing_labels = {result.check.label for result in results if not result.exists}

        self.assertIn("Git user.name configured", missing_labels)
        self.assertIn("Git user.email configured", missing_labels)
        self.assertIn("Main branch is named main", missing_labels)

    def test_next_actions_suggests_maintenance_when_complete(self):
        results = [CheckResult(Check("README.md", "README", "Needed."), True)]

        actions = next_actions(results)

        self.assertIn("docs/maintenance-backlog.md", actions[0])
        self.assertIn("docs/application-evidence-log.md", actions[2])


if __name__ == "__main__":
    unittest.main()
