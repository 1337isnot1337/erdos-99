> Generated reading edition · [exact source](../../../docs/reports/target_c_quantitative_ferrers_stability_2026-09-01.md) · source SHA-256 `6c24145b0b09f8560a83889f82bc2411ddfaaca74f96be22c0ed9d98e688c124`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-781624F60E00","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C92: quantitative Ferrers stability

**Date:** 2026-09-01  
**Repository base:** `79980f1b` (main after C91 / PR #96)  
**Status:** LEVEL I STILL OPEN

C91 proves qualitatively that the C89 endpoint `T/D -> 2+Delta_2` is impossible.
C92 makes this quantitative. It proves the explicit asymptotic bound

`liminf T/D >= 2+Delta_2+10^(-4)`

for every canonical pure-rhombic C80 chain-face survivor.

The proof is a stability version of the C82 heavy-atom weighted-Mantel argument plus
the four-wall Ferrers capacity from C91. The key point is that if

`x=T/D = 2+Delta_2+delta < 3`,

then the full weighted-Mantel slack is exactly `delta/x^2`. That single scalar controls
three possible escapes from the C91 endpoint: extra trains parallel to the chain,
atomic mass outside the chain's 60-degree phase orbit, and residual-residual crossings
inside the chain orbit.

Write

`Delta=Delta_2=pi/(2sqrt(3))`,

`x0=2+Delta`,

and pass to a subsequence on which `x=T/D` and all train-direction measures converge.
C87 gives `q/D>=2+o(1)`, so with `y=q/T`, Target B Section 39.2 gives total atomic mass

`s <= 1-y/2 <= 1-1/x =: S`.

The exact D chain trains give a chain-direction atom of mass

`a >= 1/x =: a0`.

Let `e=a-a0>=0`. In the projective 60-degree phase relation, let `r` be the total
atomic mass on the two other points in the chain atom's three-point orbit, and let `t`
be all remaining atomic mass. Then

`r+t <= S-a`.

The required unordered atomic crossing weight is

`E=Delta/x^2`.

## 1. Exact heavy-Mantel slack decomposition

Put

`R0=S-a0=(x-2)/x`.

The maximum heavy-center edge weight allowed by the exposed-hull mass constraint is

`M0=a0 R0=(x-2)/x^2`.

Hence the global capacity slack above the required crossing mass is exactly

`kappa=M0-E=(x-x0)/x^2=delta/x^2`.

Let `C0` be the crossing weight inside the chain phase orbit and `Cout` the crossing
weight in all other phase orbits. Different phase orbits do not interact at leading
order because Section 39.1 supports the limiting crossing measure on projective
angle difference `+-pi/3`.

The chain orbit is a triangle-free graph on three weighted atoms, so

`C0 <= a r`.

All other orbits together are triangle-free on total weight `t`, hence

`Cout <= t^2/4`.

Therefore

`E <= a r+t^2/4 <= a(S-a-t)+t^2/4`.

Substitute `a=a0+e`. Since `a0-R0=(3-x)/x`, exact expansion gives

`M0-[a(S-a-t)+t^2/4]`

`= e(3-x)/x + e^2 + a t - t^2/4`.

All terms are nonnegative for `x<3`. Consequently

`e(3-x)/x + e^2 <= kappa`,

and, because `t<=R0` and `a>=a0`,

`a t-t^2/4 >= [(6-x)/(4x)] t`,

so

`e <= delta/[x(3-x)]`,

`t <= 4delta/[x(6-x)]`.

Also define the internal chain-orbit deficit

`D0:=a r-C0>=0`.

The same decomposition shows

`D0<=kappa`.

## 2. Bound crossings not using the exact chain trains P

Let `P` be the exact C80 family of D chain trains. We bound all leading crossings that
are not between `P` and the residual atoms in the chain phase orbit.

First, other phase orbits contribute at most

`Cout x^2 <= 4delta^2/(6-x)^2`

in units of `D^2`.

Second, extra chain-parallel trains have normalized mass `e`; even if every such train
crosses every chain-orbit residual train, their contribution is at most

`e r x^2 <= [(x-2)/(3-x)] delta`.

Third, the two residual atoms in the chain orbit may cross one another. If their
weights are `b,c`, put `z=bc` when that residual-residual edge is present and `z=0`
otherwise. Since the chain-orbit graph is triangle-free, presence of `bc` permits at
most one chain-residual edge. If, for example, the edges are `ab` and `bc`, then

`D0=a(b+c)-(ab+bc)=c(a-b) >= c(a-r)`.

Thus in every case

`z <= [r/(a-r)]D0`.

For `x<3`,

`a-r >= a0-R0=(3-x)/x`,

so

`z x^2 <= [(x-2)/(3-x)] delta`.

Let `N` be the total leading crossing count not between `P` and chain-orbit residual
trains, normalized by `D^2`. We have proved

`N <= 2[(x-2)/(3-x)]delta + 4delta^2/(6-x)^2`.

## 3. Stable four-wall Ferrers bound

The chain-orbit residual population contains at most

`rT <= (x-2)D`

trains. Split its two phase directions by the two C90 boundary sides, giving at most
four walls as in C91.

Let `E_P` be the P-to-chain-orbit-residual crossing count normalized by `D^2`, and let

`lambda = r x <= x-2`

be the residual train count normalized by D. Since the total required crossing count
is `Delta D^2+o(D^2)`,

`E_P >= Delta-N`.

The missing P incidences satisfy

`M:=lambda-E_P <= delta+N`.

A residual train crossing at most `D/2` chain trains misses at least `D/2`, so the
total crossing count of all such bad rows is at most `M D^2+o(D^2)`.

After deleting the bad rows, every remaining row crosses more than half of P. Within
one phase/side wall the train intervals are disjoint or nested; two intervals longer
than D/2 cannot be disjoint. Hence each good wall is Ferrers exactly as in C91.

Define

`F(lambda)=integral_0^lambda sqrt(1-t^2) dt`.

The C91 parallelogram argument gives a wall of size `lambda_i D` at most
`F(lambda_i)D^2+o(D^2)` crossings. Since F is concave and the four good wall masses
sum to at most `lambda<=x-2`,

`E_P <= 4F((x-2)/4)+M`.

Combining with `E_P>=Delta-N` and `M<=delta+N` yields the stable master inequality

`Delta <= 4F((Delta+delta)/4)+delta+2N`.

## 4. Explicit 10^-4 gap

Assume for contradiction

`0<=delta<=10^(-4)`.

Then `x<2.91`, so

`(x-2)/(3-x)<11`,

and `6-x>3`. Therefore

`N <= 22delta + 4delta^2/9`.

Also `F'<=1`, so

`4F((Delta+delta)/4) <= 4F(Delta/4)+delta`.

The endpoint Ferrers gap has a simple analytic lower bound. Since

`sqrt(1-t^2) <= 1-t^2/2`,

we get

`Delta-4F(Delta/4) >= Delta^3/96`.

Since `Delta>0.9`,

`Delta^3/96 > 0.00759375`.

But the stable master inequality would require this endpoint gap to be at most

`2delta+44delta+8delta^2/9`

`<=0.00460001`

for `delta<=10^(-4)`, a contradiction.

### Theorem C92 — explicit chain-face train surplus

Every asymptotic canonical pure-rhombic C80 chain-face survivor satisfies

`liminf T/D >= 2+Delta_2+10^(-4)`.

Equivalently,

`liminf T/D >= 2.9069996821...`.

This replaces C91's non-explicit compactness gap by a certified absolute constant.
The constant is deliberately conservative; optimizing the same inequalities would
improve it, but no optimization is needed downstream.

## 5. Frontier effect

C92 removes quantitative instability as an escape from C91. Any remaining canonical
pure chain-face counterexample pays at least `10^(-4)D` additional train tracks above
the C89 extremal shell constant.

The next target is to convert that explicit linear surplus, together with C88's
quadratic secondary-train separator budget and C90's macroscopic train-cut
caterpillar, into the pure-disk shell contradiction `G+E>=c0B` or a direct Oler loss.
