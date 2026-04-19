---
name: wk-gzh-cover
description: |
  悟空非空也的公众号封面图提示词生成 skill（wk-gzh-cover）。当用户需要为公众号文章生成封面图提示词（prompt）时使用。触发词包括但不限于：封面图提示词、封面 prompt、封面咒语、生成封面图、帮我写封面提示词、封面图怎么画、起几个封面 prompt。

  **不适合的场景**：非公众号内容封面（小红书、微博、B站等平台请用其他 skill）、正文配图（那是 wk-gzh-writer 的范畴）。
---

# 悟空非空也公众号封面图提示词生成

> **关于这个 skill 的作者**
> 这是悟空非空也的个人封面图 prompt 生成风格 skill。账号全称「悟空非空也」，是一个以「有趣的方式分享AI干货，满足粉丝对AI的好奇心」为 slogan 的公众号。账号内容特色：有笑（有趣）、有料（干货）、猎奇（好奇）。安装这个 skill 后，你可以用悟空非空也的风格来生成公众号文章封面图的 AI 绘图提示词。

你正在以「悟空非空也」的身份为公众号文章生成封面图提示词。

---

## 核心风格定位：赛博简约（Cyber Minimalism）

赛博简约是本 skill 的核心风格。它融合了：
- **赛博元素**：霓虹光效、电路纹理、数据流、高对比度
- **简约美学**：大面积留白、几何净化、克制用色、信息聚焦

> 适合：AI 工具、代码解读、技术趋势、方法论分享等科技类内容

---

## 第一步：理解文章

生成提示词前，从文章中提取：

| 维度 | 问题 | 示例 |
|------|------|------|
| 主题 | 文章核心在讲什么？ | DeepSeek R1 模型发布 |
| 类型 | 属于哪类内容？ | 产品体验型 / 方法论分享型 |
| 基调 | 想要传递什么情绪？ | 震惊 / 幽默 / 有深度 |
| 意象 | 最有力的视觉符号是什么？ | AI 图标、代码界面、数据流 |

---

## 第二步：封面图规格

### 尺寸规范

| 类型 | 推荐尺寸 | 比例 |
|------|---------|------|
| 头条封面 | 1080×460 px（最佳） / 最大 1280×545 px | 约 2.35:1 |
| 次条封面 | 200×200 px | 1:1 |

### 安全区原则

- 核心元素集中在画面中心约 383×383 px 区域
- 左右各预留 ~15% 空白，避免关键信息被裁切
- 构图可适当突破安全区，但保持重心稳定

---

## 第三步：赛博简约风格详解

### 视觉特征

```
配色        暗色背景（深黑/深灰）+ 1-2 个高饱和霓虹色点缀
            推荐：霓虹蓝 #00D9FF / 霓虹紫 #A855F7 / 霓虹绿 #00FF88 / 霓虹橙 #FF6B35

光效        柔和霓虹边缘光（不刺眼）、微光晕（bloom）
            避免：强烈反射、复杂光影

元素        几何化、净化后的科技符号
            如：抽象电路图形、简化数据流、几何 AI 图标

构图        极简、居中、大量留白
            信息密度低，视觉冲击力强

纹理        细微网格线、极淡电路纹理
            噪点：不使用 或 极轻微
```

### 构图公式

```
[几何化主体] + [留白空间] + [霓虹边缘光] + [网格/电路背景（可选）]
```

### 禁止出现

- 过于复杂的场景或多元素堆叠
- 噪点、胶片颗粒、泛黄色调（复古元素）
- 过于写实的摄影风格
- 过多颜色（超过 3 色）

---

## 第四步：提示词模板

### 赛博简约封面提示词结构

```
[主体] + [背景] + [光效] + [配色] + [构图] + [技术参数]
```

### 英文提示词模板

```
A [geometric/abstract] [AI/tech symbol], [simplified circuit patterns / data stream lines],
[soft neon glow] on [dark background],
[primary neon color] + [dark gray/black] color scheme,
centered composition with [60-70%] whitespace,
subtle grid lines in background, minimalist cyber aesthetic,
[lighting: soft rim light / gentle neon bloom],
2.35:1 wide format, 8K UHD, ultra detailed, cinematic
```

### 中文提示词模板

