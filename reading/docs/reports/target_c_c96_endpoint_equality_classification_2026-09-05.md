> Generated reading edition · [exact source](../../../docs/reports/target_c_c96_endpoint_equality_classification_2026-09-05.md) · source SHA-256 `f1be10fc29fa7a9011ac8f6c0f936f44e923a2d5cb86cf411991f67f7845f6cb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3F16E3C4802D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C96 endpoint equality classification

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact finite equality classification / route audit  
**Target:** C96 common-chain endpoint floor  
**Status:** LEVEL I STILL OPEN

## 1. Purpose

The exact C96 floor is

`q>=2D+2`.

The FSB report gives the physical prefix-fiber bookkeeping needed to analyze equality
without making the false identification “prefix level 0 = z” or “prefix level D = a”.
The new mainline chain-cut load profile shows that the C96 chain train is the unique
maximally loaded chain cut.

This note classifies all overlap/split patterns at the exact endpoint

`q=2D+2`

and records a useful no-go: merely moving to adjacent chain cuts and reusing the forest
condition cannot contradict equality, because their selected graphs are edge-deleted
subforests of the equality tree.

## 2. FSB notation

For the selected `2D` C87 paired staircase diameters let

`S=sum_(X,k)(n_(X,k)-1)`

be the physical side-level split excess.

Let

`o in {0,1,2}`

count literal chain endpoints among `{z,a}` which occur in selected edges in **both**
side fibers, and let

`r0 in {0,1,2}`

count literal chain endpoints which occur somewhere in the selected paired graph at
all.  Then

`o<=r0`.

FSB gives for

`H_0=H_pair union {za}`

the exact nontrivial component count

`c_0=3+S-o-r0`.

For the complete C96 common-cut forest write

`m_r=2D+1+e_r`

and let `c_r` be its number of nontrivial components.  C96 gives

`q-(2D+2) >= e_r+(c_r-1)`.

## 3. Equality forces the selected graph to be the complete spanning tree

Assume

`q=2D+2`.

Then the nonnegative right side of the C96 inequality must vanish:

`e_r=0`,

`c_r=1`.

Therefore the complete common-cut graph has exactly the selected edges

`H_(tau_s)=H_0`,

has `2D+1` edges, and is one connected forest.  Hence it is a tree on exactly
`2D+2` diameter endpoints.

Since `H_0` itself is the complete graph at this cut,

`c_0=1`.

Substituting the FSB component formula gives the exact equality relation

### Theorem EQ1 — endpoint equality equation

If `q=2D+2`, then

`S+2=o+r0`.

In particular `r0>=1` and `S<=2`.

## 4. There are exactly four overlap/split patterns

Solve

`S+2=o+r0`,

subject to

`0<=o<=r0<=2`, `S>=0`.

The only possibilities are:

| case | `r0` | `o` | `S` | `c_pair=2+S-o` |
|---|---:|---:|---:|---:|
| A | 1 | 1 | 0 | 1 |
| B | 2 | 0 | 0 | 2 |
| C | 2 | 1 | 1 | 2 |
| D | 2 | 2 | 2 | 2 |

### Corollary EQ2 — complete equality classification

Every exact C96 endpoint configuration belongs to exactly one of A–D above.

Interpretation:

- **A:** exactly one literal chain endpoint appears, shared by the two side fibers;
  the paired graph itself is connected, and `za` attaches the absent literal endpoint
  as a leaf.
- **B:** both literal endpoints appear, neither is shared between side fibers, and
  there is no physical side-level split.  The paired graph has two components; `za`
  joins them.  This is the legal unsplit model emphasized by FSB.
- **C:** both literal endpoints appear, exactly one is shared, and exactly one unit of
  physical fiber splitting occurs.  Again `H_pair` has two components joined by
  `za`.
- **D:** both literal endpoints are shared and exactly two split units occur.  This is
  the special fully overlapped situation in which the naive doubled-lift theta picture
  becomes relevant; it is only one of four equality patterns and is not forced.

In B–D, FSB's forest condition says `z` and `a` lie in distinct components of
`H_pair`; the literal chain diameter is exactly the bridge which makes `H_0` connected.

## 5. Adjacent-cut forestness alone cannot eliminate equality

Let `N_j` be the exact chain-cut load from the mainline load-profile theorem.  The
selected graph on chain cut `tau_j` consists of

`2N_j`

of the paired staircase edges plus the literal chain diameter `za`, hence has

`2N_j+1`

edges.

At equality the common-cut selected graph `H_0` is a tree.  Every selected graph on
another chain cut is obtained from `H_0` simply by deleting those paired staircase
edges whose prefix interval does not contain `j`.  Therefore it is automatically a
forest.

### Theorem EQ3 — adjacent selected cuts are automatic subforests

At `q=2D+2`, the C90 forest condition applied only to the C87-selected diameter edges
on other chain cuts gives no new contradiction beyond C96.

The exact deficit

`2(D-N_j)`

is literally the number of selected paired edges deleted from the common-cut tree.
Thus the strict unimodality of `N_j` does not by itself force another split, cycle, or
endpoint.

This corrects a tempting but invalid continuation: one cannot argue that the two split
units of a fully overlapped abstract double cover must service all adjacent cuts,
because equality need not be in that overlap pattern at all, and in every pattern the
selected adjacent-cut graphs are already subforests.

## 6. What adjacent cuts can still contribute

The no-go is limited to the **selected** C87 edges.  The complete diameter graph across
`tau_j` may contain additional active diameter edges not present on the common cut.
Since it is a forest on at most `q=2D+2` endpoints, its total edge count is at most
`2D+1`.  Therefore a cut with selected load `2N_j+1` has room for at most

`2(D-N_j)`

additional crossing diameter edges if connected, and less if it has multiple
components.

A genuinely stronger multi-cut theorem must therefore prove a **lower** bound on these
additional cut-specific diameter edges, or use equal-length geometry/order to rule out
one of the four equality patterns.  Pure deletion bookkeeping cannot suffice.

## 7. Revised exact endpoint

The shortest exact equality attack is now one of:

1. rule out cases A–D geometrically using equal-length diameter chords and the strict
   thrackle order;
2. prove that some noncentral chain cut contains more than `2(D-N_j)` additional
   crossing active diameters;
3. show that one equality pattern forces forbidden reuse of a physical boundary
   source vertex, a unit-distance violation, or a positive KKT/reciprocal inconsistency.

No Level I closure is claimed.