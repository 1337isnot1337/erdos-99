> Generated reading edition · [exact source](../../../docs/reports/target_c_phase_component_endpoint_closure_2026-09-12.md) · source SHA-256 `7b9c963a0f95fb8814acde3c80adb865cdd55f8b404535e39f1aa7bbc7af73d2`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-BF29CCD5C701","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C phase-component endpoint closure

**Date:** 2026-09-12  
**Repository commit:** `57c08a6` at run start  
**State version:** `2026-09-12.audit.44`  
**Run type:** closing proof  
**Target:** C-II  
**Starting status:** canonical §§101--104, with proof-only Sections 116--118 used
explicitly as conditional research dependencies  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** not used  
**Computation:** `[research/verify_target_c_phase_component_endpoint_closure.py](../research/migration/2026-10-16/shards/04/evidence/research/verify_target_c_phase_component_endpoint_closure.py)`

## LEVEL I STATUS

`STILL OPEN`

This report does not promote theorem state and does not claim C-II closure. It proves
that a substantial structural subbranch of the full-core near-endpoint regime is
already impossible, and isolates the exact multi-grain premise still missing.

## 1. Starting canonical endpoint

The current canonical endpoint is the Section-104 quantitative phase/corridor gap.
The post-104 proof-only chain gives, through the safe Section-118 window,

```math
 \sigma\le 0.0088,
 \qquad
 \frac{A_4}{D^2}\ge A_*(\sigma)-o(1),
 \qquad
 \frac{T}{D}\le C_T(\sigma)+o(1),
```

where `A_4` is the number-weighted area of the strict rhombus faces in one wrapping
carrier and `T` is its number of complete local train segments. The same chain gives
three principal complement-gap routes, with total normalized route length bounded by

```math
 M(\theta)+\frac{16}{3}\sigma+o(1),
 \qquad
 M(\theta):=\sin(\theta/2)+2\sin\theta.
```

For one fixed limiting train-direction interval, the corrected Section-118
directional leakage bound is

```math
 B_*(\sigma)=\frac{35}{3}\sigma+\kappa_0,
 \qquad
 \kappa_0=0.0136038132609408\ldots,
```

once `\sigma\ge y_0=0.0012822850180674...`. This is the number of bad trains per
unit source diameter in that interval, not the number of endpoint occurrences.

The desired bridge is:

```text
phase-collapsed train components covering the carrier
  -> endpoint count on the same physical carrier
  -> contradiction with the three principal routes and Section-118 leakage.
```

## 2. Strongest genuinely new result

**Classification:** conditional, with a complete proof of the conditional theorem.

### Theorem PC — phase-component endpoint inequality

Consider a full-core Type-II wrapping carrier along a subsequence in the proof-only
Section-118 window `0<\sigma\le0.0088`. Assume its complete local train segments are
partitioned into `k` phase components. In component `j`, assume that every train
direction belongs to one of at most `r_j` projective direction windows whose widths
tend to zero, and that the Section-118 bad-train capacity applies to each such
window. Put

```math
 R_D=\text{number of strict-rhombus faces},
 \qquad
 \frac{R_D}{D^2}\ge r-o(1).
```

Assume also that all strict-rhombus crossing pairs belong to the listed phase
components. Then

```math
\boxed{
 4\sqrt r
 \le
 M(\theta)+\frac{16}{3}\sigma
   +2B_*(\sigma)\sum_{j=1}^k r_j .
}
\tag{PC.1}
```

The conclusion uses all source points in the carrier boundary accounting. It does not
delete contact-isolated source points, and it does not extend the ZR/ZF affine-kernel
theorem beyond the nonisolated positive-contact core.

In particular, at the safe Section-118 endpoint, the scalar certificate gives

```math
\begin{aligned}
 r&=0.4703752868004241\ldots,\\
 \theta&=2.7047792352154936\ldots,\\
 M(\theta)&=1.8223523984668937\ldots,\\
 B_*(\sigma)&=0.1162704799276074\ldots,
\end{aligned}
```

