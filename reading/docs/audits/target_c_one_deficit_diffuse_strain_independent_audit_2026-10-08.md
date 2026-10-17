> Generated reading edition · [exact source](../../../docs/audits/target_c_one_deficit_diffuse_strain_independent_audit_2026-10-08.md) · source SHA-256 `37ba24d11db759a2fd59dcf5e0c4f1e0a7bd4c07951e1311dc140ad8aff05d3c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0879DEC6130B","canonical":false,"claim_ids":["C-ONE-DEFICIT-DIFFUSE-STRAIN-NONGLOBAL-REGRESSION"],"claim_statuses":{"C-ONE-DEFICIT-DIFFUSE-STRAIN-NONGLOBAL-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C Audit.156 — one-point Oler slack with diffuse strain is not global optimality

**Date:** 2026-10-08

**Audit base:** `origin/main=fdbf00ea44e0b49bd519c39b732c33a5ea656044`, state `2026-10-08.audit.152`.

**Frozen source:** `origin/research/sol/target-c-overnight-closure-20261007` at `c6a75bd708e553c4feb3a540e0b17f3b65e22a82`.

**Source report:** `docs/reports/target_c_one_deficit_diffuse_strain_nonglobal_regression_2026-10-07.md`, SHA-256 `19ea88f98a1ee34580f0aa46b63c54f4180e075374390ef9212ac662e6cfe21a`.
**Verifier:** `research/verify_target_c_one_deficit_diffuse_strain_2026_10_07.py`, SHA-256 `ec04da709f68efd21630f045b8a020a223a55feb2af5c836fef3b5a6518ba324`. The source script blob is `f71d19911dfa5e17459dcaa591ba0bcd9f564bd6`.

## Exact regression audited

For every integer `M>=3`, let

```text
d = M^4 - 6M^2 - 3
u = (1,0)
v = (sqrt(d)/(2M^2), (sqrt(3)/2)(1+1/M^2))
X_M = {i u + j v : 0<=i,j<=M}
K_M = conv(X_M).
```

The vectors `u,v` are unit, and their angle `theta_M` lies in `(pi/3,pi/2)` and tends to `pi/3`. The complete unit-contact graph of `X_M` is the bipartite rectangular grid, so this is a triangle-free unit-separated source. Its boundary has `4M` labels and its strict interior has `z=(M-1)^2` labels. The area-form Oler slack relative to that interior population is exactly one point's area coefficient:

```text
area(K_M) - (sqrt(3)/4)(2z+4M-2) = sqrt(3)/2.
```

The tiled parallelogram admits a strict Delaunay triangulation by splitting each unit rhombus along its short diagonal. Every interior vertex has valence six, and every triangle has area excess `sqrt(3)/(4M^2)` above an equilateral unit triangle. Nevertheless, the fixed-coordinate set is saturated against one-site insertion: every point of `K_M` is at distance strictly less than one from at least one old grid vertex.

This family is not globally minimum-diameter. Replacing all labels by the square grid `{(i,j):0<=i,j<=M}` preserves the cardinality and triangle-free contact graph. Its squared diameter is `2M^2`, while the old squared diameter is

```text
M^2 |u+v|^2 = 2M^2 + sqrt(M^4-6M^2-3) > 2M^2.
```

Thus exact one-point Oler area slack, vanishing local triangle excess, valence-six Delaunay interiors, and fixed-coordinate one-site saturation do not establish global optimality or a usable source-preserving vacancy.

## Independent reconstruction

Write `c=sqrt(d)/(2M^2)` and `h=(sqrt(3)/2)(1+1/M^2)`. Direct expansion gives `c^2+h^2=1`; since `0<d<M^4`, `0<c<1/2`, hence `theta_M=arccos(c)` lies in `(pi/3,pi/2)`. For an integer difference `(a,b)`,

```text
|a u+b v|^2 = a^2+b^2 + (ab/M^2)sqrt(d).
```

If one coordinate is zero, only a unit coordinate step has length one. If `ab>=0` and both are nonzero, the squared length is greater than one. If `ab<0`, set `r=|a|`, `s=|b|`; then

```text
|a u+b v|^2 = (r-s)^2 + 2(1-c)rs > 1,
```

because `2(1-c)>1`. This proves both unit separation and that the only contacts are the four coordinate-neighbor directions. The contact graph is bipartite, so it has no unit triangle.

The parallelogram area is `M^2 h=sqrt(3)M^2/2+sqrt(3)/2`. Also `2z+4M-2=2M^2`, giving the displayed exact Oler slack. The old diameter is attained at equal-sign opposite corners: the quadratic form `a^2+b^2+2cab` is convex on `[-M,M]^2`, and its largest corner value is `2M^2+2cM^2=2M^2+sqrt(d)`.

Each rhombus has acute angle `theta_M`. Its two triangles after the short-diagonal split are acute, with circumradius squared

```text
R^2 = 1/(2(1+c)) < 1/2.
```

For an acute triangle, the farthest point from its nearest vertex is bounded by the circumradius (the other Voronoi-cell boundary candidates are side midpoints). Thus every point in each triangle is within distance `<1` of one of its three source vertices. Tiling proves the fixed-coordinate one-site saturation throughout `K_M`.

Across a short diagonal, the opposite-angle sum is `2 theta_M<pi`; across an interior unit side it is `pi-theta_M<pi`. The triangulation is therefore strictly Delaunay. Each interior grid vertex has four grid edges and two short diagonals, hence valence six. A triangle has area `h/2`, so its excess above `sqrt(3)/4` is exactly `sqrt(3)/(4M^2)`. All three angles tend to `pi/3` as `M` tends to infinity.

The square-grid replacement has exactly `(M+1)^2` points, minimum separation one, no unit triangle, and squared diameter `2M^2`; the old squared diameter exceeds it by `sqrt(d)>0`. No old label is retained, so there are no omitted old-pair upper constraints.

## Exact verifier audit and limits

I inspected and reran the frozen `Fraction` verifier. Its algebraic sign routine compares expressions in `Q(sqrt(d))` by exact rational coefficient signs and a squared-integer comparison; it does not use floating tolerances. The rerun produced byte-identical JSON to the frozen certificate `research/target_c_one_deficit_diffuse_strain_certificate_2026_10_07.json` (SHA-256 `c56b79657803c31e0a7492a21a8947d6102f2f1da9d0fd57f8933aae87340c8f`). It exhaustively checks old-source and square-grid pair ledgers at `M=3,4,7,10`, with respectively `120,300,2016,7260` pair comparisons, and confirms contact counts, triangle-free classification, exact old diameter, and the strict replacement diameter in those cases.

The verifier is finite evidence only. The universal formulas above prove the all-`M` claims. The script does not encode the Delaunay criterion, circumradius cover, or global `D(n)` implication; those were checked geometrically in the reconstruction. It establishes no maximum-cardinality packing theorem for `K_M`, no canonical minimizer, no full-source KKT stress, and no Level I counterexample.

## Scope against the canonical stack

This is not the existing `C-LARGE-WALL-LOCK-REGRESSION`: that result gives an explicit family whose Oler residual is strictly below one point, so Oler itself rules out an additional point in its container. The present family is at the boundary of one full point of area-form slack and adds a fixed-coordinate saturation proof plus an explicit equal-cardinality strict sub-diameter competitor. It remains a parallelogram-wall regression, with active contacts throughout its interior; it is not a six-sided curved-wall source or a canonical global minimizer.

**Verdict: REGRESSION VALID.** Promote `C-ONE-DEFICIT-DIFFUSE-STRAIN-NONGLOBAL-REGRESSION` at the exact scope above. The result blocks identifying an Oler allowance or locally near-equilateral saturated scaffold with a global minimizer. It does not change the one-deficit theorem hypotheses, extract a wall from a canonical source, or close C-II.
