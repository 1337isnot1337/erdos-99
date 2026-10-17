> Generated reading edition · [exact source](../../../../docs/research/tracks/target-c-iterative-pruning-atomic-gap.md) · source SHA-256 `c002e2c9ce67f05b16bb433b42f7e62e1924da207df3bad6348f5e7898c3af4d`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C-II — iterative-pruning pair payment and matched atomic gap

## Current status

The strongest imported unpromoted matched train-measure bound on frozen source
main is the branch-aware gap `0.0071`, proved for the canonical full-core
Type-II train-measure branch. It gives

```text
(T - q/2)/D >= 2 sqrt(Delta_2) + 0.0071 - o(1)
T_R/D         >= 2 sqrt(Delta_2) + 0.0071 - o(1)
sigma_R/D     >= 0.0142 - o(1)
Delta_2 = pi/(2 sqrt(3))
```

The source report and hostile audit both say PASS at proof-only scope. The
destination claim remains **unreviewed**, and neither the destination theorem
state nor C-II/Level I status changes. The exact outward certificate has a
margin greater than `3.66e-4`; the destination replay commands are listed
below.

## Proof chain

1. [Split-budget pair payment](../../../research/target_c_split_budget_pair_payment_2026-09-14.md)
   corrects a double charge in the older chain-cover argument and gives
   `rho >= (a+b-K)_+^2/18`. Preserve it as a proof-history contribution; its
   coefficient is superseded by the later iterative-pruning estimate.
2. [Iterative-pruning conditional pair payment](../../../research/target_c_iterative_pruning_conditional_pair_payment_2026-09-14.md)
   deletes high residual-missing-degree trains across either shore. Each
   missing edge is charged at its first deleted endpoint, yielding
   `rho >= min{g_*^2/10, 2 m_*^2/29}`, where `g_*=(a+b-K)_+`,
   `m_*=min(a,b)`, and `K=2/sqrt(3)`. The `g_*^2/10` branch applies when
   `g_*/m_* <= sqrt(20/29)`.
3. [Matched minimax gap 0.0050](../../../research/target_c_iterative_minimax_phase_star_atomic_gap_0050_2026-09-14.md)
   uses the unconditional `2/29` relaxation and proves the corresponding
   all-train and strict-rhombus floors, plus a separate Section-171
   propagation. Its source hostile audit and exact minimax and propagation
   verifiers are retained. The matched gap is superseded by 0.0071 at the
   same train-measure and rhombic scope.
4. [Branch-aware gap 0.0071](../../../research/target_c_branch_aware_iterative_pruning_atomic_gap_0071_2026-09-15.md)
   retains the `1/10` branch where the leaf-to-excess ratio forces it and uses
   the `2/29` branch elsewhere. Its [source hostile audit](../../../research/target_c_branch_aware_iterative_pruning_atomic_gap_0071_hostile_audit_2026-09-15.md)
   checks the analytic argument at its stated proof-only scope.

The exact source-main identities and dispositions for these six reports/audits
and four verifiers are in the [migration ledger](../../../../docs/research/migration/2026-10-16/ledger/source-main-files.jsonl).
The [candidate registry](../../../../docs/targets/target-c/candidate-registry.json)
separates the pair theorem, the superseded matched gap, and the active stronger
candidate.

## Existing canonical geometric dependencies

The source research invokes the destination's canonical full-core Type-II
branch (`C-FULLCORE-NEAR-DISK`), phase law (`C-PUNCTURED-PHASE`), train and
interface accounting (`C-TRAIN-INTERFACE-CURRENCY`), pseudogrid extraction
(`C-PSEUDO-GRID`), and complete phase-pure source-hull projection
(`C-HOLE-GRID-DIAMETER`). Their controlling documents are linked from the
[theorem-state manifest](../../../../docs/state/theorem-state.yaml) and the
[Target C audit directory](../../targets/target-c/README.md). The imported
pair payment adds a separate missing-edge argument; it does not replace those
canonical inputs or establish that the required atom families occur in every
source.

## What has and has not propagated

The `0.0071` report itself does **not** recompute the downstream Section-171,
outer-energy, complement-rhombus-incidence, or low-`t` chains. The `0.0050`
source has a separate finite propagation certificate for

```text
(q-k)/D >= 4/9 (pi + sqrt(Delta_2)) + 0.0023374 - o(1).
```

That remains a distinct unpromoted consequence at its recorded `0.0050`
input; it must not be silently relabeled as a `0.0071` consequence. The next
useful contribution is to substitute the stronger matched bound into each
downstream chain, retain all branch hypotheses and exact endpoints, and rerun
or replace the corresponding verifiers. The source report explicitly
identifies the Section-171 and complement-rhombus chains as the next bridge.

## Scope and remaining endpoint

The proof uses exact train-phase atoms at projective separation `pi/3`, the
full-core Type-II train-measure hypotheses, the dominant three-phase orbit,
and the stated triangle-free two-leaf correlation. The rhombic bound is rerun
on the strict-rhombus train graph; it is not inferred by deleting singleton
trains from the all-train result. Contact isolates remain in the full source.

These are asymptotic proof-only lower bounds on train and rhombic measures.
They do not establish an exact unit triangle, a positive KKT diameter-weight
floor, a source-wide diameter decrease, a same-cardinality strict sub-`D`
competitor, C-II closure, or Level I closure. The full-source endpoint still
must preserve every label and every lower and upper pair constraint.

## Reproduction

```bash
python3 research/verify_target_c_iterative_minimax_atomic_gap_0050.py
python3 research/verify_target_c_g0050_global_propagation.py
python3 research/verify_target_c_branch_aware_atomic_gap_0071.py
python3 research/verify_target_c_branch_aware_atomic_gap_0071_pi_enclosure.py
python3 tools/task_context.py target-c-branch-aware-atomic-gap
```

The first two commands validate the `0.0050` certificate and its own Section-171
propagation. The last two validate the `0.0071` outward certificate and its
Machin enclosure. None independently proves the analytic arguments or promotes
the claims.
