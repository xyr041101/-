# 图片素材池 · 使用说明

目标：把"临时找图"变成"从池子里挑"。池子越大，出图越快、风格越稳。

## 目录约定

```
photos/
  raw/<关键词>/        原始下载，按关键词分目录
  picked/              挑出来要用的（重命名为 用途-主体-编号）
  web/                 压缩后的成品（WebP，长边 ≤ 2000px）
```

## 第一步：拿 API Key（免费）

1. 打开 https://www.pexels.com/api/
2. 注册后创建应用，拿到 API Key（免费额度：200 次/小时、5000 次/月）
3. 设成环境变量，别写进代码：

```powershell
[Environment]::SetEnvironmentVariable('PEXELS_API_KEY', '你的key', 'User')
```

## 第二步：跑批量下载

```powershell
# 看语法
python photos\fetch-photos.py --help

# 按默认关键词表抓，每个词 30 张
python photos\fetch-photos.py --per-keyword 30
```

可选参数：
- `--keywords "机械臂,控制柜,车间"` 临时指定关键词
- `--per-keyword 50` 每个词抓多少张
- `--orientation landscape` 只要横图（`portrait` / `square`）
- `--min-width 1600` 过滤小图
- `--out photos\raw` 输出目录

## 默认关键词表（工业 / 自动化方向）

机械臂、自动化产线、控制柜、PLC、传感器、电池模组、车间、仓储物流、
伺服电机、工业相机、洁净车间、设备维护

改方向就直接改脚本顶部的 `DEFAULT_KEYWORDS`。

## 挑图标准（过不了就别放进 picked）

- 没有水印、没有大段文字、没有明显 AI 感
- 主体清楚，背景不抢
- 有真实细节（划痕、线缆、灰尘、反光）
- 色温能和白底界面共存（太黄太绿的不要）
- 横图够宽（≥ 1600px），能裁 16:9

## 授权

Pexels License：免费商用、可修改、无需署名，但**不能**把照片原样转售，
也不能用于暗示照片中的人/品牌为你的产品背书。工业设备照建议用厂商授权图或自己拍。
