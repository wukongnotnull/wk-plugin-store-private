## 项目概述

这是一个单页 HTML 幻灯片网站，采用卡片式布局营造层次感，支持键盘切换幻灯片。

## 技术栈

- HTML
- CSS（CSS Grid + Flexbox）
- JavaScript（键盘事件 + 幻灯片切换）


## 页面架构

每张幻灯片为 `<section class="slide">`，仅当前活动幻灯片显示（`display: grid`），其他隐藏。使用 CSS Grid `place-items: center` 实现内容居中。

## 卡片系统

### 核心卡片组件

| 组件 | 说明 |
|------|------|
| `.card` | 通用卡片，带顶部渐变强调线 |
| `.data-card` | 数据展示卡片，含图标 + 大号数字 value + 描述 label |
| `.stat` | 统计数据卡片，含 num + unit |
| `.timeline-card` | 时间线卡片，含 year + event，带左侧渐变竖线 |
| `.comparison-card` | 对比数据卡片，含图标 + 名称 + 分数 + 增幅 |
| `.feature-card` | 特性卡片，2×2 网格布局，带编号和图标 |

### 卡片设计规范

- 背景：`rgba(255,140,50,0.03~0.05)` — 微妙的琥珀色透明层
- 边框：`1px solid rgba(255,140,50,0.10~0.15)`
- 左侧强调线：3px 实色边框或顶部渐变
- 圆角：`4px ~ 8px`
- 内边距：`clamp(0.75rem, 1.5vw, 1.5rem)`
- Hover 效果：上浮 `translateY(-2px ~ -4px)` + 边框发光

### 卡片网格

- `data-grid`：`repeat(auto-fit, minmax(200px, 1fr))`
- `feature-grid`：`repeat(2, 1fr)` — 2 列布局
- `stats-row`：`flex-wrap: wrap`

## 色彩系统

| 用途 | 色值 |
|------|------|
| 背景 | `#0d0b08` (深暖黑) |
| 主强调色 | `#ff8c32` (琥珀橙) |
| 次强调色 | `#ff6600` (深橙) |
| 文字 | `#ffffff` / `rgba(255,255,255,0.5)` |
| 分类条 | `#ff6600` / `#cc4400` |

## 字体

- **标题**: `Archivo Black` — 粗壮无衬线
- **正文/数据**: `Space Grotesk` — 现代几何无衬线

## 视觉元素

1. **顶部/底部分类条** — 橙黑交替条纹，动效滑入 (`barSlide`)
2. **左侧竖线** — 渐变橙色竖线，5%-95%高度
3. **径向渐变光晕** — 左下/右下局部暖色点缀
4. **文档编号** — 顶部小字，等宽字符间距 `0.3em`

## 动效

- `reveal`: 切换幻灯片时触发渐入 (`opacity 0 → 1`, `translateY(30px) → 0`)
- `barSlide`: 分类条从左向右展开
- 延迟递增: `0.1s` → `0.2s` → `0.3s` → `0.4s` 形成层次节奏

## 动画原则

- 所有动效 300-700ms，`ease-out` 或 `ease` 时序
- `prefers-reduced-motion` 媒体查询兜底，禁用所有动画

## 创建新幻灯片

参考现有幻灯片结构，将内容放入 `.slide` 中，每张幻灯片需包含 `.content` 容器保持居中布局。
