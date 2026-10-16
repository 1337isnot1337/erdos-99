# Target C — train closure-rank saturation and response-free diameter bracing

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research theorem; theorem authority unchanged.  
**Base:** `ca6b1d43c4704f7f3f71c9b1ee90f347180a3618` (`audit.46` authority plus the audited-working finite train primitives).  
**Dependencies:** canonical core-only ZR/ZF mixed infinitesimal rigidity and relative-interior KKT equilibrium; audited-working train primitives `T1--T3` from `docs/targets/target-c/TRAIN-PRIMITIVES-AUDIT-2026-09-12.md`.

This note extracts two exact finite consequences that do not use the rejected `ZK`
response theorem.

First, every global outer-to-outer stopped train is genuinely braced by actual diameter
pairs on both sides of its shear direction. The only missing point in the old ZGS
argument is supplied by an elementary diameter fact: a diameter-bounded planar set has
at most one diameter segment in any projective direction.

Second, the whole stopped-train system has a natural **exceptional-face closure
matrix**. Train angular rates give every contact infinitesimal flex, while each bounded
nonquadrilateral face contributes at most two scalar closure equations. Mixed rigidity
and the strictly positive diameter KKT weights force this matrix to have rank at least

\[
\boxed{\operatorname{rank}C_{\rm face}\ge 2f-s_Z.}
\tag{1}
\]

Thus in the `s_Z=0` branch all `2f` exceptional-face closure rows are independent.
More generally the total closure-row corank is at most `s_Z`.

The result does not close C-II by itself. It converts the surviving all-regime defect
mechanism into a precise linear-algebraic obligation: exceptional faces are allowed to
stop the surplus trains only by supplying almost full two-dimensional angular closure
rank. This is directly compatible with the current corridor/signed-return route.

---

## 1. Setup

Let `G=(V,C)` be the connected nonisolated positive-contact core of the canonical
contact-minimal, then diameter-pair-minimal triangle-free global minimizer. Put

\[
v=|V|,
\qquad e=|C|.
\]

Let `H` be the actual diameter graph on the loaded terminals, with `h=|H|`. Choose a
relative-interior normalized KKT stress, so

\[
\alpha_e>0\quad(e\in C),
\qquad
\beta_h>0\quad(h\in H).
\tag{1.1}
\]

Canonical core-only ZR/ZF gives

\[
\ker R_{C\cup H}
=\{\text{Euclidean infinitesimal motions on }V\},
\qquad
\operatorname{rank}R_{C\cup H}=2v-3.
\tag{1.2}
\]

Write

\[
s_Z=e+h-(2v-2)\ge0.
\tag{1.3}
\]

Let `R` be the number of bounded strict-rhombus faces, `f` the number of bounded
nonquadrilateral faces, `b` the occurrence-counted outer-face length, and

\[
Q=\sum_{F\text{ nonquad}}(\deg F-4).
\]

The audited-working stopped-train theorem gives a path decomposition of all contact
edges into `T` complete trains and

\[
\boxed{
T=e-2R={b+Q\over2}+2f.
}
\tag{1.4}
\]

The canonical face ledger gives

\[
{b+Q\over2}=h-s_Z,
\]

hence

\[
\boxed{T=h-s_Z+2f,\qquad T-h=2f-s_Z.}
\tag{1.5}
\]

No contact-isolated source point is inserted into `V` or into the mixed rigidity
matrix. They remain in the full source throughout every finite competitor below.

---

## 2. One projective direction contains at most one diameter segment

### Lemma 2.1 — uniqueness of a parallel diameter

Let `X` be any finite Euclidean set of diameter `D>0`. If two diameter pairs are
parallel, then they are the same unordered pair.

### Proof

Suppose

\[
b-a=Du,
\qquad
d-c=Du,
\qquad |u|=1,
\]

after orienting the two parallel segments in the same direction. Put `v=c-a`. Since
`X` has diameter `D`, both cross distances are at most `D`:

