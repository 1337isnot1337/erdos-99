> Generated reading edition · [exact source](../../../docs/reports/target_c_tamvakis_four_endpoint_barrier_2026-09-09.md) · source SHA-256 `24a54610ec6ba81ee6aa0416769f7dd8a33e4c728ffccc7760d9a705bc6ab02a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F10708263898","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — TQB: Tamvakis gives an exact four-endpoint perimeter barrier at the HKS crossover

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** external exact small-polygon theorem import / HKN simplification  
**Target:** quantitative PI/Hemmi equality-shape separation  
**Depends on:** HKS/HKN and Tamvakis's exact unit-diameter quadrilateral perimeter theorem  
**Computation:** arithmetic only  
**Level I:** still open

## 1. Imported theorem

Tamvakis proved that every convex quadrilateral of Euclidean diameter at most one has perimeter at most

$$
\boxed{
P_4^*=2+\sqrt6-\sqrt2
=2+4\sin\frac{\pi}{12}
=3.0352761804100830494\ldots .
}
\tag{TQB.1}

Equality is attained uniquely up to congruence by the Tamvakis kite: three of its vertices form a unit equilateral triangle, and the fourth subdivides one side of the associated Reuleaux-triangle construction.

The original reference is

N. K. Tamvakis, *On the perimeter and the area of the convex polygons of a given diameter*, Bulletin of the Hellenic Mathematical Society (N.S.) 28 (1987), 115–132.

The theorem and uniqueness are also recorded in later isodiametric-polygon surveys, including Mossinghoff and Audet–Hansen–Messine.

No stronger fixed-angle version is imported here.

---

## 2. Exact separation from the HKS crossover perimeter

HKS defines the sharp PI/Hemmi crossover perimeter

\[
\boxed{
p_c=3.0353123194039776374\ldots .}
\tag{TQB.2}

Therefore

\[
\boxed{
\Delta_4:=p_c-P_4^*
=0.0000361389938945880\ldots>0.
}
\tag{TQB.3}

This is a genuine fixed perimeter separation, not an asymptotic `o(1)` statement.

---

## 3. Direct HKN contradiction from the four-point hull

Assume a threshold-approaching sequence as in HKN:

\[
\lambda_j:=\frac{e_{BB,j}+2s_{C,j}}{D_j}
\to\lambda_{HKS}.
$$

HKN already proves, after diameter normalization and Hausdorff convergence,

$$
K_j\to K_\infty,
\qquad
\operatorname{per}(K_\infty)=p_c,
\qquad
\operatorname{area}(K_\infty)=A_c,
$$

and PI supplies two limiting unit-diameter chords whose four-endpoint hull `Q` satisfies

$$
Q\subseteq K_\infty,
\qquad
\operatorname{area}(Q)\ge A_c.
$$

Since `area(K_infty)=A_c`, equality forces

$$
K_\infty=Q.
$$

Thus `K_infty` is a convex polygon with at most four vertices and diameter one. Tamvakis then gives

$$
\operatorname{per}(K_\infty)
\le P_4^*.
$$

But HKN forces

$$
\operatorname{per}(K_\infty)=p_c=P_4^*+\Delta_4>P_4^*.
$$

Contradiction.

### Corollary TQB.1

The HKS threshold is unattainable for the simpler reason

$$
\boxed{
\text{PI equality forces a four-point hull, but every diameter-one four-point hull has perimeter }<p_c.
}
\tag{TQB.4}

This gives an alternative proof of HKN independent of the detailed six-sided Hemmi equality classification once HKS has already identified the scalar crossover and area squeeze.

---

## 4. Why the numerical separation does not yet make the HKN gap explicit

The fixed perimeter gap `Delta_4` is useful but does not by itself produce a numerical lower bound on

\[
\lambda-\lambda_{HKS}.
$$

A near-threshold force hull `K` need not equal the four-endpoint PI hull `Q`; it only has very small excess area above `Q`. To turn `Delta_4` into an explicit surplus gap, one needs a quantitative nested-convex stability estimate of the form

$$
\operatorname{area}(K)-\operatorname{area}(Q)
\ge
\Psi\bigl(\operatorname{per}(K)-\operatorname{per}(Q)\bigr)
$$

for the special diameter-one PI quadrilaterals, with `Psi(delta)>0` explicitly.

Equivalently, one can solve the more tailored finite problem:

> maximize the perimeter of a diameter-one quadrilateral whose two unit diagonals make a prescribed angle `phi` near `p_c/2`.

Numerical optimization at exactly

$$
\phi=p_c/2
$$

suggests the maximum is approximately

$$
3.034910765287793,
$$

strictly below even the global Tamvakis bound. This numerical value is **not used as a theorem** in TQB.

---

## 5. Exact fixed-angle candidate exposed

Parameterize a quadrilateral with unit diagonals `AC=BD=1` crossing at angle `phi` by the intersection fractions

$$
A=a u,
\quad C=-(1-a)u,
\quad B=b v,
\quad D=-(1-b)v,
$$

where `u·v=cos phi`.

A natural boundary candidate has two consecutive unit sides,

$$
AB=BC=1.
$$

Solving those equations gives

\[
\boxed{
b=\frac{\sqrt3}{2\sin\phi},
\qquad
a=\frac12+\frac{\sqrt3}{2}\cot\phi.}
\tag{TQB.5}

The other two side lengths simplify exactly to

\[
\boxed{
CD=\sqrt{2-\sqrt3\sin\phi-\cos\phi},
}
\tag{TQB.6}

\[
\boxed{
DA=\sqrt{2-\sqrt3\sin\phi+\cos\phi}.}
\tag{TQB.7}

Hence the candidate perimeter is

\[
\boxed{
P_{cand}(\phi)
=2+
\sqrt{2-\sqrt3\sin\phi-\cos\phi}
+
\sqrt{2-\sqrt3\sin\phi+\cos\phi}.}
\tag{TQB.8}

At `phi=pi/2`, this is exactly the Tamvakis value `P_4^*`. At `phi=p_c/2`, it evaluates to the numerical value above.

TQB does **not** claim that TQB.8 is the fixed-angle global maximum. Proving or refuting that statement is the next finite optimization target.

---

## 6. Source and regression audit

- Tamvakis's theorem applies to every convex quadrilateral with diameter at most one, so it applies to the PI four-endpoint hull.
- The exact value may be written either `2+sqrt(6)-sqrt(2)` or `2+4 sin(pi/12)`.
- The uniqueness theorem is not needed for TQB.4; only the perimeter upper bound is.
- The fixed-angle candidate TQB.8 is explicitly labeled conjectural as an optimizer; only its algebraic construction is proved.
- TQB does not change the explicit HKS number and does not claim an explicit value for `eta_H`.

## 7. Classification

**Status:** proved report-level HKN simplification using an imported exact classical theorem.  
**Level I:** still open.  
**New external literature:** Tamvakis 1987; theorem independently corroborated by modern isodiametric-polygon surveys.

## 8. Compact handoff

```text
Tamvakis:
Every convex quadrilateral of diameter <=1 has
    P <= P4*=2+sqrt(6)-sqrt(2)=3.035276180410083...,
with unique equality shape.

HKS crossover:
    p_c=3.035312319403977...,
so
    p_c-P4*=3.61389938946e-5 >0.

At a hypothetical HKS threshold sequence, HKN's area squeeze plus PI forces the
normalized force-hull limit to equal the convex hull of four diameter endpoints. Then
Tamvakis gives perimeter <=P4*, contradicting the forced perimeter p_c. This is a
simpler HKN contradiction than invoking the six-sided Hemmi equality classification.

For an explicit gap, solve the fixed-angle finite problem. With unit diagonals at angle
phi, the candidate having AB=BC=1 has
    b=sqrt(3)/(2 sin phi),
    a=1/2+(sqrt(3)/2)cot phi,
    P_cand=2+sqrt(2-sqrt(3)sin phi-cos phi)
              +sqrt(2-sqrt(3)sin phi+cos phi).
At phi=p_c/2 it is numerically 3.0349107653, but global optimality at fixed phi remains
to be proved.
```
