<!-- migration-source: path=docs/reports/target_c_low_diameter_prestress_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=281ebfb039db70f7cb9e5ba82607f55f3ce35ebd; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C addendum: low-diameter prestress and rattler dichotomy

**Date:** 2026-08-31  
**Repository state:** `research/target-c-low-diameter-prestress-2026-08-31`  
**Run type:** proof / structural reduction / literature cross-check  
**Target:** canonical Target C, Gates C-I and C-II  
**Depends on:** Target C Theorems C3–C4, C6–C7, C11–C13, C18–C19; canonical Oler/Fejes Tóth and planar diameter-graph facts  
**External cross-check:** R. Connelly, *Questions, Conjectures and Remarks on Globally Rigid Tensegrities* (2009), Lemma 21 and Theorem 22. The proofs below do not depend on this source.

## LEVEL I STATUS

`STILL OPEN`

This addendum isolates the entire Target C phase in which the maximal KKT diameter
support has at most two edges.

The central new fact is self-contained: every normalized KKT stress with at most two
positive diameter edges has a positive-semidefinite signed stress matrix.  For two
positive diameter edges the scalar kernel is exactly the affine three-space
`span{1,x,y}`.  The proof uses the already-canonical contact-network Dirichlet response
C11 and a four-boundary-point Schur-complement argument; it does **not** assume a
general KKT PSD principle.

Combining this special PSD theorem with direction-dependent second-order optimality
C13 forces the whole fixed-diameter critical-cone span into the kernel of one extreme
KKT stress.  Hence a weak-contact survivor with `|H_*|=2` has only two exceptional
forms:

1. a one-diameter extreme stress is the exact full-D straight unit chain and controls
   the critical cone on that chain; or
2. a two-diameter extreme stress controls the critical cone affinely and every stressed
   contact of that extreme stress is parallel to one of the two diameter directions.

There is no generic many-direction two-diameter shear phase.

Independently, `|H_*|=2` forces the force hull to have at most four vertices and area
at most `D^2/2`.  In the fully force-visible branch this makes a two-diameter source
macroscopically rattler dominated: at least

\[
\frac{\pi-2}{2\sqrt3}D^2-\frac\pi2D-1
=0.3295\ldots D^2-O(D)
\]

source points are contact-isolated.

These are structural reductions, not a Level I proof.

---

## 1. Signed KKT stress matrix

Fix a normalized KKT stress `s=(alpha,beta)` and write

\[
C_s=\{ij:\alpha_{ij}>0\},
\qquad
H_s=\{ij:\beta_{ij}>0\}.
\]

Let

\[
V_s=V(C_s).
\]

Every endpoint of `H_s` lies in `V_s` by canonical Lemma 5.2.  Define the signed
stress matrix

\[
\boxed{
\Omega_s=L_C(\alpha)-L_H(\beta)
}
\tag{C20.1}
\]

on `V_s`.  Vertex equilibrium gives

\[
\boxed{
\Omega_s\mathbf1=0,
\qquad
\Omega_s x=0,
\qquad
\Omega_s y=0.
}
\tag{C20.2}
\]

For a scalar field `z` on `V_s`,

\[
\boxed{
z^{\mathsf T}\Omega_s z
=\sum_{ij\in C_s}\alpha_{ij}(z_i-z_j)^2
-\sum_{ij\in H_s}\beta_{ij}(z_i-z_j)^2.
}
\tag{C20.3}
\]

For a planar velocity field `v`, summing the two scalar-coordinate energies gives

\[
\boxed{
\operatorname{tr}(V^{\mathsf T}\Omega_sV)
=\sum_{C_s}\alpha_{ij}|v_i-v_j|^2
-\sum_{H_s}\beta_{ij}|v_i-v_j|^2.
}
\tag{C20.4}
\]

The sign pattern is the artificial tensegrity sign convention with positive contacts
and negative diameter members.  It is used only as a matrix object.  It is not the
physical cable/strut orientation of the original packing constraints.

---

## 2. Dirichlet reduction of one fixed KKT stress

Let

\[
B=B_s:=V(H_s),
\qquad
I=V_s\setminus B.
\]

Target C12 says `C_s` is connected.  Regard every contact `ij in C_s` as an electrical
edge of conductance `alpha_ij`.  Let `L_C` be its weighted Laplacian and let

\[
\Lambda
=L_C[B,B]-L_C[B,I]L_C[I,I]^{-1}L_C[I,B]
\tag{C20.5}
\]

