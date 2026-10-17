> Generated reading edition · [exact source](../../../../docs/targets/target-c/59-difference-body-density-audit.md) · source SHA-256 `12d835829fb18cdf09663cda0e8f169b510c616a8d37ff55ea3e42b6ac5831ca`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — independent difference-body density and symmetry audit

**Date:** 2026-09-11  
**LEVEL I STATUS:** **STILL OPEN.**  
**Disposition:** the post-ZF diameter-density theorem and its full-force-hull symmetry consequences are independently certified below.

This module audits the load-bearing core of the following unpromoted reports without importing their unrelated downstream scalar iterations:

- `docs/reports/target_c_force_hull_area_floor_2026-08-31.md` (C67 direction separation);
- `docs/reports/target_c_post_zf_difference_body_perimeter_2026-09-09.md` (DB);
- `docs/reports/target_c_difference_body_area_metric_fork_2026-09-09.md` (DA direction-polygon area);
- `docs/reports/target_c_fs_symmetry_difference_body_2026-09-10.md` (SC);
- `docs/reports/target_c_fs_symmetry_inradius_addendum_2026-09-10.md` (SI).

The audit uses the canonical lexicographic C-II representative, the canonical ZR/ZF theorem, and the universal full-source half-turn estimate from `58-full-source-geometry-audit.md`. It retains all contact-isolated source points.

No GU/JC/RS surplus decimal is promoted here. No KKT weight floor, response operator norm, force-bulk population theorem, or Level I closure is asserted.

## 1. Projective separation of all actual diameter directions

Let `H` be the full actual diameter graph of the canonical C-II source and let `D` be the source diameter. Put

$$
a_D:=\arcsin\frac1{2D},
\qquad
\delta_D:=2a_D.
$$

We first re-prove the only C67 input needed below.

### Lemma DB.1 — shared-endpoint separation

If `ba` and `bc` are distinct diameter edges sharing `b`, and `theta=angle abc`, then

$$
|a-c|=2D\sin(\theta/2).
$$

Unit separation gives `|a-c|>=1`, hence

$$
\boxed{\theta\ge\delta_D.}
\tag{DB.1}
$$

Also `|a-c|<=D`, so `theta<=pi/3`. Thus `theta` is exactly the projective circular distance between the two supporting line directions.

### Lemma DB.2 — disjoint-edge separation

Let `AB` and `CD` be vertex-disjoint diameter edges. The planar diameter graph is a straight-line thrackle, so the two segments cross properly. Let `phi in (0,pi/2]` be the acute angle between their supporting lines.

Place

$$
A=(0,0),\qquad B=(D,0),
$$

and label the second chord

$$
C=(x,-u),\qquad D'=(y,v),
$$

with `u,v>0` and `x<=y`. Because every source point is within distance `D` of both `A` and `B`,

$$
0\le x\le y\le D.
$$

The horizontal and vertical components of the length-`D` chord are

$$
y-x=D\cos\phi,
\qquad
u+v=D\sin\phi.
$$

Set

$$
s:=x+(D-y)=D(1-\cos\phi)
={D\sin^2\phi\over1+\cos\phi}.
$$

Suppose `D sin(phi)<1`. For `D>=2`, this gives `s<1/2`. Since `0<=x<=s` and `0<=D-y<=s`, unit separation of `C` from `A` and of `D'` from `B` gives

$$
u^2+x^2\ge1,
\qquad
v^2+(D-y)^2\ge1,
$$

hence

$$
u>\sqrt{1-s^2}>{\sqrt3\over2},
\qquad
v>{\sqrt3\over2}.
$$

Thus `u+v>sqrt(3)>1`, contradicting `u+v=D sin(phi)<1`. Therefore

$$
\phi\ge\arcsin(1/D)>\delta_D.
\tag{DB.2}
$$

Combining the two cases, distinct actual diameter edges have distinct projective directions with pairwise projective circular distance at least

$$
\boxed{\delta_D=2\arcsin{1\over2D}.}
\tag{DB.3}
$$

No KKT weights occur in this statement.

## 2. The diameter direction polygon in the difference body

Let `F` be the full actual force hull of the canonical relative-interior C-II stress. Since `H=H_*` and the stress is relative-interior, every actual diameter endpoint is selected, so this is the same force hull used throughout the post-ZF ledger.