\[
|b-c|=|Du-v|\le D,
\qquad
|d-a|=|Du+v|\le D.
\]

Square and add:

\[
|Du-v|^2+|Du+v|^2
=2D^2+2|v|^2
\le2D^2.
\]

Therefore `v=0`, so `c=a` and `d=b`. `\square`

This elementary fact will remove the sign ambiguity in a train-cut equilibrium when
all first shear derivatives vanish.

---

## 3. Response-free two-sided bracing of every outer train

Let `tau` be a nontrivial stopped train whose two terminal occurrences lie on the
actual global outer face. The audited train primitives give a Jordan shore split

\[
V=S\sqcup T
\]

whose contact cut is exactly `E(tau)`. Choose the train-edge unit vector `u` so every
cut contact oriented from `T` to `S` has vector `u`.

Put

\[
A_\tau:=\sum_{e\in E(\tau)}\alpha_e>0.
\]

Sum KKT equilibrium over the vertices of `S`. Internal contact and diameter forces
cancel, giving the exact cut resultant

\[
\boxed{
A_\tau u
=
\sum_{\substack{xy\in H\\x\in T,\ y\in S}}
\beta_{xy}(p_y-p_x).
}
\tag{3.1}
\]

In particular at least one actual diameter edge crosses the train cut.

For a crossing diameter edge `h=xy`, oriented from `T` to `S`, put

\[
r_h=p_y-p_x,
\qquad |r_h|=D.
\]

The audited exact shear translates the full-source shore `S` by

\[
\Delta_\theta=R_\theta u-u
\tag{3.2}
\]

and leaves the other shore fixed. It preserves every old contact exactly and preserves
all strict noncontact lower-distance inequalities for sufficiently small `theta`.
The first squared-length derivative of a crossing diameter is

\[
{d\over d\theta}|r_h+\Delta_\theta|^2\Big|_{\theta=0}
=2r_h\cdot Ju.
\tag{3.3}
\]

Taking the scalar product of (3.1) with `Ju` gives

\[
\boxed{
\sum_{h\pitchfork\tau}\beta_h(r_h\cdot Ju)=0.
}
\tag{3.4}
\]

### Theorem 3.2 — two-sided diameter bracing without response theory

Every global outer-to-outer train has crossing diameter edges `h_+,h_-` satisfying

\[
\boxed{
r_{h_+}\cdot Ju>0,
\qquad
r_{h_-}\cdot Ju<0.}
\tag{3.5}
\]

### Proof

Suppose the crossing values `r_h dot Ju` do not contain both signs. Since every
`beta_h>0`, equation (3.4) then forces

\[
r_h\cdot Ju=0
\qquad\text{for every crossing diameter }h.
\]

Thus every crossing diameter segment is parallel to `u`. Lemma 2.1 says there is only
one such unordered diameter pair. Hence the sum in (3.1) contains one edge only. Its
orientation must be

\[
r_h=Du
\]

because the left side of (3.1) is a positive multiple of `u`.

For this unique crossing diameter pair, the exact shear gives

\[
\begin{aligned}
|Du+\Delta_\theta|^2
&=D^2+2D(\cos\theta-1)+2(1-\cos\theta)\\
&=D^2-2(D-1)(1-\cos\theta)
<D^2
\end{aligned}
\tag{3.6}
\]

for every sufficiently small nonzero `theta` (and all sufficiently large C-II sources
have `D>1`).

Every old diameter pair contained in one shore is unchanged. Every other pair that was
strictly shorter than `D` remains strictly shorter for sufficiently small `theta`.
The same finite-slack choice also keeps every old noncontact strictly longer than one,
while all old contacts are preserved exactly by the audited shear.

Therefore the sheared full source is unit-separated, triangle-free, and has the same
cardinality and the same number of unit contacts. If some same-shore diameter pair
remains, the new source is another global diameter minimizer with strictly fewer actual
diameter pairs, contradicting the secondary normalization. If none remains, its
diameter is strictly below `D`, contradicting global minimality directly.

