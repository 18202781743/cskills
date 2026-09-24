# deepin-face 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | deepin-face |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE 人脸识别服务，基于 SeetaFace 引擎提供人脸注册、验证等 DBus 接口 |
| 构建系统 | qmake（.pro 文件） |
| CMake target | 不适用（使用 qmake 构建） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/deepin-face.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6dbus6 (>= 6.x)
- libdtk6core
- SeetaFace 引擎库（SeetaFaceDetector600, SeetaFaceLandmarker600, SeetaFaceAntiSpoofingX600, SeetaFaceTracking600, SeetaFaceRecognizer610, SeetaQualityAssessor300, SeetaPoseEstimation600, SeetaAuthorize, tennis）

### 开发依赖
- Qt 6 Core, Gui, DBus, Multimedia, Concurrent (>= 6.x)
- DTK6 Core
- SeetaFace 开发库
- qmake

## 3. CMake 集成

不适用（项目使用 qmake 构建系统，无 CMake 配置）

### qmake 集成

项目使用 `deepin-face.pro` 进行构建：

```qmake
QT += gui dbus dtkcore multimedia concurrent
CONFIG += c++11 link_pkgconfig
TARGET = deepin-face
TEMPLATE = app
```

## 4. pkg-config

不适用（不导出 .pc 文件）

## 5. 命名空间

不适用（内部使用，未导出公共命名空间）

## 6. 关键公共类及功能描述

| 头文件 | 类 | 功能 |
|--------|-----|------|
| `dbusfaceservice.h` | `DbusFaceService` | DBus 人脸服务，提供人脸注册和验证接口 |
| `drivermanger.h` | `DriverManger` | SeetaFace 引擎驱动管理 |
| `modelmanger.h` | `ModelManger` | 人脸识别模型管理 |
| `workmodule.h` | `WorkModule` | 工作模块，处理注册/验证逻辑 |
| `charadatamanger.h` | `CharaDataManger` | 特征数据管理 |
| `definehead.h` | - | 常量和枚举定义 |

### DbusFaceService 关键方法

| 方法 | 说明 |
|------|------|
| `EnrollStart(QString chara, qint32 charaType, QString actionId)` | 开始人脸注册，返回文件描述符 |
| `EnrollStop(QString actionId)` | 停止人脸注册 |
| `VerifyStart(QStringList charas, QString actionId)` | 开始人脸验证，返回文件描述符 |
| `VerifyStop(QString actionId)` | 停止人脸验证 |
| `Delete(QString chara)` | 删除指定人脸特征 |

### DbusFaceService 关键属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `Claim` | `bool` | 是否占用设备 |
| `List` | `QStringList` | 已注册人脸列表 |
| `CharaType` | `qint32` | 特征类型 |

### DbusFaceService 关键信号

| 信号 | 说明 |
|------|------|
| `ErollStatus(QString, qint32, QString)` | 注册状态变化（注：`ErollStatus` 为源码中的原始命名，疑似 `EnrollStatus` 的历史 typo，文档忠实记录实际代码中的名称） |
| `VerifyStatus(QString, qint32, QString)` | 验证状态变化 |

## 7. QML 模块

不适用

## 8. DBus 接口

### org.deepin.dde.Face1

| 项目 | 内容 |
|------|------|
| 服务名 | `org.deepin.dde.Face1` |
| 对象路径 | `/org/deepin/dde/Face1` |
| 接口名 | `org.deepin.dde.Face1` |
| 服务类型 | 系统服务（system bus） |

#### 关键方法

| 方法 | 参数 | 说明 |
|------|------|------|
| `EnrollStart` | `string chara, int32 charaType, string actionId` | 开始人脸注册 |
| `EnrollStop` | `string actionId` | 停止人脸注册 |
| `VerifyStart` | `string[] charas, string actionId` | 开始人脸验证 |
| `VerifyStop` | `string actionId` | 停止人脸验证 |
| `Delete` | `string chara` | 删除人脸特征 |

#### 关键属性

| 属性 | 类型 | 访问 | 说明 |
|------|------|------|------|
| `Claim` | `b` | read | 设备是否被占用 |
| `List` | `as` | read | 已注册人脸列表 |
| `CharaType` | `i` | read | 特征类型 |

#### 关键信号

| 信号 | 参数 | 说明 |
|------|------|------|
| `ErollStatus` | `string, int32, string` | 注册状态通知 |
| `VerifyStatus` | `string, int32, string` | 验证状态通知 |

## 9. 插件开发

不适用
