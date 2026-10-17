> Generated reading edition · [exact source](../../../docs/audits/target_c_isolate_paid_aggregate_detour_independent_audit_2026-09-14.md) · source SHA-256 `6608d53ae8cb5a30e223fa94b41a5bf0854329a078f5c589b5be3e105333b8e0`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-953BC4E8D194","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — isolate-aware aggregate detour payment

**Date:** 2026-09-14
**Artifact audited:** `docs/reports/target_c_isolate_paid_aggregate_detour_2026-09-14.md`
**Target:** C-II / Level I
**Verdict:** audited-working as a finite conditional bridge; not canonical and not a Level I closure

## 1. Audit conclusion

The finite implication is sound under the stated canonical C-II attachment-cell
hypotheses, with one clarification made during the audit: the local/global face
identification requires proving that a global contact edge cannot cross into the
interior of a different attachment cell. This is supplied by the strict convex force
hull and the disjoint-cell tangent-cone argument in §3.3 of the report.

The audited conclusion is

```math
 \sum_rG_r\le a_0Z_{\rm cell}+O(D),
 \qquad
 \sum_r(L_r+P_{{\rm exc},r}-2d_r)
 \le {10\over3}Z_{\rm cell}+O(D),
 \tag{A.1}
```

where the `O(D)` constants are uniform over the canonical post-ZF class. The first
inequality is a finite source-level estimate; the second uses canonical Section 121.
The coefficients in the `O(D)` terms were not optimized and do not cross the
canonical Section-122 contradiction threshold.

## 2. Dependency audit

### 2.1 Full-source force-hull slack

The source Oler slack is

```math
 \mathcal O_A=\operatorname{area}(K)+c_0\operatorname{per}(K)-a_0(n-1),
 \qquad a_0=2c_0.
```

The strict translated-triangular-lattice comparison gives
$`
\operatorname{area}(K)+c_0\operatorname{per}(K)-a_0(n-1)<c_0\operatorname{per}(K)
`$, because $`a_0(n-1)>\pi D^2/4\ge\operatorname{area}(K)`$ for the relevant
finite global-minimum source. Cauchy's inequality gives both source and force-hull
perimeters at most $`\pi D`$. The standard force-hull augmentation/cap cancellation
therefore makes the total dimensional Oler slack of bounded force-hull faces and
exterior caps `O(D)`. Isolated points are part of those Oler sets; no coordinate is
deleted.

### 2.2 Refinement identity

If an added attachment-cell chord has length `ell`, the two child face perimeters
sum to the parent perimeter plus `2ell`, while the two child boundary occurrence
counts sum to the parent count plus two. The two `+1` terms also replace the parent
`+1`, so the total dimensional Oler slack increases by exactly `ell`. The attachment
perimeter currency gives

```math
 \sum_rp_r=O(D),
```

and hence the total slack after all cell-side refinements remains `O(D)`.

### 2.3 Actual source embedding, not a scaffold substitution

Every unloaded vertex in `int(P_r)` is in `I_r` by harmonic trapping and disjoint
cell interiors. Every loaded vertex is an extreme vertex of the force hull. If a
loaded hull vertex is not in `A_r`, the strict convexity of the force hull places it
outside the tangent cone of `P_r` at every `A_r` endpoint, so a segment from `A_r`
to that loaded vertex leaves `P_r` immediately.

If a contact edge from `A_r` reaches an unloaded vertex of `I_s`, then its loaded
endpoint belongs to `A_s`. The edge lies in `P_s`; disjoint interiors of `P_r` and
`P_s` imply that the edge cannot enter `int(P_r)` at their common endpoint. An
unloaded vertex of `I_r` has no contact outside `I_r\cup A_r` by definition.

Thus every contact edge meeting the interior of `P_r` is included in the induced local
graph. The local convexified faces are an actual refinement of the global force-hull
faces. This is the crucial bridge that would fail for an abstract scaffold; it is
valid here because `A_r` consists of actual force-hull vertices and the cells are
actual disjoint convex hulls.

### 2.4 Bad-face boundary currency

Canonical Section 82 gives, for each local graph,

```math
 L_r+Q_r=4a_r-6-2s_r-2c_r,
 \qquad Q_r\le2a_r,
 \qquad f_r\le Q_r.
```

The nonquadrilateral contact-face boundary occurrences are at most `5Q_r`. The
attachment-side pockets have total boundary occurrence count
$`L_r+2h_r-a_r\le L_r+a_r`$. Since $`\sum_ra_r=O(D)`$, the total bad-face boundary
occurrence count is `O(D)`, including bridge and repeated-vertex multiplicity.

### 2.5 Isolate term

For every refined bad face `Q`, the exact Oler slack identity gives

```math
 \operatorname{area}(Q)
 \le a_0(\sigma_Q+k_Q+z_Q).
```

Summing uses `O(D)` refined slack, `O(D)` boundary occurrences, and exactly the
number `Z_cell` of contact-isolated source points in those faces. Therefore
$`\sum G_r\le a_0Z_{\rm cell}+O(D)`$. Section 121 then gives the exact coefficient
$`5a_0/(3c_0)=10/3`$ in the detour bound before adding the `O(D)` cell perimeters.

## 3. Hostile checks

| Check | Result | Reason |
| --- | --- | --- |
| Full source versus positive-contact core | pass | Isolates are counted by `z_Q`; only the force-hull contact graph is used for cell geometry |
| ZR/ZF affine kernel scope | pass | No affine-kernel statement is extended to isolates |
| Source/scaffold non-embeddability | pass under explicit tangent-cone lemma | Attachment cells are actual convex hulls of force-hull vertices; no selected scaffold is substituted for the source |
| Contact edges crossing cell boundaries | pass under the lemma | Loaded-to-loaded and loaded-to-other-component cases are separated; neither can enter a cell interior |
| Boundary-side isolates | pass | They may be subdividing boundary vertices and are charged to `Z_cell` or `O(D)` boundary count |
| Repeated outer walks and bridges | pass | All local `L_r` counts are occurrence counts and only enter upper bounds |
| Near-equilateral vanishing shear | pass | No angle gap or density loss is inferred |
| Macroscopic inactive chamber | uncovered by design | It can make `Z_cell` quadratic; the theorem records rather than removes this branch |
| Exact strict competitor | absent | The result is only an upper bound; no finite source-preserving deformation is constructed |

## 4. Exact limitation

Canonical Type-II no-chamber information is only

```math
 Z_{ch}+Z_{ext}=o(D^2),
```

not `Z_cell=o(D)`. The audited theorem therefore does not turn the Section-122
linear detour floor into a contradiction. Even after imposing `Z_cell=0`, the
unoptimized boundary coefficient in (A.1) is too large to contradict the floor.
The remaining Level-I obligations are a source-preserving deformation or exact
triangle in the full-core branch, and a separate closure of the macroscopic inactive
container/exterior-cap branch.

## 5. Lifecycle recommendation

Record the report as **audited-working**, but keep theorem authority unchanged. A
future promotion would need a lifecycle entry naming the tangent-cone face-embedding
lemma and would still not alter the open C-II status.
