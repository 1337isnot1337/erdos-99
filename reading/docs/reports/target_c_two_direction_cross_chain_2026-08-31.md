> Generated reading edition · [exact source](../../../docs/reports/target_c_two_direction_cross_chain_2026-08-31.md) · source SHA-256 `9005f8cf0c636d1e214afcab361e37a1329349f7c2488fc004245dd842f94635`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-15E498FFAEA0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: exact cross-chain normal form

**Date:** 2026-08-31  
**Repository state:** `research/target-c-low-diameter-prestress-2026-08-31`  
**Run type:** proof / structural classification  
**Target:** Target C Gate C-I, low-diameter-support exception  
**Depends on:** C12 support connectivity and `target_c_low_diameter_prestress_2026-08-31.md`

## LEVEL I STATUS

`STILL OPEN`

The low-diameter prestress reduction leaves one apparent affine exception.  A
kernel-controlling normalized KKT stress can have exactly two positive diameter edges
and every positive contact can be parallel to one of those two diameter directions.

This report classifies that exception exactly.  It is not a two-dimensional grid or an
arbitrary rhombic web.  The positive contact support is precisely the union of two
straight full-diameter unit chains, one along each positive diameter chord.  Support
connectivity forces the two chains to meet at the geometric crossing of the two
diameter chords.  In a triangle-free source the diameter chords must be disjoint and
the acute angle between their lines is strictly larger than `60` degrees.

Thus the surviving two-direction mechanism is an exact **cross-chain**.

---

## 1. Setup

Fix a normalized KKT stress `s=(alpha,beta)` with exactly two positive diameter edges

```math
h_u=a_0a_D,
\qquad
h_v=b_0b_D,
\tag{C24.1}
```

of length `D`.  Their lines are nonparallel: two distinct diameter segments in a
planar diameter-`D` set cannot be collinear.

Choose unit vectors `u,v` parallel to the two diameter chords.  Assume the
**two-direction hypothesis**

```math
\boxed{
\text{every }ij\in C_s
\text{ is parallel to }u\text{ or }v.
}
\tag{C24.2}
```

This is exactly the exceptional case left by C21.1 when a two-diameter extreme stress
controls the critical-cone span but has no third projective stressed direction.

Let the positive diameter weights be

```math
\beta_u>0,
\qquad
\beta_v>0,
\qquad
\beta_u+\beta_v=1.
\tag{C24.3}
```

---

## 2. Equilibrium splits into two independent one-dimensional systems

At every positive-support vertex, KKT equilibrium is

```math
\sum_{ij\in C_s}\alpha_{ij}(p_i-p_j)
-
\sum_{ij\in H_s}\beta_{ij}(p_i-p_j)
=0.
\tag{C24.4}
```

Every vector in (C24.4) is parallel to `u` or `v`.  Since `u,v` are linearly
independent, the coefficients in the two directions vanish separately.

Therefore the `u`-members alone form a scalar one-dimensional equilibrium system, and
so do the `v`-members.  In the `u` system there is exactly one negative member,
`h_u`; every other member is a positive unit contact parallel to `u`.  The same holds
with `u` and `v` interchanged.

### Lemma C24.1 (no unloaded directional component)

Every positive `u`-contact belongs to the same one-dimensional component as `h_u`.
There is no nontrivial component consisting only of positive `u`-contacts.

#### Proof

Suppose a finite component of positive `u`-contacts contains no endpoint of `h_u`.
Choose a vertex of that component with maximal `u`-coordinate.  All incident
`u`-contact force vectors at that vertex point in the same weak `+u` direction, and at
least one is nonzero.  Their positive scalar sum cannot vanish.  This contradicts the
separate `u`-equilibrium equation. `square`

The same proof works in the `v` direction.

---

## 3. Each directional support is the exact full-D unit chain

### Theorem C24.2 (directional chain theorem)

The complete positive `u`-contact support is

```math
\boxed{
a_k=a_0+ku,
\qquad k=0,1,\ldots,D,
}
\tag{C24.5}
```

with contacts `a_ka_{k+1}` for `0<=k<D`.  In particular `D` is an integer.  Every
such contact has stress

```math
\boxed{
\alpha_{a_ka_{k+1}}=D\beta_u.
}
\tag{C24.6}
```

Likewise the complete positive `v`-contact support is

```math
\boxed{
b_\ell=b_0+\ell v,
\qquad \ell=0,1,\ldots,D,
}
\tag{C24.7}
```

with constant contact stress `D beta_v`.

#### Proof

