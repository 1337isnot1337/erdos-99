# Independent audit: embedded two-grain rhombic disk

## Scope and candidate lemma

This audit checks PR #131 at `35c3bdb387c714e8a4f51f48e13a6b684cea7151`,
against base `7d0a450fe66991036541023f95c44c064a04b6a8` and theorem state
`2026-10-15.publication.2` / priority `public-frontier.3` / catalogue
`public-frontier.9`.

Assigned investigation: `audit-pr131-embedded-interface-macbook-20261019`;
role: reviewer; exact scope key:
`92db1a46fe52765eb57d7db0188a8a264a911aa03e10165311191877615af3ec`.

**Candidate lemma.** In the normalized `2-by-2` cell box, let a nonempty
physical mask be edge-connected with Euler characteristic one. Choose two
physical crossing cells whose train endpoints are disjoint (the two cells are
diagonally opposite). If their two complementary cross-grain slots include
both a physical interface crossing and a missing virtual crossing, then the
mask has at least three cells. Equality is attained by each of the four
three-cell L masks. For the representative mask
`{(0,0),(1,0),(0,1)}`, the rational unit directions
`u=(1,0)` and `v=(5/13,12/13)` realize the disk as eight unit-separated points,
with exactly the ten rhombus-edge unit contacts and no unit triangle.

The affected quantity is the finite physical crossing count `R` in the shared
interface inequality. The equality case has `R=3`, `G=2`, and one shared
physical interface edge, so it saturates that inequality. Its other
cross-grain slot is virtual and has no physical rhombus; adding it as a free
charge would require an extra, absent payment. This audit makes no claim that
the physical interface inequality fails.

**Falsification test:** independently enumerate all 15 nonempty cell masks,
filter the disk masks, enumerate disjoint diagonal crossing choices, and check
the exact rational point metric, contact graph, triangle count, crossing
sets, inclusion-exclusion, and area ledger. Stop after those 15 masks; no wider
grid search is in scope.

## Reconstruction

The four possible `A_i`/`B_j` crossing slots are the cells of the box. Two
disjoint one-crossing grains occupy opposite slots. Their two remaining
cross-grain slots are the other diagonal. To have one of those two slots
physical and the other virtual, the physical mask must include exactly one
of them in addition to the two grain cells. Hence it has at least three
cells. That three-cell mask is an L disk, and its two grain cells, physical
interface cell, and missing virtual cell are distinct slots.

For the positive realization, `u dot v = 5/13` and
`abs(det(u,v)) = 12/13 > 0`. Thus the affine image of the L cell complex is an
embedded rhombic disk, with disjoint cell interiors. A lattice displacement
`(m,n)` has squared length
\[
q(m,n)=m^2+n^2+\frac{10}{13}mn.
\]
The eight vertices have coordinate differences in `[-2,2]^2`. Exact
enumeration gives `q>=1` for every nonzero realized difference; equality
occurs only for `(±1,0)` and `(0,±1)`. For completeness, the non-axis
classes with absolute coordinate pairs `(1,1)`, `(1,2)`, and `(2,2)` have
minimum squared lengths `16/13`, `45/13`, and `64/13`; the remaining
nonzero axis classes have squared length at least `4`. In this L mask those
unit pairs are exactly the ten tile edges. The contact graph is a subgraph of
the square lattice, which is bipartite, so it has no triangle. The L patch has
diameter squared `85/13`; the two rhombus diagonals have squared lengths
`16/13` and `36/13`.

The physical slots are `{(0,0),(0,1),(1,0)}`. The two grains are
`Q1={A0,B1}` and `Q2={A1,B0}`. Their internal physical crossings are `(0,1)`
and `(1,0)`. The only physical cross-grain crossing is `(0,0)`, so the two
penetration sets coincide there. Their other cross-grain slot `(1,1)` is
virtual. Therefore
\[
R=3,\quad G=2,\quad I=1,\quad |X_1|=|X_2|=1,
\]
and
\[
G+\max(I,|X_1|,|X_2|,|X_1|+|X_2|-I)=3=R.
\]
The overlap subtraction is necessary: `|X1|+|X2|=2` counts the same
physical interface twice, while `|X1 union X2|=1`. The separate virtual
slot cannot be added to `R` or to this right-hand side without another
payment.

Each rhombus has determinant area `12/13`. The internal, deleted-physical,
virtual, physical, and complete-potential area totals are respectively
`24/13`, `12/13`, `12/13`, `36/13`, and `48/13`.
Thus physical area is `internal + deleted`; complete potential area is
`physical + virtual`. Deleted and virtual slots are distinct and are never
both booked as physical area.

## Relationship to canonical hypotheses

Each selected grain has one internal crossing and two train vertices of
internal degree one. These two grains are chosen subsets of the finite ambient
train graph; the construction does not show Section-50 pruning extracts them
as retained components. The patch has the single finite diameter
`D=sqrt(85/13)`, not a sequence with `D` tending to infinity. Its bounded
internal degrees do not establish the Section-50 retained-core premise
`minimum degree >= lambda D` for sufficiently large `D`. It also has `M=b=1`;
PC1 requires integer trim
depths `k<M/2`, `l<b/2` and `d=min(k,l)-2>0`. No positive integer trim depth
is available when `M=b=1`. The finite example is therefore not an instance of
the macroscopic Section-50/positive-depth-PC1 chain. It does not establish
coherent-component extraction, positive PC1/PC3 mass, virtual-area payment,
global-minimizer transfer, or Target B/Level I closure.

