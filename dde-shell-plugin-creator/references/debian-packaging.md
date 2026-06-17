# Debian Packaging Guide

This guide covers creating Debian packages for dde-shell plugins.

## Package Structure

```
debian/
├── changelog           # Package changelog
├── compat              # Debhelper compatibility level
├── control             # Package metadata and dependencies
├── copyright           # Copyright information
├── rules               # Build rules
├── source/
│   └── format          # Source format
└── <package-name>.install  # Installation files
```

## debian/control

```plaintext
Source: <package-name>
Section: DDE
Priority: optional
Maintainer: Your Name <your.email@example.com>
Build-Depends:
 debhelper-compat (= 13),
 cmake,
 pkg-config,
 qt6-base-dev,
 qt6-declarative-dev,
 qt6-tools-dev,
 libdtk6core-dev (>= 6.0),
 libdde-shell-dev (>= 0.0.10)
Standards-Version: 4.6.0
Rules-Requires-Root: no

Package: <package-name>
Architecture: any
Depends:
 ${shlibs:Depends},
 ${misc:Depends},
 dde-shell (>= 2.0)
Description: <Short description>
 <Long description>
```

### Key Dependencies

| Dependency | Purpose |
|------------|---------|
| `libdde-shell-dev` | dde-shell development files |
| `qt6-base-dev` | Qt6 core |
| `qt6-declarative-dev` | Qt6 QML support |
| `libdtk6core-dev` | DTK core library |

### Runtime Dependencies

| Dependency | Purpose |
|------------|---------|
| `dde-shell` | dde-shell runtime |
| `qml6-module-qtquick-*` | QML modules |

## debian/rules

```makefile
#!/usr/bin/make -f

%:
	dh $@

override_dh_auto_configure:
	dh_auto_configure -- -DQT_VERSION_MAJOR=6
```

## debian/changelog

```plaintext
<package-name> (1.0.0-1) unstable; urgency=medium

  * Initial release.

 -- Your Name <your.email@example.com>  Mon, 01 Jan 2024 00:00:00 +0000
```

## debian/compat

```
13
```

## debian/source/format

```
3.0 (native)
```

## Installation File

Create `<package-name>.install`:

```
usr/lib/dde-shell/plugins/*
usr/share/dde-shell/*
```

## Complete Example

### debian/control

```plaintext
Source: dde-weather-applet
Section: DDE
Priority: optional
Maintainer: Developer <dev@example.com>
Build-Depends:
 debhelper-compat (= 13),
 cmake,
 pkg-config,
 qt6-base-dev,
 qt6-declarative-dev,
 qt6-tools-dev,
 libdtk6core-dev (>= 6.0),
 libdde-shell-dev (>= 0.0.10)
Standards-Version: 4.6.0
Rules-Requires-Root: no

Package: dde-weather-applet
Architecture: any
Depends:
 ${shlibs:Depends},
 ${misc:Depends},
 dde-shell (>= 2.0)
Description: Weather applet for DDE
 A weather applet that displays current weather information
 in the Deepin Desktop Environment dock.
```

### debian/rules

```makefile
#!/usr/bin/make -f

%:
	dh $@

override_dh_auto_configure:
	dh_auto_configure -- -DQT_VERSION_MAJOR=6
```

### dde-weather-applet.install

```
usr/lib/dde-shell/plugins/*
usr/share/dde-shell/*
```

## Building the Package

```bash
# Install build dependencies
sudo apt build-dep .

# Build the package
dpkg-buildpackage -us -uc -b

# Or using debuild
debuild -us -uc -b
```

## Testing

```bash
# Install the package
sudo dpkg -i ../dde-weather-applet_1.0.0_amd64.deb

# Test the plugin
dde-shell -p org.deepin.ds.weather

# Check installation
dpkg -L dde-weather-applet
```

## Best Practices

1. **Use debhelper-compat 13** for modern packaging
2. **Specify exact versions** for critical dependencies
3. **Use ${shlibs:Depends}** for automatic library dependencies
4. **Test installation** before submitting
5. **Follow Debian policy** for package naming
6. **Include copyright** information in debian/copyright
