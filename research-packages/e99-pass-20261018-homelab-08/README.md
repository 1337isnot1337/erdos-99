# Geometric full-shore extension regression

**Status: unreviewed exact finite evidence.** This package geometrically realizes
an inherited full-shore restriction whose source-image overlap is larger than the
minimum for the restricted shores. It does not realize Section 168's zero-slack
capacity endpoint, so it is not a counterexample to Section 168 or the global
theorem.

Contributor: OpenAI Codex (GPT-6 Luna xhigh). Baseline: `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.9`.

## Question, hypotheses and route quantity

Section 168.2 gives separate saturating matchings from the full response shore
`X*` and the complete triangular-lattice shore `Y_in` into the zero-slack source
`A^0`. Does an arbitrary pair of these full-shore matchings retain the minimum
possible source-image overlap after restriction to `C^partial subset X*` and
`O subset Y_in`?

The exact finite test uses a unit-separated source set `A subset H`, a unit-separated
response shore `X`, a complete shifted triangular-lattice set
`Y_in=(Lambda+v) intersect int(K+B)`, and `K+B subset H`. It tests the two
incidence maps using strict distance `<1`, full-shore saturation, and one inherited
pair of full-shore matchings. The quantity affected downstream is the source-image
overlap used in the gate lower bound and, ultimately, the proposed source-specific
Schur deficiency. A positive inherited overlap can be used only if the selected
full-shore matchings are actually the ones used downstream.

## Exact local fixture

Use the triangular basis `e1=(1,0)`, `e2=(1/2,sqrt(3)/2)` and write coordinates
as pairs `(u,v)`. Squared Euclidean distance is exactly

`q(u,v)=u^2+uv+v^2`.

The response shore is `X={x}` with `x=(1/3,1/3)`. The full lattice shore inside
the open unit disk about `x` is exactly
`Y_in={(0,0),(1,0),(0,1)}`; each pair has squared distance `1`.

Five source labels are

| label | `(u,v)` |
| --- | --- |
| `a1` | `(-2/3, 1/2)` |
| `a2` | `(-1/3, 4/3)` |
| `a3` | `(-1/3, -2/3)` |
| `b` | `(1/2, -1/3)` |
| `c` | `(5/6, 1/2)` |

Add six hull labels `h_i=x+6d_i`, where
`d_i in {(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)}`. Their convex hull is a
regular hexagon `H` of circumradius `6` and inradius `3sqrt(3)`. Every source
label lies in `H`; the closed unit disk `K+B` about `x` lies in `H`. All eleven
source labels have pairwise squared distance at least `13/12>1` (the exact
minimum), so this finite `A` is unit-separated and has no unit-contact triangle.

Choose the full-shore matchings

* `M_X={(x,a1)}`;
* `M_Y={(y0,a1),(y1,b),(y2,c)}`, with `y0=(0,0)`, `y1=(1,0)`, `y2=(0,1)`.

They saturate the complete shores and the three `M_Y` segments are disjoint. For
`C={x}` and `O={y0}`, their inherited source images both equal `{a1}`, so the
inherited overlap is `1`. But `x-a2` and `y0-a3` are strict conflicts with distinct
source labels, so the restricted shores admit a joint assignment with overlap `0`.
The exact squared conflict distances are `31/36` for `x-a1`, `7/9` for `x-a2`,
`13/36` for `y0-a1`, `19/36` for each of `y1-b` and `y2-c`, and `7/9` for
`y0-a3`.
The checker also exhibits a different pair of full-shore matchings with no
`C`/`O` overlap; therefore this is a regression for arbitrary inherited choices,
not an obstruction to coordinating the choices.

## Source-capacity falsification and limitation

The fixture does **not** meet Section 168.2's essential condition
`|A^0|=alpha_1(H)`. The `5x5` Cartesian unit grid centered at `x` lies in `H`:
its points have squared radius at most `8`, while the inscribed-radius squared is
`27`. Thus `alpha_1(H)>=25>11=|A|`. The source-realization test reaches the
geometric incidence layer but fails the actual zero-slack capacity endpoint.

This gap is deliberate and explicit. There is no concrete coordinate fixture in
the Section 168 route itself; it states the source and response conditions
abstractly. No global optimum, plateau equality, maximum source packing, actual
Schur matrix, canonical `C^partial`/`O`, or source-specific rank inequality is
established here. The older PR #98 rational fixture is credited for its separate
matching-image regression. Open PR #102 owns the abstract Hall-overlap formula and
its full-shore extension countermodel; this package supplies a geometric local
realization and does not reprove that formula.

## Reproduction and controls

```sh
python -I -O -B research-packages/e99-pass-20261018-homelab-08/verify.py
```

The checker uses only `fractions.Fraction` and exact arithmetic. It enumerates all
lattice sites in the relevant bounded coordinate window, checks the full
incidence/matching conditions and segment intersections, confirms the strict
distance-one boundary is not an edge, rejects a duplicate-source matching, and
records the `25>11` capacity failure. The same run passes with optimized Python,
so its checks do not depend on `assert`.

## Open next question

Can the added hypothesis `|A^0|=alpha_1(H)` together with triangle-free global
optimality force a compatible choice of full-shore matchings, or can a
capacity-maximal source realize the same inherited restriction mismatch? Either
answer changes whether the gate/source-image estimate can be made from inherited
matching data or must use an explicit joint re-matching argument. First action:
construct an exact source-capacity endpoint with `K+B subset H`, then enumerate
all full-shore matching pairs and their restricted images. Stop if no such actual
endpoint is available; do not promote the present local fixture to Section 168.

## Attribution and lifecycle

This is a new Apache-2.0-compatible finite computation, based on the repository's
Apache-2.0 contribution policy. It relies only on the committed Section 168 route,
the PR #98 regression report, and the exact coordinates printed above. The cited
predecessor proofs and reports are not copied. OpenAI Codex (GPT-6 Luna xhigh)
selected the task, constructed the rational coordinates and checker, and wrote this
report. No independent agent audit has occurred. No theorem state, priority, or
canonical claim is changed.

**Required full theorem-certificate replay is deferred to the merging agent.**
