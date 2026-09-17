#include "weatherdata.h"

#include <QDir>
#include <QStandardPaths>

WeatherData::WeatherData(QObject *parent)
    : QObject(parent)
    , m_watcher(new QFileSystemWatcher(this))
    , m_pollTimer(new QTimer(this))
{
    loadWeather();

    QString path = configPath();
    QFileInfo fi(path);
    QDir dir = fi.absoluteDir();
    if (!dir.exists()) {
        dir.mkpath(QStringLiteral("."));
    }

    if (fi.exists()) {
        m_watcher->addPath(path);
    }
    m_watcher->addPath(fi.absoluteDir().path());

    connect(m_watcher, &QFileSystemWatcher::fileChanged, this, &WeatherData::onFileChanged);
    connect(m_watcher, &QFileSystemWatcher::directoryChanged, this, [this](const QString &) {
        QString path = configPath();
        if (QFileInfo::exists(path) && !m_watcher->files().contains(path)) {
            m_watcher->addPath(path);
            refreshWeather();
        }
    });

    // Poll every 5 minutes as fallback
    m_pollTimer->setInterval(5 * 60 * 1000);
    connect(m_pollTimer, &QTimer::timeout, this, &WeatherData::refreshWeather);
    m_pollTimer->start();
}

QString WeatherData::configPath() const
{
    return QStandardPaths::writableLocation(QStandardPaths::HomeLocation)
           + QStringLiteral("/.config/deepin/org.deepin.weather.conf");
}

WeatherInfo WeatherData::currentWeather() const
{
    return m_weather;
}

void WeatherData::onFileChanged(const QString &path)
{
    if (QFileInfo::exists(path)) {
        m_watcher->addPath(path);
    }
    refreshWeather();
}

void WeatherData::refreshWeather()
{
    loadWeather();
    Q_EMIT weatherChanged();
}

void WeatherData::loadWeather()
{
    QSettings settings(configPath(), QSettings::IniFormat);

    settings.beginGroup(QStringLiteral("General"));
    m_weather.cityName = settings.value(QStringLiteral("cityName"), QString()).toString();
    m_weather.weatherName = settings.value(QStringLiteral("weatherName"), QString()).toString();
    m_weather.temperature = settings.value(QStringLiteral("temp"), QString()).toString();
    m_weather.iconName = settings.value(QStringLiteral("icon"), QStringLiteral("weather-clear")).toString();
    m_weather.humidity = settings.value(QStringLiteral("humidity"), QString()).toString();
    m_weather.windDirection = settings.value(QStringLiteral("windDirection"), QString()).toString();
    m_weather.windStrength = settings.value(QStringLiteral("windStrength"), QString()).toString();
    m_weather.updateTime = settings.value(QStringLiteral("updateTime"), QString()).toString();
    settings.endGroup();

    m_weather.forecasts.clear();
    for (int i = 0; i < 7; ++i) {
        settings.beginGroup(QStringLiteral("Forecast%1").arg(i));
        ForecastDay day;
        day.dayOfWeek = settings.value(QStringLiteral("dayOfWeek"), QString()).toString();
        day.weatherName = settings.value(QStringLiteral("weatherName"), QString()).toString();
        day.tempHigh = settings.value(QStringLiteral("tempHigh"), QString()).toString();
        day.tempLow = settings.value(QStringLiteral("tempLow"), QString()).toString();
        day.iconName = settings.value(QStringLiteral("icon"), QStringLiteral("weather-clear")).toString();
        settings.endGroup();

        if (day.dayOfWeek.isEmpty() && day.weatherName.isEmpty()) {
            break;
        }
        m_weather.forecasts.append(day);
    }
}
