---
name: wk-html-slides-amber-classified
description: |
  根据用户提供的 PPT 文字稿（markdown 格式），生成琥珀色机密文档风格的幻灯片网站。
  当用户提供演讲/演示文字稿、PPT 内容、幻灯片大纲，或请求创建幻灯片网站时触发。
  支持封面页、目录页、内容页（列表/卡片/数据/对比/时间线/引用）等多种幻灯片类型。
  **风格**：深暖黑背景 + 琥珀橙强调色 + 机密文档分类条 + Space Grotesk/Archivo Black 字体。
---

# wk-html-slides-amber-classified

根据 PPT 文字稿生成幻灯片网站。样式必须与 `index.html` 保持完全一致。

## 输入格式

用户提供 PPT 文字稿（markdown 格式），应包含：
- 幻灯片编号和标题（如 `## 第1页：封面`）
- 各类内容：标题、副标题、列表、数据、引用等

## 输出要求

生成单个 `index.html` 文件，包含：
- 所有幻灯片 section
- 内联 CSS 样式（从 index.html 复制的样式系统）
- 键盘导航 JavaScript
- **禁止滚动条**：`html { overflow: hidden; }`
- **内容垂直居中**：使用 CSS Grid `place-items: center`

## 核心样式规范

### 色彩系统

```css
:root {
  --bg: #0d0b08;           /* 深暖黑背景 */
  --accent: #ff8c32;        /* 琥珀橙主强调色 */
  --accent-dark: #ff6600;   /* 深橙次强调色 */
  --text: #ffffff;
  --text-muted: rgba(255,255,255,0.5);
  --text-dim: rgba(255,255,255,0.35);
}
```

### 字体

```html
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@300;400;500;700&display=swap" rel="stylesheet">
```

- 标题：`font-family: 'Archivo Black', sans-serif`
- 正文/数据：`font-family: 'Space Grotesk', sans-serif`

## 幻灯片结构模板

```html
<div class="classified-bar"></div>
<div class="classified-bar-bottom"></div>

<section class="slide active">
  <div class="content">
    <div class="left-border"></div>
    <div class="doc-id">DOC-ID</div>
    <div class="eyebrow">眉毛标题</div>
    <h1>主标题 <span class="accent">强调词</span></h1>
    <div class="divider"></div>
    <!-- 内容区域 -->
  </div>
</section>
```

### CSS 容器规则

```css
.slide {
  height: 100dvh;
  display: none;
  grid-template-rows: 1fr;
  place-items: center;
  padding: 2rem clamp(2rem, 8vw, 6rem);
}
.slide.active { display: grid; }
.content {
  position: relative; z-index: 2;
  max-width: 900px; width: 100%;
  text-align: left;
  padding-left: clamp(2rem, 4vw, 3rem);
}
```

## 组件选择规则（关键）

### 1. 纯文本列表 → 使用 `ul > li`

当内容是**要点列表、步骤、条目**时，使用 `.card > ul > li`：

```html
<div class="card">
  <ul>
    <li>第一点内容</li>
    <li>第二点内容</li>
    <li>第三点内容</li>
  </ul>
</div>
```

```css
.card { background: rgba(255,140,50,0.03); border: 1px solid rgba(255,140,50,0.12); border-radius: 8px; padding: clamp(1.25rem, 2.5vw, 2rem); }
.card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, var(--accent), var(--accent-dark), transparent); }
ul { list-style: none; }
ul li { position: relative; padding-left: clamp(1.5rem, 3vw, 2rem); margin-bottom: clamp(0.75rem, 1.5vh, 1rem); }
ul li::before { content: ''; position: absolute; left: 0; top: 0.6em; width: 8px; height: 8px; background: var(--accent); transform: rotate(45deg); }
```

**何时使用**：Q1-Q4业绩、要点清单、步骤列表、功能列表

### 2. 并列特性/功能（2-4项） → 使用 `.feature-grid > .feature-card`

当有**多个并列的特性、功能、成就**需要突出展示时：

```html
<div class="feature-grid">
  <div class="feature-card">
    <span class="number">01</span>
    <div class="title">特性名称</div>
    <div class="desc">特性描述</div>
  </div>
  <div class="feature-card">
    <span class="number">02</span>
    <div class="title">特性名称</div>
    <div class="desc">特性描述</div>
  </div>
</div>
```

