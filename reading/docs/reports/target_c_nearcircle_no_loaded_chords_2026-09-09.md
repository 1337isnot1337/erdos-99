> Generated reading edition · [exact source](../../../docs/reports/target_c_nearcircle_no_loaded_chords_2026-09-09.md) · source SHA-256 `59a0cee3e6b60b69e1748e7b2cd2d4244c20cb0f170aed8434947cbd8747e379`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-671E8FD131F6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearcircle_no_loaded_chords_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=58e61418cd901140e118d25d694a100365a11e69; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — near-circle force hull has no nonconsecutive loaded unit chords

**Date:** 2026-09-09  
**Repository branch:** `research/disjoint-diameter-gap-2026-09-09`  
**Run type:** asymptotic convex-boundary rigidity theorem  
**Target:** DC/HB small-outer-walk near-circle endpoint  
**Depends on:** DC force-hull Hausdorff convergence, C42 identification `B_+=Vert(F)`, unit separation  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The earlier DC report proved only

```math
e_{BB}\ge q-x_B
```

and incorrectly inferred `e_BB/D->pi`; a subsequent correction withdrew that inference because extra unit chords between nonconsecutive loaded hull vertices had not been excluded.

The present theorem supplies the missing geometric upper bound.

In the `x_B=o(D)` near-circle branch, for all sufficiently large members of the sequence, **every loaded-loaded unit contact joins consecutive vertices of the force hull**. Therefore

```math
\boxed{e_{BB}\le q.}
\tag{NC.1}
```

If `a` is the number of force-hull sides that are not unit contacts, then in fact

```math
\boxed{e_{BB}=q-a,}
\tag{NC.2}
```

and the outer-walk excess gives `a<=x_B`. Hence

```math
\boxed{q-x_B\le e_{BB}\le q.}
\tag{NC.3}
```

Since DC gives

```math
q/D\to\pi,
\qquad
x_B=o(D),
```

we now legitimately obtain

```math
\boxed{e_{BB}/D\to\pi.}
\tag{NC.4}
```

For the NBd extra-loaded-contact currency

```math
E_{BB}:=e_{BB}-(q-x_B),
```

NC gives

```math
\boxed{0\le E_{BB}=x_B-a\le x_B=o(D).}
\tag{NC.5}
```

Thus a linear population of extra loaded-loaded contact chords is impossible in the disk-limit force hull.

---

## 1. Setup

Take a sequence in the PR #119 small-outer-walk branch:

```math
x_{B,j}=o(D_j).
```

DC proves that, after translations and scaling,

```math
\boxed{F_j/D_j\to B_{1/2}}
\tag{1.1}
```

in Hausdorff distance.

C42 identifies the loaded terminal set with the strict convex-hull vertices:

```math
B_{+,j}=\operatorname{Vert}(F_j).
\tag{1.2}
```

Every two source points are at distance at least one.

Suppose, toward contradiction, that along a subsequence there is a loaded-loaded unit contact

```math
|u_j-v_j|=1
\tag{1.3}
```

whose endpoints are not consecutive vertices of `F_j`.

---

## 2. The normalized endpoints coalesce at one circle point

Normalize

```math
\bar u_j=u_j/D_j,
\qquad
\bar v_j=v_j/D_j
```

after the DC translations.

Then

```math
|\bar u_j-\bar v_j|=1/D_j\to0.
```

Pass to a subsequence. Hausdorff convergence (1.1) gives

```math
\bar u_j,\bar v_j\to p\in\partial B_{1/2}.
\tag{2.1}
```

The limit lies on the boundary because both points are vertices of `F_j`.

---

## 3. The local boundary arc becomes tangent-flat

Let `Gamma_j` be the boundary arc of `F_j` from `u_j` to `v_j` corresponding, after normalization, to the short cyclic neighborhood of `p` rather than the complementary arc around the rest of the body.

### Lemma NC.1 — uniform local tangent convergence

Every oriented edge direction occurring on `Gamma_j` converges to the unique tangent direction of `partial B_{1/2}` at `p`.

### Proof

Suppose not. Then there are edges `a_jb_j` of `Gamma_j` whose oriented directions stay a fixed positive angle away from the tangent at `p`.

Because `Gamma_j/D_j` lies on the convex boundary between two vertices converging to `p` along the short local order, every point of `Gamma_j/D_j` also converges to `p`. One way to see this without assuming a boundary parametrization is to choose two fixed support lines of the limiting disk through small neighborhoods on either side of `p`. For all large `j`, convexity and Hausdorff convergence trap the short boundary arc between the corresponding nearby support points inside an arbitrarily small neighborhood of `p`.

An edge `a_jb_j` has an outward normal belonging to the normal cone of `F_j` at every relative-interior point of that edge. Pass to a convergent subsequence of these unit normals. Hausdorff convergence of convex bodies implies every limiting support normal at points converging to `p` is a support normal of the limiting disk at `p`. The disk has the unique outward normal parallel to `p`. Therefore the edge normals converge to that unique normal, and the edge directions converge to the unique tangent direction, contradiction. `square`

Thus if `d_j` is a unit tangent vector at `p` with the orientation from `u_j` to `v_j` along `Gamma_j`, every hull-side vector `w` on the arc satisfies

```math
\frac{d_j\cdot w}{|w|}=1-o(1)
\tag{3.1}
```

uniformly over the sides of `Gamma_j`.

---

## 4. A nonconsecutive unit chord would need at least two almost-parallel unit sides

Because `u_j,v_j` are assumed nonconsecutive vertices of the convex polygon `F_j`, **both** cyclic boundary arcs between them contain another hull vertex. In particular the short local arc `Gamma_j` contains at least one intermediate loaded hull vertex and therefore at least two hull sides.

Write the consecutive side vectors on `Gamma_j` as

