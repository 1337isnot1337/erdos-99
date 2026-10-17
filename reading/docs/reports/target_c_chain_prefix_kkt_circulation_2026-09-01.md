> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_prefix_kkt_circulation_2026-09-01.md) · source SHA-256 `d2cd1790bd46646b9df2e2bfbca7e7538d452a45f516fed1ffb2592d2fe669c1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BB887429B149","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C84: KKT circulation on the chain prefix graph

**Date:** 2026-09-01  
**Repository base:** `c11eaca8` (main after C83 / PR #88)  
**Run type:** exact KKT / ordered-graph reduction  
**Target:** Target C C-II, C80--C83 exact chain-face branch  
**Depends on:** C18 shared-endpoint diameter-angle gap; C65 full diameter visibility; C80 chain atom; C83 interval normal form; Target B Section 40 KKT train-gradient identity  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C83 turns every active non-chain diameter bar into one interval edge on the ordered
prefix vertices `0,1,...,D`. C84 adds the KKT relation that those interval edges must
satisfy.

Choose a relative-interior normalized KKT stress in the C65 fully force-visible
normalization. Thus every actual active diameter bar has strictly positive weight
`beta_h>0`. On the C80 chain atom, C83 writes every non-chain bar with nonempty
interval as

```math
g_h|_P=\eta_h\mathbf 1_{(a_h,b_h]},
\qquad
0\le a_h<b_h\le D,
\qquad
\eta_h\ne0.
```

Train-angle first variations preserve all unit contacts, so the KKT virtual-work
identity is

```math
\sum_{h\in H}\beta_h g_h=0.
```

The chain bar has zero gradient. Restricting to `P` therefore gives

```math
\boxed{
\sum_{h\ne h_0}\beta_h\eta_h\mathbf 1_{(a_h,b_h]}=0.
}
\tag{C84.1}
```

Under prefix summation, an interval row is the ordinary incidence row of the edge
`a_h b_h`. Thus (C84.1) is exactly a **nowhere-zero circulation** on the multigraph of
non-chain diameter intervals, with signed edge flow

```math
\boxed{w_h:=\beta_h\eta_h\ne0.}
\tag{C84.2}
```

Consequences are immediate but useful:

1. the interval multigraph has no bridges;
2. every cut met by one interval is met by at least two interval bars, with both signs
   of `eta` represented in the signed cut sum;
3. if the simple prefix graph is connected, complete first-order locking requires at
   least `D+1` non-chain diameter bars, not merely `D`;
4. more generally, if the simple prefix graph has `c` components and `n_+` nonisolated
   prefix vertices, the non-chain bars with nonempty interval are at least `n_+`;
5. every backward interval is disjoint from the chain endpoints `z,a`: any diameter
   bar sharing `z` or `a` with the chain is forward by C18.

The first-order chain blocker is therefore not an arbitrary connected interval graph.
It is the support of a nowhere-zero signed circulation, and all positive quadratic
blockers lie on its interior-crossing, non-endpoint part.

---

## 1. C83 interval notation

Work in the exact C80 chain-face geometry

```math
h_0=za,
\qquad
z=x_0,x_1,\ldots,x_D=a,
```

with ordered chain tracks

```math
P=\{\tau_1,\ldots,\tau_D\}.
```

C83 gives, for every ordered active diameter bar `h=xy`, a signed interval

```math
I_h=(a_h,b_h]\subseteq\{1,\ldots,D\}
```

and scalars

```math
c_h=\sigma_h r_h\cdot u,
\qquad
\eta_h=\sigma_h r_h\cdot Ju,
\qquad
u:=\frac{a-z}{D},
```

such that

```math
\boxed{
g_h|_P=\eta_h\mathbf1_{I_h}.}
\tag{C84.3}
```

The chain bar satisfies

```math
I_{h_0}=P,
\qquad
c_{h_0}=D,
\qquad
\eta_{h_0}=0.
\tag{C84.4}
```

C83 also proves that if `h\ne h_0` and `I_h` is nonempty, then

```math
\boxed{\eta_h\ne0.}
\tag{C84.5}
```

Indeed `eta_h=0` would make the diameter segment parallel to the chain, and a
source of diameter `D` contains at most one diameter segment in one prescribed
unoriented direction.

Bars with empty interval have zero restriction to `P` and will be omitted below.

---

## 2. Use a relative-interior KKT stress

C65 supplies a canonical C-II representative for which every actual diameter pair is
force-visible. Choose a relative-interior normalized KKT stress

```math
s=(\alpha,\beta).
```

Then

```math
\boxed{\beta_h>0\qquad(h\in H).}
\tag{C84.6}
```

Every train-angle first variation preserves every unit rhombus edge exactly to first
order. Target B Section 40 therefore gives the diameter-gradient equilibrium

```math
\boxed{\sum_{h\in H}\beta_hg_h=0.}
\tag{C84.7}
```

Restrict C84.7 to the chain coordinates. The chain bar contributes zero by C84.4,
and empty-interval bars contribute zero. Hence

```math
\boxed{
\sum_{h\in H_P}
\beta_h\eta_h\mathbf1_{(a_h,b_h]}=0,
}
\tag{C84.8}
```

where

```math
H_P:=\{h\in H\setminus\{h_0\}:a_h<b_h\}.
```

Put

```math
w_h:=\beta_h\eta_h.
\tag{C84.9}
```

By C84.5-C84.6,

```math
\boxed{w_h\ne0\qquad(h\in H_P).}
\tag{C84.10}
```

This nonvanishing is the point of using the relative-interior KKT stress rather than
the exposed chain-face stress itself.

---

## 3. Discrete derivative converts intervals to edge incidence

Let `e_0,...,e_D` be the standard basis on prefix vertices. Define the linear
operator

```math
\partial:\mathbb R^D\to\mathbf1^\perp\subset\mathbb R^{D+1}
```

by its action on interval indicators:

```math
\boxed{
\partial\mathbf1_{(a,b]}=e_b-e_a.
}
\tag{C84.11}
```

Concretely, if `q=(q_1,...,q_D)` and `q_0=q_{D+1}=0`, `partial q` is the signed
successive-difference vector with the indexing chosen so that C84.11 holds. The map
is an isomorphism from `R^D` onto `1^perp`; interval indicators generate `R^D`, so
C84.11 determines it uniquely.

Apply `partial` to C84.8:

```math
\boxed{
\sum_{h\in H_P}w_h(e_{b_h}-e_{a_h})=0.
}
\tag{C84.12}
```

Now form the directed multigraph

```math
\mathcal G_P
```

on prefix vertices `0,...,D` with one oriented edge

```math
a_h\longrightarrow b_h
```

for every `h in H_P`. Equation C84.12 is exactly the node-balance equation for the
signed flow `w_h`.

### Theorem C84.1 — nowhere-zero prefix circulation

The active non-chain diameter intervals support a circulation

```math
\boxed{w_h=\beta_h\eta_h}
```

which is nonzero on every edge of `mathcal G_P`.

No positivity of `w_h` is claimed; its sign is the sign of the transverse diameter
component `eta_h` in the C83 interval orientation.

---

## 4. No interval bar is a bridge

A standard circulation fact now becomes a geometric restriction.

Suppose an edge `e` of the underlying undirected multigraph of `mathcal G_P` were a
bridge. Delete it and let `S` be the vertex set of one resulting component. Sum the
node-balance equation C84.12 over vertices of `S`. Every internal edge cancels. The
only surviving term is the flow on `e`, with sign according to its orientation. Thus

```math
w_e=0,
```

contradicting C84.10.

### Corollary C84.2 — bridgeless interval multigraph

```math
\boxed{
\mathcal G_P\text{ has no bridges.}
}
\tag{C84.13}
```

Equivalently every non-chain diameter interval belongs to a cycle of the prefix
**multigraph**. Parallel intervals count as distinct edges and form a two-edge cycle.

This distinction matters. After collapsing parallel intervals, the simple prefix
graph may have a bridge, but then that simple edge must be represented by at least two
actual diameter bars whose signed flows cancel across the corresponding cut.

---

## 5. Every used cut carries opposite transverse signs

Equation C84.8 can be read coordinate by coordinate. For chain track `tau_j`,

```math
\boxed{
\sum_{h:\ a_h<j\le b_h}\beta_h\eta_h=0.
}
\tag{C84.14}
```

Every summand is nonzero. Therefore:

### Corollary C84.3 — two-sided cut balance

For every `j`:

- either no active non-chain diameter interval contains `tau_j`; or
- at least two such bars contain `tau_j`, and among them occur both signs of `eta_h`.

In particular, if the simple prefix graph connects some vertex in
`{0,...,j-1}` to some vertex in `{j,...,D}`, then the cut is crossed by at least two
actual active diameter bars with opposite signed transverse KKT flows.

If the simple prefix graph is connected, this holds for **every** chain track
`tau_1,...,tau_D`.

This is strictly stronger than the C83 statement that one interval row may cover a
track.

---

## 6. Exact rank formula and the extra edge forced by circulation

Let `G_P` be the simple graph obtained from `mathcal G_P` by forgetting orientations,
weights, and parallel multiplicity. Let

```math
c(G_P)
```

be its number of connected components, including isolated prefix vertices.

C83 identifies every restricted nonzero gradient row, up to a nonzero scalar, with
one interval indicator. Under `partial`, those rows become the ordinary edge-incidence
rows of `G_P`. Hence the standard graph-incidence rank formula gives

### Theorem C84.4 — exact chain-gradient rank

```math
\boxed{
\operatorname{rank}\{g_h|_P:h\in H\}
=D+1-c(G_P).
}
\tag{C84.15}
```

Equivalently the chain-supported first-order-neutral space has dimension

```math
\boxed{
c(G_P)-1.}
\tag{C84.16}
```

The extra KKT circulation now strengthens the edge count. Let `V_+` be the set of
nonisolated vertices of `G_P`, and let

```math
n_+:=|V_+|.
```

Every nontrivial connected component of the multigraph is bridgeless, hence contains
at least as many multiedges as vertices. Summing over nontrivial components gives

```math
\boxed{|H_P|\ge n_+.}
\tag{C84.17}
```

In particular, if the restricted gradient rank is full, then `G_P` is connected on
all `D+1` prefix vertices, so

```math
\boxed{|H_P|\ge D+1.}
\tag{C84.18}
```

Adding the chain bar itself:

### Corollary C84.5 — full chain locking needs at least `D+2` diameter bars

If the active diameter gradients have rank `D` on the `D` chain coordinates, then

```math
\boxed{|H|\ge D+2.}
\tag{C84.19}
```

This improves the raw spanning-tree requirement `|H|>=D+1` by one edge. It is not by
itself a contradiction because the planar diameter graph can have `Theta(D)` edges.

---

## 7. Backward intervals cannot touch the chain endpoints

C83 classifies an interval as backward exactly when

```math
c_h=\sigma_h r_h\cdot u<0.
```

The chain bar is `za` with direction `u=(a-z)/D`.

Suppose another active diameter bar is `zb`, and its chain interval is nonempty.
Orient it from level `0=t(z)` toward `t(b)>0`. Then the C83 interval sign is positive
and

```math
c_{zb}=(b-z)\cdot u.
```

Both `za` and `zb` are diameter edges sharing `z`. C18 gives, for `D>=20`,

```math
\angle azb<\Theta_D<\frac\pi3.
```

Therefore

```math
\boxed{c_{zb}>D\cos(\pi/3)=D/2>0.}
\tag{C84.20}
```

So every nonempty interval bar incident to `z` is strongly forward.

The same argument at `a` uses the vectors from `a` to `z` and from `a` to its other
diameter partner. With the C83 interval orientation toward level `D=t(a)`, it gives
again

```math
\boxed{c_{ab}>D/2>0.}
\tag{C84.21}
```

for every nonempty interval bar incident to `a`.

### Corollary C84.6 — positive quadratic blockers are interior diameter chords

Every backward interval bar is disjoint from both chain endpoints `z,a`. Hence, as a
planar diameter edge disjoint from the chain diameter `za`, its straight segment
crosses `za` in the interior.

Thus all C83 positive quadratic blockers come from diameter chords that cross the
literal straight unit chain rather than from the diameter stars at its endpoints.

This separates the two geometries:

- endpoint-star intervals are forward and can only help the chain shorten at quadratic
  order;
- backward intervals are interior crossing chords and are the only positive quadratic
  blockers.

---

## 8. What C84 removes

C83 left the first-order interval graph arbitrary. C84 shows that an actual KKT
survivor cannot realize an arbitrary interval graph:

```text
one active non-chain diameter bar h
    -> prefix edge a_h b_h
    -> nonzero signed flow w_h=beta_h eta_h