Thus both signs in (3.5) are mandatory. `\square`

This theorem uses no response conductance, no `ZK` strictness, and no weighted
second-curvature claim.

---

## 4. Train angular rates and the exceptional-face closure matrix

Choose an arbitrary orientation of every contact edge. For a train `tau`, let `omega_tau`
be a scalar. On each contact edge `e` belonging to `tau`, with oriented unit vector
`r_e`, prescribe the derivative of the edge vector to be

\[
\dot r_e=\omega_\tau Jr_e.
\tag{4.1}
\]

This is the general first-order form compatible with the unit-length constraint on
that edge.

For a strict rhombus, orient its boundary cyclically as

\[
r_1,r_2,-r_1,-r_2.
\]

The derivative of the boundary closure is

\[
(\omega_1-\omega_3)Jr_1
+(\omega_2-\omega_4)Jr_2.
\]

The two side directions are linearly independent, so a contact infinitesimal flex has

\[
\omega_1=\omega_3,
\qquad
\omega_2=\omega_4.
\tag{4.2}
\]

Hence the angular rate is constant along every complete train. Conversely, once one
scalar is assigned to each train, every strict-rhombus face closes automatically.

Now orient every bounded nonquadrilateral face boundary as an occurrence-counted walk.
For such a face `F`, first-order edge-vector closure is the two-dimensional equation

\[
\boxed{
\sum_{e\in\partial F}
\omega_{\tau(e)}Jr_e=0.
}
\tag{4.3}
\]

Let

\[
C_{\rm face}:\mathbb R^T\longrightarrow\mathbb R^{2f}
\tag{4.4}
\]

be the matrix formed by the two scalar coordinates of (4.3) for all bounded
nonquadrilateral faces, with boundary occurrences and their signs retained.

### Lemma 4.1 — contact flexes are exactly `ker C_face`

Modulo global translations, the infinitesimal flex space of the positive contact graph
is naturally isomorphic to

\[
\ker C_{\rm face}.
\tag{4.5}
\]

### Proof

Every contact infinitesimal flex gives train-constant angular rates by (4.2), and every
bounded nonquadrilateral face must satisfy (4.3), so it maps into the kernel.

Conversely, take `omega in ker C_face` and define the oriented edge-vector derivatives
by (4.1). The derivative sum around every strict-rhombus face is zero by construction,
and the derivative sum around every bounded nonquadrilateral face is zero by (4.3).
For a connected plane graph, the oriented boundaries of the bounded faces generate the
real cycle space, including in the presence of bridges or articulation vertices.
Therefore the derivative sum vanishes around every graph cycle.

Fix one base vertex and integrate the edge-vector derivatives along contact paths.
Cycle closure makes the resulting vertex velocity path-independent. It is unique up to
adding one common translation, and by construction every contact length derivative is
zero. `\square`

The constant vector

\[
\omega_\tau\equiv1
\tag{4.6}
\]

lies in the kernel and is exactly global infinitesimal rotation. Hence the
non-Euclidean contact-flex dimension is

\[
\boxed{
d_C=T-\operatorname{rank}C_{\rm face}-1.}
\tag{4.7}
\]

---

## 5. Mixed rigidity forces near-maximal exceptional-face closure rank

Choose a basis of the quotient contact-flex space modulo Euclidean motions, of
dimension `d_C`. Let

\[
M_H\in\mathbb R^{h\times d_C}
\]

be the matrix of first derivatives of the `h` actual diameter lengths (equivalently,
any nonzero scalar multiple such as squared lengths) on this basis.

Canonical mixed infinitesimal rigidity (1.2) implies

\[
\boxed{\operatorname{rank}M_H=d_C.}
\tag{5.1}
\]

