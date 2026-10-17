# Target C — hostile audit of Section 122 loaded-contact localization

**Date:** 2026-09-12  
**Artifact:** `research/target_c_section122_near_disk_loaded_contact_localization.md`  
**Verdict:** **PASS as a proof-only Type-II theorem.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit attacks the geometric step that turns canonical Type-II near-disk convergence
into the exact conclusion `c_B=0`.

## 1. The annulus reduction is valid

Let

\[
d_H(K,B(o,R))\le\delta<R.
\]

After translating `o=0`, the support functions satisfy

\[
|h_K(u)-R|\le\delta
\qquad(|u|=1).
\]

Thus `h_K(u)>=R-delta=:r` for every unit `u`. Since a convex body is the intersection
of its support half-planes,

\[
B(0,r)\subset K.
\]

The Hausdorff bound also gives

\[
K\subset B(0,R+\delta)=:B(0,R_+).
\]

So (122.4) is sound. In particular the origin is in the interior of `K`, radial
projection is one-to-one on `partial K`, and polar angle increases monotonically once
around the boundary.

## 2. Every boundary normal is close to the local radial direction

Let `x in partial K` and let `u` be an outward supporting unit normal at `x`. Then

\[
u\cdot x=h_K(u)\ge r,
\qquad
|x|\le R_+.
\]

Hence

\[
\cos\angle(u,x)
={u\cdot x\over|x|}
\ge {r\over R_+},
\]

so

\[
\angle(u,x)\le
\beta:=\arccos(r/R_+).
\tag{A122.1}
\]

This statement holds not only at vertices but at every point in the relative interior
of every hull side. That observation repairs the only terse point in the Section-122
writeup.

## 3. The short polar arc has total edge-direction spread at most `gamma+2 beta`

Let `p,q` be boundary vertices with `|p-q|=1`, and let `gamma` be the smaller angular
separation of their radial directions. Because `|p|,|q|>=r`,

\[
1=|p-q|
\ge2r\sin(\gamma/2),
\]

hence

\[
\gamma\le2\arcsin(1/(2r)).
\tag{A122.2}
\]

Choose the boundary arc from `p` to `q` on which polar angle runs through this shorter
angular interval. This arc exists because the origin lies in the interior and radial
projection of a convex boundary is cyclic-order preserving.

For every side on this arc, take a point `x` in its relative interior and its outward
normal `u`. The radial angle of `x` lies between the endpoint radial angles, while
(A122.1) places `u` within `beta` of that radial direction. Therefore all side normals
on the chosen arc lie in one angular interval of width at most

\[
\gamma+2\beta.
\]

Rotating by `pi/2` gives the same bound for the oriented side directions. Thus the
Section-122 estimate

\[
\tau\le
2\arccos(r/R_+)+2\arcsin(1/(2r))
\tag{A122.3}
\]

is rigorous. No appeal to smoothness or a possibly ambiguous endpoint normal cone is
needed.

## 4. The projection contradiction is exact

If `p,q` are nonconsecutive hull vertices, both boundary arcs contain at least two
sides. In particular the short polar arc from Section 3 contains side vectors
`v_1,...,v_j` with `j>=2`.

Source unit separation gives

\[
|v_i|\ge1.
\]

If `tau<2pi/3`, project onto the midpoint direction `w` of the direction interval:

\[
w\cdot(q-p)
=\sum_i w\cdot v_i
\ge j\cos(\tau/2)
\ge2\cos(\tau/2)>1.
\]

Therefore `|q-p|>1`, contradiction. The threshold is strict and the asymptotic
application has `tau->0`, so there is no equality-edge case to resolve.

## 5. The Type-II hypothesis gives the finite criterion eventually

Canonical Section 80 gives centers `o_D` with

\[
\delta_D:=d_H(F_D,B(o_D,D/2))=o(D).
\]

For

\[
r_D=D/2-\delta_D,
\qquad
R_{+,D}=D/2+\delta_D,
\]

we have

\[
r_D/R_{+,D}\to1,
\qquad
r_D\to\infty.
\]

Hence the right side of (A122.3) tends to zero. It is therefore below `2pi/3` for all
sufficiently large Type-II survivors.

Every side of `F_D` joins two source points and has length at least one. The finite
lemma applies exactly, giving

\[
|b-b'|=1,\ b,b'\in B
\Longrightarrow
b,b'\text{ consecutive on }\partial F.
\]

Thus `c_B=0` is valid.

## 6. Regression checks

- A unit hull side is allowed; one complementary boundary arc can be arbitrarily long.
- The theorem does not say that every hull side is unit.
- A nonunit hull side can still have a two-edge unit-contact detour through an unloaded
  point; Section 63's shallow-detour regression remains live.
- The theorem is only Type II. It gives no information in the macroscopic inactive-
  container branch.
- The proof uses no carrier coefficient and no post-104 quantitative theorem.
- Contact-isolated source points are retained and never placed in the Section-57
  kernel.

**Audit verdict:** Section 122 passes as a proof-only Type-II theorem. It does not close
C-II. Its exact structural contribution is the eventual identity `c_B=0`.
