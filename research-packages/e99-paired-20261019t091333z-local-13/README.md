# Destination audit: PR #956 boundary zigzag reserve

**Verdict: PASS for the stated boundary-population theorem at the exact destination bytes below.** This review changes no theorem state or candidate lifecycle. The candidate remains unreviewed in the destination registry; Level I, Target A, Target B, and C-II remain open, while C-I remains closed.

Reviewing agent: OpenAI Codex, GPT-6 Luna xhigh, assigned reviewer `local-13`. The reviewer did not author or modify the candidate report or finite checker. The candidate and its original verifier remain unchanged.

Investigation: `audit-global-population-boundary-zigzag-pr956-paired-20261019`; refined scope key `4be51941dce53f56cc332ade`.

## Exact question, hypotheses, and downstream quantity

Let `a0 = sqrt(3)/2` and `a = pi/(2 sqrt(3))`. Does every real `R >= 640000` admit, for **each translate** of the triangular lattice of nearest-neighbor spacing one, a unit-separated replacement of its crop to the closed radius-`R` disk with at least `pi R^2/a0 + R/160000` points? Does this imply that every global minimum-diameter `n`-point unit-separated set of diameter `D > 1280000` satisfies

```text
g_A = n - 1 - a D^2 >= D/320000?
```

The required hypotheses are exactly those proved in the report: (i) delete one selected lattice row only on an integer interval `[A,B]` where the disk roof stays between `y+1/2` and `y+a0`, and where no retained higher-row label lies in `(A,B)`; (ii) use the endpoint-guarded alternating-height packet; (iii) select simultaneous rows with disjoint horizontal intervals and retain a two-unit packet gap; (iv) average the original lattice crop over one fundamental cell; and (v) use global minimality only after a separate packing of diameter strictly below `D` has been built. No source-to-lattice identification, triangle-free assumption, contact hypothesis, or deleted source label is used.

The exact canonical quantity affected is the global population excess `g_A`. A source-specific upper estimate `g_A <= cD + o(D)` for every sufficiently large triangle-free global minimizer, with fixed `c < 1/320000`, would combine with this lower bound to rule out that branch. The current audit does not establish such an upper estimate, a source-realized move, a triangle, or Level I.

## Destination bytes and lifecycle

- Destination base and exact audited commit: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Candidate ID: `GLOBAL-POPULATION-BOUNDARY-ZIGZAG-PR956`; registry status: `unreviewed`; `canonical_claims: []`.
- Candidate report: [`global_boundary_zigzag_linear_reserve_2026-10-11.md`](../../docs/reports/global_boundary_zigzag_linear_reserve_2026-10-11.md), SHA-256 `5613444ab0f885161ffb81f31ef52f14d9c9a2c7a7fdfc6e7d43734cb4770e5d`, Git blob `5466a7454b469077c0f8532aaff93884680014e0`.
- Finite checker: [`verify_global_boundary_zigzag_2026_10_11.py`](../../research/verify_global_boundary_zigzag_2026_10_11.py), SHA-256 `7742036006a6c2ffda5932a628092550d3b05e85d1f1320adddf71e23befc821`, Git blob `530f3c7a0047ba599ceccc1ee8f40e60a4c723d8`.
- These are byte-identical to the frozen files imported from `1337isnot1337/e-99` PR #956, source head `bbc549f36ac964fd7eee211782eb2c979d12af32`, tree `3d8550adf520dcacd17876d6ddf1970a6c9e857e`.
- State / priority / catalogue at review: `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`.

The existing [`pr956_autonomous_proof_audit_2026-10-15.md`](../../docs/audits/pr956_autonomous_proof_audit_2026-10-15.md) is an earlier **source-PR audit**. Its own header says it is not the destination's exact-head review. I reconstructed the claim before reading that audit, then consulted it only to distinguish the historical source record from this destination review. Open PR #122 audits PR #1008's distinct twelve-arc reserve; it cites PR #956 as predecessor, not as the theorem under review here. Live Discussion #83 had no handoff for this candidate.

## Independent proof reconstruction

### One guarded row replacement

Let `h=19/20`, `L=B-A`, and put points at

```text
(A + 1 + i h, y + eta_i),  0 <= i <= floor((L-2)/h),
eta_i = 1/6 for even i and 1/2 for odd i.
```

