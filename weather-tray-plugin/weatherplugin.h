#ifndef WEATHERPLUGIN_H
#define WEATHERPLUGIN_H

#include "pluginsiteminterface.h"
#include "pluginsiteminterface_v2.h"
#include "weatherdata.h"
#include "tipswidget.h"

#include <QObject>

class WeatherWidget;
class WeatherApplet;

class WeatherPlugin : public QObject, public PluginsItemInterfaceV2
{
    Q_OBJECT
    Q_INTERFACES(PluginsItemInterfaceV2)
    Q_PLUGIN_METADATA(IID "com.deepin.dock.PluginsItemInterface" FILE "weather.json")

public:
    explicit WeatherPlugin(QObject *parent = nullptr);

    const QString pluginName() const override;
    const QString pluginDisplayName() const override;
    Dock::PluginFlags flags() const override;
    PluginSizePolicy pluginSizePolicy() const override;
    bool pluginIsAllowDisable() override;
    bool pluginIsDisable() override;

    void init(PluginProxyInterface *proxyInter) override;
    void pluginStateSwitched() override;

    QWidget *itemWidget(const QString &itemKey) override;
    QWidget *itemTipsWidget(const QString &itemKey) override;
    QWidget *itemPopupApplet(const QString &itemKey) override;
    const QString itemCommand(const QString &itemKey) override;
    const QString itemContextMenu(const QString &itemKey) override;
    void invokedMenuItem(const QString &itemKey, const QString &menuId, const bool checked) override;

    QIcon icon(Dock::IconType dockPart, Dock::ThemeType themeType) const override;
    void refreshIcon(const QString &itemKey) override;

    void setMessageCallback(MessageCallbackFunc cb) override;
    QString message(const QString &msg) override;

private Q_SLOTS:
    void onWeatherChanged();

private:
    void loadPlugin();
    void refreshPluginItemsVisible();
    void updateWidgets();

private:
    bool m_pluginLoaded = false;
    QScopedPointer<WeatherData> m_weatherData;
    QScopedPointer<WeatherWidget> m_mainWidget;
    QScopedPointer<WeatherApplet> m_appletWidget;
    QScopedPointer<Dock::TipsWidget> m_tipsLabel;
    MessageCallbackFunc m_messageCallback = nullptr;
};

#endif // WEATHERPLUGIN_H
