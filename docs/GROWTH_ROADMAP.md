# Growth Roadmap

本项目的成长方向不是一次性堆工具，而是逐步形成可靠、可复用、可审计的个人开发自动化系统。

## Phase 1: 基础可用

目标：让每个开发任务都能稳定走通“上下文 -> 资料 -> 实现 -> 验证 -> 审核 -> 复盘”。

任务：

- 固化 `dev-automation-mcp` Skill。
- 建立用户级 MCP 配置。
- 每个项目补齐 `CLAUDE.md`。
- 每个项目维护 `mistakes-ledger.md`。
- 把飞书、网页读取、实时文档查询接入日常开发。

完成标准：

- Agent 不再直接开写代码，而是先读上下文和错误台账。
- 涉及外部资料时能先查证再实现。
- 每个重要任务都有验证命令和多轮审核结果。

## Phase 2: 专项 Skills

目标：把高频场景拆成更细的 Skills，降低单个 Skill 的复杂度。

建议新增：

- `systematic-debugging`：复杂 Bug 排查。
- `release-check`：上线前质量检查。
- `api-contract-review`：接口契约和兼容性审核。
- `frontend-ux-review`：前端交互、视觉和响应式审核。
- `memory-audit`：定期清理项目记忆和错误台账。
- `feishu-research`：专门处理飞书文档、会议纪要和知识库研究。

完成标准：

- 不同任务能触发不同 Skill。
- 每个 Skill 保持短小清晰。
- 复杂细节放到 `references/`，主 Skill 只保留流程。

## Phase 3: MCP 能力扩展

目标：让 Agent 能访问更多真实上下文，而不是只依赖本地文件。

建议扩展：

- Brave Search MCP：联网搜索和资料发现。
- GitHub MCP：Issue、PR、代码审查、仓库管理。
- Database MCP：开发库查询和数据验证。
- Memory MCP：跨项目长期经验。
- Figma MCP：设计稿到前端实现。
- Slack/Notion/Jira/Linear MCP：按实际协作工具接入。

完成标准：

- Agent 能从需求、代码、飞书、网页、Issue、数据库中交叉验证结论。
- 资料来源可追踪。
- 高风险操作需要明确权限边界。

## Phase 4: 项目知识库

目标：让项目越做越聪明。

建议结构：

```text
CLAUDE.md
mistakes-ledger.md
docs/
  adr/
  runbooks/
  review-checklists/
  integration-notes/
```

沉淀内容：

- 架构决策。
- 环境启动方式。
- 常见故障处理。
- 上线检查清单。
- 第三方接入注意事项。
- 历史错误预防规则。

完成标准：

- 新会话能快速恢复项目上下文。
- 同类错误明显减少。
- Agent 能主动引用已有规则。

## Phase 5: 自动化治理

目标：让流程不靠记忆，而靠机制。

建议：

- 用 hooks 在编辑后自动格式化或运行轻量检查。
- 用 CI 检查文档、配置和测试。
- 用 GitHub Issues 管理 Skill 和 MCP 扩展任务。
- 用 GitHub Projects 管理路线图，而不是存放代码。

完成标准：

- 代码在提交前经过基本检查。
- 每次重要变更都有审核记录。
- 路线图、Issue、PR、文档形成闭环。

## 判断项目是否成长

看这些指标：

- 新任务启动时，Agent 是否能自动找到项目上下文。
- 返工是否减少。
- 历史错误是否被复用为预防规则。
- 外部资料是否有来源记录。
- 审核是否能发现真实问题。
- 新项目是否能快速复用同一套工作流。

