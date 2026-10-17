> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_hull_cell_and_tip_capacity_independent_audit_2026-10-07.md) · source SHA-256 `6e3d0f63378597c995c6f3ecce83550f10dbbc82178aca82833b6edddba29dce`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DA13946F3430","canonical":true,"claim_ids":["C-EXTERIOR-CAP-ACUTE-LOADED-TIPS","C-EXTERIOR-CAP-LOW-ANGLE-GUARD-REDUNDANCY","C-EXTERIOR-CAP-SHARED-TIP-GLUING-REGRESSION","C-EXTERIOR-CAP-STRICT-PACKET-CAPACITY","C-EXTERIOR-HULL-AUGMENTED-CELLS","C-EXTERIOR-ONE-UNIT-SIDE-HULL-TIP-SHIELD","C-EXTERIOR-WALL-HALF-TURN-PIN-REGRESSION"],"claim_statuses":{"C-EXTERIOR-CAP-ACUTE-LOADED-TIPS":"canonical","C-EXTERIOR-CAP-LOW-ANGLE-GUARD-REDUNDANCY":"canonical","C-EXTERIOR-CAP-SHARED-TIP-GLUING-REGRESSION":"regression","C-EXTERIOR-CAP-STRICT-PACKET-CAPACITY":"canonical","C-EXTERIOR-HULL-AUGMENTED-CELLS":"canonical","C-EXTERIOR-ONE-UNIT-SIDE-HULL-TIP-SHIELD":"canonical","C-EXTERIOR-WALL-HALF-TURN-PIN-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C independent audit: exterior hull cells and loaded-tip capacity

**Date:** 2026-10-07. **Audit base:** `08f8f1ccc0a86351287df45e60789e31289632bf`, state `2026-10-07.audit.83`.
**Frozen source:** `research/sol/target-c-exterior-cap-closure-20261006` at
`f4a362727779f6afc0f01738015112c04fdb73d5`, state `2026-10-06.audit.66`.
**Source artifact:** `docs/reports/target_c_exterior_loaded_tips_and_paired_packet_gluing_2026-10-06.md`.

This audit promotes the hull-augmented cell geometry, the one-unit-side hull-tip
shield, the acute loaded-tip consequence, and the exact strict capacity of one
actual cell. It also promotes two exact finite regressions. It does not promote
the report's paired cross-cell gluing theorem, paired-cap exchange, one-site
half-turn theorem, cap extraction, or any exterior-cap closure.

## Canonical proof chain and scope

The audited endpoint is

```text
canonical full-source geometry
 -> convex hull-augmented face with one source-hull arc and a unit path
 -> strict exterior clearance from a deleted loaded tip
 -> exact strict packet capacity = all assigned isolates
 -> one extra site would remove a loaded contact with no new contacts
 -> contradiction to contact-minimality.
```

The capacity statement is finite and source-specific. It supplies no extra slot,
no asymptotic population estimate, and no packet across multiple cells. Every
contact-isolated source point on the source-hull arc is counted in the cell
population `S_Q`.

### 1. Hull augmentation and face cells

