> Generated reading edition · [exact source](../../../docs/reports/target_c_loaded_near_unit_hull_adjacency_2026-10-01.md) · source SHA-256 `38e58843277dc69ece407802c562af62e8b05b223465d6c697704b9e95521682`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-795FCD0B3DCF","canonical":true,"claim_ids":["C-LOADED-NEAR-UNIT-ADJACENCY"],"claim_statuses":{"C-LOADED-NEAR-UNIT-ADJACENCY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C-II — near-unit loaded pairs are hull sides

**Phase 2 preservation provenance:** PR #600, branch swarm/tb1-augmented-thrackle-20261001, exact source head 9ddd9538c29244fd22183f9682b2835f54cde0c3. The finite loaded near-unit adjacency theorem is canonical in `2026-10-05.audit.62` as `C-LOADED-NEAR-UNIT-ADJACENCY`. Later swap-specific and rooted-endpoint applications in this report retain their stated conditional scope.

`short loaded-pair adjacency -> pure-conflict loaded endpoints occupy narrow
hull-direction windows -> o(D) exceptional owners at the conditional rooted
endpoint -> outer unloaded contact sites remain the joint-conflict obligation`

**Date:** 2026-10-01 run, continued 2026-10-02. **Starting commit:**
`14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`; current branch checkpoint before
this extension `c165fee5c82b4ab17490e42d9fd5b27f77b84864`.

**State version:** `2026-09-14.audit.51`.

**Mission:** `swarm/tb1-augmented-thrackle-20261001`; source geometry of the
remaining exterior Horn conflicts. **Classification:** the exact cap-threshold / loaded-hull adjacency theorem is canonical in audit.62; conditional asymptotic swap consequences remain unpromoted. C-II and Level I OPEN.

Canonical premises are actual diameter endpoints being hull extremes,
diameter-thrackle crossing, full-support source normalization and local
contact trapping. The joint-move conclusion uses our unpromoted
[Horn/face-following packet](target_c_joint_swap_horn_and_loaded_defects_2026-10-01.md).
The asymptotic specialization explicitly adds `D^-1 conv B` converging to
the radius-`1/2` disk and `per(conv B)-|B|=o(D)`. This is the unpromoted
[rooted endpoint ledger](target_c_wrapping_root_defect_stability_2026-09-30.md)
branch, not a premise about every C-II source.

The loaded-side cap threshold was independently proved in PR #599 at
`eac7bc9f8159920df6a0393a68c912a78456edc1` in its face-following/cap report.
Its elementary proof is reproduced below; the new application is to a
**nonadjacent loaded pair**, rather than an existing hull side.

## 1. A diameter-disk cap threshold

### Lemma 1

Let a unit-separated planar source have diameter `D`. Suppose `a,b` have
distance `ell<D` and actual diameter partners `c,d`, respectively, lying on
the same side of the line `ab`. If a source point lies strictly on the other
side, then

```math
(1+D^{-2})\ell^2+2\ell/D\ge3,
\qquad
\ell\ge\tau_D:=\frac{3D}{\sqrt{3D^2+4}+1}.
\tag{1}
```

The partners may coincide. No source optimality or stress is needed.

### Proof

Set `a=(-ell/2,0)`, `b=(ell/2,0)`, and orient the partner side downward.
Write

```math
c-a=(A,-C),\qquad d-b=(-B,-E),\qquad C,E\ge0.
```

The constraints `|c-b|,|d-a|<=D`, together with `|c-a|=|d-b|=D`, give
`A,B>=ell/2>0`. Let `alpha,beta` be their positive angles from the downward
vertical, and put `theta=alpha+beta`. The difference of the two diameter
vectors has length `2D sin(theta/2)`. Since

```math
|(c-a)-(d-b)|\le |c-d|+\ell\le D+\ell<2D,
```

we have `theta<pi` and

```math
2D\sin(\theta/2)\le D+\ell.
\tag{2}
```

For a source point `z=(x,y)` above `ab`, its two upper disk constraints imply

```math
-A(x+\ell/2)+Cy\le0,\qquad B(x-\ell/2)+Ey\le0.
```

Together with `y>=0` these bound the triangle with base `ab` and base angles
`alpha,beta`. Therefore the angle `azb` is at least `pi-theta`. For
`r=|z-a|>=1` and `s=|z-b|>=1`, the cosine law gives

```math
\ell^2\ge r^2+s^2+2rs\cos\theta
=(r-s)^2+2rs(1+\cos\theta)
\ge4\cos^2(\theta/2).
```

Equation (2) now yields
`ell^2>=4-(1+ell/D)^2`. Rearranging and taking the positive quadratic root
proves (1). A vertical triangle side is permitted when `C` or `E` is zero;
`theta<pi` excludes two parallel vertical sides. QED.

## 2. Every sufficiently short loaded pair is consecutive

### Theorem 2

Let `B` be the set of all actual diameter endpoints and let `conv B` be
two-dimensional. If distinct `a,b in B` are not consecutive on the boundary
of `conv B` and `|ab|<D`, then

