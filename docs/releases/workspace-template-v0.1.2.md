# WorkSeed Workspace Template v0.1.2

## 中文发布摘要

发布版本：`workspace-template-v0.1.2`

发布类型：Template patch

主要变化：强化 Core 能力加载后的运行时可见性验证流程，明确 source/control
thread 和 test thread 的职责边界，让最终记录只由源线程在读回测试结果、检查
Workspace 状态漂移并重新跑本地检查后写入。

采用边界：这是 Workspace Template 发布，不等于真实 Workspace rollout，也
不等于 Prism/Mark/mira 已完成真实业务使用验证。

需要人工确认或后补的依赖：真实 Workspace 采用、真实业务素材、adapter
连接、外部任务系统写入和运行时刷新结果仍需在目标 Workspace 内单独验证。

没有做：没有执行真实 Workspace rollout，没有连接 adapter，没有写入外部
任务系统，没有加入客户事实、raw assets、敏感接入信息或账号状态。

验证结果：发布记录包含 source/control thread、runtime visibility test
thread、状态漂移修复、本地检查重跑和测试线程归档证据。

隐私边界：Template 只发布通用初始化、能力加载、运行时可见性验证和记录
规则；不包含客户私有事实、原始素材、敏感接入信息或真实账号状态。

Status: published

Core base: `ws-core-v0.3.0`

Purpose: Core capability loading / runtime visibility workflow hardening.

Git tag: `workspace-template-v0.1.2`

GitHub Release: `https://github.com/raymondhyg/workseed-workspace-template/releases/tag/workspace-template-v0.1.2`

## What Changed

- Keeps the beginner zip-first install path from `workspace-template-v0.1.1`.
- Adds a standard runtime visibility test-thread protocol.
- Clarifies that the source/control thread owns final records.
- Clarifies that a test thread only verifies runtime visibility and must not
  edit files, execute project tasks, connect adapters, or write external
  systems.
- Requires source-thread read-back before capability-load records are marked
  `verified`.
- Requires source-thread state-drift checks before writing final status.
- Requires the source thread to archive the test thread after verification.

## Evidence Threads

- Source/control thread:
  `019f2b63-310b-7640-af0c-77670017b5c4`
- Runtime visibility test thread:
  `019f2b70-8f29-7c61-b9d5-af3d896a1cb1`

Observed result: the test thread verified runtime availability, then the source
thread read the result, detected Workspace state drift, reinstalled the standard
Core runtime zip, updated local records only after state alignment, reran local
checks, and archived the test thread.

## Claim Boundary

This publication creates the `workspace-template-v0.1.2` Template tag and
GitHub Release only.

No real Workspace rollout was performed.

No adapter was connected.

No external task system was written.

No private customer facts, raw assets, credentials, private links, or account
state were added.
