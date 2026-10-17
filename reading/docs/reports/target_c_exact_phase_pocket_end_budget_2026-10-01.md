> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_pocket_end_budget_2026-10-01.md) · source SHA-256 `6d562157e45ba622cef779353b153e3f34150f9279a7c239e9ad08042570159e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BCA0766E07EC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: exact-phase paired layers bound pocket train ends

```text
paired gap classes -> each intermediate layer has two physical loaded anchors
 -> at most one retained exact-phase end on each inner pocket
 -> Q+2k+2m<=q+2 (two shores: Q+2k+2(m_A+m_B)<=q+8)
 -> unresolved incompatibility or release of the surviving source
 -> strict competitor / exact triangle / Level I consequence
```

**Date:** 2026-10-01.
**Original base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`.
**Starting checkpoint:** `b0578956`.
**State version:** `2026-09-14.audit.51`.
**Branch / mission:** `swarm/sol/gap-leaf-release-20261001`; couple the
surviving exact-phase staircase to actual source pocket interfaces.
**Classification:** proved candidate under the explicit source/cut hypotheses;
conditional route application; default lifecycle unreviewed.
**Level I:** OPEN. C-I CLOSED. C-II OPEN.
**Active prompt:** [Target C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).

## 1. Hypotheses and dependency boundary

Use the canonical full-support post-ZF source and notation of
[Section 67](../targets/target-c/67-rhombus-population-transport-audit.md).
In particular G is the connected complete unit-contact core, B is the full actual
loaded set, `F=conv B=conv V(G)`, `q=|B|`, and the global face ledger is

```math
 b+Q=2(q-k),\qquad x_B:=b-q=q-Q-2k.                    \tag{1}
```

Q is the **global** bounded exceptional-face degree surplus. An inner pocket
means a new bounded face after adding missing sides of F to G. Its boundary is
one added hull side and a simple unit-contact path with no loaded vertex in its
interior. Distinct such paths have disjoint outer-face edge occurrences; bridge
occurrences retain their multiplicity. These are the canonical convex pockets
of Sections 67/77. The integer outer-walk identity is canonical
[Section 63](../targets/target-c/63-loaded-hull-slack-audit.md).

Retain m>=1 non-singleton complete global O–O trains of one exact projective
phase u, coherently oriented and ordered as nested cuts on one complement-dual
path. Assume the explicit October 1 fixed-star hypotheses: actual diameter
witnesses `vx_-`, `vx_+` have full support and opposite strict transverse signs;
the cut matrix has rank m; the resolved outer-boundary order is the source
diameter-endpoint order. The nested, individually cancelling support-class
theorem is the unpromoted
[earlier packet](target_c_exact_phase_nested_diameter_support_2026-10-01.md),
Sections 2--5. Its full proofs are inputs under their stated hypotheses.

The boundary host interval interpretation is the unpromoted
[joint-switch report](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md).
For two shores additionally assume a complete crossing rectangle with distinct
exact phases, m_A,m_B>=2, and its four disjoint alternating host intervals.
No report is promoted here. The geometric pairing and gap connectivity are not
asserted for arbitrary source train families.

## 2. Every intermediate layer contains two physical loaded endpoints

For k=1,...,m-1, both host arcs have an actual diameter endpoint of layer k.

### Proof

The nonzero gap graph is connected, so vertex k is incident with a nonzero
support class `(a,b]`, with k=a or k=b. Its indicator is one member of the
nested support basis. Projected positive KKT balance cancels separately in
that class; hence it has both signs of the derivative coefficient for the
orientation from lower to higher layer.

By the fixed witness-star geometry, a nonincident actual diameter with nonzero
support joins the two opposite physical arcs from v toward x_- and x_+.
An edge incident with a witness endpoint has the same arc assignment; v is
the common layer-0 endpoint, and the witness partners have layer m. For a
bar oriented from its lower to higher layer, its transverse sign is positive
precisely when its higher endpoint is on the positive arc. Two signs in the
same support class therefore put an endpoint of each of its two layers on
each physical arc. For an interior layer k these are distinct actual source
points: neither is v or a full-span witness partner, and their transverse
positions lie on opposite sides of the ray through v in direction u.