By Lemma C24.1, every positive `u`-contact lies in the component containing the unique
negative `u`-member `a_0a_D`.  Because contact edges parallel to `u` join points at
unit distance, each vertex has at most one possible contact neighbor in the `+u`
direction and at most one in the `-u` direction.  Hence the positive contact part of
this directional component is a collection of unit-step subchains on the line through
`a_0a_D`.

Endpoint equilibrium at `a_0` contains the negative diameter force of magnitude
`D beta_u`, so it requires a positive unit-contact force directed into the diameter
segment.  No contact can extend beyond `a_0` away from `a_D`, because such a point
would be farther than `D` from `a_D`, contradicting the source diameter.  Thus the
first contact is from `a_0` to `a_0+u`, with weight `D beta_u`.

At the next vertex the separate one-dimensional equilibrium equation forces a contact
of the same weight continuing in the `+u` direction unless the vertex is `a_D`.
Iterating gives unit-spaced vertices all the way to `a_D`.  Finite equilibrium cannot
terminate before the negative member's opposite endpoint, and it cannot overshoot that
endpoint by the diameter bound.  Therefore `D` is an integer and the chain is exactly
(C24.5), with constant stress (C24.6).

The `v` statement is identical. `square`

### Corollary C24.3 (support is exactly two chains)

Under the two-direction hypothesis,

```math
\boxed{
C_s
=\{a_ka_{k+1}:0\le k<D\}
\cup
\{b_\ell b_{\ell+1}:0\le\ell<D\}.
}
\tag{C24.8}
```

There are no additional positive contacts on parallel translated lines.

---

## 4. C12 forces the chain crossing to be a source point

Target C12 says the positive contact graph `C_s` has exactly one nontrivial connected
component.  By Corollary C24.3 it is the union of the `u` chain and the `v` chain.
Therefore the two chains share a vertex.

The two supporting lines are nonparallel and hence have a unique intersection point
`o`.  Consequently:

### Theorem C24 (exact cross-chain normal form)

There exist integers

```math
r,s\in\{0,1,\ldots,D\}
```

such that

```math
\boxed{
o=a_r=b_s.}
\tag{C24.9}
```

Thus the geometric intersection of the two positive diameter chords is itself a source
point and a vertex of both full unit chains.

No other intersection between the chains is possible.

---

## 5. Triangle-freeness excludes the shared-endpoint phase

Suppose the two positive diameter chords shared an endpoint `o`.  Let `a_1=o+u` and
`b_1=o+v` be the first unit-chain neighbors directed along the two chords.  If `theta`
is the angle between the two diameter rays, then the elementary diameter inequality
for two length-D chords sharing an endpoint gives

```math
0<\theta\le\frac\pi3.
\tag{C24.10}
```

Therefore

```math
|a_1-b_1|
=2\sin\frac\theta2
\le1.
\tag{C24.11}
```

Unit separation forbids strict inequality.  Equality would make

```math
o,a_1,b_1
```

a unit equilateral triangle, forbidden by the triangle-free hypothesis.  Hence a
triangle-free source cannot realize the shared-endpoint cross-chain.

So the two positive diameter edges are disjoint.  Their segments cross properly, and
`o` lies in the relative interior of both diameter chords.  In particular

```math
1\le r,s\le D-1.
\tag{C24.12}
```

---

## 6. The crossing angle is strictly larger than 60 degrees

Let `phi in (0,pi/2]` be the acute angle between the two chain lines.  Since `o` is an
interior vertex of both full chains, all four points

```math
o\pm u,
\qquad
o\pm v
```

belong to the source.

Unit separation gives, in particular,

```math
|u-v|=2\sin\frac\phi2\ge1.
\tag{C24.13}
```

Hence

```math
\phi\ge\frac\pi3.
\tag{C24.14}
```

If equality held, `o,o+u,o+v` would be a unit equilateral triangle.  Therefore:

### Corollary C24.4 (strict cross angle)

For a triangle-free source in the two-direction phase,

```math
\boxed{
\frac\pi3<\phi\le\frac\pi2.
}
\tag{C24.15}
```

Equivalently, the two full diameter chains cross at an acute angle strictly between
`60` and `90` degrees, inclusive at `90`.

---

## 7. Stress-matrix decomposition

The classification also makes C20 transparent in this exceptional phase.  Let
`Omega_u` be the normalized one-chain matrix

```math
D L_{\rm path}(a_0,\ldots,a_D)-L_{a_0a_D},
```

and define `Omega_v` analogously.  Then

```math
\boxed{
\Omega_s
=\beta_u\Omega_u+\beta_v\Omega_v.
}
\tag{C24.16}
```

