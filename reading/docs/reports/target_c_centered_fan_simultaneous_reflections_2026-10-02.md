> Generated reading edition · [exact source](../../../docs/reports/target_c_centered_fan_simultaneous_reflections_2026-10-02.md) · source SHA-256 `5a39dd0904fd4564bbb552a13d0322d43052fea76aa328e85b9b20cbe7f73f25`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B83A9F8D0B8D","canonical":true,"claim_ids":["C-CENTERED-FAN-REFLECTIONS"],"claim_statuses":{"C-CENTERED-FAN-REFLECTIONS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: simultaneous fan reflections and injective inactive blockers

`centered diameter bulk -> separated independent fan leaves -> simultaneous
contact-preserving nonexpansive full-source reflection -> only fixed inactive
lower blockers remain -> still requires their simultaneous repair for a
canonical-source competitor -> Level I after the other branches are closed`.

**Date:** 2026-10-02.\
**Research base:** `46cdb4fd3cb5f078f298fa51857e23e321ac9204`.\
**Checkpoint parent:** `75a0c8e9`.\
**State:** `2026-09-14.audit.51`; Level I and C-II OPEN.\
**Branch:** `swarm/sol/stress-support-curvature-20261002`.\
**Classification:** canonical in `2026-10-05.audit.58` as `C-CENTERED-FAN-REFLECTIONS`; the finite packets remain nonglobal illustrations/regressions rather than canonical source examples.

This continues the [centered-bulk packet](target_c_midpoint_bulk_braid_2026-10-02.md).
The previous [single-fan-flip report](../../research/target_c_degree2_fan_flip_linear_fork_2026-10-02.md)
already proves single-vertex nonexpansiveness and interior/inactive blocker
localization. We rederive the distance identity used here. The new statements
are the separation of distinct selected leaves, simultaneous nonexpansiveness,
and exact factorization of the lower obstruction. These registered statements are independently audited and canonical in audit.58.

## 1. Finite hypotheses

Let A be any finite unit-separated planar source of diameter D>=5. Retain all
source points. A selected internal fan leaf p has a unique actual diameter
partner a_p, exactly two unit-contact neighbors p_-,p_+, and

`|p-a_p|=|p_--a_p|=|p_+-a_p|=D`, `|p-p_-|=|p-p_+|=1`.

Let S be a collection of such leaves, independent in the old unit-contact
graph. Suppose their actual diameter midpoints m_p=(p+a_p)/2 satisfy
$$
|m_p-s|\le T,\qquad T<(D-2)/(2\sqrt2).
\tag{SR.1}
$$
Define the complete source map, fixing every unselected point, by
$$
F(p)=p-(p-a_p)/D^2\quad(p\in S),\qquad F(x)=x\quad(x\notin S).
\tag{SR.2}
$$
This is the reflection of p in the line p_-p_+: with unit chord angle
`a_D=2 asin(1/(2D))`, its inward displacement is exactly 1/D.

## 2. Exact separation of the selected leaves

First, each fan contact p p_+ and p p_- is a side of the **full source** hull.
All source points lie in B(a_p,D). In coordinates centered at a_p, a unit
chord's endpoints are `(sqrt(D^2-1/4), +/-1/2)`. Every point in the minor
closed disk cap beyond this chord is within distance <1 of the nearer endpoint:
its distance squared is at most

`(D-sqrt(D^2-1/4))^2+1/4<1`.

Thus no other source point is in that cap or on the chord segment. Its endpoints
are strict source-hull vertices, because they are actual diameter endpoints.
Consequently the chord is a complete hull side and p_-,p_+ are p's two immediate
neighbors on the full source hull. Contact isolates cannot be hidden in the cap.

### Lemma SR.1

Any two distinct selected leaves satisfy `|p-q|>=sqrt(2)`. More generally the
same bound holds for a selected p and any other actual diameter endpoint q
outside `{p,p_-,p_+}`, provided one of q's actual diameter midpoints is also
within T of s.

**Proof.** Suppose d=|p-q|<sqrt(2). Their actual outward diameter normals are
`n_p=(p-a_p)/D`, `n_q=(q-a_q)/D`. Since
$$
D(n_p-n_q)=2(p-q)-2(m_p-m_q),
$$
the ordinary smaller angle theta between them satisfies
$$
\sin(\theta/2)\le(d+2T)/D<1/\sqrt2,
$$
so theta<pi/2. They are distinct normals, since a fixed oriented normal has
unique diameter support endpoints. Along the hull chain corresponding to this
short normal interval, every side normal is between n_p and n_q. Projection
onto its bisector tangent therefore bounds each side vector below by its length
times cos(theta/2).

