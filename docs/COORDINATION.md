# Open coordination

Anyone may begin an unclaimed bounded task. Claims are advisory and expire in at most seven days; independent audits may overlap. Check current Issues, Discussions and PRs and compare actual hypotheses/files. The selector queries all available surfaces read-only; query failure and disabled Discussions are explicit, never evidence of no overlap.

Use `python scripts/choose_research_task.py --live-overlap --json` and `--task TASK-ID --claim-template`. Post a scoped issue only after replacing placeholders. Include task ID, method scope, expiry, upstream SHA, state/priority revisions, exact question, dependencies, planned evidence, falsification and stopping point. Add UPDATE, FINDING, HANDOFF or RELEASED to the same thread. Release/close the claim after completing or stopping.

Research belongs in a focused PR with proof/code/inputs, commands, limitations and attribution. A handoff without a PR is valid when no durable result is ready. No issue, claim, merge or Discussion changes canonical status. Returning agents refresh upstream and priorities before another session. Existing private-source proposal references are translated into public snapshot records; they are not live public claims.
