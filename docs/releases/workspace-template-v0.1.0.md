# WorkSeed Workspace Template v0.1.0

Status: Released

Date: 2026-07-03

Base Core release: `ws-core-v0.3.0`

Base Core commit: `a5b8b7355e02ef26e51d6af53b2bec28a14d08cb`

Repository: `https://github.com/raymondhyg/workseed-workspace-template`

## Purpose

This release publishes the first usable WorkSeed Workspace Template baseline.
It is intended for creating new Workspace repositories from a clean receiver
profile.

## Included

- `WORKSPACE.md`
- `workspace-system-manifest.md`
- `workspace-records/**`
- `docs/workspaces/**`
- `docs/releases/ws-core-v0.3.0-complete-beta-release.md`
- local verification scripts under `scripts/utils/**`
- Workspace feedback interface under `workspace-records/feedback/**`
- minimal starter project skeleton under `projects/starter/**`

## Boundaries

- No customer facts.
- No raw assets.
- No credentials.
- No private links.
- No real adapter configuration.
- No external task-system contents.
- No product-grade or source-equivalent claim.

## Verification

Run before publishing:

```powershell
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
python scripts/utils/check_workspace_deployment.py
```

## Decision

`workspace-template-v0.1.0` is an early public template baseline. It is useful
for new Workspace creation, but it is not Template v1.0.
