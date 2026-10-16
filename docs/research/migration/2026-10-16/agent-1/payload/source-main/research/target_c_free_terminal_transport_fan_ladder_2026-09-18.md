# Target C-II — terminal FREE transport fan ladder

**Date:** 2026-09-18  
**Status:** proof-only structural refinement; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE subsequences with `pi D-q=o(D)` and surplus within `epsilon D` of the current endpoint  
**Depends on:** terminal FREE surplus-endpoint stability; exact stopped-train endpoint multigraph; hostile-audited bounded-face endpoint fan theorem; exact singleton/full-flower incidence; isolate-host degree-seven theorem; audited one-train contact shear  
**Certificate:** `research/verify_target_c_free_terminal_transport_fan_ladder_2026_09_18.py`

C-II remains open.

The previous endpoint theorem forces either many singleton stopped trains or many fully
rhombic pentagons. It does not say where the five trains of a fully rhombic pentagon
terminate. The endpoint multigraph gives that missing localization.

At the exact surplus endpoint there is a three-way alternative. A survivor has a
linear family of singleton trains, or a linear family of outer-to-outer trains (each
of which has an exact one-train contact shear), or a linear family of empty fully
rhombic pentagons with several distinct pairwise-noncrossing rhombic trains running all
the way to the actual outer face.

The strongest useful member of the resulting fan ladder is the three-spoke version:

\[
\boxed{
\max\left\{
 {S\over D},\ {L_O\over D},\ {F^{\rm full}_{5,\ge3O}\over D}
\right\}
\ge 0.146520596600678\ldots-o(1).
}
\tag{TF.1}
\]

Here `S` is the singleton-train count, `L_O` is the number of stopped trains whose two
terminal occurrences are on the outer face, and `F^{full}_{5,>=3O}` counts fully
rhombic pentagons incident to at least three trains whose other terminal occurrence is
on the outer face. In the third branch those pentagons supply at least

\[
\boxed{0.439561789802035\ldots D-o(D)}
\tag{TF.2}
\]

distinct pentagon-to-outer non-singleton rhombic trains. The three trains at each
selected pentagon are pairwise noncrossing by the bounded-face fan theorem.

A four-spoke version is also available:

\[
\boxed{
\max\left\{
 {S\over D},\ {L_O\over D},\ {F^{\rm full}_{5,\ge4O}\over D}
\right\}
\ge 0.105849189639537\ldots-o(1),
}
\tag{TF.3}
\]

and the third branch then contains at least
`0.423396758558148...D-o(D)` distinct rhombic spokes to the outer face.

The point is not the scalar improvement. It replaces the diffuse flower alternative
by an outer-reaching train object with audited crossing-free local topology.

---

## 1. Endpoint constants and stability variables

Use the notation of the current surplus-endpoint theorem. Put

\[
s_2=\sqrt{\frac{\pi}{2\sqrt3}},\qquad g=0.007707,
\]

\[
M_*:=4s_2+2g
=3.824665227455829\ldots,
\qquad
p_*:={M_*\over5}
=0.764933045491166\ldots .
\tag{1.1}
\]

Along a terminal subsequence satisfying

\[
\limsup\mu_D\le\mu_*+\varepsilon,
\tag{1.2}
\]

the endpoint stability theorem permits a further subsequence on which

\[
\delta={b-P_F\over D}+o(1),\qquad
r={Q-f\over D}+o(1),\qquad
a={\tau_D\over D}-\tau_*+o(1)
\tag{1.3}
\]

exist, with `delta,r,a>=0`, and

\[
\boxed{
{2\over5}(r+\delta)+{1\over5}a\le\varepsilon.
}
\tag{1.4}
\]

(The omitted loaded-boundary remainder is nonnegative, so dropping it only weakens the
constraint.) The same theorem gives

\[
\boxed{
{f\over D}={M_*+2a-\delta-r\over5}+o(1),
}
\tag{1.5}
\]

while terminality gives

\[
{P_F\over D}=\pi+o(1),
\qquad
{b\over D}=\pi+\delta+o(1).
\tag{1.6}
\]

Let `S` denote the singleton stopped-train count. The exact full-flower incidence
inequality is

\[
\boxed{P_5-F_5^{\rm full}\le2S.}
\tag{1.7}
\]

---

## 2. Exact endpoint-transport identities

Use the exact stopped-train endpoint multigraph. Its vertices are the outer face `O`
and the bounded nonquadrilateral contact faces. Every stopped train is one edge.
The degree of `O` is `b`, while a bounded face of contact degree `d` has transport
degree exactly `d`. Bounded vertices support no loops.

Let

