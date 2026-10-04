```qml
import QtQuick
import QtQuick.Controls
import org.deepin.ds 1.0

AppletItem {
    implicitWidth: 100; implicitHeight: 100
    Text {
        anchors.centerIn: parent
        text: Applet.pluginId
    }
}
```
