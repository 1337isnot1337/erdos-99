> Generated reading edition · [exact source](../../../docs/reports/target_c_full_source_constant_perimeter_defect_2026-09-10.md) · source SHA-256 `ea29ba864bf0fb226a2051bd57a081c2c799c1390a567b3e88becb2625d120f6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-91B24787F9FC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_full_source_constant_perimeter_defect_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=8e849b26d675c48dfac8a957af9f2476e2cb8348; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — the full source hull has an absolute perimeter defect

**Date:** 2026-09-10  
**Repository state:** PR #178 after AS commit `5aca28a65e3e7eedc05e968f6bd8e7e8e07f6088`  
**Run type:** exact whole-source geometric sharpening  
**Target:** Target C C-II / shared global-source geometry  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md` with the promoted September 9 C-I correction  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Let `A` be any global minimum-diameter unit-separated source, not necessarily
triangle-free, and put

```math
K=\operatorname{conv}A,
\qquad
D=\operatorname{diam}A,
\qquad
P=\operatorname{per}K.
```

The exact whole-source Oler/lattice allowance already implies

```math
\delta_K:=\frac\pi4D^2-\operatorname{area}K
<\frac{\sqrt3}{4}P.
```

Combining this with the planar isoperimetric inequality gives the stronger exact
perimeter statement

```math
\boxed{
0\le\pi D-P<\frac{\pi\sqrt3}{2}.
}
\tag{CP.1}
```

Thus every global source hull has perimeter within an **absolute constant** of the
maximum possible perimeter `pi D`.  This sharpens the previously used conclusion
`P=pi D-O(1)` from the whole-source area deficit and is independent of Target C's force
hull.

---

## 1. Starting endpoint

For

```math
a_0=\frac{\sqrt3}{2},
\qquad
c_0=\frac{\sqrt3}{4},
```

define the full-source Oler surplus

```math
\mathscr O_A
=\operatorname{area}K+c_0P-a_0(n-1).
```

Oler gives

```math
\mathscr O_A\ge0.
\tag{1.1}
```

The strict translated-triangular-lattice comparison at the global minimum diameter
`D(n)` gives

```math
\boxed{
\delta_K+\mathscr O_A<c_0P.
}
\tag{1.2}
```

Therefore

```math
\boxed{
0\le\delta_K<c_0P.
}
\tag{1.3}
```

The existing reports use `P<=pi D` to conclude only `delta_K=O(D)`.  The same two
inequalities contain a stronger perimeter consequence.

---

## 2. Theorem CP — absolute full-source perimeter defect

### Theorem CP.1

Every global minimizer satisfies

```math
\boxed{
\pi D-\operatorname{per}(\operatorname{conv}A)
<\frac{\pi\sqrt3}{2}.
}
```

### Proof

The planar isoperimetric inequality gives

```math
P^2\ge4\pi\operatorname{area}K
=\pi^2D^2-4\pi\delta_K.
```

Hence

```math
(\pi D-P)(\pi D+P)
=\pi^2D^2-P^2
\le4\pi\delta_K.
\tag{2.1}
```

By (1.3),

```math
4\pi\delta_K
<4\pi c_0P
=\pi\sqrt3\,P.
\tag{2.2}
```

Combining (2.1) and (2.2),

```math
\pi D-P
<\pi\sqrt3\,
\frac{P}{\pi D+P}.
\tag{2.3}
```

Cauchy's perimeter--diameter inequality gives `P<=pi D`, so

```math
\frac{P}{\pi D+P}\le\frac12.
```

Substitution in (2.3) proves CP.1. `square`

### Scope

The proof uses only the exact whole-source global-optimality allowance, Oler, planar
isoperimetry, and the perimeter--diameter inequality.  It therefore applies to every
global minimizer, before triangle-freeness, contact minimization, diameter-pair
minimization, or any KKT normalization.

---

## 3. Width form

Cauchy's width formula is

```math
P=\int_0^\pi w_K(\theta)\,d\theta.
```

Since every width is at most the diameter,

```math
0\le D-w_K(\theta).
```

Therefore CP.1 is exactly the integrated width-defect bound

```math
\boxed{
\int_0^\pi
\bigl(D-w_K(\theta)\bigr)\,d\theta
<\frac{\pi\sqrt3}{2}.
}
\tag{CP.2}
```

The average width deficit of the full source is therefore strictly below `sqrt(3)/2`,
uniformly in the cardinality.

This does **not** imply pointwise `O(1)` width deficit.  Narrow angular dents can have
larger depth; any pointwise conversion needs the support-function Lipschitz geometry or
a separate Bonnesen argument.

