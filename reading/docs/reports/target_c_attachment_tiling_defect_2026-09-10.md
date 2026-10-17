> Generated reading edition · [exact source](../../../docs/reports/target_c_attachment_tiling_defect_2026-09-10.md) · source SHA-256 `5269430b9cfd61ab76923ff0dc4f33d3557edd609e6669dfdb92a3695273b23a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-81101C539ACA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact attachment tiling defect after PA

**Date:** 2026-09-10  
**Repository state:** continuation of `research/c2-pinned-attachment-bound-2026-09-10` after PA  
**Run type:** exact planar defect decomposition / zero-loaded-contact branch collapse  
**Target:** Target C C-II after ZF/ZJ/ZK/PA  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The PA theorem gives, for each unloaded component `I_r` with `a_r=|A_r|` distinct loaded attachments,

$$
s_r\le a_r-3.
$$

This report resolves the slack exactly and simultaneously identifies the deficit by which the convex attachment cells fail to triangulate the force hull. The two defects add up to the loaded-loaded contact currency left after mixed defect is paid.

Let

- `P_r=conv(A_r)`;
- `J_r^+` be the PA graph obtained from the internal/attachment contact graph of `I_r` by adding the `a_r` sides of `partial P_r`;
- `T_r` be the number of triangular bounded faces of `J_r^+`;
- `Q_r^+` be the sum `sum_F(deg F-4)` over bounded faces of degree at least five in `J_r^+`;
- `k=d_H+s_Z`;
- `a_inc=sum_r a_r` be the distinct attachment-incidence count.

The PA proof gives `T_r<=a_r`, because every triangular bounded face consumes exactly one newly added attachment-hull side.

## 1. Exact local PA slack

The outer face of `J_r^+` is the simple `a_r`-cycle `partial P_r`. Let `V_r^+=n_r+a_r` and `E_r^+=e_r+t_r+a_r`. If `f_r` is the number of bounded faces, Euler gives

$$
f_r=E_r^+-V_r^++1.
\tag{1.1}
$$

The bounded-face degree sum is exactly

$$
2E_r^+-a_r
=4f_r-T_r+Q_r^+.
\tag{1.2}
$$

Substituting (1.1) and rearranging gives

$$
E_r^+
=2V_r^+-2+\frac{T_r-a_r-Q_r^+}{2}.
\tag{1.3}
$$

On the other hand, by the definition

$$
s_r=e_r+t_r-2n_r-1,
$$

we have

$$
E_r^+=2n_r+1+s_r+a_r.
\tag{1.4}
$$

Compare (1.3) and (1.4).

### Theorem AT.1 — exact local defect identity

$$
\boxed{
a_r-3-s_r
=\frac{a_r-T_r+Q_r^+}{2}.
}
\tag{AT.1}
$$

Every term is nonnegative. Thus the PA inequality is equality precisely when

$$
T_r=a_r,
\qquad
Q_r^+=0.
$$

Equivalently every added side bounds one triangular face and every other bounded face is a quadrilateral. Since all non-added edges are unit contacts, those quadrilaterals are unit rhombi.

## 2. The polygon-dissection deficit

C49 proves that the convex attachment cells have pairwise disjoint interiors. Since every `A_r` is a subset of the `q` vertices of the strict convex polygon `F`, triangulate each `P_r` using only its own vertices. The resulting triangles have pairwise disjoint interiors and noncrossing edges.

The number of such triangles is

$$
N_\triangle
=\sum_r(a_r-2).
\tag{2.1}
$$

A noncrossing straight-line graph on `q` vertices in convex position has at most `q-2` bounded triangular faces. Hence

$$
N_\triangle\le q-2.
$$

Define

$$
\boxed{
d_{tile}:=q-2-\sum_r(a_r-2)\ge0.
}
\tag{AT.2}
$$

Use the ZJ notation

$$
p_A=q_{used}+2c_I-2s-a_{inc},
\qquad
u_0=q-q_{used}.
$$

Then direct substitution gives the exact identity

$$
\boxed{
d_{tile}=p_A+2(s-1)+u_0.}
\tag{AT.3}
$$

Thus the three planar-incidence slacks have one geometric meaning: they are exactly the missing number of triangles relative to a full triangulation of the loaded force hull.

## 3. Exact global defect decomposition

Sum AT.1. Since

$$
u_A=a_{inc}-3c_I,
\qquad
s_C=\sum_rs_r,
$$

we get

$$
\boxed{
u_A-s_C
=\frac12\sum_r(a_r-T_r+Q_r^+).}
\tag{3.1}
$$

PA rewrites ZJ exactly as

$$
e_{BB}-k
=(u_A-s_C)+p_A+2(s-1)+u_0.
$$

Insert (3.1) and AT.3.

### Theorem AT.2 — loaded-contact defect ledger

$$
\boxed{
 e_{BB}-(d_H+s_Z)
 =
 \frac12\sum_r(a_r-T_r+Q_r^+)
 +d_{tile}.
}
\tag{AT.4}
$$

This is a finite exact identity. In particular

$$
\boxed{
 d_{tile}\le e_{BB}-(d_H+s_Z)\le e_{BB},
}
\tag{AT.5}
$$

and

$$
\boxed{
\sum_r(a_r-T_r+Q_r^+)
\le2\bigl(e_{BB}-(d_H+s_Z)\bigr).
}
\tag{AT.6}
$$

So small loaded-loaded contact currency forces *simultaneously*:

1. near-maximal polygon-dissection incidence of the attachment cells;
2. almost every attachment-cell side to carry the PA boundary triangle;
3. only a controlled total amount of degree-above-four defect inside the augmented cells;
4. small diameter-tree/mixed-stress defect by PA.4.

No pinned-surplus term appears on the right.

## 4. Equality forces an exact tiling of the force hull

Suppose

$$
e_{BB}=0.
$$

PA gives `k=0`, and AT.4 forces

$$
d_{tile}=0,
\qquad
T_r=a_r,
\qquad
Q_r^+=0
\quad\text{for every }r.
\tag{4.1}
$$

The first equality says

$$
\sum_r(a_r-2)=q-2.
\tag{4.2}
$$

Triangulate every `P_r`. Add all these triangle edges and the outer cycle `partial F` to one straight-line graph on the `q` loaded vertices. C49's pairwise interior-disjointness implies the triangle interiors are disjoint and all edges are noncrossing. Each of the `q-2` triangles is therefore a bounded triangular face of this outerplanar graph.

A plane graph on `q` convex-position vertices with the outer `q`-cycle has at most `q-2` bounded faces, with equality only for a triangulation of the whole polygon `F`. Since we already have exactly `q-2` triangular bounded faces, there is no remaining bounded region.

### Theorem AT.3 — zero-loaded-contact attachment tiling

If `e_BB=0`, then

$$
\boxed{
F=\bigcup_r P_r,
\qquad
\operatorname{int}P_r\cap\operatorname{int}P_s=\varnothing\ (r\ne s).
}
\tag{AT.7}
$$

Equivalently the harmonic attachment cells form a polygonal dissection of the entire force hull using only loaded vertices.

The dissection has exactly

$$
\boxed{c_I-1}
\tag{AT.8}
$$

internal diagonals. Indeed a dissection of a polygon into `c_I` cells without interior dissection vertices has dual tree and therefore `c_I-1` internal edges. The same count follows from

$$
\sum_ra_r=q+2(c_I-1),
$$

where each outer side is counted once and each internal diagonal twice.

## 5. Rhombic gluing across the dissection

In the `e_BB=0` equality regime, AT.1 says that every side of every `P_r` bounds a PA triangular face with two unit contact sides.

- If a cell side is on `partial F`, this is the triangular OP outer pocket already forced by PC/TN.
- If a cell side is an internal dissection diagonal shared by `P_r` and `P_s`, it has one PA triangle on each side. Their four non-base sides are unit contacts. The union of the two triangles is exactly the corresponding global bounded quadrilateral contact face. PC gives `Q=0`, so this face is a simple strict unit rhombus.

Inside one component cell, AT.1 gives exactly `n_r-1` quadrilateral faces: from `E_r^+=2V_r^+-2`, Euler gives `f_r=V_r^+-1=n_r+a_r-1`; subtracting the `a_r` boundary triangles leaves `n_r-1` quadrilaterals.

Across the `c_I-1` internal cell diagonals, the paired boundary triangles give `c_I-1` further global rhombi. Hence the complete number `R` of bounded contact faces is

$$
\boxed{
R=\sum_r(n_r-1)+(c_I-1)=n_I-1,
}
\tag{AT.9}
$$

where `n_I=sum_r n_r=v-q`.

This agrees with the independent Euler identity from `b=2q`, `Q=0`, and `s_Z=0`.

Thus the exact zero-loaded-contact core is not merely 'rhombic-like': after adding the force-hull cycle it is a full polygonal disk consisting of strict unit rhombi plus one triangular two-unit-side cap along each of the `q` force-hull sides.

## 6. No contact-isolated source point lies inside the force hull

PC gives `d_P=Q=k=c_B=0` in the `e_BB=0` branch. Hence the hull-augmented contact graph subdivides `F` into

1. strict unit-rhombus bounded contact faces; and
2. triangular outer pockets with two unit contact sides.

A contact-isolated source point cannot lie in a strict unit rhombus by the C49/C52 rhombus-cell argument.

It also cannot lie in one of the triangular pockets. Let the triangle have two sides of length one and base length `ell`, with `1<ell<2`. The covering radius of its three vertices over the triangle is strictly less than one:

- if the triangle is acute, its circumradius is
  $$
  R=\frac1{2\sqrt{1-\ell^2/4}}<1
  $$
  because acuteness here implies `ell<sqrt(2)`;
- if it is right or obtuse, the farthest point from the nearest vertex occurs no farther than half the longest side, and `ell/2<1`.

Therefore every point of the triangle is at distance `<1` from at least one triangle vertex unless it is itself a boundary source vertex. Unit separation excludes any additional source point in the triangle interior.

Consequently:

### Corollary AT.4 — exact externalization

If `e_BB=0`, every source point outside the positive contact core lies outside the force hull:

$$
\boxed{A\setminus V(C)\subseteq\mathbb R^2\setminus F.}
\tag{AT.10}
$$

This is the zero-loaded-contact analogue of the matching-branch externalization theorem, but with outer triangular caps rather than a unit hull cycle.

## 7. Train consequences and a finite area bound

With `Q=0`, `f=0`, and outer contact-walk length `b=2q`, DT gives exactly

$$
\boxed{T=q.}
\tag{7.1}
$$

The train-crossing graph is simple and triangle-free and has one edge for each of the `R` strict rhombi. Mantel gives

$$
\boxed{R\le\frac{q^2}{4}.}
\tag{7.2}
$$

Every unit rhombus has area at most one. Every triangular outer pocket with two unit sides has area at most `1/2`. Since these pieces partition `F`,

$$
\boxed{
\operatorname{area}F
\le R+\frac q2
\le\frac{q^2}{4}+\frac q2.
}
\tag{AT.11}
$$

If along an unbounded `e_BB=0` sequence

$$
\frac qD=\frac hD\to y,
$$

FSDB supplies

$$
\liminf\frac{\operatorname{area}F}{D^2}
\ge\Phi(y):=\frac{y+\sin y}{4}.
$$

AT.11 therefore gives the necessary condition

$$
\boxed{y^2\ge y+\sin y.}
\tag{AT.12}
$$

On the DB interval `y>=2rho`, the function `y^2-y-sin y` is strictly increasing once `y>1` because its derivative is `2y-1-cos y>0`. It has a unique positive root above one,

$$
y_0=1.6175452860\ldots .
$$

Thus

$$
\boxed{
\liminf\frac qD\ge y_0
}
\tag{AT.13}
$$

for any unbounded exact zero-loaded-contact branch.

AT.13 is a consequence, not the endpoint: values `y>=y_0` remain feasible under this scalar area comparison.

## 8. Audit and regressions

| Claim | Classification | Audit |
| --- | --- | --- |
| local slack AT.1 | proved | exact Euler/face-degree identity |
| tiling deficit AT.3 | proved | direct algebra from C37/ZJ notation |
| global ledger AT.4 | proved | PA + ZJ exact identities |
| `e_BB=0` cells tile `F` | proved | `q-2` disjoint triangles saturate maximal outerplanar face count |
| internal dissection edges glue to rhombi | proved | PA equality + global `Q=0` |
| all non-core source points are external | proved | augmented subdivision plus unit-disk covering of rhombi/outer triangles |
| `R<=q^2/4` | proved | DT + Mantel with `T=q` |
| `q/D>=1.617545...` | proved asymptotically | FSDB + AT.11; decimal not a proof dependency |
| exclusion of all `e_BB=0` survivors | open | large-`q/D` rhombic odd-cycle configurations remain compatible with the current inequalities |
| Level I | open | high loaded-contact branch also remains |

Binding regressions:

- A near-`60 degree` rhombic disk can make the strict rhombus area excess arbitrarily small; no uniform per-face gap is assumed.
- Outer isosceles caps can be arbitrarily thin as their base tends to two; no uniform cap-area lower bound is assumed.
- The regular odd shell is not in `e_BB=0` and is untouched.
- Dense external isolated fillings remain logically possible; AT.10 localizes them rather than excluding them.
- Pure cycle-space counting is not used as a rigidity argument.

## 9. Exact remaining implication

The exact zero-loaded-contact survivor has now been reduced to

```text
attachment cells tile F;
every bounded contact face is a strict unit rhombus;
every force-hull side is capped by a two-unit-side triangular contact pocket;
all non-core source points are outside F;
T=q rhombus trains;
H is the single odd-unicyclic diameter graph on all q loaded terminals;
q/D >= y_0, where y_0 is the root of y^2=y+sin y.
```

A closing theorem must exclude this rhombic-disk/odd-diameter-cycle geometry using the actual KKT/response constraints or external-source capacity. The scalar Mantel/area inequality alone stops at AT.13.

For small but nonzero `e_BB`, AT.4 gives the correct stability target: `e_BB-k` is exactly the sum of local augmented-cell defect and global tiling deficit. Any near-zero loaded-contact theorem should use this exact defect rather than an uncontrolled `O(e_BB)` shell description.

## 10. Promotion recommendation

**Hold as report pending independent audit of PA.** AT depends directly on the new PA theorem. If PA is accepted, AT.1--AT.4 and the exact `e_BB=0` tiling/externalization should be indexed together as the sharpened low-loaded-contact normal form.

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact PA slack:
    a_r-3-s_r=(a_r-T_r+Q_r^+)/2.
Define
    d_tile=q-2-sum_r(a_r-2)=p_A+2(s-1)+u_0.
Then exactly
    e_BB-(d_H+s_Z)
      = 1/2 sum_r(a_r-T_r+Q_r^+) + d_tile.

Hence e_BB=0 forces all terms to vanish. The convex attachment cells therefore
triangulate and tile the whole force hull F. Their internal shared sides glue the PA
boundary triangles in pairs into global unit rhombi. Together with PC, F is subdivided
by strict unit rhombi plus q triangular two-unit-side outer caps; no non-core source
point can lie in F. DT gives T=q and Mantel gives R<=q^2/4, hence
    area(F)<=q^2/4+q/2.
With FSDB and y=q/D=h/D this implies
    y^2>=y+sin y,
so y>=1.6175452860... .

Remaining exact branch: large-y rhombic disk + odd diameter cycle + external source
population. Need KKT/response or external-capacity contradiction; the area scalar is
not enough.
```