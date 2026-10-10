# 安装

这个仓库里的东西只有两类：**skill**（文件夹）和 **MCP 配置**（一段 JSON）。skill 是主体，MCP 是可选的加强件。

没装过任何东西也能用——`my-first-agent` 是零依赖的，不需要 MCP。

## skill 装到哪儿

先把落点搞清楚，后面不管用哪种方式装，都是往这些地方放：

| 你用的工具 | skill 目录 |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Hermes | `~/.hermes/skills/` |
| Codex / Gemini CLI / Copilot / OpenCode | `~/.agents/skills/`（共享目录） |

Windows 上 `~` 就是你的用户目录，比如 `C:\Users\你的名字\`。

## 方式一：统一 CLI（推荐）

用 `npx skills`，一条命令能装到所有已安装的 agent：

```bash
# 装到所有 agent（全局）
npx skills add xnddwh/rookie-agent-guide --skill my-first-agent -g -a '*'

# 只装 Claude Code
npx skills add xnddwh/rookie-agent-guide --skill my-first-agent -a claude-code -g

# 只装完整版的 dev-automation-mcp
npx skills add xnddwh/rookie-agent-guide --skill dev-automation-mcp -g -a '*'
```

两个细节值得知道：

- 它**默认用软链接**，也就是所有 agent 指向同一份源文件。改了源文件，所有地方一起生效。想每个 agent 各存一份，加 `--copy`。
- 不放心的话先 `--list` 看看它准备装什么，再决定。

## 方式二：手动复制

不想装 CLI，直接复制文件夹，效果一样：

```bash
cp -R skills/my-first-agent ~/.claude/skills/my-first-agent
```

Windows 上用资源管理器拖也一样。

## 装完必须重启客户端

这是新手第一大「装完没反应」的原因：**skill 只在客户端启动那一刻被发现一次**，热装是不会生效的。装完，把客户端关掉重开。

重启后还是不行，检查两件事：

1. 文件夹名和 `SKILL.md` 里的 `name` 是否**一字不差**（`my-first-agent` 就是 `my-first-agent`，别多空格别改大小写）
2. 目录层级对不对——应该是 `skills/my-first-agent/SKILL.md`，不是 `skills/my-first-agent/my-first-agent/SKILL.md`

## 怎么用起来

装好之后，在任务里直接点名要用的 skill：

```text
使用 my-first-agent，完成 first-tasks.md 里的任务 1
```

```text
使用 dev-automation-mcp，先读项目上下文和 mistakes-ledger，再结合飞书/网页资料完成这个任务，最后做多轮审核
```

## MCP（可选）

MCP 是给 agent 加外部能力的，比如联网搜索、读飞书、开浏览器。`my-first-agent` 不需要它；`dev-automation-mcp` 建议配上，但没有也能按降级规则工作。

配置模板在仓库的 `mcp/` 目录下，复制一份填上你自己的值就行。**模板里只有占位符，真实凭据不要提交。**

各 agent 的 MCP 配置位置：

| Agent | 配置方式 |
|---|---|
| Claude Code | `claude mcp add <name> -- npx -y <包名>`（用户级加 `-s user`） |
| Codex | `~/.codex/config.toml` 的 `[mcp_servers]` |
| Gemini CLI | `~/.gemini/settings.json` |
| 通用 | 项目内的 `.mcp.json`（**千万别提交真实凭据**） |

具体每个 MCP 的包名和配置，见 `skills/dev-automation-mcp/references/mcp-setup.md`。MCP 生态变动很快，安装前以官方仓库的 README 为准——那个文件里也记了一次包名修正的经过，你可以看看哪些名字是坑。

## 装第三方 skill 之前

顺便提个醒，跟安装直接相关：**社区里已经出现过投毒案例**——恶意指令藏在 skill 或 MCP 里，能让你的文件被传出去，或者执行你根本没让它执行的命令。

所以，装别人做的 skill 之前，先做一件事：**把它的 `SKILL.md` 读一遍，再把 `scripts/` 里的脚本扫一眼**。看不懂就先别装。凭据一律走环境变量，别写死在配置里。

详细的安全原则见 `SECURITY.md`。

## 出问题了？

常见的坑我都收在 `FAQ.md` 里了，先去那儿看一眼。
