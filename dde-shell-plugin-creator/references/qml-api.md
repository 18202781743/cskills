# QML API Reference

## Imports

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import org.deepin.ds 1.0
import org.deepin.ds.dock 1.0  // For dock-specific APIs
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

## Dock APIs

### Panel

Attached property providing panel information.

**Properties**:
- `Panel.position` - Panel position (0=bottom, 1=left, 2=top, 3=right)
- `Panel.rootObject` - Panel's root QML object
- `Panel.rootObject.dockSize` - Dock height/width
- `Panel.rootObject.dockItemMaxSize` - Maximum item size

**Example**:
```qml
AppletItem {
    property bool useColumnLayout: Panel.position % 2
    implicitWidth: useColumnLayout ? Panel.rootObject.dockSize : Panel.rootObject.dockItemMaxSize * 0.8
    implicitHeight: useColumnLayout ? Panel.rootObject.dockItemMaxSize * 0.8 : Panel.rootObject.dockSize
}
```

### Dock

Dock-specific utilities.

**Properties**:
- `Dock.MAX_DOCK_TASKMANAGER_ICON_SIZE` - Maximum icon size

**Example**:
```qml
DciIcon {
    name: "deepin-launcher"
    sourceSize: Qt.size(Dock.MAX_DOCK_TASKMANAGER_ICON_SIZE, Dock.MAX_DOCK_TASKMANAGER_ICON_SIZE)
}
```

### DockPanelPositioner

Position helper for popups and tooltips.

**Properties**:
- `DockPanelPositioner.x` - X position
- `DockPanelPositioner.y` - Y position
- `DockPanelPositioner.bounding` - Bounding rectangle

**Example**:
```qml
PanelPopup {
    popupX: DockPanelPositioner.x
    popupY: DockPanelPositioner.y
}
```

## UI Components

### PanelPopup

Popup window anchored to the dock panel.

**Properties**:
- `width` - Popup width
- `height` - Popup height
- `popupX` - X position
- `popupY` - Y position
- `popupVisible` - Visibility state

**Methods**:
- `open()` - Show popup
- `close()` - Hide popup

**Example**:
```qml
PanelPopup {
    id: popup
    width: 400
    height: 300
    popupX: DockPanelPositioner.x
    popupY: DockPanelPositioner.y
    
    contentItem: Rectangle {
        color: "white"
        Text { text: "Popup content" }
    }
}
```

### PanelToolTip

Tooltip anchored to the dock panel.

**Properties**:
- `text` - Tooltip text
- `toolTipX` - X position
- `toolTipY` - Y position

**Methods**:
- `open()` - Show tooltip
- `close()` - Hide tooltip

**Example**:
```qml
PanelToolTip {
    id: toolTip
    text: "My Plugin"
    toolTipX: DockPanelPositioner.x
    toolTipY: DockPanelPositioner.y
}
```

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

## Signals

### Panel Signals

- `Panel.leftEdgeClicked(minOrder)` - Emitted when left edge is clicked
- `Panel.dockCenterPartPosChanged()` - Emitted when dock center position changes
- `Panel.viewDeactivated()` - Emitted when view is deactivated

**Example**:
```qml
Connections {
    target: Panel
    function onLeftEdgeClicked(minOrder) {
        if (dockOrder === minOrder) {
            togglePopup()
        }
    }
}
```

## Best Practices

1. **Use AppletItem as root** for applet plugins
2. **Set implicitWidth/implicitHeight** for proper sizing
3. **Use Panel.position** for layout decisions
4. **Use DockPanelPositioner** for popup positioning
5. **Connect to Panel signals** for dock interactions
6. **Use DS.applet()** for cross-plugin access in QML
