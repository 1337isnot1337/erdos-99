> Generated reading edition · [exact source](../../../docs/reports/target_c_linear_star_tail_2026-09-09.md) · source SHA-256 `d540255c54900c0345faea79b18c6fa434635040e6a9f018023b2e8b48038f12`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-501CF508A12A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_linear_star_tail_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=547c4a366b3eb8c6e0a319dd875342daa689c839; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — linear unweighted tail in the mechanical stress-star phase

**Date:** 2026-09-09  
**Repository state:** post-ZF main through `be9cbfb78cbda059fb4c2581118b236729cfad84`, plus the diameter-direction bounds in PR #112  
**Run type:** exact geometric consequence / near-star sharpening  
**Target:** Target C C66-C76 near-zero response branch  
**Computation:** not used in the proof

## LEVEL I STATUS

`STILL OPEN`

C66 proves that if the response defect is `o(1/D)`, almost all normalized diameter **weight** lies on one star. That statement did not control how many actual diameter edges lie outside the heavy star.

The new post-ZF diameter-edge lower bound, combined with C18's explicit shared-endpoint angle cap, shows the opposite unweighted behavior: every diameter star misses a linear number of actual diameter edges. Thus the surviving near-zero phase has a precise two-scale form:

```text
one star:       1-o(1) of beta mass
outside star:   Omega(D) actual diameter edges,
                but only o(1) total beta mass.
```

This does not close the phase, because no lower bound on individual positive `beta` coefficients is known. It identifies the exact degeneration a closing stability theorem must forbid.

## 1. Finite star-degree bound

Let

```math
\delta_D:=2\arcsin\frac1{2D}.
\tag{1.1}
```

If `by` and `bz` are two distinct diameter edges incident to the same vertex `b`, unit separation of `y,z` gives

```math
\angle ybz\ge\delta_D.
\tag{1.2}
```

C18 gives the global-minimizer upper cone width

```math
\Theta_D:=
\min\left\{
\frac\pi3,
\frac{
D(5\pi/6-\sqrt3)+4\pi/3+\pi/(2D)
}{D+1}
\right\}.
\tag{1.3}
```

All diameter partners of a fixed vertex lie in one angular interval of width at most `Theta_D`.

### Theorem ZV.1 — finite diameter-star capacity

For every diameter vertex `b`,

```math
\boxed{
\deg_H(b)
\le
1+\left\lfloor\frac{\Theta_D}{\delta_D}\right\rfloor.
}
\tag{ZV.1}
```

### Proof

Order the `deg_H(b)` rays from `b` to its diameter partners inside the C18 cone. Consecutive rays differ by at least `delta_D` by (1.2). Therefore

```math
(\deg_H(b)-1)\delta_D\le\Theta_D.
```

Taking the integer part proves ZV.1. QED.

Since

```math
D\delta_D\to1,
\qquad
\Theta_D\to
\theta_\infty:=\frac{5\pi}{6}-\sqrt3
=0.8859430704\ldots,
```

we obtain

```math
\boxed{
\limsup\frac{\Delta(H)}D
\le
\theta_\infty.
}
\tag{ZV.2}
```

## 2. Every star misses linearly many actual diameter edges

PR #112 proves for every unbounded post-ZF survivor

```math
\liminf\frac hD
\ge
\tau_*:=1.4781702664\ldots,
\tag{2.1}
```

where `tau_*` is the unique root of

```math
\tau=2\cos(\tau/2).
```

For a vertex `z`, let

```math
H_{\bar z}:=\{e\in H:z\notin e\}.
```

Then

```math
|H_{\bar z}|=h-\deg_H(z).
```

Combine (2.1) and ZV.2.

### Corollary ZV.2 — universal linear off-star tail

Uniformly over the choice of star center,

```math
\boxed{
\liminf
\frac{\min_z|H_{\bar z}|}{D}
\ge
\tau_*-	heta_\infty
=0.5922271960\ldots .
}
\tag{ZV.3}
```

Thus no post-ZF survivor is even combinatorially close to one diameter star: every vertex misses at least `(0.592227-o(1))D` actual diameter edges.

If in addition `n-v=o(D^2)`, PR #112 gives

```math
\liminf h/D\ge1.6542536485\ldots,
```

and hence the dense-core tail strengthens to

```math
\boxed{
\liminf
\frac{\min_z|H_{\bar z}|}{D}
\ge
0.7683105781\ldots .
}
\tag{ZV.4}
```

## 3. Interaction with C66 mechanical stress concentration

For the relative-interior normalized KKT stress, C66 defines

```math
\varepsilon:=\sum_{b<k}c_{bk}-1
=\frac12\operatorname{tr}(\Lambda-L_H)>0
```

and proves that there is a diameter vertex `z` such that

```math
\sum_{e\ni z}\beta_e
\ge
1-C_{66}D\varepsilon,
\tag{3.1}
```

where `C_66=2\pi/\kappa_0` is the absolute constant in C66.21.

Since the total diameter weight is one,

```math
\boxed{
\sum_{e\in H_{\bar z}}\beta_e
\le C_{66}D\varepsilon.
}
\tag{ZV.5}
```

Combine this with ZV.3. In the near-zero phase

```math
D\varepsilon\to0,
```

there are at least `(0.592227-o(1))D` actual off-star edges but their **total** normalized KKT weight tends to zero. In particular their mean coefficient satisfies

```math
\boxed{
\frac{1}{|H_{\bar z}|}
\sum_{e\in H_{\bar z}}\beta_e
=O(\varepsilon)=o(1/D).
}
\tag{ZV.6}
```

This is stronger than saying merely that the full diameter graph is not a star.

## 4. Why this still does not close C-II

Relative-interior support only guarantees

```math
\beta_e>0
\quad(e\in H).
```

It gives no configuration-uniform lower bound on a positive coefficient. A growing KKT polytope can therefore, in principle, contain a full-support stress with linearly many coefficients much smaller than `1/D`.

The regular local equilibrium regressions in the repository already warn against trying to manufacture such a coefficient floor from vertex degree alone.

Thus ZV turns the C66 near-zero branch into the following exact stability target:

> **Linear-tail stress theorem.** Exclude a sequence of actual global sources in which at least `cD` strong diameter edges carry total normalized diameter weight `o(1)` while the complementary star carries `1-o(1)`.

A proof must use more than positivity of KKT coefficients. Natural remaining inputs are:

- ZR maximal scalar stress rank;
- ZM's `Omega(D)` terminal-disjoint non-diameter response matching;
- the exact ZE/ZT/ZU post-ZF ledgers;
- the force-hull area/perimeter lower bounds from PR #112;
- contact-network equilibrium / reciprocal mixed area.

## 5. Regression audit

- A genuine diameter star is already excluded by ZV.3 in the post-ZF asymptotic regime.
- A double-star or longer caterpillar can have linearly many edges outside the heavy star, so ZV does not falsely classify the full graph.
- Tiny positive coefficients remain allowed; no unsupported conductance or stress floor is asserted.
- The `n=8` heptagon-center example is outside the large post-ZF regime.
- Regular odd shells are compatible with the unweighted statement; their diameter graph is far from a star and their natural symmetric stress does not lie in the C66 near-zero phase.

## 6. Exact remaining endpoint

The direct Level I endpoint remains

```math
\boxed{b+Q>2h.}
```

The response-side alternative is now narrower:

1. either `D epsilon` is not small, in which case a quantitative response/packing theorem is needed;
2. or `D epsilon->0`, in which case C66+ZV forces a heavy star plus at least `0.592227D` actual off-star edges of vanishing total weight.

The second phase is the sharper target produced here.
