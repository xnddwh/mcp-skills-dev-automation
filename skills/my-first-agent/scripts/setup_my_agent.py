#!/usr/bin/env python3
"""新手一键搭建自己的 agent：问 4 个问题，生成 3 个起步文件。

这是新手接触本仓库的第一个脚本（零依赖，只用 Python 标准库）。

生成内容（默认不覆盖已存在的文件，加 --force 才覆盖）：
    AGENT.md             你的 agent 说明书（目标 / 规则 / 常用命令）
    mistakes-ledger.md   错误台账（与主项目 templates/ 同一格式）
    first-tasks.md       第一周练习任务（3 个小任务）

用法：
    python setup_my_agent.py [输出目录] [--force]

与原有模块的衔接：
    - mistakes-ledger.md 直接复用仓库根 templates/ 里的模板（和
      dev-automation-mcp 的 init_project_memory.py 用的是同一份）；
    - 生成的 AGENT.md 格式与 CLAUDE.md 兼容，升级完整版时可直接并入。
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

# 向上找到仓库根的 templates/（本脚本位于 skills/my-first-agent/scripts/ 下）
def find_templates() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "templates"
        if (candidate / "mistakes-ledger.md").exists():
            return candidate
    return Path("templates")  # 找不到时退回相对路径，让报错信息可读


TEMPLATES = find_templates()

# ---------- 交互问答 ----------

QUESTIONS = [
    ("怎么称呼你？", "新手"),
    ("你最近在做什么方向的事？（例：学 Python / 做个人网站）", "学习编程"),
    ("常用语言或工具？（例：Python + VS Code）", "Python"),
    ("最想先让 agent 帮你做什么？（例：解释代码、改小 bug）", "解释代码"),
]


def ask() -> dict:
    """逐题提问；回车用默认值；在无法交互的环境（如 CI）直接全用默认值。"""
    answers = {}
    for question, default in QUESTIONS:
        try:
            raw = input(f"{question}（直接回车 = {default}）> ").strip()
        except EOFError:  # 非交互环境：input 会立刻抛 EOF
            raw = ""
        answers[question] = raw or default
    return answers


# ---------- 生成文件 ----------

def render_agent_md(a: dict) -> str:
    """AGENT.md：新手 agent 的'员工手册'。"""
    return f"""# AGENT.md — 我的 agent 说明书

> 本文件由 setup_my_agent.py 生成。agent 每次开工前先读这里。

## 我是谁

- 称呼：{a['怎么称呼你？']}
- 方向：{a['你最近在做什么方向的事？（例：学 Python / 做个人网站）']}
- 常用工具：{a['常用语言或工具？（例：Python + VS Code）']}

## 我最想让你先帮我

{a['最想先让 agent 帮你做什么？（例：解释代码、改小 bug）']}

## 给 agent 的三条规则（新手版）

1. 动手前先读本文件和 mistakes-ledger.md。
2. 需求不清楚就问我一句，不要猜。
3. 做完必留痕：成功写进下方"常用命令"，失败写进 mistakes-ledger.md。

## 常用命令（做通一条就记一条）

```text
（示例）python --version        # 确认 Python 可用
（在这里补充你验证过的命令）
```
"""


def render_first_tasks(a: dict) -> str:
    """first-tasks.md：第一周的 3 个练习，难度递增。"""
    return f"""# 第一周练习（{a['怎么称呼你？']}的第一周）

每完成一个打一个勾，并检查 mistakes-ledger.md 是否有新记录。

- [ ] 任务 1（只看不改）：让 agent 解释你项目里一个文件的作用。
      验收：你能用自己的话复述它说了什么。
- [ ] 任务 2（小改动）：让 agent 做一个 5 分钟内能完成的小修改。
      验收：改动前后各跑一次验证命令，把命令记进 AGENT.md。
- [ ] 任务 3（踩坑记录）：故意问一个 agent 答错的问题，
      把"它错在哪、下次怎么防"写进 mistakes-ledger.md。
      验收：台账里多了一条带"Prevention rule"的记录。
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="新手一键搭建自己的 agent（不覆盖已存在文件）")
    ap.add_argument("target", nargs="?", default=".", help="输出目录，默认当前目录")
    ap.add_argument("--force", action="store_true", help="覆盖已存在文件")
    ap.add_argument("--answers", nargs=4, metavar=("NAME", "FOCUS", "TOOLS", "WISH"),
                    help="非交互模式：直接给 4 个答案，跳过提问")
    args = ap.parse_args()

    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)  # 目录不存在就建

    # 1) 收集答案：命令行给过就用命令行的，否则交互提问
    if args.answers:
        a = dict(zip([q for q, _ in QUESTIONS], args.answers))
    else:
        a = ask()

    # 2) 生成 AGENT.md 与 first-tasks.md（内容内嵌在脚本里，改模板改这里）
    files = {
        "AGENT.md": render_agent_md(a),
        "first-tasks.md": render_first_tasks(a),
    }
    for name, content in files.items():
        dst = target / name
        if dst.exists() and not args.force:
            print(f"[skip] 已存在，不覆盖：{dst}")
            continue
        dst.write_text(content, encoding="utf-8")
        print(f"[write] {dst}")

    # 3) 错误台账：直接复用仓库根 templates/ 的同一份模板（衔接点）
    src = TEMPLATES / "mistakes-ledger.md"
    dst = target / "mistakes-ledger.md"
    if src.exists():
        if dst.exists() and not args.force:
            print(f"[skip] 已存在，不覆盖：{dst}")
        else:
            shutil.copy2(src, dst)
            print(f"[write] {dst}（复用 templates/ 同款格式）")
    else:
        print(f"[warn] 找不到 {src}，请手动从仓库 templates/ 复制")

    # 4) 收尾提示：告诉新手下一步做什么
    print(
        "\n下一步：\n"
        f"  1. 打开 {target / 'AGENT.md'} 检查内容\n"
        "  2. 把 skills/my-first-agent/ 复制到你所用 agent 的 skills 目录\n"
        "  3. 对 agent 说：使用 my-first-agent，完成 first-tasks.md 里的任务 1"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
