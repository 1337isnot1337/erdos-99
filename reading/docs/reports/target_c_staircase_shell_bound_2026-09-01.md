> Generated reading edition · [exact source](../../../docs/reports/target_c_staircase_shell_bound_2026-09-01.md) · source SHA-256 `504a6f3c3f21e818c4c6b83fb7476f09369f8a1d10cc75c1e39a5231dbd4a57a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9A84F640589F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C89: staircase shell bound

**Date:** 2026-09-01  
**Repository base:** `2a4094ed` (main after C88 / PR #93)  
**Status:** LEVEL I STILL OPEN

C82 combines the exact C80 chain atom with the Target B exposed-hull/weighted-Mantel
theory. C87 adds a new global input: the complete source diameter graph has at least
`2D+1` edges and therefore at least `2D+1` diameter endpoints. C89 feeds that endpoint
floor back into C82 and obtains a substantially stronger train-count bound together
with a sharp equality classification.

Put

`Delta_2=pi/(2sqrt(3))`,

`A=1+Delta_2`,

`x=T/D`, `y=q/T`.

C82 proves

`x >= A/(1-y/2)+o(1)`.

C87 gives

`q/D=xy >= 2+o(1)`.

## C89.1 — improved train lower bound

From `xy>=2-o(1)`,

`x >= 2/y-o(1)`.

Hence asymptotically

`x >= max(2/y, A/(1-y/2))`.

The first function decreases with `y`; the second increases. They meet when

`2/y = A/(1-y/2)`,

so

`y_* = 2/(A+1)`

and

`x_* = A+1 = 2+Delta_2`.

The promoted Target B range contains this intersection. Therefore:

### Theorem C89 — staircase shell bound

Every asymptotic pure-rhombic global-minimizer sequence admitting the canonical
C80-C87 chain face satisfies

`liminf T/D >= 2+Delta_2`

that is,

`liminf T/D >= 2 + pi/(2sqrt(3))`

`= 2.9068996821...`.

This improves C82's `2.5425329094...` bound by about `0.36437 D` train tracks.

## C89.2 — equality point

Suppose an asymptotic sequence attains the new lower endpoint:

`T/D -> A+1`.

Because `2/y` and `A/(1-y/2)` meet uniquely at their minimum maximum, necessarily

`q/T -> y_* = 2/(A+1)`

and

`q/D -> 2`.

Thus every endpoint-sharp sequence simultaneously saturates C87's diameter-endpoint
floor.

C82 uses the total atomic train-direction mass `s` and the mass `a` of the chain
direction. At the endpoint,

`1/x_* = 1/(A+1)`

while

`S_*:=1-y_*/2 = A/(A+1)`.

Since `1/(A+1)>S_*/2`, the C82 proof is in its heavy distinguished-atom case. Equality
in its final inequality forces equality in every intermediate step:

`a -> 1/(A+1)`,

`s -> A/(A+1)`.

Therefore the `D` C80 chain trains asymptotically exhaust the entire atom in their
projective direction: there is no additional positive-density parallel train family
hidden on top of `P`.

The crossing-density identity also becomes equality in the heavy-vertex weighted
Mantel bound:

`R/T^2 -> Delta_2/(A+1)^2`

`= a(s-a)`.

The equality case of the heavy-vertex triangle-free bound is a star centered at the
distinguished atom. Consequently:

### Corollary C89.1 — endpoint atomic star

At the sharp endpoint `T/D -> 2+Delta_2`, the positive-density atomic crossing graph
is a star centered at the C80 chain direction. All residual atomic mass is adjacent to
the chain atom and carries no residual-residual positive-density crossing weight.

This is an asymptotic direction-measure statement, not a claim that the finite train
crossing graph is literally a star.

## C89.3 — exact frontier split

The canonical pure chain-face branch now has an explicit quantitative alternative.

1. **Train-surplus branch:** there is a fixed `epsilon>0` with
   `T/D >= 2+Delta_2+epsilon` along a subsequence. The extra linear train population
   must be combined with C88's quadratic separator budget and the Target B shell
   accounting.
2. **Endpoint-sharp branch:** `T/D -> 2+Delta_2`, forcing
   `q/D ->2`, exact asymptotic saturation of the C82 exposed-hull inequality, exact
   chain-direction atomic mass `1/(2+Delta_2)`, and a star atomic crossing measure.

The endpoint-sharp branch is much more rigid than the pre-C87 weighted-Mantel
endpoint; all inequalities producing C89 are simultaneously tight.

## Next target

A useful closing theorem should exclude one of these two branches:

- in the train-surplus branch, convert the excess `T-(2+Delta_2)D` or C88's
  secondary-train incidence into an Oler/global-packing loss;
- in the endpoint-sharp branch, show that a star atomic crossing measure with the C87
  paired staircase and `q/D->2` cannot realize the required global minimum-diameter
  packing density.