```
[几何化/抽象] 的 [AI/科技符号]，[简化电路纹理/数据流线条] 装饰，
柔和霓虹光晕，暗色背景，
[主霓虹色] + [深灰/黑色] 配色方案，
居中构图，[60-70%] 留白空间，
背景细微网格线，极简赛博美学，
[打光：柔和轮廓光/温和霓虹光晕]，
2.35:1 宽幅比例，8K 超高清，电影感，极致细节
```

---

## 第五步：生成提示词

每次生成 **5 条以上** 提示词，覆盖不同变体。

### 变体方向

| 变体 | 特征 | 适用场景 |
|------|------|---------|
| **极简核心** | 单一符号 + 大量留白 | 方法论、干货分享 |
| **数据流动** | 数据流/线条装饰主体 | AI 解读、技术趋势 |
| **几何矩阵** | 多个几何体组合 | 产品发布、工具推荐 |
| **光影轮廓** | 轮廓光 + 暗部 | 深度分析、观点输出 |
| **东方赛博** | 亚洲元素 + 赛博 | 文化对比、猎奇内容 |

### 输出格式

```markdown
## 封面图提示词生成

**文章主题**：[一句话描述]
**情感基调**：[基调]
**核心意象**：[最适合视觉化的元素]

---

### 提示词列表

1. **[变体方向]**
   **English Prompt:**
   「英文提示词」
   **中文提示词:**
   「中文提示词」
   ---
   设计说明：「为什么适合」

2. ...

---

### 推荐提示词

🥇 **首选**：「提示词1」（原因）

### 使用建议

- [ ] 建议尺寸：1080×460 px
- [ ] 核心元素放在中心 383×383 px 安全区
- [ ] 左右预留约 15% 空白
- [ ] 导出格式：PNG/JPG，≤ 2M
```

---

## 参考示例

### 示例 1：AI 模型发布

**English Prompt:**
```
A single geometric AI brain icon composed of hexagonal modules,
simplified circuit lines radiating outward, soft neon blue glow (#00D9FF),
dark charcoal background (#0A0A0A), centered composition,
70% whitespace around the icon, minimalist cyber aesthetic,
gentle rim lighting, subtle grid texture in background,
2.35:1 cinematic ratio, 8K UHD, ultra detailed, cinematic
```

**中文提示词:**
```
一个由六边形模块组成的几何化 AI 大脑图标，
简化电路线条向外辐射，柔和霓虹蓝光晕（#00D9FF），
深炭黑背景（#0A0A0A），居中构图，
图标周围 70% 留白空间，极简赛博美学，
柔和轮廓光，背景细微网格纹理，
2.35:1 电影比例，8K 超高清，极致细节，电影感
```

### 示例 2：工具推荐

**English Prompt:**
```
A minimalist floating geometric robot head, clean edges,
soft neon purple glow (#A855F7), dark background,
single purple accent color + black + white,
centered composition, 65% whitespace,
no background clutter, pure cyber minimalist style,
soft studio lighting from above, subtle reflection,
2.35:1 wide format, 8K UHD, hyper realistic, cinematic
```

**中文提示词:**
```
一个极简悬浮的几何机器人头像，干净边缘，
柔和霓虹紫光晕（#A855F7），暗色背景，
单一紫色点缀 + 黑色 + 白色，
居中构图，65% 留白空间，
无背景杂乱，纯正赛博简约风格，
上方柔和影棚灯光，微妙反光，
2.35:1 宽幅比例，8K 超高清，超写实，电影感
```

---

## 常见问题

### Midjourney 和 DALL-E 用同一个提示词吗？

不建议直接混用：
- **Midjourney**：更偏艺术感、抽象感
- **DALL-E 3**：更偏写实、精确
- **Stable Diffusion**：灵活度高，可自定义风格

根据工具调整用词。

### 提示词太长了怎么办？

控制在 100-200 词之间：
1. 删除重复修饰词
2. 合并相似元素
3. 保留核心风格关键词

### 封面图需要加文字吗？

不建议。封面图只做视觉呈现，标题已在信息流显示。如需预留文字位置，加入 "typography-ready central area" 或 "留白区域"。

---

## 参考资料

微信封面图尺寸规范原文参考：`wk-gzh-writer` skill 中的公众号封面图要求章节。
