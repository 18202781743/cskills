#include "weatherplugin.h"
#include "weatherwidget.h"
#include "weatherapplet.h"
#include "constants.h"

#include <DGuiApplicationHelper>

#include <QProcess>
#include <QJsonDocument>
#include <QJsonObject>

#define PLUGIN_STATE_KEY    "enable"
#define WEATHER_SETTINGS    "weather-settings"

DGUI_USE_NAMESPACE

WeatherPlugin::WeatherPlugin(QObject *parent)
    : QObject(parent)
    , m_tipsLabel(new Dock::TipsWidget)
{
    m_tipsLabel->setText(tr("No weather data"));
    m_tipsLabel->setVisible(false);
    m_tipsLabel->setAccessibleName("Weather");
    m_tipsLabel->setObjectName("WeatherTipsLabel");
}

const QString WeatherPlugin::pluginName() const
{
    return QStringLiteral("weather");
}

const QString WeatherPlugin::pluginDisplayName() const
{
    return tr("Weather");
}

Dock::PluginFlags WeatherPlugin::flags() const
{
    return Dock::PluginFlag::Type_Tray | Dock::PluginFlag::Attribute_CanSetting;
}

PluginsItemInterface::PluginSizePolicy WeatherPlugin::pluginSizePolicy() const
{
    return PluginSizePolicy::Custom;
}

bool WeatherPlugin::pluginIsAllowDisable()
{
    return true;
}

bool WeatherPlugin::pluginIsDisable()
{
    return !(m_proxyInter->getValue(this, PLUGIN_STATE_KEY, true).toBool());
}

void WeatherPlugin::init(PluginProxyInterface *proxyInter)
{
    m_proxyInter = proxyInter;

    if (!pluginIsDisable()) {
        loadPlugin();
    }
}

void WeatherPlugin::pluginStateSwitched()
{
    m_proxyInter->saveValue(this, PLUGIN_STATE_KEY, pluginIsDisable());
    refreshPluginItemsVisible();
}

QWidget *WeatherPlugin::itemWidget(const QString &itemKey)
{
    Q_UNUSED(itemKey)
    return m_mainWidget.data();
}

QWidget *WeatherPlugin::itemTipsWidget(const QString &itemKey)
{
    Q_UNUSED(itemKey)
    return m_tipsLabel.data();
}

QWidget *WeatherPlugin::itemPopupApplet(const QString &itemKey)
{
    Q_UNUSED(itemKey)
    return m_appletWidget.data();
}

const QString WeatherPlugin::itemCommand(const QString &itemKey)
{
    Q_UNUSED(itemKey)
    return QString("dde-am org.deepin.uos-weather");
}

const QString WeatherPlugin::itemContextMenu(const QString &itemKey)
{
    Q_UNUSED(itemKey)

    QList<QVariant> items;

    QMap<QString, QVariant> settingsAction;
    settingsAction["itemId"] = WEATHER_SETTINGS;
    settingsAction["itemText"] = tr("Weather settings");
    settingsAction["isCheckable"] = false;
    settingsAction["isActive"] = true;
    items.push_back(settingsAction);

    QMap<QString, QVariant> menu;
    menu["items"] = items;
    menu["checkableMenu"] = false;
    menu["singleCheck"] = false;
    return QJsonDocument::fromVariant(menu).toJson();
}

void WeatherPlugin::invokedMenuItem(const QString &itemKey, const QString &menuId, const bool checked)
{
    Q_UNUSED(itemKey)
    Q_UNUSED(checked)

    if (menuId == WEATHER_SETTINGS) {
        QStringList args {QStringLiteral("--by-user"), QStringLiteral("org.deepin.uos-weather"), QStringLiteral("--"), QStringLiteral("-s")};
        QProcess::startDetached(QStringLiteral("dde-am"), args);
    }
}

QIcon WeatherPlugin::icon(Dock::IconType dockPart, Dock::ThemeType themeType) const
{
    Q_UNUSED(dockPart)

    QString iconName;
    if (m_weatherData) {
        iconName = m_weatherData->currentWeather().iconName;
    }

    if (themeType == Dock::ThemeType_Dark) {
        // For dark theme in control center, use built-in icon
        return QIcon::fromTheme(iconName.isEmpty() ? QStringLiteral("weather-clear") : iconName);
    }
    return QIcon::fromTheme(iconName.isEmpty() ? QStringLiteral("weather-clear") : iconName);
}