Let `h=|H|`. Order the `h` projective diameter directions cyclically and denote the gaps by

$$
g_1,\ldots,g_h,
\qquad
\sum_{i=1}^h g_i=\pi.
$$

By DB.3,

$$
\boxed{g_i\ge2a_D.}
\tag{DB.4}
$$

Choose a unit representative `u_e` for each projective direction and put

$$
P_H:=D\operatorname{conv}\{\pm u_e:e\in H\}.
$$

For a diameter edge `bk`, `p_b-p_k=+-D u_e` and both endpoints lie in `F`, so

$$
\boxed{P_H\subseteq F-F.}
\tag{DB.5}
$$

The `2h` vertices of `P_H` lie on the radius-`D` circle and the projective gap list occurs twice around that circle. Therefore

$$
\boxed{
\operatorname{per}(P_H)
=4D\sum_{i=1}^h\sin{g_i\over2},
}
\tag{DB.6}
$$

and

$$
\boxed{
\operatorname{area}(P_H)
=D^2\sum_{i=1}^h\sin g_i.
}
\tag{DB.7}
$$

For planar convex bodies, Cauchy's width formula gives Minkowski additivity of perimeter. Hence

$$
\operatorname{per}(F-F)=2\operatorname{per}(F).
$$

Using DB.5–DB.6,

$$
\boxed{
\operatorname{per}(F)
\ge2D\sum_i\sin{g_i\over2}.
}
\tag{DB.8}
$$

## 3. Exact gap minimization and force-hull perimeter

The function `sin(g/2)` is concave on `[0,pi]`. Under DB.4 and `sum g_i=pi`, the sum is minimized at an extreme point of the feasible simplex: all but at most one gap equal the lower bound `2a_D`. Thus

$$
\sum_i\sin{g_i\over2}
\ge
(h-1)\sin a_D
+
\sin\!\left({\pi-2(h-1)a_D\over2}\right).
$$

Since `sin(a_D)=1/(2D)`, this becomes

$$
\boxed{
\sum_i\sin{g_i\over2}
\ge {h-1\over2D}+\cos((h-1)a_D).
}
\tag{DB.9}
$$

Insert DB.9 into DB.8:

$$
\boxed{
\operatorname{per}(F)
\ge h-1+2D\cos((h-1)a_D).
}
\tag{DB.10}
$$

This exact inequality is independent of the contact-face ledger.

The analogous concavity argument for `sin g` gives

$$
\boxed{
\sum_i\sin g_i
\ge
(h-1)\sin(2a_D)
+
\sin(2(h-1)a_D).
}
\tag{DB.11}
$$

The second identity will feed the symmetry-corrected area theorem below.

## 4. Exact post-ZF Euler coupling

Let the connected nonisolated contact core have `v` vertices and `e` unit-contact edges. Let `b` be the degree of the outer face, counted as the boundary-walk length, so bridges occur twice. Let

$$
Q:=\sum_{f\text{ bounded}}(\deg f-4)\ge0.
$$

Euler and the face-degree sum give

$$
Q=(2e-b)-4(e-v+1)
=4v-2e-b-4.
\tag{DB.12}
$$

Canonical ZR/ZF gives

$$
s_Z:=e+h-(2v-2)\ge0.
\tag{DB.13}
$$

Substitute DB.13 into DB.12:

$$
\boxed{{b+Q\over2}=h-s_Z,}
\qquad
\boxed{b=2h-Q-2s_Z.}
\tag{DB.14}
$$

The geometric outer contact walk has convex hull `F`, so its length bounds the convex perimeter:

$$
\boxed{\operatorname{per}(F)\le b.}
\tag{DB.15}
$$

Combining DB.10, DB.14, and DB.15 yields the exact finite post-ZF inequality

$$
\boxed{
Q+2s_Z
\le
h+1-2D\cos((h-1)a_D).
}
\tag{DB.16}
$$

Since `Q,s_Z>=0`,

$$
\boxed{
h+1\ge2D\cos((h-1)a_D).}
\tag{DB.17}
$$

No response-minor magnitude or KKT coefficient floor is used.

## 5. Diameter-edge density and force-hull perimeter density