Each summand is PSD by the one-chain Cauchy–Schwarz identity.  Their scalar kernels
consist of functions affine along the corresponding chain.  Because the chains meet at
`o` and their directions are independent, the intersection of those two kernels is
exactly

```math
\operatorname{span}\{\mathbf1,x,y\}.
```

Thus the cross-chain normal form independently recovers the PSD/maximal-rank conclusion
of C20 in the exceptional two-direction case.

The single non-Euclidean vector-valued kernel mode modulo rigid motions is precisely an
infinitesimal change of the angle between the two rigid unit chains.

---

## 8. Consequence for C-I-low

Combine C21.1 with C24.

> **Low-diameter weak-contact dichotomy.**  If a contact-minimal triangle-free global
> minimizer has a weak unit contact and `|H_*|=2`, then a kernel-controlling extreme KKT
> stress supplied by C21 has one of only two forms:
>
> 1. **single-chain kernel:** it uses one positive diameter edge and is the exact full-D
>    unit chain along that chord; or
> 2. **cross-chain kernel:** it uses both positive diameter edges and its positive
>    support is exactly two full-D unit chains crossing at a common source point at
>    acute angle `phi>60 degrees`.

All other two-diameter stress geometries force a third projective stressed direction,
which collapses the affine kernel to Euclidean motions and invokes C7 to remove the weak
contact.

This is much narrower than the previous description as a generic two-direction affine
phase.

---

## 9. What is still open

The cross-chain itself has an exact finite angle-changing flex if considered in
isolation: keep every unit step on both chains equal to one and vary the angle between
the two lines.  The remaining difficulty is that `s` need not contain **all** strong
contacts `C_*`.  Strong constraints absent from the controlling extreme stress can
block that finite angle change at second order even though their first variations vanish
on the critical cone.

Therefore C24 does not yet integrate the weak-release velocity globally.

The exact next question is now:

> **Cross-chain propagation theorem.**  If the span of the fixed-D critical cone lies
> in the affine kernel of an extreme cross-chain stress, prove either that every strong
> contact is compatible with the same finite chain-angle flex, or that some third
> projective direction must enter every kernel-controlling KKT stress.

A proof would eliminate the cross-chain branch of C-I-low.

For the single-chain phase, the analogous target is to propagate the rigid motion of
one full diameter chain to the second strong diameter chord.

---

## 10. Audit table

| Claim | Status | Reason |
| --- | --- | --- |
| Directional equilibrium decouples | **proved** | Two nonparallel member directions form a basis. |
| Each directional positive support is a unique full-D unit chain | **proved** | No unloaded finite positive 1D equilibrium component; endpoint propagation and diameter bound. |
| Two chains meet at a source point | **proved** | C12 connectedness plus unique line intersection. |
| Shared-endpoint two-direction phase is triangle-free | **false / excluded** | First chain neighbors are at distance `<=1`; equality is a unit triangle. |
| Cross-chain acute angle `>60 degrees` | **proved** | Four unit neighbors at the interior crossing plus triangle-free strictness. |
| Cross-chain support has an isolated finite angle flex | **proved** | Preserve both chain step lengths while varying their angle. |
| That finite flex automatically extends through all of `C_*` | **not proved** | Strong contacts absent from the extreme stress may create higher-order obstruction. |

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C24 exact cross-chain normal form:
Suppose a normalized KKT stress has exactly two positive diameter edges and every
positive contact is parallel to one of those two diameter directions. Equilibrium
splits by direction. In each direction the unique negative diameter member forces the
entire positive contact support to be the exact straight unit chain joining its
endpoints, with constant contact stress D*beta_direction. There can be no other
parallel positive-contact component.

C12 then forces the two full-D chains to share their unique line intersection, so the
crossing point is itself a source point and D is integer.

In a triangle-free source the diameter chords cannot share an endpoint: their first
unit-chain neighbors would be at distance <=1, with equality giving a unit triangle.
Thus the two H edges are disjoint crossing chords, the common chain vertex is interior
to both, and the acute crossing angle satisfies

    60 degrees < phi <= 90 degrees.

Therefore the C21 two-direction exception is exactly an X-shaped pair of full diameter
unit chains, not an arbitrary affine grid.

Remaining C-I-low phases:
1. one full-D chain controls the critical-cone span while the other H chord shears;
2. an exact cross-chain extreme stress controls the critical-cone span.

Next: propagate the isolated chain/cross-chain finite flex through the strong contacts
missing from the controlling extreme stress, or force a third stressed direction into
every controlling stress.
```
