# Geometric obstruction to equality for inherited full-shore overlap

**Classification: unreviewed finite geometric regression.** This does not establish a new canonical claim or a Section-168 source transfer.

Contributor: OpenAI Codex (GPT-6 Luna xhigh), AI-assisted proof and checker. New material is offered under Apache-2.0. The predecessor evidence is credited below.

Baseline: `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.9`.

## Question, hypotheses, and downstream quantity

PR #102 proves that the minimum common-image size over independently chosen matchings of restricted shores `C,O` equals their combined Hall deficiency

`delta_A(C,O) = |C| + |O| - nu_A(C sqcup O)`.

Its actual-source corollary only needs the lower bound for restrictions of two full-shore matchings. The distinct question tested here is whether local Euclidean structure forces those inherited restrictions to attain `delta_A`: take a unit-separated source `A`, unit-separated full shores `X,Y`, a strict-conflict saturating matching of each full shore into `A`, and require `Y` to lie in one unit triangular lattice. For `C subset X` and `O subset Y`, must the two restricted images intersect in exactly `delta_A(C,O)`?

The exact finite fixture below answers **no**. It realizes PR #102's abstract full-shore extension obstruction with strict Euclidean conflicts, noncrossing full matchings, and a lattice shore. The quantity it controls is the overlap of these particular full-shore matching restrictions, hence the number of source V-gates available before the Section-177.5B interference loss. It does not strengthen or invalidate PR #102's lower bound `G_CO >= ceil(delta_A/10)`.

### Candidate and falsification plan

- **Candidate statement:** under unit separation of `A,X,Y`, strict Euclidean conflict matchings saturating `X,Y`, and `Y` lying in a unit triangular lattice, the inherited restricted overlap might always equal `delta_A(C,O)`.
- **Changed decision / quantity:** equality would let the actual full-shore restrictions attain the Hall-optimal common-source count; the exact quantity is `|im(M_X|C) intersect im(M_Y|O)|`, which feeds the Section-177 gate count `G_CO`.
- **Falsification:** compute every exact source-target squared distance and enumerate all full-shore and restricted-shore matchings in a rational two-by-two fixture. A counterexample with unique full matchings stops the local-equality search.
- **Stop condition:** stop if local geometry falsifies equality; continue only by adding the actual Section-168 global-capacity, plateau, and collar hypotheses. Do not treat another abstract incidence graph as progress.

## Exact fixture

Use the strict-conflict rule `p~a iff |p-a|<1` and the following rational coordinates:

| Label | Coordinate |
| --- | --- |
| `a` | `(-3/4, 1/4)` |
| `b` | `(1/2, 3/4)` |
| `c` | `(-1/8, 5/8)` |
| `u` | `(5/4, 3/4)` |
| `o` | `(0, 0)` |
| `v` | `(1, 0)` |

Let `A={a,b}`, full shores `X={c,u}` and `Y={o,v}`, and restricted shores `C={c}`, `O={o}`. The set `Y` is a pair of points in the standard unit triangular lattice, since `v-o=(1,0)`. Both source labels are retained; they are contact-isolated within `A` because `|a-b|>1`.

Exact squared-distance enumeration gives

| Target | Strict source neighborhood |
| --- | --- |
| `c` | `{a,b}` |
| `u` | `{b}` |
| `o` | `{a,b}` |
| `v` | `{b}` |

All three sets are unit-separated:

`|a-b|^2 = 29/16 > 1`, `|c-u|^2 = 61/32 > 1`, and `|o-v|^2 = 1`.

Therefore the full-shore matchings are unique:

`M_X={(c,a),(u,b)}`, `M_Y={(o,a),(v,b)}`.

Their straight segments are disjoint within each matching (the `X`-matching segments have disjoint x-projections, as do the `Y`-matching segments). Restricting them gives `im(M_X|C)=im(M_Y|O)={a}`, so the inherited overlap is one.

But in the restricted combined graph both `c` and `o` are adjacent to both `a` and `b`. Thus `nu_A(C sqcup O)=2` and `delta_A(C,O)=1+1-2=0`. The inherited overlap is strictly greater than the restricted-shore Hall defect.

The standalone verifier reconstructs every squared-distance row, checks both shore matchings and their uniqueness, checks the exact Hall value, and checks that the unrestricted restricted-shore optimum is zero. No floating-point arithmetic is used.

## Scope boundary and predecessor comparison

This is a geometric realization of the two-source abstract extension control in open PR #102 (`025628b23df11470d4eb87ee981edbf250498691`). It is distinct from PR #98's five-source rational fixture: here both restricted shores have zero combined Hall defect, but the unique full-shore extensions force a shared image. The two full matchings are genuinely noncrossing geometric matchings, and one target shore is a triangular-lattice subset.

The fixture is deliberately only a local obstruction. Its source is not asserted to be a global diameter minimizer or maximum packing of a fixed hull. `X` is not a plateau-endpoint optimum; `Y` is only the displayed finite lattice shore, not the complete Section-168 `Y_in`; there is no `K^*+B subset H`, source cell complex, Schur matrix, contact shield, or diameter endpoint. Thus this falsifies an equality upgrade based only on local unit-separation, noncrossing, and lattice geometry. It does not falsify a coupling theorem using the actual Section-168 global-capacity and plateau hypotheses.

In particular, all actual Section-168 inferences remain as stated: the full-shore restrictions obey the PR #102 lower bound, Theorem 177.5B converts a proved common-source lower bound to disjoint gates with its factor-ten loss, and no gate count alone proves a Schur-rank bound. Level I, Target A, and the zero-slack global branch remain open.

## Reproduction

From the repository root:

```sh
python research-packages/e99-pass-20261018-homelab-01/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-homelab-01 --check-only
```

The checker uses only Python 3.14 standard-library exact fractions. Repository public-integrity and local-impact checks are recorded in the PR body. Required repository-wide theorem-certificate replay is **deferred to the merging agent**; it was not run here.

## Open next question

The downstream decision is whether actual Section-168 full-shore restrictions force a source-gate count strictly above `ceil(delta_A(C,O)/10)`, or whether the Hall lower bound is sharp after imposing the source-capacity endpoint, `K^*+B subset H`, the complete co-phased `Y_in`, and the plateau optimum. Either result changes only the available gate currency `G_CO`; translating that currency into the exact Schur demand `s=Delta_Lambda-d_int` still needs the shield/tube accounting of Sections 175–177.

The next useful result must add and explicitly use those global hypotheses. A real exact-source counterexample there would show the incidence Hall floor is the best source-gate input; a uniform positive surplus would strengthen the Section-177 route. The blocker is that this bounded fixture has no verified global source/response realization. Stop this local line here rather than treating another arbitrary incidence pattern as progress.
