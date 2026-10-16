# Hostile audit — Target C Section 122 finite exchange saturation

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Lifecycle:** proof-only hostile audit on the research branch; no theorem-state promotion.  
**Audited files:**

- `research/target_c_section122_finite_exchange_saturation.md`;
- `research/target_c_section122_loaded_exchange_companion.md`.

## 1. Disposition

The finite exchange theorem and its loaded lexicographic strengthening are valid at the scopes stated in the source files.

The audit does **not** certify a C-II closure.  The macroscopic internal inactive-chamber branch is reduced to a finite packing obligation that is still open: produce a protected density-increasing repacking whose local unit-contact budget fits the deleted-core contact budget.

The principal result that survives hostile review is:

> In the contact-minimal, then diameter-pair-minimal triangle-free global representative, deletion of one loaded nonisolated core vertex can fund one additional chamber point.  Any protected replacement with no more new unit contacts than the deleted loaded vertex had, and with no unit triangle, contradicts the lexicographic normalization.  More generally, finitely many deleted core vertices fund the same number of additional chamber points with the corresponding lost-contact budget.

No isolated source point is discarded.  Every comparison preserves total cardinality.

---

## 2. Audit of Theorem 122.1

The proposed competitor is

\[
A'=(A\setminus(Z\cup\{v\}))\cup Y,
\qquad |Y|=|Z|+1,
\]

where `Z` consists of contact-isolated source points, `v` is nonisolated, and every new pair involving `Y` is strictly longer than one.

### 2.1 Cardinality

Exactly `|Z|+1` old points are removed and exactly `|Z|+1` new points are inserted.  Hence `|A'|=|A|`.  There is no hidden deletion of contact-isolated points.

### 2.2 Unit separation

Retained old pairs remain unit-separated.  The hypotheses give strict separation for every pair involving `Y`.  Therefore `A'` is unit-separated.

### 2.3 Diameter

All new points lie in `K=conv A`, and all retained old points also lie in `K`.  Since

\[
\operatorname{diam}(K)=\operatorname{diam}(A)=D(n),
\]

we have `diam A'<=D(n)`.  The definition of `D(n)` gives the reverse inequality for every unit-separated `n`-point set.  Hence `diam A'=D(n)`.

This step is exact; no assumption about a surviving old diameter pair is needed.

### 2.4 Contact count

Deleting `Z` removes no unit contacts because every point of `Z` is contact-isolated.  Deleting `v` removes at least one unit contact.  Strict separation of `Y` creates none.  Thus the contact count drops strictly.

### 2.5 Triangle-free comparison class

Since the new points have no unit contacts, they cannot lie in a unit-contact triangle.  Retained old contacts remain a subgraph of the original triangle-free contact graph.  Thus the competitor belongs to the same triangle-free global-minimizer comparison class.

**Verdict:** Theorem 122.1 is valid.

---

## 3. Audit of the chamber corollaries

Canonical Section 77 partitions inactive source points among actual convex inactive chambers.  For a chamber `C` and its assigned isolate set `Z_C`, every source point not assigned to `C` lies outside `int C` (boundary points are allowed on `partial C`).

If

\[
x\in C_{-1}
=\{x\in C:\operatorname{dist}(x,\partial C)>1\},
\]

and `a` is outside `int C`, convexity implies that the segment `xa` meets `partial C`.  Therefore

\[
|x-a|\ge\operatorname{dist}(x,\partial C)>1.
\]

This supplies automatic compatibility with every source point outside the chamber's assigned isolate set.

Consequently:

\[
C_{-1}\subseteq\bigcup_{z\in Z_C}\overline B(z,1)
\]

is valid, and the finite strict `k -> k+1` exchange obstruction inside `C_{-1}` follows directly from Theorem 122.1.

For the macroscopic chamber `C_*`, canonical Sections 79 and 87 give `area(C_*)=Omega(D^2)`, `per(C_*)=O(D)`, positive linear inradius, quadratic isolate population, and the deep inverse-diameter near-pair matching.  A fixed-width erosion removes only `O(D)` area by convex coarea/perimeter monotonicity, so `(C_*)_{-1}` still has quadratic area.

**Verdict:** Corollaries 122.2--122.4 are valid for actual internal inactive chambers.  They do not cover the separate exterior-source-cap branch.

---

## 4. Audit of the loaded companion

The companion uses the second lexicographic normalization.  Let `v` have both contact degree `d_C(v)>=1` and diameter degree `d_H(v)>=1`.  Let `Y subset int K` replace `Z union {v}` while preserving cardinality.  The competitor is assumed unit-separated and triangle-free, but it may create unit contacts.

