<!-- theorem-state: {"artifact_id":"ART-6E00AE829AAF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# ChatGPT consolidation audit — 2026-08-30

## Scope

This pass compared the current repository against the complete v1.7 theorem stack and
the subsequent Target A work developed in continuation runs. The review covered the
repository maps, problem/literature baseline, shared theory and both target route maps,
the active Target A source-response module, the continuation prompt, audit/frontier
files, research harness map, and the primary/related literature organization.
Historical reports and the archived monolithic report were treated as provenance, not
parallel theorem sources, in accordance with repository policy.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

## What was already present

The repository already contained essentially all audited v1.7 and post-v1.7 Target A
mathematics known from the continuation record, including:

- strict-rattler product-germ/local-KKT no-go;
- fixed-basis and phase-selective contractions;
- planar strict-gammoid/Schur response and response-corrected collar;
- exact genuine-hull capacity slack and fixed-container endpoint matching;
- source-capacity plateau exchange flag and its exact source-Hall profile;
- same-cardinality source saturation and capacity-shadow coupling;
- finite-chord stress identity;
- tree-circuit sequentialization and planar cycle budget;
- straight-root-path criterion for codimension-one triangle walls;
- protected finite Kuperberg transfer and compatible multi-witness Hall bound;
- finite homothetic-strain concentration for accumulated strain bounded away from zero;
- one-point semicircle/cage and simultaneous locked-triangle alternatives;
- the exact two-leaf caged-circuit regression;
- retained-rattler first-transition incidence bounds;
- monotone activation, persistent source-to-contact transfer, activation-edge forest,
  and independence of its rigidity rows; and
- the newer Target B weighted/coherent-star and finite-lattice audit material.

The repo is therefore materially ahead of the frozen monolithic v1.7 snapshot. No
missing copy of the old theorem ledger needs to be reintroduced.

## Selected five proof obligations

The five claims singled out for re-audit have the following status.

1. **Same-hull add-one for \((1+\alpha/L)\)-homothetic triangular patches:** proved.
   The existing finite homothetic-strain theorem concentrates the accumulated strain
   into a fixed positive line gap and embeds one finite Kuperberg witness.
2. **First triangle can be perturbed unless a genuine cage remains:** proved, both in
   the one-point semicircle form and the stronger simultaneous fixed-container cone
   form.
3. **A first-transition cage necessarily gives a Schur separator:** not proved. The
   exact local cage regression shows why local locking alone is insufficient; the
   globally derived source-to-Schur transport remains missing.
4. **Two-leaf gadget:** proved exactly. The analytic one-parameter family in the
   source-response module supersedes the earlier numerical discovery.
5. **Vanishing-gap Kuperberg witness size:** newly strengthened in this audit. If
   \(\kappa_*(d)\) denotes the minimum number of deleted old centers in any
   positive-gain finite rearrangement of any width-\(d\) triangular gap packing, then
   \[
   \kappa_*(d)\to\infty\qquad(d\downarrow0).
   \]
   No explicit polynomial or other growth rate is established.

The proof of item 5 is promoted in the Target A audited addendum.

## Repository issues found

Three state-management issues were found.

### 1. Stale active prompt

The old v1.7.0 continuation prompt still presented a same-hull source witness with
Hall deficiency \(\widehat p_H+1\) (and the analogous \(\tau+1\) witness for the
extended source) as an open sufficient target. The exact fixed-container capacity
theorem proves that such witnesses inside the same hull are impossible by definition.
The active prompt is therefore replaced by a v1.7.1 audited prompt. The v1.7.0 prompt
is retained as a historical artifact.

### 2. Post-v1.7 additions lacked a clean route module

The append-only source-response file contains overlapping late section numbers from
parallel continuation merges. Rather than renumbering historical material, this pass
adds `04-post-v1.7-audited-addenda.md` for new reviewed results after Section 145 and
indexes it from the Target A route map.

### 3. Stale `docs/canonical/...` references

Two audit/report files referred to `docs/canonical/erdos_problem_99_1.7.0.md`, but the
reorganized repository had no `docs/canonical/` path. A compatibility pointer was
added. It explicitly redirects to the modular theorem map and does not create a
parallel theorem source.

## Current exact Target A frontier

The direct required theorem is unchanged:

\[
\boxed{\dim\ker S\ge\Delta_\Lambda-d_{\rm int}},
\]

or equivalently

\[
\boxed{\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.}
\]

Same-hull Hall bookkeeping is exhausted exactly and cannot supply an extra integer.
The most concrete remaining routes are:

1. transport a globally derived locked first-transition triangle/family into
   independent Schur nonlinkages;
2. upgrade free homothetic strain concentration to an exterior-compatible source or
   scaffold rearrangement with a strict diameter certificate;
3. transport the capacity-shadow finite chord through plateau terminalization; or
4. prove that the independent activation-edge rank forces compensating dependence in
   the boundary response.

No result in this audit is a Level I proof or a certified infinite counterexample.
