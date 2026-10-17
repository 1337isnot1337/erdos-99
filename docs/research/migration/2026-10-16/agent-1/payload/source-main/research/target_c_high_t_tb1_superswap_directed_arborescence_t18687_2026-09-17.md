# Target C-II — the common TB1 super-swap obstruction graph has a rooted arborescence

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the one-sign strong-TB1 common-super-swap reduction; no canonical promotion claimed  
**Scope:** the one-sign strong-TB1 population through `t=(q-k)/D<=1.8687`  
**Dependencies:** common-super-swap cut theorem; common oriented TB1 axis; inactive near-unit degree bound; inactive near-diameter degree bound; superdiameter-thrackle lemma  
**Certificate:** `research/verify_target_c_high_t_tb1_superswap_directed_arborescence_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The common-super-swap theorem gives more than an undirected connected inactive graph. The endpoint violation has a preferred **moved side**. Orienting each inactive obstruction toward that moved side turns the cut theorem into a directed cut condition.

Let `M_D` be the one-sign strong-TB1 layer population, let `*` denote the residual source class, and use the common displacement

\[
V_D=-Q_Dw_*,
\qquad
Q_D={K\over D}
\]

from the common-super-swap theorem.

For a previously strict pair joining two distinct classes `A,B`, add the directed arc

\[
A\longrightarrow B
\]

whenever translating the endpoint in `B` by `V_D` while the endpoint in `A` is fixed makes that pair violate the unit or diameter bound. A pair may in principle contribute both orientations.

Then every nonempty layer subset `S\subseteq M_D` has a directed arc entering it from the complement. Hence every one-sign layer is reachable from `*`, and the directed obstruction graph contains a spanning out-arborescence rooted at `*`.

If

\[
m_D:=|M_D|>{s_0\over2}D-o(D),
\qquad
s_0={791\over320{,}000{,}000},
\]

this gives `m_D` distinct oriented inactive source pairs in one rooted obstruction tree.

Every arborescence arc belongs to one of three geometric classes:

1. **LOWER:** an inactive near-unit pair
   \[
   1<|r|\le1+{K\over D},
   \qquad
   r\cdot w_*>{K\over2D};
   \]
2. **SIGNED UPPER:** an inactive near-diameter pair with
   \[
   r\cdot w_*\le-\left({1\over4K}-o(1)\right)D;
   \]
3. **THIN UPPER:** an inactive superdiameter pair
   \[
   |r|>D-{1\over4D}>\sqrt{D^2-1}.
   \]

Therefore one class contains at least

\[
>{s_0\over6}D-o(D)
=(4.11979166667\times10^{-7})D-o(D)
\]

arborescence edges.

A pair that blocks the upper boundary in **both** orientations is much more singular:

\[
D-|r|=O(D^{-3}),
\qquad
|r\cdot w_*|=O(D^{-1}).
\]

The existing parallel-almost-diameter packing lemma therefore bounds all such bidirectional upper pairs by `O(1)` source-wide. Lower-bound blockers can never be bidirectional.

Thus, up to `O(1)` exceptions, every edge of the rooted obstruction tree has a unique preferred moved side.

---

## 1. Directed obstruction graph

Retain the common-super-swap notation. Every layer in `M_D` is a disjoint physical source class `R_i`; the root `*` contains every source point not belonging to the one-sign layer population.

Take a previously strict source pair `xy` whose endpoints lie in distinct classes `A,B`. Orient its old relative vector from the endpoint in `A` to the endpoint in `B`:

\[
r=y-x.
\tag{DA.1}
\]

If class `B` is moved by the common super-swap while `A` is fixed, its final relative vector is

\[
r-Q_Dw_*.
\tag{DA.2}
\]

Add the arc `A->B` exactly when

\[
|r-Q_Dw_*|\le1
\quad\text{or}\quad
|r-Q_Dw_*|\ge D.
\tag{DA.3}
\]

The pair was previously strict, so initially

\[
1<|r|<D.
\tag{DA.4}
\]

The reverse arc `B->A` is defined by applying the same common displacement to the endpoint in `A`; in the orientation (DA.1), this tests `r+Q_Dw_*`.

---

## 2. Every nonroot cut has an incoming arc

Take any nonempty subset

\[
S\subseteq M_D.
\]

Translate exactly the union

\[
U_S=\bigcup_{i\in S}R_i
\]

by the common super-swap vector `V_D=-Q_Dw_*`.

The common-super-swap cut theorem says that some previously strict pair has exactly one endpoint in `U_S` and violates a metric bound at the endpoint configuration.

Let its outside class be `A` and its inside class be `B\in S`. With the relative orientation from outside to inside, its final vector is exactly `r-Q_Dw_*`, so (DA.3) holds. Therefore the directed obstruction graph has an arc

\[
A\longrightarrow B
\]

with

\[
A\notin S,
\qquad
B\in S.
\]

Thus

\[
\boxed{
\delta^-(S)\ne\varnothing
\quad\text{for every nonempty }S\subseteq M_D.
}
\tag{DA.5}

---

## 3. Directed cut condition is equivalent to root reachability

Let `R` be the set of layer vertices reachable from `*` by directed paths. Suppose `R\ne M_D` and put

\[
S=M_D\setminus R.
\]

Then `S` is nonempty. By (DA.5) there is an arc from a vertex outside `S`, hence from `*\cup R`, into `S`. Its head would be reachable from `*`, contradiction.

Therefore

\[
\boxed{
\text{every layer vertex is reachable from }*.
}
\tag{DA.6}

Choose, for each layer, one incoming arc on a shortest root path. These arcs contain a spanning directed out-arborescence `T_D` rooted at `*`.

Its underlying undirected graph is a tree on `m_D+1` class vertices, so it has exactly

\[
\boxed{|E(T_D)|=m_D.}
\tag{DA.7}

The class edges of the tree are distinct. Choose one source pair realizing each selected arc. A source pair joins one fixed unordered pair of classes, so the resulting `m_D` blocker pairs are distinct.

This directed statement strictly strengthens the previous undirected connectivity conclusion.

---

## 4. Exact geometry of a lower arc

Let `A->B` be an arc caused by the unit lower boundary. With `r` oriented from `A` to `B`,

\[
|r-Q_Dw_*|\le1,
\qquad
|r|>1.
\tag{DA.8}

Expanding,

\[
|r|^2-2Q_D(r\cdot w_*)+Q_D^2\le1.
\]

Hence

\[
\boxed{
r\cdot w_*
\ge{|r|^2-1+Q_D^2\over2Q_D}
>{Q_D\over2}
={K\over2D}.}
\tag{DA.9}

The triangle inequality gives

\[
\boxed{1<|r|\le1+Q_D=1+{K\over D}.}
\tag{DA.10}

So every lower arc is geometrically oriented: the moved endpoint lies strictly farther in the `+w_*` coordinate by more than `K/(2D)`.

The reverse orientation cannot also be a lower arc. Indeed, if both

\[
|r-Q_Dw_*|\le1,
\qquad
|r+Q_Dw_*|\le1,
\]

then adding the squared inequalities gives

\[
2|r|^2+2Q_D^2\le2,
\]

contrary to `|r|>1`.

Thus lower blockers are automatically unidirectional.

---

## 5. Upper arcs split into signed and superdiameter classes

Let `A->B` instead be caused by the diameter upper boundary:

\[
|r-Q_Dw_*|\ge D,
\qquad
|r|<D.
\tag{DA.11}

Put

\[
\xi=D-|r|>0.
\]

The triangle inequality gives

\[
0<\xi\le Q_D.
\tag{DA.12}

Expanding (DA.11),

\[
r\cdot w_*
\le
-{D^2-|r|^2-Q_D^2\over2Q_D}.
\tag{DA.13}

Fix

\[
\boxed{\tau={1\over4K}.}
\tag{DA.14}

### 5.1 Signed upper

If

\[
\xi\ge\tau Q_D={1\over4D},
\tag{DA.15}

then

\[
D^2-|r|^2
=\xi(D+|r|)
\ge2D\xi-O(Q_D\xi).
\]

Using `Q_D=K/D` in (DA.13),

\[
\boxed{
r\cdot w_*
\le-\left({1\over4K}-o(1)\right)D.}
\tag{DA.16}

Thus a nonthin upper arc has a fixed macroscopic negative projection on the common transverse axis.

### 5.2 Thin upper

If instead

\[
0<\xi<{1\over4D},
\tag{DA.17}

then

\[
|r|>D-{1\over4D}.
\]

Since

\[
\sqrt{D^2-1}<D-{1\over2D}<D-{1\over4D}
\]

for all sufficiently large `D`,

\[
\boxed{|r|>\sqrt{D^2-1}.}
\tag{DA.18}

Every thin upper arborescence edge therefore belongs to the existing straight-line geometric superdiameter thrackle. Its endpoints are convex-hull vertices, and any two vertex-disjoint thin upper edges cross properly.

---

## 6. Bidirectional upper blockers are globally negligible

Suppose one previously strict pair gives both arcs `A->B` and `B->A` at the upper boundary. In the orientation (DA.1),

\[
|r-Q_Dw_*|\ge D,
\qquad
|r+Q_Dw_*|\ge D.
\tag{DA.19}

Taking the smaller of the two squared left sides gives

\[
|r|^2+Q_D^2-2Q_D|r\cdot w_*|
\ge D^2.
\tag{DA.20}

Therefore

\[
\boxed{
D^2-|r|^2\le Q_D^2,
\qquad
|r\cdot w_*|\le {Q_D\over2}.}
\tag{DA.21}

It follows that

\[
\boxed{
D-|r|\le {Q_D^2\over D+|r|}=O(D^{-3}),
}
\tag{DA.22}

and

\[
\boxed{
d_{\mathbb{RP}^1}([r],[u_*])=O(D^{-2}),
\qquad u_*=w_*^\perp.}
\tag{DA.23}

The previously proved parallel-almost-diameter packing lemma is much stronger than needed here: a unit-separated diameter-`D` source contains only `O(1)` pairs of length `D-O(D^-2)` in a common `O(D^-1)` projective cone. Hence

\[
\boxed{N_{\rm bidirectional\ upper}=O(1).}
\tag{DA.24}

So, after deleting only `O(1)` source pairs, every directed blocker has a unique preferred moved side.

---

## 7. A three-way linear arborescence fork

The rooted arborescence has

\[
m_D>{s_0\over2}D-o(D)
\]

arcs. Split them into LOWER, SIGNED UPPER, and THIN UPPER according to Sections 4--5. One class has cardinality at least

\[
\boxed{
>{s_0\over6}D-o(D)
=(4.11979166667\times10^{-7})D-o(D).}
\tag{DA.25}

### LOWER winner

All LOWER source pairs have length in `(1,1+K/D]`. The near-unit graph has maximum degree at most six for all sufficiently large `D`. Greedy matching gives a vertex-disjoint matching of size

\[
\boxed{
>{s_0\over66}D-o(D)
=(3.74526515152\times10^{-8})D-o(D).}
\tag{DA.26}

Every matching edge retains its arborescence direction and positive `w_*` projection.

### SIGNED UPPER winner

All SIGNED UPPER edges are `D-O(D^-1)` pairs with the fixed negative projection (DA.16). The existing near-diameter degree estimate

\[
\Delta\le(8\,3^{1/8}+o(1))D^{3/4}
\]

gives a vertex-disjoint matching of size

\[
\boxed{
\left({s_0\over96\,3^{1/8}}-o(1)\right)D^{1/4}.
}
\tag{DA.27}

### THIN UPPER winner

The same matching bound applies, and the whole THIN UPPER family is a geometric thrackle. Hence there is a vertex-disjoint matching of size

\[
\boxed{
\left({s_0\over96\,3^{1/8}}-o(1)\right)D^{1/4}
}
\tag{DA.28}

whose every two chords cross properly.

Numerically,

\[
{s_0\over96\,3^{1/8}}
=2.24447677217\ldots\times10^{-8}.
\tag{DA.29}

---

## 8. Frontier effect

The common super-swap obstruction is now directional rather than merely connected:

```text
root * plus > (s0/2)D one-sign strong-TB1 layers
+ every nonroot cut has an incoming violating pair
+ a rooted out-arborescence of > (s0/2)D distinct inactive pairs

arborescence edges split into:
    near-unit arcs directed toward increasing w_*;
    near-diameter arcs with macroscopic decreasing w_* projection;
    or superdiameter-thrackle arcs.

only O(1) upper pairs can block in both orientations.
```

This does not close the strong-TB1 branch. The directed tree is a graph on **layer classes**, not on common source endpoints; consecutive arborescence arcs may use unrelated source vertices inside their shared layer. Therefore one may not telescope the `w_*` projections along a root-to-layer path without an additional bound on the `w_*` diameter of each physical layer. That is the exact new seam.

A closing continuation should either:

1. control the transverse diameter of enough one-sign physical layers, allowing the directed `w_*` increments/decrements to telescope; or
2. combine the arborescence with the ordered path-layer/train grid to show that one of the three linear edge classes cannot connect all layer cuts.

No such telescoping or layer-diameter claim is made here.
