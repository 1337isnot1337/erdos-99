<!-- theorem-state: {"artifact_id":"ART-9EC4573C677B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# A global lattice population bound and a full-source defect consequence

**Classification:** proved candidates awaiting promotion; **unreviewed**.
The minimizer consequences additionally depend on the unreviewed
[linear-reserve candidate](global_boundary_zigzag_linear_reserve_2026-10-11.md).
**Level I remains open.**

Run baseline: `ab6dd3336f9f8d440f2bada76edb32153391cddc`, state
`2026-10-10.audit.234`; owned branch
`research/sol/global-independent-20261011`. No other worker's unpromoted
research is imported.

## 1. The global implication being tested

The linear reserve changes the scale of a useful crystallization theorem.
The exact chain studied here is

```text
all but o(D) actual source labels within a sufficiently small fixed distance
of one unit-separated lattice
  -> global lattice population bound with only o(D) boundary error
  -> contradiction to the candidate positive linear reserve.
```

This report proves the middle implication uniformly over all planar lattices
whose shortest nonzero vector has length at least one. It does **not** prove
the first implication for triangle-free minimizers. The missing extraction
cannot be assumed from density, a local grain, or a contact-core statement.

The concrete lattice theorem is as follows. Put `a=pi/(2sqrt(3))`. If
`S` is a finite subset of a translated unit-separated rank-two lattice and
`diam(S)<=D`, with `D>=1`, then

\[
\boxed{|S|\le aD^2+86D^{4/5}+1.}
\tag{1}
\]

The constant is uniform in lattice shape, phase, and orientation. No circular
container is assumed: the bound uses the **actual pairwise diameter** of the
lattice source. This distinction matters because a general diameter-`D` set
need not lie in a radius-`D/2` disk.

Section 7 extends the argument to full unit-separated periodic packings with
`q` points per period cell, giving the uniform error `114q^(6/5)D^(4/5)+q`
when `q<=D/16`. Full cross-coset separation is essential.

## 2. A long flat side costs isodiametric area

Let `K` be a convex polygon of diameter at most `D`, and set

\[
\delta={\pi D^2\over4}-\operatorname{area}(K)\ge0.
\]

Every side of `K`, of length `ell`, satisfies

\[
\boxed{\ell^3\le48D\delta.}
\tag{2}
\]

To prove this, form `L=(K-K)/2`. Every point of `L` has norm at most
`R=D/2`; Brunn-Minkowski gives `area(L)>=area(K)`. A supporting side of
`K` of length `ell` yields a parallel supporting face of `L` of length
`s>=ell/2`, because supporting faces add under Minkowski addition.

If that supporting line is at distance `h` from the origin, its intersection
with the radius-`R` disk has length `2sqrt(R^2-h^2)>=s`. The circular cap
beyond the line is absent from `L`. Its area is at least the cap with chord
length `s`. Writing `t=s/(2R)`, that cap has area

\[
R^2(\arcsin t-t\sqrt{1-t^2})
\ge {2R^2t^3\over3}
={s^3\over12R}.
\]

The inequality follows by differentiating the bracket: its derivative is
`2t^2/sqrt(1-t^2)>=2t^2`, and its value at zero is zero. Therefore

\[
\delta\ge\pi R^2-\operatorname{area}(L)
\ge {s^3\over12R}\ge {\ell^3\over48D},
\]

which proves (2). No equality-case uniqueness theorem is used.

## 3. Uniform control of boundary lattice multiplicity

Let `Lambda` be the untranslated lattice of differences. Its covolume `v`
is at least `a0=sqrt(3)/2`. Indeed, choose a shortest lattice vector of
length `s>=1`. It is primitive and extends to a lattice basis. Subtract an
integer multiple of it from the second basis vector to make the parallel
component have absolute value at most `s/2`. The second vector's length is
at least `s`, so its perpendicular component has magnitude at least
`sqrt(3)s/2`; hence `v>=sqrt(3)s^2/2>=a0`.

Let `N(t)` count nonzero lattice vectors of length at most `t`. Disjoint
radius-`1/2` open disks around these vectors give, for `t>=1`,

\[
N(t)\le4(t+1/2)^2\le9t^2.
\]

For every `T>=1`, summation by parts consequently gives

\[
\sum_{0<|u|\le T}{1\over|u|}
={N(T)\over T}+\int_1^T{N(t)\over t^2}\,dt
\le18T.
\tag{3}
\]

Set `K=conv(S)` and suppose it has positive area. Merge consecutive collinear
sides. Each oriented side has one primitive lattice direction `u`, and its
contribution to the number `B` of lattice points on the polygon boundary is
its length divided by `|u|`. A given oriented direction occurs at most once
on a convex polygon. With `ell_max` the longest side and `P=per(K)`, split
these directions at length `T`. Equation (3) gives

\[
\boxed{B\le18\ell_{\max}T+{P\over T}.}
\tag{4}
\]

This controls collinear boundary lattice points as well as extreme vertices.
They must not be confused: counting only hull vertices would make the bound
false even for a large lattice rectangle.

## 4. Pick's theorem and optimization of the area deficit

Pick's theorem, after an invertible basis map to the integer lattice, gives

\[
|S|\le |K\cap(t+\Lambda)|
={\operatorname{area}(K)\over v}+{B\over2}+1.
\]

For completeness, `P<=pi D` follows by projecting the polygon boundary:
the total absolute projection of its edges onto a fixed line is twice its
width. Integrating over directions in `[0,pi]` gives `P` as the integral
of those widths, each at most `D`.

Use `v>=a0`, `P<=pi D<4D`, equations (2) and (4), and
`T=D^{1/5}>=1`. Since `48^{1/3}<4` and `a0<1`,

\[
\begin{aligned}
|S|-aD^2-1
&\le-{\delta\over a_0}+9\ell_{\max}T+{P\over2T}\\
&\le-\delta+36D^{8/15}\delta^{1/3}+2D^{4/5}.
\end{aligned}
\tag{5}
\]

Put `u=delta^{1/3}/D^{4/15}`. The right side of (5) becomes
`D^{4/5}(-u^3+36u+2)`. For `u>=0`,

\[
u^3-36u+48\sqrt3=(u-2\sqrt3)^2(u+4\sqrt3)\ge0,
\]

and `48sqrt(3)+2<86`. This proves (1).

If `S` is collinear, unit separation gives `|S|<=D+1`. The same bound (1)
follows immediately for `D>=1`; empty and singleton sets also satisfy it.

This proof uses no lattice discrepancy estimate, no fixed lattice angle, no
bounded condition number, and no source embedding inside a diameter-half disk.

## 5. Full-source distance from every unit-separated lattice

Assume the linear-reserve candidate, so every sufficiently large global source
`A`, with diameter `D`, satisfies

\[
n-1\ge aD^2+cD,\qquad c={1\over320000}.
\tag{6}
\]

Fix **any** translated unit-separated rank-two lattice `Lambda` and any
`0<=rho<1/2`. Let `k_rho(A,Lambda)` count the actual source labels farther
than `rho` from the lattice. Each of the remaining labels has a unique nearby
lattice site, and distinct source labels cannot share a site: sharing would
give source distance at most `2rho<1`. Those matched sites have diameter at
most `D+2rho`.

Apply (1) to the matched sites and subtract from (6):

\[
\boxed{
k_\rho(A,\Lambda)
\ge(c-4a\rho)D-4a\rho^2-86(D+2\rho)^{4/5}.
}
\tag{7}
\]

All source labels participate, including every contact isolate. The bound is
uniform over lattice shape, orientation and translation. In particular, for
`rho0=1/10000000`, one has `4a rho0<c/4`. Thus, for every sufficiently
large global minimizer and **every** such lattice,

\[
\boxed{k_{\rho_0}(A,\Lambda)\ge {D\over640000}.}
\tag{8}
\]

The threshold implied by this deliberately coarse estimate is very large;
the result is asymptotic, with explicit finite inequality (7). No practical
finite threshold is claimed.

## 6. Remaining global bridge and regression checks

Equation (8) is a necessary condition on every global minimizer, whether or
not it contains triangles. It does not supply a unit triangle. To obtain a
contradiction from it, one would need an additional theorem forcing a
triangle-free global minimizer to have fewer unmatched labels than (7) allows.
No such extraction is proved here. In particular:

- An `O(D)` exceptional set is not `o(D)` and can absorb this obstruction.
- Several grains with different phases or orientations cannot silently be
  treated as one lattice.
- A contact-core chart does not cover contact isolates by definition.
- A lattice whose own shortest vector is less than one is outside the theorem.
- A slowly varying chart can have positional error much larger than `rho0`.

The independent dense odd-ring regression remains compatible with this result:
its sources are nonglobal and fail (6). The triangle-free deformation of the
zigzag competitor also causes no contradiction: it is not globally optimal,
and it includes boundary replacements that need not match its original lattice.

### A finite-union shortcut is false: an exact 39-lattice regression

One cannot replace the single lattice in (1) by an arbitrary fixed finite
union and keep an `o(D)` error, even for triangle-free sources. The existing
zigzag construction gives a direct counterexample.

Let `Gamma` be generated by `(19/10,0)` and `(1,a0)`. It is
unit-separated: a nonzero vector with vertical index zero has length at least
`19/10`; vertical index of magnitude at least two gives vertical separation
at least `sqrt(3)`; at vertical index `+-1`, the smallest horizontal
absolute coordinate is `9/10`, giving squared length at least
`81/100+3/4=39/25>1`.

A packet point from row `k` and index `i=2j+sigma` has coordinates

\[
(A_k+1+(19/10)j+(19/20)\sigma,\quad t_y+ka_0+\eta_\sigma),
\]

with `sigma in {0,1}`, `eta_0=1/6`, and `eta_1=1/2`. Choose the
residue `r in {0,...,18}` of the integer `A_k+1-k` modulo 19.
Subtracting the shift `(r+(19/20)sigma,t_y+eta_sigma)` leaves a vector
of `Gamma`: its vertical index is `k`, and its remaining horizontal
coordinate is an integer multiple of `19/10`.

Thus all packets, simultaneously and at every radius, belong to just 38
translates of `Gamma`. The retained original lattice adds one more translate
class. The whole competitor lies in a union of 39 unit-separated lattices.
Each constituent lattice is unit-separated; their infinite union need not be.
The selected finite source is unit-separated by the complete zigzag pair ledger.

Apply the arbitrarily small vertical expansion from Section 5 of the
linear-reserve report. All 39 lattices remain unit-separated; the actual
source becomes triangle-free while retaining horizontal unit pairs. For any
fixed `0<c'<1/320000` and all sufficiently large comparison diameters `D`,
the resulting source has more than `aD^2+c'D` points and actual diameter
`d<D`. In particular it has more than `ad^2+c'd` points. Its actual
diameter tends to infinity with its population.

This is a **nonglobal regression**. It rejects only the finite-union
population shortcut. It does not refute a theorem using nonoverlapping grain
hulls, paid interfaces, actual source stresses, or exact global optimality.
None of those additional hypotheses is supplied by finite lattice coverage.

## 7. Full periodic packings: a uniform motif bound

Unlike an arbitrary finite union of lattices, a **globally unit-separated
periodic packing** has a uniform population bound. Suppose

\[
P=\bigcup_{i=1}^q(t_i+\Lambda)
\]

is unit-separated as a whole, with `q` distinct cosets. The lattice, phases,
and `q` may vary with the source. If `S` is any finite subset of `P`,
`diam(S)<=D`, and `1<=q<=D/16`, then

\[
\boxed{|S|\le aD^2+114q^{6/5}D^{4/5}+q.}
\tag{9}
\]

This counts the full source. It assumes no contact connectivity, grain
decomposition, circular container, or common hull for the separate coset
crops. It requires every distance in the infinite periodic packing,
including cross-coset distances, to be at least one.

### Covolume-sensitive lattice estimate

For a unit-separated lattice of covolume `V`, and `D>=max(1,V)`,
Sections 2--4 give the stronger estimate

\[
\boxed{|X|\le {\pi D^2\over4V}+86V^{1/5}D^{4/5}+1}
\tag{10}
\]

for any subset of a translate with diameter at most `D`. For a noncollinear
hull put `delta=pi D^2/4-area(conv X)` and retain its coefficient in Pick:

\[
|X|-{\pi D^2\over4V}-1
\le-\delta/V+36D^{1/3}T\delta^{1/3}+2D/T,\qquad T\ge1.
\]

The maximum of the first two terms is
`48sqrt(3) sqrt(V) D^(1/2) T^(3/2)`. Choose
`T=(D/V)^(1/5)>=1`. Both remaining terms have scale
`V^(1/5)D^(4/5)`, and `48sqrt(3)+2<86` proves (10).
A collinear subset has at most `D+1` points. If `V<=D/2`, the leading
term in (10) already exceeds `D`; if `D/2<V<=D`, its error term exceeds
`D`. Empty and singleton subsets are immediate.

### Dense and sparse period cells

The period lattice is unit-separated, since `p,p+lambda` belong to `P`
for any `p in P` and nonzero period `lambda`. Its covolume satisfies

\[
\boxed{V\ge q a_0.}
\tag{11}
\]

Indeed apply the canonical [finite Oler inequality](../theory/03-oler-shell.md)
to increasingly large parallelograms of period cells. Population is `q`
times the cell count up to a boundary-order error. Dividing by area and
taking the limit gives `q/V<=1/a0`. Here it is essential that the **whole**
periodic packing is separated.

If `V<=4q`, then `q<=D/16` gives `V<=D/4`. Apply (10) to each actual
subset `S_i=S intersect (t_i+Lambda)`. Their hulls need not coincide, but
each has diameter at most `D`. Summing and using (11) gives

\[
|S|\le {q\pi D^2\over4V}+86qV^{1/5}D^{4/5}+q
\le aD^2+114q^{6/5}D^{4/5}+q,
\]

because `86*4^(1/5)<114`.

Large covolume cannot evade the bound. A shortest period vector has length
`s>=1`, is primitive, and extends to a basis. Reduce the other basis
vector's parallel component to absolute value at most `s/2`. Its normal
component satisfies `h>=a0 s`, with `V=sh`. A diameter-`D` coset subset
uses at most `D/h+1` rows and at most `D/s+1` points per row. Hence

\[
|S|\le q\left({D^2\over V}+D\left({1\over s}+{1\over h}\right)+1\right)
<{qD^2\over V}+3qD+q.
\]

For `V>4q` and `q<=D/16`, this is at most `D^2/2`, below the right
side of (9). This proves (9) in both alternatives.

### Consequence for global minimizers

Combining (9) with the candidate linear reserve, every global minimizer
with `D>1280000` contained in a full unit-separated periodic packing with
`q` points per period cell satisfies

\[
\boxed{q\ge {D^{1/6}\over(36800000)^{5/6}}.}
\tag{12}
\]

For `q<=D/16`, the two population bounds give
`D/320000<=114q^(6/5)D^(4/5)+q-1<=115q^(6/5)D^(4/5)`, which is
(12). For `q>D/16`, use `D>=1` and `(36800000)^(5/6)>16`.

A uniformly bounded periodic motif therefore cannot contain global
minimizers of unbounded diameter, even if its lattice shape and phases
vary. The constants supply an extremely large threshold; no practical
finite threshold is claimed. This applies to minimizers with triangles
as well. It supplies no bounded-motif extraction from triangle-free
sources and does not close Level I. The 39-lattice regression remains
compatible with (9): its selected finite source is separated, while its
infinite lattice union is not.

## 8. Checked literature, computation, and lifecycle

The imported geometric formulas are planar Brunn-Minkowski, Pick's theorem,
and canonical finite Oler in Section 7. Brunn-Minkowski is used for compact convex bodies
`K,-K` of positive area with equal weights, solely to infer
`area((K-K)/2)>=area(K)`; see Gardner, *The Brunn-Minkowski Inequality*,
equation (2), page 355, in the
[checked journal paper](https://www.ceremade.dauphine.fr/~carlier/Brunn-Minkowski).
Pick's theorem is used after a lattice basis change, with area divided by
covolume and with **all** boundary lattice points counted; its statement was
checked in the
[UC Davis LattE notes](https://www.math.ucdavis.edu/~latte/background/countingLecture/pick/pick/index.php).
For the primitive-triangle count, the correct identities are
`V-E+T=1`, `3T=2E-B` and `V=I+B`. They give
`T=2I+B-2`, and primitive area one half gives `area=I+B/2-1`.
This does not rely on the signs in the notes' expanded Euler substitution.
No imported equality classification is needed.

`research/verify_global_lattice_population_bound_2026_10_11.py` checks exact
lattice crops and noncircular hulls, Pick counts, diameter normalization, the
symmetrized-hull area and radius claims, and the cubic side-length inequality
with rational interval bounds. These finite checks do not establish the
universal theorem, its minimizer premise, or the missing extraction step.

The theorem-state files remain unchanged. The claims await independent audit;
their conditional use of the linear reserve is explicit.

The completed lattice verifier checked 16 exact crops/hulls, 309 supporting
sides, and 18,154 lattice labels. The zigzag verifier separately checks the
explicit 38 packet-lattice memberships for all 15,460 inserted labels in its
five examples; the untouched original lattice supplies the thirty-ninth class.

The periodic extension additionally checks four full periodic patterns with
5,462 cropped labels, 214 coset-hull sides, and 1,112 exact period/phase pair
tests. A quadratic-form bound covers every omitted period translate. The
fixtures include a nonlattice triangle-free two-site motif, a three-site
triangular motif, and both dense-cell and sparse-cell alternatives. Each
eligible coset also checks the covolume-sensitive bound (10). These are
nonglobal fixtures; the universal motif bound and its global implication are
the analytic arguments of Section 7.
