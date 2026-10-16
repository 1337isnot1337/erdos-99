<!-- theorem-state: {"artifact_id":"ART-C55C0FF5B1C7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: pivot-localized secondary load

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Input

Use the C87--C88 common-chain staircase. Every simple staircase interval

`e=(a_e,b_e]`

contains the common pivot train `tau_s`, so

`a_e < s <= b_e`.

Fix `r` simple staircase edges and both physical C87 orientations above each of them. The most useful choice is the `r` shortest staircase intervals, as in the secondary cap load/span theorem, but the localization lemma below only uses that all selected intervals contain `s`.

For a secondary train `sigma`, let

`K_sigma`

be its consecutive block of chain prefix levels, and let

`j_sigma`

be the number of chain trains crossed by `sigma`; thus `|K_sigma|=j_sigma+1`.

Let `m_sigma(r)` be the number of selected physical diameter edges separated by `sigma`.

Finally let

`Q_s={sigma secondary : sigma crosses tau_s}`.

Equivalently, `s` is an interior chain cut of the consecutive block `K_sigma`.

## 2. Double hits are possible only at the pivot

For one simple staircase interval `e=(a,b]`, C87 supplies two physical oriented diameters above the same prefix endpoints `a,b`.

A secondary train can separate at most one of these two physical diameters unless both prefix endpoints `a,b` lie in `K_sigma`. This is exactly the double-hit mechanism used in the earlier CSL1 proof.

But every staircase interval satisfies

`a < s <= b`.

Therefore, if both `a,b` lie in the consecutive integer block `K_sigma`, then the entire integer interval from `a` to `b` lies in `K_sigma`, in particular the pivot cut `s` lies in that block. Hence `sigma` crosses `tau_s`.

So a secondary train outside `Q_s` has **no** double-hit staircase edge at all.

### Lemma PL1 — pivot localization

For the selected `r` simple staircase edges,

- if `sigma notin Q_s`, then `m_sigma(r) <= r`;
- if `sigma in Q_s`, then

`m_sigma(r) <= r + min(r,j_sigma)`.

Proof. The baseline contribution is at most one physical diameter per selected simple edge, hence at most `r`. A second contribution from a selected simple edge is possible only when both prefix endpoints lie in `K_sigma`; by the preceding paragraph this forces `sigma in Q_s`. The double-hit simple edges form a forest in the prefix tree induced on `K_sigma`, hence there are at most `j_sigma` of them, and trivially at most `r`. QED.

This strictly sharpens CSL1 away from the common cut.

## 3. Localized load inequality

Let `M=T-D` be the number of secondary trains. Let

`I_r = sum_sigma m_sigma(r)`.

The existing lower-incidence theorem LS2 gives

`I_r >= r(2D+1-r)`.

Using PL1,

`I_r`

`<= r(M-|Q_s|) + sum_(sigma in Q_s) [r+min(r,j_sigma)]`

`= rM + sum_(sigma in Q_s) min(r,j_sigma)`.

Hence, for every admissible `r`,

`sum_(sigma in Q_s) min(r,j_sigma)`

`>= r(2D+1-r-M)`

`= r(3D+1-T-r)`.                              (PL2)

This is the same quadratic lower demand as CSL2, but now the entire excess is carried by secondary trains crossing one distinguished chain train `tau_s`.

## 4. Two exact consequences

Set

`A=3D+1-T`.

Taking `r=1` in PL2 gives

`|Q_s| >= A-1 = 3D-T`.                         (PL3)

Thus every deficit of one train below `3D` forces at least one secondary train through the common pivot.

Taking `r=floor(A/2)` and using `min(r,j_sigma)<=j_sigma` gives

`sum_(sigma in Q_s) j_sigma >= floor(A^2/4)`.  (PL4)

Equivalently,

`sum_(sigma in Q_s) j_sigma`

`>= floor((3D+1-T)^2/4)`.

So the full quadratic chain--secondary crossing demand from CSL3 is already present inside the fan of secondary trains that all cross `tau_s`.

For `T/D -> x<3`, this yields asymptotically

`|Q_s|/D >= 3-x-o(1)`

and

`D^(-2) sum_(sigma in Q_s) j_sigma >= (3-x)^2/4-o(1)`.

At the current explicit threshold `x=2.9346`, the localized fan therefore has at least about `0.0654D` trains and carries at least about `0.001069D^2` chain--secondary crossing incidences.

## 5. Geometric phase consequence

All trains in `Q_s` cross the same chain train `tau_s`.

In a pure unit-rhombic triangle-free packing, two crossing train directions must meet at projective angle strictly between `pi/3` and `2pi/3` in an oriented representative, equivalently at acute line angle strictly greater than `pi/3`: otherwise one diagonal of the unit rhombus has length at most `1`, with equality producing a unit equilateral triangle.

Choose the chain direction as angle `0 mod pi`. Every train in `Q_s` therefore has projective direction in the open interval

`(pi/3,2pi/3) mod pi`,

whose width is exactly `pi/3`.

Hence two distinct trains in `Q_s` have projective angular separation strictly less than `pi/3`. They cannot cross one another in a triangle-free unit-rhombic disk.

### Lemma PL5 — pivot fan is noncrossing

`Q_s` is an independent set in the train-crossing graph.

Thus PL3--PL4 localize a quadratic amount of chain--secondary incidence into a linear-size family of mutually noncrossing secondary trains.

## 6. Why this is new leverage

The earlier cap load/span theorem allowed its quadratic demand to be distributed over all secondary trains. PL2 shows that this is unnecessary: the deficit below `3D` creates one macroscopic noncrossing pivot fan.

Any crossing/area upper envelope used to prove `T/D>2.9346` can therefore be sharpened by treating `Q_s` as a forced independent phase block of size at least `3D-T`, rather than as unrestricted secondary mass.

The remaining task is to insert this forced block into the repaired same-side/central-block QJ capacity calculation without reintroducing the retracted Cartesian cross-wall assumption. If that capacity loss exceeds the present `~8e-4 D^2` numerical margin gap, the explicit train lower bound improves; if the resulting envelope stays below the Oler density constant all the way to `x=3`, it would close Target C asymptotically.
