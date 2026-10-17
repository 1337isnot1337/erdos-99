> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_finite_barrier_and_coembedding_regression_2026-10-01.md) · source SHA-256 `86eb1939092631678d210bd23d6d00e5bacabac938021b08b1a0eab94d856feb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8D6A5FC268A7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: finite exact-phase motion requires the actual source embedding

**Date:** 2026-10-01
**Starting commit:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`
**State version:** `2026-09-14.audit.51`
**Mission/branch:** finite gap-cut deformation, `swarm/root/c2-gap-cut-20261001`
**Classification:** proved candidate awaiting promotion for the local barrier;
regression for the proposed global abstract barrier. Generated lifecycle is unreviewed.
**Level I:** OPEN. C-I CLOSED. C-II OPEN.
**Literature:** no new imports.

```text
actual-source cut deformation -> all active diameter inequalities plus finite
inactive slack -> strict diameter competitor or lower lexicographic pair count.
```

The missing bridge is a finite deformation of the actual source. The regression
below does not provide that deformation. It rules out replacing that bridge by
rank, interval support, and circulation alone.

## 1. Dependencies and objects

Canonical premises used for the source specialization:

- `C-ZRF`, [Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md): mixed
  rigidity on the nonisolated positive-contact core, not isolated coordinates.
- Contact-minimal, then diameter-pair-minimal source normalization in
  [CURRENT](../targets/target-c/CURRENT.md). Every source point is retained.

Unpromoted inputs checked at their stated scope:

- [Complete-grid rank](target_c_complete_grid_rank_switching_2026-10-01.md):
  independent shear coordinates and rank `m` on the retained shore.
- [Gap connectivity](target_c_exact_phase_gap_graph_connectivity_2026-10-01.md):
  signed interval rows and their exact graphic representation.
- The circulation audit at Git commit
  `625a8f02d1bbeec3a0c94612788128ee3b8ba132`, report
  `docs/reports/target_c_exact_phase_gap_graph_circulation_2026-10-01.md`:
  strictly positive diameter weights give a signed circulation. The following
  proof rederives the virtual-work identity it uses; it imports no hub assertion.
- [Block transposition](target_c_open_cell_block_transposition_2026-10-01.md):
  the contact-cut property. Our local theorem explicitly assumes this property.

This report does not promote any dependency or claim. The broad canonical
full-core and macroscopic-container branches remain open.

## 2. Exact finite local isolation

Consider a finite source and `m` nested source subsets `S_i`. Put
`s_i(p)=1_{p in S_i}` and assume every original unit contact crosses at most one
selected cut. A contact crossing cut `i`, oriented from outside into `S_i`, has
unit vector `u`, the same vector for all selected cuts. Fix `J` as the positive
quarter turn.

For arbitrary angles `theta_i`, set

```math
 P_\theta(p)=P(p)+\sum_i s_i(p)
 [(\cos\theta_i-1)u+\sin\theta_i Ju].                 \tag{1}
```

Every original contact stays exactly unit: its relative vector is either
unchanged or replaced by the corresponding rotated unit vector. This formula
is an explicit finite integration, including contacts outside the retained grid.
It requires actual full-source cutsets; local rhombus directions do not imply it.

For an original diameter `h=xy`, put `r_h=P(y)-P(x)` and
`epsilon_hi=s_i(y)-s_i(x)`. Define

```math
 M_{hi}=\epsilon_{hi}(r_h\cdot Ju).
```

Assume `rank M=m` and a strictly positive vector `beta` with `beta^T M=0`.
Both are source specialization hypotheses, not assertions about an arbitrary
shell. Positive KKT virtual work supplies the latter when all old contacts have
zero first variation in the selected coordinates.

**Theorem 1.** Define

```math
 \kappa=\min_{\|z\|_\infty=1}\max_h(M_hz),
 \qquad B=Dm+m^2.
```

Then `kappa>0`. If all old diameter lengths in (1) stay at most `D`, either
`theta=0` or

```math
 \|\theta\|_\infty\ge {2\kappa\over B}.             \tag{2}
```

Thus every nontrivial contact-preserving move in these coordinates that does
not lengthen an old diameter crosses a positive finite angle barrier. This is
stronger than the absence of a first-order strict descent, but the barrier is
source-dependent and need not stay bounded below as `D` grows.

**Proof.** If `Mz<=0`, pairing with `beta>0` makes every component zero, so
full column rank gives `z=0`. Consequently `max_h M_hz>0` for every nonzero
`z`. Continuity and compactness of the unit infinity sphere give `kappa>0`.

Put `t=||theta||_infinity` and

```math
 q_h=\sum_i\epsilon_{hi}
 [(\cos\theta_i-1)u+\sin\theta_i Ju].
```

The unit-circle Taylor remainder has norm at most `theta_i^2/2`, for every
real `theta_i`; this follows by twice integrating the unit-norm second
derivative. Also `|R_theta u-u|<=|theta|`. Hence

```math
 |q_h-Ju\sum_i\epsilon_{hi}\theta_i|\le mt^2/2,
 \qquad |q_h|\le mt.
```

Therefore

```math
 |r_h+q_h|^2-D^2
 \ge 2M_h\theta-(Dm+m^2)t^2.
```

