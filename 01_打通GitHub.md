# 01 · 打通 GitHub

> 目标：今天结束时，用手机浏览器打开自己的仓库，能看到这 6 个文件。
> 预计 20–30 分钟，其中大部分是在网页上点几下。

---

## 换个走法：不去网页建仓库

之前提过「建仓库时别勾 Add a README file」这个坑。现在换一条更短的路，**网页建仓库这一步整个跳过**：

用 VS Code 的 **Publish to GitHub**，它会从本地文件夹直接完成三件事：

```
① 在你的 GitHub 账号下创建远程仓库
② 自动把它设为本地仓库的 origin
③ 把第一次提交 push 上去
```

那个坑自然就不存在了。也不用配 SSH、不用生成 token、不用敲命令行。

---

## 已经替你做好的部分（核对用）

| 项 | 状态 |
|---|---|
| Git | 2.55.0，装在 `C:\Program Files\Git` |
| 凭据助手 | `manager`（Windows 凭据管理器，登录一次会记住） |
| 本地仓库 | 已 `git init`，默认分支 `main` |
| `.gitignore` | 已配好：忽略 `.vscode/`、`__pycache__`、大文件 |
| `README.md` | 已由模板转正，写好了项目简介和进度表 |
| 中文文件名 | 已设 `core.quotepath=false`，显示正常 |
| VS Code | 装在 `E:\VSCode`，Python / Jupyter 扩展已装 |

**还没做的**：git 的作者身份（`user.name` / `user.email`）和首次提交。
这两项需要你的 GitHub 账号信息，见第 2 步。

---

## 第 1 步：GitHub 账号（只能你自己做，约 5 分钟）

**已有账号** → 跳过，直接看第 2 步。

**没有账号** → 打开 `github.com` → Sign up：

1. 邮箱：用你常用的、能立刻收信的邮箱
2. 密码、用户名
3. 邮箱验证码
4. 一路跳过问卷和套餐选择（**免费版够用**，不要选 Copilot 试用）

⚠️ **用户名认真起一次，别用 `user12345` 这类**。它会永久出现在：

```
https://github.com/<你的用户名>/data-analysis-journey
```

这个链接 2028 年要写进简历，HR 会点开。建议：全小写英文、能看出是本人、不带随机数字。
想不出就用 `姓名拼音 + ds` / `姓名拼音 + materials` 这类组合。

---

## 第 2 步：告诉我两样东西（决定绿色格子会不会亮）

需要：**GitHub 用户名** + **账号邮箱**。

### 为什么邮箱很关键

GitHub 判断一次提交算不算你的贡献，靠的是 **commit 里记录的 email 是否在你账号的邮箱列表里**。

邮箱不匹配 → 代码确实推上去了，但**贡献图一片空白**，你计划里「绿色格子是学习日志」这条就落空了。而且这种问题事后要改历史，很麻烦。**第一次就配对。**

### 在哪查邮箱

GitHub 右上角头像 → **Settings** → 左侧 **Emails**。

- 如果没开「Keep my email addresses private」→ 用页面上显示的那个主邮箱
- 如果开了 → 页面上会有一串 `12345678+你的用户名@users.noreply.github.com`，用这串

> 建议顺便把「Keep my email addresses private」勾上。commit 邮箱是公开的，
> 勾上后 GitHub 会用 noreply 地址代替，避免真实邮箱被爬。

把这两样发给我，我会配好 `user.name` / `user.email` 并完成首次提交。

---

## 第 3 步：VS Code 登录 GitHub

1. 双击桌面 **Visual Studio Code**
2. **File → Open Folder** → 选 `E:\WorkBuddy\文档\阶段0_W1_启动包`
3. 如果弹出「Do you trust the authors of the files in this folder?」→ 点 **Yes, I trust**
4. 按 `Ctrl+Shift+G` 打开 **Source Control**（左侧第三个分支图标）
5. 按 `Ctrl+Shift+P` → 输入 `Publish to GitHub` → 回车

这时会**自动打开浏览器**，进入 GitHub 授权页：

- 页面标题类似 `Authorize Visual Studio Code`
- 点绿色的 **Authorize** 按钮
- 可能要输一次 GitHub 密码
- 浏览器提示「You may now close this window」→ 关掉标签页，回到 VS Code

右下角如果弹出账号提示，说明登录成功。凭据会被 Windows 记住，**以后不用再登录**。

> 如果浏览器没自动弹出：看 VS Code 右下角通知，里面有一个可复制的链接和验证码，
> 手动打开 `https://github.com/login/device` 输入验证码也行。

---

## 第 4 步：发布

按提示依次回答：

