# Eval: 字体大小层级

## 任务

使用 DFontManager 获取字体大小：
1. 获取 T4 层级字体大小
2. 应用到标签控件
3. 监听系统字体变化

## 验证要点

- [ ] #include <DFontManager>
- [ ] DFontManager::instance()->t4()
- [ ] 连接 fontChanged 信号
