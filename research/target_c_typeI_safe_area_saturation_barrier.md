<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "866331d34c63357095be6a2938eac75a2d854534", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_typeI_safe_area_saturation_barrier.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "cda20682b6508139c59e1ee7566dee12dc71d3c6ee487e68f5b2698b44eecb5a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — safe-area saturation barrier for every Type-I inactive region

**Date:** 2026-09-12  
**Status:** proof-only structural theorem; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The contact-wall and safe-lattice theorems identify large regions in which replacement
points are protected from the retained source. It is tempting to close Type I by
showing that those regions have enough triangular-lattice area to contain the current
isolates plus a diameter-graph vertex cover.

Lexicographic contact minimality forbids that strategy at the level of area alone.
Every protected region is already saturated in the following sharp sense:

\[
 \boxed{area(S)\le a_0 z,\qquad a_0=\sqrt3/2,}
\]

where `z` is the number of assigned contact-isolated source points. Otherwise a lattice
of spacing slightly larger than one produces `z+1` strictly separated protected
points; replacing all `z` isolates and one nonisolated positive-contact vertex gives a
same-cardinality feasible configuration with fewer contacts.

The theorem applies to

1. an internal exceptional-face contact-wall region;
2. a Section-67 hull-augmentation outer-pocket mixed-wall region; and
3. the full depth-one inner body of either Type-I macroscopic container, including the
   genuine Section-80/162 exterior cap.

It yields exact upper bounds dual to the earlier constructive lower bounds and implies
that the aggregate real area currency `Xi` is nonpositive.

---

## 1. Abstract strict-safe saturation lemma

Let `S subset int K` be a bounded measurable open set associated with an assigned set
`Z` of `z` contact-isolated source points. Assume:

1. every `y in S` is at distance **strictly greater than one** from every old source
   point outside `Z`; and
2. there exists at least one old source vertex `v notin Z` incident to a unit contact.

### Lemma 1.1 — strict-safe area saturation

\[
 \boxed{area(S)\le a_0z.}
\tag{1.1}
\]

#### Proof

Suppose instead that `area(S)>a_0z`. Choose `lambda>1` sufficiently close to one that

\[
 {area(S)\over a_0\lambda^2}>z.
\tag{1.2}
\]

Let `Lambda_lambda=lambda Lambda`, where `Lambda` is the unit triangular lattice. Its
covolume is `a_0 lambda^2` and all distinct lattice points are at distance at least
`lambda>1`.

Translation averaging over a fundamental cell gives

\[
 \mathbb E_t |(\Lambda_\lambda+t)\cap S|
 ={area(S)\over a_0\lambda^2}>z.
\]

The count is integer-valued, so some translate contains at least `z+1` points of `S`.
Choose exactly `z+1` and call the set `Y`.

Delete `Z` together with the positive-contact vertex `v`, and insert `Y`:

\[
 A':=(A\setminus(Z\cup\{v\}))\cup Y.
\tag{1.3}
\]

Cardinality is preserved. New-new distances are `>1`, and assumption 1 gives strict
new-old distances `>1`. Thus every unit contact incident to `v` is removed and no new
unit contact involving `Y` is created.

All new points lie in `int K`, so every distance involving a new point is `<D`.
Retained old-old distances are unchanged and remain at most `D`. Therefore

