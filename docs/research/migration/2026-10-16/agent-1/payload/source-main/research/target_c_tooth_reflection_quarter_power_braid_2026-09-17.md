# Target C-II — the reflection branch contains a quarter-power pairwise-crossing braid

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the shallow-tooth reflection branch; no canonical promotion claimed  
**Scope:** Type-II full-core shallow-tooth branch at `eta=4/15`  
**Dependencies:** reflection/perimeter collapse; same-center source-hull disk sandwich; fixed-slack midpoint/star bounds; flat-cap reflection crossing-braid theorem; shallow-tooth penetration matching  
**Certificate:** `research/verify_target_c_tooth_reflection_quarter_power_braid_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding reflection-braid theorem chose the normal-bin width

\[
w_D=D^{-1/8}.
\]

That choice was convenient but far from the geometric threshold.  The actual error in
aligning a flat shallow-tooth inward normal with its reflection-blocker direction is
only `O(D^-1/4)`, while fixed-slack blocker midpoints lie in an `O(D^3/4)` ball.  One
can therefore work directly at a fixed multiple of the inverse-quarter-power scale.

Taking

\[
\boxed{w_D=14D^{-1/4}}
\tag{QB.1}
\]

is already enough.  It yields a pairwise vertex-disjoint family `B_D` of reflection
blockers with

\[
\boxed{
|B_D|>
(0.00560157806945454\ldots-o(1))D^{1/4}.
}
\tag{QB.2}
\]

Every two edges of `B_D` cross properly.  Every edge has length greater than

\[
D-{4\sqrt{14}\over15}.
\tag{QB.3}
\]

Moreover the retained tooth gadgets can be made completely vertex-disjoint without
another density loss: for each selected blocker `x_i y_i`, if `a_i b_i` is its loaded
base and `x_i w_i` is the canonical chosen penetration contact, then the five-point
sets

\[
\boxed{
\{a_i,b_i,x_i,w_i,y_i\}
}
\tag{QB.4}
\]

are pairwise disjoint.  In particular the loaded bases are pairwise nonadjacent sides
of the loaded hull and inherit an unambiguous cyclic order.

The exponent `1/8` in the preceding crossing-braid theorem is therefore not intrinsic.
The natural scale of the current Bonnesen/midpoint machinery is already `D^(1/4)`.

---

## 1. Leading inverse-quarter-power constants

Retain the notation of the flat-cap crossing-braid proof.  Put

\[
a:=3^{1/4},
\qquad
b:=3^{1/8},
\qquad
s:=3^{5/8}.
\tag{QB.5}
\]

The same-center source-hull sandwich gives

\[
R_+={D\over2}+a\sqrt D,
\qquad
R_-={D\over2}-2a\sqrt D.
\tag{QB.6}
\]

For a flat selected tooth base the cap depth is `H_D=o(1)`, and the previous proof
defined

\[
S_D:=\sqrt{R_+^2-(R_--H_D)^2}.
\]

Since

\[
R_+^2-R_-^2
=3aD^{3/2}-3a^2D,
\qquad
2R_-H_D-H_D^2=o(D),
\]

we now record the leading constant:

\[
\boxed{
S_D=(s+o(1))D^{3/4}.
}
\tag{QB.7}
\]

The fixed-slack midpoint theorem at

\[
C_4={4\sqrt{14}\over15}
\]

gives

\[
L_D^2
=D(a\sqrt D)+a^2D+{C_4D\over2},
\]

hence

\[
\boxed{
L_D=(b+o(1))D^{3/4}.
}
\tag{QB.8}
\]

Let `n_i` be the inward normal of a flat shallow base, `x_i` its apex, and `d_i` the
oriented reflection-blocker direction from `x_i` toward its blocker.

The flat-cap radial estimate gives

\[
\angle(n_i,o-x_i)
\le
\arctan{S_D\over R_--H_D-1}
=
(2s+o(1))D^{-1/4}.
\tag{QB.9}
\]

For the blocker, let `m_i` be its midpoint and `ell_i=|x_i-y_i|`.  Since

\[
{\ell_i\over2}d_i=m_i-x_i,
\qquad
|(m_i-x_i)-(o-x_i)|=|m_i-o|<L_D,
\]

the elementary unit-vector estimate

\[
\left|
{m_i-x_i\over|m_i-x_i|}
-
{o-x_i\over|o-x_i|}
\right|
\le {4L_D\over D-C_4}
\]

gives

\[
\angle(d_i,o-x_i)
\le
2\arcsin{2L_D\over D-C_4}
=
(4b+o(1))D^{-1/4}.
\tag{QB.10}
\]

Therefore

\[
\boxed{
\angle(d_i,n_i)
\le
(A+o(1))D^{-1/4},
\qquad
A:=2s+4b
=8.5628374546\ldots .
}
\tag{QB.11}
\]

The fixed-slack star proof also has a leading constant.  If two distinct
`D-C_4` blocker edges share one source endpoint, their projective directions differ by
at most

\[
\boxed{
(B+o(1))D^{-1/4},
\qquad
B:=8b
=9.1776215235\ldots .
}
\tag{QB.12}
\]

Indeed the two relevant midpoints are both in `B(o,L_D)`, so the two opposite
endpoints differ by at most `4L_D`, exactly as in the fixed-slack star theorem.

For later use note the crude exact bounds

\[
3^{1/8}<{6\over5},
\qquad
3^{5/8}=\sqrt3\,3^{1/8}
<{7\over4}{6\over5}={21\over10}.
\tag{QB.13}
\]

Thus

\[
A<9,
\qquad
B<{48\over5}=9.6,
\qquad
2\cdot14-2A>10>B.
\tag{QB.14}
\]

This is why the fixed constant `14` in (QB.1) is sufficient.

---

## 2. A fixed inverse-quarter-power bin has only `O(D^3/4)` blocked bases

The previous bin-capacity inequality was valid before specializing the bin width.  For
an inward-normal interval `I` of width `w_D`, it says

\[
N_I
\le
{15\over26}
{2S_D+2R_+\sin(w_D/2)\over\cos(w_D/2)}.
\tag{QB.15}
\]

Insert

\[
w_D=14D^{-1/4}.
\]

Equations (QB.6)--(QB.8) give

\[
2S_D=(2s+o(1))D^{3/4}
\]

and

\[
2R_+\sin(w_D/2)
=(7+o(1))D^{3/4}.
\]

Hence

\[
\boxed{
N_I
\le
(C_{14}+o(1))D^{3/4},
\qquad
C_{14}:={15\over26}(2s+7)
=6.33116924587\ldots .
}
\tag{QB.16}
\]

This is the only change needed in the dispersion count.

---

## 3. Linear blocked population gives `Omega(D^1/4)` separated bins

The dedicated `eta=4/15` reflection/perimeter theorem supplies

\[
U_D>(u_4-o(1))D,
\qquad
u_4=0.4255744656201161781\ldots .
\tag{QB.17}
\]

As in the preceding crossing-braid proof, deleting the nonflat caps costs only `o(D)`.
One of four normal quadrants therefore contains more than

\[
\left({u_4\over4}-o(1)\right)D
\tag{QB.18}
\]

flat blocked bases.

Partition that quadrant into consecutive bins of width `14D^-1/4`.  By (QB.16), the
number of occupied bins is more than

\[
\left(
{u_4/4\over C_{14}}-o(1)
\right)D^{1/4}.
\tag{QB.19}
\]

Color the bins by index modulo three and retain the largest color class.  Choose one
flat blocked tooth from every retained occupied bin.  The retained inward normals are
pairwise separated by at least

\[
2w_D=28D^{-1/4},
\tag{QB.20}
\]

and their number is greater than

\[
\boxed{
\left(c_{14}-o(1)\right)D^{1/4},
}
\tag{QB.21}
\]

where

\[
\boxed{
c_{14}
={u_4\over12C_{14}}
={13u_4\over90(2\,3^{5/8}+7)}
=0.00560157806945454\ldots .
}
\tag{QB.22}
\]

All retained normals remain in one quadrant.

---

## 4. Blocker endpoints are automatically distinct

Choose one reflection blocker for each retained tooth.  By (QB.11), two retained
blocker directions have projective separation at least

\[
\begin{aligned}
28D^{-1/4}
-2(A+o(1))D^{-1/4}
&=
(28-2A-o(1))D^{-1/4}\\
&>(10-o(1))D^{-1/4}.
\end{aligned}
\tag{QB.23}
\]

If two blocker edges shared a source endpoint, the fixed-slack star estimate (QB.12)
would instead give separation less than

\[
(9.6+o(1))D^{-1/4}.
\]

For sufficiently large `D` these statements are incompatible.  Therefore all retained
blocker edges are pairwise vertex-disjoint.

This also excludes the possibility that two retained directed blockers are opposite
orientations of the same physical source pair.

---

## 5. Every two retained blocker segments cross properly

Let two selected blocker edges have midpoints `m_1,m_2` and supporting-line acute
angle `phi`.  By (QB.8),

\[
|m_1-m_2|\le2L_D=(2b+o(1))D^{3/4}.
\tag{QB.24}
\]

Equation (QB.23) gives

\[
\phi\ge(28-2A-o(1))D^{-1/4}.
\tag{QB.25}
\]

If `z` is the intersection of the two supporting lines, elementary two-line geometry
gives, for `j=1,2`,

\[
|z-m_j|
\le {|m_1-m_2|\over\sin\phi}.
\tag{QB.26}
\]

Consequently

\[
\limsup_{D\to\infty}{|z-m_j|\over D}
\le
{2b\over28-2A}
={b\over14-A}
=0.2109928994\ldots
<\frac14.
\tag{QB.27}
\]

Each blocker has half-length

\[
{|x_i-y_i|\over2}
>{D-C_4\over2}
=\left({1\over2}-o(1)\right)D.
\]

Thus the line intersection lies strictly inside both blocker segments for sufficiently
large `D`.  Because the segments are vertex-disjoint, the intersection is proper.
This proves the pairwise-crossing claim in (QB.2).

The previous `D^(1/8)` proof used `w_D >> D^-1/4` to make the same conclusion by a
scale separation.  Equation (QB.27) shows that a sufficiently large fixed multiple of
`D^-1/4` already leaves a large quantitative interior margin.

---

## 6. The loaded bases are pairwise endpoint-disjoint

The selected normal gap also removes the remaining base-overlap caveat from the fixed
slack matching theorem.

Suppose two retained loaded bases shared a loaded endpoint `v`.  Their shallow apices
`x_i,x_j` satisfy

\[
|x_i-v|=|x_j-v|=1,
\]

so

\[
|x_i-x_j|\le2.
\tag{QB.28}
\]

Both vectors `o-x_i,o-x_j` have length `D/2+O(sqrt D)`, hence (QB.28) implies

\[
\angle(o-x_i,o-x_j)=O(D^{-1}).
\tag{QB.29}
\]

Using only the base-normal part of (QB.11), namely

\[
\angle(n_i,o-x_i)
\le(2s+o(1))D^{-1/4},
\]

we get

\[
\angle(n_i,n_j)
\le
(4s+o(1))D^{-1/4}.
\tag{QB.30}
\]

But

\[
4s<4{21\over10}=8.4<28,
\]

contradicting the selected normal separation (QB.20).  Hence no two retained bases
share a loaded endpoint.  They are pairwise nonadjacent sides of the convex loaded
hull.

---

## 7. Add the penetration contacts without any further thinning

For every selected shallow tooth choose the penetration contact `x_iw_i` from the
existing `eta=4/15` penetration-matching theorem.  Globally, those contacts already
satisfy

\[
\{x_i\}\text{ pairwise distinct},
\qquad
\{w_i\}\text{ pairwise distinct},
\qquad
\{x_i\}\cap\{w_i\}=\varnothing,
\tag{QB.31}
\]

and `x_i,w_i` are unloaded while `a_i,b_i` are loaded.

It remains only to rule out a reflection blocker head `y_j` coinciding with one of the
local vertices of a different tooth gadget.

All selected inward normals lie in one quadrant.  From (QB.9), the radial directions
`o-x_i` therefore have pairwise angle at most

\[
{\pi\over2}+o(1).
\]

Also every source point lies in `B(o,R_+)`.  Hence

\[
\boxed{
|x_i-x_j|
\le
\left({1\over\sqrt2}+o(1)\right)D
}
\tag{QB.32}
\]

uniformly over selected apexes.

Every local vertex

\[
z_i\in\{a_i,b_i,w_i\}
\]

satisfies `|z_i-x_i|=1`.  Thus

\[
|x_j-z_i|
\le
\left({1\over\sqrt2}+o(1)\right)D+1.
\tag{QB.33}
\]

On the other hand a reflection blocker head `y_j` satisfies

\[
|x_j-y_j|>D-C_4.
\tag{QB.34}
\]

Because `1/sqrt(2)<1`, equations (QB.33)--(QB.34) imply, for all sufficiently large
`D`,

\[
y_j\notin\{a_i,b_i,w_i\}
\]

for every pair of selected indices `i,j`.  The blocker matching itself already gives
pairwise distinct `x_i,y_i` endpoints, while Section 6 gives pairwise disjoint base
endpoints.

Therefore the five-point tooth/reflection/penetration gadgets in (QB.4) are pairwise
vertex-disjoint with no extra constant-factor loss.

---

## 8. Resulting normal form and remaining obstruction

The shallow-tooth reflection branch now contains

\[
\boxed{
(0.00560157806945454\ldots-o(1))D^{1/4}
}
\]

pairwise disjoint five-point gadgets with all of the following simultaneous structure:

- `a_i b_i` is a distinct nonadjacent loaded-hull side of length at least `26/15`;
- `x_i` is its shallow unloaded tooth apex;
- `x_iw_i` is the distinct inward penetration contact;
- `x_iy_i` has length greater than `D-4sqrt(14)/15`;
- the blocker chords `x_iy_i` cross pairwise properly;
- the inward base normals are cyclically ordered, lie in one quadrant, and are
  separated by at least `28D^-1/4`;
- the blocker directions preserve that separated normal order up to an
  `O(D^-1/4)` error;
- all five source vertices attached to different gadgets are distinct.

This is stronger than both preceding reflection normal forms: it has the full
`D^(1/4)` exponent of the arbitrary blocker matching and the pairwise-crossing/order
structure of the earlier `D^(1/8)` braid.

It still does not turn the blockers into actual diameter edges.  The remaining closure
problem is therefore genuinely geometric: exploit the ordered nonadjacent loaded bases
and the pairwise-crossing, normal-aligned `D-O(1)` chords together.  A useful next
statement would show that such a quarter-power family either forces a forbidden
source-hull width oscillation or permits a simultaneous reflection/diameter-decreasing
motion.

**Disposition:** optimized the flat-cap dispersion scale from `D^-1/8` to the fixed
`14D^-1/4` threshold, upgrading the reflection braid from `Omega(D^(1/8))` to an
explicit `Omega(D^(1/4))` pairwise-crossing family and simultaneously making the full
five-point tooth gadgets vertex-disjoint.  C-II and Level I remain open.
