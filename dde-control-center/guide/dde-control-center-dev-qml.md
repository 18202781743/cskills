# 导出类型介绍

dde-control-center 的 QML 模块 URI 为 `org.deepin.dcc`，导入版本为 `1.0`。该模块为 STATIC 模块，由控制中心运行时提供，使用方通过 `import org.deepin.dcc 1.0` 导入后可使用以下 QML 类型构建设置页面。

## org.deepin.dcc

### DccObject

#### 定位

控制中心的树形结构数据节点，可表示界面的一个菜单项或功能项。作为 QML 元素在插件 QML 文件中使用，通过 `parentName` 和 `weight` 属性构建多级层级结构。

#### 功能能力总结

- 设置节点标识：`name` 属性作为唯一标识，结合父项 `name` 组成 URL，用于定位跳转和配置隐藏、禁用
- 设置节点位置：`parentName` 属性指定父项 URL，`weight` 属性控制同级节点排列顺序，取值范围 0–4294967295
- 设置显示信息：`displayName` 设置显示名称，`description` 设置描述文本，`icon` 设置图标名称
- 控制可见性与可用性：`visible` 和 `enabled` 控制节点是否显示和可用，`visibleToApp` 和 `enabledToApp` 反映经控制中心配置后的实际可见和可用状态，`canSearch` 控制节点是否参与搜索
- 设置页面类型：`pageType` 属性指定页面渲染方式，包括 `EditorPage`（编辑控件，左侧显示名称和描述，右侧显示 `page` 组件）、`ItemPage`（整行控件）、`Menu`（菜单项，子页面为 `page`）、`MenuEditor`（菜单加编辑控件）、`Control`（页面中的控件，与其他类型组合使用）、`Editor`（`EditorPage` 与 `Control` 组合）、`Item`（`ItemPage` 与 `Control` 组合）、`UserType`（用户自定义类型，0x80 及以上）
- 设置背景样式：`backgroundType` 属性指定背景渲染方式，包括 `AutoBg`（自动，默认）、`Normal`（正常背景）、`Hover`（悬浮背景）、`Clickable`（可点击触发 `active` 信号）、`Highlight`（高亮）、`Warning`（红色）、`ClickStyle`（有悬浮背景并可点击）
- 设置页面内容：`page` 属性指定 `QQmlComponent` 作为节点的页面组件，`parentItem` 属性设置父 `QQuickItem`
- 管理子节点：`children` 属性返回子节点列表，`currentObject` 属性设置或返回当前选中的子节点，`data` 为默认属性，可直接在 `DccObject` 内部嵌套子对象
- 发出激活信号：`active` 信号在节点被激活时发出，`deactive()` 信号在节点被停用时发出
- 发出子项变化信号：`childAdded`、`childRemoved`、`childMoved`、`childrenChanged` 信号在子节点增删移动时发出
- 发出属性变化信号：各属性变化时分别发出对应的 changed 信号，包括 `nameChanged`、`parentNameChanged`、`weightChanged`、`displayNameChanged`、`descriptionChanged`、`iconChanged`、`iconSourceChanged`、`badgeChanged`、`visibleChanged`、`enabledChanged`、`visibleToAppChanged`、`enabledToAppChanged`、`canSearchChanged`、`backgroundTypeChanged`、`currentObjectChanged`、`pageTypeChanged`、`pageChanged`、`parentItemChanged`

#### 使用场景

在插件 QML 文件中定义设置页面的菜单项和功能项。`{Name}.qml` 文件中根对象为 `DccObject`，包含插件入口菜单的元数据信息。`{Name}Main.qml` 文件中根对象为 `DccObject`，通过嵌套子 `DccObject` 或使用 `parentName` 引用构建完整的设置页面层级结构。

### DccModel

#### 定位

`DccObject` 层级结构的树形数据模型，继承自 `QAbstractItemModel`，为控制中心界面提供导航数据的模型接口。

#### 功能能力总结

- 设置根节点：`root` 属性指定 `DccObject` 作为模型根节点
- 提供模型索引：`index` 返回指定位置的模型索引，`parent` 返回父索引
- 提供行数和列数：`rowCount` 和 `columnCount` 返回指定父索引下的行数和列数
- 提供数据：`data` 返回指定索引和角色对应的数据
- 获取节点对象：`getObject` 方法返回指定行的 `DccObject` 指针
- 获取节点索引：`index` 方法返回指定 `DccObject` 对应的模型索引
- 发出根节点变化信号：`rootChanged` 信号在根节点变更时发出

#### 使用场景

控制中心内部使用 `DccModel` 包装 `DccObject` 树结构，为导航列表和搜索功能提供数据模型。第三方插件通常不需要直接使用 `DccModel`，控制中心通过 `DccApp.navModel()` 和 `DccApp.searchModel()` 提供已配置的模型实例。

### DccRepeater

#### 定位

基于模型的 `DccObject` 子节点批量生成器，继承自 `DccObject`，根据 `model` 和 `delegate` 自动创建多个子 `DccObject`。

#### 功能能力总结

