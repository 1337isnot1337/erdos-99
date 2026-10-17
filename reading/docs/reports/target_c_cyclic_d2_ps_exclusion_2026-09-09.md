> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_ps_exclusion_2026-09-09.md) · source SHA-256 `9d0b0b45300c43d6528aeff86a5afb0e5dc9bcc8903466d4e602f924a97af8fd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 25 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-5FA4C81EC61D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2` PS is impossible

**Date:** 2026-09-09  
**Run type:** exact two-circle defect comparison / endpoint exclusion  
**Target:** primitive cyclic `d_H=2`, AD/PS  
**Depends on:** CP2 two-circular-path completion theorem on this branch; elementary local difference-body geometry  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

CP2 reduces every `d_H=2` phase to two equal-radius circular diameter paths joined in projective antipodal order by two short cross-component states. In PS, one short state is a resolved parallel-side tie of fixed length

```math
L:=\sqrt{D^2-1},
```

while the other is a genuine off-circle vertex of `K=F-F` with length `rho<D`.

The same fixed vector

```math
S:=C_B-C_A
```

between the two component-circle centers must be represented by both defects. This is impossible for sufficiently large `D`.

### Theorem PSX — PS exclusion

For

```math
D\ge3,
```

the primitive cyclic endpoint cannot satisfy

```math
(d_H,r_\parallel,a_{short})=(2,1,1).
```

Together with the P2 exclusion PX, this leaves only

```math
\boxed{
(d_H,r_\parallel,a_{short})=(2,0,2).
}
\tag{PSX.1}
```

Thus every sufficiently large `d_H=2` survivor has **no parallel shell sides** and exactly two genuine short antipodal vertex pairs of `F-F`.

---

## 1. Local normal form of one genuine short state

Let

```math
g\in K=F-F,
\qquad |g|=\rho<D,
```

be one genuine off-circle K-vertex in a chosen projective half. CP2 says its two neighboring refined antipodal states are endpoint diameter edges of the two path components. Let their oriented difference vectors be

```math
x,y,
\qquad |x|=|y|=D,
```

with

```math
|g-x|=|y-g|=1.
\tag{1.1}
```

After rotating coordinates put

```math
g=(\rho,0).
```

The intersections of the radius-`D` circle about the origin and the unit circle about `g` are symmetric about the x-axis. Hence, after swapping `x,y`,

```math
\boxed{
x=D(\cos a,-\sin a),
\qquad
y=D(\cos a,\sin a)}
\tag{1.2}
```

for some `a in (0,pi/2)`.

The unit-distance equation gives

```math
D^2+\rho^2-2D\rho\cos a=1,
```

so

```math
\boxed{
D\cos a=\frac{D^2+\rho^2-1}{2\rho}.}
\tag{1.3}
```

Define the radial protrusion beyond the chord `[x,y]` by

```math
\boxed{
\lambda
:=\rho-D\cos a
=\frac{\rho^2-D^2+1}{2\rho}.}
\tag{1.4}
```

Because `K` is convex and contains the origin, a strict boundary vertex `g` between the circular boundary points `x,y` must lie strictly on the outward side of the chord `[x,y]`. Therefore

```math
\lambda>0.
```

Equivalently,

```math
\boxed{\rho>\sqrt{D^2-1}=L.}
\tag{1.5}
```

At equality `rho=L`, the three K-boundary states become collinear and `g` ceases to be a vertex; this is exactly the parallel-side tie degeneration.

The same unit-distance equation may be written

```math
\boxed{
\lambda^2+D^2\sin^2a=1.}
\tag{1.6}
```

---

## 2. Midpoint displacement across the defect

Choose shell vertices so the three consecutive refined antipodal states have the one-endpoint-at-a-time form

```math
x=p_a-p_c,
\qquad
g=p_b-p_c,
\qquad
y=p_b-p_d.
\tag{2.1}
```

Then the two K-boundary unit steps are the two shell transition contacts

```math
p_b-p_a=g-x,
\qquad
p_d-p_c=g-y
```

up to orientation.

Let

```math
M_A:=\frac{p_a+p_c}{2},
\qquad
M_B:=\frac{p_b+p_d}{2}
```

be the midpoints of the neighboring A- and B-component diameter edges.

A direct substitution from (2.1) gives

```math
\boxed{
M_B-M_A
=g-\frac{x+y}{2}.}
\tag{2.2}
```

Using (1.2),

```math
\frac{x+y}{2}=D(\cos a,0),
```

so

