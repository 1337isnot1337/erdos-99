> Generated reading edition · [exact source](../../../docs/audits/target_c_actual_diameter_cubic_replacement_cover_independent_audit_2026-10-08.md) · source SHA-256 `870358502878740817993c9f49136bbe2300cb80977ce1609d19fe53abbe5b56`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-ED164F0DFCE1","canonical":true,"claim_ids":["C-ACTUAL-DIAMETER-CUBIC-MOMENT","C-CORE-DIAMETER-REPLACEMENT-COVER-COST"],"claim_statuses":{"C-ACTUAL-DIAMETER-CUBIC-MOMENT":"canonical","C-CORE-DIAMETER-REPLACEMENT-COVER-COST":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: actual-diameter cubic moment and replacement cover cost

**Date:** 2026-10-08. **Audit base:** `origin/main=8b23081616e721556efa69f30c24a83917d67914`, state `2026-10-08.audit.173`. **Target:** C-II. C-II and Level I remain open.

## Frozen source and scope

The source is `origin/research/level-i-closure-20261007` at immutable tip
`12f6833725f281ce39a6d04ebcb45630b3a6768f`. This audit covers only Section 4 of
`docs/reports/target_c_isolate_normalization_core_diameter_replacement_2026-10-07.md`,
SHA-256 `c3e1baac507b2ad0e28e5de1d69c5eb8db619e21a4d9370b5103d08df615828e`.
The source report was introduced at `3457d175bafad554b71c442a3a3667b077025dcf`.
Sections 2–3 were separately audited and promoted in Audit.177; no later source
commit was imported into either audit.

The source verifier
`research/verify_target_c_inactive_diameter_cubic_moment_2026_10_04.py` was inspected
and rerun. It checks specified rational nonglobal examples, algebraic samples, and
finite graph cover/matching reductions. It does not certify the analytic limiting
argument or global optimality.

## Verdict

- **PASS — promote `C-ACTUAL-DIAMETER-CUBIC-MOMENT`.** The canonical finite
  near-diameter estimate gives the exact actual-diameter degree moment by taking a
  finite-source zero-width limit before any asymptotic sequence limit.
- **PASS — promote `C-CORE-DIAMETER-REPLACEMENT-COVER-COST`.** For the already
  feasible endpoint normalized in Audit.177, every changed-label cover and every
  maximum-matching endpoint cover of the new core diameter pairs obeys the stated
  cubic-moment cost. A linear lost-pair count forces at least order `sqrt(D)` changed
  labels and matching pairs, with the exact constants below.
- **No frontier change.** The theorem presupposes a feasible endpoint; it neither
  constructs one nor gives a strict sub-`D` competitor.

## Exact statements

Let `H(A)` be the actual diameter graph of a finite planar unit-separated source
`A` of diameter `D`, let `d_H(x)` be its degree, let `K=conv(A)`, and put
`delta_K=pi D^2/4-area(K)`.

### 1. Actual-diameter cubic moment

For every noncollinear global minimum-diameter source with `D>=2`,

$$
\boxed{\sum_{x:d_H(x)>2}(d_H(x)-1)^3\le6144D\,\delta_K.}
$$

Consequently, by canonical `C-FS-GEOM`,

$$
\boxed{\sum_x(d_H(x)-2)_+^3<C_0D^2,\qquad C_0=1536\pi\sqrt3.}
$$

Every source vertex is included, including contact isolates.

### 2. Cover cost for a replacement bank

Use the canonical contact-minimal, then full-source actual-diameter-pair-minimal
triangle-free minimizer `P` with `D>=9`, its nonisolated contact core `V`, and an
already feasible same-label endpoint as in Audit.177. After the full-source isolate
normalization, write `Q'` for the endpoint. Let `F` be the graph whose edges are the
formerly non-diameter pairs of `P` that have length `D` in `Q'`; Audit.177 gives
`F subseteq H(Q')[V]` and `N=|E(F)|=N_V>=L>=1`, where `L` counts old diameter pairs
of `P` shortened in `Q'`.

For any vertex cover `S` of `F` of size `s>0`,

$$
\boxed{N\le 2s+C_0^{1/3}s^{2/3}D^{2/3},\qquad
       L\le 2s+C_0^{1/3}s^{2/3}D^{2/3}.}
$$

In particular, choose any rigid alignment of the core endpoints with `P` and let
`S` be the labels whose endpoint coordinates differ from `P`. Every new diameter pair
meets this set, so the inequality holds with `s` equal to the number of changed core
labels. If `nu` is the maximum matching size in `F`, its `2 nu` endpoints are a vertex
cover, and

$$
N\le4\nu+2^{2/3}C_0^{1/3}\nu^{2/3}D^{2/3},\qquad
L\le4\nu+2^{2/3}C_0^{1/3}\nu^{2/3}D^{2/3}.
$$

Along any sequence of such endpoints with `D->infinity` and
`L>=(kappa-o(1))D` for fixed `kappa>0`,

$$
\boxed{\liminf\frac{s}{\sqrt D}\ge\frac{\kappa^{3/2}}{\sqrt{C_0}},\qquad
       \liminf\frac{\nu}{\sqrt D}\ge\frac{\kappa^{3/2}}{2\sqrt{C_0}}.}
$$

The first bound holds for the chosen changed-label cover; the second holds for the
maximum matching. Neither gives a linear-sized support or a finite motion.

## Independent proof reconstruction

