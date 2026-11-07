# 01 · 打通 GitHub

> ✅ **全部完成（2026-11-07 17:00）**。不用再照着做下面的步骤了，这份文档改为**排查手册 + 日常动作清单**。
>
> **仓库地址**：https://github.com/DLZ66/data-analysis-journey

---

## 一、验收结果（已用 GitHub 公开接口核对）

| 项 | 实际结果 |
|---|---|
| 可见性 | **public**（不是私有，链接可以直接写进简历） |
| 默认分支 | `main` |
| 文件 | 7 个，含 `data/messy_sample.csv`；`.vscode/` 已被正确忽略 |
| 提交历史 | 2 个：`d0fbbd3` → `945aad7`，与本地完全一致 |
| 提交作者 | `DLZ66`，邮箱 `353659693+DLZ66@users.noreply.github.com` |
| 贡献归属 | ✅ GitHub 已识别为本人，绿色格子会亮（可能有几小时延迟） |
| 本地关联 | `origin` → 远程仓库，`main` 已设 upstream |
| 同步链路 | 已在「无代理的普通终端」下验证 `ls-remote` 正常 |

**真实邮箱没有出现在任何公开提交里。** 中途通过接口上传时曾短暂产生过带 QQ 邮箱的提交，已用强制推送覆盖掉，`main` 上不再有。

换台设备（手机浏览器）打开上面的链接，能看到 7 个文件，今天这一步就算彻底结束。

---

## 二、身份与配置（留档）

```
GitHub 账号 : DLZ66（ID 353659693，2026-11-07 注册）
git 用户名  : DLZ66
git 邮箱    : 353659693+DLZ66@users.noreply.github.com
凭据        : VS Code 授权后由 Windows 凭据管理器记住，不用重复登录
Git         : 2.55.0
Python 环境 : E:\miniconda3\envs\ds（Python 3.11.18）
编辑器      : E:\VSCode
```

> 建议在 GitHub → Settings → Emails 勾上
> `Keep my email addresses private` 和 `Block command line pushes that expose my email`。
> 前者让网页端也用隐私邮箱，后者能从源头拦住「误把真实邮箱推上去」。

**为什么邮箱重要**：GitHub 靠 commit 里的 email 判断这次提交算不算你的贡献。邮箱对不上 → 代码推上去了，贡献图却一片空白，计划里「绿色格子是学习日志」就落空了。

---

## 三、以后每天 / 每周的固定动作

**每天写完代码（30 秒）**

1. `Ctrl+Shift+G` 打开源代码管理
2. 消息框写一句人话，例如 `W1D3: 用函数批量读取 CSV 完成`
3. 点 **✓ Commit**（VS Code 会自动暂存）
4. 点 **Sync Changes**（上传）

**每周日晚上（含在 30 分钟整理时间里）**

- 更新 `README.md` 的进度表，把那一周 `⬜` 改成 `✅`
- 写 3 句周报，追加到 `周报.md`（第二周开始建）
- 提交并同步

等价的命令行写法（在「启动 ds 环境」窗口里）：

```bash
cd /d "E:\WorkBuddy\文档\阶段0_W1_启动包"
git add .
git commit -m "W1D3: 用函数批量读取 CSV 完成"
git push
```

> 提交消息写「今天会了什么」比写 `update` 有用得多。秋招时面试官翻的就是这段历史，
> 能看出是不是真的连续学了 30 个月。**别断周**，哪怕某天只做 30 分钟也提交一次。

**如果 Sync Changes 报网络错**：等半分钟重试一次；连续失败就看下面第五节的代理说明。

---

## 四、今天踩过的坑（以后遇到直接查这里）

| 现象 | 原因 | 正确做法 |
|---|---|---|
| 发布后仓库名变成 `DLZ66/--0_W1_---` | 输入框预填了中文文件夹名，GitHub 仓库名不支持中文 | 蓝色选中状态下**直接敲** `data-analysis-journey` 整段替换 |
| 建出来是私有仓库 | 下拉列表默认高亮第一行 `private repository` | **用鼠标点第二行 public**，别按回车 |
| `Publish to GitHub` 按钮消失、再也不出现 | 发布失败但本地已写入一条错误的 `origin` | 终端跑 `git remote remove origin`，按钮会回来 |
| `Sign in failed: network error` | VS Code 走了系统代理，而该代理访问 GitHub 超时 | 已在 VS Code 用户设置里关掉代理，见第五节 |
| `Failed to connect to github.com:443` / 21 秒超时 | DNS 解析到坏 IP，或环境里被注入了代理变量 | 见第五节；命令行可加 `git -c http.proxy= push` 强制直连 |
| 提交作者邮箱变成真实邮箱 | 绕过 git、用网页/API 直接上传文件时，GitHub 用账号主邮箱当作者 | 始终走 `git commit` + `git push`，作者才是配好的 noreply 地址 |

