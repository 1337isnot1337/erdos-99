> Generated reading edition · [exact source](../../../docs/reports/target_c_oo_fixed_star_pair_concentration_2026-10-01.md) · source SHA-256 `aacce3e608f09dd92246abfdccb4b3db577bb85fefaec7e61bbf2d6a21ebcb44`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-12D8337E3508","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- fixed-star-pair concentration for quadratic outer-train crossings

Base main: aa872a0e2aa2b74a011e9a86b8083bc985a0bcb7.

Stacked dependency: 5dc33a249690b2e7cde50c5e88c129a3bfb3fcef
(\`target_c_phase_bin_star_multiplicity_2026-10-01.md\`).

Status: proof-only. C-II remains open.

Let the Section-90 inverse-phase core have phase shores $`A_*,B_*`$, with at most
$`C_TD`$ train vertices on each shore. Put

```math
C_K=\lfloor 4K\rfloor+2.
```

The stacked narrow-bin theorem says that all single-star two-sided Section-157 braces
on either shore use at most $`C_K`$ diameter vertices. It also says that two retained
Section-90 trains which cross in a strict rhombus cannot be single-star braced by the
same diameter vertex.

Retain only Section-90 train vertices whose containing complete stopped train is
global outer-to-outer, then identify local vertices belonging to the same complete
train. Two complete trains cross in at most one strict rhombus, so this quotient does
not merge retained crossing edges. Write the resulting simple bipartite graph as

```math
G_{OO}=(A_{OO},B_{OO},E_{OO}),
\qquad
|A_{OO}|,|B_{OO}|\le C_TD.
\tag{1}
```

Call an outer-to-outer train split-star if no one diameter vertex carries both
opposite-sign Section-157 witnesses. Otherwise call it single-star and choose one such
diameter vertex as its assigned bracing star. Let $`s_A,s_B`$ count split-star trains
on the two shores.

## Theorem -- split or fixed star pair

Assume that for some fixed $`\xi>0`$,

```math
|E_{OO}|\ge \xi D^2.
\tag{2}
```

Then at least one of the following holds.

1. One phase shore contains at least
```math
\boxed{\frac{\xi}{4C_T}D}
\tag{3}
```
split-star outer-to-outer trains.

2. There are distinct diameter vertices $`v\ne w`$, a subfamily $`A_v\subseteq A_{OO}`$
all single-star braced by $`v`$, and a subfamily $`B_w\subseteq B_{OO}`$ all
single-star braced by $`w`$, such that
```math
\boxed{
e(A_v,B_w)\ge\frac{\xi}{2C_K^2}D^2
}
\tag{4}
```
and
```math
\boxed{
|A_v|,|B_w|\ge\frac{\xi}{2C_K^2C_T}D.
}
\tag{5}
```

Every edge in (4) is an actual retained strict-rhombus crossing.

### Proof

Assume alternative 1 fails. Then

```math
s_A+s_B<\frac{\xi}{2C_T}D.
\tag{6}
```

Deleting every split-star vertex removes at most

```math
C_TD(s_A+s_B)<\frac{\xi}{2}D^2
\tag{7}
```

edges, since the opposite shore has at most $`C_TD`$ vertices. Thus more than
$`\xi D^2/2`$ edges remain between single-star trains.

The stacked narrow-bin theorem gives at most $`C_K`$ assigned bracing stars on each
shore. Hence the remaining edges are partitioned among at most $`C_K^2`$ ordered star
pairs. One pair $`(v,w)`$ carries at least $`\xi D^2/(2C_K^2)`$ edges, proving (4).

Every such edge is an actual Section-90 train crossing. The stacked crossing-direction
theorem says two crossing trains cannot be single-star braced by the same diameter
vertex, so $`v\ne w`$.

Finally, simplicity and (1) give

```math
e(A_v,B_w)\le |A_v|C_TD,
\qquad
e(A_v,B_w)\le C_TD|B_w|,
```

which with (4) proves (5).

## Corollary -- near-complete outer-to-outer phase shores

The full Section-90 core has at least $`\kappa^2D^2`$ retained crossing edges. If only
$`o(D)`$ Section-90 train vertices on each shore fail to belong to global
outer-to-outer complete trains, deleting them removes only $`o(D^2)`$ edges, and the
global-train quotient loses no further edges. Hence

```math
|E_{OO}|\ge\kappa^2D^2-o(D^2).
```

For all sufficiently large $`D`$, applying the theorem with
$`\xi=\kappa^2/2`$ gives either

```math
\max(s_A,s_B)\ge\frac{\kappa^2}{8C_T}D
\tag{8}
```

or fixed distinct diameter vertices $`v,w`$ with

```math
e(A_v,B_w)\ge\frac{\kappa^2}{4C_K^2}D^2,
\qquad
|A_v|,|B_w|\ge\frac{\kappa^2}{4C_K^2C_T}D.
\tag{9}
```

Thus a quadratic outer-to-outer part of the inverse-phase core cannot be supported by
a diffuse collection of ordinary single-star braces. It either creates a linear
split-star population or collapses to one fixed pair of diameter stars supporting
linear train families with quadratic actual crossing incidence.

This report does not prove that the Section-90 core has quadratic outer-to-outer
crossing mass. That is now the immediate missing transfer. In the fixed-pair branch,
the next geometric target is a subquadratic crossing bound for two linear inverse-phase
train families braced by fixed distinct diameter stars. In the split branch, the target
is a multiplicity bound for split-star Section-157 witnesses.

No computation, verifier, numerical experiment, or CI result is used.
