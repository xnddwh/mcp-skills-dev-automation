# MCP Setup Reference

Use MCP for capabilities, not workflow text. Keep workflows in skills.

## Recommended MCP Servers

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
      "args": ["-y", "playwright-mcp"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server", "--transport", "stdio"],
      "env": {
        "BRAVE_API_KEY": "REPLACE_WITH_BRAVE_API_KEY"
      }
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

## Feishu Access

Use app identity for shared application-level resources. Use OAuth/user access token mode when the agent must access documents or resources only visible to the signed-in user.

Do not commit real App ID, App Secret, or API keys. Put real credentials in user-level MCP config or environment variables.

## Filesystem Safety

Do not expose an entire disk or home directory through a filesystem MCP. Prefer one project root at a time.

## Restart Rule

After changing MCP config or installing skills, restart the Claude/Codex client so discovery reloads.

