# org.deepin.dde.Face1 接口参考（兼容接口）

## 功能概述

`org.deepin.dde.Face1` 是旧版 `deepin-face` 独立组件提供的 D-Bus 接口（对象路径 `/org/deepin/dde/Face1`，System 总线），提供以下基础人脸识别功能：

- **人脸录入**：EnrollStart / EnrollStop
- **人脸验证**：VerifyStart / VerifyStop
- **人脸删除**：Delete
- **属性**：Claim（设备占用状态）、List（人脸列表）、CharaType（特征类型）
- **信号**：ErollStatus（录入状态）、VerifyStatus（验证状态）

该接口已被 `deepin-authentication` 统一认证服务中的 `org.deepin.dde.Authenticate1.Face` 接口取代，后者提供了更完整的人脸管理能力（包括重命名、批量删除、默认设备/服务设置、共享内存信息获取等）。新应用应使用 `org.deepin.dde.Authenticate1.Face` 接口。

---