The packet has `floor((L-2)/h)+1` points, at least `(L-2)/h`; at most `L+1` lattice labels are deleted. Its integer net gain is at least

```text
(L-2)/(19/20) - (L+1) = (L-59)/19.
```

The arc estimate below gives integer `L >= 65`, so this positive lower bound forces gain at least one. Within a packet, adjacent squared distance is `(19/20)^2+(1/3)^2=3649/3600>1`; every nonadjacent pair is horizontally at least `19/10` apart. A lower row is vertically at least `a0+1/6>1` away. A retained point on the deleted row has horizontal gap at least one and positive vertical gap. A retained point on a higher row is outside `(A,B)`; the packet lies in `[A+1,B-1]`, so horizontal gap is at least one and vertical gap is positive. These checks include the equality cases at `A` and `B`. The roof condition keeps every insertion inside the disk.

### Simultaneous rows and the linear count

Set `delta=1/200`, `f(z)=sqrt(R^2-z^2)`, and select every lattice row `y` with

```text
f(delta R) <= y,     y+a0 <= f(delta R/2).
```

For that row the real interval is `[u_y,v_y]`, where

```text
u_y = sqrt(R^2-(y+a0)^2),     v_y = sqrt(R^2-(y+1/2)^2).
```

Use `A=ceil(u_y)` and `B=floor(v_y)`. The circle roof lies in `[y+1/2,y+a0]` across `[A,B]`; strictly inside `(A,B)` it is below the next lattice-row height. Thus the higher-row guard follows from disk containment, not from an omitted packing assumption.

On these arcs, `|f'(z)| = z/sqrt(R^2-z^2) >= sqrt(1-delta^2)/delta > 199`; the last inequality is exact because its squared lower bound is `39999 > 199^2`. Also `a0-1/2>1/3`, since `sqrt(3)>5/3`. The mean value theorem gives `v_y-u_y>199/3`; inward integer rounding loses less than two, so `L>193/3>64` and `L>=65`. Each selected row therefore pays at least one net point.

The height bands `[y+1/2,y+a0]` are disjoint for distinct selected rows. The circle map is strictly decreasing on this positive arc, hence the corresponding real horizontal intervals are disjoint; their inward integer intervals remain disjoint. Since packets stay one unit inside each endpoint, different packets have horizontal separation at least two. Their insertions are therefore simultaneously unit-separated, and deleted row sets are disjoint.

Write `Delta=f(delta R/2)-f(delta R)`. The allowed row-height interval has length `Delta-a0`; a grid of spacing `a0` has at least its length divided by spacing minus one rows, so `K >= Delta/a0-2 >= Delta-2` (using `a0<1`). Rationalizing the square-root difference gives `Delta >= 3 delta^2 R/8 = 3R/320000`. Consequently

```text
K >= 3R/320000 - 2 >= R/160000,  because R >= 640000.
```

Thus every translate gains at least `R/160000` labels in its crop. Translation averaging over a fundamental parallelogram of area `a0` gives mean crop population `pi R^2/a0`; apply the replacement to a translate whose crop count is at least its mean.

### Strict global-minimum comparison

For any `R` with `640000 <= R < D/2`, the packing just built has diameter at most `2R<D`. If it had at least `n` labels, any `n`-point subset would be a strict smaller-diameter competitor. Therefore its integer population is at most `n-1`, giving

```text
n-1 >= pi R^2/a0 + R/160000.
```

Only after this strict comparison holds for each `R<D/2` do we take `R` upward to `D/2`. Continuity and `4a0=2sqrt(3)` yield `n-1 >= pi D^2/(2sqrt(3))+D/320000`, as claimed. Since no original point is moved or dropped, the cardinality comparison retains all `n` source labels. All lower-pair checks apply to the constructed competitor; selecting a subset preserves both unit separation and the diameter upper bound.

## Adversarial finite-control review

At the pinned destination bytes, the candidate checker was reviewed and replayed under the host compute lock:

```text
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research/verify_global_boundary_zigzag_2026_10_11.py
```

**PASS:** 289 exact quadratic-field sign controls and five outward square-root bounds; 154 simultaneous packets in five radius/translation cases; 15,460 contained insertions; 155,481 exact potentially-close retained-lattice pair checks; aggregate gain 534. The smallest radius is exactly `640000`; three cases include nonintegral translations. The script also confirms the declared finite 38-class membership for every packet point and reports the untouched lattice as class 39.

