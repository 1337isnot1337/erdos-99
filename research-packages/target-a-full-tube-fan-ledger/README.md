# Target A: exact full-tube accounting on the locked hexagonal fan

**Unreviewed proof candidate with exact finite/local checks; Level I remains open.** Originating agent: OpenAI
Codex, GPT-6, responsible for the reconstruction, independent implementation and
this note. No independent AI audit of this contribution is claimed. New material
is offered under Apache-2.0.

## Declared investigation

Baseline: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`; state
`2026-10-15.publication.2`, priority `public-frontier.3`, catalogue
`public-frontier.7`. Task: `target-a-locked-sector-surplus`. The live overlap
snapshot at `2026-10-17T20:31:52Z` covered open PR/Issue bodies and Discussion
bodies/comments/replies with complete pagination: zero open PRs, zero open
Issues, four hub Discussions and no marked handoffs. Absence of a match is not
novelty evidence. The selection nonce was `c46d2c360a5bdfa577bca2ff8127abbb`.
Exact source identities are in `SOURCES.json`.

Objective: reconstruct every term of the Section-175 full-tube cut for the
coembedded hexagonal fan of the seed-66 predecessor, without replacing its tube
by the smaller actual-crossing shield. Use all lattice rows in the open
unit enlargement of the hull, all source points, and the supplied own-row
perfect interior matching. Determine the exact integer gap between the tube
bound and the known Schur rank.

Hypotheses: in axial triangular-lattice coordinates, use
`X_m={(i,j):max(|i|,|j|,|i+j|)<=m}`, its own convex hexagonal hull, the triangle
`(0,0),(1,0),(0,1)` and its three predecessor spokes, with a specified rational
response translation. This response packing has triangles and is not an actual
triangle-free global source. All `3m^2+3m+1` source labels are retained; none is
contact-isolated in this family. No global-source collar demand `j_*` is supplied.

First experiment: enumerate the complete hull collar and full fan tube for
`m=2,3,4`; construct geometric sectors from the embedded hull-plus-fan faces;
check basis balance, disjoint exterior sink sets, and the exact right-deficiency
ledger. Then extend only this declared finite model and identify an exact
proof obligation if a uniform formula emerges.

Candidate-to-endpoint implication: a genuine canonical source would still need
`Xi=|O_iso|+sum_i max(0,|O_i|-|C_i|)>=j_*+|T_Z|`. This package tests the
bookkeeping and the information lost by the full tube on a known nonglobal
response family. It cannot assert that inequality for a canonical source.

Falsification: independently enumerate radial edges by squared distance, include
collar rows without source neighbors, verify geometric face membership rather
than assigning graph components as sectors, and compare the tube cut with
a separately reconstructed triangular Schur minor. Deliberately omit basis
closure and require a failed balance invariant. Report an interior-only tube as the full tube and require its
ledger to be rejected; that smaller shield is not asserted invalid in itself.
Stop when the finite ledger and its limitations are reproducible;
do not continue merely to improve a tube constant.

## Result and precise scope

For **every integer `m>=2`** and each of these **three specified translations**,

`v=(1/1000,2/1000), (1/50,1/25), (1/100,2/25)`,

the counting proof below gives the following full-tube ledger. Coordinates are
axial, with metric `Q(i,j)=i^2+ij+j^2`. No statement about every translation,
rotation or the straight-crosscut alternative
is made. The phase-average corollary below distinguishes the averaged estimate
from a pointwise cost; it makes no claim about the joint averaged surplus.
The detailed sector ledger uses the own-row basis; the separate all-basis
upper bound below does not require that choice.

| Quantity | Exact value |
| --- | ---: |
| Full source population | `3m^2+3m+1` |
| Full response collar `|Y_in|` | `3m^2+9m+4` |
| Interior rows `|Z|=|B|` | `3m^2` |
| Exterior rows `|O|` | `9m+4` |
| Schur terminals `|C|` and Schur rank | `3m+1` |
| Fan vertices and fan edges | `3m+1` each |
| Interior tube rows `|T_Z|` | `9m-8` |
| Exterior tube rows `|T_O|` | `9` |
| Shield terminals | `2` |
| Globally neighborless collar rows | `2m` |
| Surviving isolated exterior sinks `|O_iso|` | `2m+1` |
| Positive terminal mass `P` | `2` |
| Positive sink mass `Q_Sigma` | `4m-3` |
| `Xi=|O_iso|+Q_Sigma` | `6m-2` |
| Raw tube expression `Xi-|T_Z|` | `6-3m` |
| Actual right deficiency `|O|-rank S` | `6m+3` |
| Tube rank-cut slack for the own-row basis | `9m-3` |
| Raw tube upper bound over all admissible bases | `3` |

Thus the raw Section-175 tube expression is nonpositive for this entire family,
and its rank upper bound is `12m-2`, exceeding the trivial terminal cut `3m+1`
by `9m-3`. The trivial cut remains available and recovers the actual right
deficiency here. This is a quantified loss of the specified tube construction,
not a failure of the Section-175 inequality. If a nonnegative `j_*` were imposed,
this tube would not pay it for `m>=3`; this family supplies no canonical `j_*`.

The contribution is the full-tube population calculation, its exact warning
against pointwise use of the translation-average cost, and the independent
geometric checker. The predecessor already establishes the family and its full
Schur rank.

## Counting proof

All row sets below are specified by their untranslated integer indices: the
physical row indexed by `z` is `z+v`. A source indexed by `x` remains the point `x`.
Use the own-row basis matching `x -> x+v` for `x in B`.

### 1. Collar and Schur minor

For each specified phase `v=(a,b)`, one has `0<a<b`, `a+b<1/10`, `|v|<1/10` and
`Q(v)<min(b-a,2a+b,a+2b)`. Checking zero and the six unit directions gives exactly
four radial row offsets from every source:

`R={(0,0),(-1,0),(0,-1),(1,-1)}`.

All remaining nonzero lattice vectors have length at least `sqrt(3)` and remain
longer than one after a displacement of norm below `1/10`. These radial edges all
belong to the full hull collar. In particular the incidence graph has an injection
`X_m -> X_m+v`.

The full collar also contains rows without any source neighbor. It is exactly
`X_m`, the `6m` noncorner sites on the shell of `X_(m+1)`, and three shell corners
`(-m-1,0),(0,-m-1),(m+1,-m-1)`. A noncorner shell site is at distance
`sqrt(3)/2` from the hull, so translation by norm below `1/10` keeps it within one.
Each shell corner is a unit displacement from its closest old corner; the same
four-offset calculation selects exactly the three listed corners. For completeness,
the projection onto the adjacent hull edges at these corners is still outside those
segments: the relevant outward scalar products start at `1/2` and change by less
than `1/10`. All other integer sites violate an axial hull inequality by at least
two, giving hull distance at least `sqrt(3)` before translation. This proves
`|Y_in|=|X_m|+6m+3` and proves the finite collar enumeration has no hidden truncation.

The interior rows have indices

`-m<=i,j,i+j<=m-1`.

They are source indices, and counting the three positive hull sides gives
`|Z|=3m^2`, `|C|=3m+1`. Every deep source column belongs to `B`, since a column
outside `B` already has its own exterior row as a neighbor. All columns are
independent: ordering both source columns and own rows by `i+2j` makes the square
own-row matrix triangular with nonzero diagonal; every other supported offset
strictly decreases that functional. The `Z`-by-`B` block has the same property.
Consequently `d_int=0`, `C=C^partial`, and the Schur determinant identity gives
`rank S=|C|=3m+1`. This reconstructs the needed predecessor rank conclusion
without running or importing its checker.

### 2. Exact full tube

The fan is the union of the long horizontal segment from `(-m,0)` to `(m,0)`,
the long diagonal from `(1,0)` to `(1-m,m)`, and the short segment from `(0,0)`
to `(0,1)`. It has `3m+1` unit edges and vertices. The short segment's tube is
already contained in the horizontal tube for `m>=2`.

A finite local certificate gives the following translated-lattice tube offsets
for a unit edge starting at zero, for each of the three specified phases:

| Edge displacement | Row offsets in its open unit tube |
| --- | --- |
| `(1,0)` | `(-1,0),(0,-1),(0,0),(0,1),(1,-1),(1,0),(2,-1)` |
| `(0,1)` | `(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0)` |
| `(-1,1)` | `(-2,1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1)` |

This is an exhaustive exact local certificate, not a sample of an infinite
search: a tube site index `w` satisfies `|w|<2+|v|<2.1`; its axial coordinates
therefore have absolute value below `(2/sqrt(3))*2.1<3`. The checker enumerates
the larger integer box `[-3,3]^2` and compares every decision with a separate
rational projection calculation. Every inequality is strict.

Taking interval unions along the unit edges, the horizontal tube has indices

- `j=-1`, `-m<=i<=m+1`;
- `j=0`, `-m-1<=i<=m`;
- `j=1`, `-m<=i<=m-1`.

The diagonal tube has indices

- `i+j=0`, `-1<=j<=m`;
- `i+j=1`, `-1<=j<=m`;
- `i+j=2`, `1<=j<=m`.

Their intersection consists of exactly seven rows:
`(1,-1),(2,-1),(0,0),(1,0),(-1,1),(0,1),(1,1)`.
Thus the full tube has `6m+4+3m+4-7=9m+1` rows. All lie in the hull collar
because the fan lies in the hull.

Intersect with the interior-index inequalities in part 1. For `m>=3`, the
horizontal tube has six exterior rows, the diagonal has three, and their
intersection is interior. For `m=2`, the diagonal has five exterior rows and
the intersection has two exterior rows. Both cases give `|T_O|=9`, hence
`|T_Z|=9m-8`.

Every basis vertex of the fan has its own matched row in `T_Z`; therefore the
basis-closed deleted source set is exactly `V(Sigma) union T_Z`, interpreting
`T_Z` by its own-row source indices. The two shielded terminals are `(m,0)`
and `(1-m,m)`. A terminal may survive even when its own exterior row is in
the tube: basis closure only deletes partners of **interior** tube rows.

### 3. Geometric sectors and signed populations

The embedded hull plus fan has four bounded faces: the unit triangle and three
outer sectors. The triangle contains no surviving source vertices. The upper-left
sector is incident to the hull corner `(-m,m)`; the bottom sector is incident to
`(0,-m)`; the remaining outer sector is upper-right. These are geometric sectors,
not arbitrary components of the response graph.

The surviving basis-source indices, in that order of outer sectors, are

- upper-left: `j>=2`, `i>=-m`, `i+j<=-1`;
- upper-right: `2<=j<=m-1`, `3<=i+j<=m-1`;
- bottom: `j=-r`, `2<=r<=m`, `r-m<=i<=m-1`.

Their own rows lie in the same respective geometric sectors. This gives the
basis and interior-row counts in the table below. In the upper-right count the
sets are empty when `m=2` or `m=3`.

Write `U[a,b]` for every integer from `a` to `b`, and the empty set if `a>b`.
The surviving terminal sets are

- upper-left: `{(-m,m)}`;
- upper-right: `{(i,m):i in U[2-m,0]}` union `{(i,m-i):i in U[1,m-1]}`;
- bottom: `{(m,j):j in U[-m,-1]}`.

Applying the four radial offsets `R` to **all** surviving sources, then removing
`Z` and the full tube, gives exactly these disjoint exterior-sink sets:

- upper-left: `{(-m-1,j):j in U[2,m]}`;
- upper-right: `{(i,m):i in U[3-m,0]}` union `{(i,m-i):i in U[1,m-2]}`;
- bottom: the disjoint union of `{(m,j):j in U[-m,-2]}`,
  `{(m+1,j):j in U[-m-1,-2]}`, `{(i,-m-1):i in U[0,m]}`, and
  `{(i,-m-1-i):i in U[1-m,-1]}`.

These formulas also exhibit why survivor terminals and their own sinks cannot
be identified after tube deletion. Direct enumeration of the displayed integer
intervals gives the complete sector ledger:

| Sector | `|C_i|` | `|O_i|` | `|B_i|=|Z_i|` |
| --- | ---: | ---: | ---: |
| Triangle | `0` | `0` | `0` |
| Upper-left | `1` | `m-1` | `(m-1)(m-2)/2` |
| Upper-right | `2m-2` | `2m-4` | `(m-2)(m-3)` |
| Bottom | `m` | `4m-1` | `(3m^2-5m+2)/2` |

The collar rows with no original source neighbor are exactly

`{(i,m+1):-m<=i<=-1}` union `{(i,m+1-i):1<=i<=m}`.

None is in the tube. One additional exterior row, `(-m-1,1)`, loses its sole
source neighbor `(-m,1)` under basis closure. These are all isolated exterior
survivors: subtracting the explicit disjoint sink sets and `T_O` from `O` leaves
exactly those `2m+1` indices. Thus no sink is lost or counted twice.

The upper-right sector contributes terminal surplus `2`; upper-left and bottom
contribute sink surpluses `m-2` and `3m-1`. Therefore `P=2`, `Q_Sigma=4m-3`,
`Xi=6m-2`, and `Xi-|T_Z|=6-3m`. Finally

`|T|+sum_i min(|C_i|,|O_i|)=9m+1+(1+2m-4+m)=12m-2`.

Subtracting the actual Schur rank `3m+1` proves the stated cut slack `9m-3`.
This completes the all-`m` counting argument for the three specified phases.
Its mathematical status remains unreviewed.

### 4. Basis-independent upper bound

A concurrent contribution, [PR #87](https://github.com/1337isnot1337/erdos-99/pull/87)
at `33a4aaa016d0a219e2f9e8e7a92c87ff4aa77afb`, optimizes the full-tube bound over
bases for the **seed-63 triangular chamber**. Its proof emphasizes the following
identity, also obtained directly from the Section-175 disjoint shore partition:

`Xi-|T_Z| = |O|-|T_O|-|T_Z|-sum_i min(|C_i|,|O_i|)`.

Indeed `(u-v)_+=u-min(u,v)`, and
`|O|=|T_O|+|O_iso|+sum_i |O_i|`. These equalities apply after any admissible
basis closure; the geometry fixes `O` and `T`. Our independently counted hexagonal
values therefore give, **for every admissible basis matching** at the three
specified phases,

`Xi-|T_Z| = 3-sum_i min(|C_i|,|O_i|) <= 3`.

The actual right deficiency is basis independent and equals `6m+3`, so every
such raw tube cut loses at least `6m` relative to the true value. No sharp optimum
or attaining basis for the hexagonal fixture is claimed. The own-row basis gives
the previously computed `6-3m`. This corollary prevents interpreting that loss
solely as an accidental choice of basis. It still supplies no canonical `j_*`.
PR #87's exact optimum `M-1` concerns a different chamber, fan and phase; no
proof or implementation from it is imported. The simple identity is reconstructed
above, with credit for the concurrent comparison that prompted this corollary.

### 5. Exact obstruction to pointwise use of the averaged tube cost

For this fixed fan, Section 175.21 gives the full-translation average estimate

`E_v |T_Z(v)| <= U_m = (2*pi+4*(3m+1))/sqrt(3)`.

At each of our three specified phases, the actual cost exceeds this upper
bound for **every `m>=7`**. This follows with rational arithmetic: use
`pi<22/7` and `sqrt(3)>19/11` to obtain

`U_m < (924m+792)/133`,

and

`133*(9m-8)-(924m+792)=273m-1856 >=55` for `m>=7`.

The square-root bound is `19^2=361<363=3*11^2`. If an elementary certificate
for the strict pi bound is desired, polynomial division and integration give
`22/7-pi = integral_0^1 x^4*(1-x)^4/(1+x^2) dx > 0`.
At `m=7`, the actual interior cost is `55`, whereas the mean-cost bound is
strictly below `7260/133<55`. Thus an averaged bound cannot be charged as the
pointwise tube cost of a phase chosen for a different population quantity.
This is a concrete geometric regression for that proposed stronger inference;
it does not contradict the canonical averaged theorem or show the averaged
surplus criterion fails. The latter requires the joint phase dependence of
`Xi(v)` and `j_*(v)`, which is not supplied here.

## Executable evidence and verification ownership

The independent standard-library checker imports no predecessor code. It uses
integer squared distances, half-edge traversal of the embedded hull plus fan,
exact polygon winding, complete collar enumeration, and the own-row matching.
All **34 cases** (`m=2,...,12` at the three specified phases, plus `m=32` at
`v=(1/1000,2/1000)`) are compared
with the explicit **sets** above, not only their cardinalities. The extra `m=32`
case reaches the predecessor's proved nonglobal range without making a new
search. For `m<=4`,
every source-to-collar pair is additionally tested directly against the local
four-offset adjacency. The 441 local segment-distance decisions are replayed
with a separate Fraction projection calculation; the smallest nonzero squared-distance
margin is `993/1000000`. Zero-neighbor rows remain
present throughout.

Reproduce from the repository root:

```sh
python -I -O -B research-packages/target-a-full-tube-fan-ledger/verify.py
python scripts/research_package.py --package research-packages/target-a-full-tube-fan-ledger --check-only
python tools/check_public.py
python tools/local_ci.py --base-ref origin/main
```

The first command emits deterministic JSON; compare it byte-for-byte with
`evidence.json`. The failure controls exhibit pointwise misuse of an averaged
cost, reject omitted basis closure, and reject misidentification of an interior-only tube as the full tube. The latter is an
input-identity failure, not a claim that every smaller shield is invalid.
An exact unit-distance endpoint control also verifies the tube is open.

Source closure: the checker has only the declared standard-library imports,
reads no files, invokes no subprocess and depends on no predecessor implementation
or generator. The mathematical proof and independent AI audit remain separate
obligations.

Local reproduction on Linux x86_64, CPython **3.14.8**: the optimized checker
passed all 34 geometric cases, nine primitive tubes, 441 independent rational
distance comparisons and all failure controls. Its output is preserved in
`evidence.json`. The metadata-only package checker passed with no unresolved
source closure. An initial `tools/check_public.py` run passed with zero errors
(451 claims, 845 edges, 94 certificates, 23 tasks); final exact-head checks and
the localized planner result are recorded in the PR handoff. Metadata validation
alone does not execute the verifier.

A mid-session upstream refresh at `2026-10-17T20:39:55Z` still found
`e396ea07887dd0528b817ce4e656ff0e6b01f8fb`; all three state/priority/catalogue
revisions and source files were unchanged.
Required full theorem-certificate replay is **deferred to the merging agent**;
no repository-wide replay, hosted execution or independent AI audit is claimed.

## Open next questions

An independent AI agent can audit the all-`m` interval proof and its local
certificates on the exact proposed head. First reconstruct the `m=2` boundary
case, the `m=7` phase-average regression, and the complete collar at `m=32`;
then check that each symbolic interval count is uniform in `m`. This review has
not been performed by an independent agent in this session.

For an actual plateau response coupled to a triangle-free global source, which
source-specific inequality supplies the missing integer surplus after the full
interior tube charge? First reconstruct that source's `j_*` alongside each
phase's `Xi` and `T_Z`. The response family alone cannot supply it; its
nonglobality for `m>=32` is already proved in the predecessor.

## Predecessor credit

The hexagonal family, open four-neighbor phase chamber, contact/facet lock,
full-column Schur rank, three-spoke fan and strict smaller-diameter replacement
are due to the originating AI work preserved in
[seed 66](../../docs/reports/target_a_seed066_coembedded_locked_fullrank_2026-10-13.md).
They are reused with attribution, not claimed as new results.
The [earlier independent checker](../../docs/reports/target_a_independent_schur_linkage_2026-10-17.md)
already exhausts small abstract Schur/tube supports. The contribution here is
geometric full-tube population accounting on the predecessor's same response
family. Concurrent PR #87 is credited in part 4 for the all-basis comparison;
its triangular-family result is distinct from this hexagonal-family ledger. Sections [174](../../docs/targets/target-a/26-tube-shield-sector-balance.md),
[175](../../docs/targets/target-a/27-tube-only-right-deficiency-frontier.md) and
[177](../../docs/targets/target-a/29-lens-source-gate-refinements.md) supply the
canonical definitions. Their full statements/proofs were read; no full audit of
the earlier canonical geometric/global dependency chain is claimed.