```css
.feature-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: clamp(1rem, 2vw, 1.5rem); }
.feature-card { background: rgba(255,140,50,0.04); border: 1px solid rgba(255,140,50,0.1); border-radius: 8px; padding: clamp(1rem, 2vw, 1.5rem); position: relative; overflow: hidden; }
.feature-card .number { font-family: 'Archivo Black', sans-serif; font-size: clamp(2rem, 4vw, 3rem); color: rgba(255,140,50,0.15); position: absolute; top: -0.5rem; right: 0.5rem; }
.feature-card .title { font-family: 'Archivo Black', sans-serif; font-size: clamp(0.85rem, 1.3vw, 1rem); color: var(--accent); margin-bottom: 0.5rem; }
.feature-card .desc { font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: var(--text-muted); line-height: 1.6; }
```

**何时使用**：核心功能展示、产品特性、优势对比

### 3. 数据指标 → 使用 `.data-grid > .data-card`

当有**数值、数据、统计指标**需要突出时：

```html
<div class="data-grid">
  <div class="data-card">
    <div class="icon">📊</div>
    <div class="value">83.1%</div>
    <div class="label">漏洞利用</div>
  </div>
</div>
```

```css
.data-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: clamp(1rem, 2vw, 1.5rem); }
.data-card { background: rgba(255,140,50,0.05); border: 1px solid rgba(255,140,50,0.15); border-radius: 4px; padding: clamp(1rem, 2vw, 1.5rem); position: relative; }
.data-card::before { content: ''; position: absolute; top: 0; left: 0; width: 3px; height: 100%; background: var(--accent); border-radius: 4px 0 0 4px; }
.data-card .icon { font-size: clamp(1.5rem, 2.5vw, 2rem); margin-bottom: 0.75rem; }
.data-card .value { font-family: 'Archivo Black', sans-serif; font-size: clamp(1.5rem, 3vw, 2.2rem); color: var(--accent); line-height: 1; }
.data-card .label { font-size: clamp(0.7rem, 1vw, 0.85rem); color: var(--text-muted); margin-top: 0.5rem; }
```

**何时使用**：百分比、金额、用户数、增长率等量化数据

### 4. 时间线 → 使用 `.timeline > .timeline-card`

当内容涉及**时间顺序、阶段、历程**时：

```html
<div class="timeline">
  <div class="timeline-card">
    <div class="year">💰 $1亿</div>
    <div class="event">事件描述</div>
  </div>
</div>
```

```css
.timeline { position: relative; padding-left: 2rem; }
.timeline::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, var(--accent), transparent); }
.timeline-card { position: relative; margin-bottom: clamp(0.75rem, 1.5vh, 1rem); padding: clamp(0.75rem, 1.5vw, 1rem) clamp(1rem, 2vw, 1.25rem); background: rgba(255,140,50,0.04); border: 1px solid rgba(255,140,50,0.1); border-radius: 6px; }
.timeline-card::before { content: ''; position: absolute; left: -2rem; top: 50%; transform: translateY(-50%) rotate(45deg); width: 10px; height: 10px; background: var(--accent); box-shadow: 0 0 15px rgba(255, 140, 50, 0.5); }
.timeline-card .year { font-family: 'Archivo Black', sans-serif; font-size: clamp(0.9rem, 1.3vw, 1.1rem); color: var(--accent); display: flex; align-items: center; gap: 0.5rem; }
.timeline-card .event { font-size: clamp(0.75rem, 1.1vw, 0.9rem); color: var(--text-muted); margin-top: 0.25rem; padding-left: 1.25rem; }
```

### 5. 统计数据 → 使用 `.stats-row > .stat`

当只有**少量关键数字**需要展示时（用于封面页等）：

```html
<div class="stats-row">
  <div class="stat">
    <div class="num">83.1%</div>
    <div class="unit">漏洞利用</div>
  </div>
</div>
```

```css
.stats-row { display: flex; flex-wrap: wrap; gap: clamp(1.5rem, 4vw, 3rem); margin-top: clamp(1.5rem, 3vh, 2.5rem); }
.stat .num { font-family: 'Archivo Black', sans-serif; font-size: clamp(1.8rem, 4vw, 3rem); color: var(--accent); line-height: 1; }
.stat .unit { font-size: clamp(0.6rem, 1vw, 0.75rem); color: var(--text-dim); letter-spacing: 0.1em; text-transform: uppercase; margin-top: 0.25rem; }
```

### 6. 引用 → 使用 `.quote`

```html
<div class="quote">引用内容</div>
```

```css
.quote { font-size: clamp(1.1rem, 2vw, 1.4rem); color: var(--text); font-style: italic; padding-left: 1.5rem; border-left: 3px solid var(--accent); margin: clamp(1.5rem, 3vh, 2rem) 0; }
```

## 动画

