> Generated reading edition · [exact source](../../../../docs/targets/target-a/25-contact-shield-sector-hall.md) · source SHA-256 `d922b306d598a062a6e59a0475ae52f234081e6d6fa390c93665bd76f4749e6c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — contact-shield sector Hall theorem

Section 170 converted one locked contact crosscut into a two-side Menger bound.
Sections 171--172 show that the locked stress can supply a larger plane contact
subgraph, including a three-channel fan.  The theorem below treats an arbitrary finite
unit-contact shield at once.  After deleting the shield vertices and their lattice
neighbors, every surviving response path is trapped in one component of the geometric
complement.  A finite coarse Hall problem between those components and the exterior
response sinks then gives an exact Schur-nullity lower bound.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 173. Sector Hall deficiency behind a contact shield

Use the plateau-terminalized response notation
$$
G\subseteq X^*\times(Z\sqcup O),
\qquad
Z=(\Lambda+v)\cap\operatorname{int}K^*,
\tag{173.1}
$$
with Schur terminal set `C^partial subset X^*` and
$$
\operatorname{rank}S
=\lambda(C^\partial,O).
\tag{173.2}
$$
Assume `K^*` is full-dimensional and choose the response phase generically as in
Section 170, so no response radial edge passes through a distinct point of `X^*`.

Let `Sigma` be any finite subgraph of the unit-contact graph of `X^*`.  Its straight-
line realization is plane because disjoint unit-contact edges cannot cross.  Write
`|Sigma|` for its polygonal realization and let
$$
D_1,\ldots,D_k
\tag{173.3}
$$
be the connected components of the relative complement
$$
K^*\setminus|\Sigma|.
\tag{173.4}
$$
Components with no response vertices are allowed.

Put
$$
R_\Sigma
=
\left(\bigcup_{q\in V(\Sigma)}N_\Lambda(q)\right)\cap Y_{\rm in},
\qquad
W_\Sigma=V(\Sigma)\sqcup R_\Sigma.
\tag{173.5}
$$

## 173.1 Geometric shielding

> **Lemma 173.1 (finite contact shield).**  No response edge of `G-W_Sigma`
> intersects `|Sigma|`.  Consequently every connected component of the induced graph
> on
> 

$$

> (X^*\sqcup Z)\setminus W_\Sigma
> \tag{173.6}
> 
$$


> is contained in one geometric component `D_i`.

### Proof

Let `xy` be a response edge not incident with `W_Sigma`, with `x in X^*` and
`y in Z sqcup O`.  It cannot pass through a shield vertex distinct from `x` by the
genericity assumption, while `x in V(Sigma)` would itself make the edge incident with
the shield.

Suppose `xy` meets the relative interior of a shield contact edge `pq`.  If the
intersection is the right endpoint `y`, then `y` lies in the open unit segment `pq`,
so
$$
|y-p|<1,
\qquad |y-q|<1,
\tag{173.7}
$$
and `y in R_Sigma`, contradiction.

A nontrivial collinear overlap is impossible.  Since `x` is distinct from `p,q`, unit
separation gives `|x-p|,|x-q|>=1`; a segment of length `|x-y|<1` starting at `x`
cannot reach the relative interior of `pq` along the same line.  Hence every remaining
intersection is proper.  Lemma 169.5 then gives
$$
|y-p|<1
\quad\text{or}\quad
|y-q|<1,
\tag{173.8}
$$
again putting `y` in `R_Sigma`.  Thus no surviving response edge meets the shield.

Every edge whose endpoints lie in `K^*` is contained in `K^*` by convexity.  Therefore
a path in the induced `X^* sqcup Z` graph cannot pass between different components of
`K^*\setminus|Sigma|` without intersecting the shield.  $\square$

As before, every generic response point has at most four strict lattice neighbors, so
$$
\boxed{
|R_\Sigma|\le4|V(\Sigma)|,
}
\tag{173.9}
$$
and
$$
\boxed{
|W_\Sigma\setminus C^\partial|
\le4|V(\Sigma)|+|V(\Sigma)\setminus C^\partial|.
}
\tag{173.10}
$$

## 173.2 The coarse sector-sink graph

For each component `D_i`, put
$$
C_i
=
\{c\in C^\partial\setminus W_\Sigma:c\in D_i\}.
\tag{173.11}
$$
For each exterior response vertex `o in O\setminus W_Sigma`, define its sector set
$$
I(o)
=
\{i:\text{some surviving response edge }xo
\text{ has }x\in D_i\}.
\tag{173.12}
$$
Equivalently, put
$$
O_i=\{o\in O\setminus W_\Sigma:i\in I(o)\}.
\tag{173.13}
$$
One exterior sink may belong to several `O_i`; this is precisely the overlap that the
single-crosscut estimate of Section 170 treated only by a weaker separate count.

Construct a finite bipartite **coarse sector graph** `H_Sigma` as follows.  The right
shore is `O\setminus W_Sigma`.  The left shore contains `|C_i|` abstract copies of
sector `i`, and every such copy is adjacent to every vertex of `O_i`.  Let
$$
\nu_\Sigma
\tag{173.14}
$$
be its maximum matching size and define
$$
\delta_\Sigma
=
\sum_{i=1}^k|C_i|-\nu_\Sigma.
\tag{173.15}
$$
Hall's deficiency formula gives the explicit expression
$$
\boxed{
\delta_\Sigma
=
\max_{J\subseteq\{1,\ldots,k\}}
\left(
\sum_{i\in J}|C_i|
-
\left|\bigcup_{i\in J}O_i\right|
\right)_+.
}
\tag{173.16}
$$

## 173.3 Exact Schur-nullity bound

> **Theorem 173.2 (contact-shield sector Hall bound).**  For every finite unit-contact
> shield `Sigma`,
> 

$$

> \boxed{
> \operatorname{rank}S
> \le
> |W_\Sigma|+
u_\Sigma.
> }
> \tag{173.17}
> 
$$


> Consequently
> 

$$

> \boxed{
> \zeta=\dim\ker S
> \ge
> \delta_\Sigma-|W_\Sigma\setminus C^\partial|.
> }
> \tag{173.18}
> 
$$


> In particular,
> 

$$

> \boxed{
> \zeta
> \ge
> \delta_\Sigma
> -4|V(\Sigma)|-|V(\Sigma)\setminus C^\partial|.
> }
> \tag{173.19}

### Proof

Take a maximum family `mathcal P` of pairwise vertex-disjoint directed
`C^partial-to-O` response paths.  At most `|W_Sigma|` paths meet the shield vertex set;
delete them.

Every remaining path begins at a terminal in exactly one `C_i`.  By Lemma 173.1 all
of its vertices before the final exterior sink remain in the corresponding component
`D_i`.  Its final sink therefore lies in `O_i`.  Distinct response paths have distinct
initial terminals and distinct exterior sinks.  Mapping each path to its sector index
and final sink therefore gives a matching in the coarse graph `H_Sigma`.  Hence at
most `nu_Sigma` shield-avoiding paths remain, proving (173.17).

Every Schur terminal outside the shield lies in exactly one complement component, so
\[
C^\partial
=
(C^\partial\cap W_\Sigma)
\sqcup\bigsqcup_{i=1}^kC_i.
\tag{173.20}
$$
Subtract (173.17) from `|C^partial|` and use
`nu_Sigma=sum_i|C_i|-delta_Sigma`:
$$
\begin{aligned}
\zeta
&\ge
|C^\partial\cap W_\Sigma|
+
\sum_i|C_i|
-
|W_\Sigma|
-
\nu_\Sigma\\
&=
\delta_\Sigma
-
\bigl(|W_\Sigma|-|C^\partial\cap W_\Sigma|\bigr)\\
&=
\delta_\Sigma-|W_\Sigma\setminus C^\partial|.
\end{aligned}
\tag{173.21}
$$
This proves (173.18), and (173.19) follows from (173.10).  $\square$

## 173.4 Locked-stress fan specialization

Assume all three locked-triangle vertices are interior to `K^*`.  Corollary 172.3
supplies three vertex-disjoint positive-contact spokes from the triangle to three
distinct boundary reaction vertices.  Let `Sigma_*` be the union of those spokes and
the three triangle edges.  Its plane realization separates the response hull into
three outer sectors plus the bounded interior of the unit triangle.  The latter contains
no point of `X^*` other than its boundary vertices by unit separation, and every lattice
site in its interior is a strict neighbor of the triangle vertices and therefore lies
in `R_{Sigma_*}`.  Thus it contributes no surviving response path.

Theorem 173.2 therefore reduces the entire locked interior-triangle branch to a
three-sector Hall quantity
$$
\boxed{
\delta_{\rm fan}
=
\max_{J\subseteq\{1,2,3\}}
\left(
\sum_{i\in J}|C_i|
-
\left|\bigcup_{i\in J}O_i\right|
\right)_+,
}
\tag{173.22}
$$
with
$$
\boxed{
\zeta
\ge
\delta_{\rm fan}
-|W_{\Sigma_*}\setminus C^\partial|.
}
\tag{173.23}
$$
This automatically counts an exterior sink only once even when that sink is adjacent
to more than one sector.

For locked triangles meeting the hull boundary, use any shield formed from the proper
crosscut(s) supplied by Sections 171--172; the general theorem remains unchanged even
when the complement has only two relevant sectors.

## 173.5 Exact closing criterion

With
$$
s=\Delta_\Lambda-d_{\rm int},
\tag{173.24}
$$
Target A closes whenever a stress-generated contact shield satisfies
$$
\boxed{
\delta_\Sigma
\ge
s+|W_\Sigma\setminus C^\partial|.
}
\tag{173.25}
$$
Thus the remaining locked-branch theorem is now a finite **sector Hall imbalance**
statement.  The qualitative topology is no longer missing: Sections 169--172 provide
the response-boundary stress support and contact shields, while Theorem 173.2 converts
any such shield into the exact Schur quantity.  What is not yet proved is the
quantitative inequality (173.25) from global minimum-diameter geometry.
