---
name: ecology-docs
description: 登录统信生态文档后台 ecology.chinauos.com，持久保存会话，查询目录和文章，上传 Markdown 新建或更新在线文档，上传图片和附件并回读验证。用户提到更新生态文档、上传 UOSDN 开发文档、保存文档后台内容、复用后台登录时使用。适用于生态文档后台，OA 工时和审批使用对应 OA 技能。
compatibility: Python 3.10+、requests；验证码自动识别建议安装 ddddocr，缺少时回退人工填写；加密凭据需系统已有 cryptography、PyGObject/libsecret 和可用 Secret Service 密钥环。必须能访问统信生态站点。
metadata:
  Categories: Application
---

# 生态在线文档

在本 skill 根目录运行命令。只使用两个 Python 脚本：

- `scripts/auth_session.py`：账号密码加密配置、验证码自动识别登录（识别失败回退人工填写）、会话保存与校验。
- `scripts/ecology_docs.py`：目录文章树、正文读取、附件上传、文档新建与更新，会话失效时自动重新登录。

HTTP 登录使用标准库，文档请求使用 requests；加密配置使用系统已有 cryptography、PyGObject/libsecret 和 Secret Service。
缺少依赖时报告缺项，不自动安装软件或回退到明文。接口细节见 [references/workflow.md](references/workflow.md)。

## 1. 配置与登录

首次配置（login 自动获取验证码并识别，识别失败才需要人工填写）：

```bash
python scripts/auth_session.py configure --username <用户名>
python scripts/auth_session.py login
```

configure 隐藏输入密码；自动化配置可加 `--password-stdin`，不把密码放在命令行参数或历史中。
账号密码加密保存到 `${XDG_CONFIG_HOME:-~/.config}/ecology-docs/credentials.enc`（0600），目录权限 0700。
解密密钥在系统密钥环，锁定时由用户解锁。会话、验证码、备份和记录在 `${XDG_STATE_HOME:-~/.local/state}/ecology-docs/`。
脚本必须用能访问系统密钥环的解释器运行（系统 python3，或在虚拟环境 pyvenv.cfg 中启用 `include-system-site-packages`）；否则报当前 Python 缺少 PyGObject/Secret。
认证脚本支持全局 `--config-dir`、`--state-dir`；文档脚本只需 `--state-dir`。这些参数放在子命令前。
登录入口（client_id、redirect_uri、scope）优先从后台页面解析，解析不到才用脚本内置兜底值；这些是公开的应用标识，不是密钥，换机器不需要改。
不输出密码、token，不将凭据、会话、验证码或原始请求录制加入日志、技能包或 Git。

login 先校验并复用已有会话。无有效会话时自动获取验证码并用 ddddocr 识别（默认模型无效时换 beta 模型复核），识别失败或验证码被拒就换新验证码重试，默认最多 5 张；成功即保存会话并打印 `method=username-password-http`。
全部尝试失败时：真人终端再获取一张新验证码、输出绝对 `captcha_image` 路径并等待输入；非交互 AI 终端不阻塞、不等待输入，直接报错并给出 `captcha_image` 路径，由用户到真人终端重试。
验证码与登录会话绑定，不能提前传入，所以 login 没有验证码参数。单独看验证码可用 `captcha` 子命令：识别成功给出 `status=captcha_recognized` 和验证码，失败给出 `status=human_input_required`、`captcha_recognition_error` 和图片路径。
识别由脚本完成，模型不需要视觉能力；只在人工兜底时向用户展示图片或可访问的路径。

认证后校验会话：

```bash
python scripts/auth_session.py status
```

已有会话时不要重复 login；需要重新认证时执行 `login --force`；只刷新图片可用 `captcha --open`。
自动识别可能出错，`login` 会自己换图重试；仍失败再请用户到真人终端重试；密码错误如实报告，不使用旧会话声称新登录成功。
成功后保存新会话，普通任务先 status 校验再复用；会话有效时不需要解密密码。
无人参与且会话已过期时先自动识别重试；识别失败再报告需要人工认证。
文档脚本在执行长任务时会话失效（HTTP 401/403/重定向，或业务状态非 200 且 islogin 校验失败）会自动重新登录并重试一次，不中断任务、不等待终端输入；自动重登失败才报错并提示执行 login。

