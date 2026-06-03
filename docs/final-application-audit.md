# Codex for OSS 最终申请 Audit

提交申请前，用这个文件做最后检查。目标是确认“材料真实、仓库公开、维护证据足够、计划具体”。

## 1. 官方页面复查

- [ ] Run `python -m src.codex_oss_readiness --repo . --application-audit --missing-only`.
- [ ] 打开申请表确认字段和说明仍然一致：<https://openai.com/form/codex-for-oss/>
- [ ] 打开项目条款确认资格要求：<https://developers.openai.com/codex/codex-for-oss-terms>
- [ ] 确认自己有有效 ChatGPT 账号。
- [ ] 确认 OpenAI Organization ID 填写正确。

## 2. GitHub 公开证据

- [ ] GitHub profile 是公开、可信、可识别的。
- [ ] 仓库是 public。
- [ ] 仓库 URL 可以无登录访问。
- [ ] 你是 main maintainer 或 core maintainer。
- [ ] Evidence log 记录了仓库 URL、维护者身份、权限证据和首个公开 commit URL。
- [ ] README、LICENSE、CONTRIBUTING、issue templates、PR template 都存在。
- [ ] 有 GitHub Actions CI 或其他可见检查。
- [ ] 有 release 或 release draft。

## 3. 最低建议维护记录

申请前建议至少完成这些证据：

- [ ] 3 个真实 issue。
- [ ] 2 个已合并 pull request。
- [ ] 至少 1 条 PR review note 或清晰 merge note。
- [ ] 1 次通过的 CI run。
- [ ] 1 个 public release。
- [ ] 1 份清晰的 application evidence log。
- [ ] Evidence log 里的 Permission evidence 是 `owner`、`admin`、`write access` 或 `maintain access`。
- [ ] Evidence log 里的 First public commit 是 GitHub commit URL。
- [ ] Evidence log 里的 issue、PR、CI、release 链接类型正确。

如果这些还没有完成，建议先继续维护，不急着提交申请。

## 4. 项目说明审查

- [ ] 本地 application audit 已检查项目说明草稿。
- [ ] 不超过 500 字。
- [ ] 说明项目解决的问题。
- [ ] 说明谁会使用它。
- [ ] 说明为什么它适合作为 OSS 项目。
- [ ] 引用真实维护状态，不夸大使用量。
- [ ] 说明未来 1-3 个月计划。

## 5. API Credits 使用计划审查

- [ ] 本地 application audit 已检查 API credits 使用计划草稿。
- [ ] `docs/codex-api-credits-plan.md` 说明了 issue triage、PR review、CI debugging、release workflow 和人工审核边界。
- [ ] 不超过 500 字。
- [ ] 说明 credits 会用于 PR review、issue triage、release workflow、文档维护或其他核心 OSS 工作。
- [ ] 明确所有 AI 建议都由维护者审核。
- [ ] 不承诺无人监督自动合并或自动决策。
- [ ] 说明预期产出和节省的维护时间。

## 6. 最终提交记录

- Application submitted date:
- Application form URL:
- Repository URL:
- Notes:
