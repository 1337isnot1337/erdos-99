# Target C-II — perimeter collapse of the exterior reflection-witness branch

**Date:** 2026-09-15  
**Status:** proved proof-only composition; theorem-state authority unchanged  
**Scope:** current no-container Type-II full-core low-`t` tooth branch  
**Dependencies:** shallow-tooth reflection blocker reduction; global-turn shallow-apex theorem; exterior-cap decomposition; Type-II `per(F)/D -> pi`  
**LEVEL I STATUS:** `STILL OPEN`

The reflection-blocker reduction for a shallow two-edge tooth gives two possibilities:

1. reflecting the unloaded tooth apex across its loaded base would violate the diameter
   bound at a source point lying in the inward normal cone; or
2. the reflection is blocked at unit scale by an actual source point outside the loaded
   force hull `F`.

The second branch looked compatible with the canonical allowance of `o(D^2)` exterior
isolates. It is not compatible with the much stronger Type-II perimeter saturation.

The key geometric point is that every exterior reflection witness projects into the
relative interior of the tooth base. Hence one witness belongs to exactly one exterior
cap of `K=conv(A)` over `F`, and that cap replaces a loaded side by an outer source-hull
arc of uniformly greater length. Type II has no linear perimeter budget for such caps:

\[
\operatorname{per}(F)=\pi D-o(D),
\qquad
\operatorname{per}(K)\le\pi D.
\]

Therefore only `o(D)` shallow teeth can use exterior witnesses. Almost the entire
shallow-tooth population is forced into the normal-aligned near-diameter branch.

At the current low-`t` floor this yields

\[
\boxed{
0.425574465620116\ldots D-o(D)
}
\]

distinct shallow apices carrying a source point within `0.997775304...` of diameter
and inside the corresponding inward normal cone.

## 1. Setup and the reflection witness

Let one shallow tooth have loaded base

\[
a=(-c,0),\qquad b=(c,0),
\]

unloaded apex

\[
x=(0,h),
\]

and reflected apex

\[
x^-=(0,-h),
\]

with

\[
c=\cos\alpha,\qquad h=\sin\alpha,
\qquad 0<\alpha<\pi/6.
\tag{PC.1}
\]

The force hull lies in `y>=0`. An exterior reflection witness is a source point

\[
z=(u,-r),\qquad r>0,
\]

such that either

\[
|z-x^-|<1
\tag{PC.2}
\]

(a strict lower blocker), or

\[
|z-x^-|=1
\tag{PC.3}
\]

(a new unit contact forced by contact minimality when the reflected move is otherwise
feasible).

In both cases `z` lies outside `F` and is contact-isolated in the original canonical
source. Thus

\[
|z-a|>1,\qquad |z-b|>1,
\qquad |z-x|>1.
\tag{PC.4}
\]

The reflection theorem also gives the depth floor

\[
r>Y_-(\alpha):=\sin(\pi/3-\alpha).
\tag{PC.5}
\]

The proof of that depth floor only needs `alpha<pi/6`: the earlier argument uses
`h<1/2`, the monotonicity of cosine below `2pi/3`, and strict endpoint separation.
The stronger `pi/12` threshold was needed by an older pointwise apex-injectivity
argument, not by the reflection geometry.

## 2. Every exterior witness has its foot inside the loaded base

### Lemma PC.1 — foot-interiority

For every exterior reflection witness `z=(u,-r)` satisfying (PC.1)--(PC.4),

\[
\boxed{|u|<c.}
\tag{PC.6}
\]

Hence the perpendicular projection of `z` onto the base line is a point of
`relint([a,b])`.

### Proof

Put `U=|u|`.

First suppose `r<1` and set

\[
B:=\sqrt{1-r^2}.
\]

Separation from the nearer base endpoint gives

\[
|U-c|>B.
\tag{PC.7}
\]

If `U>c+B`, then

\[
U^2+(r-h)^2
>(c+B)^2+(r-h)^2.
\]

But

\[
(c+B)^2-\bigl(1-(r-h)^2\bigr)
=1+2cB-2rh
>1-2h>0,
\tag{PC.8}
\]

because `h<1/2`. Thus `U^2+(r-h)^2>1`, contradicting either (PC.2) or (PC.3).
Therefore the other branch of (PC.7) holds:

