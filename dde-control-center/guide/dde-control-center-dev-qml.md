# 导出类型介绍

dde-control-center 的 QML 模块 URI 为 `org.deepin.dcc`，导入版本为 `1.0`。该模块为 STATIC 模块，由控制中心运行时提供，使用方通过 `import org.deepin.dcc 1.0` 导入后可使用以下 QML 类型构建设置页面。

## org.deepin.dcc

### DccObject

#### 定位

控制中心的树形结构数据节点，可表示界面的一个菜单项或功能项。作为 QML 元素在插件 QML 文件中使用，通过 `parentName` 和 `weight` 属性构建多级层级结构。

#### 功能能力总结

- 构建控制中心设置页面的层级树结构，每个节点代表一个菜单项或功能页面，通过父子引用和权重值自动组织多级导航层次
- 提供节点标识与定位能力，每个节点拥有唯一名称标识，结合父节点名称组成 URL 路径，用于页面跳转、搜索定位以及全局可见性和可用性配置
- 管理节点的显示信息，包括显示名称、描述文本、图标和角标，为界面渲染提供统一的元数据来源
- 控制节点的可见性与可用性，区分开发者设置的本地状态和经控制中心全局配置后的实际生效状态，支持按节点控制是否参与搜索
- 定义页面的渲染方式，支持菜单项、编辑控件、整行控件、组合控件及用户自定义等多种页面类型，适配不同布局需求
- 配置背景渲染样式，支持自动适配、正常背景、悬浮效果、可点击交互、高亮选中、警告提示等多种视觉风格
- 管理子节点的动态增删与层级维护，支持通过嵌套声明或引用父项名称两种方式构建父子关系，自动维护当前选中状态
- 提供页面组件挂载能力，可将 QML 组件指定为节点的页面内容，并管理页面组件的父项归属
- 在节点激活、停用及子节点增删移动时发出相应通知，便于插件监听页面生命周期变化并执行自定义逻辑

#### 使用场景

在插件 QML 文件中定义设置页面的菜单项和功能项。`{Name}.qml` 文件中根对象为 `DccObject`，包含插件入口菜单的元数据信息。`{Name}Main.qml` 文件中根对象为 `DccObject`，通过嵌套子 `DccObject` 或使用 `parentName` 引用构建完整的设置页面层级结构。

### DccModel

#### 定位

`DccObject` 层级结构的树形数据模型，继承自 `QAbstractItemModel`，为控制中心界面提供导航数据的模型接口。

#### 功能能力总结

- 以树形结构管理 DccObject 层级关系，支持动态设置和切换根节点，自动维护父子索引映射
- 为视图层提供标准化的模型数据访问接口，支持按角色获取节点属性数据，并提供行数、列数和索引查询能力
- 自动监听 DccObject 树的增删移动变化并同步更新模型索引，保证视图与数据的一致性

#### 使用场景

控制中心内部使用 `DccModel` 包装 `DccObject` 树结构，为导航列表和搜索功能提供数据模型。第三方插件通常不需要直接使用 `DccModel`，控制中心通过 `DccApp.navModel()` 和 `DccApp.searchModel()` 提供已配置的模型实例。

### DccRepeater

#### 定位

基于模型的 `DccObject` 子节点批量生成器，继承自 `DccObject`，根据 `model` 和 `delegate` 自动创建多个子 `DccObject`。

#### 功能能力总结

- 根据数据模型批量生成 DccObject 子节点，支持以整数指定数量或以任意模型对象作为数据源，配合委托组件自动实例化每个子节点
- 在数据源变化时自动同步增删子节点，支持随时重置并重新生成全部子节点
- 提供已生成子节点的查询访问能力，并在子节点增删时发出通知，便于外部同步状态

#### 使用场景

在插件 QML 文件中需要根据动态数据批量创建设置项时，使用 `DccRepeater` 配合 `model` 和 `delegate` 生成多个 `DccObject` 子节点，避免手动逐个声明。

### DccDBusInterface

#### 定位

QML 中与 D-Bus 交互的组件，通过 `QML_NAMED_ELEMENT(DccDBusInterface)` 注册到 `org.deepin.dcc` 模块，支持在 QML 中监听 D-Bus 属性变化、信号和异步调用方法。

#### 功能能力总结

- 在 QML 中提供与 D-Bus 服务交互的能力，通过声明服务名、对象路径和接口名建立连接，支持会话总线和系统总线两种连接方式
- 自动将 D-Bus 属性映射为 QML 属性，属性变化时自动更新并在 QML 中发出对应信号，实现数据双向绑定
- 支持 QML 中直接监听 D-Bus 信号，通过约定命名规则自动关联信号处理函数
- 提供异步方法调用能力，通过回调函数处理返回结果和错误，避免阻塞 QML 线程
- 支持属性名前缀隔离，防止 D-Bus 属性名与 QML 保留字冲突；支持动态启用和禁用 D-Bus 连接

#### 使用场景

在插件 QML 文件中需要访问 D-Bus 服务时，将 `DccDBusInterface` 作为 `DccObject` 的子项声明，配置服务名、路径和接口名，通过 QML 属性绑定监听 D-Bus 属性变化，通过 `callWithCallback` 异步调用 D-Bus 方法。

### Repeater

#### 定位

控制中心定制的 `QQuickRepeater` 子类，通过 `QML_NAMED_ELEMENT(Repeater)` 注册到 `org.deepin.dcc` 模块，覆盖 Qt Quick 原生 `Repeater`，在创建子项时调整父项以适配控制中心布局。

#### 功能能力总结

- 在控制中心 QML 模块中替代 Qt Quick 原生 Repeater，批量生成 QML 控件子项
- 在子项创建时自动修正父项归属，确保生成的控件正确嵌入控制中心的布局体系

#### 使用场景

在插件 QML 文件中使用 `Repeater` 批量生成 QML 控件（非 `DccObject`）时，控制中心模块中的 `Repeater` 会自动替代 Qt Quick 原生 `Repeater`，无需额外配置。

### DccSettingsObject

#### 定位

封装标准设置页面结构的 `DccObject` 模板，在 QML 文件 `DccSettingsObject.qml` 中定义，预创建 `body` 和 `footer` 两个子 `DccObject`，并使用 `DccSettingsView` 作为页面组件。

#### 功能能力总结

- 提供标准设置页面布局模板，预置主内容区域和底部操作区域两个子节点，并自动使用 DccSettingsView 作为页面组件渲染分区布局
- 为主内容区域和底部操作区域分别提供可引用的 URL，插件通过 parentName 引用即可向对应区域添加子节点

#### 使用场景

插件需要标准设置页面布局（主内容区域加底部操作区域）时，使用 `DccSettingsObject` 作为根对象，通过 `bodyUrl` 和 `footerUrl` 向对应区域添加子 `DccObject`。

### DccTitleObject

#### 定位

包含标题和描述的分组标题节点，在 QML 文件 `DccTitleObject.qml` 中定义，继承自 `DccObject`，`pageType` 设置为 `Item`，使用 `DccLabel` 渲染标题和描述文本。

#### 功能能力总结

- 提供带标题和描述的分组标题节点，自动以较大深色字号渲染标题文本，以较小半透明字号渲染描述文本
- 自动设置左侧内边距使标题与内容区域对齐，作为 DccObject 子项声明后设置显示名称和描述即可显示

#### 使用场景

在设置页面中需要添加分组标题时，使用 `DccTitleObject` 作为 `DccObject` 的子项，设置 `displayName` 和 `description` 属性即可显示标题和描述。