---

## 4. Consequences for the AS annular normal form

Let `F` be the post-ZF force hull.  In the AS low-surplus branch, MP gives for every
fixed `lambda_0<lambda_disk` a constant `epsilon(lambda_0)>0` such that

```math
\operatorname{per}F\le(\pi-\epsilon)D.
```

CP.1 then gives the exact boundary separation

```math
\boxed{
P_K-P_F
\ge
\epsilon D-\frac{\pi\sqrt3}{2}.
}
\tag{CP.3}
```

Thus the quadratic saturated external annulus from AS is bounded externally by a
source hull whose perimeter is maximum up to `O(1)`, while its inner force hull loses a
fixed linear amount of perimeter.

Combined with AS,

```math
Z_{ext}
=\frac2{\sqrt3}
\bigl(\operatorname{area}K-\operatorname{area}F\bigr)+O(D),
```

so the remaining low-surplus branch simultaneously has:

1. an `O(1)` outer perimeter defect;
2. an `Omega(D)` outer-minus-inner perimeter gap;
3. an `Omega(D^2)` annular area;
4. triangular-density-saturated external isolated population up to `O(D)` points.

This is a substantially narrower finite-container problem than an arbitrary dense
isolated filling.

---

## 5. Exact target implication

CP does not by itself prove the C-II contradiction

```math
b+Q>2h
```

or produce a smaller-diameter `n`-point configuration.  Its value is boundary-order:
the full source has only constant perimeter slack left, while every low-surplus force
hull below the MP threshold has linear perimeter slack.

A closing annular rearrangement can therefore spend at most `O(1)` uncertainty on the
outer convex boundary.  The unresolved `O(D)` loss is entirely the inner-interface /
packing-boundary term exposed by AV.

---

## 6. Exact remaining lemma

> **ASR+ — saturated annulus with constant outer defect.**  In the AS low-surplus
> regime, use
> 

```math
> \pi D-P_K<\pi\sqrt3/2,
> \quad
> P_K-P_F=\Omega(D),
> \quad
> Z_{ext}=\frac2{\sqrt3}A_{ann}+O(D),
> 
```
> and `s_ext=1+O(D^{-1})` to obtain either a cardinality-preserving strict sub-`D`
> rearrangement or an exact post-ZF boundary surplus.
>
> The proof must control the inner annulus boundary at `O(D)` accuracy; the outer
> perimeter is no longer a macroscopic source of error.

---

## 7. Regression audit

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | its convex hull perimeter is itself `pi D-O(1/D)` and satisfies CP |
| unit square and finite small optima | yes | CP is an inequality, not an asymptotic classification |
| dense artificial shell filling | not in scope for CP unless globally optimal | CP's decisive input is the strict `D(n)` lattice comparison |
| Reuleaux constant-width body | not a source counterexample | CP only bounds perimeter; it does not claim central symmetry or disk shape |
| AS external annulus | compatible | CP sharpens its outer boundary error but does not remove the inner-interface loss |

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `delta_K<c_0P` | already available | exact whole-source allowance plus Oler nonnegativity |
| CP.1 absolute perimeter defect | proved | isoperimetry + exact allowance + Cauchy |
| CP.2 integrated width defect | proved | Cauchy's width formula |
| CP.3 linear `P_K-P_F` in MP low-surplus branch | proved | CP.1 + MP perimeter deficit |
| pointwise constant-width closeness | not claimed | integrated width control alone does not give it |
| Level I | still open | ASR+ / high-surplus branch remain |

---

## 9. Canonical promotion recommendation

**Promote after independent audit.**

CP.1 is short, exact, source-level, and depends only on already canonical whole-source
inputs.  It should be recorded in the shared Oler/source geometry module rather than
left only in Target C if the audit confirms the strict translated-lattice comparison
used in (1.2).

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

CP theorem for every global source:
    delta_K + O_A < (sqrt3/4)P,
    O_A>=0,
so
    delta_K < (sqrt3/4)P.
Isoperimetry gives
    (pi D-P)(pi D+P) <= 4pi delta_K < pi sqrt3 P.
Since P<=pi D,
    pi D-P < pi sqrt3/2.
Equivalently
    integral_0^pi (D-w_K(theta)) dtheta < pi sqrt3/2.

In the MP/AS low-surplus branch:
    P_K-P_F >= epsilon D-pi sqrt3/2,
while
    Z_ext=(2/sqrt3)area(K\F)+O(D),
    area(K\F)=Omega(D^2),
    s_ext=1+O(1/D).
The outer convex boundary now has only O(1) perimeter slack.
```
