# GitHub Setup

你给出的页面：

```text
https://github.com/xnddwh?tab=projects
```

这是 GitHub Projects 页面，用来管理看板、路线图和任务状态，不是代码仓库。

## 正确关系

```text
Repository  -> 放代码、文档、配置、Skills、模板
Issues      -> 放待办、Bug、改进点
Projects    -> 组织 Issues 和路线图
Wiki        -> 可选，用于长期知识库
```

## 推荐做法

1. 先创建 Repository。
2. 把本项目文档和模板推到 Repository。
3. 再创建 GitHub Project 看板。
4. 用 Issues 表达每个成长任务。
5. 把 Issues 加入 Project 看板管理进度。

## 推荐仓库名

首选：

```text
mcp-skills-dev-automation
```

备选：

```text
personal-ai-dev-workflow
dev-automation-mcp-skills
ai-dev-ops-playbook
```

## 建议仓库结构

```text
mcp-skills-dev-automation/
  README.md
  mcp/
    mcp.example.json
    mcp.feishu-user-oauth.example.json
  skills/
    dev-automation-mcp/
      SKILL.md
      references/
        mcp-setup.md
    claude-code/
      dev-automation-mcp.md
  templates/
    CLAUDE.project-template.md
    mistakes-ledger.md
  docs/
    GROWTH_ROADMAP.md
    GITHUB_SETUP.md
    SECURITY.md
```

## 不要提交的内容

- 真实 `.mcp.json`。
- 飞书 App Secret。
- Brave Search API Key。
- Claude/Codex 本地 settings。
- 任何 token、cookie、session、私有文档全文。

## 上传前检查

- README 是否说明 MCP 和 Skills 的分工。
- 是否没有真实密钥。
- 是否提供可复制的模板。
- 是否说明如何启用飞书和搜索。
- 是否说明如何扩展新的 Skills 和 MCP。

