<!-- theorem-state: {"artifact_id":"ART-F80457D8F1E2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C second referee — one-deficit source exchange and isolate accounting

Date: 2026-10-10. Canonical base: `origin/main=a1935b7c01cbcbe511743d3eb72f3fb1a725aac2`, state `2026-10-10.audit.230`.

Frozen discovery branch: `origin/research/sol/target-c-overnight-closure-20261007` at `c6a75bd708e553c4feb3a540e0b17f3b65e22a82`. The all-M report `docs/reports/target_c_all_M_one_deficit_sector_peeling_2026-10-07.md` is unchanged from the source snapshot independently promoted by Audit.77 at `01328c805e5bcc3726dac0751c1e9cc6274c163a`; its SHA-256 is `7febb3769caec4221c83375c9c752168910c0370e5572c8296973a8574bba17a`. The current finite verifier `research/verify_target_c_one_deficit_sector_peeling_2026_10_07.py` has SHA-256 `c66a97dec048c4704e0629bcc56ac3432be634cdeaa489fd923f35ca50ba2081`; since the Audit.77 snapshot it only parameterizes the rational angle and adds three finite root-clearance/window checks.

## Verdict

**PASS WITH NARROWED SCOPE — the all-M source-exclusion theorem remains valid, but its label-retention wording must be narrowed.** The exchange counts every point strictly inside the wall, including any contact-isolated points there, in `z`; it then deletes all `z` interior labels and one wall vertex and inserts `z+1` strict packet points. It retains every source point outside the wall, including exterior contact isolates. It does not preserve the identities of interior contact isolates. This distinction changes no cardinality, contact, diameter, or nonexistence conclusion.

The same correction applies to the arithmetic-window source exclusion (Audit.80) and to the `z<=N-1` branch of the polynomial-window source exclusion (Audit.107), both of which use this exchange. The theorem-state entry for the five exact Audit.76 cases already says only that exterior points are retained; its audit report used a broader phrase and now carries a clarification. The actual fixed-wall and growing-M fixed-profile conclusions remain canonical.

## Exact theorem under audit

For each fixed `M>=4` and fixed strictly decreasing symmetric real rate profile, at every sufficiently small positive curvature allowed to depend on `M` and the profile, no contact-minimal then diameter-pair-minimal triangle-free global minimizer containing all `6M` vertices of the specified wall can have `z<=N-1` points strictly inside it, where `N=3M^2-3M+1`. The canonical proof dependencies are:

- `C-ONE-DEFICIT-ALL-M-STRICT-PACKET`: the specified wall has a strict packet of `N` interior sites, pairwise strictly separated and clear of every retained wall vertex after one wall vertex is deleted;
- `C-ONE-VERTEX-CONVEX-WALL-SHIELD`: a site clear of every other wall vertex is strictly clear of every retained exterior source point, including exterior isolates;
- `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`: a finite full-source replacement with no new unit contacts and at least one removed old contact contradicts contact minimality when its diameter is at most the old `D`.

No uniform onset in `M` or the profile, arbitrary-wall extraction, or exclusion of `z=N` is part of this theorem.

## Independent source-exchange reconstruction

Let `A` be a source containing the wall and let `I=A intersect int(W)`, `z=|I|`. Every source point on a wall side other than a wall vertex is within distance strictly less than one of an endpoint of that unit side, so unit separation forbids such a boundary point. Thus all points in the closed wall besides its `6M` named vertices are counted in `I`.

Since `z<=N-1`, select any `z+1` distinct points of the strict `N`-site packet. Delete the complete set `I`, including any interior contact isolates, and a wall vertex `v_0` cleared only by the packet construction. Insert the `z+1` selected packet sites. The number of labels removed and inserted is both `z+1`; all old source labels outside the closed wall remain. This is an exact same-cardinality replacement, with no assumption about the old interior points' contacts or locations.

The packet sites are pairwise strictly more than one apart and clear of each retained wall vertex. The canonical one-vertex shield then gives strict unit clearance from every retained exterior source point, including exterior contact isolates. Consequently no new unit contact is created and no new triangle appears. The two distinct unit wall edges incident to `v_0` are removed, so at least two old contacts disappear. The retained contact graph is an induced subgraph of the old triangle-free graph.

For upper constraints, all inserted sites lie in `int(W)`. The wall is contained in the convex hull of the old source because every wall vertex was in `A`; hence each inserted site is strictly inside `conv(A)`. For any retained old point `y`, the strictly convex function `x -> |x-y|^2` on `W` is strictly below its maximum at an interior point, and all wall vertices are old source points at distance at most `D` from `y`. For two inserted sites, both are interior to `W`, so their distance is strictly less than `diam(W)<=D`. Old-retained pairs are unchanged. Thus the new source is unit-separated with diameter at most `D`.

If its diameter is below `D`, global minimality is contradicted. If it equals `D`, the contact-minimality endpoint applies with `j=0<t`, because at least two contacts were deleted and none added. This proves the nonexistence theorem even when `I` contains contact isolates: they are counted and replaced, not omitted from the population. It does not establish label-preserving retention for those interior isolates.

## Updated finite verifier

The verifier was inspected at the current frozen branch tip and rerun. Its exact `Fraction` / `Q(sqrt(3))` checks passed for eight base cases (`M=3,...,10`) and three explicit angle-window cases (`M=4,6,10`), totaling 206,058 lower-pair checks and 304 constructive opening rows. Ten cases completed full half-plane elimination; `M=3` remains only the explicitly labeled local peeling regression. The added root checks test all chart/wall guards except the omitted site and deleted vertex, plus every wall support line, in those three finite cases.

These computations establish only the finite cases and arithmetic encoded in this script. They do not prove the all-M analytic peeling argument, the profile root for all profiles, the fixed-profile onset, or global optimality. The all-M theorem uses the reconstructed Gordan/finite-opening proof and the canonical packet, shield, and contact-budget dependencies.

## Canonical correction and frontier

The literal conclusion is narrowed to: all source points outside the wall are retained; every strict-interior label, including any contact isolate there, is counted in `z` and deleted as part of the interior cloud; `z+1` packet points replace that cloud together with the deleted wall vertex. The nonexistence conclusion, theorem dependencies, and fixed-wall frontier do not change. Audit.77, Audit.80, and Audit.107 wording and the current Target C summaries are clarified accordingly. No route-map change is warranted; the active prompt was updated only to point to state `.231`, with its research obligation unchanged. C-II and Level I remain open.
