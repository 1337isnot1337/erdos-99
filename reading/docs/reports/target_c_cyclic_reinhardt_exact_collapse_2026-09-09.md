> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_reinhardt_exact_collapse_2026-09-09.md) · source SHA-256 `1a07f3ff7814068e14e4819f435e2f231b2a675a019ba89427931e4836c982af`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EF15A8A43F18","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic unicyclic phase collapses to exact Reinhardt equality

**Date:** 2026-09-09  
**Repository branch:** PR #118, after CY/CG/DP/RP  
**Run type:** exact convex-geometry closure of one cyclic subphase  
**Target:** cyclic primitive endpoint, `d_H=0`  
**Depends on:** CY cyclic endpoint, DA/DP diameter-direction polygon, polygonal isoperimetry  
**External literature:** Datta (1997) and Fejes Tóth (2022) are used only for the equality-family corollary; the exact collapse itself is self-contained  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The preceding RP report proves only an asymptotic Reinhardt-scale match in the cyclic endpoint. In the `d_H=0` subphase one can do substantially better: the DA lower bound and the sharp polygonal-isoperimetric upper bound are monotone in opposite directions and meet at exactly one point.

The result is finite and exact.

### Theorem RE — exact cyclic Reinhardt collapse

Let a sufficiently large cyclic primitive survivor satisfy

$$
d_H=0.
$$

Then

$$
\boxed{
D=\frac1{2\sin(\pi/(2q))},
\qquad
\delta_D:=2\arcsin\frac1{2D}=\frac\pi q.}
\tag{RE.1}
$$

Every projective diameter-direction gap is exactly `pi/q`. Moreover the DA diameter-direction polygon equals the complete difference body:

$$
\boxed{
P_H=F-F,}
\tag{RE.2}
$$

and this common body is the regular `2q`-gon with circumradius `D`.

Consequently the force hull attains Reinhardt's sharp perimeter-diameter bound exactly:

$$
\boxed{
\operatorname{per}(F)=q
=2q\sin\frac\pi{2q}\,D.}
\tag{RE.3}
$$

Thus the `d_H=0` cyclic phase is not merely asymptotically close to the Reinhardt family. It lies on the exact equality locus for every member.

---

## 1. Starting data in the `d_H=0` cyclic phase

CY gives

$$
C=C_q,
\qquad
\operatorname{per}(F)=q,
\qquad
h=q-d_H=q.
\tag{1.1}
$$

There are `q` actual diameter directions. Put them in projective cyclic order and let their positive gaps be

$$
g_1,\ldots,g_q,
\qquad
\sum_{i=1}^q g_i=\pi.
\tag{1.2}
$$

C67/DA gives the exact separation

$$
\boxed{
g_i\ge\delta_D,
\qquad
\delta_D:=2\arcsin\frac1{2D}.}
\tag{1.3}
$$

Therefore

$$
\boxed{q\delta_D\le\pi.}
\tag{1.4}
$$

DA constructs

$$
P_H=D\operatorname{conv}\{\pm u_1,\ldots,\pm u_q\}
\subseteq F-F
\tag{1.5}
$$

and, by concavity of sine under (1.2)-(1.3), proves

$$
\operatorname{area}(P_H)
\ge
D^2\left[(q-1)\sin\delta_D+
\sin((q-1)\delta_D)\right].
\tag{1.6}
$$

Because

$$
D=\frac1{2\sin(\delta_D/2)},
\tag{1.7}
$$

define

$$
\boxed{
\Psi_q(\delta)
:=
\frac{(q-1)\sin\delta+\sin((q-1)\delta)}
{4\sin^2(\delta/2)}.}
\tag{1.8}
$$

Then (1.6) is

$$
\operatorname{area}(P_H)
\ge\Psi_q(\delta_D).
\tag{1.9}
$$

---

## 2. The DA lower envelope is strictly decreasing

The key point missing from the asymptotic RP argument is that `Psi_q` is strictly decreasing on the complete feasible interval

