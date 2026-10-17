# Target C-II — adjacent switching diameter rows form a one-arc ordered interface

**Date:** 2026-09-15  
**Status:** proof-only exact structural refinement  
**Scope:** any two consecutive outer-to-outer train cuts on one laminar complement-dual path; in particular the triple-small adjacent pair used by the finite-cusp theorem  
**Dependencies:** exact laminar interval support; audited proper O--O train crosscuts; convex geometric-thrackle property of actual diameter edges; ordered-thrackle train-cut theorem  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The adjacent-cut finite-cusp theorem leaves a bounded family of actual diameter rows whose interval incidence changes between two consecutive laminar O--O cuts. That family is not an arbitrary finite set.

For two consecutive cuts `tau_i,tau_{i+1}`, let `M` be the unique complement-dual layer between them, `L` the union of layers to the `tau_i` side, and `R` the union of layers to the `tau_{i+1}` side. Split the switching rows into

- **left-switch rows**: diameter edges meeting `tau_i` but not `tau_{i+1}`;
- **right-switch rows**: diameter edges meeting `tau_{i+1}` but not `tau_i`.

Then:

1. every switching diameter edge has exactly one endpoint in `M`; a left-switch edge joins `L` to `M`, and a right-switch edge joins `M` to `R`;
2. the switching diameter graph is bipartite and hence a forest;
3. the two proper train crosscuts cut the outer boundary into four cyclic arcs
   \[
   B_L,\ B_M^+,\ B_R,\ B_M^-;
   \]
   every switching middle endpoint lies in `B_M^+ union B_M^-`;
4. if both left-switch and right-switch rows occur, **all** switching middle endpoints lie on one common middle boundary arc, either `B_M^+` or `B_M^-`;
5. on that common middle arc there is one monotone interface: after orienting the arc suitably, every right-switch middle endpoint precedes every distinct left-switch middle endpoint. The two middle endpoint sets have at most one common vertex, which can occur only at the transition;
6. consequently, when both switch orientations occur, the complete switching graph is an ordered convex-thrackle caterpillar forest across two complementary cyclic vertex intervals.

Thus the finite cusp left by the opposite two-cut shear is an **ordered one-arc interface forest**, not an arbitrary bounded collection of active diameter constraints.

---

## 1. Interval support localizes one endpoint to the middle layer

Use the layer notation of the exact laminar multishear theorem. For a diameter edge `h=xy`, orient it so

\[
\ell(x)=a<b=\ell(y).
\]

Its selected-cut support is the interval

\[
I_h=\{a+1,\ldots,b\}.
\]

Fix consecutive cut indices `i,i+1`.

If `h` meets cut `i` but not cut `i+1`, then

\[
i\in I_h,
\qquad
i+1\notin I_h.
\]

Because `I_h` is an interval, its right endpoint is exactly `i`. Hence

\[
b=i,
\qquad a<i.
\]

So one endpoint lies in layer `i=M`, while the other lies in `L`.

Similarly, if `h` meets cut `i+1` but not cut `i`, then the left endpoint of `I_h` is `i+1`, so

\[
a=i,
\qquad b>i,
\]

and `h` joins `M` to `R`.

Therefore

