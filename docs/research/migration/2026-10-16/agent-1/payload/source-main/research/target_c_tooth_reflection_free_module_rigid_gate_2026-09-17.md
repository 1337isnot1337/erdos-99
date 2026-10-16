# Target C-II - free reflection modules force a finite near-contact gate

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the current shallow-tooth reflection branch  
**Scope:** FREE-MODULE side of the slow-scale reflection module-anchor dichotomy at `eta=3/26`  
**Dependencies:** simultaneous reflection block diagonalization; canonical farthest reflected blocker; full-source circumradius bound; module-anchor dichotomy  
**Certificate:** `research/verify_target_c_tooth_reflection_free_module_rigid_gate_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The module-anchor dichotomy leaves a FREE-MODULE branch in which every upper blocker of a reflected apex is an old contact isolate and an old diameter isolate. This note gives a finite obstruction for that branch.

For one free module let

\[
U=\{z\in A:|z-q|>D\},
\]

let `y` be the canonical farthest blocker, put

\[
L:=|y-q|=D+\delta,
\qquad 0<\delta<h_*:=\frac{\sqrt{303}}{52},
\]

and let

\[
N:=\frac{y-q}{L}
\]

be the exact outward support normal of the original source hull at `y`.

Then the whole blocker set can be translated rigidly by almost exactly its radial excess,

\[
T_s(z):=z-sN,
\qquad 0\le s\le t_D:=\delta+D^{-1/3},
\]

without ever creating a distance larger than `D`. At the terminal time every translated blocker lies at distance `<D` from `q`.

Internal blocker distances are unchanged. Hence, if no translated blocker meets a fixed source point at unit distance through time `t_D`, the terminal rigid translation followed by the exact tooth reflection `x -> q` is a same-cardinality feasible source with strictly fewer unit contacts. This contradicts the canonical contact-minimal normalization.

Therefore every FREE module has a finite gate. There are original source points

\[
z\in U,
\qquad v\notin U,
\]

and a time

\[
0<s_*\le t_D
\]

such that

\[
|z-s_*N-v|=1.
\]

In the original source this gate pair obeys

\[
\boxed{
1<|z-v|\le 1+\delta+D^{-1/3},
}
\tag{FG.1}
\]

\[
\boxed{
D-1-\delta-D^{-1/3}<|v-q|\le D,
}
\tag{FG.2}
\]

and

\[
\boxed{
N\cdot(z-v)>0.
}
\tag{FG.3}
\]

Thus an active-free upper obstruction cannot remain free under the finite repair needed to clear it. It must be guarded from the inward side by an original source point at distance at most `1+delta+o(1)`.

Across the slow-scale FREE-MODULE family these gate pairs are pairwise vertex-disjoint for all sufficiently large `D`, because the modules are separated by `Omega(kappa_D D^(3/4))` while every gate has length below `1+h_*+o(1)`.

In particular, if a free subfamily has `delta_i=o(1)` uniformly, it forces the same-size family of pairwise-disjoint original source pairs of length

\[
\boxed{1+o(1)}.
\tag{FG.4}
\]

The surviving FREE branch is therefore no longer just a set of unconstrained diameter violators. It has an exact finite repair obstruction: either the reflection excess itself stays macroscopically positive, or clearing the active-free blockers forces a new near-unit gate no later than the moment the reflection becomes diameter-feasible.

---

## 1. Blocker rays are close to the canonical support normal

The geometric contact-tube theorem gives a fixed constant

\[
C_A=2\,3^{5/8}+4\,3^{1/8}+1
=9.56283745460\ldots
\]

such that every blocker ray satisfies

\[
\angle(z-q,n)\le C_A D^{-1/4}
\qquad(z\in U),
\]

where `n` is the selected tooth normal. The canonical farthest ray `N=(y-q)/L` is itself one of these blocker rays. Hence

\[
\boxed{
\angle\left(\frac{z-q}{|z-q|},N\right)
\le 2C_A D^{-1/4}.
}
\tag{FG.5}
\]

Write

\[
C_N:=2C_A.
\]

For `r=|z-q|` and the angle `phi` in (FG.5), maximality of `y` gives

\[
D<r\le L=D+\delta.
\]

---

## 2. A translation of length `delta+D^-1/3` clears every upper blocker

Put

\[
t_D=\delta+D^{-1/3}.
\]

For sufficiently large `D`, `t_D<h_*+o(1)<1/2`.

For one blocker,

\[
|z-t_DN-q|^2
=r^2+t_D^2-2rt_D\cos\phi.
\]

The right side is increasing in `r` throughout the present range, so use `r<=D+delta` and `1-cos(phi)<=phi^2/2`:

\[
\begin{aligned}
|z-t_DN-q|^2
&\le (D+\delta-t_D)^2
 +2(D+\delta)t_D(1-\cos\phi)\\
&\le (D-D^{-1/3})^2
 +(D+h_*)t_D C_N^2D^{-1/2}.
\end{aligned}
\tag{FG.6}
\]

The second term is `O(sqrt(D))`, whereas

\[
D^2-(D-D^{-1/3})^2
=2D^{2/3}-D^{-2/3}.
\]

Therefore

\[
\boxed{|z-t_DN-q|<D}
\tag{FG.7}
\]

for every `z in U` and all sufficiently large `D`.

The exponent `-1/3` is not special. Any positive clearance `epsilon_D` with `epsilon_D -> 0` and `epsilon_D sqrt(D) -> infinity` works.

---

## 3. The rigid translation cannot create a new upper-diameter violation

This is the point that makes the finite motion usable.

Let

\[
K=\operatorname{conv}A,
\qquad H=h_K(N),
\qquad m=\min_{p\in K}N\cdot p,
\qquad W=H-m.
\]

The canonical farthest-blocker theorem gives

\[
N\cdot y=H,
\qquad D-W<h_*.
\tag{FG.8}
\]

For `z in U`, define its original support depth

\[
a_z:=H-N\cdot z.
\]

Since `q=y-LN`, writing `e=(z-q)/r` gives

\[
a_z=L-rN\cdot e
=(L-r)+r(1-\cos\phi).
\]

Using (FG.5),

\[
\boxed{
a_z
\le h_*+\frac{C_N^2}{2}(D+h_*)D^{-1/2}
=:B_D
=O(\sqrt D).
}
\tag{FG.9}
\]

Now fix `v notin U` and suppose that for some `0<s<=t_D`

\[
|z-sN-v|>D.
\]

The original source has `|z-v|<=D`, so

\[
|z-sN-v|^2-|z-v|^2
=-2sN\cdot(z-v)+s^2>0.
\]

Hence

\[
N\cdot(z-v)<s/2.
\]

If `a_v:=H-N\cdot v`, then

\[
a_v-a_z=N\cdot(z-v)<s/2,
\]

and therefore

\[
\boxed{a_v<B_D+1/2.}
\tag{FG.10}
\]

Thus both endpoints of any hypothetical newly superdiametral pair lie in an `O(sqrt(D))` cap at the same support line.

Use the canonical full-source circumradius bound

\[
K\subset B(o,R_D),
\qquad
R_D<\frac D2+\eta_D,
\qquad
\eta_D=3^{1/4}\sqrt D.
\tag{FG.11}
\]

Let `c=N\cdot o`. Since `m>=c-R_D`, (FG.8) implies

\[
H-c\ge W-R_D
>\frac D2-\eta_D-h_*.
\tag{FG.12}
\]

For every point of support depth at most `B_D+1/2`, its `N`-coordinate relative to `o` is at least

\[
\frac D2-\eta_D-h_*-B_D-\frac12
=\frac D2-O(\sqrt D).
\]

Inside the radius-`D/2+O(sqrt(D))` disk (FG.11), the transverse coordinate of such a point is therefore only

\[
O(D^{3/4}).
\]

Consequently any two points in this cap are at distance

\[
O(D^{3/4})=o(D).
\tag{FG.13}
\]

In particular

\[
|z-sN-v|\le |z-v|+s=o(D),
\]

contradicting the supposed value `>D`. Hence

\[
\boxed{
|z-sN-v|\le D
\quad
(z\in U,\ v\notin U,\ 0\le s\le t_D)
}
\tag{FG.14}
\]

for all sufficiently large `D`.

Pairs internal to `U` are preserved exactly by the rigid translation, and pairs outside `U` are fixed. Thus the entire homotopy creates no upper-distance violation.

---

## 4. Contact minimality forces a gate by the terminal time

Assume now that the module is FREE. By the module-anchor theorem,

\[
\deg_C(z)=\deg_H(z)=0
\qquad(z\in U).
\tag{FG.15}
\]

Translate the complete set `U` by `-sN` from `s=0` to `s=t_D`.

- Distances internal to `U` are unchanged.
- All distances between fixed vertices are unchanged.
- By (FG.14), no distance exceeds `D`.
- Since no vertex of `U` is an actual diameter endpoint, at least one old actual diameter pair remains completely fixed, so the diameter stays exactly `D` throughout any feasible initial part of the motion.

Suppose no cross-pair reaches unit distance at any time `s in [0,t_D]`. Then every cross-pair remains strictly larger than one, because it starts strictly larger than one by (FG.15). The terminal translated source is therefore still unit-separated, has diameter `D`, and has exactly the same old contact graph.

Now replace the shallow apex `x` by its reflected point `q`.

The simultaneous reflection theorem was built after deleting the exterior-witness teeth, so `q` is already unit-separated from every fixed original source point, with only the intended base contacts `qa=qb=1`. Equation (FG.7) removes every upper blocker. For translated blockers,

\[
|q-(z-t_DN)|
\ge |q-z|-t_D
>D-1
>1
\]

for large `D`, so they create no lower contact.

Thus the reflected source is feasible and has diameter at most `D`. The two base contacts survive, while every other old contact at the unloaded shallow apex is broken. Canonical C26 gives `deg_C(x)>=3`, so at least one contact is lost and no new contact is created.

If the new diameter were smaller than `D`, global optimality would fail. If it remains `D`, contact minimality would fail. Both are impossible.

Therefore some cross-pair reaches unit distance at a first time

\[
\boxed{0<s_*\le t_D.}
\tag{FG.16}
\]

The endpoint case `s_*=t_D` is allowed and is enough for every conclusion below; no contact-count comparison is made after a terminal-time gate has already appeared.

---

## 5. Geometry of the first gate in the original source

At the first time there are `z in U` and `v notin U` with

\[
|z-s_*N-v|=1.
\tag{FG.17}
\]

The original pair is not a contact because `z` is contact-isolated. Hence

\[
|z-v|>1.
\]

The triangle inequality and (FG.16) give

\[
|z-v|
\le 1+s_*
\le1+\delta+D^{-1/3},
\]

which proves (FG.1).

Since `v notin U`,

\[
|v-q|\le D.
\]

Also

\[
|v-q|
\ge |z-q|-|z-v|
>D-1-\delta-D^{-1/3},
\]

which proves (FG.2).

Finally, square (FG.17):

\[
1
=|z-v|^2-2s_*N\cdot(z-v)+s_*^2.
\]

Therefore

\[
\boxed{
N\cdot(z-v)
=\frac{|z-v|^2+s_*^2-1}{2s_*}
>0,
}
\tag{FG.18}
\]

proving (FG.3). The guard lies strictly inward of its blocker in the canonical support-normal direction.

---

## 6. The gates are module-disjoint

For two distinct slow-scale modules,

\[
\operatorname{dist}(U_i,U_j)
=\Omega(\kappa_DD^{3/4}),
\qquad \kappa_D\to\infty.
\tag{FG.19}
\]

Every gate endpoint `v_i` is at original distance below

\[
1+h_*+o(1)<1.335
\]

from its blocker `z_i in U_i`. Thus two distinct modules cannot share either blocker or guard endpoint for sufficiently large `D`.

Hence a FREE-MODULE subfamily of size `M` produces `M` pairwise vertex-disjoint original gate pairs satisfying (FG.1)--(FG.3).

If additionally

\[
\max_i\delta_i=o(1)
\]

on such a subfamily, then (FG.1) becomes

\[
1<|z_i-v_i|\le1+o(1),
\]

which is (FG.4).

---

## 7. Frontier effect

The module-anchor split can now be sharpened schematically to

```text
selected reflection module
    |
    +-- ANCHORED
    |      -> tagged exact actual diameter
    |      -> full slow-scale anchored family is an exact central diameter braid
    |
    +-- FREE
           -> all old upper blockers have deg_C=deg_H=0
           -> rigidly translate all blockers toward q
           -> no new upper-diameter violation is possible
           -> a new unit gate must appear by the time q becomes diameter-feasible
```

The remaining FREE-MODULE problem is therefore a finite lower-distance obstruction, not an inherited active-graph obstruction. The immediate next split is quantitative in the reflection excess `delta_i=L_i-D`:

1. if a large free subfamily has `delta_i=o(1)`, it produces a same-size matching of original `1+o(1)` gate pairs in the module-normal caps;
2. otherwise a large free subfamily has a non-negligible reflected diameter excess, which must be attacked through the canonical support-width/tooth geometry.

This note does not close either subcase. It does remove the possibility that an active-free blocker module can simply be translated out of the way without encountering a new lower-distance obstruction.

**Disposition:** proved a finite rigid-translation repair lemma for the FREE-MODULE branch. Clearing all active-free upper blockers creates no new upper-diameter violation, so contact minimality forces a new inward near-contact gate no later than the terminal clearing time. C-II and Level I remain open.
