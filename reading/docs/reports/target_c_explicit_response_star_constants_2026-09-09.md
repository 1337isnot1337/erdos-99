> Generated reading edition · [exact source](../../../docs/reports/target_c_explicit_response_star_constants_2026-09-09.md) · source SHA-256 `c003949a5cb2b67384cd3e0833c99c600b0cb1974ee92bf2d4ca3e203c0bf6a9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 11 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-B8C116EC5E5D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — E43R: explicit response and stress-star constants from E43

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-explicit-anti-reuleaux`  
**Run type:** exact constant propagation through C44/C45/C66  
**Target:** quantitative Target C response/star branches  
**Depends on:** E43, C44, C45, C66  
**External literature:** none beyond E43's Bezdek–Connelly input  
**Computation:** arithmetic only

## LEVEL I STATUS

**STILL OPEN.**

E43 gives the explicit global anti-Reuleaux constants

```math
\rho_0=\frac{24}{25},
\qquad
\eta_0=\frac1{25},
\qquad
\gamma_0=1-\rho_0^2=\frac{49}{625}.
```

Substituting these values into the existing C44/C45/C66 proofs makes their previously existential constants completely explicit.

---

## 1. C44 has `K_0=30`

C44 defines

```math
K_0=\left\lceil\frac{9\pi}{\rho_0}\right\rceil.
```

With `rho_0=24/25`,

```math
\frac{9\pi}{\rho_0}
=\frac{75\pi}{8}
=29.4524311274\ldots,
```

so

```math
\boxed{K_0=30.}
\tag{E43R.1}
```

Therefore every sufficiently large fully force-visible C-II survivor satisfies one of the two explicit alternatives below.

### Branch A

The total response conductance on terminal pairs of length at most `24D/25` is at least `1/2`. C44 then gives

```math
\boxed{
\operatorname{tr}(\Lambda-L_H)
\ge\gamma_0
=\frac{49}{625}
=0.0784.
}
\tag{E43R.2}
```

### Branch B

There is one unpinned harmonic component `I_r` with long response mass

```math
\boxed{L_r>\frac1{60}.}
\tag{E43R.3}
```

It also has

```math
\boxed{
\operatorname{diam}A_r>\frac{24}{25}D,
}
\tag{E43R.4}
```

```math
\boxed{
\delta_r>\frac{24}{25}D-2,
}
\tag{E43R.5}
```

```math
\boxed{
|A_r|>\frac{8}{25}D+\frac13,
}
\tag{E43R.6}
```

and

```math
\boxed{
t_r>\frac{24}{25}D+1.}
\tag{E43R.7}
```

No hidden constant remains in C44 after E43.

---

## 2. C45 gives a 1.536% component stress fraction

C45 converts Branch B long response mass into contact stress through the componentwise coordinate-energy identity:

```math
\sum_{e\in E_r}\alpha_e
>\frac{\rho_0^2}{2K_0}D^2.
```

Substitute

```math
\rho_0^2=\frac{576}{625},
\qquad
2K_0=60.
```

Then

```math
\frac{\rho_0^2}{2K_0}
=\frac{576}{37500}
=\frac{48}{3125}
=0.01536.
```

Hence Branch B contains one unloaded harmonic component satisfying

```math
\boxed{
\sum_{e\in E_r}\alpha_e
>\frac{48}{3125}D^2
=0.01536D^2.
}
\tag{E43R.8}
```

Since the full normalized contact-stress mass is `D^2`, one component carries more than `1.536%` of the complete stress.

This is an absolute fraction, not `Omega(1)` notation with an unspecified constant.

---

## 3. C66 star concentration becomes explicit

C66 defines

```math
\kappa_0
=\frac{2\gamma_0}{1+2\gamma_0},
\qquad
C_0=\frac{2\pi}{\kappa_0}.
```

With `gamma_0=49/625`,

```math
2\gamma_0=\frac{98}{625},
\qquad
1+2\gamma_0=\frac{723}{625}.
```

Therefore

```math
\boxed{
\kappa_0=\frac{98}{723}
=0.1355463347\ldots,
}
\tag{E43R.9}
```

and

```math
\boxed{
C_0
=\frac{723\pi}{49}
=46.3545201744\ldots .
}
\tag{E43R.10}
```

