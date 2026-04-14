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

## 第一步：理解文章内容与封面需求

在生成提示词之前，先从文章中提取：

- **文章主题**：这篇文章在讲什么？（核心话题）
- **文章类型**：调查实验型 / 产品体验型 / 现象解读型 / 工具分享型 / 方法论分享型
- **情感基调**：严谨、幽默、震惊、有深度、轻松、感慨
- **目标读者**：从业者、普通人、还是特定群体
- **核心意象**：文章里最有力的视觉符号是什么？（如 DeepSeek 图标、代码界面、人物剪影等）

## 第二步：微信封面图的官方要求

生成提示词时必须遵循以下规格：

### 封面图尺寸规范

| 类型 | 推荐尺寸 | 比例 |
|------|---------|------|
| 头条封面 | 900×383 px（最佳显示效果：1080×460 px） | 约 2.35:1（横版） |
| 次条封面 | 200×200 px | 1:1 正方形 |
| 安全区域 | 核心内容尽量集中在正中约 383×383 px 区域内（但不绝对） | — |

> 注：头条封面最大尺寸为 1280×545 px，导出格式 PNG/JPG，单张文件大小建议 ≤ 2M

### 构图原则

1. **安全区**：主体尽量集中在画面正中约 383×383 px 安全区内，确保微信转发和分享时核心内容不被裁剪
2. **文字预留**：左右各预留约 15% 空白空间，避免关键信息被裁切
3. **不绝对**：安全区是参考而非绝对，构图可以根据创意需求适当突破
4. **简洁有力**：封面图上的文字要少而精，一眼能看清
5. **信息聚焦**：2-3 秒内让用户 get 到文章核心价值

### 封面图视觉风格参考

**科技感风格**：适合 AI、工具、代码类内容
> 渐变背景、霓虹线条、故障艺术（glitch art）、暗色系 + 亮色点缀

**极简风格**：适合方法论、认知升级、深度分析
> 大面积留白、几何形状、单一主题、克制用色

**插画风格**：适合故事型、情感型、人物话题
> 手绘质感、扁平插画、暖色调、人物剪影或侧脸

**复古风格**：适合怀旧、互联网发展史、经典话题
> 噪点纹理、泛黄色调、旧报纸/杂志排版感

**赛博朋克风格**：适合前沿科技、AI 进化、未来趋势
> 霓虹灯光、高对比度、城市夜景、东方明珠/东京街景元素

**摄影风格**：适合实地调查、真实记录、人物访谈
> 浅景深、电影感构图、自然光线、真实场景

**3D 渲染风格**：适合产品发布、工具展示、功能演示
> 纯色背景、悬浮的 3D 物体、柔和阴影、莫兰迪色系或马卡龙色

## 第三步：提示词生成方法

### 提示词结构模板

封面图提示词一般由以下元素组合：

```
[主体] + [场景/环境] + [视觉风格] + [构图] + [配色] + [技术参数]
```

### 各元素说明

**主体**：画面的核心对象
> 可以是：人物剪影、产品图、抽象图形、符号图标、真实物体

**场景/环境**：主体所处的背景
> 可以是：科技感实验室、城市天际线、极简白色空间、复古房间、自然风景

**视觉风格**：整体美术方向
> 参考上方「视觉风格参考」中的 7 种风格

**构图**：画面布局方式
> 可以是：居中对称、三分法、螺旋构图、俯视、平视、仰视

**配色**：整体色调
> 可以是：赛博朋克（蓝紫霓虹）、极简（黑白灰）、科技蓝、暖色调、冷色调

**技术参数**：画面质量要求
> 如：8K、 UHD、 detailed、 cinematic lighting、 high contrast

## 第四步：生成多种风格的提示词

每次生成至少 **5 条提示词**，覆盖不同的视觉方向，每条同时提供中英文版本。

### 提示词类型分类

**类型1：科技感封面**
> 适合：AI 工具、代码、技术解读类产品体验文章
> 示例英文：
> "A floating holographic AI brain icon with circuit board patterns, cyberpunk neon blue and purple gradient background, 2.35:1 wide format, centered composition, cinematic lighting with glowing edges, dark background with bright tech elements, 8K UHD, ultra detailed"
> 示例中文：
> "一个悬浮的全息 AI 大脑图标，带有电路板纹理，赛博朋克蓝紫渐变背景，2.35:1 宽幅比例，居中构图，电影感打光，暗色背景配明亮科技元素，8K 超高清，极致细节"

**类型2：极简留白封面**
> 适合：方法论、认知升级、干货分享类文章
> 示例英文：
> "A single minimalist geometric shape floating in pure white space, subtle shadow beneath, Pantone color palette, centered composition, clean and modern, typography-ready central area, 8K, soft natural lighting"
> 示例中文：
> "一个简约的几何形状漂浮在纯白空间中，底部有柔和阴影，潘通色系，居中构图，干净现代，文字区域预留充足，8K 画质，柔和自然光"

**类型3：人物叙事封面**
> 适合：故事型、调查实验型、情感共鸣类文章
> 示例英文：
> "A silhouette of a person looking at a glowing screen in a dark room, dramatic rim lighting, shallow depth of field, cinematic atmosphere, warm orange light contrasting with cold blue screen glow, 2.35:1 format, photorealistic, 8K"
> 示例中文：
> "一个人的剪影在暗室中凝视发光的屏幕，戏剧性的轮廓光，浅景深，电影感氛围，暖橙色光与冷蓝色屏幕光芒对比，2.35:1 比例，写实摄影风格，8K 超高清"

