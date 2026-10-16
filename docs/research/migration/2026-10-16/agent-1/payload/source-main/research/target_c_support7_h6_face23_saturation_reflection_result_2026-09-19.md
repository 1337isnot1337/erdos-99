# Target C support-seven H6: face-(2,3) saturation and reflection closure

Date: 2026-09-19

Status: exact finite reduction inside the degree-pure support-seven generic `H6` branch. The theorem-state authority is unchanged. C-II remains open.

## Result

The previous explicit reflection-closed generic-`H6` endpoint was

\[
4158=3316\,C_7+842\,(C_3\sqcup C_4).
\]

The frozen face-`(2,3)` saturation ledger contains 192 states that remain in that endpoint. Every one of those 192 direct candidates has now been excluded by exact rational Farkas certificates covering the full local branch product at physical faces 2 and 3. Closing those direct exclusions under the already-certified hull-reflection involution removes 284 distinct states in total. Therefore the new explicit exact endpoint is

\[
\boxed{3874=3076\,C_7+798\,(C_3\sqcup C_4)}.
\]

The 284 removed states split as

```text
C7       240
C3+C4     44
```

and by ground sign pattern as

```text
235    42
236    96
245     4
256    96
346     4
356    42
```

The surviving reflection-symmetric census is

```text
145      4
156     16
235    514
236    950
237     16
245    445
256    950
345     16
346    445
347      4
356    514
```

Thus the paired pattern counts remain exactly equal under hull reflection:
`145 <-> 347`, `156 <-> 237`, `235 <-> 356`, `236 <-> 256`, and `245 <-> 346`; `345` is self-reflecting.

## Exactification ledger

The 192 direct candidates were frozen in

`research/verify_target_c_support7_h6_face23_saturation_fast_2026_09_19.py`

with SHA-256 guard

`3388a16ee53a772581652d144b03d25230f44aeff1db9a7b954860f84250b6f0`.

They split as

```text
C7       159
C3+C4     33
```

with direct ground-pattern counts

```text
235    41
236    49
245     4
256    71
356    27
```

The four exactification chunks covered all 192 candidates and all passed. In aggregate they checked 17,094 exact rational Farkas certificates. Their forced constants were

```text
negative    16331
zero          763
```

and the largest active rational multiplier denominator was

`209643407927959363247856376694`.

The bounded rerun ledger is

```text
range       states   C7   C3+C4   certificates   negative   zero   max denominator
0..49          50    42       8          3887       3700    187   1845201429004817659476259
50..99         50    38      12          5258       5088    170   209643407927959363247856376694
100..149       50    43       7          4097       3884    213   12360927146073734868730000000
150..191       42    36       6          3852       3659    193   4979217501673542382479484
```

Numerical LPs were used only to recover sparse dual supports. A branch was accepted as impossible only after exact rational reconstruction verified nonnegative inequality multipliers, normalized positive weight on the original strict facets, coefficientwise cancellation in all 85 affine variables, unrestricted equality multipliers, and a nonpositive forced constant.

For each direct state, the verifier covers all twenty closed branches at face 2 and all twenty closed branches at face 3. Locally dead one-face branches receive exact certificates; every product of the remaining live branches receives an exact two-face certificate. Hence each direct cell is excluded without treating numerical infeasibility as proof.

## Reflection accounting

The 192 direct states have 192 reflected images. Exactly 100 states lie in both sets, so

\[
|D\cup\rho(D)|=192+192-100=284.
\]

The hull-reflection map on the exact 14,174-state `H6` representation was already proved to be an involution preserving the relevant geometric problem. Therefore an exact impossibility certificate for a direct state excludes its reflected state as well. The summary reconstruction checks that the 284-state removal set and the resulting 3,874-state survivor set are both reflection invariant.

The separate source-backed bookkeeping run reproduced

```text
fresh_direct          192
reflected_image       192
direct_image_overlap  100
removed_union         284
survivors             3874
```

with the graph and pattern censuses stated above.

## Scope and next target

This closes every state in the committed numerical fixed-face-`(2,3)` candidate ledger that survives to the 4,158-state endpoint. It does **not** prove exact feasibility of every remaining state for the face-`(2,3)` affine branch system. A state absent from the numerical candidate ledger had a positive numerical feasibility margin in the discovery pass; that numerical primal evidence is not promoted here to an exact feasibility certificate. The proved statement is the 284-state exact exclusion and the 3,874-state reflection-closed endpoint, not a claim that no further exact face-`(2,3)` obstruction exists. Reciprocal-collinearity walls remain outside the generic `H6` branch.

The next higher-value affine test is the already-proved all-root interior-domination theorem. For each interior target `t in {6,7}` and every root `r != t`, let hull edge `ab` bracket the ray `r -> t`. Every genuine realization satisfies

\[
D^{(r)}_{a t}<0\quad\text{or}\quad D^{(r)}_{b t}<0.
\]

A cheap first pass should test the two closed alternatives separately on each of the 3,874 surviving cells and exclude a cell whenever both alternatives for one root-target pair have exact Farkas contradictions. Only survivors of that depth-one filter need the full fourteen-disjunction branch-and-bound, global `L(K_8)` segment-order cycle tests, and nonlinear sine-law metric conditions.

A secondary affine route is to scan non-reflection-equivalent two-face pairs. Earlier exact reductions already found useful witnesses at `(2,7)`, `(2,6)`, and `(2,4)`, so those pairs are concrete targets if the domination filter stalls.

Primary certificates and bookkeeping:

- `research/verify_target_c_support7_h6_face23_saturation_reflection_2026_09_19.py`
- `research/verify_target_c_support7_h6_face23_saturation_fast_2026_09_19.py`
- `.github/workflows/target-c-face23-saturation.yml`

No theorem-state authority file is changed by this reduction.
