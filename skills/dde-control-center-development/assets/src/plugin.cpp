```cpp
// mypluginmodule.h
#include <QObject>

class MyPluginModule : public QObject {
    Q_OBJECT
    Q_PROPERTY(QString name READ name WRITE setName NOTIFY nameChanged FINAL)
public:
    explicit MyPluginModule(QObject *parent = nullptr);
    QString name() const;
    void setName(const QString &name);
    Q_INVOKABLE int calc(int a, int b);
Q_SIGNALS:
    void nameChanged(const QString &name);
private:
    QString m_name;
};
