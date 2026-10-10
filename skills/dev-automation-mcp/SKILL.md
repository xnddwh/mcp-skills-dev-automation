---
name: dev-automation-mcp
description: "MCP + Skills 个人开发自动化工作流。用于开始开发任务、修 Bug、重构、接入功能，调研飞书/网页/官方文档，规避历史错误（mistakes-ledger），做多轮审核（需求/正确性/安全/测试/交付），以及会话复盘沉淀。触发词：开发任务、修 bug、重构、代码审核、上线检查、调研、读飞书文档、查官方文档、历史错误、复盘、多轮审核。Use for development tasks, debugging, refactoring, external research, multi-round review, and project memory."
license: MIT
compatibility: "需要 git；MCP 可选（sequential-thinking / fetch / playwright / context7 / lark-mcp）。无任何 MCP 时按降级规则工作。"
metadata:
  author: xnddwh
  version: "1.1.0"
---

# Dev Automation MCP

MCP 提供能力，本 skill 提供流程。**先读上下文、再查证、再实现、再验证、再审核、最后沉淀。**

## 硬规则（不可跳过）

1. **先读上下文再动手** —— 未读 `CLAUDE.md` 与 `mistakes-ledger.md` 不得改代码。
2. **先查证再实现** —— 涉及外部事实（API、版本、库行为、产品决策、权限）必须先查，禁止凭记忆下结论。
3. **区分事实与推断** —— 结论标注来源与置信度；无法核验的标「待确认」，不得补写。
4. **最小完整改动** —— 匹配现有项目风格，不顺手重构无关代码。
5. **验证命令优先** —— 改完必须跑最相关的测试/构建/lint/类型检查/浏览器验证；跑不了要明说为什么。
6. **不编造来源** —— 无来源的结论标待确认；引用必须带出处与日期。
7. **不提交密钥** —— 真实凭据只进用户级配置或环境变量。
8. **事实先于立场** —— 发现计划或上一轮判断有误，直接说出来并给出修正。

## MCP 能力（可用则用，不可用则降级）

| MCP | 用途 | 包名（2026-10 核实） |
|---|---|---|
| `sequential-thinking` | 任务拆解、方案权衡、多轮审核 | `@modelcontextprotocol/server-sequential-thinking` |
| `fetch` | 读取指定 URL 并转为证据 | `@modelcontextprotocol/server-fetch` |
| `playwright` | 浏览器操作、E2E、视觉验证 | `@playwright/mcp` |
| `context7` | 查询框架/SDK 当前文档 | `@upstash/context7-mcp` |
| `lark-mcp` | 飞书文档、知识库、会议记录、日历 | `@larksuiteoapi/lark-mcp` |
| `github` | Issue / PR / 代码检索 | 官方远程 HTTP：`https://api.githubcopilot.com/mcp/` |
| `brave-search` | 联网搜索 | `@modelcontextprotocol/server-brave-search`（**已停止维护**，优先用内置 WebSearch） |

**降级规则**：某个 MCP 不可用时，明确说出缺失的能力，再用本地文件、内置搜索或用户提供的资料替代。**不得假装查过。**

配置细节见 `references/mcp-setup.md`。

## 开发任务流程

1. 读取 `CLAUDE.md`、`mistakes-ledger.md`、README、依赖文件、相关代码与测试、近期变更。
2. 明确目标、约束、未知事实、可能的失败模式、验证命令。
3. 若依赖飞书/网页/API/第三方库/权限/产品决策 → 先查证再设计。
4. 若台账有同类错误 → **显式写出本次适用的预防规则**。
5. 做最小完整改动。
6. 跑验证命令。
7. 重要改动执行多轮审核。

## 调研流程

1. 把问题拆成具体子问题。
2. 产品/团队问题 → 先查项目文件与飞书；技术/版本问题 → 官方优先。
3. 优先级：官方文档 > 源码仓库 > 标准/规范 > API 实际响应 > 项目测试 > 博客。
4. 每条关键结论记录来源、日期、版本、置信度。
5. 输出可执行建议 + 剩余未知项，不堆砌资料。

## 错误台账

每个项目维护 `mistakes-ledger.md`（模板见本仓库 `templates/`）：

```markdown
### YYYY-MM-DD - 标题

- Context:
- Mistake:
- Root cause:
- Detection signal:
- Prevention rule:
- Verification next time:
```

- 开始任务前必读。
- 出现返工、误判、漏测、配置错误、来源错误后**立即追加**。
- 同类任务再次出现时，必须显式引用对应预防规则。

初始化（不覆盖已存在文件）：

```bash
python scripts/init_project_memory.py <目标项目目录>
```

## 多轮审核（重要改动必做）

1. **需求一致性**：是否解决真实目标，有无遗漏或过度实现。
2. **代码正确性**：主路径、异常路径、边界、并发、状态、资源释放。
3. **数据与安全**：鉴权、授权、输入校验、敏感信息、日志、迁移、回滚。
4. **测试与回归**：覆盖风险、测试质量、构建与类型检查。
5. **交付质量**：文档、配置、启动方式、可观测性、残余风险。

输出按严重度排序并附文件/行号/来源。除非用户只要 review，否则**先修高危问题再交付**。

## 会话复盘

- 说明改了什么、验证了什么、**还有什么没验证**。
- 可复用的预防规则写入 `mistakes-ledger.md`。
- 只有长期有效的项目知识（架构决策、常用命令、反复踩的坑）才写入 `CLAUDE.md`。
