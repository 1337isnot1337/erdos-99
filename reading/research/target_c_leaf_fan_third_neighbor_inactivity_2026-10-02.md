> Generated reading edition · [exact source](../../research/target_c_leaf_fan_third_neighbor_inactivity_2026-10-02.md) · source SHA-256 `1a453ca113677e02cb363086add7b2d726ab8dae95b9941e553381c6d709cece`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "caf43c8ad2ddd0e34a37157bd8e1fec769a32c28", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_leaf_fan_third_neighbor_inactivity_2026-10-02.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "255552154f2752f1f0cb17a6065210ea9d9608d1eda001bdf3394106db184844"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: third contacts of exact diameter-leaf fans are diameter-inactive

**Date:** 2026-10-02  
**Base main:** b2bed44eadfdd049794e5f5db5ec830f90e46119  
**Status:** proof-only local geometry theorem. Level I and C-II remain open.

## 1. Statement

Let
$$
p_{i-1},p_i,p_{i+1}
$$
be three consecutive vertices of one exact good same-carrier diameter-leaf fan from
research/target_c_leaf_fan_outerwalk_fork_2026-10-02.md. Let $a$ be their common
diameter carrier, so
$$
|p_j-a|=D
\qquad (j=i-1,i,i+1),
$$
and
$$
|p_{i-1}-p_i|
=
|p_i-p_{i+1}|
=1.
$$

Assume $p_i$ has contact degree three, and let $z$ be its third unit-contact
neighbor.

Then
$$
\boxed{
z\in
\operatorname{int}
\operatorname{conv}
\{a,p_{i-1},p_{i+1}\}.
}
\tag{1}
$$

Consequently $z$ is not an extreme point of the source convex hull. Every actual
diameter endpoint is extreme, so
$$
\boxed{
\deg_H(z)=0.
}
\tag{2}
$$

Thus the "inward spoke" branch of the current fan theorem is not merely deep inside
the carrier circle: every third-contact port is a genuinely diameter-inactive
positive-contact source vertex.

Combined with
research/target_c_global_sqrt_leaf_fan_fork_2026-10-02.md, the low-outer-walk,
square-root-matching branch therefore contains either

- $\Omega(\sqrt D)$ distinct diameter-inactive positive-contact vertices, each
  joined by a unit edge to a loaded diameter leaf; or
- an $\Omega(\sqrt D)$-long exact degree-two stress-flat fan block.

No macroscopic-container conclusion is asserted from the first alternative.

## 2. Exact fan coordinates

Put
$$
p:=p_i,
\qquad
u={p-a\over D},
\qquad
\varepsilon={1\over2D},
\qquad
\tau=\sqrt{1-\varepsilon^2}.
\tag{3}
$$

Choose the unit tangent $t$ so that the two unit fan-contact vectors from the
neighbors toward $p$ are
$$
p-p_{i-1}=\varepsilon u+\tau t,
\qquad
p-p_{i+1}=\varepsilon u-\tau t.
\tag{4}
$$

Hence
$$
p_{i-1}
=
a+(D-\varepsilon)u-\tau t,
\tag{5}
$$
and
$$
p_{i+1}
=
a+(D-\varepsilon)u+\tau t.
\tag{6}
$$

The triangle
$$
\Delta:=
\operatorname{conv}\{a,p_{i-1},p_{i+1}\}
$$
therefore has the exact coordinate description
$$
\Delta
=
\left\{
a+xu+yt:
0\le x\le D-\varepsilon,\quad
|y|\le{\tau x\over D-\varepsilon}
\right\}.
\tag{7}
$$

## 3. The third-contact cone

Let
$$
v:=p-z,
\qquad
|v|=1,
$$
and write
$$
v=ru+st,
\qquad
r^2+s^2=1.
\tag{8}
$$

The current inward-spoke theorem proves
$$
r\ge
c_D:=
{\varepsilon+\sqrt3\,\tau\over2}.
\tag{9}
$$

Therefore
$$
z
=
a+(D-r)u-st.
\tag{10}
$$

For $D>1$, one has $0<\varepsilon<1/2$. Equation (9) gives
$$
r>\varepsilon,
\tag{11}
$$
while $r\le1<D$. Hence
$$
0<D-r<D-\varepsilon.
\tag{12}
$$

It remains only to prove the strict side inequality
$$
|s|
<
{\tau(D-r)\over D-\varepsilon}.
\tag{13}
$$

