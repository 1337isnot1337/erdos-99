# Target C-II — convex Section-63 pockets reduce the angular-deletion loss

**Date:** 2026-09-15  
**Repository base:** `1a47985b905f9c06df1a43f227d1e9ea0076cae7`  
**Status:** proof-only composition of audited pocket geometry with the signed penetration theorem; theorem-state authority unchanged  
**Scope:** fully force-visible no-container/full-core Type-II low-`t` branch  
**LEVEL I STATUS:** `STILL OPEN`

The current global straight-event theorem treats each distinguished Section-63 outer route as an arbitrary occurrence-counted walk. It therefore pays an angularly bad edge twice, because one bad edge can spoil the straightness test at the internal occurrences on both ends.

Canonical Section 67 and the hostile-audited Section-126 pocket identification give more structure for free. After adding every missing loaded-hull side, the augmented graph `Ghat` is 2-connected and every bounded face is convex. For each nonunit hull side `b_i b_{i+1}`, the inward pocket incident to that side has boundary exactly

\[
b_i b_{i+1}\cup W_i,
\]

where `W_i` is the canonical Section-63 interval, with all old bridge/articulation multiplicities included. Since the pocket face boundary in `Ghat` is a simple convex cycle, `W_i` is in fact a simple convex chain. A unit hull side is already the direct outer edge between the corresponding consecutive loaded marks and has no internal occurrence.

Along a convex chain, lifted edge directions are monotone. The principal-angle `beta`-good edges therefore form at most two contiguous blocks. This reduces the arbitrary-walk angular loss substantially. A companion split-route lemma sharpens the resulting endpoint to

\[
\boxed{1.3005161906103485\ldots D-o(D)}
\]

distinct signed inward penetration contacts at the current low-`t` floor.

This file records the convex-route reduction itself. The exact coefficient-seven endpoint is in
`research/target_c_convex_route_split_energy_sharpening_2026-09-15.md`.

---

## 1. Canonical hull augmentation already makes the pockets convex

Let `G` be the connected positive-contact core, let

\[
B=(b_1,\ldots,b_q)
\]

be the loaded force-hull vertices in cyclic order, and let

\[
W_i:b_i\leadsto b_{i+1}
\]

be the distinguished Section-63 outer-face interval. Put

\[
s_i=|b_i-b_{i+1}|,
\qquad
\ell_i=|W_i|
\]

with occurrence length on the outer-face walk.

Canonical Section 67 proves

\[
V(G)\cap\partial F=B,
\qquad F=\operatorname{conv}B,
\]

and forms `Ghat` by adding every missing straight hull side between consecutive loaded vertices, retaining a side only once when it is already a unit contact. It then proves:

1. `Ghat` is 2-connected;
2. every face boundary of `Ghat` is a simple cycle;
3. every bounded face of `Ghat` is a convex polygon;
4. the new bounded faces are exactly the convex pockets cut from the old outer contact face by the loaded hull cycle.

The hostile audit of Section 126 checks the occurrence-level identification needed here: for a missing hull side `b_i b_{i+1}`, the boundary of its inward pocket minus that added side is **exactly** the old Section-63 interval `W_i`, even when the old outer-face walk has bridges or repeated articulation occurrences.

Therefore:

### Theorem CR.1 — distinguished route convexity

For every nonunit loaded-hull side `s_i>1`,

\[
\boxed{b_i b_{i+1}\cup W_i}
\]

is the simple boundary cycle of one convex `Ghat` pocket. In particular `W_i` is a simple convex chain.

If `s_i=1`, the hull side `b_i b_{i+1}` is already an outer loaded-loaded contact. Since the full hull cycle is the outer boundary of the 2-connected augmented graph and Section 63 lists loaded occurrences in this same cyclic order, the corresponding interval is the direct edge:

