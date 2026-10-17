> Generated reading edition · [exact source](../../../docs/reports/target_c_collective_shallow_wall_packet_release_2026-10-08.md) · source SHA-256 `9070c35f645125614a0c6b3a70e84b47857c3e88afe660b736ddded7330247d0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "4469222d68a1eebc4511bebe5f321011d4dfd335", "source_branch_refs": ["refs/heads/research/level-i-closure-20261007"], "source_commit": "4583329a0eebd5b489f34185ec4ebdc16cabd353", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_c_collective_shallow_wall_packet_release_2026-10-08.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1eab31772c03aabae60944b5de4b718ed81a70d128698dee4c49c209e521fe2e"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Target C: collective packet release behind a shallow unit wall

Date: 2026-10-08.
Run base: `7d83184bea41668bac619324df0f62e61dd9f70f`.
Canonical base: `350c8ed6cf38d9a051bffe1edae1d0d54df10672`.
State: `2026-10-08.audit.145`.
Classification: proved candidate awaiting independent audit/promotion,
with a scoped collective-translation regression.
Registry: unreviewed; canonical=false. Level I and C-II remain open.

Rechecked after rebasing onto `2010296d3c00903423b67d96d70ae369d56b9e26`,
state `2026-10-08.audit.147`. The added supplied-crosscut bandwidth and
capsule-packing claims do not change the wall-release premises.

## 1. Closing implication and present limit

The finite-move implication under investigation is

    a full-source equal-cardinality weak packet behind an actual unit wall
      -> a collective translation opens every packet-to-wall contact
      -> a small dilation opens every internal packet contact
      -> deletion of an old contact or diameter pair contradicts the
         canonical lexicographic source; a diameter cover gives strict descent.

This report proves the two motion arrows under a total-wall-turn bound
below `2pi/3`, with strict tip clearance and no omitted internal guard.
An initially triangular packet is allowed: every new contact is opened
before the contact/diameter endpoint is invoked. The report does not
extract a packet with the required cardinality, move the wall, or supply
capacity after deleting a stress transversal. Neither C-II branch closes.

The other result is an exact triangle-free 529-site packet behind a
convex unit wall turning by less than `pi`. Every site separately meets
the local nonsurrounding condition, but the aggregate wall contacts
strictly surround the origin. No common nonzero translation is feasible
to first order. A small rigid rotation followed by a translation and
dilation nevertheless opens all its contacts. This is a regression only
against substituting independent site escape for collective translation.
It does not refute a general nonlinear packet-release theorem.

## 2. Geometry and full-source hypotheses

Let `A` be finite and unit-separated, `D=diam(A)`, and `K=conv(A)`.
Let `Q` be a convex hull-augmented face cell, with one actual
source-hull arc and one proper unit-contact path
`W=(v_0,...,v_m)`. Retain collinear hull labels and every source isolate.
Write `S_Q=(A intersect Q) minus W`, including labels on the hull arc.
These are the canonical cell objects, not an interior nonunit chord.

Orient the unit path with `Q` on its left. Its edge directions have
monotone lifted angles `theta_0,...,theta_{m-1}` and total turn
`T=theta_{m-1}-theta_0`. Assume

```math
T<2\pi/3.
\tag{CW1}
```

Let `Y subset int(Q)` be finite and unit-separated. Every site has
distance at least one from every wall vertex and strictly greater than
one from both path tips `v_0,v_m`. No internal guard is omitted.
Let `R` contain `S_Q` and satisfy `|R|=|Y|`; additional deleted labels
are allowed. Virtual guards at deleted wall labels are still required
by this stated theorem. No triangle-free assumption on `Y` is made.

The [weak full-source shield](../audits/target_c_exterior_cell_weak_guard_contact_ledger_independent_audit_2026-10-08.md)
protects all retained source points outside the unit path strictly.
For completeness, a segment from a site in `int(Q)` to an outside
retained label cannot first exit through the actual hull arc. At a
unit-wall crossing, weak unit clearance from both edge endpoints
puts both endpoints of the segment at least `sqrt(3)/2` from the
crossing, hence at least `sqrt(3)` apart. A path-vertex exit gives
distance at least two. All assigned nonwall source points in `Q`
belong to `S_Q` and are deleted. Thus only wall contacts need opening.
This checks outside contact isolates as well.

## 3. A common direction for every wall contact

For a unit packet-to-wall contact at an internal `v_j` put
`u=x-v_j`, `|u|=1`, and let its lifted angle be `alpha`.
The tangent cone of `Q` gives

```math
\theta_j<\alpha<\theta_{j-1}+\pi.
```

The weak guards at the two adjacent wall vertices give

```math
|u-e_{\theta_j}|^2\ge1,\qquad
|u+e_{\theta_{j-1}}|^2\ge1.
```

Because the relevant angles lie in the interior half-plane, these
inequalities imply

```math
\boxed{\theta_j+\pi/3\le\alpha\le\theta_{j-1}+2\pi/3.}
\tag{CW2}
```

This calculation uses all adjacent internal guards; it must not be
applied at an omitted guard. Tip contacts are excluded by hypothesis.
Taking the union over all sites and internal wall contacts,

```math
\alpha\in[\theta_0+\pi/3,\theta_{m-1}+2\pi/3].
\tag{CW3}
```

This one interval has width `T+pi/3<pi`. Let `n` be its unit bisector.
Every inward contact vector satisfies the uniform bound

```math
n\cdot u\ge c_T:=\cos((T+\pi/3)/2)>0.
\tag{CW4}
```

No relation between different packet sites was needed. Packet size,
internal contacts, and internal triangles do not change the direction.

Translate the entire packet by `t n`, with `t>0` sufficiently small.
At each former wall contact,

```math
|x+tn-v_j|^2=1+2t(n\cdot u)+t^2>1.
\tag{CW5}
```

All strict noncontact margins, tip guards and membership in `int(Q)`
persist by finiteness. Translation preserves every internal distance.
Now every packet-to-retained-source pair is strictly above one.

Dilate this translated packet by a factor `1+epsilon>1` about any
fixed point, with `epsilon` sufficiently small. All existing strict
margins and membership in `int(Q)` persist, while every internal
distance becomes strictly above one. Thus the final packet has no
new unit contact anywhere in the complete retained source.

All inserted-involving upper distances remain strict: for `x in int(K)`
and `z in K`, equality `|x-z|=D` would allow a small extension away
from `z` within `K`, contradicting `diam(K)=D`. Both finite steps
keep every site in `int(Q) subset int(K)`.

## 4. Exact canonical consequence

If `A` is the canonical triangle-free contact-minimal, then
diameter-pair-minimal global source, its retained induced contact graph
is triangle-free. The final packet is contact-free, so the complete
replacement is triangle-free regardless of the initial packet triangles.

If `R` deletes any old contact, the final contact count decreases.
If it deletes no contact but an old diameter pair, the contact count
stays equal and the diameter-pair count decreases. If it covers all
old diameter pairs, every retained and inserted pair is strictly below
`D`, giving a strict smaller-diameter source. Each is forbidden by the
canonical [contact/diameter endpoint](../audits/target_c_exterior_cell_weak_guard_contact_ledger_independent_audit_2026-10-08.md).

The theorem supplies an explicit motion for a packet satisfying CW1
and the complete guard hypotheses. It supplies no such packet.
In particular it does not evade Audit.140's one-omitted-guard capacity
barrier: the present theorem omits no internal guard at all.

One capacity corollary is

```math
\operatorname{Pack}_1\{x\in\operatorname{int}Q:
 |x-v_j|\ge1\ (0<j<m),\ |x-v_0|,|x-v_m|>1\}
