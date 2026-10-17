> Generated reading edition · [exact source](../../../docs/reports/target_c_disjoint_diameter_gap_outerwalk_collapse_2026-09-09.md) · source SHA-256 `fa329592905ddaef304ac6163a56cc86c274b486bee8def6aceeb045c5cf396f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-46CFB9DBDC89","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — disjoint-diameter angle doubling and outer-walk collapse

**Date:** 2026-09-09  
**Repository base:** `e555cad22322c1e430a3aa1e25518742b35615c0`  
**Run type:** exact convex geometry / post-ZF stability  
**Target:** Target C C-II after ZF, DB, NM, NB  
**External web search:** used only to inspect unrelated perimeter/area literature; no external theorem is used below  
**Computation:** only decimal evaluation already present in upstream reports; no computation is used in the proofs

## LEVEL I STATUS

`STILL OPEN`

This report adds a geometric distinction that DB does not use: two consecutive diameter directions cost twice as much angular spacing when the corresponding diameter edges are vertex-disjoint.

For a unit-separated set of diameter `D`, put

```math
a_D:=\arcsin\frac1{2D}.
```

C67 gives the universal separation `2a_D` between any two distinct diameter directions. The first theorem below proves the exact stronger bound

```math
\boxed{\theta\ge4a_D}
```

for two vertex-disjoint diameter edges.

In the post-ZF diameter graph this interacts with the tree-component defect

```math
d_H=q-h.
```

At least `d_H` consecutive pairs in the cyclic direction order are vertex-disjoint. Feeding their doubled angular cost into the DB difference-body perimeter argument yields a new exact lower bound for the outer-walk excess

```math
x_B=b-q.
```

The main asymptotic consequence is:

> if `x_B=o(D)`, then `q/D -> pi`, `per(F)/D -> pi`, and the force hull becomes uniformly constant-width at scale `D`.

Combining with NM further gives

```math
\boxed{
\liminf h/D\ge3\pi/5,
\qquad
\liminf (Q+2s_Z)/D\ge\pi/5
}
```

inside this small-outer-walk phase.

Thus NB's three-way linear-defect alternative sharpens: outer-walk excess can be sublinear only in a near-perimeter-maximal, near-constant-width force hull carrying a linear face/mixed-stress defect.

---

## 1. A doubled angular gap for disjoint diameter edges

### Theorem DG — exact disjoint-diameter gap

Let `A` be any finite unit-separated planar set of diameter `D>1`. Let `AC` and `BD` be two vertex-disjoint diameter edges:

```math
|A-C|=|B-D|=D.
```

Let `theta in (0,pi/2]` be the acute projective angle between the two diameter lines. Then

```math
\boxed{
\theta\ge4\arcsin\frac1{2D}=4a_D.
}
\tag{DG.1}
```

The constant is sharp for the four-endpoint geometry subject only to the distance window `1<=|x-y|<=D`.

### Proof

Orient the two diameter vectors so their mutual angle is `theta`:

```math
u=C-A,
\qquad
v=D-B,
\qquad
|u|=|v|=D,
\qquad
u\cdot v=D^2\cos\theta.
```

Let `m_1,m_2` be the two diagonal midpoints and put

```math
w:=m_2-m_1,
\qquad
p:=\frac{u-v}{2},
\qquad
r:=\frac{u+v}{2}.
```

Because `|u|=|v|`,

```math
p\perp r,
\qquad
|p|=D\sin\frac\theta2=:P,
\qquad
|r|=D\cos\frac\theta2=:R,
```

and

```math
P^2+R^2=D^2.
\tag{1.1}
```

The four cross-pair displacement vectors are, up to sign,

```math
w+p,\quad w-p,\quad w+r,\quad w-r.
\tag{1.2}
```

Every source distance is at most `D`, so in particular

```math
|w+r|\le D,
\qquad
|w-r|\le D.
\tag{1.3}
```

Choose orthogonal coordinates with `p=(P,0)`, `r=(0,R)`, and write `w=(x,y)`. Replacing `x,y` by absolute values can only preserve the expressions below, so take `x,y>=0`.

From (1.3),

```math
x^2+(y+R)^2\le D^2.
```

Hence

```math
0\le x\le P,
\qquad
0\le y\le\sqrt{D^2-x^2}-R.
\tag{1.4}
```

The smaller of the two opposite cross distances `|w+p|,|w-p|` is

```math
\min\{|w+p|,|w-p|\}
=\sqrt{(P-x)^2+y^2}.
\tag{1.5}
```

For fixed `x` this is increasing in `y`, so (1.4) gives

```math
\min\{|w+p|,|w-p|\}^2
\le
(P-x)^2+(\sqrt{D^2-x^2}-R)^2.
\tag{1.6}
```

Write

```math
\frac\theta2=t,
\qquad
x=D\sin\phi,
\qquad
0\le\phi\le t.
```

Using `P=D sin t`, `R=D cos t`, the right side of (1.6) becomes

```math
\begin{aligned}
& D^2\sin^2t-2D^2\sin t\sin\phi+D^2\sin^2\phi \\
&\quad +D^2\cos^2\phi+D^2\cos^2t-2D^2\cos t\cos\phi \\
&=2D^2\bigl(1-\cos(t-\phi)\bigr) \\
&=4D^2\sin^2\frac{t-\phi}{2} \\
&\le4D^2\sin^2\frac t2.
\end{aligned}
\tag{1.7}
```

Therefore

```math
\boxed{
\min\{|A-B|,|C-D|\}
\le2D\sin\frac\theta4.
}
\tag{1.8}
```

The two endpoints are distinct source points, so unit separation gives

```math
1\le2D\sin\frac\theta4.
```

Since `theta/4 in (0,pi/8]`, sine is increasing there, and DG.1 follows.

For sharpness of the four-point distance-window problem, take `x=0` and `y=D-R`. Then equality holds in (1.7), one of the other cross distances equals `D`, and setting `2D sin(theta/4)=1` realizes the endpoint value. `square`

### Comparison with the shared-endpoint gap

If two diameter edges share a vertex `z`, their two other endpoints lie on the radius-`D` circle about `z`; unit separation gives only

```math
\theta\ge2\arcsin\frac1{2D}=2a_D.
\tag{1.9}
```

Thus a disjoint consecutive pair costs exactly twice the universal angular quantum.

---

## 2. At least `d_H=q-h` cyclic neighbor pairs are disjoint

Order the `h` actual diameter edges by their projective directions around the projective circle. Call two cyclically consecutive edges **shared** if they have a common endpoint and **disjoint** otherwise. Let

```math
m:=\#\{\text{disjoint consecutive pairs}\}.
\tag{2.1}
```

The post-ZF source is not a diameter star by ZS.

### Lemma DG.2

```math
\boxed{m\ge q-h=d_H.}
\tag{2.2}
```

### Proof

For one terminal `v` of diameter degree `d_v`, mark the `d_v` incident edges among the cyclic list of all `h` edge directions. Because the full diameter graph is not a star, `d_v<h`. A proper subset of `d_v` positions on a cyclic list has at most `d_v-1` cyclic adjacent pairs lying entirely inside the subset.

Therefore the number of consecutive direction pairs sharing endpoint `v` is at most `d_v-1`.

Two distinct diameter edges cannot share both endpoints, so every shared consecutive pair is charged to exactly one terminal. Hence, writing `s=h-m` for the number of shared consecutive pairs,

```math
s\le\sum_{v\in B_+}(d_v-1)
=2h-q.
```

Thus

```math
m=h-s\ge h-(2h-q)=q-h=d_H.
```

`square`

This is exact. The quantity `d_H` is already identified by the post-ZF ledger with the number of tree components of the planar diameter pseudoforest.

---

## 3. Mixed-gap difference-body perimeter bound

Let the cyclic projective direction gaps be

```math
g_1,\ldots,g_h,
\qquad
\sum_i g_i=\pi.
```

DB gives

```math
\operatorname{per}(F)
\ge2D\sum_i\sin\frac{g_i}{2}.
\tag{3.1}
```

By C67 and DG,

- every gap is at least `2a_D`;
- every disjoint-neighbor gap is at least `4a_D`.

By DG.2 at least `d_H` gaps belong to the second class.

### Theorem DG.3 — exact mixed-gap perimeter lower bound

If `d_H=0`, DB already gives

```math
\boxed{
\operatorname{per}(F)
\ge q-1+2D\cos((q-1)a_D),
}
\tag{3.2}
```

because then `q=h`.

If `d_H>=1`, then

```math
\boxed{
\operatorname{per}(F)
\ge
h-d_H
+2(d_H-1)\cos a_D
+2D\cos((q-2)a_D).
}
\tag{3.3}
```

### Proof for `d_H>=1`

Choose any `d_H` of the disjoint consecutive pairs guaranteed by DG.2. Relax the actual gap constraints by retaining only

```math
g_i\ge4a_D
```

on those designated `d_H` gaps and

```math
g_i\ge2a_D
```

on all remaining gaps. Dropping any additional doubled-gap restrictions can only lower the minimum of the right side of (3.1), so a lower bound for this relaxed problem is valid for the actual source.

The function `sin(g/2)` is concave. Over the simplex with the displayed lower bounds and fixed sum `pi`, its sum is minimized at an extreme point: all excess angular mass lies in one gap.

For a fixed excess amount, putting that excess on a gap with the larger lower bound `4a_D` gives no larger increment than putting it on a `2a_D` gap, because

```math
\sin\frac{L+R}{2}-\sin\frac L2
```

is nonincreasing in the base value `L` for `R>=0` in the feasible angular range. Thus an extremizer may be chosen with

- all `h-d_H` ordinary gaps equal to `2a_D`;
- `d_H-1` doubled gaps equal to `4a_D`;
- the final doubled gap carrying the remaining mass.

The remaining gap is

```math
\pi-2a_D(h-d_H)-4a_D(d_H-1)
=
\pi-2a_D(h+d_H-2).
\tag{3.4}
```

Since `h+d_H=q`, its half-sine contribution is

```math
\sin\left(\frac\pi2-(q-2)a_D\right)
=\cos((q-2)a_D).
```

Also

```math
2D\sin a_D=1,
\qquad
2D\sin(2a_D)=2\cos a_D.
```

Substitution into (3.1) proves (3.3). `square`

---

## 4. The outer contact walk must pay the mixed angular cost

The outer contact-face walk has length

```math
b=q+x_B
```

and convex hull exactly `F`. OP's closed-walk perimeter lemma gives

```math
\operatorname{per}(F)\le b=q+x_B.
\tag{4.1}
```

Combine this with DG.3.

### Corollary DG.4 — exact outer-walk excess floor

If `d_H=0`,

```math
\boxed{
 x_B
\ge
2D\cos((q-1)a_D)-1.
}
\tag{4.2}
```

If `d_H>=1`,

```math
\boxed{
 x_B
\ge
2D\cos((q-2)a_D)
-2
-2(d_H-1)(1-\cos a_D).
}
\tag{4.3}
```

### Proof

The `d_H=0` case follows by subtracting `q` from (3.2) and using (4.1).

For `d_H>=1`, note

```math
h-d_H=q-2d_H.
```

Subtract `q` from (3.3):

```math
\begin{aligned}
\operatorname{per}(F)-q
&\ge
-2d_H+2(d_H-1)\cos a_D
+2D\cos((q-2)a_D)\\
&=
2D\cos((q-2)a_D)
-2-2(d_H-1)(1-\cos a_D).
\end{aligned}
```

Then use `x_B>=per(F)-q`. `square`

The correction involving `d_H` is asymptotically negligible because

```math
d_H\le q\le\pi D,
\qquad
1-\cos a_D=O(D^{-2}).
\tag{4.4}
```

---

## 5. Continuous asymptotic tradeoff: outer-walk excess versus terminal density

Take any unbounded post-ZF sequence and a subsequence on which

```math
\frac qD\to\eta,
\qquad
0<\eta\le\pi.
\tag{5.1}
```

Both cases of DG.4 give the same limiting inequality:

### Theorem DG.5

```math
\boxed{
\liminf\frac{x_B}{D}
\ge2\cos\frac\eta2.
}
\tag{5.2}
```

Indeed `Da_D->1/2`, the finite additive constants vanish after division by `D`, and the correction in (4.4) is `o(D)` before division.

Equivalently, for every fixed `epsilon>0`, if

```math
\frac qD\le\pi-\epsilon
```

along a subsequence, then

```math
\boxed{
\liminf\frac{x_B}{D}
\ge2\sin\frac\epsilon2>0.
}
\tag{5.3}
```

Thus sublinear outer-walk excess is possible only at the perimeter-maximal endpoint.

---

## 6. Small outer-walk excess forces asymptotic constant width

### Theorem DG.6 — `x_B=o(D)` collapse

If an unbounded post-ZF sequence satisfies

```math
x_B=o(D),
\tag{6.1}
```

then

```math
\boxed{
\frac qD\to\pi,
\qquad
\frac{\operatorname{per}(F)}D\to\pi.
}
\tag{6.2}
```

Moreover its width function satisfies uniformly in direction

```math
\boxed{
\min_\theta w_F(\theta)=D-o(D),
}
\tag{6.3}
```

so every Hausdorff subsequential limit of the normalized force hulls `F/D` is a convex body of constant width one.

Finally

```math
\boxed{
\operatorname{area}(F)\ge\left(\frac12-o(1)\right)D^2.
}
\tag{6.4}
```

### Proof

DG.5 and `x_B/D->0` force

```math
\cos(\eta/2)=0.
```

Since `0<eta<=pi`, necessarily `eta=pi`, proving `q/D->pi`.

Consecutive force-hull vertices are unit-separated, so

```math
q\le\operatorname{per}(F).
```

The outer walk gives

```math
\operatorname{per}(F)\le b=q+x_B,
```

hence (6.2).

Now write

```math
E_D:=\pi D-\operatorname{per}(F)=o(D).
\tag{6.5}
```

Cauchy's perimeter formula and the diameter bound give

```math
E_D
=
\int_0^\pi [D-w_F(\theta)]\,d\theta,
\qquad
0\le D-w_F(\theta).
\tag{6.6}
```

The width function is the support function of the difference body `F-F`:

```math
w_F(\theta)=h_{F-F}(u_\theta).
```

Since `F-F` lies in the radius-`D` disk, its support function is `D`-Lipschitz in angular parameter:

```math
|w_F(\theta)-w_F(\phi)|
\le D|\theta-\phi|.
\tag{6.7}
```

Let

```math
M_D:=\max_\theta[D-w_F(\theta)].
```

At a maximizing direction, (6.7) implies the deficit remains at least `M_D/2` throughout an angular interval of total length at least `M_D/D` (using the projective circle and `M_D<=D`). Therefore

```math
E_D\ge\frac{M_D^2}{2D}.
\tag{6.8}
```

Since `E_D=o(D)`, (6.8) gives `M_D=o(D)`, proving (6.3). Uniform width convergence immediately gives the constant-width statement for every normalized Hausdorff subsequential limit.

For the area bound, take a diameter chord `AB` of `F`, `|A-B|=D`, as a base line. Let `w_perp` be the width perpendicular to `AB`. Choose support points on the two parallel supporting lines normal to that direction. The two triangles with common base `AB` and those support points lie in `F` and have disjoint interiors except along the base. Their total area is exactly

```math
\frac D2 w_{\perp}.
```

Hence

```math
\operatorname{area}(F)
\ge\frac D2 w_{\perp}
\ge\frac D2\min_\theta w_F(\theta)
=\left(\frac12-o(1)\right)D^2.
```

This proves (6.4). `square`

The area constant `1/2` is self-contained and deliberately conservative; no external minimum-area theorem for constant-width bodies is imported.

---

## 7. NM forces much denser diameter support in the constant-width endpoint

The exact post-ZF branching identity is

```math
r_H:=2h-q=x_B+Q+2s_Z.
\tag{7.1}
```

NM proves

```math
3r_H\ge h-2.
\tag{7.2}
```

Assume the small-outer-walk phase `x_B=o(D)`. Put, along a subsequence,

```math
\frac hD\to y.
```

Theorem DG.6 gives `q/D->pi`. Divide (7.2) by `D`:

```math
3(2y-\pi)\ge y.
```

Therefore

```math
\boxed{
y\ge\frac{3\pi}{5}.}
\tag{7.3}
```

Thus:

### Corollary DG.7 — small-outer-walk phase constants

Every post-ZF sequence with `x_B=o(D)` satisfies

```math
\boxed{
\liminf\frac hD\ge\frac{3\pi}{5}
=1.8849555921\ldots,
}
\tag{7.4}
```

```math
\boxed{
\liminf\frac{2h-q}{D}\ge\frac\pi5
=0.6283185307\ldots,
}
\tag{7.5}
```

and, using (7.1) with `x_B=o(D)`,

```math
\boxed{
\liminf\frac{Q+2s_Z}{D}\ge\frac\pi5.
}
\tag{7.6}
```

Also

```math
\boxed{
\limsup\frac{d_H}{D}
\le\frac{2\pi}{5}.
}
\tag{7.7}
```

The diameter-edge density `3pi/5` is substantially above DB's universal `2rho=1.47817...` and arises only after the new doubled-gap theorem forces `q/D` to the maximum-perimeter endpoint.

---

## 8. Updated post-ZF phase split

NB proves universally

```math
x_B+Q+2s_Z\ge(c_*-o(1))D,
\qquad
c_*=0.6099043189\ldots .
```

DG sharpens the interpretation.

### Phase A — terminal density bounded away from `pi`

If for some fixed `epsilon>0`,

```math
q\le(\pi-\epsilon)D,
```

then

```math
\boxed{x_B\ge(2\sin(\epsilon/2)-o(1))D.}
```

So the linear defect is already forced into the geometric outer-walk currency.

### Phase B — sublinear outer-walk excess

If

```math
x_B=o(D),
```

then simultaneously

```math
q/D\to\pi,
\qquad
per(F)/D\to\pi,
\qquad
\min w_F/D\to1,
\qquad
area(F)/D^2\ge1/2-o(1),
```

and

```math
h/D\ge3\pi/5-o(1),
\qquad
(Q+2s_Z)/D\ge\pi/5-o(1).
```

Thus the only way outer-walk defect can disappear is for the force hull to approach the constant-width endpoint while a linear face/mixed-stress defect remains.

This is a substantially narrower target than NB's undifferentiated three-currency alternative.

---

## 9. Regression checks

### Diameter star

DG.2 uses the already-proved post-ZF nonstar theorem. A pure star can have every consecutive pair share the center and would violate `m>=q-h`; it is explicitly outside that lemma's hypotheses and is already excluded upstream.

### Regular odd polygon

Its force hull is asymptotically constant width in the large regular-shell limit, with `q/D->pi` and outer walk equal to the hull cycle (`x_B=0`). Thus it lands in Phase B, as it should. It also carries large bounded-face/mixed-stress defect; DG does not falsely eliminate this known local regression family.

### Crossing matching

Every consecutive pair of matching edges is disjoint, so every direction gap pays the doubled quantum `4a_D`. This is consistent with MC/NM already excluding a large post-ZF perfect matching; DG supplies a separate geometric explanation for why such a matching consumes perimeter extremely rapidly.

### Unit square

Below the sufficiently-large post-ZF regime. DG itself remains valid as a finite four-point distance statement when its hypotheses are feasible.

---

## 10. Exact remaining lemma

DG removes the generic small-`x_B` branch. A closing proof can now split cleanly:

1. **linear outer-walk phase:** convert `x_B=Omega(D)` into a strict boundary-capacity loss or a quantitative response mass;
2. **near-constant-width phase:** use the simultaneous facts
   ```math
   q/D\to\pi,
   \quad min\,w_F/D\to1,
   \quad h/D\ge3\pi/5,
   \quad Q+2s_Z\ge(\pi/5-o(1))D
   
   ```
   to show that a triangle-free global optimum cannot carry the required linear exceptional-face/mixed-stress defect.

The second branch is particularly rigid: the hull is asymptotically perimeter-maximal while the contact/mixed framework is quantitatively far from defect-free.

No Level I contradiction is claimed here.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

DG exact geometry:
Two vertex-disjoint diameter edges at projective angle theta satisfy
    theta >= 4 asin(1/(2D)),
exactly twice the shared-endpoint spacing.

Let m be the number of disjoint consecutive pairs in cyclic diameter-direction order.
Post-ZF nonstar + degree counting gives
    m >= q-h = d_H.

Using d_H doubled gaps in the DB difference-body perimeter minimization gives,
for d_H>=1,
    per(F) >= h-d_H + 2(d_H-1)cos(a_D)
              + 2D cos((q-2)a_D),
where a_D=asin(1/(2D)).
Since per(F)<=b=q+x_B,
    x_B >= 2D cos((q-2)a_D)
           -2-2(d_H-1)(1-cos a_D).
Asymptotically, if q/D->eta,
    liminf x_B/D >= 2 cos(eta/2).

Therefore x_B=o(D) forces
    q/D -> pi,
    per(F)/D -> pi,
    min_width(F)/D -> 1,
    area(F) >= (1/2-o(1))D^2.
NM then forces
    liminf h/D >= 3pi/5,
    liminf (Q+2s_Z)/D >= pi/5.

Next:
- linear x_B branch: charge outer-walk excess;
- x_B=o(D) branch: exploit near-constant-width hull + linear Q/2s_Z defect.
```
