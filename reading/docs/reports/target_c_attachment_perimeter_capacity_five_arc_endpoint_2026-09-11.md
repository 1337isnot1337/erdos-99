> Generated reading edition · [exact source](../../../docs/reports/target_c_attachment_perimeter_capacity_five_arc_endpoint_2026-09-11.md) · source SHA-256 `6e89b40d5558ff265e1b07abfee21dd68e007213c29bc7c7e54f06648293a5f4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7B00F6C7C8DF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — attachment-perimeter capacity excludes the five-arc endpoint

**Date:** 2026-09-11  
**Run type:** exact planar attachment theorem / endpoint exclusion  
**Target:** Target C, C-II, all-phase renormalized-surplus frontier  
**Status:** unpromoted research report; route-map status unchanged

## LEVEL I STATUS

`STILL OPEN`.

The five-arc pin-delay report gives the all-phase lower bound

$$
 \liminf\mu_D\ge z_* >0.9604,
 \qquad
 10\arcsin z_*-4\pi=z_*/3,
$$

for

$$
 \mu_D={e_{BB}+2s_C-3(d_H+s_Z)\over D}.
$$

It also identifies the only possible endpoint geometry: one macroscopic unloaded
component has normalized graph diameter and attachment count

$$
 {\delta_r\over D}\to z_* ,
 \qquad {|A_r|\over D}\to z_*/3,
$$

and its actual attachment directions saturate five wrapping arcs.  The new theorem
below excludes that endpoint exactly.  Consequently there is a nonexplicit absolute
gap above `z_*`.  This does not close the unrestricted high-surplus branch.

## 1. Attachment-perimeter capacity

Let `I` be one unloaded positive-contact component, with

$$
 n=|I|,
 \qquad
 A=\{b\in B: b\text{ has a contact edge into }I\},
 \qquad a=|A|.
$$

Let `e` be the number of contacts internal to `I`, and `t` the number of contacts
between `I` and `A`.  Put

$$
 P_A=\operatorname{per}(\operatorname{conv}A).
$$

### Theorem APC

In the fully force-visible C-II branch,

$$
\boxed{P_A\le 4a-6.}
\tag{APC.1}
$$

### Proof

Consider the straight-line contact graph `G_I` induced by `I\cup A`, retaining the
`e` internal edges and the `t` attachment edges.  It is connected because `I` is
connected and each member of `A` is attached to `I`.  It is a simple triangle-free
planar penny graph: these are inherited from the source contact graph.

The pinned-rigidity argument used in C40 applies to this component.  The positive
contact stress restricted to the `e+t` rows gives a nonzero left-kernel relation,
whereas the pinned contact matrix has rank `2n`.  Therefore

$$
 e+t\ge 2n+1.
\tag{APC.2}
$$

All vertices of `I` lie in `\operatorname{conv}A` by the harmonic attachment-hull
theorem.  Every member of `A` is a vertex of `\operatorname{conv}A`, because the
loaded force-hull vertices are strictly convex and `A` is a subset of them.

Let `b` be the length of the outer-face boundary walk of `G_I`, counting a bridge
twice.  The geometric image of that walk contains all vertices of `A` and all other
vertices lie in `\operatorname{conv}A`; hence the convex-hull perimeter inequality for
a closed polygonal walk gives

$$
 b\ge P_A.
\tag{APC.3}
$$

If `f` is the number of bounded faces, Euler's formula gives

$$
 f=e+t-(n+a)+1.
$$

Every bounded face has length at least four, since `G_I` is simple and triangle-free.
Thus

$$
 2(e+t)\ge b+4f
 =b+4(e+t-n-a+1),
$$

or

$$
 e+t\le 2(n+a)-2-b/2.
\tag{APC.4}
$$

Combining (APC.2) and (APC.4) gives `b\le4a-6`.  Together with (APC.3), this is
(APC.1). `square`

There is also a retained-defect form. Define the component pinned-stress slack

$$
 s_I:=e+t-2n-1\ge0.
$$

Replacing (APC.2) by `e+t=2n+1+s_I` in (APC.4) gives the exact strengthening

$$
\boxed{P_A\le4a-6-2s_I.}
\tag{APC.10}
$$

Thus any extra pinned-contact nullity makes the attachment-perimeter capacity
strictly tighter. This uses no Eppstein equality or near-equality classification.

More generally, suppose a macroscopic attachment set has `m` cyclic inter-block gaps
of angular size at least `2\varphi+o(1)`, with all those gaps asymptotically below
`\pi`. If `a/D\to\alpha`, then APC gives the necessary density inequality

$$
\boxed{m\sin\varphi\le4\alpha.}
\tag{APC.11}
$$

Indeed each such gap contributes `D\sin\varphi+o(D)` to the perimeter of the
attachment polygon, and the remaining edges contribute nonnegatively. This is an
attachment-incidence analogue of the projective pin-density bound; it survives even
when the occupied arcs are not equal or uniformly filled.

No equality classification of Eppstein's theorem is used.  In particular, the
argument is valid in the near-Eppstein regime where the earlier audit correctly
rejected a quadrangulation conclusion.

## 2. Five saturated arcs force a large attachment perimeter

Use the five-arc endpoint notation from the pin-delay report.  Let

$$
 \varphi_*:=\pi-2\arcsin z_*.
$$

The five wrapping arcs are separated cyclically by gaps of angular size at least
`2\varphi_*`.  The endpoint saturation statement means that the actual attachment
set `A_r` has points in all five occupied arcs; the selected diameter directions and
the attachment polar directions differ by `o(1)` uniformly.

Since `0.9604<z_*<0.961`,

$$
 2\varphi_*<\pi,
 \qquad
 2\pi-8\varphi_*<\pi.
\tag{APC.5}
$$

Therefore the five inter-arc gaps between consecutive attachment points are all in
`(0,\pi)` for sufficiently large sources.  All attachment points lie at radius
`D/2+o(D)` from the common full-source center.  A chord spanning an angular gap
`\gamma` consequently has length

$$
 D\sin(\gamma/2)+o(D).
$$

Each of the five inter-arc gaps is at least `2\varphi_*+o(1)`, so the perimeter of
the attachment hull satisfies

$$
 \liminf {P_{A_r}\over D}
 \ge 5\sin\varphi_* .
\tag{APC.6}
$$

On the other hand, endpoint pin saturation gives

$$
 {|A_r|\over D}\to {z_*\over3}.
\tag{APC.7}
$$

APC.1 and (APC.7) imply

$$
 \limsup {P_{A_r}\over D}\le {4z_*\over3}.
\tag{APC.8}
$$

The two limits are incompatible.  Indeed,

$$
5\sin\varphi_*
 =10z_*\sqrt{1-z_*^2},
$$

and `z_*<0.961` gives `\sqrt{1-z_*^2}>2/15`, whereas

$$
 10z_*\sqrt{1-z_*^2}>{4z_*over3}.
\tag{APC.9}
$$

This proves:

### Theorem APE

There is no unbounded post-ZF C-II survivor sequence with

$$
 \mu_D\to z_*.
\tag{APE.1}
$$

### Proof

Assume such a sequence.  The pin-delay endpoint theorem supplies the giant component
and its five saturated arcs.  Apply APC to that component and then (APC.6)--(APC.9),
which gives a contradiction. `square`

## 3. Uniform consequence

The five-arc pin-delay theorem already gives `\liminf\mu_D\ge z_*`.  If there were
no uniform gap, there would be an unbounded sequence with

$$
 z_*\le\mu_D<z_*+1/j
$$

for its `j`th member.  Passing to the endpoint subsequence invokes APE, a
contradiction.  Hence:

### Corollary APG

There exist absolute `\varepsilon_{AP}>0` and `D_0<\infty` such that every
sufficiently large post-ZF survivor satisfies

$$
\boxed{\mu_D\ge z_*+\varepsilon_{AP}.}
\tag{APG.1}
$$

The gap is nonexplicit because the current five-arc theorem supplies endpoint
compactness but not a quantitative stability rate for the saturation statement.

## 4. Exact surviving obstruction

APG removes only convergence to the first five-arc pin-delay endpoint.  It does not
prove `\mu_D\ge1`.  The unrestricted high-surplus branch still contains:

* three-arc attachment cells with `\mu` above the scalar `\pi/4` area threshold;
* genuine five-arc configurations away from the endpoint, where the inequality
  `P_A\le4|A|-6` has room;
* higher odd-component attachment phases;
* selected maximal forest circuits;
* underbraced singular extreme circuits (`\sigma_*>0`); and
* contact-isolated source points, which the attachment theorem does not see.

In particular APG is a new endpoint exclusion and not a settlement of Erdős #99.

## 5. Regression audit

* **Contact-isolated points:** absent from `I\cup A` and untouched by APC; they remain
  the full-source obstruction.
* **Odd shells:** not in the C-II post-ZF endpoint hypothesis; regular shells have
  `s_Z=2` and remain a separate regression.
* **Bridge/repeated outer edges:** the outer-face walk counts bridges with multiplicity,
  so APC does not assume a 2-connected component.
* **Whole-circuit attachment exception:** APC uses only the exact C40 pinned-rank
  relation and Euler, not a proper-subset circuit sparsity inequality.
* **Near-Eppstein equality:** no quadrangulation or deletion classification is used.
* **Five-arc orientation:** the five large gaps are read from actual stopped endpoint
  directions, not hypothetical through-hole continuations.

## 6. Promotion note

This report is unpromoted.  Before route-map promotion, audit the passage from the
five saturated projective endpoint arcs to the five actual cyclic attachment gaps in
(APC.6), including the `o(1)` full-source center error and the finite-source choice of
one attachment point per arc.
