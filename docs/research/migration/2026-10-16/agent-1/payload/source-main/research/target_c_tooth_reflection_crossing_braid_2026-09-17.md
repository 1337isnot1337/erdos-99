# Target C-II — flat-cap dispersion forces a growing pairwise-crossing reflection braid

**Date:** 2026-09-17  
**Status:** proof-only continuation of the shallow-tooth reflection branch; no canonical promotion claimed  
**Scope:** Type-II full-core shallow-tooth branch at the dedicated threshold `eta=4/15`  
**Dependencies:** reflection/perimeter collapse; global-turn apex multiplicity; same-center full-source disk sandwich; fixed-slack blocker localization; canonical exterior-cap decomposition  
**Certificate:** `research/verify_target_c_tooth_reflection_crossing_braid_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The dedicated shallow-tooth branch contains

\[
U_D>(u_4-o(1))D,
\qquad
u_4=0.4255744656201161781\ldots,
\tag{CB.1}
\]

distinct upper-blocked `eta`-shallow teeth at

\[
\eta={4\over15}.
\]

The fixed-slack matching theorem used only the near-diameter graph degree and extracted an arbitrary `Omega(D^(1/4))` vertex-disjoint matching. That loses the cyclic order of the loaded bases.

The source-hull cap ledger recovers that order. Since

\[
\operatorname{per}(K)-\operatorname{per}(F)=o(D),
\tag{CB.2}
\]

all but `o(D)` of the blocked tooth bases have an exterior source-hull cap whose arc exceeds its chord by `o(1)`. Those flat-cap bases are quantitatively tangent to the same-center near-disk from the full-source Bonnesen theorem. Consequently their inward base normals and their upper-blocker chord directions differ by only

\[
O(D^{-1/4}).
\tag{CB.3}
\]

Now partition one winning normal quadrant into bins of width

\[
w_D:=D^{-1/8}.
\tag{CB.4}
\]

A bin can contain only

\[
\left({15\over52}+o(1)\right)D^{7/8}
\tag{CB.5}
\]

flat blocked bases. Hence there are linearly many occupied bins on the `D^(1/8)` scale. Taking one residue class modulo three produces more than

\[
\boxed{
(0.122943734512478\ldots-o(1))D^{1/8}
}
\tag{CB.6}

blocked teeth whose inward normals are pairwise separated by at least `2D^-1/8` and all lie in one quadrant.

For sufficiently large `D`, (CB.3) is negligible compared with (CB.4). Their chosen reflection-blocker chords therefore have pairwise projective angle at least `D^-1/8`. The fixed-slack star theorem makes their endpoints automatically distinct. Their midpoints all lie in the common `O(D^(3/4))` circumcenter ball, so the intersection of any two supporting lines lies only

\[
O(D^{7/8})=o(D)
\]

from the chord midpoints. Since each blocker has length `D-O(1)`, every such line intersection lies in the relative interiors of both blocker segments.

Thus:

> **Reflection crossing-braid theorem.** The shallow-tooth upper-blocker branch contains a family `B_D` of pairwise vertex-disjoint inactive source pairs with
> \[
> |B_D|>
> (0.122943734512478\ldots-o(1))D^{1/8},
> \]
> every pair in `B_D` crosses properly, every edge has length greater than
> \[
> D-{4\sqrt{14}\over15},
> \]
> and every edge retains its own distinct shallow-tooth base/apex/reflection tag.

This is a genuine approximate-thrackle normal form: the branch no longer permits the reflection blockers to hide in unrelated stars or an arbitrary near-parallel matching. It still does not promote them to actual diameter edges, so C-II is not closed.

---

## 1. Flat-cap purification

Let

\[
E_D:=\operatorname{per}(K)-\operatorname{per}(F)=o(D).
\tag{CB.7}
\]

For each loaded side `ab`, let

\[
e(ab):=L_K(a,b)-|a-b|\ge0
\]

be the excess of the associated source-hull cap arc over the loaded chord. The canonical cap decomposition gives

\[
\sum_{ab}e(ab)=E_D.
\tag{CB.8}
\]

Set

\[
\tau_D:=\sqrt{E_D/D}+D^{-1/4}.
\tag{CB.9}
\]

Then

\[
\tau_D=o(1),
\qquad
{E_D\over\tau_D}=o(D).
\tag{CB.10}
\]

Call a blocked shallow tooth base **flat** when

\[
e(ab)\le\tau_D.
\]

At most `E_D/tau_D=o(D)` blocked bases are nonflat, so the family (CB.1) still contains

\[
(u_4-o(1))D
\tag{CB.11}

flat blocked bases.

The global-turn theorem says all but two shallow tooth occurrences have distinct apices. Deleting those two exceptions does not change (CB.11).

---

## 2. A flat cap has `o(1)` depth

Fix one flat tooth base. Put

\[
a=(-c,0),
\qquad
b=(c,0),
\qquad
s:=|a-b|=2c.
\]

For `eta=4/15`, shallowness gives

\[
\boxed{s\ge2-\eta={26\over15}.}
\tag{CB.12}
\]

Also `s<2` because the base is a nonunit chord of two unit tooth edges.

Let `z` lie on the exterior source-hull cap arc from `a` to `b`, and let `H=dist(z,ab)`. The two subarcs from `a` to `z` and `z` to `b` have total length at most

\[
s+\tau_D.
\]

Therefore

\[
|a-z|+|z-b|\le s+\tau_D.
\]

For fixed height `H`, the left side is minimized when the perpendicular foot of `z` is the midpoint of `ab`, giving

\[
2\sqrt{{s^2\over4}+H^2}
\le s+\tau_D.
\]

Hence

\[
H^2
\le {s\tau_D\over2}+{\tau_D^2\over4}
\le \tau_D+{\tau_D^2\over4}.
\tag{CB.13}
\]

Put

\[
H_D:=\sqrt{\tau_D+\tau_D^2/4}=o(1).
\tag{CB.14}
\]

Every point of every flat cap lies within distance `H_D` of its loaded base line.

---

## 3. The same-center annulus aligns a flat base with the circumcenter

Use the same-center full-source disk sandwich with circumcenter `o`:

\[
B(o,R_-)
\subset K
\subset B(o,R_+),
\tag{CB.15}
\]

where

\[
R_-={D\over2}-2\eta_D,
\qquad
R_+={D\over2}+\eta_D,
\qquad
\eta_D=3^{1/4}\sqrt D.
\tag{CB.16}
\]

Orient the base coordinates so the loaded force hull lies in `y>=0`; the inward unit normal is

\[
n=(0,1).
\]

By convexity and the canonical exterior-cap decomposition, the portion of `K` on the exterior side `y<0` is precisely the cap over `ab`. Equation (CB.14) therefore gives

\[
K\subset\{y\ge-H_D\}.
\tag{CB.17}
\]

Write the circumcenter relative to the base midpoint as

\[
o=(p,q).
\]

The inner disk in (CB.15) must also lie in (CB.17), hence

\[
q-R_-\ge-H_D,
\]

so

\[
\boxed{q\ge R_--H_D.}
\tag{CB.18}
\]

The two base endpoints belong to `K` and hence to `B(o,R_+)`. Therefore

\[
(p-c)^2+q^2\le R_+^2,
\qquad
(p+c)^2+q^2\le R_+^2.
\]

Thus

\[
(|p|+c)^2+q^2\le R_+^2.
\tag{CB.19}
\]

Define

\[
S_D:=
\sqrt{R_+^2-(R_--H_D)^2}.
\tag{CB.20}
\]

Equations (CB.18)--(CB.19) imply

\[
|p|+c\le S_D.
\tag{CB.21}
\]

Since `R_+-R_-=3eta_D=O(sqrt D)`, while `H_D=o(1)`,

\[
\boxed{S_D=O(D^{3/4}).}
\tag{CB.22}
\]

Let `x=(0,h)` be the shallow tooth apex, so `0<h<1`. The vector from `x` toward the circumcenter is

\[
o-x=(p,q-h).
\]

Equations (CB.18), (CB.21) give

\[
\angle(n,o-x)
\le
\arctan{S_D\over R_--H_D-1}
=O(D^{-1/4}).
\tag{CB.23}

Thus a flat tooth's inward base normal is already inverse-quarter-power close to the radial direction toward the common circumcenter.

---

## 4. Its reflection blocker has the same direction to inverse-quarter-power accuracy

At `eta=4/15`, every retained reflection blocker `xy` has

\[
|x-y|>D-C_4,
\qquad
C_4={4\sqrt{14}\over15}<1.
\tag{CB.24}
\]

Let

\[
m={x+y\over2}
\]

be its midpoint. The fixed-slack localization theorem gives

\[
|m-o|<L_D,
\qquad
L_D=O(D^{3/4}).
\tag{CB.25}
\]

Orient the blocker direction from the shallow apex toward its blocker:

\[
d={y-x\over|y-x|}.
\]

Since

\[
m-x={|x-y|\over2}d,
\]

while `(o-x)-(m-x)=o-m`, equations (CB.24)--(CB.25) give

\[
\angle(d,o-x)=O(D^{-1/4}).
\tag{CB.26}
\]

Combining with (CB.23), uniformly over the flat blocked family,

\[
\boxed{
\angle(d,n)=O(D^{-1/4}).
}
\tag{CB.27}

This is substantially sharper than the original fixed `alpha_eta<pi/6` reflection cone.

---

## 5. A `D^-1/8` normal bin contains only `O(D^(7/8))` flat blocked bases

Fix an angular interval `I` of inward base normals of width

\[
w_D=D^{-1/8}<\frac\pi2.
\]

Let `n_0` be its central normal and `t_0` the corresponding positively oriented tangent.

The flat loaded sides with normals in `I` occur in one contiguous boundary block of the convex loaded hull. Traverse that block in boundary order. Every side tangent makes angle at most `w_D/2` with `t_0`, so its positive projection on `t_0` is at least its length times

\[
\cos(w_D/2).
\tag{CB.28}
\]

Consider an endpoint `z` of a flat selected side whose inward normal is `n in I`. Relative to its base midpoint and the common center `o`, equation (CB.21) says its tangential coefficient has absolute value at most `S_D`, while its normal distance from `o` is at most `R_+`. Therefore

\[
|(z-o)\cdot t_0|
\le
S_D+R_+\sin(w_D/2).
\tag{CB.29}
\]

Take the first and last selected flat bases in the bin. Summing positive tangent projections over the intervening convex boundary block and using (CB.29),

\[
\sum_{ab\in I}|a-b|\cos(w_D/2)
\le
2S_D+2R_+\sin(w_D/2).
\tag{CB.30}
\]

By (CB.12), every selected base has length at least `26/15`. Thus the number `N_I` of flat blocked bases in the bin satisfies

\[
N_I
\le
{15\over26}
{2S_D+2R_+\sin(w_D/2)\over\cos(w_D/2)}.
\tag{CB.31}
\]

Now

\[
S_D=O(D^{3/4})=o(D^{7/8}),
\]

and

\[
2R_+\sin(w_D/2)
=\left({1\over2}+o(1)\right)D^{7/8}.
\]

Therefore

\[
\boxed{
N_I
\le
\left({15\over52}+o(1)\right)D^{7/8}.
}
\tag{CB.32}

---

## 6. Extract separated normal bins with an explicit coefficient

Partition the oriented normal circle into four fixed quadrants. By (CB.11), one quadrant contains at least

\[
\left({u_4\over4}-o(1)\right)D
\tag{CB.33}

flat blocked bases.

Partition that quadrant into consecutive bins of width `w_D=D^-1/8`. By (CB.32), the number of occupied bins is at least

\[
\left(
{u_4/4\over15/52}-o(1)
\right)D^{1/8}
=
\left({13u_4\over15}-o(1)ight)D^{1/8}.
\tag{CB.34}
\]

Color the bins by their index modulo three and retain the largest color class. Choose one flat blocked tooth from every retained occupied bin. The number selected is more than

\[
\left({13u_4\over45}-o(1)ight)D^{1/8}.
\tag{CB.35}

Since

\[
{13u_4\over45}
=0.122943734512478\ldots,
\]

this is (CB.6).

Two retained bins have at least one entire intervening bin, so their inward normals differ by at least

\[
2w_D.
\tag{CB.36}
\]

All retained normals lie in one quadrant, so their oriented separation is at most `pi/2`.

---

## 7. The selected blockers are automatically vertex-disjoint

Choose one upper reflection blocker for every selected tooth. Equation (CB.27) gives a uniform angular error

\[
\zeta_D=O(D^{-1/4})=o(w_D)
\tag{CB.37}

between its oriented blocker direction and the corresponding inward base normal.

Hence for any two selected blocker lines, their projective angle is at least

\[
2w_D-2\zeta_D>w_D
\tag{CB.38}

for sufficiently large `D`.

Suppose two selected blocker edges shared a source endpoint. If they were the same undirected edge, their projective directions would agree, contradicting (CB.38). Otherwise that common source point would have two distinct neighbors at distance greater than `D-C_4` whose ray directions differ projectively by more than `w_D`.

But the fixed-slack star proof gives every pair of such rays at one source vertex ordinary angular separation

\[
O(D^{-1/4})=o(w_D).
\]

Contradiction. Therefore the selected blockers are pairwise vertex-disjoint.

---

## 8. Every two selected blocker segments cross properly

Let two selected blocker segments have midpoints `m_1,m_2`, directions `d_1,d_2`, and lengths `ell_1,ell_2`.

Their acute line angle `theta` obeys

\[
\theta>w_D
\tag{CB.39}
\]

by (CB.38) and the common-quadrant restriction.

Both midpoints lie in `B(o,L_D)` by (CB.25), so

\[
|m_1-m_2|<2L_D=O(D^{3/4}).
\tag{CB.40}
\]

Let the supporting lines meet at `z`. Solving the two-line intersection equation gives

\[
|z-m_i|
\le
{|m_1-m_2|\over\sin\theta}
\le
{2L_D\over\sin w_D}
=O(D^{7/8})
=o(D)
\tag{CB.41}
\]

for `i=1,2`.

On the other hand

\[
{\ell_i\over2}>{D-C_4\over2}.
\tag{CB.42}
\]

Therefore, for sufficiently large `D`,

\[
|z-m_i|<{\ell_i\over2}
\]

for both segments. Their line intersection lies in the relative interior of each blocker segment.

Because the blocker edges are vertex-disjoint, this is a proper crossing. The argument applies to every pair, proving the theorem.

---

## 9. Frontier effect

The tooth-reflection branch has now progressed through three multiplicity scales:

```text
linear blocked shallow-tooth population;
    -> fixed-slack star degree O(D^(3/4));
    -> Omega(D^(1/4)) arbitrary vertex-disjoint matching;
    -> Omega(D^(1/8)) vertex-disjoint pairwise-crossing braid
       with cyclically separated loaded-base normals.
```

The last family is an approximate geometric thrackle, but its edges remain inactive by a fixed additive slack below `D`. Exact diameter thrackle theorems therefore cannot yet be applied directly.

The next useful bridge is now precise: upgrade the pairwise-crossing braid from `D-C_4` to `D-o(1)`/actual diameter using the shallow-tooth reflection normal form, or derive a source-preserving finite multi-tooth exchange from the fact that all blocker crossings occur in a common `o(D)` central region while their tagged base normals are cyclically separated.

**Disposition:** used the vanishing source-hull cap excess and the same-center annulus to align flat tooth bases with their upper blockers, then extracted an explicit `Omega(D^(1/8))` family of pairwise vertex-disjoint, pairwise properly crossing fixed-slack reflection blockers. C-II and Level I remain open.
