# 进度与加载控件规范

## 1. 概述与适用场景

| 控件 | 适用场景 |
|------|----------|
| `DProgressBar` | 确定进度条 |
| `DColoredProgressBar` | 彩色进度条 |
| `DIndeterminateProgressBar` | 不确定进度条（无具体进度） |
| `DCircleProgress` | 圆形进度指示 |
| `DWaterProgress` | 水波纹进度 |
| `DSpinner` | 旋转加载指示器 |
| `DLoadingIndicator` | 加载状态指示 |

## 2. 各控件用法

### 2.1 DProgressBar — 进度条

```cpp
#include <DProgressBar>

auto *bar = new DProgressBar(this);
bar->setRange(0, 100);
bar->setValue(50);
bar->setOrientation(Qt::Horizontal);
```

### 2.2 DIndeterminateProgressBar — 不确定进度

```cpp
#include <DIndeterminateProgressbar>

auto *bar = new DIndeterminateProgressbar(this);
// 自动显示动画，无需手动 start/stop
```

### 2.3 DSpinner — 旋转加载

```cpp
#include <DSpinner>

auto *spinner = new DSpinner(this);
spinner->start();  // 开始旋转
spinner->stop();   // 停止旋转
```

### 2.4 DCircleProgress — 圆形进度

```cpp
#include <DCircleProgress>

auto *progress = new DCircleProgress(this);
progress->setValue(75); // 0-100
```

### 2.5 DWaterProgress — 水波纹进度

```cpp
#include <DWaterProgress>

auto *progress = new DWaterProgress(this);
progress->setValue(60); // 0-100
progress->start();      // 开始水波动画
progress->stop();       // 停止
```

## 3. 选择决策

```
需要进度/加载？
    │
    ├─ 知道具体进度？
    │   ├─ 是 → 线性？ → DProgressBar
    │   │       圆形？ → DCircleProgress / DWaterProgress
    │   └─ 否 → DIndeterminateProgressBar / DSpinner
    │
    └─ 仅需加载提示？
        └─ DSpinner / DLoadingIndicator
```

## 4. 相关文档

- [index.md](index.md) - 控件选择决策树
