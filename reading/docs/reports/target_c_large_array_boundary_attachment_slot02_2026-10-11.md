> Generated reading edition · [exact source](../../../docs/reports/target_c_large_array_boundary_attachment_slot02_2026-10-11.md) · source SHA-256 `f2225a9ceebddb2b3318ed948bb94d247f2a61c9e73db80d7ce3567093e037c6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-85AD449A16C4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: large actual bent arrays need linearly many external contacts

**Date:** 2026-10-11. **Worker:** 02.  
**Base main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.  
**Theorem state:** `2026-10-10.audit.234`.  
**Starting checkpoint:** `d3b7123e`.  
**Branch / PR:** `research/sol61-slot02-20261010-integrated-fold`,
[PR #948](../publication/provenance.md#source-records).  
**Classification:** proved candidates awaiting independent mathematical audit;
unreviewed and noncanonical. **C-II AND LEVEL I REMAIN OPEN.**

## 1. Statement and consequence

An **actual complete bent array** in a source `P` means the actual labels

`p_ij=z+x_i+y_j`, `0<=i<=a`, `0<=j<=c`, `a,c>=1`,

are distinct source points, every consecutive row and column edge has length
one, and every consecutive cell is an actual strict unit-rhombic contact
face. Orient the cell boundaries consistently so that

`u_i=x_(i+1)-x_i`, `v_j=y_(j+1)-y_j`

have positive determinant and their angle is strictly between `pi/3` and
`2pi/3` for **every** index pair. The directions may vary. There are no
virtual completion points in this definition.

A **boundary attachment** is a distinct noncorner array boundary vertex
having an actual unit contact to a source label outside the array. Count
vertices, not contact incidences, and let that count be `r`.

**Theorem 1.1 (proved candidate, source-level attachment).** For each
`delta>0` there exist `epsilon_delta>0` and `D_delta<infinity` such that:
if `P` is a contact-minimal triangle-free global unit-separated
minimum-diameter source, `D=diam P>=D_delta`, and it contains an actual
complete bent array with `a,c>=delta D`, then

`r>=epsilon_delta D`.

Consequently there are at least `epsilon_delta D/5` distinct outside source
labels with unit contacts to the array. No isolate is deleted, moved, counted
as an available site, or replaced in this assertion. These outside labels
are nonisolated by their actual contacts.

The constants are existential; the proof below gives no numerical value for
`D_delta` or `epsilon_delta`.

**Corollary 1.2 (proved candidate, complete-core exclusion).** There is an
absolute `D_0<infinity` such that no canonical triangle-free C-II source of
diameter `D>=D_0` has its entire nonisolated positive-contact core equal to an
actual complete bent array. The cardinality or position of the retained
contact-isolated source population is unrestricted.

Here canonical includes the contact-minimal, then diameter-pair-minimal
normalization, in which every actual diameter endpoint is in the nonisolated
core. This last condition is needed in the finite aspect-ratio argument.
The attachment theorem itself needs only contact minimality and the global
source circumradius estimate, not secondary diameter minimality, ZF,
quarter-fold feasibility, or a supplied phase chart.

```text
actual large complete array + few external contacts
 -> almost every pair of opposite boundary stars is regular
 -> one vertex in each regular pair is an actual source diameter endpoint
 -> global source circumradius puts those vertices near radius D/2
 -> rescaled row and column curves lie on boundaries of two disk lenses
 -> strict transverse monotonicity prevents either curve switching circles
 -> one row shore and one column shore lie on one circle and share a corner
 -> their tangents are parallel, contradicting the 60-to-120 degree window
 -> linearly many actual external contacts are necessary

whole-core complete array
 -> actual diameter-bank geometry gives a,c>D/14 for D>=15
 -> zero external contacts contradicts the attachment theorem
 -> the whole-core complete-array regime is absent for sufficiently large D
