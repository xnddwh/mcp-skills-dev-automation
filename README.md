# Personal AI Development Automation

一个面向个人开发者的 MCP + Skills 工作流项目。它把外部工具能力交给 MCP，把可复用的开发方法沉淀为 Skills，让 AI Agent 在开发任务中稳定完成：自动思考、资料检索、飞书/网页阅读、历史错误规避、多轮审核和复盘沉淀。

Skill 遵循 **Agent Skills 开放标准**（`SKILL.md` + `scripts/` + `references/`），因此写一次即可装进 Claude Code、Codex、Cursor、Gemini CLI、Hermes 等 75+ 个 agent。

## 一键安装

```bash
# 装到所有已安装的 agent（全局）
npx skills add xnddwh/mcp-skills-dev-automation --skill dev-automation-mcp -g -a '*'

# 只装 Claude Code
npx skills add xnddwh/mcp-skills-dev-automation --skill dev-automation-mcp -a claude-code -g

# 手动方式：复制目录到目标 agent 的 skills 目录
cp -R skills/dev-automation-mcp ~/.claude/skills/dev-automation-mcp
```

常用落点：`~/.claude/skills/`（Claude Code）、`~/.codex/skills/`（Codex）、`~/.hermes/skills/`（Hermes）、`~/.agents/skills/`（Codex/Gemini/Copilot/OpenCode 共享目录）。

## 新手从这里开始

第一次接触 agent？先不要看完整版，从 **`skills/my-first-agent/`** 开始：

```bash
# 回答 4 个问题，生成你自己的三个起步文件（AGENT.md / mistakes-ledger.md / first-tasks.md）
python skills/my-first-agent/scripts/setup_my_agent.py <你的项目目录>
```

然后把 `skills/my-first-agent/` 复制到你所用 agent 的 skills 目录，对它说
「使用 my-first-agent，完成 first-tasks.md 里的任务 1」。

三步循环：**说清楚 → 先读记忆 → 做完记录**。三周熟练后升级 `dev-automation-mcp`，
生成的 `AGENT.md` 可直接并入 `CLAUDE.md`（格式兼容）。详见 `skills/my-first-agent/references/beginner-guide.md`。

## 当前模式

本项目采用三层结构：

```text
MCP Servers          -> 提供真实工具能力
Skills              -> 固化可复用工作流程
Project Memory      -> 保存项目上下文、经验和历史错误
```

### 1. MCP 工具层

MCP 负责"能做什么"：

- `sequential-thinking`：复杂任务拆解、多轮思考、方案审核。
- `fetch`：读取网页资料和指定 URL。
- `playwright`：浏览器自动化、页面交互、端到端验证。
- `context7`：查询当前库、框架和 SDK 文档。
- `lark-mcp`：读取飞书文档、知识库、团队资料和协作信息。

后续可扩展：

- GitHub MCP：Issue、PR、仓库管理、代码审查（官方远程 HTTP）。
- Database MCP：开发库查询和数据验证。
- Memory MCP：跨项目长期记忆。
- Figma MCP：前端设计稿还原。

搜索优先使用 agent 内置的 WebSearch / WebFetch；Brave MCP 的官方 server 已停止维护，只作补充。

### 2. Skills 流程层

Skills 负责"应该怎么做"。

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

**单一真源**：流程只维护在 `skills/dev-automation-mcp/SKILL.md`。`skills/claude-code/dev-automation-mcp.md` 只是安装说明，不重复流程内容。

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

一键初始化（不覆盖已存在文件）：

```bash
python skills/dev-automation-mcp/scripts/init_project_memory.py <项目目录>
```

## 使用方式

重启客户端后，直接在任务中要求使用该 Skill：

```text
使用 dev-automation-mcp，先读项目上下文和 mistakes-ledger，再结合飞书/网页资料完成这个任务，并在最后做多轮审核。
```

示例：

```text
使用 dev-automation-mcp，读取飞书需求文档，修复登录页移动端无法提交的问题。
使用 dev-automation-mcp，对当前项目做上线前多轮审核。
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
- MCP 配置模板只放占位符，真实凭据走用户级配置或环境变量。
- 文件系统 MCP 不开放整个磁盘或用户根目录，只开放当前项目目录。
- 飞书权限从最小权限开始授权。
- 第三方 skill / MCP 安装前先看它的 `scripts/` —— 社区已出现投毒案例。

详见 `docs/SECURITY.md`。

## 仓库结构

```text
README.md
LICENSE                              # MIT
mcp/
  mcp.example.json
  mcp.feishu-user-oauth.example.json
skills/
  dev-automation-mcp/                # 单一真源
    SKILL.md
    agents/openai.yaml               # Codex 展示名与默认提示词
    scripts/init_project_memory.py
    references/mcp-setup.md
  claude-code/
    dev-automation-mcp.md            # 仅安装说明
  my-first-agent/                    # 新手版（零依赖，三步循环）
    SKILL.md
    agents/openai.yaml
    scripts/setup_my_agent.py
    references/beginner-guide.md
templates/
  CLAUDE.project-template.md
  mistakes-ledger.md
docs/
  GROWTH_ROADMAP.md
  GITHUB_SETUP.md
  SECURITY.md
```

## 路线图

成长方向与阶段状态见 `docs/GROWTH_ROADMAP.md`。

## 修订记录

### 2026-10-10（二）

- 新增 `skills/my-first-agent/`：面向初学者的极简个人 agent。
  - 与 `dev-automation-mcp` 的衔接：它是完整版的**子集**（三步循环 ⊂ 七步流程 + 五轮审核），
    复用同一份 `templates/mistakes-ledger.md`，升级时 `AGENT.md` 直接并入 `CLAUDE.md`。
  - 新增交互式引导脚本 `setup_my_agent.py`（支持 `--answers` 非交互模式，幂等不覆盖）。
- 归档入口更新：本仓库 skill 已收入 `E:\SkillsHub`（含各 agent 本地已装副本）。

### 2026-10-10

- 修正 MCP 包名：Playwright `playwright-mcp` → `@playwright/mcp`；Brave 标注为已停止维护；补充 GitHub 官方远程 MCP。
- `SKILL.md` 补齐 `license` / `compatibility` / `metadata` 字段，description 增加中文触发词。
- 新增 8 条硬规则（先读上下文、先查证、区分事实与推断、验证命令优先、不编造来源等）与明确的 MCP 降级规则。
- 新增 `scripts/init_project_memory.py`，一键初始化项目记忆层。
- 消除双份维护：`skills/claude-code/dev-automation-mcp.md` 改为安装说明，流程只保留在标准 `SKILL.md`。
- 新增 `LICENSE`（MIT，此前公共仓库无许可证）。
- 文档补齐：路线图加阶段状态、安全文档加第三方 skill 审计、清理仓库命名决策残留。

## 仓库定位

这个仓库不是单一项目脚手架，而是个人 AI 开发操作系统的基础设施。

它的目标是持续沉淀：

- MCP 配置模板。
- Skills 工作流。
- 项目记忆模板。
- 历史错误规避规则。
- 审核清单。
- 面向不同项目类型的自动化方法。

## License

MIT
