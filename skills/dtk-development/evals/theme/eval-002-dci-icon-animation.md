# dci 图标动画

## 任务

播放 dci 图标动画，要求：
1. 加载一个 dci 图标文件
2. 自动播放图标中的动画
3. 循环播放

## 期望输出

代码应：
1. #include <DDciIconPlayer>
2. setIcon() 设置图标
3. play() 开始播放
4. 连接 updated 信号更新显示
5. 未使用 QSS 替代 DPalette
6. 未使用绝对路径查找 DCI 图标
7. 未滥用 setDciThemeSearchPaths()

## 验证要点

- [ ] #include <DDciIconPlayer>
- [ ] setIcon() 设置图标
- [ ] play() 开始播放
- [ ] 连接 updated 信号更新显示

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未使用 QSS 替代 DPalette
- [ ] 未使用绝对路径查找 DCI 图标
- [ ] 未滥用 setDciThemeSearchPaths()
