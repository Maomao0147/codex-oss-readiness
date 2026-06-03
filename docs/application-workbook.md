# Codex for OSS 申请工作簿

这个文件用于准备申请材料。请只填写真实信息，不要夸大项目使用量或维护身份。

官方入口：

- Application form: <https://openai.com/form/codex-for-oss/>
- Program terms: <https://developers.openai.com/codex/codex-for-oss-terms>

截至 2026-06-02 的公开申请页信息，申请会要求姓、名、ChatGPT 邮箱、GitHub username、public repository、维护者角色、500 字以内项目资格说明、兴趣项、OpenAI Organization ID、500 字以内 API credits 使用计划和附加说明；页面还说明 selected maintainers may receive API credits for Codex usage in pull request review, maintainer automation, release workflows, or other core OSS work. 提交前请再次打开官方页面确认最新要求。

## 申请信息清单

- Last name:
- First name:
- Email associated with ChatGPT account:
- GitHub username:
- Public repository URL:
- OpenAI organization ID:
- Maintainer role: main maintainer / core maintainer
- ChatGPT account status:
- Country or region:
- Areas of interest:
- Additional information:

配套材料：

- [`github-profile-checklist.md`](github-profile-checklist.md)
- [`application-evidence-log.md`](application-evidence-log.md)
- [`final-application-audit.md`](final-application-audit.md)
- [`openai-org-id-guide.md`](openai-org-id-guide.md)
- [`privacy-and-public-repo.md`](privacy-and-public-repo.md)
- [`private-info.template.md`](private-info.template.md)
- [`codex-api-credits-plan.md`](codex-api-credits-plan.md)
- [`application-form-walkthrough.md`](application-form-walkthrough.md)

本地审查命令：

```powershell
python -m src.codex_oss_readiness --repo . --application-audit --missing-only
```

这个命令会检查必填字段、公开证据链接、项目说明草稿和 API credits 使用计划是否存在，并提醒它们是否超过 500 文字。最终字数限制以提交当天官方表单为准。

## 500 字以内项目说明草稿

可以按这个结构写：

1. 项目解决什么问题。
2. 谁会使用它。
3. 为什么这个项目适合作为开源项目。
4. 当前维护状态：issue、PR、release、文档、测试。
5. 未来 1-3 个月计划。

草稿：

```text
Codex OSS Readiness is a small open-source CLI and learning workspace that helps beginner maintainers prepare a GitHub repository for public review. It checks core OSS materials, guides issue/PR/CI/release practice, and collects application evidence. I maintain it as the primary maintainer and plan to improve repository health checks, bilingual docs, and release workflows.
```

## 500 字以内 API credits 使用计划草稿

可以按这个结构写：

1. Codex/API 会用于哪些维护任务。
2. 哪些任务不会完全自动化，需要人工 review。
3. 如何避免浪费额度。
4. 预期产出是什么。

详细计划见 [`codex-api-credits-plan.md`](codex-api-credits-plan.md)。申请表只需要短版，详细计划用于帮助你保持具体、真实、可审核。

草稿：

```text
I would use API credits for maintainer tasks: drafting issue triage summaries, suggesting PR review notes, generating test ideas, improving bilingual documentation, and drafting release notes from merged work. All AI output would be reviewed by me before posting, committing, or merging. The goal is faster, clearer maintenance without automated decisions.
```

## 申请前最终检查

- [ ] `python -m src.codex_oss_readiness --repo . --application-audit --missing-only` 没有剩余 TODO。
- [ ] 敏感信息只记录在 `private/application-info.private.md` 或其他不提交的位置。
- [ ] GitHub profile 是公开且可信的。
- [ ] 仓库是 public。
- [ ] README 解释了项目价值、安装方式、运行方式和贡献方式。
- [ ] LICENSE 存在。
- [ ] CONTRIBUTING 存在。
- [ ] 至少有几个真实 issue。
- [ ] 至少有几个 PR 或清晰 commit 历史。
- [ ] 至少有一个 release。
- [ ] `docs/application-evidence-log.md` 有真实链接。
- [ ] `docs/final-application-audit.md` 已完成。
- [ ] 申请说明和 credits 使用计划都真实、具体、不过度承诺。
