<!-- theorem-state: {"artifact_id":"ART-50BABAC43702","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — HKN: the sharp Hemmi/PI crossover threshold is uniformly unattainable

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** compactness / incompatible equality-shape theorem  
**Target:** Target C C-II after HKS  
**Depends on:** HKS, PI exact projective-spread theorem, JC/GU area-gap upper machinery, Blaschke selection, Hemmi equality classification in the sharp first branch  
**Computation:** none beyond the already defined HKS constant  
**New external input beyond HKS:** none

## LEVEL I STATUS

**STILL OPEN.**

HKS proves the explicit asymptotic lower bound

\[
\lambda:=\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{HKS}-o(1),
\qquad
\lambda_{HKS}=0.4807218393889119189\ldots .
\]

The crossover value is defined by

\[
p_c=3.0353123194039776374\ldots,
\]

\[
A_c
:=
\frac12\sin\frac{p_c}{2}
=A_H(p_c)
=0.4992941967756003210\ldots,
\]

where `A_H` is the sharp first-branch Hemmi minimum-area function.

The scalar threshold cannot actually be approached. Equality would force two incompatible normalized force-hull shapes:

1. **Hemmi equality:** a genuine six-sided first-branch Hemmi polygon;
2. **PI equality:** the convex hull of the endpoints of two unit-diameter chords, hence a polygon with at most four extreme vertices.

Compactness converts this incompatibility into a uniform positive surplus gap.

### Theorem HKN — strict post-HKS gap

There exists an absolute constant

\[
\boxed{\eta_H>0}
\tag{HKN.1}
\]

such that every sufficiently large audited post-ZF survivor satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{HKS}+\eta_H.
}
\tag{HKN.2}

No explicit value of `eta_H` is claimed.

---

## 1. Assume a threshold-approaching sequence

Suppose for contradiction that there is an unbounded post-ZF survivor sequence with

