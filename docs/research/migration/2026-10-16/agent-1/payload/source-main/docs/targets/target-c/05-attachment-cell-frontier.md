# Target C — attachment-cell frontier C43-C46

**LEVEL I STATUS: STILL OPEN.**

This module is additive to the canonical C41-C42 response/defect theorems already on `main`.

## C43 — disjoint harmonic cells

For each unpinned harmonic component `I_r`, let `A_r` be its distinct loaded attachment set and `P_r=conv(A_r)`. C36 gives `I_r subset P_r` and `|A_r|>=3`.

C43 proves the cell interiors are pairwise disjoint:

`int(P_r) cap int(P_s)=empty` for `r!=s`.

Hence

`sum_r area(P_r) <= area(F)`.

The proof combines C36 noncrossing with C37's incidence bound to exclude both proper crossing and containment.

## C44 — exact partition endpoint

Assume `e_BB=0` and every loaded vertex belongs to exactly one attachment set. Then C44 proves

`c_I=1` and `A_1=B_+`.

Reason: each harmonic component has zero net boundary response, so its attachment block must have zero sum of C10 reaction vectors. Every proper cyclic interval of the strictly cyclic nonzero reaction field has nonzero resultant. Every noncrossing partition with at least two blocks has a proper interval block. Contradiction.

Thus any multi-component response phase must spend boundary surplus on shared loaded pins or loaded-loaded contacts.

## C45 — cellwise Oler capacity

Let

`G=area(F)-sum_r area(P_r)>=0`.

Applying Oler separately to `I_r union A_r` inside `P_r` gives

`(sqrt3/2)(n_I+sum|A_r|-c_I)
 <= area(F)-G +(sqrt3/4)sum per(P_r)`.

Using `per(P_r)<=pi D` and C38's `q-q_used<=e_BB`, the force-visible core population `m` satisfies

`m <= (2/sqrt3)(area(F)-G) +(pi/2)D c_I+c_I+e_BB`.

Hence

`m <= Delta_2 D^2 -(2/sqrt3)G +(pi/2)D c_I+c_I+e_BB`.

This isolates the exact area/perimeter quantity needed for a finite-capacity closure. It deliberately reduces to ordinary Oler in the C44 one-component endpoint, where `G=0`.

## C46 — diameter coupling is mostly cross-cell

For sufficiently large sources, at most three attachment cells contain a full core diameter edge with both endpoints in that cell's attachment set.

Two vertex-disjoint diameter chords internal to distinct cells would have to cross by diameter-thrackle geometry, contradicting C43. Thus selected internal diameter edges from distinct cells are pairwise intersecting. Four such edges form either a common star or a diameter triangle. The diameter triangle is globally excluded; a common star would put one loaded vertex in four attachment sets, contradicting loaded contact degree at most three.

Therefore, except for at most three cells, all full-diameter coupling is exported across the harmonic cell decomposition.

## Current geometric normal form

In the C33 near-minimal boundary phase:

```text
Theta(D) loaded boundary vertices
all but o(D) belong to exactly one of o(D) harmonic components
I_r subset P_r=conv(A_r)
P_r have pairwise disjoint interiors
sum internal component graph diameters = O(D)
exact zero-defect multi-cell partition impossible (C44)
except in at most 3 cells, full diameter edges leave the cell (C46)
```

Together with canonical C41's strict response diameter-defect trace and C42's linear quadrangulation defect, the remaining response problem is sharply geometric: convert the contact-local / diameter-nonlocal cell decomposition into a quantitative response, area, or container contradiction.

## Shortest next targets

1. **Cell response-area theorem:** lower-bound the C41 response diameter defect or cell-area gap in terms of attachment-cell geometry without assuming a lower bound on individual KKT weights.
2. **Force-bulk theorem:** show the force-visible core contains all but `O(D)` source points, so C45 becomes a global source-capacity estimate rather than only a core estimate.
3. **Cross-cell diameter theorem:** exploit C46 plus diameter-thrackle/C18 geometry to constrain the quotient graph of diameter couplings between the nonoverlapping cells.

No current theorem proves any of these three.