\[
U<c-B<c.
\]

Now suppose `r>=1`. If `U>=c`, then

\[
|z-x^-|^2
=U^2+(r-h)^2
\ge c^2+(r-h)^2
=1+r(r-2h).
\]

Since `r>=1>2h`, the right side is strictly larger than `1`, again contradicting
(PC.2) or (PC.3). Hence `U<c` in this case as well. QED.

## 3. One exterior witness can belong to only one tooth side

Let

\[
p=(u,0)\in\operatorname{relint}[a,b]
\]

be the perpendicular foot of `z`. Since `F` lies in `y>=0`, every `v in F` satisfies

\[
|z-v|\ge r=|z-p|,
\]

with equality only at `p`. Therefore

\[
\boxed{p=\operatorname{proj}_F(z),}
\tag{PC.9}
\]

where `proj_F` is the Euclidean projection onto the closed convex set `F`.

Euclidean projection onto a closed convex set is unique. Consequently the same source
point `z` cannot be an exterior reflection witness for two distinct loaded sides: a
second witnessed side would give a second relative-interior perpendicular foot and
hence a second nearest point of `F`.

Thus

\[
\boxed{
\text{exterior reflection witnesses are injective across distinct tooth bases.}
}
\tag{PC.10}
\]

This is stronger than any disk-packing reuse bound.

## 4. Each witnessed side costs a fixed amount of source-hull perimeter

Let `K=conv(A)` be the full source hull. The loaded vertices are actual source-hull
extreme vertices, so consecutive loaded vertices `a,b` define one cap in the canonical
exterior-cap decomposition of `K\setminus F`.

Because `z` lies strictly outside the supporting line of `[a,b]`, this cap is
nondegenerate. Write

\[
s:=|a-b|=2c
\]

and let `L_K(a,b)` be the length of the corresponding source-hull boundary arc from
`a` to `b` outside `F`.

The cap is convex and contains the triangle `conv{a,b,z}`. Perimeter is monotone under
convex inclusion, so

\[
s+L_K(a,b)
\ge s+|z-a|+|z-b|.
\]

Therefore

\[
L_K(a,b)-s
\ge |z-a|+|z-b|-2c.
\tag{PC.11}
\]

For fixed `c,r`, the right side is minimized at `u=0`, hence

\[
|z-a|+|z-b|
\ge2\sqrt{c^2+r^2}.
\]

Thus

\[
L_K(a,b)-s
\ge2\bigl(\sqrt{c^2+r^2}-c\bigr).
\tag{PC.12}
\]

For an `eta`-shallow tooth, `c<=1` and

\[
r>Y_-(\alpha)
\ge Y_-(\alpha_\eta)=:Y_\eta.
\]

The function `sqrt(c^2+r^2)-c` decreases in `c` and increases in `r`, so every exterior
witnessed shallow side obeys the uniform bound

\[
\boxed{
L_K(a,b)-|a-b|
>g_\eta:=2\bigl(\sqrt{1+Y_\eta^2}-1\bigr)>0.
}
\tag{PC.13}
\]

Distinct witnessed tooth sides are distinct exterior caps by (PC.10). Summing their
arc-minus-chord increments gives, if `M_ext(eta)` is the number of `eta`-shallow tooth
occurrences using exterior witnesses,

\[
\boxed{
\operatorname{per}(K)-\operatorname{per}(F)
>g_\eta M_{ext}(\eta).
}
\tag{PC.14}
\]

## 5. Type-II perimeter saturation kills the exterior branch

In the current no-container Type-II full-core branch,

\[
{\operatorname{per}(F)\over D}\to\pi.
\tag{PC.15}
\]

Every convex set of diameter at most `D` has perimeter at most `pi D`, so

\[
0\le\operatorname{per}(K)-\operatorname{per}(F)
\le\pi D-\operatorname{per}(F)
=o(D).
\tag{PC.16}
\]

Combining (PC.14) and (PC.16), for every fixed shallow threshold with
`alpha_eta<pi/6`,

\[
\boxed{M_{ext}(\eta)=o(D).}
\tag{PC.17}
\]

Therefore all but `o(D)` shallow tooth occurrences must have an upper reflection
blocker.