No parallel-u diameter contributes a nonzero row or an interior gap endpoint.
Thus zero rows cannot substitute for either loaded anchor. QED.

Consequently there is a loaded endpoint strictly between every two consecutive
retained train ends on **each** host arc. These are physical loaded points;
repeated outer-walk occurrences do not supply extra anchors. The two host
intervals are separated on the two sides by the layer-0 star v and by the
layer-m witness partners, respectively.

## 3. One shore forces Q+2k+2m<=q+2

### Theorem

Under Section 1's one-shore hypotheses,

```math
 \boxed{Q+2k+2m\le q+2.}                              \tag{2}
```

### Proof

An inner-pocket contact path has no loaded vertex in its interior. It cannot
contain two retained train ends on one host arc, by Section 2; nor can it
contain ends on both host arcs, because the star or witness partners separate
them. Thus each inner pocket hosts at most one of the 2m train ends.

Each end is a distinct contact-edge midpoint. A complete non-singleton stopped
O–O train ends on an edge incident to one rhombus and the old outer face.
Across that edge, after adding the force-hull cycle, it sees either an inner
pocket or the exterior of F. In the latter case it is a unit hull side of F.
Every end edge has projective direction u. A convex polygon has at most two
distinct sides of one projective direction; an extreme source vertex cannot
be inserted along a straight hull side. Hence at most two ends use direct
unit hull sides, and at least 2m-2 distinct inner pockets have an end.

Each such pocket has a nonunit closing side. Its unit-contact path has at
least two edges, so it contributes at least one to the integer outer-walk
excess x_B. Summing these distinct occurrences gives

```math
 x_B\ge2m-2.
```

Insert (1) to prove (2). No estimate on the lengths of the nonunit hull sides
has been used. QED.

The new constraint retains the global Q that defeated the earlier near-hull
endpoint-count shortcut. It does not replace b by per(F).

## 4. Two exact-phase shores share at most four pockets

### Theorem

Under the two-shore hypotheses of Section 1,

```math
 \boxed{Q+2k+2(m_A+m_B)\le q+8.}                      \tag{3}
```

### Proof

There are 2m_A+2m_B train ends. At most four use direct unit hull sides,
two for each of the two distinct projective phases.

Section 3 puts at most one A end and at most one B end in each inner pocket.
A pocket containing both must cross a transition between consecutive host
intervals in the cyclic order `A+,B+,A-,B-`. Each host interval contains at
least two ends and, by Section 2 on its own shore, a loaded point between its
consecutive ends. Thus a loaded-free pocket path cannot pass across two
host transitions: the entire intervening host interval contains a loaded
point. There are four transitions. The pocket paths have disjoint open
outer-boundary occurrence intervals, so at most four pockets contain an end
of both shores. A transition can be chosen away from every endpoint and
loaded point; repeated articulation occurrences remain resolved and counted.

It follows that at least `2(m_A+m_B)-4-4` distinct inner pockets contain an
end. Their integer excess contributions give
`x_B>=2(m_A+m_B)-8`. Equation (1) proves (3). QED.

At the conditional rooted endpoint q=(pi+o(1))D, the necessary source budget is

```math
 Q+2k+2(m_A+m_B)\le (\pi+o(1))D.
```

This is stronger than merely requiring enough actual diameter rows on each
shore: it couples the actual contact interface currency to both gap systems.
The currently extracted shore coefficients are too small to violate it.

## 5. At the near-disk rooted endpoint, triangular pockets cannot host a linear shore

Now additionally assume a sequence D tending to infinity with, after translations,
`D^{-1}F` converging in Hausdorff distance to the radius-1/2 disk, and
`E_F=per(F)-q=o(D)`. This is an explicitly conditional specialization to the
unpromoted [rooted endpoint ledger](target_c_wrapping_root_defect_stability_2026-09-30.md)
and its near-disk full-core ancestry. For one exact-phase shore,

