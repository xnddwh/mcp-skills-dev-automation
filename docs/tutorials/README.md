# 新手教程：从零到跑通你自己的 Agent

这套教程是写给「完全没碰过 AI Agent」的人的。如果你已经能熟练写工具调用、调框架，那它对你太浅了，可以直接跳到本仓库的 `dev-automation-mcp`。

我写这套东西的时候一直在提醒自己一件事：别把人当傻子，也别把 Agent 说成魔法。所以每一章我都会尽量回答两个问题——**它到底在干嘛**，以及**你踩坑时应该往哪儿看**。

## 这套教程解决什么问题

新手卡住的地方，翻来覆去就那么几个：

- 听了一堆名词（LLM、Prompt、Context、MCP、Skill、ReAct），但串不起来
- 照着 demo 抄了一遍能跑，换个任务就崩，也不知道错在哪
- 不知道该给 agent 几个工具、要不要做记忆、要不要一上来就上多 agent
- 做出来的东西「看着挺聪明」，但不敢真用它做事

这套教程按「先看懂 → 再跑通 → 再避坑 → 最后升级」的顺序走，就是冲着这几个问题去的。

## 学习路线

| 章节 | 你会得到什么 | 建议 |
|---|---|---|
| [01 什么是 Agent](./01-what-is-an-agent.md) | 分清楚 Agent、聊天机器人、自动化脚本 | 先读，建立直觉 |
| [02 Agent 是怎么工作的](./02-how-agent-works.md) | 搞懂那个「想—做—看」的循环 | 全篇最核心，读两遍 |
| [03 MCP 和 Skill 是什么](./03-mcp-and-skills.md) | 知道「能力」和「流程」是两码事 | 读完能看懂别人的配置 |
| [04 搭出你的第一个 Agent](./04-build-your-first-agent.md) | 真的跑起来一个属于你的 agent | 动手，别只看 |
| [05 记忆与错误台账](./05-memory-and-mistakes.md) | 让 agent 不再重复犯同一个错 | 动手 |
| [06 新手常踩的坑](./06-pitfalls.md) | 提前知道哪里会翻车 | 边做边对照 |
| [07 最佳实践清单](./07-best-practices.md) | 一份能贴在墙上的检查表 | 每次动手前扫一眼 |
| [08 接下来往哪走](./08-level-up.md) | 什么时候该升级、该上框架 | 最后读 |

如果你只想尽快摸到东西，最短路径是：**02 → 04 → 06**。先弄明白循环，再动手跑通，然后立刻知道坑在哪。

## 我参考了什么，哪些地方有分歧

写之前我把全网能找到的入门资料翻了一遍，下面这些是我实际用到并核对过的来源。放在这里不是为了显得权威，而是想让你知道：**这套教程的结论不是我一个人拍的**，你有不同意见，可以顺着这些链接自己去验证。

- IABAC，[Building AI Agents in 10 Easy Steps](https://iabac.org/blog/building-ai-agents-in-10-easy-steps)（2026）
- Centre for Behavioral Science，[AI Agent Development Skills: A Practical Guide for 2026](https://www.cbs.com.sg/ai-agent-development-skills-a-practical-guide-for-2026)
- Tech With Sanjay，[AI Agent Building Guide – No Code Framework](https://www.techwithsanjay.in/2026/06/ai-agent-building-guide-no-code-framework-2026.html)（2026）
- AI Discoveries，[How to Create a Personal AI Agent](https://aidiscoveries.io/how-to-create-a-personal-ai-agent-a-practical-guide-for-2026/)（2026）
- TheAI 學院，[打造你的第一個 AI Agent](https://www.theai.tw/guide/build-your-first-ai-agent-2026)（2026）
- Hustle to AI，[What Are AI Agents for Developers?](https://www.hustletoai.com/blog/ai-agentic-systems-5/what-are-ai-agents-for-developers-61)（2026）
- Amanai Lab，[Building Your First AI Agent: A Realistic Step-by-Step Guide](https://www.amanailab.com/blog/building-your-first-ai-agent)
- LearnAI，[How to Build AI Agents in 2026](https://www.uselearnai.com/blog/how-to-build-ai-agents-beginners-guide-2026)
- Agent 101，[How to Build an AI Agent in 2026: The Complete Beginner's Guide](https://agent101.net/how-to-build-an-ai-agent-in-2026-the-complete-beginners-guide)
- Red Hat Developers，[MCP servers vs. skills](https://developers.redhat.com/articles/2026/05/25/mcp-servers-vs-skills-choosing-right-context-your-ai)（2026）
- DEV Community，[MCP vs Skill: An Evolutionary Perspective](https://dev.to/openwaygate/mcp-vs-skill-an-evolutionary-perspective-gkb)
- Web Pulse，[MCP vs. Agent Skills: A Decision Framework for Context Engineering](https://wpnews.pro/news/mcp-vs-agent-skills-a-decision-framework-for-context-engineering)

**大家的共识**很一致，几乎每一篇都在说同一件事：从一个小而明确的任务开始，工具别贪多，记忆要早设计，防护栏不能省，从第一天就留日志。这一套我全盘接受了，第 06、07 章基本就是在展开它。

**分歧**也真实存在，而且挺有意思。一派（IABAC、Hustle to AI）鼓励你直接上框架，LangChain、CrewAI、LangGraph 都被点名推荐；另一派（Amanai Lab、TheAI 學院）坚持让你先手写那个几十行的循环，说「手刻一遍比看一百篇教程学到的都多」。我在第 08 章没有替你选边，而是把两边的理由都摆出来，你自己按情况定。

来源更新到 2026 年前后，里面提到的具体模型版本我刻意没往正文里写——这类东西半年就过时一次，写进去只会误导你。具体选型那部分我留了判断方法，没留标准答案。