```math
|ab|\ge\tau_D.
\tag{3}
```

In particular for `D>=6`, every pair in `B` of length at most `13/12` is a
side of `conv B`. The near-unit graph induced by `B` is a subgraph of its
hull cycle, so each loaded vertex has at most two loaded near-unit neighbors.

### Proof

Since `|ab|<D`, neither is a diameter partner of the other. The two open
hull arcs between `a` and `b` contain their diameter partners. All partners
of both endpoints lie on **one** of those arcs. Indeed partners `c` of `a`
and `d` of `b` on opposite arcs would be distinct, with cyclic order
`a,c,b,d`; their diameter chords would not cross, contradicting the
diameter-thrackle property. Fixing a partner of one endpoint and varying
the partners of the other proves the same-arc assertion, including shared
partners.

Both arcs contain a loaded vertex because `a,b` are not consecutive. Choose
`z` on the arc without their partners. Convex hull extremality puts `z` on
one side of the line `ab` and the partners on the other. Lemma 1 applies,
giving (3).

For `D>=6`, insertion of `ell=3/2` into the left side of (1) gives strictly
less than `3`; hence `tau_D>3/2>13/12`. QED.

This proof does not select an Euler path, assume a diameter matching, or
delete pendant leaves. Stars and odd-cycle-plus-leaf graphs obey the same
argument. The hull in this theorem is the loaded hull, not an arbitrary
source chart or the hull of a smaller configuration.

### The limiting constant sqrt(3) cannot be increased

For integers `D>=6`, take `t=(1+1/(4D^2))/(2D)`,
`C=(1-t^2)/(1+t^2)`, `S=2t/(1+t^2)`, and the five points

```math
c=0,\quad x=(D,0),\quad y=(D/2,\sqrt3D/2),
```
```math
p=(D(1-C),DS),\quad
q=(D(1-C)/2+\sqrt3DS/2,\sqrt3D(1-C)/2-DS/2).
```

The exact verifier certifies unit separation and diameter `D` for seven
values through `10^4`, with actual diameter set
`{cx,cy,xy,xp,yq}`. The loaded hull order is `c,q,x,y,p`; `p,q` are not
consecutive. Their squared distance is

```math
|p-q|^2=D^2((1-C)^2+3S^2-2\sqrt3(1-C)S)
=3-\sqrt3/D+O(D^{-2}).
```

Also
`|cp|^2=|cq|^2=4D^2t^2/(1+t^2)=1+1/(4D^2)+O(D^-4)>1`.
For this choice of `t`, the strict inequality follows directly from
`t^2(4D^2-1)>1`. The other two nonconstant cross lengths have squares
`|py|^2=|qx|^2=D^2+D^2(1-C-sqrt(3)S)=D^2-sqrt(3)D+O(1)`.
The five listed diameter identities are exact. These formulas prove all
lower and upper pair inequalities for every sufficiently large integer `D`,
not only for the seven computed values. The five consecutive hull cross
products in order `c,q,x,y,p` have positive leading terms, respectively
`D/2`, `sqrt(3)D^2/2`, `sqrt(3)D^2/2`, `D/2`, and `sqrt(3)/2`.
Thus that hull order also holds eventually.

The limiting value of the nonadjacent loaded-pair distance is `sqrt(3)`
from below. The formula's limit, rather than finite survival alone, rejects
any universally larger asymptotic threshold. These packets have no unit
contacts and fail positive source KKT, so they are not canonical sources or
global optima. Five points on a unit-spaced line have diameter `4<D` at
the same cardinality. No sharper finite threshold than (3) is claimed.

An initial fixture `t=1/(2D-1)` overshot the unit-radius threshold by order
`1/D`, giving `|p-q|^2=3+(3-sqrt(3))/D+O(D^-2)`. It did not establish
approach from below. The exact certificate caught this and the displayed
fixture repairs it; the adjacency proof was unaffected.

## 3. Narrow directional windows have o(D) sides at the near-disk endpoint

### Lemma 3

Suppose convex polygons `F_D` have side lengths at least one and
`D^-1 F_D` converges after translations to the radius-`1/2` disk. For any
fixed finite number of projective direction windows of widths tending to
zero, the number of sides in those windows is `o(D)`, uniformly when their
central directions depend on `D`.

### Proof

Let `delta_D` be the normalized Hausdorff error. Every normalized point has
norm at most `1/2+delta_D`; every support value is at least
`1/2-delta_D`. For an edge whose outward normal differs from `n_0` by at
most `eta_D`, either endpoint `p` therefore has

```math
p\cdot n_0\ge1/2-\delta_D-(1/2+\delta_D)\eta_D.
```

Its tangential coordinate is bounded in absolute value by
`O(sqrt(delta_D+eta_D))`. Such oriented normals occur in one contiguous
convex boundary arc. The projection of each oriented edge onto the
reference tangent is at least `cos(eta_D)` times its length. The total
normalized length of the arc is consequently
`O(sqrt(delta_D+eta_D))`. Each original side has length at least one, so
there are `O(D sqrt(delta_D+eta_D))=o(D)` sides. Projective windows have
two oriented normal windows. Summing a fixed finite number proves the lemma.
No area error is converted into a boundary count. QED.

