> Generated reading edition · [exact source](../../../docs/reports/target_c_affine_lattice_boundary_vertex_exclusion_2026-09-11.md) · source SHA-256 `57641d938a7e3815fb9d3fd1301242130c5826113bb438c70f87d8cb4a3709b6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-563402BFA5FC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — boundary-vertex exclusion for unit-rhombic affine lattice cores

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact convex-lattice boundary theorem / C-II branch exclusion  
**Target:** Target C after C34/C65  
**Depends on:** C34 force-visible boundary count, C65 full visibility, convex perimeter-diameter inequality  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`.

The existing affine-lattice density theorem excludes every fixed lattice whose
covolume is bounded above the triangular value, but explicitly leaves open a sequence
of unit-rhombic lattices whose angle approaches `pi/3` at the boundary scale.  In the
fully force-visible C-II branch there is a stronger obstruction that does not use
packing density at all.

A convex polygon with vertices in a rank-two lattice cannot have linearly many extreme
vertices at linear diameter scale.  For the unit-rhombic lattices relevant to the
triangle-free rhombic regression, an elementary fundamental-cell count gives

$$
q=O(D^{2/3}).
$$

But C34 gives

$$
q\ge {\lceil D\rceil+2\over2}.
$$

Therefore no sufficiently large C-II force hull can have all its vertices in one
unit-rhombic affine lattice.  The conclusion is uniform as the rhombus angle tends to
`pi/3`; it removes the vanishing-strain exception left by the older affine-lattice
bulk theorem.

---

## 1. Lattice setup

Let

$$
\Lambda=\mathbb Zu+\mathbb Zv,
\qquad
|u|=|v|=1,
\qquad
\theta=\angle(u,v)\in[\pi/3,2\pi/3].
\tag{1.1}
$$

Its fundamental area is

$$
a_\Lambda=|\det(u,v)|=\sin\theta\ge {\sqrt3\over2}=:a_0.
\tag{1.2}
$$

Use the centered half-open fundamental parallelogram

$$
Q=\{su+tv:-1/2\le s,t<1/2\}.
$$

As in the existing affine-lattice audit,

$$
Q\subseteq B(0,R_\Lambda),
\qquad
R_\Lambda={1\over2}\max\{|u+v|,|u-v|\}.
$$

For `theta in [pi/3,2pi/3]`,

$$
\boxed{R_\Lambda\le {\sqrt3\over2}=:R_0.}
\tag{1.3}
$$

---

## 2. Count lattice vectors in a Euclidean disk

Let

$$
N_\Lambda(r)=|\{w\in\Lambda:|w|\le r\}|.
$$

The translates `w+Q` have disjoint interiors.  For every `|w|<=r`,

$$
w+Q\subseteq B(0,r+R_\Lambda).
$$

Therefore

$$
N_\Lambda(r)a_\Lambda
\le\pi(r+R_\Lambda)^2.
$$

Hence

$$
\boxed{
N_\Lambda(r)
\le {\pi\over a_\Lambda}(r+R_\Lambda)^2.
}
\tag{2.1}
$$

No number theory is used.

---

## 3. Convex lattice polygons have superlinear perimeter in their vertex count

Let `P` be a strictly convex polygon with `q>=3` vertices in one translate of
`Lambda`.  Write its oriented edge vectors in cyclic order as

$$
e_1,\ldots,e_q\in\Lambda\setminus\{0\}.
$$

Strict convexity implies the oriented edge directions are all distinct.  In
particular the `e_i` themselves are distinct lattice vectors.

Order their lengths as

$$
\ell_1\le\ell_2\le\cdots\le\ell_q.
$$

Since at least `j` distinct lattice vectors have length at most `ell_j`, (2.1) gives

$$
j
\le {\pi\over a_\Lambda}(\ell_j+R_\Lambda)^2.
$$

Thus

$$
\boxed{
\ell_j
\ge
\sqrt{{a_\Lambda j\over\pi}}-R_\Lambda.
}
\tag{3.1}
$$

Summing and using

$$
\sum_{j=1}^q\sqrt j
\ge\int_0^q\sqrt x\,dx
={2\over3}q^{3/2},
$$

we obtain the finite perimeter inequality

### Theorem AL.1 — convex lattice vertex/perimeter bound

$$
\boxed{
\operatorname{per}P
\ge
{2\over3}\sqrt{{a_\Lambda\over\pi}}q^{3/2}
-R_\Lambda q.
}
\tag{AL.1}
$$

For the unit-rhombic family, uniformly in `theta`,

