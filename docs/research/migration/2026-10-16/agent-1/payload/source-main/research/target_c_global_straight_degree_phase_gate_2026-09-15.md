# Target C-II — global straight-event degree split and local phase gates

**Date:** 2026-09-15  
**Repository base:** `494b8b7cd3a2fe4120e673f09a46072e74b9a917`  
**Status:** proved proof-only strengthening; theorem-state authority unchanged  
**Scope:** fully force-visible, no-container/full-core Type-II low-`t` branch  
**Depends on:** the hostile-audited loaded internal-route exclusion and the global unloaded straight-event theorem  
**LEVEL I STATUS:** `STILL OPEN`

The global unloaded straight-event theorem forces more than `0.640D` distinct
strongly transverse contacts at the current low-`t` endpoint. Tightening its angular
window from `30` degrees to `15` degrees gives a different and more structural gain:
more than `1.154D` **distinct unloaded physical outer-route vertices**, each of contact
degree exactly three or four.

There is one topological branch that must be kept explicit. A physical vertex can have
only one `15`-degree-straight outer occurrence while still appearing elsewhere on the
outer facial walk in a non-straight occurrence. Such a vertex is an unloaded
articulation. We therefore split the straight population into

1. repeated-outer unloaded articulations; and
2. simple-outer straight vertices, whose remaining angular sectors are bounded-face
   incidences.

The second class has an exact local normal form. A cubic simple-outer vertex either
hits an exceptional bounded face or is a two-rhombus phase gate. A degree-four
simple-outer vertex either hits an exceptional face or is a three-rhombus acute fan.
The rhombus defects obey exact identities with the local boundary turn. This gives a
finite route from the global straight-event population into the canonical
exceptional-face, angular-defect, articulation, and phase-cut currencies.

---

## 1. Setup

Let

\[
W_i:b_i\leadsto b_{i+1}
\]

be the Section-63 distinguished outer-face contact routes. Put

\[
s_i=|b_i-b_{i+1}|,
\qquad
u_i={b_{i+1}-b_i\over s_i},
\]

and orient every unit edge occurrence of `W_i` from `b_i` to `b_{i+1}`.
For fixed

\[
0<\beta\le\pi/6,
\]

an internal occurrence is `beta`-straight when both adjacent oriented route-edge
occurrences make angle strictly less than `beta` with `u_i`.

The global unloaded theorem gives

\[
\boxed{
S_\beta
\ge
x_B-{2d_{out}\over1-\cos\beta},
}
\tag{DG.1}
\]

where

\[
x_B=b-q,
\qquad
d_{out}=b-\operatorname{per}(F).
\]

The hostile-audited loaded-route exclusion says every physical vertex occurring
internally on a distinguished route is unloaded. Canonical C26 therefore gives

\[
3\le\deg_C(x)\le5.
\tag{DG.2}
\]

---

## 2. A straight internal occurrence has degree at most four

Fix one `beta`-straight occurrence at a physical vertex `x`, and let `d=deg_C(x)`.
The two route-contact rays from `x` lie within `beta` of the two opposite directions
`-u_i` and `+u_i`. Hence their smaller angular separation is strictly greater than

\[
\pi-2\beta.
\tag{DG.3}
\]

The two route rays delimit the angular sector belonging to this occurrence of the
unbounded face. Call its angle `g`. Either sector between two rays is at least their
smaller separation, hence

\[
\boxed{g>\pi-2\beta.}
\tag{DG.4}
\]

No other contact ray can lie inside that face sector. Thus all `d-2` remaining
contact rays lie in the complementary sector of angle `2pi-g`. Traversing that
complement from one route ray to the other encounters `d-1` consecutive angular gaps
between contact rays.

Triangle-freeness makes every such gap strictly greater than `pi/3`: two unit
neighbors of `x` separated by angle at most `pi/3` would be at mutual distance at most
one, with equality producing a forbidden unit equilateral triangle. Therefore

\[
(d-1){\pi\over3}
<2\pi-g
<\pi+2\beta.
\tag{DG.5}
\]

For `beta<=pi/6`, the right side is at most `4pi/3`. The inequalities are strict, so

