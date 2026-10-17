> Generated reading edition · [exact source](../../../docs/audits/target_c_laminar_outer_train_multishear_hostile_audit_2026-09-15.md) · source SHA-256 `aa1daafe745e861c5de320ff224489d0018092caa28d126e62682fc1b93a66fb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DA4C860F93FA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — finite multi-shear chart for noncrossing outer trains

**Date:** 2026-09-15  
**Artifact:** `research/target_c_laminar_outer_train_multishear_2026-09-15.md`  
**Verdict:** **PASS at proof-only scope**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This audit targets the places where a simultaneous-train argument is most likely to
smuggle in a false statement.  In particular, the repository already contains an
audited warning that one-train finite shears may be superposed at first order without
thereby producing an arbitrary finite multi-train motion.  The new note claims a finite
motion only under the additional hypothesis that the selected outer-to-outer train
tracks are pairwise disjoint proper crosscuts, so their complement dual is a tree.

The claim survives the checks below.

---

## 1. No false global-stack assumption

The theorem does **not** say that every same-phase outer-to-outer train in the source is
globally linearly ordered.  Its finite construction uses the actual complement dual
`mathcal T`, which may branch.

For the current smallest-leaf application, pairwise noncrossing proper crosscuts and
the complement-tree description are already the corrected topological statements used
by the small-leaf rectangle theorem.  The new proof needs no stronger topology.

**Verdict:** pass.

---

## 2. The selected train curves contain no source vertex

The audited outer-train primitive uses a train midpoint track.  It meets the contact
graph only at interiors of the physical train edges.  Closing at the actual outer face
produces the usual shore split, and the equivalent proper-crosscut picture has no source
vertex on a selected crosscut.

Thus every source vertex belongs to a unique complementary region of the selected
crosscut family.  The region translation `X_v(theta)` is well-defined on every source
vertex, including contact-isolated source points.

**Verdict:** pass.

---

## 3. A selected contact sees exactly one increment

Fix a contact `xy` in selected train `tau_e`.  For its own cut, the audited cutset
lemma puts the two endpoints on opposite shores.  For any other selected train
`tau_f`, the same cutset lemma says that the only contact edges joining the two
`tau_f` shores are physical edges of `tau_f`.  Since distinct stopped trains cannot
share a physical contact edge, `xy` does not cross the `tau_f` shore split.

Therefore the endpoint region root paths differ by exactly dual edge `e`, not by a
larger path.  Their relative translation is precisely

```math
R_{\theta_e}u_e-u_e.
```

This is the key point that makes the finite construction exact.

**Verdict:** pass.

---

## 4. An unselected contact is unchanged

Let `xy` be a contact belonging to no selected train.  For every selected cut, the
cutset theorem puts `x,y` on the same shore.  Two regions of a tree-cut decomposition
are equal exactly when they have the same side label for every dual edge.  Hence the
endpoint regions coincide and the two endpoint translations are equal.

So there is no hidden accumulation of shear on an unselected contact, including a
contact on a train that crosses selected trains through rhombi.  Such a crossing train
meets the selected train **midpoint track**, but its own physical side contacts do not
cross the selected Jordan cut; the audited cutset theorem is exactly the needed
statement.

**Verdict:** pass.

---

## 5. Finite noncontact slack is legitimate

At each fixed finite source there are finitely many noncontact pairs and each starts at
distance strictly greater than one.  The region translations are continuous functions
of the finite parameter vector.  A common open neighborhood of the origin therefore
preserves all lower-distance inequalities.

No uniform-in-`D` radius is claimed or needed.  The theorem is a finite exact chart at
each source.

**Verdict:** pass.

---

## 6. Pair displacement really has tree-path support

For rooted dual edge `e`, the indicator `chi_e` is the child-component indicator.
Therefore

```math
\chi_e(v_y)-\chi_e(v_x)\ne0
```

exactly when deleting `e` separates the two endpoint regions.  In a tree this is
exactly the condition that `e` lies on the unique region path `P(v_x,v_y)`.

Subtracting the two root-path translation sums cancels every common edge and leaves
exactly that signed tree path.  On a dual-tree backbone path, the support is therefore
one consecutive interval.  This is a combinatorial identity, not an asymptotic
approximation.

**Verdict:** pass.

---

## 7. KKT shore-resultant signs are consistent

The theorem orients `u_e` from the root shore into the child shore.  With

```math
\varepsilon_{he}=\chi_e(v_y)-\chi_e(v_x),
```

a diameter edge contributes the oriented vector `epsilon_he r_h` to the child-shore
KKT sum.  Internal active edges cancel.  Hence

```math
A_eu_e=\sum_h\beta_h\varepsilon_{he}r_h
```

with the same sign convention used in the pair displacement formula.

The linear term in the weighted square expansion is consequently

```math
2\sum_e A_eu_e\cdot(R_{\theta_e}u_e-u_e)
=-2\sum_eA_e(1-\cos\theta_e).
```

No response inequality is needed.

**Verdict:** pass.

---

## 8. The quadratic term is not discarded

A dangerous false shortcut would sum the one-train negative-curvature formulas and
ignore cross terms.  The theorem does not do that.  It retains the exact term

```math
\sum_h\beta_h
\left|\sum_e\varepsilon_{he}\Delta_e\right|^2,
```

which contains every diagonal and cross correlation between selected shears.
Consequently the theorem makes no sign claim for the multi-shear weighted energy.

It also explicitly refuses to import the old unaudited response conclusion
`A_e>w_e`.

**Verdict:** pass.

---

## 9. Second variation normalization

For a one-parameter ray `theta_e=t x_e`,

```math
\Delta_e
=t x_eJu_e-{t^2x_e^2\over2}u_e+O(t^3).
```

Thus

```math
{1\over2}\Psi''(0)[x,x]
=\sum_h\beta_h
\left|\sum_e\varepsilon_{he}x_eJu_e\right|^2
-\sum_eA_ex_e^2.
```

The factor `1/2` and the sign of the `A_e` term in (MS.14) are correct.

**Verdict:** pass.

---

## 10. Mixed-rigidity rank claim has the required escape clause

The rank argument assumes an unselected contact train exists.  A nonzero Euclidean
rotation has one common angular rate on every contact, while a selected multi-shear
tangent has zero angular rate on every unselected train.  Hence a selected combination
that is Euclidean must have zero rotation rate.  Translation has zero train angular
rates, so every selected coefficient is then zero.

In the smallest-leaf application this hypothesis is automatic: the live dominant
orbit has a nonempty center phase, and the complete-rectangle theorem in fact provides
linearly many center trains crossing selected leaf trains.

Contact-isolated source points do not create an escape.  The selected train angular
rates live on the connected positive-contact core, so a nonzero selected coefficient
already makes the core motion non-Euclidean.

**Verdict:** pass.

---

## 11. The `|H|>=|L|+1` consequence is linear algebra only

`G` has `|L|` columns and full column rank.  The strictly positive KKT vector `beta`
is a nonzero vector in `ker G^T`.  Therefore the number of rows satisfies

```math
|H|-|L|=\dim\ker G^T\ge1.
```

No stronger diameter-edge count is inferred.  This avoids double-counting one diameter
edge across many selected cuts.

**Verdict:** pass.

---

## 12. Current smallest-leaf application

The parent phase theorem gives retained pair weight

```math
P_V={1\over D}\sum_\tau w_\tau>0.0848-o(1),
\qquad 0<w_\tau\le1.
```

Therefore the number of distinct positive-weight trains exceeds
`0.0848D-o(D)`.  Those trains are outer-to-outer and lie in one leaf phase; the parent
work already treats the family as pairwise noncrossing.

The new theorem can therefore be applied to that entire selected family.  The
complete-rectangle backbone is only needed for the further consecutive-interval and
inverse-`D` phase-spread specialization.

**Verdict:** pass.

---

## 13. What the audit does not certify

This audit does **not** certify any of the following stronger statements:

- that arbitrary crossing outer-train shears integrate to a finite multi-parameter
  motion;
- that the selected multi-shear can keep all diameter pairs nonincreasing;
- that the weighted multi-shear quadratic form is negative;
- that any KKT coefficient has a uniform positive lower bound;
- that tree-path support alone contradicts convex-thrackle geometry; or
- that C-II is closed.

The surviving new theorem is narrower and exact: a pairwise-disjoint O--O crosscut
family integrates to a finite contact-preserving dual-tree shear chart, and all pair
motions/KKT rows have the stated tree-path formulas.

**Final disposition:** PASS at proof-only scope.  The next serious obligation is a
metric/order theorem for the positive-spanning tree-path diameter rows, preferably on
the current inverse-`D` phase-collapsed rectangle.

## Salvage provenance

Copied from `sol/c2-laminar-multishear-20260915` at tip
`a72257592979becabd4f6fe46dfa4845a29fee20`; the audit applies only to the finite
crosscut hypotheses and proof-only claims in the linked report.
