// DTK QWidget 应用最小示例 (DApplication + DMainWindow)
// 使用说明：将 #include 按需增减，替换 DMainWindow 为实际主窗口类

#include <DApplication>
#include <DMainWindow>
#include <DTitlebar>
#include <DIconTheme>
#include <DPalette>
#include <DGuiApplicationHelper>

int main(int argc, char *argv[])
{
    DApplication app(argc, argv);

    DMainWindow w;
    w.setMinimumSize(800, 600);
    w.titlebar()->setTitle("My DTK App");
    w.titlebar()->setIcon(DIconTheme::findQIcon("deepin"));
    w.show();

    return app.exec();
}