$$
\boxed{
\operatorname{per}P
\ge
c_0q^{3/2}-R_0q,
\qquad
c_0={2\over3}\sqrt{{\sqrt3\over2\pi}},
\quad R_0={\sqrt3\over2}.
}
\tag{AL.2}
$$

This is the elementary convex-lattice-polygon mechanism usually associated with
Jarnik-type bounds, but the displayed estimate is proved here directly.

---

## 4. Diameter consequence

Every convex planar body of diameter `D` has perimeter at most `pi D`.  Hence if
`diam(P)<=D`, AL.2 gives

$$
c_0q^{3/2}-R_0q\le\pi D.
\tag{4.1}
$$

Once

$$
q\ge (2R_0/c_0)^2,
$$

the left side is at least `(c_0/2)q^(3/2)`.  Therefore

$$
\boxed{
q
\le
\left({2\pi\over c_0}D\right)^{2/3}
=O(D^{2/3}).
}
\tag{AL.3}
$$

The constant is deliberately crude; only the sublinear exponent matters.

---

## 5. C-II exclusion

Work now in the C65 fully force-visible branch.  The loaded terminal set `B_+` is
exactly the vertex set of the convex force hull `F`, and

$$
\operatorname{diam}F=D.
$$

C34 gives the exact lower bound

$$
\boxed{
q:=|B_+|
\ge {\lceil D\rceil+2\over2}.
}
\tag{5.1}
$$

Suppose the entire force-visible contact core, or merely all force-hull vertices, lies
in one translate of a unit-rhombic lattice (1.1).  Then AL.3 gives

$$
q=O(D^{2/3}),
$$

while (5.1) gives `q=Omega(D)`.  These are incompatible for sufficiently large `D`.

### Theorem AL.2 — no unit-rhombic affine-lattice C-II phase

There exists `D_0<infinity` such that no C65 fully force-visible survivor with
`D>=D_0` has its complete force-hull vertex set in a translate of a lattice

$$
\mathbb Zu+\mathbb Zv,
\qquad
|u|=|v|=1,
\qquad
\angle(u,v)\in[\pi/3,2\pi/3].
$$

A fortiori the entire positive contact core cannot be a finite subset of one such
lattice.

---

## 6. Relation to the old affine-lattice theorem

The older theorem proves, for a fixed affine lattice `Lambda`, that a global minimizer
must have

$$
a_\Lambda-\sqrt3/2=O(n^{-1/2}).
$$

Thus it excludes a fixed oblique angle but leaves the distributed-strain regime

$$
\theta_D-\pi/3=O(1/D).
$$

AL.2 is independent of that density comparison.  Its determinant lower bound remains
uniform all the way to `theta=pi/3`, so it excludes even

$$
\theta_D-\pi/3\to0
$$

at an arbitrarily fast rate, provided the force-hull vertices remain in one affine
lattice grain.

The price is different: AL.2 is C-II-specific because it uses the linear loaded-hull
vertex lower bound C34.  It does not exclude multiple grains, drifting train phases,
or a nonlattice rhombic mesh.

---

## 7. Scope and regressions

- A large triangular-lattice disk has only `O(D^{2/3})` convex lattice vertices, so it
  is correctly excluded as a C-II force hull even though it has optimal bulk density.
- The theorem does not assert that a near-rhombic contact complex lies in one lattice.
  Phase drift and multiple grains are precisely the surviving cases.
- No lower bound on KKT weights is used.
- External contact-isolated source points need not lie in the lattice and are irrelevant:
  only the force-hull vertices are used in the contradiction.
- The angle interval includes the equilateral endpoint.  Triangle-freeness is not used
  in the lattice-count proof; it enters upstream in C34/C65.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For Lambda=Zu+Zv with |u|=|v|=1 and angle in [pi/3,2pi/3],
    det Lambda >= sqrt3/2,
    centered cell radius <=sqrt3/2.
Thus the number of lattice vectors of length <=r is at most
    (pi/det Lambda)(r+R)^2.
If a strictly convex lattice polygon has q vertices, its q oriented edge vectors are
distinct.  Ordering their lengths gives
    ell_j >= sqrt(det Lambda*j/pi)-R.
Therefore
    per(P) >= (2/3)sqrt(det Lambda/pi) q^(3/2)-Rq.
Since per(P)<=pi D,
    q=O(D^(2/3)).

But C34/C65 give q>= (ceil D+2)/2 in every sufficiently large C-II survivor.
Contradiction.

Hence no sufficiently large C-II force hull can lie in one unit-rhombic affine
lattice, even if its angle approaches pi/3 at the boundary scale or faster.
```
