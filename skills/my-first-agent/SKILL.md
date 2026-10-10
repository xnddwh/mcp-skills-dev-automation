---
name: my-first-agent
description: "新手版个人 agent：用最简单的三步循环（说清任务 → 先读记忆 → 做完记录）带初学者上手 AI 开发协作。用于第一次让 agent 帮你做事、不知道怎么给 agent 下指令、想建立自己的项目记忆和错误台账。触发词：新手、入门、第一次、怎么用 agent、搭建我的 agent、我的第一个 agent。A beginner-friendly personal agent with a minimal three-step loop."
license: MIT
compatibility: "零依赖：不需要 MCP、不需要任何配置，读文件和写文件即可工作。"
metadata:
  author: xnddwh
  version: "1.0.0"
---

# My First Agent（新手版个人 agent）

这是 `dev-automation-mcp` 的**新手简化版**：去掉所有高级概念，只保留一个能立刻上手的循环。
不需要 MCP、不需要子 agent、不需要任何配置 —— 会读文件、写文件就能用。

## 三步循环（每次任务都走这三步）

```
第 1 步  说清楚          我要做什么 + 什么算做完
第 2 步  先读记忆        agent 先看 AGENT.md 和 mistakes-ledger.md 再动手
第 3 步  做完记录        做完/做错都写一笔，下次不再踩同一个坑
```

## 硬规则（只有 3 条，新手先守住这 3 条）

1. **动手前先读 `AGENT.md` 和 `mistakes-ledger.md`** —— 里面有你的目标和踩过的坑。
2. **不确定就问，不猜** —— 需求不清楚时先问一句，不要自己编。
3. **做完必须留痕** —— 成功写进 `AGENT.md` 的"常用命令"，失败写进 `mistakes-ledger.md`。

## 第一次使用（5 分钟）

1. 运行引导脚本，回答 4 个问题，生成你自己的三个起步文件：

   ```bash
   python skills/my-first-agent/scripts/setup_my_agent.py <你的项目目录>
   ```

2. 打开生成的 `AGENT.md`，检查"我的目标"和"常用命令"是否填对。
3. 把 `skills/my-first-agent/` 整个目录复制到你所用 agent 的 skills 目录（各工具落点见仓库 README）。
4. 对 agent 说：「使用 my-first-agent，完成我的第一个任务」。

## 什么时候升级

当你发现自己经常需要：查外部资料、读飞书文档、做多轮审核 —— 说明你已经超出新手区，
换用本仓库的 `dev-automation-mcp`（它是完整版，本 skill 的三步循环是它的子集）。

概念不懂？看 `references/beginner-guide.md`（10 分钟读完的术语速查）。
