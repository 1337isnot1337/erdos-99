> Generated reading edition · [exact source](../../../docs/audits/target_c_near_triangular_chart_double_port_localization_independent_audit_2026-10-09.md) · source SHA-256 `80296f8058e0ce7781a5d4647ec92a584133e3b262b533b147638e0a4b8c8536`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-EBDDB9EE9EA2","canonical":true,"claim_ids":["C-NEAR-TRIANGULAR-CHART-DOUBLE-PORT-LOCALIZATION"],"claim_statuses":{"C-NEAR-TRIANGULAR-CHART-DOUBLE-PORT-LOCALIZATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: near-triangular double-port localization

## Frozen source and authority

- Audit base: `origin/main=a3e2e83b6c0dc4534a053215c1024d76c8b875a9`, state `2026-10-09.audit.213`.
- Frozen source: `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate: Lemma 9.1 and Corollary 9.2 of `docs/reports/target_c_localized_curved_boundary_slow_lattice_deformation_2026-10-09.md`, SHA-256 `2bc5da1876e0b2cd079fe2c533b62c8d884a61d845a90cb652dcfbcf28cf5a48`.
- The report and source tip were re-read from the frozen commit. The source branch and its worktree were not modified.

## Exact claim promoted

Let `D` tend to infinity through finite unit-separated planar sources. For each source, let a supplied chart have map
```math
\phi(\lambda)=\lambda+g(\lambda),\qquad \lambda\in X\subset \Lambda=\mathbb Zu+\mathbb Zv,
```
where `u,v` are unit vectors with angle `theta` in `[pi/3, pi/3+K_0/D]` and `g` is `K/D`-Lipschitz on `X`, for fixed `K,K_0`. If a source point `p` has two distinct actual unit neighbors `a=phi(lambda_a)` and `b=phi(lambda_b)` in this chart, then for all sufficiently large `D` there is a label `lambda_p` in the full lattice `Lambda` such that
```math
|\lambda_p-\lambda_a|\le C_{K,K_0},\qquad
|p-[\lambda_p+g(\lambda_a)]|\le C_{K,K_0}D^{-1/2}.
```
The label `lambda_p` need not belong to the chart domain or represent a source point. The claim uses neither triangle-freeness, actual-diameter endpoint status, global optimality, nor KKT hypotheses.

## Independent reconstruction

Set `w=b-a` and `w_theta=lambda_b-lambda_a=iu+jv`. Since `a,b` are distinct source points with a common unit neighbor, unit separation and the triangle inequality give `1<=|w|<=2`. The chart lower-Lipschitz estimate gives
```math
|w_theta|\le 2/(1-K/D).
```
For sufficiently large `D`, `theta` is just above `pi/3`; the least eigenvalue of the basis Gram matrix is `1-cos(theta)>=1/2`. Hence `i^2+j^2<=8` after increasing the fixed onset in `D`. In particular the integer pair is nonzero and uniformly bounded.

Let `v_0` be the unit vector obtained from `u` by rotation through `pi/3`, and put `w_0=iu+jv_0`. The chart perturbation is at most `(K/D)|w_theta|=O_K(D^{-1})`, while `|v-v_0|=O_{K_0}(D^{-1})`; bounded `i,j` therefore give
```math
|w-w_0|=O_{K,K_0}(D^{-1}).
```
The triangular squared norm `Q=i^2+ij+j^2=|w_0|^2` is a positive integer. From `1<=|w|<=2` and the preceding perturbation bound, for sufficiently large `D` it satisfies `1<=Q<=4`. The value `2` is impossible because `4Q=(2i+j)^2+3j^2` cannot be congruent to `8` modulo `3`. Thus `Q` is `1`, `3`, or `4`.

For `Q=1`, the two intersections of the unit circles centered at `0,w_0` are the rotations of `w_0` by `+/-pi/3`, hence triangular-lattice points. For `Q=3`, the six possible vectors are rotations by multiples of `pi/3` of `u+v_0`; its two common unit neighbors are `u` and `v_0`, also lattice points. For `Q=4`, `w_0` is twice a triangular-lattice unit vector, so the tangent intersection `w_0/2` is a lattice point. This yields a triangular-lattice intersection `z_0` for either actual circle-intersection branch.

For `|x|,|y| in [1,2]`, the unit-circle intersection formula
```math
F_\pm(x)=x/2\ \mathord\pm\ (Jx/|x|)\sqrt{1-|x|^2/4}
```
has a uniform one-half-Hölder modulus: normalization is Lipschitz on this annulus and `|sqrt(s)-sqrt(t)|<=sqrt(|s-t|)` for nonnegative `s,t`. Since `p-a=F_\pm(w)` for one sign, this gives `|p-a-z_0|=O_{K,K_0}(D^{-1/2})`, including the tangent `Q=4` case. The bounded triangular-lattice vector `z_0` is within `O_{K_0}(D^{-1})` of a vector with the same integer coefficients in the supplied basis `(u,v)`. Adding `a=lambda_a+g(lambda_a)` proves the stated conclusion and the bound on `|lambda_p-lambda_a|`.

The source verifier `research/verify_target_c_two_port_triangular_limits_2026_10_09.py` was inspected and rerun from the frozen commit. Its SHA-256 is `f49ca51e55985cda3840b0d6675655489ac2534e9ad78ac94539e87e44702cee`; it reports 18 eligible integer vectors, six for each norm `1,3,4`, and 30 corresponding circle intersections. This finite check agrees with the explicit classification above; it does not check the perturbation estimates or the asymptotic localization.

## Scope, compression, and frontier effect

- **Verdict:** PASS — promote `C-NEAR-TRIANGULAR-CHART-DOUBLE-PORT-LOCALIZATION` with no nontrivial canonical dependency.
- Corollary 9.2's `O(D^(4/5))` endpoint count is not promoted as a separate claim: its near-triangular chart family is a subclass of the arbitrary slow rhombic charts in canonical `C-SLOW-CHART-DOUBLE-PORT-COUNT` (Audit.218).
- The lattice label is only a positional approximation. It does not give chart occupancy at that label, extend a chart across ports, extract a chart family, or provide a finite source motion. All source points, including contact isolates, remain retained. C-II and Level I remain open; the Target C frontier is unchanged.
