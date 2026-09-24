```qml
import org.deepin.dcc 1.0

DccObject {
    name: "myplugin"           // 与 CMake PLUGIN_NAME 相同
    parentName: "root"         // 父模块 URL
    displayName: qsTr("My Plugin")
    icon: "myplugin_icon"
    weight: 100

    // 通过 DBus 条件控制模块显隐
    visible: false
    DccDBusInterface {
        property var available
        service: "com.example.Service"
        path: "/com/example"
        inter: "com.example.Service"
        connection: DccDBusInterface.SessionBus
        onAvailableChanged: root.visible = available > 0
    }
}
```

## {Name}Main.qml — 主页面