```css
.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease, transform 0.6s ease; }
.reveal.visible { opacity: 1; transform: translateY(0); }
.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
.reveal-delay-3 { transition-delay: 0.3s; }
.reveal-delay-4 { transition-delay: 0.4s; }
```

## 键盘导航

```javascript
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

function showSlide(index) {
  if (index < 0) index = 0;
  if (index >= totalSlides) index = totalSlides - 1;
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    if (i === index) {
      slide.classList.add('active');
      slide.querySelectorAll('.reveal').forEach(el => {
        el.classList.remove('visible');
        void el.offsetWidth;
        setTimeout(() => el.classList.add('visible'), 50);
      });
    }
  });
  currentSlide = index;
}

document.addEventListener('keydown', (e) => {
  if (e.code === 'Space') { e.preventDefault(); showSlide(currentSlide + 1); }
  if (e.code === 'ArrowRight' || e.code === 'ArrowDown') { e.preventDefault(); showSlide(currentSlide + 1); }
  if (e.code === 'ArrowLeft' || e.code === 'ArrowUp') { e.preventDefault(); showSlide(currentSlide - 1); }
});

showSlide(0);
```

## 内容类型决策流程

```
解析内容 → 判断类型 → 选择组件

1. 是要点/步骤列表吗？
   → YES: 使用 ul > li (在 .card 内)

2. 是2-4个并列特性吗？
   → YES: 使用 .feature-grid > .feature-card

3. 有具体数值/统计数据吗？
   → YES: 使用 .data-grid > .data-card

4. 涉及时间顺序吗？
   → YES: 使用 .timeline > .timeline-card

5. 是名人名言/结论吗？
   → YES: 使用 .quote

6. 只有少量关键数字（封面用）？
   → YES: 使用 .stats-row > .stat
```

## 常见错误避免

| 错误 | 正确做法 |
|------|----------|
| Q1/Q2/Q3/Q4 业绩用 feature-card | 应该用 `.card > ul > li` 展示列表 |
| 数字指标用 feature-card | 应该用 `.data-card` |
| 步骤流程用 data-card | 应该用 `.card > ul > li` |
| 忘记添加 `.reveal` 类 | 所有可见元素添加 `.reveal` 和延迟类 |

## 完整 HTML 结构

```html
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>幻灯片标题</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
/* 所有 CSS 样式 */
</style>
</head>
<body>
<div class="classified-bar"></div>
<div class="classified-bar-bottom"></div>

<!-- 幻灯片内容 -->

<script>
/* 导航脚本 */
</script>
</body>
</html>
```

## 将 HTML 幻灯片导出为 PNG 图片

用户请求将幻灯片导出为图片时，使用以下脚本：

### 环境准备

```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装 Playwright
pip install playwright
playwright install chromium
```

### 截图脚本 (scripts/capture_slides.py)

```python
#!/usr/bin/env python3
"""将 HTML 幻灯片截图为 PNG 图片"""

import asyncio
from playwright.async_api import async_playwright
import os
import sys

# 配置
HTML_FILE = sys.argv[1] if len(sys.argv) > 1 else "index.html"
OUTPUT_DIR = sys.argv[2] if len(sys.argv) > 2 else "slides"
SCALE = int(sys.argv[3]) if len(sys.argv) > 3 else 2  # 默认2倍清晰度

async def capture_slides():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=SCALE  # 2=4K, 3=8K
        )

        await page.goto(f"file://{os.path.abspath(HTML_FILE)}")
        await page.wait_for_timeout(1500)  # 等待字体加载

        slide_count = await page.locator(".slide").count()
        print(f"共 {slide_count} 张幻灯片")

        for i in range(slide_count):
            if i > 0:
                await page.keyboard.press("Space")
                await page.wait_for_timeout(800)  # 等待动画

            filename = f"{OUTPUT_DIR}/slide-{i+1:02d}.png"
            await page.screenshot(path=filename, full_page=False)
            print(f"已保存: {filename}")

        await browser.close()
        print("完成!")

if __name__ == "__main__":
    asyncio.run(capture_slides())
```

### 使用方式

```bash
# 基本用法
source venv/bin/activate
python scripts/capture_slides.py index.html slides/

# 高清模式 (4K)
python scripts/capture_slides.py index.html slides/ 2

# 超高清模式 (8K)
python scripts/capture_slides.py index.html slides/ 3
```

### 输出

- 分辨率：1920×1080 × scale
  - scale=1: 1920×1080 (约 400KB/张)
  - scale=2: 3840×2160 (约 1MB/张) **推荐**
  - scale=3: 5760×3240 (约 2MB/张)
- 文件：`slides/slide-01.png`, `slides/slide-02.png`, ...
