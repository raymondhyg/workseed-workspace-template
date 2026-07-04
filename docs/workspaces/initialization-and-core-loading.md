# Workspace Initialization And Core Loading

This guide explains how a new WorkSeed Workspace moves from first greeting to a
usable Workspace state.

It is version-aware. The current Template baseline is `workspace-template-v0.1.2`
with Core base `ws-core-v0.3.0`, but the loading pattern should work for later
Core packages too.

## First Principle

The Template is a clean Workspace starting point. Core is the capability source.
WorkSeed Core is the continuously iterating capability core. A Workspace should
record which Core version and runtime surfaces it has loaded instead of
assuming it always has the newest Core behavior.

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

A new user does not need to know WorkSeed terms. If they say things like
`帮我初始化`, `安装 Core`, `安装能力`, `给我指引一下`, `告诉我下一步怎么做`, or
`我不知道怎么开始`, treat that as a request to start the guided initialization
flow.

Natural language triggers start guidance only. They do not authorize a real
write install. They also do not authorize the receiving AI to auto-scan the
computer for a Core checkout or to silently use a path found in Workspace
files. The receiving AI should first ask the user where the Core zip package
is. The user can paste a file path or drop the zip file into the chat.

Before a receiving AI runs an install command without `--dry-run`, writes a
capability-load record, or changes the manifest, it must pause and ask the user
to confirm the selected Core zip package and write action.

Use this as the first message in a new Template Workspace:

```text
你好，请帮我初始化这个 WorkSeed Workspace，并一步一步指引我安装和使用 Core 能力。

我可能不熟悉 AI 和 WorkSeed，请用通俗的话告诉我：
1. 你是谁；
2. 这个 Workspace 是做什么的；
3. Core 是什么；
4. 我下一步应该做什么。

先不要直接执行项目任务。

请先读取：
1. WORKSPACE.md
2. workspace-system-manifest.md
3. AGENTS.md
4. docs/workspaces/receiver-operating-standard.md
5. docs/workspaces/entry-and-record-standard.md
6. docs/workspaces/upgrade-playbook.md
7. workspace-records/README.md
8. docs/workspaces/initialization-and-core-loading.md

然后先用 2-3 句话介绍自己：你是这个 Workspace 的 Codex 协作者，不是
WorkSeed Core 本体；你会先保护本地事实，再按版本加载 Core 能力。

再用清单方式确认：
- 当前 Workspace 名称、owner、用途是否仍是模板默认值
- 当前 Core base version
- 当前 Template version
- 当前身份是 Workspace，不是 Core
- 哪些内容属于本地 Workspace 私有事实
- 是否已经安装可运行 Core capability files，例如 .codex/agents 和 .agents/skills
- 如果尚未安装，请不要自动扫描我的电脑，也不要直接使用文件里写着的默认 Core 路径
- 请先问我 Core 压缩包在哪里；我可以贴 zip 路径，也可以把 zip 文件丢进聊天框
- 如果我还没有 Core 压缩包，请用最简单的话告诉我获取方式：
  1. 联系 Raymond 微信：18002997691
  2. 关注抖音 @有光蔓延【1688运营】，抖音号：289566513，并加入粉丝群获取
- 在正式运行不带 `--dry-run` 的安装命令、写 capability-load record、或改 manifest 前，必须先停下来确认
- 确认时请用通俗话列出：将使用的 Core zip、将安装哪些类型的文件、会写入哪些本地记录、不会做哪些事
- 只有我明确回复类似“确认安装”“用这个来源安装”“继续正式安装”后，才可以执行真实安装
- 如果我只说“安装 Core”或“安装能力”，这只是进入安装引导，不等于授权立即写入文件
- 初始化前不修改真实项目事实、不连接 adapter、不写外部任务系统

请最后给我一个“下一步我只需要回复什么”的简单提示。
```

## Initialization Stages

| Stage | Purpose | Evidence |
|---|---|---|
| 1. Greeting | Establish Workspace identity and boundaries | AI echoes identity, Core base, Template version, and non-actions |
| 2. Local identity | Replace template defaults with real Workspace fields | `workspace-system-manifest.md`, `WORKSPACE.md` |
| 3. Core capability source | Ask for the Core zip package location | user-provided zip path or dropped zip file |
| 4. Pre-install confirmation | Ask for explicit confirmation before write install | user confirms source and write action |
| 5. Capability install | Copy safe runtime capability files | `.codex/agents/**`, `.agents/skills/**`, supporting docs/templates |
| 6. State writeback | Update local install state without claiming runtime availability | capability-load record plus manifest state row |
| 7. Verification | Run local checks | `check_workspace_deployment.py`, `check_sync.py`, `verify_open_box.py` |
| 8. Runtime availability | Reopen or restart Codex and verify project agents/skills | `templates/core-runtime-availability-verification-prompt.md`, updated capability-load record |
| 9. Source-thread verification | If a separate test thread was used, read back its report and compare against current Workspace files | source/control thread report |
| 10. Record and archive | Preserve what was loaded and what remains unverified, then archive any narrow test thread after source verification | `workspace-records/capability-loads/**`, archived test thread evidence |