```math
\boxed{M_B-M_A=(\lambda,0).}
\tag{2.3}
```

Thus `lambda` is exactly the radial displacement between the two endpoint-diameter midpoints across the genuine short defect.

---

## 3. Component-circle center offsets

CP2 gives both diameter paths the universal circle radius

```math
R_D=\frac{D}{2\cos(\delta/2)},
\qquad
\delta=2\arcsin\frac1{2D}.
```

For any component diameter edge, its circle center lies at fixed perpendicular distance

```math
\boxed{
h_D=\frac1{4\cos(\delta/2)}}
\tag{3.1}
```

from the edge midpoint.

Therefore, for independent signs `sigma_A,sigma_B in {+1,-1}` absorbing the unoriented choice of diameter normal,

```math
C_A=M_A+\sigma_A h_D J\frac{x}{D},
\qquad
C_B=M_B+\sigma_B h_D J\frac{y}{D}.
\tag{3.2}
```

Set

```math
S:=C_B-C_A.
```

Using (1.2)-(2.3), there are exactly two sign types.

### Same-sign type

If `sigma_A=sigma_B`, the normal correction is radial. Hence

```math
\boxed{
|S|=
\left|\lambda\pm2h_D\sin a\right|.}
\tag{3.3}
```

### Opposite-sign type

If `sigma_A=-sigma_B`, the normal correction is transverse. Hence

```math
\boxed{
|S|^2
=\lambda^2+4h_D^2\cos^2a.}
\tag{3.4}
```

These formulas are exact for every genuine PS/S2 short state.

---

## 4. The tie endpoint has two discrete center-separation lengths

At a resolved parallel tie, the inserted short state has

```math
\rho=L=\sqrt{D^2-1}.
```

Then (1.4) gives

```math
\lambda=0.
```

Also (1.3) gives

```math
\sin a=\frac1D,
\qquad
\cos a=\frac LD.
```

Thus the two possible center-separation lengths are

```math
\boxed{
s_L:=\frac{2h_D}{D}}
\tag{4.1}
```

and

```math
\boxed{
s_S:=\frac{2h_DL}{D}.}
\tag{4.2}
```

These are exactly the Type-L and Type-S values used in the P2 exclusion.

Since `L>1` for `D>sqrt2`,

```math
0<s_L<s_S.
```

---

## 5. A genuine short state never has the tie lengths

Assume now

```math
L<\rho<D.
```

Then

```math
0<\lambda<\frac1{2D}.
\tag{5.1}
```

The upper endpoint follows from (1.4), whose derivative in `rho` is positive, evaluated at `rho=D`.

Equation (1.6) gives

```math
D\sin a=\sqrt{1-\lambda^2}.
```

Since

```math
2h_D/D=s_L,
```

we have the useful identity

```math
\boxed{
2h_D\sin a
=s_L\sqrt{1-\lambda^2}.}
\tag{5.2}
```

Put

```math
\mu:=s_L\sqrt{1-\lambda^2}.
```

Then

```math
0<\mu<s_L.
```

Moreover

```math
\mu>\lambda
```

for `0<lambda<1/(2D)`, because equality occurs only at the endpoint `lambda=1/(2D)`; algebraically

```math
\mu^2-\lambda^2
=\frac{1}{4D^2-1}
-\lambda^2\frac{4D^2}{4D^2-1}>0.
\tag{5.3}
```

### Same-sign minus value

From (3.3), one possibility is

```math
|S|=\mu-\lambda.
```

Hence

```math
\boxed{0<|S|<s_L.}
\tag{5.4}
```

So it is neither tie value.

### Same-sign plus value

The other possibility is

```math
|S|=\mu+\lambda.
```

It is strictly larger than `s_L`. Indeed

```math
\lambda
>s_L\left(1-\sqrt{1-\lambda^2}\right)
```

because after rationalizing the right side it is enough that

```math
1>
\frac{s_L\lambda}{1+\sqrt{1-\lambda^2}},
```

which is immediate from `s_L lambda<1`.

Thus

```math
|S|>s_L.
\tag{5.5}
```

For `D>=3`, it is still strictly below `s_S`. Using (5.1)-(5.2),

```math
|S|
<\frac1{2D}+s_L.
```

Now

```math
\frac{1}{2Ds_L}
=\frac{\sqrt{4D^2-1}}{2D}<1,
```

so

```math
\frac1{2D}+s_L<2s_L.
```

But for `D>=3`,

```math
L=\sqrt{D^2-1}>2,
```

and hence

