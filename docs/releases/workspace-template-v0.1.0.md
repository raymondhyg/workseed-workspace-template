# WorkSeed Workspace Template v0.1.0

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