```math
 \boxed{Q+2k+4m\le q+o(D).}                           \tag{4}
```

If both shores satisfy Section 1's hypotheses,

```math
 \boxed{Q+2k+4(m_A+m_B)\le q+o(D).}                   \tag{5}
```

### Proof

An inner triangular pocket has two unit-contact sides and one force-hull
closing side of length L>1. If one contact side has the exact retained phase u,
the angle between that side and the closing side is `arccos(L/2)`, by the
isosceles triangle cosine law. For L=1+o(1), its projective closing direction
therefore approaches one of the two directions `u+pi/3`, `u-pi/3`.

Here is the necessary uniform directional-count fact for a near-disk convex
polygon. If its normalized Hausdorff error is delta, the endpoints p of any
edge whose outward normal lies within eta of n_0 satisfy
`|p|<=1/2+delta` and `p dot n_0>=1/2-delta-C eta`. Hence their tangential
coordinates are `O(sqrt(delta+eta))`. The edges form one contiguous oriented
boundary arc; projection on its reference tangent is positive and at least
cos(eta) times the edge length. Its total normalized length is therefore
`O(sqrt(delta+eta))`. The estimate is uniform in n_0, including normals
depending on D. Every hull side has length at least one, so the number of
sides in any fixed finite union of such narrow directional windows is
`O(sqrt(delta+eta)D)`.

Fix epsilon>0. At most `E_F/epsilon=o(D)` hull sides have L>1+epsilon.
All remaining triangular pockets with a retained end have closing directions
in the two windows of width O(epsilon) just described (four windows for two
shores). The directional-count fact, first D tending to infinity and then
epsilon tending to zero, shows that only o(D) triangular pockets can carry
retained ends. This is a boundary-order conclusion; no area error was
converted to o(D) without the uniform projection argument.

Only O(1) ends use direct hull unit sides. All other retained ends are on
pockets with at least three unit-contact path edges. For one shore they
occupy distinct pockets, giving `x_B>=2(2m-o(D))`. For two shores, at most
four pockets are shared, so `x_B>=2(2(m_A+m_B)-o(D))`. Insert (1) to prove
(4) and (5). QED.

Since q=(pi+o(1))D at the conditional rooted endpoint, (5) forces
`m_A+m_B<=pi D/4-Q/4-k/2+o(D)`. This doubles the necessary interface payment
per retained end. The extracted shore sizes still need not exceed this budget.

## 6. The actual closing attack and its failure

An initially plausible shortcut was that per(F)-q=o(D), together with the
linear pocket count above, would make the pockets disappear. It does not.
Their nonunit closing lengths can all be 1+o(1), while their unit-contact
paths have length at least two and pay x_B at order D. The canonical
[Type-II audit, Section 84.6](../targets/target-c/84-typeII-interface-collapse-audit.md)
also permits out-and-back macroscopic pockets over o(D) closing sides.

The inequalities cannot be contradicted just by positivity or graphic rank.
For example, formal first-order data `q=pi D`, `k=0`, `Q=D`, and
`m_A=m_B=D/10` satisfy even (5) with a fixed margin. These numbers are a regression
against the algebraic contradiction, **not** a realizable KKT source or a
global-minimizer family. The exact-phase extraction does not imply
`m_A+m_B>(pi/4-o(1))D`, nor a lower Q exceeding the leftover margin.

### A three-contact closing chord is not automatically immune

Here is an exact local/source regression against extending the triangular
exclusion to every short higher-degree pocket. For D>=10 put t=1/(100D),
`c=(1-t^2)/(1+t^2)`, `s=2t/(1+t^2)`, L=1+2s, and
`H=sqrt(D^2-(D+L)^2/4)`. Take six source points

```math
 a=(c,-s),\quad x=(0,0),\quad y=(0,1),\quad b=(c,1+s),
```
```math
 p=(c-H,1/2+D/2),\qquad z=(c-H,1/2-D/2).
```

