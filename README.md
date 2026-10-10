# Rookie Agent Guide · 菜鸟 Agent 入门

给完全没碰过 AI Agent 的人，一套能自己走完的路。不吹概念，也不假设你懂什么。有台电脑、会在终端敲几行命令，就能从「这是啥」走到「我搭起来一个自己的」。

这个仓库最初是给我自己攒的 MCP + Skills 工作流。后来发现真正难的从来不是跑通一次，而是让 agent 可靠：边界划清楚、错误看得见、踩过的坑真的记住。所以现在的定位是**面向新手的入门指南**——把我踩过的坑整理成教程、练习和两个能直接用的 skill。

## 项目简介

一句话：**教程 + 练习 + 两个 skill**，覆盖从零基础到能独立交付的完整路径。

三个组成部分各管一段：

| 组成 | 是什么 | 给谁用 |
|---|---|---|
| [`docs/tutorials/`](./docs/tutorials/README.md) | 八章教程，从「Agent 是什么」讲到「什么时候该上框架」 | 想搞懂原理的人 |
| [`docs/tutorials/practice/`](./docs/tutorials/practice/README.md) | 13 个分级练习，每个带场景、步骤、验收 | 想动手的人 |
| [`skills/`](./skills/) | 两个遵循开放标准的 skill，新手版和完整版 | 直接要工具的人 |

教程的结论不是我自己拍脑袋。写了 20 个来源的交叉核对，共识和分歧都列在[教程总览](./docs/tutorials/README.md)里，你可以顺着链接自己去验证。教程正文用三种标记区分内容的可信赖程度：🖐️ 必须亲手做、🔬 必须自己验证、✅ AI 可代劳——这份清单本身就回答了「学 Agent 哪些事 AI 替代不了」。

## 核心功能

### 两个 skill，一条升级路线

| | [my-first-agent](./skills/my-first-agent/) | [dev-automation-mcp](./skills/dev-automation-mcp/) |
|---|---|---|
| 流程 | 3 步循环：说清楚 → 先读记忆 → 做完记录 | 7 步流程 + 5 轮审核 |
| 依赖 | 无，零依赖 | 建议配 5 个 MCP，没有也能按降级规则跑 |
| 适合 | 第 1~4 周 | 已经顺手、要碰真项目之后 |

新手版是完整版**严格的子集**。升级不是推倒重来：`AGENT.md` 的内容直接并进 `CLAUDE.md`（格式兼容），错误台账是同一个文件，一个字不用改。

### 两个脚本

- [`setup_my_agent.py`](./skills/my-first-agent/scripts/setup_my_agent.py) —— 问 4 个问题，生成 `AGENT.md`、`mistakes-ledger.md`、`first-tasks.md` 三个起步文件。支持 `--answers` 非交互模式，默认不覆盖已有文件。
- [`init_project_memory.py`](./skills/dev-automation-mcp/scripts/init_project_memory.py) —— 一键初始化项目记忆层（`CLAUDE.md` + 错误台账 + `docs/adr/`），同样幂等。

两个脚本都只用 Python 标准库，零第三方依赖。

### 文档体系

- [Skill 分类与搭配推荐](./docs/SKILL-TAXONOMY.md) —— 按「作用对象」分四类，三步判类法，四套搭配方案。skill 装多了之后用得上。
- [INSTALL](./docs/INSTALL.md) / [FAQ](./docs/FAQ.md) —— 各 agent 的安装落点、MCP 配置、排错。
- [SECURITY](./docs/SECURITY.md) / [ROADMAP](./docs/ROADMAP.md) / [REPO_SETUP](./docs/REPO_SETUP.md) —— 安全原则、成长路线、仓库约定。

## 快速开始

15 分钟，先跑起来再说。

```bash
# 1. 生成你的三个起步文件
python skills/my-first-agent/scripts/setup_my_agent.py <你的项目目录>

# 2. 回答 4 个问题（直接回车用默认值也行）
# 3. 把 skills/my-first-agent/ 复制到你所用 agent 的 skills 目录
# 4. 重启 agent 客户端
```

然后对它说：

```text
使用 my-first-agent，完成 first-tasks.md 里的任务 1
```

跑完你会得到一个属于自己的 agent。它简单，但那个三步循环是你以后所有自动化流程的骨架。

**装完没反应？** 九成是没重启客户端——skill 只在启动那一刻被发现一次。剩下的排错见 [FAQ](./docs/FAQ.md)。

## 安装与使用说明

### 安装 skill

用统一安装器，一条命令装到所有已安装的 agent：

```bash
npx skills add xnddwh/rookie-agent-guide --skill my-first-agent -g -a '*'
```

不装 CLI，手动复制也一样：

```bash
cp -R skills/my-first-agent ~/.claude/skills/my-first-agent
```

常用落点：`~/.claude/skills/`（Claude Code）、`~/.codex/skills/`（Codex）、`~/.hermes/skills/`（Hermes）、`~/.agents/skills/`（Codex / Gemini / Copilot / OpenCode 共享）。全部遵循 **Agent Skills 开放标准**，写一次，75 个以上的 agent 都认。