void WeatherPlugin::refreshIcon(const QString &itemKey)
{
    Q_UNUSED(itemKey)
    updateWidgets();
}

void WeatherPlugin::setMessageCallback(MessageCallbackFunc cb)
{
    m_messageCallback = cb;
}

QString WeatherPlugin::message(const QString &msg)
{
    QJsonObject msgObj = QJsonDocument::fromJson(msg.toUtf8()).object();
    QString msgType = msgObj[Dock::MSG_TYPE].toString();

    if (msgType == Dock::MSG_GET_SUPPORT_FLAG) {
        QJsonObject data;
        data[Dock::MSG_SUPPORT_FLAG] = true;
        QJsonObject reply;
        reply[Dock::MSG_TYPE] = msgType;
        reply[Dock::MSG_DATA] = data;
        return QJsonDocument(reply).toJson();
    }

    if (msgType == Dock::MSG_WHETHER_WANT_TO_BE_LOADED) {
        QJsonObject data;
        data[QStringLiteral("whetherWantToBeLoaded")] = true;
        QJsonObject reply;
        reply[Dock::MSG_TYPE] = msgType;
        reply[Dock::MSG_DATA] = data;
        return QJsonDocument(reply).toJson();
    }

    if (msgType == Dock::MSG_PLUGIN_PROPERTY) {
        QJsonObject data;
        data[Dock::PLUGIN_PROP_NEED_CHAMELEON] = false;
        QJsonObject reply;
        reply[Dock::MSG_TYPE] = msgType;
        reply[Dock::MSG_DATA] = data;
        return QJsonDocument(reply).toJson();
    }

    return QStringLiteral("{}");
}

void WeatherPlugin::loadPlugin()
{
    if (m_pluginLoaded) {
        return;
    }
    m_pluginLoaded = true;

    m_weatherData.reset(new WeatherData);
    connect(m_weatherData.data(), &WeatherData::weatherChanged, this, &WeatherPlugin::onWeatherChanged);

    m_mainWidget.reset(new WeatherWidget);
    m_mainWidget->setFixedSize(32, Dock::TRAY_PLUGIN_ITEM_FIXED_HEIGHT);

    m_appletWidget.reset(new WeatherApplet);

    updateWidgets();

    m_proxyInter->itemAdded(this, pluginName());
}

void WeatherPlugin::refreshPluginItemsVisible()
{
    if (pluginIsDisable()) {
        m_proxyInter->itemRemoved(this, pluginName());
    } else {
        if (!m_pluginLoaded) {
            loadPlugin();
            return;
        }
        m_proxyInter->itemAdded(this, pluginName());
    }
}

void WeatherPlugin::onWeatherChanged()
{
    updateWidgets();
    m_proxyInter->itemUpdate(this, pluginName());
}

void WeatherPlugin::updateWidgets()
{
    if (!m_weatherData) return;

    WeatherInfo info = m_weatherData->currentWeather();

    // Update tray widget
    QIcon weatherIcon = QIcon::fromTheme(info.iconName.isEmpty() ? QStringLiteral("weather-clear") : info.iconName);
    m_mainWidget->setWeatherIcon(weatherIcon);
    m_mainWidget->setTemperature(info.temperature);
    m_mainWidget->setThemeType(
        DGuiApplicationHelper::instance()->themeType() == DGuiApplicationHelper::LightType ? 1 : 2);

    // Update tips
    QString tipsText;
    if (info.weatherName.isEmpty() && info.temperature.isEmpty()) {
        tipsText = tr("No weather data");
    } else {
        tipsText = info.weatherName;
        if (!info.temperature.isEmpty()) {
            tipsText += QStringLiteral(" ") + info.temperature + QStringLiteral("°");
        }
    }
    m_tipsLabel->setText(tipsText);

    // Update applet
    m_appletWidget->updateWeather(info);
}
