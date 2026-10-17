> Generated reading edition · [exact source](../../../docs/reports/target_c_slope_one_core_collapse_2026-09-09.md) · source SHA-256 `32485f1110cfba9b9273cb5dc46ed873e0a980f8e8559d837e9922de37876eff`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-485D0DB158E3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — SCC: the RCC slope-one endpoint has subquadratic force-visible core

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** exact planar Euler ledger + diameter-geodesic strip + packing  
**Target:** Target C C-II, S1E slope-one endpoint  
**Depends on:** S1E, DGS, C40 population bound, Oler finite packing inequality  
**New external literature:** none beyond canonical Eppstein/Oler dependencies  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

S1E leaves two apparent global possibilities at the RCC slope-one endpoint: a quadratic force-visible/rhombic bulk, or a subquadratic force-visible core with a quadratic invisible/rattler population.

SCC eliminates the first alternative completely.

Assume

$$
D\varepsilon\to0,
\qquad
\frac{e_{BB}+2s_C}{D}\to1.
\tag{SCC.1}
$$

S1E gives a unique harmonic component `I_*` with internal graph diameter

$$
\delta_*=D+o(D)
\tag{SCC.2}
$$

and Eppstein slack

$$
r_*=2n_*-\delta_*-2-e_*=o(D).
\tag{SCC.3}
$$

NSE/DGS give actual loaded attachments `z,a in A_*` with

$$
|z-a|=D.
\tag{SCC.4}
$$

Adjoin `z` and `a` to the internal penny graph `C[I_*]`, retaining **one** actual contact edge from each attachment into `I_*`. Call the resulting connected plane triangle-free unit-distance graph `G'`.

Then the exact planar identity

$$
\boxed{
b'+Q'=2\delta'+2r'
}
\tag{SCC.5}
$$

holds, where

- `delta'` is the graph diameter of `G'`;
- `r'=2|V(G')|-delta'-2-|E(G')|` is its Eppstein slack;
- `b'` is its outer-face boundary-walk length;
- `Q'=sum_F(deg F-4)` over bounded faces, with face degrees counted as boundary-walk lengths.

For the augmented graph,

$$
\delta'=D+o(D),
\qquad
r'=o(D).
$$

The attachments `z,a` are force-hull extreme points, hence extreme in `conv V(G')` and therefore outer-face vertices of `G'`. Splitting the outer boundary walk at `z,a` gives two polygonal `z-a` walks. Each has unit-edge length at least `D` by SCC.4. Thus

$$
b'\ge2D.
$$

Using SCC.5,

$$
b'+Q'=2D+o(D).
$$

Since `Q'>=0`, this forces

$$
\boxed{b'=2D+o(D),\qquad Q'=o(D).}
\tag{SCC.6}
$$

Each of the two outer `z-a` walks therefore has length `D+o(D)`. The elementary DGS projection argument applies to each walk, whether or not it is graph-shortest, and puts every outer-face vertex in an `o(D)`-width strip around the diameter line `za`.

Every vertex of a finite plane straight-line graph lies in the convex hull of its outer-face vertices. Hence **every** vertex of `G'` lies in the same `o(D)`-width strip.

Oler packing then gives

$$
\boxed{n_*=o(D^2).}
\tag{SCC.7}
$$

S1E also gives

$$
\sum_{r\ne *}\delta_r=o(D).
$$

C40's component population bound

$$
n_r\le(2\delta_r+1)^2
$$

and `c_I=O(D)` imply

$$
\boxed{
\sum_{r\ne *}n_r=o(D^2).
}
\tag{SCC.8}
$$

Finally `q=|B_+|=O(D)`, so the complete force-visible contact core satisfies

$$
\boxed{|V(C)|=o(D^2).}
\tag{SCC.9}
$$

Since a global minimum-diameter source has `n=Theta(D^2)`, the RCC slope-one endpoint can survive only if a quadratic population lies outside the force-visible core.

This removes the quadratic-rhombic-bulk alternative from S1E.

---

## 1. Exact Eppstein slack / face ledger

Let `G` be any connected plane triangle-free simple graph. Put

