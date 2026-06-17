# DAppletBridge Guide

DAppletBridge enables cross-plugin communication in dde-shell.

## Overview

DAppletBridge allows plugins to:
- Access properties of other plugins
- Invoke methods on other plugins
- Connect to signals from other plugins

## Basic Usage

### Creating a Bridge

```cpp
#include <appletbridge.h>

DS_USE_NAMESPACE

DAppletBridge bridge("org.deepin.ds.weather");
```

### Checking Validity

```cpp
if (!bridge.isValid()) {
    qWarning() << "Target plugin not found";
    return;
}
```

### Accessing Properties

```cpp
if (auto applet = bridge.applet()) {
    // Read property
    int temp = applet->property("temperature").toInt();
    QString city = applet->property("currentCity").toString();
    
    // Write property (if writable)
    applet->setProperty("city", "Beijing");
}
```

### Invoking Methods

```cpp
if (auto applet = bridge.applet()) {
    // Invoke method with return value
    QString result;
    QMetaObject::invokeMethod(applet, "getData", 
        Qt::DirectConnection,
        Q_RETURN_ARG(QString, result));
    
    // Invoke method with arguments
    QMetaObject::invokeMethod(applet, "setCity",
        Qt::DirectConnection,
        Q_ARG(const QString&, "Beijing"));
}
```

### Connecting to Signals

```cpp
if (auto applet = bridge.applet()) {
    connect(applet, SIGNAL(temperatureChanged(int)),
            this, SLOT(onTemperatureChanged(int)));
}
```

## Complete Example

```cpp
#include "myapplet.h"
#include <appletbridge.h>
#include <appletproxy.h>

DS_USE_NAMESPACE

MyApplet::MyApplet(QObject *parent)
    : DApplet(parent)
{
}

bool MyApplet::init()
{
    DApplet::init();
    
    // Access weather plugin
    DAppletBridge weatherBridge("org.deepin.ds.weather");
    if (weatherBridge.isValid()) {
        if (auto weather = weatherBridge.applet()) {
            m_temperature = weather->property("temperature").toInt();
            m_city = weather->property("currentCity").toString();
            
            connect(weather, SIGNAL(temperatureChanged(int)),
                    this, SLOT(onWeatherUpdate(int)));
        }
    }
    
    // Access apps plugin
    DAppletBridge appsBridge("org.deepin.ds.dde-apps");
    if (appsBridge.isValid()) {
        if (auto apps = appsBridge.applet()) {
            QAbstractItemModel *model = apps->property("appModel").value<QAbstractItemModel*>();
            if (model) {
                // Use the model
            }
        }
    }
    
    return true;
}

void MyApplet::onWeatherUpdate(int temp)
{
    m_temperature = temp;
    emit temperatureChanged();
}

D_APPLET_CLASS(MyApplet)
```

## Multiple Applets

Some plugins may have multiple instances. Use `applets()` to get all:

```cpp
DAppletBridge bridge("org.deepin.ds.example");
if (bridge.isValid()) {
    QList<DAppletProxy*> applets = bridge.applets();
    for (auto applet : applets) {
        QString id = applet->property("id").toString();
        // Process each instance
    }
}
```

## QML Usage

Access other plugins from QML using `DS.applet()`:

```qml
AppletItem {
    Component.onCompleted: {
        var weather = DS.applet("org.deepin.ds.weather")
        if (weather && weather.rootObject) {
            console.log("Temperature:", weather.rootObject.temperature)
        }
    }
}
```

## Common Plugin IDs

| Plugin ID | Description |
|-----------|-------------|
| `org.deepin.ds.dock` | Main dock panel |
| `org.deepin.ds.dde-apps` | Application model |
| `org.deepin.ds.weather` | Weather applet (example) |

## Best Practices

1. **Always check isValid()** before accessing properties
2. **Check for null** when calling applet()
3. **Use signals** for reactive updates
4. **Handle missing plugins gracefully** - they may not be loaded
5. **Avoid tight coupling** - plugins should work independently

## Error Handling

```cpp
DAppletBridge bridge("org.deepin.ds.weather");

if (!bridge.isValid()) {
    // Plugin not found - handle gracefully
    qWarning() << "Weather plugin not available";
    return;
}

auto applet = bridge.applet();
if (!applet) {
    // No instances available
    qWarning() << "No weather instances";
    return;
}

// Safe to use
int temp = applet->property("temperature").toInt();
```

## Debugging

### Checking Available Plugins

```bash
# List all loaded plugins
dde-shell --list-plugins

# Run specific plugin
dde-shell -p org.deepin.ds.weather
```

### Logging

```cpp
qDebug() << "Bridge valid:" << bridge.isValid();
qDebug() << "Plugin ID:" << bridge.pluginId();
qDebug() << "Applets count:" << bridge.applets().size();
```
