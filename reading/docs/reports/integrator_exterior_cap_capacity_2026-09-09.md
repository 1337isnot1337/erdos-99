> Generated reading edition · [exact source](../../../docs/reports/integrator_exterior_cap_capacity_2026-09-09.md) · source SHA-256 `bedc15cdaf5d82cd38a6be3b029f724ab979c7a7c583bbaa14be925dcab5cf3d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-869730602C2C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — exact exterior-cap capacity transport

**Date:** 2026-09-09
**Run type:** cross-target packing / finite-container theorem
**Targets:** A source capacity; B Oler shell; C exterior force-hull population
**Dependencies:** canonical finite Oler inequality, strict global lattice bound,
diameter endpoints are source-hull vertices
**Computation/literature:** no computation in proofs; no new literature

## LEVEL I STATUS

`STILL OPEN`

**Promotion scope:** the Target C route map and shared integrator module promote
EC/EP/ES (Sections 1–5 and 7). Numerical Section 6 remains conditional.

This report proves an exterior-population upper bound complementary to the ER lower
bound. It also gives an exact decomposition of the remaining finite packing slack.
It does not declare external points absent, move them, or create a compatible
scaffold exchange.

## 1. Endpoint and objects

Let `A` be any unit-separated global minimum-diameter planar source with diameter
`D`, and let `K=conv A`. Let `E` be any subset of the extreme vertices of `K` whose
convex hull `F=conv E` is two-dimensional. In particular, `E` may be the endpoint
set of a selected normalized KKT diameter support, or the full actual diameter
endpoint set in C-II. Write

$$
a_0=\sqrt3/2,\quad P_K=\operatorname{per}(K),\quad
P_F=\operatorname{per}(F),\quad Z=|A\setminus F|.
$$

The desired bridge is

```text
diameter endpoints are actual source-hull vertices
  -> convex, disjoint exterior caps between K and F
  -> exact Oler capacity sum for the actual external population
  -> upper and lower population bounds with matching quadratic term
  -> boundary-order total capacity slack, suitable for a protected rearrangement.