Since q is not either fan neighbor of p, that chain contains
at least two full hull sides. Their endpoint distances are each >=1 by source
separation, including sides ending at contact isolates. Summing the projections
gives
$$
d\ge2\cos(\theta/2)>\sqrt2,
$$
contradicting the assumption. QED.

This lemma uses ordinary exposed-normal order, not an incident-diameter
Euler-path inference or an identification of outer-walk occurrences.

## 3. Every upper constraint is protected simultaneously

For a selected p and any other original source y, put r=p-a_p. The diameter
upper bound to a_p gives
$$
2(p-y)\cdot r=|p-y|^2+D^2-|y-a_p|^2\ge|p-y|^2.
$$
Writing d=|p-y|, the exact single-reflection identity yields
$$
|F(p)-y|^2-d^2
=-2(p-y)\cdot r/D^2+1/D^2\le-(d^2-1)/D^2\le0.
\tag{SR.3}
$$
For an old unit neighbor, its distance to a_p is D, so equality holds and
the unit contact is preserved exactly. For d>1 the distance strictly decreases.

If p,q both move, add their two single-reflection squared changes. The joint
change has the additional term `-2(F(p)-p) dot (F(q)-q)`, at most 2/D^2. Hence
$$
\boxed{|F(p)-F(q)|^2-|p-q|^2\le-2(|p-q|^2-2)/D^2\le0.}
\tag{SR.4}
$$
The final sign is Lemma SR.1. Fixed-fixed pairs are unchanged. Thus F is a
nonexpansive map on the **entire original source**, not just its active pairs.
No inactive upper pair can become a new diameter. Every old diameter incident
to S strictly shortens (D^2>2).
There are exactly |S| such edges: a fan carrier is incident with the three
distinct diameters to p,p_-,p_+, so it is not a selected degree-one leaf.
If the new source is unit-separated, its actual diameter-pair count is exactly
`h-|S|`; the old unchanged pairs are the only remaining diameter pairs.

Furthermore
$$
|F(p)-F(q)|\ge\sqrt2-2/D>1\quad(p,q\in S),
\tag{SR.5}
$$
so no moving-moving pair creates a lower overlap or a new contact. All old
contacts are moving-fixed or fixed-fixed and stay exactly unit.

## 4. Exact lower-obstruction factorization and canonical implication

Let F_p be the map reflecting only p and fixing the entire rest of A. The only
possible lower violations of the simultaneous map are
$$
|F(p)-y|<1,\qquad p\in S,\ y\in A\setminus S.
$$
These are the **same** inequalities as in the corresponding solo map. Solo
pairs with another selected leaf are also safe, by (SR.3), the triangle bound
`|F_p(p)-q|>=sqrt2-1/D>1`, and Lemma SR.1.

Therefore simultaneous lower feasibility is equivalent to lower feasibility of
every solo map. The same equivalence holds with strict `>1` required at old
noncontact pairs: (SR.5) prevents any new moving-moving equality.

For the canonical contact-minimal, then diameter-pair-minimal source, if all
these old noncontacts remain strict, the new source has the same cardinality,
all old contacts and no new contacts, diameter <=D, and fewer old diameter pairs
with no replacement. Global optimality or the secondary normalization is
contradicted. Thus a nonempty selected family cannot avoid the unary lower
obstruction. Its individual blockers are within distance `1+1/D` in the old
source and remain fixed. The earlier fan-triangle calculation further locates
them at diameter-inactive source vertices; that optional localization retains
the unpromoted status of the independently checked single-flip proof.

For epsilon=1/3 in the preceding bulk theorem, its T meets (SR.1) for D>=100.
Indeed `T<2.6 sqrt(D)` whereas `(D-2)/(2sqrt(2))>(D-2)/3`, and
`2.6 sqrt(D)<(D-2)/3` for D>=100. Any independently selected degree-two fan
leaves in that bulk therefore satisfy the simultaneous theorem. This does not
assert that every canonical source has such fan leaves.

## 5. Distinct unary blockers and the canonical 2U/5 matching

Assume in addition
$$
D\ge20,\qquad T\le D/6-2.
\tag{SR.6}
$$
A **strict-pair blocker** for p is an original source vertex y with
`|p-y|>1` and `|F_p(p)-y|<=1`.

### Lemma SR.2: blocker uniqueness across selected leaves

No original vertex is a strict-pair blocker for two distinct members of S.

