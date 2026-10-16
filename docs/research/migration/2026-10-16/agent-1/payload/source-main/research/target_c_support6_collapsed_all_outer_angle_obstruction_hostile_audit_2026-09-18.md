# Hostile audit — collapsed common all-outer angle obstruction

**Date:** 2026-09-18  
**Audited source:** `research/target_c_support6_collapsed_all_outer_angle_obstruction_2026-09-18.md`  
**Disposition:** PASS as a chamber-local conditional exclusion; theorem-state authority unchanged

## Scope of the topological input

The endpoint-order step is not a consequence of six parallel directions alone. It
requires the stated common-host chord model: six pairwise disjoint outside trains run
from the six pentagon hosts to one common outer face, and their noncrossing arcs induce
one cyclic order of the six host endpoints. The note is restricted to that model. It
does not apply when the six trains terminate at several activated faces, when the
global routing has intervening holes that invalidate the chord model, or outside the
certified local angle box.

## Interval check

The verifier uses the twelve rational center angles and radius `10^-10` from the exact
local contraction certificate. It encloses `pi` by the Machin formula with alternating
series bounds. For each of the 720 endpoint orders it enumerates every endpoint-
alternating pair, computes the minimum upper bound of its projective angle distance,
and requires that one is below the lower bound `pi/3`. The printed maximum witness
upper bound is about `0.842605`, while `pi/3` is above `1.047197`; the margin is
strictly positive.

## Geometric implication

An alternating pair of endpoint-disjoint proper chords must intersect. The audited
train-pseudosegment theorem permits a strict train crossing only when the projective
direction separation is greater than `pi/3`. The interval witness has separation
strictly below `pi/3`, so it cannot be such a crossing. This contradicts every cyclic
order in the common-host model.

No assertion is made that all train interactions are crossings, that the local
auxiliary genus-two quotient is physical, or that the entire collapsed branch is
excluded.

**Audit conclusion:** the certificate is exact at its stated chamber/local-routing
scope and leaves the multi-host positive-slack branch open.
