> Generated reading edition · [exact source](../../../docs/reports/target_c_groemer_stability_explicit_surplus_2026-09-09.md) · source SHA-256 `280e874604a1b92f62a2cdd49c4e600f919966bc3bd70238f9ac3c326b97e88b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C34771931AA3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_groemer_stability_explicit_surplus_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=f1ec9b6149cccee9ed83e7cf3c4517d480fd3aea; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Groemer stability makes the post-PI surplus gap explicit

**Date:** 2026-09-09  
**Run type:** quantitative convex-stability import / explicit branch exclusion  
**Target:** Target C C-II after ZF/DB/PI/JC/JN  
**Depends on:** JC joint cavity budget with actual force-hull perimeter, PI area floor, GU attachment-cell upper bound, Groemer's 1988 Rosenthal--Szász stability theorem, Blaschke--Lebesgue  
**External source:** H. Groemer, *Stability Theorems for Convex Domains of Constant Width*, Canadian Mathematical Bulletin 31 (1988), 328--337, DOI 10.4153/CMB-1988-048-3, Theorem 2.  
**Computation:** decimal evaluation only; all inequalities are explicit

## LEVEL I STATUS

`STILL OPEN`

JN proves nonconstructively that the JC threshold

$$
\lambda_1=0.4633168953789\ldots
$$

is separated from the true feasible region by a positive constant. Groemer's explicit stability theorem makes part of that gap numerical.

The result is

$$
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_G
=0.4647922503\ldots .
}
\tag{GS.1}
$$

The chosen split constant is deliberately simple rather than numerically optimized:

$$
\boxed{\varepsilon_*=0.0096=\frac6{625}.}
\tag{GS.2}
$$

---

## 1. Groemer's perimeter stability theorem

Normalize a planar convex body `K` to diameter one. Groemer's Theorem 2 states that if

$$
\operatorname{per}(K)\ge\pi-\varepsilon,
\tag{GS.3}
$$

then there exists a convex body `C` of constant width one such that

$$
K\subseteq C
$$

and

$$
\boxed{
d_H(K,C)
\le
c_G\varepsilon^{2/3},
\qquad
c_G:=\frac{34}{25}.
}
\tag{GS.4}
$$

The exponent `2/3` is sharp in Groemer's theorem; no stronger stability exponent is being assumed.

Let

$$
\delta:=c_G\varepsilon^{2/3}.
$$

Since `K subset C` and the Hausdorff distance is at most `delta`,

$$
C\subseteq K+B(0,\delta).
$$

Steiner's formula gives

$$
\operatorname{area}(C)
\le
\operatorname{area}(K)
+\delta\operatorname{per}(K)
+\pi\delta^2.
\tag{GS.5}
$$

The Blaschke--Lebesgue theorem gives every constant-width-one body the area floor

$$
\operatorname{area}(C)
\ge
A_{BL}:=\frac{\pi-\sqrt3}{2}.
\tag{GS.6}
$$

Using `per(K)<=pi`, GS.5--GS.6 imply

$$
\boxed{
\operatorname{area}(K)
\ge
A_{BL}-\pi\delta-\pi\delta^2.
}
\tag{GS.7}
$$

This is the only quantitative stability input needed below.

---

## 2. The actual-perimeter form of the JC cavity bound

Let

$$
p:=\frac{\operatorname{per}(F)}D,
\qquad
\lambda:=\frac{e_{BB}+2s_C}{D},
\qquad
 t:=\frac{e_{BB}}D.
$$

JC's proof before replacing the force-hull perimeter by `pi D` gives

$$
\boxed{
E_{out}+Q
\le
 e_{BB}+\min\{h,\operatorname{per}(F)-h\}.
}
\tag{GS.8}
$$

Since `0<=h<=per(F)`, the minimum is at most half the perimeter:

$$
E_{out}+Q
\le
 e_{BB}+\frac12\operatorname{per}(F).
\tag{GS.9}
$$

Therefore the joint pocket/exceptional cavity capacity satisfies

$$
\boxed{
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
\frac{(t+p/2)^2}{4\pi}.
}
\tag{GS.10}
$$

Since `t<=lambda`, a convenient one-parameter relaxation is

$$
\boxed{
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
\frac{(\lambda+p/2)^2}{4\pi}.
}
\tag{GS.11}
$$

ZG/GU adds only `O(D)` to pass from this cavity area to the full attachment gap `G`.

---

## 3. Case I — perimeter at least `pi-epsilon_*`

Assume along an unbounded subsequence

$$
p\ge\pi-\varepsilon_*.
\tag{GS.12}
$$

Apply Groemer to the normalized force hull `D^{-1}F`. Put

$$
\delta_*
:=
\frac{34}{25}\varepsilon_*^{2/3}.
\tag{GS.13}
$$

Then GS.7 gives

$$
\frac{\operatorname{area}(F)}{D^2}
\ge
A_*:=
A_{BL}-\pi\delta_*-\pi\delta_*^2.
\tag{GS.14}
$$

For `epsilon_*=0.0096`,

$$
\delta_*=0.06143\ldots,
$$

and

$$
\boxed{A_*=0.4999246963\ldots>A_{PI}.}
\tag{GS.15}
$$

GU bounds the total attachment-cell area by

$$
\frac\pi4\lambda^2D^2+o(D^2).
$$

Hence

$$
\liminf\frac G{D^2}
\ge
A_*-rac\pi4\lambda^2.
\tag{GS.16}
$$

In the same case GS.11 can still use the universal `p<=pi`, so

$$
\limsup\frac G{D^2}
\le
\frac{(\lambda+\pi/2)^2}{4\pi}.
\tag{GS.17}
$$

Let `lambda_near` be the positive root of

$$
A_*-rac\pi4\lambda^2
=
\frac{(\lambda+\pi/2)^2}{4\pi}.
\tag{GS.18}
$$

Numerically,

$$
\lambda_{near}=0.46528\ldots .
\tag{GS.19}
$$

Thus Case I requires a surplus strictly larger than the final constant GS.1.

---

## 4. Case II — perimeter at most `pi-epsilon_*`

Now assume

$$
p\le p_*:=\pi-\varepsilon_*.
\tag{GS.20}
$$

No stability theorem is needed. PI gives

$$
\frac{\operatorname{area}(F)}{D^2}
\ge
A_{PI}-o(1),
\qquad
A_{PI}=\frac12\sin(2\rho).
\tag{GS.21}
$$

Therefore

$$
\liminf\frac G{D^2}
\ge
A_{PI}-\frac\pi4\lambda^2.
\tag{GS.22}
$$

But GS.11 improves because `p<=p_*`:

$$
\limsup\frac G{D^2}
\le
\frac{(\lambda+p_*/2)^2}{4\pi}.
\tag{GS.23}
$$

Let `lambda_G` be the positive root of

$$
\boxed{
A_{PI}-\frac\pi4\lambda^2
=
\frac{(\lambda+p_*/2)^2}{4\pi}.
}
\tag{GS.24}
$$

Equivalently,

$$
(\pi^2+1)\lambda^2
+p_*\lambda
+\frac{p_*^2}{4}
-4\pi A_{PI}=0.
\tag{GS.25}
$$

Thus

$$
\boxed{
\lambda_G
=
\frac{-p_*+
\sqrt{p_*^2-4(\pi^2+1)(p_*^2/4-4\pi A_{PI})}}
{2(\pi^2+1)}.
}
\tag{GS.26}
$$

With `epsilon_*=0.0096`,

$$
\boxed{
\lambda_G
=0.464792250394\ldots .
}
\tag{GS.27}
$$

Case II therefore requires `lambda>=lambda_G`.

Because Case I has the stronger lower bound GS.19, GS.27 holds universally. This proves GS.1. `square`

---

## 5. Why the improvement is small but real

Groemer's Hausdorff estimate scales as the `2/3` power of the perimeter deficit. To make the resulting Blaschke--Lebesgue area bound exceed PI's already strong

$$
A_{PI}=0.4978566363\ldots,
$$

the perimeter must be extremely close to `pi D`. Consequently the explicit numerical improvement over JC is modest:

$$
0.4647922504-0.4633168954
=0.0014753550\ldots .
$$

JN's compactness theorem still proves that the true gap above `lambda_1` is positive without specifying its size. GS gives a certified explicit portion of that gap.

---

## 6. Regression audit

- Groemer's theorem is applied only to the convex force hull after scaling its actual diameter to one.
- The containing constant-width body `C` is an auxiliary convex body, not a replacement source configuration.
- Steiner is used only to transfer the Hausdorff containment back to a lower area bound for `F`.
- No quantitative stability of Blaschke--Lebesgue is required; only its exact area minimum for constant-width bodies.
- The regular-shell regression is compatible: near-circular shells have perimeter near `pi D` and area above both PI and the Groemer-transferred floor.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| Groemer bound `d_H(K,C)<=(34/25)epsilon^(2/3)` | external theorem | Groemer 1988, Theorem 2 |
| area transfer GS.7 | proved | containment + Steiner + Blaschke--Lebesgue |
| actual-perimeter cavity bound GS.10 | proved | retained JC perimeter variable |
| far-perimeter root `0.4647922504...` | proved | explicit quadratic |
| near-perimeter branch is stronger | proved | Groemer area floor at `epsilon_*=0.0096` |
| universal explicit floor GS.1 | proved | two-case split |
| optimal explicit constant from Groemer | not claimed | split was chosen for simplicity |
| Level I | still open | high-surplus shell remains |

---

## 8. Next target

The current rigorous post-ZF floor is now explicit:

$$
\frac{e_{BB}+2s_C}{D}
\ge0.4647922504\ldots-o(1).
$$

Combined with ZK/DB,

$$
\frac{r_H}{D}
+\frac13\frac{e_{BB}+2s_C}{D}
\ge2\rho-o(1),
$$

so a survivor near this floor has

$$
\frac{r_H}{D}
\ge1.3232395163\ldots-o(1).
$$

The next step should exploit the resulting simultaneous high diameter branching and positive loaded/pinned contact currency, rather than further optimizing a one-dimensional cavity constant.
