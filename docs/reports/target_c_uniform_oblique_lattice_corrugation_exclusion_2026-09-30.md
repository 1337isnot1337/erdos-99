<!-- theorem-state: {"artifact_id":"ART-626995D9AA5D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: uniform exclusion of exact oblique-lattice sources

**Date:** 2026-09-30

**Base main:** `c00bb08090cf3a7a89fc195cbe3ab450983a5de0`

**State version:** `2026-09-14.audit.51`

**Classification:** proved candidate awaiting promotion; finite analytic proof.

**Scope:** closes the exact oblique-lattice subcase, conditional on this
candidate and its deformation dependency passing independent audit.
Level I and general C-II remain open.

## 1. The finite theorem

Let \(u,v\) be unit vectors with
\[
\pi/3<\theta=\angle(u,v)<2\pi/3,
\qquad \Lambda=\mathbb Zu+\mathbb Zv.
\]
Let \(A\subset p_0+\Lambda\) be any finite source with at least two
points, and set \(D=\operatorname{diam}A\), \(s=\sin\theta\).
If
\[
\boxed{D>64\pi^3/s,}
\tag{1.1}
\]
then \(A\) has an arbitrarily small continuous deformation preserving
all its original unit contacts, preserving unit separation and cardinality,
and strictly decreasing its diameter.

In particular the angle-independent sufficient threshold is
\[
\boxed{D>128\pi^3/\sqrt3.}
\tag{1.2}
\]
The safe integer threshold \(D\ge2292\) suffices. No full-dimensionality
assumption is needed. All contact-isolated source points are included.
No lower bound on \(\theta-\pi/3\) or \(2\pi/3-\theta\) is needed,
even one depending on \(D\).

The exact implication is

> lattice determinant \(\longrightarrow\) sublinear number of actual
> diameter directions \(\longrightarrow U<D\) in the marked-grid
> deformation \(\longrightarrow\) strict full-source competitor.

This supplies the missing inverse-diameter shear exclusion in the
canonical restricted theorem `C-OBLIQUE-LATTICE-COMPETITOR`. It does not
supply the missing global affine chart for a general C-II source.

## 2. Unit contacts and the actual chart

For a lattice difference \(mu+nv\),
\[
|mu+nv|^2=m^2+n^2+2mn\cos\theta.
\]
Since \(|\cos\theta|<1/2\), a difference with both \(m,n\ne0\)
satisfies
\[
|mu+nv|^2>(|m|-|n|)^2+|mn|\ge1.
\tag{2.1}
\]
A difference on an axis has length \(|m|\) or \(|n|\). Therefore
every such finite subset is unit-separated, and its only unit contacts
are differences \(\pm u,\pm v\). In particular it is triangle-free.

Assign the unique actual coordinates \((i,j)\) in the lattice and use
\(X_i=iu\), \(Y_j=jv\) in the marked-grid theorem. Take \(W=A\);
no normalization, co-embedding, deletion of isolates, or rigidity theorem
is needed. All source hypotheses of that theorem hold.

## 3. Circle points in a lattice

**Lemma.** If a planar lattice has covolume \(s>0\), \(D>0\), and
the radius-\(D\) circle centered at zero contains \(M\ge3\) lattice
points, then
\[
M\le2\pi s^{-1/3}D^{2/3}.
\tag{3.1}
\]

**Proof.** List the points in circular order. Three consecutive distinct
points form a nondegenerate triangle: a line intersects a circle in at
most two points. Its area is at least \(s/2\), since the determinant of
two lattice differences is a nonzero integer multiple of \(s\).

Let \(x,y\) be the lengths of the two consecutive circular arcs for
this triple, and put \(\ell=x+y\). The corresponding first two chord
lengths are at most \(x,y\), and the third is at most \(x+y\).
The triangle's circumradius is \(D\), so
\[
\frac s2\le\frac{abc}{4D}
 \le\frac{xy(x+y)}{4D}
 \le\frac{\ell^3}{16D}.
\tag{3.2}
\]
Hence \(\ell\ge(8Ds)^{1/3}\). Summing over the \(M\) cyclic
triples counts each circular arc twice and gives
\[
M(8Ds)^{1/3}\le4\pi D.
\]
This is (3.1). No angular equidistribution, annulus count, or number
theory beyond the lattice determinant is used. \(\square\)

## 4. Diameter edges have distinct projective vectors

For any planar source, two distinct diameter pairs cannot be parallel.
Indeed orient their vectors the same way and write
\(b-a=d-c=Du\), \(|u|=1\). With \(t=c-a\), the source diameter
bounds imply
\[
|t+Du|\le D,\qquad |t-Du|\le D.
\]
Adding their squares gives \(2|t|^2+2D^2\le2D^2\), hence \(t=0\)
and the pairs coincide.

Let \(h\) be the number of actual diameter pairs of \(A\).
Each supplies two different lattice vectors \(\pm(b-a)\) on the
radius-\(D\) circle, and no other diameter pair supplies either vector.
Thus \(2h\le M\). Here \(D\ge1\) and \(s\le1\); if \(M=2\),
the bound below is also immediate. Applying (3.1) otherwise gives
\[
\boxed{h\le\pi s^{-1/3}D^{2/3}.}
\tag{4.1}
\]
This counts actual diameter pairs, including all incidences of high-degree
stars; it is not an inference from a small exceptional vertex set.

## 5. Use the finite deformation immediately

For the odd-gap count \(U\) in the marked-grid report, the number
\(q\) of actual diameter endpoints satisfies
\[
U\le2q-2\le4h-2<4\pi s^{-1/3}D^{2/3}.
\tag{5.1}
\]
Condition (1.1) implies
\(4\pi s^{-1/3}D^{2/3}<D\), and consequently \(U<D\).
The marked-grid theorem now produces the strict finite competitor.
Since \(s>\sqrt3/2\), (1.2) implies (1.1).

The deformation parameter is allowed to depend on all finite source
slacks. This dependence remains valid when the basis angle approaches
\(\pi/3\) faster than any prescribed rate. There is no transfer of
Hausdorff or limiting equality information into a finite inequality.

An elementary cardinality version follows without a packing-density
asymptotic. Fix a source point \(a\). The disjoint interiors of the
radius-\(1/2\) source disks lie in the disk centered at \(a\) of
radius \(D+1/2\), so
\[
|A|\le4(D+1/2)^2.
\]
Thus every source in this exact lattice class with
\[
|A|\ge4585^2+1=21{,}022{,}226
\tag{5.2}
\]
has \(D>2292\) and cannot be a global minimizer. The explicit
threshold is intentionally unoptimized.

## 6. Audit, dependencies, and exact remaining theorem

The only substantive dependency is the noncanonical proved candidate
`target_c_marked_grid_corrugation_strict_competitor_2026-09-30.md`.
Sections 2--4 here are self-contained finite proofs. Exact rational
arithmetic in `research/verify_oblique_lattice_corrugation_threshold.py`
certifies the safe constant and checks small circle-point examples.
The finite computations are not premises of (3.1) or the deformation
theorem. The exact rotation examples are in
`research/verify_marked_grid_corrugation.py`.

Hostile checks: three distinct circle points cannot be collinear; projective
directions identify opposite vectors only once; no edge-incidence count is
replaced by a vertex count; the \(M=2\) case is covered; low-dimensional
sources are included; all contact-isolated points are retained; all finite
nonactive constraints are controlled; no uniform angular slack is claimed.

The endpoints \(\theta=\pi/3,2\pi/3\) are not covered: the triangular
lattice has additional possible unit differences. A triangle-free subset
of that lattice need not itself contain a triangle. The theorem therefore
does not dispose of such a subset merely by noting that its ambient lattice
contains triangles.

**Exact remaining source theorem for this route:** show that every
sufficiently large canonical triangle-free C-II survivor admits one actual
additive unit-grid motion satisfying all contact constraints and \(U<D\),
or a compatible motion across its chart interfaces with a strictly smaller
diameter. Local rhombic charts alone do not supply this global condition.
Inactive containers and positive interface/defect regimes are still open.

The full Erdős problem is not solved here. This restricted closure remains
a candidate until independently audited and promoted under the state contract.