## 2. 列出组织结构与读取

```bash
python scripts/ecology_docs.py list
python scripts/ecology_docs.py list --parent <目录ID>
python scripts/ecology_docs.py read --id <文章ID> --output /tmp/ecology-doc-before.json
```

list 不指定 parent 时列出完整目录与文章树；指定 parent 时只列出该目录及其全部后代。
结果包括 directory_count、document_count 和嵌套 items；节点 kind 是 directory 或 document，目录的 children 保留层级。
按 sort 排序。全量 list 各查询一次目录与全部文章；--parent 先定位子树，再按目录请求该子树的文章，避免下载无关正文。
响应条数不完整、目录过滤不匹配或目录循环时停止，不报告完整成功。
父目录不可见的目录/文章在全量结果中作为根项呈现，并保留原 parent，避免遗漏。

从用户 URL 取文章 id、目录 dirid；仅有标题时查询 list，唯一匹配后操作。多个同名结果需用户指定目标。
ID 为 24 位小写十六进制字符串；parent/dirid 是目录，id 是文章，不使用录制中的 ID 作为默认目标。
read --output 保存完整 JSON，正文在 info。树中不输出正文；需要时单独 read。

## 3. 上传附件与准备正文

```bash
python scripts/ecology_docs.py upload --file /path/screenshot.png
python scripts/ecology_docs.py upload --file /path/example.zip
```

下载回读验证 SHA256 后，用返回 URL 替换 Markdown 的本机图片/附件路径。
跨文章链接使用文章的 front_url。检查所有正文链接，不上传仍依赖本机相对路径的正文。
不自动转换 Word/HTML、重写链接或转存外部图片；先准备 UTF-8 Markdown。

## 4. 更新或新建

```bash
python scripts/ecology_docs.py update --id <文章ID> --file /path/article.md
python scripts/ecology_docs.py create --parent <目录ID> --title '文章标题' --file /path/article.md
```

更新保留原标题和当前发布状态；新建默认草稿 save。明确目标的保存请求即已授权，不重复询问是否保存。
用户要求发布时指定 `--status publish`；只有用户要求草稿或取消发布时才将已发布文章设为 `--status save`。
仅支持普通 document Markdown 文档，不处理案例、新闻或视频。

已审核线上正文时，用其 UTF-8 SHA256 作为 `update --expected-sha256 <hash>`，不是 JSON 文件或待上传正文的哈希。
脚本备份原文、写前再次读取检测变化、写后回读验证正文及属性。
服务端无已确认的原子条件更新接口，最后读取与 POST 之间仍有并发窗口。
网络失败或新建未返回 ID 时先查询现状，不自动重复写入。

## 5. 结果与验证

update/create/upload 的 `--dry-run` 仅本地校验和展示，不加载会话、不发请求，不能证明远端可用。
文档请求只在服务端明确拒绝（未处理）会话时才自动重新登录后重试一次；网络失败和业务错误不做自动重试，避免重复写入。
真实保存不得携带 dry-run。仅返回 `verified=true` 时报告写入完成。
报告文章 ID、前后台链接、document_status、正文 SHA256、备份位置和验证结果。
写后回读失败则报告“写入已尝试，尚未验证”，给出记录路径。

备份和结果在私有状态目录的 runs/，附件结果在 uploads/。
恢复时从 before.json 提取 info 到 Markdown，再按原 ID、标题、状态更新；未经用户要求不自动回滚。

```bash
python -m unittest discover -s tests -v
```

场景提示见 [evals/evals.json](evals/evals.json)。会话校验或读取成功不代表真实密码登录、上传、新建和更新均已验证。