- `E_BB` be the number of transport edges joining two bounded faces;
- `E_BO` the number joining a bounded face to `O`; and
- `L_O` the number of loops at `O`, equivalently the number of outer-to-outer stopped
  trains.

Occurrence counting gives the two exact identities

\[
2E_{BB}+E_{BO}=4f+Q,
\qquad
E_{BO}+2L_O=b.
\tag{2.1}
\]

Subtracting them gives

\[
\boxed{
E_{BB}-L_O={4f+Q-b\over2}.
}
\tag{2.2}
\]

At the surplus endpoint, (1.5)--(1.6) turn this into

\[
{E_{BB}-L_O\over D}
=
{M_*-\pi\over2}+a-\delta+o(1).
\tag{2.3}
\]

Set

\[
e_*:={M_*-\pi\over2}
=0.341536286933018\ldots .
\tag{2.4}
\]

Since (1.4) implies `delta<=5epsilon/2`, we obtain the stable transport surplus

\[
\boxed{
E_{BB}\ge L_O+
\left(e_*-{5\over2}\varepsilon-o(1)\right)D.
}
\tag{2.5}
\]

Thus bounded-to-bounded transport cannot disappear at the endpoint. It exceeds the
outer-to-outer train population by `0.341536...D` at exact saturation.

### 2.1 Outer loops are individually shearable

If an outer-to-outer train is non-singleton, the audited outer-to-outer train theorem
supplies an exact one-parameter contact shear. If it is singleton, its one contact
edge has the outer face on both sides and is therefore a bridge of the connected plane
contact graph. Removing that edge gives two contact components; translating one
component by `R_theta u-u` rotates the bridge contact and leaves all other contacts
unchanged. Finite strict slack preserves every noncontact unit-separation inequality
for sufficiently small `theta`.

Therefore every edge counted by `L_O`, singleton or not, carries an individual exact
contact-preserving shear coordinate. No diameter monotonicity, and no simultaneous
compatibility of different coordinates, is asserted.

---

## 3. Counting pentagon-to-outer train incidences

Let `n_+` be the number of bounded nonquadrilateral faces of degree at least six. Since

\[
rD+o(D)=Q-f=\sum_F(\deg F-5),
\tag{3.1}
\]

we have

\[
n_+\le rD+o(D).
\tag{3.2}
\]

The total transport degree of those superpentagonal faces is exactly

\[
\sum_{\deg F\ge6}\deg F
=5n_+ +(Q-f)
\le 6rD+o(D).
\tag{3.3}
\]

Let `E_5O` be the number of transport edges joining a bounded pentagon to `O`. Since
all non-pentagonal bounded-to-outer edges use a superpentagonal endpoint,

\[
E_{5O}
\ge E_{BO}-5n_+-(Q-f)
=b-2L_O-5n_+-(Q-f).
\tag{3.4}
\]

For `1<=k<=5`, let

\[
Y_k:=\#\{P:\ P\text{ is a bounded pentagon and }o(P)\ge k\},
\tag{3.5}
\]

where `o(P)` is the number of incident transport edges joining `P` to `O`. A pentagon
outside `Y_k` contributes at most `k-1` such incidences and a pentagon in `Y_k`
contributes at most five. Hence

\[
E_{5O}\le (k-1)P_5+(6-k)Y_k.
\tag{3.6}
\]

Write `P_5=f-n_+`. Combining (3.4)--(3.6) gives the finite inequality

\[
\boxed{
(6-k)Y_k
\ge b-2L_O-(k-1)f-(Q-f)-(6-k)n_+.
}
\tag{3.7}
\]

Using `n_+<=Q-f` gives

\[
(6-k)Y_k
\ge b-2L_O-(k-1)f-(7-k)(Q-f).
\tag{3.8}
\]

This is the only loss in the fan count.

---

## 4. The endpoint fan ladder

Pass to a further subsequence with

\[
\ell:=\lim {L_O\over D},
\qquad
s:=\lim {S\over D}
\tag{4.1}
\]

whenever needed. Substitute (1.5)--(1.6) into (3.8). For `1<=k<=4`,

\[
\begin{aligned}
\liminf{Y_k\over D}
\ge {}& A_k-B_k\ell
+{k+4\over5(6-k)}\delta
-{6\over5}r
-{2(k-1)\over5(6-k)}a,
\end{aligned}
\tag{4.2}
\]

where

\[
A_k:={\pi-(k-1)p_*\over6-k},
\qquad
B_k:={2\over6-k}.
\tag{4.3}
\]

For `k<=4`, the negative coefficients in (4.2), together with (1.4), imply the clean
uniform estimate

\[
\boxed{
\liminf{Y_k\over D}
\ge A_k-B_k\ell-3\varepsilon.
}
\tag{4.4}
\]

