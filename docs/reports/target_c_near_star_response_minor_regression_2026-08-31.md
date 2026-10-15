<!-- theorem-state: {"artifact_id":"ART-5FC2DD3257D6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: bounded-degree near-star response regression

**Date:** 2026-08-31
**Target:** Target C-II, weighted strict-minor transport
**Depends on:** circular-planar response theory and CR4 terminal-path packing
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

CR4 forces a linear number of strict circular minors from the C-II degree caps, but
the strictness cannot be converted into a quantitative minor mass using only graph
degree, circular planarity, and response positivity. The following exact family has
the CR4 number of strict connections while all disjoint size-two circular minors tend
to zero.

This is a regression against abstract weighted transport. It does not satisfy the
full Target C unit-contact embedding, KKT equilibrium, or global-minimality
hypotheses; those are precisely the ingredients a successful weighted theorem must
use.

## 1. Regression statement

For every integer `q>=4` and every `epsilon>0`, there is a connected positive
circular-planar electrical network with terminal set `T` of size `q` such that

```
degree(t) = 1 for t in T,
degree(v) = 3 for v outside T,
```

the network contains at least

```
floor((q-1)/8)
```

pairwise terminal-disjoint circular two-connections, but the sum of the absolute
values of all disjoint size-two circular response minors is less than `epsilon`.

Consequently no positive lower bound for that aggregate minor mass follows from
the CR4 hypotheses alone, even though every minor supplied by a two-connection is
strict.

## 2. Construction

Take a cycle with interior vertices

```
u_0,u_1,...,u_(q-1)
```

and attach one terminal leaf `t_i` to each `u_i`. Give every terminal edge
conductance `1` and every cycle edge conductance `M>0`. Embed the cycle in the disk
and place the terminal leaves on the outer boundary in cyclic order. This is a
positive circular-planar network. Every terminal has degree one and every interior
vertex has degree three.

Let `L_q` be the unweighted cycle Laplacian. Ordering terminals first and cycle
vertices second, the weighted Laplacian is

```
[ I       -I       ]
[ -I  I + M*L_q  ].
```

Schur reduction of the cycle vertices gives the terminal response

```
Lambda_M = I - (I + M*L_q)^(-1).
```

The cycle Laplacian has one-dimensional kernel spanned by the constant vector and
is positive definite on its orthogonal complement. Therefore

```
(I + M*L_q)^(-1) -> (1/q) J
```

entrywise as `M` tends to infinity, and hence

```
Lambda_M -> I - (1/q) J.
```

The limit is the response of a star with unit terminal conductances.

## 3. All disjoint circular minors vanish in the limit

A disjoint size-two circular minor uses two distinct row terminals and two distinct
column terminals, with the row and column sets disjoint. At the star limit, every
off-diagonal response entry equals `-1/q`. Thus every such minor is

```
(-1/q)*(-1/q) - (-1/q)*(-1/q) = 0.
```

There are finitely many disjoint size-two minors for fixed `q`, so entrywise
convergence implies that their total absolute value tends to zero as `M` tends to
infinity. Choose `M` sufficiently large that this total is less than `epsilon`.

On the other hand, CR4 applies to this graph because the terminal degree is at most
three and the nonterminal degree is at most five. It gives

```
nu_T >= (q-1)/4.
```

Pairing a maximum T-path packing gives at least

```
floor((q-1)/8)
```

terminal-disjoint circular two-connections. The circular-minor connection theorem
makes each corresponding response minor strictly positive for every finite `M`.
Thus the network has linearly many strict minors whose aggregate numerical mass can
still be made arbitrarily small.

Taking `q` through any sequence tending to infinity and choosing `M=M(q)` with
aggregate minor mass below `1/q` gives the asymptotic regression.

## 4. Exact scope and omitted hypotheses

The family deliberately omits:

1. a unit-distance realization of every network edge in the plane;
2. positive KKT equilibrium of the conductances against those edge directions;
3. the coordinate response identity `Lambda P_B=L_H P_B` for a diameter support;
4. the C34 relation `q=Omega(D)` between terminal count and source diameter; and
5. global minimum-diameter optimality and its Reuleaux/packing consequences.

It therefore is not a source configuration or a counterexample to Erdős Problem
#99. It only proves that CR4 plus circular-planar response theory cannot supply the
missing quantitative transport by itself.

Scaling all conductances by a common positive factor only scales the response
minors, so normalization of the electrical units does not remove this regression.

## 5. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| The cycle-with-leaves network has the stated degree caps | proved | Direct construction. |
| It has at least `floor((q-1)/8)` strict circular minors | proved with literature input | CR4 plus the circular-minor connection theorem. |
| All disjoint size-two minors can have aggregate mass below `epsilon` | proved | Schur formula and convergence to the star response. |
| The family is a unit-contact KKT framework | not claimed | Internal positions and equilibrium are omitted. |
| A quantitative C-II response gap is impossible | not proved | Unit geometry, equilibrium, C34, and global optimality remain available. |

## 6. Exact next lemma

> **Mechanical weighted transport.** Use unit edge lengths, positive KKT equilibrium,
> total contact stress `D^2`, and `q=Omega(D)` to prove a lower bound on an
> aggregate strict circular-minor quantity, or derive a bridge/cell contradiction
> when that quantity is small.

The regression shows why a proof that invokes only topological strictness or generic
circular-planar response continuity would be invalid.
