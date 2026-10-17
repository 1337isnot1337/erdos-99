> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_paired_cell_gluing_independent_audit_2026-10-07.md) · source SHA-256 `11f36db175e7882fdf53f4e3f93c02a0672f2bc3a42b9ecfad7564fb2218d4bf`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7E93D4BE8B87","canonical":true,"claim_ids":["C-EXTERIOR-FOUR-TIP-CROSS-SEPARATION","C-EXTERIOR-FOUR-TIP-FULL-SOURCE-SHIELD","C-EXTERIOR-PAIRED-CELL-CONTACT-BUDGET-ENDPOINT","C-EXTERIOR-PAIRED-CELL-STRICT-CAPACITY","C-EXTERIOR-TWO-UNIT-SIDE-WALL-SHIELD"],"claim_statuses":{"C-EXTERIOR-FOUR-TIP-CROSS-SEPARATION":"canonical","C-EXTERIOR-FOUR-TIP-FULL-SOURCE-SHIELD":"canonical","C-EXTERIOR-PAIRED-CELL-CONTACT-BUDGET-ENDPOINT":"canonical","C-EXTERIOR-PAIRED-CELL-STRICT-CAPACITY":"canonical","C-EXTERIOR-TWO-UNIT-SIDE-WALL-SHIELD":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C independent audit: separated four-tip cell gluing

**Date:** 2026-10-07. **Audit base:** `23be84d473ba3a1cf6c54b4f35cc988260e50768`, state `2026-10-07.audit.84`.
**Frozen source:** `research/sol/target-c-exterior-cap-closure-20261006` at
`f4a362727779f6afc0f01738015112c04fdb73d5`.
**Source artifacts:** `docs/reports/target_c_exterior_cap_mixed_boundary_wall_capacity_2026-10-06.md`,
`docs/reports/target_c_exterior_loaded_tips_and_paired_packet_gluing_2026-10-06.md`.

The source report's four-tip geometry survives when its separation is kept as an
explicit hypothesis. This audit promotes the two-sided wall shield, the
four-tip whole-source shield, strict cross-cell separation, the conditional
contact-budget endpoint, and the resulting total strict-capacity bound. It does
not promote the report's derivation that macroscopic antipodal caps produce four
pairwise-separated tips. That derivation uses an unpromoted cap-pairing input.

## Run lock and exact endpoint

Audit base is main `23be84d473ba3a1cf6c54b4f35cc988260e50768`, state audit.84;
Target C has C-I closed and C-II open. The immutable Worker2 source is commit
`f4a362727779f6afc0f01738015112c04fdb73d5`; its branch and source worktree were
not modified.

The audited implication is

```text
four actual extreme hull tips with pair distances >=4
 -> every point in either guarded cell is safe against the complete retained source
 -> packets from the two cells are strictly separated from each other
 -> a packet with |S_1|+|S_2|+4 sites triggers the exact contact/diameter endpoint
 -> combined strict capacity is at most |S_1|+|S_2|+3.
```

The first line is a hypothesis in the promoted theorems, not a conclusion here.
The implication chain has no population lower bound, so the result does not
eliminate a cap or close C-II.

Canonical dependencies actually used are Audit.84
`C-EXTERIOR-HULL-AUGMENTED-CELLS` and
`C-EXTERIOR-ONE-UNIT-SIDE-HULL-TIP-SHIELD`, `C-EXTERIOR-CAP-ACUTE-LOADED-TIPS`,
`C-FS-GEOM`, and Audit.64 `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`.
Canonical Section 67 supplies the hull-augmented face convention and every
component of `G-x` sees a loaded vertex. The antipodal cap-pairing report is not
used.

## 1. Two-sided unit-wall vertex shield

Let `Q` be an actual convex face in the source hull `K`, bounded by one source-
hull arc and a simple path of unit edges. Let `v` be an internal path vertex,
with unit path neighbors `a,b`; let `W_Q` be all path vertices. If
`x in int(Q)` is at distance at least one from every vertex in `W_Q\{v}`, and
`q in K\Q` is at distance at least one from every vertex in `W_Q`, then