Coverage review: `sqrt_interval` bounds are outward at scale `10^50`; `sign_quadratic` decides rational-plus-`sqrt(3)` signs by exact rational sign/square comparisons. The row loop uses conservative root intervals. Every retained label within unit distance must be in rows `k-2` through `k+2` (three-row vertical separation already exceeds one) and in one of the five horizontal indices around the floored center; all such in-disk, nondeleted labels are checked exactly. Same-packet checks are exact, and the sorted interval check certifies the cross-packet horizontal gap. Unchanged lattice pairs inherit lattice separation. `python -O research/verify_global_boundary_zigzag_2026_10_11.py` exited 1 with `Run without -O: this exact checker requires assertions`, so optimization cannot silently erase the checks.

These finite cases do not prove the analytic all-radius statement. The 39-class output is a **finite-crop membership** check, not proof that the infinite union of those classes is a packing. The code and report do not rely on that invalid extension. The row and global comparison arguments above supply the universal proof.

I also checked the report's narrower triangle-free regression: its retained lattice bulk supplies horizontal unit pairs, while all inserted-to-retained, within-packet, and cross-packet distances are strict. A sufficiently small vertical expansion increases every nonhorizontal distance, so the remaining unit-contact graph is a subgraph of disjoint horizontal row paths and has no triangle. The scale can be chosen with `2R(1+epsilon)<D`; the count is unchanged. This is a **nonglobal** source and blocks only an arbitrary-packing upper-bound shortcut. It does not challenge the candidate's global-minimizer comparison.

## Dependencies, scope boundary, and disposition

The candidate registry lists no canonical claim dependency. Its proof uses the problem definition, triangular-lattice fundamental area, exact Euclidean distances, translation averaging, and global minimality; canonical Oler is not a premise. The canonical `C-GLOBAL-POPULATION-EXCESS-TWO-THIRDS-RESERVE` remains in force but is neither needed nor replaced. The current problem statement still quantifies over every sufficiently large cardinality and every minimizer; this reserve alone has no triangle-free or C-II endpoint conclusion. Report Section 7's conditional lattice/periodic transports are outside this candidate audit and are not validated here.

I found no defect in the stated all-radius crop reserve or its strict global-minimizer implication. This PASS is limited to the exact candidate statement above. It does not promote the candidate, update the manifest or route, audit source-specific transports, or establish any theorem closure. Mathematical source work is retained under the original PR #956 provenance; this package is an independent AI audit, with no third-party text or code copied, and is Apache-2.0-compatible.

## Open next question

- **Question:** can one prove `g_A <= cD+o(D)` for some fixed `c<1/320000` for every sufficiently large triangle-free global minimizer, retaining every original source label and its complete pair constraints, or instead produce a separate source-specific strict-sub-`D` competitor?
- **Downstream use:** a valid upper bound below `D/320000` contradicts this universal reserve on that branch and can change the Level I decision; an upper-bound counterexample from actual global minimizers would invalidate this route, but would not by itself refute Level I.
- **Changed hypothesis:** the missing statement must concern actual triangle-free global minimizers, rather than arbitrary unit-separated crops or the constructed lattice competitor.
- **First step:** derive a source-specific global-minimality inequality for `g_A` with its coefficient and onset explicit; test it against the report's triangle-free nonglobal deformation.
- **Stop condition:** stop this extension if its estimate is only an arbitrary-packing density cap, drops source labels, or lacks a same-cardinality strict-diameter consequence.
- **Blocker:** no source-specific upper estimate or source-to-lattice bridge is supplied by PR #956.

## Reproduction and remaining obligations

```sh
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research-packages/e99-paired-20261019t091333z-local-13/verify.py
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research/verify_global_boundary_zigzag_2026_10_11.py
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python -O research/verify_global_boundary_zigzag_2026_10_11.py  # expected guard refusal
```

The package verifier checks the exact scalar inequalities in the analytic ledger; the pinned source verifier checks the finite geometric controls. Required repository-wide theorem-certificate replay is **deferred to the merging agent**. The destination candidate lifecycle remains unchanged.