Indeed, a vector in `ker M_H` would be a contact flex with every diameter derivative
zero, hence a mixed infinitesimal flex; after quotienting Euclidean motions it must
vanish.

KKT stationarity on any contact flex gives

\[
\boxed{M_H^T\beta=0,}
\tag{5.2}
\]

where every coordinate of `beta` is strictly positive. In particular `beta` is a
nonzero left-kernel vector of `M_H`. A full-column-rank `h x d_C` matrix with a nonzero
left kernel must satisfy

\[
h\ge d_C+1.
\tag{5.3}
\]

Insert (4.7):

\[
h\ge T-\operatorname{rank}C_{\rm face}.
\]

Therefore

\[
\operatorname{rank}C_{\rm face}
\ge T-h.
\]

Using the exact train ledger (1.5) proves the main theorem.

### Theorem 5.1 — exceptional-face closure-rank saturation

\[
\boxed{
\operatorname{rank}C_{\rm face}
\ge 2f-s_Z.
}
\tag{5.4}
\]

Since `C_face` has only `2f` rows,

\[
\boxed{
0\le 2f-\operatorname{rank}C_{\rm face}\le s_Z.
}
\tag{5.5}
\]

In particular, if `s_Z=0`, then

\[
\boxed{
\operatorname{rank}C_{\rm face}=2f.
}
\tag{5.6}
\]

Every scalar exceptional-face closure row is then independent of all the others.

Equivalently, any family of exact linear dependencies among the two-coordinate face
closure equations has total dimension at most the mixed-rigidity surplus `s_Z`.

---

## 6. Structural consequences for the C-II frontier

The theorem identifies exactly where the `2f` term in

\[
T-h=2f-s_Z
\]

can go. It is not free train surplus. Each bounded exceptional face may remove at most
two train angular degrees of freedom, and a C-II minimizer requires those closure
conditions to be independent up to only `s_Z` total losses.

This has three immediate consequences.

1. **Zero-surplus branch.** Every exceptional face must contribute its full two scalar
   closure dimensions, globally independently. Any exact mechanism making even one
   face closure equation redundant closes the `s_Z=0` branch.
2. **Small-surplus branch.** At most `s_Z` scalar row dependencies are allowed across
   all exceptional faces. Thus a theorem producing `s_Z+1` independent closure
   dependencies gives an immediate mixed-rigidity contradiction.
3. **Corridor handoff.** Proof-only corridor results show that a macroscopic defect
   face is nearly projectively one-directional. Rank saturation says that this
   near-one-dimensional geometry must nevertheless retain exact two-dimensional face
   closure rank and remain globally independent of the other face closures. This is a
   quantitative conditioning problem on the same physical endpoint occurrences used
   by signed return, not a new carrier-decimal problem.

The rank theorem alone does not turn near-rank-one into exact rank loss. Arbitrarily
small transverse edge components can keep a finite matrix full rank. A closing theorem
must now quantify that conditioning against global minimality/KKT response or extract
an exact dependency from ordered phase/topological structure.

---

## 7. Hostile scope check

- `V` is only the nonisolated positive-contact core. Contact-isolated source points are
  retained globally and are not inserted into the Section-57 affine kernel.
- The exact shear theorem moves all full-source points on the chosen Jordan shore, so
  source cardinality is unchanged.
- The response-free bracing theorem uses only finite slack, KKT equilibrium, and
  diameter-pair minimality. It does not use `A_tau>w_tau`, `ZK`, or the old weighted
  curvature argument.
- The train-angle proof does not assume independent train angles. It derives the exact
  compatibility matrix and then counts its rank.
- Bridges and articulation points are permitted: bounded face boundaries generate the
  cycle space and singleton train variables simply appear as columns of `C_face`.
- No numerical carrier bound is used.
- The theorem is finite and branch-independent once the audited-working stopped-train
  decomposition is available.

**Disposition:** proof-only structural theorem. C-II remains open.
