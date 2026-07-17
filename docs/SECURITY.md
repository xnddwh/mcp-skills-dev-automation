# Security

本项目会连接飞书、网页、浏览器、搜索和未来可能的 GitHub、数据库、长期记忆，因此安全边界必须清晰。

## Secrets

不要提交：

- 飞书 App Secret。
- API Key。
- Token。
- Cookie。
- `.mcp.json` 中的真实凭据。
- 本地 Claude/Codex settings。

只提交：

- `*.example.json`
- `.env.example`
- 不含真实值的模板。

## MCP Permissions

原则：

- 最小权限。
- 只开放当前项目目录。
- 不开放整个用户目录或磁盘。
- 高风险 MCP 先在测试项目中验证。

## Feishu

建议：

- 从只读权限开始。
- 优先授权具体文档、知识库或应用需要的范围。
- 如果要访问个人私有资料，使用 OAuth/user token 模式。
- 定期轮换 App Secret。

## Repository Hygiene

上传前检查：

```text
secret
token
api_key
app_secret
password
cookie
authorization
```

如果发现真实凭据已经提交，立即：

1. 在服务商后台吊销或轮换密钥。
2. 从 Git 历史中移除。
3. 检查访问日志。

