# Maintainer intake: continue changed work

This is the entry point for authorized PR maintenance. The
[ledger](pr-ledger.json) records exact-head review scope and evidence; the
[scheduling cache](pr-intake-state.json) avoids repeating unchanged work.
Neither is a theorem authority or an automatic merge gate.

## Plan once, then inspect selected entries

```sh
python scripts/pr_intake.py plan --refresh --output /tmp/erdos99-intake.json
```

The planner verifies that origin is canonical (forks may select `--remote upstream`), fetches main without checking it
out, and reads open PR metadata once. It does not read PR bodies, run contribution
code, alter the ledger/cache, post, merge or close. Preserve local work. Read the
selected entries, exact heads and prior decisions before the full backlog.
The bounded default selects up to 100 actionable heads; unselected actionable
work remains counted. A fresh empty selection ends routine intake unless the
user requested monitoring.

New/changed heads, watched source/tree/mode changes, watched PR changes/departure,
a policy-version change or explicit `--wake NUMBER` trigger reconsideration.
Changed obligations reset scheduling readiness to pending review. Unrelated main
commits, queue size, time and compaction do not wake an unchanged hold. The
planner does not inspect comments; comment-only evidence or environment changes
may require `--wake`. A departed PR is not presumed merged or incorporated.

For diagnostics, `plan --live-json FILE --base-ref HEAD` accepts a repository-bound
snapshot with `pulls` records containing number, title and exact head. It is labelled
`offline-fixture` and never substitutes for fresh GitHub evidence.

## Record the exact reviewed head

Commit your actual review evidence first, then record its immutable identity:

```sh
python scripts/pr_intake.py record --number 123 --head FULL_REVIEWED_SHA \
  --status waiting_revision --lane archive --review-status partially_reviewed \
  --reason 'Exact unresolved objection and repair' \
  --coverage 'Exact source/integrity checks actually completed' \
  --remaining 'The scientific or execution obligation still open' \
  --evidence docs/research/REAL_REVIEW_RECEIPT.json \
  --watch-path research/RELEVANT_SOURCE.py --watch-pr 122
```

Replace examples with real paths and omit irrelevant watches. The command checks
the live head, requires committed unchanged evidence, appends its hash/commit to
the ledger, and updates scheduling state. Commit those two records. Evidence paths
are watched automatically; also watch relevant scientific and shared-code inputs.
Concurrent records across worktrees refuse a shared Git-directory lock; retry
only after the other writer finishes. If interrupted, inspect both documents and
the lock before manually clearing it. The ledger is written first; a partial
failure leaves extra actionable work rather than a false acceptance receipt.
Identical decisions do not append duplicate ledger entries.

| Scheduling status | Meaning |
| --- | --- |
| `ready_to_integrate` | Finish explicit acceptance, verification and publication gates. |
| `pending_review` | Substantive review is unfinished and remains actionable. |
| `waiting_revision` | A specific correctness/integrity repair is required; unchanged heads sleep. |
| `deferred_replay` | Execution is explicitly scheduled separately or resource-stopped; obligation remains open. |

A generic lack of review is pending work, not a revision request. Each receipt
states a review lane, coverage and remaining obligations. `scope_verified` applies
only to the recorded scope; it never means full theorem verification. Archive
receipts must remain `partially_reviewed`. Lane declarations are reviewer evidence,
not automated validation of source inventory or permission to merge.

## Reuse evidence and finish honestly

Group related mechanisms and review each unique delta once, retaining predecessor
credit. Carry unchanged exact-source evidence by reference. Do not regenerate
historical audit packets or run all-history suites after compaction. Expensive
runs need explicit scope, time/memory limits and a recorded environment. Preserve
resource stops as deferred execution, not mathematical failures. Poll an existing
hosted run by ID instead of restarting it after a transient observation failure.

The merging agent owns required full replay on the final integration candidate;
see [verification ownership](../ci/README.md#verification-ownership). A new
unresolved full-verification requirement cannot be relabelled archival to avoid
that gate. [Archive intake](research-archive-intake.md) is available only after
establishing isolated source scope and integrity. Mathematical proof promotion
still follows [review policy](../REVIEW_POLICY.md), separately from publication.

Recheck the live head before merge/closure and retain source/attribution links.
An unfinished partial submission remains open with its next action. A checkpoint
needs base, exact heads/decisions, live run IDs, remaining obligations and one next
command in the existing evidence/thread. Report new integrations, new holds,
actionable unfinished work and deferred replay separately. Queue counts are not
completed scientific reviews.