Let `G` be the canonical connected positive-contact core, `B` its loaded
actual-diameter endpoint set, `F=conv V(G)`, and `K=conv A` for the full source
`A`. Let `Gamma` be the plane graph obtained by adjoining the entire source-hull
cycle `partial K`, including collinear source-hull vertices; duplicate edges are
kept once. The audited canonical dependencies are `C-FS-GEOM`, `C-RHOMBUS-POP`
(including Section 67's loaded-component and hull-boundary lemmas), and
`C-CONTACT-FACE-REGULARITY`.

Every component of `G-x` contains a loaded vertex by canonical Section 67. The
cycle `partial K` connects all loaded vertices because they are actual extreme
source-hull points. If `x` is a core vertex, each component of `G-x` therefore
connects through the surviving hull cycle (or its path when `x` is on the cycle).
If `x` is a hull isolate, `G` stays connected and the remaining hull path attaches
to it at loaded vertices. Thus `Gamma-x` is connected for every vertex `x` and
`Gamma` is 2-connected.

Every bounded-face boundary is consequently a simple cycle. At a source-hull
vertex its face angle is at most `pi` by convexity of `K`. At a non-hull core
vertex the vertex is unloaded and has positive contact equilibrium. A reflex
face sector would put every contact vector into the complementary open cone of
width less than `pi`, contradicting positive equilibrium. Thus all bounded-face
angles are at most `pi`, and every bounded face is convex.

For each interval of `partial K` between consecutive loaded hull vertices,
either its arc is already a unit core edge or adjoining the full arc increases
`E-V` by one. If `r` arcs are new, Euler's formula gives exactly `r` new bounded
faces. Each new face contains at least one new arc, while each new arc borders
exactly one bounded face on the `K` side. Hence each such new face has exactly
one full source-hull arc, and its remaining boundary is a simple path of unit
core edges. This is the only cell-extraction claim promoted; no area or
macroscopic-cap statement is included.

### 2. One-unit-side hull-tip shield

Consider a convex cell `Q` contained in `K`, whose boundary consists of one arc
of `partial K` and a simple path `P` of actual unit edges. Let `v` be an endpoint
of the path on the hull arc, `w` its path neighbor, and `W_Q` the path vertices.
For `x in int(Q)`, assume `|x-v|>=1` and `|x-u|>=1` for every
`u in W_Q\{v}`. For any `q in K\\Q` that is unit-clear of all vertices of
`W_Q`,

$$
|x-q|>1.
$$

The statement applies to retained old source points by source separation. It
also applies to other proposed points when their distances to the whole path are
at least one.

For the proof, translate `v` to the origin, set `w=(1,0)`, and let the hull arc
ray have angle `theta`, where `0<theta<pi`. The tangent cone of `K` at `v` lies
between angles `theta-pi` and `theta`. If `|x|>=1`, every path vertex is at
distance at least one from `x`. On a first-exit crossing of a unit wall edge
`cd`, at parameter `s`, the identity

$$
|z-((1-s)c+sd)|^2=(1-s)|z-c|^2+s|z-d|^2-s(1-s)
$$

puts each endpoint at distance at least `sqrt(3)/2` from the crossing point;
the crossed segment therefore has length at least `sqrt(3)`. A vertex exit has
length at least two. The segment cannot exit through the source-hull arc before
`q`, since `x` is interior to `K` and `q` lies in `K`.

If `r=|x|<1`, the guard at `w` gives `x dot w <= r^2/2`. A point `q` in `K`
outside the `Q` cone has direction in `[theta-pi,0]`. Since the angle between
`x` and that direction is in `(0,pi)`, the scalar product is maximized uniquely
on the ray `w`; together with `|q|>=1`, this gives

$$
|x-q|^2\ge r^2+1-2(x\cdot w)\ge1,
$$

with equality possible only at `q=w`, which is on `partial Q` and hence is not
an exterior point. If `q` is inside the cone but outside `Q`, the segment exits
through a different unit path side; the unit-edge calculation gives strict
clearance. This checks exterior isolates and does not assume a closed unit wall.

### 3. Acute actual hull tips

In a canonical contact-minimal source, each loaded tip angle `theta` of such a
cell is strictly less than `pi/2`. If `theta>pi/2`, choose a ray at an angle
`phi` with `pi/2<phi<theta`; for sufficiently small `x` on this ray,
`|x-w|>1`. At `theta=pi/2`, use `x=(t^2/4,t)`, which is inside `Q` and satisfies
`|x-w|^2=1+t^2/2+t^4/16>1`.

Every other path vertex is strictly separated from `v`: a unit chord from `v`
to a nonconsecutive path vertex would subdivide the convex face, and consecutive
path neighbors are already accounted for. Every other source point in `Q` is a
contact isolate and is also strictly separated from `v`. Finiteness preserves
these inequalities for small `x`; the hull-tip shield handles every source
point outside `Q`. Replacing `v` creates no contact, removes at least `vw`, and
keeps every inserted distance below `D` because `x` is interior to the source
hull. This contradicts contact-minimality. No uniform acute-angle margin is
claimed.

### 4. Exact strict capacity of one actual cell

Define

$$
E_Q=\{x\in int(Q): |x-u|>1\text{ for every }u\in W_Q\},
$$

and let `Pack_1(E_Q)` be the largest cardinality of a finite unit-separated
subset. For a canonical contact-minimal source and an actual face cell `Q` as
above, with

$$
S_Q=(A\cap Q)\setminus W_Q,
$$

the exact identity is

$$
\boxed{Pack_1(E_Q)=|S_Q|.}
$$

For the lower bound, all points of `S_Q` are contact isolates, so all their
mutual, wall, and exterior distances are strictly greater than one. Contract
them by a sufficiently small common factor about an interior point of `Q`.
Convexity moves every hull-boundary isolate into `int(Q)`, while finiteness
preserves every strict pair margin.

For the upper bound, suppose `|S_Q|+1` sites fit in `E_Q`. Dilate the finite
packet slightly about an interior point of `Q`; its points stay inside `Q`, all
internal unit distances open, and strict wall guards persist. Delete `S_Q` and
one loaded hull tip `v`. The strict hull-tip shield checks every retained source
point outside `Q`, including isolates. All new points are in `int(K)`, so every
inserted-involving upper distance is strictly below `D`. No new contact is
created, at least one old contact at `v` is removed, the cardinality is
unchanged, and the source remains triangle-free. This contradicts the canonical
contact-minimal endpoint.

The conclusion is exact even when `S_Q` includes source-hull points. The
high-angle or exact-contact packet variants in the source report are not part of
this claim.

### 5. Low-angle deleted guards are redundant

At a hull tip of angle `theta<pi/2`, if `x` lies inside its sector and is
strictly farther than one from its single retained unit path neighbor `w`, then
`|x-v|>2 cos(theta)`. Hence when `theta<=pi/3`, omitting the tip guard does not
enlarge the strict region. At an internal unit-path vertex of interior angle
`psi<=2pi/3`, the two strict neighbor guards imply
`|x-v|>2 cos(psi/2)>=1`, so that guard is redundant as well. If deleted path
vertices are pairwise separated by at least four path edges, their immediate
neighbors remain guarded. Thus any such low-angle separated deletion bank
leaves the strict guarded region unchanged, with capacity still exactly
`|S_Q|`; it gains no strict spare site.

### 6. Exact finite certificates and regression

The frozen source verifier was inspected and rerun with Python `Fraction`
arithmetic. Its output matched the saved certificate byte-for-byte; SHA-256:
`e3daa623a24699b7a4146134e42b29eb7d246a61843000655a9aad7770f78cd9`.
It checks 3,942 exact old/endpoint pair distances and verifies three finite
examples: a right-angle tip opening, a sharp half-turn unit path with a
triangle-free three-contact inserted site, and the shared-tip family below. It
does not verify any of the analytic cone or cell arguments.

For each `L in {26,40}`, the exact source
`{(k,0):0<=k<=L} union {(1,7),(1,-7)}` is unit-separated and triangle-free,
with diameter `L` and only the consecutive chain contacts. The sites
`x+=(1/20,1/3)` and `x-=(1/20,-1/3)` each separately replace the left chain
endpoint by a same-cardinality unit-separated triangle-free source of strictly
smaller diameter and one fewer contact. But
`|x+-x-|^2=4/9<1`, so the two individually feasible endpoint replacements
cannot be performed together. The source is collinear and nonglobal; its core
does not satisfy the canonical positive-equilibrium degree/rank hypotheses.
This refutes only the general inference from separate packet feasibility to
simultaneous gluing when cells share loaded endpoints. It does not refute the
source report's distinct, four-tip, separated-endpoint paired-gluing claim.

The exact half-turn example likewise supplies only a finite boundary case: a
convex unit path with total internal turn `pi` admits a triangle-free inserted
site contacting three wall vertices. No global-minimizer claim follows.

## Audit verdict and remaining queue

| Candidate | Verdict | Disposition |
| --- | --- | --- |
| Hull augmentation and unique-arc face structure | PASS — promote | `C-EXTERIOR-HULL-AUGMENTED-CELLS` |
| One-unit-side actual hull-tip shield | PASS — promote | `C-EXTERIOR-ONE-UNIT-SIDE-HULL-TIP-SHIELD` |
| Loaded actual hull tips are acute | PASS — promote | `C-EXTERIOR-CAP-ACUTE-LOADED-TIPS` |
| Exact strict cell capacity | PASS — promote | `C-EXTERIOR-CAP-STRICT-PACKET-CAPACITY` |
| Low-angle deleted-guard redundancy | PASS — promote | `C-EXTERIOR-CAP-LOW-ANGLE-GUARD-REDUNDANCY` |
| Shared-tip cross-packet collision | REGRESSION VALID | `C-EXTERIOR-CAP-SHARED-TIP-GLUING-REGRESSION` |
| Exact half-turn boundary example | REGRESSION VALID | `C-EXTERIOR-WALL-HALF-TURN-PIN-REGRESSION` |
| Distinct four-tip gluing, paired-cap release, and T.6 general theorem | Not audited here | Remain unreviewed |

The exact cell-capacity result does not extract a high-capacity packet, eliminate
an exterior cap, or alter the C-II endpoint. C-II and Level I remain open. The
next independent items are T.3/T.4's four-tip shield and cross-packet proof,
then the conditional paired exchange T.5; after these, continue the residual
PR #722 audit queue.
