# 第一个 Pull Request 实验室

完成这个实验后，你就走过了一次真实开源维护闭环：issue -> branch -> commit -> pull request -> CI -> merge。

前提：

- 本仓库已经 push 到 GitHub public repository。
- `python -m src.codex_oss_readiness --repo . --missing-only` 不再提示 first commit 和 GitHub remote。

## 1. 创建 issue

在 GitHub 网页创建 issue：

Title:

```text
Improve README missing-only explanation
```

Body:

```text
The README shows the --missing-only command, but the explanation could be clearer for first-time GitHub users.

Acceptance criteria:
- Explain when to use --missing-only.
- Mention that it shows the highest-priority setup gaps.
- Keep the example Windows PowerShell friendly.
```

证据链接：

- Issue:

Add labels:

- `documentation`
- `good first issue`
- `triaged`

## 2. 创建本地分支

Branch naming guide: [`commit-and-branch-guide.md`](commit-and-branch-guide.md).

```powershell
git checkout -b docs/explain-missing-only
```

检查当前分支：

```powershell
git branch --show-current
```

## 3. 修改 README

只改一个小地方：在 README 的 `--missing-only` 示例下面增加 1-2 句说明。

这是第一次 PR，重点不是改很多，而是练习完整流程。

## 4. 运行检查

```powershell
python -m unittest discover -s tests
python -m src.codex_oss_readiness --repo .
```

记录结果：

- Tests:
- Readiness score:

## 5. 提交并推送分支

Commit message guide: [`commit-and-branch-guide.md`](commit-and-branch-guide.md).

```powershell
git status
git add README.md
git commit -m "Explain missing-only readiness output"
git push -u origin docs/explain-missing-only
```

## 6. 打开 Pull Request

在 GitHub 网页打开 PR：

Title:

```text
Explain missing-only readiness output
```

Body:

```text
## Summary

Clarifies when beginners should use --missing-only and how it helps focus on setup gaps.

## Testing

- python -m unittest discover -s tests
- python -m src.codex_oss_readiness --repo .
```

证据链接：

- Pull request:

## 7. 查看 CI

打开 PR 页面，查看 GitHub Actions 检查结果。

如果 CI 通过：

- 在追踪表里记录 PR 链接。
- 在 `docs/application-evidence-log.md` 里记录 issue、PR 和 CI 链接。
- 按 [`pr-review-guide.md`](pr-review-guide.md) 写一次简短 review note 或 merge note。
- 合并 PR。

如果 CI 失败：

- 打开失败日志。
- 找到失败命令。
- 按 [`ci-debugging-lab.md`](ci-debugging-lab.md) 记录失败原因和修复步骤。
- 在同一个分支修复后再次 push。

## 8. 合并并复盘

合并 PR 后，回到 `main`：

```powershell
git checkout main
git pull
```

写三句话：

1. 这个 PR 改了什么？
2. CI 帮我确认了什么？
3. 下一次 PR 我想练什么？
