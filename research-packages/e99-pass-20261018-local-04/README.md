# Two coupled rhombi with a diameter-setting contact isolate

**Classification:** unreviewed exact finite regression. No claim is promoted.
**Investigation:** `frontier-target-c-face-coupled-move-20261018` (producer,
local-04). **Baseline:** `7d0a450fe66991036541023f95c44c064a04b6a8`.
**Authority:** state `2026-10-15.publication.2`, priority `public-frontier.3`,
catalogue `public-frontier.9`. Level I, A, B and C-II remain open; C-I remains
closed.

## Candidate question and downstream quantity

Can a common shear of a two-face unit-rhombus train give a strict improvement
in the Target C lexicographic endpoint quantity `(|C|, |H|)` while its full
source remains unit-separated and has diameter at most its original `D`?
Here `C` is the set of unit pairs and `H` is the set of actual distance-`D`
pairs. The source is the seven-point realization below; all seven labels are
retained, including its contact-isolated point. The result can screen this
specific motion family against the finite endpoint test in the canonical C-II
route. It cannot establish a canonical-source implication.

The six face labels are

```text
v_(i,j) = i a + j b(c),   i=0,1,2; j=0,1
a = (1,0),   b(c) = (c, sqrt(1-c^2))
```

They form two adjacent parallelogram faces sharing the middle unit edge. At
`c=0` both are unit squares. The seventh label is the fixed contact isolate
`z=(1,11/5)`. At the source `c=0`, the full-source diameter is
`D^2=146/25`; its two actual diameter pairs join `z` to `v_(0,0)` and
`v_(2,0)`. The unit-contact graph is the two-cell grid, with seven edges and
no triangle.

## Exact result

For the complete common-shear family with `c` in `[-1,1]`, all source pairs
satisfy the original lower bound and the upper bound `D` exactly when
`|c| <= 21/100`. On the open interval `|c| < 21/100`, all seven unit contacts
and both actual diameter pairs persist, so `(|C|,|H|)=(7,2)` is unchanged.
At either boundary, one cross-row pair becomes a third actual diameter pair.
Outside the interval, that pair exceeds `D`. Thus this full-source face motion
has no strict sub-`D` or lexicographic endpoint in this fixture; the isolate
sets a sharp cap on the shear.

The largest cross-row squared distance is
`max_{k=±2}(5+2kc)=5+4|c|`. Since `D^2=146/25=5+21/25`, it reaches `D^2`
exactly at `|c|=21/100` and exceeds it for every larger `|c|`.

An explicit interior finite move is `c=-1/5`, for which
`b=(-1/5, sqrt(24)/5)`. It preserves all 21 lower and upper pair constraints,
keeps the contact graph triangle-free, and leaves `D`, `|C|`, and `|H|`
unchanged. The boundary `c=-21/100` is the exact activation control: the new
cross-row squared distance is `146/25`, increasing `|H|` from 2 to 3.

### Complete pair ledger

There are 21 unordered pairs among the seven retained labels:

| Pair class | Count | Exact squared distance or bound for `|c| <= 21/100` | Lower/upper disposition |
| --- | ---: | --- | --- |
| Same row, adjacent indices | 4 | `1` | old unit contacts |
| Same row, indices two apart | 2 | `4` | strictly between `1` and `D^2` |
| Different rows, equal index | 3 | `1` | old unit contacts |
| Different rows, index difference `k=±1` | 4 | `2+2kc`, in `[79/50,121/50]` | strict lower and upper slack |
| Different rows, index difference `k=±2` | 2 | `5+2kc`, in `[104/25,146/25]` | strict lower; upper tight only at one boundary pair |
| `z` to bottom row `v_(i,0)` | 3 | `121/25` for `i=1`; `146/25` for `i=0,2` | one strict pair and the two fixed diameter pairs |
| `z` to top row `v_(i,1)` | 3 | exact expression below; uniformly in `[36/25,2977/1000)` | strict lower and upper slack |
| **Total** | **21** |  | **all pairs included** |