\[
\boxed{d\le4.}
\tag{DG.6}
\]

Together with (DG.2):

### Theorem DG.1 — degree collapse

For every `beta<=pi/6`, every `beta`-straight internal distinguished-route occurrence
is supported at an unloaded physical vertex of contact degree exactly three or four.

Thus the degree-five case retained in the previous Hall-selection argument is absent
on the straight subpopulation.

---

## 3. At a 15-degree window, straight occurrences are vertex-injective

A physical vertex may occur more than once on the outer facial walk. The existing
global theorem only needed the bound of two straight occurrences per physical vertex.
At a smaller angular threshold even the second **straight** occurrence is impossible.

Suppose one physical vertex supports at least two `beta`-straight outer occurrences.
Each occurrence corresponds to a distinct angular gap occupied by the unbounded face,
and each such gap has size strictly greater than `pi-2beta` by (DG.4).

There is at least one further angular gap because the vertex has degree at least three.
Every gap between consecutive contact rays is strictly greater than `pi/3`. Therefore
already for two straight occurrences,

\[
2\pi
>
2(\pi-2\beta)+{\pi\over3}.
\tag{DG.7}
\]

If

\[
\boxed{\beta\le{\pi\over12},}
\]

then the right side of (DG.7) is at least `2pi`, a contradiction.

### Theorem DG.2 — straight-occurrence vertex injectivity

For every `beta<=pi/12`, one physical contact vertex supports at most one
`beta`-straight internal distinguished-route occurrence.

Consequently, at this angular scale, `S_beta` is simultaneously

1. the number of straight internal outer-route occurrences; and
2. the number of **distinct physical unloaded vertices** supporting them.

This theorem does **not** say that the physical vertex has only one occurrence on the
outer facial walk. A second non-straight outer occurrence remains possible and is
handled explicitly in Section 6.

Write

\[
V_3(\beta)+V_4(\beta)=S_\beta
\tag{DG.8}
\]

for the degree-three and degree-four populations.

---

## 4. Use every transverse contact, not one representative

At a straight occurrence, the two route edges consume two contact incidences. By
Theorem DG.1 there are therefore

- exactly one extra contact incidence at a degree-three straight vertex;
- exactly two extra contact incidences at a degree-four straight vertex.

The angular argument from the global straight-event theorem applies to **every** extra
contact, not merely to one selected representative. Thus every such edge `xw`
satisfies

\[
\boxed{
|(w-x)\cdot Ju_i|
>
\sin(\pi/3-\beta).
}
\tag{DG.9}
\]

Let `E_all(beta)` be the number of distinct physical contact edges appearing among all
of these extra incidences over the distinct straight vertices. The total number of
selected incidences is exactly

\[
V_3+2V_4
=S_\beta+V_4
=2S_\beta-V_3.
\tag{DG.10}
\]

An undirected physical edge has only two endpoints, so it can occur in this incidence
set at most twice. Hence

\[
\boxed{
2E_{all}(\beta)
\ge S_\beta+V_4(\beta)
=2S_\beta-V_3(\beta).
}
\tag{DG.11}
\]

Equivalently,

\[
\boxed{
2E_{all}(\beta)+V_3(\beta)
\ge2S_\beta.
}
\tag{DG.12}
\]

A large degree-four population therefore raises the robust transverse-edge count. The
only way to stay near the old edge-count floor is to create many cubic straight
vertices.

---

## 5. Quantitative 15-degree straight-vertex floor

Set

\[
\boxed{\beta={\pi\over12}},
\qquad
c_{15}:=1-\cos(\pi/12)
=1-{\sqrt6+\sqrt2\over4}.
\tag{DG.13}
\]

Every extra edge in (DG.9) then has

\[
\boxed{
|(w-x)\cdot Ju_i|>{\sqrt2\over2}.
}
\tag{DG.14}
\]

On a convergent low-`t` Type-II subsequence write

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D}.
\]

Near-disk perimeter convergence gives

\[
{x_B\over D}
=\pi+\delta-t-\kappa+o(1).
\]

Divide (DG.1) by `D`:

\[
\liminf {S_{\pi/12}\over D}
\ge
\pi-t-\kappa
-\left({2\over c_{15}}-1\right)\delta.
\tag{DG.15}
\]

