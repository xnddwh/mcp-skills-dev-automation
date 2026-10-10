# Rookie Agent Guide · 菜鸟 Agent 入门

给完全没碰过 AI Agent 的人，一套能自己走完的路。

不吹概念，也不假设你懂什么。你只要有台电脑、会用终端敲几行命令，就能从「这是啥」一路走到「我搭起来一个自己的」。

## 15 分钟，先跑起来

别读文档了，先动手。打开终端，把 `<你的项目目录>` 换成你自己的路径：

```bash
# 1. 生成你的三个起步文件（AGENT.md / mistakes-ledger.md / first-tasks.md）
python skills/my-first-agent/scripts/setup_my_agent.py <你的项目目录>

# 2. 回答 4 个问题（或者直接回车用默认值）
# 3. 把 skills/my-first-agent/ 复制到你所用 agent 的 skills 目录
# 4. 重启 agent 客户端，然后对它说：
#    「使用 my-first-agent，完成 first-tasks.md 里的任务 1」
```

跑完你会得到一个属于你自己的 agent。它简单，但它不是玩具——那个「说清楚 → 先读记忆 → 做完记录」的三步循环，是你以后所有自动化流程的骨架。

**装完没反应？** 一定是没重启客户端。这是新手第一大坑，我在 `docs/FAQ.md` 里把这类问题都收好了。

## 仓库里有什么

| 你想干什么 | 去这儿 |
|---|---|
| 完全零基础，先看懂概念 | [`docs/tutorials/`](./docs/tutorials/README.md) 八章教程，建议从 01 顺着读 |
| 想尽快动手 | [教程 04](./docs/tutorials/04-build-your-first-agent.md)，或者上面那 15 分钟 |
| 装不上 / 装完没反应 | [`docs/INSTALL.md`](./docs/INSTALL.md)、[`docs/FAQ.md`](./docs/FAQ.md) |
| 想提前知道哪儿会翻车 | [教程 06 新手常踩的坑](./docs/tutorials/06-pitfalls.md) |
| 想要一份能贴墙上的清单 | [教程 07 最佳实践](./docs/tutorials/07-best-practices.md) |
| skill 装多了，不知道该怎么理、怎么搭 | [Skill 分类与搭配推荐](./docs/SKILL-TAXONOMY.md) |
| 想边做边学，要练习项目 | [练习项目](./docs/tutorials/practice/README.md) 13 个分级练习 |
| 要接外部工具（飞书/联网/浏览器） | [`docs/INSTALL.md`](./docs/INSTALL.md) 的 MCP 部分、[教程 03](./docs/tutorials/03-mcp-and-skills.md) |
| 想知道后面还能怎么长 | [`docs/ROADMAP.md`](./docs/ROADMAP.md) |
| 关心安全 | [`docs/SECURITY.md`](./docs/SECURITY.md) |

## 两个 skill，一条升级路线

仓库里就两个 skill，正好是新手和进阶的两端：

| | [my-first-agent](./skills/my-first-agent/) | [dev-automation-mcp](./skills/dev-automation-mcp/) |
|---|---|---|
| 是什么 | 新手版 | 完整版 |
| 流程 | 3 步循环 | 7 步流程 + 5 轮审核 |
| 依赖 | 无，零依赖 | 建议配 5 个 MCP |
| 适合 | 第 1~4 周 | 已经顺手、要碰真项目之后 |

关键的一点：**新手版是完整版严格的子集**。升级不是推倒重来，是长出来。你 `AGENT.md` 里攒的内容直接并进 `CLAUDE.md` 就行（格式兼容），错误台账更是同一个文件，一个字都不用改。

所以别急着上完整版。先把三步循环走熟，等你真的开始需要「查外部资料」「做多轮审核」了，再升。

## 装上它

用统一定位安装器，一条命令装到所有已安装的 agent：

```bash
npx skills add xnddwh/rookie-agent-guide --skill my-first-agent -g -a '*'
```

不想装 CLI，手动复制文件夹也一样：

