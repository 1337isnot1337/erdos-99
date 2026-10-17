> Generated reading edition · [exact source](../../../docs/audits/target_c_loaded_endpoint_local_incidence_independent_audit_2026-10-07.md) · source SHA-256 `3ebdc72958ffdbeb27c8a1842b676c2e308c4db3c315146b7c44ea97e32f929d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-74BB3967C43C","canonical":true,"claim_ids":["C-DIAMETER-ENDPOINT-LOCAL-DEGREE-TWO","C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE"],"claim_statuses":{"C-DIAMETER-ENDPOINT-LOCAL-DEGREE-TWO":"canonical","C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C nearby diameter-endpoint incidence: independent audit

Date: 2026-10-07. Audit base: `fe99a394b0a0327dc9cf78aceda1aaf4e90874f5` (`2026-10-07.audit.103`).

Source: PR #722 branch `research/target-c-residual-closure-20261005` at frozen commit `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. Source artifact: `docs/reports/target_c_loaded_neighbor_outer_owner_bound_2026-10-05.md`, SHA-256 `73fcdb63e60c7104eede09e47d9dca9e82f7b0b5fb3bc89631de04d6d5863bff`.

I audit only the source-geometric claims in §§2--3. The report's owner-capacity applications in §§1, 4--5 are not part of this promotion; in particular, no actual O--O proposal-family capacity bound is promoted here.

## Exact statements audited

Let `A` be a noncollinear global minimum-diameter unit-separated planar source with diameter `D`, and let `B` be any subset of its actual diameter endpoints. For every fixed real `t` with `1<t<sqrt(2)`, there is `D_0(t)` such that whenever `D>=D_0(t)`:

1. For every source point `y in A`, at most two distinct points `p in B\{y}` satisfy `|p-y|<=t`.
2. Any two distinct `p,q in B` with `|p-q|<=t` are consecutive vertices of the full source hull `conv(A)`.

The threshold depends only on `t`. Since the conclusions hold for any subset of actual diameter endpoints, they apply in particular to the loaded set of any normalized KKT stress. The second statement is stronger than the already-canonical conclusion that sufficiently short loaded pairs are sides of the loaded hull: it rules out intervening contact isolates or other unlabeled source hull vertices on the full hull boundary arc.

## Independent proof of the local-degree bound

By canonical `C-FS-GEOM`, every actual diameter midpoint of one source lies within

```text
L_D = sqrt(D*eta_D + eta_D^2),   eta_D = 3^(1/4)*sqrt(D),
```

of one common center, so `L_D/D -> 0` uniformly as `D -> infinity`. For any diameter endpoint `p_i`, choose an actual diameter partner `a_i`, and put

```text
n_i = (p_i-a_i)/D,     m_i=(p_i+a_i)/2.
```

For every other source point `w`, the diameter bound `|w-a_i|<=D` gives

```text
n_i dot (w-p_i) <= -|w-p_i|^2/(2D) < 0.
```

Thus `n_i` is a strict supporting normal of the full source hull at `p_i`. For any two selected endpoints,

```text
D(n_i-n_j) = 2(p_i-p_j) - 2(m_i-m_j).
```

Assume, toward contradiction, there are arbitrarily large `D` sources and source points `y` with three distinct endpoints `p_1,p_2,p_3 in B` satisfying `|p_i-y|<=t`. Translate `y` to zero. Unit separation gives `1<=|p_i|<=t` and `|p_i-p_j|>=1`. The midpoint identity gives

```text
sin(angle(n_i,n_j)/2) <= (2t+2L_D)/D -> 0.
```

All three supporting normals therefore converge to the same direction after taking a subsequence. Order the endpoints by their normal angles. For consecutive ordered endpoints, the strict support inequalities at the two ends put the chord direction strictly between the corresponding quarter-turns of the normals. Consequently the two forward chords have directions whose angle tends to zero. Compactness of the annulus `1<=|p_i|<=t` now gives a subsequential limit of three points on one line, in order, with each consecutive distance at least one.

No such triple fits in the closed annulus `1<=|x|<=t` when `t<sqrt(2)`. Let `h` be the distance from the line to the origin. If `h>=1`, its intersection with the radius-`t` disk has length at most `2sqrt(t^2-1)<2`, but a separated ordered triple needs endpoint distance at least two. If `h<1`, the annulus cuts the line into two intervals, each of length

```text
sqrt(t^2-h^2)-sqrt(1-h^2) <= sqrt(t^2-1) < 1.
```

Each interval can contain at most one unit-separated point, so the two intervals cannot contain three. This contradiction proves the uniform `D_0(t)` assertion. The argument permits `y` to be any source point, including a contact isolate; it imposes no equilibrium condition at `y`.

## Independent proof of full-hull adjacency

Take distinct actual diameter endpoints `p,q` with `|p-q|<=t`, and choose actual diameter partners to obtain strict supporting normals `n_p,n_q`. The same midpoint identity gives

```text
sin(angle(n_p,n_q)/2) <= (t+2L_D)/D -> 0.
```

Let `theta` be their smaller angular separation. The hull boundary arc associated with the short normal interval from `n_p` to `n_q` has all its outward normals in that interval. Its directed side vectors therefore lie within angle `theta/2` of the central tangent direction. If `p` and `q` were not consecutive full-source hull vertices, this arc would contain at least two sides. Every source side has length at least one, so projection of the two sides onto the central tangent gives

```text
|p-q| >= 2*cos(theta/2).
```

For sufficiently large `D`, `theta` is uniformly small and `2*cos(theta/2)>t`, contradicting `|p-q|<=t`. Therefore `p,q` are consecutive on the full source hull. In particular, every noncontact loaded pair in this range is a nonunit full-hull side and hence a nonunit loaded-hull side. The latter corollary is compatible with, and its weaker loaded-hull part is already covered by, `C-LOADED-NEAR-UNIT-ADJACENCY`; the full-source consecutivity is the additional conclusion.

## Scope audit and disposition

- **PASS — promote** `C-DIAMETER-ENDPOINT-LOCAL-DEGREE-TWO` with the fixed-`t` and sufficiently-large-`D` quantifiers above.
- **PASS — promote** `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE` with the same quantifiers.
- The proof uses only actual diameter endpoints, actual diameter midpoints, source separation, and full-source hull support. It does not replace the full diameter graph with a selected stress support or discard isolates.
- No numerical verifier is claimed. The sufficient-large-diameter threshold follows by compactness and the canonical uniform `L_D/D -> 0` bound; there is no explicit `D_0(t)`.
- The loaded-owner counting argument, root allocation, O--O extraction, and any source-realized finite move remain unaudited. The outer-isolate collar report that cites the loaded-neighbor claim is a separate audit item.

**Frontier effect.** For any fixed `t<sqrt(2)`, each source point has at most two actual diameter endpoints in its radius-`t` neighborhood in all sufficiently large global minimizers. This gives a uniform local incidence bound that may be used in subsequent owner-capacity arguments, but it does not itself bound the number of owners or prove any exchange exists.

## Repository validation

No theorem-specific verifier is claimed or needed. Before promotion, the artifact index regenerated 1,264 records, generated theorem views refreshed, `check_theorem_state.py` and `check_active_route_summaries.py` passed, all 16 theorem-state tooling unit tests passed, all 70 registered theorem certificates passed, and `git diff --check` passed. These checks establish repository consistency, not the geometric assertions above.
