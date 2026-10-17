> Generated reading edition · [exact source](../../../docs/reports/target_c_one_spare_site_contact_minimality_endpoint_2026-10-05.md) · source SHA-256 `afd5a20ba695bd56ee8306beb1a0f78b961176b2a7b239603670f4e6466814f5`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-4D8046BD79F1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — one spare site suffices in both canonical branches

Date: 2026-10-05. Base: `3c94a1a93641a5f8fa24d43068d487594d3e38cd`.
State: `2026-10-05.audit.57`. Classification: **proved candidate synthesis
awaiting independent audit**; registry status remains **unreviewed**.
Level I and C-II remain open. No computation or external literature is used.

## 1. Provenance and exact implication

This mechanism is present in the unpromoted September report
[open-guard packing saturation, Theorem 3.1](target_c_open_guard_packing_saturation_2026-09-12.md).
It is rederived here from canonical contact-first normalization and the
canonical strict wall-refill contract at audit.57. It is not claimed as a
new packing theorem or silently promoted from the older report.

```
one strict surplus site in an actual protected region
-> replace its old population and delete one nonisolated source vertex
-> same-cardinality triangle-free source with diameter <= D and fewer contacts
-> contradict canonical contact minimality or diameter optimality.
```

This endpoint needs neither a diameter cover nor the value of s_Z. It
therefore applies equally to s_Z=o(D), s_Z=Omega(D), and the macroscopic
inactive-container branch.

## 2. Finite theorem

Let A be a triangle-free global minimum-diameter source of cardinality n,
chosen to minimize its unit-contact count among all triangle-free global
minimizers of that cardinality. Assume it has a nonisolated contact vertex.
Let S be a set of explicitly removed source labels. Let Y be a finite
packet such that:

1. |Y|>=|S|+1;
2. all distinct pair distances in Y are >1 and <D;
3. all distances from Y to A\S are >1 and <D.

Then A cannot exist with this packet.

Choose a nonisolated vertex v. If v lies in S, keep any |S| points from Y,
remove S and insert them. Otherwise keep |S|+1 points, remove S union {v}
and insert them. In both cases cardinality is unchanged, retained old
pairs satisfy their original constraints, and all new pairs are strict.
The contact graph is an induced subgraph of the old triangle-free graph
plus isolated new vertices. At least one original contact incident to v
has disappeared, and no contact is introduced. If the new diameter is
<D, global optimality fails; if it is D, the new triangle-free global
minimizer has fewer contacts, contradicting normalization. QED.

The same proof with |Y|>=|S| suffices whenever S already contains a
nonisolated vertex. This is the canonical embedded-wall theorem's
contact-minimality endpoint, now stated independently of a particular wall.

## 3. Protected packets and the full source

For disjoint actual unit-contact walls, let S be the union of *all* old
interior populations. Canonical `C-EMBEDDED-WALL-REFILL` gives simultaneous
strict new-old clearance for packets inside the open wall-safe sets.
Small packet dilation supplies strict new-new clearance. Interior-hull
location supplies strict upper bounds. Thus aggregate capacity

    sum M_i >= sum |S_i|+1

already contradicts the canonical source. The deleted v may be a wall
vertex: clearance was verified at its original position and deletion
cannot spoil it. Every source isolate is retained or explicitly replaced;
there is no extension of the §57 affine kernel to isolate coordinates.

The same argument applies to actual noncontact walls satisfying the
**unpromoted** [sqrt(3) shield candidate](target_c_noncontact_wall_shield_2026-10-05.md),
conditional on audit of that finite shield. More generally it applies
directly whenever an actual finite packet satisfies the three pair
conditions above, whether or not a polygon is used.

## 4. Relation to the residual-cage release theorem

The [candidate residual-cage theorem](target_c_residual_cage_release_refill_2026-10-05.md)
proves a strict sub-D competitor when surplus pays kappa(H,G), and
kappa<=tau_*<=s_Z+1. Positive KKT stationarity prevents a strict shortening
direction when U is empty, so kappa>=1 for a canonical source with
nonempty H. For m=0, deleting no rows likewise leaves nonempty H and no
shortening direction. Therefore any packet surplus sufficient to pay
kappa is already excluded by Section 2, without moving the source.

The residual-cage theorem remains a valid strict-diameter construction
and can matter when a packet has weak contacts, when a different source
normalization is used, or when strict packet geometry is available only
after a motion. But for strict packets at the original canonical source,
requiring their surplus to pay s_Z+1 overstates the necessary capacity.
In this setting the strongest spendable endpoint is **one spare site**.

This does not turn linear train currency into capacity. It narrows the
missing theorem to an exact integer existence statement rather than a
comparison of two linear coefficients.

## 5. Quantifiers and remaining obstruction

If any triangle-free global minimizer of a fixed cardinality exists,
its contact count is a nonnegative integer. Hence one can choose a
triangle-free global minimizer with the least such count and then with
least diameter-pair count. Canonical `C-ZTA` / the
[C-I restoration module](../targets/target-c/56-ci-restored-frontier.md)
provides the exact source scope used throughout Target C.

Thus a theorem producing the Section 2 packet for *every sufficiently
large canonical source*, in both exhaustive branches, would exclude every
sufficiently large triangle-free global minimizer. Conversely, a packet
for only one favorable source or one subbranch does not prove Level I.

Audit.57 rules out spare sites in preserved terminal pentagons. The
large-wall lock regression rules out obtaining one site just from positive
residual and large near-triangular walls. Those exact obstructions remain.
A quantitative contact-breaking motion, a capacity-improving composite
region, or a different finite replacement is still required.

No existence theorem for the required packet has been proved here. This
report records the current closing endpoint, not Level I closure. Its
next obligation is: construct one actual strictly protected surplus site
(after explicitly replacing its old population) in every surviving source,
or prove an alternative contradiction excluding sources without one.

## 6. Dependencies and classification

Canonical inputs: `C-ZTA` for contact-first normalization;
`C-EMBEDDED-WALL-REFILL` for the unit-wall application. The finite packet
theorem itself is proved directly above. The older open-guard report is
prior art, not a load-bearing premise. The long-edge shield and residual
cage reports remain unreviewed candidates on this branch.

| Claim | Classification | Effect |
| --- | --- | --- |
| One strict spare site excludes canonical source | Proved candidate synthesis awaiting audit | Capacity target reduced to one |
| Application to original unit-wall packets | Proved candidate synthesis awaiting audit | Both exhaustive branches |
| Application to noncontact walls | Conditional on shield audit | Wider geometric extraction scope |
| Every canonical source has a spare site | Unproved | No branch or Level I closure |

No authoritative state, route, or prompt is changed.