```bash
cp -R skills/my-first-agent ~/.claude/skills/my-first-agent
```

常用落点：`~/.claude/skills/`（Claude Code）、`~/.codex/skills/`（Codex）、`~/.hermes/skills/`（Hermes）、`~/.agents/skills/`（Codex / Gemini / Copilot / OpenCode 共享）。

各工具更细的步骤、MCP 配置、排错，全在 [`docs/INSTALL.md`](./docs/INSTALL.md)。

## 为什么是 Skill 的形式

这里的东西都遵循 **Agent Skills 开放标准**：一个 `SKILL.md` 加上可选的 `scripts/` 和 `references/`。好处很实在——**写一次，75 个以上的 agent 都能用**，不用给每个工具各维护一份。

这也是我为什么把流程单独拎出来当卖点：它不绑定 Claude Code，也不绑定 Codex，你哪天换工具了，这些 skill 跟着你走。

## 安全

这个仓库会连飞书、网页、浏览器这些外部东西，所以边界得说清楚。三条最要紧的：

- 不提交真实密钥，模板里只有占位符。
- 文件系统权限只开放当前项目目录，不开放整个磁盘。
- 装第三方 skill 之前，先把它读一遍——社区已经出现过投毒案例。

完整原则在 [`docs/SECURITY.md`](./docs/SECURITY.md)。

## 许可与使用

简单说：**拿去用，随便改，不用问。**

- **许可证**：MIT。个人使用、修改、再分发、甚至商用都可以，只要保留 `LICENSE` 文件。
- **当作个人项目**：完全可以。这本就是给你自己攒工作流用的仓库，不是某个平台的官方产物。
- **第三方内容**：文档里提到的 MCP 包名、工具名属于**事实性指名引用**，不涉及转载或复制他人的受版权保护内容。
- **教程内容**：基于多份公开资料交叉核对后重新撰写的，不是搬运。我参考的 12 个来源和它们的观点分歧，都列在 [`docs/tutorials/README.md`](./docs/tutorials/README.md) 里，你可以自己去核对。
- **代码**：脚本只用各自语言的标准库，没有引入任何第三方代码或依赖。

如果你要在此基础上二次发布，改一下作者信息就行。

## 修订记录

### 2026-10-10（三）

- 仓库更名为 `rookie-agent-guide`，定位从「MCP + Skills 自动化」调整为「面向新手的入门指南」。
- 新增 `docs/tutorials/` 八章教程体系，覆盖概念、原理、MCP 与 Skill、动手搭建、记忆与台账、常见坑、最佳实践、进阶；结论经 12 个来源交叉核对，清单在教程总览里。
- 新增 `docs/INSTALL.md`、`docs/FAQ.md`。
- 新增 `docs/SKILL-TAXONOMY.md`：按「作用对象」把 skill 分成四类（协作规范 / 领域专家 / 产出加工 / 系统操作），
  给出三步判类法、四套搭配方案（应试闭环 / 内容生产 / 工程开发 / 生产运维）与四条搭配原则。
  文中的 skill 一律以**来源链接**呈现（不收录他人文件），查不到公开来源的显式标注，不编链接。
- 结构调整：`skills/claude-code/`（放的是安装说明，不是 skill）挪并进 `docs/INSTALL.md`，避免污染 skill 扫描；`GROWTH_ROADMAP.md` → `ROADMAP.md`，`GITHUB_SETUP.md` → `REPO_SETUP.md`；新增 Phase 0 新手教程体系。
- 修正 `mcp/mcp.example.json`：Playwright 包名改为 `@playwright/mcp`，Brave 标注为已停止维护，补充 GitHub 官方远程 MCP——之前这个示例文件和 `references/mcp-setup.md` 里的写法是矛盾的。

### 2026-10-10（二）

- 新增 `skills/my-first-agent/`：零依赖、三步循环的新手版，含交互式引导脚本。

### 2026-10-10

- 修正 MCP 包名，`SKILL.md` 补齐标准字段与 8 条硬规则，新增项目记忆初始化脚本，补 `LICENSE`。

## License

MIT
