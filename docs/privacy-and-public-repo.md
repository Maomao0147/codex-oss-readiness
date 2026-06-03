# 公开仓库隐私保护指南

这个项目最终会发布成 public GitHub repository。公开仓库很适合展示维护证据，但不适合保存私人账号信息。

## 可以公开提交的内容

- GitHub username。
- Public repository URL。
- README、贡献指南、issue/PR/release 链接。
- 项目说明草稿和 API credits 使用计划。
- `OpenAI Organization ID: recorded privately` 这种占位说明。

## 不建议公开提交的内容

- ChatGPT 登录邮箱。
- 完整 OpenAI Organization ID。
- 真实姓名，如果你不想公开。
- 私人申请确认信息。
- token、API key、`.env` 文件。
- GitHub personal access token 或 SSH private key。
- 任何只想填进申请表、不想放到 GitHub 的内容。

## 推荐做法

1. 保持 `docs/application-workbook.md` public-safe。
2. 复制 `docs/private-info.template.md` 到 `private/application-info.private.md`。
3. 把敏感字段填在 `private/application-info.private.md`。
4. 提交前运行：

   ```powershell
   git status --short
   python -m src.codex_oss_readiness --repo . --missing-only
   ```

5. 确认没有 `private/`、`.env`、`*.private.md` 出现在待提交文件中。

## 如果误提交了敏感信息

不要继续 push。先停止操作，确认敏感信息类型，再决定是否需要更换密钥、删除提交或重写历史。

如果已经 push 到 public GitHub，单纯删除文件通常不够，因为历史记录仍然可能包含敏感内容。
