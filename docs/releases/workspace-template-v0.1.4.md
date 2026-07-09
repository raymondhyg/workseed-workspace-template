# WorkSeed Workspace Template v0.1.4

## 中文发布摘要

发布版本：`workspace-template-v0.1.4`

发布类型：Template PATCH

发布日期：2026-07-09

关联 Core：`ws-core-v0.3.1`

本版本修复 Workspace Template 在加载 WorkSeed Core v0.3.1 运行面时漏装
`capability-radar` 的问题。旧的 Template v0.1.3 安装器会把
`.codex/agents/capability-radar.toml` 和 `.agents/skills/capability-radar`
列为 skipped，导致安装结果显示 `missing: none`，但雷达能力实际上没有进入
Workspace。

## 技术变化

- `scripts/utils/install_core_capabilities.py` 将
  `.codex/agents/capability-radar.toml` 加入必装 agent 清单。
- `scripts/utils/install_core_capabilities.py` 将
  `.agents/skills/capability-radar` 加入必装 skill 清单。
- `scripts/utils/check_workspace_deployment.py` 将 radar agent 和 skill
  加入 capability-load 后的必检运行面。
- `WORKSPACE.md` 和 `workspace-system-manifest.md` 更新到 Template
  `workspace-template-v0.1.4` 与 Core `ws-core-v0.3.1`。

## 影响范围

受影响的是新 Workspace 从 Template 安装 Core runtime capability files 的路径。
本版本不会自动把 Core 能力装进任何真实 Workspace；它只修复 Template 的安装器
和 checker，使用户在明确提供 Core 包并确认安装后，雷达能力不会被静默跳过。

## 使用或采用方式

新用户应使用 `workspace-template-v0.1.4` 作为 Template 包，并配合 Core 包：

```powershell
python scripts/utils/install_core_capabilities.py --zip-path "<core-package.zip>" --core-version ws-core-v0.3.1
python scripts/utils/check_sync.py
python scripts/utils/check_workspace_deployment.py
python scripts/utils/verify_open_box.py
```

安装后如 Codex UI 没有立刻显示项目子智能体，应重开 Workspace 或新开窄测试线程
验证 runtime visibility。文件安装、checker 通过、Codex 运行时可见是三个不同
状态。

## 验证证据

- 从 GitHub 读取 Template `workspace-template-v0.1.3` release asset，确认旧包
  SHA256 为 `11a3601ecc3570b1e3b019dc896a4f37ae273ec79b96aabe8de8b1f71ba3c1c2`。
- 从 GitHub `ws-core-v0.3.1` tag 读取 Core 源，确认 Core 包包含
  `capability-radar` agent 和 skill。
- 重置 `E:\Claude Code Projects\workseed-workspace-lab` 为 Template，并装入
  Core `ws-core-v0.3.1`。
- 修复前安装结果：`missing: none`，但 skipped 包含 `capability-radar` agent 和
  skill。
- 修复后安装结果：`missing: none`，`skipped: none`。
- 修复后运行：

```powershell
python scripts/utils/check_sync.py
python scripts/utils/check_workspace_deployment.py
python scripts/utils/verify_open_box.py
```

以上检查均通过。

## 明确没有做

- 没有修改 WorkSeed Core `ws-core-v0.3.1`。
- 没有连接真实 adapter。
- 没有写入外部任务系统。
- 没有声明任何真实 Workspace 已完成采用。
- 没有复制客户事实、私有资料、账号状态、浏览器状态或凭证。

## 隐私和边界

本发布只包含 Template 安装器、checker、入口说明和发布记录。它不包含真实
`.codex/.env`，不包含私有 Core 源访问凭证，不包含客户材料，也不包含任何真实
Workspace 的本地业务事实。