Choose a row attaining `max_h M_h theta>=kappa t`. If all old diameters
remain at most `D`, `0>=2kappa t-Bt^2`. For `t>0` this gives (2).
No inactive constraint was made active, no uniform slack was assumed, and
no isolated source point was removed. QED.

For a computable conservative bound, put `b_min=min beta_h`,
`b_sum=sum beta_h`, and let `sigma` be the smallest Euclidean singular value
of `M`. With `N` rows,

```math
 \kappa\ge {b_{\min}\sigma\over b_{\rm sum}\sqrt N}.
                                                               \tag{3}
```

Indeed some row of `Mz` has absolute value at least `sigma/sqrt(N)` when
`||z||_infinity=1`. A positive such row directly bounds the maximum; a
negative row forces positive weighted mass at least `b_min` times that
absolute value, hence a positive row of at least that mass divided by `b_sum`.

**Leaf consequence.** A leaf of a chosen spanning-tree basis cannot supply
a sufficiently small contact-preserving release in these exact-phase
coordinates. Every nonzero first direction has a lengthening diameter row
in the full system. This agrees with the circulation audit: a private basis
leaf is not a private full-system diameter. It does not rule out a finite
competitor outside the neighborhood (2).

## 3. A global extension is false in the abstract interval model

The following assertion is **rejected**:

> Full rank, positive transverse KKT circulation, a common interval hub,
> opposite-sign axial-reaction bundles, and unique diameter directions
> prevent every finite contact-bar substitution inside the original empty
> diameter-direction cell.

Take `m=3`, `u=(1,0)`, `D=13`. For each of the following support intervals,
use two diameter vectors with the indicated two transverse signs, each of
weight `1/6`:

| Support | Diameter vectors |
| --- | --- |
| `[1,2]` | `13(4/5, +/-3/5)` |
| `[2,3]` | `13(3/5, +/-4/5)` |
| `[1,3]` | `13(12/13, +/-5/13)` |

All vectors have length `D`, and their six projective directions are
distinct. The nearest directions to `u` have slopes `+/-5/12`.
The derivative rows have full rank three, since the three interval
indicators have determinant one in absolute value. The two rows of each
support cancel in transverse KKT virtual work. The full directed gap
multigraph is the tree `2--0--3--1` with both orientations of every edge,
so it is strongly connected and bridgeless as a multigraph. Every interval
contains train index 2.

The resulting axial cut totals are

```math
 (A_1,A_2,A_3)=(112/15,151/15,33/5).
```

Thus `A_1-A_2=-13/5` and `A_2-A_3=52/15` are nonzero. At each internal
interface the switching packet consists of the two bars of one support,
with opposite transverse signs and a nonzero axial sum in its inward
orientation (negative at gap 1, positive at gap 2). These
are exact abstract reaction identities, not full-source vertex equilibrium.

Now take `tan(theta/2)=3/20`, so

```math
 c=391/409,\qquad s=120/409,
 \qquad (u'_1,u'_2,u'_3)=((c,s),(c,-s),(c,s)).
```

Every new unit-bar phase stays inside the original empty cell, because
`s/c=120/391<5/12`. Under the exact interval substitution

```math
 r'_h=r_h+\sum_{i\in[a_h,b_h]}(u'_i-u),              \tag{4}
```

the interval changes are `(-36/409,0)` for the two length-two supports
and `(-54/409,120/409)` for the length-three support. Every one of the
six old diameter lengths strictly decreases. The largest squared change
for the full support is

```math
 -{96\over409}+{17316\over167281}
 =-{21948\over167281}<0.                           \tag{5}
```

The exact verifier checks the remaining five inequalities individually.
The regression does not contradict Theorem 1: it makes a finite jump,
and the intermediate small counter-rotations violate diameter constraints.

## 4. Separate thrackle geometry is also insufficient

The twelve points `+/-r_h/2` realize the **old** six diameter vectors as
an actual convex circular matching. Every pair is separated by more than
one; the only diameter pairs are the six antipodal pairs. The diameters
all cross at the circle center. Thus unique directions and even a separate
exact diameter-thrackle realization do not repair the abstract implication.

This circular matching has no unit contacts. It is not the source of (4),
has no actual O--O train cutsets, has no full-source positive contact
stress, and is not a global-minimizer counterexample. In particular, one
must not assign its twelve endpoints the abstract gap labels and silently
claim a source realization. The report makes no such assignment.

The repaired obligation must retain the source co-embedding: cut membership
of the **actual** endpoints, their hull order, actual contact geometry,
and all unchanged/inactive source pairs. A diameter vector list plus a
separate thrackle realization omits precisely this information.

## 5. Certificate and next attack

Run `python3 research/verify_exact_phase_gap_finite_barrier.py`.
Arithmetic is rational throughout. A positive output certifies the finite
abstract regression and the independent circular matching. It proves no
global optimality, no canonical source existence, and no general barrier
beyond the analytic Theorem 1.

The next attack is an actual-source cut contraction: find simultaneously
compatible unit-contact cut motions for which every original diameter has
an exact decreasing vector formula, without requiring a global additive
lattice chart. The certificate must be evaluated on one co-embedded source.

Canonical frontier effect: none. Fixed-star exact/nonconstant phase,
split-star, inactive-interface, and macroscopic-container branches are
not eliminated. No state-version or canonical prompt change is warranted.