The low-`t` network squeeze gives

\[
2\delta+{\kappa\over2}\le R(t),
\qquad
R(t)={9t\over2}-2\pi-C_0.
\tag{DG.16}
\]

Because

\[
{1\over2}\left({2\over c_{15}}-1\right)>2,
\]

the right side of (DG.15) is minimized by spending the entire network budget on
outer detour:

\[
\delta={R(t)\over2},
\qquad
\kappa=0.
\tag{DG.17}
\]

Therefore

\[
\boxed{
\liminf {S_{\pi/12}\over D}
\ge
\pi-t
-{1\over2}
\left({2\over c_{15}}-1\right)R(t).
}
\tag{DG.18}
\]

At the current endpoint

\[
t_{42}=1.8208886379794447041\ldots,
\qquad
R(t_{42})=0.00576795,
\]

this is

\[
\boxed{
{S_{\pi/12}\over D}
\ge
1.1543116921171727469\ldots-o(1).
}
\tag{DG.19}
\]

Thus the source has at least

\[
\boxed{1.1543116921D-o(D)}
\]

distinct unloaded physical outer-route vertices of degree three or four, each carrying
one or two extra contacts with transverse component greater than `sqrt(2)/2`.

Equation (DG.12) gives the simultaneous tradeoff

\[
\boxed{
2{E_{all}\over D}+{V_3\over D}
\ge
2.3086233842343454938\ldots-o(1).
}
\tag{DG.20}
\]

A simple half split is

\[
\boxed{
\begin{array}{ll}
\text{either}&V_3/D\ge0.57715584605858637\ldots-o(1),\\[1mm]
\text{or}&E_{all}/D\ge0.86573376908787956\ldots-o(1).
\end{array}
}
\tag{DG.21}
\]

---

## 6. Repeated-outer versus simple-outer straight vertices

For a `pi/12`-straight physical vertex `x`, call the straight outer-face sector
**simple-outer** if it is the only incidence of the unbounded face at `x`. Otherwise
call `x` **repeated-outer**.

A repeated-outer vertex occurs at least twice on the same facial boundary walk. The
plane-graph facial-repetition lemma used in the hostile-audited loaded-route exclusion
therefore gives

\[
\boxed{
\text{every repeated-outer straight vertex is an unloaded articulation vertex.}
}
\tag{DG.22}
\]

Let

\[
V_{rep}+V_{simp}=S_{\pi/12}.
\tag{DG.23}
\]

Equation (DG.19) yields the clean topological split

\[
\boxed{
\begin{array}{ll}
\text{either}&V_{rep}/D\ge0.57715584605858637\ldots-o(1),\\[1mm]
\text{or}&V_{simp}/D\ge0.57715584605858637\ldots-o(1).
\end{array}
}
\tag{DG.24}
\]

The first branch is now a concrete linear population of **distinct unloaded contact
articulations**. The loaded non-articulation theorem does not exclude it; its scope is
loaded vertices only. This branch should be attacked with the grounded separator /
Woodall diameter-interaction machinery.

For the rest of the note fix a simple-outer straight vertex. Then every angular sector
other than its unique outer-face sector is a bounded-face incidence.

---

## 7. Positive equilibrium fixes the simple outer-sector side

Every straight vertex is unloaded, so it is incident to no positive diameter row.
Relative-interior positivity gives a strictly positive contact equilibrium

\[
\sum_{xy\in C}\alpha_{xy}(y-x)=0,
\qquad \alpha_{xy}>0.
\tag{DG.25}
\]

The contact rays therefore cannot lie in a closed half-plane. Equivalently every
angular gap between consecutive contact rays is strictly less than `pi`.

For the straight outer-face sector,

\[
\pi-2\beta<g<\pi.
\tag{DG.26}
\]

Define its positive local boundary turn

\[
\boxed{\tau:=\pi-g.}
\tag{DG.27}
\]

Then

\[
\boxed{0<\tau<2\beta.}
\tag{DG.28}
\]

At `beta=pi/12`,

\[
\boxed{0<\tau<\pi/6.}
\tag{DG.29}
\]

