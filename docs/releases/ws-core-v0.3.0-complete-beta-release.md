# WorkSeed Core Release Note

Release version: ws-core-v0.3.0

Status: Released

Publication state: Released

Date: 2026-07-03

Core commit: `a5b8b7355e02ef26e51d6af53b2bec28a14d08cb`

Core remote: `parent/codex/workseed-capability-upgrade-guide`

Source draft:
`docs/releases/ws-core-v0.3.0-complete-beta-draft.md`

Release gate record:
`docs/release-gate-preparation/ws-core-v0.3.0-final-release-gate-2026-07-03.md`

Git tag: `ws-core-v0.3.0`

GitHub release URL: `https://github.com/raymondhyg/workseed-core/releases/tag/ws-core-v0.3.0`

Release type:
- MINOR

Workspace adoption state: Blocked

## Purpose

This record publishes WorkSeed Core `ws-core-v0.3.0` as the Complete Beta
capability release.

The release packages the Core framework, operating spine, execution truth,
ecommerce substrate, required Prism/Mark/mira identity layer, strong Workspace
profile, source-signal path, milestone ledger, and Workspace feedback/patch
loop into one versioned Core baseline.

This is a Core publication. It does not run Workspace Lab, does not modify a
real Workspace, does not connect a real adapter, and does not create or update
external tasks.

## Release Evidence Chain

| Evidence | Status |
|---|---|
| Complete Beta target | `docs/core/v0.3/core-v0.3-target.md` |
| Completion proof | `docs/core/v0.3/core-v0.3-execution-completion-proof-2026-07-03.md` |
| Capability replication report | `docs/core/v0.3/core-v0.3-capability-replication-detail-report-2026-07-03.md` |
| Capability comparison HTML | `docs/core/v0.3/core-v0.3-capability-replication-comparison-2026-07-03.html` |
| Release preparation readiness | `docs/release-gate-preparation/ws-core-v0.3.0-release-preparation-readiness-2026-07-03.md` |
| Final release gate | `docs/release-gate-preparation/ws-core-v0.3.0-final-release-gate-2026-07-03.md` |
| Stable release note | This file |
| Publication checker | `scripts/utils/check_release_publication_v0_3_0.py` |
| Git tag | `ws-core-v0.3.0` |
| GitHub Release | `https://github.com/raymondhyg/workseed-core/releases/tag/ws-core-v0.3.0` |
| Workspace adoption | Blocked until later target evidence exists |

## User-Facing Changes

- Promotes the v0.3 Complete Beta capability construction lane from draft and
  release-preparation state into a stable Core release.
- Makes Prism, Mark, and mira required named capability identities for the
  Core v0.3 baseline.
- Preserves Mark -> mira -> Prism handoff as a required behavior shape when
  those capabilities are used.
- Upgrades the default Workspace receive target from a minimal skeleton to a
  strong Workspace profile.
- Publishes operating spine, execution truth, source signal, milestone ledger,
  proof/detail planning, ecommerce business operation, and feedback/patch loop
  surfaces as Core-owned release content.

Changed file classes:

| File class | Release handling |
|---|---|
| Core docs and standards | Included as release content and governance evidence |
| Capability nodes and validations | Included as capability construction evidence |
| Required named capability agents and skills | Included as required identity and behavior surfaces |
| Capability packs and templates | Included as reusable structured surfaces |
| Workspace adoption package drafts | Included as future receive guidance only |
| Lab learning and assessment drafts | Included as future Lab inputs only |
| Checkers | Included as mechanical verification surfaces |
| Workspace-local surfaces | Not included; real Workspace context remains protected |

Inheritable capabilities:

- Versioned Core capability evolution and release/adoption truth.
- Workflow/session operating spine, closeout, handoff, and recovery standards.
- Execution evidence gate and true external-write status vocabulary.
- Prism writeback operating loop and trust-state routing.
- Required Mark, mira, and Prism named capability identities.
- Mark/mira source-style replay boundary for strategy and image-production
  work without copying private source facts.
- Proof/detail planning and ecommerce business operation loops.
- Strong Workspace profile structure with manifest, records, and feedback
  path.
- Lightweight source-radar signal and milestone-ledger maintenance.

Upgrade impact:

- Core consumers may treat `ws-core-v0.3.0` as the Complete Beta Core baseline.
- A Workspace may evaluate this release for adoption only through the receiver
  standard, upgrade playbook, Lab/review path, target manifest, and target
  verification records.
