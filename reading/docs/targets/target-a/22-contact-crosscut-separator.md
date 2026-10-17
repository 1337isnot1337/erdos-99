> Generated reading edition · [exact source](../../../../docs/targets/target-a/22-contact-crosscut-separator.md) · source SHA-256 `1c7050144616004d8b28561a5ce0bca9e680330de37a0f6c11418095f888db56`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — contact-crosscut Schur separator bound

This addendum continues the actual-response locked branch of Section 169.  A locked
positive-contact component reaches the boundary of the actual response hull.  The
result below converts any simple contact crosscut from that component into an exact
Schur-rank inequality.  It does not assert that the resulting inequality is already
large enough to close Target A.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 170. A geometric crosscut gives an exact Menger bound

Work with the plateau-terminalized response optimum
$$
X^*\subset K^*,
\qquad Z=(\Lambda+v)\cap\operatorname{int}K^*,
\qquad O=Y_{\rm in}\setminus Z,
\tag{170.1}
$$
and the planar radial conflict graph
$$
G\subseteq X^*\times (Z\sqcup O).
\tag{170.2}
$$
Assume `K^*` is full-dimensional.  Choose the lattice translate generically so that,
in addition to the canonical no-distance-equality conditions, no response radial edge
passes through a distinct point of `X^*`.  This excludes only finitely many
codimension-one translation conditions and therefore does not affect the pointwise
survivor argument.

Let
$$
Q=(q_0,q_1,\ldots,q_L)
\tag{170.3}
$$
be a simple unit-contact path in `X^*` such that
$$
q_0,q_L\in\partial K^*,
\qquad
q_1,\ldots,q_{L-1}\in\operatorname{int}K^*,
\tag{170.4}
$$
and the polygonal arc `|Q|` meets `partial K^*` only at its two endpoints.  Thus
`|Q|` is a crosscut of the topological disk `K^*`.  The relative complement
$$
K^*\setminus |Q|
\tag{170.5}
$$
has exactly two connected components; call them `D_L,D_R`.  Each component contains
one of the two open boundary arcs of `partial K^*\setminus{q_0,q_L}`.  In particular,
every point of `K^*\setminus |Q|`, including a point on the hull boundary away from the
crosscut endpoints, belongs to exactly one of `D_L,D_R`.

For a response point `x in X^*`, let `N_Lambda(x)` denote its strict neighborhood in
the response lattice.  Put
$$
R_Q=
\left(\bigcup_{q\in V(Q)}N_\Lambda(q)\right)\cap Y_{\rm in},
\qquad
W_Q=V(Q)\sqcup R_Q.
\tag{170.6}
$$
The two shores are disjoint, so this is a disjoint union.

## 170.1 Removing `W_Q` eliminates every crossing of the crosscut

> **Lemma 170.1 (crosscut shielding).**  No response edge of `G-W_Q` intersects
> `|Q|`.  Consequently every connected component of the induced graph on
> 

$$

> (X^*\sqcup Z)\setminus W_Q
> \tag{170.7}
> 
$$


> lies entirely in `D_L` or entirely in `D_R`.

### Proof

Let `xy` be a response edge not incident with `W_Q`, where `x in X^*` and
`y in Z sqcup O`.  By the strengthened genericity assumption it cannot pass through a
crosscut vertex distinct from `x`.  If `x in V(Q)` then the edge is incident with
`W_Q`, contrary to assumption.

Suppose `xy` nevertheless meets the relative interior of a unit contact edge
`q_iq_{i+1}`.  If the intersection point is the right endpoint `y`, then `y` lies in
the open segment between `q_i` and `q_{i+1}` and hence
$$
|y-q_i|<1,
\qquad |y-q_{i+1}|<1.
\tag{170.8}
$$
Thus `y in R_Q`, contradiction.

The two segments cannot overlap collinearly in a nontrivial interval.  Indeed, because
`x` is distinct from `q_i,q_{i+1}`, unit separation gives
$$
|x-q_i|\ge1,
\qquad |x-q_{i+1}|\ge1.
\tag{170.9}
$$
A collinear segment from `x` of length `|x-y|<1` therefore cannot reach the relative
interior of the unit segment `q_iq_{i+1}`.  Hence every remaining intersection is a
proper crossing.  Lemma 169.5 then gives
$$
|y-q_i|<1
\quad\text{or}\quad
|y-q_{i+1}|<1,
\tag{170.10}
$$
so again `y in R_Q subset W_Q`, a contradiction.  Thus no surviving response edge
meets the crosscut.

Every edge with both endpoints in `K^*` is contained in `K^*` by convexity.  A path in
the induced graph on `X^* sqcup Z` therefore cannot pass from `D_L` to `D_R` without
meeting the crosscut.  The first assertion excludes that possibility.  $\square$

Because a generic response point has at most four strict lattice neighbors,
$$
\boxed{|R_Q|\le4|V(Q)|,
\qquad |W_Q|\le5|V(Q)|.}
\tag{170.11}
$$
More precisely,
$$
\boxed{
|W_Q\setminus C^\partial|
=|R_Q|+|V(Q)\setminus C^\partial|
\le4|V(Q)|+|V(Q)\setminus C^\partial|.
}
\tag{170.12}
$$

## 170.2 Side decomposition of terminals and exterior sinks

Delete `W_Q`.  For `sigma in {L,R}` define
$$
C_\sigma
=
\{c\in C^\partial\setminus W_Q:c\in D_\sigma\}.
\tag{170.13}
$$
For an exterior right vertex `o in O\setminus W_Q`, put `o in O_sigma` when `o`
has at least one surviving response neighbor `x in X^*\setminus W_Q` belonging to
`D_sigma`.  Thus an exterior vertex may belong to both `O_L` and `O_R`; allowing this
overlap only weakens the upper bound below.

