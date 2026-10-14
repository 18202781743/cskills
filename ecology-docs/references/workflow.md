# 接口与认证流程

## 依据

依据用户提供的 2026-10-14 请求录制与实际登录页整理。录制仅包含已有 SSO 状态的授权跳转，
普通文档更新 multipart 请求，以及成功的生态会话校验。登录页确认了账号密码和人工验证码契约。
原始录制含凭据及正文，不随 skill 分发；不支持从录制文件导入会话。

## 认证与加密

认证、加密配置和会话文件均由 scripts/auth_session.py 管理。

1. 统一登录站点为 https://login-platform.uniontech.com。
2. 登录入口参数优先从后台页面里的登录链接解析：access_type=offline、response_type=code、scope=base,user:read,certify:edit。
3. client_id 是公开的应用标识（当前 f92a36f237733b6c2aef5423efbf2a045a5131b7），页面解析失败时才用内置兜底值。
4. redirect_uri=https://ecology.chinauos.com/adaptidentification/uos/develop/callbackdoc；页面里 state 由 JS 拼当前地址，脚本固定用生态后台地址，与浏览器行为一致。
5. GET /captcha 返回图片 data URL；保存对应 CookieJar 和唯一名称的图片，用 ddddocr 识别 4 位数字/字母验证码：默认模型的结果不是 4 位时再用 beta 模型复核，仍失败或验证码被拒就换新验证码重试，最多 5 张；全部失败才人工填写。
6. POST /login 保留上述 OAuth 查询参数，urlencoded 字段为 username、password、captcha。
7. code=0 时 msg 是授权跳转地址；-10002 表示验证码错误/过期，-10003 表示账号或密码错误。
8. 跟随授权与回调，仅允许两个固定 HTTPS 域。OAuth code 不打印或重放。
9. 回调后 POST /api/auth/islogin，JSON cookie 字段为 decodeURIComponent(document.cookie) 对应内容。
10. code=200，用户对象 code 为后续请求使用的 usercode；range 必须含文档管理。
11. 再校验 usercode 可复用后保存 session.json，后续 status/login 校验已有会话。
12. 文档请求被会话失效拒绝（HTTP 401/403/3xx，或业务状态非 200 且 islogin 试探失败）时，自动重新登录并重试一次；网络失败不自动重试。

账号密码使用 Fernet 加密到 ~/.config/ecology-docs/credentials.enc（0600），解密密钥在系统 Secret Service。
密钥环 schema=com.uniontech.ecology-docs，config_path 是配置目录的绝对路径；保持原配置路径才能查到对应密钥。
已加密配置及已保存会话可直接沿用。可用会话不需读取密码。没有已确认的 token 续期接口。

## 文档接口

所有文档 API 请求携带 usercode；HTTP 200 与 JSON 业务 code=200 均需通过。

| 操作 | 方法与路径 | 参数与响应 |
|---|---|---|
| 目录 | GET /api/doc | type=document,statusall=all；data 目录数组 |
| 全部文章 | GET /api/doc/doc | type=document,status=all；data 文章数组，count 为总数 |
| 指定文章 | GET /api/doc/doc | id,status=all；恰好一个匹配 _id 的对象 |
| 更新 | POST /api/doc/adddoc | multipart file,title,type=document,id,status；data 可为空 |
| 新建 | POST /api/doc/adddoc | multipart file,title,type=document,dirid,status；data 为新文章 ID |
| 图片/附件 | POST /adaptidentification/uos/develop/imgtobase64 | multipart file；data 为托管 URL |

list 将全部目录和文章按 parent 组织成树；--parent 先确定可见子树，
再通过 /api/doc/doc 的 parent 参数只获取子树各目录的直接文章，避免下载全站正文。
只输出文章元信息，不附带正文。count 与 data 长度不匹配时不报告完整列表。

更新与新建的 file 是 UTF-8 Markdown，MIME=text/markdown;charset=utf-8，不是 info 字符串或整份 JSON。
更新只发 id，不发 dirid，服务器保留目录与排序；新建发 dirid，不发 id。
状态 save 为未发布，publish 为已发布。更新默认沿用当前状态。
新建与资源接口依据页面脚本及实际资源结果整理，不能称为请求录制中均已实际成功验证。

写入顺序：读取、核对预期哈希、备份、再读检测变化、记录 write_attempted、POST、回读验证、记录 verified。
没有已确认的原子条件更新，双重读取仍有并发窗口。POST 不自动重试。
前台地址：https://uosdn.uniontech.com/#document3?dirid=<目录ID>&id=<文章ID>。