$$
0<\delta\le\frac\pi q.
$$

Split

$$
\Psi_q(\delta)
=
\frac{q-1}{2}\cot\frac\delta2
+
\frac{\sin((q-1)\delta)}{4\sin^2(\delta/2)}.
\tag{2.1}
$$

The first summand is strictly decreasing.

For the second summand put

$$
n=q-1
$$

and

$$
G_n(\delta)
:=
\frac{\sin(n\delta)}{\sin^2(\delta/2)}.
$$

On `0<delta<=pi/q`, one has

$$
0<n\delta<\pi,
$$

so `G_n>0`, and logarithmic differentiation gives

$$
\frac{G_n'(\delta)}{G_n(\delta)}
=n\cot(n\delta)-\cot(\delta/2).
\tag{2.2}
$$

If

$$
n\delta\ge\frac\pi2,
$$

then the first term is nonpositive while the second is positive, so (2.2) is strictly negative.

If

$$
n\delta<\frac\pi2,
$$

put `x=delta/2`. Then `2nx<pi/2`. The function

$$
\frac{\tan y}{y}
$$

is strictly increasing on `(0,pi/2)`, hence

$$
\tan(2nx)>2n\tan x>n\tan x.
$$

All terms are positive, so reciprocation gives

$$
n\cot(2nx)<\cot x.
$$

This is exactly

$$
n\cot(n\delta)<\cot(\delta/2).
$$

Thus (2.2) is again strictly negative.

Therefore `G_n`, and hence both summands in (2.1), are strictly decreasing. We have proved:

### Lemma RE.1

$$
\boxed{
\Psi_q'(\delta)<0
\quad
\left(0<\delta\le\frac\pi q\right).}
\tag{RE.4}
$$

---

## 3. The polygonal upper bound meets the lower envelope at exactly one point

Since `F` has `q` vertices, its difference body is a centrally symmetric convex polygon with at most `2q` sides. Minkowski/Cauchy perimeter additivity gives

$$
\operatorname{per}(F-F)=2\operatorname{per}(F)=2q.
\tag{3.1}
$$

The sharp polygonal isoperimetric inequality for a polygon with at most `2q` sides and perimeter `2q` gives

$$
\boxed{
\operatorname{area}(F-F)
\le
U_q:=\frac{q}{2\tan(\pi/(2q))}.}
\tag{3.2}
$$

At the endpoint `delta=pi/q`,

$$
\sin((q-1)\pi/q)=\sin(\pi/q),
$$

so

$$
\begin{aligned}
\Psi_q(\pi/q)
&=
\frac{q\sin(\pi/q)}{4\sin^2(\pi/(2q))}\\
&=
\frac{q}{2\tan(\pi/(2q))}\\
&=U_q.
\end{aligned}
\tag{3.3}
$$

Now combine all inequalities:

$$
\Psi_q(\delta_D)
\le
\operatorname{area}(P_H)
\le
\operatorname{area}(F-F)
\le U_q.
\tag{3.4}
$$

But (1.4) gives

$$
\delta_D\le\frac\pi q,
$$

and Lemma RE.1 plus (3.3) gives

$$
\Psi_q(\delta_D)
\ge
\Psi_q(\pi/q)
=U_q,
\tag{3.5}
$$

with strict inequality unless

$$
\delta_D=\frac\pi q.
$$

Equations (3.4)-(3.5) therefore force equality everywhere:

$$
\boxed{
\delta_D=\frac\pi q,}
\tag{3.6}
$$

$$
\boxed{
\operatorname{area}(P_H)
=\operatorname{area}(F-F)
=U_q.}
\tag{3.7}
$$

Using the definition of `delta_D`, (3.6) is exactly RE.1.

---

## 4. Every diameter-direction gap is exactly minimal

From (1.2), (1.3), and (3.6),

$$
\sum_i g_i
=\pi
=q\delta_D
$$

while every term obeys `g_i>=delta_D`. Therefore

$$
\boxed{g_i=\delta_D=\frac\pi q
\quad(1\le i\le q).}
\tag{4.1}
$$

Thus the `2q` oriented vectors

$$
\{\pm D u_i\}
$$

are equally spaced on the radius-`D` circle. Hence `P_H` is the regular `2q`-gon of circumradius `D`.

By (1.5),

$$
P_H\subseteq F-F.
$$

Both are two-dimensional compact convex bodies and (3.7) says they have the same area. Proper convex containment would leave positive area between their boundaries. Hence

$$
\boxed{P_H=F-F.}
$$

This proves RE.2.

The polygonal-isoperimetric upper bound (3.2) is also attained, so its equality characterization independently confirms that `F-F` is a regular `2q`-gon.

---

## 5. Exact Reinhardt equality

From RE.1,

$$
2q\sin\frac\pi{2q}\,D=q.
$$

But the cyclic force hull has perimeter exactly `q`. Therefore

$$
\boxed{
\operatorname{per}(F)
=2q\sin\frac\pi{2q}\,D,}
$$

which is RE.3.

The classical Reinhardt inequality states that every convex `q`-gon of diameter `D` satisfies

$$
\operatorname{per}(F)
\le
2q\sin\frac\pi{2q}\,D.
$$

Thus `F` lies on the exact equality locus.

Datta's 1997 equality theorem gives the immediate arithmetic consequence:

$$
\boxed{q\text{ has an odd factor; in particular }q\ne2^r.}
\tag{5.1}
$$

The modern Reinhardt description reviewed by Fejes Tóth identifies every equality polygon as an equilateral polygon inscribed in a suitable Reuleaux polygon. In the terminology of that literature, `F` is a Reinhardt/clipped-Reuleaux polygon.

These literature statements are corollaries only. The Target C collapse RE.1-RE.2 was proved above without importing Reinhardt's theorem.

---

## 6. What this replaces in the cyclic ledger

RP currently records

$$
\pi D-q
=\frac\pi{24D}+O(D^{-2})
$$

and projective gap excess

$$
\sum_i(g_i-\delta_D)=O(D^{-3})
$$

in the `d_H=0` phase.

RE replaces both asymptotic statements by exact equalities:

$$
\boxed{
\pi D-q
=
\pi D-\frac{\pi}{2\arcsin(1/(2D))}
}
$$

with `q delta_D=pi`, and more usefully

$$
\boxed{
\sum_i(g_i-\delta_D)=0.}
\tag{6.1}
$$

There is no residual projective angular defect at any order.

The local normal-cone sum from RP also becomes exact:

$$
\sum_b\left(\theta_b-\deg_H(b)\delta_D\right)
=2(\pi-h\delta_D)=0.
$$

Each summand is nonnegative, hence

$$
\boxed{
\theta_b=\deg_H(b)\frac\pi q
\quad\text{for every loaded vertex }b.}
\tag{6.2}
$$

Thus every local diameter normal cone also attains its minimum-width packing exactly.

---

## 7. Regression audit

### Regular odd shell

A regular odd unit `q`-gon has

$$
D=\frac1{2\sin(\pi/(2q))},
$$

its diameter graph is a `q`-cycle, its projective diameter directions are exactly equally spaced, and `F-F` is the regular `2q`-gon. It attains every equality above. RE therefore retains the principal cyclic regression.

### General Reinhardt polygons

RE does not assert that `F` is regular. The Reinhardt equality family contains nonregular clipped-Reuleaux polygons for many composite `q`. The exact conclusion is `F-F` regular together with the existing Target C stress/diameter conditions; any further primal classification must use the Reinhardt equality theorem or additional Target C structure.

### Power-of-two `q`

Datta's equality classification rules these out in the `d_H=0` phase. This is a genuine finite exclusion but does not settle arbitrary `q`.

### `d_H=1,2`

The proof uses `h=q` essentially. If `h=q-d_H`, the DA lower has fewer direction terms and the exact endpoint match disappears. No conclusion for those phases is claimed here.

---

## 8. New exact endpoint

The `d_H=0` cyclic source now satisfies simultaneously:

1. `F` is a unit-side Reinhardt `q`-gon;
2. `F-F` is exactly the regular `2q`-gon of circumradius `D`;
3. all `q` projective diameter directions are spaced exactly by `pi/q`;
4. every local exterior angle obeys
   $$
   \theta_b=\deg_H(b)\pi/q;
   $$
5. the normalized KKT polytope is two-dimensional (`s_Z=2`);
6. every normalized stress keeps all cycle contacts positive and has maximal scalar rank by CY/CG;
7. the full source still contains `n-q=Theta(D^2)` contact-isolated points in the C65 representative.

The remaining task is therefore an exact Reinhardt/KKT compatibility problem, not an asymptotic stability problem.

---

## 9. Next theorem

Two routes are now sharply defined.

### RE-A — classify the exact diameter graph from Reinhardt equality

Use the clipped-Reuleaux equality representation together with

$$
\theta_b=\deg_H(b)\pi/q
$$

and the canonical diameter-thrackle pseudoforest structure. The aim is to classify the only possible full diameter graphs and then solve the two-dimensional KKT stress polytope explicitly.

### RE-B — exploit the regular difference body

Since

$$
F-F=P_H
$$

is regular, every support-width equality used by the diameter directions is exact. Combine this with the positive unit-contact equilibrium around `C_q` to test whether the only compatible primal shell is the regular odd polygon or a much smaller Reinhardt subclass.

Either route would turn the cyclic `d_H=0` phase into a finite equality-family analysis.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The monotonicity proof and area sandwich are exact. The report depends on the report-level cyclic/DA stack, and the Reinhardt classification is used only after the self-contained exact collapse.

---

## 11. Literature note

The equality-family corollary is consistent with:

- Basudeb Datta, *A Discrete Isoperimetric Problem*, Geometriae Dedicata 64 (1997), 55–68: the Reinhardt perimeter bound is attained iff the number of sides has an odd factor, with finitely many equality classes;
- Gábor Fejes Tóth, *Finite variations on the isoperimetric problem* (2022): survey and modern description of clipped-Reuleaux/Reinhardt equality polygons.

No unreviewed 2026 power-of-two proof candidate is used.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Cyclic d_H=0 gives h=q and q projective diameter gaps g_i>=delta_D with
sum g_i=pi, delta_D=2asin(1/(2D)); hence delta_D<=pi/q.

DA lower:
  area(P_H) >= Psi_q(delta_D),
  Psi_q(delta)=((q-1)sin delta+sin((q-1)delta))/(4 sin^2(delta/2)).

Psi_q is strictly decreasing on (0,pi/q].
Proof: split it as
  (q-1)/2 cot(delta/2)
  + sin((q-1)delta)/(4 sin^2(delta/2)).
The first term decreases. For the second,
  d log G/d delta=(q-1)cot((q-1)delta)-cot(delta/2)<0;
if (q-1)delta>=pi/2 this is immediate, and otherwise monotonicity of tan(x)/x gives it.

Difference-body upper:
  per(F-F)=2q,
  F-F has <=2q sides,
  area(F-F)<=U_q=q/(2tan(pi/(2q))).
At delta=pi/q,
  Psi_q(pi/q)=U_q.
Since P_H subset F-F,
  Psi_q(delta_D)<=area(P_H)<=area(F-F)<=U_q.
But delta_D<=pi/q and Psi_q decreases, so Psi_q(delta_D)>=U_q.
Therefore equality holds throughout and
  delta_D=pi/q,
  D=1/(2sin(pi/(2q))).
All direction gaps equal pi/q; P_H=F-F is the regular 2q-gon.
Hence F attains exact Reinhardt perimeter-diameter equality.
Datta then excludes power-of-two q and identifies the equality locus with the Reinhardt family.

Next: exact Reinhardt/KKT compatibility, not further asymptotic stability.
```
