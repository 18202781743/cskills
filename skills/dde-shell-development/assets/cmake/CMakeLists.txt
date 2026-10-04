```cmake
ds_install_package(PACKAGE org.deepin.ds.example.applet)
```

```cmake
find_package(DDEShell REQUIRED)

add_library(ds-weather SHARED
    weatherapplet.h weatherapplet.cpp
)
target_link_libraries(ds-weather PRIVATE Dde::Shell)
ds_install_package(PACKAGE org.deepin.ds.weather TARGET ds-weather)
```cmake
ds_install_package(PACKAGE <plugin-id> TARGET <library-name>)
```

纯 QML 插件可不传 TARGET。内部自动处理 PREFIX/OUTPUT_NAME 设置和安装路径。

### ds_handle_package_translation

配置翻译：

```cmake
ds_handle_package_translation(PACKAGE <plugin-id>)
```

自动扫描 package/ 下 QML 文件和当前目录 C++ 文件，生成 23 种语言翻译并安装到正确路径。

### 依赖

```cmake
find_package(DDEShell REQUIRED)
target_link_libraries(my-plugin PRIVATE Dde::Shell)
```

### 构建

