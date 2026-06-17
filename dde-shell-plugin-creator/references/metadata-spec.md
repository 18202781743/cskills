# Metadata Specification

## metadata.json Format

Every dde-shell plugin must have a `package/metadata.json` file:

```json
{
    "Plugin": {
        "Version": "1.0",
        "Id": "org.deepin.ds.example",
        "Url": "main.qml",
        "Parent": "org.deepin.ds.dock"
    }
}
```

## Fields

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `Version` | string | Plugin version (e.g., "1.0") |
| `Id` | string | Unique plugin identifier |
| `Url` | string | QML entry file relative to package directory |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `Parent` | string | Parent plugin ID for containment hierarchy |
| `ContainmentType` | string | Type indicator (e.g., "Panel") |

## Plugin ID Convention

Use reverse domain notation:
- Base: `org.deepin.ds.<name>`
- Dock plugins: `org.deepin.ds.dock.<name>`
- Examples: `org.deepin.ds.example.<name>`

Examples:
- `org.deepin.ds.weather` - Weather applet
- `org.deepin.ds.dock.launcherapplet` - Launcher in dock
- `org.deepin.ds.example` - Example panel

## Parent Plugin IDs

Common parent plugins:
- `org.deepin.ds.dock` - Dock panel
- `org.deepin.ds.example.containment` - Example containment

## ContainmentType Values

| Value | Description |
|-------|-------------|
| `Panel` | Top-level panel plugin |

## Examples

### Simple Applet

```json
{
    "Plugin": {
        "Version": "1.0",
        "Id": "org.deepin.ds.weather",
        "Url": "main.qml",
        "Parent": "org.deepin.ds.dock"
    }
}
```

### Panel Plugin

```json
{
    "Plugin": {
        "Version": "1.0",
        "Id": "org.deepin.ds.example",
        "Url": "main.qml",
        "ContainmentType": "Panel"
    }
}
```

### Applet Without QML

```json
{
    "Plugin": {
        "Version": "1.0",
        "Id": "org.deepin.ds.example.applet-widget",
        "Parent": "org.deepin.ds.example.containment"
    }
}
```
