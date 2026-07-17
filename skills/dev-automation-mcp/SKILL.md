---
name: dev-automation-mcp
description: MCP-backed personal development automation. Use when starting development work, researching Feishu or web materials, avoiding previously recorded mistakes, debugging systematically, reviewing a project across multiple rounds, or turning work into reusable project memory.
---

# Dev Automation MCP

Use this skill to combine MCP tools with repeatable development workflows. MCP provides external capabilities; this skill decides when and how to use them.

## MCP Tool Policy

Prefer these MCP capabilities when available:

- `sequential-thinking`: break down ambiguous work, compare options, audit reasoning, and run multi-round review.
- Feishu/Lark MCP: read product docs, design notes, team decisions, meeting notes, messages, wiki pages, and calendars.
- Search MCP: discover external sources when facts, APIs, laws, package behavior, or versions may have changed.
- Web reader/fetch MCP: read specific URLs and convert them into concise evidence.
- Playwright MCP: inspect sites, reproduce browser flows, validate UI behavior, or run visual checks.
- Context/library docs MCP: read current framework or SDK documentation before changing code that depends on it.
- Memory MCP, when configured: retrieve and write durable rules, decisions, and repeated mistakes.

If an MCP is unavailable, state the missing capability and use the best local fallback.

## Start Workflow

For development tasks:

1. Read local context first: `CLAUDE.md`, `mistakes-ledger.md`, README, package files, related source, tests, and recent changes.
2. Identify the target, constraints, unknown facts, likely failure modes, and validation command.
3. Use MCP research before implementation if the task depends on Feishu docs, web pages, external APIs, third-party libraries, permissions, product decisions, or unstable facts.
4. If `mistakes-ledger.md` has related entries, explicitly name the prevention rule that applies now.
5. Implement the smallest coherent change that matches existing project patterns.
6. Verify with the most relevant test, build, typecheck, lint, browser run, or API call.
7. Run the multi-round audit before finalizing substantial work.

## Research Workflow

For Feishu/web research:

1. Convert the user request into concrete questions.
2. Query project sources and Feishu first when the topic is product-specific.
3. Query external search only for public docs, package behavior, examples, or current facts.
4. Prefer official docs, source repositories, standards, API responses, and project tests over blogs.
5. Record each important conclusion with source, date, version, and confidence.
6. Separate facts from inferences.
7. End with executable recommendations and remaining unknowns.

Read `references/mcp-setup.md` when configuring MCP servers.

## Mistake Prevention

Always look for a project `mistakes-ledger.md`. If absent and the task is non-trivial, create one from this structure:

```markdown
# Mistakes Ledger

## Entries

### YYYY-MM-DD - Title

- Context:
- Mistake:
- Root cause:
- Detection signal:
- Prevention rule:
- Verification next time:
```

Before changing code, scan for related entries. After any material miss, failed assumption, repeated bug, or verification gap, append an entry.

## Multi-Round Audit

Run these rounds for substantial changes, project reviews, and release checks:

1. Requirement fit: user goal, product docs, scope, omissions, overreach.
2. Code correctness: main path, edge cases, error handling, state, concurrency, resource cleanup.
3. Data and security: auth, permissions, input validation, secrets, logs, migrations, rollback.
4. Tests and regression: changed behavior, missing cases, fixture quality, deterministic checks.
5. Delivery quality: docs, config, startup, environment, observability, residual risks.

Output findings by severity with file or source references where possible. Fix critical issues before finalizing unless the user asked only for review.

## Session Retrospective

At the end of meaningful work:

- State what changed and what was verified.
- State what remains unverified.
- Update `mistakes-ledger.md` for reusable prevention rules.
- Update `CLAUDE.md` only for durable project knowledge, commands, architecture decisions, or recurring traps.