```math
2s_L<L s_L=s_S.
```

Therefore

```math
\boxed{s_L<|S|<s_S}
\tag{5.6}
```

in the plus case.

### Opposite-sign value

Using (3.4), a direct substitution of (1.3)-(1.4) yields

```math
\boxed{
|S|^2-s_S^2
=
\frac{D^2(\rho^2-D^2+1)^2}
{\rho^2(4D^2-1)}
>0.}
\tag{5.7}
```

Equivalently, since `rho^2-D^2+1=2rho lambda`,

```math
|S|^2-s_S^2
=
\frac{4D^2\lambda^2}{4D^2-1}>0.
```

Hence

```math
\boxed{|S|>s_S.}
\tag{5.8}
```

Combining (5.4), (5.6), and (5.8), every genuine short state has center-separation magnitude in one of the three open ranges

```math
(0,s_L),
\qquad
(s_L,s_S),
\qquad
(s_S,\infty),
```

and never equals either tie value `s_L,s_S`.

---

## 6. PS is impossible

In PS, CP2 supplies exactly two defect states:

1. one resolved parallel tie, whose representation of the fixed component-center vector `S=C_B-C_A` has length exactly `s_L` or `s_S` by Section 4;
2. one genuine off-circle short state, whose representation of the **same** vector `S` has length different from both `s_L,s_S` by Section 5.

This is impossible.

Therefore PS cannot occur for `D>=3`. `square`

---

## 7. The `d_H=2` endpoint is now S2 only

AD gave exactly three `d_H=2` defect types:

```text
P2 = two parallel ties, no genuine short pair;
PS = one tie, one genuine short pair;
S2 = no ties, two genuine short pairs.
```

PX on PR #139 excludes P2 for `D>sqrt2`. PSX excludes PS for `D>=3`.

Hence every sufficiently large `d_H=2` cyclic survivor satisfies

```math
\boxed{r_\parallel=0,
\qquad a_{short}=2.}
\tag{7.1}
```

So the force hull has no parallel sides, and `F-F` has exactly two antipodal pairs of genuine off-circle vertices.

By CP2, the full diameter graph is still the disjoint union of two explicit circular paths, and the two short K-vertices are exactly the two cross-component cycle edges of the canonical maximal antipodal thrackle.

---

## 8. Next theorem

S2 now has no discrete tie choices. Its full vertex-vertex antipodal graph is canonical and consists of

```math
T=H\cup\{g_1,g_2\},
```

where both short states are genuine K-vertices with radii

```math
L<\rho_1,\rho_2<D.
```

Each gives one of the exact center-vector formulas (3.3)-(3.4). Equating the **vectors**, not only magnitudes, for `g_1,g_2` is now the complete remaining two-circle compatibility condition.

A promising next step is to use the fact that the two short edges lie on one odd cycle and alternate the two path components. That parity should determine the relative center-offset sign type at the two defects. If the types must differ, (5.4)-(5.8) may already be incompatible; if they agree, the vector directions impose a rigid relation between the two short K radial directions.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

CP2: every d_H=2 phase is two equal-radius circular diameter paths joined by two short
cross-component antipodal states. In PS one state is a parallel tie with rho=L=sqrt(D^2-1),
the other is a genuine K-vertex with rho>L.

For a genuine short state rotate so g=(rho,0), neighboring actual D states are
  x=D(cos a,-sin a), y=D(cos a,sin a),
  |g-x|=|g-y|=1.
Convexity gives
  lambda=rho-D cos a=(rho^2-D^2+1)/(2rho)>0,
so rho>L. Also lambda^2+D^2 sin^2 a=1.
If h_D=1/[4cos(delta/2)], component-center displacement S=C_B-C_A has either
  |S|=|lambda +/- 2h_D sin a|
or
  |S|^2=lambda^2+4h_D^2 cos^2 a.

At a tie lambda=0, giving exactly
  s_L=2h_D/D,
  s_S=2h_D L/D.
For every genuine rho>L:
  same-sign minus: |S|<s_L;
  same-sign plus:  s_L<|S|<s_S for D>=3;
  opposite-sign:   |S|>s_S,
with exact identity
  |S|^2-s_S^2=4D^2 lambda^2/(4D^2-1)>0
in the last case.
Thus a genuine short state can never represent the same fixed center-separation length
as a tie. PS is impossible.

Together with PX: every large d_H=2 survivor is S2 only: no parallel shell sides,
exactly two genuine short antipodal states, and H is two circular paths.
```
