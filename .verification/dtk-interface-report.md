# DTK 二次开发接口验证报告

验证日期：2026-10-07。范围：`skills/dtk/interface` 的六份文档及 `skills/dtk/SKILL.md` 开发接口入口。

## 源码基准

源码目录为 `~/repo/` 下的四个项目。逐条声明来源记录在
[dtk-interface-manifest.json](dtk-interface-manifest.json)。以下提交版本对应本次头文件、QML 文件和导出清单；
dtkcore 的未跟踪 guide/、dtkgui 的 README.zh_CN.md 本地修改及未跟踪 guide/ 未作为接口依据，也未修改。

| 项目 | 源码提交 |
|------|----------|
| dtkcore | e362b7d1b14c170668e8b7cfa51bd2b773c18fb1 |
| dtkgui | 166be36c43fb88df2aa27aaca7b31c56d2b2590e |
| dtkwidget | a1c52a84643736f968a8fefa7dc5f4ced3c0e1a1 |
| dtkdeclarative | c82227ab413616a0ecdfcb773e7fc41db839996b |

## 接口清单结果

每项保留定位、功能能力总结和使用场景。清单覆盖公开类型定义及 QML 具名导出，
包括兼容类型、嵌套公开结构和模板；Qt 控件别名在使用方式中说明，`dwidgetutil.h` 自由函数单列。
枚举保留在所属类型的能力说明中，内部助手和私有嵌套类型不作为开发接口推荐。

| 文档 | 原有条目 | 当前条目 | 声明及覆盖检查 | 能力源码对照 |
|------|----------|----------|----------------|--------------|
| dtkcore-dev.md | 45 | 59 | PASS | PASS |
| dtkgui-dev.md | 25 | 26 | PASS | PASS |
| dtkwidget-dev.md | 108 | 177 | PASS | PASS |
| dtkdeclarative-dev.md | 9 | 9 | PASS | PASS |
| org.deepin.dtk.md | 102 | 141 | PASS | PASS |
| org.deepin.dtk.settings.md | 9 | 11 | PASS | PASS |
| 合计 | 298 | 423 | FAIL 0，NOT FOUND 0 | 源码描述一致 |

## 重点修正的源码依据

下列路径相对源码根目录 `~/repo`；能力对照包含公开成员、继承关系、实现和安装条件，
不把源码中的 TODO 当成已经废弃或已经实现的功能。

| 验证项 | 依据 | 结果 |
|--------|------|------|
| 布局、展开组、页面栈、模型和标题栏工具的遗漏 | dtkwidget/include/widgets/ 对应公开头文件，详见逐条清单 | PASS |
| 打印机、预览、颜色选择及 12 类打印设置结构 | dtkwidget/include/widgets/dprintpreviewwidget.h、dprintpickcolorwidget.h、dprintpreviewsettinginfo.h | PASS |
| DSizeModeHelper、DGraphicsGlowEffect、工具自由函数的实际名称 | dtkwidget/include/util/dsizemode.h、dtkwidget/include/widgets/dgraphicsgloweffect.h、dtkwidget/include/util/dwidgetutil.h | PASS |
| DFloatingButton 的 DIconButton 继承，DCrumbEdit 的标签编辑用途 | dtkwidget/include/widgets/dfloatingbutton.h、dcrumbedit.h | PASS |
| 窗口按钮需要连接动作，打印和动画仅描述实际能力 | dtkwidget/include/widgets/dwindow*button.h 及对应实现、动画和打印公开头文件 | PASS |
| DFontManager 管理字号，拖拽源与接收方的角色 | dtkgui/include/kernel/dfontmanager.h、dtkgui/include/util/dfiledrag*.h 及对应实现 | PASS |
| 当前公开 DPlatformHandle 与 DPlatformTheme 不因未来 TODO 被误标废弃 | dtkgui/include/kernel/dplatformhandle.h、dplatformtheme.h | PASS |
| 配置后端、路径范围、结果模板和旧版异步类型 | dtkcore/include/global/dconfig.h、dconfigfile.h、include/filesystem/dcap*.h、include/base/dexpected.h、include/util/dasync.h、src/util/util.cmake | PASS |
| DSecureString 不保证同时擦除普通 QString 副本 | dtkcore/include/global/dsecurestring.h、src/dsecurestring.cpp、include/util/dutil.h | PASS |
| 加载器禁止默认构造、主组件与预加载接口、creatApplication 拼写 | dtkdeclarative/src/dapploader.h、dqmlappmainwindowinterface.h、dqmlapppreloadinterface.h | PASS |
| 背景采样、视口与窗口附加属性 | dtkdeclarative/src/dquickblitframebuffer.h、dquickitemviewport.h、dquickwindow.h 及对应实现 | PASS |
| DTK6 QML 文件、具名 C++ 类型、外部类型和运行时注册无遗漏 | dtkdeclarative/qt6/src/qml.cmake、src/**/*.h、qt6/src/dquickextendregister_p.h、qmlplugin/qmlplugin_plugin.cpp | PASS |
| Qt5/Qt6 QML 注册差异，ButtonPanel 为 private，WindowQuitFullButton 未注册 | dtkdeclarative/qmlplugin/qmlplugin_plugin.cpp、qt6/src/qml.cmake | PASS |
| DWindow、ColorSelector、MessageManager 为附加入口，AppLoader 为场景项 | dtkdeclarative/src/dquickwindow.h、src/private/dquickcontrolpalette_p.h、dmessagemanager_p.h、dquickapploaderitem_p.h | PASS |
| 设置模块的 8 个 QML 类型和 3 个模型，Style 不属于设置模块 | dtkdeclarative/qt6/src/qml/settings/CMakeLists.txt、src/private/dsettingscontainer_p.h、qmlplugin/qmlplugin_plugin.cpp | PASS |
| QML 插件与 Chameleon 风格包区分 | dtkdeclarative/debian/libdtk6declarative.install、libdtkdeclarative5.install 及 Chameleon 安装清单 | PASS |
| skill 入口与相对文件链接 | 六份文档及 skills/dtk/SKILL.md | PASS |

## 可重复验证与边界

执行 `python .verification/verify-dtk-interface.py --source-root ~/repo`：423 条声明来源存在，
公开头文件类型覆盖、QML 导出覆盖、三段结构和相对文件链接 PASS，FAIL 0，NOT FOUND 0。
该脚本不能证明能力说明的语义或控件运行正确；表中的能力源码对照来自逐项阅读和修正。
执行 `git diff --check` 通过。

本机可用 Qt6 工具，但没有 DTK 的 pkg-config 开发模块。本次没有新增可执行示例，
未执行 DTK 工程编译、完整 QML 实例化或交互验证；原有集成片段按源码 CMake 导出和 Debian 安装清单核对，
不标记为编译运行 PASS。

两项导出接口有源码实现限制，已经直接写入文档：`ArrowShapePopupWindow` 引用未定义的
`ArrowShapeContainer` 和 `loader`；`StyledArrowShapeWindow` 使用未定义且未注册的
`ArrowShapeWindow` 根类型。对应条目 PASS 表示文档准确披露现状，不表示这些控件可以直接运行。

通用 skill-creator 的 `quick_validate.py` 因原有 `Categories` 字段返回非零；仓库采用该元数据格式，
本次保持原格式。已另行解析 YAML 并检查必需的 name、description 和文档路由，未把通用验证器标为 PASS。
