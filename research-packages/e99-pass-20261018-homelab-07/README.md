# Smallest embedded two-grain rhombic disk

**Status:** unreviewed finite geometric regression. Level I and Target B remain
open. **Task:** `compute-b-two-grain-interface-regressions`. **Investigation:**
`frontier-compute-b-two-grain-interface-regressions-20261018`.

Contributor and originating AI: OpenAI Codex (GPT-6 Luna xhigh), producing the
geometry, exact enumeration and checker. No independent mathematical audit has
occurred. This package is new work under Apache-2.0 and uses no external text or
private source.

Research checkpoint: base `7d0a450fe66991036541023f95c44c064a04b6a8`, theorem
state `2026-10-15.publication.2`, priority `public-frontier.3`, catalogue
`public-frontier.9`. The existing handoff is Discussion #83 and the distinct
abstract inventory predecessor is PR #86. This result changes no state,
priority, lifecycle or theorem claim.

## Candidate lemma and downstream decision

In a simply connected finite tiling by equal-side rhombi from two fixed edge
directions, two nonempty retained one-cell grains with disjoint train labels
cannot be realized by a disk of at most two rhombi. Three rhombi suffice, and a
three-cell L patch can have exactly one physical deleted crossing and one
missing virtual crossing between the grains. In this smallest example the
actual-count shared-interface bound is exact, while adding virtual determinant
mass to that physical lower bound is false.

The exact physical quantity is

`R - G = 1 = I = |X_1| = |X_2|`,

where `R` is the number of physical rhombi/crossings, `G=2` is the sum of the
two internal one-cell grids, `I` is the actual physical crossing count between
the grains, and `X_j` counts physical crossings with exactly one endpoint in
grain `Q_j`. Separately, there is one virtual cross-grain train pair with
determinant area `12/13`. The ledger therefore has 3 physical crossings, 1
deleted physical interface crossing and 1 absent virtual crossing.

This changes the downstream question of whether the reviewed shared-interface
bound from the predecessor can be strengthened by appending virtual determinant
mass. The changed hypothesis is an actual embedded, triangle-free rhombic disk
with two disjoint retained train components; the predecessor's extremal
inventory was an abstract edge-state assignment. If the fixture failed to
saturate the physical formula, the discrepancy would identify a geometric
restriction to test. It instead saturates the formula and falsifies an
unqualified rule that also charges its virtual determinant pair. This is a
finite regression only; it supplies no virtual payment theorem for global
minimizers.

## Exact embedding

Use the rational unit vectors

`u=(1,0)` and `v=(5/13,12/13)`.

For integer coordinates `(i,j)`, map `(i,j)` to `i u + j v`. Keep the three
unit rhombi whose cell indices are `(0,0)`, `(1,0)` and `(0,1)`; omit `(1,1)`.
The union is a simply connected L-shaped disk. Its cell adjacency graph is a
tree, its boundary has 8 unit edges, and its cell complex has
`V-E+F=8-10+3=1`.

Both edge vectors have squared length 1. For any lattice difference `(m,n)`,

`|m u+n v|^2 = (13 m^2 + 13 n^2 + 10 m n)/13`.

If one coordinate is zero, a nonzero difference has squared length at least
1. If the coordinates have opposite signs, write `a=|m|`, `b=|n|`; then the
numerator is `13(a-b)^2+16ab >= 16`. If they have the same sign it is at least
36. Thus the shortest nonzero lattice distances are exactly the edge vectors
`+/-u,+/-v`; all other distances exceed 1. The acute angle has cosine `5/13`,
strictly between 0 and 1/2, and the rhombus diagonal squares are `16/13` and
`36/13`. All three faces are strict rhombi, the finite vertex set is
1-separated, and its unit-contact graph has no triangle.

The two `u`-trains are rows `A_0,A_1`; the two `v`-trains are columns
`B_0,B_1`. A physical crossing `A_j B_i` is exactly the present cell `(i,j)`.
The grains are

- `Q_1={A_0,B_1}`, with internal cell `(1,0)`;
- `Q_2={A_1,B_0}`, with internal cell `(0,1)`.

Delete the crossing between different retained components. The remaining
crossing graph has exactly the two stated components. The actual absent pair
`A_1 B_1` would occupy cell `(1,1)` and is virtual.

## Exact ledger

| Quantity | Exact value | Meaning |
| --- | ---: | --- |
| Potential train pairs | 4 | `A_j B_i`, `i,j in {0,1}` |
| Physical rhombi/crossings `R` | 3 | cells `(0,0),(1,0),(0,1)` |
| Internal grid crossings `G` | 2 | one in each retained grain |
| Actual physical interface `I` | 1 | crossing `A_0 B_0`, deleted between grains |
| `|X_1|, |X_2|` | `1,1` | each is the same deleted physical edge |
| Virtual cross-grain pairs | 1 | absent pair `A_1 B_1` |
| Deleted physical interface edges `e_del` | 1 | equals `I` in this fixture |
| Determinant per unlike-direction pair | `12/13` | `|det(u,v)|` |
| Physical rhombus area | `36/13` | `3 * 12/13` |
| Virtual determinant area | `12/13` | `1 * 12/13` |
| Total train-pair determinant area | `48/13` | `4 * 12/13` |