be the boundary response matrix.  The Dirichlet block `L_C[I,I]` is positive definite
because `C_s` is connected and `B` is nonempty.

Let `L_H` be the beta-weighted Laplacian of `H_s` on `B`.  Canonical C11 gives

\[
\boxed{
M:=\Lambda-L_H,
\qquad
M\mathbf1=0,
\qquad
MP_B=0.
}
\tag{C20.6}
\]

The full signed matrix has block form

\[
\Omega_s=
\begin{pmatrix}
L_C[B,B]-L_H & L_C[B,I]\\
L_C[I,B] & L_C[I,I]
\end{pmatrix}.
\tag{C20.7}
\]

Eliminating the interior block by an invertible block congruence gives

\[
\boxed{
\Omega_s
\sim_{\rm cong}
M\oplus L_C[I,I].
}
\tag{C20.8}
\]

Hence the inertia of `Omega_s` is the inertia of `M` plus a positive-definite block.
All possible indefiniteness is therefore concentrated in the at-most-four-dimensional
boundary matrix `M` when `|H_s|<=2`.

Two standard electrical facts will be used:

1. `Lambda` is a Laplacian/M-matrix, so
   \[
   \Lambda_{ij}\le0\qquad(i\ne j);
   \tag{C20.9}
   \]
2. because `C_s` is connected, the response matrix has
   \[
   \ker\Lambda=\operatorname{span}\{\mathbf1\}.
   \tag{C20.10}
   \]

Both follow directly from Kron reduction of a connected positive-conductance graph.

---

## 3. One positive diameter edge

### Lemma C20.1 (one-diameter PSD chain)

If `|H_s|=1`, then `D` is an integer, the positive contact support is the exact straight
unit chain

\[
p_k=p_0+ku,
\qquad k=0,1,\ldots,D,
\qquad |u|=1,
\tag{C20.11}
\]

joining the unique positive diameter pair.  Every chain contact has weight `alpha=D`,
and

\[
\boxed{
\Omega_s\succeq0.
}
\tag{C20.12}
\]

Its scalar kernel is exactly the two-dimensional space of affine functions along the
chain.

#### Proof

Target C3 gives

\[
\operatorname{conv}V(C_s)=\operatorname{conv}B,
\]

and now `B` consists of the two endpoints of the unique positive diameter edge.  Since
`C_s` is connected by C12, every positive-contact vertex lies on the diameter segment
and the contact graph contains a unit-step path between the endpoints.  Unit separation
forces the sorted gaps to be exactly one.  Thus (C20.11) holds and `D` is an integer.

The normalized diameter weight is one.  Endpoint equilibrium gives the first chain
weight `D`, and interior equilibrium propagates the same weight along the chain.

For any scalar field `z`, put `d_k=z_k-z_{k-1}`.  Then

\[
\begin{aligned}
z^{\mathsf T}\Omega_s z
&=D\sum_{k=1}^D d_k^2-(z_D-z_0)^2\\
&=D\sum_{k=1}^D d_k^2-\left(\sum_{k=1}^D d_k\right)^2\\
&\ge0
\end{aligned}
\tag{C20.13}
\]

by Cauchy–Schwarz, with equality exactly when all `d_k` are equal. `square`

The same conclusion is visible directly from (C20.8): here `B` has two vertices and
C11 forces `Lambda=L_H`, so `M=0`.

---

## 4. Two positive diameter edges: self-contained PSD theorem

Two distinct diameter segments in one planar set of diameter `D` cannot be collinear:
a line contains at most one unordered pair of points at mutual distance `D`.  Thus two
distinct members of `H_s` determine two different directions.

There are two cases.

### 4.1 The two diameter edges share an endpoint

Then `B` has three vertices.  Since the two diameter directions are distinct, those
three points are noncollinear.  Therefore the restrictions of

\[
\mathbf1,x,y
\]

to `B` form a basis of `R^B`.  But `M` annihilates all three by (C20.6).  Hence

\[
\boxed{M=0.}
\tag{C20.14}
\]

By (C20.8), `Omega_s` is PSD and its scalar nullity is exactly three.

### 4.2 The two diameter edges are disjoint

Then `B` has four vertices.  Every point of `B` is a diameter endpoint and therefore a
vertex of `conv B`.  Distinct planar diameter segments intersect, so in the cyclic
order

\[
b_1,b_2,b_3,b_4
\]

the two members of `H_s` are the crossing diagonals

