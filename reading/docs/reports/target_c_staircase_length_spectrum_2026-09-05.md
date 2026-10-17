> Generated reading edition · [exact source](../../../docs/reports/target_c_staircase_length_spectrum_2026-09-05.md) · source SHA-256 `c9e16e111f33610f12b29c142191e5288db371246f990e90c3ba5e6c4346dc49`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-16C456950FD5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C exact staircase length spectrum

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact consequence of C88 + C93  
**Target:** canonical C80–C96 chain-face survivor  
**Status:** LEVEL I STILL OPEN

## 1. Input

Use the exact C88 staircase parametrization.  The distinct left endpoints are

`a_i=i-1`, `1<=i<=s`,

and row `i` contains exactly the edges

`(i-1,b)`, `t_i<=b<=t_(i-1)`,

where

`t_0=D`, `t_s=s`, `t_0>=t_1>=...>=t_s`.

For an edge `e=(a,b)`, write its chain-interval length as

`ell(e)=b-a`.

C93 says that each selected physical diameter over an interval of length `ell`
requires at least

`D+1-ell`

non-chain separating trains.  C87 supplies two selected physical diameter orientations
over each staircase edge.

## 2. Exact length spectrum

For row `i`, the edge lengths are the consecutive integers

`{t_i-i+1, t_i-i+2, ..., t_(i-1)-i+1}`.

For adjacent rows, the maximum length in row `i` is

`t_(i-1)-i+1`,

while the minimum length in row `i-1` is

`t_(i-1)-(i-2)=t_(i-1)-i+2`.

Thus adjacent row-length intervals are disjoint and consecutive.  The bottom row has
minimum length

`t_s-s+1=1`,

and the top row has maximum length

`t_0=D`.

There are exactly `D` staircase edges.  Hence:

### Theorem LS1 — staircase length spectrum

The multiset of chain-interval lengths of the C88 staircase tree is exactly

`{1,2,...,D}`.

In particular every possible positive chain length occurs once and only once.

This strictly refines the aggregate identity

`sum_e ell(e)=D(D+1)/2`.

## 3. Tail-resolved secondary-separator budget

Order the staircase edges by length.  For `1<=r<=D`, let `E_(<=r)` be the `r` edges
whose lengths are `1,...,r`, and let `S_(<=r)` be the `2r` selected physical diameter
pairs over those edges, one in each hull-arc orientation.

For the two selected diameters over the unique interval of length `ell`, C93 gives at
least

`2(D+1-ell)`

incidences with non-chain separating trains.  Summing for `ell=1,...,r` gives

`I_r >= 2 sum_(ell=1)^r (D+1-ell)`

`    = 2r(D+1)-r(r+1)`

`    = r(2D+1-r)`.

Therefore:

### Theorem LS2 — exact tail incidence profile

For every `1<=r<=D`, the selected diameters over the `r` shortest staircase intervals
have at least

`r(2D+1-r)`

incidences with the `T-D` non-chain trains.

Consequently some non-chain train separates at least

`ceil( r(2D+1-r)/(T-D) )`

of those `2r` selected diameters.

At `r=D`, this recovers C93 exactly:

`I_D>=D(D+1)`.

For a sequence with `T/D -> x>1` and `r/D -> alpha in (0,1]`, LS2 gives a secondary
train cutting at least

`((2alpha-alpha^2)/(x-1)-o(1))D`

selected diameters whose chain intervals all have length at most

`(alpha+o(1))D`.

## 4. Why the tail form is stronger input

C93 only forces one secondary train to be heavily loaded somewhere in the full paired
staircase.  LS2 permits the averaging to be restricted to short chain intervals.
Thus any prospective two-cut capacity theorem can trade two quantities explicitly:

1. secondary-cut load `~(2alpha-alpha^2)D/(x-1)`;
2. maximum chain span `alpha D` of every loaded candidate edge.

For example, throughout `T<=3D`, choosing `alpha=1/2` forces one secondary train to
separate at least

`(3/8-o(1))D`

selected diameters all having chain span at most `(1/2+o(1))D`.

This is weaker in raw edge count than the full C93 half-density cut, but substantially
stronger geometrically because every selected edge in the subsystem has a uniformly
short chain interval.

## 5. Frontier

A closing theorem may now use a span-sensitive two-cut capacity rather than a
span-blind caterpillar count.  It would be enough to show that a secondary train cannot
separate

`r(2D+1-r)/(T-D)`

paired staircase diameters all having chain span at most `r`, for some optimized `r`,
without forcing an even diameter cycle, a forbidden unit triangle, or a strict
sub-`D` competitor.

No such capacity theorem is claimed here.