\[
 diam(A')\le D=D(n).
\]

Global minimality forces `diam(A')=D(n)`, so `A'` is another global minimizer of the
same cardinality. It has strictly fewer unit contacts than the lexicographically
contact-minimal representative `A`, contradiction. `square`

The argument uses contact minimality only after global diameter minimality. The
replacement need not be triangle-free.

---

## 2. Internal contact-wall region

For an internal exceptional face `C` with boundary source vertices `p_i`, define the
**strict** wall-safe region

\[
 S_\partial^\circ(C)
 :=\{y\in int C:|y-p_i|>1\ \forall i\}.
\tag{2.1}
\]

The contact-edge crossing proof strengthens immediately from `>=1` to `>1`: if an
old outside source `x` had `|x-y|<=1`, a boundary-vertex exit contradicts the strict
guard, while a proper unit-edge crossing gives distance `<=1` from one of its
endpoints, again contradicting the guard. Hence every point of
`S_partial^circ(C)` is strictly farther than one from every old source outside the
assigned isolate set.

The strict and non-strict wall-safe regions differ only by finitely many circular arcs,
so they have the same area. Lemma 1.1 gives

\[
 \boxed{area(S_\partial(C))\le a_0z_C.}
\tag{2.2}
\]

Combine this with the contact-chain lower bound

\[
 area(S_\partial(C))\ge A_C-mc_*-h_*.
\]

Using

\[
 r_\partial={A_C\over a_0}-{m\over2}+1-z_C,
\]

one obtains the exact residual ceiling

\[
 \boxed{
 r_\partial
 \le \kappa_*m+C_*,
 }
\tag{2.3}
\]

where

\[
 \kappa_*={\pi\over3\sqrt3},
 \qquad
 C_*={1\over2}+{2\pi\over3\sqrt3}.
\]

Thus the earlier sufficient condition
`r_partial>=tau(H)+kappa_*m+C_*` cannot be reached by a positive `tau(H)` in a
surviving lexicographically normalized source. The area lower bound and contact
minimality meet at exactly the same boundary coefficient.

---

## 3. Hull-augmentation outer pocket

For a Section-67 outer pocket, define the strict mixed-wall region by

\[
 dist(y,[u,v])>1,
 \qquad |y-p_i|>1
\]

for every old contact-path boundary vertex. The same exit-case proof as in the
mixed-wall theorem gives strict distance `>1` from every old source outside the
assigned pocket population.

The strict/non-strict regions again have the same area, so Lemma 1.1 gives

\[
 \boxed{area(S_{mix}(C))\le a_0z_C.}
\tag{3.1}
\]

Combining with

\[
 area(S_{mix}(C))\ge A_C-s-\ell c_*-h_*
\]

and the pocket residual `r_C` yields

\[
 \boxed{
 r_C
 \le \kappa_*\ell+\lambda_*s+\eta_*,
 }
\tag{3.2}
\]

where

\[
 \lambda_*={2\over\sqrt3}+{1\over2},
 \qquad
 \eta_*={2\pi\over3\sqrt3}-{1\over2}.
\]

Again the area-realization lower bound is sharp at the exact coefficient forced by
contact minimality; it cannot by itself produce even one guaranteed strict extra slot.

---

## 4. Full depth-one body, including the genuine exterior cap

Let `C_*` be either Type-I macroscopic container from audited-working Section 162, and
let `Z_*` be its assigned isolate population of size `z_*`. Section 162 proves that
all old sources outside `int C_*` are at distance `>1` from every point of

\[
 C_{*,-1}=\{x\in C_*:dist(x,partial C_*)>1\}.
\]

Thus Lemma 1.1 applies directly and gives

\[
 \boxed{
 area(C_{*,-1})\le a_0z_*.
 }
\tag{4.1}
\]

For the genuine exterior-cap branch, the real lattice-spare variable introduced in the
pooled theorem therefore satisfies

\[
 \boxed{
 \Psi_E={area(C_{E,-1})\over a_0}-z_E\le0.
 }
\tag{4.2}
\]

This does not say that the non-strict unit-packing capacity `M_1(C_E)` is at most
`z_E`: extra points may exist only through exact unit contacts. It says that ordinary
area averaging cannot force them.

---

## 5. Aggregate force-hull consequence

Apply (2.2) and (3.1) to every inactive chamber inside `F`. Chamber interiors are
disjoint, so

\[
 \boxed{
 area(S_F)\le a_0Z_{ch}.
 }
\tag{5.1}
\]

The aggregate safe-area theorem proves

\[
 {area(S_F)\over a_0}-Z_{ch}\ge\Xi.
\]

Therefore

\[
 \boxed{\Xi\le0.}
\tag{5.2}
\]

In the genuine exterior-cap pooled theorem,

\[
 \boxed{\Xi+\Psi_E\le0.}
\tag{5.3}
\]

Hence the purely **area-averaged** sufficient condition

\[
 \Xi+\Psi_E\ge\tau(H)>0
\]

is impossible in every surviving lexicographically contact-minimal source.

This is a route-exclusion theorem, not a contradiction with existence of a survivor.
The diameter-cover repacking theorem remains valid, but any successful proof of its
capacity hypothesis must exploit discrete exact-contact structure rather than mean
packing density alone.

---

## 6. Exact new frontier

Type I is forced into an exact-contact packing endpoint:

- the protected region cannot have triangular-lattice **area** for even one guaranteed
  strict extra point;
- any additional non-strict unit-packing slots needed to absorb the diameter cover must
  be created by exact unit contacts;
- the canonical deep near-unit isolate matching and blocker graph therefore become
  relevant again, but now with a sharper purpose: prove that the exact-contact
  saturation needed for `tau(H)` extra slots forces a unit equilateral triangle, a
  loaded-contact contradiction, or a collective strict-diameter exchange.

The theorem preserves every source point outside an explicitly cardinality-preserving
exchange and never extends the Section-57 affine-kernel theorem to contact isolates.