The actual diameter set is exactly `{ap,bz,pz}`. The actual unit contacts are
exactly `{ax,xy,yb}`. The other distances lie strictly between one and D:
the path vertices x,y lie strictly inside the loaded trapezoid
`conv{a,b,p,z}`, and their noncontact local squared distances are `2+2s`;
the other loaded cross distances have square `D^2-DL>1`. The closing pair ab
has length L>1. These claims hold for all D>=10 directly from the displayed
formulas, and the bounded radical certificate checks six widely separated D.

Replace a by

```math
 v=((1-4t^2)/(1+4t^2),4t/(1+4t^2)),
```

fixing all other points. Every old contact is preserved. The amplitude is
`2sin(3 arctan t)<=6t<1/(2D)`. Its displacement has negative horizontal
and positive vertical coordinates, so its dot product with
`a-p=(H,-(D+L)/2)` is negative; the squared-length formula shows ap strictly
shortens. More explicitly `2H Delta_x-(D+L)Delta_y+|Delta|^2<0`, because
`Delta_y>=t`, `|Delta|^2<=36t^2`, and D>=10. The new a is strictly inside the
old loaded trapezoid, so every inactive upper constraint remains strict.

Nevertheless ab becomes an overlap. Put A=1+t^2, B=1+4t^2. Its new difference
has components `6t^2/(AB)` and `1-2t(1-2t^2)/(AB)`. For t<=1/1000 the second
decrement is at least t, so

```math
 |b-v|^2\le36t^4+(1-t)^2<1.
```

The other changed lower diagonal has square `2-2v_y>1`.

This construction has real source contacts, real diameter partners, a convex
three-contact path over a near-unit loaded closing side, and a small finite
contact-preserving diameter-shortening replacement. It **does not** give a
canonical source: the diameter partners p,z are contact-isolated, so full
positive KKT equilibrium is impossible and the contact-core hull differs from
the loaded hull. The local path is a pocket scaffold, not a silently identified
canonical force-hull pocket. It also lacks the second actual slab boundary,
complete O–O trains, a transverse grid and global optimality. A six-point
unit-spaced line has diameter 5<D. The regression rejects automatic local
three-contact immunity; it does not reject a source/KKT closing theorem.

The next concrete source obligation is to use the one-end-per-pocket geometry
and actual contact reactions to release pocket chords or force enough global
interface cost to violate (2)--(5). In particular, each surviving pocket has
only one retained cut end per exact-phase shore; treating it as a private
diameter support still fails because every support class has both signs.
The finite in-witness-cell rigidity theorem remains binding.

No exact triangle or source-preserving diameter competitor has been obtained.
Nonconstant phase, split-star O–O, inactive-interface, macroscopic-container,
and all other full-core branches survive. Canonical theorem state is unchanged.

## 7. Certificates, scope, and promotion recommendation

The [face/cap verifier](../../../research/verify_target_c_face_following_cap_blockers_2026_10_01.py)
includes a complete finite cyclic-host-word census with all optional corner
loaded markers and all choices of up to four direct-end exemptions in its
documented bounded universe. It checks the one-end-per-host and four shared
pocket bounds and preserves an abstract packet attaining the loss of eight.
This certificate encodes physical anchor separation as an explicit hypothesis;
it does not prove the train extraction, actual source equilibrium, or global
optimality. The geometric/source statements above are analytic.

Executed counts: 144 cyclic host words, 140,416 direct-end exemption packets,
and 1,023 doubled nested gap trees through m=10: PASS. The constant-eight
abstract equality packet is retained in the verifier.
Six exact three-contact overlap packets additionally certify every old distance,
the contact/diameter sets, all final upper constraints and the sole new overlap.

**Promotion recommendation:** unreviewed pending independent hostile audit,
with conditional extraction ancestry retained. Theorem (2) applies to a
source satisfying the exact-phase hypotheses, and (3) additionally requires
both shores exact and the four-host interpretation. Neither is a universal
C-II conclusion.
