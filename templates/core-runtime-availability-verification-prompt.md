# Core Runtime Availability Verification Prompt

Use this prompt after Core capability files have been installed and the
Workspace has been reopened, restarted, or opened in a fresh Codex thread.

If this verification is delegated to a separate test thread, use
`templates/runtime-visibility-test-thread-prompt.md`. The source thread must
read back the test report, confirm current Workspace state still matches, write
final records only from the source thread, and archive the test thread.

## Natural Triggers

If the user says any of the following after installing Core, guide them through
runtime verification:

- 帮我检查 Core 能不能用了
- 检查能力是否安装好了
- 检查运行时
- Core 安装完了，下一步呢
- 帮我看看 agent/skill 能不能用
- Prism / Mark / mira 能用了吗
- 给我验证一下
- 告诉我现在能不能开始工作

## Guided Prompt

```text
请帮我检查这个 Workspace 的 Core 能力是否真的可以用了，并一步一步指引我。

先确认当前 Codex 线程确实运行在这个 Workspace 根目录里。不要在 WorkSeed
Core、Workspace Template、projectless 线程或其他 Workspace 里代替验证。

先读取：
1. WORKSPACE.md
2. workspace-system-manifest.md
3. docs/workspaces/initialization-and-core-loading.md
4. workspace-records/capability-loads/README.md
5. 最新的 workspace-records/capability-loads/*-capability-load.md

然后检查当前 Workspace 文件中是否存在：
- .codex/agents/mark.toml
- .codex/agents/mira.toml
- .codex/agents/prism.toml
- .codex/agents/system-maintainer.toml
- .codex/agents/workflow-coach.toml
- .agents/skills/b2b-strategy/SKILL.md
- .agents/skills/background-memory/SKILL.md
- .agents/skills/ecommerce-domain/SKILL.md
- .agents/skills/image-production/SKILL.md
- .agents/skills/prism-writeback/SKILL.md
- .agents/skills/reference-learning/SKILL.md
- .agents/skills/workflow-coach/SKILL.md

再报告当前 Codex 运行时是否实际可见或可调用这些项目 agent/skill。

请用通俗的话分开报告三种状态：
1. 文件安装状态：installed / missing / partial
2. 本地检查状态：passed / failed / not run
3. Runtime availability：verified / not verified / requires reopen-restart

如果只是文件存在或本地检查 PASS，不要把它说成 Runtime availability verified。
不要把文件存在或本地检查 PASS 当成运行时可见。

只有在当前 Codex 运行时确实能看到或调用对应 project agents/skills 时，
才把最新 capability-load record 里的 Runtime availability 更新为 verified，
并写明证据。

如果当前运行时仍不可见，请保持 not verified 或 requires reopen-restart，
并说明我下一步应该怎么做。

同时检查 `workspace-system-manifest.md` 是否在已经存在 capability-load record
和已安装文件后仍写着 `Not installed by default`。如果是，请报告这是本地状态
回填缺口；确认安装文件和 load record 后，只能把 manifest 更新为
installed / runtime availability not verified，不能直接写 verified。

不要修改真实项目事实，不连接 adapter，不写外部任务系统，不声明 product-grade、
source-equivalent、real Workspace rollout 或 Core release/tag。

最后请给我一句最简单的结论：
- 可以开始使用 Core 能力；
- 需要重开/重启后再测；
- 或者还没装好，需要先安装。
```
