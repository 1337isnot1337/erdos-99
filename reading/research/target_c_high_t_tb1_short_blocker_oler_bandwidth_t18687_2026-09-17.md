> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_short_blocker_oler_bandwidth_t18687_2026-09-17.md) · source SHA-256 `d2ad07bd352354b7edef066ff3b6b9e3bad0647b592b5b437a138be35afbc6d4`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C-II — Oler packing sharpens near-unit blocker bandwidth to six rows

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the short-blocker bandwidth theorem; no canonical promotion claimed  
**Scope:** selected O--O path coordinates in the high-`t` branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** proper pairwise-disjoint O--O midpoint crosscuts; strict unit-rhombus angle bounds; canonical finite Oler inequality  
**Certificate:** `research/verify_target_c_high_t_tb1_short_blocker_oler_bandwidth_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous short-blocker theorem bounded the path bandwidth of a `1+O(D^-1)` source pair by fourteen. That proof packed the **whole crossed rhombi** into a `sqrt(3)`-tube around the short segment. The same geometry has a substantially denser packing object: the centers of those crossed rhombi.

Every strict unit rhombus contains a disk of radius greater than `sqrt(3)/4` centered at its rhombus center. If the midpoint centerline of the rhombus meets a source segment, the rhombus center is within `1/2` of that segment. Distinct crossed selected rows give distinct rhombi with disjoint interiors, so their centers are mutually separated by at least `sqrt(3)/2`.

Applying the canonical finite Oler inequality to these centers in the radius-`1/2` capsule around the source segment gives the exact bound

```math
\boxed{
N\le
1+{14L+5\pi\over3\sqrt3},
}
\tag{OB.1}
```

where `L` is the source-segment length and `N` is the number of selected O--O rows separating its endpoints.

At `L=1`, the right side is

```math
1+{14+5\pi\over3\sqrt3}
=6.7173001966\ldots<7.
```

Therefore every source pair satisfying

```math
1<|xy|\le1+O(D^{-1})
```

has, for all sufficiently large `D`,

```math
\boxed{
|\operatorname{reg}(x)-\operatorname{reg}(y)|\le6.
}
\tag{OB.2}
```

This replaces the previous bound `14` by `6`.

The improvement is large enough to change the exact-swap thinning scale: seven-spaced retained coordinates now suffice to make every LOWER singleton blocker permanent. A separate propagation note records the resulting Horn-density improvements.

---

## 1. Crossed-row rhombus centers lie in a thin capsule

Use the ordered selected O--O crosscuts

```math
R_0\xleftrightarrow{\tau_1}R_1
\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m.
\tag{OB.3}
```

Let source vertices `x,y` lie in path regions `R_p,R_q`, with `p<q`, and put

```math
L=|x-y|,
\qquad
N=q-p.
\tag{OB.4}
```

The segment `xy` meets every separating selected row

```math
\tau_{p+1},\ldots,\tau_q.
```

For each crossed row choose one strict unit rhombus `F` whose midpoint centerline meets `xy`. At a centerline vertex either adjacent rhombus may be chosen; at a terminal midpoint choose the terminal rhombus. Pairwise disjointness of the selected O--O rows implies that the chosen rhombi are distinct.

Write a chosen unit rhombus as

```math
F=\operatorname{conv}\{0,u,v,u+v\},
\qquad |u|=|v|=1,
```

where the selected row enters and exits across the two sides parallel to `u`. Its midpoint centerline is

```math
\left\{{u\over2}+tv:0\le t\le1\right\},
```

which has length exactly one. Its midpoint is the rhombus center

```math
c_F={u+v\over2}.
```

If `z in xy` is a point where the row centerline meets the segment, then

```math
\boxed{|c_F-z|\le{1\over2}.}
\tag{OB.5}
```

Hence every chosen center belongs to the closed capsule

```math
K_L:=xy+B(0,1/2).
\tag{OB.6}
```

This capsule is convex and has

```math
\boxed{
\operatorname{area}(K_L)=L+{\pi\over4},
\qquad
\operatorname{per}(K_L)=2L+\pi.
}
\tag{OB.7}
```

---

## 2. The rhombus centers are `sqrt(3)/2`-separated

Let `theta` be an interior angle of a strict unit rhombus. Triangle-free unit separation gives

```math
{\pi\over3}<\theta<{2\pi\over3}.
\tag{OB.8}
```

A rhombus is tangential, with incenter at its diagonal intersection. Its inradius is half its altitude:

```math
r_F={\sin\theta\over2}.
\tag{OB.9}
```

Equation (OB.8) gives

```math
\boxed{r_F>{\sqrt3\over4}.}
\tag{OB.10}
```

Thus every chosen face contains the closed disk

```math
B\!\left(c_F,{\sqrt3\over4}\right)
```

strictly inside its face interior.

Distinct bounded contact faces have disjoint interiors. Therefore these equal disks are pairwise disjoint, and their centers satisfy

```math
\boxed{
|c_F-c_{F'}|\ge{\sqrt3\over2}
\quad(F\ne F').
}
\tag{OB.11}
```

No phase synchronization, KKT stress, or TB1 property is used here.

---

## 3. Oler packing in the capsule

The canonical finite Oler inequality says that if a point set `X` is unit-separated inside a convex body `K`, then

```math
|X|\le {2\over\sqrt3}\operatorname{area}(K)
+{1\over2}\operatorname{per}(K)+1.
\tag{OB.12}
```

For a point set with mutual distance at least

```math
\delta={\sqrt3\over2},
```

rescale by `1/delta`. Equation (OB.12) becomes

```math
|X|
\le
{2\over\sqrt3\,\delta^2}\operatorname{area}(K)
+{1\over2\delta}\operatorname{per}(K)+1.
\tag{OB.13}
```

Apply this to the `N` centers from Sections 1--2 in `K_L`. Since

```math
\delta^2={3\over4},
\qquad
{1\over2\delta}={1\over\sqrt3},
```

(OB.7) and (OB.13) give

```math
\begin{aligned}
N
&\le
{8\over3\sqrt3}\left(L+{\pi\over4}\right)
+{1\over\sqrt3}(2L+\pi)+1\\
&=
\boxed{
1+{14L+5\pi\over3\sqrt3}
}.
\end{aligned}
\tag{OB.14}
```

This is (OB.1).

For `L=1`,

```math
1+{14+5\pi\over3\sqrt3}
=6.7173001966086\ldots .
\tag{OB.15}
```

Hence there is a fixed positive margin below seven.

For an explicit elementary asymptotic threshold, use

```math
\sqrt3>{265\over153},
\qquad
\pi<{22\over7}.
\tag{OB.16}
```

These give

```math
{14\over3\sqrt3}<{714\over265},
\qquad
1+{5\pi\over3\sqrt3}<{1493\over371}.
\tag{OB.17}
```

If

```math
L\le1+{K\over D}
```

and `D>10K`, then

```math
N
<
{714\over265}{11\over10}+{1493\over371}
={64814\over9275}
=6.9880323450\ldots<7.
\tag{OB.18}
```

Since `N` is an integer,

```math
\boxed{N\le6.}
\tag{OB.19}
```

For a general `1+O(D^-1)` family, absorb the implicit constant into one fixed `K` and apply the same conclusion for sufficiently large `D`.

---

## 4. Consequence for exact TB1 swaps

A LOWER singleton blocker in the one-sign exact-swap system satisfies

```math
1<|xy|\le1+q_i,
\qquad
q_i=O(D^{-1}).
\tag{OB.20}
```

Equation (OB.19) therefore gives

```math
\boxed{
|\operatorname{reg}(x)-\operatorname{reg}(y)|\le6
}
\tag{OB.21}
```

for every LOWER blocker once `D` is sufficiently large.

Consequently, if retained swap coordinates are chosen from one residue class modulo seven, distinct retained layers are at index distance at least seven and no LOWER blocker can contain endpoints in two retained layers. Every LOWER singleton blocker is then a permanent one-coordinate obstruction relative to that retained system.

The previous proof used residue classes modulo fifteen solely because its geometric bandwidth was fourteen. The Oler-center estimate therefore reduces that loss from a factor `15` to a factor `7` without changing the Boolean exact-swap argument.

---

## 5. Frontier effect

The finite-swap seam now has a substantially tighter local metric input:

```text
old:
    inverse-D near-unit pair
    -> path bandwidth <= 14
    -> retain one class mod 15;

new:
    inverse-D near-unit pair
    -> crossed-rhombus centers are sqrt(3)/2-separated
       inside the radius-1/2 capsule of the pair
    -> Oler: path bandwidth <= 6
    -> retain one class mod 7.
```

This theorem does not close the permanent LOWER branch. It does, however, more than double the density of the exact-swap subsystem on which lower coupling disappears. The next note propagates that gain through the Horn poison/localization chain.

**Disposition:** proved the universal capsule/Oler bound (OB.14), sharpened inverse-`D` near-unit path bandwidth from fourteen to six, and reduced the exact-swap residue spacing needed to eliminate LOWER binary coupling from fifteen to seven. C-II and Level I remain open.
