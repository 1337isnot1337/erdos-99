<!-- theorem-state: {"artifact_id":"ART-D3A50EF2E4E2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZEG: exceptional trunk reset forces the post-ZF high-surplus/gap branch

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** exact phase coupling after ZAC/ZDC  
**Target:** Target C bridge-dominant near-zero phase  
**Depends on:** ZDC, ZHL, current-main component ledger and GU  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZDC reduces the complete ZHT trunk to directed, asymptotically radial corridors at all but `o(D)` block positions. The only way the route can still make a macroscopic geometric reset is for the exceptional blocks to consume a macroscopic amount of the global internal block-diameter budget.

The current-main component cancellation identity charges that budget exactly to

\[
L_2:=6-3(d_H+s_Z)+e_{BB}+2s_C.
\]

This report records the resulting exact phase split and feeds it into GU. It does not close either branch, but it removes the possibility that the exceptional-block escape is a free geometric phenomenon.

---

## 1. Exceptional blocks after ZDC

Let the ZHT trunk have successive bridge blocks

\[
X_0,\ldots,X_H,
\qquad H=\Omega_\eta(D).
\]

ZDC supplies a set `G_D` of good internal block positions with

\[
|\{1,\ldots,H-1\}\setminus G_D|=o(D),
\tag{1.1}
\]

such that every `i in G_D` is either singleton or has a directed, asymptotically radial port-to-port corridor.

Let

\[
\mathcal E_D
:=
\{X_i:i\notin G_D\}
\tag{1.2}
\]

be the exceptional block set and define its exact graph-diameter budget

\[
\boxed{
R_D:=\sum_{X\in\mathcal E_D}\delta_X.
}
\tag{1.3}

The cardinality of `mathcal E_D` is `o(D)`, but a priori `R_D` may still be `Theta(D)`.

---

## 2. Exact component ledger charges every exceptional reset

Current main proves

\[
\boxed{
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+e_{BB}+2s_C.
}
\tag{2.1}

All terms are nonnegative. Hence

\[
\sum_r\delta_r
\le
6-3(d_H+s_Z)+e_{BB}+2s_C
\le
6+e_{BB}+2s_C.
\tag{2.2}

Every trunk block lies inside the captured unloaded component closure, and its internal block diameter is among the graph-diameter costs counted by the same contact decomposition. In particular

\[
R_D\le\sum_r\delta_r.
\tag{2.3}

Therefore

\[
\boxed{
 e_{BB}+2s_C
\ge
R_D-6+3(d_H+s_Z).
}
\tag{ZEG1}

and in particular

\[
\boxed{
 e_{BB}+2s_C\ge R_D-6.
}
\tag{ZEG2}

Thus a macroscopic exceptional-block reset forces a quantitatively macroscopic post-ZF contact/stress surplus.

---

## 3. Exact two-way route split

Pass to any subsequence. There are only two possibilities.

### Branch ZEG-A — sublinear exceptional detour

\[
\boxed{R_D=o(D).}
\tag{ZEG3}

Then the total graph length available inside all ZDC-exceptional blocks is sublinear. Since every contact edge has Euclidean length one, the total Euclidean displacement and total possible loss of forward `u_0` progress generated inside those exceptional blocks is also `o(D)`.

Consequently the only remaining macroscopic part of the ZHT route is carried by the ZDC directed radial segments. This does not yet prove the sharp Theorem-P angular hypothesis, but it removes the last macroscopic **length** reset from the bridge blocks.

### Branch ZEG-B — macroscopic exceptional detour

There is a fixed `theta>0` and a further subsequence such that

\[
\boxed{R_D\ge\theta D.}
\tag{ZEG4}

Then ZEG2 gives

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge\theta-o(1).
}
\tag{ZEG5}

So the exceptional reset is paid one-for-one, at leading order, by the exact GU surplus currency.

---

## 4. Feed Branch B into GU

Current main's GU theorem writes

\[
\lambda_2
:=
\limsup\frac{e_{BB}+2s_C}{D}
\]

and proves

\[
\boxed{
\liminf\frac G{D^2}
\ge
\frac{\sqrt3}{4}-\frac\pi4\lambda_2^2.
}
\tag{4.1}

A positive quadratic attachment-cell area gap is forced whenever

\[
\lambda_2<
\lambda_*:=
\sqrt{\frac{\sqrt3}{\pi}}
=0.7425152492\ldots.
\tag{4.2}

Therefore the exceptional-reset branch splits further:

1. if
   \[
   \theta\le\lambda_2<\lambda_*,
   \]
   the source has a positive quadratic attachment-cell gap, which GU localizes to a macroscopic outer pocket or a bounded exceptional face of linear perimeter;
2. if
   \[
   \lambda_2\ge\lambda_*,
   \]
   the post-ZF contact/stress surplus itself is at least `0.7425...D` asymptotically.

Thus a macroscopic reset cannot stay in a low-surplus/no-gap region.

---

## 5. Add the independent ZOB bridge currency

The same bridge-dominant phase satisfies the exact ZOB bound

\[
\boxed{x_B\ge\eta D-1.}
\tag{5.1}

Hence Branch ZEG-B simultaneously pays

\[
\boxed{
 x_B\ge\eta D-O(1),
\qquad
 e_{BB}+2s_C\ge\theta D-O(1).
}
\tag{ZEG6}

These are distinct exact post-ZF currencies. In the low-`lambda_2` subbranch they coexist with a quadratic force-hull/attachment-cell gap; in the high-`lambda_2` subbranch they coexist with a quantitatively large pinned/contact surplus.

Current exact ledgers do not yet provide an upper bound coupling this pair strongly enough to contradict `q<=pi D`. ZEG's role is to make the remaining geometric reset branch explicit and charged.

---

## 6. What Branch A now means geometrically

If `R_D=o(D)`, concatenate the ZDC-good route pieces through arbitrary shortest paths inside the exceptional blocks. The exceptional pieces add only `o(D)` contact edges.

All good internal corridor edges have

\[
|\Delta r|=1-o(1)
\]

and positive `u_0` displacement; all but `o(D)` trunk bridges have the same strong-radial property. Therefore one obtains a complete `z`-to-deep-route contact path for which

- only `o(D)` edges lie in exceptional blocks or fail the moving radial threshold;
- the total number of exceptional-block path edges is `o(D)`;
- the remaining macroscopic population is directed and radially efficient.

This is now an **almost-geodesic path problem with a sparse exceptional set**, rather than a block-tree problem.

The missing conversion is quantitative: sparse exceptional edges can still turn by large angles, and the sharp Theorem P assumes a uniform angular bound on every edge. A robust/sparse-error extension of Theorem P is therefore a concrete next target in Branch A.

---

## 7. Exact next theorem split

ZEG reduces the bridge-dominant small-defect branch to two checkable mathematical targets.

### Target A: robust narrow-path theorem

Prove that a diameter-realizing contact route with only `o(D)` exceptional length, and with every other edge directed in `u_0` and satisfying `|Delta r|=1-o(1)`, cannot occur in a sufficiently large triangle-free global minimizer unless an internal route vertex becomes a diameter endpoint or a strict sub-`D` motion exists.

### Target B: surplus/gap coupling

Prove that a post-ZF source cannot simultaneously have

\[
x_B\ge\eta D-O(1)
\]

and either

\[
e_{BB}+2s_C\ge\lambda_*D-o(D)
\]

or GU's macroscopic outer-pocket/giant-face geometry.

Either theorem eliminates the exceptional-reset escape.

---

## 8. Classification

**Status:** exact report-level phase reduction.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.  
**Dependencies:** ZDC/ZHT, current-main component cancellation and GU, ZOB.