```

This closes the supplied **whole-core complete-array model**, including its
potential quadratic isolate population. It does not extract a complete array
from an arbitrary rhombic disk or construct the general full-source finite
quarter-fold endpoint. It is therefore not a Level I resolution.

## 2. Canonical inputs and exact scope

Use [local structure](../theory/01-local-structure.md), Lemma 5.1 and
Theorem 6.1: a diameter endpoint is strictly exposed, while a nonisolated
point with no diameter incidence has unit contacts positively spanning the
plane after contact minimization. Triangle-freeness gives contact degree at
most five. We do not impose separate hull saturation.

Use the promoted [ambient source geometry](../theory/04-ambient-force-and-cap-transport.md),
Section 1: for every global source with `D>16sqrt(3)`, at its full-source
circumcenter,

`|p|<=D/2+eta`, `eta=3^(1/4)sqrt(D)`, for every source point `p`.       (2.1)

This estimate is source-only. Its proof does not assume that a normalized
limiting force hull is the full disk or that diameter directions cover a
circle. Such coverage is not imported here.

If `p` is an actual diameter endpoint, its actual partner `q`, wherever it
is in the source, gives

`D=|p-q|<=|p|+|q|<=|p|+D/2+eta`.

Thus uniformly over **all actual diameter endpoints**,

`D/2-eta<=|p|<=D/2+eta`.                                      (2.2)

No stress weights, selected supports, or inside/outside isolate assumptions
enter (2.2).

For Corollary 1.2, the promoted [ZR/ZF audit](../targets/target-c/57-zr-zf-rigidity-audit.md)
records that actual diameter endpoints belong to the nonisolated core of
the canonical source. Its affine-kernel result applies to that core alone;
we make no claim about an affine kernel on isolate coordinates.

The prior [diameter-forest report](target_c_complete_array_diameter_forest_slot02_2026-10-11.md)
developed the bank decomposition. Section 7 below rederives the elementary
part needed here. Neither its path-parity lemma nor an unreviewed forest
conclusion is required as a premise of this report.

## 3. Direction windows and actual contact stars

Let `alpha_i=arg u_i`, `beta_j=arg v_j`. Fix one `v` direction, and lift all
`alpha_i` into its interval of width `pi/3`. Lift every `beta_j` by its
60-to-120 degree difference from one fixed `alpha`. The provisional pair
differences are in `(0,pi)`, so the strict cell condition has no possible
`2pi` wrap. It follows for every lifted pair that

`pi/3<beta_j-alpha_i<2pi/3`.

For the smallest containing intervals `I_u,I_v`, of widths `Delta_u,Delta_v`,

`min I_v-max I_u>pi/3`,
`max I_v-min I_u<2pi/3`,
`Delta_u+Delta_v<pi/3`.                                       (3.1)

A sum of `m>=1` consecutive vectors in either family has length greater than
`(sqrt(3)/2)m`; its direction remains in the family's interval. Indeed its
projection on the interval bisector is at least `m cos(Delta/2)`, and
`Delta<pi/3`.

**Lemma 3.1.** The only unit contacts between array labels are its designated
consecutive grid edges.

For labels differing only in one index by at least two, the preceding chord
bound is greater than one. If they differ in both indices by `m,n>=1`, let
their positive consecutive sums be `U,V`. Their angle is in `(pi/3,2pi/3)`,
so

`|U+/-V|^2 > |U|^2+|V|^2-|U||V| >= (|U|^2+|V|^2)/2`.

If `(m,n)!=(1,1)`, this is greater than `3(m^2+n^2)/8>=15/8>1`.
If `m=n=1`, the strict rhombic diagonal bounds give `|u+/-v|>1`
directly. This proves the lemma without discarding any array chord.

Call a noncorner boundary vertex **regular** when it has no external unit
contact. Lemma 3.1 makes its full source contact star precisely the three
designated grid neighbors.

**Lemma 3.2 (opposite-star loading).** If both `(i,0)` and `(i,c)` are
regular, for an interior index `1<=i<a`, then exactly one of these two
vertices is an actual source diameter endpoint. The analogous statement
holds for the pair `(0,j),(a,j)` at every regular interior row index.

Let `tau=alpha_i-alpha_(i-1)`. At the two vertices the three contact rays
have enclosing interior angles `pi-tau` and `pi+tau`, respectively: the
intermediate `v_0` or `-v_(c-1)` direction cancels in that angle sum. The
other two gaps are actual rhombic angles, each strictly below `pi`.
If `tau!=0`, one star is strictly inside a half-plane, hence does not
positively span. Contact minimality forces diameter incidence there.
The other star positively spans the plane, so that vertex cannot be
strictly exposed and is not a diameter endpoint.

If `tau=0`, both stars contain exactly opposite horizontal contact rays.
Neither positively spans the plane, so contact minimality would force
diameter incidence. But their vertex is the midpoint of its two unit
neighbors and cannot be strictly exposed. This contradiction rules out
`tau=0` for a regular opposite pair. The row proof interchanges the families.

At most `r` interior column indices and at most `r` interior row indices
have an irregular member of their opposite pair. This counts distinct
source vertices once and does not require the two sets to be disjoint.

## 4. Compactness under a sublinear attachment count

Suppose Theorem 1.1 fails for some fixed `delta>0`. Choose a sequence of
counterexamples with `D_n->infinity`, `a_n,c_n>=delta D_n`, and
`r_n/D_n->0`. This sequence follows directly from failure of any uniform
positive lower bound: take `D_n>=n` and `r_n/D_n<1/n`.

Translate each full-source circumcenter to zero and rotate so that the
bisector of `I_u` is horizontal. Absorb the starting `x_0,y_0` into the
rescaled starting corner `z_n=p_00/D_n`. Define continuous piecewise linear
curves on `[0,1]` by

`X_n(i/a_n)=(x_i-x_0)/D_n`,
`Y_n(j/c_n)=(y_j-y_0)/D_n`.

Every interpolated `z_n+X_n(s)+Y_n(t)` is a convex combination of four
actual array labels, hence lies in the full-source circumdisk (2.1).
This interpolation is an analytic device, not an added source population
or a proposed competitor.

Put `A_n=X_n(1)`, `B_n=Y_n(1)`. Actual endpoint upper bounds and the chord
projection give

`delta<=a_n/D_n<2/sqrt(3)`, `delta<=c_n/D_n<2/sqrt(3)`.          (4.1)

The curves are uniformly Lipschitz, with respective constants `a_n/D_n`
and `c_n/D_n`. The starting corner is bounded by (2.1). By compactness of
the interval endpoints and the Arzela--Ascoli theorem, pass to a subsequence
with uniformly convergent curves `X_n->X`, `Y_n->Y`, starting corner
`z_n->z`, and closed direction windows `I_u,I_v` in the limit. Their widths
have sum at most `pi/3`, and every cross angle lies in `[pi/3,2pi/3]`.
Write `A=X(1)`, `B=Y(1)`; both have positive length.

Positive consecutive coefficients and `det(u_i,v_j)>sqrt(3)/2` give, for
all `s<t`, including partial end segments,

`det(X_n(t)-X_n(s),B_n) >= (sqrt(3)/2)(a_n c_n/D_n^2)(t-s)`.

Similarly

`det(A_n,Y_n(t)-Y_n(s)) >= (sqrt(3)/2)(a_n c_n/D_n^2)(t-s)`.

Taking limits proves the uniform strict transverse monotonicity

`det(X(t)-X(s),B) >= (sqrt(3)/2)delta^2(t-s)>0`,
`det(A,Y(t)-Y(s)) >= (sqrt(3)/2)delta^2(t-s)>0`.                (4.2)

All oriented chords of `X` lie in the closed cone `I_u`, and all oriented
chords of `Y` lie in `I_v`. These cones have width at most `pi/3` and contain
no pair of parallel or antiparallel vectors across the families.

The limit of the full circumdisk constraint is

`|z+X(s)+Y(t)|<=1/2` for all `s,t in [0,1]`.                  (4.3)

Almost every opposite boundary pair is regular. More precisely, the good
interior column indices form a mesh of maximum gap at most
`(r_n+2)/a_n`, which tends to zero; the row mesh has gap at most
`(r_n+2)/c_n`, also tending to zero. Lemma 3.2 and the uniform endpoint
estimate (2.2) imply at every good column index

`max(|z_n+X_n(i/a_n)|,|z_n+X_n(i/a_n)+B_n|) >= 1/2-eta_n/D_n`.

The same maximum is at most `1/2+eta_n/D_n`. Uniform Lipschitz continuity,
vanishing mesh gaps, and `eta_n/D_n->0` therefore give **for every** `s`

`max(|z+X(s)|,|z+X(s)+B|)=1/2`.                             (4.4)

The row version gives **for every** `t`

`max(|z+Y(t)|,|z+A+Y(t)|)=1/2`.                             (4.5)

Thus (4.4)--(4.5) hold at the corners too, even though a corner may have
external contacts and was not assumed loaded. No pointwise subsequence
depending on a boundary position is used.

## 5. A strictly transverse lens path cannot switch active circles

**Lemma 5.1.** Let `R>0`, `b!=0`, and let a continuous path `w(s)` lie in
`L={w:|w|<=R, |w+b|<=R}`. Suppose `max(|w(s)|,|w(s)+b|)=R` for every `s`,
and `det(w(t)-w(s),b)>0` for every `s<t`. Then one fixed circle is active
along the whole path: either `|w(s)|=R` for all `s`, or `|w(s)+b|=R` for
all `s`.

If `|b|>2R`, the lens is empty. If `|b|=2R`, it is a single point and
strict monotonicity is impossible. Hence `0<|b|<2R`. Rotate so that
`b=(0,h)`, `0<h<2R`. Its two boundary circles intersect at

`w=(+/-sqrt(R^2-h^2/4),-h/2)`.

For every lens point `(x,y)`,

`max(|w|^2,|w+b|^2)=x^2+(y+h/2)^2+h^2/4+h|y+h/2|<=R^2`.

The two intersection points are therefore precisely the global extremes
of the perpendicular `x` projection of the lens. Strict monotonicity of
that projection prevents either intersection point at an interior path
parameter. On the connected interval `(0,1)` the path consequently stays
on one circle, since switching circles would require an intersection
point. Continuity includes the endpoints. This proves the lemma. Reversing
the strict monotonicity direction has the identical conclusion.

Apply Lemma 5.1 to `w(s)=z+X(s)`, `b=B`, using (4.2)--(4.4), and to
`w(t)=z+Y(t)`, `b=A`, using (4.2), (4.3), and (4.5). There are fixed
`epsilon_y,epsilon_x in {0,1}` such that

`|z+X(s)+epsilon_y B|=1/2` for all `s`,
`|z+epsilon_x A+Y(t)|=1/2` for all `t`.                       (5.1)

The monotonicity in the second application is reversed in determinant
notation, which the last sentence of the lemma permits.

The two nonconstant curves in (5.1) meet at the actual limiting corner

`p=z+epsilon_x A+epsilon_y B`

on the **same** radius-`1/2` circle centered at zero.

**Lemma 5.2 (the common-corner contradiction).** A nonconstant curve on
a circle, all of whose oriented chords lie in a closed cone of width
less than `pi`, has at each endpoint a chord-direction limit tangent to
that circle. To see this without differentiating the parameterization,
for a chord `h` from a circle point `p` to another circle point,

`2p dot h+|h|^2=0`.

As the other point tends to `p`, any unit chord limit is perpendicular to
`p`. The cone cannot contain both opposing tangent directions, so there
is only one possible limit. At the terminal endpoint use forward-oriented
chords ending there; their limits satisfy the same perpendicularity.
Strict transverse monotonicity guarantees the chords are nonzero.

Apply this to both curves at their common corner. Their tangent limits are
parallel or antiparallel, since they touch the same circle at the same
point. One tangent lies in `I_u`, the other in `I_v`; the cross-angle
restriction `[pi/3,2pi/3]` excludes both parallelism and antiparallelism.
This is the desired contradiction.

No smoothness, bounded total turning, phase convergence rate, lower stress
weight, uniform face-angle margin, or global diameter-direction coverage
has been assumed. In particular the closed limiting 60-degree margins
still exclude parallel tangents.

This proves Theorem 1.1. Each outside source label has at most five unit
neighbors in a triangle-free unit-separated set, so `r` distinct attached
boundary vertices require at least `r/5` distinct outside labels.

## 6. Why the theorem is uniform

The proof has ruled out every sequence with `D_n->infinity`, both array
dimensions at least `delta D_n`, and `r_n/D_n->0`. If no positive uniform
`epsilon_delta` and finite `D_delta` existed, choosing the thresholds
`D_n>=n` and ratios below `1/n` would produce just such a sequence.
This contradiction establishes the exact quantified assertion, not merely
the absence of one particular limiting shape.

When `delta` is too large for (4.1), the assertion is vacuous. For other
fixed positive `delta`, strict transverse monotonicity (4.2) survives
unchanged. There is no interchange of a nonuniform family of limits.

## 7. A whole-core array has both dimensions proportional to D

Suppose the array is the entire canonical nonisolated core. There are no
external unit contacts: a point with such a contact would itself belong
to that core. All noncorner boundary vertices are regular.

If `a>=2`, Lemma 3.2 supplies an actual diameter endpoint `p_i0` or `p_ic`
with an interior column index. Its actual diameter partner is an array
label by the canonical normalization. For any diameter endpoint `p` with
partner `q`, put `n=(p-q)/D`. For every other source point `w`, the actual
upper bound yields

`n dot(w-p)<=-|w-p|^2/(2D)<0`.                               (7.1)

Its two adjacent row contacts force
`n dot u_(i-1)>0`, `n dot u_i<0`. Hence projectively `n` is perpendicular
to a direction in `I_u`. Completeness separates the support of the two
summands. In one of the two oriented normal intervals `+/-J I_u`, all
`n dot v_j` have the same strict sign. The diameter edge therefore joins
rows zero and `c`. Its displacement, up to sign, has the form

`Dn=r+B`, `B=y_c-y_0`,

where `r` is a consecutive `u` sum or its negative. Thus

`|n dot r|<=sin(Delta_u)|r|`, `|r|<=D+|B|`,

and

`D<=sin(Delta_u)(D+|B|)+|B|`.

Since `Delta_u<pi/3` and `|B|<=c`,

`D <= ((1+sin Delta_u)/(1-sin Delta_u))|B|
   < (7+4sqrt(3))c <14c`.                                  (7.2)

If `r=0`, the estimate remains valid directly; in fact completeness
rules out a same-column diameter pair using both cross pairs, but that
extra fact is not needed. The analogous argument, when `c>=2`, gives

`D<14a`.                                                    (7.3)

If `a=1,c>=2`, (7.3) forces `D<14`. If `c=1,a>=2`, (7.2) does the same.
If `a=c=1`, all core pairs have distance at most two, and an actual
diameter pair lies in the core, so `D<=2`. Therefore for `D>=15` both
dimensions are at least two, and (7.2)--(7.3) imply

`a,c>D/14`.

Apply Theorem 1.1 with `delta=1/14` to this array, whose `r=0`. For
`D>=max(15,D_(1/14))` it gives `0>=epsilon_(1/14)D`, a contradiction.
This proves Corollary 1.2 without any isolate population bound or motion.

## 8. Adversarial checks, earlier routes, and limits

The sublinear-contact assumption concerns actual boundary vertices.
Extra source contacts at even a small set of boundary labels can destroy
Lemma 3.2 there; the proof explicitly removes those index pairs and shows
the remaining mesh is dense. Corners may be irregular, and no original
corner is assumed loaded in Theorem 1.1.

The full source, including every isolate, determines the circumcenter,
circumradius, and diameter partners in (2.1)--(2.2). The argument never
uses a core-only global optimality assumption. A disk near one array shore
does not count as an empty insertion region.

The strict unit-cell angle condition is indispensable. The limiting
direction cones can reach the endpoint angles `pi/3,2pi/3`; they cannot
become parallel. Allowing a 180-degree cross window would invalidate the
common-circle contradiction. Mere additive coordinates, or a virtual
completion of missing labels, are insufficient.

Earlier attacks used (i) an isolate population burden, (ii) the finite
diameter-bank path-parity contradiction, and (iii) a full-source Gram shear
when each direction family is constant. The population burden did not
bound exterior storage, and the parity theorem left two forest classes.
The present argument instead couples actual source contacts to global
circumradius and excludes both residual complete-array forest classes.
It applies to bent arrays with arbitrary turning variation.

It does **not** say that every macroscopic rhombic disk contains an actual
complete array of dimensions proportional to `D`, that an incomplete grid
has few attachment vertices, or that general trains obey the separated
two-family direction windows (3.1). Those are new premises which would
need their own source-level theorem. The existence of a large train
crossing graph alone does not supply them.

## 9. Exact finite certificate and next obligation

Run

`python3 research/verify_target_c_large_array_boundary_attachment_2026_10_11.py`.

The saved output is
`research/target_c_large_array_boundary_attachment_certificate_2026_10_11.json`.
The checker verifies exact rational lens intersection/extremality identities,
the common-circle chord-to-tangent identity, regular opposite-star sign
cases, determinant monotonicity on rational bent arrays, and the exact
aspect constant `7+4sqrt(3)<14`. Its fixtures model finite geometric
ingredients. They do not model global optimality or prove the compactness
argument, universal source circumradius, or a numerical value of `D_0`.
The analytic proof is Sections 2--7.

**One exact next obligation:** extract from every remaining canonical
quadrilateral survivor an actual complete bent array with `a,c>=delta D`
for some absolute `delta>0` and fewer than `epsilon_delta D` distinct
noncorner vertices having source contacts outside that array, or prove a
different source-level endpoint in the complementary regime. A theorem
giving the stated extraction would contradict Theorem 1.1. Neither
independently supplied charts nor virtual grid points fulfill it.

No canonical state, dependency edge, or registered certificate is changed.
