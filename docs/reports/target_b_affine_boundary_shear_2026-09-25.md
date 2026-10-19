<!-- theorem-state: {"artifact_id":"ART-0AFF54BC7BA3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "7601a39c3932e1b45cca0106a1e8de1e19760041", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_b_affine_boundary_shear_2026-09-25.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b205ed8bff3b5797bb4c0532ca4e3abfcb3eaba155b4da130d90adeb06a2761b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — affine boundary count and inverse-diameter shear

**Date:** 2026-09-25
**Base commit:** `60e0d60801e1abfa2cfba65ba82ce89740c399f0`
**State version:** `2026-09-14.audit.51`
**Run type:** closing-proof attempt
**Target:** B, with a restricted affine-source application to C-II
**Status:** proved candidate awaiting independent audit; noncanonical
**Active Target B prompt:** none
**Computation:** none

The earlier unreviewed
`target_c_oblique_lattice_pick_comparison_2026-09-14.md` already gives the
finite Pick comparison with the crude bound (b_\Lambda(K)\le\pi D\).
The new step here is (b_\Lambda(K)=o(D)) for a sequence of actual global
minimizers admitting a bounded-displacement affine chart. The exact shell
identity (6) is a separate consequence.

## Level I status and endpoint

**STILL OPEN.** The exact Target B sufficient closure is

\[
G+E\ge a_0 B/2+a_0(t+\chi-1),\qquad a_0=\sqrt3/2,
\]

where the pure rhombic disk has \(t=0,\chi=1\). Section 36 gives the strict
reverse inequality for a global minimizer. The attempted implication chain was

```text
near-disk global minimizer on one oblique lattice
  -> sublinear lattice-point count on its convex-hull boundary
  -> Pick identity for G+E-a_0 B/2
  -> either exact shell contradiction or a narrowed affine-source survivor.
```

The last step yields the narrowed source conditions below. Canonical Target B
Section 39 already excludes an exact affine chart in the jammed pure-disk
branch, by its non-atomic train-mass theorem. The new affine scale is relevant
to source classes outside that branch, especially the restricted C-II route.
No global affine chart is known for a general C-II source.

## 1. Boundary-count theorem

Write \(\Lambda_\theta=\mathbb Zu+\mathbb Zv\), where \(|u|=|v|=1\) and
\(\theta\in[\pi/3,2\pi/3]\). Its covolume is \(a=\sin\theta\ge a_0\).
For a convex lattice polygon \(K\), let
\(b_\Lambda(K)=|\Lambda\cap\partial K|\), counting each boundary point once.

> **Theorem 1 (proved candidate).** Let \(A_j\) be unit-separated global
> minimum-diameter sets with \(D_j=\operatorname{diam}A_j\to\infty\).
> Suppose there are distinct lattice points \(z_{j,p}\in\Lambda_{\theta_j}\),
> one for every \(p\in A_j\), such that
> \(|p-z_{j,p}|\le\varepsilon_j\), with \(\sup_j\varepsilon_j<\infty\).
> Put \(K_j=\operatorname{conv}\{z_{j,p}:p\in A_j\}\) and
> \(a_j=\sin\theta_j\). Then
> \[
> b_{\Lambda_{\theta_j}}(K_j)=o(D_j),\qquad
> D_j(a_j-a_0)\le4a_0\varepsilon_j+o(1).
> \tag{1}
> \]
> In particular, exact affine-lattice global minimizers satisfy
> \(D_j(a_j-a_0)\to0\). If \(\varepsilon_j\to0\), the same conclusion holds.
> For open oblique angles this is
> \(D_j\operatorname{dist}(\theta_j,\{\pi/3,2\pi/3\})\to0\).
> In the exact affine case, with \(K_j=\operatorname{conv}A_j\), the
> isodiametric deficit also satisfies
> \(\pi D_j^2/4-\operatorname{area}(K_j)=o(D_j)\).

All source points, including contact-isolated points, are included in the
matching. The theorem does not claim that arbitrary minimizers have such a
matching.

### Proof

Abbreviate \(D=D_j\), \(\varepsilon=\varepsilon_j\), and
\(K=K_j\). The centered fundamental parallelogram of \(\Lambda_\theta\)
lies in a disk of radius at most \(\sqrt3/2\): its farthest points are its
four corners, with radii \(|u+v|/2\) and \(|u-v|/2\). Its translates centered
at the distinct \(z_{j,p}\) have disjoint interiors. Hence, by Steiner's
formula and the perimeter-diameter inequality,

\[
n a\le \operatorname{area}(K)+\tfrac{\sqrt3}{2}\operatorname{per}(K)
       +\tfrac{3\pi}{4}
\le \operatorname{area}(K)+\tfrac{\pi\sqrt3}{2}(D+2\varepsilon)
       +\tfrac{3\pi}{4}.
\tag{2}
\]

Here \(\operatorname{diam}K\le D+2\varepsilon\). The canonical strict
translated-triangular-lattice comparison, Target B Section 36, says

\[
n-1>\frac{\pi D^2}{4a_0}.
\tag{3}
\]

Since \(a\ge a_0\), equations (2) and (3) give
\(\operatorname{area}(K)\ge\pi D^2/4-O(D)\). Isodiametry gives the upper bound
\(\operatorname{area}(K)\le\pi(D+2\varepsilon)^2/4\). Thus
\(\operatorname{area}(K)/D^2\to\pi/4\) and
\(\operatorname{diam}(K)/D\to1\).

After translating and scaling by \(D^{-1}\), every subsequence of these
convex bodies has a Hausdorff-convergent further subsequence. Its limit has
diameter one and area \(\pi/4\); the equality case of the planar
isodiametric inequality makes it a radius-\(1/2\) disk. Consequently every
edge of \(K\) has length \(o(D)\). Otherwise a subsequence of normalized
edges of positive length, together with their supporting lines, would
converge to a nontrivial segment on the boundary of a disk.

We now count boundary lattice sites. An edge vector is an integer multiple
of a primitive lattice vector \(w\), and its contribution to
\(b_\Lambda(K)\) is that integer multiple. For fixed \(M>0\), primitive
vectors of length below \(M\) have only finitely many possible integer
coefficient pairs, uniformly for \(\theta\in[\pi/3,2\pi/3]\):
\(|iu+jv|^2\ge(i^2+j^2)/2\). A convex polygon has at most two edges
parallel to each such primitive direction. Their total contribution is
\(o(D)\), because every edge is \(o(D)\) and every nonzero lattice vector
has length at least one. The remaining edges contribute at most
\(\operatorname{per}(K)/M\le\pi(D+2\varepsilon)/M\).
First let \(j\to\infty\), then \(M\to\infty\). This proves
\(b_\Lambda(K)=o(D)\).

For completeness, Pick's identity on an affine lattice gives
\[
|\Lambda\cap K|
=\frac{\operatorname{area}(K)}a+\frac{b_\Lambda(K)}2+1.
\tag{4}
\]
It applies because \(K\) is a lattice polygon. It can be proved without
an equality hypothesis: triangulate \(K\) using all of its lattice sites;
each empty lattice triangle has area \(a/2\), and Euler's formula gives
\(2I+b-2\) triangles, where \(I\) is the number of interior lattice sites.
An empty lattice triangle has determinant one in lattice coordinates: if
the determinant exceeded one, a nonzero lattice point in the half-open
parallelogram of two edges, or its reflection through the opposite corner,
would lie in the triangle. This proves (4).

All \(n\) matched lattice sites lie in \(K\). Combining (3), (4), and
isodiametry gives the exact finite inequality

\[
\frac{\pi D^2}{4a_0}
<n-1
\le\frac{\pi(D+2\varepsilon)^2}{4a}
    +\frac{b_\Lambda(K)}2,
\]

and hence

\[
D(a-a_0)
<4a_0\varepsilon+\frac{4a_0\varepsilon^2}{D}
  +\frac{2aa_0}{\pi}\frac{b_\Lambda(K)}D.
\tag{5}
\]

The last two terms tend to zero, proving (1). Since
\(\sin\theta-a_0\) vanishes only at the two endpoints and has nonzero
one-sided derivative there, the angle statement follows. ∎

For the final exact-affine assertion, set \(\varepsilon=0\). Equations
(3)--(4) yield
\[
\operatorname{area}(K)
\ge a\left(n-1-\frac{b_\Lambda(K)}2\right)
>\frac{a}{a_0}\frac{\pi D^2}{4}-\frac a2b_\Lambda(K)
\ge\frac{\pi D^2}{4}-o(D).
\]
Isodiametry supplies the reverse bound. This gives the stated \(o(D)\)
deficit.

## 2. Exact pure-disk Pick ledger

> **Theorem 2 (proved candidate).** Suppose \(A\subset\Lambda_\theta\)
> is exactly the vertex set of one edge-to-edge pure unit-rhombic disk:
> every bounded face is an elementary \(u,v\) rhombus and there are no
> other source points. Let \(R\) be its rhombus count, \(B\) its boundary
> edge count, \(K=\operatorname{conv}A\), and
> \(M=|\Lambda_\theta\cap K|-|A|\). With
> \(G=\operatorname{area}(K)-aR\) and \(E=(a-a_0)R\),
> \[
> \boxed{G+E-\frac{a_0B}{2}
> =(a-a_0)(n-1)+aM-\frac a2b_{\Lambda_\theta}(K).}
> \tag{6}
> \]
> If such sources are global minimizers along a sequence with \(D\to\infty\),
> then \(M=o(D)\), \(D(a-a_0)\to0\), and the shell gap satisfies
> \(a_0B/2-(G+E)=o(D)\).

**Proof.** Euler's formula for the quadrangulated disk gives
\(n=R+B/2+1\). Equation (4), with \(|\Lambda\cap K|=n+M\), gives
\[
G=a\left(M+\frac{B-b_\Lambda(K)}2\right).
\]
Add \(E=(a-a_0)R\), subtract \(a_0B/2\), and use
\(R+B/2=n-1\) to obtain (6). For a global minimizer the strict Section-36
shell window is \(G+E<a_0B/2\). Every term on the right of (6) except
the last is nonnegative, so
\[
(a-a_0)(n-1)+aM<\frac a2b_\Lambda(K).
\tag{7}
\]
Theorem 1 gives \(b_\Lambda(K)=o(D)\), whence \(M=o(D)\).
It also gives \(D(a-a_0)\to0\). Equation (6) and the nonnegativity of
\((a-a_0)(n-1)\) and \(aM\) bound the positive shell gap by
\(ab_\Lambda(K)/2=o(D)\). ∎

This exact identity is the affine-source connection to the canonical
\(G+E\) currency. It does not hold for a multi-grain source or a source
with exceptional faces without additional terms.

## 3. Vanishing-chart exclusion in the Target B pure disk

> **Corollary 3 (proved candidate from canonical Section 39).** There is no
> sequence of sufficiently large triangle-free, first-order-jammed,
> pure-rhombic-disk global minimizers that admits injective matching of
> every source point to one unit oblique lattice with maximum displacement
> \(\varepsilon_D=o(1)\).

**Proof.** Theorem 1 first gives \(a_D-a_0=o(D^{-1})\), so after possibly
replacing \(v\) by \(-v\), the lattice angle tends to \(\pi/3\). For any
unit contact \(pq\), its matched lattice difference \(z_p-z_q\) has length
at most \(1+2\varepsilon_D\). The quadratic-form bound
\(|iu+jv|^2\ge(i^2+j^2)/2\) leaves only finitely many integer coefficient
pairs in this range. At the triangular endpoint, the only nonzero lattice
vectors of length one are \(\pm u,\pm v,\pm(u-v)\), and every other vector
has length bounded away from one. Therefore, for large \(D\), every unit
contact direction lies within \(o(1)\) of one of three fixed projective
directions. Every rhombic train inherits a unit-edge direction, so every
weak limit of its normalized direction measure has total atomic mass
\(s=1\).

Canonical Target B Section 39.2--39.3 instead gives
\(s\le1-y/2\) and \(y\ge1/2\) for every such jammed pure-disk survivor,
so \(s\le3/4\). This contradiction proves the corollary. ∎

The exact affine pure-disk case follows already from Section 39 without
the Pick argument. Corollary 3 extends that exclusion to vanishing source
displacement and makes explicit the source-to-train step. It does not rule
out a chart with a fixed positive displacement, or any flexible/non-pure
source.

## 4. Adversarial checks and failed closure

The missing-sites term cannot be forced positive by Pick's theorem. For
\(m\ge2\), take \(A_m=\{iu+jv:0\le i,j\le m\}\) with
\(\theta_m=\pi/3+m^{-2}\). This is an exact unit-separated,
triangle-free rhombic disk with \(R=m^2\), \(B=b_\Lambda(K)=4m\),
\(G=M=0\), and \(E=m^2(\sin\theta_m-a_0)<1\). Thus
\(G+E<a_0B/2\) for every \(m\ge2\). The sets are not global
minimizers: their diameter is \(m|u+v|\sim\sqrt3m\), far above the
triangular-lattice comparison for \(n=(m+1)^2\). The example kills a
universal Pick-only shell inequality, even at inverse-square angle excess.

There is also a scalar-bound regression. For each fixed \(n\),
Section 36 constructs an \(n\)-point triangular-lattice set \(T_n\) with
\(\operatorname{diam}(T_n)^2<(2\sqrt3/\pi)(n-1)\). Replace its triangular
basis angle \(\pi/3\) by \(\pi/3+\eta\), keeping its finite integer
coordinates. For every sufficiently small \(\eta>0\), continuity preserves
the strict diameter inequality; the resulting set is unit-separated and
triangle-free. Thus the strict \(n-1\) scalar bound does not distinguish a
triangle-free feasible source from a global minimizer. The proof must use
exact optimality at the source.

The proof also checks the source/scaffold distinction: all bounds use the
actual \(n\) source points or their stated injective lattice matches.
No matching for a general rhombic grain is inferred. Contact-isolated
source points are retained in Theorem 1. The rejected full-source ZR/ZF
extension, local-jamming-to-global inference, and boundary-order loss
shortcuts are not used.

## 5. Exact remaining lemma and classification

The exact affine pure-disk jammed subroute is already excluded by Section
39. Outside that subroute, Theorem 1 leaves the following source question:

> Can every sufficiently large triangle-free global minimizer that is an
> exact subset of one unit oblique lattice and satisfies
> \(0<a-a_0=o(D^{-1})\) be given an actual same-cardinality unit-separated
> competitor of diameter \(<D\), without assuming the Target B jammed
> pure-disk hypotheses?

The conclusion must cover arbitrarily small positive shear; an area estimate
with an uncontrolled \(O(D)\) boundary term cannot do so. Even a solution
for this affine subroute would leave nonaffine grains, interfaces, holes,
and the macroscopic inactive-container branch.

| Claim | Classification | Dependency and limit |
| --- | --- | --- |
| Theorem 1 | proved candidate awaiting audit | Canonical Target B §36 strict global comparison; elementary convex geometry and Pick proof above |
| Theorem 2 | proved candidate awaiting audit | Theorem 1 and canonical pure-disk Euler/shell identities; only one exact affine lattice |
| Corollary 3 | proved candidate awaiting audit | Theorem 1 plus canonical Target B Section 39; only the jammed pure-disk branch |
| Universal Pick-only shell inequality | rejected | Exact parallelogram regression above |
| General Target B/C-II closure | open | No global affine chart or source-preserving competitor |

**Promotion recommendation:** independent audit first. The result narrows a
restricted affine-source scale but does not change the canonical global
frontier. If promoted, update the manifest, Target B/C route text, active
prompt if its obligation changes, and generated views in one transaction.
