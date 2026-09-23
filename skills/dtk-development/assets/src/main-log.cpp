// DTK 应用日志最小示例
// CMake 依赖：Dtk6::Core，不需要 Dtk6::Log

#include <QCoreApplication>
#include <DLog>

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);

    DLogManager::registerConsoleAppender();

    qInfo() << "DTK application started";
    return 0;
}
