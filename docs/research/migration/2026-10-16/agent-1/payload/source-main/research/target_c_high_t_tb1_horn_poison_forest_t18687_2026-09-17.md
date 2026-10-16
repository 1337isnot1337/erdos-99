# Target C-II — Horn poisoning forces a linear permanent family or a linear implication forest

**Date:** 2026-09-17  
**Status:** proof-only continuation of the 15-spaced Horn reduction; no canonical promotion claimed  
**Scope:** the 15-spaced one-sign strong-TB1 exact-swap subsystem through `t=(q-k)/D<=1.8687`  
**Dependencies:** short-blocker bandwidth theorem; 15-spaced Horn reduction; upper near-diameter implication interpretation  
**Certificate:** `research/verify_target_c_high_t_tb1_horn_poison_forest_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The Horn reduction leaves a linear retained coordinate set

\[
P_D,
\qquad
|P_D|>(\gamma-o(1))D,
\qquad
\gamma={s_0\over30}={791\over9{,}600{,}000{,}000},
\tag{HP.1}
\]

with an implication digraph `I_D` and forbidden set `F_D`. A swap set is feasible for every previously strict pair exactly when it is out-closed in `I_D` and avoids `F_D`. Canonical minimality therefore forces every sink strongly connected component of `I_D` to meet `F_D`.

That statement already has a stronger global consequence which was not recorded in the Horn note:

> **Horn poison-forest theorem.** Every retained coordinate reaches `F_D` by a directed implication path. Consequently either
> \[
> |F_D|\ge {|P_D|\over2},
> \]
> or `I_D` contains an acyclic directed forest of at least `|P_D|/2` distinct implication arcs, every component directed toward `F_D`.

Since all implication arcs are upper near-diameter source pairs, the second alternative gives a linear family of geometrically tagged near-diameter interactions with no SCC ambiguity left.

The first alternative also has a useful source-pair extraction. Every forbidden coordinate has a permanent blocker. A lower blocker is supported on that coordinate alone by the fourteen-row bandwidth plus fifteen-spacing theorem, so one lower pair cannot poison two retained coordinates. An upper blocker can involve at most two retained coordinates. Hence, if `|F_D|>=|P_D|/2`, then either

\[
\boxed{
N_{\rm permanent\ lower}
>\left({\gamma\over4}-o(1)\right)D
}
\tag{HP.2}
\]

or

\[
\boxed{
N_{\rm permanent\ upper}
>\left({\gamma\over8}-o(1)\right)D.
}
\tag{HP.3}
\]

If instead `|F_D|<|P_D|/2`, the implication forest has

\[
\boxed{
N_{\rm implication\ forest}
>\left({\gamma\over2}-o(1)\right)D.
}
\tag{HP.4}
\]

Numerically,

\[
{\gamma\over2}=4.11979166667\times10^{-8},
\]

\[
{\gamma\over4}=2.05989583333\times10^{-8},
\]

\[
{\gamma\over8}=1.02994791667\times10^{-8}.
\]

Thus sink-SCC poisoning cannot remain a purely qualitative graph obstruction. It forces a linear population in one of three concrete geometries:

1. permanent inverse-`D` near-unit blockers, each supported in a path bandwidth of at most fourteen;
2. permanent inverse-`D` near-diameter upper blockers;
3. a directed acyclic forest of inverse-`D` near-diameter implication pairs joining retained layers.

The third case is especially useful because each forest tail is unique and every arc joins two actual path regions, so exact selected-cut interval support can now be imposed on the Horn interaction graph without any SCC quotient or endpoint multiplicity loss.

---

## 1. Every retained coordinate reaches the forbidden set

Let

\[
G=I_D,
\qquad
V=P_D,
\qquad
F=F_D.
\]

The Horn theorem gives

\[
\boxed{
\text{every sink SCC of }G\text{ intersects }F.
}
\tag{HP.5}
\]

Fix `v in V`. In the condensation DAG of `G`, start at the SCC containing `v` and follow outgoing arcs until reaching a sink SCC `C`. This is possible because the condensation is finite and acyclic.

By (HP.5),

\[
C\cap F\ne\varnothing.
\]

Once a directed path reaches `C`, strong connectivity inside `C` reaches every vertex of `C`, in particular one element of `F`. Therefore

\[
\boxed{
\text{every }v\in P_D\text{ has a directed path in }I_D\text{ to }F_D.
}
\tag{HP.6}
\]

This is stronger than merely saying every sink SCC is poisoned.

---

## 2. Shortest paths give a directed forest toward `F_D`

For `v in P_D`, define

\[
d(v)=\operatorname{dist}_{I_D}(v,F_D).
\tag{HP.7}
\]

Equation (HP.6) makes `d(v)` finite. For every

\[
v\notin F_D,
\]

choose one outgoing implication arc

\[
v\longrightarrow p(v)
\]

on a shortest path to `F_D`, so

\[
d(p(v))=d(v)-1.
\tag{HP.8}
\]

The selected arcs cannot contain a directed cycle, because `d` strictly decreases along every selected arc. Every nonforbidden vertex contributes exactly one selected outgoing arc. Hence they form a directed forest, with all components flowing into `F_D`, and

\[
\boxed{
|E_{\rm forest}|=|P_D|-|F_D|.
}
\tag{HP.9}

Every selected arc is one of the Horn implication arcs and therefore is realized by a previously strict **upper near-diameter** source pair joining the two corresponding retained physical path layers.

The selected source pairs are distinct. A source pair has at most the two retained coordinates containing its endpoints. If the same pair supplied both directed orientations, selecting both would create a two-cycle, impossible because the forest distance strictly decreases. It cannot supply any third arc.

Therefore (HP.9) is also an exact count of distinct geometric blocker pairs in this forest.

If

\[
|F_D|<{|P_D|\over2},
\]

then

\[
|E_{\rm forest}|>{|P_D|\over2}
>\left({\gamma\over2}-o(1)\right)D,
\]

which proves (HP.4).

---

## 3. Many forbidden vertices force many permanent blockers

Assume instead

\[
|F_D|\ge {|P_D|\over2}.
\tag{HP.10}
\]

For each forbidden coordinate choose one previously strict source pair which makes that coordinate forbidden in the Horn encoding.

Class the chosen incidences by metric boundary:

- **LOWER:** the singleton exact swap reaches or violates distance `1`;
- **UPPER:** the singleton exact swap reaches or violates diameter `D` and remains bad whenever its other retained endpoint, if any, is also swapped.

At least one class contains at least `|F_D|/2` chosen coordinate incidences.

### 3.1 Lower winner

By the short-pair bandwidth theorem, every lower singleton blocker has endpoint-region distance at most fourteen. Retained coordinates are fifteen-spaced. Therefore its other endpoint cannot lie in a second retained layer.

So a lower source pair can poison only one coordinate of `P_D`. Distinct forbidden coordinates in the LOWER class require distinct lower source pairs. If LOWER wins,

\[
N_{\rm permanent\ lower}
\ge {|F_D|\over2}
\ge {|P_D|\over4}
>\left({\gamma\over4}-o(1)\right)D.
\tag{HP.11}
\]

Every such pair has

\[
1<|xy|\le1+O(D^{-1})
\]

and exact selected-cut support of length at most fourteen.

### 3.2 Upper winner

An upper source pair has at most two retained coordinates in its Boolean support, because a source pair has only two endpoints and every source vertex belongs to one physical layer. Hence the same upper pair can poison at most two retained coordinates.

If UPPER wins, at least `|F_D|/2` forbidden-coordinate incidences are upper, so the number of distinct permanent upper pairs is at least

\[
{1\over2}{|F_D|\over2}
={|F_D|\over4}
\ge {|P_D|\over8}
>\left({\gamma\over8}-o(1)\right)D.
\tag{HP.12}
\]

Every such pair lies in the inverse-`D` upper window

\[
D-O(D^{-1})\le|xy|<D.
\]

It is either an external one-coordinate blocker or a persistent two-coordinate upper blocker.

Equations (HP.11)--(HP.12) prove (HP.2)--(HP.3).

---

## 4. Ordered path support survives in every branch

The selected O--O dual path has regions

\[
R_0\xleftrightarrow{\tau_1}R_1\xleftrightarrow{}\cdots
\xleftrightarrow{\tau_m}R_m.
\]

If a retained blocker pair has endpoints in `R_a,R_b`, `a<b`, the phase-free exact path theorem gives selected-cut support

\[
\boxed{
I_{ab}=\{a+1,\ldots,b\}.
}
\tag{HP.13}

Thus the three-way extraction above retains more information than cardinality:

- permanent LOWER pairs are supported on intervals of length at most fourteen;
- permanent UPPER pairs carry arbitrary exact path intervals;
- implication-forest arcs carry exact path intervals and a directed tail coordinate, with each nonforbidden tail used once.

This interval structure is the natural input for the global train-defect budget. In particular, a linear upper family can now be split by interval length and forced either through a heavily loaded low-defect common cut or into a blocker-rich low-defect path window.

That is the next quantitative seam.

---

## 5. Frontier effect

The Horn obstruction now has the source-level normal form

```text
|P_D| > (gamma-o(1)) D, gamma = 791/9.6e9,
and no nonempty feasible closed set

=> either
   > (gamma/4-o(1)) D distinct permanent LOWER blockers,
   each with path bandwidth <= 14;

or
   > (gamma/8-o(1)) D distinct permanent UPPER near-diameter blockers;

or
   > (gamma/2-o(1)) D distinct UPPER near-diameter implication pairs
   forming an acyclic directed forest toward F_D.
```

This removes the possibility that all sink SCCs are poisoned by only a sparse exceptional set. A linear retained Horn system necessarily exposes a linear geometric obstruction population.

C-II remains open. The remaining work is now to fuse the two upper alternatives with the global low-defect train ladder, while the lower alternative is a fixed-bandwidth ordered near-unit obstruction family.
