# WorkSeed Workspace Template v0.1.2

## 中文发布摘要

发布版本：`workspace-template-v0.1.2`

发布类型：模板补丁发布

主要变化：强化 Core 能力加载后的运行时可见性验证流程，明确源控制线程
和测试线程的职责边界，让最终记录只由源线程在读回测试结果、检查
Workspace 状态漂移并重新跑本地检查后写入。

采用边界：这是 Workspace Template 发布，不等于真实 Workspace 推出或采用，也
不等于 Prism/Mark/mira 已完成真实业务使用验证。

需要人工确认或后补的依赖：真实 Workspace 采用、真实业务素材、适配器
连接、外部任务系统写入和运行时刷新结果仍需在目标 Workspace 内单独验证。

没有做：没有执行真实 Workspace 推出或采用，没有连接适配器，没有写入外部
任务系统，没有加入客户事实、原始素材、敏感接入信息或账号状态。

验证结果：发布记录包含源控制线程、运行时可见性测试线程、状态漂移修复、
本地检查重跑和测试线程归档证据。

隐私边界：Template 只发布通用初始化、能力加载、运行时可见性验证和记录
规则；不包含客户私有事实、原始素材、敏感接入信息或真实账号状态。

## 技术变化

- 保留初学者优先使用 Core 压缩包的安装路径。
- 增加标准的运行时可见性测试线程协议。
- 明确源控制线程拥有最终记录，测试线程只负责运行时可见性验证。
- 要求源线程读回测试结果后，先检查 Workspace 状态是否漂移，再写入最终记录。
- 要求测试线程验证结束后由源线程归档，避免测试上下文变成新的执行主线。

## 受影响范围

- Template 可继承内容：初始化说明、Core 能力加载流程、运行时可见性验证提示词、记录模板和本地检查器。
- 新 Workspace 需要执行内容：提供 Core 压缩包、确认安装、重开或刷新 Codex、验证子智能体和技能是否可见。
- 不属于 Template 的内容：真实项目事实、客户材料、账号状态、适配器配置和外部任务系统内容。

## 使用或采用方式

1. 在 GitHub 上使用模板创建自己的 Workspace 仓库。
2. 克隆到本地后先阅读 `WORKSPACE.md` 和 `README.md`。
3. 按初始化提示提供 Core 压缩包，并在确认后安装能力文件。
4. 使用运行时可见性提示词验证当前 Codex 是否看见项目子智能体和技能。
5. 由源线程读回测试结果，检查状态漂移，再写入 capability-load record。

## 验证证据

- Git 标签：`workspace-template-v0.1.2`
- GitHub Release：已发布并读回。
- 本地检查：`check_sync.py`、`check_workspace_deployment.py`、`verify_open_box.py`
- 证据线程：源控制线程和运行时可见性测试线程均已记录。

## 明确没有做

- 没有替任何真实 Workspace 完成采用。
- 没有连接适配器。
- 没有写入外部任务系统。
- 没有加入客户事实、原始素材、敏感接入信息或账号状态。

## 隐私和边界

本发布只包含公开模板、初始化流程、能力加载流程、验证提示词和检查器；不包含
客户资料、原始素材、私有链接、账号状态、凭证、外部任务内容或真实 Workspace
私有记录。

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