\[
b_1b_3,
\qquad
b_2b_4.
\tag{C20.15}
\]

The three affine boundary vectors `1,x,y` are independent, and `M` annihilates them.
Thus

\[
\operatorname{rank}M\le1.
\tag{C20.16}
\]

Let `a` span the one-dimensional orthogonal complement of the affine data:

\[
a\perp\mathbf1,x,y.
\tag{C20.17}
\]

For a strictly convex quadrilateral the unique affine dependence has alternating signs
around the cyclic order.  After multiplying by `-1` if necessary,

\[
a_1,a_3>0,
\qquad
a_2,a_4<0.
\tag{C20.18}
\]

Therefore for every boundary-adjacent pair,

\[
a_i a_{i+1}<0.
\tag{C20.19}
\]

Because `M` is symmetric and has image contained in `span{a}`, there is a scalar
`lambda` with

\[
M=\lambda aa^{\mathsf T}.
\tag{C20.20}
\]

For adjacent boundary vertices there is no diameter edge, so

\[
M_{i,i+1}=\Lambda_{i,i+1}\le0.
\tag{C20.21}
\]

Together with (C20.19)–(C20.20), this forces

\[
\lambda\ge0.
\tag{C20.22}
\]

In fact `lambda>0`.  If `lambda=0`, then `M=0`, so `Lambda=L_H`.  But `L_H` is the
Laplacian of two disjoint edges and has a two-dimensional kernel, whereas connectedness
of `C_s` gives `ker Lambda=span{1}` by (C20.10).  Contradiction.

Thus

\[
\boxed{M\succeq0,
\qquad
\operatorname{rank}M=1.}
\tag{C20.23}
\]

The congruence (C20.8) now yields the main theorem.

### Theorem C20 (low-diameter KKT prestress)

For every normalized KKT stress `s`, if

\[
|H_s|\le2,
\]

then

\[
\boxed{
\Omega_s\succeq0.
}
\tag{C20.24}
\]

If `|H_s|=2`, then

\[
\boxed{
\operatorname{rank}\Omega_s=|V_s|-3,
\qquad
\ker\Omega_s=\operatorname{span}\{\mathbf1,x,y\}.
}
\tag{C20.25}
\]

#### Literature cross-check

Connelly's 2009 Lemma 21 proves the same maximal-rank conclusion for a planar strict
proper stress with exactly two non-collinear negative members, and the eigenvalue
interpolation in the proof of Theorem 22 proves positive semidefiniteness before the
additional third-direction hypothesis is used to exclude an affine flex.  This is an
independent cross-check of C20, not a dependency of the proof above.

### Scope warning

C20 does **not** say arbitrary KKT stress matrices are PSD.  The proof collapses the
boundary Schur complement to dimension at most four and uses the special crossing
pattern of exactly two diameter edges.  With three or more positive diameter edges,
`M` has higher rank and no analogous sign conclusion has been proved.

---

## 5. Second-order optimality plus PSD gives a finite kernel cover

Let `S(A)` be the normalized KKT polytope with extreme stresses

\[
s_1,\ldots,s_M.
\]

Assume the maximal positive diameter support satisfies

\[
|H_*|\le2.
\tag{C21.1}
\]

Then every normalized KKT stress has at most two positive diameter edges, so C20 applies
to every point of the polytope.

Embed each `Omega_s` on the full source vertex set by zero rows and columns outside its
positive support.  Define

\[
L:=\operatorname{span}\mathcal K_D(A).
\tag{C21.2}
\]

### Theorem C21 (critical-cone kernel-face theorem)

There exists an extreme normalized KKT stress `s_0` such that

\[
\boxed{
L\subseteq\ker(\Omega_{s_0}\otimes I_2)
}
\tag{C21.3}
\]

in the full-space embedding.  Equivalently, every critical velocity restricts to the
vector-valued stress kernel on `V_{s_0}`.

#### Proof

Fix `v in K_D(A)`.  Target C13.3 supplies a normalized KKT stress `s` for which

\[
\sum_{H_s}\beta_h|dv_h|^2
-
\sum_{C_s}\alpha_c|dv_c|^2
\ge0.
\tag{C21.4}
\]

By (C20.4),

\[
\operatorname{tr}(V^{\mathsf T}\Omega_sV)\le0.
\tag{C21.5}
\]

C20 gives `Omega_s succeq0`, so the same quadratic form is nonnegative.  It must be
zero, and therefore

