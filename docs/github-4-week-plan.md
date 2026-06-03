# GitHub 入门到 Codex for OSS 申请的 4 周实战计划

这个计划假设你从零开始学习 GitHub，并且还没有公开开源仓库。目标不是“尽快提交申请”，而是先建立一个真实、可维护、能展示开源维护能力的项目。

## 第 1 周：GitHub 基础

目标：能独立完成仓库、提交、分支、Pull Request、Issue 的基础操作。

每天任务：

1. 注册或整理 GitHub 账号，完善头像、简介、公开邮箱或联系入口。
2. 学习仓库、commit、branch、remote、clone、push、pull 的含义。
3. 阅读 [`docs/commit-and-branch-guide.md`](commit-and-branch-guide.md)，学习 branch name 和 commit message。
4. 阅读 [`docs/github-auth-and-push-guide.md`](github-auth-and-push-guide.md)，理解 HTTPS、SSH 和 token 不进仓库的原则。
5. 在本地运行：

   ```powershell
   git status
   git add .
   git commit -m "Describe the change"
   git log --oneline
   ```

6. 在 GitHub 网页创建一个练习 issue。
7. 按 [`docs/github-labels.md`](github-labels.md) 创建基础 labels。
8. 新建分支，修改 README，通过 Pull Request 合并。

推荐实操：按 [`docs/first-pr-lab.md`](first-pr-lab.md) 完成第一次 issue -> PR -> CI -> merge。

验收方式：每完成一项，把证据链接或复盘写进 [`docs/github-skills-matrix.md`](github-skills-matrix.md)。

完成标准：

- 你知道 `git status` 什么时候该看。
- 你能解释 commit、branch、pull request 分别解决什么问题。
- 你能写出 3 个清楚的 commit messages 和 branch names。
- 你至少合并过 1 个自己的 PR。
- 你按 review checklist 检查过 1 个 PR。
- 你看过 1 次 GitHub Actions CI 的结果。
- 你至少给 1 个 issue 加过 `triaged` 和类型标签。

## 第 2 周：创建候选开源项目

目标：把这个仓库整理成一个可以公开展示的小型 OSS 项目。

项目默认方向：Codex OSS Readiness，一个帮助开源维护者检查申请准备度的小工具。

需要完成：

- README：说明项目用途、安装、运行、贡献方式。
- LICENSE：使用 MIT 许可证。
- CONTRIBUTING：说明如何提 issue、开 PR、跑测试。
- Issue templates：bug 和 feature request。
- Pull request template：要求说明变更和测试。
- Tests：至少覆盖核心检查逻辑。
- Repository settings：按 [`docs/repository-settings-checklist.md`](repository-settings-checklist.md) 设置 About、topics、Actions 和 releases。

完成标准：

- 仓库设为 public 后，陌生人能看懂项目并运行。
- `python -m unittest discover -s tests` 能通过。
- `python -m src.codex_oss_readiness --repo .` 能输出检查结果。
- GitHub Actions 失败时，你能按 [`docs/ci-debugging-lab.md`](ci-debugging-lab.md) 找到失败步骤。

## 第 3 周：模拟真实维护

目标：留下真实维护痕迹，而不是只有一次性提交。

推荐节奏：

- 创建 3 个 issue：
  - 改进 README 示例
  - 添加缺失文件检查
  - 改进申请文案模板
- 每个 issue 用一个分支和一个 PR 完成。
- 至少做一次 release，例如 `v0.1.0`。
- 按 [`docs/first-release-lab.md`](first-release-lab.md) 发布第一个 release。
- 写 release notes：说明新增了什么、如何运行、下一步计划。

完成标准：

- 有 3 个以上 issue。
- 有 3 个以上 PR，其中至少 2 个已合并。
- 有至少 1 个 release。
- commit message 简短清楚。

## 第 4 周：申请准备

目标：准备可以提交到 Codex for OSS 表单的信息，但只在仓库证据足够时提交。

需要准备：

- GitHub username。
- 公开仓库 URL。
- OpenAI organization ID。
- 500 字以内项目说明。
- 500 字以内 API credits 使用计划。
- 维护者身份说明。

申请前自查：

- 我是不是 main maintainer 或 core maintainer？
- 仓库是不是 public？
- `docs/github-skills-matrix.md` 里的最低申请前信号是否已经满足？
- README 是否说明项目价值和用户？
- 是否有 issue、PR、release 作为维护证据？
- API credits 使用计划是否具体、真实、不夸大？
