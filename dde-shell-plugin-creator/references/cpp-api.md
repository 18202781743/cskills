# C++ API Reference

## Namespaces

All dde-shell classes are in the `ds` namespace:

```cpp
DS_USE_NAMESPACE  // Using directive
DS_NAMESPACE::DApplet  // Fully qualified
```

## Core Classes

### DApplet

Base class for all plugins.

**Header**: `applet.h`

**Properties**:
- `id` (QString, read-only) - Unique instance ID
- `pluginId` (QString, read-only) - Plugin ID from metadata
- `parent` (DApplet*, read-only) - Parent applet
- `rootObject` (QObject*, notify) - QML root object

**Methods**:
- `virtual bool load()` - Load the plugin
- `virtual bool init()` - Initialize the plugin
- `DPluginMetaData pluginMetaData()` - Get plugin metadata
- `DAppletData appletData()` - Get applet data
- `void setAppletData(const DAppletData &data)` - Set applet data
- `void setRootObject(QObject *root)` - Set QML root object

**Signals**:
- `rootObjectChanged()` - Emitted when QML root object changes

**Example**:
```cpp
class MyApplet : public DS_NAMESPACE::DApplet
{
    Q_OBJECT
    Q_PROPERTY(QString name READ name NOTIFY nameChanged)
public:
    explicit MyApplet(QObject *parent = nullptr);
    virtual bool init() override;
    
    QString name() const { return m_name; }
    
signals:
    void nameChanged();
    
private:
    QString m_name;
};

D_APPLET_CLASS(MyApplet)
```

### DContainment

Container plugin that holds multiple applets.

**Header**: `containment.h`

**Inherits**: DApplet

**Properties**:
- `appletItems` (DAppletItemModel*, read-only) - Model of child applets

**Methods**:
- `DApplet *createApplet(const DAppletData &data)` - Create child applet
- `void removeApplet(DApplet *applet)` - Remove child applet
- `QList<DApplet *> applets()` - Get list of child applets
- `DApplet *applet(const QString &id)` - Find applet by ID

**Example**:
```cpp
class MyContainment : public DS_NAMESPACE::DContainment
{
    Q_OBJECT
public:
    explicit MyContainment(QObject *parent = nullptr);
    virtual bool load() override;
    virtual bool init() override;
};

D_APPLET_CLASS(MyContainment)
```

### DPanel

Top-level panel plugin (like dock).

**Header**: `panel.h`

**Inherits**: DContainment

**Properties**:
- `popupWindow` (QQuickWindow*, notify) - Popup window
- `toolTipWindow` (QQuickWindow*, notify) - Tooltip window
- `menuWindow` (QQuickWindow*, notify) - Menu window

**Methods**:
- `QQuickWindow *window()` - Get the panel window

**Example**:
```cpp
class MyPanel : public DS_NAMESPACE::DPanel
{
    Q_OBJECT
public:
    explicit MyPanel(QObject *parent = nullptr);
    virtual bool load() override;
    virtual bool init() override;
};

D_APPLET_CLASS(MyPanel)
```

### DAppletBridge

Cross-plugin communication bridge.

**Header**: `appletbridge.h`

**Constructor**:
- `DAppletBridge(const QString &pluginId, QObject *parent = nullptr)`

**Methods**:
- `bool isValid()` - Check if bridge is connected
- `QString pluginId()` - Get target plugin ID
- `QList<DAppletProxy *> applets()` - Get all applet proxies
- `DAppletProxy *applet()` - Get first applet proxy

**Example**:
```cpp
DAppletBridge bridge("org.deepin.ds.weather");
if (bridge.isValid()) {
    if (auto applet = bridge.applet()) {
        int temp = applet->property("temperature").toInt();
        QString city = applet->property("currentCity").toString();
    }
}
```

### DAppletProxy

Proxy object for accessing applet properties.

**Header**: `appletproxy.h`

**Methods**:
- Standard QObject property access via `property()`
- Method invocation via `QMetaObject::invokeMethod()`

## Macros

### D_APPLET_CLASS(classname)

Registers a C++ class as a dde-shell plugin. Must be used in the .cpp file:

```cpp
D_APPLET_CLASS(MyApplet)
```

### DS_USE_NAMESPACE

Import the ds namespace:

```cpp
DS_USE_NAMESPACE
```

### DS_BEGIN_NAMESPACE / DS_END_NAMESPACE

Define code within the ds namespace:

```cpp
DS_BEGIN_NAMESPACE
// Your code here
DS_END_NAMESPACE
```

## Lifecycle

1. **Constructor**: Initialize member variables
2. **load()**: Load plugin data, set up models
3. **init()**: Initialize connections, register services
4. **rootObjectChanged**: QML root object is ready

## Best Practices

1. **Override init()** for initialization logic
2. **Use Q_PROPERTY** to expose data to QML
3. **Use signals** to notify QML of changes
4. **Check bridge.isValid()** before accessing other plugins
5. **Use D_APPLET_CLASS()** exactly once per plugin