and hence

```math
4\sqrt r-
M(\theta)-\frac{16}{3}\sigma
-2B_*(\sigma)\sum_jr_j
\ge
0.8740707140169731\ldots
-0.2325409598552148\ldots\sum_jr_j.
\tag{PC.2}
```

Therefore the full-core carrier is impossible whenever

```math
\boxed{\sum_jr_j\le3.}
\tag{PC.3}
```

The strongest immediate case is one phase-collapsed train component: it may use all
three labels, so `\sum_jr_j\le3` holds. Thus:

> A wrapping carrier in the safe Section-118 window whose entire train-crossing
> complex is phase-collapsed into one component is impossible, even if all three
> phase labels occur.

The same endpoint calculation also rules out two components using at most one label
window each, but does not rule out two two-label components or the general
multi-grain situation.

### Proof

Write `T_D` for the total number of complete local train segments. The train-crossing
graph is a simple triangle-free graph: each vertex is a train segment, each edge is a
strict-rhombus crossing, and three pairwise crossing trains are forbidden by the
projective-angle theorem. Mantel's inequality therefore gives

```math
 R_D\le \frac{T_D^2}{4},
 \qquad
 T_D\ge2\sqrt{R_D}.
\tag{PC.4}
```

Every complete train has exactly two distinct physical terminal edge occurrences,
including terminals on hole boundaries. Hence the carrier has exactly `2T_D` train
endpoint occurrences.

Let `W_1,W_2,W_3` be the three principal complement-gap route pieces. The exact
Section-104 gap bookkeeping gives

```math
 \sum_{i=1}^3\frac{|W_i|}{D}
 \le
 M(\theta)+\frac{16}{3}\sigma+o(1).
\tag{PC.5}
```

Here the `13\sigma/6` term bounds the perturbation of the three chord lengths from
`M(\theta)`, and the `19\sigma/6` term bounds their total route excess. This is only
an upper bound on the number of physical terminal occurrences which happen to lie on
the principal routes, so it remains valid even when some principal route edges are
not train terminals or have the wrong orientation.

Consider one phase window in component `j`. A train in this window with an endpoint
off the principal routes is a bad train in the sense of Section 117/118. The
proof-only Section-118 leakage theorem bounds its count by

```math
 B_*(\sigma)D+o(D).
\tag{PC.6}
```

Each such train has at most two off-principal endpoint occurrences. Consequently all
off-principal endpoints belonging to the `r_j` windows of component `j` number at
most

```math
 2r_jB_*(\sigma)D+o(D).
\tag{PC.7}
```

The windows are assumed to be assigned to the components without double counting a
train. Summing (PC.7) over components and adding (PC.5) gives

```math
 2T_D
 \le
 \left(M(\theta)+\frac{16}{3}\sigma\right)D
 +2B_*(\sigma)D\sum_jr_j+o(D).
\tag{PC.8}
```

Combining (PC.4) and (PC.8), dividing by `D`, and passing to the limit proves (PC.1).
The endpoint arithmetic in (PC.2)--(PC.3) is independently reproduced by the
companion script. `square`

## 3. Exact frontier effect

This is a structural reduction, not a canonical state mutation.

It eliminates the following conditional full-core branch:

```text
safe Section-118 near-endpoint carrier
+ all carrier train segments in at most three inverse-diameter phase windows
  (in particular, one connected phase-collapsed train component)
-> contradiction.
```

The proof uses the exact same carrier for rhombus count, train endpoints, and principal
routes. It does not infer an Euler trail, a global KKT weight floor, or a strict
sub-`D` competitor.

The new remaining structural target is now precise:

```math
\boxed{
\text{show that the total number of genuinely distinct phase windows carrying all
carrier trains is at most three,}
}
```

or weaken it to a weighted endpoint-capacity inequality that replaces the coarse term
`2B_*\sum_jr_j`. The existing canonical phase-cut and coherent-grain theorems only
give an `O(D)` interface and permit more than three macroscopic phase windows, so this
is exactly where the proof stops.

