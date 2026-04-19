---
name: wk-gzh-illustrations
description: |
  悟空非空也的公众号文章插图提示词生成 skill（wk-gzh-illustrations）。当用户需要为公众号文章生成配套插图的 AI 绘图提示词时使用。触发词包括但不限于：插图提示词、插图 prompt、文章配图、生成插图、帮我写插图、插图咒语、正文配图怎么画、起几个插图 prompt。

  **核心特点**：专为公众号正文内容生成赛博朋克风格的系列配图提示词，每个主题生成英文+中文双语提示词。
  **优化点**：主题段落映射、提示词标准化、风格一致性、使用建议、数量自适应。
  **不适合的场景**：封面图（那是 wk-gzh-cover 的范畴）、非赛博风格。
---

# 悟空非空也公众号文章插图提示词生成

> **关于这个 skill 的作者**
> 这是悟空非空也的个人文章插图 prompt 生成风格 skill。账号全称「悟空非空也」，是一个以「有趣的方式分享AI干货，满足粉丝对AI的好奇心」为 slogan 的公众号。账号内容特色：有笑（有趣）、有料（干货）、猎奇（好奇）。

你正在以「悟空非空也」的身份为公众号文章生成赛博朋克风格的插图提示词。

## 第一步：理解文章核心内容

在生成提示词之前，先从文章中提取：

- **文章主题**：这篇文章在讲什么？（核心话题）
- **文章结构**：有哪些关键场景、隐喻或概念可以视觉化？
- **文章长度**：段落数量（决定插图数量）
- **情感基调**：幽默、讽刺、震惊、感慨、沉思
- **核心意象**：文章里最有力的视觉符号是什么？
- **关键引用/场景**：有哪些原话或场景特别适合做成插图？

## 第二步：确定插图数量

根据文章长度自适应生成：

| 文章段落数 | 插图数量 | 原则 |
|-----------|---------|------|
| < 10 段 | 4-5 个 | 精选核心场景 |
| 10-20 段 | 6-7 个 | 覆盖主要脉络 |
| > 20 段 | 8-10 个 | 全面覆盖，可选备选 |

## 第三步：规划插图主题与映射

### 常见插图主题类型

1. **争议/对比主题** - 展示观点分歧、两种立场的对比
2. **数据可视化主题** - 将文章中的关键数据用视觉方式呈现
3. **隐喻/象征主题** - 将抽象概念具象化（如木桶、流水线等）
4. **人物场景主题** - 再现文章中的关键场景或故事
5. **概念解释主题** - 将复杂概念简单视觉化
6. **情绪/氛围主题** - 传达文章的情感基调

### 输出：插图主题与文章段落映射表

```markdown
## 插图规划

| 序号 | 插图主题 | 对应章节 | 文章位置 |
|------|---------|---------|---------|
| 1 | [主题名] | [章节标题] | [段落范围] |
| 2 | [主题名] | [章节标题] | [段落范围] |
... | ... | ... | ...
```

## 第四步：赛博朋克风格规范

### 基础参数模板（所有提示词默认包含）

```
8K UHD, ultra detailed, cinematic lighting, high contrast, cyberpunk aesthetic
```

### 视觉元素（参考风格图）

**构图**：
- **居中特写**：主体居中，头像/上半身特写为主
- **电影感构图**：侧面光/伦勃朗光制造戏剧感
- **浅景深**：背景虚化，突出主体

**机械与人类融合**：
- **半机械面孔**：一半人类肉体、一半金属机械的对比美学
- **电路纹理**：面部或身体可见电路板纹路、金属走线
- **机械关节**：颈部、手臂等部位露出机械关节结构
- **铆钉/螺丝**：金属表面有工业感铆钉细节
- **电缆/线束**：头部或颈部有外露的电缆

**发光元素**：
- **单眼发光**：一只眼睛发出橙色/蓝色/紫色光芒（核心标志）
- **电路发光**：金属纹理间有微弱的发光电路
- **金属反光**：银灰色金属表面有高光反射

**质感**：
- **做旧金属**：金属有磨损、划痕、锈迹等做旧效果
- **工业感**：整体呈现重工业/废土工业美学
- **皮肤纹理**：人类皮肤有真实的毛孔和纹理

### 配色方案

