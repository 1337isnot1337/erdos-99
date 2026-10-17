> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_diameter_pair_bridge_depth_2026-09-09.md) · source SHA-256 `54340ea36ade97aed0dd53ff8760a0308c78b72bfd0b3682381dee581e503322`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CDC253BBCCFA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — bridge dominance forces one diameter pair to cross linearly many bridges

**Date:** 2026-09-09  
**Repository state:** branch `sol/2026-09-09-zr-kernel-consequences`, reconciled against main `a8efd00fa7fca0c4a20911e86efd46cb0aadeb9c`  
**Run type:** exact bridge-flow synthesis  
**Target:** Target C, Gate C-II bridge-dominant phase  
**External web search:** no theorem imported  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C23 states the bridge-flow layer-cake identity in endpoint-mass form and concludes that bridge-dominant stress forces large `s_b/2`-weighted mean endpoint depth from the common diameter-routing hub. The same identity has a stronger pairwise interpretation that is not explicitly recorded in C23:

> the bridge-flow sum is exactly the `beta`-weighted mean bridge-tree path length of the **actual positive diameter edges**.

Consequently, if bridge stress is `eta D^2`, at least one actual diameter pair has a bridge-tree route of length at least `eta D`.

This is stronger than merely finding one endpoint at depth `eta D/2`, and it is independent of the C66 near-zero response phase. It complements ZBC, which under the additional near-zero hypothesis finds a shorter but macroscopic **heavy** subchain on one stress-star diameter route.

## 1. Setup

Let `T` be the positive-contact bridge-block tree and let `X_*` be the C23 Helly hub common to every active diameter path. For a loaded endpoint `b`, let

```math
d_b:=d_T(\tau(b),X_*).
\tag{1.1}
```

For an active diameter edge

```math
h=bk\in H
```

let `P_h` be the unique tree path joining `tau(b)` and `tau(k)`, and write

```math
\ell_T(h):=|E(P_h)|.
\tag{1.2}
```

Because C23 proves

```math
X_*\in P_h
\qquad(h\in H),
\tag{1.3}
```

the hub lies between the endpoint blocks on every diameter route. Therefore

```math
\boxed{
\ell_T(bk)=d_b+d_k.
}
\tag{1.4}
```

For each endpoint let

```math
s_b:=\sum_{bk\in H}\beta_{bk},
\qquad
\sum_b s_b=2,
\tag{1.5}
```

and for each rooted bridge edge let `w_e` be the C23 descendant endpoint mass. C23 gives

```math
\sum_e w_e
=\sum_b s_b d_b
\tag{1.6}
```

and

```math
\alpha_e\le D w_e.
\tag{1.7}
```

## 2. Strongest genuinely new audited theorem

### Theorem ZBD — actual-diameter pair depth identity

Under the C23 bridge-tree hypotheses,

```math
\boxed{
\sum_{e\in E(T)}w_e
=
\sum_{h\in H}\beta_h\,\ell_T(h).
}
\tag{ZBD1}
```

Consequently

```math
\boxed{
S_{\rm br}:=\sum_{e\in E(T)}\alpha_e
\le
D\sum_{h\in H}\beta_h\ell_T(h).
}
\tag{ZBD2}
```

If, for fixed `eta>0`,

```math
S_{\rm br}\ge\eta D^2,
\tag{ZBD3}
```

then

```math
\boxed{
\sum_{h\in H}\beta_h\ell_T(h)\ge\eta D
}
\tag{ZBD4}
```

and, because `sum_H beta_h=1`, there exists an actual active diameter edge `h_*` such that

```math
\boxed{
\ell_T(h_*)\ge\eta D.
}
\tag{ZBD5}
```

Thus one actual diameter pair of Euclidean length `D` is separated, in the positive-contact block tree, by at least `eta D` distinct contact bridges.

### Proof

Expand the endpoint expression in C23.16 using (1.5):

```math
\begin{aligned}
\sum_b s_b d_b
&=
\sum_b\left(\sum_{bk\in H}\beta_{bk}\right)d_b\\
&=
\sum_{bk\in H}\beta_{bk}(d_b+d_k).
\end{aligned}
\tag{2.1}
```

By the Helly-hub property (1.3), the unique tree path from `tau(b)` to `tau(k)` passes through `X_*`, so (1.4) gives

```math
d_b+d_k=\ell_T(bk).
\tag{2.2}
```

Insert (2.2) into (2.1) and combine with C23.16 to obtain ZBD1.

Now sum C23.12 over all contact bridges:

```math
S_{\rm br}
=\sum_e\alpha_e
\le
D\sum_e w_e.
\tag{2.3}
```

Use ZBD1 to get ZBD2. Under ZBD3, divide by `D` to obtain ZBD4.

Finally the normalized diameter weights satisfy