```math
|x-q|>1.
```

This includes old source points and proposed points in another cell. Weak
guards suffice; exterior equality cannot occur.

Translate `v` to zero. The two incident path rays bound the local convex face
sector, of angle `psi<=pi`. If `r=|x-v|>=1`, the first segment exit from `Q`
to `q` cannot use the source-hull arc before reaching `q`: an interior point of
`K` joined to a point of `K` stays in `int(K)` until that endpoint. The first
exit is therefore through a unit path edge or a path vertex. The exact
weighted-square identity used in Audit.84 gives endpoint-to-crossing distances
at least `sqrt(3)/2` at each side of a crossed unit edge, hence
`|x-q|>=sqrt(3)>1`; a vertex exit gives at least two.

Suppose instead `r<1`. Let `u_a,u_b` be the unit vectors along the two incident
edges. The weak neighbor guards imply

```math
x\cdot u_a\le r^2/2,\qquad x\cdot u_b\le r^2/2.
```

For any unit direction `z` outside the open sector between `u_a,u_b`, the
circular angular distance from `x/r` to `z` is at least its distance to one
of the two boundary rays. Thus

```math
x\cdot z\le \mu:=\max(x\cdot u_a,x\cdot u_b)\le r^2/2.
```

Write `q=t z` with `t>=1`, which follows from its unit-clearance from `v`. Since
`t-\mu>0`, `t^2-2t\mu` is increasing for `t>=1`, and

```math
|x-q|^2\ge r^2+t^2-2t\mu
\ge r^2+1-2\mu\ge1.
```

Equality requires `t=1` and `z` to be one of the boundary rays, which makes
`q=a` or `q=b`; both lie on `partial Q`, excluded by `q in K\Q`.

If `q` is inside the open sector but outside `Q`, the segment `xq` stays inside
that sector and cannot leave through either incident edge or through `v`. It
also cannot exit through a source-hull side before `q`. Its first exit is
through another unit wall side or vertex, where the crossing estimate above
gives strict clearance. This proves the two-sided version independently; it
does not require a closed polygonal unit wall.

## 2. Four-tip full-source shield

Let `Q_1,Q_2` be distinct actual hull-augmented cells with path vertex sets
`W_1,W_2`. Let `R` be their four distinct loaded hull-arc tips. Assume every
point of `R` is extreme in `K` and

```math
|v-w|\ge4\quad(v,w\in R,\ v\ne w).
```

Set `S_i=(A intersect Q_i) minus W_i` and

```math
N_i=\{x\in int(Q_i): |x-w|\ge1\text{ for all }w\in W_i\setminus R\}.
```

For each `x in N_i`, every retained old point in `A\(S_i union R)` is at
distance at least one from `x`. Every such point outside `W_i` is strictly
farther than one; the same strict conclusion holds for each `v in R` not on
`W_i`.

If `x` is not strictly within distance one of any omitted path guard in
`R intersect W_i`, all path vertices are weak guards. The unit-edge exit
argument gives strict separation from every old nonwall source point outside
`Q_i`; retained wall vertices are checked by their guard. If `x` is strictly
within one of an omitted path guard `v`, pair separation of `R` puts every
other omitted guard farther than three from `x`. All other path vertices remain
weak guards. If `v` is a hull tip, Audit.84's one-unit-side shield applies; if
`v` is internal, the two-sided shield in Section 1 applies. Both give strict
clearance from every nonwall source point outside `Q_i`, including other
members of `R`. Any such point on `W_i\setminus R` is directly guarded.

These are pointwise geometric implications: if a proposed point `q` in another
cell is unit-clear of the complete path and lies in `K\Q_i`, the same
one-sided or two-sided proof gives strict separation from `x`. The shield does
not depend on `q` being an old source label.

Every source point in `Q_i` is either in `S_i` or on `W_i`, because `Q_i` is a
face of the augmented graph and has no graph vertices in its interior. Thus
the preceding checks cover the full retained source. This explicitly retains
every point except those in the named deletion sets.