| 提示 | 填什么 |
|---|---|
| Repository name | `data-analysis-journey` |
| Public / Private | **Public**（作品集要给人看；Private 的贡献默认不对外显示） |
| Select files to include | 全勾（应该能看到 6 个文件） |

然后等几秒。VS Code 底部状态栏会转一下，完成后 **「Publish to GitHub」按钮变成「Sync Changes」**，就是成功了。

---

## 第 5 步：验证（今天的验收标准）

用**手机浏览器**打开（换设备才能确认真的上传到了网上，不是只在本机）：

```
https://github.com/<你的用户名>/data-analysis-journey
```

应该看到这些文件：

```
.gitignore
00_今天就开始.md
01_打通GitHub.md
README.md
data/messy_sample.csv
w1_参考答案.py
w1_我的作业.py
```

**不应该看到 `.vscode/`** —— 它被 `.gitignore` 挡住了，这是对的（个人编辑器设置不该公开）。

再点头像 → 个人主页，**今天的格子上应该有一个绿点**（有时延迟几小时，最多 24 小时）。

✅ 看到这两样，今天就结束了。

---

## 以后每天 / 每周的固定动作

**每天写完代码（30 秒）**：

1. `Ctrl+Shift+G` 打开源代码管理
2. 在消息框写一句人话，例如 `W1D3: 用函数批量读取 CSV 完成`
3. 点 **✓ Commit**（VS Code 会自动暂存）
4. 点 **Sync Changes**（上传）

**每周日晚上（含在 30 分钟整理时间里）**：

- 更新 `README.md` 的进度表，把那一周 `⬜` 改成 `✅`
- 写 3 句周报，追加到 `周报.md`（第二周开始建）
- 提交并同步

> 提交消息写「今天会了什么」比写 `update` 有用得多。秋招时面试官翻的是这段历史，
> 能看出你是不是真的连续学了 30 个月。

---

## 常见坑

| 现象 | 原因 | 处理 |
|---|---|---|
| 提示 `Author identity unknown` / 让填 name 和 email | git 身份没配 | 把用户名和邮箱发我，我配好再做首次提交 |
| 推送后贡献图没变绿 | commit 邮箱和 GitHub 账号邮箱不一致 | Settings → Emails 核对；已发生的提交要改历史，尽早发现 |
| 浏览器授权页打不开 / 一直转 | 国内访问 GitHub 偶发波动 | 刷新重试；或用设备码方式 `github.com/login/device` |
| `Publish to GitHub` 找不到 | 命令面板拼写、或没打开文件夹 | `Ctrl+Shift+P` → 输入 `Publish`，或确认已打开学习包文件夹 |
| 提示 `repository already exists` | 之前已在网页建过同名仓库 | 换个名字，或删掉网页那个空仓库再发布 |
| 文件列表里少了文件 | 被 `.gitignore` 挡了 | 正常，`.vscode/` 本就不该上传 |
| `failed to connect` / timeout | 网络 | 见下方备选方案 |

---

## 备选方案 B：VS Code 授权实在不通时（PAT）

这条路要敲几行命令，但更抗网络波动。

1. GitHub → 头像 → **Settings** → 左下 **Developer settings** →
   **Personal access tokens → Tokens (classic)** → **Generate new token (classic)**
2. Note 填 `my-laptop`，Expiration 选 `90 days`，**只勾 `repo`**
3. 点生成，**立刻复制**（这串只显示一次）
4. 在 GitHub 网页新建仓库，名字 `data-analysis-journey`，**README / .gitignore / license 三项全部不要勾**，创建后会看到一串命令，不用管
5. 在「启动 ds 环境」那个黑窗口里：

```bash
cd /d "E:\WorkBuddy\文档\阶段0_W1_启动包"
git remote add origin https://github.com/<用户名>/data-analysis-journey.git
git push -u origin main
```

6. 弹出登录框时：用户名填 GitHub 用户名，**密码粘贴那串 token**（不是账号密码）
7. Windows 凭据管理器会记住，以后 `git push` 不用再输

> 三条铁律：**token 不要发给任何人、不要写进代码、不要提交到仓库**。
> 泄露了就回第 1 步 Revoke 掉重新生成。

---

## 命令速查（不用背，留着查）

| 命令 | 作用 |
|---|---|
| `git status` | 看现在改了什么 |
| `git log --oneline` | 看提交历史 |
| `git add .` | 暂存全部改动 |
| `git commit -m "消息"` | 提交 |
| `git push` | 上传 |
| `git pull` | 下载 |
| `git remote -v` | 看远程仓库地址 |

日常在 VS Code 里点按钮就够了，命令行只在排查时用。
