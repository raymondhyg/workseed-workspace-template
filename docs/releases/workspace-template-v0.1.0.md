# WorkSeed Workspace Template v0.1.0

## 中文发布摘要

发布版本：`workspace-template-v0.1.0`

发布类型：公开模板基线

主要变化：发布第一个公开可用的 WorkSeed Workspace Template 基线，让使用者
可以从干净的 Workspace 接收结构开始，而不是直接复制 WorkSeed Core 母系统。

采用边界：这是早期公开模板基线，不是 Template v1.0，不等于真实客户/项目
采用，也不等于源系统等价或产品级成熟承诺。

需要人工确认或后补的依赖：真实 Workspace 采用、真实适配器配置、外部
任务系统写入和项目私有事实都必须在目标 Workspace 内另行验证。

没有做：没有加入客户事实、原始素材、敏感接入信息、真实适配器配置或外部
任务系统内容。

验证结果：发布前需通过 `check_sync.py`、`verify_open_box.py` 和
`check_workspace_deployment.py`。

隐私边界：Template 只包含干净 starter、Workspace records、Core 接收标准、
模板和检查脚本；不包含客户私有事实、原始素材、敏感接入信息或账号状态。

## 技术变化

- 提供 `WORKSPACE.md`、`workspace-system-manifest.md` 和 `workspace-records/**` 作为新 Workspace 的基础结构。
- 带入 Core v0.3.0 接收标准、反馈结构、检查脚本和 starter 项目骨架。
- 将 Core 母系统和 Workspace 项目仓库分开，避免用户直接复制 Core 作为项目 Workspace。

## 受影响范围

- Template 可继承内容：公开 starter、Workspace 记录结构、Core 接收标准、检查脚本和反馈接口。
- 新 Workspace 需要补齐内容：真实 Workspace 名称、owner、用途、本地路径、远端仓库和项目计划。
- 不包含内容：客户事实、原始素材、敏感接入信息、真实适配器配置或外部任务系统内容。

## 使用或采用方式

1. 使用 GitHub 模板创建新仓库。
2. 克隆到本地并阅读 `WORKSPACE.md`。
3. 填写 `workspace-system-manifest.md`。
4. 运行 `check_sync.py`、`verify_open_box.py` 和 `check_workspace_deployment.py`。
5. 在自己的 Workspace 中开始项目计划和本地记录。

## 验证证据

- Git 标签：`workspace-template-v0.1.0`
- GitHub Release：已发布并读回。
- 发布前检查：同步检查、开箱验证和 Workspace deployment 检查。

## 明确没有做

- 没有声明 Template v1.0。
- 没有声明产品级成熟。
- 没有替任何真实 Workspace 完成采用。
- 没有连接适配器或写入外部任务系统。

## 隐私和边界

本发布只包含干净 starter、Workspace records、Core 接收标准、模板和检查脚本；
不包含客户私有事实、原始素材、敏感接入信息或账号状态。

状态：Released

日期：2026-07-03

基础 Core 版本：`ws-core-v0.3.0`

基础 Core commit：`a5b8b7355e02ef26e51d6af53b2bec28a14d08cb`

仓库：`https://github.com/raymondhyg/workseed-workspace-template`

## 用途

这是第一个公开可用的 WorkSeed Workspace Template 基线。

它用于创建新的 WorkSeed Workspace，让使用者可以从一个干净的接收结构开始，而不是直接复制 WorkSeed Core 母系统。

## 包含内容

- `README.md`
- `WORKSPACE.md`
- `workspace-system-manifest.md`
- `workspace-records/**`
- `docs/workspaces/**`
- `docs/releases/ws-core-v0.3.0-complete-beta-release.md`
- `scripts/utils/**`
- `workspace-records/feedback/**`
- `projects/starter/**`

## 边界

- 不包含客户事实。
- 不包含 raw assets。
- 不包含 credentials。
- 不包含 private links。
- 不包含真实 adapter 配置。
- 不包含外部任务系统内容。
- 不声称 product-grade。
- 不声称 source-equivalent。
- 不声称 Template v1.0。

## 验证

发布前需要通过：

```powershell
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
python scripts/utils/check_workspace_deployment.py
```

## 结论

`workspace-template-v0.1.0` 是早期公开模板基线。它适合创建新的 Workspace，也适合继续积累真实使用反馈；但它还不是 `v1.0.0` 稳定承诺。
