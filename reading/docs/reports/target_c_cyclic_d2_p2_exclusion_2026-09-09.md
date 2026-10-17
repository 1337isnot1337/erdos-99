> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_exclusion_2026-09-09.md) · source SHA-256 `52c9acadeddce1e5c079fe186a2ea429f417bd92446154662b8da9efe4e43514`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 11 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-C8988A30562A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2` P2 is impossible

**Date:** 2026-09-09  
**Run type:** exact endpoint exclusion  
**Target:** primitive cyclic `d_H=2`, AD/P2  
**Depends on:** P2R twin-rectangle normal form; CP two-circular-path theorem on this branch  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The P2 branch does not merely reduce to two circular zigzag paths. The two endpoint rectangles are incompatible with having two distinct parallel side directions.

### Theorem PX — P2 exclusion

For

```math
D>\sqrt2,
```

the primitive cyclic endpoint cannot lie in AD subcase P2.

Equivalently, for all sufficiently large Target C sources,

```math
\boxed{
(d_H,r_\parallel,a_{short})\ne(2,2,0).
}
\tag{PX.1}
```

### Proof in one paragraph

CP puts the two diameter-tree paths on circles with the same radius

```math
R_D=\frac{D}{2\cos(\delta/2)},
\qquad
\delta=2\arcsin\frac1{2D}.
```

For a path diameter edge of length `D`, its component-circle center lies at perpendicular distance

```math
h_D=\sqrt{R_D^2-D^2/4}
=\frac1{4\cos(\delta/2)}
```

from the edge midpoint. At either P2 rectangle, the A and B endpoint diameter edges are its two diagonals, hence have the same midpoint and acute line angle

```math
\Delta=2\arcsin\frac1D.
```

Therefore the fixed vector joining the two component-circle centers has one of exactly two lengths,

```math
2h_D\sin(\Delta/2)=\frac{2h_D}{D}
```

or

```math
2h_D\cos(\Delta/2)=\frac{2h_D\sqrt{D^2-1}}{D},
```

and is parallel respectively to the long or short rectangle axis. For `D>sqrt2` the two lengths differ, so both P2 rectangles use the same type. The center-difference vector is the same nonzero vector at both rectangles, hence the corresponding axes are parallel. In either type the unit shell-side axes of the two rectangles are parallel. But those unit sides are exactly the two supposedly distinct P2 parallel-side pairs. A strictly convex polygon has at most one side in each oriented direction, so two distinct unordered parallel pairs cannot have the same direction. Contradiction. `square`

---

## 1. Fixed offset of a component-circle center from every path edge

CP gives one diameter component as a path

```math
a_0a_1,\ldots,a_{m-1}a_m
```

whose vertices lie on one circle of radius

```math
R_D=\frac{D}{2\cos(\delta/2)}.
\tag{1.1}
```

Every path edge has chord length `D`. Therefore the perpendicular distance from the component-circle center `C` to the midpoint `M` of any path edge is

```math
\begin{aligned}
h_D
&=\sqrt{R_D^2-\frac{D^2}{4}}\\
&=\sqrt{
\frac{D^2}{4\cos^2(\delta/2)}-\frac{D^2}{4}}\\
&=\frac D2\tan\frac\delta2.
\end{aligned}
```

Since

```math
\sin\frac\delta2=\frac1{2D},
```

this is

```math
\boxed{
h_D=\frac1{4\cos(\delta/2)}.}
\tag{1.2}
```

Thus for an unoriented path diameter chord with unit tangent `u`,

```math
\boxed{C=M+\sigma h_D Ju,
\qquad \sigma\in\{+1,-1\},}
\tag{1.3}
```

where `J` is quarter-turn. The sign is determined by which side of the chord contains the rest of that component circle.

Both P2 components have the same `D` and the same ordinary gap `delta`, hence the same radius `R_D` and offset `h_D`.

---

## 2. One P2 rectangle determines the center-difference vector up to two types

Take one P2 rectangle. P2R labels its four shell vertices cyclically as

```math
a\in A,\quad b\in B,\quad c\in A,\quad d\in B,
```

with unit parallel shell sides `ab,cd` and actual diameter diagonals

```math
ac\in T_A,\qquad bd\in T_B.
```

Let `O` be the rectangle center. Then

```math
O=\frac{a+c}{2}=\frac{b+d}{2},
```

so `O` is the midpoint of both endpoint path edges `ac` and `bd`.

The rectangle dimensions are

```math
1\times L,
\qquad
L:=\sqrt{D^2-1}.
```

Choose coordinates with the long side horizontal and the unit shell side vertical. Unit tangent vectors along the two diameter diagonals may be chosen as

```math
u_A=\frac1D(L,1),
\qquad
u_B=\frac1D(L,-1).
\tag{2.1}
```

Their acute angle is

```math
\Delta=2\arcsin\frac1D,
```

because

```math
\sin\frac\Delta2=\frac1D,
\qquad
\cos\frac\Delta2=\frac LD.
\tag{2.2}
```

By (1.3), for signs `sigma_A,sigma_B`,

```math
C_A=O+\sigma_A h_D J u_A,
\qquad
C_B=O+\sigma_B h_D J u_B.
\tag{2.3}
```

Hence

```math
C_B-C_A
=h_D(\sigma_BJu_B-\sigma_AJu_A).
\tag{2.4}
```

There are two geometric possibilities, according to whether the signs agree.

### Type L — equal signs

If `sigma_A=sigma_B`, then using (2.1)

```math
Ju_B-Ju_A
=\frac1D(2,0)
```

up to a global sign. Thus

```math
\boxed{
|C_B-C_A|=\frac{2h_D}{D}
=2h_D\sin\frac\Delta2,}
\tag{2.5}
```

and `C_B-C_A` is parallel to the long rectangle axis.

### Type S — opposite signs

If `sigma_A=-sigma_B`, then

```math
Ju_B+Ju_A
=\frac1D(0,2L)
```

up to sign. Thus

```math
\boxed{
|C_B-C_A|=\frac{2h_DL}{D}
=2h_D\cos\frac\Delta2,}
\tag{2.6}
```

and `C_B-C_A` is parallel to the short rectangle axis, i.e. to the unit P2 shell sides.

So every P2 rectangle forces the same global vector `C_B-C_A` into one of two discrete length/direction types.

---

## 3. The two types have different lengths for large sources

The Type-L and Type-S lengths are equal exactly when

```math
\frac{2h_D}{D}
=
\frac{2h_D\sqrt{D^2-1}}{D},
```

or

```math
\sqrt{D^2-1}=1.
```

Thus equality occurs only at

```math
D=\sqrt2.
```

For every

```math
\boxed{D>\sqrt2,}
\tag{3.1}
```

Type L and Type S are metrically distinct.

The two component circles are fixed objects, so the vector

```math
s:=C_B-C_A
```

is identical when computed from either of the two P2 rectangles. In particular its length is identical.

Therefore, for `D>sqrt2`, both rectangles must have the same type.

Also `s` cannot vanish: the two diagonal lines in a nondegenerate `1 x L` rectangle are not parallel, so neither vector difference in (2.4) is zero.

---

## 4. Same type forces the two parallel-pair directions to coincide

If both rectangles are Type S, the fixed nonzero vector `s` is parallel to the short axis of each rectangle. Hence the two short axes are parallel. But each short axis is exactly the direction of that rectangle's pair of parallel unit shell sides. Thus the two P2 parallel pairs have the same direction.

If both rectangles are Type L, the fixed vector `s` is parallel to the long axis of each rectangle. Hence the two long axes are parallel. Their perpendicular short axes are also parallel, so again the two P2 parallel shell-side pairs have the same direction.

Thus in either case

```math
\boxed{
\text{the two purported P2 parallel-side pairs have one common direction}.}
\tag{4.1}
```

---

## 5. Strict convexity forbids two distinct pairs in one direction

The force hull `F` is strictly convex. Along the counterclockwise polygon boundary, every oriented side tangent direction occurs at most once.

For one unordered parallel-side direction there can therefore be at most

- one side with oriented tangent `u`, and
- one opposite side with oriented tangent `-u`.

Those two sides form the unique unordered parallel pair in that direction.

P2 requires exactly two **distinct** unordered parallel-side pairs. Equation (4.1) says they have the same direction, so they would have to be the same pair. Contradiction.

This proves PX.1.

---

## 6. Consequence for the full `d_H=2` phase

AD had three exact possibilities:

```text
P2: r_parallel=2, a_short=0
PS: r_parallel=1, a_short=1
S2: r_parallel=0, a_short=2.
```

PX eliminates P2 for every sufficiently large source. Therefore the complete `d_H=2` cyclic endpoint now satisfies

```math
\boxed{
a_{short}\ge1.}
\tag{6.1}
```

Equivalently, every surviving `d_H=2` source must have at least one antipodal vertex pair of `F-F` strictly inside the radius-`D` circle.

The exact fully circle-saturated two-parallel-pair branch is gone.

---

## 7. Regression audit

### Why two circles are needed

The argument does not follow from the two rectangles alone. CP supplies one fixed circle center for every edge of `T_A` and one fixed circle center for every edge of `T_B`. The same vector `C_B-C_A` must therefore be represented at both rectangles.

### Sign choices

No orientation convention for the path edges is assumed. Equation (1.3) explicitly retains independent signs `sigma_A,sigma_B` at each rectangle. The proof uses only the two possible relative sign types and their different magnitudes.

### The value `D=sqrt2`

At that isolated value the two type lengths coincide, so the magnitude argument does not force the two rectangles to use the same type. Target C concerns sufficiently large `D`, so no claim is needed there.

### Shared rectangle vertices

The two P2 parallel pairs are distinct shell-side pairs. Strict convexity makes their oriented tangent directions distinct. The conclusion that their directions coincide is therefore a genuine contradiction even if some larger combinatorial construction attempted to reuse vertices.

### Circle centers need not coincide

They do not. The proof uses the opposite fact: `C_B-C_A` is a fixed nonzero vector with two possible P2 representations.

---

## 8. What this changes

Before PX, the `d_H=2` tree endpoint had three AD branches. The most saturated one, P2, looked especially dangerous because every difference-body vertex was an actual diameter state and the shell was within `1/(2D^2)` of exact Reinhardt perimeter.

That branch is now impossible by finite geometry.

The live `d_H=2` endpoint is reduced to

```text
PS: one parallel pair + one short antipodal pair,
or
S2: two short antipodal pairs.
```

Both surviving branches contain a genuine radial defect in `F-F`. The next theorem should quantify/localize those short vertices and map them to the two MT completion chords. Unlike P2, the ordinary-gap path argument will fail only in the immediate neighborhoods of the one/two short states, so one expects `T_A,T_B` to be paths away from O(1) explicitly localized branch sites.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P2R+CP give two diameter paths T_A,T_B, each lying on a circle of universal radius
  R_D=D/[2 cos(delta/2)].
For any path D-edge with midpoint M, its component-circle center is
  C=M+sigma h_D J u,
  h_D=sqrt(R_D^2-D^2/4)=1/[4 cos(delta/2)].

At either P2 rectangle the A/B endpoint D-edges are its two diagonals, with common
midpoint O and acute angle Delta=2asin(1/D). Therefore s=C_B-C_A has exactly two
possible types:
  Type L: |s|=2h_D sin(Delta/2)=2h_D/D, parallel to long rectangle side;
  Type S: |s|=2h_D cos(Delta/2)=2h_D sqrt(D^2-1)/D, parallel to unit shell side.
For D>sqrt2 these lengths differ. Since the same fixed vector s is computed at both
P2 rectangles, both rectangles must have the same type. Then their corresponding axes
are parallel; in either type their unit shell-side axes are parallel. Hence the two
supposedly distinct P2 parallel-side pairs have the same direction. Strict convexity
allows only one pair in one direction. Contradiction.

Thus P2 is impossible for D>sqrt2. Every surviving d_H=2 cyclic source is PS or S2,
so F-F has at least one genuine short antipodal vertex pair.
```
