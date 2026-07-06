# WorkSeed Workspace Template v0.1.3 Candidate

## 中文发布摘要

发布版本：`workspace-template-v0.1.3` candidate

发布类型：Template PATCH candidate

当前状态：本地候选已落地，尚未 tag、尚未 GitHub Release、尚未发布。

主要变化：

- 新增网络健康与重连恢复开箱指引。
- 新增独立网络健康指南线程提示词，避免在网络不稳定时继续推进项目任务。
- 新增 `.codex/.env` 本地网络配置模板，用于端口或代理控制。
- 新增只读检查脚本 `python scripts/utils/check_network_health.py`，只输出 key 名和值已打码状态。
- 新增 `workspace-records/checks/network-health-check-template.md`，用于记录诊断、重启/重开和用户确认结果。
- 显式忽略 `.codex/.env`，允许本地修复但禁止真实本地 env 被 Git 跟踪。

采用边界：

- 适用于新 Workspace 初始化、Core 安装引导后，以及使用中遇到反复重连、网络不稳定、端口、代理、VPN 或 `.codex/.env` 问题时。
- 默认流程是保留源线程，创建或指引用户创建网络健康指南线程，在窄线程里判断网络状态并参照成功路线处理。
- 成功路线是 Workspace 本地 `.codex/.env` 端口或代理控制，然后重启或重开 Codex，再由用户确认重连是否停止。

没有做：

- 没有发布 `workspace-template-v0.1.3`。
- 没有创建 tag 或 GitHub Release。
- 没有修改真实 Workspace。
- 没有连接 adapter。
- 没有写外部任务系统。
- 没有承诺所有网络问题永久解决。

验证结果：

- `python scripts/utils/check_network_health.py`
- `python scripts/utils/check_workspace_deployment.py`
- `python scripts/utils/check_sync.py`
- `python scripts/utils/check_network_health_guidance_replay.py`
- `python scripts/utils/check_network_health_redaction.py`
- `python scripts/utils/check_workspace_template_v0_1_3_package_readiness.py`
- `python scripts/utils/check_workspace_template_v0_1_3_release_preflight.py`
- `python scripts/utils/verify_open_box.py`

隐私边界：

- 不提交真实 `.codex/.env`。
- 不打印端口或代理值。
- 报告只列 key 名、是否存在、是否识别、下一步动作。
- 不复制用户机器网络私有值、账号状态、项目事实或外部系统内容。

## Technical Change

This candidate turns a prior repeated-reconnect recovery lesson into a
Template-owned support capability. The Template now includes:

- `docs/workspaces/network-health-and-reconnect-guide.md`
- `templates/network-health-guidance-thread-prompt.md`
- `templates/network-health-source-thread-handoff-template.md`
- `templates/codex-env-network-template.txt`
- `scripts/utils/check_network_health.py`
- `scripts/utils/check_network_health_redaction.py`
- `workspace-records/checks/network-health-check-template.md`
- `scripts/utils/check_network_health_guidance_replay.py`
- `scripts/utils/check_workspace_template_v0_1_3_package_readiness.py`
- `scripts/utils/check_workspace_template_v0_1_3_release_preflight.py`
- `workspace-records/feedback/network-health-core-feedback-template.md`

The deployment checker now requires these surfaces and verifies that
`.codex/.env` remains local and untracked.

The release preflight additionally requires the candidate files to be present
in the release commit, visible in `HEAD`, and free of uncommitted changes before
any tag/archive operation. A local worktree can pass package readiness while
still failing release preflight if required files are not yet committed.

## Status Boundary

This file is a candidate release note only. It does not claim publication,
Workspace Lab proof, real Workspace adoption, or permanent runtime repair.