\[
v\in\ker(\Omega_s\otimes I_2).
\tag{C21.6}
\]

Write

\[
s=\sum_j t_js_j,
\qquad
t_j\ge0,
\qquad
\sum_jt_j=1.
\]

Stress matrices depend linearly on the multipliers:

\[
\Omega_s=\sum_jt_j\Omega_{s_j}.
\]

Every summand is PSD.  Since the total quadratic energy of `v` is zero, every summand
with `t_j>0` also has zero energy on `v`.  Hence `v` lies in the kernel of at least one
extreme stress.

Thus

\[
\mathcal K_D(A)
\subseteq
\bigcup_{j=1}^M\ker(\Omega_{s_j}\otimes I_2).
\tag{C21.7}
\]

The relative interior of `K_D(A)` is nonempty in its span `L`.  A finite union of
proper linear subspaces of `L` cannot contain a relatively open subset of `L`.
Therefore at least one of the kernel subspaces in (C21.7) contains all of `L`, proving
(C21.3). `square`

This is stronger than a direction-by-direction second-order certificate: one extreme
KKT stress controls the complete linear span of all fixed-diameter critical motions.

---

## 6. Third-direction collapse for a two-diameter controlling stress

Assume now

\[
|H_*|=2
\tag{C21.8}
\]

and let `s_0` be supplied by C21.

If `s_0` uses both positive diameter edges, C20.25 implies every critical velocity on
`V_{s_0}` is affine:

\[
\boxed{
v_i=A_vp_i+t_v.
}
\tag{C21.9}
\]

Every member of `s_0` is strong, so its radial first variation is zero for every
critical velocity.  Put

\[
S_v=\frac{A_v+A_v^{\mathsf T}}2.
\]

For every stressed member direction `r`,

\[
\boxed{
r^{\mathsf T}S_vr=0.}
\tag{C21.10}
\]

A nonzero homogeneous quadratic form in two variables has at most two real projective
zero directions.  The two diameter chords already supply two distinct directions.
Therefore:

### Corollary C21.1 (third-direction collapse)

If `s_0` has any positive contact whose direction is not parallel to either positive
diameter chord, then

\[
S_v=0
\]

for every `v in K_D(A)`.  Hence every critical velocity is an infinitesimal Euclidean
motion on `V_{s_0}`, and the two members of `H_*` have one common angular rate.

For a contact-minimal triangle-free source with a weak unit contact, choose the strict
weak-release velocity supplied by C6.  Since `H_*` consists of exactly these two
chords, the common-angular-rate conclusion invokes C7 and integrates the release to a
finite same-D motion deleting the weak contact.  This contradicts contact minimality.

Consequently a weak-contact survivor with `|H_*|=2` and a kernel-controlling extreme
stress using both diameter edges must satisfy

\[
\boxed{
\text{every positive contact of }s_0
\text{ is parallel to one of the two diameter directions.}
}
\tag{C21.11}
\]

This is the exact two-direction affine-shear exception.

### The other exceptional phase

C21 does not force the controlling extreme stress to use both elements of `H_*`.  It
may use one diameter edge.  Then C20.1 says its positive support is the exact full-D
straight unit chain, and every critical velocity restricts to an affine motion of that
chain.

Hence every weak-contact source with `|H_*|=2` is reduced to one of two mechanisms:

1. **chain-kernel phase:** a one-diameter extreme stress is the full straight unit chain
   and its vector kernel contains the critical-cone span;
2. **two-direction phase:** a two-diameter extreme stress has affine kernel and all of
   its positive contacts lie in the two diameter directions.

No many-direction two-diameter phase survives.

---

## 7. A source-wide reaction disk

There is also a new convex identity valid for every normalized KKT stress, independent
of the low-support hypothesis.

For `b in B_+`, define

\[
s_b=\sum_{bk\in H_+}\beta_{bk},
\qquad
c_b=\frac1{s_b}\sum_{bk\in H_+}\beta_{bk}k.
\tag{C22.1}
\]

Then

\[
g_b=s_b(b-c_b).
\tag{C22.2}
\]

### Theorem C22 (reaction-center disk)

For every `x in conv A`,

\[
\boxed{
|x-c_b|\le|b-c_b|.
}
\tag{C22.3}
\]

Thus the entire source hull lies in the disk centered at the beta-weighted barycenter
of the positive diameter partners of `b` and passing through `b`.

Moreover

\[
\boxed{
P_*=\sum_b s_b|b-c_b|,
\qquad
\sum_b s_b=2.
}
\tag{C22.4}
\]

