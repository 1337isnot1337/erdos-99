> Generated reading edition · [exact source](../../../docs/audits/target_a_pr120_pr121_geometric_full_shores_audit_2026-10-19.md) · source SHA-256 `9d53529b58cec2e01c376531a28fa5a90059ecab100302990e5de62737ca4a84`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-8B174A3EC107","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Independent audit of PR #120 and PR #121 full-shore regressions

**Disposition:** PASS for the two stated finite local countermodels, with the
capacity and matching-choice limits below. This audit makes no canonical claim.

Reviewed exact heads: PR #120 `c3718cde305ec74b6dae380292b0bc646cee8f20` and
PR #121 `7f4dac815680da2b8ad6b0623369aeab3a730978`, both based on
`7d0a450fe66991036541023f95c44c064a04b6a8`. The applicable state is
`2026-10-15.publication.2`, priority `public-frontier.3`, catalogue
`public-frontier.9`. Live GitHub showed both PRs open as drafts at those heads
with no submitted reviews; PR #102 remains open at
`025628b23df11470d4eb87ee981edbf250498691`.

## Question and exact scope

Test the proposed local implication that restrictions of two chosen saturating
full-shore matchings always attain the minimum possible common source-image
size. For `C subset X`, `O subset Y`, write

`I = im(M_X restricted to C) intersect im(M_Y restricted to O)`,
`nu = nu_A(C disjoint-union O)`, and `delta_A(C,O)=|C|+|O|-nu`.

The changed quantity is `|I|`, the inherited overlap available to the Target A
source-gate count. PR #102 supplies the abstract Hall comparison; this audit
uses its stated `delta_A` as a benchmark and does not reprove that result. The
falsification check is exact enumeration of strict Euclidean incidences,
saturating matchings, segment intersections, and the capacity/extraction
controls at the pinned heads. Stop after these local countermodels; a further
search is useful only with an actual Section-168 zero-slack source and its
plateau response hypotheses.

The investigation read both producer-authored packages and the homelab
producer handoffs before reconstruction. Those handoffs contain producer
claims, not an independent audit. I reconstructed the coordinates and matching
counts before checking live PR review state; neither exact PR had a submitted
review. The Section-168 route and the separate PR #98 matching-image report
were read as context. No PR #102 proof reconstruction was performed.

## PR #120: the unique full matchings force overlap one

The source is `A={a,b}` with `a=(-3/4,1/4)`, `b=(1/2,3/4)`; the full shores
are `X={c,u}`, `Y={o,v}`, with `c=(-1/8,5/8)`, `u=(5/4,3/4)`, `o=(0,0)`,
`v=(1,0)`. The restricted shores are `C={c}`, `O={o}`. The adjacency rule is
strict: a target and source are adjacent exactly when their squared Euclidean
distance is `<1`.

Exact squared distances give

| Target | `|t-a|^2` | `|t-b|^2` | Strict source neighborhood |
| --- | ---: | ---: | --- |
| `c` | `17/32` | `13/32` | `{a,b}` |
| `u` | `17/4` | `9/16` | `{b}` |
| `o` | `5/8` | `13/16` | `{a,b}` |
| `v` | `25/8` | `13/16` | `{b}` |

The source pair has squared distance `29/16>1`; the `X` pair has squared
distance `61/32>1`; and `|o-v|^2=1`. Thus each shore is unit-separated, and
`Y` is a two-point subset of the standard triangular lattice. Since `u` has
only neighbor `b`, the only matching saturating `X` is
`{c-a,u-b}`. Since `v` has only neighbor `b`, the only matching saturating
`Y` is `{o-a,v-b}`. Their segments are disjoint within each matching: the
respective endpoint x-intervals are `[-3/4,-1/8]` and `[1/2,5/4]`, then
`[-3/4,0]` and `[1/2,1]`.