The diameter graph is a convex geometric thrackle, so `h<=q`, where `q` is the number of force-hull vertices. Consecutive force-hull vertices are unit-separated, hence

$$
q\le\operatorname{per}(F)\le\pi D.
$$

Thus `h/D` is bounded. Pass to a subsequence with

$$
{h\over D}\to y.
$$

Because

$$
a_D={1\over2D}+O(D^{-3}),
$$

DB.17 gives

$$
\boxed{y\ge2\cos(y/2).}
\tag{DB.18}
$$

On `[0,pi]`, the function `y-2cos(y/2)` is strictly increasing. Let `rho` be the unique positive solution of

$$
\rho=\cos\rho.
$$

The unique positive root of equality in DB.18 is `y=2rho`. Therefore every unbounded post-ZF survivor sequence satisfies

$$
\boxed{
\liminf {h\over D}
\ge2\rho
=1.4781702664303213\ldots .
}
\tag{DB.19}
$$

This is strictly stronger than the canonical ZF count `h>=ceil(D)`.

DB.10 also gives, along the same subsequence,

$$
\liminf{\operatorname{per}(F)\over D}
\ge y+2\cos(y/2).
$$

The right side has derivative `1-sin(y/2)>=0` on `[0,pi]`, so DB.19 implies

$$
\boxed{
\liminf {\operatorname{per}(F)\over D}
\ge4\rho
=2.9563405328606427\ldots .
}
\tag{DB.20}
$$

This remains below the diameter-maximal perimeter `pi D`; it is not a near-disk conclusion by itself.

## 6. Canonical near half-turn symmetry of the full actual force hull

The universal full-source theorem `C-FS-GEOM` applies to every selected stress. On the canonical lexicographic C-II source choose a relative-interior normalized stress. Its positive diameter support is the full actual `H=H_*`, so its selected force hull is precisely the full actual force hull `F` used above.

Let `o` be the full-source circumcenter and put

$$
F_0:=F-o,
\qquad
L_D:=\sqrt{D\eta+\eta^2},
\qquad
\eta=3^{1/4}\sqrt D.
$$

The canonical half-turn estimate is

$$
\boxed{d_H(F_0,-F_0)\le2L_D,}
\qquad
L_D=O(D^{3/4})=o(D).
\tag{DB.21}
$$

Set `epsilon_D=2L_D`. Then

$$
-F_0\subseteq F_0+\epsilon_DB_2,
$$

so

$$
F-F=F_0+(-F_0)
\subseteq2F_0+\epsilon_DB_2.
$$

Steiner's formula and `per(F)<=pi D` give the finite bound

$$
\boxed{
\operatorname{area}(F-F)
\le
4\operatorname{area}(F)
+2\epsilon_D\operatorname{per}(F)
+\pi\epsilon_D^2.
}
\tag{DB.22}
$$

The last two terms are `o(D^2)`. Thus the generic planar Rogers–Shephard factor six improves on this source to the asymptotic centrally symmetric factor four:

$$
\boxed{
\operatorname{area}(F-F)
\le4\operatorname{area}(F)+o(D^2).
}
\tag{DB.23}
$$

The factor four is sharp for centrally symmetric `F`.

## 7. Symmetry-corrected force-hull area floor

By DB.5, DB.7, DB.11, and DB.22,

$$
\begin{aligned}
\operatorname{area}(F)
\ge{}&{D^2\over4}
\left[(h-1)\sin(2a_D)+\sin(2(h-1)a_D)\right]\\
&-{\epsilon_D\over2}\operatorname{per}(F)
-{\pi\over4}\epsilon_D^2.
\end{aligned}
\tag{DB.24}
$$

Along a subsequence with `h/D->y`, the error is `o(D^2)` and

$$
(h-1)\sin(2a_D)\to y,
\qquad
2(h-1)a_D\to y.
$$

Therefore

$$
\boxed{
\liminf{\operatorname{area}(F)\over D^2}
\ge A_{sym}(y):={y+\sin y\over4}.
}
\tag{DB.25}
$$

On `[0,pi]`, `A_sym'(y)=(1+cos y)/4>=0`. Combining with DB.19 gives the universal post-ZF force-hull area floor

