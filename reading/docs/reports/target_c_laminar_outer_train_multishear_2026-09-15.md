> Generated reading edition · [exact source](../../../docs/reports/target_c_laminar_outer_train_multishear_2026-09-15.md) · source SHA-256 `b565ad6aa6a14537e25eb07fa83a0264a77c1f6bc149ff83c8e8e37a89e995c0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4F57A48BE71B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — exact finite multi-shear chart for noncrossing outer trains

**Date:** 2026-09-15  
**Status:** proof-only structural strengthening  
**Scope:** any finite pairwise-disjoint family of audited outer-to-outer stopped-train crosscuts; application to the current `t=(q-k)/D<=1.844` smallest-leaf family  
**Dependencies:** audited finite stopped-train/cutset/shear primitives; audited complement-dual tree fact for pairwise noncrossing proper crosscuts; full actual-diameter visibility and relative-interior KKT stress  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The old global-train-shear report proves an exact finite shear for one outer-to-outer
train and only **superposes several train shears at first order**.  The current
smallest-leaf branch supplies a large pairwise-noncrossing family of outer-to-outer
trains, so the topology is much better: the complement dual of those crosscuts is a
tree.

That tree makes the several one-train shears exactly integrable.  If the selected
trains are indexed by the dual-tree edges, one may prescribe an independent small
angle on every selected train and translate each complementary region by the sum of
the corresponding one-train increments along its root path.  Then

1. every selected train contact is rotated by its prescribed angle and keeps length
   one;
2. every unselected contact is unchanged exactly;
3. every source pair changes by the signed sum of the shear increments on the unique
   dual-tree path joining its two regions; and
4. the relative-interior KKT stress gives an exact finite multi-shear diameter-energy
   identity.

Thus the current smallest-leaf family is not merely a collection of individually
available contact shears.  It carries a genuine finite-dimensional contact-preserving
chart whose active-diameter rows have **tree-path support**.  On the complete-rectangle
backbone this specializes to consecutive-interval support.

No response-conductance theorem and no sign claim such as `A_tau>w_tau` is used.

---

## 1. Selected crosscuts and the dual tree

Let

$$
\mathcal L=\{\tau_e:e\in E(\mathcal T)\}
$$

be a finite family of complete stopped trains satisfying:

- each `tau_e` has both terminal occurrences on the actual outer face;
- their audited midpoint tracks, viewed as proper outer-to-outer crosscuts, are
  pairwise disjoint.

The complement region/crosscut dual is therefore a tree `mathcal T`.  Its vertices
are the complementary regions and each selected train is one dual edge.

Root `mathcal T` at one region `o`.  For a dual edge `e`, delete `e` and call the
component not containing `o` the **child shore** `S_e`; the other component is
`T_e`.  Use the audited exact train-cut primitive to orient the unit contact vector
`u_e` so that every physical contact edge of `tau_e`, oriented from `T_e` to `S_e`,
has vector exactly `u_e`.

For a real parameter `theta_e`, put

$$
\boxed{
\Delta_e(\theta_e):=R_{\theta_e}u_e-u_e.
}
\tag{MS.1}
$$

For a dual region `v`, define its translation

$$
\boxed{
X_v(\theta)
:=\sum_{e\in P(o,v)}\Delta_e(\theta_e),
}
\tag{MS.2}
$$

where `P(o,v)` is the unique dual-tree path from the root to `v`.

Every source vertex lies in one complementary region because the train Jordan curves
cross physical contact edges only at edge interiors and contain no source vertex.
Translate every source vertex in region `v` by `X_v(theta)`.

---

## 2. Exact simultaneous contact preservation

### Theorem MS.1 — finite dual-tree multi-shear

For every sufficiently small parameter vector `theta=(theta_e)`, the deformation
(MS.2) preserves every actual contact length exactly.  More precisely:

- if a contact belongs to selected train `tau_e`, its new vector is
  `R_{theta_e}u_e` up to the fixed orientation;
- every other contact vector is unchanged.

Consequently, after shrinking the parameter neighborhood if necessary, every strict
noncontact also remains strictly longer than one.  Hence (MS.2) is a genuine finite
full-source unit-separation-preserving deformation.

### Proof

Fix a physical contact `xy`.

First suppose `xy` belongs to selected train `tau_e`.  The audited cutset theorem says
that `xy` crosses the Jordan cut of `tau_e`.  Since the selected train tracks are
pairwise disjoint, `xy` crosses no other selected cut.  Thus the dual regions of `x`
and `y` are adjacent across the single dual edge `e`.  Their root paths differ by
exactly `e`, so

$$
X_y-X_x=\pm\Delta_e.
$$

With the orientation from `T_e` to `S_e`, the sign is positive and

$$
(p_y+X_y)-(p_x+X_x)
=u_e+\Delta_e
=R_{\theta_e}u_e,
$$

which has length one.

Now suppose `xy` belongs to no selected train.  For every selected train `tau_e`, the
audited exact cutset theorem says that the only contact edges joining its two shores
are the physical edges of `tau_e`.  Hence `x` and `y` lie on the same side of every
selected cut.  Equivalently they lie in the same vertex of the complement dual tree,
so `X_x=X_y`.  Their contact vector is unchanged.

This proves exact contact preservation for every parameter vector for which the
translations are defined.  The source is finite and each noncontact starts at distance
strictly greater than one.  All pair distances depend continuously on the finite
parameter vector, so a sufficiently small common neighborhood of the origin preserves
all strict noncontact inequalities. `square`

The statement is stronger than first-order superposition.  No commutator or path-order
correction occurs because the construction is a sum of **translations** of regions;
the only rotations are the exact relative rotations of the cut contact vectors encoded
by (MS.1).

---

## 3. Every pair displacement is a tree-path sum

For a selected dual edge `e`, let

$$
\chi_e(v)=
\begin{cases}
1,&v\in S_e,\\
0,&v\in T_e.
\end{cases}
$$

For an ordered source pair `h=xy`, with endpoint regions `v_x,v_y`, put

$$
\varepsilon_{he}:=\chi_e(v_y)-\chi_e(v_x)\in\{-1,0,1\}.
\tag{MS.3}
$$

Then (MS.2) gives the exact identity

$$
\boxed{
X_{v_y}-X_{v_x}
=\sum_e\varepsilon_{he}\Delta_e(\theta_e).
}
\tag{MS.4}
$$

Moreover

$$
\boxed{
\{e:\varepsilon_{he}\ne0\}=P(v_x,v_y),
}
\tag{MS.5}
$$

the unique simple dual-tree path between the two endpoint regions.  Along that path
the signs are coherent after orienting the ordered pair from one endpoint region to
the other.

Thus if `r_h=p_y-p_x`, the exact deformed pair vector is

$$
\boxed{
r_h(\theta)
=r_h+\sum_e\varepsilon_{he}\Delta_e(\theta_e).
}
\tag{MS.6}
$$

For a selected family whose dual edges lie on one dual-tree path, (MS.5) says every
row support is one consecutive interval.  This is the exact finite version of the
interval structure suggested by the current small-leaf rectangle.

---

## 4. Exact KKT multi-shear identity

Let `H` be the full set of actual diameter pairs after the full-visibility
normalization.  Choose any fixed orientation for each `h in H` and write

$$
r_h=p_{y_h}-p_{x_h},\qquad |r_h|=D.
$$

Let `beta_h>0` be the relative-interior KKT diameter weights.  For selected train
`tau_e`, write

$$
A_e:=\sum_{c\in E(\tau_e)}\alpha_c>0
\tag{MS.7}
$$

for the total positive contact stress on its physical cut contacts.

Summing KKT equilibrium over the child shore `S_e` gives the audited shore resultant

$$
\boxed{
A_eu_e
=\sum_{h\in H}\beta_h\varepsilon_{he}r_h.
}
\tag{MS.8}
$$

Define the weighted actual-diameter square sum under the simultaneous shear by

$$
\Psi(\theta)
:=\sum_{h\in H}\beta_h|r_h(\theta)|^2.
\tag{MS.9}
$$

### Theorem MS.2 — exact finite multi-shear energy identity

For every sufficiently small `theta`, one has

$$
\boxed{
\Psi(\theta)-\Psi(0)
=-2\sum_eA_e(1-\cos\theta_e)
+\sum_{h\in H}\beta_h
\left|\sum_e\varepsilon_{he}\Delta_e(\theta_e)\right|^2.
}
\tag{MS.10}
$$

### Proof

Expand (MS.6):

$$
|r_h(\theta)|^2-|r_h|^2
=2r_h\cdot\sum_e\varepsilon_{he}\Delta_e
+\left|\sum_e\varepsilon_{he}\Delta_e\right|^2.
$$

After weighting and summing, interchange the first double sum and use (MS.8):

$$
2\sum_e\Delta_e\cdot
\sum_h\beta_h\varepsilon_{he}r_h
=2\sum_eA_e\Delta_e\cdot u_e.
$$

By (MS.1),

$$
\Delta_e\cdot u_e=\cos\theta_e-1.
$$

Substitution proves (MS.10). `square`

No sign is asserted for the right side.  In particular, the old response-based claim
`A_e>w_e` is not imported.  The cross terms in the final square are genuine and are
exactly the correlations a closing multi-train theorem must control.

---

## 5. First and second variations

Differentiate at the origin.  The first derivative of one actual diameter square is

$$
\boxed{
D_h'(0)[x]
=2\sum_e\varepsilon_{he}
(r_h\cdot Ju_e)x_e.
}
\tag{MS.11}
$$

Let `G` be the `|H| x |mathcal L|` matrix

$$
G_{he}:=2\varepsilon_{he}(r_h\cdot Ju_e).
\tag{MS.12}
$$

Equation (MS.8) immediately gives

$$
\boxed{G^{\mathsf T}\beta=0,
\qquad \beta_h>0.}
\tag{MS.13}
$$

The exact second variation of the weighted square sum is

$$
\boxed{
{1\over2}\Psi''(0)[x,x]
=
\sum_h\beta_h
\left|\sum_e\varepsilon_{he}x_eJu_e\right|^2
-\sum_eA_ex_e^2.
}
\tag{MS.14}
$$

Again, no sign is claimed.  Formula (MS.14) identifies the precise metric quadratic
form left after the first-order positive-spanning cusp.

---

## 6. Rank consequence from mixed rigidity

Suppose the selected family does not contain every stopped train of the connected
positive-contact core; equivalently there is at least one contact whose train is not
selected.  This is automatic in the smallest-leaf application below because the
center phase is nonempty and crosses the selected leaf trains.

The tangent vector obtained by differentiating parameter `theta_e` changes the angular
rate of train `tau_e` by one and changes the angular rate of every other contact train
by zero.  Hence a linear combination of the selected shear tangents is a Euclidean
translation only when all coefficients vanish.  It cannot be a nonzero Euclidean
rotation because a rotation gives the same nonzero angular rate on **every** contact
edge, including an unselected train.

If `Gx=0`, the corresponding selected multi-shear tangent preserves every contact and
every actual diameter length to first order.  Canonical mixed infinitesimal rigidity
then makes it Euclidean.  The preceding paragraph forces `x=0`.  Therefore

$$
\boxed{\operatorname{rank}G=|\mathcal L|.}
\tag{MS.15}
$$

Together with the strictly positive left-kernel vector (MS.13), this implies

$$
\boxed{|H|\ge|\mathcal L|+1.}
\tag{MS.16}
$$

The count itself is not the main gain; related global train/diameter counts already
exist.  The new information is that the full-rank matrix in (MS.15) has **tree-path
row support** by (MS.5), and interval support on every selected dual-tree backbone.

---

## 7. Application to the current smallest-leaf family

In the current `t<=1.844` full-core Type-II branch, the hostile-audited phase-resolved
work gives retained smallest-leaf outer-to-outer pair weight

$$
P_V>0.0848-o(1).
\tag{MS.17}
$$

Every retained pair weight is at most one.  Therefore there are more than

$$
\boxed{0.0848D-o(D)}
\tag{MS.18}
$$

distinct smallest-leaf outer-to-outer trains with positive retained pair weight.
They lie in one phase and are pairwise noncrossing.  Applying MS.1--MS.6 to this
family gives:

$$
\boxed{
\text{an exact finite }(0.0848D-o(D))\text{-parameter contact-preserving shear chart,}
}
\tag{MS.19}
$$

whose actual-diameter rows are supported on simple paths of the leaf complement dual
tree.

The stronger current complete-rectangle theorem extracts a dual-tree backbone block
of leaf trains all crossed by one common linear center family.  On any such backbone
block the matrix `G` has consecutive-interval row support.  After the current
inverse-`D` phase-collapse trimming, the selected `u_e` also lie in an angular window
of width `O(D^{-1})`.  Hence one obtains the concrete live object

```text
linear exact finite shear coordinates
+ interval-supported actual-diameter derivative rows
+ positive KKT left kernel
+ full column rank by mixed rigidity
+ O(D^-1) spread of the selected leaf directions on the trimmed rectangle.
```

This is substantially narrower than the general circular-split matrix in the old ZGS
report.

---

## 8. What remains for C-II closure

The theorem does **not** show simultaneous diameter feasibility.  A local maximum of
active diameter functions can still be pinned by a positive-spanning cusp, and
(MS.13)--(MS.15) explicitly allow that.

The remaining source-level problem is now a finite tree/interval problem.  One needs a
theorem showing that an actual planar diameter thrackle cannot positively span the
large near-parallel tree-path shear system supplied by the smallest-leaf rectangle.
Promising forms are:

1. an interval-row reuse bound using convex-thrackle endpoint order;
2. a second-order theorem combining (MS.14) with the `O(D^{-1})` phase spread;
3. a cut-resultant difference theorem that charges changes of
   `A_eu_e` to diameter endpoints in consecutive dual strips; or
4. a discrepancy choice of shear signs whose tree-path sums remain small while the
   coherent `1-cos(theta_e)` terms accumulate.

The last route is especially concrete on the ordered rectangle: alternating signs
keep first-order sums of nearly parallel `Ju_e` bounded on every interval, whereas
all `1-cos(theta_e)` terms have the same sign.  Turning that observation into a
uniform bound on **each** actual diameter, rather than only on a weighted aggregate,
is the missing step.

**Disposition:** proved proof-only finite integration of a noncrossing O--O shear
family and exact tree-path/KKT identities.  C-II and Level I remain open.

## Salvage provenance and lifecycle

Copied from `sol/c2-laminar-multishear-20260915` at tip
`a72257592979becabd4f6fe46dfa4845a29fee20`. This report is proof-only and its
finite crosscut family assumes the audited outer-to-outer train/cutset primitives stated
above. It gives no uniform feasible-radius estimate, nonzero descent direction, or C-II
or Level I closure. The accompanying 2026-09-15 hostile audit is retained separately;
this candidate remains unreviewed and noncanonical.
