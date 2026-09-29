# org.deepin.dde.daemon.ambient-brightness DConfig 配置参考

该文件文档化环境亮度感知的 DConfig 配置项，包括自动亮度开关、映射模式、加权窗口、lux-亮度曲线、滞回比例和防抖时间。仅介绍 visibility 为 public 的配置项。

## 配置项总览

共 9 个 public 配置项。

## 自动亮度控制

### ambientLightAdjustBrightness

- **类型**：`boolean`
- **默认值**：false
- **权限**：readwrite
- **功能**：启用或禁用环境光自动亮度。启用时，服务声明传感器、读取 lux 并发布推荐亮度；禁用时，服务释放传感器声明并停止推荐

## 映射模式

### continuousMappingMode

- **类型**：`string`
- **默认值**：`steps`
- **权限**：readwrite
- **功能**：映射模式。steps 表示 lux 落入某个档位区间时输出该区间固定亮度（默认）；curve 表示在 log1p(lux) 空间对控制点做连续插值

### continuousLuxCurve

- **类型**：`array`
- **默认值**：`[{"lux":20,"brightness":0.2},{"lux":120,"brightness":0.4},{"lux":220,"brightness":0.6},{"lux":320,"brightness":0.8},{"lux":650,"brightness":0.9},{"lux":2000,"brightness":1.0}]`
- **权限**：readwrite
- **功能**：由 {lux, brightness} 控制点组成的 JSON 数组。至少需要两个点；lux 必须是有限、非负且严格递增的数值；brightness 必须位于 [0,1] 且单调不降。steps 模式下相邻 lux 的中点作为初始中性边界，每个控制点提供固定亮度；curve 模式下在 log1p(lux) 空间线性插值。配置无效时回退到内置默认值

### stepHysteresisRatio

- **类型**：`double`
- **默认值**：0.6
- **权限**：readwrite
- **功能**：仅 steps 模式下生效。有效范围 [0.5, 1.0]。对于相邻 lux 点 a<b，变亮阈值为 a+ratio*(b-a)，变暗阈值为 b-ratio*(b-a)。0.5 不产生滞回带；值越大滞回带越宽

## 加权窗口

### useWeightedWindows

- **类型**：`boolean`
- **默认值**：false
- **权限**：readwrite
- **功能**：是否使用 fast/slow 时间加权窗口平滑传感器数据。true 时 ambientLightHorizonMs 和 fastLightHorizonMs 生效；false 时直接使用最新 rawLux，依靠防抖和滞回，适合约 800ms 上报一次的低频传感器

### ambientLightHorizonMs

- **类型**：`int32`
- **默认值**：10000
- **权限**：readwrite
- **功能**：慢加权窗口时长，单位毫秒。仅 useWeightedWindows=true 时生效。有效范围 (0, 10000]，且必须大于或等于 fastLightHorizonMs。值越大越稳定，但响应越慢

### fastLightHorizonMs

- **类型**：`int32`
- **默认值**：1000
- **权限**：readwrite
- **功能**：快加权窗口时长，单位毫秒。仅 useWeightedWindows=true 时生效。有效范围 (0, ambientLightHorizonMs]。值越小响应越快，但平滑能力越弱

## 防抖时间

### brightenDebounceMs

- **类型**：`int32`
- **默认值**：2000
- **权限**：readwrite
- **功能**：变亮防抖时间，单位毫秒。lux 必须连续高于变亮阈值达到该时长，才发布更亮的推荐值。有效范围 >= 0。值越大越能过滤短暂闪光，但响应越慢

### darkenDebounceMs

- **类型**：`int32`
- **默认值**：2000
- **权限**：readwrite
- **功能**：变暗防抖时间，单位毫秒。lux 必须连续低于变暗阈值达到该时长，才发布更暗的推荐值。有效范围 >= 0。值越大越能过滤短暂遮挡，但响应越慢

---
