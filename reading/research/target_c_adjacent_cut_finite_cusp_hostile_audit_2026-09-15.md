> Generated reading edition · [exact source](../../research/target_c_adjacent_cut_finite_cusp_hostile_audit_2026-09-15.md) · source SHA-256 `285dab6240c2b1a41372af5c914967c7af6bb94e70d8443e3230d279aa126cd2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "efbea54ada674bc46b3a383b75289f202726fe13", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_cut_finite_cusp_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4d66b6209495691b2c370a332355ed84b310bb9e3a480b863739104162041b8e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — finite-cusp reduction for the phase-close adjacent O--O pair

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_adjacent_cut_finite_cusp_reduction_2026-09-15.md`  
**Disposition:** **PASS with an explicit local-jamming warning.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate applies the exact finite multishear to the triple-small adjacent pair and chooses the two shear coefficients with the projective sign that minimizes the Euclidean difference of the two unit train vectors.  It claims that only the bounded switching set can have first diameter derivatives of order `D`, while every diameter row spanning both cuts has derivative `O(1)`.

The calculation is correct.  The audit adds one strategic warning: positive full-support KKT stationarity and mixed rigidity imply that no nonzero train-shear direction can be first-order feasible for **all** active diameter rows.  Therefore the theorem is a finite-cusp/interface reduction, not a route to an infinitesimal descent.

---

## 1. Projective orientation is handled correctly

The triple-small theorem bounds only projective angle.  The candidate does not silently identify the two oriented contact vectors.  It chooses `s in {+1,-1}` so that

$$
|u-su'|=2\sin(\eta/2)\le\eta,
$$

where `eta=d_RP1(u,u')`.  The shear coefficients are then `(1,-s)`.

This is the correct sign-invariant way to exploit projective phase closeness.

**Verdict:** PASS.

---

## 2. Consecutive interval rows have exactly the stated three types

For two adjacent coordinates of a laminar interval system, an interval contains neither coordinate, both coordinates, or exactly one.  There is no fourth pattern.

With coefficients `(1,-s)`, the first displacement coefficient is respectively

$$
0,
\qquad
J(u-su'),
\qquad
Ju\text{ or }-sJu'.
$$

Thus non-switching spanning rows have coefficient norm at most `21200/D+o(D^-1)`, while switching rows have coefficient norm one.

The switching rows are exactly those counted by the triple-small boundary theorem, so their number and total beta mass have the advertised bounds.

**Verdict:** PASS.

---

## 3. First-derivative bounds have the correct scale

For an active diameter vector `r_h`, `|r_h|=D` and

$$
L_h'(0)=2r_h\cdot A_h.
$$

Hence spanning rows satisfy

$$
|L_h'(0)|
\le2D|u-su'|
<42400+o(1).
$$

A switching row satisfies the coarse sharp-scale bound

$$
|L_h'(0)|\le2D.
$$

Multiplying the latter by the total switching beta mass `<21200/D+o(D^-1)` gives weighted absolute contribution `<42400+o(1)`.

No unsupported sign is assigned to any individual derivative.

**Verdict:** PASS.

---

## 4. The `t=xi/D` finite-amplitude scaling is safe

The exact multishear formula is trigonometric, so for fixed `xi` the Taylor derivatives of each translation increment are uniformly bounded.  A diameter vector contributes one extra factor `D` only through its dot product with the displacement.

For a spanning row, the first derivative is `O(1)` and the second Taylor coefficient is `O(D)`.  With `t=xi/D`, these contribute `O(D^-1)` to squared length.  The third and higher terms are `O(D t^3)=O(D^-2)`.

For a switching row the first derivative is `O(D)`, so the same scaling permits an `O(1)` squared-length change.  This is exactly the claimed separation of scales.

**Verdict:** PASS.

---

## 5. Local first-order descent is impossible in the selected train-shear space

This point is not a flaw in the candidate, but it is essential for downstream use.

Let `M` be the active-diameter first-derivative matrix on any selected exact train-shear coordinates.  Relative-interior KKT gives

$$
M^T\beta=0,
\qquad
\beta_h>0\text{ for every actual diameter row}.
$$

Suppose a nonzero shear direction `c` satisfied

$$
Mc\le0
$$

componentwise.  Then

$$
0=\beta^TMc.
$$

Because every `beta_h` is strictly positive and every component of `Mc` is nonpositive, every component must vanish:

$$
Mc=0.
$$

Canonical mixed infinitesimal rigidity then makes the contact-preserving motion Euclidean.  For the selected one-phase block an outside train has zero angular rate, eliminating Euclidean rotation; translation has zero train rates.  Hence `c=0`, a contradiction.

Therefore

$$
\boxed{
\text{there is no nonzero first-order diameter-feasible direction in this train-shear subspace.}
}
$$

In particular, one must not interpret the small switching beta mass as permission to ignore those active constraints.

**Verdict:** binding local-jamming regression, correctly retained.

---

## 6. Correct downstream interpretation

The finite-cusp theorem is still useful because it says a nonlocal replacement or interface theorem only needs to understand a bounded exceptional active set at one phase-close adjacent strip.  It does **not** produce a local path out of the minimizer.

A valid next theorem must therefore do one of the following:

1. construct a same-cardinality configuration directly, without requiring a diameter-feasible infinitesimal path from the current source;
2. use the finite switching set to prove an impossible diameter-thrackle/interface pattern; or
3. enlarge the move beyond exact old-contact preservation, allowing a controlled set of old contacts to break while all pair distances remain at least one.

The candidate's final paragraph is consistent with this interpretation.

**Final verdict:** PASS as a finite-cusp/interface reduction.  No local-descent claim is valid or needed. C-II and Level I remain open.
