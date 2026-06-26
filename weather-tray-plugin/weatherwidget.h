#ifndef WEATHERWIDGET_H
#define WEATHERWIDGET_H

#include <QWidget>
#include <QIcon>

class WeatherWidget : public QWidget
{
    Q_OBJECT

public:
    explicit WeatherWidget(QWidget *parent = nullptr);

    void setWeatherIcon(const QIcon &icon);
    void setTemperature(const QString &temp);
    void setThemeType(int themeType);

protected:
    void paintEvent(QPaintEvent *e) override;

private:
    QIcon m_icon;
    QString m_temperature;
    int m_themeType = 0;  // 0=none, 1=light, 2=dark
};

#endif // WEATHERWIDGET_H