=\operatorname{Pack}_1(E_Q)=|S_Q|,
\tag{CW6}
```

under CW1 and canonical strict cell capacity. The release takes any
finite weak packet of the left-hand cardinality into the all-strict
region `E_Q`, with strict internal distances. Conversely `E_Q` is a
subset of the weak region. Thus weak contacts alone give no extra
static capacity in this shallow-wall scope. The [strict cell capacity](../audits/target_c_exterior_internal_wall_vertex_capacity_independent_audit_2026-10-08.md)
is already canonical. No multi-cell or moving-wall capacity is claimed.

## 5. Exact larger-turn collective-translation regression

The guarded old path starts at `(-16/65,24+63/65)`, takes one unit
edge to `(0,24)`, then 25 steps `(7/25,-24/25)`, 514 horizontal
unit steps, 25 steps `(7/25,24/25)`, and one final unit step
`(16/65,63/65)`. Its end is `(528+16/65,24+63/65)`.
Its total turn is

```math
T=2\arccos(16/65)\in(2\pi/3,\pi).
```

Let `c=(264,1)`. The moving packet consists of the 529 distinct
interior sites along two 265-step unit chains from `(0,24)` and
`(528,24)` to `c`, omitting the two fixed tips and counting `c` once.
Their unit directions toward `c` are

```math
u_L=(264,-23)/265,\qquad u_R=(-264,-23)/265.
```

The packet-to-wall contacts are exactly the two former tips (now
internal guarded vertices of the extended wall) and the vertical
contact from `c` to `(264,0)`. The three inward contact vectors are
`u_L,u_R,(0,1)`, with positive balancing weights `1,1,46/265`.
They strictly surround the origin. A common translation `b` with
nonnegative derivatives at all three contacts would have all three
derivatives zero; noncollinearity forces `b=0`.

Every packet site separately has at most one wall contact. Its contact
vectors therefore do not surround it, and no site contacts both ends
of a wall edge. This verifies the distinction from
[Audit.145](../audits/target_c_strict_turn_path_non_surrounding_independent_audit_2026-10-08.md):
the one-site conclusion holds at every site but does not supply a
single translation for the whole packet.

Weight every chain contact by one and the bottom contact by `46/265`.
Every moving vertex is in exact positive pinned equilibrium. Consequently
no velocity field can strictly open a supported row to first order
while keeping every other supported row noncontracting: the weighted
first variations sum to zero. This is not full pinned rigidity.
There are only 531 moving-involving rows for 1,058 moving coordinates,
and most packet vertices have degree two.

Nevertheless a finite release exists. Set `t=10^{-7}`, rotate about
`c` using the rational Cayley rotation with tangent half-angle `t`,
translate upward by `t^2`, and dilate about the translated `c` by
`1+t^2`. The checker certifies every lower and upper source pair
and strict opening of every packet-involving contact. The wall is
fixed and its actual diameter remains `528+32/65`.

The complete 1,096-label initial source is triangle-free but nonglobal:
a `34-by-33` unit grid has enough sites and diameter squared `2113`,
strictly below the source diameter squared. Its two actual diameter
endpoints and low packet degrees fail the canonical global-source
requirements. It is a first-order/collective-translation regression,
not a canonical-source obstruction or a strict-D competitor.

## 6. Certificate boundary

`research/verify_target_c_collective_shallow_wall_release_2026_10_08.py`
checks the full pair census and finite endpoint for:

- a ten-site shallow-wall packet containing an actual unit triangle,
  with a retained outside contact isolate;
- the rational 529-site packet, including its entire positive pinned
  stress, triangle-freeness, collective force balance and nonlinear
  release.

The analytic theorem is proved in Sections 2–4. The script certifies
only these nonglobal finite fixtures, not the general theorem or
global packet extraction. No canonical theorem or lifecycle is changed.
