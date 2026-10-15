#ifndef WEATHERDATA_H
#define WEATHERDATA_H

#include <QObject>
#include <QSettings>
#include <QFileSystemWatcher>
#include <QTimer>

struct ForecastDay {
    QString dayOfWeek;
    QString weatherName;
    QString tempHigh;
    QString tempLow;
    QString iconName;
};

struct WeatherInfo {
    QString cityName;
    QString weatherName;
    QString temperature;
    QString iconName;
    QString humidity;
    QString windDirection;
    QString windStrength;
    QString updateTime;
    QList<ForecastDay> forecasts;
};

class WeatherData : public QObject
{
    Q_OBJECT

public:
    explicit WeatherData(QObject *parent = nullptr);
    WeatherInfo currentWeather() const;

Q_SIGNALS:
    void weatherChanged();

private Q_SLOTS:
    void onFileChanged(const QString &path);
    void refreshWeather();

private:
    void loadWeather();
    QString configPath() const;

    QFileSystemWatcher *m_watcher;
    QTimer *m_pollTimer;
    WeatherInfo m_weather;
};

#endif // WEATHERDATA_H
