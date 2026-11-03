# 日常做题记录

## 命令行工具

在项目目录运行：

```sh
./leetcode new 2784         # 创建 Kotlin 题解（默认语言）
./leetcode new today rust   # 创建今日题目的 Rust 题解，并注册 Rust 模块
./leetcode show 2784        # 其他命令转发给外部 LeetCode CLI
```

统一使用 `./leetcode` 作为入口。创建命令支持题号或 `today`，语言支持 `kotlin` 和 `rust`。

工具自动加载项目根目录的 `.env`，配置项见 `.env.example`。
外部 CLI 优先使用 `LEETCODE_CLI` 指定的路径，然后查找 `PATH`，
最后查找 VS Code LeetCode 扩展内附的 CLI。

## 标识 
- todo: 还不理解的题目 
- 阅读理解: 玩文字游戏的题目
