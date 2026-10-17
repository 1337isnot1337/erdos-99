> Generated reading edition · [exact source](../../research/target_c_global_outer_train_exact_multishear_hostile_audit_2026-09-15.md) · source SHA-256 `f25080966ce8998194168431f2fff4b246f3e189e2ff282435a03c574edae59e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Hostile audit — exact simultaneous finite shear for arbitrary O--O trains

**Date:** 2026-09-15
**Reviewed:** `research/target_c_global_outer_train_exact_multishear_2026-09-15.md`
**Disposition:** **PASS at proof-only audited O--O cutset scope**
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The candidate upgrades the old statement “one-train shears superpose at first order”
to an exact finite multi-parameter placement for arbitrary O--O train cuts, including
crossing cuts.  That is a meaningful strengthening, so the audit focuses on the points
where finite composition could fail: overlapping shore translations, contacts from a
second train, singleton trains, inactive source points, and orientation signs in the
KKT identity.

---

## 1. Finite superposition is addition of translations, not composition of rotations

For train `i` the one-train displacement vector is

$$
\Delta_i=R_{\theta_i}u_i-u_i.
$$

The candidate does **not** rotate an entire shore as a rigid body and then rotate it
again about another center.  It defines one final source placement

$$
p_v(\theta)=p_v+\sum_{i:v\in S_i}\Delta_i.
$$

Thus different train operations commute algebraically: they are ordinary translations
of subsets in the final coordinate formula.  Noncommutativity of planar rotations is
irrelevant.

**Verdict:** PASS.

---

## 2. A contact is separated by exactly its own train cut

The audited O--O cutset theorem says that for cut `i`, the contact edges with endpoints
on opposite shores are exactly the physical contact edges belonging to `tau_i`.
Complete stopped trains partition the contact edges.

Therefore a contact `xy` on `tau_j` satisfies:

- cut `j` separates its endpoints;
- every selected cut `i!=j` puts its endpoints on the same shore.

Consequently the relative displacement of that contact under the full multi-parameter
placement contains only `Delta_j`, and its vector becomes

$$
u_j+\Delta_j=R_{\theta_j}u_j.
$$

Every other train's finite shear cancels exactly between the two endpoints.  This
argument does not use disjointness or laminarity of the train midpoint curves.

**Verdict:** PASS.

---

## 3. Crossing train cuts create no hidden contact interference

Suppose two selected O--O train midpoint curves cross in a strict rhombus.  Their shore
boundaries intersect, so there is no common nesting order.  This does not affect the
proof.

At the rhombus, a contact edge belongs to exactly one of the two stopped trains.  The
cutset theorem for the other train therefore places both endpoints of that contact on
the same shore.  The other train's translation moves those endpoints equally.  The
same statement holds at every crossing rhombus.

Thus the candidate's finite superposition remains exact even for mutually crossing
selected train families.

**Verdict:** PASS.

---

## 4. Singleton O--O trains are legitimate

An O--O singleton train is an outer-face bridge.  The audited finite train primitives
include the bridge shear: choose one connected bridge shore, translate it by
`R_theta u-u`, and the only contact crossing the shore cut is the singleton bridge
edge itself.

Hence the same cancellation proof applies to singleton selected trains.  No assertion
that the current retained O--O populations are individually non-singleton is needed.

**Verdict:** PASS.

---

## 5. Full-source and inactive unit-separation constraints survive locally

The placement is defined on the full finite source, including contact-isolated points,
using their side membership for each selected shore split.  Every old contact is
preserved exactly as above.

Every old noncontact begins with distance strictly greater than one.  There are only
finitely many source pairs, and every pair distance is continuous in the finite
parameter vector.  Therefore one neighborhood of the origin preserves all strict
noncontact lower bounds simultaneously.

No uniform-in-`D` radius is required.

**Verdict:** PASS.

---

## 6. Signed split-row formula is exact

For an arbitrarily oriented pair `h=xy`, define

$$
\sigma_{hi}=1_{S_i}(y)-1_{S_i}(x).
$$

Subtracting the explicit vertex placements gives

$$
r_h(\theta)=r_h+\sum_i\sigma_{hi}\Delta_i.
$$

If `sigma_hi=+1`, the global row orientation is from `T_i` to `S_i`.  If
`sigma_hi=-1`, then `sigma_hi r_h` reverses the row and is again oriented from `T_i`
to `S_i`.  Hence Section 157's cut resultant has the sign-correct global form

$$
A_i u_i=\sum_h\beta_h\sigma_{hi}r_h.
$$

There is no missing orientation sign in the KKT reduction.

**Verdict:** PASS.

---

## 7. Weighted first and second variation algebra passes

Along `theta_i=t c_i`, expansion of

$$
R_{tc_i}u_i-u_i
$$

gives

$$
tc_iJu_i-{t^2c_i^2\over2}u_i+O(t^3).
$$

Thus

$$
A_h=\sum_i\sigma_{hi}c_iJu_i,
\qquad
B_h=\sum_i\sigma_{hi}c_i^2u_i.
$$

The cut resultant implies

$$
\sum_h\beta_h r_h\cdot A_h=0
$$

and

$$
\sum_h\beta_h r_h\cdot B_h=\sum_iA_i c_i^2.
$$

Therefore

$$
{1\over2}{d^2\over dt^2}
\sum_h\beta_h|r_h(t)|^2\Big|_0
=
\sum_h\beta_h|A_h|^2-\sum_iA_i c_i^2.
$$

The identity is exact.  No sign of the right side follows without additional input.

**Verdict:** PASS.

---

## 8. The two-leaf `0.206D` application is correctly weighted-to-unweighted

The current near-frontier theorem gives

$$
P_U>0.103-o(1),\qquad P_V>0.103-o(1),
$$

where each retained O--O pair weight lies in `[0,1]`.  Therefore each phase contains
strictly more than `0.103D-o(D)` distinct O--O trains.  Distinct exact phase classes
cannot contain the same train, so their union has more than `0.206D-o(D)` distinct
coordinates.

This conclusion does not assert that the two O--O families form a complete crossing
product.  The finite multishear theorem does not require such a product.

**Verdict:** PASS.

---

## 9. No false second-order optimality conclusion is imported

The old ZGS report combined its weighted curvature formula with the rejected response
claim `A_tau>w_tau`.  The present theorem does not restore that claim.

Even if the weighted quadratic form is negative in some direction, active diameter
rows may have first derivatives of both signs and the diameter max function may have a
strict cusp at the origin.  Therefore negative weighted curvature alone is not a
source-level descent certificate.

The new theorem is a coordinate and curvature **identity**, not a closure theorem.

**Verdict:** PASS.

---

## Final disposition

The finite superposition survives crossing cuts because every contact is separated by
exactly one train cut, and the signed KKT formula has the correct orientation.  The
candidate establishes a new exact source-level object:

```text
arbitrary O-O train family
  -> exact finite simultaneous contact shear
  -> signed split support for every diameter row
  -> exact KKT split-Gram curvature identity.
```

At the current two-leaf frontier this gives more than `0.206D-o(D)` simultaneous
coordinates.

**Final verdict:** PASS at proof-only scope. C-II and Level I remain open.