$$
\boxed{
\liminf{\operatorname{area}(F)\over D^2}
\ge
A_{SC}:={2\rho+\sin(2\rho)\over4}
=0.6184708847696858\ldots .
}
\tag{DB.26}
$$

The isodiametric maximum is `pi/4`, so this leaves at most

$$
\left({\pi\over4}-A_{SC}+o(1)\right)D^2
=
(0.1669272786277625\ldots+o(1))D^2
$$

of force-hull area deficit.

This does not imply that the full source population outside `F` is subquadratic.

## 8. A common-center force-hull inradius floor

Let

$$
g_{max}:=\max_i g_i.
$$

Because every other gap is at least `2a_D`,

$$
\boxed{g_{max}\le\pi-2(h-1)a_D.}
\tag{DB.27}
$$

The vertices of `P_H/2` lie on the radius-`D/2` circle. For a centrally symmetric inscribed polygon, the centered inradius is the distance to the side subtending the largest angular gap:

$$
r(P_H/2)={D\over2}\cos(g_{max}/2).
$$

Hence DB.27 gives

$$
\boxed{
B\!\left(0,{D\over2}\sin((h-1)a_D)\right)
\subseteq {1\over2}P_H.
}
\tag{DB.28}
$$

From DB.5 and DB.21,

$$
P_H\subseteq F-F
\subseteq2(F-o)+2L_DB_2.
$$

Dividing by two,

$$
{1\over2}P_H\subseteq(F-o)+L_DB_2.
$$

Support functions and DB.28 therefore give

$$
\boxed{
B\!\left(
o,
{D\over2}\sin((h-1)a_D)-L_D
\right)
\subseteq F
}
\tag{DB.29}
$$

whenever the displayed radius is positive.

Along `h/D->y`,

$$
\liminf {r_o(F)\over D}
\ge{1\over2}\sin(y/2),
$$

where `r_o(F)` is the largest disk centered at the common source circumcenter and contained in `F`. Using DB.19 and `y<=pi`,

$$
\boxed{
\liminf {r_o(F)\over D}
\ge{1\over2}\sin\rho
=0.3368060145916074\ldots .
}
\tag{DB.30}
$$

Thus the same point `o` simultaneously satisfies

$$
B(o,(0.336806\ldots-o(1))D)
\subseteq F
\subseteq K
\subseteq B(o,D/2+O(\sqrt D)).
$$

The annular completion region between these radii still has quadratic area. Ordinary area capacity alone therefore does not close the contact-isolated population branch.

## 9. Regression audit

### Regular odd shells

For regular odd shells, `h/D->pi`. Then

$$
A_{sym}(\pi)={\pi\over4},
\qquad
{1\over2}\sin(\pi/2)={1\over2}.
$$

The area and inradius statements converge to the exact disk limits, so the theorem does not falsely exclude the mandatory shell regression.

### Dense isolated fillings

The proof never sets `n=v`, never removes contact-isolated source points, and never bounds their number. They can remain KKT-invisible while the force hull satisfies DB.26–DB.30.

### Response weights

Every statement in Sections 1–5 is weight-free. Sections 6–8 use only the canonical geometric half-turn estimate. No lower bound on an individual or aggregate `beta` weight is inferred.

### No trace/operator shortcut

The odd-shell response regression from `58-full-source-geometry-audit.md` remains binding. The area and inradius floors do not imply a small response trace defect, an operator-norm estimate, or an almost-full-weight matching.

## 10. Canonical effect and remaining obligation

The post-ZF full actual force hull now has a stronger quantitative normal form:

$$
\boxed{
{h\over D}\ge2\rho-o(1),
\qquad
{\operatorname{per}(F)\over D}\ge4\rho-o(1),
}
$$

$$
\boxed{
{\operatorname{area}(F)\over D^2}
\ge0.6184708847696858\ldots-o(1),
}
$$

and, around the same full-source circumcenter,

$$
\boxed{
{r_o(F)\over D}
\ge0.3368060145916074\ldots-o(1).
}
$$

These statements sharply restrict the geometry available to both Woodall branches. They do not close either branch. A successful continuation still needs a source-capacity loss, an upper restriction crossing the canonical surplus floors, or a strict sub-`D` competitor. In particular, the remaining quadratic completion annulus and the absence of a KKT-weight floor must be handled rather than discarded.
