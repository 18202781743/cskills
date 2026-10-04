# Eval: 调试 DConfig 问题

## 任务

调试 deepin/UOS v25 上 DConfig 配置不生效的问题：
1. 检查配置文件路径
2. 检查 meta 文件格式
3. 检查 DBus 服务状态

## 期望输出

代码应：
1. 从 `dde-dconfig-daemon` 的 systemd `STATE_DIRECTORY` 确认缓存根目录；默认检查 `/var/lib/dde-dconfig-daemon/.config`
2. 区分当前路径与早期、过渡期路径，避免固定使用 `/var/lib/dde-daemon/config/`
3. 验证 meta.json 格式正确
4. 检查 dde-dconfig-daemon 服务运行状态
5. 排查思路遵循 DTK 分层架构（gui → widget/declarative → 应用层）
6. 未修改系统安装文件进行调试（应使用临时环境变量）

## 验证要点

- [ ] 从 `dde-dconfig-daemon` 的 systemd `STATE_DIRECTORY` 确认缓存根目录；默认检查 `/var/lib/dde-dconfig-daemon/.config`
- [ ] 区分当前路径与早期、过渡期路径，避免固定使用 `/var/lib/dde-daemon/config/`
- [ ] 验证 meta.json 格式正确
- [ ] 检查 dde-dconfig-daemon 服务运行状态

## 人工复核

- 排查步骤先确认运行版本和 daemon 实际配置，再判断缓存路径，不把历史路径当成所有版本的固定值。

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 排查思路遵循 DTK 分层架构（gui → widget/declarative → 应用层）
- [ ] 未修改系统安装文件进行调试（应使用临时环境变量）
