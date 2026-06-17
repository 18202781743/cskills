# Plugin Types

dde-shell supports three plugin types, each with different capabilities and use cases.

## Type Comparison

| Type | Base Class | Use Case | Can Contain Children |
|------|------------|----------|---------------------|
| Applet | `DApplet` | Basic widget | No |
| Containment | `DContainment` | Container for applets | Yes |
| Panel | `DPanel` | Top-level panel | Yes |

## Applet

The most common plugin type. A basic widget that can be embedded in a containment or panel.

### Use Cases
- Weather widget
- System monitor
- Clock
- Quick settings

### C++ Class
```cpp
class WeatherApplet : public DS_NAMESPACE::DApplet
{
    Q_OBJECT
    Q_PROPERTY(QString temperature READ temperature NOTIFY temperatureChanged)
public:
    explicit WeatherApplet(QObject *parent = nullptr);
    virtual bool init() override;
    
signals:
    void temperatureChanged();
    
private:
    QString m_temperature;
};
```

### Registration
```cpp
D_APPLET_CLASS(WeatherApplet)
```

### QML Root Element
```qml
AppletItem {
    // Your QML content
}
```

## Containment

A container that holds multiple applets. Used to group related plugins.

### Use Cases
- App drawer
- Widget container
- Settings group

### C++ Class
```cpp
class MyContainment : public DS_NAMESPACE::DContainment
{
    Q_OBJECT
public:
    explicit MyContainment(QObject *parent = nullptr);
    virtual bool load() override;
    virtual bool init() override;
};
```

### Registration
```cpp
D_APPLET_CLASS(MyContainment)
```

### QML Root Element
```qml
ContainmentItem {
    Repeater {
        model: Applet.appletItems
        Control {
            contentItem: model.data
        }
    }
}
```

## Panel

A top-level panel that serves as a container for dock applets. Inherits from DContainment.

### Use Cases
- Dock panel
- Top bar
- Side panel

### C++ Class
```cpp
class MyPanel : public DS_NAMESPACE::DPanel
{
    Q_OBJECT
public:
    explicit MyPanel(QObject *parent = nullptr);
    virtual bool load() override;
    virtual bool init() override;
};
```

### Registration
```cpp
D_APPLET_CLASS(MyPanel)
```

### QML Root Element
```qml
Window {
    visible: true
    DLayerShellWindow.anchors: DLayerShellWindow.AnchorBottom | DLayerShellWindow.AnchorLeft | DLayerShellWindow.AnchorRight
    
    Repeater {
        model: Applet.appletItems
        Control {
            contentItem: model.data
        }
    }
}
```

## Choosing the Right Type

### Use Applet when:
- Creating a single widget
- The plugin doesn't need to contain other plugins
- Embedding in an existing panel (like dock)

### Use Containment when:
- Need to group multiple applets
- Creating a custom container layout
- Managing dynamic child plugins

### Use Panel when:
- Creating a new top-level panel
- Need window management capabilities
- Serving as a dock-like container

## Inheritance Hierarchy

```
QObject
└── DApplet
    ├── DContainment
    │   └── DPanel
    └── [Your Applet]
```

## Examples in dde-shell

### Applet Examples
- `applet-example` - Simple QML applet
- `applet-widget-example` - QWidget applet
- `bridge-example` - Applet with cross-plugin access

### Containment Examples
- `containment-example` - Container with dynamic children

### Panel Examples
- `panel-example` - Top-level panel with DLayerShell