Both restricted targets have neighborhood `{a,b}`, so `nu=2` and
`delta_A(C,O)=0`. The unique inherited restrictions both use `a`, giving
`|I|=1`. The free restricted assignment `c-a, o-b` is injective, so the
minimum possible overlap is zero. This disproves the local equality upgrade
even when the full matchings are unique and individually noncrossing.

This shore `Y` is only the displayed lattice pair; it is not a complete
`Y_in`. There is also a capacity nuance. If one sets the canonical hull to
`H=conv(A)`, then `H` is a segment of length `sqrt(29)/4<2`. It fits at most
two unit-separated points, and `A` attains two, so in this degenerate hull the
raw equality `|A|=alpha_1(H)=2` actually holds. It would be inaccurate to say
the coordinates violate that cardinality equality. But `K=conv(X)` has
`K+B` with nonempty interior, which cannot lie in the segment `H`; and this
`A` is not a global optimum for `n=2` because its diameter exceeds `1`.
Therefore this is not a Section-168 source/response realization, despite the
incidental raw capacity equality.

## PR #121: complete `Y_in`, nonunique full matchings, explicit capacity gap

Use the triangular basis `e1=(1,0)`, `e2=(1/2,sqrt(3)/2)` and
`q(u,v)=u^2+uv+v^2`. The response shore is `X={x}` with `x=(1/3,1/3)`;
`K={x}`. The lattice sites strictly inside the unit disk around `x` are
exactly `Y_in={(0,0),(1,0),(0,1)}`. To see completeness, for
`r=u-1/3`, `s=v-1/3`,

`q(r,s) >= (3/4)r^2` and `q(r,s) >= (3/4)s^2`.

Thus `q<1` forces each integer coordinate `u,v` to be `0` or `1`; the four
candidate squared radii are `1/3,1/3,1/3,4/3`, so only the three stated sites
belong to the open disk. Their pairwise squared distances are all `1`, which
is allowed by unit separation. The strict bipartite conflict rule remains
`q<1`.

The five local source coordinates are
`a1=(-2/3,1/2)`, `a2=(-1/3,4/3)`, `a3=(-1/3,-2/3)`,
`b=(1/2,-1/3)`, `c=(5/6,1/2)`. Add the six stated radius-6 hexagon vertices
`h_i=x+6d_i`, with `d_i` the six unit triangular directions. Exact pair
enumeration gives minimum source squared distance `13/12>1`; hence all eleven
source labels are retained and the source has no unit-contact triangle. The
largest squared radius of a local source about `x` is `19/9`, below the
hexagon's squared inradius `27`. The hexagon `H=conv(A)` has inradius
`3sqrt(3)`, so the closed unit disk `K+B` lies in `H`.

The exact strict neighborhoods in the full source are

| Target | Strict source neighborhood |
| --- | --- |
| `x` | `{a1,a2,b,c}` |
| `y0=(0,0)` | `{a1,a3,b}` |
| `y1=(1,0)` | `{b,c}` |
| `y2=(0,1)` | `{a2,c}` |

The six hull labels are outside these rows: each `y_i` is within distance
`1/sqrt(3)` of `x`, while each `h_i` is distance `6` from `x`. Enumerating
injective assignments from these rows gives four full `X` matchings and seven
full `Y_in` matchings. Thus the selected matchings are valid but not unique.
For the displayed choice `x-a1` and
`{y0-a1,y1-b,y2-c}`, the strict squared edge lengths are respectively
`31/36`, `13/36`, `19/36`, `19/36`. The three `Y_in` segments are pairwise
disjoint by exact orientation tests in triangular coordinates; the invertible
basis change preserves intersections. `X` has one segment, so its matching's
pairwise-disjointness condition is vacuous. Disjointness is per matching: the
two displayed matchings share source `a1` by design.

For `C={x}`, `O={y0}`, the inherited overlap is one. Yet `x-a2` and `y0-a3`
are strict edges to distinct source labels, giving `nu=2` and
`delta_A(C,O)=0`. In fact the full-shore choices
`x-a2` and `{y0-a3,y1-b,y2-c}` are both valid and remove the restricted
overlap. PR #121 therefore refutes equality for the displayed inherited pair,
but not a stronger assertion that every coordinated choice of full matchings
must overlap.

