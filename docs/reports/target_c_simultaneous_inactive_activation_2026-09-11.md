<!-- theorem-state: {"artifact_id":"ART-51A17348657C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — simultaneous deep activation preserves the force core

**Date:** 2026-09-11  
**Repository base:** `67f66ac`  
**State version:** `2026-09-11.audit.33`  
**Run type:** C-II closing-proof attempt / exact transport and no-go result  
**Classification:** proved candidate awaiting independent audit; noncanonical  
**Active prompt:** [current Target C prompt](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md)  
**External literature search / mathematical computation:** not used

## LEVEL I STATUS

**STILL OPEN. Neither global C-II branch is closed.**

## 1. Endpoint tested

The promoted deep-matching theorem supplies `Omega(D)` vertex-disjoint pairs of
contact-isolated source points at distances in `(1,1+K/D]`, at any fixed depth in
one actual inactive chamber. A natural proposed closing step is to turn that family
into compatible exact contacts and use the resulting constraints to reach the loaded
core.

This report proves the compatible-activation step, including all first blockers.
It also proves that these activations leave the entire normalized KKT polytope
unchanged. Thus their existence supplies no contradiction to the minimum-contact
representative: they increase its contact count through universally zero-stressed
edges. The separate [finite escape-barrier report](target_c_core_escape_barrier_2026-09-11.md)
shows that continuing any diameter-nonincreasing motion cannot unlock the original
post-ZF core either.

The intended chain was

```text
deep matching -> simultaneous exact contacts -> new force support -> contradiction.
```

The first arrow below is proved quantitatively. The second arrow is false for this
construction: all the new contacts are universally unsupported.

## 2. Finite simultaneous-activation theorem

Let `A` be a labeled triangle-free unit-separated planar source of diameter `D>1`.
Let `C_0` be a convex chamber contained in `conv(A)`, with no nonisolated contact
vertex in its interior. Suppose a matching of `M` pairs `x_i,y_i` of contact-isolated
source points satisfies

\[
1<|x_i-y_i|\le1+\epsilon,\qquad
x_i,y_i\in(C_0)_{-w},
\qquad w>1,\quad 0<\epsilon<1/4.
\tag{SA.1}
\]

Here `(C_0)_{-w}` is the inner parallel body at distance `w`. Assume at least one
original diameter pair remains outside these movable isolate labels. This is
automatic in the canonical C-II application, where every diameter endpoint is in
the original positive core.

### Theorem SA

There is a family of at least

\[
\boxed{N\ge\lceil M/81\rceil}
\tag{SA.2}
\]

independent one-point motions, each of length at most `epsilon`, whose full Cartesian
product is a cube of triangle-free unit-separated configurations of diameter exactly
`D`. All original unit contacts and all original diameter pairs remain unchanged.

At the far corner of the cube:

1. at least `N` new contacts have been created;
2. the new nontrivial contact components are `N` pairwise vertex-disjoint stars;
3. every vertex of each star is an original contact isolate in `int(C_0)`;
4. no new diameter pair has been created;
5. for every normalized KKT equilibrium stress, every new contact coefficient is
   zero; and
6. after adjoining these zero coordinates, the normalized KKT polytope is exactly
   the original one.

If `A` is a global minimum-diameter source, every point of this cube is a global
minimum-diameter source of the same cardinality.

### Proof: choose separated movers

Choose one endpoint `x_i` from each matched pair. These `M` points are unit-separated.
At most 81 of them lie in any radius-four closed disk centered at one of them: their
open radius-`1/2` disks have disjoint interiors and lie in a radius-`9/2` disk, so the
ratio of areas is 81.

Greedily retain one endpoint and discard all remaining endpoints at distance at most
four. Each selection discards at most 81 candidates. Thus at least `ceil(M/81)`
endpoints remain, and their pairwise distances are strictly greater than four. Call
them `x_1,...,x_N`, retaining their original stationary mates `y_i`. A mate cannot be
one of the selected movers, because the original pairs form a matching and only one
endpoint from each pair was eligible to move.

### Proof: stop each mover at its first contact

For each `i`, move `x_i` along its original segment toward `y_i`, with every other
source point provisionally fixed. Its original distance to every point is strictly
greater than one. At travel distance `|x_i-y_i|-1<=epsilon`, its mate is exactly one
unit away. By continuity there is a first travel distance

\[
0<\ell_i\le\epsilon
\tag{SA.3}
\]

at which some source distance reaches one. Stop there; ties between several first
blockers are allowed. Before stopping, every lower-distance inequality is strict;
at the endpoint all remain valid and at least one is equality.

The whole segment lies in the convex inner parallel body `(C_0)_{-w}`. Consequently
it stays at distance at least `w>1` from every point outside `int(C_0)`. Its first
blockers are therefore in `int(C_0)`, which contains no original nonisolated vertex.
All first blockers are original contact isolates.

Every first blocker of mover `i` lies within `1+epsilon` of the original `x_i`.
The selected original movers are more than four apart. Therefore:

- no other selected mover can be a first blocker;
- no stationary point can be a blocker for two selected movers;
- points in distinct endpoint star clusters stay more than one apart, since
  `4-2(1+epsilon)>1`;
- two selected movers remain more than one apart throughout their motions, since
  `4-2epsilon>1`.

### Proof: simultaneous compatibility and the whole cube

Parameterize the `i`th stopped segment by `t_i in [0,1]`. Change all movers using
arbitrary and independent values of the `t_i`. Every mover-to-stationary-point
distance is at least one by the first-contact construction. Every mover-to-mover
distance is greater than one by their separation. Stationary distances are unchanged.
Thus the whole Cartesian product is feasible for unit separation.

At a parameter value `t_i<1`, mover `i` has no unit contact. At `t_i=1`, its contacts
form a star with stationary original isolates. No two leaves are in unit contact:
their original distance was strictly greater than one and neither moved. Stars from
different movers have disjoint vertex sets and no edges between them. No star attaches
to the original contact graph. Hence no unit triangle appears anywhere in the cube.

Each mover stays in `conv(A)`, so its distance to every stationary source point is
at most `D`; the same is true between any two movers. More strongly, a mover belongs
to `(C_0)_{-w}`, so its radius-`w` disk is contained in `conv(A)`. For every other point
`a` in that convex hull, extend the ray from `a` through the mover by length `w`.
The extended point is still in the hull; since the hull has diameter `D`,

\[
|x_i(t_i)-a|\le D-w<D.
\tag{SA.4}
\]

Thus no new diameter pair involves a mover. Stationary pairs are unchanged. The
original diameter pair assumed in the statement remains present, so diameter is
exactly `D` everywhere.

The stopped segments have positive length and distinct moving labels. Their product
therefore is an injectively parameterized `N`-dimensional cube, not just `N`
one-at-a-time candidate motions.

### Proof: every added contact is universally zero-stressed

Each new star is a connected component of the full endpoint contact graph. Its
vertices lie in `int(C_0)`, hence in `int(conv(A))`: movers have depth at least `w`
and their leaves depth at least `w-1>0`. No such vertex is an endpoint of a diameter
pair, and no new diameter pair was introduced.

Take any normalized KKT equilibrium stress at the new source. Sum the equilibrium
equations over one star after taking the dot product at each vertex with its position.
There is no diameter load and no contact edge leaving that component. Internal
contributions pair to give

\[
\sum_{ij\text{ in the star}}\alpha_{ij}|p_i-p_j|^2=0.
\tag{SA.5}
\]

The lengths are one and all coefficients are nonnegative. Hence every coefficient
on that star is zero. This works for every star and every normalized stress, including
stresses different from the originally chosen one.

All remaining active constraints are the unchanged original contacts and diameter
pairs between unchanged points. Restricting a new stress to them gives an original
stress. Conversely every original stress extends by zero on all new contacts and is
still an equilibrium stress. These inverse restrictions/extensions prove exact equality
of the normalized KKT polytopes. The same argument applies on every face of the cube.
`square`

## 3. Canonical chamber consequence

Apply [Section 87](../targets/target-c/87-deep-near-unit-isolate-matching-audit.md),
`C-INACTIVE-DEEP-MATCHING`, at any fixed `w>1`. It supplies constants `c_w,K_w>0`
and at least `M>=c_w D` matched pairs in the actual macroscopic inactive chamber,
with `epsilon=K_w/D<1/4` for sufficiently large `D`.

The chamber is convex, lies inside the force hull, and contains no positive-core
vertex in its interior. Every original actual diameter endpoint belongs to the
positive core. All hypotheses of Theorem SA hold. Therefore the source belongs to
an exact cube of triangle-free global minimizers of dimension at least

\[
\boxed{\lceil c_w D/81\rceil,}
\tag{SA.6}
\]

obtained by moving each selected isolate at most `K_w/D`. Its far corner has linearly
many new contacts but precisely the same normalized KKT polytope and force hull.
All `n` original source labels remain present.

The statement is invoked here only where the promoted deep-matching theorem supplies
its chamber. The finite theorem can also be applied to any other chamber or cap for
which (SA.1) and the core-free interior condition have separately been verified; no
such verification is silently assumed for every Type-I exterior cap.

## 4. Exact effect on the closing attempt

The familiar qualitative attachment theorem is already canonical:
[Theorem 12.1](../theory/02-nonlinear-and-regressions.md) attaches a single isolate,
and Theorem 12.4 builds a different hybrid representative with a fixed backbone.
The new statement here is quantitative and simultaneous: linearly many deep
activations fit inside an inverse-diameter displacement cube, all blocker ties are
handled, and the full stress polytope is preserved at every corner and face.

It closes a compatibility subproblem, not C-II. In particular:

- creating more unit contacts does not contradict contact *minimality*;
- the new stars do not satisfy full contact visibility, so one cannot reapply the
  C-II identity `C=C_*` to the resulting higher-contact representative;
- C-I can release these weak contacts again, as is already explicitly visible by
  moving into the cube's interior;
- no individual KKT coefficient floor is obtained;
- no global population or exact packing gain is obtained.

By the escape-barrier result, any continuous source motion with diameter at most
`D`, including motions extending beyond this cube and changing the isolate contact
graph again, keeps the original post-ZF core congruent. This observation is stronger
than checking that the one particular activation procedure leaves the core fixed.

## 5. Regression and dependency audit

| Issue | Check |
| --- | --- |
| Simultaneous moves may conflict | Movers are more than four apart; all movers and first-blocker sets satisfy the explicit distance bounds above |
| A first blocker may differ from the chosen mate | Allowed; stopping at any first blocker still creates a star |
| Several blockers may tie | Allowed; stationary leaves are original isolates and cannot have unit edges between them |
| New constraints may acquire positive stress | The exact component virial (SA.5) rules this out for every stress |
| Isolated points could be dropped accidentally | The parameter cube retains every source label |
| Activation might reduce diameter immediately | An original core diameter pair remains fixed |
| A no-isolate representative might be substituted for the canonical one | Not done; the activated representative has new weak contacts |
| Near-lattice strict packings | Compatible with the theorem; no density-to-exact-triangle inference is made |

The finite theorem uses elementary disk area, convexity, first-contact stopping, and
the equilibrium equations from [Theorem 4.1](../theory/01-local-structure.md).
Its asymptotic application uses the canonical `C-INACTIVE-DEEP-MATCHING` and chamber
definition. The continuation barrier uses only canonical `C-ZRF` and full stress
support, as detailed in the separate report. No unpromoted Type-II cell theorem is
used as an input.

## 6. Remaining lemma and handoff

The attempted local chamber route now has an exact endpoint: inverse-diameter contact
creation is possible in bulk, but it is entirely force-invisible. It cannot provide
the necessary global diameter reduction by a feasible continuation of the original
core.

The highest-value unresolved obligation is an actual **global replacement inequality**:
under one of the two canonical C-II population alternatives, construct a labeled
unit-separated `n`-point configuration `X` with `diam(X)<D`, proving every cross-distance
with the retained isolated population. Its original core labels necessarily lie at
least `kappa(P)/2` from their old congruence orbit. Alternatively, a structural theorem
must prove that one of the two alternatives is incompatible with the post-ZF core
itself. Neither implication is established here.

**Promotion recommendation:** retain as an unreviewed report. The work does not change
the canonical C-II status, state version, or current prompt.