最后一条最值得记：**作品集仓库的历史要走 git，不要用网页上传文件**。否则提交会被拆成一条一个文件，作者信息也不受控制。

---

## 五、为了打通做过的环境改动（都可逆，留档备查）

| 改动 | 位置 | 怎么撤销 |
|---|---|---|
| 指定 `github.com` 的解析 IP | `C:\Windows\System32\drivers\etc\hosts` 追加一行 `<当前可用IP> github.com`（会轮换，见下方） | 删掉带 `# GitHub DNS fix 2026-11-07` 的两行；原文件备份在同目录 `hosts.bak.20261107` |
| 让 VS Code 绕过代理 | `%APPDATA%\Code\User\settings.json`，两项 `http.proxySupport: off`、`http.proxy: ""` | 删掉这两项即可 |
| 让中文文件名正常显示 | `git config --global core.quotepath false` | 不用撤，无害 |
| 默认分支名 | `git config --global init.defaultBranch main` | 不用撤，无害 |
| 工作区解释器 | `E:\WorkBuddy\文档\阶段0_W1_启动包\.vscode\settings.json` | 不用撤；该文件已被 `.gitignore` 排除 |

> **2026.11.07 记录**：当天 hosts 里的 IP 轮换过两次 ——
> `20.27.177.113` → 下午失效换 `20.205.243.166` → 晚上又失效，换回 `20.27.177.113`。
> 症状一律是 `git push` 报 `Failed to connect to github.com:443`，而 `api.github.com` 始终正常。
> **结论：写死 IP 只是临时手段，别指望一劳永逸。**

### IP 又失效了怎么办

**第一步：测哪个 IP 现在能用**（终端里整段粘贴，挑返回 200 且最快的）：

```bash
for ip in 20.27.177.113 20.205.243.166 140.82.121.4 140.82.112.3 140.82.114.4; do
  printf "%-18s " "$ip"
  curl -s -o /dev/null --noproxy '*' --resolve github.com:443:$ip -w "HTTP %{http_code}  %{time_total}s\n" --max-time 6 https://github.com
done
```

**第二步：用管理员 PowerShell 替换那一行**（把 `新IP` 换成第一步挑中的）：

```powershell
$h = "$env:windir\System32\drivers\etc\hosts"
(Get-Content $h -Raw) -replace '\d+\.\d+\.\d+\.\d+ github\.com', '新IP github.com' | Set-Content $h -Encoding ASCII
Clear-DnsClientCache
```

也可以**直接删掉 hosts 里那两行**恢复系统自动解析（DNS 有时自己会恢复），或者直接把报错发我。
**不要剪切 `E:\miniconda3` 或 `E:\VSCode` 文件夹** —— 路径写进了大量配置，移动后整个环境会失效。
>
> **不要剪切 `E:\miniconda3` 或 `E:\VSCode` 文件夹**，
> 这两处路径被写进了大量配置，移动后整个环境会失效。

---

## 六、命令速查（不用背，留着查）

| 命令 | 作用 |
|---|---|
| `git status` | 看现在改了什么 |
| `git log --oneline` | 看提交历史 |
| `git add .` | 暂存全部改动 |
| `git commit -m "消息"` | 提交 |
| `git push` | 上传 |
| `git pull` | 下载 |
| `git remote -v` | 看远程仓库地址 |
| `git -c http.proxy= push` | 绕过代理直连推送（网络异常时用） |

日常在 VS Code 里点按钮就够了，命令行只在排查时用。

---

## 七、备选方案 B：凭据失效时（PAT）

只在「换电脑 / 凭据被清掉 / VS Code 怎么都登不上」时才需要。

1. GitHub → 头像 → **Settings** → **Developer settings** →
   **Personal access tokens → Tokens (classic)** → **Generate new token (classic)**
2. Note 填 `my-laptop`，Expiration 选 `90 days`，**只勾 `repo`**
3. 点生成，**立刻复制**（只显示一次）
4. 弹出登录框时：用户名填 GitHub 用户名，**密码粘贴那串 token**（不是账号密码）
5. Windows 凭据管理器会记住，以后 `git push` 不用再输

> 三条铁律：**token 不要发给任何人、不要写进代码、不要提交到仓库**。
> 泄露了就回第 1 步 Revoke 掉重新生成。