Let

```math
\varepsilon=\frac12\operatorname{tr}(\Lambda-L_H).
```

C66's near-zero branch now reads:

> There is an actual diameter vertex `z` such that
> 

```math
> \boxed{
> \sum_{h\not\ni z}\beta_h
> \le\frac{723\pi}{49}D\varepsilon.
> }
> \tag{E43R.11}
> 
```

Equivalently,

```math
\boxed{
\sum_{h\ni z}\beta_h
\ge1-\frac{723\pi}{49}D\varepsilon.
}
\tag{E43R.12}
```

Thus a bound such as

```math
D\varepsilon\le10^{-3}
```

already forces more than `95.36%` of the normalized diameter stress onto one star.

---

## 4. Explicit large-defect / structured-cell / stress-star trichotomy

Combining the same constants gives a convenient numerical version of the response frontier.

For every sufficiently large fully force-visible C-II survivor, at least one of the following holds:

1. **absolute response defect**
   ```math
   \operatorname{tr}(\Lambda-L_H)\ge0.0784;
   
   ```

2. **macroscopic harmonic cell**
   one component carries more than `0.01536D^2` contact stress and has attachment diameter greater than `0.96D`;

3. **small trace / star degeneration**
   when the relevant C66 small-defect assumptions are imposed, the nonstar mechanical diameter mass is at most
   ```math
   (723\pi/49)D\varepsilon.
   
   ```

The numbered branches above summarize existing implications and are not asserted to be a new logically disjoint trichotomy beyond the hypotheses of C44/C45/C66. Their purpose is to expose the actual scales after E43.

---

## 5. Effect on the PR #111 bridge branch

PR #111 repeatedly uses the asymptotic condition

```math
D\varepsilon\to0
```

to obtain stress-star concentration, harmonic-cell capture, and radialization.

E43R shows the exact rate entering those arguments:

```math
\tau_z:=\sum_{h\not\ni z}\beta_h
\le46.354521\,D\varepsilon.
```

Thus every later statement of the form `tau_z=o(1)` can, if desired, be made effective after tracing its remaining constants.

E43R by itself does not make the full PR #111 chain explicit because several later reductions still use asymptotic `o(1)` or compactness constants unrelated to C43.

---

## 6. Classification

**Status:** proved exact constant propagation.  
**Level I:** still open.  
**New external literature:** none beyond E43.  
**Strongest new numerical alternatives:** trace gap `0.0784`, harmonic-cell stress fraction `0.01536`, star leakage coefficient `723pi/49`.

## 7. Next exact target

Use E43 directly at the four-point PI level rather than only through response constants.

FAQ proves that the unconstrained fixed-angle maximal quadrilateral perimeter is attained only when three quadrilateral vertices are pairwise diametral. E43 forbids even a uniform neighborhood of that configuration by requiring every triple to contain a pair at most `24/25` of the diameter.

The finite optimization target is therefore:

```math
\max P(ABCD)
```

subject to

- `diam{A,B,C,D}<=1`;
- `AC=BD=1`;
- prescribed diagonal angle `phi` near the HKS/ANS angle;
- for every three vertices, at least one pair has distance at most `24/25`.

An explicit perimeter bound below FAQ's `P_4(phi)` can be inserted into NCS/ANS and should produce a visibly larger explicit surplus improvement.

## 8. Compact handoff

```text
E43R substitutes eta0=1/25 into the existing response stack:
  rho0=24/25,
  gamma0=49/625.
C44:
  K0=ceil(9pi/rho0)=30.
  Branch A: tr(Lambda-L_H)>=49/625=0.0784.
  Branch B: one harmonic component has long response mass >1/60,
            attachment diameter >0.96D,
            graph diameter >0.96D-2,
            |A_r|>8D/25+1/3,
            t_r>0.96D+1.
C45:
  the same component carries >rho0^2/(2K0) D^2
    =48/3125 D^2=0.01536D^2 contact stress.
C66:
  kappa0=98/723,
  C0=723pi/49=46.354520...,
  nonstar beta mass <=(723pi/49)D epsilon.

Next: solve the E43-constrained FAQ quadrilateral problem and feed the sharper perimeter
bound into ANS.
```