## 3. Strict cross-cell separation

Under the same four-tip hypotheses, every
`x in N_1` and `y in N_2` satisfy

```math
|x-y|>1.
```

Call a point close if it is within distance one of a member of `R`. Pairwise
tip separation gives at most one such member per point. By Section 2, a close
point in `N_i` must be close to a tip lying on its own path: tips outside that
path are strictly shielded.

Two points close to different tips have distance at least `4-1-1=2`. They
cannot both be close to the same tip `v`. Indeed, the local sectors of the two
distinct faces at `v` are disjoint and lie in the interior cone of the extreme
point `v` of `K`, whose total angle is strictly below `pi`. If a point at
distance `r<=1` is weakly clear of the two neighbors of an internal path
vertex, then its sector angle `psi` satisfies `r>=2cos(psi/2)`, so
`psi>=2pi/3`. If it is close to a hull tip and weakly clear of its one path
neighbor, the direction angle is at least `pi/3`; since the point is interior
to the tip sector, that sector angle is strictly greater than `pi/3`. Two
internal sectors sum to at least `4pi/3`; a tip and an internal sector sum to
strictly more than `pi`. Two hull-tip sectors at the same point would repeat
one of the four distinct tips. Each alternative contradicts the hull-cone
angle.

It remains to consider neither point close, or only one close. A point not
close is weakly clear of every wall vertex in the other cell: vertices omitted
from its defining guard set are at distance greater than one by non-closeness,
and all other vertices are handled by Section 2 or the direct path guard. If
both are not close, the segment between them exits `Q_1` through a unit wall
side or vertex; the two endpoints weakly guard that wall, giving distance at
least `sqrt(3)` or two. If only `x` is close to `v`, then `y` is weakly clear
of every wall vertex of `Q_1`, including `v`. Apply the one-sided or two-sided
shield at `v` with `q=y`. It gives strict distance. The case where only `y` is
close is symmetric.

This proves strict cross separation for the finite four-tip hypothesis even
with nonstrict wall guards. It does not derive that hypothesis from a
macroscopic-cap regime.

## 4. Conditional paired contact/diameter endpoint

The two cell populations `S_1,S_2` are disjoint: distinct face interiors are
disjoint; their only shared source points on the unit-path boundaries are core
wall vertices, excluded from `S_i`; a hull-arc isolate belongs to only one
interval between consecutive loaded vertices. The four loaded tips are
disjoint from both isolate populations. Put

```math
R_{all}=S_1\cup S_2\cup R,
\qquad m=|S_1|+|S_2|+4.
```

All actual contacts removed by `R_all` are incident to `R`; there are no
contacts between members of `R` because their pairwise distances are at least
four. Each tip has an incident unit path edge, so at least four old contacts
are removed. Every point of `R` is an actual diameter endpoint, so at least
one actual diameter pair is removed.

Suppose packets `Y_i subset N_i` are locally unit-separated and
`|Y_1|+|Y_2|=m`. Assume the complete new contact graph involving each local
packet and its retained wall anchors is triangle-free. Let `j` be the number
of distinct new unit pairs in the complete replacement and `t` the number of
old contacts deleted. If `j<=t`, the canonical source is impossible.

Delete `R_all` and insert both packets. Section 2 checks every new-to-retained
old lower pair; Section 3 checks every cross-packet pair strictly. All inserted
points are interior to `K`, so every inserted-involving upper distance is
strictly below `D`. Any new unit contact is internal to one packet or joins it
to one of that cell's retained wall vertices; the locally triangle-free
hypothesis covers all triangles there, and no triangle can span the two
packets because there is no cross contact. The replacement is a same-cardinality
triangle-free source with at least one old diameter pair removed and no new
diameter pair. The canonical contact-budget endpoint excludes it whenever
`j<=t`.

The source version counts local contacts `j_i`. Since a shared wall anchor may
be counted in both local ledgers, the audited sufficient condition is
`j_1+j_2<=t`; this implies the required bound on distinct global new contacts
`j`. No equality between the sum of local ledgers and `j` is claimed.

