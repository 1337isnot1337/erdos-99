> Generated reading edition · [exact source](../../research/target_c_section129_corridor_phase_purity.md) · source SHA-256 `56cd238217a75d7458d0e7fcfbdfc9dd2f8b7ba314226e0a8f1f2967a352672d`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8d18d3b80dbfedcd24b6219a282d1dd3b43e8cef", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section129_corridor_phase_purity.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "dca6fe36a60a30af3b0f965fb44d81a2148cc50ff9d23228cb38fe18a6efa550"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — Section 129: macroscopic inactive corridors are phase-pure endpoint hosts

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** proof-only Type-II structural theorem.
**Dependencies:** canonical Section 84 and proof-only Sections 127–128 for the harmonic-cell/train corollaries.

Let `C` be a convex unit-edge polygon of degree `k`. Choose farthest boundary vertices
`a,b`, put

```math
r:=|a-b|=\operatorname{diam}C,
\qquad q:={b-a\over r},
```

and for `0<eta<=pi/2` let `N_C(eta)` count boundary edge occurrences whose projective
direction is at angular distance at least `eta` from `[q]`.

Then

```math
\boxed{
N_C(\eta)\le {k-2r\over1-\cos\eta}.
}
\tag{129.1}
```

A weighted form is

```math
\boxed{
\sum_{e\subset\partial C}(1-|q\cdot u_e|)
\le k-2r,
}
\tag{129.2}
```

where `u_e` is either unit orientation of the edge direction.

## 129.1 One-route projection identity

For a directed unit-edge path from `a` to `b`, with oriented steps `v_i` and length
`m`,

```math
\sum_i v_i=rq,
```

hence exactly

```math
m-r=\sum_i(1-q\cdot v_i).
\tag{129.3}
```

If the projective direction of `v_i` is at least `eta` from `[q]`, then its oriented
angle from `q` lies in `[eta,pi-eta]`, so

```math
q\cdot v_i\le\cos\eta
```

and that occurrence costs at least `1-cos eta` in (129.3).

## 129.2 Pay both boundary arcs once

The two boundary arcs from `a` to `b` have lengths `m_+` and `m_-` with
`m_++m_-=k`. Orient both arcs from `a` to `b`. Their occurrence sets are disjoint and
each has displacement `rq`. Applying (129.3) to both gives total route excess

```math
(m_+-r)+(m_--r)=k-2r.
```

Every projectively `eta`-bad occurrence costs at least `1-cos eta`, proving (129.1).

For (129.2), if the route orientation of occurrence `e` is `v_e=+-u_e`, then

```math
q\cdot v_e\le|q\cdot u_e|,
```

so

```math
1-|q\cdot u_e|\le1-q\cdot v_e.
```

Summing the two route identities proves (129.2).

## 129.3 Type-II macroscopic faces are occurrence-counted phase-pure

Let `C_D` be a sequence of bounded nonquadrilateral global contact faces with

```math
{\deg C_D\over D}\to\lambda>0.
```

Canonical Section 84 gives

```math
{\operatorname{diam}C_D\over D}\to{\lambda\over2},
```

hence

```math
\deg C_D-2\operatorname{diam}C_D=o(D).
\tag{129.4}
```

For every fixed `eta>0`, (129.1) therefore yields

```math
\boxed{N_{C_D}(\eta)=o(D).}
\tag{129.5}
```

Likewise (129.2) gives

```math
\boxed{
\sum_{e\subset\partial C_D}(1-|q_D\cdot u_e|)=o(D).
}
\tag{129.6}
```

Thus all but `o(D)` physical boundary occurrences of a macroscopic inactive corridor
lie in one projective phase window at every fixed angular scale.

## 129.4 Harmonic train endpoints

Section 127 identifies bounded harmonic-cell defect faces with actual global bounded
faces, preserving physical boundary contact occurrences. A complete strict-rhombus
train endpoint on such a face is one of those occurrences, with train projective phase
equal to the terminal contact direction.

Therefore a macroscopic local defect face can contain only `o(D)` terminal occurrences
from any train-phase window separated by a fixed positive angle from its corridor
direction.

Section 128 adds injectivity at the train level: one complete train cannot use the same
bounded face at both ends. Hence a linear endpoint population on one macroscopic face
corresponds to linearly many distinct trains, all but `o(D)` of one projective phase.

## 129.5 Signed-return host interpretation

Cutting a macroscopic corridor cycle at its diameter pair creates two routes with
antipodal hosts `q_D,-q_D`. Their total excess is exactly

```math
\deg C_D-2\operatorname{diam}C_D=o(D).
```

The support width of that host pair for train direction `u` is `2|q_D·u|`; the return
deficit is

```math
2(1-|q_D\cdot u|).
```

Equation (129.2) explains physically why the host pair can have small return deficit
for the endpoint cohort actually assigned to its corridor: the total alignment defect
is paid by the same corridor route excess. Conversely, a fixed-angle transverse
endpoint costs a fixed positive amount, so only `o(D)` such endpoints can be hosted by
an `o(D)`-excess corridor.

This prevents treating a macroscopic corridor as a directionally arbitrary free host.
It does not by itself close C-II: an oblique parallelogram rhombus patch realizes
multiple phase-aligned straight corridors with zero route excess. A closing theorem
must use source-specific global force-hull, loaded-interface, KKT, or minimality
information absent from that regression.

**Disposition:** proved proof-only Type-II phase-purity theorem. C-II remains open.
