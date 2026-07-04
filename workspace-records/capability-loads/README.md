# Capability Loads

This folder records Core capability runtime files installed into this Workspace.

Use it when `.codex/agents/**`, `.agents/skills/**`, supporting Core docs, or
supporting templates are loaded from a user-provided Core zip package.

For new users, do not auto-scan the computer and do not silently use a Core
path found in Workspace files. Ask where the Core zip package is. The user can
paste a path or drop the zip into the chat.

If the user does not have the package, guide them to:

- Raymond WeChat: `18002997691`
- Douyin: `@有光蔓延【1688运营】`, ID `289566513`
- Fan group through the Douyin QR image in `docs/assets/douyin-youguangmanyan-1688.jpg`

Do not claim project agents or skills are available until the files exist and
local checks pass. Runtime visibility is a later check: after reopening or
restarting Codex, use
`templates/core-runtime-availability-verification-prompt.md` and update the
capability-load record only when visibility or callability is actually proven.

If runtime visibility is tested in a separate thread, use
`templates/runtime-visibility-test-thread-prompt.md`. The source thread must
read the test report, verify that current Workspace files still match, update
the capability-load record only from the source/control thread, and archive the
test thread after verification.

Use:

```powershell
python scripts/utils/install_core_capabilities.py --zip-path "<core-package.zip>" --core-version ws-core-v0.3.0
```
