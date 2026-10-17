> Generated reading edition · [exact source](../../../docs/audits/target_c_g0077_atomic_and_residual_floor_hostile_audit_2026-09-15.md) · source SHA-256 `9e8a9a6384659209ad40ad59687e7fdfe97f62e365aeae8f7e917587162a1dc4`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-64C5442AA2A2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — matched `g=0.0077` and residual-coupled floor `1.843577`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_uniform_strong_branch_atomic_gap_0077_2026-09-15.md`
- `research/verify_target_c_uniform_strong_branch_orbit_capacity_gap_0077.py`
- `research/target_c_g0077_residual_stability_floor_1843577_2026-09-15.md`
- `research/verify_target_c_g0077_residual_stability_floor_1843577.py`

**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit attacks the two points where a small numerical strengthening can easily become invalid: the branch condition in the physical center/leaf pair theorem, and the reuse of the endpoint-residual stability argument after changing the matched endpoint from `C76` to `C77`.

---

## 1. The strong physical pair branch still covers the actual capacity optimizer

The physical pair theorem is

```math
\rho\ge
\min\left\{
{e^2\over10},{2m^2\over29}
\right\},
\qquad
 e=(a+b-K)_+,
\qquad
m=\min(a,b),
\qquad
K={2\over\sqrt3}.
```

The `1/10` branch is valid only when

```math
{e\over m}\le\sqrt{20/29}.
```

For the dominant orbit on the interval `C<=W/2`, every leaf satisfies `L<=C`, hence

```math
{(C+L-K)_+\over L}
\le2-{K\over C}
\le2-{2K\over W}
\le2-{2K\over A_0},
```

where

```math
A_0=2\sqrt{\Delta_2}+0.0077.
```

The exact verifier proves

```math
2-{2K\over A_0}<0.79236
<\sqrt{20/29}=0.83045\ldots .
```

Thus the entire strong optimizer interval remains strictly within the stated theorem scope.  No out-of-scope center/leaf application is introduced by the `0.0001` increase.

**Verdict:** PASS.

---

## 2. The capacity optimizer remains in the same branch geometry

For

```math
\Phi(W,C)=C(W-C)-{1\over10}{3C-W\over C}
\left({W+C\over2}-K\right)^2,
```

the parent proof gives `Phi_CC<=-2` on `W/3<=C<=W/2`.  The `0.0077` certificate checks

```math
\Phi_C(W,W/3)>0.6254
```

uniformly over the entire dominant-mass interval, while `Phi_C(W,W/2)<0` analytically.  Hence there is one strong-branch maximizer in `(W/3,W/2)`.

The fallback boundary

```math
C_s(W)=W-{W-K\over\sqrt{20/29}}
```

still obeys

```math
C_s(W)>W/2.
```

Since the fallback `Phi_{2/29}` is decreasing for `C>=W/2`, its maximum occurs at that boundary.  Therefore the two branch maxima used by the certificate are exhaustive.

**Verdict:** PASS.

---

## 3. Residual-orbit optimization is still worst at `W=A_0`

The dominant orbit is accompanied by residual exact-orbit mass at most `A_0-W`, whose generic crossing capacity is `(A_0-W)^2/4`.

The exact certificate proves, after differentiating the strong envelope and subtracting the residual-square derivative,

```math
{d\over dW}
\left[
\Psi_{strong}(W)+{(A_0-W)^2\over4}
\right]
>0.5966,
```

and for the fallback branch the corresponding derivative is greater than `0.8362`.  Thus both exhaustive capacities increase with `W` and are worst at `W=A_0`.

This rules out a hidden interior orbit-mass configuration that could defeat the endpoint tangent calculation.

**Verdict:** PASS.

---

## 4. The exact endpoint margins are positive

At the rational tangent point

```math
c_0=0.935386,
```

strong concavity gives

```math
\max_C\Phi(A_0,C)
\le
\Phi(A_0,c_0)+{\Phi_C(A_0,c_0)^2\over4}.
```

The outward-Fraction verifier gives

```math
\Delta_2-\max_C\Phi(A_0,C)
>6.67\times10^{-6}.
```

The fallback branch has margin greater than

```math
1.39\times10^{-3}.
```

The strong margin is small but still several orders above the rational-enclosure scale used by the certificate.  No floating-point equality is load-bearing.

**Verdict:** PASS.

---

## 5. The strict-rhombus transfer remains legitimate

The parent hostile audits already check that the same physical pair theorem and orbit decomposition can be rerun on the strict-rhombus train graph itself.  The `0.0077` argument changes only the scalar endpoint `A_0`; it does not use singleton trains or an all-train-only hypothesis.

Hence

```math
T_R/D\ge2\sqrt{\Delta_2}+0.0077-o(1)
```

and the standard identity gives

```math
\sigma_R/D\ge0.0154-o(1).
```

**Verdict:** PASS.

---

## 6. Residual stability is symbolic in the matched endpoint

The residual theorem needs three ingredients on `U<=2.013`:

1. `Psi(C_*)<Delta_2` at the matched endpoint `C_*`;
2. every physical capacity branch below `C_*` has slope greater than `0.60`;
3. the generic two-bin residual satisfies `R<0.112`.

Sections 1--4 establish item 1 for `C_*=C77`.  The exact residual verifier rechecks item 2 with the new `C77` and obtains strong/fallback/high-center slope lower bounds greater than `0.60`, `0.84`, and `1.15`, respectively.  Item 3 is independent of the matched endpoint.

Therefore, if `h=U-C77` and `R=U-M`, the same calculation gives

```math
R-h<{R^2\over2.4}
<{0.112\over2.4}R,
```

so

```math
\boxed{R<1.05h.}
```

The `1.05` constant is not specific to `C76`.

**Verdict:** PASS.

---

## 7. Full feasible-triangle monotonicity remains valid

At the proposed safe endpoint

```math
t=1.843577,
```

the exact certificate gives

```math
U_{max}<2.012912<2.013,
```

```math
\delta_{max}<0.050293<0.051,
\qquad
h_{max}<0.100586<0.101.
```

These are within the same conservative box used by the parent residual proof.  With `F'(z)<0.134`, the survivor-capacity derivatives satisfy

```math
Q_x<-2.73,
\qquad
Q_h<-2.56.
```

Thus the weakest feasible point is genuinely the corner

```math
\kappa=0,
\qquad
h=0,
\qquad
U=M=C77.
```

No incompatible separate maxima are combined.

**Verdict:** PASS.

---

## 8. Corner arithmetic and non-conclusions

At the corner, every survivor requires

```math
{1\over2}\left({9t\over2}-2\pi-C77\right)
\ge
F\left(\pi-{t\over2}\right).
```

The exact verifier proves the reverse inequality at `t=1.843577` by more than

```math
1.36\times10^{-6}.
```

The numerical zero is `1.8435775982814395...`, so the rounded theorem value leaves positive margin.

This remains a proof-only Type-II strengthening.  It does not prove an exact unit equilateral triangle, does not construct a strict same-cardinality sub-`D` competitor, and does not address Level I inactive-container quantifiers.

**Final disposition:** **PASS at proof-only full-core Type-II scope.  The matched gap `0.0077` and scalar floor `1.843577` are valid.  C-II remains open.**