## Confirmation Gate

The receiving AI may read Workspace files to understand the Workspace state,
but it should not auto-scan the computer for Core or silently use a Core path
recorded in local files. For new users, the default installation path is a Core
zip package provided by the user.

It must not run the real install command, create/update a capability-load
record, or change `workspace-system-manifest.md` until the user explicitly
confirms. A path found in `workspace-system-manifest.md` or an example command
is not a candidate to auto-use; ask the user for the Core zip location instead.

Recommended confirmation wording:

```text
你给我的 Core 压缩包是：<zip path>。
正式安装会写入 .codex/agents、.agents/skills、部分支持文档/模板，并创建 capability-load record。
不会修改真实项目事实、不会连接 adapter、不会写外部任务系统。

如果确认用这个来源安装，请回复：确认安装。
```

## Loading From A Zip Package

Use this when the user has received a Core zip package:

```powershell
python scripts/utils/install_core_capabilities.py --zip-path "<core-runtime-package.zip>" --core-version ws-core-v0.3.0
```

Do not run this command for real until the user explicitly confirms. Use
`--dry-run` first when checking a candidate package.

The installer extracts the zip into a temporary folder, finds the Core package
root, copies only the approved capability runtime surfaces, and writes a local
capability-load record.

## How To Get The Core Zip Package

If the user already has a Core zip package, ask for its exact location or ask
them to drop the zip file into the chat.

If the user does not have the package yet, explain the access path in plain
language:

- Contact Raymond on WeChat: `18002997691`
- Follow Douyin `@有光蔓延【1688运营】`, Douyin ID: `289566513`
- Use the QR image at `docs/assets/douyin-youguangmanyan-1688.jpg` to follow
  and join the fan group

Plain-language reason: the Workspace is intended to be shared for free inside
the private community. Joining through WeChat or the Douyin fan group lets
users receive updates, ask for help, and stay reachable for future win-win
business cooperation.

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

Runtime availability must be checked from the generated Workspace itself. A
Core thread, Template thread, projectless thread, or another Workspace cannot
prove that this Workspace's project agents and skills are visible. In Codex
Desktop, open the generated Workspace as the active project first, then run the
runtime verification prompt there.

After restart or when opening a fresh Codex thread in this Workspace, use:

```text
templates/core-runtime-availability-verification-prompt.md
```

If the source thread cannot see project agents but the Workspace may need a
fresh Codex runtime to test visibility, use a separate narrow test thread:

```text
templates/runtime-visibility-test-thread-prompt.md
```

The source thread owns the final truth. The test thread must only verify
runtime visibility. It should not edit files, execute project tasks, connect
adapters, write external systems, or claim product-grade/source-equivalent
readiness. After the test thread reports, the source thread must:

1. read the test report,
2. confirm the test ran in the same Workspace root,
3. compare the report with the current `.codex/agents/**`, `.agents/skills/**`,
   local checks, and latest capability-load record,
4. repair state drift before writing `verified`,
5. update `WORKSPACE.md`, `workspace-system-manifest.md`, and the latest
   capability-load record only when evidence still matches,
6. archive the test thread after verification and report the archive evidence.

This prompt asks the receiving Codex runtime to inspect the installed
`.codex/agents/**` and `.agents/skills/**` surfaces, report which named
capabilities are visible or callable in the current runtime, and update the
capability-load record only when evidence exists.

The capability-load record must distinguish installed, missing, and skipped
surfaces. It must also record runtime availability as `verified`,
`not verified`, or `requires reopen/restart`. Do not use a green file check as
a substitute for runtime availability.

After a successful real install, update the Workspace's local state surfaces so
future readers do not see the old default state:

- keep the capability-load record as the install evidence,
- update `workspace-system-manifest.md` so `Core capability runtime loading`
  changes from `Not installed by default` to installed for the recorded Core
  package,
- keep `Runtime availability` as `not verified` until the active Codex runtime
  actually sees or can call the project agents/skills,
- do not change the public Template's default state when editing a generated
  Workspace.

## Claim Boundary

After initialization and loading, the Workspace may claim:

- Core base version recorded,
- Template version recorded,
- capability runtime files installed if the record and files exist,
- local checks passed if commands passed.
- runtime availability only when the receiving Codex runtime has actually made
  the expected project agents or skills visible or callable.

It must not claim:

- product-grade readiness,
- source-equivalent capability,
- real adapter connected,
- external task system updated,
- private Core GitHub access,
- live Mark/mira/Prism output without Workspace-owned evidence.
