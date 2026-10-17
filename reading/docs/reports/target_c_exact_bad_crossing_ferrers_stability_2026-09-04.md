> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_bad_crossing_ferrers_stability_2026-09-04.md) · source SHA-256 `62cd2d28a6c1b1aca278a709ee87aaf94c2aba99a00c5847f64de0dda83e0f38`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A01B1D10DC8C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C exact bad-crossing Ferrers stability

**Date:** 2026-09-04  
**Repository base:** `89c17412` plus research commits `60a33275`, `e7a01467`  
**Run type:** exact extremal refinement of C92  
**Target:** pure-rhombic C80-C96 chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Result

Write

`Delta = pi/(2sqrt(3))`,

`x0 = 2+Delta`.

C92 proves

`liminf T/D >= x0+10^(-4)`

by bounding the leading train crossings that do not use the exact `D` C80 chain
trains. Its bound is deliberately crude near `x=3`.

This report solves that intermediate extremal problem exactly. For

`x0 <= x <= 3`,

define

`u(x) = ((x-1)-sqrt((x-1)^2-4Delta))/2`.

Then the leading crossing mass not using the exact chain family `P` is at most

`(Delta-u(x))D^2+o(D^2)`.

Consequently the exact `P`-to-residual crossing mass is at least

`u(x)D^2-o(D^2)`.

Combining this with the C91 four-wall Ferrers capacity gives the necessary inequality

`2u(x) <= (x-2) + 4F((x-2)/4)`,

where

`F(lambda)=integral_0^lambda sqrt(1-t^2) dt`.

That inequality fails uniformly for

`x <= x0+3*10^(-4)`.

Hence:

### Theorem X1 — improved explicit chain-face train surplus

Every asymptotic canonical pure-rhombic C80-C96 chain-face survivor satisfies

`liminf T/D >= 2+Delta+3*10^(-4)`

that is,

`liminf T/D >= 2.9071996821...`.

This improves C92's certified `10^(-4)` surplus by a factor of three. It still does
not close the chain-face branch.

## 2. C92 limiting notation

Pass to a subsequence with

`T/D -> x`, `x0<=x<=3`.

C87 gives `q/D>=2+o(1)`. C82/C92 therefore give, for the limiting train-direction
measure, total atomic mass at most

`S=1-1/x`.

The exact C80 chain family `P` consists of `D` trains in one projective direction, so
its normalized mass is

`a0=1/x`.

Thus all remaining atomic train mass is at most

`M=S-a0=(x-2)/x`.

The total leading unordered train-crossing mass is

`E=Delta/x^2`,

because `R/D^2->Delta` and `T/D->x`.

As in C92, the limiting crossing measure is supported on projective angle difference
`+-pi/3`. Hence the atomic phase graph decomposes into three-point phase orbits, and
the supported graph in every orbit is triangle-free.

Call a leading crossing **good** if it joins one of the exact `P` trains to one of
the two residual phase atoms in the chain phase orbit. Every other leading crossing is
**bad**.

## 3. A two-variable domination of every chain-orbit support

Let the full atom in the chain direction have mass

`a=a0+e`,

where `e>=0` is extra atomic mass parallel to `P`. Let the other two atoms in that
three-point phase orbit have masses `b,c`. Let `t` be the total atomic mass in all
other phase orbits. Then

`e+b+c+t <= M`.

Because the three-point chain orbit is triangle-free, its supported edge set is a
subgraph of a path or a two-edge star. In every case there exist numbers `p,y>=0`
with

`p+y <= e+b+c`

such that

`C_chain <= p(a0+y)`

and

`B_chain <= p y`,

where `C_chain` is its total leading crossing mass and `B_chain` is its bad crossing
mass.

Indeed:

- for the star with edges from the chain phase to both residual phases, take
  `p=b+c`, `y=e`;
- for a path with edges chain--`b` and `b`--`c`, take `p=b`, `y=e+c`;
- the symmetric path is identical;
- one-edge and residual-only supports are obtained by deleting terms and are dominated
  by the same form.

All other phase orbits together have total mass `t`, so weighted Mantel gives both

`C_out <= t^2/4`

and

`B_out=C_out <= t^2/4`.

Therefore every survivor admits `p,y,t>=0` with

`p+y+t <= M`,

`E <= p(a0+y)+t^2/4`,

and bad leading mass

`B_bad <= p y+t^2/4`.

The next lemma optimizes this relaxation exactly.

## 4. Exact bad-mass extremal lemma

### Lemma X2

Let `x0<=x<=3`, and put

`a0=1/x`, `M=(x-2)/x`, `E=Delta/x^2`.

Suppose `p,y,t>=0` satisfy

`p+y+t<=M`

and

`p(a0+y)+t^2/4 >= E`.

Let `p0` be the unique solution in `(M/2,M]` of

`p0(a0+M-p0)=E`.

Then

`p y+t^2/4 <= p0(M-p0)`.

### Proof

For fixed `p,t`, increasing `y` only increases both displayed left sides, so for an
upper bound on the bad mass set

`y=M-t-p`.

Write `m=M-t`. The total-capacity upper bound becomes

`f_t(p)=p(a0+m-p)+t^2/4`.

Since `x<=3`,

`a0>=M>=m`,

