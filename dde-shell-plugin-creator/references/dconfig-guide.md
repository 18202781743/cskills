# DConfig Guide

DConfig provides persistent configuration storage for dde-shell plugins.

## Configuration File

Create a JSON file in the `configs/` directory named after your plugin ID:

```
configs/
└── org.deepin.ds.weather.json
```

## JSON Format

```json
{
    "magic": "dsg.config.meta",
    "version": "1.0",
    "contents": {
        "settingName": {
            "value": "defaultValue",
            "serial": 0,
            "flags": [],
            "name": "Setting description",
            "name[zh_CN]": "设置描述",
            "permissions": "readwrite",
            "visibility": "public"
        }
    }
}
```

## Field Descriptions

### Top Level

| Field | Type | Description |
|-------|------|-------------|
| `magic` | string | Must be "dsg.config.meta" |
| `version` | string | Configuration version |
| `contents` | object | Configuration entries |

### Content Entry

| Field | Type | Description |
|-------|------|-------------|
| `value` | any | Default value |
| `serial` | int | Version serial number |
| `flags` | array | Configuration flags |
| `name` | string | Description (English) |
| `name[zh_CN]` | string | Description (Chinese) |
| `permissions` | string | "readwrite" or "readonly" |
| `visibility` | string | "public" or "private" |

## Supported Value Types

- `string`: Text value
- `int`: Integer value
- `bool`: Boolean value
- `array`: Array of values
- `object`: Nested object

## CMake Integration

Add DConfig support in CMakeLists.txt:

```cmake
find_package(Dtk${DTK_VERSION_MAJOR}DConfig REQUIRED)

dtk_add_config_meta_files(APPID "org.deepin.dde.shell" FILES org.deepin.ds.weather.json)
```

## C++ Usage

```cpp
#include <DConfig>

DCORE_USE_NAMESPACE;

// Create config instance
std::unique_ptr<DConfig> config(DConfig::create("org.deepin.dde.shell", "org.deepin.ds.weather"));

// Read value
QString city = config->value("city").toString();
int interval = config->value("refreshInterval").toInt();

// Write value
config->setValue("city", "Beijing");
config->setValue("refreshInterval", 30);

// Check if key exists
if (config->keyList().contains("city")) {
    // Key exists
}
```

## QML Usage

Expose config values via Q_PROPERTY:

```cpp
class WeatherApplet : public DApplet
{
    Q_OBJECT
    Q_PROPERTY(QString city READ city WRITE setCity NOTIFY cityChanged)
public:
    QString city() const { return m_config->value("city").toString(); }
    void setCity(const QString &city) { 
        m_config->setValue("city", city); 
        emit cityChanged();
    }
signals:
    void cityChanged();
private:
    std::unique_ptr<DConfig> m_config;
};
```

## Example Configuration

```json
{
    "magic": "dsg.config.meta",
    "version": "1.0",
    "contents": {
        "city": {
            "value": "auto",
            "serial": 0,
            "flags": [],
            "name": "City name or 'auto' for auto-detection",
            "name[zh_CN]": "城市名称或'auto'自动检测",
            "permissions": "readwrite",
            "visibility": "public"
        },
        "refreshInterval": {
            "value": 30,
            "serial": 0,
            "flags": [],
            "name": "Refresh interval in minutes",
            "name[zh_CN]": "刷新间隔（分钟）",
            "permissions": "readwrite",
            "visibility": "public"
        },
        "temperatureUnit": {
            "value": "celsius",
            "serial": 0,
            "flags": [],
            "name": "Temperature unit (celsius/fahrenheit)",
            "name[zh_CN]": "温度单位（摄氏/华氏）",
            "permissions": "readwrite",
            "visibility": "public"
        }
    }
}
```

## Best Practices

1. **Use descriptive names** for configuration keys
2. **Provide Chinese translations** for user-facing descriptions
3. **Set appropriate permissions** (readwrite for user settings, readonly for system values)
4. **Use public visibility** for user-configurable settings
5. **Increment serial** when adding new configuration entries
