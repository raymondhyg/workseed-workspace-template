# WorkSeed Workspace Template v0.1.0

This repository is a clean starting point for new WorkSeed Workspace
repositories.

Base Core release: `ws-core-v0.3.0`

Template version: `workspace-template-v0.1.0`

## What This Is

- A GitHub template repository for creating a new WorkSeed Workspace.
- A receiver profile with `WORKSPACE.md`, `workspace-system-manifest.md`,
  `workspace-records/**`, local checks, and feedback records.
- A safe baseline with no customer facts, raw assets, credentials, adapter
  state, or external task-system contents.

## What This Is Not

- It is not WorkSeed Core.
- It is not a real customer/project Workspace.
- It is not Template v1.0.
- It does not connect adapters or write external tasks.

## Start

1. Use this repository as a GitHub template, or clone it and rename it for your
   Workspace.
2. Read `WORKSPACE.md`.
3. Update `workspace-system-manifest.md` with your Workspace name, owner,
   purpose, path, and remote.
4. Run:

```powershell
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
python scripts/utils/check_workspace_deployment.py
```

## Version Policy

`v0.1.0` means this is the first usable public template baseline. It is early
and should evolve through real Workspace use before any `v1.0.0` claim.
