> Generated reading edition · [exact source](../../../docs/reports/target_c_transition_perimeter_shell_tradeoff_2026-09-05.md) · source SHA-256 `05f0d09b66ac26537ec27ae26498eec343cbcf7d231e671cb5950a953f72e035`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F55767481747","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C transition perimeter/shell tradeoff

**Date:** 2026-09-05  
**Repository state:** `738f6f87` (`main`)  
**Run type:** exact finite strengthening of the chain-terminal transition budget  
**Target:** Target C C80–C96 pure-rhombic chain-face branch  
**External web search:** not used  
**Computation:** arithmetic only

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting point

The chain-terminal hull-transition theorem gives `2D` distinguished convex-hull indentation chains, one through every terminal incidence of the `D` chain trains. If `m_2` of those distinguished chains have exactly two unit contact edges, then

`m_2 >= 4D+q-2T-4`,

and C96 gives the coarser bound

`m_2 >= 2(3D-T)-2`.

For one two-edge transition `A--V--B`, let `alpha` be the angle between the two unit rays `VA,VB`. Then

`|A-B| = 2 sin(alpha/2) > 1`

by triangle-freeness and unit separation, so `alpha>pi/3`. The old transition report records the exact dichotomy:

1. `alpha<=2pi/3`, in which case the shell ear between `AV,VB` and the hull chord `AB` has area at least `sqrt(3)/4`; or
2. `alpha>2pi/3`, in which case the convex-hull side `AB` has length strictly greater than `sqrt(3)`.

The missing observation is that both resources can be summed globally because the distinguished transitions lie in distinct indentation chains between consecutive convex-hull vertices.

## 2. Perimeter-excess bound for the shallow-ear class

Let

- `M=m_2`;
- `M_E` be the number of two-edge distinguished transitions with ear area at least `sqrt(3)/4`;
- `M_L=M-M_E` be the number whose hull side has length `>sqrt(3)`;
- `P` be the convex-hull perimeter.

Every hull side joins two source points, hence has length at least `1`. There are `q` hull vertices and therefore `q` hull sides. Since the hull has diameter `D`, the classical perimeter bound gives

`P <= pi D`.

Consequently the total perimeter excess above the unit baseline obeys

`sum_(hull sides s) (|s|-1) = P-q <= pi D-q`.

Every side belonging to the `M_L` class contributes strictly more than

`sqrt(3)-1`

to that excess, and these sides are pairwise distinct. Therefore

`M_L (sqrt(3)-1) < pi D-q`.

Equivalently,

`M_E > M - (pi D-q)/(sqrt(3)-1)`.

For a weak non-strict form convenient in asymptotic bookkeeping,

`M_E >= M - floor((pi D-q)/(sqrt(3)-1))`.

## 3. Additive shell charge

The shell ears associated with distinct convex-hull sides have pairwise disjoint interiors: each is the region between one convex-hull side and its corresponding contact-boundary indentation chain. Hence the `M_E` large ears may be summed directly inside the old shell defect `G`.

Thus

`G >= (sqrt(3)/4) M_E`.

Combining with the perimeter-excess estimate gives the exact finite tradeoff

`G >= (sqrt(3)/4) max(0, M - floor((pi D-q)/(sqrt(3)-1)))`.

Using `M=m_2` and the transition-count theorem,

`G >= (sqrt(3)/4) max(0,
  4D+q-2T-4 - floor((pi D-q)/(sqrt(3)-1)))`.

Ignoring only the integer floor gives the asymptotic form

`G/D >= (sqrt(3)/4) max(0,
  4 + q/D - 2T/D - (pi-q/D)/(sqrt(3)-1)) - o(1)`.

This is a genuine additive statement. It does not assume persistence of activated contacts and does not combine events at different source configurations.

## 4. Coarse C96 corollary

C96 gives `q>=2D+2`. Substituting only that lower bound yields

`G >= (sqrt(3)/4) max(0,
  6D-2T-2 - floor(((pi-2)D-2)/(sqrt(3)-1)))`.

The resulting coefficient becomes positive only below approximately

`T/D < 3 - (pi-2)/(2(sqrt(3)-1)) = 2.2202...`,

which is far below the already canonical C92 range. Therefore the coarse `q>=2D+2` specialization does **not** close the active low-train branch.

The theorem is useful only when another argument supplies a stronger lower bound on `q/D`, or when the long-side class can be charged by a sharper diameter/area inequality than perimeter excess alone.

## 5. Why this is still progress

The previous boundary-neighbor handoff left two cases qualitatively:

- large-angle neighbors give shell ears;
- shallow-angle neighbors give long hull sides.

The present theorem removes the possibility that the second class is arbitrarily large for free. Its entire population is paid for by the finite perimeter-excess currency `pi D-q`.

Therefore any future lower bound on `q`, or any independent use of perimeter excess elsewhere in the shell master inequality, can be inserted without redoing the transition geometry.

It also identifies the exact obstruction to this line by itself: in the current canonical range, the available perimeter-excess budget is still large enough to absorb all forced two-edge transitions.

## 6. Audit classification

| Statement | Classification | Reason |
| --- | --- | --- |
| `M_L(sqrt(3)-1)<pi D-q` | proved | distinct hull sides + unit baseline + perimeter `<=pi D` |
| large-ear transition regions are additive | proved | distinct convex-hull side shell ears have disjoint interiors |
| displayed perimeter/shell tradeoff | proved | direct combination |
| C96 lower bound alone closes `T<3D` | rejected | numerical threshold is only about `2.2202D` |
| a stronger `q/D` lower bound could make the tradeoff effective | conditional interface | requires an independent theorem |

## 7. Handoff

```text
LEVEL I STATUS: STILL OPEN.

For M=m2 forced two-edge chain-terminal transitions, split them into large-ear and long-side classes. Then

  M_long (sqrt(3)-1) < pi D-q

and

  G >= (sqrt(3)/4) M_ear.

Therefore

  G >= (sqrt(3)/4) max(0,
      4D+q-2T-4 - floor((pi D-q)/(sqrt(3)-1))).

This is an exact additive shell/perimeter tradeoff. The coarse q>=2D+2 bound is too weak to close the live range, so the next useful step is either a stronger q/D lower bound or a sharper cost for the long-side class.
```