all bars together
    -> divergence-free flow on prefix graph
    -> no bridge edges in the multigraph
    -> every used chain cut has opposite transverse signs
    -> full locking requires >=D+1 non-chain bars
```

At second order, C83 says only backward intervals can oppose the negative C80 chain
curvature. C84.6 further says every such interval comes from a diameter chord crossing
the chain in its interior.

The remaining obstruction is therefore a **bridgeless signed interval circulation
whose backward-labelled edges are all interior-crossing diameter chords**.

---

## 9. Next target

The next useful theorem should exploit one of the two pieces C84 has put together.

1. **Crossing-chord circulation theorem.** Use the straight-line diameter-thrackle
   property of the interior backward chords to show that a bridgeless prefix
   circulation cannot have enough backward intervals to block the C80 negative
   chain-bending space.
2. **Cycle-sign theorem.** Every prefix edge lies on a circulation cycle. Relate the
   ordered cycle to the actual diameter graph and the C19 `Omega(sqrt(D))` diameter
   cycle-girth bound, or show that a short prefix cycle forces a forbidden geometric
   diameter configuration.
3. **Cut-energy theorem.** C84.14 supplies opposite transverse flows across every used
   chain cut. Combine that balance with the C83 radial signs `c_h` and
   `c_h^2+eta_h^2=D^2` to force quantitative backward mass or a response defect.
4. **Secondary-cusp reduction.** On a disconnected prefix graph use C84.15-C84.16 to
   choose a chain-supported neutral mode. Then C83/Target B reduces all positive
   quadratic blocking to backward intervals; C84.6 localizes those to interior
   crossing diameter chords.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C84. In the C65 full-diameter-visible normalization choose a relative-interior KKT
stress, so beta_h>0 for every active diameter bar. C83 gives on the C80 chain atom
  g_h|P = eta_h 1_(a_h,b_h],
with eta_h!=0 for every non-chain nonempty interval.

KKT train virtual work gives
  sum_h beta_h g_h = 0.
Hence
  sum_h w_h 1_(a_h,b_h] = 0,
  w_h=beta_h eta_h !=0.
Taking the discrete derivative turns this into
  sum_h w_h(e_b-e_a)=0.
So the non-chain interval multigraph on prefix levels 0,...,D carries a nowhere-zero
circulation.

Consequences:
  * no multigraph edge is a bridge;
  * every used cut is crossed by at least two bars with opposite eta signs;
  * rank{g_h|P}=D+1-c(G_P);
  * full rank D requires at least D+1 non-chain bars, hence |H|>=D+2.

C18 also implies every interval bar incident to z or a is strongly forward:
  c_h>D/2.
Therefore every backward interval (the only positive quadratic blocker by C83) is a
diameter chord disjoint from z,a and crossing the straight chain za in its interior.

Next: exploit the bridgeless signed circulation plus interior diameter-chord crossing
to prove the backward intervals have deficient blocker rank.
```
