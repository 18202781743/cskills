#include "weatherapplet.h"
#include "constants.h"

#include <QHBoxLayout>
#include <QGridLayout>
#include <QPainter>
#include <DGuiApplicationHelper>

DGUI_USE_NAMESPACE

WeatherApplet::WeatherApplet(QWidget *parent)
    : QWidget(parent)
{
    setupUI();
}

void WeatherApplet::setupUI()
{
    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->setContentsMargins(10, 10, 10, 10);
    mainLayout->setSpacing(6);

    // Current weather section
    QHBoxLayout *currentLayout = new QHBoxLayout();

    QVBoxLayout *infoLayout = new QVBoxLayout();
    m_cityLabel = new QLabel(this);
    m_cityLabel->setStyleSheet(QStringLiteral("font-size: 14px; font-weight: bold;"));
    m_weatherLabel = new QLabel(this);
    m_weatherLabel->setStyleSheet(QStringLiteral("font-size: 12px;"));
    m_windLabel = new QLabel(this);
    m_windLabel->setStyleSheet(QStringLiteral("font-size: 11px; color: gray;"));
    m_humidityLabel = new QLabel(this);
    m_humidityLabel->setStyleSheet(QStringLiteral("font-size: 11px; color: gray;"));

    infoLayout->addWidget(m_cityLabel);
    infoLayout->addWidget(m_weatherLabel);
    infoLayout->addWidget(m_windLabel);
    infoLayout->addWidget(m_humidityLabel);

    m_tempLabel = new QLabel(this);
    m_tempLabel->setAlignment(Qt::AlignCenter);
    m_tempLabel->setStyleSheet(QStringLiteral("font-size: 32px; font-weight: bold;"));
    m_tempLabel->setMinimumWidth(80);

    currentLayout->addLayout(infoLayout);
    currentLayout->addWidget(m_tempLabel);
    mainLayout->addLayout(currentLayout);

    // Separator
    QFrame *separator = new QFrame(this);
    separator->setFrameShape(QFrame::HLine);
    separator->setFrameShadow(QFrame::Sunken);
    mainLayout->addWidget(separator);

    // Forecast section
    m_forecastWidget = new QWidget(this);
    m_forecastLayout = new QVBoxLayout(m_forecastWidget);
    m_forecastLayout->setContentsMargins(0, 0, 0, 0);
    m_forecastLayout->setSpacing(4);
    mainLayout->addWidget(m_forecastWidget);

    setFixedWidth(Dock::DOCK_POPUP_WIDGET_WIDTH);
}

void WeatherApplet::updateWeather(const WeatherInfo &info)
{
    m_cityLabel->setText(info.cityName.isEmpty() ? tr("Unknown") : info.cityName);
    m_tempLabel->setText(info.temperature.isEmpty() ? QStringLiteral("--") : info.temperature + QStringLiteral("°"));
    m_weatherLabel->setText(info.weatherName.isEmpty() ? tr("No data") : info.weatherName);

    QString windText;
    if (!info.windDirection.isEmpty()) {
        windText = info.windDirection;
        if (!info.windStrength.isEmpty()) {
            windText += QStringLiteral(" ") + info.windStrength;
        }
    }
    m_windLabel->setText(windText);

    if (!info.humidity.isEmpty()) {
        m_humidityLabel->setText(tr("Humidity") + QStringLiteral(": ") + info.humidity + QStringLiteral("%"));
    } else {
        m_humidityLabel->setText(QString());
    }

    // Update forecast
    QLayoutItem *item;
    while ((item = m_forecastLayout->takeAt(0)) != nullptr) {
        delete item->widget();
        delete item;
    }

    for (const ForecastDay &day : info.forecasts) {
        QHBoxLayout *row = new QHBoxLayout();

        QLabel *dayLabel = new QLabel(day.dayOfWeek, this);
        dayLabel->setFixedWidth(60);
        dayLabel->setStyleSheet(QStringLiteral("font-size: 12px;"));

        QLabel *iconLabel = new QLabel(this);
        QIcon icon = QIcon::fromTheme(day.iconName);
        if (!icon.isNull()) {
            iconLabel->setPixmap(icon.pixmap(20, 20));
        }
        iconLabel->setFixedWidth(24);

        QLabel *weatherLabel = new QLabel(day.weatherName, this);
        weatherLabel->setStyleSheet(QStringLiteral("font-size: 12px;"));

        QLabel *tempLabel = new QLabel(this);
        if (!day.tempHigh.isEmpty() && !day.tempLow.isEmpty()) {
            tempLabel->setText(day.tempLow + QStringLiteral("°~") + day.tempHigh + QStringLiteral("°"));
        } else if (!day.tempHigh.isEmpty()) {
            tempLabel->setText(day.tempHigh + QStringLiteral("°"));
        }
        tempLabel->setAlignment(Qt::AlignRight);
        tempLabel->setStyleSheet(QStringLiteral("font-size: 12px;"));

        row->addWidget(dayLabel);
        row->addWidget(iconLabel);
        row->addWidget(weatherLabel);
        row->addStretch();
        row->addWidget(tempLabel);

        m_forecastLayout->addLayout(row);
    }
}