---

## 8. Cubic simple-outer all-rhombic gates

Let `x` be a degree-three simple-outer `pi/12`-straight vertex. It has one unique
extra contact edge. Its two non-outer angular sectors are bounded-face sectors; call
their angles `gamma_1,gamma_2`. By (DG.27),

\[
\boxed{
\gamma_1+\gamma_2
=2\pi-g
=\pi+\tau.
}
\tag{DG.30}
\]

If either bounded face is exceptional, the straight vertex has already hit the
exceptional-face network. Suppose instead that both bounded faces are strict unit
rhombi.

For a strict triangle-free unit rhombus, write its acute angle as

\[
\theta={\pi\over3}+\delta,
\qquad
0<\delta\le{\pi\over6}.
\tag{DG.31}
\]

The face angle at `x` is either

\[
{\pi\over3}+\delta
\quad\text{(acute/right branch)}
\]

or

\[
{2\pi\over3}-\delta
\quad\text{(obtuse branch)}.
\]

Because (DG.30) is strictly greater than `pi`, the two face angles cannot both be
acute/right. There are exactly two all-rhombic possibilities.

### DG.3a — mixed gate

One face is acute/right and the other is obtuse. If their rhombus defects are
`delta_a,delta_o`, then

\[
\boxed{
\tau=\delta_a-\delta_o>0.
}
\tag{DG.32}
\]

Thus the unique extra contact is a two-rhombus phase-transmission gate: the local
boundary turn is exactly the difference of the two adjacent train-crossing defects.

### DG.3b — double-obtuse gate

Both face angles are obtuse. Then

\[
\boxed{
\delta_1+\delta_2
={\pi\over3}-\tau.
}
\tag{DG.33}
\]

Since `tau<pi/6`, every such event spends a fixed amount of rhombus angular defect:

\[
\boxed{
\delta_1+\delta_2>{\pi\over6}.
}
\tag{DG.34}
\]

So a cubic simple-outer straight vertex lies in exactly one of:

1. exceptional bounded-face incidence;
2. mixed two-rhombus transmission gate satisfying (DG.32);
3. double-obtuse two-rhombus gate satisfying (DG.33)--(DG.34).

---

## 9. Degree-four simple-outer all-rhombic fans

Let `x` be a degree-four simple-outer `pi/12`-straight vertex. Its unique outer-face
sector has angle `g`, and its other three sectors are bounded-face sectors with angles
`gamma_1,gamma_2,gamma_3`. Equation (DG.27) gives

\[
\boxed{
\gamma_1+\gamma_2+\gamma_3
=\pi+\tau,
\qquad 0<\tau<\pi/6.
}
\tag{DG.35}
\]

If one of the three bounded faces is exceptional, the vertex hits the exceptional-face
network. Suppose all three are strict unit rhombi.

Each `gamma_j>pi/3`. None can be at least `pi/2`, because then

\[
\gamma_1+\gamma_2+\gamma_3
>{\pi\over2}+2{\pi\over3}
={7\pi\over6},
\]

whereas (DG.35) is strictly below `7pi/6`. Hence every one of the three rhombi is
acute at `x`. Write

\[
\gamma_j={\pi\over3}+\delta_j,
\qquad \delta_j>0.
\]

Then

\[
\boxed{
\delta_1+\delta_2+\delta_3=\tau<\pi/6.
}
\tag{DG.36}
\]

Thus every all-rhombic degree-four simple-outer straight vertex is a three-rhombus
acute fan with total rhombus defect exactly equal to its local outer-boundary turn.

---

## 10. Finite global phase-gate normal form

Let

- `A` be the number of repeated-outer `pi/12`-straight vertices;
- `X` be the number of simple-outer straight vertices incident to at least one bounded
  exceptional face;
- `O` be the number of cubic simple-outer double-obtuse gates; and
- `P` be the number of remaining simple-outer all-rhombic transmission gates, namely
  mixed cubic gates and degree-four acute fans.

Then

\[
\boxed{S_{\pi/12}=A+X+O+P.}
\tag{DG.37}
\]

Let `f` be the number of bounded exceptional faces and `Q` their total degree-above-four
excess. Their total number of boundary vertex incidences is exactly

