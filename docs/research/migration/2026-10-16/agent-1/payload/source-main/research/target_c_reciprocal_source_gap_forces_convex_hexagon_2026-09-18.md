# Target C-II — source turn gaps force the minimal reciprocal block to a convex hexagon

**Date:** 2026-09-18  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** the six-point unit-force reciprocal `K_6` forced by a degree-pure minimal one-anchor `K_5` dual block  
**Depends on:** `target_c_one_anchor_k5_reciprocal_unit_force_2026-09-18.md`; `target_c_one_anchor_k5_reciprocal_turn_gap_2026-09-18.md`; `target_c_reciprocal_hull_angle_sign_split_2026-09-18.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The coarse unit-force argument already forces the reciprocal hull to have five or six
vertices.  The source pentagon supplies one more local fact at every non-ground
reciprocal vertex: every cyclic gap between consecutive force directions is strictly
less than `2pi/3`.

Combining these two structures gives a stronger conclusion:

\[
\boxed{
\text{every non-ground reciprocal hull angle is strictly greater than }2\pi/3.
}
\tag{0.1}
\]

The five-vertex hull branch is therefore impossible.  All six reciprocal points are
vertices of a strictly convex hexagon.  Moreover every reciprocal vertex, including the
ground vertex, has a `2+3` sign split.  Consequently, after choosing either sign color,
every signed degree is two or three.

This removes the H5 branch completely and leaves a single convex-hexagon finite target.

---

## 1. Local setup at a non-ground hull vertex

Fix a non-ground reciprocal hull vertex `y_i`.  Put

\[
g_j:={y_i-y_j\over |y_i-y_j|},
\qquad
f_j:=s_{ij}g_j,
\qquad j\ne i.
\tag{1.1}
\]

The raw directions `g_j` point along the five reciprocal edges from the other points
toward `y_i`; multiplying every direction by `-1` would not change any angular span.
Because `y_i` is a hull vertex, the five raw directions lie in an open cone whose width
is the hull interior angle `phi_i<pi`.

The reciprocal equilibrium is

\[
\sum_{j\ne i}f_j=0.
\tag{1.2}
\]

The source-turn theorem says that, because `i` is non-ground, the five force directions
`f_j` are the oriented side directions of the corresponding strict contact pentagon,
and every cyclic gap between consecutive `f_j` is strictly less than

\[
{2\pi\over3}.
\tag{1.3}
\]

The coarse hull-angle theorem already excludes a `0+5` split.  A `1+4` split forces

\[
\phi_i>2\arccos(1/4)>2\pi/3,
\tag{1.4}
\]

so only the `2+3` split needs work.

Assume for contradiction that

\[
\phi_i\le {2\pi\over3}.
\tag{1.5}
\]

Globally reverse the five signs in the local equilibrium if necessary so that the
size-two sign class is positive.  Rotate coordinates so the resultant of those two
unit raw directions lies on the positive real axis.  Their arguments are then

\[
-p,\quad p,
\qquad 0<p<\pi/3,
\tag{1.6}
\]

and their sum is `2 cos p`.

Let the three opposite-sign raw directions have lifted arguments

\[
a<b<c
\tag{1.7}
\]

in the same raw cone.  Their sum equals the two-vector resultant:

\[
e^{ia}+e^{ib}+e^{ic}=2\cos p.
\tag{1.8}
\]

Write

\[
s:={a+c\over2},
\qquad
d:={c-a\over2}.
\tag{1.9}
\]

Because all five raw directions lie in an interval of width at most `2pi/3`,

\[
0<d\le\pi/3.
\tag{1.10}
\]

---

## 2. The source force-gap gives a lower bound on `d`

The two positive force directions are `-p,p`.  The three negative force directions are
`a+pi,b+pi,c+pi`.  Under (1.5), the raw cone and its antipodal copy are disjoint.  The
two cyclic force gaps between these two clusters are therefore

\[
\pi+a-p
\quad\text{and}\quad
\pi-p-c.
\tag{2.1}
\]

Both are strictly below `2pi/3` by (1.3).  Hence

\[
a<p-\pi/3,
\qquad
c>\pi/3-p.
\tag{2.2}
\]

Using `a=s-d` and `c=s+d`, these become

\[
d-s>\pi/3-p,
\qquad
d+s>\pi/3-p.
\]

Therefore

\[
\boxed{
d>\pi/3-p+|s|.}
\tag{2.3}
\]

In particular

\[
p+d-\pi/3>|s|\ge0.
\tag{2.4}
\]

---

## 3. The three-vector equilibrium gives the opposite inequality

From (1.8), the two extreme three-class vectors sum to

\[
e^{ia}+e^{ic}=2\cos d\,e^{is}.
\]

Thus

\[
e^{ib}=2\cos p-2\cos d\,e^{is}.
\]

Taking absolute values and using `|e^{ib}|=1` gives

\[
4\cos^2p+4\cos^2d-8\cos p\cos d\cos s=1.
\tag{3.1}
\]

We now prove the elementary trigonometric inequality

\[
\boxed{|s|\ge p+d-\pi/3}
\tag{3.2}
\]

whenever the right side is nonnegative and `0<=p,d<=pi/3`.

Set

\[
u:=\pi/3-p,
\qquad
v:=\pi/3-d.
\tag{3.3}
\]

Under (2.4), `p+d>pi/3`, hence `u+v<pi/3`.  A direct expansion gives the exact identity

\[
\begin{aligned}
&8\cos p\cos d
\left[\cos(p+d-\pi/3)-\cos s\right]\\
&\qquad=
8\cos(u+v)\sin u\sin v
\ge0.
\end{aligned}
\tag{3.4}
\]

Here (3.1) was used to replace `8 cos p cos d cos s` by
`4 cos^2 p+4 cos^2 d-1`.  Since `p,d<=pi/3`, both cosine factors in the prefactor are
positive.  Also `0<=p+d-pi/3<pi`, and the chosen lifts put `|s|<pi`.  Cosine is strictly
decreasing on `[0,pi]`, so (3.4) implies (3.2).

But (3.2) contradicts the strict reverse inequality (2.4).  Therefore assumption (1.5)
is false:

\[
\boxed{\phi_i>2\pi/3}
\tag{3.5}
\]

at every non-ground reciprocal hull vertex.

The proof is sharp at the forbidden boundary: equality in (3.4) occurs only when one of
`p,d` reaches `pi/3` (or at the trivial endpoint), exactly where the strict source-gap
or general-position hypotheses prevent the limiting configuration from being an
admissible reciprocal block.

---

## 4. The H5 reciprocal hull is impossible

The coarse reciprocal hull theorem leaves only H5 and H6.

Suppose H5 holds.  Its angle sum is `3pi`.

If the ground point `y_0` is interior, all five hull vertices are non-ground, so (3.5)
gives

\[
\sum_{v\in\partial H}\phi_v>5\cdot{2\pi\over3}={10\pi\over3}>3\pi,
\]

impossible.

If the ground point is one of the five hull vertices, the other four hull vertices are
non-ground and contribute more than `8pi/3`.  The coarse unit-force theorem applies at
the ground vertex as well and gives

\[
\phi_0>\arccos(-1/4)>\pi/2.
\]

Therefore

\[
\sum_{v\in\partial H}\phi_v
>{8\pi\over3}+{\pi\over2}
={19\pi\over6}
>3\pi,
\]

again impossible.

Hence

\[
\boxed{\text{H5 is impossible.}}
\tag{4.1}
\]

All six reciprocal points are hull vertices:

\[
\boxed{\text{the reciprocal point configuration is a strictly convex hexagon.}}
\tag{4.2}
\]

---

## 5. Every reciprocal vertex has a `2+3` sign split

In the convex hexagon, the five non-ground hull angles are each strictly greater than
`2pi/3`.  Since the total hexagon angle sum is `4pi`, the ground angle satisfies

\[
\boxed{\phi_0<2\pi/3.}
\tag{5.1}
\]

The coarse `1+4` unit-force bound is

\[
\phi>2\arccos(1/4)>2\pi/3.
\]

Thus the ground vertex cannot have a `1+4` split; it has `2+3`.

No non-ground vertex can have a `1+4` split either.  If one did, its angle would exceed
`2 arccos(1/4)`.  The other four non-ground vertices exceed `2pi/3`, and the ground
vertex exceeds `arccos(-1/4)`.  Therefore the hexagon angle sum would be strictly larger
than

\[
2\arccos(1/4)
+4\cdot{2\pi\over3}
+\arccos(-1/4).
\tag{5.2}
\]

Using `arccos(-1/4)=pi-arccos(1/4)`, the expression in (5.2) equals

\[
{11\pi\over3}+\arccos(1/4)>4\pi,
\]

because `arccos(1/4)>pi/3`.  This contradicts the exact `4pi` angle sum.

Hence

\[
\boxed{
\text{all six reciprocal vertices have a `2+3` incident sign split.}
}
\tag{5.3}
\]

Equivalently, for either sign color, every vertex has signed degree two or three.

---

## 6. Sharpened sign-graph endpoint

Choose the minority sign color.  The earlier sign-count theorem gives six or seven
minority edges.  Statement (5.3) now sharpens its H6 degree ledgers.

If there are six minority edges, the total minority degree is twelve, so every vertex
has degree two.  Thus the minority graph is a simple two-regular graph on six vertices:

\[
\boxed{C_6\quad\text{or}\quad C_3\sqcup C_3.}
\tag{6.1}
\]

If there are seven minority edges, total minority degree is fourteen.  Exactly two
vertices have minority degree three and the other four have degree two:

\[
\boxed{(3,3,2,2,2,2).}
\tag{6.2}
\]

The majority degrees are the complementary `5-d_i` values.

So the minimal `K_5` dual obstruction has now been reduced to a strictly convex
reciprocal hexagon with all local sign splits `2+3`, sign counts `6+9` or `7+8`, and the
small graph classes in (6.1)--(6.2).  The five non-ground vertices additionally retain
the strict source force-gap `<120` degrees.

No theorem-state file is changed.

**Disposition:** combined the source `<120` force-gap with the unit-force reciprocal
equilibrium to prove every non-ground reciprocal hull angle `>120` degrees, exclude the
entire H5 order-type branch, force a convex reciprocal hexagon, and reduce every local
sign split to `2+3`.  C-II remains open.