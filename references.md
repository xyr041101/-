# References · 素材与参考来源

按"找灵感 / 拿图 / 拿图标 / 拿字体 / 拿组件"五类分开，每条都标了能不能商用。

## 1. 参考站（找方向，不是抄）

| 站点 | 用途 | 备注 |
|---|---|---|
| `mobbin.com` | 真实 App / Web 界面截图库，按场景筛 | 分付费，免费额度够看 |
| `refero.design` | 成组的产品页面截图 | 免费 |
| `godly.website` | 高质感站点合集，偏视觉冲击 | 免费 |
| `land-book.com` | Landing page 精选 | 免费 |
| `awwwards.com` | 获奖站点，看交互与动效 | 免费浏览 |

**用法**：先选 3–5 张参考截图存本地，作为"方向锚点"。让 AI 照着这批图做，比给形容词有效得多。

## 2. 图库（真实摄影优先）

| 来源 | 许可 | 备注 |
|---|---|---|
| `unsplash.com` | Unsplash License，免费商用 | 有 API，适合批量囤 |
| `pexels.com` | Pexels License，免费商用 | 有 API，`photos/fetch-photos.py` 用的是它 |
| `pixabay.com` | Pixabay License，免费商用 | 有 API |
| 厂商官网 / 展会官方图 | 需确认授权 | 工业设备实拍图最好的来源 |

注意：图库照片不能直接当"我们自己的产线照片"用。产品/项目页要真实场景，必须自己拍或用厂商授权图。

## 3. 图标

| 来源 | 数量 | 许可 | 用法 |
|---|---|---|---|
| `iconify` | 20 万+ | 混合（按集合看） | 一套 API 全站调用，最省事 |
| `lucide.dev` | 1000+ | ISC | 线性风格统一，最通用 |
| `phosphor-icons` | 7000+ | MIT | 多种线重，适合做层级 |
| `simpleicons.org` | 品牌 logo | 各品牌商标 | 只放技术栈 logo |

**规则**：一个项目只用一套图标，线重和圆角统一。混用是最常见的"廉价感"来源。

## 4. 字体（免费商用）

| 字体 | 类型 | 许可 | 适合 |
|---|---|---|---|
| 思源黑体 / Noto Sans SC | 中文黑体 | OFL | 正文、界面 |
| Inter | 英文无衬线 | OFL | 英文正文/数字 |
| Geist | 英文无衬线 | OFL | 科技感标题 |
| 思源宋体 / Noto Serif SC | 中文宋体 | OFL | 正式、文化类 |
| JetBrains Mono | 等宽 | OFL | 代码、编号、数据 |

**规则**：中文 + 英文各选一套，不要三套混排。数字统一用表格数字（`font-variant-numeric: tabular-nums`）。

## 5. 组件库（当底盘，别让 AI 自造样式）

| 库 | 适合 | 许可 |
|---|---|---|
| `shadcn/ui` | React/Tailwind，AI 工具默认都懂 | MIT |
| `meta/astryx` | Meta 开源设计系统，150+ 组件，专门为人和 AI 协作 | MIT |
| `HiUI 5.0`（小米） | AI Native，输出可直接交付的 React 代码 | 见官网 |
| `radix-ui/themes` | 无障碍底层 + 主题 | MIT |
| `daisyui` | Tailwind 组件类，轻量 | MIT |
| `Magic UI` / `Smooth UI` | 补动效和视觉细节（AI 生成最缺的部分） | MIT |

## 6. AI 建站工具（按身份选）

| 工具 | 适合 | 输出 |
|---|---|---|
| v0 | 开发者，React/Next | 干净可合并的代码 |
| Claude Design | 有自己设计系统 | 原型 + HTML/代码交接 |
| Figma Make | 已有 Figma 稿 | 可交互原型 |
| Google Stitch | 免费探索方向 | HTML/CSS |

## 7. 反面清单（避开这些，审美立刻回升）

- 紫色渐变 + 玻璃拟态 + 大圆角发光按钮（2023 年的 AI 味）
- 每个区块都加图标、都加阴影、都加边框
- 无意义的插画占满半屏，却没有一句说清产品是什么
- 中英混排字体不统一、行高不一致
- 所有卡片一样大、一样密，没有主次