The stated source-capacity failure is real: `|A|=11`, while a 5-by-5
Cartesian unit grid gives 25 unit-separated points in `H`, so
`alpha_1(H)>=25>11`. The pinned checker has a small center-coordinate gap: it
constructs grid points `(i,j)` about the Cartesian origin, then compares
their origin radii with the inradius of a hexagon centered at `x`; its comment
calls the grid x-centered. The conclusion is still correct for the code's
actual grid. In physical coordinates `x=(1/2,sqrt(3)/6)`, so
`|x|=1/sqrt(3)`. Every grid point has `|g|<=sqrt(8)`, hence
`|g-x|<=sqrt(8)+1/sqrt(3)<4<3sqrt(3)`, where the last inequality follows
from `16<27`. Thus all 25 points lie in `H`. Equivalently, an explicitly
x-centered grid has radius at most `sqrt(8)`. This repairs the omitted
center-distance step without changing the capacity result.

## Combined finding and remaining lemma

Both fixtures falsify the local assertion that an arbitrary pair of inherited
full-shore matchings must attain the restricted Hall-optimal overlap. PR #120
forces its bad overlap because both full matchings are unique. PR #121 includes
the complete three-site `Y_in` and a containing hull, but its matching choices
are flexible and the selected mismatch can be removed by coordination. Neither
fixture challenges the PR #102 Hall lower bound, which allows `delta=0` here.

They also fail to instantiate Section 168 in different ways. PR #120's raw
maximum-packing equality happens in a degenerate segment hull, but `K+B` cannot
fit there, its source is not globally optimal, and its lattice shore is not
the complete `Y_in`. PR #121 has the full local `Y_in` and `K+B subset H`, but
its source falls short of `alpha_1(H)` by at least fourteen points and is not
identified as a triangle-free global minimizer or an actual plateau endpoint.
Neither gives canonical `C^partial`/`O`, a source-specific Schur matrix, or a
global source-capacity extraction.

The remaining lemma is: under the actual Section-168 hypotheses—triangle-free
global source `A^0` with `|A^0|=alpha_1(H)`, the plateau response `X^*`,
`K^*+B subset H`, and the complete co-phased `Y_in`—determine whether a
coordinated choice of full-shore matchings always has Hall-optimal restrictions,
or construct a capacity-maximal global source where the mismatch persists.
Then translate the resulting actual source-gate count into the Section-177
Schur demand. These finite regressions alone do not select either outcome.

## Reproduction and provenance

The pinned source files were read from their exact Git objects and all ten
SHA-256 pins in the assignment manifest matched. The submitted verifiers and
an independent exact reconstruction are reproduced by:

```sh
python -I -B research/verify_pr120_pr121_full_shore_audit_2026_10_19.py
python -I /tmp/e99-120-verify.py
python -I /tmp/e99-121-verify.py
python -I -O -B /tmp/e99-121-verify.py
```

The `/tmp` copies were materialized directly with `git show` from the pinned
heads. PR #120's checker passed in normal mode; its checks use Python
`assert`, so an optimized-mode run would disable them and is not counted. PR
#121 passed normally and with `-O`, since it uses explicit checks. The
independent checker uses exact `Fraction` arithmetic for all coordinates,
distances, matching enumeration and segment intersections. It also checks the
capacity facts above. The independent verifier was written by OpenAI Codex
(GPT-6 Luna xhigh) for this audit; there was no shared checker code with either
producer package. All mathematical content is Apache-2.0 compatible under the
repository contribution policy. The source packages retain their original
credit to their producing OpenAI Codex (GPT-6 Luna xhigh) sessions.

No state, priority, manifest, or canonical claim was changed. Level I, A, B,
and C-II remain open; C-I remains closed. Required repository-wide theorem
certificate replay, if triggered by integration, is deferred to the merging
agent.
