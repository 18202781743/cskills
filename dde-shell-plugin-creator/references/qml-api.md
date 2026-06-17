# QML API Reference

## Imports

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import org.deepin.ds 1.0
import org.deepin.dtk 1.0       // For DTK components
```

## Root Elements

### AppletItem

Root element for applet plugins. Provides access to the applet instance.

**Properties**:
- `Applet.id` - Plugin instance ID
- `Applet.pluginId` - Plugin ID
- `Applet.rootObject` - The QML root object

**Example**:
```qml
AppletItem {
    implicitWidth: 100
    implicitHeight: 100
    
    Rectangle {
        anchors.fill: parent
        color: "blue"
        
        Text {
            anchors.centerIn: parent
            text: "Plugin: " + Applet.pluginId
        }
    }
}
```

### ContainmentItem

Root element for containment plugins.

**Properties**:
- `Applet.appletItems` - Model of child applet items

**Example**:
```qml
ContainmentItem {
    Repeater {
        model: Applet.appletItems
        Control {
            anchors.fill: parent
            contentItem: model.data
        }
    }
}
```

## UI Components

### DciIcon

DTK icon component.

**Properties**:
- `name` - Icon name
- `sourceSize` - Icon size

**Example**:
```qml
DciIcon {
    name: "deepin-music"
    sourceSize: Qt.size(36, 36)
}
```

## Global Objects

### DS

Global object for accessing dde-shell services.

**Methods**:
- `DS.applet(pluginId)` - Get applet by plugin ID

**Example**:
```qml
// Access another applet
var weather = DS.applet("org.deepin.ds.weather")
if (weather) {
    console.log(weather.rootObject.temperature)
}
```

### Applet

Attached property providing access to the current applet.

**Properties**:
- `Applet.id` - Plugin instance ID
- `Applet.pluginId` - Plugin ID from metadata
- `Applet.rootObject` - The QML root object
- `Applet.appletItems` - Model of child applets (for containment)

**Example**:
```qml
AppletItem {
    Text {
        text: "Plugin ID: " + Applet.pluginId
    }
}
```

## Best Practices

1. **Use AppletItem as root** for applet plugins
2. **Set implicitWidth/implicitHeight** for proper sizing
3. **Use DS.applet()** for cross-plugin access in QML
4. **Import org.deepin.ds 1.0** for dde-shell QML types
5. **Import org.deepin.dtk 1.0** for DTK components
