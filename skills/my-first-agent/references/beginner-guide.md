# 新手概念速查（10 分钟读完）

只解释本仓库用到的 4 个词，每个词一句话 + 一个例子。

## 1. Skill（技能）

**一句话**：一个装着"怎么做事"说明书的文件夹，agent 读到它就会照着做。

```
my-first-agent/
├── SKILL.md        # 说明书本体（唯一必需的文件）
├── scripts/        # 可选：能直接运行的脚本
├── references/     # 可选：更详细的参考文档
└── agents/         # 可选：给某些工具看的展示信息
```

例子：你把 `my-first-agent/` 复制到 agent 的 skills 目录后，对它说
「使用 my-first-agent 完成任务」，它就会先读 SKILL.md，照里面的三步循环做事。

## 2. MCP（模型上下文协议）

**一句话**：给 agent 接外部工具的标准插口 —— 能联网查、能开浏览器、能读飞书。

例子：配置了 `fetch` 这个 MCP 后，agent 才能自己去读一个网页。
**没有 MCP 也能用本 skill**，只是不能自动查外部资料，需要你把资料贴给它。

## 3. 项目记忆（AGENT.md + mistakes-ledger.md）

**一句话**：agent 每次开工前先读的两个文件，让它"记得你是谁、踩过什么坑"。

- `AGENT.md`：你的目标、规则、常用命令 —— 相当于 agent 的"员工手册"。
- `mistakes-ledger.md`：错误台账 —— 每次做错/误判都记一笔，下次先查再动手。

例子：你上周发现"改 CSS 前必须先清浏览器缓存"，记进台账后，
本周 agent 改样式时会先说出这条规则再动手。

## 4. 三步循环 vs 完整版

| | my-first-agent（本 skill） | dev-automation-mcp（完整版） |
|---|---|---|
| 步骤 | 3 步 | 7 步 + 五轮审核 |
| 依赖 | 无 | 建议 5 个 MCP |
| 适合 | 第 1~4 周 | 已经顺手之后 |

## 上手路径（建议顺序）

1. 跑 `scripts/setup_my_agent.py` 生成三个起步文件。
2. 用三步循环完成 3 个小任务（见生成的 `first-tasks.md`）。
3. 每完成一个任务，检查 `mistakes-ledger.md` 是否记了一笔。
4. 第 4 周：换 `dev-automation-mcp`，把 `AGENT.md` 的内容并进 `CLAUDE.md`。

## 常见问题

**Q：我该把 skill 目录复制到哪？**
看你用什么工具：Claude Code → `~/.claude/skills/`；Codex → `~/.codex/skills/`；
Hermes → `~/.hermes/skills/`；其他工具见仓库 README 的落点表。

**Q：AGENT.md 和 CLAUDE.md 什么关系？**
`AGENT.md` 是工具无关的通用名；Claude Code 默认读 `CLAUDE.md`。
升级到完整版时把 `AGENT.md` 内容并进 `CLAUDE.md` 即可，两者格式兼容。

**Q：装完没反应？**
重启 agent 客户端（skill 只在启动时被发现一次），然后确认目录名与 `SKILL.md` 里的 `name` 一致。