- 设置数据模型：`model` 属性指定数据源，支持整数（生成对应数量的对象）或模型对象
- 设置委托组件：`delegate` 属性指定 `QQmlComponent`，用于实例化每个子 `DccObject`
- 获取生成数量：`count` 属性返回已生成的子对象数量
- 重置模型：`resetModel()` 方法清除并重新生成所有子对象
- 获取指定对象：`objectAt` 方法返回指定索引处的 `DccObject` 指针
- 发出对象增删信号：`objAdded` 信号在添加子对象时发出，`objRemoved` 信号在移除子对象时发出
- 发出属性变化信号：`modelChanged`、`delegateChanged`、`countChanged` 信号在对应属性变化时发出

#### 使用场景

在插件 QML 文件中需要根据动态数据批量创建设置项时，使用 `DccRepeater` 配合 `model` 和 `delegate` 生成多个 `DccObject` 子节点，避免手动逐个声明。

### DccDBusInterface

#### 定位

QML 中与 D-Bus 交互的组件，通过 `QML_NAMED_ELEMENT(DccDBusInterface)` 注册到 `org.deepin.dcc` 模块，支持在 QML 中监听 D-Bus 属性变化、信号和异步调用方法。

#### 功能能力总结

- 设置 D-Bus 服务信息：`service` 属性指定服务名，`path` 属性指定对象路径，`inter` 属性（对应 `interface`）指定接口名
- 设置总线类型：`connection` 属性指定总线类型，可选 `SessionBus`（会话总线）或 `SystemBus`（系统总线）
- 设置属性前缀：`suffix` 属性为动态属性添加前缀，防止属性名与 QML 保留字冲突
- 控制启用状态：`enabled` 属性控制是否连接 D-Bus
- 异步调用方法：`callWithCallback` 方法异步调用 D-Bus 方法，通过 JS 回调函数处理返回结果和错误
- 监听 D-Bus 属性变化：在 QML 中声明与 D-Bus 属性同名的 `property`，属性变化时自动更新并发出对应信号
- 监听 D-Bus 信号：在 QML 中定义 `on<SignalName>` 函数关联 D-Bus 信号
- 发出属性变化信号：`serviceChanged`、`pathChanged`、`interfaceChanged`、`connectionChanged`、`suffixChanged`、`enabledChanged` 信号在对应属性变化时发出

#### 使用场景

在插件 QML 文件中需要访问 D-Bus 服务时，将 `DccDBusInterface` 作为 `DccObject` 的子项声明，配置服务名、路径和接口名，通过 QML 属性绑定监听 D-Bus 属性变化，通过 `callWithCallback` 异步调用 D-Bus 方法。

### Repeater

#### 定位

控制中心定制的 `QQuickRepeater` 子类，通过 `QML_NAMED_ELEMENT(Repeater)` 注册到 `org.deepin.dcc` 模块，覆盖 Qt Quick 原生 `Repeater`，在创建子项时调整父项以适配控制中心布局。

#### 功能能力总结

- 继承 `QQuickRepeater` 的全部功能，包括 `model`、`delegate`、`count` 属性以及 `itemAt` 方法
- 在子项创建时自动调整父项归属，使生成的子项正确嵌入控制中心的布局体系

#### 使用场景

在插件 QML 文件中使用 `Repeater` 批量生成 QML 控件（非 `DccObject`）时，控制中心模块中的 `Repeater` 会自动替代 Qt Quick 原生 `Repeater`，无需额外配置。

### DccSettingsObject

#### 定位

封装标准设置页面结构的 `DccObject` 模板，在 QML 文件 `DccSettingsObject.qml` 中定义，预创建 `body` 和 `footer` 两个子 `DccObject`，并使用 `DccSettingsView` 作为页面组件。

#### 功能能力总结

- 预创建 `body` 子节点：`name` 为 `body`，`pageType` 为 `Item`，用于承载主内容区域的子 `DccObject`
- 预创建 `footer` 子节点：`name` 为 `footer`，`pageType` 为 `Item`，用于承载底部操作区域的子 `DccObject`
- 提供 `bodyUrl` 只读属性：返回 `body` 子节点的完整 URL，用于通过 `parentName` 向 `body` 中添加子项
- 提供 `footerUrl` 只读属性：返回 `footer` 子节点的完整 URL，用于通过 `parentName` 向 `footer` 中添加子项
- 使用 `DccSettingsView` 作为 `page` 组件，自动渲染主内容区域和底部悬浮区域

#### 使用场景

插件需要标准设置页面布局（主内容区域加底部操作区域）时，使用 `DccSettingsObject` 作为根对象，通过 `bodyUrl` 和 `footerUrl` 向对应区域添加子 `DccObject`。

### DccTitleObject

#### 定位

包含标题和描述的分组标题节点，在 QML 文件 `DccTitleObject.qml` 中定义，继承自 `DccObject`，`pageType` 设置为 `Item`，使用 `DccLabel` 渲染标题和描述文本。

#### 功能能力总结

- 渲染 `displayName` 作为标题文本，使用较大字号和深色文本
- 渲染 `description` 作为描述文本，当描述不为空时显示，使用较小字号和半透明文本
- 自动设置左侧内边距为 14 像素，使标题文本与内容区域对齐

#### 使用场景

在设置页面中需要添加分组标题时，使用 `DccTitleObject` 作为 `DccObject` 的子项，设置 `displayName` 和 `description` 属性即可显示标题和描述。
