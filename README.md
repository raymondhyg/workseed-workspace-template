# WorkSeed Workspace Template v0.1.0

这是 WorkSeed 的公开 Workspace 模板仓库。

你可以直接用它创建一个新的 WorkSeed Workspace，然后在自己的 Workspace 里开始项目规划、资料沉淀、执行记录和反馈迭代。

基础来源：

- Core 版本：`ws-core-v0.3.0`
- Template 版本：`workspace-template-v0.1.0`

## 这是什么

- 一个 GitHub Template Repository，用来创建新的 WorkSeed Workspace。
- 一个干净的 Workspace 起点，包含 `WORKSPACE.md`、`workspace-system-manifest.md`、`workspace-records/**`、本地检查脚本和反馈记录结构。
- 一个不带私有资料的安全基线。

## 这不是什么

- 不是 WorkSeed Core 母系统。
- 不是某个真实客户或真实项目的 Workspace。
- 不是 Template v1.0。
- 不连接真实 adapter。
- 不写入外部任务系统。

## 怎么使用

推荐方式：

1. 在 GitHub 上点击 **Use this template** 创建你的新 Workspace 仓库。
2. clone 你的新仓库到本地。
3. 先读 `WORKSPACE.md`。
4. 修改 `workspace-system-manifest.md`，填入你的 Workspace 名称、owner、用途、本地路径和远端仓库。
5. 运行检查：

```powershell
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
python scripts/utils/check_workspace_deployment.py
```

## 你需要改哪些地方

创建自己的 Workspace 后，通常先改：

- `WORKSPACE.md`：让入口说明符合你的 Workspace。
- `workspace-system-manifest.md`：记录真实身份、路径、远端、Core base。
- `projects/starter/plan.md`：写下你的第一个项目目标。
- `workspace-records/**`：以后记录升级、实现、决策、检查和反馈。

不要把客户资料、账号状态、原始图片、私有链接、token、cookie 放进这个模板结构里。

## 版本说明

`v0.1.0` 表示这是第一个公开可用模板基线。

它已经可以作为新 Workspace 的起点，但还不是稳定承诺版。Template 是否能到 `v1.0.0`，需要经过更多真实 Workspace 使用、反馈和修正。

## 与 WorkSeed Core 的关系

WorkSeed Core 负责沉淀通用能力。  
Workspace Template 负责把这些能力整理成别人可以直接创建的新 Workspace 起点。  
你的 Workspace 负责保存自己的真实项目事实、材料、决策和执行记录。
