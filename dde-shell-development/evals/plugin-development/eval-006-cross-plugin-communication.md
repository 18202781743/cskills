# Eval: 跨插件通信

## 任务

用户的 Dock 面板插件需要获取天气插件的数据。

指导用户使用 DAppletBridge 进行跨插件通信。

## 期望输出

回答应：
1. 展示 C++ 中使用 DAppletBridge
2. 展示 QML 中使用 DS.applet()
3. 展示属性读取和方法调用
4. 说明 createProxyMeta 的作用

## 验证要点

- [ ] C++: DAppletBridge bridge("org.deepin.ds.weather")
- [ ] C++: bridge.applet()->property("temperature")
- [ ] QML: DS.applet("org.deepin.ds.weather")
- [ ] 说明 bridge.isValid() 检查
- [ ] 说明插件可通过 createProxyMeta() 暴露自定义接口