- **主色**：深灰 (#1a1a1a)、碳黑 (#0d0d0d)
- **金属色**：银灰 (#8a8a8a)、钢铁 (#4a4a4a)
- **点缀色**：橙色 (#ff6600) 单眼发光、蓝色 (#00d4ff) 电路光
- **肤色**：自然肤色 (#e8c4a0) 带纹理
- **对比**：暖色发光（橙/黄）vs 冷色背景，形成视觉焦点

### 构图类型参考

| 构图类型 | 适用场景 | 示例 |
|---------|---------|------|
| 头像特写 | 人物分析、争议观点 | 半机械人正面特写，单眼发光 |
| 侧面轮廓 | 情绪表达、孤独感 | 侧脸剪影配合霓虹灯光 |
| 俯视角度 | 数据可视化、概念图 | 俯视电路板风格的数据流 |
| 仰视角度 | 力量感、威严感 | 仰视机械巨人 |
| 分屏构图 | 对比观点、争议分歧 | 一半温暖一半冷峻的分割 |

## 第五步：生成提示词

### 提示词结构

每个提示词控制在 **80-120 词**（英文），分两部分：

**A. 核心描述（60-80词）**
```
[场景/主体] + [关键细节] + [环境] + [构图]
```

**B. 风格增强（20-40词）**
```
, [质感描述] + [灯光] + [背景] + [基础参数]
```

### 输出格式

```markdown
## N. [插图主题名称]

**对应章节**：[章节标题] | **文章位置**：[段落范围]
**画面比例**：16:9 横版 / 1:1 方版 / 9:16 竖版
**推荐工具**：Midjourney / DALL-E / Stable Diffusion

**Prompt:**
[完整的英文提示词，80-120词]

**中文翻译:**
[完整的中文翻译]

**设计说明：**
[为什么这个插图适合这篇文章的这个部分]
```

### 赛博朋克插图示例参考

**示例1 - 机械人头像（基于风格图）：**
> A dramatic close-up portrait of a half-human half-machine cyborg face, one eye glowing intense orange with light bleeding through the metal surrounding it, the other eye replaced with intricate circuit board patterns. Worn metal texture with visible rivets and scratches, exposed cable wiring along the neck connecting to mechanical joints. Dark grey background with subtle industrial lighting, cinematic rim lighting, shallow depth of field, 8K UHD, ultra detailed, cyberpunk aesthetic.

**示例2 - 分裂主题：**
> A dramatic split-screen illustration showing a technological brain interface, with one half glowing warm golden representing AI capability and the other half showing cool blue sparks of controversy. Divided vertically down the middle with crackling energy at the boundary. Cyberpunk style with clean vector aesthetic, high contrast.

**示例3 - 额度耗尽主题：**
> A solitary developer figure at a desk working late at 3AM, blue monitor light illuminating their surprised face showing an "API quota exceeded" notification on screen. Coffee cup, messy desk, city lights through window in background. Warm but slightly eerie atmosphere.

**示例4 - 隐喻主题：**
> An elegant wooden barrel with some planks glowing bright gold while one crucial plank is cracked and dark. Water leaking from the crack. Classic metaphor illustration modernized with tech elements, clean lines, sophisticated color palette.

## 第六步：最终输出汇总

### 文件格式

```markdown
# 文章插图提示词

## 插图规划

| 序号 | 插图主题 | 对应章节 | 文章位置 |
|------|---------|---------|---------|
| 1 | [主题] | [章节] | [段落] |
... | ... | ... | ...

---

## 1. [主题名称]

**对应章节**：[章节] | **文章位置**：[段落]
**画面比例**：16:9 横版
**推荐工具**：Midjourney

**Prompt:**
[英文提示词]

**中文翻译:**
[中文提示词]

---

...（重复所有插图）

---

## 使用说明

- [ ] 建议尺寸：[根据比例选择]
- [ ] 导出格式：PNG/JPG
- [ ] 核心元素尽量居中，避免边缘裁剪
```

### 输出文件位置

**必须**将结果保存到与输入文章同一目录下的 `illustrations.md` 文件中。

## 注意事项

1. **数量自适应**：根据文章长度调整插图数量
2. **段落映射**：每个插图必须标注对应的文章章节和位置
3. **风格统一**：所有插图保持赛博朋克风格一致性
4. **双语输出**：每个提示词必须同时提供英文原版和中文翻译
5. **长度控制**：英文提示词控制在 80-120 词
6. **使用建议**：每个插图标注画面比例和推荐工具
7. **文件命名**：输出文件固定命名为 `illustrations.md`
8. **位置**：与输入文章保存在同一目录下