## 6. Current low-`t` tooth branch

Use the global-turn threshold

\[
\eta={4\over15}.
\tag{PC.18}
\]

Then

\[
\cos\alpha_\eta={13\over15}>{\sqrt3\over2},
\qquad
\sin\alpha_\eta={2\sqrt{14}\over15},
\qquad
\alpha_\eta<\pi/6.
\tag{PC.19}
\]

The current low-`t` tooth alternative and detour bound give

\[
\boxed{
{N_{sh}(4/15)\over D}
\ge0.4255744656201161781\ldots-o(1).
}
\tag{PC.20}
\]

The global-turn shallow-apex theorem says at most two of these tooth occurrences can
be duplications at a common apex. By (PC.17), only `o(D)` of them can use exterior
reflection witnesses. Hence

\[
\boxed{
\text{at least }
0.4255744656201161781\ldots D-o(D)
\text{ distinct shallow apices have an upper blocker.}
}
\tag{PC.21}
\]

For every such apex `x`, the reflection theorem supplies a source point `y` satisfying

\[
\boxed{
|x-y|>D-2h_\eta
=D-{4\sqrt{14}\over15}
=D-0.997775303139718\ldots,
}
\tag{PC.22}
\]

and, in coordinates whose tangent axis is the loaded base and whose inward normal is
positive,

\[
\boxed{
q>0,
\qquad
{|p|\over q}<\tan\alpha_\eta
={2\sqrt{14}\over13}
=0.575639597965222\ldots.
}
\tag{PC.23}
\]

The eliminated exterior branch had the uniform witness depth

\[
Y_\eta
={13\sqrt3-2\sqrt{14}\over30}
=0.501111524161584\ldots,
\tag{PC.24}
\]

so its per-cap perimeter cost in (PC.13) is

\[
g_\eta
=2\left(\sqrt{1+Y_\eta^2}-1\right)
=0.237063038582101\ldots.
\tag{PC.25}
\]

## 7. Cap-count and area side effects

Foot-interiority gives more than the perimeter contradiction. Every exterior witness
lies in a distinct nondegenerate exterior cap over its tooth side. Therefore

\[
k\ge M_{ext}(\eta),
\tag{PC.26}
\]

where `k` is the nondegenerate-cap count in the exact exterior-cap capacity identity.

Also the triangle `conv{a,b,z}` lies in that cap and has area

\[
{1\over2}|a-b|r
>{1\over2}(2-\eta)Y_\eta.
\tag{PC.27}
\]

The interiors of these witness triangles are disjoint for distinct sides: every
interior point outside `F` has perpendicular projection in the relative interior of
its associated side, and convex projection is unique. Thus

\[
\operatorname{area}(K)-\operatorname{area}(F)
>{1\over2}(2-\eta)Y_\eta M_{ext}(\eta).
\tag{PC.28}
\]

At `eta=4/15`, the area coefficient per witness is

\[
{13\over15}Y_\eta
=0.434296654273373\ldots.
\]

The perimeter argument is stronger because Type II already has only `o(D)` perimeter
headroom. Equations (PC.26)--(PC.28) are retained for the exact exterior-cap ledger.

## 8. Frontier effect

The current tooth branch has changed qualitatively:

```text
>= 0.425574 D shallow tooth occurrences
 -> reflect each apex across its loaded base
 -> exterior witnesses would create distinct source-hull caps
 -> each such cap costs >= 0.237063... perimeter
 -> per(F)=pi D-o(D), per(K)<=pi D
 -> only o(D) exterior witnesses
 -> >= 0.425574 D-o(D) distinct shallow apices are diameter-blocked
 -> each blocker is within <0.998 of diameter and lies in the base-normal cone.
```

This is a direct bridge from the tooth geometry to the diameter scale. It removes the
exterior-isolate escape rather than merely counting it.

C-II remains open because the upper blockers need not be exact diameter edges and one
source point may block many shallow apices. The next target is now sharply defined:
convert the linear family of normal-aligned `D-O(1)` pairs into an actual-diameter
thrackle or force-hull width contradiction.

## 9. Reproducibility

Run

```bash
python3 research/verify_target_c_tooth_reflection_perimeter_collapse.py
```

for the exact constants and finite geometric regression checks.