## 4. Exact remaining lemma

The next theorem-level obligation is:

> **Three-window globalization lemma.** In the full-core Type-II branch, after deleting
> only `o(D^2)` strict-rhombus faces, all remaining train segments of the unique
> wrapping carrier can be assigned to at most three inverse-diameter direction
> windows, with the Section-118 leakage bound charged once per window.

If proved, Theorem PC would contradict the safe Section-118 endpoint and eliminate the
entire full-core branch in that window. A weaker valid substitute is a source-level
upper bound on off-principal terminal occurrences below
`(4\sqrt r-M(\theta)-16\sigma/3)D`.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Mantel lower bound `T\ge2\sqrt{R_D}` | canonical input | Theorem 10.6 / `docs/theory/01-local-structure.md` | triangle-free train-crossing graph |
| Principal route-length upper bound (PC.5) | audited-working input | canonical §§100--104 plus proof-only §§113--118 | same-carrier gap and route slack bookkeeping |
| Per-window bad-train bound (PC.6) | audited-working input | proof-only Section 118 sharp companion and hostile review | valid at `\sigma\le0.0088`, not canonical |
| Phase-component endpoint inequality (PC.1) | conditional candidate | PC.4--PC.8 | complete once its phase-window premise is supplied |
| One-component closure | conditional consequence | PC.1 + safe Section-118 scalar endpoint | phase-window premise is not canonical |
| Three-window globalization lemma | unresolved | canonical phase-cut/coherent-grain stack | multi-grain interfaces may be `O(D)` |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Section-118 contact-isolated-source correction | pass | The argument uses only train endpoints of the nonisolated carrier and never extends the affine-kernel theorem. |
| Hole/bridge endpoint occurrence accounting | pass | Every train has two physical terminal occurrences; principal-route count is only an upper bound. |
| Section-120 uniform chord sampling barrier | pass | This proof does not use uniform averaging; it uses the endpoint count and the route upper currency. |
| Multiple phase windows | unresolved by design | The factor `\sum_jr_j` records the exact cost of not having a three-window globalization theorem. |

## 7. Literature imports

None. The only graph inequality used is Mantel's elementary theorem, already part of
the canonical train-structure input.

## 8. Computation

`python3 docs/research/migration/2026-10-16/shards/04/evidence/research/verify_target_c_phase_component_endpoint_closure.py` evaluates the
safe Section-118 endpoint constants and checks the strict margin in (PC.2) for
`\sum_jr_j\le3`. It uses binary64 arithmetic for displayed diagnostics only; the
theorem's algebra is symbolic and the margin is far larger than the displayed
roundoff. The script does not certify a global minimizer, the phase-window premise, or
C-II closure.

## 9. Corrections / supersessions

No prior theorem is corrected or superseded. The report deliberately does not combine
the one-component premise with the canonical phase cut; such a combination would be an
unproved multi-grain assertion.

## 10. Promotion recommendation

**conditional** — preserve as a proof-only research artifact. The mathematical
inequality is complete, but the phase-component premise is the missing global bridge.
No theorem-state files are changed.

## 11. Handoff

1. Strongest new theorem: (PC.1), with a strict endpoint contradiction for total phase-
   window count at most three.
2. Canonical dependency chain: `C-HARMONIC-CARRIER-QUAD` / §82 -> `C-HARMONIC-TRAIN-BUDGET`
   / §89 -> `C-PUNCTURED-PHASE` / §68 -> `C-WRAP-QUANT-PHASE-GAP` / §104, with
   audited-working Sections 116--118 supplying the safe scalar endpoint and leakage
   bound.
3. Exact remaining lemma: the three-window globalization lemma above.
4. Binding dead routes: no Euler-path inference, no full-source ZR/ZF extension, no
   deletion of contact-isolated points, no uniform chord-sampling shortcut.
5. Read next: Section 69 coherent-grain interfaces, Section 84 collapsed inactive
   corridors, Section 120 anisotropic two-arc regression, then attack the
   three-window globalization lemma or the inactive-container branch.