**类型4：创意合成封面**
> 适合：观点输出、创意解读、两个事物对比类文章
> 示例英文：
> "A surreal split composition: one side showing a traditional desk with papers, the other side showing a sleek modern desk with holographic displays, dreamlike aesthetic, split-screen visualization, vibrant colors, 2.35:1 cinematic ratio, 8K UHD, detailed"
> 示例中文：
> "超现实分割构图：一侧是堆满纸张的传统办公桌，另一侧是带有全息显示器的极简现代办公桌，梦一般美学，分屏视觉效果，色彩鲜艳，2.35:1 电影比例，8K 超高清，细节丰富"

**类型5：复古怀旧封面**
> 适合：互联网发展史、经典话题、怀旧情感类文章
> 示例英文：
> "A vintage computer terminal with green phosphor screen glow, noisy CRT texture, warm sepia tones, nostalgic 1980s aesthetic, slight film grain, centered composition, 2.35:1 wide format, photorealistic, 8K"
> 示例中文：
> "一台老式电脑终端，绿色磷光屏幕发光，噪点 CRT 纹理，暖色泛黄色调，80 年代怀旧美学，轻微胶片颗粒感，居中构图，2.35:1 宽幅比例，写实风格，8K 超高清"

**类型6：抽象概念封面**
> 适合：哲学思考、趋势分析、AI 本质探讨类文章
> 示例英文：
> "An abstract visualization of data streams flowing like water, deep blue and gold color scheme, particles floating in space, ethereal and mysterious atmosphere, minimalist composition with empty center space for text, 2.35:1 cinematic ratio, 8K, ultra detailed"
> 示例中文：
> "数据的流动以水波形式抽象可视化，深蓝和金色配色方案，粒子漂浮在空间中，空灵神秘氛围，极简构图，中心预留文字空间，2.35:1 电影比例，8K 超高清，极致细节"

**类型7：产品展示封面**
> 适合：工具推荐、产品评测、新功能介绍类文章
> 示例英文：
> "A clean 3D render of a modern smartphone with AI app interface floating above it, soft studio lighting, pastel gradient background, minimalist and professional, centered composition, product showcase style, 8K UHD, hyper realistic"
> 示例中文：
> "一台现代智能手机的干净 3D 渲染，AI 应用界面悬浮其上，柔和影棚灯光，马卡龙渐变背景，极简专业风格，居中构图，产品展示风格，8K 超高清，超写实"

## 第五步：提示词输出格式

```
## 封面图提示词生成

**文章主题**：[一句话描述]
**文章类型**：[类型]
**情感基调**：[基调]
**核心意象**：[文章里最适合视觉化的元素]

---

### 提示词列表

1. **[类型1：科技感封面]**
   **English Prompt:**
   「英文提示词全文」
   **中文提示词:**
   「中文提示词全文」
   ---
   设计说明：「为什么这个风格适合这篇文章」

2. **[类型2：极简留白封面]**
   **English Prompt:**
   「英文提示词全文」
   **中文提示词:**
   「中文提示词全文」
   ---
   设计说明：「为什么这个风格适合这篇文章」

...（共 5 条以上）

---

### 推荐提示词

🥇 **首选**：「推荐提示词1」（适合的原因）
🥈 **备选**：「推荐提示词2」（适合的原因）

### 使用建议

- [ ] 建议尺寸：1080×460 px（最佳显示效果）
- [ ] 核心元素尽量放在画面中心 383×383 px 安全区域内（不绝对，可根据创意适当突破）
- [ ] 左右各预留约 15% 空白作为文字安全区
- [ ] 导出格式：PNG/JPG，单张文件大小建议 ≤ 2M
```

## 常见问题

### Midjourney 和 DALL-E 用同一个提示词吗？

不建议直接混用。两者的风格偏好不同：

- **Midjourney**：更偏艺术感、抽象感，适合有创意感的封面
- **DALL-E 3**：更偏写实、精确，适合需要清晰物体的封面
- **Stable Diffusion**：灵活度高，可自定义风格，适合有特定风格要求的封面

建议根据你使用的工具调整用词。

### 提示词太长了怎么办？

控制提示词长度在 100-200 词之间。如果太长，可以：
1. 删除重复修饰词
2. 合并相似元素
3. 保留核心风格关键词即可

### 文章封面需要加文字吗？

不建议在封面图上直接加文字。微信封面图的文字很容易被裁剪或看不清，建议：
- 封面图只做视觉呈现
- 标题本身已经在订阅号信息流里显示了
- 如果必须加文字，用提示词里的 "typography-ready" 或 "留白区域" 让 AI 预留文字位置

### 如何让封面图和文章调性一致？

在生成提示词时，思考这几个问题：
1. 文章是严肃还是轻松？
2. 目标读者是谁？
3. 文章最想传递的情绪是什么？

答案决定了你应该选「科技感」还是「插画风」，「冷色调」还是「暖色调」。

---

## 参考资料

微信封面图尺寸规范原文参考：`wk-gzh-writer` skill 中的公众号封面图要求章节。
