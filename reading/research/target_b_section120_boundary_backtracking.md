> Generated reading edition · [exact source](../../research/target_b_section120_boundary_backtracking.md) · source SHA-256 `1a4f2b87186a61cc6bc22e49c593a3e03914ec9bafc059160a83526150a051ad`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target B — Section 120: exact boundary backtracking for backward trains

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN.**  
**Status:** proof-only research candidate pending independent hostile audit.

The Target-B train-angle stack has long contained the proposed estimate

```math
\sum_{\lambda_\tau<0}(-\lambda_\tau)
\le {D\over2}(L-D),
```

where `L` was intended to be a suitable boundary arc joining an active diameter pair.
The 2026-08-30 mathematical audit correctly left this **unproved** because neither the
arc nor a non-overcounted charging map from backward trains to boundary occurrences had
been defined.

The train pseudoline / partial-cube geometry and the signed terminal-orientation
bookkeeping now supply exactly that missing map.  In a simply connected pure strict-
rhombic disk, **either** boundary arc joining the diameter endpoints works.

The result is finite and exact.

---

## 120.1 Setup

Let `mathcal R` be a finite simply connected pure strict-unit-rhombus disk.  Its outer
boundary is a simple cycle of unit contact edges.  Let `z,a` be vertices with

```math
r:=p_a-p_z,
\qquad |r|=D,
\qquad q:={r\over D}.
\tag{120.1}
```

For every train `tau`, choose an arbitrary unit edge direction `u_tau`.  The standard
train-coordinate representation of the diameter vector is

```math
r=\sum_\tau d_\tau u_\tau,
\qquad d_\tau\in\{-1,0,1\}.
\tag{120.2}
```

A train is separating for `z,a` iff `d_tau!=0`.  For such a train define

```math
a_\tau:=d_\tau u_\tau.
\tag{120.3}
```

Canonical train-coordinate geometry orients `a_tau` from the `z`-side of the train to
the `a`-side.  In particular

```math
r=\sum_{\tau\in P(z,a)}a_\tau,
\qquad |a_\tau|=1.
\tag{120.4}
```

Define

```math
\lambda_\tau:=r\cdot a_\tau.
\tag{120.5}
```

A separating train is **backward** for the diameter pair when

```math
\lambda_\tau<0.
```

This is the same signed coefficient used in the exact train-angle Hessian

```math
\mathrm d^2f_{za}[v,v]
=-\sum_\tau\lambda_\tau(v_\tau-\bar v)^2.
\tag{120.6}
```

Let `Gamma` be either one of the two outer-boundary arcs from `z` to `a`, directed from
`z` to `a`, and let `L=|Gamma|` be its number of unit edges.

## 120.2 Every separating train has one canonically oriented terminal edge on each arc

Canonical Theorem 10.6 realizes every complete train as a proper simple crosscut of
the rhombic disk.  The train crosses precisely the contact edges carrying its fixed
edge direction, and its two terminal contact edges lie on the outer boundary.

Fix a separating train `tau`.  Its crosscut divides the disk into two sides, one
containing `z` and the other containing `a`.  Its two boundary endpoints split the
outer boundary into two arcs, one lying on each side.  Consequently each boundary arc
from `z` to `a` contains exactly one terminal edge occurrence of `tau`.

Traverse `Gamma` from `z` to `a`.  At that terminal edge, `Gamma` crosses the train
from the `z`-side chamber to the `a`-side chamber.  Therefore the directed unit vector
of this boundary edge is exactly

```math
\boxed{a_\tau,}
\tag{120.7}
```

not `-a_tau`.

Distinct trains have distinct terminal boundary-edge occurrences: a contact edge is
carried by exactly one train.  Thus

```math
\tau\longmapsto e_\tau(\Gamma)
```

is an injective charging map from the separating trains to edge occurrences of either
chosen boundary arc.

This is the missing topological/orientation statement in the old proposed Section
37.7.

## 120.3 Exact boundary projection identity

Write the directed unit edge vectors of `Gamma` as

```math
v_1,\ldots,v_L.
```

Their sum is the diameter vector:

```math
\sum_{j=1}^L v_j=r=Dq.
```

Therefore

```math
\boxed{
L-D
=\sum_{j=1}^L(1-q\cdot v_j).
}
\tag{120.8}
```

Every summand is nonnegative because `|q|=|v_j|=1`.

For the terminal edge assigned to a separating train `tau`, (120.7) gives the exact
loss

```math
1-q\cdot a_\tau
=1-\frac{\lambda_\tau}{D}.
\tag{120.9}
```

If `tau` is backward, put

```math
x_\tau:={-\lambda_\tau\over D}.
```

Since `|r|=D` and `|a_tau|=1`,

```math
0<x_\tau\le1.
\tag{120.10}
```

Its charged boundary edge contributes exactly

```math
1+x_\tau.
\tag{120.11}
```

## 120.4 Boundary backtracking theorem

Let

```math
P_-(z,a):=\{\tau:\lambda_\tau<0\},
\qquad
S_-(z,a):=
\sum_{\tau\in P_-(z,a)}(-\lambda_\tau).
```

Injectivity of the charge and (120.8)--(120.11) give the stronger raw estimate