\[
4f+Q.
\]

Choosing one exceptional face at every vertex counted by `X` gives

\[
\boxed{X\le4f+Q.}
\tag{DG.38}
\]

Let

\[
\Delta_{train}:=\sum_R\delta_R
\]

be the canonical total strict-rhombus angular defect. Every double-obtuse gate pays
more than `pi/6` through its two incident rhombi by (DG.34). A rhombus has four
vertices, so in the sum over all such gate incidences one rhombus defect is reused at
most four times. Hence

\[
O{\pi\over6}<4\Delta_{train},
\]

and therefore

\[
\boxed{O<{24\over\pi}\Delta_{train}.}
\tag{DG.39}
\]

Combining (DG.37)--(DG.39),

\[
\boxed{
P
\ge
S_{\pi/12}
-A-(4f+Q)-{24\over\pi}\Delta_{train}.
}
\tag{DG.40}
\]

There is also a turn-sum bound. At a mixed cubic gate,

\[
\tau=\delta_a-\delta_o\le\delta_a+\delta_o,
\]

while at a degree-four acute fan,

\[
\tau=\delta_1+\delta_2+\delta_3.
\]

Again each rhombus has only four vertices, so

\[
\boxed{
\sum_{x\in P}\tau_x\le4\Delta_{train}.
}
\tag{DG.41}
\]

Thus a large transmission-gate population is necessarily a many-small-turn regime;
the canonical angular-defect budget cannot be evaded by hiding large turn at many
gates.

Finally apply the canonical Section-68 phase-circle cut. It deletes a set `F_cut` of
strict-rhombus crossing relations with

\[
|F_{cut}|\le {3\Delta_{train}\over\pi}
\]

(up to the harmless floor), after which every retained train component has an exact
real phase potential. A deleted rhombus has only four vertices, so it can hit at most
four gates counted by `P`. If `P_ret` denotes transmission gates all of whose incident
rhombi survive the cut, then

\[
\boxed{
P_{ret}
\ge
S_{\pi/12}
-A-(4f+Q)-{36\over\pi}\Delta_{train}-O(1).
}
\tag{DG.42}
\]

Every gate counted by `P_ret` is therefore an actual local transmission gadget inside
the retained acyclic phase-potential network.

---

## 11. Frontier effect

The current low-`t` endpoint now has the source-level normal form

```text
S_pi/12 >= 1.1543116921 D-o(D)
    distinct unloaded degree-3/4 straight vertices

split each straight vertex into:
    repeated outer occurrence
        -> unloaded articulation;
    or simple outer occurrence
        -> exceptional-face incidence;
        -> cubic double-obtuse gate, paying > pi/6 defect;
        -> mixed cubic phase gate, tau = delta_a-delta_o;
        -> degree-4 acute fan, tau = delta_1+delta_2+delta_3.

After the global phase cut:
P_ret >= S_pi/12
         - A
         - (4f+Q)
         - (36/pi) Delta_train
         - O(1).
```

This does not close C-II, but it identifies two materially different live global
obstructions.

1. **Articulation branch.** A linear `A` gives a linear family of distinct unloaded
   contact articulation vertices. The grounded separator theorem says the diameter
   interaction across each such cut cannot have a bipartite connected component. A
   closure needs to combine those repeated separator obligations with Woodall's
   near-unicyclic/caterpillar diameter topology without allowing unlimited reuse of
   the same diameter braces.
2. **Phase-gate branch.** After paying exceptional-face and angular-defect currency,
   the remaining straight vertices are literal transmission gates in the retained
   train phase potential. A closure needs an occupancy theorem for how many such gates
   one stopped train, phase corridor, or diameter brace can serve, or a simultaneous
   shear that decreases the source diameter.

Vanishing-shear rhombic strips remain legitimate regressions: no positive lower bound
on an individual rhombus defect or KKT coefficient is used here.

**C-II remains open.**

---

## 12. Reproducibility

The numerical constants in Section 5 are certified by

```bash
python3 research/verify_target_c_global_straight_degree_phase_gate.py
```

The geometric statements in Sections 2--10 are exact and do not depend on numerical
rounding.
