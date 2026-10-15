# Research report template

Reports are research/audit artifacts. They do not become canonical or audited merely by
being committed, merged, or placed under `docs/reports/`. A new report enters the
artifact registry as **unreviewed** unless the same change records an explicit completed
audit and stronger lifecycle classification.

Do not hand-write the generated first-line `<!-- theorem-state: ... -->` header. Run
`python3 tools/build_artifact_index.py --write --write-headers`; the manifest controls
the header and artifact index.

Read `../STATE.md` and `../RESEARCH_WORKFLOW.md` first.

---

# Erdős Problem #99 — [short run title]

**Date:** YYYY-MM-DD  
**Repository commit:** [sha]  
**State version:** [from `docs/state/theorem-state.yaml`]  
**Run type:** closing proof / audit / literature / computation / synthesis  
**Target:** A / B / C / Level I / shared  
**Starting status:** canonical frontier / unreviewed artifact / audited-working dependency / conditional branch  
**Active prompt:** [path or none]  
**External literature search:** not used / used  
**Computation:** not used / used [scripts]

## LEVEL I STATUS

`STILL OPEN` / `SOLVED` / `DISPROVED`

Do not change this status unless the global quantifiers in `docs/problem/statement.md`
are actually settled.

## 1. Starting canonical endpoint

State the exact route theorem/inequality that was open at the start.

```text
new lemma -> exact canonical quantity -> contradiction / Level I result
```

If the run depends on an audited-working result, name it here and say whether the new
conclusion is conditional on that result or whether this report audits it first.

## 2. Strongest genuinely new result

**Classification:** unreviewed candidate / audited-working / conditional / regression /
rejected attempt

### Statement

[Complete hypotheses and conclusion in canonical notation.]

### Scope

State explicitly whether this concerns global minimizers, arbitrary feasible packings,
a fixed container/hull, a shell/scaffold/response object, local perturbations, exact or
asymptotic conclusions, and whether contact-isolated source points are included.

### Proof

[Complete proof of the genuinely new statement.]

### Dependencies

For every nontrivial dependency give:

- repository theorem ID when one exists;
- repository path + theorem/section;
- its lifecycle status;
- literature theorem/source if external;
- computational certificate if logically required.

No unlisted report may be treated as canonical or audited-working by default.

## 3. Exact frontier effect

State what changes:

- branch eliminated;
- rank/nullity bound improved;
- exact constant improved;
- topology classified;
- missing hypothesis isolated;
- strict sub-`D` competitor constructed;
- or no canonical change yet.

If a numeric constant improves but the same high-level phase survives, say so plainly.

## 4. Exact remaining lemma

State one precise next theorem when possible. Do not write only “need a stronger
argument.”

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| [claim] | canonical / unreviewed / audited-working / conditional / regression / superseded / rejected | [theorem IDs + paths] | [decisive note] |

Include important claims from the run that failed.

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| [named regression] | pass/fail | [reason] |

For a new exact counterexample, include its complete data or a reproducible exact
certificate.

## 7. Literature imports

For each imported theorem give source, theorem number if available, exact hypotheses,
conclusion, normalization, and the precise bridge into the present argument.

Record near misses separately. Do not strengthen equality/uniqueness statements beyond
the source.

## 8. Computation

For every script used state:

- exact proposition tested;
- assumptions encoded/omitted;
- arithmetic type;
- command;
- certified output/margin;
- what the result does not prove.

If the script becomes load-bearing for a ledger entry, add it to that entry's
`certificates` list so CI executes it.

## 9. Corrections / supersessions

If this report corrects prior work, name the exact old claim and classify it as
superseded, conditional, or rejected. Trace any downstream result that actually used it.
Preserve unaffected conclusions.

## 10. Promotion recommendation

Choose one:

- **promote now** — proof and dependency/regression audit complete;
- **unreviewed** — preserve the research artifact but do not claim an audit;
- **audited-working** — completed audit, but do not admit as canonical yet;
- **conditional** — exact missing premise named;
- **regression/rejection only** — update state to prevent reuse;
- **provenance only**.

If promoting a frontier-changing theorem, list required same-change edits:

- increment `state_version` in `docs/state/theorem-state.yaml`;
- `docs/STATE.md`;
- affected route map/current-frontier file;
- active prompt if the mission changes;
- regenerated artifact index/headers and generated state views;
- theorem dependency edges and computational certificates when applicable.

## 11. Handoff

End with:

1. strongest new theorem;
2. exact canonical dependency chain by theorem ID;
3. exact remaining lemma;
4. binding dead routes/regressions;
5. files that must be read next.
