> Generated reading edition · [exact source](../../../docs/reports/target_c_good_end_outerwalk_tradeoff_audit_2026-10-03.md) · source SHA-256 `6e1129fbc68330f2af9600c069bc707f6b1e7cbb27c0ac334cbaeced74e157e2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-79919906D127","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_good_end_outerwalk_tradeoff_audit_2026-10-03.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=208abfb0d31c6f35f2fe83562214bdd41f750245; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C — good-end audit closes the low-outer-walk collar branch

**Date:** 2026-10-03
**Base:** `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`
**Source branch/tip:** `research/full-settlement-collar-20261003` @ `bc52d9f5153c8c936fd3fbf96f755c8d57bbee86`
**Run:** canonical-input derivation, scope audit, and October branch composition.
**Classification:** unreviewed proof candidate under current-main Sections 61 and 63.
The source branch proposed `2026-10-03.audit.52`, but current main remains
`2026-09-14.audit.51`; this report is not canonical.
**Audit:** hostile self-audit only; no independent external review is represented.
**Level I / C-II:** STILL OPEN.

## 1. Novelty and precise theorem

The September 25 report
`target_c_outerwalk_surplus_mu_tradeoff_2026-09-25.md`, equations OW.4--OW.9,
already contains the algebraic precursor in its full-core surplus notation.
We do not claim a new endpoint-counting mechanism or a new `3pi/5` constant.
The audit below isolates its **finite all-C-II scope**, using only canonical
Sections 61 and 63, and composes it with the October high-t collar assumptions
to eliminate that entire branch, independently of the matching number.

A later all-refs overlap check also found commit `bc790e61` on another
research branch: `research/target_c_low_x_train_face_feasibility_2026-10-03.md`
already excludes this October branch using a stronger, unpromoted matched
all-train bound. This audit does not claim first discovery of that exclusion.
Its contribution is an explicit all-C-II proof and canonical dependency
registration using Sections 61 and 63 alone, with no numerical train-measure
premise. Neither precursor is used as a theorem premise below.

Let `A` be any canonical post-ZF contact-minimal, then diameter-pair-minimal
C-II source, retaining every source point. Define `q,h,d_H,s_Z,k,Q,f,b,x_B`
as in canonical Sections 61 and 63, and put `t_D=(q-k)/D`.
Then

$$
\boxed{5(q-k)+2\ge3q+x_B,}                                  \tag{GE.1}
$$

and

$$
\boxed{5(q-k)+2x_B+2\ge3\operatorname{per}(F).}               \tag{GE.2}
$$

These are finite statements. They require neither the full-core dichotomy,
near-disk convergence, the loaded-chord elimination, a matching bound, nor
an affine-kernel theorem on isolated coordinates.

Thus, for every C-II sequence with `D->infinity` and `per(F)/D->pi`,

$$
\liminf\left(5t_D+2x_B/D\right)\ge3\pi.                      \tag{GE.3}
$$

In particular **no such sequence** can satisfy both
`t_D<=93/50+o(1)` and `x_B=o(D)`. Every sequence with the first inequality
instead obeys

$$
\boxed{\liminf x_B/D\ge(3\pi-93/10)/2
=0.0623889803846898\ldots.}                                  \tag{GE.4}
$$

The same argument excludes any fixed upper bound `t_D<=t_0+o(1)` with
`t_0<3pi/5` when `x_B=o(D)`.

## 2. Complete proof and exact slacks

Canonical Section 61.7 gives the complete stopped-train count

$$
N=(b+Q)/2+2f=q-k+2f.
$$

Section 61.9 pays at most `2x_B` bad exterior endpoint occurrences.
Section 61.10 pays `4f+Q` bounded exceptional-face occurrences.
Section 61.12 proves at most two trains have two good loaded-hull ends.
Consequently its canonical equation 61.13 is

$$
N-2\le2x_B+4f+Q.
$$

Put `s_end=2x_B+4f+Q-(N-2)>=0`. Substituting
`b=q+x_B`, `Q=q-x_B-2k`, and `N=q-k+2f` yields the exact identity

$$
\boxed{5(q-k)+2-3q-x_B=s_{\rm end}+2(Q-f)\ge0.}              \tag{GE.5}
$$

This proves GE.1. Since `b=q+x_B>=per(F)`, another exact identity is

$$
\boxed{5(q-k)+2x_B+2-3\operatorname{per}(F)
=s_{\rm end}+2(Q-f)+3(b-\operatorname{per}(F))\ge0.}          \tag{GE.6}
$$

This proves GE.2 with every discarded term identified. Divide by `D` to get
GE.3. If `limsup t_D<=93/50`, rearrange GE.2 and use the actual perimeter
limit to obtain GE.4. Its positive margin follows already from
`pi>157/50`: `3pi-93/10>3/25`, hence the safe lower bound
`liminf x_B/D>=3/50`. Decimals are explanatory evaluations only.

Equivalently, at least `q-x_B` distinguished hull intervals are good
contacts; they contribute at least `q-x_B-2` distinct trains. This gives
`k<=2f+x_B+2`, the same inequality. We use the already-audited 61.13
and the exact slack identities rather than introducing any new train topology.

## 3. Same-source October composition

The October high-t fan/collar reports explicitly assume, in one and the
same source, `per(F)/D->pi`, `t_D<=1.860+o(1)`, and
`x_B=O(sqrt(D))`. Those assumptions alone contradict GE.2:

$$
9.3+o(1)\ge3\pi,
$$

which is false. No lower bound on `sum Q_r^+ +2d_tile` is needed for this
branch; its supposed positive allowance describes an infeasible source regime.

The excluded branch includes its proposed degree-two fan alternative,
degree-three fan/collar alternative, and stopped-collar endpoint network.
It is excluded for **every matching number**, not only `nu=O(sqrt(D))`.
There is no claim that `t_D<=1.860` holds canonically for every C-II source.
The conditional October reductions retain their existing lifecycle.

## 4. Dependency and regression audit

| Input or risk | Exact audit |
| --- | --- |
| Train number | Canonical `C-LINEAR-NONMATCH`, Section 61.2: all contacts, including singleton trains, are counted. |
| Two good ends | Canonical Section 61.5: hull side directions, alternating boundary endpoints, and the triangle-free crossing graph prove the bound two. |
| Bridges/repeated occurrences | Section 61.3 uses distinguished forward hull intervals; all remaining occurrences cost bad-end capacity. No vertex or edge occurrence is collapsed. |
| Exceptional-face degree | Every bounded nonquadrilateral contributes at least one; `Q-f>=0`. |
| Euler/rigidity ledger | Canonical `C-LOADED-HULL`: `Q=q-x_B-2k`. The same nonisolated-core convention is retained. |
| Metric detour | Each unit-edge exterior interval has length at least its hull chord, so `b>=per(F)`. |
| Contact isolates | Every source point stays present. No isolate population estimate, stress kernel extension, or motion is used. |
| Source co-embedding | All quantities are the actual canonical source's global contact outer walk and loaded hull. No harmonic-cell walk is substituted. |
| Old RSR/Eppstein/FB4 failures | No equality uniqueness, near-quadrangulation, or FB4 implication is used. |
| Global conclusion | GE.4 is an outer-walk requirement, not a strict competitor or exact triangle. |

The exact bounded verifier
`research/verify_target_c_fan_train_tradeoff_2026_10_03.py` additionally
checks this endpoint/ledger implication and its slack decomposition in every
nonnegative integer case of its stated bounded universe. The geometric
premises are canonical inputs, not claims proved by that finite computation.

## 5. Candidate frontier effect and current-main disposition

GE.1--GE.4 are proposed as an unreviewed consequence of current-main
`C-LINEAR-NONMATCH` and `C-LOADED-HULL` (Sections 61 and 63). This salvage
preserves the proof candidate and bounded checker only. It does not apply the
source branch's `audit.52` promotion transaction or change current theorem state.

The candidate near-disk obstruction is

$$
\boxed{t_D\ge3\pi/5-o(1)\quad\text{or}\quad
2x_B/D\ge3\pi-5t_D-o(1).}
$$

At `t_D<=1.860`, the second branch is compulsory. The highest-value next
lemma must turn this **actual linear global outer-walk excess** into a
strict same-cardinality sub-D source or exact triangle, while checking all
contact-isolated source points and all active diameters. The higher-t and
macroscopic-container branches remain open.
