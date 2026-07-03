# Capability Loads

This folder records Core capability runtime files installed into this Workspace.

Use it when `.codex/agents/**`, `.agents/skills/**`, supporting Core docs, or
supporting templates are loaded from:

- a local Core repo,
- an extracted Core package folder,
- a zip package sent by the Core owner.

Do not claim project agents or skills are available until the files exist and
local checks pass.

Use:

```powershell
python scripts/utils/install_core_capabilities.py --source-path "<core-folder>" --core-version ws-core-v0.3.0
```

or:

```powershell
python scripts/utils/install_core_capabilities.py --zip-path "<core-package.zip>" --core-version ws-core-v0.3.0
```