#### Proof

C5 gives, for every positive diameter partner `k` and every `x in conv A`,

\[
(b-k)\cdot(b-x)\ge\frac{|b-x|^2}{2}.
\]

Multiply by `beta_bk`, sum over the positive diameter partners, and divide by `s_b`:

\[
(b-c_b)\cdot(b-x)\ge\frac{|b-x|^2}{2}.
\]

Expanding

\[
|x-c_b|^2=|(b-c_b)-(b-x)|^2
\]

proves (C22.3).  Equation (C22.4) follows from `g_b=s_b(b-c_b)`, the reciprocal
perimeter definition, and double-counting the normalized beta weights. `square`

Summing the undivided inequality over `b` also gives

\[
\boxed{
\sum_b s_b|b-x|^2\le2D^2
\qquad(x\in\operatorname{conv}A).
}
\tag{C22.5}
\]

The reaction disks are exact but do not by themselves improve C18: averaging the
partners loses the endpoint-by-endpoint intersection information present in the exact
three-disk container.

---

## 8. Two maximal diameter edges force a macroscopic rattler population in C-II

Assume the fully force-visible branch

\[
C=C_*
\tag{C23.1}
\]

and

\[
|H_*|=2.
\tag{C23.2}
\]

Target C4 gives

\[
F=\operatorname{conv}V(C_*)=\operatorname{conv}B_*.
\tag{C23.3}
\]

The endpoint set `B_*` has at most four points, so `F` is a triangle or quadrilateral.
Its diameter is `D`.

### Lemma C23.1 (four-vertex force-hull area)

\[
\boxed{
\operatorname{area}F\le\frac{D^2}{2}.}
\tag{C23.4}
\]

#### Proof

For a convex quadrilateral, area equals one half the absolute cross product of the two
diagonal vectors, so it is at most one half the product of their lengths, each at most
`D`.  For a triangle, the sharp diameter-D area bound is `sqrt(3)D^2/4<D^2/2`.
`square`

Oler's finite packing inequality applied to the unit-separated set `V(C_*)` gives

\[
|V(C_*)|
\le
\frac{\operatorname{area}F}{\sqrt3/2}
+\frac{\operatorname{per}F}{2}+1.
\]

Together with (C23.4) and `per(F)<=pi D`,

\[
\boxed{
|V(C_*)|
\le
\frac{D^2}{\sqrt3}+\frac\pi2D+1.
}
\tag{C23.5}
\]

Global minimum-diameter optimality gives

\[
D^2<\frac n{\Delta_2},
\qquad
\Delta_2=\frac\pi{2\sqrt3},
\]

hence

\[
\boxed{
n>\frac\pi{2\sqrt3}D^2.}
\tag{C23.6}
\]

### Theorem C23 (two-diameter rattler lower bound)

Let `z` be the number of contact-isolated source points.  Under (C23.1)–(C23.2),

\[
\boxed{
z
\ge
\frac{\pi-2}{2\sqrt3}D^2
-\frac\pi2D-1.}
\tag{C23.7}
\]

In particular

\[
z=(0.3295\ldots)D^2-O(D)=\Omega(n).
\tag{C23.8}
\]

#### Proof

Every point outside `V(C_*)` is contact-isolated when `C=C_*`: any unit contact
incident to it would itself belong to `C_*` and place the point in `V(C_*)`.  Therefore

\[
z\ge n-|V(C_*)|,
\]

and (C23.7) follows by subtracting (C23.5) from (C23.6). `square`

Thus a fully force-visible source with only two supported diameter edges cannot have a
force-carrying bulk.  It must coexist with a positive-density KKT-invisible population.

---

## 9. Why the fixed affine-lattice theorem does not close C21.11

The repository's fixed affine-lattice exclusion says that an **entire** sufficiently
large global minimizer cannot lie in one fixed affine lattice whose covolume is
strictly greater than `sqrt(3)/2`.

C21.11 is weaker: it constrains only the positive support of one extreme KKT stress.
Other strong vertices can be absent from that stress, and C23 shows that in C-II a
linear number of contact-isolated points may lie outside the force-visible support.
Thus the fixed-lattice theorem cannot be imported as a closure without a new
support-to-source propagation theorem.

A valid next step must either propagate the two-direction affine kernel from the
controlling extreme stress to all of `C_*`, or charge the KKT-invisible population to
global insertion/plateau capacity.

