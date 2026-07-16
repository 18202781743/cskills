# Eval: 主窗口与标题栏

## 任务

创建一个 DTK 主窗口，要求：
1. 窗口最小尺寸 800x600
2. 标题栏显示 "我的应用"
3. 标题栏包含菜单按钮

## 期望输出

代码应：
1. 继承 DMainWindow
2. 使用 titlebar() 获取标题栏
3. 设置标题和菜单

## 验证要点

- [ ] #include <DMainWindow>
- [ ] #include <DTitlebar>
- [ ] titlebar()->setTitle("我的应用")
- [ ] titlebar()->setMenu(menu)
