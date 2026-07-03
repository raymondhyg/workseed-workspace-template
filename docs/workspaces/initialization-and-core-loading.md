# Workspace Initialization And Core Loading

This guide explains how a new WorkSeed Workspace moves from first greeting to a
usable Workspace state.

It is version-aware. The current Template baseline is `workspace-template-v0.1.0`
with Core base `ws-core-v0.3.0`, but the loading pattern should work for later
Core packages too.

## First Principle

The Template is a clean Workspace starting point. Core is the capability source.

A new Workspace should first understand its own identity, then load or install
Core capability files only when needed.

Plain-language rule:

```text
Initialize the Workspace first.
Load Core capability packages second.
Keep private project facts local.
Record what was loaded and verified.
```

## First Greeting Prompt

Use this as the first message in a new Template Workspace:

```text
你好，请先按 WorkSeed Workspace 初始化流程开始，不要直接执行项目任务。

请先读取：
1. WORKSPACE.md
2. workspace-system-manifest.md
3. AGENTS.md
4. docs/workspaces/receiver-operating-standard.md
5. docs/workspaces/entry-and-record-standard.md
6. docs/workspaces/upgrade-playbook.md
7. workspace-records/README.md
8. docs/workspaces/initialization-and-core-loading.md

然后先用 2-3 句话介绍自己：你是这个 Workspace 的 Codex 协作者，
不是 WorkSeed Core 本体；你会先保护本地事实，再按版本加载 Core 能力。

再只回声确认：
- 当前 Workspace 名称、owner、用途是否仍是模板默认值
- 当前 Core base version
- 当前 Template version
- 当前身份是 Workspace，不是 Core
- 哪些内容属于本地 Workspace 私有事实
- 是否已经安装可运行 Core capability files，例如 .codex/agents 和 .agents/skills
- 如果尚未安装，下一步应该从 Core repo、Core package folder，还是 zip 包加载
- 初始化前不修改真实项目事实、不连接 adapter、不写外部任务系统
```

## Initialization Stages

| Stage | Purpose | Evidence |
|---|---|---|
| 1. Greeting | Establish Workspace identity and boundaries | AI echoes identity, Core base, Template version, and non-actions |
| 2. Local identity | Replace template defaults with real Workspace fields | `workspace-system-manifest.md`, `WORKSPACE.md` |
| 3. Core capability source | Choose Core source: local repo, package folder, or zip | user-provided path, version, or extracted package |
| 4. Capability install | Copy safe runtime capability files | `.codex/agents/**`, `.agents/skills/**`, supporting docs/templates |
| 5. Verification | Run local checks | `check_workspace_deployment.py`, `check_sync.py`, `verify_open_box.py` |
| 6. Record | Preserve what was loaded | `workspace-records/capability-loads/**` |

## Loading From A Local Core Repo

Use this when the Workspace can read a local WorkSeed Core checkout:

```powershell
python scripts/utils/install_core_capabilities.py --source-path "E:\Claude Code Projects\WorkSeed" --core-version ws-core-v0.3.0
```

## Loading From A Core Package Folder

Use this when Core has been provided as an extracted folder:

```powershell
python scripts/utils/install_core_capabilities.py --source-path "D:\Downloads\workseed-core-package" --core-version ws-core-v0.3.0
```

## Loading From A Zip Package

Use this when the user cannot access the private Core GitHub repository and
receives a zip file instead:

```powershell
python scripts/utils/install_core_capabilities.py --zip-path "D:\Downloads\workseed-core-ws-core-v0.3.0.zip" --core-version ws-core-v0.3.0
```

The installer extracts the zip into a temporary folder, finds the Core package
root, copies only the approved capability runtime surfaces, and writes a local
capability-load record.

## What Gets Installed

The default installer copies only safe, reusable capability runtime surfaces
when they exist in the Core package:

- `.codex/agents/*.toml`
- `.agents/skills/*/SKILL.md`
- `docs/codex/prism-knowledge-writeback.md`
- `docs/capability-packs/**`
- `docs/core/p1/**`
- selected capability templates under `templates/**`

This is enough for `@prism`, `@mark`, and `@mira` style capability use to have
their paired skills and supporting instructions when the local Codex surface
supports project agents.

## What Does Not Get Installed

The installer must not copy:

- customer facts,
- project-private files,
- raw materials,
- account state,
- credentials,
- private links,
- real adapter configuration,
- external task-system contents,
- Core release working history that is not required for runtime capability use.

## After Installing

Run:

```powershell
python scripts/utils/check_workspace_deployment.py
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
```

Then restart or reopen the Workspace in Codex if project agents or skills do
not appear immediately. File installation and Codex UI runtime refresh are
different steps.

## Claim Boundary

After initialization and loading, the Workspace may claim:

- Core base version recorded,
- Template version recorded,
- capability runtime files installed if the record and files exist,
- local checks passed if commands passed.

It must not claim:

- product-grade readiness,
- source-equivalent capability,
- real adapter connected,
- external task system updated,
- private Core GitHub access,
- live Mark/mira/Prism output without Workspace-owned evidence.