Recall the Section-113 orientation determined by a `Z`-perfect basis matching.  Every
directed `C^partial-to-O` path has all of its vertices except its final `O` endpoint in
`X^* sqcup Z`.

> **Theorem 170.2 (contact-crosscut Menger bound).**  The Schur rank satisfies
> 

$$

> \boxed{
> \operatorname{rank}S
> \le
> |W_Q|
> +\min\{|C_L|,|O_L|\}
> +\min\{|C_R|,|O_R|\}.
> }
> \tag{170.14}
> 
$$


> Consequently the terminal vertices of the shield cancel exactly from the nullity
> loss:
> 

$$

> \boxed{
> \zeta=\dim\ker S
> \ge
> \max\{0,|C_L|-|O_L|\}
> +\max\{0,|C_R|-|O_R|\}
> -|W_Q\setminus C^\partial|.
> }
> \tag{170.15}
> 
$$


> Hence
> 

$$

> \boxed{
> \zeta
> \ge
> \max\{0,|C_L|-|O_L|\}
> +\max\{0,|C_R|-|O_R|\}
> -4|V(Q)|-|V(Q)\setminus C^\partial|.
> }
> \tag{170.16}
> 
$$


> The earlier crude `5|V(Q)|` loss is recovered by discarding the information that
> some crosscut vertices may themselves be Schur terminals.

### Proof

Take a maximum family `mathcal P` of pairwise vertex-disjoint directed
`C^partial-to-O` paths.  By Theorem 113.1,
$$
|\mathcal P|=\operatorname{rank}S.
\tag{170.17}
$$
At most `|W_Q|` paths of `mathcal P` contain a vertex of `W_Q`, because the paths are
vertex-disjoint.  Delete those paths.

Every remaining path avoids `W_Q`.  Its initial terminal belongs to
`K^*\setminus |Q|`, so by the relative crosscut decomposition it lies in exactly one
of `C_L,C_R`; this includes terminals on either hull-boundary arc.  By Lemma 170.1 all
of its vertices before the final exterior endpoint remain in the same component
`D_L` or `D_R`.  Hence a path starting in `C_L` ends at a vertex of `O_L`, and a path
starting in `C_R` ends at a vertex of `O_R`.  Vertex-disjointness makes both the
initial terminals and the exterior endpoints distinct.  Therefore at most
$$
\min\{|C_L|,|O_L|\}
\tag{170.18}
$$
remaining paths start on the left and at most the analogous minimum start on the
right.  Adding the at most `|W_Q|` deleted paths proves (170.14).

Now the left-shore terminal set is partitioned exactly as
$$
C^\partial
=
(C^\partial\cap W_Q)\sqcup C_L\sqcup C_R.
\tag{170.19}
$$
Subtract (170.14) from its cardinality:
$$
\begin{aligned}
\zeta
&\ge |C^\partial\cap W_Q|+|C_L|+|C_R|-|W_Q|\\
&\quad-\min\{|C_L|,|O_L|\}
      -\min\{|C_R|,|O_R|\}\\
&=
\max\{0,|C_L|-|O_L|\}
+
\max\{0,|C_R|-|O_R|\}
-
\bigl(|W_Q|-|C^\partial\cap W_Q|\bigr)\\
&=
\max\{0,|C_L|-|O_L|\}
+
\max\{0,|C_R|-|O_R|\}
-|W_Q\setminus C^\partial|.
\end{aligned}
\tag{170.20}
$$
This is (170.15), and (170.16) follows from (170.12).  $\square$

## 170.3 Exact closing criterion for the locked branch

Put as usual
$$
s=\Delta_\Lambda-d_{\rm int}.
\tag{170.21}
$$

> **Corollary 170.3 (crosscut-imbalance closure criterion).**  If a locked positive-
> contact component supplies a crosscut `Q` for which
> 

$$

> \boxed{
> \max\{0,|C_L|-|O_L|\}
> +\max\{0,|C_R|-|O_R|\}
> \ge s+|W_Q\setminus C^\partial|,
> }
> \tag{170.22}
> 
$$


> then Target A closes for that configuration.  It is enough to prove
> \[
> \boxed{
> \max\{0,|C_L|-|O_L|\}
> +\max\{0,|C_R|-|O_R|\}
> \ge
> s+4|V(Q)|+|V(Q)\setminus C^\partial|.
> }
> \tag{170.23}

### Proof

Equation (170.15) gives `zeta>=s`, which is exactly the Target A Schur-nullity
criterion.  \(\square\)

The theorem does not assert (170.22).  It isolates the exact quantitative information
still missing from the locked branch: either a sufficiently economical contact
crosscut must separate a positive terminal/exterior-sink imbalance, or several
stress-generated crosscuts must be combined so that the union shielding cost does not
erase the required `s` units.

## 170.4 Relation to the current regressions

This theorem is not a planarity-only argument.  An arbitrary annular planar response
may have full linkage rank; then both side imbalances in (170.15) can vanish.  The
crosscut must come from the globally optimal locked-contact structure of Section 169.
The Section-166 common-neighbor collision also remains compatible: no distinct common
lattice neighbor is assigned to every contact or source edge.

The next exact locked-branch problem is therefore a **locked-crosscut imbalance
theorem**: derive (170.22), or an equivalent multi-crosscut inequality, from the
nonnegative equilibrium stress, the minimum-diameter origin of `X^*`, and the exact
boundary/collar population identities.  A mere existence theorem for a crosscut is no
longer enough.