The [independent dense-grid audit](../../docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md)
records the scoped PC1/PC3 results. PR #86 at
`a392a910899b06d20df6c7c29010896223ebfa70` received a PASS for its abstract
incidence theorem and conditional PC1/PC3 substitutions in
`docs/research/review-artifacts/merge-2026-10-18/review-b.txt`. That review
retains the geometric-realization, source-extraction, positive-gain,
virtual-area, and topology limits. This audit does not redo that proof; it
checks the exact finite specialization against the embedded geometry.

The separately open PR #103 at
`4b708e27e9e26f8c163685dfe8b033b6d6369177` gives a conditional macroscopic
two-component virtual-mass estimate when both components contain linear-size,
angle-separated train subsets. A one-crossing grain is outside that hypothesis.
Open PR #125 (Euler correction) and PR #128 (a different complete-grid phase
family) are adjacent Target B work; neither changes the declared 2-by-2 mask
domain or supplies a premise used here. PR #131 and these adjacent results
remain open; no state or priority revision changed at review time.

## Audit disposition and reproduction

**Disposition:** PASS for the stated finite lemma, L-patch realization, and
count/area ledger at the pinned PR #131 source. This is an independent
finite-model audit, not a canonical promotion. The enumerator and exact metric
checker in this package were written separately and do not import PR #131's
checker. The pinned candidate's own README/RESULT conclusions were inspected
after this reconstruction. The original author, code, and mathematical credit
remain with the PR #131 contributor; this audit is OpenAI Codex, GPT-6 Luna
xhigh assistance. Reviewer session: `macbook-16`, GPT-6 Luna xhigh, assigned
independently of the PR #131 producer. This new audit package is contributed
under Apache-2.0; it does not copy external text or code. Credit for the
original geometric construction and submitted checker remains with the PR #131
contributor. The package itself remains classified `unreviewed` pending normal
repository intake; no manifest claim or theorem state is changed.

Reviewed candidate: PR #131, commit
`35c3bdb387c714e8a4f51f48e13a6b684cea7151`, tree
`04c670dedd832140193321e8baba880924be750a`. Exact SHA-256 pins for the six
reviewed files:

| File | SHA-256 |
| --- | --- |
| `research-packages/e99-pass-20261018-homelab-07/README.md` | `8bc5ce9150074a1f7c5fad6199091ad3c3f7f92adf781829ef92b279042c2b96` |
| `research-packages/e99-pass-20261018-homelab-07/RESULT.json` | `5f6def57e6c50bb7a6f57ea5f6425e6f7cdd5e9bbe05c4f2ad64749a0d63c7cc` |
| `research-packages/e99-pass-20261018-homelab-07/SOURCES.json` | `af4599c25d20541c0a81934f01984bbc2f806c9a83131e08c5cb5a7290c6f553` |
| `research-packages/e99-pass-20261018-homelab-07/TASK.json` | `c0161edbc1e640d97936747b8d34ef610bbb42b40ef3dbb34815914d39013d3f` |
| `research-packages/e99-pass-20261018-homelab-07/VERIFY.json` | `b26e34b83fafefbe58cbf7bf82b5515b99e23827fcf46c82d5959f2578be95fe` |
| `research-packages/e99-pass-20261018-homelab-07/verify.py` | `9c69b11f0772e06ca5d5eb995dca1e74aaa2b026a43f4df23c80e35359a347c3` |

Run:

```sh
python research-packages/e99-macbook-20261019T054318Z-16/verify.py
python -O research-packages/e99-macbook-20261019T054318Z-16/verify.py
```

Both commands were run with CPython 3.12.3 and produced byte-identical output;
the normal output is recorded in `RESULT.json`. The pinned PR #131 verifier was
also materialized from its exact source commit, hash-checked, and replayed; its
output matched its pinned `RESULT.json`. These direct replays use only Python's
standard library and exact integers/rationals. `VERIFY.json` declares Python
3.14 for the optional isolated package protocol; that sandbox replay remains a
separate validation obligation if the host backend supports it.

`python scripts/research_package.py --package
research-packages/e99-macbook-20261019T054318Z-16 --check-only` returned
`metadata-valid`, with no unresolved metadata fields. This is a metadata/source
check and is not the mathematical replay.

The bounded proof says nothing about larger boxes or canonical source
extraction. Level I, Target B, and C-II remain open; C-I remains closed.

## Open next question

The downstream Target B decision is whether multiple retained components in a
canonical source can force a positive net payment after physical crossings,
deleted interfaces, and virtual determinant mass are all accounted for. This
fixture changes only the number of physical cells in a one-crossing grain
(`R=3`) and does not alter the canonical `G+E` endpoint. A useful next step is
to prove, or refute under exact canonical hypotheses, a uniform macroscopic
extraction statement that gives each retained component `M,b >= cD` and
positive trim depth; either outcome determines whether PC1 can enter the
multi-grain ledger. The obstacle is source realization and payment of virtual
mass with all retained components and interfaces present.
