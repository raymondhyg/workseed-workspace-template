# Template Initialization And Core Loading Implementation

Date: 2026-07-03

Template version: `workspace-template-v0.1.0`

Default Core base: `ws-core-v0.3.0`

## Purpose

Prepare the Template for the full path from first greeting to usable Workspace
state.

This implementation does not install Core runtime capability files by default.
It adds the path for a Workspace to load them from a local Core repo, extracted
Core package folder, or zip package.

## Landed Surfaces

- `docs/workspaces/initialization-and-core-loading.md`
- `templates/first-workspace-initialization-prompt.md`
- `templates/core-capability-load-record-template.md`
- `scripts/utils/install_core_capabilities.py`
- `workspace-records/capability-loads/README.md`

## Behavior

- First greeting is routed through a Workspace initialization prompt.
- The Workspace must echo identity, Core base, Template version, private fact
  boundary, and runtime capability install state.
- Core runtime capability loading is version-aware and accepts local repo,
  package folder, or zip package input.
- Installed runtime files are recorded under `workspace-records/capability-loads/`.
- If project agents or skills do not appear after install, the Workspace should
  be restarted or reopened in Codex.

## Verification

| Command | Result |
|---|---|
| `python scripts/utils/check_workspace_deployment.py` | PASS |
| `python scripts/utils/check_sync.py` | PASS |
| `python scripts/utils/verify_open_box.py` | PASS |
| `python scripts/utils/install_core_capabilities.py --source-path "E:\Claude Code Projects\WorkSeed" --core-version ws-core-v0.3.0 --dry-run` | PASS |
| zip-package dry-run smoke | PASS |

## Boundary

This implementation does not claim Template v1.0, product-grade readiness,
source-equivalent capability, real adapter connection, external task-system
write, or private Core GitHub access.