## 4. Exact factorization of the side inequality

Because $s^2=1-r^2$, inequality (13) is equivalent to
$$
\tau^2(D-r)^2
>
(1-r^2)(D-\varepsilon)^2.
\tag{14}
$$

Using
$$
D={1\over2\varepsilon},
\qquad
\tau^2=1-\varepsilon^2,
$$
the difference factors exactly:
$$
\boxed{
\tau^2(D-r)^2
-
(1-r^2)(D-\varepsilon)^2
=
{(r-\varepsilon)
(r-3\varepsilon+4\varepsilon^3)
\over4\varepsilon^2}.
}
\tag{15}
$$

The first factor is positive by (11). We next show
$$
c_D>3\varepsilon-4\varepsilon^3
\qquad (0<\varepsilon<1/2).
\tag{16}
$$

Indeed (16) is equivalent to
$$
\sqrt3\,\tau
>
5\varepsilon-8\varepsilon^3.
\tag{17}
$$
Both sides are nonnegative on $0<\varepsilon\le1/2$. Squaring gives
$$
\begin{aligned}
3(1-\varepsilon^2)
-
\varepsilon^2(5-8\varepsilon^2)^2
&=
-(2\varepsilon-1)^2
 (2\varepsilon+1)^2
 (4\varepsilon^2-3)\\
&>0
\end{aligned}
\tag{18}
$$
for $0<\varepsilon<1/2$. Thus (17), hence (16), holds strictly.

Since $r\ge c_D$, the second factor in (15) is also positive:
$$
r-3\varepsilon+4\varepsilon^3>0.
\tag{19}
$$

Therefore the left side of (15) is strictly positive, proving (14) and (13).

Combining (12) and (13) with the coordinate description (7) gives
$$
z\in\operatorname{int}\Delta.
$$
This proves (1).

## 5. Diameter inactivity

The three vertices
$$
a,p_{i-1},p_{i+1}
$$
are source points distinct from $z$. Since $z$ lies strictly inside their
triangle, $z$ is not an extreme point of the convex hull of the full source.

Every endpoint of an actual diameter is an extreme point. One proof, already used
in the current star-free witness-cell theorem, is strict convexity of squared
distance: if a diameter endpoint were a nontrivial convex combination of two other
source points, its distance to its diameter partner would be strictly less than
$D$.

Hence $z$ cannot be incident with any actual diameter edge:
$$
\deg_H(z)=0.
$$
This proves (2).

Because $pz$ is a positive unit contact, $z$ is nevertheless nonisolated in the
positive-contact graph.

## 6. Global consequence for the square-root fan fork

The global square-root fan theorem gives, for fixed
$$
\nu\le K_\nu\sqrt D,
\qquad
x_B\le K_x\sqrt D,
$$
a constant $c>0$ such that all sufficiently large sources contain either

1. at least $c\sqrt D$ distinct third-contact neighbors; or
2. a degree-two stress-flat fan block of length at least $c\sqrt D$.

By the present theorem, every neighbor in alternative 1 has diameter degree zero.
Therefore the first branch sharpens to
$$
\boxed{
\Omega(\sqrt D)
\text{ distinct positive-contact vertices with }
\deg_H=0.
}
\tag{20}
$$

Each such vertex is connected by an actual unit contact to a diameter leaf
$p_i$, and the preceding inward-spoke theorem additionally gives the carrier-depth
bound
$$
|z-a|\le D-\delta_D,
\qquad
\delta_D\to{\sqrt3\over2}.
\tag{21}
$$

The contact-degree-five lemma in the global fork ensures that distinct fan leaves
cannot collapse this population onto $o(\sqrt D)$ third neighbors.

## 7. Scope and next target

This theorem does not say that the $\Omega(\sqrt D)$ diameter-inactive vertices lie
in one connected inactive chamber, one attachment cell, or one common geometric
chart. It therefore does not by itself enter the macroscopic-container alternative.

What it removes is a structural ambiguity: the spoke-rich branch can no longer hide
its third-contact ports among the loaded/diameter endpoint set.

The next high-value question is whether a square-root population of these
diameter-inactive vertices, each one unit from a loaded diameter leaf and strictly
inside the corresponding three-loaded-vertex triangle, can be charged to the
canonical inactive attachment/interface currency with bounded multiplicity.

**Disposition:** exact proof-only geometry theorem. No computation, numerical
experiment, verifier execution, CI output, or unexecuted certificate code is used.
