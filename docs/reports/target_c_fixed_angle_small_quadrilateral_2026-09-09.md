<!-- theorem-state: {"artifact_id":"ART-2BACD0209E5D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — FAQ: exact maximal perimeter of a small quadrilateral with prescribed unit-diagonal angle

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** exact finite convex-geometry theorem / PI equality refinement  
**Target:** explicit HKN four-endpoint geometry  
**Depends on:** elementary Euclidean geometry only  
**External literature:** Tamvakis is used only for comparison, not for the proof  
**Computation:** not used in the proof

## LEVEL I STATUS

**STILL OPEN.**

TQB reduced the explicit HKN gap problem to a finite four-endpoint optimization. That optimization can be solved exactly.

### Theorem FAQ — fixed-angle small quadrilateral

Let `ABCD` be a nondegenerate convex quadrilateral of diameter at most one whose two diagonals satisfy

\[
AC=BD=1.
\]

Let

\[
\phi\in[\pi/3,2\pi/3]
\]

be the smaller oriented angle between the diagonal lines. Then

\[
\boxed{
\operatorname{per}(ABCD)
\le P_4(\phi),
}
\tag{FAQ.1}

where

\[
\boxed{
P_4(\phi)
:=
2+
\sqrt{2-\sqrt3\sin\phi-\cos\phi}
+
\sqrt{2-\sqrt3\sin\phi+\cos\phi}.
}
\tag{FAQ.2}

Equality is attained. Every equality configuration has a three-vertex equilateral triangle of side one among the four quadrilateral vertices.

The function is symmetric under

\[
\phi\mapsto\pi-\phi.
\]

At `phi=pi/2`, FAQ.2 becomes

\[
2+2\sqrt{2-\sqrt3}
=2+\sqrt6-\sqrt2,
\]

recovering Tamvakis's maximal unit-diameter quadrilateral perimeter.

At the HKS angle

\[
\phi_c:=p_c/2
=1.5176561597019888\ldots,
\]

FAQ gives

\[
\boxed{
P_4(\phi_c)
=3.0349107652877701707\ldots,
}
\tag{FAQ.3}

so

\[
\boxed{
p_c-P_4(\phi_c)
=0.0004015541162074667\ldots .}
\tag{FAQ.4}

This is more than eleven times the global Tamvakis separation `p_c-P_4^*` used in TQB.

---

## 1. Convert the quadrilateral to a four-disk intersection

Fix unit vectors `e,v` making angle `phi`. Translate and rotate so

\[
A=0,
\qquad C=e,
\]

and orient `BD` so

\[
B-D=v.
\]

Thus

\[
D=B-v.
\]

The four side lengths are

\[
AB=|B|,
\qquad
BC=|B-e|,
\]

\[
DA=|B-v|,
\qquad
CD=|B-e-v|.
\]

Because the complete quadrilateral has diameter at most one, all four quantities are at most one. Therefore `B` belongs to the compact convex set

\[
\boxed{
K
=B(0,1)\cap B(e,1)\cap B(v,1)\cap B(e+v,1).
}
\tag{FAQ.5}

The perimeter is the convex function

\[
\boxed{
F(x)
=|x|+|x-e|+|x-v|+|x-e-v|.
}
\tag{FAQ.6}

The four disk centers are the vertices of a unit rhombus. Its two vertex angles are `phi` and `pi-phi`, both lying in `[pi/3,2pi/3]`.

A convex function on a compact convex set attains its maximum on the boundary. Thus it suffices to bound `F` on each circular boundary arc of `K`.

---

## 2. One rhombus-vertex boundary arc

Take any one disk center `O`. The two adjacent disk centers are unit distance from `O`; let the angle between their center vectors be

\[
\psi\in[\pi/3,2\pi/3].
\]

After translating `O` to zero and rotating, write the adjacent centers as

\[
e_1=(1,0),
\qquad
e_2=(\cos\psi,\sin\psi).
\]

The opposite rhombus center is `e_1+e_2`.

A point on the active circle is

\[
x=(\cos t,\sin t).
\]

Feasibility with the two adjacent unit disks gives

\[
|x-e_1|\le1,
\qquad
|x-e_2|\le1.
\]

For unit vectors, distance at most one is equivalent to angular separation at most `pi/3`. Hence, after choosing the relevant angular lift,

\[
\boxed{
\psi-\frac\pi3
\le t\le
\frac\pi3.
}
\tag{FAQ.7}

The fourth disk can only shrink this interval, so an upper bound on the whole interval is sufficient.

On this active circle,

\[
F(t)
=1
+2\sin\frac t2
+2\sin\frac{\psi-t}{2}
+\sqrt{3+2\cos\psi-2\cos t-2\cos(\psi-t)}.
\tag{FAQ.8}

---

## 3. The boundary objective is strictly largest at the arc endpoints

Put

\[
\theta:=\frac\psi2,
\qquad
x:=t-\theta.
\]

Then

\[
|x|\le a:=\frac\pi3-\theta\le\frac\pi6.
\]

Write

\[
C:=\cos\theta,
\qquad
R(x):=\sqrt{1+4C^2-4C\cos x}.
\]

Equation FAQ.8 becomes the even function

\[
\boxed{
F(x)
=1+4\sin\frac\theta2\cos\frac x2+R(x).
}
\tag{FAQ.9}

For `x>0`, differentiation gives

\[
F'(x)
=2\sin\frac x2
\left[
-\sin\frac\theta2
+
\frac{2C\cos(x/2)}{R(x)}
\right].
\tag{FAQ.10}

It remains to show the bracket is positive.

All quantities are nonnegative, so square the desired inequality. Put

\[
q:=\cos\frac x2.
\]

Using

\[
\sin^2\frac\theta2=\frac{1-C}{2},
\]

and

\[
R(x)^2=(2C+1)^2-8Cq^2,
\]

one finds exactly

\[
4C^2q^2
-\sin^2\frac\theta2\,R(x)^2
=
\frac{4C^3+8Cq^2-3C-1}{2}.
\tag{FAQ.11}

Now

\[
\frac12\le C\le\frac{\sqrt3}{2}
\]

and

\[
q^2\ge\cos^2\frac\pi{12}
=rac{2+\sqrt3}{4}.
\]

The numerator in FAQ.11 is increasing in both `q^2` and `C` on this rectangle, because

\[
\frac{\partial}{\partial C}
(4C^3+8Cq^2-3C-1)
=12C^2+8q^2-3>0.
\]

At the lower corner it equals

\[
4(1/2)^3
+8(1/2)\frac{2+\sqrt3}{4}
-3(1/2)-1
=\sqrt3>0.
\]

Therefore the bracket in FAQ.10 is strictly positive for every `x>0`.

Hence

\[
\boxed{F(x)\text{ is strictly increasing in }|x|.}
\tag{FAQ.12}

The maximum on every feasible boundary arc occurs at one of the two endpoint angles

\[
t=\frac\pi3
\quad\text{or}\quad
t=\psi-\frac\pi3.
\]

---

## 4. Endpoint value and feasibility

Take

\[
t=\frac\pi3.
\]

Then the distances to `O` and `e_1` are both one. The remaining squared distances are

\[
|x-e_2|^2
=2-\sqrt3\sin\psi-\cos\psi,
\tag{4.1}
\]

\[
|x-e_1-e_2|^2
=2-\sqrt3\sin\psi+\cos\psi.
\tag{4.2}

The endpoint lies in all four disks. Indeed `|x-e_2|<=1` follows from `|psi-pi/3|<=pi/3`, while

\[
|x-e_1-e_2|^2\le1
\iff
1+\cos\psi\le\sqrt3\sin\psi,
\]

which is equivalent to

\[
\cot(\psi/2)\le\sqrt3
\]

and holds for `psi>=pi/3`.

Thus the endpoint value is actually attained and equals

\[
2+
\sqrt{2-\sqrt3\sin\psi-\cos\psi}
+
\sqrt{2-\sqrt3\sin\psi+\cos\psi}.
\tag{4.3}

At the other endpoint the two square-root terms are exchanged.

For the original rhombus, `psi` is either `phi` or `pi-phi`. Since sine is unchanged and cosine changes sign, expression (4.3) is the same in both cases. This proves FAQ.1–FAQ.2.

---

## 5. Equality forces a diametral equilateral triple

At every boundary maximum, the active point has distance one to the active rhombus center and to one adjacent rhombus center. Those adjacent centers themselves are unit distance apart.

Translating this back through FAQ.5 gives one of the four source triples

\[
ABC,\ ABD,\ BCD,\ ACD
\]

with all three pairwise distances equal to one.

Therefore:

### Corollary FAQ.1

Every equality case in FAQ.1 contains a unit equilateral triangle among three quadrilateral vertices.

In the Target C normalization these are three pairwise **diametral** source points. Thus C15 excludes exact FAQ equality for every sufficiently large global minimizer, and C43 gives a uniform neighborhood exclusion.

This equality classification is stronger for Target C than the global Tamvakis uniqueness statement because it applies at every prescribed diagonal angle in `[pi/3,2pi/3]`.

---

## 6. HKS numerical specialization

At

\[
\phi_c=p_c/2,
\]

FAQ.2 gives

\[
P_4(\phi_c)
=3.0349107652877701706750\ldots .
\]

Therefore

\[
p_c-P_4(\phi_c)
=0.00040155411620746672497\ldots .
\]

The global Tamvakis gap was only

\[
p_c-(2+\sqrt6-\sqrt2)
=0.0000361389938945880\ldots .
\]

So using the actual PI diagonal angle enlarges the exact four-point perimeter separation by a factor greater than eleven.

---

## 7. What FAQ changes and what remains

FAQ replaces the conjectural fixed-angle optimization left in TQB by a complete exact theorem.

It gives three new pieces of information for HKN stability:

1. the exact best four-endpoint perimeter at the HKS angle;
2. a substantially larger fixed perimeter separation from `p_c`;
3. an equality condition already forbidden by C15/C43.

It still does **not** by itself turn `eta_H` into a numerical surplus gap. A near-HKS force hull can strictly contain the PI four-endpoint quadrilateral; one needs a quantitative relation between the small excess area and the required extra perimeter/shape.

The finite next target is now sharper:

> **nested PI-hull stability.** If a diameter-one convex body `K` contains a FAQ quadrilateral `Q` with unit diagonals at angle near `phi_c`, and `per(K)` is near `p_c`, give an explicit lower bound on `area(K)-area(Q)`.

Because FAQ gives

\[
\operatorname{per}(Q)\le p_c-0.00040155\ldots,
\]

only a very weak quantitative nested-convex estimate is needed to make the HKN surplus gap explicit.

---

## 8. Regression audit

- The proof uses the complete diameter-one condition on all six quadrilateral distances; without the four side constraints the perimeter can approach four.
- The diagonal angle range `[pi/3,2pi/3]` is essential to the simple arc analysis. The HKS angle lies well inside it.
- The objective maximum-on-boundary step uses only convexity of the sum-of-distances function and convexity/compactness of the four-disk intersection.
- The fourth disk is not ignored: it may shrink the feasible boundary arc, but the proved maximum on the larger adjacent-disk arc is attained at a point that also satisfies the fourth constraint.
- FAQ equality creates a diameter triangle, not a unit-contact triangle. C15/C43, not the original Level I triangle condition, is the relevant exclusion.

## 9. Classification

**Status:** proved exact finite convex-geometric theorem.  
**Level I:** still open.  
**New external literature used in proof:** none.  
**Computation:** none.

## 10. Compact handoff

```text
FAQ fixed-angle quadrilateral theorem:
Let a convex diameter-one quadrilateral have AC=BD=1 and diagonal angle
phi in [pi/3,2pi/3]. Then
  P <= P4(phi)
     =2+sqrt(2-sqrt(3)sin phi-cos phi)
        +sqrt(2-sqrt(3)sin phi+cos phi).

Proof: write B in the intersection of the four unit disks centered at
0,e,v,e+v. The perimeter is the convex sum of distances to those four centers,
so maximize on the boundary. On a boundary circle whose adjacent-center angle is
psi in [pi/3,2pi/3], feasibility restricts t to [psi-pi/3,pi/3]. Centering at
x=t-psi/2 gives
  F(x)=1+4sin(psi/4)cos(x/2)+sqrt(1+4C^2-4C cos x), C=cos(psi/2).
A direct derivative calculation reduces F'(x)>0 for x>0 to
  4C^3+8C cos^2(x/2)-3C-1>0,
whose minimum on the allowed rectangle is sqrt(3)>0. Thus the maximum is an arc
endpoint, yielding the formula above. Endpoints are feasible.

Equality forces three quadrilateral vertices pairwise at distance one. Hence Target C
C15 excludes exact equality for sufficiently large minimizers.

At phi_c=p_c/2:
  P4(phi_c)=3.034910765287770...,
  p_c-P4(phi_c)=0.00040155411620747....
Next: quantitative nested-convex area penalty for adding that missing perimeter.
```