For the last row, writing `s=sqrt(1-c^2)`,

```text
|z-v_(i,1)|^2 = (1-i-c)^2 + 146/25 - c^2 - (22/5)s.
```

The interval follows from `s>97/100`, `s<=1`,
`|1-i-c|<=121/100`, and `11/5-s` in `[6/5,123/100)`. In particular,
`2977/1000 < 146/25`. These bounds check every isolate-to-face pair, not only
the old active diameter pairs.

The verifier prints the 21 individual source-pair rows at `c=0` and checks the
uniform family bounds using rational arithmetic. At `c=-1/5`, the two
`k=±2` cross-row distances squared are `21/5` and `29/5`; both remain below
`146/25`. At `c=-21/100`, they are `104/25` and `146/25`.

## Hypotheses, falsification and stop condition

- **Hypotheses:** exactly the seven coordinates above; a common rotation of
  the train vector `b`; fixed horizontal vector `a`; fixed isolate `z`; and
  the full-source constraints `1 <= |p-q| <= D` for every distinct pair.
- **Falsification test:** enumerate every unordered pair and compare exact
  squared-distance formulas. Check all lower bounds, all old and newly active
  upper bounds, the contact graph, triangle count, diameter and actual diameter
  pair count at `c=0`, `c=-1/5`, and `c=±21/100`. The verifier also includes an
  invalid-shear control at `c=-1/4` and a unit-triangle control at `c=-1/2`.
- **Stop condition:** stop after the exact admissible interval and endpoint
  counts are established. Do not generalize this one-parameter obstruction
  to other source geometry or motion modes.

This is a finite exact regression, not a global-minimizer example. It does not
reconstruct the historical quarter-fold or through-splicing arguments, prove
that a canonical source contains this pattern, or rule out moving `z`, other
face/train motions, source replacements, or the separate macroscopic branch.
It says nothing about uniformity in cardinality.

## Predecessor comparison and next lemma

The train-return track already warns that an unspecified geometric train shear
does not check intersections, outside pairs, diameter uppers, or isolates.
The nearby finite rhombus and quarter-fold records study different wall or fold
hypotheses. This package supplies a concrete two-face realization, keeps an
explicit contact isolate in the seven-label source, and completes the 21-pair
lower/upper ledger for one common shear. It does not audit those predecessor
proofs. Open PR #102 concerns a Target A source-incidence Hall formula and is
mathematically separate.

**Open next question:** for the canonical full-core C-II source, can a
nonzero face-coupled motion transport a diameter-setting contact isolate
alongside its face/train component while preserving every old contact lower
bound and every actual or previously inactive upper pair? The affected
quantity is `(|C|,|H|)` at `D`. The changed hypothesis is that the isolate may
move with the train rather than remain fixed. Either a verified motion would
give a full-source candidate for the existing lexicographic endpoint proof,
or an exact obstruction would identify an owner/upper-pair condition that the
source extraction must avoid. First action: form the finite displacement
constraints for the moving isolate and two-face train together. The remaining
blocker is deriving such a compatible component and motion from every
canonical source.

## Reproduction and provenance

Run from the repository root:

```sh
python research-packages/e99-pass-20261018-local-04/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-local-04 --check-only
```

The verifier uses only Python's standard library and exact rational arithmetic;
the square-root coordinate is bounded with rational inequalities. No external
literature or private repository dependency is used. The mathematical setup,
derivation, verifier and report were prepared by OpenAI Codex (GPT-6 Luna
xhigh) under the project owner's coordinated assignment. Independent AI
mathematical review remains pending. Required repository-wide certificate
replay is deferred to the merging agent if required by the final impact plan.

Executed with Python 3.14.8: the verifier exited 0, enumerated all 21 source
pairs, checked the shear interval and both falsification controls. The package
metadata check reported `metadata-valid`, no unresolved package inputs, and no
executed isolated replay; metadata validation is not mathematical approval.

Apache-2.0-compatible contribution. No predecessor text or code was copied.