**Proof.** If y blocks p and q, the two reflected points p',q' are at distance
<=2, hence d=|p-q|<=2+2/D. Their outward-normal angle theta satisfies
$$
\sin(\theta/2)\le(d+2T)/D<1/3.
$$
Every hull side on the short normal interval has bisector-tangent projection
at least its length times cos(theta/2)>2sqrt(2)/3. Three sides would imply
`d>2sqrt(2)>2+2/D`. Thus the hull chain has exactly two sides, and its
intermediate vertex r is the common unit-contact neighbor of p and q. Both
reflections preserve those contacts: `|r-p'|=|r-q'|=1`. Moreover
$$
|p'-q'|\ge2\cos(\theta/2)-2/D>4\sqrt2/3-1/10>7/4>\sqrt3.
$$
The intersection of the two closed unit disks about p',q' has diameter less
than one: it is contained in the ball about their midpoint of radius
`sqrt(1-|p'-q'|^2/4)`. Both r and y lie in that lens, contrary to unit
separation unless y=r. But r is an old unit neighbor and is not a strict-pair
blocker. QED.

Now use the canonical full-source midpoint estimate
[Section 58, FS.6](../targets/target-c/58-full-source-geometry-audit.md), which
puts **every** actual diameter midpoint within
`T=sqrt(D eta+eta^2)=O(D^(3/4))` of the full-source circumcenter,
`eta=3^(1/4)sqrt(D)`. It satisfies (SR.6) for every D>=10000: using
`3^(1/4)<4/3` and `sqrt(3)<7/4`,
$$
T^2/D^2<\frac4{3\sqrt D}+\frac7{4D}
\le\frac4{300}+\frac7{40000}<\frac1{64},
$$
so T<D/8<=D/6-2.
The newer square-root bulk improves the quantitative radius but is unnecessary
for this qualitative application; no unpromoted midpoint theorem is required.

Let U be the total number of internal actual-diameter fan leaves with contact
degree two. Their induced contact graph has maximum degree two and contains
no triangle. Each path or even cycle has an independent set of at least half
its vertices; each odd cycle has length at least five and an independent set
of at least two-fifths of its vertices. Thus choose
$$
|S|\ge\lceil2U/5\rceil.
$$
Every solo reflection must have a strict-pair blocker, by global minimality
and the contact/diameter-count normalization. Every blocker has old distance
at most 1+1/D from its leaf. It cannot be another actual diameter endpoint:
the generalized Lemma SR.1, the uniform FS.6 bound, and `1+1/D<sqrt(2)`
exclude that possibility. Lemma SR.2 makes all selected blockers distinct.
Hence the canonical source contains the exact disjoint matching
$$
\boxed{\#\{\text{disjoint loaded-to-diameter-inactive blocker pairs}\}
\ge\lceil2U/5\rceil,\qquad1<|p-y|\le1+1/D.}
\tag{SR.7}
$$
No near-unit maximum-degree estimate or greedy eleven-edge loss is used.
The theorem is conditional on the actual fan population U, not on any recent
unpromoted theorem that forces U to be large. It does not assert that these
inactive endpoints are contact-isolated.
In any independently justified branch with `U>=D/2-O(sqrt(D))`, it yields
`D/5-O(sqrt(D))` disjoint blocker pairs. This arithmetic application does not
promote the recent fan-population extraction or eliminate its other branch.

## 6. Exact certificates and further repair attempt

[The verifier](../../../research/verify_centered_fan_reflections_2026_10_02.py)
uses Q(sqrt(4D^2-1)) with D=100. A nine-leaf unit-chord circular arc and its
carrier form an actual diameter source. Three nonadjacent internal leaves
are reflected together. Every source pair is checked exactly: old contacts
stay unit, every upper distance is nonincreasing, moving-moving lower distances
stay >1, and three actual diameters disappear without replacements.

Adding the isolated point `y=(D-1-1/(2D),0)` blocks the middle leaf: its old
distance is 1+1/(2D), and its new distance is 1-1/(2D). Exact enumeration checks
that every failed simultaneous inequality is already a unary solo failure.
Moving y by the middle leaf's displacement repairs this particular packet,
and all full-source pairs are checked again. A third packet adds the second
isolate `z=(D-2-1/D,0)`. Moving y alone then creates the exact inactive-inactive
overlap `|y'-z|=1-1/(2D)`, although every upper constraint remains safe.
Moving z with y repairs this finite two-point chain, with all pairs checked.
This rejects the universal claim that moving each first blocker alone is enough.
A small same-cardinality integer
grid has diameter <D in each case, so none of the packets is globally optimal
or asserted to carry canonical KKT stress.

The repaired packet is not a general theorem: an inactive point can have
arbitrarily small lower slack to other inactive or unloaded points, and translating
it can transfer a collision. The simultaneous upper theorem deliberately fixes
those points; it cannot be applied to the repaired map without checking them.
This is where the next attempted competitor fails to become universal.

The new reduction removes active and inactive upper-distance interactions and
moving-moving lower interactions from this **specific** independent centered
fan family. It does not remove each fan's existing unary lower obstruction.
The exact remaining obligation is to move or replace its actual fixed inactive
blockers while preserving all their lower constraints and their full-source
upper distances. Other canonical C-II branches remain open.
