# Weather Tray Plugin (天气托盘插件)

DDE 任务栏天气托盘插件，实时显示天气信息。

## 功能

- 托盘区显示天气图标和温度（宽度 32px）
- 鼠标悬停提示天气状况及温度
- 单击打开 uos-weather 天气应用
- 右键菜单跳转天气应用设置
- 快捷面板显示详细天气信息（含一周天气预报）
- 支持控制中心显隐切换
- 读取 `~/.config/deepin/org.deepin.weather.conf` 配置文件实时刷新

## 依赖

- Qt 6 + C++17
- DTK 6 (Dtk6::Widget, Dtk6::Gui)
- `dde-tray-loader-dev`（接口头文件）

## 编译

```bash
mkdir build && cd build
cmake .. -DTRAY_LOADER_INTERFACE_DIR=/path/to/dde-tray-loader/interfaces
make
```

## 安装

```bash
sudo make install
```

插件安装到 `lib/dde-dock/plugins/weather.so`。

## 配置文件格式

天气数据从 `~/.config/deepin/org.deepin.weather.conf` 读取（QSettings INI 格式）：

```ini
[General]
cityName=北京
weatherName=晴
temp=25
icon=weather-clear
humidity=60
windDirection=东北风
windStrength=3级
updateTime=2024-01-01T12:00:00

[Forecast0]
dayOfWeek=今天
weatherName=晴
tempHigh=27
tempLow=18
icon=weather-clear

[Forecast1]
dayOfWeek=明天
weatherName=多云
tempHigh=28
tempLow=19
icon=weather-cloudy
```

## 项目结构

```
weather-tray-plugin/
├── weatherplugin.h       # 插件类声明
├── weatherplugin.cpp     # 插件类实现
├── weatherwidget.h       # 托盘主控件声明
├── weatherwidget.cpp     # 托盘主控件实现（天气图标+温度）
├── weatherdata.h         # 天气数据模型声明
├── weatherdata.cpp       # 天气数据读取与监听
├── weatherapplet.h       # 快捷面板弹窗声明
├── weatherapplet.cpp     # 快捷面板弹窗实现（详细天气+预报）
├── weather.json          # 插件元数据
├── weather.qrc           # Qt 资源文件
├── icons/                # 图标资源
│   ├── weather.svg       # 亮色图标
│   └── weather-dark.svg  # 暗色图标
├── CMakeLists.txt        # 构建配置
└── README.md             # 说明文档
```
