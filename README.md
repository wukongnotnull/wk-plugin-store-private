# wk-plugin-store-private

悟空非空也的私人 Claude 插件市场

## 添加市场到 Claude Code

在 Claude Code 中添加此市场：

```bash
/plugin marketplace add wukongnotnull/wk-plugin-store-private
```

## 安装市场中的插件

安装市场中某个插件：

```bash
/plugin install <plugin-name>@wk-plugin-store-private
```

例如：
```bash
# 安装 demo-plugin
/plugin install demo-plugin@wk-plugin-store-private

# 安装 tangseng
/plugin install tangseng@wk-plugin-store-private

# 安装 quality-review-plugin
/plugin install quality-review-plugin@wk-plugin-store-private
```

## 插件列表

### demo-plugin
一个用于学习的简单插件，包含代码审查技能。

### tangseng
悟空非空也自媒体创作插件，包含以下技能：
- wk-gzh-writer - 公众号长文写作
- wk-gzh-title - 公众号标题生成
- wk-gzh-cover - 封面图提示词生成
- wk-video-script - 视频脚本写作
- wk-html-slides-amber-classified - 琥珀色风格幻灯片生成

### quality-review-plugin
代码质量审查插件，提供 /quality-review 命令。

## 本地开发

```bash
# 验证整个市场
claude plugin validate .

# 验证单个插件
claude plugin validate ./plugins/<plugin-name>
```