\[
\boxed{s_i=1\Longrightarrow \ell_i=1.}
\tag{CR.1}

Thus every interval with an internal occurrence is a complementary chain of a convex pocket.

This is not a new convexity theorem. It is an explicit composition of canonical Section 67 with the already-audited Section-63/Section-126 occurrence identification.

---

## 2. Convexity leaves at most two principal-angle good blocks

Fix a nontrivial route `W_i` and orient it from `b_i` to `b_{i+1}`. Let its unit edge vectors be

\[
v_{i,1},\ldots,v_{i,\ell_i},
\qquad |v_{i,j}|=1,
\]

and let

\[
u_i={b_{i+1}-b_i\over s_i}
\]

be the chord direction.

Because `W_i` is part of the boundary of a convex polygon, its oriented edge directions admit a monotone continuous lift

\[
\vartheta_{i,1}\le\vartheta_{i,2}\le\cdots\le\vartheta_{i,\ell_i}
\]

relative to `u_i` (or the same statement with all inequalities reversed). The complementary chain turns through strictly less than `2pi`: the closing loaded-hull side is a genuine side of the convex polygon and both endpoint turns are positive.

Fix

\[
0<\beta\le\pi/6.
\]

Call an edge `beta`-good when its principal angular distance from `u_i` is less than `beta`. In the monotone lift this means

\[
\vartheta_{i,j}
\in
\bigcup_{m\in\mathbb Z}(2\pi m-\beta,2\pi m+\beta).
\]

Since the lift spans less than `2pi`, the good edge indices form at most two contiguous blocks.

Let

\[
A_i(\beta)=\#\{j:\text{edge }j\text{ is not }\beta\text{-good}\}.
\]

If there are zero or one good blocks, the number of internal occurrences that are not between two consecutive good edges is at most `A_i(beta)`.

If there are two nonempty good blocks, the loss is at most `A_i(beta)+1`: the extra one is the break between the two good blocks.

Define `r_i=1` in this two-block case and `r_i=0` otherwise. For a unit interval set `A_i=S_{i,beta}=r_i=0`. Then

\[
\boxed{
S_{i,\beta}
\ge(\ell_i-1)-A_i(\beta)-r_i.
}
\tag{CR.2}

Summing over all intervals and using canonical Section 63,

\[
x_B=\sum_i(\ell_i-1),
\]

gives

\[
\boxed{
S_\beta\ge x_B-A_\beta-r,
\qquad
A_\beta=\sum_iA_i(\beta),
\qquad
r=\sum_i r_i.
}
\tag{CR.3}

---

## 3. Directional energy pays the ordinary bad edges

The exact outer-route directional-energy identity is

\[
d_{out}
=\sum_{i,j}(1-\cos\vartheta_{i,j}).
\tag{CR.4}

Every `beta`-bad edge contributes at least `1-cos(beta)`, hence

\[
\boxed{
A_\beta
\le {d_{out}\over1-\cos\beta}.
}
\tag{CR.5}

For a split route (`r_i=1`) the monotone direction sequence must wind from a good block near angle zero to another near angle `2pi`. The coarse consequence is that such a route spends at least one unit of directional energy, so

\[
r\le d_{out}.
\tag{CR.6}

Equations (CR.3)--(CR.6) already improve the arbitrary-walk estimate to

\[
S_\beta
\ge
x_B-\left(1+{1\over1-\cos\beta}\right)d_{out}.
\tag{CR.7}

The companion split-energy theorem improves (CR.6) to

\[
r\le{d_{out}\over1+\cos\beta},
\]

which is the form used for the strongest endpoint.

---

## 4. Composition with signed edge-injective penetration

The merged signed penetration theorem applies to the same Section-63 straight occurrences. In the current low-detour Type-II scope it proves:

1. every internal route occurrence is at an unloaded branching contact vertex;
2. the local occurrence selections can be chosen distinctly at one physical vertex;
3. every selected contact points to the core side and has signed inward component
   \[
   >\sin(\pi/3-\beta);
   \]
4. no physical contact edge can be selected from both endpoints, because that would force two loaded-hull normals separated by more than `pi/3` and hence total outer detour `D-o(D)`.

Therefore the occurrence-to-contact map is globally injective:

\[
\boxed{E_\perp(\beta)\ge S_\beta.}
\tag{CR.8}

At `beta=pi/6`, every selected edge has signed inward component strictly greater than `1/2`.

---

## 5. Frontier effect

Canonical hull augmentation therefore removes a real bookkeeping loss from the global straight-event theorem:

```text
Section 67 + audited Section 126
 -> every nontrivial Section-63 interval is a simple convex pocket chain
 -> edge directions are monotone
 -> beta-good edges form at most two blocks
 -> ordinary bad edges are paid once rather than twice
 -> only split routes require one additional route-level charge
 -> signed penetration selections are globally edge-injective.
```

With the exact split-route energy charge developed in the companion theorem, the present endpoint forces more than `1.3005161906D-o(D)` distinct signed inward contacts.

This does not close C-II. A long one-rhombus-thick boundary strip remains a binding local regression: one stopped train can absorb linearly many selected inward edges. The live problem after this sharpening is macroscopic strip/train occupancy and its compatibility with the near-extremal diameter thrackle.

No theorem-state promotion is requested.