#include "weatherwidget.h"
#include "constants.h"

#include <QPainter>
#include <QFontMetrics>
#include <DGuiApplicationHelper>

DGUI_USE_NAMESPACE

WeatherWidget::WeatherWidget(QWidget *parent)
    : QWidget(parent)
{
    setFixedSize(32, Dock::TRAY_PLUGIN_ITEM_FIXED_HEIGHT);
}

void WeatherWidget::setWeatherIcon(const QIcon &icon)
{
    m_icon = icon;
    update();
}

void WeatherWidget::setTemperature(const QString &temp)
{
    m_temperature = temp;
    update();
}

void WeatherWidget::setThemeType(int themeType)
{
    m_themeType = themeType;
    update();
}

void WeatherWidget::paintEvent(QPaintEvent *e)
{
    Q_UNUSED(e)
    QPainter p(this);
    p.setRenderHint(QPainter::Antialiasing);

    // Draw weather icon (left half, 16x16)
    if (!m_icon.isNull()) {
        QRect iconRect(0, 0, 16, height());
        m_icon.paint(&p, iconRect);
    }

    // Draw temperature text (right half)
    if (!m_temperature.isEmpty()) {
        QColor textColor;
        if (m_themeType == 1) {
            textColor = QColor(0, 0, 0);
        } else {
            textColor = QColor(255, 255, 255);
        }

        QFont font;
        font.setPixelSize(10);
        p.setFont(font);
        p.setPen(textColor);

        QRect textRect(16, 0, 16, height());
        p.drawText(textRect, Qt::AlignLeft | Qt::AlignVCenter, m_temperature);
    }
}
