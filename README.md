# Personal AI Development Automation

一个面向个人开发者的 MCP + Skills 工作流项目。它把外部工具能力交给 MCP，把可复用的开发方法沉淀为 Skills，让 AI Agent 在开发任务中稳定完成：自动思考、资料检索、飞书/网页阅读、历史错误规避、多轮审核和复盘沉淀。

## 当前模式

本项目采用三层结构：

```text
MCP Servers          -> 提供真实工具能力
Skills              -> 固化可复用工作流程
Project Memory      -> 保存项目上下文、经验和历史错误
```

### 1. MCP 工具层

MCP 负责“能做什么”：

- `sequential-thinking`：复杂任务拆解、多轮思考、方案审核。
- `fetch`：读取网页资料和指定 URL。
- `playwright`：浏览器自动化、页面交互、端到端验证。
- `context7`：查询当前库、框架和 SDK 文档。
- `lark-mcp`：读取飞书文档、知识库、团队资料和协作信息。

后续可扩展：

- Brave Search：联网搜索。
- GitHub MCP：Issue、PR、仓库管理和代码审查。
- Database MCP：MySQL、PostgreSQL、SQLite 数据查询。
- Memory MCP：跨项目长期记忆。
- Figma MCP：前端设计稿还原。

### 2. Skills 流程层

Skills 负责“应该怎么做”。

当前核心 Skill：

```text
dev-automation-mcp
```

它要求 Agent 在开发任务中遵循固定流程：

1. 读取项目上下文：`CLAUDE.md`、README、依赖文件、相关代码和测试。
2. 读取历史错误：`mistakes-ledger.md`。
3. 判断是否需要外部资料：飞书、网页、库文档、搜索结果。
4. 先核实事实，再设计方案。
5. 按项目风格做最小完整实现。
6. 运行相关测试、构建、lint、类型检查或浏览器验证。
7. 做多轮审核。
8. 把可复用经验写回项目记忆或错误台账。

### 3. 项目记忆层

每个项目建议包含：

```text
CLAUDE.md
mistakes-ledger.md
docs/adr/
```

- `CLAUDE.md`：项目目标、技术栈、架构约束、常用命令、坑点。
- `mistakes-ledger.md`：历史错误、根因、发现信号、预防规则、下次验证方式。
- `docs/adr/`：重要架构决策记录。

## 使用方式

重启 Claude Code 或 Codex 后，直接在任务中要求使用该 Skill：

```text
使用 dev-automation-mcp，先读项目上下文和 mistakes-ledger，再结合飞书/网页资料完成这个任务，并在最后做多轮审核。
```

示例：

```text
使用 dev-automation-mcp，读取飞书需求文档，修复登录页移动端无法提交的问题。
```

```text
使用 dev-automation-mcp，对当前项目做上线前多轮审核。
```

```text
使用 dev-automation-mcp，结合 Context7 和官方文档调研这个 SDK 的接入方式。
```

## 多轮审核标准

每次重要变更至少审核五轮：

1. 需求一致性：是否解决真实目标，是否遗漏明确要求。
2. 代码正确性：主路径、异常路径、边界条件、并发、资源释放。
3. 数据与安全：鉴权、授权、输入校验、敏感信息、日志、迁移和回滚。
4. 测试与回归：测试覆盖、构建、类型检查、浏览器或 API 验证。
5. 交付质量：文档、配置、启动方式、可观测性和残余风险。

## 历史错误规避

`mistakes-ledger.md` 使用以下格式：

```markdown
### YYYY-MM-DD - 标题

- Context:
- Mistake:
- Root cause:
- Detection signal:
- Prevention rule:
- Verification next time:
```

规则：

- 开始任务前必须读取。
- 出现返工、误判、漏测、配置错误、资料来源错误时必须追加。
- 下次遇到同类任务时，Agent 必须显式引用对应预防规则。

## 安全原则

- 不提交真实 API Key、App Secret、Token。
- MCP 配置模板只放占位符。
- 真实凭据放在用户级配置或环境变量中。
- 文件系统 MCP 不开放整个磁盘或用户根目录，只开放当前项目目录。
- 飞书权限从最小权限开始授权。

## 仓库定位

这个仓库不是单一项目脚手架，而是个人 AI 开发操作系统的基础设施。

它的目标是持续沉淀：

- MCP 配置模板。
- Skills 工作流。
- 项目记忆模板。
- 历史错误规避规则。
- 审核清单。
- 面向不同项目类型的自动化方法。

## 推荐仓库名

可选：

- `personal-ai-dev-workflow`
- `mcp-skills-dev-automation`
- `ai-dev-ops-playbook`
- `dev-automation-mcp-skills`

推荐使用：

```text
mcp-skills-dev-automation
```

这个名字最准确表达当前模式：MCP 提供能力，Skills 固化流程。

