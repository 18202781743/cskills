# Translation Guide

dde-shell plugins support internationalization (i18n) using Qt's translation system.

## Translation Files

Translation files are stored in the `translations/` directory:

```
translations/
├── org.deepin.ds.weather.ts           # Base (English)
├── org.deepin.ds.weather_zh_CN.ts     # Chinese (Simplified)
├── org.deepin.ds.weather_zh_HK.ts     # Chinese (Hong Kong)
├── org.deepin.ds.weather_zh_TW.ts     # Chinese (Taiwan)
├── org.deepin.ds.weather_ja.ts        # Japanese
├── org.deepin.ds.weather_ko.ts        # Korean
└── ... (23 languages total)
```

## Supported Languages

| Code | Language |
|------|----------|
| ar | Arabic |
| az | Azerbaijani |
| bo | Tibetan |
| ca | Catalan |
| de | German |
| es | Spanish |
| fi | Finnish |
| fr | French |
| hu | Hungarian |
| it | Italian |
| ja | Japanese |
| ko | Korean |
| lo | Lao |
| nb_NO | Norwegian |
| pl | Polish |
| pt_BR | Portuguese (Brazil) |
| ru | Russian |
| sq | Albanian |
| uk | Ukrainian |
| zh_CN | Chinese (Simplified) |
| zh_HK | Chinese (Hong Kong) |
| zh_TW | Chinese (Taiwan) |

## CMake Integration

Use `ds_handle_package_translation()` macro:

```cmake
ds_handle_package_translation(
    PACKAGE org.deepin.ds.weather
    QML_FILES
        ${CMAKE_CURRENT_LIST_DIR}/package/main.qml
        ${CMAKE_CURRENT_LIST_DIR}/package/WeatherWidget.qml
)
```

The macro automatically:
1. Finds all QML files in the package directory
2. Finds all C++ source files
3. Creates translation targets for all 23 languages
4. Installs compiled translations to the correct location

## Marking Strings for Translation

### In QML

```qml
// Simple text
Text {
    text: qsTr("Hello World")
}

// With parameters
Text {
    text: qsTr("Temperature: %1°C").arg(temp)
}

// With plural forms
Text {
    text: qsTr("%n item(s)", "", count)
}
```

### In C++

```cpp
// Simple string
QString text = tr("Hello World");

// With parameters
QString text = tr("Temperature: %1°C").arg(temp);

// With context
QString text = QCoreApplication::translate("WeatherApplet", "Refresh");
```

## Translation File Format

Translation files (.ts) are XML files:

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="zh_CN">
<context>
    <name>main</name>
    <message>
        <source>Hello World</source>
        <translation>你好世界</translation>
    </message>
</context>
</TS>
```

## Generating Translations

### Using Qt Linguist

1. Open `.ts` file in Qt Linguist
2. Translate each string
3. Save and compile

### Using Command Line

```bash
# Update translation files
lupdate -no-obsolete -no-ui-lines -locations none \
    package/main.qml package/*.qml *.cpp \
    -ts translations/org.deepin.ds.weather_zh_CN.ts

# Compile translation files
lrelease translations/org.deepin.ds.weather_zh_CN.ts
```

## Installation Path

Translations are installed to:
```
/usr/share/dde-shell/<plugin-id>/translations/
```

## Best Practices

1. **Use qsTr()** for all user-visible strings in QML
2. **Use tr()** for all user-visible strings in C++
3. **Provide context** with comments for ambiguous strings
4. **Use parameters** instead of string concatenation
5. **Test with different languages** to ensure proper layout
6. **Keep translations updated** when adding new strings

## Example

### QML File
```qml
import QtQuick 2.15

AppletItem {
    Column {
        Text {
            text: qsTr("Weather Applet")
        }
        Text {
            text: qsTr("City: %1").arg(Applet.city)
        }
        Text {
            text: qsTr("Temperature: %1°C").arg(Applet.temperature)
        }
        Button {
            text: qsTr("Refresh")
            onClicked: Applet.refresh()
        }
    }
}
```

### Translation File (zh_CN)
```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="zh_CN">
<context>
    <name>main</name>
    <message>
        <source>Weather Applet</source>
        <translation>天气小部件</translation>
    </message>
    <message>
        <source>City: %1</source>
        <translation>城市：%1</translation>
    </message>
    <message>
        <source>Temperature: %1°C</source>
        <translation>温度：%1°C</translation>
    </message>
    <message>
        <source>Refresh</source>
        <translation>刷新</translation>
    </message>
</context>
</TS>
```
