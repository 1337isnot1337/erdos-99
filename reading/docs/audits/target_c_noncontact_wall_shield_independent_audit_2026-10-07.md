> Generated reading edition · [exact source](../../../docs/audits/target_c_noncontact_wall_shield_independent_audit_2026-10-07.md) · source SHA-256 `649f96184f85487a0da0319fb41126aabf79ba541cdad02b8de77f40fa4a7f5b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F8A0033706B9","canonical":true,"claim_ids":["C-NONCONTACT-WALL-SQRT3-THRESHOLD-REGRESSION","C-NONCONTACT-WALL-STRICT-SHIELD","C-UNIT-PENTAGON-ACTIVATION-THRESHOLD","C-WALL-SAFE-WINDING-BARRIER"],"claim_statuses":{"C-NONCONTACT-WALL-SQRT3-THRESHOLD-REGRESSION":"regression","C-NONCONTACT-WALL-STRICT-SHIELD":"canonical","C-UNIT-PENTAGON-ACTIVATION-THRESHOLD":"canonical","C-WALL-SAFE-WINDING-BARRIER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: noncontact wall shield and finite activation threshold

Date: 2026-10-07. Audit base: `68c39e6a946e7d0241ee88dae23a15eba0532bc4`, state `2026-10-07.audit.87`, Target C C-II open. Frozen source: PR #722 branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. Source artifact: `docs/reports/target_c_noncontact_wall_shield_2026-10-05.md`.

## Verdict

**PASS — promote** the finite strict shield for simple source-vertex polygons with side lengths at most `sqrt(3)`, its joint compatibility for disjoint polygon interiors, the winding-number capacity barrier, and the resulting finite pentagon activation threshold.

**REGRESSION VALID — promote** the exact rational rectangle showing that no universal vertex-guard shield extends to a larger edge cap without another hypothesis. The square example also confirms that noncontact four-edge walls can have strict wall-safe capacity, within the audited shield range.

The source report's residual-cage/competitor composition remains **conditional only**. This audit proves no finite wall-opening motion, no surplus population, and no C-II or Level I conclusion.

## 1. Exact audited statements

Let `A` be a finite unit-separated source and `C` a simple polygon whose distinct cyclic vertices are points of `A`. Assume every side has length at most `L`, where `0<L<=sqrt(3)`. Define

```text
W_C = {x in int(C): |x-b|>1 for every wall vertex b}.
```

For any source point `q` outside `int(C)`:

- if `q` is a wall vertex, `|x-q|>1` by definition;
- otherwise,
  `|x-q| > 2 sqrt(1-L^2/4) >= 1` for every `x in W_C`.

A source point cannot lie in the relative interior of a wall side: if `q=(1-t)a+tb` with distinct source vertices `a,b` and `0<t<1`, at least one of `|q-a|,|q-b|` is at most `|a-b|/2<=sqrt(3)/2<1`. Thus the outside-source cases above are exhaustive.

If `C_1,...,C_m` have pairwise disjoint interiors, any finite unit-separated packets `Y_i subset W_{C_i}` are jointly unit-separated. Cross-packet distances are strictly greater than one. A sufficiently small common dilation of each finite packet can make every internal distance strict while keeping all its sites in its open wall-safe region.

For a simple polygon with `n>=3` sides, each of length at most `L`, suppose `x` is wall-safe and let `r=min_i |x-v_i|>1`. Then

```text
r <= L/(2 sin(pi/n))
L > 2 sin(pi/n).
```

The regular `n`-gon attains equality in the radius bound. In particular, a simple five-edge wall with every side at most `L` can contain a wall-safe point only if `L>2 sin(pi/5)=sqrt((5-sqrt(5))/2)`. If its five original labels started with unit edges and each label moves by at most `epsilon`, then any resulting simple wall with a wall-safe point must satisfy

```text
epsilon > (2 sin(pi/5)-1)/2.
```

## 2. Independent shield proof

Take `x in W_C` and a source point `q` outside the polygon interior. If the segment `[x,q]` first exits at a wall vertex `b`, then `|x-b|>1`; unless `q=b`, source separation gives `|q-b|>=1`. Hence `|x-q|>2`; when `q=b`, the definition gives `|x-q|>1` directly.

Otherwise the first exit `z` lies in the relative interior of one side `ab`, so `z=(1-t)a+tb` for `0<t<1`. For any point `w`, the exact weighted-square identity is

```text
|w-z|^2=(1-t)|w-a|^2+t|w-b|^2-t(1-t)|a-b|^2.
```

For `w=x`, both endpoint distances are strictly greater than one. For nonvertex source `w=q`, both are at least one. Since `t(1-t)<=1/4` and `|a-b|<=L`,

```text
|x-z| > sqrt(1-L^2/4),
|q-z| >= sqrt(1-L^2/4).
```

The point `z` lies on `[x,q]`, so the lengths add. Their sum is strictly greater than `2 sqrt(1-L^2/4)`, which is at least one when `L<=sqrt(3)`. No convexity is used.

For two disjoint-interior polygons, a vertex of one cannot lie in the open interior of the other: the polygon's interior wedge near that vertex would overlap the other interior. Fix `x in W_{C_i}` and `y in W_{C_j}`. The shield just proved, applied inside `C_j`, puts `y` strictly farther than one from every source vertex of `C_i`. At the first exit `z` of `[x,y]` from `C_i`, both `x` and `y` are therefore strictly farther than one from the endpoints of the side containing `z`. The weighted-square identity makes both `|x-z|` and `|y-z|` strictly greater than `sqrt(1-L^2/4)`. They add along `[x,y]`, giving `|x-y|>2 sqrt(1-L^2/4)>=1`.

The strictification step uses only finiteness and openness: each finite packet has positive clearance from the complement of `W_C`; a homothety with factor just above one moves each point continuously within that open set and multiplies every internal pair distance by the factor.

## 3. Sharp edge threshold and exact regression

For any `sqrt(3)<L_0<2`, choose

```text
sqrt(1-L_0^2/4) < h < 1/2,     1 <= H <= L_0.
```

Use the rectangle with vertices `(-L_0/2,0)`, `(L_0/2,0)`, `(L_0/2,-H)`, `(-L_0/2,-H)`, the old source point `q=(0,h)`, and the proposed interior point `x=(0,-h)`. All source points in the rectangle's wall and `q` are unit-separated; `x` is strictly farther than one from all four wall vertices; yet `|x-q|=2h<1`. The choice of `h` is possible exactly because `L_0>sqrt(3)`. Thus any claimed universal shield using only the wall-vertex guards and an edge cap greater than `sqrt(3)` fails: for a proposed cap below two choose such an `L_0` under it, and for a cap at least two choose any `L_0` in `(sqrt(3),2)`.

The frozen exact verifier uses `Fraction` throughout. Its rational instance is `L_0=7/4`, `H=3/2`, `h=49/100`; it checks all source pair distances are at least one, all new-point wall distances are strictly above one with squared minimum `40229/40000`, and the cross distance has square `2401/2500<1`. It also checks a four-edge square with side `3/2` whose center is strictly wall-safe, and 160 exact weighted-square identities. I inspected and reran the verifier from the frozen source commit. Its output certifies these finite examples only; it does not prove the universal shield or winding theorem.

## 4. Independent winding and pentagon-threshold proof

Assume first `r>L/2`. For the principal angular change `theta_i` from `v_i-x` to `v_{i+1}-x`, the cosine-law identity gives

```text
|v_i-v_{i+1}|^2=(r_i-r_{i+1})^2+4 r_i r_{i+1} sin^2(theta_i/2),
```

where `r_i,r_{i+1}>=r`. Since each side is at most `L`, this yields `|theta_i|<=2 asin(L/(2r))`. The polygon has winding number `+1` or `-1` about its interior point, so the sum of absolute principal angular changes is at least `2 pi`. Therefore

```text
2 pi <= n * 2 asin(L/(2r)),
```

which gives `r<=L/(2 sin(pi/n))`. If instead `r<=L/2`, then `r>1` implies `L>2`; for `n>=3`, `2 sin(pi/n)<=sqrt(3)<2`, so the strict necessary condition `L>2 sin(pi/n)` follows, and the radius bound is automatic because `1/(2 sin(pi/n))>=1/sqrt(3)>1/2`. The regular polygon gives equality in the radius bound.

For a simple pentagon obtained by moving each of five original unit-wall labels by at most `epsilon`, the triangle inequality bounds every new side by `1+2 epsilon`. A wall-safe point forces the maximum new side to exceed `2 sin(pi/5)`, giving the stated strict displacement threshold. This is a lower bound on the finite motion size; it does not say such a motion exists or remains feasible against other source points.

## 5. Scope, dependencies, and frontier effect

The finite shield theorem is proved directly from source separation, segment-wall intersection, and the weighted-square identity. It needs no equilibrium, contact manifold, convexity, global minimality, or source minimizer hypothesis. The winding theorem is direct planar geometry. No canonical theorem is needed as a premise.

The result recovers the unit-edge shield used in `C-EMBEDDED-WALL-REFILL` when `L=1` and is compatible with `C-SHORT-WALL-ZERO-CAPACITY`, whose six-edge conclusion specifically assumes all edges have length at most one. The square example prevents transferring that zero-capacity conclusion to all noncontact walls with at most six sides.

The new shield can be used only after an actual configuration has produced a simple polygon with side lengths at most `sqrt(3)` and certified wall-safe capacity. It does not produce a finite motion that opens a unit pentagon; any such motion must move at least one label by more than the displayed positive threshold. It also does not pay a deletion/transversal cost or establish spare capacity. The C-II finite-competitor and source-capacity obligation is unchanged.

| Claim | Verdict | Disposition |
| --- | --- | --- |
| Strict `sqrt(3)` shield for a source-vertex polygon | PASS | Promote as `C-NONCONTACT-WALL-STRICT-SHIELD` |
| Joint separation of packets in pairwise disjoint polygon interiors | PASS | Include in the same shield theorem |
| Winding radius / edge-length barrier | PASS | Promote as `C-WALL-SAFE-WINDING-BARRIER` |
| Five-edge finite activation displacement bound | PASS | Promote as `C-UNIT-PENTAGON-ACTIVATION-THRESHOLD` |
| Edge cap above `sqrt(3)` under vertex guards alone | REGRESSION VALID | Promote as `C-NONCONTACT-WALL-SQRT3-THRESHOLD-REGRESSION` |
| Residual-cage refill after contact opening | CONDITIONAL ONLY | Do not promote without an actual feasible finite opening and paid surplus |
| C-II or Level I closure | NOT PROVED | Both remain open |
