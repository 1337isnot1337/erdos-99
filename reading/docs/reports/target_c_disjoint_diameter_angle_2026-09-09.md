> Generated reading edition · [exact source](../../../docs/reports/target_c_disjoint_diameter_angle_2026-09-09.md) · source SHA-256 `f5a191f70d1fd7ce5123f0bc7dd03c481cbbb8d413e72037044ca44707150b27`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C2B3B2EC8D15","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — sharp angle separation for disjoint diameter chords

**Date:** 2026-09-09  
**Repository state:** current post-ZF campaign  
**Run type:** exact finite geometry / regression-sharp bound  
**Target:** Target C diameter-direction geometry  
**Computation:** not used in the proof

## LEVEL I STATUS

`STILL OPEN`

C67 uses the universal unit-separation bound

```math
2\arcsin\frac1{2D}
```

between distinct projective diameter directions. When the two diameter edges share no endpoint, the exact constant doubles asymptotically and admits a clean finite formula.

## Theorem ZW — disjoint diameter chords cost twice the angle

Let `ac` and `bd` be two vertex-disjoint diameter edges of a unit-separated planar point set of diameter `D>1`. Let

```math
\phi\in(0,\pi/2]
```

be the acute angle between their supporting lines. Then

```math
\boxed{
\phi\ge4\arcsin\frac1{2D}.
}
\tag{ZW.1}
```

The bound is sharp as a four-point diameter geometry.

### Proof

Two vertex-disjoint diameter segments cross. Let `p,q` be their directed chord vectors, chosen so that

```math
|p|=|q|=D,
\qquad
\angle(p,q)=\phi.
```

Let the midpoint of the `p` chord be the origin and let `w` be the displacement to the midpoint of the `q` chord. Define

```math
d:=\frac{p-q}{2},
\qquad
c:=\frac{p+q}{2}.
```

Since `|p|=|q|`,

```math
d\cdot c=0.
```

Put

```math
r:=|d|=D\sin\frac\phi2,
\qquad
s:=|c|=D\cos\frac\phi2.
```

Choose orthogonal coordinates with

```math
d=(r,0),
\qquad
c=(0,s),
\qquad
w=(a,b).
```

Up to signs and cyclic relabeling, the four side vectors joining an endpoint of one diameter to an endpoint of the other are

```math
w+d,\quad w-d,\quad w+c,\quad w-c.
```

Every source distance is at most `D`, so

```math
|w+c|\le D,
\qquad
|w-c|\le D.
```

Squaring both inequalities and taking the larger sign of `b` gives

```math
\boxed{
a^2+b^2+2s|b|\le r^2.}
\tag{ZW.2}
```

In particular

```math
|a|\le r.
\tag{ZW.3}
```

Setting `a=0` in the left side of ZW.2 only relaxes the constraint, so the positive root of

```math
b^2+2sb=r^2
```

gives the universal bound

```math
|b|\le\sqrt{s^2+r^2}-s=D-s.
\tag{ZW.4}
```

Unit separation applies to the other opposite pair of cross-side distances:

```math
|w+d|\ge1,
\qquad
|w-d|\ge1.
```

Their smaller squared length is

```math
\min\{|w+d|^2,|w-d|^2\}
=a^2+b^2+r^2-2r|a|.
```

Because `|a|<=r`,

```math
a^2-2r|a|\le0.
```

Using ZW.4,

```math
\begin{aligned}
1
&\le
\min\{|w+d|^2,|w-d|^2\}\\
&\le r^2+b^2\\
&\le r^2+(D-s)^2\\
&=D^2\left[\sin^2\frac\phi2+\left(1-\cos\frac\phi2\right)^2\right]\\
&=4D^2\sin^2\frac\phi4.
\end{aligned}
```

Therefore

```math
\sin\frac\phi4\ge\frac1{2D},
```

which proves ZW.1. QED.

## Sharpness

Equality is realized at the level of the four-point distance constraints by taking

```math
a=0,
\qquad
b=D-s,
\qquad
2D\sin(\phi/4)=1.
```

Then

```math
|w+d|=|w-d|=1,
```

one of `|w\pm c|` equals `D`, and the other is at most `D`. Thus the constant cannot be improved from the assumptions `1<=all pair distances<=D` plus two disjoint diameter pairs alone.

No global optimality or KKT hypothesis enters the proof.

## Consequences and limitation

As `D->infinity`,

```math
4\arcsin\frac1{2D}
=\frac2D+O(D^{-3}),
```

exactly twice the shared-endpoint spacing

```math
2\arcsin\frac1{2D}
=\frac1D+O(D^{-3}).
```

Thus matching-like diameter directions consume twice the projective angular budget of a tightly packed star.

For a matching of `m` diameter edges, all pairs are vertex-disjoint, so their projective directions are pairwise separated by ZW.1. Hence

```math
\boxed{
m\le
\left\lfloor
\frac{\pi}{4\arcsin(1/(2D))}
\right\rfloor.}
\tag{ZW.5}
```

Asymptotically this is `m<=(pi/2+o(1))D`, consistent with the classical `q<=pi D` plus `m<=q/2`. The leading constant is therefore sharp at the level of existing shell regressions and does not by itself close C-II.

The useful role of ZW is conditional: any future decomposition that proves a positive fraction of consecutive projective direction gaps come from disjoint diameter edges can feed the stronger local spacing directly into the Cauchy-perimeter argument of PR #112.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZW:
Two vertex-disjoint D-chords in a unit-separated diameter-D point set have acute
line angle
    phi >= 4 asin(1/(2D)).

Proof:
write equal diagonals p,q, midpoint displacement w, and
    d=(p-q)/2, c=(p+q)/2,
with d perpendicular c,
    |d|=D sin(phi/2), |c|=D cos(phi/2).
The D-upper constraints on |w+-c| force
    a^2+b^2+2|c||b| <= |d|^2,
so |a|<=|d| and |b|<=D-|c|.
The unit lower constraints on |w+-d| then give
    1 <= 4D^2 sin^2(phi/4).

Asymptotic cost: 2/D, exactly twice a shared-endpoint gap.
Matching consequence:
    m <= floor(pi/[4 asin(1/(2D))]).
This is sharp at leading order and is not a Level I closure by itself.
```