```

The role of global optimality is explicit: the cap decomposition and finite upper
bound hold for arbitrary feasible sources. Global optimality supplies the matching
lower bound and the `O(D)` total slack.

## 2. Convex exterior-cap partition

List `E` in its cyclic source-hull order. For each consecutive pair `u,v`, the
oriented chord `uv` is a side of `F`. If the source-hull arc from `u` to `v`
coincides with that chord, call it common. Otherwise the arc and chord bound a
nondegenerate convex cap `K_i`, lying on the opposite side of the chord from
`int F`. Let `k` be the number of nondegenerate caps and `P_com` the total length
of the common sides. If `F=K`, use `k=0` and `P_com=P_F`.

### Lemma EC.1

The caps have pairwise disjoint interiors and partition `K\F` up to their chord
boundaries. Every external source point belongs to exactly one cap away from its
closing chord. If `A_i=area(K_i)` and `P_i=per(K_i)`, then

$$
\sum_i A_i=\operatorname{area}(K)-\operatorname{area}(F),
\tag{EC.1}
$$

$$
\sum_i P_i=P_K+P_F-2P_{\rm com}.
\tag{EC.2}
$$

### Proof

A chord joining two vertices of a convex polygon cuts it into the convex hulls
of its two boundary arcs. Because `u,v` are consecutive in `E`, every other
selected vertex lies on the other arc. The cap is the intersection of `K` with
the exterior closed half-plane of this side of `F`, hence is convex.

The chords form the noncrossing boundary of the inscribed polygon `F`. Cutting
along them partitions `K` into `F` and precisely the arc caps. This also proves
disjointness and the assignment of points. In the perimeter sum, every
noncommon source arc occurs once and every noncommon chord occurs once. The
common sides occur in neither cap sum, giving EC.2. QED.

This uses the fact that the vertices of `F` are actual extreme vertices of `K`.
An arbitrary interior convex container does not have this partition.

## 3. Theorem EC — finite exterior-population upper bound

Let `z_i` count the external source points assigned to `K_i`, so `sum z_i=Z`.
The two chord endpoints are additional, distinct source points. Applying Oler
to these `z_i+2` points inside the convex cap gives

$$
z_i\le A_i/a_0+P_i/2-1.
\tag{EC.3}
$$

Summing EC.3 proves

$$
\boxed{Z\le
\frac{\operatorname{area}(K)-\operatorname{area}(F)}{a_0}
+\frac{P_K+P_F}{2}-P_{\rm com}-k.}
\tag{EC.4}
$$

No source points are deleted in this argument. Endpoints shared by several
containers are counted separately within each Oler application and canceled
explicitly by the `-k` and perimeter terms.

Since both hulls have diameter at most `D`, EC.4 gives the simpler bound

$$
\boxed{Z\le
\frac{\pi D^2/4-\operatorname{area}(F)}{a_0}+\pi D.}
\tag{EC.5}
$$

## 4. Theorem EP — the external density equals the missing area density

The strict global comparison `D(n)^2<(2sqrt(3)/pi)n` gives
`n>pi D^2/(4a_0)`. Oler inside `F` gives

$$
n-Z\le\operatorname{area}(F)/a_0+P_F/2+1.
$$

Thus

$$
Z>\frac{\pi D^2/4-\operatorname{area}(F)}{a_0}-P_F/2-1.
\tag{EP.1}
$$

Combining with EC.5,

$$
\boxed{-\pi D/2-1
< Z-\frac{\pi D^2/4-\operatorname{area}(F)}{a_0}
\le\pi D.}
\tag{EP.2}
$$

The stronger canonical `n-1` comparison improves the harmless constant `1`, but
is not needed here. In particular, for any unbounded sequence of global sources,

$$
\boxed{\frac{Z}{D^2}
=\frac{2}{\sqrt3}\left(\frac\pi4-
\frac{\operatorname{area}(F)}{D^2}\right)+O(D^{-1}),}
\tag{EP.3}
$$

uniformly over the chosen extreme-vertex subsets `E`.

This is a two-sided law. In the C-II application, all these external source
points are contact-isolated by full support and the force-hull definition.
The [ER report](target_c_external_rattler_force_area_dichotomy_2026-09-09.md)
proved the lower direction; an area floor alone cannot bound `Z` from above
using that direction. EC supplies the needed missing upper direction.

## 5. Theorem ES — exact simultaneous cap-capacity slack

For a convex body `L` containing a specified unit-separated population `N_L`,
write its dimensionless Oler slack as

$$
\sigma(L,N_L)=\operatorname{area}(L)/a_0+
\operatorname{per}(L)/2+1-N_L\ge0.
$$

Let `sigma_K=sigma(K,n)`, `sigma_F=sigma(F,n-Z)`, and
`sigma_i=sigma(K_i,z_i+2)`. Then

$$
\boxed{\sigma_F+\sum_i\sigma_i
=\sigma_K+P_F-P_{\rm com}-k.}
\tag{ES.1}
$$

### Proof

The total area is `area(K)`. The total perimeter over `F` and the caps is
`P_K+2P_F-2P_com` by EC.2. There are `k+1` Oler constants, and the total counted
population is `(n-Z)+sum(z_i+2)=n+2k`. Substitution gives ES.1. QED.

Global optimality and isodiametry imply
`sigma_K<P_K/2+1`. Consequently

$$
\boxed{0\le\sigma_F+\sum_i\sigma_i
< P_K/2+P_F-P_{\rm com}-k+1
\le3\pi D/2+1.}
\tag{ES.2}
$$

This transports Target B's exact shell accounting into Target A's finite
container-capacity language on the actual Target C source. If `alpha_1(L)` is
the maximum unit-separated population in `L`, then Oler also gives

$$
0\le\alpha_1(F)-(n-Z)\le\sigma_F,
$$

$$
0\le\alpha_1(K_i)-(z_i+2)\le\sigma_i.
\tag{ES.3}
$$

Therefore the sum of these independent container-capacity deficits is bounded
by ES.2. This is not a simultaneous realizability claim: separate optimal cap
packings may collide across their shared interfaces.

For any cap sequence with `A_i=Omega(D^2)`, the uniform perimeter bound from
EC.2 and ES.2 imply

$$
z_i=A_i/a_0+O(D).
\tag{ES.4}
$$

Thus every macroscopic external cap is filled at asymptotically triangular bulk
density. Exact unit triangles need not occur: the near-equilateral equality
well remains a binding obstruction.

## 6. Conditional numerical consequence of ambient-force integration

Under the additional report-level DB assumptions, the
[ambient-force theorem](integrator_ambient_force_geometry_2026-09-09.md), AD.4,
gives `liminf area(F)/D^2>=A_int=0.6184708847...`. Hence EP.3 gives

$$
\boxed{\limsup\frac{Z_{\rm ext}}{D^2}\le
\frac{2}{\sqrt3}\left(\frac\pi4-A_{\rm int}\right).}
\tag{EN.1}
$$

Since `n/D^2 -> pi/(2sqrt(3))`, equivalently

$$
\boxed{\limsup\frac{Z_{\rm ext}}n
\le1-\frac{4A_{\rm int}}\pi<0.213.}
\tag{EN.2}
$$

Over 78.7 percent of the source population is therefore inside the force hull
in this conditional regime. These points need not be in the force-carrying
contact core; interior isolates are fully retained.

## 7. Regression and failure audit

| Candidate inference or test | Classification |
| --- | --- |
| All external points lie in convex cap containers | Proved because `E` consists of actual source-hull vertices. |
| Same assertion for an arbitrary interior force-like polygon | Not asserted; vertex alignment is essential. |
| Heptagon plus isolated center | Compatible: with its hull as `F`, `Z=0`; the isolated center is counted inside `F`. |
| All sources satisfying EP are globally optimal | Rejected converse. The theorem only supplies necessary conditions. |
| Near-triangular cap density forces a unit triangle | Rejected; exact contacts do not follow from asymptotic density. |
| Independent cap replacements are mutually feasible | Not proved; interface distances remain necessary. |
| Boundary-order capacity slack solves A | Rejected: neither the source-specific Schur inequality nor a strict diameter improvement follows. |
| EN gives 78.7 percent force-visible points | Rejected: it gives points inside the geometric force hull, including isolates. |

## 8. Promotion recommendation and next obligation

EC, EP, and ES are promoted after the integrator proof/scope audit, using only
the stated canonical inputs. EN remains conditional on DB. The finite cap
partition identities were additionally checked on 675 reproducible examples by
`research/integrator_ambient_force_audit.py`; those floating-point checks are
not the proof and do not certify global optimality.

The precise remaining cap route is a **protected replacement theorem**: use an
actual cap's near-capacity population, its fixed chord interface, and the source
diameter constraints to construct a feasible replacement which yields an
`n`-point configuration of diameter strictly less than `D`. A same-`D` extra
point alone is insufficient without a plateau/diameter-improvement argument.

The exact simultaneous slack ES.1 identifies what such a theorem must recover.
It cannot discard `O(D)` interface terms when the intended gain is one point.