### 使用示例

**例 1 · 新手版，做第一个任务：**

```text
使用 my-first-agent，完成 first-tasks.md 里的任务 1
```

**例 2 · 完整版，跑一个开发任务：**

```text
使用 dev-automation-mcp，先读项目上下文和 mistakes-ledger，
再结合飞书/网页资料修复登录页移动端无法提交的问题，
改完跑一遍构建验证，最后做多轮审核。
```

**例 3 · 初始化一个新项目的记忆层：**

```bash
python skills/dev-automation-mcp/scripts/init_project_memory.py ./my-new-project
```

**例 4 · 一条典型的错误台账记录**（这是它该有的样子，不是格式表演）：

```markdown
### 2026-10-10 - 改完 CSS 浏览器没变化
- Context: 修改 header 高度，保存后刷新无变化
- Mistake: 直接断言"已修复"，实际用户看到的是旧样式
- Root cause: 浏览器缓存了旧 CSS，改动本身没问题
- Detection signal: 改样式后页面"完全没反应"，往往是缓存而非代码错
- Prevention rule: 改 CSS 后先硬刷新（Ctrl+Shift+R）再判断
- Verification next time: 硬刷新确认变化后，再跑一次构建确认产物更新
```

### 配置 MCP（可选）

`my-first-agent` 不需要 MCP；`dev-automation-mcp` 配上更强。模板在 [`mcp/`](./mcp/) 目录，复制后把 `REPLACE_WITH_*` 换成你自己的值，**真实凭据不要提交**。包名核对时间和已知的坑都写在 [`references/mcp-setup.md`](./skills/dev-automation-mcp/references/mcp-setup.md)。

## 目录结构

```text
rookie-agent-guide/
├── README.md
├── LICENSE                          # MIT
├── docs/
│   ├── INSTALL.md                   # 各 agent 安装方式 + MCP 配置
│   ├── FAQ.md                       # 装 / 用 / 懂 三类常见问题
│   ├── SECURITY.md                  # 安全原则
│   ├── ROADMAP.md                   # 成长路线（Phase 0~5）
│   ├── REPO_SETUP.md                # 仓库约定
│   ├── SKILL-TAXONOMY.md            # skill 分类与搭配推荐
│   └── tutorials/
│       ├── README.md                # 学习路线 + 20 个参考来源
│       ├── 01-what-is-an-agent.md   # Agent 是什么
│       ├── 02-how-agent-works.md    # 「想—做—看」循环
│       ├── 03-mcp-and-skills.md     # MCP 与 Skill 的分工
│       ├── 04-build-your-first-agent.md
│       ├── 05-memory-and-mistakes.md
│       ├── 06-pitfalls.md           # 十个坑
│       ├── 07-best-practices.md
│       ├── 08-level-up.md
│       └── practice/                # 13 个分级练习
│           ├── README.md
│           ├── level-1-intuition.md     # 建立直觉（零安装）
│           ├── level-2-hands-on.md      # 动手搭
│           └── level-3-quality.md       # 评测与轨迹审计
├── skills/
│   ├── my-first-agent/              # 新手版
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── references/beginner-guide.md
│   │   └── scripts/setup_my_agent.py
│   └── dev-automation-mcp/          # 完整版
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/mcp-setup.md
│       └── scripts/init_project_memory.py
├── mcp/                             # MCP 配置模板（只有占位符）
└── templates/                       # CLAUDE.md / 错误台账模板
```

## 安全

这个仓库会连飞书、网页、浏览器这些外部东西，边界得说清楚。三条最要紧的：

- 不提交真实密钥，模板里只有占位符。
- 文件系统权限只开放当前项目目录，不开放整个磁盘。
- 装第三方 skill 之前，先把它读一遍——社区已经出现过投毒案例。

完整原则见 [`docs/SECURITY.md`](./docs/SECURITY.md)。

## 许可与使用

**拿去用，随便改，不用问。**

- **许可证**：MIT。个人使用、修改、再分发、商用都可以，只要保留 `LICENSE` 文件。
- **当作个人项目**：完全可以，这本就是给自己攒工作流用的仓库，不是任何平台的官方产物。
- **第三方内容**：提到的 MCP 包名、工具名属于事实性指名引用，不涉及转载。
- **教程内容**：基于 20 份公开资料交叉核对后重新撰写，来源清单在[教程总览](./docs/tutorials/README.md)。教程里引用他人 skill 一律用链接，不收录文件；查不到公开来源的会显式标出来。
- **代码**：只用标准库，无第三方依赖。

二次发布的话，改一下作者信息就行。

## 更新记录

- 2026-10-10：仓库更名 `rookie-agent-guide`；新增八章教程、13 个分级练习与 Skill 分类指南；README 重写。更早的改动看 git 提交历史。

## License

MIT