---

## 10. Revised Target C subproblems

### C-I-low

For a contact-minimal triangle-free global minimizer with a weak unit contact, exclude
both surviving `|H_*|=2` mechanisms:

1. **chain-kernel:** one extreme stress is the exact full-D chain while the second
   strong diameter chord shears relative to it;
2. **two-direction:** a two-diameter controlling extreme stress has every positive
   contact parallel to one of the two diameter directions.

Any theorem forcing a third projective member direction into a kernel-controlling
stress immediately closes the whole `|H_*|=2` weak-contact phase by C21.1 and C7.

### C-II-low

In the fully force-visible branch, `|H_*|=2` forces the explicit macroscopic-rattler
bound C23.7.  The natural closure is therefore a force-core/insertion-capacity theorem:
prove that a global minimum-diameter source cannot have a three- or four-vertex force
hull carrying every unit contact while a positive fraction of its points remain
contact-isolated.

The right-plateau insertion-body cover C2 and source plateau cavity inequalities are
plausible inputs, but no such incompatibility is proved here.

---

## 11. Audit table

| Claim | Status | Reason |
| --- | --- | --- |
| One-diameter PSD chain C20.1 | **proved** | Exact support plus Cauchy–Schwarz. |
| Two-diameter PSD/max-rank theorem C20 | **proved** | C11 Schur complement; 3-boundary case gives `M=0`; 4-boundary case gives rank-one alternating-sign `M=lambda aa^T` with `lambda>0`. |
| Connelly two-strut theorem | **literature cross-check** | Same PSD/max-rank phenomenon; not needed for C20. |
| Critical-cone kernel-face theorem C21 | **proved** | C13 + C20 + finite extreme-point kernel cover. |
| Third-direction collapse C21.1 | **proved** | A nonzero planar homogeneous quadratic has at most two projective zero directions. |
| Reaction-center disk C22 | **proved** | Weighted C5 support inequality. |
| Two-diameter rattler lower bound C23 | **proved** | Four-vertex area + Oler + strict global diameter bound. |
| Two-direction phase globally impossible | **not proved** | It currently constrains one extreme stress support, not the whole source. |
| Chain-kernel phase globally impossible | **not proved** | The other strong diameter can still shear relative to the chain. |
| General KKT stress matrix PSD | **not proved and not inferred** | C20 is special to at most two positive diameter edges. |

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C20 (new, self-contained):
If a normalized KKT stress has <=2 positive diameter edges, then
  Omega=L_C(alpha)-L_H(beta) is PSD.
For 2 H edges, rank Omega=|V|-3 and ker Omega=span{1,x,y}.
Proof uses C11: Schur complement to B=diameter endpoints gives M=Lambda-L_H.
- |B|=3: M kills 1,x,y, hence M=0.
- |B|=4: H are crossing diagonals; M has rank <=1. Write M=lambda aa^T where the
  affine-dependence vector a alternates signs around the convex quadrilateral.
  Adjacent M_ij=Lambda_ij<=0 and a_i a_j<0, so lambda>=0; connectedness rules out 0.
Thus M PSD and the full matrix is PSD by congruence.

C21:
If maximal |H_*|<=2, C13 and C20 force every critical velocity into the kernel of
some extreme KKT stress. A finite-union/relative-interior argument gives one extreme
stress whose kernel contains the entire critical-cone span.

If |H_*|=2 and that controlling stress uses both H edges, every critical motion on its
support is affine. Any third stressed direction kills the affine shear, makes both H
angular rates equal, and C7 contradicts weak-contact minimality. Therefore a weak-contact
|H_*|=2 survivor is reduced to:
  (a) one-H exact chain-kernel phase; or
  (b) two-H controlling stress with every positive contact parallel to the two H directions.

C22:
For each positive diameter endpoint b, the whole source hull lies in the reaction disk
centered at the beta-weighted barycenter c_b of b's positive diameter partners and
passing through b.

C23:
In fully force-visible C=C_* with |H_*|=2,
  |V(C_*)| <= D^2/sqrt3 + (pi/2)D + 1,
so at least
  ((pi-2)/(2sqrt3))D^2 - (pi/2)D - 1
source points are contact-isolated. The low-H C-II phase is necessarily macroscopically
rattler dominated.

Next exact tasks:
- eliminate the chain-kernel and two-direction C-I-low exceptions; or
- prove force-core/insertion-capacity incompatibility for the Omega(n) isolated points
  forced by C23.
```