Let `c_new` count every unit-contact edge of the competitor incident to at least one new point.

Because the deleted isolates have contact degree zero,

\[
|C(A')|=|C(A)|-d_C(v)+c_{new}.
\]

Thus `c_new<d_C(v)` contradicts contact minimality.

If `c_new=d_C(v)`, the contact count is unchanged.  The only additional point requiring audit is the claim that `Y subset int K` creates no diameter pair.

Fix `y in int K` and `x in K`.  Since `diam K=D`,

\[
K\subseteq\overline B(x,D).
\]

If `|y-x|=D`, then `y` lies on the boundary circle of that disk.  Every Euclidean neighborhood of `y` contains points outside the disk, contradicting the existence of a neighborhood contained in `K`.  Hence

\[
|y-x|<D
\qquad(y\in int K,\ x\in K).
\]

Therefore no new point creates an actual diameter pair.  Deleting the loaded vertex removes at least one old diameter pair, and deleting isolates can only remove additional diameter pairs.  So the diameter-pair count drops strictly.  This contradicts the second lexicographic minimization.

The argument requires `K` to have nonempty planar interior.  That holds in the post-ZF C-II regime and is explicitly assumed in the companion theorem.

**Verdict:** Theorem 122C.1 is valid.

---

## 5. Multi-vertex extension

For finite deleted core set `U`, define

\[
c_{lost}=\#\{e\in C(A):e\cap U\ne\varnothing\},
\]

so contacts internal to `U` are counted once, not twice.  Define `h_lost` analogously for diameter pairs incident to `U union Z`.

A replacement `Y subset int K` with the same total cardinality and `c_new<=c_lost` has contact count no larger than the original.  Strict inequality contradicts contact minimality.  Equality plus `h_lost>0` contradicts diameter-pair minimality because `Y` creates no diameter pairs.

**Verdict:** the multi-vertex extension is valid as stated.

---

## 6. Adversarial failure tests

### 6.1 New contacts at equality

The base theorem cannot allow a new unit contact: contact count might fail to decrease.  The loaded companion repairs exactly this by using diameter-pair minimality when the new-contact count equals the lost-contact count.

### 6.2 New unit triangle

A replacement that creates a unit triangle is not eligible for the lexicographic comparison class.  The companion therefore explicitly requires the resulting unit-contact graph to remain triangle-free.  No implication from a triangle in the *competitor* to a triangle in the original source is asserted.

### 6.3 Replacement on `partial K`

A point on the source-hull boundary can participate in a new diameter pair.  The loaded companion correctly restricts `Y` to `int K`.  For an internal positive-area chamber, every point of `C_{-1}` lies in `int C subset int K`, so the chamber corollary meets this condition.

### 6.4 Removing all old diameter pairs

If the deleted vertices hit every old diameter pair, the new interior points create none, so the proposed competitor would have diameter strictly below `D`.  That is already impossible by global minimality.  The proof does not require a surviving old diameter pair.

### 6.5 Quantitative gap size

Neither theorem supplies a lower bound on the strict pairwise gaps between isolates.  A sequence may have minimum excess gap much smaller than `1/D`.  Therefore no bounded-support Kuperberg-type exchange follows merely from strictness and the Section-87 upper bound `1+O(1/D)` on selected near-pairs.

### 6.6 Standard complete saturation terminology

The base file defines its own finite exchange property.  It does not import a stronger theorem from infinite-packing saturation theory.  This avoids a terminology-based overclaim.

---

## 7. Exact remaining inactive-branch obligation

After this audit, Section 95 is no longer the immediate obstruction for an internal macroscopic inactive chamber.  It is enough to prove one of the following source-local statements inside the protected interior:

1. a finite strict `k -> k+1` repacking;
2. more generally, a finite triangle-free `k -> k+1` repacking creating at most `d_C(v)` new unit contacts for one deleted loaded core vertex `v`; or
3. the corresponding `k -> k+r` repacking with new-contact count at most the contacts lost from a finite deleted loaded/core set.

The canonical Section-77 `O(D)` Oler slack and Section-87 inverse-diameter near-pair matching do not yet imply any of these.  The missing theorem must be scale-free, or must derive additional lattice-phase / quantitative-gap information.

The exterior-cap branch also remains separate.

---

## 8. Lifecycle

**Proof status:** passes this hostile audit.  
**Canonical status:** noncanonical / proof-only.  
**C-II:** open.  
**Manifest mutation:** none.
