# org.deepin.dde.Graphic1 接口参考

该接口提供图像模糊、裁剪、合成、转换、翻转、缩放、旋转、缩略图生成等图像处理能力，以及颜色格式转换和主色调提取功能。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Graphic1` |
| Object path | `/org/deepin/dde/Graphic1` |
| Interface | `org.deepin.dde.Graphic1` |
| Bus | Session |

> **验证说明**：该接口为 Session 总线服务，当前环境无 X11 显示，无法进行运行时内省验证。以下方法签名基于 dde-api 源码（`graphic/exported_methods_auto.go`、`graphic/graphic.go`）确认。

## 图像处理方法

### BlurImage

对图像进行高斯模糊处理。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `sigma`（double, 类型 `d`）：高斯模糊的 sigma 值
  - `numSteps`（double, 类型 `d`）：模糊步数
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.BlurImage \
  "/path/to/input.png" "/path/to/output.png" 10.0 5.0 "png"
```

### ClipImage

裁剪图像的指定区域。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `x`（int32, 类型 `i`）：裁剪区域左上角 x 坐标
  - `y`（int32, 类型 `i`）：裁剪区域左上角 y 坐标
  - `w`（int32, 类型 `i`）：裁剪区域宽度
  - `h`（int32, 类型 `i`）：裁剪区域高度
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.ClipImage \
  "/path/to/input.png" "/path/to/output.png" 0 0 100 100 "png"
```

### CompositeImage

将两张图像合成为一张。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `compFile`（string, 类型 `s`）：叠加图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `x`（int32, 类型 `i`）：叠加位置 x 坐标
  - `y`（int32, 类型 `i`）：叠加位置 y 坐标
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.CompositeImage \
  "/path/to/base.png" "/path/to/overlay.png" "/path/to/output.png" 10 10 "png"
```

### CompositeImageUri

将两个 data URI 格式的图像合成为一个 data URI。

- **输入参数**:
  - `srcDataUri`（string, 类型 `s`）：源图像的 data URI
  - `compDataUri`（string, 类型 `s`）：叠加图像的 data URI
  - `x`（int32, 类型 `i`）：叠加位置 x 坐标
  - `y`（int32, 类型 `i`）：叠加位置 y 坐标
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: `resultDataUri`（string, 类型 `s`）：合成后的 data URI

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.CompositeImageUri \
  "data:image/png;base64,..." "data:image/png;base64,..." 10 10 "png"
```

### ConvertDataUriToImage

将 data URI 转换为图像文件。

- **输入参数**:
  - `dataUri`（string, 类型 `s`）：图像的 data URI
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.ConvertDataUriToImage \
  "data:image/png;base64,..." "/path/to/output.png" "png"
```

### ConvertImage

将图像从一种格式转换为另一种格式。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.ConvertImage \
  "/path/to/input.bmp" "/path/to/output.png" "png"
```

### ConvertImageToDataUri

将图像文件转换为 data URI。

- **输入参数**:
  - `imgfile`（string, 类型 `s`）：图像文件路径
- **返回值**: `dataUri`（string, 类型 `s`）：图像的 data URI

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.ConvertImageToDataUri \
  "/path/to/input.png"
```

### FillImage

根据指定样式生成目标尺寸的新图像。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `width`（int32, 类型 `i`）：目标宽度
  - `height`（int32, 类型 `i`）：目标高度
  - `style`（string, 类型 `s`）：填充样式（`tile` 或 `center`）
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.FillImage \
  "/path/to/input.png" "/path/to/output.png" 1920 1080 "center" "png"
```

### FlipImageHorizontal

水平翻转图像。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.FlipImageHorizontal \
  "/path/to/input.png" "/path/to/output.png" "png"
```

### FlipImageVertical

垂直翻转图像。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.FlipImageVertical \
  "/path/to/input.png" "/path/to/output.png" "png"
```

### GetDominantColorOfImage

获取图像的主色调（HSV 格式）。

- **输入参数**:
  - `imgFile`（string, 类型 `s`）：图像文件路径
- **返回值**:
  - `h`（double, 类型 `d`）：色相（0~360）
  - `s`（double, 类型 `d`）：饱和度（0~1）
  - `v`（double, 类型 `d`）：明度（0~1）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.GetDominantColorOfImage \
  "/path/to/input.png"
```

### GetImageSize

获取图像的宽度和高度。

- **输入参数**:
  - `imgFile`（string, 类型 `s`）：图像文件路径
- **返回值**:
  - `width`（int32, 类型 `i`）：图像宽度
  - `height`（int32, 类型 `i`）：图像高度

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.GetImageSize \
  "/path/to/input.png"
```

### Hsv2Rgb

将 HSV 颜色转换为 RGB 颜色。

- **输入参数**:
  - `h`（double, 类型 `d`）：色相（0~360）
  - `s`（double, 类型 `d`）：饱和度（0~1）
  - `v`（double, 类型 `d`）：明度（0~1）
- **返回值**:
  - `r`（uint8, 类型 `y`）：红色分量（0~255）
  - `g`（uint8, 类型 `y`）：绿色分量（0~255）
  - `b`（uint8, 类型 `y`）：蓝色分量（0~255）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.Hsv2Rgb \
  120.0 1.0 1.0
```

### ResizeImage

调整图像尺寸到指定的宽度和高度。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `newWidth`（int32, 类型 `i`）：目标宽度
  - `newHeight`（int32, 类型 `i`）：目标高度
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.ResizeImage \
  "/path/to/input.png" "/path/to/output.png" 800 600 "png"
```

### Rgb2Hsv

将 RGB 颜色转换为 HSV 颜色。

- **输入参数**:
  - `r`（uint8, 类型 `y`）：红色分量（0~255）
  - `g`（uint8, 类型 `y`）：绿色分量（0~255）
  - `b`（uint8, 类型 `y`）：蓝色分量（0~255）
- **返回值**:
  - `h`（double, 类型 `d`）：色相（0~360）
  - `s`（double, 类型 `d`）：饱和度（0~1）
  - `v`（double, 类型 `d`）：明度（0~1）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.Rgb2Hsv \
  "byte 0" "byte 255" "byte 0"
```

### RotateImageLeft

将图像向左旋转 90 度。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.RotateImageLeft \
  "/path/to/input.png" "/path/to/output.png" "png"
```

### RotateImageRight

将图像向右旋转 90 度。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.RotateImageRight \
  "/path/to/input.png" "/path/to/output.png" "png"
```

### ThumbnailImage

按最大宽度和高度限制生成缩略图（等比缩放）。

- **输入参数**:
  - `srcFile`（string, 类型 `s`）：源图像路径
  - `dstFile`（string, 类型 `s`）：目标图像路径
  - `maxWidth`（uint32, 类型 `u`）：最大宽度
  - `maxHeight`（uint32, 类型 `u`）：最大高度
  - `format`（string, 类型 `s`）：输出格式（`png` 或 `jpeg`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --session \
  --dest org.deepin.dde.Graphic1 \
  --object-path /org/deepin/dde/Graphic1 \
  --method org.deepin.dde.Graphic1.ThumbnailImage \
  "/path/to/input.png" "/path/to/output.png" 200 200 "png"
```