Indeed, after adding three times the left side of (1.4), the remainder in (4.2) is
nonnegative for `k=1,2,3,4`; the worst coefficient is attained at `k=4`.

Now let `F^{full}_{5,>=kO}` count pentagons which are both fully rhombic and members of
`Y_k`. By (1.7), at most `2S` pentagons can fail full-rhombicity for the purpose of
this intersection, so

\[
F^{\rm full}_{5,\ge kO}\ge Y_k-2S.
\tag{4.5}
\]

Therefore

\[
\boxed{
\liminf {F^{\rm full}_{5,\ge kO}\over D}
\ge A_k-B_k\ell-2s-3\varepsilon,
\qquad 1\le k\le4.
}
\tag{4.6}
\]

Let

\[
C_k(\varepsilon)
:={A_k-3\varepsilon\over3+B_k}
={\pi-(k-1)p_*-3(6-k)\varepsilon\over20-3k}.
\tag{4.7}
\]

If all three normalized quantities `S/D`, `L_O/D`, and
`F^{full}_{5,>=kO}/D` were below `C_k(epsilon)`, (4.6) would give the reverse strict
inequality. Hence

\[
\boxed{
\max\left\{
\liminf{S\over D},
\liminf{L_O\over D},
\liminf{F^{\rm full}_{5,\ge kO}\over D}
\right\}
\ge C_k(\varepsilon),
\qquad 1\le k\le4,
}
\tag{4.8}
\]

with the usual interpretation after fixing a convergent subsequence. More robustly:
for each fixed `k`, at least one of the three quantities is
`(C_k(epsilon)-o(1))D` along every such subsequence.

At `epsilon=0` the constants are

| `k` outer spokes | `A_k` | `C_k(0)` | guaranteed spokes in fan branch `k C_k(0)` |
|---:|---:|---:|---:|
| 1 | 0.628318530717959 | 0.184799567858223 | 0.184799567858223 |
| 2 | 0.594164902024657 | 0.169761400578473 | 0.339522801156947 |
| 3 | 0.537242187535821 | 0.146520596600678 | 0.439561789802035 |
| 4 | 0.423396758558148 | 0.105849189639537 | 0.423396758558148 |

The three-spoke row maximizes the guaranteed number of localized outer-reaching spokes
among `k=1,2,3,4`. The four-spoke row gives the stronger local fan at a smaller face
coefficient.

---

## 5. Geometry of the fan branch

Every face counted by `F^{full}_{5,>=kO}` has the following properties.

1. It is source-empty. The isolate-host theorem says a bounded positive-contact face
   containing a source point has degree at least seven.
2. All five boundary edges have a strict rhombus on the opposite side, so all five
   incident stopped trains are non-singleton rhombic trains.
3. Bounded train loops are impossible, so the five incident train occurrences belong
   to five distinct complete trains.
4. At least `k` of those trains have their other terminal occurrence on the actual
   outer face.
5. Any two complete trains sharing this bounded pentagon are noncrossing by the
   hostile-audited bounded-face endpoint fan theorem.

A pentagon-to-outer train has only one bounded terminal face. Consequently, choosing
`k` outer-reaching spokes from every selected pentagon gives `k F^{full}_{5,>=kO}`
distinct complete non-singleton rhombic trains. Thus the `k=3` fan alternative in
(4.8) contains at least

\[
3C_3(0)D-o(D)
=0.439561789802035\ldots D-o(D)
\tag{5.1}
\]

distinct pentagon-to-outer rhombic trains, grouped into crossing-free triples at
`0.146520596600678...D-o(D)` distinct empty pentagons. The `k=4` alternative contains
at least `0.423396758558148...D-o(D)` such trains grouped into crossing-free quadruples.

This is stronger localization than the previous statement that a linear family of
fully rhombic pentagons exists. It puts a positive fraction of their rhombic train
network directly on the global outer face.

---

## 6. What this does and does not solve

The endpoint is now split into objects with a direct deformation or routing meaning:

- **singleton branch:** a linear family of contact edges which terminate no rhombus;
- **outer-loop branch:** a linear family of individually exact contact-shear trains;
- **outer-fan branch:** a linear family of empty fully rhombic pentagons supporting
  several distinct pairwise-noncrossing rhombic train corridors to the outer face.

No simultaneous diameter-decreasing motion is proved. In particular, the individual
outer-loop shears can increase active diameter distances, and the fan theorem by
itself does not upper-bound the outer-walk detour. The next useful step is to combine
the crossing-free outer fan with the force-hull outer-walk or diameter-edge incidence
structure, or to prove simultaneous feasibility for a positive-density subfamily of
the outer-loop shear coordinates.

**Disposition:** proved proof-only transport/fan refinement; theorem-state authority
unchanged; C-II remains open.