```math
\boxed{
L-D
\ge
|P_-(z,a)|+{S_-(z,a)\over D}.
}
\tag{120.12}
```

Because `1+x>=2x` for `0<=x<=1`, they also give

```math
L-D
\ge2\sum_{\tau\in P_-}x_\tau
={2S_-(z,a)\over D}.
```

Hence:

### Theorem 120.1 — exact boundary backtracking

For **either** outer-boundary arc `Gamma` from `z` to `a`,

```math
\boxed{
\sum_{\lambda_\tau<0}(-\lambda_\tau)
\le
{D\over2}(L-D).
}
\tag{120.13}
```

This is exactly the old proposed equation (37.7), now with a canonical arc and a
non-overcounted proof.

Equation (120.12) also gives the complementary count-sensitive bound

```math
\boxed{
S_-(z,a)
\le
D\bigl(L-D-|P_-(z,a)|\bigr).
}
\tag{120.14}
```

In particular, any backward train forces strictly more than one unit of boundary
projection excess on each diameter-joining boundary arc.

## 120.5 Shorter-arc corollaries

Let the two outer-boundary arcs joining `z` and `a` have lengths `L_1,L_2`.  In a pure
rhombic disk every train has exactly two physical outer-boundary ends, so if `T` is the
number of trains then the outer-boundary length is

```math
B=2T=L_1+L_2.
\tag{120.15}
```

Let

```math
L_*:=\min(L_1,L_2)\le T.
```

Every unit-edge path joining Euclidean distance `D` has length at least `D`, so
`L_*>=D`.  Theorem 120.1 gives

```math
\boxed{
S_-(z,a)
\le {D\over2}(L_*-D)
\le {D\over2}(T-D)
={D\over4}(B-2D).
}
\tag{120.16}
```

The raw bound (120.12) also yields

```math
\boxed{|P_-(z,a)|<L_*-D\le T-D}
\tag{120.17}
```

whenever at least one backward train exists; with integer lengths the obvious integral
rounding can be applied.

Thus both the number and total signed weight of backward incidences are controlled by
literal boundary detour beyond a Euclidean geodesic.

## 120.6 Positive quadratic curvature is boundary-detour limited

For a first-order-neutral train-angle velocity `v`, put

```math
\eta_\tau:=v_\tau-\bar v.
```

The exact signed-variance formula is

```math
\mathrm d^2f_{za}[v,v]
=-\sum_\tau\lambda_\tau\eta_\tau^2.
```

Discarding the nonpositive contributions from `lambda_tau>=0`,

```math
\mathrm d^2f_{za}[v,v]
\le
\sum_{\lambda_\tau<0}(-\lambda_\tau)\eta_\tau^2
\le
S_-(z,a)\|\eta\|_\infty^2.
```

Therefore either boundary arc gives

```math
\boxed{
\mathrm d^2f_{za}[v,v]
\le
{D\over2}(L-D)\|v-\bar v\|_\infty^2.
}
\tag{120.18}
```

and the shorter arc gives

```math
\boxed{
\mathrm d^2f_{za}[v,v]
\le
{D\over2}(T-D)\|v-\bar v\|_\infty^2.
}
\tag{120.19}
```

These inequalities quantify the old statement that positive quadratic curvature must
be paid by boundary backtracking.

A diameter pair whose shorter boundary arc is an exact `D`-edge geodesic has no
backward train incidences at all, so its quadratic Hessian is negative semidefinite on
the first-order-neutral space.

## 120.7 Relation to signed train-return

The proof is the one-arc, diameter-specific specialization of the signed terminal
orientation principle developed in the recent Target-C return-capacity work, but it
uses additional pure-disk train-coordinate information:

1. every separating train is a proper crosscut;
2. the coefficient `a_tau=d_tau u_tau` is oriented from the `z` side to the `a` side;
3. either boundary arc therefore contains one uniquely oriented terminal edge from
   every separating train.

The general signed-return theorem aggregates two terminal ends of a train against a
small host set.  The present theorem instead uses a single terminal end and the known
diameter direction `q`, which is why it recovers the signed coefficient
`lambda_tau=r·a_tau` exactly.

## 120.8 Scope and the remaining Target-B obstruction

The theorem is finite and exact, but its scope is the simply connected pure
strict-rhombic disk where standard train coordinates and proper train crosscuts are
available.  It does not automatically cross exceptional faces, holes, multiple
rhombic components, or outside source vertices.

Most importantly, it closes only the old **quadratic backward-incidence** gap.  The
second-pass audit correctly identified a separate higher-order mechanism: separating
trains with

```math
\lambda_\tau=0
```

can block at quartic order in balanced tangent classes.  Equation (120.13) says nothing
about those zero-weight tangent incidences.  Therefore Section 120 does **not** close
Target B or LEVEL I.

The next structural target is now sharper: combine the finite backward-mass bound with
the existing tangent-class quartic theorem and the ordered pseudoline shell to prove
that the boundary cannot simultaneously provide enough detour for the backward
quadratic modes and enough tangent-pair capacity for all residual first-order modes.

**Theorem state:** unchanged.  Independent hostile audit is required before replacing
the `UNPROVED` label in canonical Section 37.5.
