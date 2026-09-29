# 导出类型介绍

dde-polkit-agent 提供认证代理扩展接口，允许第三方扩展认证行为。扩展插件通过继承 `dpa::AgentExtension` 接口实现自定义认证逻辑，通过 `dpa::AgentExtensionProxy` 接口获取当前认证上下文信息（动作 ID、用户名、密码）。插件通过 Qt Plugin 机制加载，IID 为 `com.deepin.dpa.AgentExtension`。

## AgentExtension

### 定位

认证代理扩展接口，面向需要自定义认证行为的调用者。调用者通过继承此接口并实现全部纯虚方法，将自定义认证逻辑接入 dde-polkit-agent。插件类需要声明 `Q_PLUGIN_METADATA(IID AgentExtensionPluginIID)` 和 `Q_INTERFACES(dpa::AgentExtension)`，使 `QPluginLoader` 能够识别并实例化插件对象。`AgentExtensionPluginIID` 宏定义在 `agent-extension.h` 中，值为 `com.deepin.dpa.AgentExtension`。

### 功能能力总结

- 通过代理对象初始化扩展，获取认证上下文信息
- 释放扩展资源
- 声明感兴趣的认证动作 ID 列表
- 返回扩展的描述信息，在认证对话框中向用户展示潜在风险
- 返回扩展提供给用户选择的选项按钮组（`QButtonGroup*`）
- 执行扩展的实际认证逻辑

### 使用场景

需要为特定 Polkit 认证动作添加自定义认证逻辑时，继承 `AgentExtension` 实现扩展插件。例如：为某个提权操作添加额外的认证选项按钮供用户选择，并在用户确认后执行自定义的认证或验证流程。通过 `interestedActions()` 声明扩展关注的动作 ID，dde-polkit-agent 在遇到匹配的认证动作时调用 `options()` 获取选项按钮，并在用户确认后调用 `extendedDo()` 执行扩展逻辑。

## AgentExtensionProxy

### 定位

扩展代理接口，面向已注册的扩展插件，提供获取当前认证上下文信息的能力。在 `AgentExtension::initialize()` 中传入此接口的实例，插件后续通过该实例读取当前认证会话的相关信息。

### 功能能力总结

- 返回当前认证动作的 ID
- 返回认证用户名
- 返回用户输入的密码

### 使用场景

扩展插件需要获取当前认证动作 ID、用户名或密码时，通过 `initialize()` 传入的代理对象调用对应方法。例如：根据动作 ID 判断是否执行特定的认证流程，或使用用户名和密码完成自定义认证操作。