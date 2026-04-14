# wukong-private-plugins

悟空非空也的私人 Claude 插件市场

## 插件列表

### demo-plugin
一个用于学习的简单插件，包含代码审查技能。

### tangseng
悟空非空也自媒体创作插件，包含以下技能：
- wk-gzh-writer - 公众号长文写作
- wk-gzh-title - 公众号标题生成
- wk-gzh-cover - 封面图提示词生成
- wk-video-script - 视频脚本写作

### quality-review-plugin
代码质量审查插件，提供 /quality-review 命令。

## 安装

```bash
claude plugin add wukongnotnull/wukong-private-plugins
```

## 本地开发

```bash
# 验证插件结构
claude plugin validate .

# 验证单个插件
claude plugin validate ./plugins/<plugin-name>
```