## 5. Exact total strict-capacity bound

For each cell let

```math
E_i=\{x\in int(Q_i):|x-w|>1\text{ for all }w\in W_i\setminus R\},
\qquad M_i=Pack_1(E_i).
```

If `M_1+M_2>=|S_1|+|S_2|+4`, choose finite packets with total cardinality
`m`. Dilate each packet by a sufficiently small common factor about an interior
point of its cell. Strict wall margins and cell interiority persist, every
internal unit pair opens, and Sections 2--3 retain strict full-source and
cross-cell lower clearance. Thus the replacement has `j=0<t`, contradicting
the paired endpoint. Consequently

```math
\boxed{M_1+M_2\le |S_1|+|S_2|+3.}
```

The Audit.84 single-cell lower construction gives `M_i>=|S_i|`, so the sum of
the two strict-capacity surpluses is at most three. This is a conditional
finite bound on two cells with four separated tips; it does not supply the
surplus sites, establish the four-tip hypothesis for any asymptotic cap pair,
or exclude arbitrary exterior caps.

## 6. Hostile checks and exclusions

- **Shared tips:** the canonical exact `C-EXTERIOR-CAP-SHARED-TIP-GLUING-REGRESSION`
  is the necessary guardrail. In its collinear chain family, each one-tip
  replacement is feasible and strictly sub-D, but the two inserted sites have
  squared distance `4/9`. Its tips are not four distinct pairwise-separated
  extremes and the source is nonglobal; it does not refute the theorem above.
- **Nonstrict guards:** all wall and local-packet guards used for T.3/T.4 may
  be weak. The proofs give strict distances to exterior nonwall points and
  strict cross-cell separation; equality in a cone estimate would force the
  tested point to be a path neighbor on the cell boundary.
- **Isolates:** every point in `S_1 union S_2` is explicitly deleted and
  repaid by equal packet cardinality. Every other contact isolate remains in
  the source and is checked by the shield.
- **Diameter pairs:** the four selected loaded tips guarantee `d>0`, and
  interior placement makes every new upper pair strict. No active diameter
  pair is silently treated as a contact.
- **Triangle-freeness:** the paired endpoint requires the complete local new
  contact graphs to be triangle-free. A packet-internal forest alone would
  not suffice.
- **Unpromoted asymptotic premise:** the source report's antipodal-cap argument
  is not in the canonical dependency graph. The lower bound `|v-w|>=4` remains
  an explicit hypothesis; no conclusion for every sufficiently large
  canonical source is claimed.

The finite verifier from source commit `f4a3627` uses exact rational arithmetic
for the right-angle, half-turn, and shared-tip examples. It does not check the
universal shields, four-tip sectors, or paired capacity. Its 3,942 pair checks
support only those finite examples; they were rerun in Audit.84 and matched the
saved certificate. No new computation is cited as proof of T.3/T.4.

## Verdicts

| Candidate | Verdict | Canonical disposition |
| --- | --- | --- |
| Two-unit-side internal wall-vertex shield (M.2) | PASS — promote | `C-EXTERIOR-TWO-UNIT-SIDE-WALL-SHIELD` |
| Four-tip retained-source shield (T.3) | PASS — promote | `C-EXTERIOR-FOUR-TIP-FULL-SOURCE-SHIELD` |
| Strict cross-cell separation under four-tip hypothesis (T.4) | PASS — promote | `C-EXTERIOR-FOUR-TIP-CROSS-SEPARATION` |
| Paired contact/diameter endpoint (T.5), with local counts narrowed to a sufficient upper bound | PASS — promote | `C-EXTERIOR-PAIRED-CELL-CONTACT-BUDGET-ENDPOINT` |
| Total strict-capacity surplus at most three (corollary) | PASS — promote | `C-EXTERIOR-PAIRED-CELL-STRICT-CAPACITY` |
| Antipodal-cap derivation of four separated tips | NOT AUDITED | Remains unreviewed; do not infer it from these conditional theorems |

These exact conditional results sharpen the exterior-cell capacity route but
do not change the C-II frontier or Level I status.
