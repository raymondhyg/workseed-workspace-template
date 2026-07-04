# WorkSeed Workspace Template v0.1.1

状态：Local candidate

日期：2026-07-04

基础 Core 版本：`ws-core-v0.3.0`

用途：Core capability loading / runtime verification hardening candidate.

## What Changed

- Added plain-language initialization guidance for new users.
- Added confirmation-gated Core runtime installation.
- Changed the beginner installation path to ask for a user-provided Core zip
  package instead of auto-scanning for a Core checkout or silently using a path
  found in Workspace files.
- Added package access guidance: Raymond WeChat `18002997691`, Douyin
  `@有光蔓延【1688运营】` / ID `289566513`, and the fan group QR image at
  `docs/assets/douyin-youguangmanyan-1688.jpg`.
- Added capability-load records with installed, missing, skipped, source
  identity, and runtime availability state.
- Added runtime availability verification prompt.
- Clarified that `Core-aware` is not `capability-ready`.
- Preserved the boundary that WorkSeed Core is the continuously iterating
  capability core, while each Workspace owns local facts and adoption truth.

## Lab Evidence

Saved Lab was reset from the latest Template candidate and installed the
repaired callable Prism Core runtime package:

`D:\Users\hanyo\Desktop\workseed-core-runtime-ws-core-v0.3.0-20260704-prism-callable.zip`

Fresh Lab runtime verification:

`codex://threads/019f2b51-55b0-7c50-af67-b622c443709d`

Result:

- agent roles visible: `prism`, `Mark`, `mira`, `system-maintainer`,
  `workflow-coach`,
- project skills visible: `b2b-strategy`, `background-memory`,
  `ecommerce-domain`, `image-production`, `prism-writeback`,
  `reference-learning`, `workflow-coach`,
- runtime availability: `runtime verified`,
- Prism/Mark/mira live business use: `Not evaluated`.

## Verification

Local candidate checks:

```powershell
python scripts/utils/check_workspace_deployment.py
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
```

## Boundaries

- No Template tag was created.
- No GitHub Release was created.
- No public release announcement was made.
- No real Workspace rollout was performed.
- No adapter was connected.
- No external task system was written.
- No private facts, raw assets, credentials, private links, or account state
  are included.
