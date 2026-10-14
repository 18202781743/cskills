# 验证计划

本 skill 的接口依据为 2026-10-14 用户提供的请求录制、实际登录页与生态文档后台页面；没有公开头文件或服务端源码。验证只读取接口结构和非敏感状态值，不输出密码、token、Cookie、工号或原始响应。

| 项目 | 验证方式 | 结果 |
| --- | --- | --- |
| 登录入口参数优先从后台页面解析，回调必须等于本应用 `callbackdoc` | 抓取 `https://ecology.chinauos.com/identification/doc_admin/`，与内置参数逐字段比对；同站其他应用与外部域链接被忽略 | PASS |
| 页面解析失败或不可达时回退内置注册参数 | 单元测试 `test_login_endpoint_ignores_unrelated_login_links`、`test_login_endpoint_falls_back_without_admin_page` | PASS |
| 登录链路 GET /login → GET /captcha → POST /login → 跟随授权 → islogin → 保存 session → 复用校验 | 实际登录返回 `method=username-password-http`、`reusable_session_verified=true`，随后 `status` 复用成功 | PASS |
| 验证码自动识别：默认模型优先，结果非 4 位时用 beta 模型复核 | 单元测试 `test_captcha_session_and_image_are_private`；实测多次真实验证码识别 | PASS |
| 识别失败或验证码被拒时自动换图重试，不中断任务 | 单元测试 `test_login_auto_retries_with_new_captcha`、`test_login_auto_stops_after_attempts`、`test_login_auto_retries_when_recognition_fails` | PASS |
| 缺少 ddddocr 时不再换图重试，直接给出安装提示 | 单元测试 `test_login_auto_stops_without_ocr_dependency` | PASS |
| `login` 没有验证码参数，验证码与会话绑定不可提前传入 | 单元测试 `test_login_has_no_manual_captcha_option`；实际执行 `login --captcha` 被 argparse 拒绝 | PASS |
| 非交互终端不读 stdin、不阻塞；真人终端才提示手输 | 单元测试 `test_noninteractive_login_reports_failure_without_reading_stdin`、`test_interactive_path_is_output_before_waiting` | PASS |
| 账号密码 Fernet 加密 + 系统密钥环，缺组件或密钥环不可用不回退明文 | 单元测试 `test_missing_key_does_not_fall_back_to_plaintext`、`test_modified_ciphertext_is_rejected`；实际 configure/login 通过 | PASS |
| 凭据 0600、目录 0700，密钥或密码不写入状态文件与仓库 | 单元测试 `test_encrypted_credentials_have_private_permissions`、`test_complete_chain_saves_verified_session_not_password`；`.gitignore` 排除会话与验证码 | PASS |
| 会话失效时自动重新登录并重试一次，不直接终止任务 | 单元测试 `test_expired_session_is_renewed_and_request_retried`；实际把 `session.json` 的 usercode 置为无效后 `read` 自动重登并成功 | PASS |
| 仅服务端明确拒绝会话时重试，网络失败与业务错误不盲目重试 | 单元测试 `test_repeated_rejection_stops_after_one_renewal`、`test_business_error_with_live_session_is_not_retried`、`test_business_error_on_expired_session_triggers_relogin` | PASS |
| 业务状态非 200 时用 islogin 探活判断是否失效，探活失败不误判 | 单元测试 `test_probe_failure_is_not_treated_as_expiry` | PASS |
| 目录树、正文读取接口与 `references/workflow.md` 记录一致 | 实际 `read` 请求返回文档正文与后台链接，参数为 `id`、`status` | PASS |
| 更新/新建保留状态、写前二次读取、写后回读校验，失败不报成功 | 单元测试 `test_update_preserves_publication_and_metadata`、`test_no_write_on_conflict`、`test_failed_readback_is_not_success` | PASS |
| 上传回读 SHA256 校验，只接受本站资源地址 | 单元测试 `test_asset_upload_download_hash_and_host_validation` | PASS |
| `--dry-run` 不发请求、不加载会话 | 单元测试 `test_dry_run_does_not_load_session_or_network` | PASS |
| 脚本无本机硬编码路径，状态与配置走 XDG 目录，可在其他机器使用 | 检查脚本无 `/home`、用户名等本机路径；解释器与依赖要求写入 `SKILL.md` | PASS |
| 触发范围覆盖生态文档更新、UOSDN 文档上传与后台登录复用 | 对照 `SKILL.md` 的 `description` 与 `evals/evals.json` 场景 | PASS |

验证命令：

```bash
cd ecology-docs
python3 -m unittest discover -s tests -v
```

已知限制：验证码单次识别成功率约 50%，默认最多换 5 张重试；极端情况下仍需人工到真人终端补录。会话失效只在登录链路和文档请求被拒时触发重新登录，不主动探测过期时间。