The two same-direction train pairs have determinant zero, so the four unlike-
direction pairs above exhaust the total determinant mass.

For the predecessor's actual-interface formula,

`G + max(I, |X_1|, |X_2|, |X_1|+|X_2|-I) = 2 + 1 = R`.

The upper-cap version also gives `G + max(1,1,2-1)=3`. The virtual pair is not
a physical edge, so `G+I+virtual_count=4 > R=3`. This is a counterexample to
adding this virtual determinant count directly to the physical crossing
lower bound, even in an actual embedded disk. The predecessor's formula itself
is saturated, not contradicted.

Each determinant unit is `12/13`; the same ledger in area units is: internal
physical `24/13`, deleted physical `12/13`, virtual `12/13`, total pair
determinant mass `48/13`. Thus physical rhombus area and virtual determinant
area remain distinct quantities.

## Minimality and falsification

Two rhombi in a connected two-direction tiling must share a full edge. They
then share a train, so they cannot be disjoint one-cell grains. If two rhombi
do not share an edge, their union is not a disk. A one-rhombus disk cannot
contain two nonempty grains. Therefore at least three physical rhombi are
needed. The three-cell L construction attains this lower bound and has a
nonzero virtual cross-grain pair.

`verify.py` exhausts all 15 nonempty subsets of a normalized 2-by-2 cell block,
checks cell connectivity and Euler characteristic, and searches every pair of
occupied cells with different row and column labels. It confirms that no
one- or two-cell disk realizes two disjoint one-cell grains with both a physical
and a virtual cross-grain pair; the minimum is 3 cells, with the L patches
having `(R,G,I,V)=(3,2,1,1)`. It independently checks all point distances,
unit contacts, triangles, rhombus diagonals, interface charges, determinant
areas and the exact shared-interface formulas using `Fraction` only.

The falsification controls are: remove the bridge cell and the patch is no
longer a connected disk; fill the missing corner and the virtual count becomes
zero; try either adjacent two-cell patch and its cells share a train; and mutate
the deleted edge or virtual edge classification and the exact ledger checks
fail.

Reproduce from the repository root with:

```sh
python research-packages/e99-pass-20261018-homelab-07/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-homelab-07 --check-only
```

The checker uses only the Python standard library and exact integer/rational
arithmetic. `RESULT.json` is the exact saved stdout of the verifier and is an
output fixture, not an undeclared checker input. The package metadata command
checks source pins and metadata; it does not execute the verifier. Required
repository-wide theorem-certificate replay is **deferred to the merging
agent**.

## Predecessors, live overlap and next lemma

The report in `docs/reports/target_b_interface_capacity_2026-10-17.md` already
proves the abstract shared-interface inventory formula and labels its edge
states as non-geometric. This package does not re-audit that inequality. It
adds an explicit rational rhombic-disk realization with exact physical,
deleted and virtual counts. The September PC1/PC3 report is credited for the
physical-versus-determinant distinction and its broader separator setting.

Live open PR #103 at `4b708e27e9e26f8c163685dfe8b033b6d6369177` proves a
complementary conditional analytic bound: if two final retained components
contain fixed linear-size train subsets in angle-separated arcs, then almost
all cross-pair determinant mass is virtual after paying only the initial
high-defect physical crossings. It does not construct a smallest embedded
disk or force those subsets from the shell hypotheses. The present fixture has
one-crossing grains and supplies the exact finite geometry; it fails PR #103's
macroscopic subset hypothesis and neither audits nor proves its analytic
statement.

The two grains here each contain one crossing only. They do not satisfy the
asymptotic Section-50 minimum-degree or the PC1 positive trim-depth hypotheses.
No `D`-scale, PC1/PC3 penetration, component extraction, shell endpoint,
global minimality, or source-uniform conclusion is established. The result
shows that virtual mass needs a geometric or topological payment mechanism; it
cannot be included as an extra physical crossing by bookkeeping alone.

**Open next question:** Can the canonical shell hypotheses force two final
Section-50 components to contain fixed `alpha D` and `beta D` direction subsets
with `|sin(phi_1-phi_2)|>2 epsilon`, as required by PR #103, and how does the
resulting `V_(A,B)` enter the canonical shell endpoint? The downstream
decision is whether the conditional cross-component determinant bound can
contribute to the Target B endpoint. The exact quantity is `V_(A,B)`; the
changed hypothesis is the existence of those macroscopic angle-separated
subsets, absent from the one-crossing fixture. If forced, PR #103 supplies a
positive quadratic virtual term after high-defect payment; if not, the route
must retain an aligned or sublinear-component branch. First step: prove or
obstruct that subset extraction from the actual Section-50/source hypotheses.
Blocker: the current finite model gives no source-uniform extraction or
transfer of `V_(A,B)` through the support-depth and topology terms.