## 4. Moving long isolates are also sublinear under loaded perimeter slack

### Lemma 4

For a source whose loaded hull has `q` sides, put `E=per(conv B)-q`. Suppose
`D>=6` and `1+E<=D/4`. Then the number of source-hull extreme vertices outside
`B` is at most

```math
\frac{24}{\sqrt{39}}E.
\tag{4}
```

### Proof

Each loaded hull side has length `1<=ell<=1+E`. A nonempty cap beyond it
has `ell>=tau_D>3/2` by Lemma 1, and its two diameter-disk tangent triangles
contain that cap. With `ell<=D/4`, (2) gives
`cos(theta/2)>=sqrt(39)/8`. The sum of the two nonbase triangle side lengths,
divided by `ell`, is

```math
\frac{\sin\alpha+\sin\beta}{\sin(\alpha+\beta)}
=\frac{\cos((\alpha-\beta)/2)}{\cos(\theta/2)}
\le\frac8{\sqrt{39}}.
```

Convex perimeter monotonicity bounds the expanded source-hull arc by that
sum. If it has `t` added extreme vertices, unit separation bounds its arc
length below by `t+1`. Thus
`t<=8ell/sqrt(39)<=24(ell-1)/sqrt(39)` on every nonempty cap. All loaded
vertices remain source-hull extreme vertices. Summing their disjoint cap
arcs gives (4). QED.

An arbitrary exterior cloud is not counted by (4); only extreme vertices are.
That distinction is sufficient here because every strict-long endpoint is
extreme. Under `E=o(D)` the right side is `o(D)` and the size hypothesis
holds eventually.

## 5. Consequence for genuine joint conflict clauses

Work with the fixed rooted and face-following dispatch and co-oriented
small swaps in the joint packet. Assume `s=O(1/D)`, shore width `W=O(1/D)`,
and the additional near-disk/perimeter hypotheses stated at the top.

Then all but `o(D)` pure joint-conflict pairs have at least one **unloaded
nonisolated core vertex** as an endpoint. They lie in the old outer face,
and both endpoints are unbracketed in the two-sided shore sense of that
packet. Disabling the owners of the `o(D)` other pure conflicts removes
only `o(D)` swap variables.

### Proof

A pure conflict has old length at most `1+s` and transverse projection
`O(1/D)` on the common displacement axis by joint-packet Theorem 2. Its
projective direction is thus within `O(1/D)` of the shore direction. If
both endpoints are loaded, Theorem 2 above makes the pair a hull side,
and Lemma 3 counts those sides as `o(D)`.

A moving contact isolate outside bounded faces must be incident with the
strict-long graph: the default assignment keeps the other outer-face
isolates fixed. It is therefore extreme and lies outside `B`. Lemma 4
bounds these moving isolates by `o(D)`. A source point has at most nine
neighbors within distance `13/12`: radius-`1/2` disks at it and its neighbors
are disjoint and contained in a radius-`19/12` disk, so the integer neighbor
count is at most nine. There are consequently only `o(D)` pure conflicts
touching these isolates. Bounded-face moving isolates cause no binary lower
clauses by face-following.

Every remaining pure conflict has two core endpoints, at least one outside
`B`. Exterior binary localization and two-sided-contact exclusion are exactly
joint-packet Theorem 8 and Lemma 3. Each source pair touches at most two
movement owners, proving the final owner deletion statement. QED.

Canonical contact trapping makes every nonisolated vertex outside `B` a
strict contact barycenter; in the contact-minimal source its degree is `3`,
`4`, or `5`. That is an actual source restriction on the remaining endpoint,
not an assertion that the endpoint population is small.

Unary obstructions from fixed isolates remain, as do unilateral rhombus
phase-threshold obstructions. Directed returns and pure conflicts involving
unloaded outer-pocket contact sites have not been excluded. In particular
the result does not assert an acyclic movement-owner quotient: distinct
implication edges may use far-apart sites of the same physical slab.

## 6. Exact verification and current obligation

Run `python3 research/verify_loaded_near_unit_hull_adjacency_2026_10_01.py`.
The finite rational packets encode unit separation, all actual diameter
endpoints, convex hull order and short-pair adjacency. Star and antipodal
matching packets are included. They do not certify full source stress,
actual stopped-train cuts, the near-disk asymptotic hypotheses, global
optimality, or any Level I branch. The proofs above establish the universal
statements; finite survival is not a substitute.

The next source-level obligation is to propagate or release a pure exterior
conflict at an unloaded positive contact barycenter, while respecting its
complete train indicators and every inactive lower constraint. Alternatively
prove an actual simultaneous Horn seed avoiding all unary and conflict
certificates. Fixed exterior isolates and pocket closing pairs cannot be
discarded. Exact phase, split-star, inactive-interface, macroscopic inactive
container and all other C-II branches remain open.
