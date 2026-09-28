# 导出类型介绍

dde-app-services 提供 DConfig 配置管理能力，包括按应用标识和键名读取配置值、写入配置值、列出指定应用的所有配置项，以及配置资源管理能力。

## org.desktopspec.ConfigManager

### 定位

配置读写主接口，面向需要编程方式读取或修改 DConfig 配置项的调用者。

### 功能能力总结

提供以下能力：

- 按 appid 和 key 获取配置值
- 按 appid 和 key 设置配置值
- 按 appid 列出所有配置项

### 使用场景

需要在程序中读写应用配置项时。

## org.desktopspec.ConfigManager.Manager

### 定位

配置资源管理接口，面向需要管理配置资源的调用者。

### 功能能力总结

提供配置资源的管理能力。

### 使用场景

需要管理 DConfig 配置资源时。

## dde-dconfig

### 定位

命令行配置工具，面向需要在脚本或终端中读写 DConfig 配置项的调用者。

### 功能能力总结

提供以下能力：

- 按 appid 和 key 读取配置值（`get` 子命令）
- 按 appid 和 key 写入配置值（`set` 子命令）
- 按 appid 列出所有配置项（`list` 子命令）

### 使用场景

需要在脚本或命令行环境中批量读取或修改配置时。
