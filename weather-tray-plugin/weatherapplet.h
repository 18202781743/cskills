#ifndef WEATHERAPPLET_H
#define WEATHERAPPLET_H

#include <QWidget>
#include <QLabel>
#include <QVBoxLayout>
#include "weatherdata.h"

class WeatherApplet : public QWidget
{
    Q_OBJECT

public:
    explicit WeatherApplet(QWidget *parent = nullptr);

    void updateWeather(const WeatherInfo &info);

private:
    void setupUI();

    QLabel *m_cityLabel;
    QLabel *m_tempLabel;
    QLabel *m_weatherLabel;
    QLabel *m_windLabel;
    QLabel *m_humidityLabel;
    QWidget *m_forecastWidget;
    QVBoxLayout *m_forecastLayout;
};

#endif // WEATHERAPPLET_H