- `ws-core-v0.3.x` is the compatible patch lane for small bugs, checker fixes,
  doc clarification, template field repair, and Workspace feedback fixes.
- `ws-core-v0.4.0` remains the later lane for full radar automation, concrete
  adapters, deeper proof/OCR/detail-page execution, and broader
  source-equivalence validation.

Migration steps:

1. Read this release note, the final release gate, and the v0.3 target.
2. Read the Workspace receiver standard, entry/record standard, upgrade
   playbook, feedback loop, and strong Workspace profile template.
3. Identify the target Workspace current Core base version from its manifest.
4. Build the multi-version chain from the current base to `ws-core-v0.3.0`.
5. Classify files as Core-following, review-required, Workspace-owned,
   local-only, or blocked.
6. Run Workspace Lab learning and assessment before any real rollout.
7. Record Core review as `Approved`, `Partial`, or `Blocked`.
8. Only then execute a target Workspace adoption plan with manifest and check
   evidence.

## Workspace Adoption Boundary

Real Workspace adoption is not performed by this release action.

Workspace adoption remains `Blocked` until a target Workspace has:

- target manifest evidence,
- Lab/Core review decision,
- protected-surface classification,
- implementation or merge records,
- local verification output,
- sanitized feedback path for reusable gaps.

## Required Named Capability Boundary

Prism, Mark, and mira are required capability identities in this Core release.

Required means Core must preserve their names, boundaries, handoff shape, and
decision gates. It does not mean every Workspace has live strategy output,
live image generation, or automatic writeback without Workspace-owned evidence
and tool authorization.

## Adapter Boundary

Concrete adapters remain `Adapter later`.

Core provides the adapter contract, status vocabulary, mock/read-only path, and
read-back evidence shape. A Workspace chooses and authorizes real external
tools later.

## Verification Commands

Verification commands:

```powershell
python scripts/utils/check_release_publication_v0_3_0.py
python scripts/utils/check_core_v0_3_workspace_migration_package.py
python scripts/utils/check_core_v0_3_execution_completion.py
python scripts/utils/check_core_v0_3_capability_replication_report.py
python scripts/utils/check_core_v0_3_capability_replication_html.py
python scripts/utils/check_core_v0_3_release_preparation_readiness.py
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
```

## Explicit Non-Claims

This release record does not claim:

- real Workspace rollout performed
- real Workspace repository modified
- Workspace-adopted
- Workspace-ready
- product-grade
- source-equivalent capability
- live proof/OCR/detail-page execution
- real adapter connected
- external task created or updated

## Privacy Boundary

Privacy boundary:

This release record contains sanitized release labels, file paths, status
vocabulary, checker names, and Core release conclusions only. It does not copy
customer materials, raw assets, private links, account state, credentials,
external task contents, real Workspace private records, or source-system
private data.

Workspace manifest update:

- Current Core base version: do not set a real Workspace to
  `ws-core-v0.3.0` from this Core publication action alone.
- Core commit: use the final release tag and target commit after read-back.
- Files that follow Core releases: classify in the target Workspace before
  copy or merge.
- Upgrade history row: not applicable until a real Workspace adoption action is
  separately authorized and verified.
- Workspace local decisions: protect Workspace-owned context and record any
  future copy, merge, skipped, or blocked decisions in the target Workspace.

GitHub communication:

- Core GitHub Release: published as `ws-core-v0.3.0`.
- Core to Workspace Lab: not pushed by this publication action.
- Core to real Workspace: not sent by this publication action.
- Workspace to Core: future feedback must be sanitized and recorded
  separately.

## Post-Publication Read-Back

- Local tag: `ws-core-v0.3.0`
- Tag object: `1c3437372c4540decad7a1e80524581ce41b8728`
- Tag target commit: `a5b8b7355e02ef26e51d6af53b2bec28a14d08cb`
- Remote tag: `ws-core-v0.3.0`
- GitHub Release: `ws-core-v0.3.0`
- Release URL: `https://github.com/raymondhyg/workseed-core/releases/tag/ws-core-v0.3.0`
- GitHub Release published at: `2026-07-03T12:28:20Z`
- GitHub Release draft state: `false`
- GitHub Release prerelease state: `false`
- Branch remote HEAD at tag creation: `a5b8b7355e02ef26e51d6af53b2bec28a14d08cb`
- Final verification: passed before publication
