#!/usr/bin/env python3
"""初始化项目的记忆层：CLAUDE.md / mistakes-ledger.md / docs/adr/。

默认不覆盖已存在文件；需要覆盖时显式加 --force。

用法：
    python init_project_memory.py <目标项目目录> [--force]
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

def find_templates() -> Path:
    """脚本在 <repo>/skills/<skill>/scripts/ 下，向上找到含 templates/ 的仓库根。"""
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "templates"
        if candidate.is_dir() and (candidate / "mistakes-ledger.md").exists():
            return candidate
    return here.parents[min(3, len(here.parents) - 1)] / "templates"


TEMPLATES = find_templates()


def main() -> int:
    ap = argparse.ArgumentParser(description="初始化项目记忆层（不覆盖已存在文件）")
    ap.add_argument("target", nargs="?", default=".", help="目标项目目录，默认当前目录")
    ap.add_argument("--force", action="store_true", help="覆盖已存在文件")
    args = ap.parse_args()

    target = Path(args.target).resolve()
    if not target.is_dir():
        print(f"[error] 不是目录：{target}", file=sys.stderr)
        return 2
    if not TEMPLATES.is_dir():
        print(f"[error] 找不到模板目录：{TEMPLATES}", file=sys.stderr)
        return 2

    for src_name, dst_name in (("CLAUDE.project-template.md", "CLAUDE.md"),
                               ("mistakes-ledger.md", "mistakes-ledger.md")):
        src, dst = TEMPLATES / src_name, target / dst_name
        if not src.exists():
            print(f"[skip] 模板缺失：{src}")
            continue
        if dst.exists() and not args.force:
            print(f"[skip] 已存在，不覆盖：{dst}")
            continue
        shutil.copy2(src, dst)
        print(f"[write] {dst}")

    adr = target / "docs" / "adr"
    if adr.exists():
        print(f"[skip] 已存在：{adr}")
    else:
        adr.mkdir(parents=True, exist_ok=True)
        print(f"[mkdir] {adr}")

    print("\n下一步：填写 CLAUDE.md 中的项目目标、技术栈、常用命令与坑点。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