```math
\sum_{h\in H}\beta_h=1.
\tag{2.4}
```

Thus the left side of ZBD4 is a weighted average of the nonnegative integers `ell_T(h)`. At least one term is no smaller than the average, proving ZBD5. QED.

## 3. Exact Target C implication

The old C23 conclusion from bridge dominance was

```math
\frac12\sum_b s_b d_b\ge\frac\eta2D,
\tag{3.1}
```

a weighted endpoint-depth statement. ZBD identifies the same quantity as half of the `beta`-weighted diameter-pair route length and therefore produces one concrete diameter pair with bridge depth at least `eta D`.

This removes a quantifier weakness from the bridge frontier. A bridge-dominant survivor cannot hide all of its large tree depth in tiny endpoint masses spread across unrelated diameter pairs. Some actual diameter constraint itself traverses linearly many bridge cuts.

Under the additional C66 hypothesis `D epsilon->0`, ZBC gives more geometry on a route incident to the stress-star center: it contains an `Omega_eta(D)` subchain of bridges with `alpha=Omega_eta(D)`, line distance `o(D)` from the center, and near-unit radial progress on all but `o(D)` members. ZBD and ZBC are complementary:

- ZBD gives the stronger raw route-length lower bound `eta D` without near-zero assumptions;
- ZBC gives macroscopic stress and radial localization on a fixed positive fraction subchain under near-zero response.

## 4. Exact remaining lemma

The global scalar endpoint remains

```math
\boxed{
 b+\sum_F(\deg F-4)>2h.
}
\tag{4.1}
```

For the bridge-dominant branch, the route-local target can now be stated without endpoint-mass language:

> **BD — linear diameter-route exclusion.** For every fixed `eta>0`, exclude a sufficiently large lexicographically normalized triangle-free global minimizer having an actual diameter edge `bk` whose contact bridge-tree route contains at least `eta D` bridges, while the C29/C39 loaded-block and internal-diameter budgets and the ZBR/ZBL/ZBC constraints hold.
>
> It is enough to derive a strict sub-`D` competitor, an `Omega(1/D)` response defect in the near-zero phase, or the exact face inequality (4.1).

The main missing issue remains the geometry of the 2-edge-connected blocks between successive bridges. ZBD counts the cuts exactly but does not make the route an actual narrow contact path.

## 5. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| Helly hub for all diameter paths | canonical/report input C23 | Existing theorem. |
| `sum_e w_e=sum_b s_b d_b` | canonical/report input C23 | Existing layer-cake identity. |
| `sum_e w_e=sum_h beta_h ell_T(h)` | proved here | Expand endpoint incidences and use that every diameter path passes through the hub. |
| Bridge dominance gives one actual diameter pair with `ell_T>=eta D` | proved here | ZBD2 plus normalized `sum beta=1`. |
| Long bridge-tree route is a narrow contact path | not proved | Intervening 2-edge-connected blocks can have nontrivial geometry. |
| Long actual diameter route is impossible | still open | This is BD. |

## 6. Regressions and failed implications

### Tiny endpoint masses

ZBD eliminates the concern that large weighted endpoint depth could exist without any deep actual diameter pair. It does **not** give a lower bound on the `beta` weight of the deep pair; the maximizing pair may have arbitrarily small positive weight.

### Large intervening blocks

A diameter pair can cross `eta D` bridge cuts while the 2-edge-connected blocks between them contain substantial internal contact paths. The bridge count does not imply a contact path of length `eta D`, nor a path whose edge directions are controlled.

### Direct Theorem P application

Invalid. Theorem P requires an actual narrow contact path. ZBD provides a block-tree path. The conversion from block-tree depth to a narrow embedded contact path is the missing geometric theorem.

## 7. Literature imported

None.

## 8. Computation and reproducibility

No computation is used.

## 9. Canonical promotion recommendation

**Hold as report.**

If the ZR/ZF bridge synthesis is promoted, C23's endpoint-depth section should be amended by the exact pairwise identity ZBD1 and the direct consequence ZBD5.

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C23 gives a Helly hub X_* on every active diameter path and
  sum_e w_e = sum_b s_b d_b.
Because every diameter path bk passes through X_*,
  ell_T(bk)=d_b+d_k.
Therefore
  sum_e w_e = sum_{bk in H} beta_bk ell_T(bk).

Since alpha_e<=D w_e,
  S_bridge <= D sum_H beta_h ell_T(h).
Thus
  S_bridge >= eta D^2
implies
  sum_H beta_h ell_T(h) >= eta D,
and because sum_H beta_h=1, some actual diameter pair h_* satisfies
  ell_T(h_*) >= eta D.

Remaining issue:
control the 2-edge-connected blocks along this concrete deep diameter route strongly
enough to obtain a narrow contact path, response gap, strict sub-D competitor, or the
exact face inequality.
```
