# dev-automation-mcp（Claude Code 入口）

> **单一真源**：`../dev-automation-mcp/SKILL.md`。
> 本文件不再重复维护流程内容 —— 之前两份并存导致内容漂移，现在只保留一份。

## 安装

方式一（复制目录）：

```bash
cp -R ../dev-automation-mcp ~/.claude/skills/dev-automation-mcp
```

方式二（统一 CLI，顺带装到其他 agent）：

```bash
npx skills add xnddwh/mcp-skills-dev-automation --skill dev-automation-mcp -a claude-code -g
```

## 说明

- `SKILL.md` 的 `name` 与目录名一致，符合 Agent Skills 开放标准（agentskills.io）。
- `agents/openai.yaml` 供 Codex 显示名称与默认提示词；其他 agent 忽略该文件。
- 本 skill **不绑定任何 agent**：没有 MCP、没有子 agent 能力时按 SKILL.md 的降级规则工作。

## 改动流程

改流程请只改 `../dev-automation-mcp/SKILL.md`，不要在这里复制一份。
