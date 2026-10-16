# Target C-II - loaded reflection heads force an exact diameter braid

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the shallow-tooth reflection branch; no canonical promotion claimed  
**Scope:** Type-II full-core slow-scale reflection family at `eta=3/26`  
**Dependencies:** slow-scale central reflection braid; simultaneous reflection block diagonalization; canonical-hull farthest blocker theorem; radial-interface loaded-sink theorem; exact diameter support-normality; full-source diameter midpoint localization; convex diameter-thrackle property  
**Certificate:** `research/verify_target_c_tooth_reflection_loaded_head_exact_diameter_braid_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The radial-interface theorem gives a sharp dichotomy for the canonical farthest head `y_i` of every reflection module:

\[
y_i\in B_+
\quad\text{or}\quad
\deg_C(y_i)=\deg_H(y_i)=0.
\]

The first branch can be strengthened substantially. A loaded canonical head does not merely contribute some actual diameter edge. The reflection support normal and an actual diameter normal both lie in the same convex normal cone at `y_i`. Distinct canonical heads occupy distinct source-hull vertices, whose normal-cone widths have total at most `2pi`. Therefore most loaded heads have an actual diameter direction within `O(omega_D^{-2})` of the reflection normal.

At the natural slow scale

\[
\kappa_D={D^{1/4}\over\omega_D^2},
\qquad
\omega_D\to\infty,
\qquad
\omega_D=o(D^{1/8}),
\tag{LB.1}
\]

the full reflection family has `Theta(omega_D^2)` modules and consecutive selected normals are already separated at scale `omega_D^{-2}`. A constant-factor spacing extraction therefore turns the loaded branch into `Theta(omega_D^2)` **vertex-disjoint actual diameter edges**, every two crossing properly. The partner endpoint of each exact diameter lies within `O(D/omega_D^2)` of the corresponding reflected apex `q_i`, and all mutual diameter crossings lie in one

\[
O(D^{3/4}\omega_D^2)=o(D)
\]
central disk.

Thus the full slow-scale reflection family has the following new two-way normal form:

\[
\boxed{
\begin{array}{ll}
\text{FREE-HEAD:}&\Theta(\omega_D^2)\text{ canonical heads have }\deg_C=\deg_H=0;\\[1mm]
\text{LOADED-HEAD:}&\Theta(\omega_D^2)\text{ tagged, vertex-disjoint actual diameters}\n\\
&\text{form an exact crossing braid through one }o(D)\text{ core.}
\end{array}}
\tag{LB.2}
\]

This removes the factor-`omega_D` loss in the first loaded-head corollary and promotes the loaded escape from a count of arbitrary diameter incidences to an ordered exact-diameter braid geometrically coupled to the reflected positions.

---

## 1. Use the full slow-scale module family

The slow-scale theorem gives, for every `kappa_D` satisfying

\[
\kappa_D\to\infty,
\qquad
\kappa_D=o(D^{1/4}),
\]

a selected family of pairwise-disjoint full tooth gadgets of size

\[
M_D>
(c_*-o(1)){D^{1/4}\over\kappa_D},
\qquad
c_*=0.129220199818177\ldots .
\tag{LB.3}
\]

Take (LB.1). Then

\[
\boxed{M_D>(c_*-o(1))\omega_D^2.}
\tag{LB.4}
\]

All selected tooth normals `n_i` lie in one fixed quadrant and satisfy

\[
\boxed{
\angle(n_i,n_j)
\ge(2-o(1)){1\over\omega_D^2}
\qquad(i\ne j),
}
\tag{LB.5}
\]

with the ordinary lifted angle in that quadrant. In their linear order, consecutive selected normals therefore have this same lower gap.

Let `q_i` be the reflected apex and `U_i` its blocker set. The simultaneous reflection theorem gives

\[
\angle(q_i-o,-n_i)=O(D^{-1/4}),
\qquad
|q_i-o|={D\over2}+O(\sqrt D),
\tag{LB.6}
\]

and the geometric tube theorem gives, for every blocker `z in U_i`,

\[
\angle(z-q_i,n_i)\le C_AD^{-1/4},
\qquad
C_A=9.56283745460\ldots .
\tag{LB.7}
\]

Because

\[
\omega_D^2=o(D^{1/4}),
\]

we have

\[
D^{-1/4}=o(\omega_D^{-2}).
\tag{LB.8}
\]

So the existing geometric error is negligible at the normal-spacing scale selected in (LB.5).

For each module choose the canonical blocker head `y_i`, the source point maximizing `|z-q_i|`. The blocker sets `U_i` are pairwise disjoint, hence the `y_i` are distinct.

The radial-interface theorem gives

\[
\boxed{
y_i\in B_+\quad\text{or}\quad\deg_C(y_i)=\deg_H(y_i)=0.}
\tag{LB.9}
\]

If the second alternative holds for at least half of the modules, (LB.4) already gives the FREE-HEAD branch of (LB.2). It remains to analyze the case in which at least half of the canonical heads are loaded.

---

## 2. Two support normals at one loaded canonical head

Fix a loaded head `y_i` and put

\[
L_i:=|y_i-q_i|,
\qquad
N_i:={y_i-q_i\over L_i}.
\tag{LB.10}
\]

The canonical farthest-blocker theorem says `y_i` is uniquely exposed on the full source hull `K` by `N_i`. Thus

\[
N_i\in N_K(y_i).
\tag{LB.11}
\]

Because `y_i in B_+`, choose one positive actual diameter edge `y_i t_i` and orient its diameter normal outward at `y_i`:

\[
M_i:={y_i-t_i\over D}.
\tag{LB.12}
\]

Exact diameter normality gives

\[
M_i\in N_K(y_i).
\tag{LB.13}
\]

Let `w_i` be the angular width of the convex normal cone `N_K(y_i)`, and let

\[
\theta_i:=\angle(N_i,M_i).
\]

Then

\[
0\le\theta_i\le w_i.
\tag{LB.14}
\]

The selected heads are distinct vertices of the finite convex polygon `K`. The interiors of their normal cones are disjoint, and all vertex normal cones together partition the unit normal circle. Therefore

\[
\boxed{
\sum_{i\in L_D}w_i\le2\pi,
\qquad
\sum_{i\in L_D}\theta_i\le2\pi,
}
\tag{LB.15}
\]

where `L_D` is any selected set of loaded heads.

This is the missing bridge between the reflection normal and a true diameter direction. It uses no near-circular approximation.

---

## 3. Most loaded heads have an `O(omega^-2)` aligned actual diameter

Assume the LOADED-HEAD side of (LB.9) wins. From (LB.4), for all sufficiently large `D`,

\[
|L_D|\ge {c_*\over3}\omega_D^2.
\tag{LB.16}
\]

Set the fixed constant

\[
T:={12\pi\over c_*}=291.743178668\ldots .
\tag{LB.17}
\]

By (LB.15), the number of loaded heads with

\[
\theta_i>{T\over\omega_D^2}
\]

is at most

\[
{2\pi\omega_D^2\over T}
={c_*\over6}\omega_D^2.
\]

Hence at least

\[
\boxed{
{c_*\over6}\omega_D^2
}
\tag{LB.18}
\]

loaded heads satisfy

\[
\boxed{
\theta_i\le {T\over\omega_D^2}.
}
\tag{LB.19}
\]

Call them **aligned loaded heads**.

Since `y_i in U_i`, (LB.7) gives

\[
\angle(N_i,n_i)=O(D^{-1/4})=o(\omega_D^{-2}).
\tag{LB.20}
\]

Therefore their actual diameter directions obey

\[
\boxed{
\angle(M_i,n_i)
\le {T+o(1)\over\omega_D^2}.
}
\tag{LB.21}
\]

---

## 4. Constant-factor spacing makes the diameter endpoints disjoint

Order the aligned loaded heads by the lifted normal order of `n_i`. Retain every `J`-th one, where `J` is any fixed integer satisfying

\[
J>4T+100.
\tag{LB.22}
\]

For example one may take

\[
J=1267.
\]

The retained set `R_D` still has

\[
\boxed{|R_D|=\Theta(\omega_D^2).}
\tag{LB.23}
\]

By (LB.5), two consecutive retained base normals differ by at least

\[
{2J-o(1)\over\omega_D^2}.
\tag{LB.24}
\]

Combining this with (LB.21), distinct actual diameter directions in `R_D` satisfy

\[
\boxed{
\angle(M_i,M_j)
\ge {2J-2T-o(1)\over\omega_D^2}
=\Omega(\omega_D^{-2}).
}
\tag{LB.25}
\]

They inherit the same strict order as the tooth normals.

The canonical blocker shell gives

\[
0<L_i-D<h_*.
\tag{LB.26}
\]

Using

\[
q_i=y_i-L_iN_i,
\qquad
t_i=y_i-DM_i,
\]

we obtain the exact partner-localization identity

\[
t_i-q_i=(L_i-D)N_i+D(N_i-M_i).
\]

Since `|N_i-M_i|<=theta_i`,

\[
\boxed{
|t_i-q_i|
\le h_*+{TD\over\omega_D^2}.
}
\tag{LB.27}
\]

On the other hand, (LB.6), (LB.8), and the `J`-spaced normal gap imply

\[
\boxed{
|q_i-q_j|
\ge(J-o(1)){D\over\omega_D^2}
\qquad(i\ne j\text{ consecutive in }R_D).
}
\tag{LB.28}
\]

Because `J>4T`, the balls in (LB.27) are pairwise disjoint for large `D`. Thus all partner endpoints `t_i` are distinct.

The heads `y_i` are already distinct. A cross-collision `t_i=y_j` is also impossible. Indeed, (LB.6) puts `q_i-o` near `-n_i`, while the simultaneous reflection theorem puts every `y_j-o` near `+n_j`; all `n_i,n_j` lie in one quadrant. Hence

\[
|q_i-y_j|\ge(1/\sqrt2-o(1))D,
\tag{LB.29}
\]

whereas (LB.27) is `o(D)`. Therefore

\[
\boxed{
\{y_i,t_i\}\cap\{y_j,t_j\}=\varnothing
\qquad(i\ne j\text{ in }R_D).
}
\tag{LB.30}

The retained actual diameter edges are vertex-disjoint.

---

## 5. The loaded branch is an exact crossing diameter braid

The actual diameter graph of a planar source is a convex geometric thrackle. Two vertex-disjoint actual diameter edges therefore cross properly. By (LB.30), every two retained edges `y_i t_i` cross.

Thus the loaded reflection branch contains

\[
\boxed{
\Theta(\omega_D^2)
}
\tag{LB.31}

vertex-disjoint actual diameter chords which cross pairwise and whose directions are strictly ordered with separation

\[
\Omega(\omega_D^{-2}).
\]

This is a true diameter braid, not a fixed-slack near-diameter braid.

The partner endpoint is simultaneously localized by (LB.27): each exact diameter connects the canonical blocker head `y_i` to a source point lying within

\[
O(D/\omega_D^2)
\]

of the reflected apex `q_i`. The reflection obstruction and the actual diameter support are therefore geometrically paired module-by-module.

---

## 6. All exact-diameter crossings lie in one `o(D)` core

Let `m_i=(y_i+t_i)/2` be the midpoint of one retained actual diameter. The full-source geometry theorem gives one circumcenter `o` and a universal bound

\[
|m_i-o|\le L_D,
\qquad
L_D=O(D^{3/4}).
\tag{LB.32}
\]

Take two retained diameter lines with angle `phi_ij`. Their line intersection `c_ij` satisfies the elementary two-line estimate

\[
|c_{ij}-m_i|
\le {|m_i-m_j|\over\sin\phi_{ij}}
\le {2L_D\over\sin\phi_{ij}}.
\tag{LB.33}
\]

By (LB.25),

\[
\sin\phi_{ij}=\Omega(\omega_D^{-2}),
\]

so

\[
\boxed{
|c_{ij}-o|
=O(D^{3/4}\omega_D^2).
}
\tag{LB.34}
\]

Because `omega_D=o(D^(1/8))`,

\[
D^{3/4}\omega_D^2=o(D).
\tag{LB.35}
\]

The diameter segments themselves cross by the thrackle property, so `c_ij` is their actual proper crossing point. Hence **every mutual crossing of the exact diameter braid lies in one common `o(D)` disk**.

---

## 7. Strengthened slow-scale dichotomy

For every

\[
\omega_D\to\infty,
\qquad
\omega_D=o(D^{1/8}),
\]

the reflection branch admits a full slow-scale family of `(c_*-o(1))omega_D^2` modules. Applying the canonical-head dichotomy and the preceding extraction yields one of two alternatives.

### FREE-HEAD

There are

\[
\boxed{\Theta(\omega_D^2)}
\]

distinct canonical exposed heads `y_i` with

\[
\deg_C(y_i)=\deg_H(y_i)=0.
\]

The block-diagonal and geometric-tube theorems remain available around these modules; in particular any contact radius `r_D=o(kappa_D)` can still be exposed while the total buffered population stays `o(D)`.

### LOADED-HEAD

There are

\[
\boxed{\Theta(\omega_D^2)}
\]

pairwise vertex-disjoint actual diameter edges `y_i t_i` such that

\[
|t_i-q_i|=O(D/\omega_D^2),
\]

\[
\angle(M_i,n_i)=O(\omega_D^{-2}),
\]

\[
\angle(M_i,M_j)=\Omega(\omega_D^{-2}),
\]

and every two edges cross properly inside one

\[
\boxed{B(o,O(D^{3/4}\omega_D^2))=B(o,o(D))}
\]

central core.

For the concrete slow choice `omega_D=log log D`, the loaded branch contains `Theta((log log D)^2)` tagged actual diameters and the free branch contains the same-order number of completely active-constraint-free canonical heads.

---

## 8. Frontier effect

The loaded reflection escape is no longer an arbitrary collection of diameter incidences attached somewhere to blocker paths. It is an exact ordered diameter braid with a module-by-module endpoint correspondence:

```text
loaded canonical blocker head y_i
    reflection support normal N_i
    actual diameter normal M_i in the same convex normal cone
    most heads have |M_i-N_i| = O(omega^-2)
    exact partner t_i lies O(D/omega^2) from reflected apex q_i
    constant spacing makes all endpoints distinct
    convex diameter thrackle forces pairwise crossings
    all crossings lie in one o(D) central core
```

C-II remains open. The two surviving reflection seams are now genuinely different:

1. **FREE-HEAD:** continue a finite compensated move from a canonical hull point with no old unit or diameter constraints, through its first newly active event, until the reflection blocker is removed.
2. **LOADED-HEAD:** exploit the exact braid together with the shallow-tooth tags. The partner endpoints are forced into small neighborhoods of the reflected apexes, while the opposite endpoints are the canonical blocker heads. A closing theorem should compare this antipodal exact-diameter matching with the ordered loaded tooth bases or penetration contacts, rather than treating the diameter graph as an untagged thrackle.

**Disposition:** upgraded the loaded-head alternative from `Omega(omega_D)` arbitrary diameter edges to `Theta(omega_D^2)` vertex-disjoint, pairwise-crossing actual diameters with ordered `Omega(omega_D^-2)` direction gaps, `O(D/omega_D^2)` reflection-partner localization, and one `o(D)` common crossing core. C-II and Level I remain open.