```math
w_{1,j},\ldots,w_{k_j,j},
\qquad k_j\ge2.
```

Every hull side joins two distinct source points, so unit separation gives

```math
|w_{r,j}|\ge1.
\tag{4.1}
```

Their sum is the endpoint chord:

```math
\sum_{r=1}^{k_j}w_{r,j}=v_j-u_j.
\tag{4.2}
```

Project (4.2) onto the local tangent `d_j`. By NC.1,

```math
\begin{aligned}
|v_j-u_j|
&\ge d_j\cdot(v_j-u_j)\\
&=\sum_{r=1}^{k_j}d_j\cdot w_{r,j}\\
&\ge(1-o(1))\sum_{r=1}^{k_j}|w_{r,j}|\\
&\ge(1-o(1))k_j\\
&\ge2-o(1).
\end{aligned}
\tag{4.3}
```

But the assumed contact has

```math
|v_j-u_j|=1,
```

contradiction for all sufficiently large `j`.

Therefore every loaded-loaded unit contact eventually joins consecutive force-hull vertices. This proves NC.1.

---

## 5. Exact contact count on the loaded hull

There are exactly `q` force-hull sides. Let `a` be the number whose Euclidean length is strictly greater than one. The remaining `q-a` hull sides have length exactly one and are therefore loaded-loaded contact edges.

NC.1 says there are no other loaded-loaded contact edges. Hence

```math
e_{BB}=q-a,
```

proving NC.2.

The outer-walk decomposition used in HB has `q` intervals of positive integer lengths `ell_i` and

```math
x_B=\sum_i(\ell_i-1).
```

If a hull side is not a unit contact, its interval cannot have length one, so each of the `a` missing unit hull sides contributes at least one to `x_B`. Therefore

```math
a\le x_B.
```

This gives NC.3--NC.5.

---

## 6. Consequences for the exact near-circle boundary budget

NBd defines

```math
E_{BB}=e_{BB}-(q-x_B).
```

Before NC, only `E_BB>=0` was known. NC now gives

```math
E_{BB}=x_B-a=o(D).
```

Therefore NBd simplifies asymptotically to

```math
\boxed{
S+R_I+s_B+3c_I+s_C
=(\pi+o(1))D
}
\tag{6.1}
```

throughout the near-circle branch.

Likewise ZU becomes

```math
\boxed{
c_I+s_C=d_H+s_Z+o(D),}
\tag{6.2}
```

because `e_BB=q+o(D)` and `x_B=o(D)`.

Thus the disk-limit branch has no linear loaded-loaded chord escape: every linear post-ZF defect must be carried by the harmonic components, unused loaded degree, pinned-contact stress, face defect, or diameter/mixed-stress currencies.

---

## 7. Audit against local regressions

### Equilateral near-triangle on the hull

Three nearby convex hull vertices can have two unit sides and a nearly unit diagonal without violating NC. The theorem excludes only an **exact** unit diagonal between nonconsecutive loaded vertices once the normalized hull tends to the smooth disk. Exact equality would force a two-edge local boundary path of length at least two to sum to a vector of length one while its directions become tangent-parallel.

### Rhombic ear

A convex unit rhombus can have a unit diagonal edge in a different unit-rhombus orientation only at a fixed positive turning angle. A linear-scale disk has vanishing tangent turn over any boundary chord of fixed Euclidean length, so such a local rhombic ear cannot sit entirely among loaded hull vertices in the near-circle limit.

### Bad outer intervals

NC does not assert that every hull side is a contact. Missing hull-side contacts remain allowed and are counted by `a<=x_B=o(D)`.

### Interior loaded-loaded contacts

Any straight contact between two loaded vertices is a chord of the convex force hull. NC proves such a unit chord cannot be nonconsecutive, so there are no additional interior `B-B` contacts asymptotically.

---

## 8. Relation to the earlier DC correction

The correction report was necessary: DC.7 alone did not justify `e_BB/D->pi`.

NC supplies a genuinely new upper theorem, so the convergence may now be restored **with NC as a dependency**:

```math
q-x_B\le e_{BB}\le q,
\qquad
q/D\to\pi,
\qquad
x_B=o(D)
```

imply

```math
e_{BB}/D\to\pi.
```

Any downstream use of this equality should cite NC, not the original DC argument.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| local tangent directions on a shrinking disk-limit boundary arc converge | proved | convex Hausdorff convergence to a smooth strictly convex limit with unique normal |
| nonconsecutive unit loaded chord impossible | proved | short arc has at least two sides of length >=1 with asymptotically common direction |
| `e_BB=q-a` | proved | all and only unit hull sides remain as B-B contacts |
| `a<=x_B` | proved | every missing hull contact requires a long outer-walk interval |
| `e_BB/D->pi` in near-circle branch | proved with NC | two-sided squeeze |
| `E_BB=o(D)` | proved | `E_BB=x_B-a` |
| Level I | still open | harmonic/face/stress currencies remain |

---

## 10. Next target

NC removes one entire linear escape from the near-circle budget. Combined with TD/TS, the cap-minimal full-core branch now has

```text
q=(pi+o(1))D,
e_BB=(pi+o(1))D,
E_BB=o(D),
S=(2+o(1))D,
R_I>=(pi/sqrt(2)-2-o(1))D,
```

with two positive-density semicircular harmonic components.

The next useful theorem is to exploit the **actual semicircle perimeter**, rather than Eppstein's shape-free isoperimetric perimeter, for each of those two internal penny graphs. This should strengthen the internal edge deficit from `pi/(2sqrt(2)) D` to at least half the semicircle perimeter `((pi/4)+1/2)D` if their internal convex hulls are forced to fill the cap. That improvement can be proved directly from Euler once the internal-hull convergence is established.
