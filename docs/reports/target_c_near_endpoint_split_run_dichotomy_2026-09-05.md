<!-- migration-source: path=docs/reports/target_c_near_endpoint_split_run_dichotomy_2026-09-05.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=dd478e129fc9e506f586ecf2acdf165179f80abf; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C: near-endpoint split/run dichotomy

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Input

Write

`x=T/D`

for the train/diameter ratio and

`Delta=pi/(2sqrt(3))=0.9068996821...`.

C82 gives, in the canonical low-train phase,

`q/D <= 2x-2(1+Delta)+o(1)`,

where `q` is the number of source points incident with at least one diameter.

The corrected prefix-fiber split budget gives

`S <= q-2D`,

where

`S=sum_(X in {L,U}) sum_(k=0)^D (n_(X,k)-1)`

is the total physical split excess over the two formal prefix fibers.

Therefore

`S/D <= sigma(x)+o(1)`,

with

`sigma(x)=2x-4-2Delta=2(x-2-Delta)`.          (1)

At the current explicit threshold `x=2.9346`,

`sigma(2.9346)=0.0554006358...`.               (2)

Thus fewer than `0.055401D+o(D)` units of prefix splitting are available there.

## 2. Bad prefix levels are sparse

Call a prefix level `k` **good** when both side fibers are unsplit:

`n_(L,k)=n_(U,k)=1`.

Call it **bad** otherwise, and let `B` be the number of bad prefix levels.

Every bad level contributes at least one unit to `S`, so

`B <= S`.                                      (3)

Combining (1)--(3),

`B/D <= sigma(x)+o(1)`.

At `x=2.9346`, at least

`0.944599364...D-o(D)`

of the `D+1` prefix levels are good.

This statement concerns prefix levels, not staircase edges. A bad high-degree run center can still touch many staircase edges, so no edge-density conclusion is being smuggled in here.

## 3. Insert the C99 run-center spine

C99 identifies the simple prefix tree `G_P` with the occupied cells of a monotone lattice path. Let

`R`

be the number of maximal constant runs in its binary move word. The `R` vertices of degree at least two in `G_P` are exactly the run centers, in run order, and they induce a path with `R-1` spine edges.

Let `H` be the number of spine edges whose two endpoints are both good prefix levels.

Each bad run center can spoil at most two spine edges. Therefore

`H >= R-1-2B`.                                 (4)

Using `B<=S`,

### Theorem NSR1 — split/run dichotomy

`H >= R-1-2S`.                                 (5)

In particular, either

`R <= 2S+1`,                                   (6)

or the C99 spine contains at least one good--good adjacency. More quantitatively, if

`R/D -> rho`,

then

`H/D >= max(0,rho-2sigma(x))-o(1)`.            (7)

At `x=2.9346`,

`H/D >= max(0,rho-0.1108012716...)-o(1)`.      (8)

Thus a staircase with more than about `0.110802D` runs forces a linear family of consecutive unsplit run-center adjacencies.

## 4. The complementary long-run regime

If (6) holds, the binary move word has length `D-1` partitioned into at most `2S+1` runs. Hence its longest run has length at least

`L_max >= (D-1)/(2S+1)`.                       (9)

At the 2.9346 threshold, (2) gives asymptotically

`L_max >= 1/(0.1108012716...)-o(1)`

`= 9.02516...-o(1)`.                           (10)

This finite lower bound is not itself a contradiction; the point is a clean phase split:

- **few-run phase:** one has a long diameter star in the C99 caterpillar;
- **many-run phase:** one has many adjacent good run centers, so every corresponding prefix-tree edge is completely unsplit at both endpoints and the exact C100 two-sheet diameter quadrilateral identities apply there without physical-fiber ambiguity.

## 5. Stronger finite form for a prescribed run density

For any `epsilon>0`, if

`R >= (2sigma(x)+epsilon)D`,

then (5) gives

`H >= epsilon D-o(D)`.

At `x=2.9346`, any run density above

`0.110801272`

therefore produces a positive-density path segment set on which the physical two-sheet lift is exact.

Conversely, if the number of such exact consecutive junctions is `o(D)`, then

`R/D <= 0.110801272+o(1)`

and the average binary run length is at least `9.025+o(1)`.

## 6. Remaining gate

NSR1 is the first direct transfer from the repaired quantitative train bound to the exact C99/C100 endpoint geometry. It does not yet close Target C because:

1. a single split at a high-degree run center can partition arbitrarily many incident staircase edges;
2. a run of length about nine is geometrically legal under the current shared-endpoint diameter fan bound;
3. the local C100 identities on many good--good spine edges still need a global summation or curvature/capacity inequality.

A closing argument must therefore show either that long C99 runs consume more hull/diameter angular capacity than available, or that a positive density of consecutive unsplit C100 quadrilaterals forces an impossible equal-length diameter geometry.