Fix one finite noncollinear global minimizer `A`. In canonical
`C-INACTIVE-NEAR-DIAMETER-CUBIC-BUDGET`, `H_c` contains exactly the source pairs at distance at least
`D-c/D`, with
`B_c=1+ceil(20 sqrt(c))` and `M_c=2(4 sqrt(c)+1)^2`. Among the finitely many
strictly shorter source-pair lengths, the gap below `D` is positive. Therefore, for
all sufficiently small positive `c`, `H_c=H(A)`. Also `D>=2` meets the input
diameter threshold for all sufficiently small `c`, `B_c=2` when `c<1/400`, and
`M_c -> 2` as `c -> 0`. Apply the canonical finite inequality at this fixed source
and take `c -> 0`:

$$
\sum_{d_H(x)>2}(d_H(x)-1)^3
\le3072\cdot2\,D\delta_K=6144D\delta_K.
$$

The gap is used only source-by-source. It need not have a uniform lower bound along
any sequence. Since `(d-2)^3 <= (d-1)^3` for `d>2`, `C-FS-GEOM` gives

$$
\sum_x(d_H(x)-2)_+^3
\le6144D\delta_K
<6144D\frac{\pi\sqrt3D}{4}=C_0D^2.
$$

For the cover inequality, apply the moment bound to the global minimizer `Q'` and
its actual diameter graph `H(Q')`. Every edge of `F` has an endpoint in `S`, whence

$$
N=|E(F)|\le\sum_{x\in S}d_{H(Q')}(x)
\le2s+\sum_{x\in S}(d_{H(Q')}(x)-2)_+.
$$

Holder's inequality and the cubic moment give

$$
\sum_{x\in S}(d_{H(Q')}(x)-2)_+
\le s^{2/3}\left(\sum_x(d_{H(Q')}(x)-2)_+^3\right)^{1/3}
<C_0^{1/3}s^{2/3}D^{2/3}.
$$

Audit.177 supplies `N>=L>=1`, so the new-pair graph is nonempty and a changed-label
cover has `s>0`. New pairs cannot have both endpoints fixed at their old coordinates:
their old distance would then already equal `D`. The endpoints of a maximum matching
cover every edge, since a maximum matching is maximal. Substituting cover size `2 nu`
gives the matching inequality.

For the changed-label asymptotic, divide
`L<2s+C_0^(1/3)s^(2/3)D^(2/3)` by `D`. On a subsequence where `s/sqrt(D)` tends to a
finite liminf, the term `2s/D` tends to zero, leaving
`kappa<=C_0^(1/3)(s/sqrt(D))^(2/3)`. If that normalized quantity has infinite
liminf, the claimed lower bound is automatic. With a matching cover, substitute
`s=2 nu`; the same argument gives the factor `1/2` in the matching bound.

The normalized endpoint `Q'` is a noncollinear global minimizer: same-cardinality
unit separation and diameter at most `D=D(n)` make it globally minimal. Since
one-, two-, and three-point sources have optimum diameter at most one, `D>=9`
implies `n>=4`. For `n>=4`, the `n` points fit into a `ceil(sqrt(n))` square
lattice block of diameter at most `sqrt(2)(ceil(sqrt(n))-1)<sqrt(2n)<n-1`,
while every collinear unit-separated `n`-point source has diameter at least
`n-1`. Thus the use of `C-FS-GEOM` at `Q'` is within its noncollinear scope.

## Hostile checks and limits

- **Finite-source versus sequence limit:** first choose the positive inactive gap
  for one finite source and take `c -> 0`; only the resulting uniform-constant
  actual-diameter theorem is then applied along a sequence.
- **Actual graph:** the moment concerns every edge of the actual diameter graph at
  each endpoint. No selected-stress graph or near-diameter graph is substituted at
  zero width.
- **Full source:** `Q'` retains every contact isolate. Audit.177 opens all
  isolate-involving diameter equalities before `F` is localized to the core.
- **Globality:** the cubic moment uses global minimality through `C-FS-GEOM`; the
  finite cover/Hölder calculation alone is a graph inequality.
- **No endpoint or motion:** the endpoint hypotheses come from Audit.177 and remain
  unconstructed. A lower bound on support size is not a finite feasible displacement.
- **Numerical scope:** the rerun canonical verifier passed 7,007 exact source-pair
  checks, 647 algebra checks, 39,675 cover checks, and 3,300 matching checks. Its
  fixtures do not prove the analytic moment or asymptotic bounds.

## Canonical dependencies and disposition

| Claim | Verdict | Dependencies |
| --- | --- | --- |
| `C-ACTUAL-DIAMETER-CUBIC-MOMENT` | PASS — promote | `C-INACTIVE-NEAR-DIAMETER-CUBIC-BUDGET`; `C-FS-GEOM` |
| `C-CORE-DIAMETER-REPLACEMENT-COVER-COST` | PASS — promote | `C-ACTUAL-DIAMETER-CUBIC-MOMENT`; `C-CORE-DIAMETER-REPLACEMENT-AFTER-ISOLATE-NORMALIZATION`; canonical full-source diameter-pair minimality |
| Any source Section 4 claim beyond the statements above | Not promoted | No additional claim audited |
| C-II / Level I closure | Not claimed | — |

Audit.178 adds an exact support-cost restriction after a feasible endpoint exists.
It does not change the active C-II finite-move/payment obligation or Target C
frontier.
