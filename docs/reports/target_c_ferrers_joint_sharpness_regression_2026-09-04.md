<!-- theorem-state: {"artifact_id":"ART-E8D0008213C2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C Ferrers joint-sharpness regression

**Date:** 2026-09-04  
**Repository base:** research branch after `ddbd894f`  
**Run type:** exact regression / route limitation  
**Target:** exact bad-crossing refinement of C92  
**Status:** LEVEL I STILL OPEN

## 1. Why this regression is needed

The exact bad-crossing theorem in `target_c_exact_bad_crossing_ferrers_stability_2026-09-04.md`
proves, for `x=T/D in [2+Delta,3]`,

`bad crossings <= (Delta-u)D^2+o(D^2)`,

where

`u=u(x)` is the lower root of

`u(x-1-u)=Delta`.

It also uses the independent residual-population bound

`lambda <= x-2`.

A possible next improvement would be to argue that these two bounds cannot be sharp at
the same time. That is false already in the limiting three-phase capacity model used
by C92.

## 2. Exact atomic-path extremizer

Put

`r=x-2`

and let

`u=u(x)`.

Consider three projective phase atoms `A,B,C` in one `60-degree` orbit with scaled
train populations, in units of `D`,

`|A_exact|=1`,

`|B|=u`,

`|C|=r-u`.

Use the triangle-free phase-support path

`A -- B -- C`

and no other positive-density phase edges. There is no extra chain-parallel atomic
mass and no atomic mass in other phase orbits.

The two complete product capacities are

`AB = u`,

`BC = u(r-u)`.

Since

`u(x-1-u)=u(1+r-u)=Delta`,

one has

`u+u(r-u)=Delta`.

Also

`u(r-u)=Delta-u`.

Therefore this single abstract phase assignment simultaneously has

- total leading crossing capacity exactly `Delta D^2`;
- exact-chain good crossing capacity exactly `uD^2`;
- bad crossing capacity exactly `(Delta-u)D^2`;
- full chain-orbit residual population exactly `(x-2)D`.

Thus the two scalar bounds used in the improved Ferrers argument are jointly sharp in
the same phase model.

## 3. Consequence

No improvement that uses only

1. total atomic mass `s<=1-1/x`,
2. the exact `D`-train chain atom,
3. triangle-freeness of the limiting phase graph, and
4. the total required crossing density `Delta D^2`

can force either a smaller bad-crossing term or a smaller residual-wall population in
general. The obstruction is the three-phase path above.

This is a regression for the **scalar phase-capacity mechanism**, not a construction
of an actual global minimizer. It deliberately ignores the finite train pseudoline
order, the C87 staircase, the C93 separator incidence, and the C96 common-cut
caterpillar. Those are exactly the structures that must now exclude the path.

## 4. Geometric form of the next target

The dangerous asymptotic phase pattern is now explicit:

- `A`: the exact C80 chain direction, population `D`;
- `B`: population `uD`, carrying almost all `A-B` capacity;
- `C`: population `(x-2-u)D`, carrying almost all `B-C` capacity;
- `A-C`: negligible leading crossing mass.

At `x=3`, for example,

`u=1-sqrt(1-Delta)=0.69487655...`,

so the abstract escape has approximately

`0.69488D` B-trains and `0.30512D` C-trains.

A closing theorem for the interval up to `x=3` should therefore attack this path
geometrically: show that two macroscopic coherent residual train families cannot make
`Theta(D^2)` B-C crossings while one of them also makes the required dense crossings
with the exact chain family and the other remains nearly chain-invisible, subject to
the C87/C93/C96 ordered diameter structure.

Further scalar weighted-Mantel optimization is exhausted by this regression.
