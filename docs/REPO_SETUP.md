# 仓库约定

这份文档说清楚：这个仓库叫什么、里面东西怎么放、什么不该提交。

## 名字

仓库叫 **`rookie-agent-guide`**。

名字的意思很直白——给「菜鸟」看的 agent 入门指南。前身叫 `mcp-skills-dev-automation`，那个名字偏技术、也偏窄，只说了技术栈没说给谁用。现在定位换成「面向新手」，名字跟着换。

## Repository / Issues / Projects 的分工

新手容易把这仨搞混，尤其是那个 `?tab=projects` 的链接——它打开的是看板，不是代码仓库。

```text
Repository  →  放代码、文档、配置、Skills、模板
Issues      →  放待办、Bug、改进点
Projects    →  组织 Issues，管理路线图的进度
```

顺序一般是：先有 Repository，再建 Project 看板，然后用 Issues 表达每个具体任务，最后把 Issues 拖进看板。

## 目录结构

```text
rookie-agent-guide/
  README.md                     # 首页：这是什么 + 新手快速开始 + 导航
  LICENSE                       # MIT
  docs/
    INSTALL.md                  # 各 agent 安装方式
    FAQ.md                      # 常见问题
    SECURITY.md                 # 安全原则
    ROADMAP.md                  # 成长路线图
    REPO_SETUP.md               # 本文件
    tutorials/                  # 新手教程（8 章）
      README.md                 # 学习路线 + 参考来源
      01-what-is-an-agent.md
      02-how-agent-works.md
      03-mcp-and-skills.md
      04-build-your-first-agent.md
      05-memory-and-mistakes.md
      06-pitfalls.md
      07-best-practices.md
      08-level-up.md
  skills/
    my-first-agent/             # 新手版（零依赖，三步循环）
    dev-automation-mcp/         # 完整版（七步流程 + 五轮审核）
  mcp/
    mcp.example.json
    mcp.feishu-user-oauth.example.json
  templates/
    CLAUDE.project-template.md
    mistakes-ledger.md
```

**几个约定：**

- `skills/` 下面**只能放真正的 skill**（含 `SKILL.md` 的文件夹）。安装说明之类的文档放 `docs/`。之前这里有个 `skills/claude-code/` 文件夹，里面是安装说明，已经挪去 `docs/INSTALL.md` 了——放在 `skills/` 下会让 skill 扫描器把它当成一个坏 skill。
- 每个 skill 的流程**只维护一份**，就在它的 `SKILL.md` 里。别的文档如果需要提到流程，一句话带过并指回去，别复制。
- 教程、安装、FAQ 分开，同一件事只在一个地方讲透，别在三个文件里各讲一半。

## 不要提交

- 真实的 `.mcp.json`
- 飞书 App ID / App Secret
- 任何搜索服务的 API Key
- Claude / Codex 的本地 settings
- 任何 token、cookie、session、私有文档全文

`.gitignore` 已经拦了大部分，但提交前还是顺手看一眼。

## 上传前检查

- README 有没有说清楚「这是什么」和「新手第一步做什么」
- 有没有混进真实密钥（搜一下 `secret`、`token`、`api_key`、`app_secret`、`password`、`cookie`）
- 模板是不是可以复制就用的
- 新增的东西在 README 或对应文档里有没有入口

## 改名字要注意什么

如果你以后还想改仓库名，记住一件事：**GitHub 会给旧地址做 301 跳转**，所以老链接不会立刻失效。但仓库内所有写死了旧名字的地方（README 的安装命令、本文档）都需要一起改，否则新读者照抄命令会装错仓库。

改名的完整动作是：先在 GitHub 上改名（Desktop 或网页都行），再全仓库搜一遍旧名字替换掉。