\[
\boxed{
H_{sw}\subseteq (L\times M)\cup(M\times R).
}
\tag{SO.1}

In particular `H_sw` is bipartite with parts

\[
M,\qquad L\cup R.
\]

The actual diameter graph is a straight-line convex geometric thrackle: any two distinct vertex-disjoint diameter edges cross, and every graph cycle is odd. A bipartite subgraph has no odd cycle, while a geometric-thrackle subgraph has no even cycle. Hence

\[
\boxed{H_{sw}\text{ is a forest}.}
\tag{SO.2}

This conclusion uses no asymptotic phase information and no KKT multiplier estimate.

---

## 2. Two consecutive crosscuts give a four-block boundary order

Represent `tau_i,tau_{i+1}` by their audited pairwise-disjoint proper centerline crosscuts of the closed outer-face disk. Their four boundary endpoints are distinct because the selected O--O trains are disjoint.

Two disjoint proper crosscuts divide the disk into exactly three regions: the `L` region, the middle `M` region, and the `R` region. The middle region meets the outer boundary in exactly two open arcs. After possibly reversing the boundary orientation, write the four open boundary blocks in cyclic order as

\[
\boxed{
B_L,\ B_M^+,\ B_R,\ B_M^-.
}
\tag{SO.3}

The `L` region meets the outer boundary only in `B_L`; the `R` region only in `B_R`; and the middle region in `B_M^+ union B_M^-`.

Every endpoint of an actual diameter edge is an extreme point of the source convex hull. Indeed, if a diameter endpoint were a nontrivial convex combination of two distinct source-convex-hull points, strict convexity of squared distance to the opposite endpoint would make its distance strictly smaller than the maximum of the two endpoint distances. Thus every diameter endpoint lies on the actual outer boundary, and the outer-face cyclic order restricted to diameter endpoints agrees with their convex-hull cyclic order.

Consequently a left-switch diameter has boundary type

\[
B_L-B_M^+
\quad\text{or}\quad
B_L-B_M^-,
\tag{SO.4}
\]

while a right-switch diameter has type

\[
B_M^+-B_R
\quad\text{or}\quad
B_M^--B_R.
\tag{SO.5}

---

## 3. Opposite middle arcs are incompatible across switch orientations

Suppose there is a left-switch diameter

\[
e_L=lm_+,
\qquad l\in B_L,\ m_+\in B_M^+,
\]

and a right-switch diameter

\[
e_R=rm_-,
\qquad r\in B_R,\ m_-\in B_M^-.
\]

The four endpoints occur cyclically in the block order

\[
l,\ m_+,\ r,\ m_-.
\]

The chords `lm_+` and `rm_-` pair adjacent blocks and therefore do not cross. They are vertex-disjoint because their endpoints lie in four disjoint open boundary blocks. This contradicts the convex diameter-thrackle property.

Hence

\[
\boxed{
(L-M^+)\text{ and }(R-M^-)\text{ switching edges cannot coexist}.}
\tag{SO.6}

The same argument with `+` and `-` interchanged gives

\[
\boxed{
(L-M^-)\text{ and }(R-M^+)\text{ switching edges cannot coexist}.}
\tag{SO.7}

Now assume both left-switch and right-switch rows occur. Choose one of each. By (SO.6)--(SO.7), their middle endpoints must lie on the same middle boundary arc, say `B_M^+`. Once one right-switch edge uses `B_M^+`, (SO.7) forbids every left-switch edge from using `B_M^-`. Once one left-switch edge uses `B_M^+`, (SO.6) forbids every right-switch edge from using `B_M^-`.

Therefore

\[
\boxed{
\text{if both switch orientations occur, every switching middle endpoint lies on one common }B_M^\star.
}
\tag{SO.8}

This is the first collapse of the finite cusp from two middle boundary arcs to one.

---

## 4. The common middle arc has one prefix/suffix interface

Assume the common arc is `B_M^+`; the other case is the same after reversing orientation. Orient `B_M^+` consistently with the cyclic block order

\[
B_L\to B_M^+\to B_R.
\]

Take a left-switch edge

\[
e_L=lm_L,
\qquad l\in B_L,\ m_L\in B_M^+,
\]

and a right-switch edge

\[
e_R=m_Rr,
\qquad m_R\in B_M^+,\ r\in B_R.
\]

If `m_L=m_R`, the two diameter edges share their middle endpoint and the thrackle condition is already satisfied.

Suppose `m_L` and `m_R` are distinct. Then the two edges are vertex-disjoint, because their exterior endpoints lie in disjoint blocks `B_L,B_R`. They must therefore cross. In convex cyclic order, the chords `l m_L` and `m_R r` cross exactly when their four endpoints alternate. Since `l` precedes the whole middle block and `r` follows it, alternation is equivalent to

\[
\boxed{m_R<m_L\quad\text{along }B_M^+.}
\tag{SO.9}

Thus every distinct right-switch middle endpoint precedes every left-switch middle endpoint.

Let `M_R` and `M_L` denote the sets of middle vertices incident respectively to right-switch and left-switch edges. Equation (SO.9) implies

\[
\boxed{
M_R\setminus M_L
\text{ is an initial block and }
M_L\setminus M_R
\text{ is a terminal block of the participating middle vertices}.}
\tag{SO.10}

Moreover

\[
\boxed{|M_R\cap M_L|\le1.}
\tag{SO.11}

Indeed, if two distinct middle vertices `m_1<m_2` each belonged to both sets, choose a left-switch edge incident to `m_1` and a right-switch edge incident to `m_2`. They are vertex-disjoint and (SO.9) would require `m_2<m_1`, contradiction.

So at most one middle hull vertex can serve as a common left/right switching hub, and if it exists it lies exactly at the interface between the right prefix and left suffix.

---

## 5. Ordered caterpillar consequence

When both switch orientations occur, (SO.8) leaves no participating switching vertex on the unused middle boundary arc. In the cyclic order restricted to vertices of `H_sw`, the common middle arc `B_M^star` is one interval, while the exterior switching vertices in `B_R union B_L` form the complementary cyclic interval across the boundary wrap.

Therefore the standard ordered-thrackle train-cut theorem applies to `H_sw`. Besides the forest property (SO.2), each connected component is a caterpillar; for independent switching edges the order of exterior endpoints agrees with the order of middle endpoints after the usual reversal convention on complementary arcs.

Combined with (SO.10), the finite switching cusp has the schematic form

```text
exterior:      ... L ... | ... R ...
                         \\ /
middle arc:  [ right-switch prefix ][optional common hub][ left-switch suffix ]
```

with no switching middle endpoint on the second middle boundary arc.

---

## 6. Effect on the triple-small finite cusp

Apply the theorem to the triple-small adjacent pair used in the finite-cusp reduction. That theorem already gives

\[
\#H_{sw}<21200+o(1),
\qquad
\sum_{h\in H_{sw}}\beta_h<{21200\over D}+o(D^{-1}),
\]

and projective train-direction gap `O(D^-1)`.

The present theorem adds exact source-level topology:

```text
bounded switching set
+ one endpoint of every switching diameter lies in the single middle layer
+ switching graph is a forest
+ if both start/stop orientations occur, all middle endpoints lie on one hull arc
+ right-switch middle endpoints form one prefix
+ left-switch middle endpoints form one suffix
+ at most one middle vertex is a common left/right hub
+ each component is an ordered caterpillar.
```

This does not itself produce a diameter-decreasing shear. A star centered at the possible transition hub remains a legitimate regression, and KKT stationarity still prevents simply discarding small-multiplier active rows.

The next closing target is therefore narrower: analyze the first-derivative signs of this one-arc ordered interface under the opposite two-cut shear, or prove that a transition-hub/star regression is incompatible with two-sided Section-157 bracing and the exact cut resultants.

**Disposition:** proved proof-only exact structural refinement of the finite cusp. C-II and Level I remain open.