\[
\lambda_j
:=
\frac{e_{BB,j}+2s_{C,j}}{D_j}
\longrightarrow
\lambda_{HKS}.
\tag{1.1}

Pass to a subsequence on which

\[
p_j:=\frac{\operatorname{per}(F_j)}{D_j}\to p,
\qquad
 y_j:=\frac{h_j}{D_j}\to y,
\qquad
 t_j:=\frac{e_{BB,j}}{D_j}\to t.
\tag{1.2}

HKS divides perimeter into three regimes:

- below `p_c`, the optimized PI/JC required surplus is strictly decreasing in `p`;
- from `p_c` to `p_2=12 sin(pi/12)`, the sharp-Hemmi/JC required surplus is strictly increasing in `p`;
- at and above `p_2`, the coarse Hemmi bound forces a much larger surplus.

By continuity and strict monotonicity, (1.1) is possible only if

\[
\boxed{p=p_c.}
\tag{HKN.3}

---

## 2. Tightness also forces the diameter density to `p_c/2`

JC uses

\[
m_j:=\min\{y_j,p_j-y_j\}
\le\frac{p_j}{2}.
\tag{2.1}

At fixed area floor and perimeter, replacing `m_j` by `p_j/2` only enlarges the allowed cavity and therefore weakens the lower bound on `lambda`.

At `p=p_c`, HKS's threshold equation is

\[
A_c-rac\pi4\lambda_{HKS}^2
=
\frac{(\lambda_{HKS}+p_c/2)^2}{4\pi}.
\tag{2.2}

If along a subsequence

\[
m\le p_c/2-\xi
\]

for some `xi>0`, the right side of the actual JC inequality would be smaller by a fixed amount. Since the left side is continuous and strictly decreasing in `lambda`, a fixed positive increase above `lambda_HKS` would be necessary, contradicting (1.1).

Thus

\[
\boxed{m=p_c/2.}
\tag{HKN.4}

But `0<=y<=p_c` and `min(y,p_c-y)=p_c/2` only when

\[
\boxed{y=p_c/2.}
\tag{HKN.5}

So threshold approach forces

\[
\frac hD\to\frac{p_c}{2}.
\]

---

## 3. The normalized force-hull area must converge to `A_c`

GU gives the attachment-cell area bound

\[
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4\lambda_j^2D_j^2+o(D_j^2).
\tag{3.1}

The actual-perimeter JC cavity estimate and gap charging give

\[
G_j
\le
\frac{(t_j+\min\{y_j,p_j-y_j\})^2}{4\pi}D_j^2
+o(D_j^2).
\tag{3.2}

Since `t_j<=lambda_j`, add (3.1) and (3.2):

\[
\frac{\operatorname{area}(F_j)}{D_j^2}
\le
\frac\pi4\lambda_j^2
+
\frac{(\lambda_j+p_j/2)^2}{4\pi}
+o(1).
\tag{3.3}

By HKN.3 and (1.1), the right side tends to `A_c` by (2.2). Therefore

\[
\limsup_j
\frac{\operatorname{area}(F_j)}{D_j^2}
\le A_c.
\tag{3.4}

On the other hand, for all sufficiently large `j`, `p_j` lies in Hemmi's sharp first branch or arbitrarily close to its crossover neighborhood. HKS gives

\[
\frac{\operatorname{area}(F_j)}{D_j^2}
\ge
\max\left\{
A_H(p_j),
A_{PI}^*(p_j)-o(1)
\right\},
\]

and both lower floors converge to `A_c` as `p_j->p_c`.

Hence

\[
\boxed{
\frac{\operatorname{area}(F_j)}{D_j^2}
\longrightarrow A_c.
}
\tag{HKN.6}

---

## 4. Normalize and take a convex-body limit

Choose translations `x_j` and define

\[
K_j:=D_j^{-1}(F_j-x_j).
\]

Then

\[
\operatorname{diam}(K_j)=1.
\]

After translating into a fixed bounded region, Blaschke selection gives a Hausdorff-convergent subsequence

\[
K_j\to K_\infty.
\tag{4.1}

Diameter, perimeter, and area are continuous for planar convex bodies under Hausdorff convergence. Therefore HKN.3 and HKN.6 give

\[
\boxed{
\operatorname{diam}(K_\infty)=1,
\qquad
\operatorname{per}(K_\infty)=p_c,
\qquad
\operatorname{area}(K_\infty)=A_c.
}
\tag{HKN.7}

Because `A_c=A_H(p_c)`, the limit body attains the sharp Hemmi minimum area for diameter one and perimeter `p_c`.

---

## 5. Hemmi equality makes the limit genuinely six-sided

The sharp first-branch equality classification in Hemmi/Kripfganz says that for

\[
3<L/D<p_2,
\]

the area-minimizing body is a six-sided Hemmi polygon. In the notation of HKS, its side lengths are

\[
2\sin\frac\alpha2
\]

on three alternating sides and

\[
2\sin\left(\frac\pi6-\frac\alpha2\right)
\]

on the other three, where

\[
\alpha\in(\pi/6,\pi/3)
\]

for an interior perimeter `p in(3,p_2)`.

Since

\[
p_c\in(3,p_2),
\]

both side lengths are strictly positive. Thus every sharp Hemmi equality body at `p_c` has six genuine sides and six extreme vertices.

Consequently HKN.7 implies

\[
\boxed{K_\infty\text{ is a genuine six-sided Hemmi equality body}.}
\tag{HKN.8}

---

## 6. PI equality makes the same limit a four-point hull

For each `j`, let

\[
\phi_j
\]

be the maximum projective angle between two actual diameter-edge directions.

PI gives

\[
\phi_j
\ge
\min\left\{
(h_j-1)\delta_{D_j},
\frac\pi2-\delta_{D_j}
\right\},
\tag{6.1}

where

\[
D_j\delta_{D_j}\to1.
\]

Using HKN.5 and `p_c/2<pi/2`,

\[
\liminf\phi_j
\ge
\frac{p_c}{2}.
\tag{6.2}

Choose two actual diameter edges realizing `phi_j`. After the normalization in Section 4, write their four endpoints as

\[
a_j,c_j,b_j,d_j\in K_j,
\]

with

\[
|a_j-c_j|=|b_j-d_j|=1.
\]

Pass to a further subsequence so all four endpoints converge:

\[
a_j\to a,
\quad c_j\to c,
\quad b_j\to b,
\quad d_j\to d
\]

in `K_infty`.

Their limiting diameter segments have projective angle

\[
\phi_\infty\ge p_c/2.
\]

The C67/PI two-diameter formula gives

\[
\operatorname{area}(\operatorname{conv}\{a,b,c,d\})
=
\frac12\sin\phi_\infty
\ge
\frac12\sin\frac{p_c}{2}
=A_c.
\tag{6.3}

But

\[
\operatorname{conv}\{a,b,c,d\}
\subseteq K_\infty
\]

and HKN.7 gives `area(K_infty)=A_c`. Therefore equality holds throughout (6.3):

\[
\boxed{
K_\infty
=
\operatorname{conv}\{a,b,c,d\}.
}
\tag{HKN.9}

Indeed, if a compact convex body properly contains a full-dimensional compact convex polygon, the added point creates positive additional area. Since `A_c>0`, the endpoint hull is full-dimensional.

Thus `K_infty` has at most four extreme vertices.

---

## 7. Contradiction

HKN.8 says the same convex body has six genuine extreme vertices.

HKN.9 says it has at most four.

Contradiction.

Therefore no unbounded post-ZF survivor sequence can satisfy

\[
\lambda_j\to\lambda_{HKS}.
\tag{7.1}

This proves strict nonattainment of the HKS scalar threshold.

---

## 8. Nonattainment gives a uniform positive gap

HKS already proves the universal asymptotic lower bound

\[
\liminf\lambda_j\ge\lambda_{HKS}
\]

for every unbounded survivor sequence.

If HKN.2 failed for every `eta_H>0`, then for each integer `m` one could choose a sufficiently large post-ZF survivor with

\[
\lambda<\lambda_{HKS}+\frac1m.
\]

Choosing diameters increasingly large and using the HKS lower bound produces a diagonal sequence with

\[
\lambda_j\to\lambda_{HKS},
\]

contradicting Sections 1–7.

Hence some absolute `eta_H>0` exists.

The proof is intentionally qualitative. An explicit gap would require a quantitative stability theorem either for the first Hemmi branch or for the PI endpoint-hull equality mechanism.

---

## 9. Relation to the older JN nonattainment theorem

JN used a different incompatible equality pair:

- Rosenthal--Szász equality forced a constant-width limit;
- Blaschke--Lebesgue then forced an area much larger than the old JC threshold allowed.

HKN works at a much stronger scalar floor and a perimeter far below `pi`. Its equality conflict is more discrete:

- sharp Hemmi equality gives six sides;
- PI equality gives at most four extreme points.

Thus HKN is not a numerical refinement of JN. It is a new equality-shape obstruction made possible by the sharp perimeter-diameter theorem.

---

## 10. External source scope

No external theorem beyond HKS is added here.

The equality classification used in Section 5 is part of the same sharp Hemmi solution:

- Hemmi's original 1954 Proceedings paper states that the `(L,D)` problem is solved and divides `3D<L<pi D` into sharp cases;
- Kripfganz Section 5.4 states the problem is qualitatively and quantitatively completely solved, says the lower bounds are attained by Hemmi polyhedra, and in the first case explicitly describes the six-sided Hemmi polygon with three sides of each of two positive lengths.

---

## 11. Classification

**Status:** proved nonconstructive strict improvement over HKS, conditional on the same classical Hemmi equality classification.  
**Level I:** still open.  
**Explicit improved decimal:** not yet; the theorem gives `lambda_HKS+eta_H` for some absolute positive `eta_H`.  
**Computation:** none.

## 12. Next exact target

Quantify the equality-shape separation.

There are two finite routes:

1. **PI quadrilateral perimeter gap:** maximize the perimeter of the convex hull of two unit-diameter chords making angle near `p_c/2`, under the condition that the complete hull still has diameter one. Preliminary exact geometry suggests the maximum at angle `p_c/2` is strictly below `p_c`; proving and quantifying this would turn `eta_H` explicit without any Hemmi stability theorem.
2. **Hemmi stability:** derive a quantitative Hausdorff/area penalty for a diameter-one, perimeter-`p_c` convex body with at most four extreme points relative to the six-sided Hemmi minimum.

The first route is more elementary and currently preferred.

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

HKS threshold lambda_HKS cannot be approached.
Suppose lambda_j->lambda_HKS. Strict monotonicity in HKS forces
    per(F_j)/D_j -> p_c,
    h_j/D_j -> p_c/2.
The GU+JC upper area bound and sharp Hemmi lower area bound squeeze
    area(F_j)/D_j^2 -> A_c=0.5 sin(p_c/2).
Normalize diameter to one and take a Hausdorff limit K.

Because area(K)=A_H(p_c), sharp Hemmi equality classifies K as a genuine six-sided
first-branch Hemmi polygon (both alternating side lengths positive).

PI supplies two unit-diameter chords with limiting projective angle >=p_c/2. Their
endpoint hull Q has
    area(Q)>=0.5 sin(p_c/2)=A_c=area(K).
Since Q subset K, equality forces K=Q, so K has at most four extreme vertices.
Contradiction.

Therefore there exists eta_H>0 such that all sufficiently large post-ZF survivors obey
    (e_BB+2s_C)/D >= 0.4807218393889119... + eta_H.

Next: quantify the gap by maximizing the perimeter of a diameter-one quadrilateral
formed by two unit diagonals at angle p_c/2. Preliminary calculation gives a maximum
below p_c, which would make eta_H explicit.
```
