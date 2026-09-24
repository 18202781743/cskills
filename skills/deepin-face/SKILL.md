---
name: deepin-face
description: 提供系统级人脸录入、验证、列出、重命名、删除及默认设备与服务设置的 D-Bus 接口
Categories:
  - Settings
---

# deepin-face

deepin-face 是 DDE 的人脸识别组件，通过 System 总线提供系统级人脸录入、验证、列出、重命名、删除及默认设备与服务设置能力。其中录入、重命名、删除操作需要 polkit 提权。

## D-Bus 接口

### 人脸识别管理

提供人脸录入、验证、列出、重命名、删除及默认设备与服务设置能力，所有接口面向系统全局用户的人脸数据管理。

详见 [com.deepin.daemon.Authenticate.Face.md](references/dbus/com.deepin.daemon.Authenticate.Face.md)

### 兼容接口：org.deepin.dde.Face1

`org.deepin.dde.Face1` 是旧版 `deepin-face` 独立组件提供的 D-Bus 接口（对象路径 `/org/deepin/dde/Face1`，System 总线），提供人脸录入（EnrollStart/EnrollStop）、验证（VerifyStart/VerifyStop）、删除（Delete）及人脸列表查询（List 属性）等基础人脸识别功能。该接口已由 `deepin-authentication` 统一认证服务中的 `com.deepin.daemon.Authenticate.Face` 接口取代，后者提供了更完整的人脸管理能力（包括重命名、批量删除、默认设备/服务设置、共享内存信息获取等）。`org.deepin.dde.Face1` 仅作为兼容旧版接口保留，新应用应使用 `com.deepin.daemon.Authenticate.Face` 接口。
