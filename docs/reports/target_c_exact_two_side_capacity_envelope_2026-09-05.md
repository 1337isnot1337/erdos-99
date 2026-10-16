<!-- theorem-state: {"artifact_id":"ART-954236E9E00E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C exact two-side capacity envelope

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact optimization of the audited TS4 phase capacity  
**Target:** C80–C96 low-train chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Input

Retain the audited two-independent-side theorem from
`target_c_two_independent_side_capacity_2026-09-04.md`.

Write

`Delta=pi/(2sqrt(3))`,

`x=T/D`,

`r=x-2`,

and work in the low-train branch `0<=r<1`.

For the chain three-phase orbit, let

- `lambda D+o(D)` and `mu D+o(D)` be the two boundary-side populations adjacent to
  the exact chain phase, with `lambda>=mu>=0`;
- `qD+o(D)` be all remaining atomic complement population.

The audited phase bookkeeping gives

`lambda+mu+q<=r`

and the exact necessary capacity inequality

`Delta <= G(lambda)+G(mu)+max(lambda q,q^2/4)`,

where

`G(z)=integral_0^z sqrt(1-3t^2/4) dt`.

The previous report relaxed `lambda<=lambda+mu`, which produced the certified decimal
bound `x>2.9328`.  That relaxation is not sharp because it combines a balanced
extremizer for the two `G` terms with a one-sided extremizer for `lambda q`.

This report optimizes the displayed three-variable expression exactly.

## 2. Elementary properties of G

On `0<=z<=1`,

`G'(z)=sqrt(1-3z^2/4)>0`,

and

`G''(z)=-(3z/4)/sqrt(1-3z^2/4)<=0`.

Thus `G` is increasing and concave.

A useful inequality is

### Lemma E1

If `0<=mu<=lambda` and `lambda+mu<=1`, then

`G'(mu)>=lambda`.

### Proof

It is enough to show

`1-3mu^2/4 >= lambda^2`.

Since `lambda<=1-mu`,

`lambda^2+3mu^2/4`

`<= (1-mu)^2+3mu^2/4`

`=1-2mu+7mu^2/4`

`<=1`,

because `0<=mu<=1` and `-2mu+7mu^2/4<=0` for `mu<=1<8/7`.  QED.

## 3. Eliminate complement mass in the star term

Consider first

`F_star(lambda,mu,q)=G(lambda)+G(mu)+lambda q`.

Because every term is nondecreasing under adding unused side mass, a maximizer under
`lambda+mu+q<=r` may be taken on the full-budget plane

`lambda+mu+q=r`.

Suppose `mu<lambda` and `q>0`.  Transfer an amount `epsilon` from `q` to the smaller
side `mu`, keeping `lambda` fixed.  For sufficiently small `epsilon`, ordering is
preserved.  The derivative of the capacity is

`G'(mu)-lambda`.

By Lemma E1 this is nonnegative.  Hence complement mass can be moved into the smaller
side without decreasing capacity until either `q=0` or `mu=lambda`.

If `mu=lambda=a` while `q>0`, transfer an amount `epsilon` from `q` equally into the
two sides.  The first derivative is

`G'(a)-a+q/2`.

Here `2a+q=r<=1`, so `a<=1/2`, while

`G'(a)>=G'(1/2)=sqrt(13)/4>1/2>=a`.

Thus this derivative is strictly positive.  Continue until `q=0`.

Therefore every star-term maximizer has `q=0`.  With `lambda+mu=r`, concavity gives

`G(lambda)+G(mu)<=2G(r/2)`.

Hence

### Theorem E2 — exact star envelope

For `0<=r<=1`,

`max [G(lambda)+G(mu)+lambda q] = 2G(r/2)`

over

`lambda>=mu>=0`, `q>=0`, `lambda+mu+q<=r`.

Equality is attained at

`lambda=mu=r/2`, `q=0`.

## 4. Eliminate complement mass in the Mantel term

Now consider

`F_M(lambda,mu,q)=G(lambda)+G(mu)+q^2/4`.

For fixed `q`, concavity and monotonicity give

`G(lambda)+G(mu)<=2G((r-q)/2)`.

Thus

`F_M<=f_r(q):=2G((r-q)/2)+q^2/4`.

Differentiate:

`f_r'(q)=-G'((r-q)/2)+q/2`.

For `0<=q<=r<=1`,

`q/2<=1/2`,

whereas

`G'((r-q)/2)>=G'(1/2)=sqrt(13)/4>1/2`.

Therefore `f_r'(q)<0` throughout the interval.  Its maximum is at `q=0`, giving

### Theorem E3 — exact Mantel envelope

For `0<=r<=1`,

`max [G(lambda)+G(mu)+q^2/4] = 2G(r/2)`

under the same population constraints.

## 5. Exact TS4 envelope

Since the maximum of the two bad terms may be optimized by taking the larger of their
separate maxima, Theorems E2 and E3 give

### Theorem E4 — exact audited two-side capacity

For every `0<=r<=1`,

`max_{lambda>=mu>=0, q>=0, lambda+mu+q<=r}`

`[G(lambda)+G(mu)+max(lambda q,q^2/4)]`

`=2G(r/2)`.

Thus every asymptotic C80–C96 chain-face survivor with `T/D<3` must satisfy

`Delta <= 2G((T/D-2)/2)`

in the subsequential limit.

The dangerous capacity configuration is not a three-phase path or a star with bad
complement mass.  It is the pure two-wall configuration with equal side populations
and no leading bad atomic complement.

This is useful structurally even though the numerical improvement over the previous
relaxation is small: the scalar Ferrers/phase mechanism is now exactly optimized, so
any further progress toward `T/D=3` must rule out or destabilize this balanced pure
two-wall endpoint.

## 6. Exact threshold

The function `2G(r/2)` is strictly increasing on `[0,1]`.  Let `r_*` be the unique
solution of

`2G(r_*/2)=Delta`.

Using

`G(z)=z/2 sqrt(1-3z^2/4) + (1/sqrt(3)) asin(sqrt(3)z/2)`,

the root is

`r_*=0.932935111451...`.

Therefore every subsequential low-train survivor obeys

`T/D >= 2+r_*`

`=2.932935111451...`.

Equivalently, no fixed subsequential limit

`T/D < 2.932935111451...`

is possible.

This slightly sharpens the audited `2.9328` certificate without introducing any
cross-side Cartesian block.

## 7. New endpoint normal form

Near the exact threshold, equality in E4 forces, at leading order,

`q=o(1)`,

`lambda-mu=o(1)`,

`lambda+mu=r_*+o(1)`.

Thus almost all atomic population outside the exact chain family lies in the two
chain-adjacent phase populations, split equally between the two boundary sides, and
all other leading phase-orbit crossing mass vanishes.

This is the correct next target.  A closing theorem should exploit the rigidity of a
balanced two-wall near-extremizer together with one of:

1. C93/LS2's quadratic secondary-separator demand;
2. C96's near-spanning common-cut diameter caterpillar;
3. C94's macroscopic exact active-face tangent flat; or
4. the strict `>60 degree` wall geometry, now in a near-equality rather than merely
   capacity setting.

No Level I conclusion is claimed.