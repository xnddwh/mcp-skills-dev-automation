# MCP 配置参考

MCP 提供能力，不提供流程。流程一律写在 skill 里。

> 包名核对时间：2026-10-10。MCP 生态变动快，安装前以官方仓库 README 为准。

## 推荐配置

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "lark-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@larksuiteoapi/lark-mcp",
        "mcp",
        "-a",
        "REPLACE_WITH_FEISHU_APP_ID",
        "-s",
        "REPLACE_WITH_FEISHU_APP_SECRET",
        "--domain",
        "https://open.feishu.cn",
        "-l",
        "zh"
      ]
    }
  }
}
```

## 包名修正记录（2026-10-10）

| 项 | 旧写法（有问题） | 现行写法 |
|---|---|---|
| Playwright | `playwright-mcp` | `@playwright/mcp`（微软官方） |
| Brave Search | `@brave/brave-search-mcp-server` | `@modelcontextprotocol/server-brave-search`，且**该 server 已停止维护** |
| GitHub | 未配置 | 官方推荐远程 HTTP：`https://api.githubcopilot.com/mcp/`（旧 npm 包 `@modelcontextprotocol/server-github` 已弃用） |

**搜索建议**：优先用 agent 内置的 WebSearch / WebFetch，Brave MCP 只作补充。

## 各 agent 的配置位置

| Agent | 配置方式 |
|---|---|
| Claude Code | `claude mcp add <name> -- npx -y <pkg>`（用户级加 `-s user`） |
| Codex | `~/.codex/config.toml` 的 `[mcp_servers]` |
| WorkBuddy | `~/.workbuddy/mcp.json` |
| Gemini CLI | `~/.gemini/settings.json` |
| 通用 | 项目内 `.mcp.json`（**不得提交真实凭据**） |

## 安全

- 不提交 App ID / App Secret / API Key；模板只放占位符。
- 真实凭据放用户级配置或环境变量，配置里用 `${VAR}` 引用。
- 文件系统 MCP 只开放当前项目目录，**不开放整个磁盘或用户根目录**。
- 第三方 MCP 与第三方 skill 安装前先看一眼它的 `scripts/` —— 社区生态已出现投毒案例（恶意指令借 skill / MCP 注入）。

## 生效规则

改完 MCP 配置或安装新 skill 后，**重启客户端**才会重新发现。
