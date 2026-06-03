# 第一次提交并发布到 GitHub

这个文件从你当前状态继续：本地仓库已经创建，但还没有提交，也还没有连接到 GitHub 远程仓库。

## 1. 配置 Git 身份

先设置这个仓库的提交姓名和邮箱。建议使用你的 GitHub 用户名和 GitHub 提供的 no-reply 邮箱。

GitHub no-reply 邮箱可以在 GitHub 网页找到：

1. 打开 GitHub。
2. 进入 Settings。
3. 打开 Emails。
4. 找到类似 `12345678+YOUR_USERNAME@users.noreply.github.com` 的地址。

如果暂时找不到 no-reply 邮箱，也可以先用常用邮箱完成本地练习；正式公开维护项目前，再检查邮箱隐私设置。

```powershell
git config user.name "你的 GitHub 用户名"
git config user.email "你的 GitHub no-reply 邮箱"
```

查看是否设置成功：

```powershell
git config user.name
git config user.email
```

把默认分支改成 GitHub 常用的 `main`：

```powershell
git branch -M main
```

本地检查：

```powershell
python -m src.codex_oss_readiness --repo . --missing-only
```

## 2. 做第一次提交

提交前先阅读 [`commit-and-branch-guide.md`](commit-and-branch-guide.md)，理解为什么 commit message 要具体。

查看文件状态：

```powershell
git status
```

把文件加入暂存区：

```powershell
git add .
```

提交：

```powershell
git commit -m "Create Codex OSS readiness starter project"
```

查看历史：

```powershell
git log --oneline
```

## 3. 在 GitHub 创建公开仓库

在 GitHub 网页新建仓库：

- Repository name: `codex-oss-readiness`
- Visibility: Public
- 不要勾选自动创建 README、LICENSE、gitignore，因为本地已经有了。

本项目不要求安装 GitHub CLI。当前路线默认使用 GitHub 网页创建仓库，再用本地 Git 命令推送。

## 4. 连接远程仓库并推送

认证和 push 细节见 [`github-auth-and-push-guide.md`](github-auth-and-push-guide.md)。如果系统要求登录 GitHub，不要把 token、密码或账号敏感信息写进仓库文件。

把下面的 URL 换成你自己的 GitHub 用户名：

```powershell
git remote add origin https://github.com/YOUR_USERNAME/codex-oss-readiness.git
git branch -M main
git push -u origin main
```

## 5. 第一次 GitHub 练习

发布后，去 GitHub 网页完成：

- 创建一个 issue：`Improve README quick start`
- 新建一个分支：`docs/improve-readme`
- 修改 README 的 Quick start
- 提交并打开 Pull Request
- 合并 Pull Request
- 关闭或关联 issue

这组动作就是开源维护的最小闭环。

## 6. 回到本地检查

推送完成后，回到本地运行：

```powershell
python -m src.codex_oss_readiness --repo . --missing-only
```

如果输出 `All checklist items are present.`，说明第 1 周的本地发布准备已经完成，可以进入 issue、branch、pull request 练习。