so `f_t` is nondecreasing on `[0,m]`.

At `t=0`,

`x^2 f_0(M/2)=x(x-2)/4 <=3/4<Delta=x^2E`,

while

`x^2 f_0(M)=x-2>=Delta`.

Hence the stated `p0` exists uniquely and satisfies `p0>M/2`.

For `t>0`,

`f_t(p0)=E-p0 t+t^2/4`.

Because `t<=M<2p0`, one has `t/4<p0`, and therefore

`f_t(p0)<E`.

Since `f_t` is nondecreasing, every feasible `p` obeys `p>p0` when `t>0`, and
`p>=p0` when `t=0`.

Now

`h_t(p)=p(m-p)+t^2/4`

is the bad-mass upper bound. Since `p0>M/2>=m/2`, `h_t` is decreasing throughout the
feasible range `p>=p0`. Thus

`h_t(p)<=h_t(p0)`

`=p0(M-p0)-p0t+t^2/4`

`<=p0(M-p0)`,

with strict inequality for `t>0`. This proves the lemma.

## 5. Closed form

Put

`u=x p0`.

The defining equation for `p0` becomes

`u(x-1-u)=Delta`.

The other quadratic root exceeds `x-2`, whereas `xp0<=x-2`; hence

`u=u(x)=((x-1)-sqrt((x-1)^2-4Delta))/2`.

Moreover

`x^2 p0(M-p0)=u(x-2-u)`.

Using `u(x-1-u)=Delta`,

`u(x-2-u)=Delta-u`.

Therefore:

### Corollary X3 — exact bad-crossing bound

The bad leading crossing mass is at most

`(Delta-u(x))D^2+o(D^2)`.

Since the total leading crossing count is `Delta D^2+o(D^2)`, the good exact-chain
crossing count is at least

`u(x)D^2-o(D^2)`.

At the C89 endpoint `x=x0`, one has `u(x0)=Delta`, so the bad mass is exactly zero,
recovering the equality structure used by C91. At `x=3`, the formula remains finite;
there is no `1/(3-x)` blowup.

## 6. Feed the exact mass into the four-wall Ferrers argument

Let `lambda D+o(D)` be the number of residual atomic trains in the chain phase orbit.
Since all atomic mass outside the exact `P` family is at most `M`,

`lambda <= x-2`.

The good crossing lower bound says the number of missing `P` incidences is at most

`[(x-2)-u(x)]D^2+o(D^2)`.

Call this coefficient `M_x=x-2-u(x)`.

As in C91-C92, split the two residual phase directions by which of the two `z`--`a`
boundary arcs contains their train terminals. There are at most four walls. A residual
train crossing at most `D/2` exact chain trains misses at least `D/2`; therefore all
such bad rows together contribute at most

`M_x D^2+o(D^2)`

good crossings.

Every remaining row crosses more than half of `P`. Within one phase/side wall the
crossing intervals are disjoint or nested, so the remaining rows in each wall form a
Ferrers diagram. C91's parallelogram capacity and concavity of

`F(lambda)=integral_0^lambda sqrt(1-t^2)dt`

give total good-wall capacity at most

`4F((x-2)/4)D^2+o(D^2)`.

Since the actual good crossing count is at least `u(x)D^2-o(D^2)`, every survivor in
`x0<=x<=3` must satisfy

`u(x) <= 4F((x-2)/4)+(x-2-u(x))`.

Equivalently:

### Necessary inequality X4

`G(x):=2u(x)-(x-2)-4F((x-2)/4) <=0`.

## 7. Certified `3*10^-4` gap

At `x=x0`, `u(x0)=Delta`, so

`G(x0)=Delta-4F(Delta/4)`.

C91's elementary estimate `sqrt(1-t^2)<=1-t^2/2` gives

`G(x0)>=Delta^3/96`.

Since `Delta>0.9`,

`G(x0)>0.00759375`.

Differentiate `u(x-1-u)=Delta`:

`u'(x)=-u/sqrt((x-1)^2-4Delta)`.

For `x>=x0`, the square root is at least `1-Delta`, while `u<=Delta<1`. Using the
safe elementary bound `Delta<0.91`,

`|u'| < 1/(1-Delta) < 100/9`.

Also `0<F'<=1`. Hence throughout `[x0,3]`,

`G'(x) >= -2(100/9)-2 = -218/9`.

If `0<=x-x0<=3*10^(-4)`, then

`G(x) > 0.00759375 - (218/9)(3*10^(-4))`

`>0.00032>0`.

This contradicts the necessary inequality X4. Therefore no asymptotic survivor can
have

`x<=x0+3*10^(-4)`.

This proves Theorem X1.

## 8. Scope and next obligation

The extremal lemma is exact for the C92 limiting phase model; it does not assume a
new PSD comparison or a finite-rate atomic convergence statement. The final numerical
constant is intentionally conservative. Solving `G(x)=0` numerically suggests that
the same exact inequality excludes approximately up to

`x=2.90727855...`,

but the promoted claim here is only the analytically certified `3*10^(-4)` gap.

The remaining interval between this bound and `x=3` is still large. Closing it needs a
new capacity input beyond total bad crossing mass, most likely the C93/C96 simultaneous
staircase-caterpillar order or the C94-C95 exact-flat activation mechanism.
