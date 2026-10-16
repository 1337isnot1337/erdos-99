<!-- theorem-state: {"artifact_id":"ART-1BC740C47469","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C secondary-cap load/span transfer

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact cap/span-sensitive two-cut theorem  
**Target:** C90 + LS2 secondary-cut frontier  
**Status:** LEVEL I STILL OPEN

## 1. Purpose

The double-cover audit shows that the word `caterpillar` is graph-theoretically
redundant on the selected paired staircase.  What is not redundant is that a non-chain
train is one **same-side boundary cap** and crosses one consecutive interval of the
exact chain family.

This report converts those geometric facts into an exact load/span inequality.
Restrict to the `r` shortest staircase intervals.  If a secondary train crosses `j`
exact chain tracks, it can separate at most

`r+j`

of the `2r` selected physical diameter orientations.  Combined with LS2, a heavily
loaded secondary train must therefore penetrate a quantitatively long interval of the
chain.  Summing the same inequality also gives a new exact lower bound on the total
number of `P`-to-secondary train crossings.

## 2. Setup

Let `G_P` be the C88 staircase tree on prefix levels `0,...,D`.  By LS1, for every
`1<=ell<=D` there is exactly one simple staircase edge of chain length `ell`.

For `1<=r<=D`, let

`E_r={e in E(G_P): ell(e)<=r}`.

Then

`|E_r|=r`.

For every `e={a,b} in E_r`, choose the two C87 physical diameter orientations, one
with its `L` endpoint at prefix level `a` and one with its `L` endpoint at prefix level
`b` (equivalently the two opposite `L/U` orientations).  Let `S_r` be this `2r`-edge
selected diameter set.

Fix a non-chain train `sigma`.  By C90 both terminals of `sigma` lie on one boundary
arc, say `L`; the `U` case is identical.  Let

`C_sigma`

be the boundary cap cut off by `sigma` and the subarc of `L` between its two terminals.
Let

`j_sigma=# {tau in P : tau crosses sigma}`.

By the C91 boundary-order observation, these are exactly the chain trains whose `L`
terminals lie between the two terminals of `sigma`.  Hence the source prefix level
along `C_sigma` ranges through at most

`j_sigma+1`

consecutive values.

Let

`m_sigma(r)=# {h in S_r : sigma separates the endpoints of h}`.

## 3. One staircase edge contributes at most one unless both prefix endpoints lie in the cap

Fix `e={a,b} in E_r`.  Its two selected physical orientations have exactly one
selected `L` endpoint at level `a` and exactly one selected `L` endpoint at level `b`.
Their opposite endpoints lie on `U`, outside the `L` boundary cap.

Therefore `sigma` separates a selected orientation if and only if that orientation's
selected `L` endpoint lies in `C_sigma`.

Thus the contribution of `e` to `m_sigma(r)` is `0`, `1`, or `2`.  Let

`B_sigma(r)`

be the set of staircase edges in `E_r` which contribute `2`.

Since there are only `r` underlying staircase edges,

`m_sigma(r) <= r + |B_sigma(r)|`.

No uniqueness of physical vertices inside one prefix fiber is used here.

## 4. Double-hit edges form an induced subforest on at most j+1 prefix levels

If `e={a,b}` lies in `B_sigma(r)`, the cap contains a selected physical `L` endpoint at
both prefix levels `a` and `b`.

Along the boundary arc `L`, the C83 prefix level changes only when a terminal of one of
the exact chain trains `P` is crossed.  The terminals of `sigma` enclose exactly
`j_sigma` such `P` terminals.  Hence every prefix level represented in the cap belongs
to one consecutive level interval

`K_sigma`

with

`|K_sigma|<=j_sigma+1`.

In particular both endpoints of every edge in `B_sigma(r)` lie in `K_sigma`.

But `G_P` is a tree.  The subgraph induced by any `k` of its vertices has at most
`k-1` edges.  Therefore

`|B_sigma(r)| <= |E(G_P[K_sigma])| <= |K_sigma|-1 <= j_sigma`.

Combining with the preceding section proves the main finite inequality.

### Theorem CSL1 — cap load/span bound

For every non-chain train `sigma` and every `1<=r<=D`,

`m_sigma(r) <= r+j_sigma`.

Equivalently,

`j_sigma >= m_sigma(r)-r`.

The theorem is insensitive to prefix-fiber splitting: physical multiplicity can alter
which selected incidence in a boundary-level fiber lies inside the cap, but an edge
can be double-hit only when both of its **distinct prefix levels** occur inside the
same cap, and the tree bound then applies.

## 5. Combine with LS2: a loaded secondary cut must penetrate the chain

LS2 gives at least

`I_r >= r(2D+1-r)`

incidences between `S_r` and the `T-D` non-chain trains.  Hence some non-chain train
`sigma` satisfies

`m_sigma(r) >= ceil(r(2D+1-r)/(T-D))`.

CSL1 yields immediately:

### Corollary CSL2 — one-train penetration bound

For every `1<=r<=D`, some non-chain train satisfies

`j_sigma >= ceil(r(2D+1-r)/(T-D))-r`.

For a sequence with

`T/D -> x<3`, `r/D -> alpha`,

and `0<alpha<3-x`, this becomes

`j_sigma/D >= alpha(3-x-alpha)/(x-1)-o(1)`.

Optimizing at

`alpha=(3-x)/2`

gives

`j_sigma/D >= (3-x)^2/[4(x-1)]-o(1)`.

Thus every fixed low-train gap below `3D` forces a secondary train which is
simultaneously

- loaded by the LS2 short-span selected diameters, and
- separated from the opposite side by a **linear** number of exact chain tracks.

The coefficient becomes small as `x` approaches `3`; the point is structural rather
than a present numerical contradiction.

## 6. Sum over all secondary trains

Let

`R_P=# { (tau,sigma): tau in P, sigma notin P, tau crosses sigma }`.

Equivalently,

`R_P=sum_(sigma notin P) j_sigma`.

Summing CSL1 over all `T-D` non-chain trains gives

`I_r=sum_sigma m_sigma(r)`

`<= r(T-D)+R_P`.

Using LS2 therefore gives the exact finite lower bound

### Theorem CSL3 — separator budget forces chain-crossing rhombi

For every `1<=r<=D`,

`R_P >= r(3D+1-T-r)`.

When the right side is positive, optimize over integer `r`.  Put

`A=3D+1-T`.

If `0<=A<=2D`, then

`max_r r(A-r)=floor(A^2/4)`.

Hence

`R_P >= floor((3D+1-T)^2/4)`.

This is an exact bridge from the C93/LS2 **diameter-separator** demand to actual
rhombus crossings between the chain family and secondary trains.

## 7. What remains

CSL1 removes the purely graph-theoretic caterpillar dead end and identifies the right
quantity to combine with wall geometry.  A closing continuation needs an upper bound
which couples

- the load `m_sigma(r)`,
- the cap chain span `j_sigma`, and
- physical diameter endpoint geometry inside the same cap,

more strongly than the tree inequality `m<=r+j`.

The obvious next inputs are:

1. C18's shared-endpoint angular width when load concentrates in a few prefix fibers;
2. the FSB split budget when load is distributed among many physical vertices of one
   fiber;
3. one-side Ferrers circular capacity when `j_sigma` is itself macroscopic;
4. C94's exact active-face flat for the residual case near `T/D=3`.

No Level I closure is claimed.