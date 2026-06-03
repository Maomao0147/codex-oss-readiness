# GitHub 技能验收矩阵

这个矩阵用来判断你是否已经从“看过教程”进入“能自己完成真实维护流程”。每一项都尽量对应一个公开证据链接，方便后面整理 Codex for OSS 申请材料。

不要急着一次填满。先做真实操作，再补链接和复盘。

## 使用方式

1. 完成一次真实 GitHub 操作。
2. 把对应链接填到 Evidence link。
3. 用一句话写下你学会了什么。
4. 每周复盘时，把最重要的证据同步到 [`application-evidence-log.md`](application-evidence-log.md)。
5. 运行技能验收：

   ```powershell
   python -m src.codex_oss_readiness --repo . --skills-audit --missing-only
   ```

## 第 1 级：本地 Git 基础

| Skill | Acceptance evidence | Evidence link or note | Reflection |
| --- | --- | --- | --- |
| 查看仓库状态 | 能解释 `git status` 里的 staged、unstaged、untracked | Local status checked before first commit; files are currently untracked. | I learned that untracked files are new files Git can add to the first commit. |
| 配置提交身份 | 本仓库有正确的 `user.name` 和 `user.email` | Local repo uses `Maomao0147` and GitHub noreply email. | I learned that Git commit identity is configured separately from the GitHub plugin login. |
| 创建第一次提交 | `main` 分支有 first commit | Local first commit: `ce1efb8 Initialize Codex OSS readiness project`. | I learned that a commit saves the current project as a named point in history. |
| 阅读提交历史 | 能用 `git log --oneline` 找到最近 3 次提交 | Ran `git log --oneline -3` and found `ce1efb8`. | I learned that `git log` shows the commit message and short commit ID. |
| 写清楚 commit message | 至少 3 个 commit message 能说明原因和结果 | First message: `Initialize Codex OSS readiness project`. | I learned that a good commit message should say what changed, not just say "update". |

## 第 2 级：公开仓库基础

| Skill | Acceptance evidence | Evidence link or note | Reflection |
| --- | --- | --- | --- |
| 创建 public 仓库 | GitHub repository URL 可以无登录访问 | Public repo created: `https://github.com/Maomao0147/codex-oss-readiness`. | I learned that a public GitHub repository is the online home for the local project. |
| 添加 remote | `origin` 指向 GitHub 仓库 | Local `origin` points to `https://github.com/Maomao0147/codex-oss-readiness.git`. | I learned that a remote connects local commits to a GitHub repository. |
| 推送 main 分支 | GitHub 上能看到最新 README 和 docs | Pushed `main` to `origin/main`; GitHub shows `README.md`. | I learned that `git push` publishes local commits to GitHub. |
| 设置仓库 About | About、description、topics 清楚说明项目用途 |  |  |
| 检查公开隐私 | 没有提交 private notes、tokens、OpenAI organization ID | Scanned public files before push; private account fields remain blank or ignored. | I learned to check for secrets before making a repository public. |

## 第 3 级：Issue 和分支

| Skill | Acceptance evidence | Evidence link or note | Reflection |
| --- | --- | --- | --- |
| 创建 issue | 至少 1 个真实 issue 描述问题或改进 |  |  |
| 分诊 issue | issue 有类型标签和优先级标签 |  |  |
| 从 issue 创建分支 | 分支名能对应 issue 或维护任务 |  |  |
| 小步提交 | 一个分支只解决一个清楚问题 |  |  |
| 关闭已完成 issue | PR merge 后 issue 状态和说明清楚 |  |  |

## 第 4 级：Pull Request 和 Review

| Skill | Acceptance evidence | Evidence link or note | Reflection |
| --- | --- | --- | --- |
| 创建 PR | PR 描述包含变更、测试和关联 issue |  |  |
| 读 CI 结果 | 能找到 GitHub Actions 的通过或失败步骤 |  |  |
| 处理失败 CI | 至少记录 1 次失败原因和修复方式 |  |  |
| 写 review note | PR 里有 review、merge note 或自查说明 |  |  |
| 合并 PR | 至少 2 个 PR 已合并，历史清楚 |  |  |

## 第 5 级：Release 和申请准备

| Skill | Acceptance evidence | Evidence link or note | Reflection |
| --- | --- | --- | --- |
| 准备 release notes | release draft 说明新增内容、修复和升级方式 |  |  |
| 发布第一个 release | 有公开 `v0.1.0` 或后续版本链接 |  |  |
| 整理申请证据 | `application-evidence-log.md` 链接完整且类型正确 |  |  |
| 写 500 字项目说明 | 草稿真实、具体、没有夸大用户量 |  |  |
| 写 API credits 计划 | 计划覆盖 issue、PR、CI、release，并有人类审核 |  |  |

## 最低申请前信号

在考虑提交 Codex for OSS 申请前，建议至少满足：

- Public GitHub profile 和 public repository 都可以访问。
- 你是 main maintainer 或 core maintainer。
- 有 first commit、至少 3 个 issue、至少 2 个 merged PR、至少 1 个 passing CI run、至少 1 个 release。
- README、CONTRIBUTING、LICENSE、issue templates、PR template 都已经公开。
- `python -m src.codex_oss_readiness --repo . --application-audit --missing-only` 不再显示公开证据类 TODO。
