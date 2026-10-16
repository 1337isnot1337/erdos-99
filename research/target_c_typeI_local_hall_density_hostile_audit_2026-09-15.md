<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ea70c4ce652879bef67e9e01ace052ca87a72637", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_typeI_local_hall_density_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c98fc4d59ce4dc9bec4459c8665b4fece1e611263f4503da2d331352809ff373"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Type-I local Hall density and multiscale near matching

**Date:** 2026-09-15  
**Audited source:** `research/target_c_typeI_local_hall_density_2026-09-15.md`  
**Verdict:** **PASS AFTER ONE LITERAL BALL-NOTATION REPAIR**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The source theorem composes the adaptive strict-safe saturation theorem with canonical C-INACTIVE-NEAR-MATCHING.  The main claim is valid: arbitrary-deletion saturation implies an exact local Hall area inequality in the protected Type-I container, and that inequality forces an `Omega(r)` matching of `1+O(1/r)` isolate pairs in every radius-`r` deep ball.

One notation point should be repaired in the source before promotion: in Section 2, take

\[
E=\overline B(x,r)
\]

rather than an unspecified/open `B(x,r)`.  This makes the distance-one witness in the definition of `N_Z(E)` literally attained.  The area and every subsequent estimate are unchanged.  Nothing else in the proof depends on open versus closed ball convention.

---

## 1. The deletion set is legal and removes no contact

The Hall neighborhood is

\[
R=N_Z(E)=\{z\in Z:\operatorname{dist}(z,E)\le1\}.
\]

The full source is finite, so `R` is finite.  Every member of the assigned set `Z` is an actual contact isolate in the canonical Type-I representative.  Hence

\[
E_C(R)=\varnothing.
\]

This is exactly the first branch of Theorem AS.1, not the stronger deleted-contact branch.  The source theorem uses the correct coefficient

\[
\operatorname{area}E\le a_0|R|.
\]

There is no hidden deletion of a boundary/core contact.

**Result:** PASS.

---

## 2. Strict safety relative to `R` is exact

Take `y in E subset C_{-1}`.

- If `z in Z\setminus R`, then `dist(z,E)>1`; in particular `|y-z|>1`.
- Every source point outside the assigned set `Z` lies outside `int C` in the audited Type-I container decomposition.
- Since `dist(y,partial C)>1`, the segment from `y` to any such outside point exits `C` only after length strictly greater than one.  Therefore that source point is strictly farther than one from `y`.

Thus every `y in E` satisfies

\[
|y-a|>1\qquad(a\in A\setminus R),
\]

which is precisely AS.3.

The argument works for the internal chamber and for the exterior cap because the audited Type-I unification theorem gives the same assigned-source / outside-interior separation property and fixed-depth protection for both.

**Result:** PASS.

---

## 3. Local Hall inequality is genuinely stronger than unit covering

AS.1 therefore gives

\[
\operatorname{area}E\le a_0|N_Z(E)|.
\]

This is not merely the old covering statement `C_{-1} subset union B(z,1)`.  Ordinary unit-disk covering would only imply the crude area-count coefficient `pi`; the new inequality has the optimal packing-cell coefficient

\[
a_0={\sqrt3\over2}.
\]

The theorem does not reverse Oler or assert a packing extension.  It is a neighborhood-expansion inequality forced by lexicographic source minimality.

**Result:** PASS.

---

## 4. Ball population floor

Assume

\[
x\in C_{-(r+1)}.
\]

With the literal repair

\[
E=\overline B(x,r),
\]

one has `E subset C_{-1}`.  If `z in N_Z(E)`, compactness of the closed ball gives `y in E` with `|z-y|<=1`, hence

\[
|z-x|\le r+1.
\]

Therefore

\[
N_Z(E)\subseteq Z\cap\overline B(x,r+1).
\]

The Hall inequality gives

\[
\pi r^2
\le a_0|N_Z(E)|
\le a_0|Z\cap\overline B(x,r+1)|,
\]

which is exactly the claimed local count floor.

No point outside the radius-`r+1` disk is silently counted.

**Result:** PASS AFTER THE CLOSED-BALL WORDING REPAIR.

---

## 5. The local Oler slack calculation has the correct sign

Let

\[
n_r=|Z\cap\overline B(x,r+1)|.
\]

For the radius-`r+1` disk, finite Oler gives the nonnegative slack

\[
\sigma_r
={\pi(r+1)^2\over a_0}+\pi(r+1)+1-n_r.
\]

The Hall count floor gives a **lower** bound on `n_r`, hence the required **upper** bound

\[
\sigma_r
\le
{\pi(2r+1)\over a_0}+\pi(r+1)+1.
\]

The direction is correct.  No Oler upper bound is reversed into a capacity lower bound.

**Result:** PASS.

---

## 6. Canonical Section 81 is in scope locally

C-INACTIVE-NEAR-MATCHING is stated for any convex body containing a specified contact-isolated set.  It does not require the convex body to be one of the canonical chambers or to contain every chamber isolate.

The pair

\[
\left(\overline B(x,r+1),\ Z\cap\overline B(x,r+1)\right)
\]

therefore satisfies its hypotheses exactly.  The selected points remain contact-isolated in the full source, so every near-contact edge produced by Section 81 has old length strictly greater than one.

**Result:** PASS.

---

## 7. The `r>=4` matching constant is algebraically correct

For

\[
\epsilon={4\over r},
\qquad r\ge4,
\]

canonical Section 81 gives

\[
\nu_{4/r}
\ge
{3\pi(r+1)^2\over2a_0r}
-
{1\over2}
\left(
{\pi(2r+1)\over a_0}+\pi(r+1)+1
\right).
\]

Define

\[
c_H={\pi(1-a_0)\over2a_0}.
\]

Subtracting `c_H r` gives exactly

\[
{5\pi\over2a_0}
-{\pi\over2}
-{1\over2}
+{3\pi\over2a_0r},
\]

which is strictly positive because `a_0<1`.  Numerically

\[
c_H=0.243003037439\ldots.
\]

Thus

\[
\nu_{4/r}\ge c_Hr
\]

for every real `r>=4`.  The use of the Section-81 small-scale estimate is legal because `4/r<=1`.

**Result:** PASS.

---

## 8. Scope and non-conclusions

The source theorem correctly does **not** claim:

- an exact new unit contact;
- an exact equilateral triangle;
- a protected extra packing slot;
- a coherent triangular-lattice phase;
- a uniform positive packing-density gap; or
- C-II closure.

A slowly sheared near-triangular packing with strain on the order of `1/r` remains a live local regression.  The theorem removes mesoscopic low-density holes; it does not yet remove inverse-scale shear.

The useful new normal form is instead

```text
for every protected scale r >= 4:
    every radius-r deep ball
      has triangular-density population up to O(r) boundary error
      and contains Omega(r) disjoint 1+O(1/r) isolate pairs.
```

This is a legitimate strengthening of the Type-I packing endpoint and is independent of the parallel Type-II scalar work.

---

## Final disposition

**PASS AFTER ONE NOTATION REPAIR.**  Replace the Section-2 test ball by the closed ball `overline B(x,r)`.  After that literal edit, the local Hall inequality, local Oler-slack bound, and explicit multiscale matching constant are all valid at the stated proof-only scope.

C-II and Level I remain open.