$$
n=|V(G)|,
\qquad e=|E(G)|,
\qquad\delta=\operatorname{diam}_{graph}(G).
$$

Let `f` be the number of bounded faces, `b` the outer-face boundary-walk length, and

$$
Q:=\sum_{F\ bounded}(\deg F-4).
$$

Euler gives

$$
f=e-n+1.
\tag{1.1}
$$

The face-degree sum is

$$
2e=b+4f+Q.
\tag{1.2}
$$

Substitute (1.1):

$$
b+Q=4n-4-2e.
\tag{1.3}
$$

Define the Eppstein slack

$$
r:=2n-\delta-2-e.
\tag{1.4}
$$

Then

$$
2\delta+2r
=4n-4-2e.
$$

Comparing with (1.3) proves the exact identity

$$
\boxed{b+Q=2\delta+2r.}
\tag{SCC.10}
$$

This is algebraic; Eppstein is used only to know `r>=0` for triangle-free penny graphs.

---

## 2. Augment the giant harmonic component by two diameter attachments

Let

$$
G_*:=C[I_*].
$$

Choose one contact edge `zu` with `u in I_*` and one contact edge `av` with `v in I_*`. Define `G'` by adding `z,a` and exactly these two edges to `G_*`.

Thus

$$
|V(G')|=n_*+2,
\qquad
|E(G')|=e_*+2.
\tag{2.1}
$$

Both new vertices have degree one in `G'`. Therefore adding them creates no shortcut between old internal vertices. Hence

$$
\delta_*\le\delta'\le\delta_*+2.
\tag{2.2}
$$

Also `z,a` are vertices of `G'` at Euclidean distance `D`, and every graph edge has Euclidean length one, so

$$
\delta'\ge d_{G'}(z,a)\ge D.
\tag{2.3}
$$

Using S1E's `delta_*=D+o(D)`, equations (2.2)--(2.3) give

$$
\boxed{\delta'=D+o(D).}
\tag{SCC.11}
$$

The augmented slack is

$$
\begin{aligned}
r'
&=2(n_*+2)-\delta'-2-(e_*+2)\\
&=2n_*-\delta'-e_*.
\end{aligned}
$$

While

$$
r_*=2n_*-\delta_*-2-e_*.
$$

Thus

$$
\boxed{r'=r_*+(\delta_*-\delta')+2.}
\tag{2.4}
$$

By (2.2), the correction lies in `[0,2]`. Therefore

$$
\boxed{r_*=o(D)\Longrightarrow r'=o(D).}
\tag{SCC.12}
$$

The graph remains a triangle-free penny graph because it is a subgraph of the unit-contact graph of the same unit-separated point set.

---

## 3. The diameter attachments lie on the augmented outer face

C26/C42 give

$$
B_+=\operatorname{Vert}(F),
\qquad F=\operatorname{conv}V(C).
$$

Thus `z` and `a` are extreme points of `F`.

Because

$$
V(G')\subseteq V(C),
\qquad z,a\in V(G'),
$$

an extreme point of `F` cannot become a convex combination of the smaller set `V(G')`. Therefore `z,a` are also extreme points of

$$
\operatorname{conv}V(G').
$$

Every extreme point of the straight-line embedded graph lies on its outer face. Hence `z,a` occur on the outer-face boundary walk of `G'`.

Split that closed boundary walk at `z` and `a`. This gives two `z-a` polygonal walks `W_1,W_2`, with lengths `L_1,L_2` satisfying

$$
L_1+L_2=b'.
\tag{3.1}
$$

Each consists of unit edges and has endpoint displacement `D`, so

$$
\boxed{L_1\ge D,\qquad L_2\ge D.}
\tag{SCC.13}
$$

Therefore

$$
\boxed{b'\ge2D.}
\tag{SCC.14}
$$

---

## 4. Near Eppstein equality forces both outer arcs to be diameter geodesics

Apply SCC.10 to `G'`:

$$
b'+Q'=2\delta'+2r'.
$$

By SCC.11--SCC.12,

$$
b'+Q'=2D+o(D).
\tag{4.1}
$$

Together with SCC.14 and `Q'>=0`,

$$
2D\le b'\le2D+o(D).
$$

Hence

$$
b'=2D+o(D).
$$

Subtracting from (4.1) gives

$$
Q'=o(D).
$$

This proves SCC.6.

Now (3.1), SCC.13, and `b'=2D+o(D)` give separately

$$
\boxed{L_1=D+o(D),\qquad L_2=D+o(D).}
\tag{SCC.15}

Thus both outer-face arcs are polygonal near-geodesics joining the actual diameter pair.

---

## 5. Both outer arcs lie in an `o(D)` strip

The projection part of DGS does not need graph-shortestness. It needs only a unit-edge polygonal walk of length `D+E` whose endpoints are distance `D` apart.

For each `W_i`, let

\[
E_i:=L_i-D=o(D).
$$

DGS gives transverse width

$$
B_i:=\sqrt{2L_iE_i}=o(D).
\tag{5.1}
$$

It also gives longitudinal prefix coordinates within `[-E_i,D+E_i]`. Therefore every vertex occurrence on `W_i` lies in the rectangle

$$
\mathcal S_i
:=
\left\{
 z+pu+yJu:
 -E_i\le p\le D+E_i,
 \ |y|\le B_i
\right\}.
$$

Let

$$
E_{out}:=\max(E_1,E_2),
\qquad
B_{out}:=\max(B_1,B_2).
$$

Then every outer-face vertex lies in the common convex strip rectangle

$$
\mathcal S
=
\left\{
 z+pu+yJu:
 -E_{out}\le p\le D+E_{out},
 \ |y|\le B_{out}
\right\}.
\tag{5.2}
$$

Its area is

$$
\operatorname{area}(\mathcal S)
=2B_{out}(D+2E_{out})
=o(D^2),
\tag{5.3}
$$

and its perimeter is `O(D+B_out+E_out)=O(D)+o(D)`.

Every vertex of `G'` lies in the convex hull of the outer-face vertices, and `S` is convex. Therefore

$$
\boxed{V(G')\subseteq\mathcal S.}
\tag{SCC.16}
$$

This is the key global use of near-Eppstein equality: the **entire** giant harmonic component, not only one selected path, is trapped in the near-diameter strip.

---

## 6. Oler packing makes the giant component subquadratic

The vertices of `G'` are unit-separated and lie in the convex rectangle `S`. Oler's finite packing inequality gives

$$
|V(G')|
\le
\frac2{\sqrt3}\operatorname{area}(\mathcal S)
+\frac12\operatorname{per}(\mathcal S)+1.
\tag{6.1}
$$

By (5.3),

$$
\operatorname{area}(\mathcal S)=o(D^2),
$$

and the perimeter term is `O(D)+o(D)=o(D^2)`. Hence

$$
|V(G')|=o(D^2).
$$

Since `|V(G')|=n_*+2`, this proves SCC.7.

---

## 7. All remaining harmonic components are subquadratic in aggregate

S1E gives

$$
T_D:=\sum_{r\ne *}\delta_r=o(D).
\tag{7.1}
$$

C40 gives for every component

$$
n_r\le(2\delta_r+1)^2
=4\delta_r^2+4\delta_r+1.
$$

Summing over `r!=*`,

$$
\sum_{r\ne *}n_r
\le
4\sum_{r\ne *}\delta_r^2
+4T_D
+(c_I-1).
\tag{7.2}
$$

Now

$$
\sum_{r\ne *}\delta_r^2
\le T_D^2=o(D^2).
$$

Also `c_I=O(D)` from ZU together with `q=O(D)` and the slope-one bound `e_BB+2s_C=O(D)`. Therefore every term in (7.2) is `o(D^2)`, proving SCC.8.

Finally

$$
|V(C)|
=q+\sum_rn_r.
$$

Since `q<=pi D`, SCC.7--SCC.8 give SCC.9.

---

## 8. Global consequence

The canonical global-minimum diameter asymptotics give

$$
n=\Theta(D^2).
$$

SCC proves

$$
|V(C)|=o(D^2).
$$

Thus the number of source points outside the force-visible contact core satisfies

$$
\boxed{n-|V(C)|=\Theta(D^2).}
\tag{SCC.17}

This statement is deliberately phrased at the force-visible-core level. SCC does not assume that all of these points lie outside `F`; some may be contact-invisible points geometrically contained in the force hull.

Therefore the only surviving slope-one branch is now a **quadratic invisible/rattler population branch**. The quadratic rhombic-force-bulk branch is impossible.

---

## 9. Relation to the previous Target B regression

A wide square rectangle can exactly saturate Eppstein's edge bound, and a constant-width square ladder can also satisfy a near-diameter path. Neither contradicts SCC.

The extra ingredient is that `z,a` are an **actual Euclidean diameter pair** and both are outer-face vertices of the augmented giant component. Near Eppstein equality then forces *both* outer-face arcs between them to have length `D+o(D)`. A genuinely wide rectangle cannot satisfy that: its two boundary arcs between opposite Euclidean-diameter endpoints pay a linear excess.

Thus SCC removes the wide-rhombic-grid regression specifically at the S1E slope-one endpoint without asserting any false local degree-four theorem.

A narrow or sublinear-width ladder remains possible, but Oler shows it contains only `o(D^2)` force-visible vertices, which is enough for SCC.

---

## 10. Audit / edge cases

- `G'` retains only one contact edge from each of `z,a` into `I_*`. This is intentional: it makes them leaves and prevents new shortcuts among internal vertices.
- The selected attachment edges are actual unit contacts, so `G'` is still a straight-line triangle-free penny graph.
- Outer-face boundary is a **walk**; bridges may be repeated. Splitting at `z,a` still gives two unit-edge walks of length at least the Euclidean endpoint distance.
- DGS's strip estimate applies to polygonal walks as well as paths because its projection identity uses only edge count and endpoint displacement.
- SCC does not claim the giant component has few vertices linearly; only `o(D^2)` is proved.
- The conclusion concerns the force-visible contact core, not the location of the remaining source points.

## 11. Next target

SCC removes the force-bulk branch from RCC equality. The slope-one endpoint now has

\[
\Theta(D^2)
$$

source points outside the force-visible core, while the entire `D^2` KKT stress and nearly unit boundary response live on an `o(D^2)` near-diameter strip.

The next closing route should therefore be global rather than another local rhombus argument:

1. use OP/ER to divide the quadratic invisible population between points inside the force hull and points outside it;
2. if a quadratic population lies outside `F`, combine the actual source-hull annulus / fixed-source Hall machinery with the thin stressed core;
3. if most invisible points lie inside `F`, near-saturation of the Oler capacity of `F` should force `F` toward the full source-hull disk, while the force-visible vertices themselves remain confined to the near-diameter strip plus only `o(D^2)` other core vertices.

That is now the only slope-one global obstruction.

## 12. Compact handoff

```text
SCC kills the quadratic force-visible bulk at RCC slope one.
S1E: giant harmonic I_* has delta_*=D+o(D), Eppstein slack r_*=o(D).
NSE supplies actual diameter attachments z,a in A_* with |z-a|=D.
Add z,a as leaves using one contact edge each, forming G'. Then
    delta'=D+o(D), r'=o(D).
For any connected plane triangle-free graph,
    b+Q=2delta+2r
exactly by Euler and the face-degree sum.
z,a are force-hull extreme, hence outer-face vertices of G'. The two outer boundary
z-a walks each have unit-edge length >=D, so b'>=2D.
Thus
    b'+Q'=2D+o(D)
forces
    b'=2D+o(D), Q'=o(D),
and each outer z-a walk has length D+o(D).
DGS puts both walks in an o(D)-width strip around za. Every graph vertex lies in
the convex hull of outer-face vertices, hence in the same strip. Oler gives
    n_*=o(D^2).
S1E has sum_{r!=*}delta_r=o(D); C40 then gives sum_{r!=*}n_r=o(D^2).
Since q=O(D),
    |V(C)|=o(D^2).
But global n=Theta(D^2), so the slope-one endpoint requires a quadratic population
outside the force-visible core. The quadratic rhombic-bulk branch is eliminated.
```
