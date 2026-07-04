# WorkSeed Workspace Template v0.1.2

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
