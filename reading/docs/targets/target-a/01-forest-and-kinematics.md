> Generated reading edition · [exact source](../../../../docs/targets/target-a/01-forest-and-kinematics.md) · source SHA-256 `53adf786af862e93ccc4d2463ed2ec5120ee482c592f21375c685bde8fed31e5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A: forest and component kinematics

> Canonical v1.7.0 route module. The original section numbering is preserved for
> cross-references; see the [route map](../README.md).

# 46. Target A: flexible bridge-forest branch

The hybrid normal form from Sections 12 and 18 remains valid. There is a fixed
contact-minimal pinned-jammed core $`K`$; every contact edge outside it is a bridge,
and after contraction the residue is a forest. If

```math
\ell=\dim\mathcal L_{\widehat Q}
```

is the pinned contact-preserving lineality, then

```math
|V(\widehat A)\setminus V(K)|
\le
\ell+2|\widehat Q|.
```

Since $`|\widehat Q|=O(D)`$, the case $`\ell=O(D)`$ already leaves an
$`n-O(D)`$ jammed almost-rhombic core. The genuinely separate obstruction is

```math
\boxed{\ell=\omega(D).}
\tag{46.1}
```

The post-synthesis train-Hessian work does **not** eliminate this branch. These
forest modes are already actual first-order contact-preserving motions with the
relevant pinned roots fixed. Plain Oler area accounting also cannot see the excess
lineality because outside vertices receive the same bulk allowance on both sides of
the topology-corrected shell identity.

The still-open theorem is:

> **Super-boundary forest-capacity theorem.** No sufficiently large triangle-free
> global minimizer in the hybrid normal form has
> $`\ell=\omega(D)`$.

A successful proof must use a global occupancy/configuration-space mechanism, or a
unified shell-rank principle that charges independent forest motions to the same
finite diametral/fault resources used by Target B.

---

# 47. Regression models and routes that the final proof must survive

The complete regression suite is now:

1. **unit square:** triangle-free exact global minimizer, zero-cone branch;
2. **regular unit pentagon and the small exact cases:** diameter-loaded polygon
   corners defeat naive low-degree movement claims;
3. **$`n=8`$ heptagon plus center:** triangle-free global minimizer with a rattler;
4. **regular odd-prime unit polygons:** arbitrarily large triangle-free strict local
   diameter minima;
5. **dense regular-shell fillings:** asymptotically optimal density, exact stress,
   local diameter optimality, but no global certificate;
6. **five-sector $`C_5`$-blowup rhombic complexes:** strict near-equilateral rhombi,
   positive pinned stress and zero pinned cone, but non-diametral/nonextreme pins;
7. **11-point sun:** true diametral hull and local pinning but explicit global
   suboptimality;
8. **disk-clipped near-$`60^\circ`$ oblique grids:** near-disk rhombic bulk showing
   that no uniform density gap or naive angular-collapse argument can work;
9. **near-equilateral pentagonal/triangular pocket degenerations:** local Oler slack
   can approach zero;
10. **disk chord systems:** quadratic raw support depth is normal and therefore not a
    contradiction currency;
11. **parallel tangent quartic class:** one diameter bar can block linearly many
    paired modes at fourth order.

Dead routes remain:

- uniform triangle-free density gaps;
- eventual lattice classification;
- raw contact counts or Laman counts;
- degeneracy alone;
- KKT or positive stress alone;
- a fixed universal prestress Hessian;
- affine shear alone;
- angular defect quantization;
- raw support depth converted directly to Oler surplus;
- arbitrary dense-graph biclique extraction;
- counting one higher-order mode per diameter bar;
- assuming a same-diameter local family is already a diameter decrease.

---

# 48. Version 1.1.0 continuation audit and notation

**LEVEL I STATUS: STILL OPEN.**

The continuation after v1.0.0 produces a sharper normal form for the two remaining
branches but does not prove either final capacity theorem.  The central change is
that the macroscopic higher-order train obstruction is no longer an undifferentiated
mixture of backward and tangent effects.  After minimal-face reduction, visible
tangent transport has only constant-dimensional freedom; any large residual freedom
is forced into strict-backward/Dirichlet rank or into a genuine same-diameter optimal
flat.

Throughout Sections 48--57 we retain the pure simply connected strict-rhombic-disk
notation

```math
V=\mathbb R^T/\langle\mathbf1\rangle,
\qquad
\mathcal L=\bigcap_{h\in H}\ker g_h,
\qquad
K=\ker\mathcal B\subseteq\mathcal L.
\tag{48.1}
```

The v1.0.0 quantitative stack gives

```math
G+E<c_0B,
\qquad
\dim\mathcal L\ge T-q,
\tag{48.2}
```

and

```math
\boxed{
\frac{T-q}{D}
\ge0.3338292869\ldots-o(1).
}
\tag{48.3}
```

Thus any residual higher-order mechanism is macroscopic unless it is compressed by
the structure proved below.

The exact pure-disk contradiction gate remains

```math
\boxed{G+E\ge c_0B.}
\tag{48.4}
```

For topology-corrected rhombic complexes the exact window remains

```math
c_0(B-P)+a_0(t+\chi-1)
\le G_{\mathcal R}+E_{\mathcal R}
<c_0B+a_0(t+\chi-1).
\tag{48.5}
```

No result below silently absorbs an uncontrolled $`O(D)`$ topology error into the
one-integer pure-disk rank contradiction.

---

# 49. Minimal-face harmonic--Dirichlet reduction

Assume $`K\ne0`$, and lift it to

```math
\widetilde K=\{x\in\mathbb R^T:[x]\in K\},
\qquad
\dim\widetilde K=\dim K+1.
\tag{49.1}
```

For an active diameter bar $`h`$, write

```math
s_h(x)=\frac1{D^2}\sum_\tau\lambda_{h\tau}x_\tau.
\tag{49.2}
```

Let

```math
E_0=\{h:H_h|_K\equiv0\}.
\tag{49.3}
```

The signed-variance theorem makes every $`H_h|_K`$ negative semidefinite.  If
$`h\notin E_0`$, its equality set in $`K`$ is a proper subspace.  Choosing a vector
outside the finite union of these subspaces and applying the secondary-cusp theorem
gives

```math
0\in\operatorname{conv}\{g_h:h\in E_0\}.
\tag{49.4}
```

Let $`F`$ be the minimal face of this convex hull containing $`0`$, and put

```math
S=\{h\in E_0:g_h\in F\}.
\tag{49.5}
```

Then there are coefficients

```math
\beta_h>0\quad(h\in S),
\qquad
\sum_{h\in S}\beta_hg_h=0.
\tag{49.6}
```

Define the $`S`$-invisible train set

```math
\mathcal I=\{\tau:d_{h\tau}=0\text{ for every }h\in S\},
\qquad I=|\mathcal I|.
\tag{49.7}
```

Let $`m`$ be the number of distinct functionals
$`s_h|_{\widetilde K}`$, $`h\in S`$.

## 49.1 Visible coordinates factor through bar potentials

For $`h\in S`$, equality of the signed-variance formula on $`K`$ gives

```math
x_\tau=s_h(x)
\qquad
(d_{h\tau}\ne0,\ \lambda_{h\tau}\ne0,
\ x\in\widetilde K).
\tag{49.8}
```

If $`d_{h\tau}\ne0`$, $`\lambda_{h\tau}=0`$, and the coordinate functional
$`x_\tau`$ is not identically $`s_h`$, then the $`\tau`$-coordinate of $`g_h`$
has magnitude $`D`$.  Taking the $`\tau`$-coordinate in (49.6) supplies another
$`k\in S`$ with $`(g_k)_\tau\ne0`$.  Two distinct active diameter segments cannot
have the same unoriented direction; hence $`k`$ is non-tangent to $`\tau`$, and
(49.8) gives

```math
x_\tau=s_k(x).
\tag{49.9}
```

Therefore every $`S`$-visible train coordinate factors through one of the $`m`$
bar-potential functionals.

Choose representatives $`h_1,\dots,h_m`$, and put

```math
N_j=\{\tau:d_{h_j\tau}\ne0,\ \lambda_{h_j\tau}\ne0\}.
\tag{49.10}
```

If a train belonged to both $`N_i`$ and $`N_j`$, then (49.8) would make the two
potential functionals equal; thus the sets $`N_j`$ are pairwise disjoint.  Let
$`e_j=r_{h_j}/D`$.  Tangent trains have zero longitudinal projection, so

```math
D=e_j\cdot r_{h_j}
 =\sum_{\tau\in N_j}e_j\cdot a_{h_j\tau}
 \le |N_j|.
\tag{49.11}
```

Hence

```math
\boxed{mD\le T-I.}
\tag{49.12}
```

Recording the $`I`$ invisible coordinates and the $`m`$ potential values gives an
injective linear map

```math
\widetilde K\longrightarrow
\mathbb R^{\mathcal I}\oplus\mathbb R^m,
\tag{49.13}
```

so

```math
\boxed{
\dim K+1\le I+m
\le I+\left\lfloor\frac{T-I}{D}\right\rfloor.
}
\tag{49.14}
```

Pinned rigidity already gives $`T\le2q-2`$, while $`q\le P\le\pi D`$.  Thus

```math
T\le2\pi D-2,
\qquad
\boxed{m\le6.}
\tag{49.15}
```

In particular,

```math
\boxed{\dim K\le I+5,}
\tag{49.16}
```

or equivalently

```math
\boxed{
\operatorname{rank}\mathcal B+I
\ge\dim\mathcal L-5
\ge0.3338292869\ldots D-o(D)-5.
}
\tag{49.17}
```

This is the first constant-dimensional compression of the residual tangent/equality
branch.

---

# 50. Ordered tangent collapse, harmonic transport, and peripheral duality

## 50.1 Sign coherence of a tangent family

Fix an active diameter bar $`h`$, and let $`e_h=r_h/D`$.  All trains tangent to
$`h`$ are parallel crosscuts perpendicular to $`r_h`$.  Orient their common train
vector consistently.  Their crosscuts are nested, and because each separates the two
endpoints of $`h`$, the endpoint-side relation cannot reverse between two nested
crosscuts.  Hence there is one sign $`\sigma_h\in\{\pm1\}`$ such that

```math
\boxed{
a_{h\tau}=d_{h\tau}u_\tau=\sigma_hJe_h
}
\tag{50.1}
```

for every tangent train $`\tau`$ of $`h`$.

Suppose a bar in potential class $`j`$ has tangent trains $`\mathcal T_h`$, and let
$`c(\tau)`$ denote the potential class transported by $`\tau`$.  First-order
neutrality, together with (50.1), gives the exact positive averaging law

```math
\boxed{
s_j=\frac1{t_h}\sum_{\tau\in\mathcal T_h}s_{c(\tau)},
\qquad t_h=|\mathcal T_h|>0.
}
\tag{50.2}
```

## 50.2 Terminal potential classes

Construct the directed graph of potential classes by directing $`j`$ to every class
transported by a tangent train of a bar in class $`j`$.  The scalar maximum principle
applied to (50.2) shows that a terminal strongly connected component cannot contain
two distinct potential functionals.  Thus every terminal component is one potential
class, and every transient potential is a convex combination of terminal potentials.

Let $`r`$ be the number of terminal potential classes.  Recording the $`I`$
invisible coordinates and the $`r`$ terminal potentials determines every train
coordinate on $`\widetilde K`$, so

```math
\boxed{\dim K+1\le I+r.}
\tag{50.3}
```

For a terminal representative $`h_j`$, every train separating its endpoints has
coordinate functional $`s_j`$; an extremal terminal potential cannot have a moving
tangent train, because a positive average equals an extremum only when all entries
equal that extremum.  Distinct terminal classes therefore have disjoint complete
separator sets $`\Sigma_{h_j}`$.  The triangle inequality gives

```math
D=|r_{h_j}|
\le\sum_{\tau\in\Sigma_{h_j}}|a_{h_j\tau}|
=|\Sigma_{h_j}|.
\tag{50.4}
```

Hence

```math
\boxed{
rD\le T-I,
\qquad
r\le6.
}
\tag{50.5}
```

The visible tangent obstruction has at most

```math
\boxed{r-1\le5}
\tag{50.6}
```

non-rotational potential degrees of freedom.

If $`r\ge2`$, two disjoint terminal cuts have at least $`D^2`$ cross pairs.  Since
only

```math
R=\frac{\pi}{2\sqrt3}D^2+o(D^2)
\tag{50.7}
```

pairs cross in rhombi, the two cuts contain at least

```math
\boxed{
\left(1-\frac{\pi}{2\sqrt3}\right)D^2-o(D^2)
=0.093100317882891\ldots D^2-o(D^2)
}
\tag{50.8}
```

noncrossing pairs.  This is a structural resource, not by itself Oler surplus.

## 50.3 Tangent cubic/quartic trichotomy under sign coherence

After subtracting the common bar rotation, put

```math
w_\tau=x_\tau-s_h(x),
\qquad
S_m=\sum_\tau\sigma_{h\tau}w_\tau^m.
\tag{50.9}
```

The exact expansion from v1.0.0 is

```math
\begin{aligned}
|r_h(t)|^2-D^2
={}&\frac D3S_3t^3+\frac{S_2^2}{4}t^4-\frac D{60}S_5t^5\\
&+\left(\frac{S_3^2}{36}-\frac{S_2S_4}{24}\right)t^6+O(t^7).
\end{aligned}
\tag{50.10}
```

Because of (50.1),

```math
\boxed{S_2=\sigma_h\sum_\tau w_\tau^2.}
\tag{50.11}
```

Therefore:

1. $`S_3\ne0`$ is one-sided at cubic order;
2. $`S_3=0`$, $`S_2\ne0`$ is a genuine positive two-sided quartic blocker;
3. $`S_2=0`$ forces every tangent deviation to vanish.

Thus there is no higher straight-line tangent branch once the ordered minimal-face
sign coherence is imposed.  Curved paths and changes of active face still require
the facial analysis below.

## 50.4 Dirichlet-boundary theorem

For $`\tau`$, let

```math
p_\tau=x_\tau|_{\widetilde K}\in\widetilde K^*,
\qquad
\mathscr P=\operatorname{conv}\{p_\tau:\tau\text{ a train}\}.
\tag{50.12}
```

All coordinate functionals take value $`1`$ on common rotation and span
$`\widetilde K^*`$, so

```math
\dim\operatorname{aff}\mathscr P=\dim K.
\tag{50.13}
```

Call a vertex class of $`\mathscr P`$ **free** if every train in it is
$`S`$-invisible and no train in it is backward for any active diameter bar.

For a backward incidence, the exact positive averaging identity on $`K`$ is

```math
\boxed{
p_\tau
=\sum_{\lambda_{h\sigma}>0}
\frac{\lambda_{h\sigma}}{\Lambda_h^+}p_\sigma,
\qquad
\Lambda_h^+\ge D^2.
}
\tag{50.14}
```

Since $`\lambda_{h\sigma}\le D`$, at least $`D`$ forward trains occur.  If
$`p_\tau`$ is an extreme point of $`\mathscr P`$, extremality forces every
$`p_\sigma`$ in (50.14) to equal $`p_\tau`$; hence a vertex class containing a
backward train contains at least $`D`$ trains.

A visible vertex is a convex combination of terminal potentials and therefore must
itself be terminal.  Its complete terminal separator cut again contributes at least
$`D`$ trains in the same vertex class.  Distinct vertex classes are disjoint.  Thus
at most

```math
\left\lfloor\frac TD\right\rfloor\le6
\tag{50.15}
```

vertex classes are nonfree.

If $`J`$ is the number of free vertex classes, every $`d`$-dimensional polytope has
at least $`d+1`$ vertices, so

```math
\boxed{
J\ge\dim K+1-\left\lfloor\frac TD\right\rfloor
\ge\dim K-5.
}
\tag{50.16}
```

## 50.5 Free trains are peripheral zero-secondary-stress cuts

Take an extreme normalized secondary stress on the minimal face $`S`$.  The
train-by-train balance is

```math
\sum_{h\in S}\beta_hd_{h\tau}r_h=A_\tau u_\tau,
\qquad A_\tau\ge0.
\tag{50.17}
```

If $`\tau`$ is $`S`$-invisible, the left side is zero, hence $`A_\tau=0`$.  Because
$`A_\tau`$ is a sum of nonnegative contact-stress coefficients on the edges of the
train, every such coefficient vanishes.  No supported diameter bar crosses the cut
either.

If positive diameter support lay on both sides, the equilibrium stress would split
into two nonzero proper positive stresses, contradicting extremality.  A side with
contact stress but no diameter stress is also impossible: multiplying its contact-
only equilibrium equations by the vertex positions and summing gives

```math
0=\sum_{ij}\omega_{ij}|p_i-p_j|^2,
\tag{50.18}
```

forcing every nonnegative contact coefficient $`\omega_{ij}`$ to vanish.  Thus all
positive secondary support lies on one side of every free train.  These are genuine
peripheral zero-stress cuts.

## 50.6 Peripheral-dual rank theorem

Let $`M`$ be the number of nonfree vertex classes and
$`\mathcal V_{\rm free}`$ the free vertices of $`\mathscr P`$.  Define

```math
W_{\rm per}
=\operatorname{span}\{p-p':p,p'\in\mathcal V_{\rm free}\}
\subseteq K^*.
\tag{50.19}
```

Adding $`M`$ points to an affine set raises affine dimension by at most $`M`$, hence

```math
\dim K
\le\dim\operatorname{aff}(\mathcal V_{\rm free})+M.
\tag{50.20}
```

The translation space of the free-vertex affine hull is exactly $`W_{\rm per}`$, so

```math
\boxed{
\dim W_{\rm per}\ge\dim K-M\ge\dim K-6.
}
\tag{50.21}
```

Equivalently, with

```math
K_{\rm core}
=\{x\in K:(p-p')(x)=0\ \forall p,p'\in\mathcal V_{\rm free}\},
\tag{50.22}
```

we have

```math
\boxed{\dim K_{\rm core}\le M\le6.}
\tag{50.23}
```

Thus, modulo at most six dimensions, the residual equality kernel is dual-detected
by differences of peripheral backward-free zero-secondary-stress train cuts.

## 50.7 Exact rank consequences

Rank-nullity together with (50.3) gives

```math
\boxed{
\operatorname{rank}\mathcal B+I+r
\ge\dim\mathcal L+1
\ge T-q+1.
}
\tag{50.24}
```

Likewise (50.16) gives

```math
\boxed{
\operatorname{rank}\mathcal B+J
\ge T-q+1-\left\lfloor\frac TD\right\rfloor
\ge T-q-5.
}
\tag{50.25}
```

Asymptotically,

```math
\boxed{
\operatorname{rank}\mathcal B+J
\ge0.3338292869\ldots D-o(D)-5.
}
\tag{50.26}
```

The unreduced $`m`$-potential form also gives a useful quantitative corollary.
From

```math
\operatorname{rank}\mathcal B+I+m\ge T-q+1
\tag{50.27}
```

and $`I\le T-mD`$,

```math
\boxed{
\operatorname{rank}\mathcal B
\ge [m(D-1)-q+1]_+.
}
\tag{50.28}
```

Using $`q\le\pi D+o(D)`$, this yields

```math
\begin{array}{c|c}
m&\operatorname{rank}\mathcal B/D\\\hline
4&\ge0.8584073464\ldots-o(1)\\
5&\ge1.8584073464\ldots-o(1)\\
6&\ge2.8584073464\ldots-o(1).
\end{array}
\tag{50.29}
```

For $`m=6`$,

```math
\boxed{I\le(2\pi-6)D-2
=0.2831853071\ldots D-2.}
\tag{50.30}
```

These are diagnostic bounds; the final theorem still needs ordered geometry rather
than potential count alone.

These inequalities expose the one-integer pure-disk target: a geometric shell upper
bound

```math
\operatorname{rank}\mathcal B+I+r\le T-q
\tag{50.31}
```

would contradict (50.24) immediately.

---

# 51. Terminal direction-network normal form

Let $`z_1,\ldots,z_q`$ be the hull vertices, cyclically ordered, and let $`C_j`$ be
the rhombic-boundary chain from $`z_j`$ to $`z_{j+1}`$.

Construct a multigraph $`\Theta`$ whose vertices are $`C_1,\ldots,C_q`$.  Every train
$`\tau`$ gives an edge joining the two chains containing its terminal boundary
edges.  Orient the train vectors consistently.  The two terminal boundary edges of a
train appear with opposite induced orientations, so there is an oriented incidence
matrix $`\partial`$ such that

```math
\boxed{
z_{j+1}-z_j=\sum_\tau\partial_{j\tau}u_\tau.
}
\tag{51.1}
```

## 51.1 No loops

If both terminal edges of one train belonged to the same chain, their contributions
to every chain vector in (51.1) would cancel.  Rotating that train alone would then
leave every hull-chain displacement unchanged.  After fixing one hull vertex, all
hull vertices would be fixed, while the train-angle motion preserves all contacts to
first order.  Pinned jamming would force the train velocity to vanish, contradiction.
Thus $`\Theta`$ has no loops.

## 51.2 Hull chords are interval cuts

If $`U`$ is a cyclic interval of boundary chains, summing (51.1) over $`j\in U`$
telescopes to the chord joining its endpoints.  Therefore, for an active diameter
bar $`h`$ and either cyclic interval $`U_h`$ between its endpoints,

```math
\boxed{
d_{h\tau}=(\partial^{\mathsf T}\mathbf1_{U_h})_\tau,
\qquad
r_h=\sum_\tau d_{h\tau}u_\tau.
}
\tag{51.2}
```

Thus every active diameter constraint is an interval-cut constraint on the terminal
graph.

## 51.3 Terminal direction map

Define

```math
(\mathcal Dv)_j
=\sum_\tau\partial_{j\tau}Ju_\tau v_\tau.
\tag{51.3}
```

This is the derivative of the chain vector in (51.1).  If $`\mathcal Dv=0`$, all
hull-chain vectors are fixed.  After one translation, all hull vertices are fixed.
The train-angle motion preserves all contacts to first order, so pinned jamming
forces every vertex velocity to vanish.  Along an edge of train $`\tau`$, relative
velocity is $`Ju_\tau v_\tau`$; hence $`v_\tau=0`$.  Therefore

```math
\boxed{\ker\mathcal D=\{0\}.}
\tag{51.4}
```

Every subset of columns is consequently independent.  If a subgraph $`\Theta'`$
has $`V'`$ vertices and $`c(\Theta')`$ nonempty components, its vector-incidence
matrix has two row-sum dependencies per component.  Hence

```math
\boxed{
|E(\Theta')|\le2|V'|-2c(\Theta').
}
\tag{51.5}
```

The scalar incidence matrix has rank $`q-c(\Theta)`$, so its scalar cycle space
satisfies

```math
\boxed{
\dim\ker\partial=T-q+c(\Theta)\ge T-q+1.
}
\tag{51.6}
```

This explains why the same one-integer scale $`T-q+1`$ appears in the blocker rank
lower bound, but it does **not** identify scalar circulations with neutral train-angle
motions.

---

# 52. Terminal-turn theorem and boundary-velocity blocker form

## 52.1 Terminal-turn factorization

Put

```math
C(\Theta)=\ker\partial.
\tag{52.1}
```

For each terminal-chain vertex $`j`$, define

```math
t_j=\dim\operatorname{aff}
\{u_\tau:\partial_{j\tau}\ne0\}\in\{0,1,2\}.
\tag{52.2}
```

For $`z\in C(\Theta)`$, choose an incident reference train $`\rho(j)`$.  Since
$`\sum_\tau\partial_{j\tau}z_\tau=0`$,

```math
\begin{aligned}
(\mathcal Dz)_j
&=\sum_\tau\partial_{j\tau}Ju_\tau z_\tau\\
&=\sum_\tau\partial_{j\tau}
J(u_\tau-u_{\rho(j)})z_\tau.
\end{aligned}
\tag{52.3}
```

Thus the $`j`$-th block lies in a space of dimension at most $`t_j`$.  Since
$`\mathcal D`$ remains injective on $`C(\Theta)`$,

```math
\boxed{
T-q+c(\Theta)
=\operatorname{rank}(\mathcal D|_{C(\Theta)})
\le\sum_{j=1}^qt_j.
}
\tag{52.4}
```

Combining with (48.3),

```math
\boxed{
\sum_jt_j
\ge0.3338292869\ldots D-o(D)+c(\Theta).
}
\tag{52.5}
```

Because $`t_j\le2`$, at least

```math
\boxed{
\frac{T-q+c(\Theta)}2
\ge0.1669146434\ldots D-o(D)
}
\tag{52.6}
```

terminal chains contain a genuine affine direction turn.  Repeated incidences of one
common direction carry no scalar-cycle rank.

## 52.2 Boundary velocity of an active chord

For a train-angle velocity $`x`$, put

```math
y=\mathcal Dx.
\tag{52.7}
```

Summing (51.3) over the interval $`U_h`$ and using (51.2) gives

```math
\boxed{
\dot r_h(x)=\sum_{j\in U_h}y_j.
}
\tag{52.8}
```

Hence

```math
\boxed{
g_h(x)=r_h\cdot\sum_{j\in U_h}y_j.}
\tag{52.9}
```

Moreover,

```math
Jr_h\cdot\dot r_h(x)
=\sum_\tau\lambda_{h\tau}x_\tau,
\tag{52.10}
```

so

```math
\boxed{
s_h(x)=
\frac{Jr_h}{D^2}\cdot\sum_{j\in U_h}y_j.
}
\tag{52.11}
```

On the neutral space $`\mathcal L`$, (52.9) vanishes, so $`\dot r_h\perp r_h`$, and

```math
\boxed{
x\in\mathcal L
\Longrightarrow
\dot r_h(x)=s_h(x)Jr_h.
}
\tag{52.12}
```

Thus $`s_h`$ is exactly the angular velocity of the active diameter chord.

Since $`\mathcal D`$ is injective, the strict-backward row on
$`Y=\operatorname{im}\mathcal D`$ becomes

```math
\boxed{
\ell_{h\tau}(\mathcal D^{-1}y)
=(\mathcal D^{-1}y)_\tau
-
\frac{Jr_h}{D^2}\cdot\sum_{j\in U_h}y_j.
}
\tag{52.13}
```

This inverse-coordinate minus interval-rotation functional is the correct object for
a determinant/matroid analysis of shell capacity.

## 52.3 Rejected cycle-lift inference

The tempting statement

```math
\operatorname{rank}(\mathcal D|_{\ker\partial})
<\dim\ker\partial
\tag{52.14}
```

after "imposing" blocker conditions cannot be obtained by restricting the domain.
Indeed, for every subspace $`W\subseteq\ker\partial`$, injectivity (51.4) gives

```math
\boxed{
\ker(\mathcal D|_W)=0,
\qquad
\operatorname{rank}(\mathcal D|_W)=\dim W.
}
\tag{52.15}
```

Shrinking the domain merely lowers its dimension.  Projecting the codomain can
create a kernel, but such a vector need not satisfy $`\mathcal Dz=0`$ and therefore
is not a pinned flex.  Furthermore,

```math
\ker\partial\not\subseteq\mathcal L,
\qquad
\mathcal L\not\subseteq\ker\partial
\tag{52.16}
```

in general: scalar circulation equations $`\partial z=0`$ and the weighted radial
interval-cut equations $`g_hz=0`$ are different systems.

Accordingly, a valid closing theorem must construct an actual intertwining between
(52.13), the radial-neutral subspace of $`Y`$, and the terminal-turn quotient.  Pure
cycle-space counting is a dead route.

---

# 53. Corrected six-block facial peeling: backward rank or optimal flat

The algebraic peeling mechanism from the continuation is valid, but the earlier
claim that a globally diameter-invisible train is automatically impossible is not
needed and is not promoted.  The correct theorem is the following.

> **Theorem 53.1 (six-block peeling dichotomy).**
> Let $`K=\ker\mathcal B\subseteq\mathcal L`$, $`k=\dim K`$, in a pure simply
> connected strict-rhombic-disk global minimizer.  Then either
>
> 

```math
> k\le5,
> \tag{53.1}
> 
```
>
> or there exists a triangle-free pure-rhombic-disk global minimizer of the same
> diameter $`D`$, arbitrarily close to the original (possibly the original itself),
> whose train-angle realization space contains a local same-$`D`$ manifold of
> dimension at least
>
> 

```math
> \boxed{k-5.}
> \tag{53.2}
> 
```
>
> If the construction reaches a strict-separation stage after at least one face has
> been protected, the nearby minimizer may additionally be chosen with strictly
> fewer active diameter bars.

### Proof

Lift $`K`$ to $`\widetilde K`$, so $`\dim\widetilde K=k+1`$.  At a peeling stage let
$`U`$ be the trains still allowed to vary, $`W\subseteq\mathbb R^U`$ the surviving
subspace, and $`P`$ the already protected active bars satisfying

```math
d_{h\tau}=0
\qquad(h\in P,\ \tau\in U).
\tag{53.3}
```

Thus every bar in $`P`$ is exactly independent of the remaining $`U`$-angle
coordinates.

Let

```math
E_0=\{h:H_h|_W\equiv0\}
\tag{53.4}
```

among the unprotected active bars.  Choose $`v\in W`$ outside the finite union of
proper quadratic equality subspaces, so $`H_h[v,v]<0`$ for every unprotected
$`h\notin E_0`$.

If there is a $`U`$-supported acceleration $`y`$ with

```math
g_h\cdot y<0
\qquad(h\in E_0),
\tag{53.5}
```

then for sufficiently small $`\varepsilon>0`$

```math
\phi(t)=\phi+t v+\frac{\varepsilon t^2}{2}y
\tag{53.6}
```

strictly shortens every unprotected active diameter at order $`t^2`$, while the bars
in $`P`$ remain exactly at $`D`$.  At the first stage $`P=\varnothing`$, this would
contradict the definition of $`D(n)`$.  At a later stage the protected bars keep the
diameter equal to $`D`$, all formerly unprotected active bars acquire strict slack,
and all inactive constraints retain slack for small $`t`$.  Hence the resulting
configuration is another global minimizer, with fewer active diameter bars.  A small
open set of $`U`$-angle variations remains feasible and same-$`D`$, giving a local
optimal manifold of dimension at least $`\dim W`$.

If (53.5) has no solution, finite-dimensional separation gives a nonempty
$`S\subseteq E_0`$ and positive coefficients with

```math
\sum_{h\in S}\beta_hg_h^U=0.
\tag{53.7}
```

The minimal-face factorization from Section 49 applies on $`W`$.  If $`m`$ distinct
nonzero potential functionals occur and $`I\subseteq U`$ is the train set invisible
to all bars in $`S`$, then

```math
mD\le|U\setminus I|.
\tag{53.8}
```

Setting all $`S`$-potentials equal to zero removes at most $`m`$ dimensions and
leaves a subspace $`W'`$ supported on $`I`$:

```math
\dim W'\ge\dim W-m.
\tag{53.9}
```

Replace $`(U,W,P)`$ by $`(I,W',P\cup S)`$ and iterate.  The train sets removed at
different rounds are disjoint, so

```math
D\sum_jm_j\le T.
\tag{53.10}
```

Since $`T<2\pi D`$,

```math
\sum_jm_j\le6.
\tag{53.11}
```

Therefore any terminal surviving subspace has dimension at least

```math
(k+1)-6=k-5.
\tag{53.12}
```

If the iteration terminates because no trains remain, then $`k\le5`$.  Otherwise the
surviving train set $`U`$ is invisible to **every** active diameter bar.  For every
active bar $`h`$, its coefficient vector has $`d_{h\tau}=0`$ for all $`\tau\in U`$,
so its diameter vector is exactly independent of arbitrary $`U`$-angle variations.
All unit rhombus contacts are preserved exactly by the train-angle realization, and
all inactive distance inequalities have a strict margin.  Consequently a sufficiently
small neighborhood in the surviving $`W`$-directions consists of triangle-free
global minimizers of diameter exactly $`D`$.  This is the local same-$`D`$ manifold
in (53.2).  No global-invisible-train impossibility claim is required.  $`\square`$

A direct corollary is the corrected macroscopic alternative

```math
\boxed{
\operatorname{rank}\mathcal B
\ge\dim\mathcal L-5
\ge T-q-5
}
\tag{53.13}
```

**unless a local same-diameter optimal train flat occurs.**  Using (48.3),

```math
\boxed{
\operatorname{rank}\mathcal B
\ge0.3338292869\ldots D-o(D)-5
}
\tag{53.14}
```

unless the pure branch exits into the optimal-flat alternative.

This is the authoritative replacement for the earlier statement that a globally
invisible train must be impossible.

---

# 54. Exact diameter-plateau theorem and Target A optimal flat

> **HISTORICAL FRONTIER NOTE.** Theorem 54.1 remains part of the trusted stack.
> The coarse dimensional bookkeeping in Section 54.2 is retained for provenance but
> is superseded by the exact rooted-forest identity in Section 60 and the rattlerized
> Target A normal form in Sections 62--64.

## 54.1 Diameter plateaus have boundary-order length

> **Theorem 54.1.**  For arbitrary integers $`2\le m<n`$, if
>
> 

```math
> D(m)=D(n)=D,
> \tag{54.1}
> 
```
>
> then
>
> 

```math
> \boxed{n-m<\frac\pi2D.}
> \tag{54.2}
> 
```

### Proof

Apply finite Oler, the isodiametric inequality, and the perimeter-diameter inequality
to an $`n`$-point minimizer:

```math
\begin{aligned}
n-1
&\le\frac2{\sqrt3}\operatorname{area}(K)+\frac12\operatorname{per}(K)\\
&\le\frac2{\sqrt3}\frac{\pi D^2}{4}+\frac{\pi D}{2}\\
&=\frac{D^2}{c}+\frac{\pi D}{2}.
\end{aligned}
\tag{54.3}
```

The strict translated-lattice theorem at $`m`$ gives

```math
D^2=D(m)^2<c(m-1),
\qquad
\frac{D^2}{c}<m-1.
\tag{54.4}
```

Substitution in (54.3) yields

```math
n-1<m-1+\frac{\pi D}{2},
```

which is (54.2).  $`\square`$

Thus an exact plateau of the optimal-diameter sequence cannot have super-boundary
length.

## 54.2 The hybrid forest lineality is an actual optimal flat

Let $`\mathcal L_{\widehat Q}(\widehat A)`$ be the pinned bridge-forest lineality of
dimension $`\ell`$.  For every sufficiently small
$`w\in\mathcal L_{\widehat Q}`$, an old unit contact $`ij`$ satisfies

```math
(p_i-p_j)\cdot(w_i-w_j)=0,
```

so

```math
\boxed{
|p_i+w_i-p_j-w_j|^2
=1+|w_i-w_j|^2\ge1.
}
\tag{54.5}
```

Every active diameter pair has pinned endpoints and therefore remains exactly fixed.
Every inactive inequality retains strict slack in a sufficiently small ball.
Consequently the triangle-free global-minimizer set contains a genuine local affine
ball of dimension $`\ell`$.

Target A is therefore not a missing higher-order rigidity problem.  It is an
**optimal-flat capacity/occupancy problem**.

Let $`u`$ be the number of genuinely moving forest vertices after contracting every
edge fixed throughout the flat.  Since the flat lives in $`2u`$ scalar coordinates,

```math
u\ge\left\lceil\frac\ell2\right\rceil.
\tag{54.6}
```

A particularly strong sufficient bridge would be

```math
\boxed{D(n-u)=D(n).}
\tag{54.7}
```

At the v1.1 stage, Theorem 54.1 combined only with the coarse estimate (54.6), giving

```math
u<\frac\pi2D,
\qquad
\boxed{\ell<\pi D.}
\tag{54.8}
```

**Superseding note.** Theorem 60.1 later proves $`\ell\le u`$. Therefore, under the
same still-unproved deletion-inheritance hypothesis (54.7), the current conditional
conclusion is the stronger

```math
\boxed{\ell\le u<\frac\pi2D.}
\tag{54.8a}
```

Equation (54.8) is retained only as historical v1.1 bookkeeping.

But (54.7) is **not** automatic: deleting the moving vertices leaves a unit-separated
configuration of diameter $`D`$, not necessarily a globally optimal configuration
for cardinality $`n-u`$.  Thus the exact Target A gap is either a proof of
same-diameter deletion inheritance or a direct occupancy/reattachment proof of

```math
\boxed{\ell=O(D).}
\tag{54.9}
```

---

# 55. Ferrers endpoint and ordered shell resources

> **HISTORICAL FRONTIER NOTE.** The Ferrers estimate, terminal resources, and
> phase-atomic inequalities in this section remain trusted. Their v1.1 frontier
> interpretation is superseded by the componentwise decomposition in Sections 65--68.

The shell theorem is now a rank-and-order problem rather than a scalar boundary
count.

## 55.1 Ferrers staircase estimate

Let a Ferrers diagram have row lengths

```math
d_1\ge d_2\ge\cdots\ge d_a,
\qquad d_i\le b,
\tag{55.1}
```

and let

```math
L=\max_i i\,d_i
\tag{55.2}
```

be the largest all-ones Cartesian rectangle.  Since $`d_i\le\min(b,L/i)`$, putting
$`k=\lfloor L/b\rfloor`$ gives

```math
\begin{aligned}
e=\sum_{i=1}^ad_i
&\le kb+\sum_{i=k+1}^a\frac Li\\
&\le L+L\log\frac{ab}{L}+O(a+b).
\end{aligned}
\tag{55.3}
```

Hence

```math
\boxed{
e\le L\left(1+\log\frac{ab}{L}\right)+O(a+b).
}
\tag{55.4}
```

For a tight wall with $`a,b=D+o(D)`$, if no actual Cartesian block of asymptotic
area $`D^2/\sqrt3`$ is present, then

```math
L\le\frac{D^2}{\sqrt3}+o(D^2),
\tag{55.5}
```

and therefore

```math
\boxed{
e\le
\frac{1+\log\sqrt3}{\sqrt3}D^2+o(D^2)
=0.8944923195\ldots D^2+o(D^2).
}
\tag{55.6}
```

The rhombus crossing count is

```math
R=\frac{\pi}{2\sqrt3}D^2+o(D^2)
=0.9068996821\ldots D^2+o(D^2),
\tag{55.7}
```

leaving the positive leading-order gap

```math
\boxed{0.0124073626\ldots D^2+o(D^2).}
\tag{55.8}
```

This becomes a contradiction only after proving that the relevant blocker/crossing
mass is concentrated in one tight ordered wall or in a controlled collection of
walls.  That concentration theorem is open.

## 55.2 Terminal and boundary resources

The v1.0.0 terminal-pair theorem remains in force: every separating train with
$`\lambda_{h\tau}\le0`$ has both terminal edges off the convex hull, and different
trains have different terminal pairs.  The boundary-curvature theorem gives

```math
\boxed{
r_3\ge2(T-q)+4
\ge0.6676585739\ldots D-o(D).
}
\tag{55.9}
```

The terminal-turn theorem adds a rank-sensitive resource:

```math
\sum_jt_j\ge T-q+c(\Theta).
\tag{55.10}
```

Thus repeated equal-direction walls cannot provide unlimited independent scalar
circulation rank.

## 55.3 Phase-atomic bounds: correct logical use

Let $`s`$ be the limiting atomic train mass, $`y=q/T`$, and $`x=T/D`$.  The audited
bounds are

```math
\boxed{s\le1-\frac y2,}
\tag{55.11}
```

```math
\boxed{
\limsup\frac{R}{T^2}
\le\frac14\left(1-\frac y2\right)^2,
}
\tag{55.12}
```

and

```math
\boxed{s\ge\frac{2}{\sqrt c\,x}.}
\tag{55.13}
```

The **combination** of the lower and upper bounds, not (55.11) alone, shows that a
positive fraction of train mass is forced into finitely many near-triangular phase
grains while another controlled fraction remains available for the non-atomic hull
regularization.  Within a coherent grain, same-phase train families are internally
noncrossing and ordered.  This is the geometric setting in which an interval/Ferrers
blocker theorem must be proved.

---

# 56. Exact v1.1.0 remaining lemmas

> **HISTORICAL -- SUPERSEDED FRONTIER.** This section records the v1.1 target.
> Equations (56.1)--(56.2) remain the total pure upper/lower rank targets, but the
> authoritative v1.2 residual budget after isolating component rotations is Section 68.2.
> Target A is superseded by Sections 60--64.

The continuation compresses the Level I problem to the following statements.

## 56.1 Pure ordered blocker--turn coforest lemma

Under the pure strict-rhombic-disk hypotheses and $`G+E<c_0B`$, with the convention
$`I=0,r=1`$ if $`K=0`$, prove

```math
\boxed{
\operatorname{rank}\mathcal B+I+r\le T-q
}
\tag{56.1}
```

unless at least one of the following already occurs:

1. $`G+E\ge c_0B`$;
2. an exact $`60^\circ`$ rhombus occurs;
3. an actual Cartesian block violates the audited global capacity bound;
4. a genuine diameter-decreasing feasible motion exists; or
5. the configuration enters the same-diameter optimal-flat alternative of
   Theorem 53.1.

This would contradict the proved lower bound

```math
\boxed{
\operatorname{rank}\mathcal B+I+r\ge T-q+1.
}
\tag{56.2}
```

The proof must operate on the actual blocker functionals (52.13), the peripheral dual
span (50.21), and the terminal-turn quotient (52.4).  It must **not** invoke the
rejected cycle-lift argument.

The desired combinatorial content is that independent backward rows, peripheral
Dirichlet data, and terminal potential blocks leave at least $`q`$ protected ordered
continuation slots.  Equality should force exact triangular continuation, a zero
phase difference, or an oversized Cartesian block.

## 56.2 Topology-corrected extension

The pure theorem must be transported through the $`O(D)`$ exceptional shell:
nonquadrilateral faces, holes, multiple rhombic components, boundary pinches, and
vertices outside the rhombic core.  Each exception must be represented as a finite-
rank transfer gadget whose rank is charged to the exact topology-corrected shell
residual (48.5).  An uncontrolled $`O(D)`$ rank loss is not sufficient, because the
pure contradiction is a one-integer deficit.

## 56.3 Optimal-flat / bridge-forest capacity theorem

The unified flat branch now contains both:

- the local same-$`D`$ train-angle flat supplied by Theorem 53.1; and
- the hybrid bridge-forest affine flat of Section 54.2.

For the forest branch it is sufficient to prove

```math
\boxed{\ell=O(D),}
\tag{56.3}
```

or the stronger deletion-inheritance statement (54.7).  More ambitiously, prove a
single optimal-flat capacity theorem saying that a triangle-free global minimizer
cannot possess a same-diameter contact-preserving flat of super-boundary dimension
unless its boundary hits an exact triangle event or an independently chargeable
shell obstruction.

This would absorb the train-flat alternative of Target B and Target A into one
mechanism.

---

# 57. Preferred next proof architecture

> **HISTORICAL -- SUPERSEDED STRATEGY.** Retained to document the v1.1 route.
> For current work use the saturated-rattler program of Section 64 and the
> component-quotiented internal blocker program of Sections 67--68.

## 57.1 Work in the boundary-velocity image

Let

```math
Y=\operatorname{im}\mathcal D,
```

and define the radial-neutral subspace

```math
Y_0=
\left\{
y\in Y:
 r_h\cdot\sum_{j\in U_h}y_j=0
 \text{ for every active }h
\right\}.
\tag{57.1}
```

On $`Y_0`$, each backward row is the exact functional

```math
b_{h\tau}(y)
=(\mathcal D^{-1}y)_\tau
-
\frac{Jr_h}{D^2}\cdot\sum_{j\in U_h}y_j.
\tag{57.2}
```

Every peripheral free datum is a difference of coordinate functionals associated to
peripheral zero-stress cuts.

## 57.2 Ordered blocker-to-turn matroid target

At each terminal chain, quotient its incidence data by the common train direction;
the resulting local turn space has dimension $`t_j`$.  Construct an explicit
intertwining map taking:

- independent backward rows;
- peripheral Dirichlet differences; and
- terminal rigid-potential blocks

into ordered turn/coforest slots.  The map must satisfy:

1. repeated use of one staircase wall contributes only its actual independent turns;
2. cycles of wall potentials telescope;
3. a complement of a blocker basis contains at least $`q`$ protected continuation
   slots;
4. equality forces exact triangular continuation or a Cartesian block.

The Ferrers gap (55.8) is the quantitative endpoint if most crossing mass
concentrates in a tight wall.  If the blocker rank spreads across many walls, the
alternative endpoint should be a lower bound on independent terminal turns strong
enough to force the exact shell gate.

## 57.3 Optimal-flat route

For a same-diameter optimal flat, contract every edge fixed throughout the flat and
study the first-event walls of the remaining moving rooted clusters.  Generic-event
selection alone is insufficient because codimension-one triangle walls can bound the
flat.  The desired theorem is instead one of:

1. flat-to-deletion inheritance $`D(n-u)=D(n)`$;
2. an occupancy/free-volume bound giving $`u=O(D)`$;
3. a Dirichlet/turn theorem charging at least one independent shell slot per bounded
   number of flat dimensions.

The exact plateau theorem then turns any genuine same-diameter cardinality
inheritance into an explicit $`O(D)`$ dimension bound.

## 57.4 Routes not to repeat

The following remain dead or superseded:

- pure scalar cycle-space counting;
- interpreting a restriction of injective $`\mathcal D`$ as a new kernel;
- abstract averaging-degree arguments without order;
- tangent incidence counting;
- one active diameter bar per higher-order mode;
- a fixed KKT stress as a universal Hessian certificate;
- raw support depth as Oler currency;
- generic dense-graph biclique extraction;
- generic first-event selection in an optimal flat;
- assuming deletion from an optimal flat preserves optimality;
- the unconditional globally-invisible-train exclusion used in the raw continuation;
- the older two-potential wall theorem as a required dependency.

---

# 58. Version 1.1.0 exact status

> **HISTORICAL STATUS.** This section is the frozen v1.1 status and is superseded
> by the v1.2 status in Section 69.

**LEVEL I STATUS: STILL OPEN.**

The v1.1.0 theorem state sharpens the final architecture substantially.

## Target B — jammed almost-rhombic branch

For the pure disk, the first-order-neutral train space has dimension at least

```math
0.3338292869\ldots D-o(D).
```

The minimal-face and harmonic--Dirichlet theorems show that visible tangent quartic
transport has at most five non-rotational potential degrees, while all but at most
six dimensions of an equality kernel are dual-detected by peripheral zero-stress
cuts.  The terminal direction graph gives an exact interval-cut representation of
active diameter bars and identifies affine direction turns as the scalar terminal
cycle-rank resource.  The corrected facial-peeling theorem yields the macroscopic
dichotomy

```math
\boxed{
\text{macroscopic strict-backward/Dirichlet rank}
\quad\text{or}\quad
\text{macroscopic same-}D\text{ optimal flat}.
}
\tag{58.1}
```

The unresolved pure theorem is the ordered blocker--turn/coforest upper bound
(56.1).  It must then be made topology-correct without losing the exact one-integer
deficit.

## Target A — flexible bridge-forest branch

The bridge-forest lineality is now known to be an actual local affine family of
triangle-free global minimizers.  Exact plateaus of $`D(n)`$ have length
$`<(\pi/2)D`$, but deletion of moving vertices is not known to preserve global
optimality.  The unresolved theorem remains

```math
\boxed{\ell=O(D),}
```

or a stronger optimal-flat inheritance theorem implying it.

## Unified endgame

The most economical Level I proof would establish two compatible capacity facts:

1. an ordered shell cannot carry the macroscopic independent backward/Dirichlet rank
   forced by Target B while $`G+E<c_0B`$; and
2. a triangle-free global minimizer cannot support a same-diameter optimal flat of
   super-boundary dimension.

The first should terminate in the exact shell gate, a $`60^\circ`$ rhombus, or an
oversized Cartesian block.  The second should terminate in the plateau theorem,
occupancy saturation, or an exact triangle wall.

No theorem in v1.1.0 closes both statements, and no infinite family of triangle-free
**global** minimizers is known.  No proof or disproof is claimed.

---

# 59. Version history and provenance

- **v1.0.0 (2026-08-26):** canonical synthesis and second-pass audit through the
  translated-lattice, phase-atomic, first-order cusp, backward-flip, tangent-quartic,
  support-turning, and hybrid-forest reductions.
- **v1.1.0 (2026-08-26):** promotes the audited minimal-face harmonic--Dirichlet,
  peripheral-dual, terminal direction-network/turn, boundary-velocity, exact plateau,
  and optimal-flat results; rejects the cycle-lift shortcut; corrects facial peeling
  to the backward-rank-or-optimal-flat dichotomy.

The only supplied external literature remains:

1. `mp05-2-261-269.pdf`;
2. `1951-03.pdf`;
3. `1-s2.0-S0097316598928898-main.pdf`;
4. `s00454-002-0747-6.pdf`;
5. `1204.4403v1.pdf`;
6. `463.pdf`;
7. `10.1007_PL00009374.pdf`.

No internet source is part of this theorem-state file.

---

# 60. Rooted-forest rank and self-stress theorem

Let $`F`$ be the quotient bridge forest in the hybrid representative.  Let

- $`u`$ be the number of unpinned forest vertices;
- $`r`$ be the number of incident fixed roots;
- $`c`$ be the number of nonempty forest components;
- $`R_F`$ be the pinned contact-equality matrix, with $`2u`$ scalar columns;
- $`\ell=\dim\ker R_F`$ be the pinned contact-preserving lineality; and
- $`\sigma=\dim\ker R_F^{\mathsf T}`$ be the pinned forest self-stress dimension.

Here a self-stress is an unrestricted linear dependence among the forest contact
rows; equilibrium is imposed only in the unpinned columns.

> **Theorem 60.1 (rooted-forest rank/self-stress identity).**
> One has
> 

```math
> \boxed{
> \ell=u-r+c+\sigma,
> \qquad
> 0\le\sigma\le r-c.
> }
> \tag{60.1}
> 
```
> Consequently
> 

```math
> \boxed{
> u-r+c\le\ell\le u,
> \qquad
> 0\le u-\ell=r-c-\sigma\le r-c.
> }
> \tag{60.2}
> 
```
> Since $`r\le |\widehat Q|\le\pi D`$,
> 

```math
> \boxed{0\le u-\ell\le\pi D.}
> \tag{60.3}
> 
```

### Proof

The forest has

```math
e=u+r-c
\tag{60.4}
```

edges.  Every retained edge is incident with an unpinned vertex, so every edge gives
one nonzero row of $`R_F`$.  Since

```math
\operatorname{rank}R_F=e-\sigma,
```

rank-nullity gives

```math
\ell
=2u-(e-\sigma)
=u-r+c+\sigma.
\tag{60.5}
```

It remains to prove $`\operatorname{rank}R_F\ge u`$.  In one tree component with
$`u_i`$ unpinned vertices and $`r_i\ge1`$ fixed roots, delete $`r_i-1`$ edges so that
each resulting component contains exactly one root.  The retained forest has exactly
$`u_i`$ edges.

These $`u_i`$ contact rows are independent.  In every nontrivial one-root tree there
is an unpinned leaf.  The two coordinate columns of that leaf occur in only its unique
incident row, whose contact vector is nonzero.  Hence the coefficient of that row in
any row dependence is zero.  Remove the leaf and iterate.  All coefficients vanish.
Summing over components gives $`u`$ independent rows.  Thus

```math
\sigma=e-\operatorname{rank}R_F
\le (u+r-c)-u=r-c.
```

This proves (60.1)--(60.3). $`\square`$

The estimate is sharp.  A tree with one fixed root has $`e=u`$, $`\sigma=0`$, and
$`\ell=u`$.  Therefore rooted-forest linear algebra alone cannot yield
$`\ell\le\alpha u+O(D)`$ with any $`\alpha<1`$.

The authoritative Target A parameter is henceforth $`u`$, not an abstract lineality:

```math
\boxed{\ell=u-O(D).}
\tag{60.6}
```

A super-boundary hybrid flat is asymptotically one degree of freedom per moving
forest vertex.

---

# 61. Root-skeleton exactification

The affine flat from Section 54.2 is enough for rattlerization, but the hybrid branch
also admits a large genuine exact-unit-bar manifold after paying only boundary-order
contacts.

Let $`S`$ be the minimal subtree of each forest component spanning its fixed roots.
Pin every nonroot vertex of $`S`$ having degree at least three in $`S`$.  Let $`b`$
be the total number of such newly pinned branch vertices.

> **Lemma 61.1 (branch count).**
> 

```math
> \boxed{b\le r-c.}
> \tag{61.1}
> 
```

### Proof

In a tree whose minimal root-spanning subtree has $`r_i`$ root leaves/vertices and
$`b_i`$ nonroot vertices of degree at least three, the usual degree identity
$`\sum_v(\deg v-2)=-2`$ gives $`b_i\le r_i-1`$.  Summing gives
$`b\le r-c`$. $`\square`$

Suppress the remaining degree-two vertices of the root skeleton.  The resulting
forest has

```math
k=r+b-c
\tag{61.2}
```

skeleton paths between roots and/or pinned branch vertices.  Cut one old contact edge
on each such path.

> **Theorem 61.2 (root-skeleton exactification).**
> There is a nearby triangle-free global minimizer of the same diameter carrying a
> smooth exact-contact manifold $`\mathcal M`$ such that
> 

```math
> \boxed{
> \dim\mathcal M=u-b\ge u-r+c,
> }
> \tag{61.3}
> 
```
> while the number of old forest contacts made strict is at most
> 

```math
> \boxed{
> L_{\rm lost}\le r+b-c\le2(r-c).
> }
> \tag{61.4}
> 
```

### Proof

After cutting one edge from each skeleton path, every remaining forest component
contains exactly one fixed vertex: either an original root or a newly pinned branch
vertex.  There are $`u-b`$ unpinned vertices and exactly $`u-b`$ retained forest
edges.

For a one-fixed-root tree, the unit vector of every edge may be chosen independently;
positions are then recovered uniquely by summing edge vectors from the root.  Hence
the abstract bar-realization space is a product of circles and is smooth of dimension
equal to the number of retained edges.  Locally, all previously inactive pair
inequalities remain open conditions.  Thus the retained forest supplies a smooth
$`(u-b)`$-dimensional exact-unit-bar manifold.

It remains to open the cut contacts.  Consider one skeleton path and one of its two
halves.  Let $`A`$ be the fixed special endpoint of the half, $`x=A+v`$ its movable
endpoint at the cut, and $`y`$ the opposite cut endpoint.  Rigidly rotate the entire
half, including all off-skeleton branches attached to it, about $`A`$.  All retained
contacts in that half remain exactly unit.  Put

```math
F(\phi)=|A+R_\phi v-y|^2.
\tag{61.5}
```

At $`\phi=0`$, $`F(0)=1`$, and

```math
F'(0)=2(x-y)\cdot Jv.
\tag{61.6}
```

If this is nonzero, choose the sign of $`\phi`$ for which the cut edge length
increases.  If $`F'(0)=0`$, then $`x-y=\pm v/|v|`$, and

```math
F''(0)=2\bigl(|v|^2\mp|v|\bigr).
\tag{61.7}
```

In the minus-sign case this is positive.  In the plus-sign case, unit separation
between $`A`$ and $`y`$ excludes $`|v|<1`$; equality $`|v|=1`$ would force
$`y=A`$, impossible for the two distinct endpoints of a simple cut path.  Hence
$`F''(0)>0`$ in the only remaining case.

The supports associated with distinct suppressed skeleton paths are disjoint except
at fixed special vertices, so sufficiently small opening rotations may be chosen
simultaneously.  All inactive lower and upper inequalities retain strict slack.
Original diameter pairs have fixed endpoints and remain exactly $`D`$.  The nearby
configuration is therefore another triangle-free global minimizer.  The number of
cut contacts is $`k=r+b-c`$, giving (61.4). $`\square`$

Combining Sections 60 and 61,

```math
\boxed{
\dim\mathcal M\ge u-(r-c)\ge \ell-(r-c)\ge\ell-\pi D.
}
\tag{61.8}
```

The stronger claim that one can always retain a full $`u`$-dimensional exact-bar
manifold is not promoted: a branch junction can be locally caged by several fixed unit
neighbors.  Pinning at most $`r-c`$ such junctions is the sharp safe reduction used
below.

---

# 62. Affine forest factor exclusion and rattlerization

After the root-skeleton reduction, let $`F`$ denote the remaining forest of one-root
components.  Put

```math
v=u-b.
\tag{62.1}
```

Then $`F`$ has exactly $`v`$ unpinned vertices and $`v`$ retained unit edges.
Orient each retained edge away from the unique fixed vertex of its component and
write its unit vector as $`u_e`$.

The pinned first-order contact-preserving space is parametrized by one scalar $`x_e`$
per retained edge:

```math
w_{\operatorname{child}(e)}-w_{\operatorname{parent}(e)}
=x_eJu_e.
\tag{62.2}
```

Because the graph is a one-root forest, this gives a linear isomorphism

```math
\mathbb R^{E(F)}\cong W,
\qquad
\dim W=v.
\tag{62.3}
```

For two labels $`a,b`$, fixed or moving, let

```math
F_{ab}(x)
=
\left|
 p_a-p_b+w_a(x)-w_b(x)
\right|^2-1.
\tag{62.4}
```

For an oriented retained edge $`e`$, let $`T_e`$ be the descendant subtree below
its child endpoint, and define

```math
\eta_e(a)=
\begin{cases}
1,&a\in T_e,\\
0,&a\notin T_e,
\end{cases}
\qquad
\epsilon_e^{ab}=\eta_e(a)-\eta_e(b)\in\{-1,0,1\}.
\tag{62.5a}
```

Every fixed label has $`\eta_e=0`$ for every retained edge. Equivalently, one may
identify all fixed vertices to one abstract super-root; then $`\epsilon_e^{ab}\ne0`$
exactly when the cut defined by $`e`$ separates $`a`$ and $`b`$ in this super-rooted
forest. This convention works whether the labels lie in the same one-root component
or in different components. The rooted path formula gives

```math
w_a-w_b
=
\sum_e\epsilon_e^{ab}x_eJu_e.
\tag{62.5}
```

Hence the coefficient of $`x_e^2`$ in $`F_{ab}`$ is
$`(\epsilon_e^{ab})^2`$. Therefore

```math
\boxed{
F_{ab}\text{ depends on }x_e
\iff
\eta_e(a)\ne\eta_e(b).
}
\tag{62.6}
```

## 62.1 Algebraic triangle-wall lemma

> **Lemma 62.1.**
> Suppose three nonzero real polynomials on $`\mathbb R^v`$ vanish simultaneously on
> a relatively open codimension-one smooth semialgebraic set.  Then their common
> zero set has a height-one real algebraic component; equivalently the three
> polynomials share a nonconstant irreducible factor.

### Proof

The Zariski closure of a real semialgebraic set of dimension $`v-1`$ has algebraic
dimension at least $`v-1`$.  Since the defining polynomials are nonzero, the closure
has a codimension-one irreducible component.  Its prime ideal has height one.  The
polynomial ring over $`\mathbb R`$ is a UFD, so every height-one prime is generated by
one irreducible polynomial.  That generator divides all three polynomials. $`\square`$

> **Theorem 62.2 (affine forest triangle-factor exclusion).**
> Every relatively open codimension-one triangle wall in the affine forest flat has
> an identically unit side.  Moreover that persistent side lies entirely in the fixed
> part: the old core, a fixed diameter vertex, or one of the $`b`$ pinned branch
> junctions.

### Proof

Suppose a codimension-one wall carries a unit triangle $`i,j,k`$, while none of
$`F_{ij},F_{jk},F_{ki}`$ is identically zero on $`W`$.  By Lemma 62.1 they have a
common nonconstant irreducible factor $`P`$.  Choose a variable $`x_e`$ on which
$`P`$ depends.  Degree in one variable is additive under multiplication in a domain,
so every polynomial divisible by $`P`$ depends on $`x_e`$.  By (62.6), edge $`e`$
must separate each of the three pairs

```math
ij,\qquad jk,\qquad ki.
```

But for a fixed descendant set $`T_e`$, membership of the three labels is a
$`0+3`$ or $`1+2`$ bipartition. Thus $`\eta_e`$ differs on either no pair or exactly
two of the three pairs, never all three. Contradiction.

Thus one triangle side is identically unit on $`W`$. If either endpoint of that side
were an unpinned forest vertex, some retained edge has a descendant subtree containing
exactly one endpoint, so (62.6) would give a nonzero quadratic term. Hence both
endpoints are fixed. $`\square`$

This theorem does not contradict the regression that length-two triangle walls on the
exact-bar torus can have rank $`v-O(1)`$.  The theorem concerns the affine straight
forest flat, on which nonfixed old bars open quadratically.

## 62.2 Rattlerization

> **Theorem 62.3 (forest rattlerization).**
> There is a nearby triangle-free global minimizer of the same diameter in which all
> $`v=u-b`$ unpinned vertices of the reduced forest are genuine strict rattlers.
> Denote this strict-rattler set by $`\mathscr R`$. Its vertices have no unit contact,
> no active diameter incidence, and strict slack in every constraint involving them.
> Consequently
> 

```math
> \boxed{
> |\mathscr R|\ge v=u-b\ge u-r+c\ge\ell-(r-c),
> }
> \tag{62.7}
> 
```
> and the local same-$`D`$ minimizer set contains an open ball of dimension at least
> 

```math
> \boxed{
> 2|\mathscr R|\ge2(u-r+c)\ge2\ell-2(r-c).
> }
> \tag{62.8}
> 
```
> In particular, since $`r-c\le\pi D`$,
> 

```math
> \boxed{
> |\mathscr R|\ge\ell-\pi D,
> \qquad
> \dim_{\rm local}\mathcal O_D\ge2\ell-2\pi D.
> }
> \tag{62.9}
> 
```

### Proof

Choose $`x\in\mathbb R^{E(F)}`$ with $`x_e\ne0`$ for every retained edge and let
$`w=w(x)`$.  For sufficiently small nonzero $`t`$, move every unpinned forest vertex
by $`tw_i`$.  For a retained forest edge $`e=ij`$,

```math
p_i(t)-p_j(t)=u_e+t x_eJu_e,
```

so

```math
\boxed{
|p_i(t)-p_j(t)|^2=1+t^2x_e^2>1.
}
\tag{62.10}
```

The contacts cut in Section 61 already have strict slack.  Every other inactive
lower- or upper-distance constraint remains strict for sufficiently small $`t`$.
The unpinned forest vertices are not diameter endpoints; all active diameter pairs
have fixed endpoints and remain exactly $`D`$.  Hence the new configuration is a
triangle-free global minimizer of diameter $`D`$.

Every reduced forest vertex is now strict against every other point.  A sufficiently
small product neighborhood in their $`2v`$ Cartesian coordinates preserves all
inequalities while the fixed diameter pair keeps the diameter equal to $`D`$.  This
proves (62.7)--(62.9). $`\square`$

Thus a surviving super-boundary Target A branch has the much stronger consequence

```math
\boxed{
\ell=\omega(D)
\Longrightarrow
\text{a nearby global minimizer has }\omega(D)
\text{ mutually independent strict rattlers.}
}
\tag{62.11}
```

Target A is no longer a linkage-regularity problem.

---

# 63. Same-diameter saturation and strict replacement

## 63.1 Triangle-free saturation inside the fixed hull

> **Theorem 63.1 (same-diameter saturation).**
> Let $`A`$ be a triangle-free $`n`$-point global minimizer of diameter $`D`$, with
> $`K=\operatorname{conv}A`$.  Then $`A`$ is contained in a triangle-free global
> minimizer $`A^+\subset K`$ of the same diameter satisfying
> 

```math
> \boxed{|A^+\setminus A|<\frac\pi2D,}
> \tag{63.1}
> 
```
> and
> 

```math
> \boxed{
> K\subseteq\bigcup_{p\in A^+}\overline B(p,1).
> }
> \tag{63.2}
> 
```
> If a specified finite subset of $`A`$ consists of strict rattlers, the added points
> may be chosen generically so that those vertices remain non-diametral strict
> rattlers.

### Proof

While there is a point $`y\in K`$ with $`|y-p|>1`$ for every point in the current
set, add such a $`y`$.  It creates no unit contact, hence no triangle.  All points
remain in $`K`$, so their diameter is at most $`D`$; the original diameter pair
remains, so the diameter is exactly $`D`$.  Monotonicity of the optimal-diameter
sequence therefore makes every intermediate configuration globally optimal at its
new cardinality.

The process terminates because a bounded region contains only finitely many mutually
unit-separated points.  At termination (63.2) holds.  If the final cardinality is
$`N`$, then $`D(N)=D(n)=D`$, so Theorem 54.1 gives
$`N-n<(\pi/2)D`$.

At each insertion step the available uncovered set is relatively open in $`K`$.
Avoiding finitely many diameter circles around a prescribed strict-rattler set does
not exhaust it, so the original strict rattlers can be kept non-diametral. $`\square`$

Consequently, if Target A survives at super-boundary scale, it may be normalized to a
**unit-covering saturated** global minimizer while retaining $`\omega(D)`$ strict
rattlers and adding only boundary-order many points.

## 63.2 Open-disk lattice replacement

The finite Oler inequality for an $`n`$-point minimizer gives

```math
n-1\le\frac{D^2}{c}+\frac{\pi D}{2}.
\tag{63.3}
```

The mean number of points of a translated triangular lattice in the open disk of
diameter $`D`$ is $`D^2/c`$.  As in the strict translated-lattice argument, a
translate has strictly more than the mean.  Therefore there is a unit-separated set
of diameter strictly less than $`D`$ with cardinality

```math
\boxed{
N_0>n-\frac{\pi}{2}D-1.
}
\tag{63.4}
```

Thus fewer than $`(\pi/2)D+1`$ additional sites separate a strict sub-$`D`$ lattice
replacement from the full cardinality $`n`$.

## 63.3 Parallel-body identity and collar growth

Let an $`m`$-point minimizer have diameter $`d`$, hull $`K_m`$, area deficit

```math
\delta_m=\frac{\pi d^2}{4}-\operatorname{area}K_m
```

and perimeter deficit

```math
\varepsilon_m=\pi d-\operatorname{per}K_m.
```

Put

```math
t=\frac{D-d}{2}.
```

Steiner's formula gives the exact identity

```math
\boxed{
\operatorname{area}(K_m+tB)
=
\frac{\pi D^2}{4}-\delta_m-\varepsilon_mt.
}
\tag{63.5}
```

Using $`\delta_m<c_0P_m`$ and the audited strict perimeter deficit
$`\varepsilon_m<2\pi c_0`$, one obtains

```math
\boxed{
\delta_m+\varepsilon_mt<c_0\pi D.
}
\tag{63.6}
```

This parallel-body population estimate is exact, but by itself is weaker than the
open-disk estimate (63.4).  Its value is geometric: it provides a scaffold and a
collar in which missing sites might be grafted.

Now let $`\rho=|\mathscr R|`$ be the number of strict rattlers and put $`m=n-\rho`$.  The Oler lower
bound at $`n`$ and the strict translated-lattice upper bound at $`m`$ give

```math
\boxed{
D^2-D(m)^2
>
c\left(\rho-\frac{\pi}{2}D\right).
}
\tag{63.7}
```

Hence, with $`d=D(m)`$,

```math
\boxed{
\frac{D-d}{2}
>
\frac{c}{4D}
\left(\rho-\frac{\pi}{2}D\right).
}
\tag{63.8}
```

If $`\rho/D\to\infty`$, the available collar width tends to infinity.

Equations (63.4) and (63.8) reduce Target A to a precise packing problem: a strict
sub-$`D`$ replacement misses only $`O(D)`$ points while a super-boundary rattler
population produces a diverging-width geometric collar.

---

# 64. Target A after rattlerization

The exact remaining Target A theorem can now be stated without any forest-kinematic
language.

> **Target A1 (saturated rattler-capacity theorem).**
> Let $`A`$ be a triangle-free global minimizer of diameter $`D`$, normalized as in
> Theorems 62.3 and 63.1.  Let $`\mathscr R\subset A`$ be the set of vertices satisfying
> 

```math
> 1<|p-q|<D
> \qquad(q\in A\setminus\{p\}).
> \tag{64.1}
> 
```
> Put $`\rho=|\mathscr R|`$. Prove
> 

```math
> \boxed{\rho=O(D).}
> \tag{64.2}
> 
```

Since $`\rho\ge\ell-\pi D`$, this immediately gives $`\ell=O(D)`$ and closes the
hybrid branch.

A stronger sufficient geometric form is:

> **Target A2 (scaffolded grafting theorem).**
> If $`\rho/D\to\infty`$, use the $`m=n-\rho`$ optimum, the collar (63.8), and the
> strict lattice replacement (63.4) to embed the missing $`O(D)`$ sites compatibly
> inside a region of diameter $`<D`$, producing $`n`$ unit-separated points of
> diameter $`<D`$.

The correct next language is Hall/matching or local finite-Oler capacity, not
single-ray linkage deformation.  A Hall deficiency should force one of:

1. a boundary-order region containing too many strict rattlers;
2. an exact area-plus-perimeter capacity violation;
3. an oversized ordered Cartesian block; or
4. a reusable saturated covering cell from which a missing replacement site can be
   grafted.

The following approaches are explicitly superseded for Target A:

- another rooted-forest rank count;
- raw first-event normal rank;
- assuming deletion of the rattlers preserves optimality;
- treating codimension-one triangle walls on the exact-bar torus as low-rank;
- requiring the forest linkage itself to realize prescribed lattice positions.

---

# 65. Terminal-component Minkowski decomposition

Return to the pure simply connected strict-rhombic disk.  Let $`\Theta`$ be the
terminal graph from Section 51, with hull-chain vertices $`1,\ldots,q`$, train edges,
and oriented incidence matrix $`\partial`$.  Put

```math
e_j=z_{j+1}-z_j
=
\sum_\tau\partial_{j\tau}u_\tau.
\tag{65.1}
```

Let $`C`$ be a connected component of $`\Theta`$, and let $`J_C`$ be its hull-chain
vertex set.

> **Theorem 65.1 (component closure and Minkowski splitting).**
> For every terminal component,
> 

```math
> \boxed{
> \sum_{j\in J_C}e_j=0.
> }
> \tag{65.2}
> 
```
> The vectors $`\{e_j:j\in J_C\}`$, in their inherited cyclic angular order, are the
> edge vectors of a possibly degenerate convex polygon $`K_C`$.  Up to translation,
> 

```math
> \boxed{
> K=K_1+\cdots+K_{c(\Theta)}.
> }
> \tag{65.3}
> 
```

### Proof

Every train edge of component $`C`$ has both terminal vertices in $`J_C`$.  Hence

```math
\sum_{j\in J_C}e_j
=
\sum_{\tau\in E(C)}u_\tau
\sum_{j\in J_C}\partial_{j\tau}
=0.
```

The hull side vectors are already cyclically ordered by direction.  Any subsequence
inherits that order; together with zero sum it forms the edge sequence of a convex
polygon, allowing degenerate segment summands.  Minkowski addition merges convex
polygon edge sequences in angular order, so the union of the component edge
sequences reconstructs the original hull sequence.  This proves (65.3). $`\square`$

This identifies the formerly mysterious terminal components as genuine convex
Minkowski summands of the hull.

---

# 66. Componentwise turn closure and equality classification

For terminal chain $`j`$, choose an incident reference train $`\rho(j)`$ and put

```math
L_j=
\operatorname{span}
\{J(u_\tau-u_{\rho(j)}):\partial_{j\tau}\ne0\},
\qquad
t_j=\dim L_j\in\{0,1,2\}.
\tag{66.1}
```

For component $`C`$, define

```math
s_C=
\dim\operatorname{span}_{j\in J_C}L_j.
\tag{66.2}
```

> **Theorem 66.1 (componentwise closure-corrected turn inequality).**
> 

```math
> \boxed{
> |E(C)|-|V(C)|+1
> \le
> \sum_{j\in J_C}t_j-s_C.
> }
> \tag{66.3}
> 
```
> Summing over components,
> 

```math
> \boxed{
> T-q+c(\Theta)
> \le
> \sum_jt_j-\sum_Cs_C.
> }
> \tag{66.4}
> 
```

### Proof

On the scalar cycle space $`\ker\partial_C`$, the terminal direction lift factors
through $`\bigoplus_{j\in J_C}L_j`$.  Moreover every direction velocity
$`y=\mathcal Dz`$ satisfies

```math
\sum_{j\in J_C}y_j=0,
\tag{66.5}
```

because summing the incidence columns over a component gives zero.  The summation map

```math
\bigoplus_{j\in J_C}L_j
\longrightarrow
\operatorname{span}_{j\in J_C}L_j
```

is surjective and has rank $`s_C`$.  Thus the closure-constrained codomain has
dimension $`\sum t_j-s_C`$.  Since $`\mathcal D`$ is injective, its restriction to
$`\ker\partial_C`$ is injective.  The domain has dimension
$`|E(C)|-|V(C)|+1`$, proving (66.3).  Sum over $`C`$. $`\square`$

The missing $`c(\Theta)`$-scale geometric closure relations are therefore literal
vector-closure relations of the Minkowski summands; they are not supplied by a fake
kernel of $`\mathcal D`$.

> **Theorem 66.2 (equality geometry of $`s_C`$).**
> 

```math
> \boxed{
> \begin{array}{ll}
> s_C=0
> &\Longrightarrow
> C\text{ is a tree and all its trains have one oriented direction};\\[1mm]
> s_C=1,\ C\text{ cyclic}
> &\Longrightarrow
> C\text{ uses exactly two train directions};\\[1mm]
> s_C=2
> &\Longrightarrow
> C\text{ contains genuine two-dimensional phase turning}.
> \end{array}
> }
> \tag{66.6}
> 
```

### Proof

If $`s_C=0`$, then all $`L_j=0`$.  At each terminal vertex all incident oriented
train vectors are equal, and connectivity propagates one common vector $`u`$ through
$`C`$.  If $`C`$ had a scalar cycle $`z\ne0`$, then
$`\mathcal Dz=Ju\,\partial z=0`$, contradicting injectivity.  Hence $`C`$ is a tree.

If $`s_C=1`$, all local direction-difference spaces lie in one common line $`L`$.
At a terminal vertex with at least two incident directions, all incident unit vectors
lie on one affine line parallel to $`L`$.  Shared train edges propagate that same
affine line through the connected component.  An affine line meets the unit circle in
at most two points.  A cyclic component cannot use only one direction by the first
case, so it uses exactly two.  The $`s_C=2`$ statement is the definition of genuine
two-dimensional turning. $`\square`$

Thus every cyclic component either pays two-dimensional closure or is an exact
two-family ordered system, precisely the regime where the Ferrers endpoint applies.

---

# 67. Stochastic Minkowski-width formula for component rotations

Let $`h`$ be an active diameter bar with

```math
r_h=De_h.
```

For terminal component $`C`$, define

```math
r_{h,C}
=
\sum_{j\in U_h\cap J_C}e_j.
\tag{67.1}
```

Then

```math
r_h=\sum_Cr_{h,C}.
\tag{67.2}
```

Because every active diameter direction has unique support maximizer and minimizer,
$`r_{h,C}`$ is the support chord of the Minkowski summand $`K_C`$ in direction
$`e_h`$.  Hence

```math
\boxed{
 r_h\cdot r_{h,C}=D\,w_{K_C}(e_h),
}
\tag{67.3}
```

and width additivity gives

```math
\boxed{
\sum_C w_{K_C}(e_h)=D.
}
\tag{67.4}
```

Now give every train in component $`C`$ the same angular velocity $`\alpha_C`$.
Then

```math
\dot r_{h,C}=\alpha_CJr_{h,C}.
\tag{67.5}
```

Using the exact bar-rotation formula from Section 52,

```math
\boxed{
 s_h(\alpha)
 =
 \sum_C
 \frac{w_{K_C}(e_h)}D\,\alpha_C.
}
\tag{67.6}
```

Put

```math
a_{hC}=\frac{w_{K_C}(e_h)}D.
\tag{67.7}
```

Then

```math
\boxed{
 a_{hC}\ge0,
 \qquad
 \sum_Ca_{hC}=1.
}
\tag{67.8}
```

Thus on the component-rotation quotient a backward/blocker row belonging to a train
of component $`C`$ has the stochastic harmonic-difference form

```math
\boxed{
 \alpha_C-
 \sum_{C'}a_{hC'}\alpha_{C'}.
}
\tag{67.9}
```

Every such row annihilates common component rotation. Therefore

```math
\boxed{
\operatorname{rank}\mathcal B_{\rm comp.rot.}
\le c(\Theta)-1.
}
\tag{67.10}
```

Potential cycles telescope because (67.9) is an exact stochastic averaging system.
This is the first explicit intertwining of a nontrivial part of the **actual inverse
blocker** with the Minkowski terminal decomposition.

For rank bookkeeping, let $`\mathscr S_\alpha`$ be the span in the blocker-row space
of the component-rotation restrictions (67.9), and put

```math
\boxed{
r_\alpha:=\dim\mathscr S_\alpha\le c(\Theta)-1.
}
\tag{67.10a}
```

Write henceforth

```math
x_\tau=\alpha_C+\xi_\tau
\qquad(\tau\in E(C)),
\tag{67.11}
```

where $`\alpha_C`$ is common component rotation and $`\xi`$ is the internal
relative-angle coordinate. Quotient the blocker-row span by $`\mathscr S_\alpha`$,
and denote the induced internal row family by $`\overline{\mathcal B}_\xi`$. Then

```math
\boxed{
\operatorname{rank}\mathcal B
\le r_\alpha+\operatorname{rank}\overline{\mathcal B}_\xi.
}
\tag{67.12}
```

Thus the component-rotation contribution is **isolated and bounded, not free**. The
remaining unbounded contribution is the internal $`\xi`$-part, but any final coforest
inequality must explicitly reserve the rank budget $`r_\alpha`$.

---

# 68. Exact v1.2.0 remaining lemmas

> **HISTORICAL v1.2 FRONTIER.** Target A in this section is superseded by Sections 71--75.
> Target B remains valid and is restated without substantive change in Section 76.

## 68.1 Target A: saturated rattler capacity

The hybrid branch is closed if one proves

```math
\boxed{
\rho=O(D)
}
\tag{68.1}
```

for the saturated rattlerized representative of Sections 62--63, where
$`\rho=|\mathscr R|`$.

Equivalently, it is sufficient to prove the scaffolded grafting theorem of Target A2:
when $`\rho/D\to\infty`$, the diverging collar (63.8) and the boundary-order missing
population (63.4) permit an $`n`$-point unit-separated configuration of diameter
strictly below $`D`$.

The next viable mechanism is a Hall-type matching/capacity theorem.  Candidate missing
replacement sites should be matched to disjoint rattler/Voronoi covering cells in the
saturated hull.  A Hall deficiency must be converted into a finite Oler or ordered
shell capacity violation.

## 68.2 Target B: internal component blocker/coforest theorem

Let $`\mathscr S_\alpha`$, $`r_\alpha`$, and
$`\overline{\mathcal B}_\xi`$ be as in Section 67. After quotienting the component
rotations, construct an explicit injective matroidal map from the **internal** parts of

- the backward rows $`b_{h\tau}`$;
- the peripheral free-coordinate differences; and
- the terminal rigid-potential blocks

into the componentwise closure-corrected turn/coforest spaces. The exact sufficient
residual inequality is

```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha.
}
\tag{68.2a}
```

Since $`r_\alpha\le c(\Theta)-1`$, the stronger component-count-only statement

```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-c(\Theta)+1
}
\tag{68.2b}
```

is also sufficient. Indeed, (67.12) and either residual bound give the desired total
pure inequality

```math
\boxed{
\operatorname{rank}\mathcal B+I+r\le T-q.
}
\tag{68.2}
```

This contradicts the established lower bound

```math
\boxed{
\operatorname{rank}\mathcal B+I+r\ge T-q+1.
}
\tag{68.3}
```

The proof should split terminal components by Theorem 66.2:

1. if $`s_C=2`$, use both vector-closure equations and the internal turn quotient;
2. if $`s_C=1`$ and $`C`$ is cyclic, use the exact two-family ordering and the
   Ferrers staircase theorem;
3. tree/one-direction components contribute no scalar cycle obstruction;
4. component rotations are paid separately by the explicit budget $`r_\alpha`$ in
   (67.10a)--(67.12), not silently discarded or mixed into the internal rank count.

The available two-family numerical endpoint remains

```math
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2,
\tag{68.4}
```

with gap

```math
\boxed{0.0124073626\ldots D^2.}
\tag{68.5}
```

No improved constant is presently required.

## 68.3 Topology-corrected Target B

After (68.2) is proved in the pure disk, it must still be transported through
nonquadrilateral faces, holes, multiple components, boundary pinches, and vertices
outside the rhombic core.  Each exceptional gadget must be charged **exactly** to the
topology-corrected residual.  An uncontrolled $`O(D)`$ rank loss remains fatal to the
one-integer contradiction.

---

# 69. Version 1.2.0 exact status

> **HISTORICAL STATUS.** Retained as the frozen v1.2 endpoint. The authoritative
> status is Section 77.

**LEVEL I STATUS: STILL OPEN.**

Version 1.2.0 compresses the two remaining branches substantially beyond v1.1.0.

## Target A — saturated strict-rattler branch

The hybrid forest now has the exact rank identity

```math
\ell=u-r+c+\sigma,
\qquad
0\le\sigma\le r-c,
```

and can be transformed, after losing only $`O(D)`$ old contacts, into a nearby
triangle-free global minimizer containing

```math
\boxed{
\rho=|\mathscr R|\ge u-r+c\ge\ell-\pi D
}
\tag{69.1}
```

genuine strict rattlers.  The local same-$`D`$ minimizer set then has dimension at
least

```math
2\rho\ge2\ell-2\pi D.
\tag{69.2}
```

After adding fewer than $`(\pi/2)D`$ further points, the fixed hull may also be
assumed unit-covering saturated without destroying the original strict rattlers.

Therefore the old forest-flex problem is superseded by the precise global question:

```math
\boxed{
\text{Can a triangle-free globally optimal diameter-}D\text{ packing contain }
\omega(D)\text{ strict rattlers?}
}
\tag{69.3}
```

The remaining proof target is the saturated rattler-capacity theorem or an equivalent
Hall/grafting contradiction.

## Target B — internal terminal-component rank

The terminal graph components are exact Minkowski summands of the hull.  Their scalar
cycle rank satisfies the strengthened closure inequality

```math
T-q+c(\Theta)
\le
\sum_jt_j-\sum_Cs_C.
\tag{69.4}
```

Cyclic $`s_C=1`$ components are exactly two-direction systems; $`s_C=2`$ components
carry genuine two-dimensional closure. Uniform component rotations enter every
active diameter bar through stochastic width weights. Their row span
$`\mathscr S_\alpha`$ has explicit rank budget $`r_\alpha\le c(\Theta)-1`$.

Thus the common component rotations are isolated rather than mysterious, but their
rank is not free: it must be reserved in the final count. The exact remaining pure
theorem is the internal residual inequality (68.2a), or the stronger universal
version (68.2b), which together with (67.12) yields the total blocker--turn/coforest
inequality (68.2). The topology-corrected extension then remains.

## Unified endgame

A Level I proof now needs two global capacity statements:

1. **rattler capacity:** a saturated diameter minimizer cannot carry a
   super-boundary population of strict rattlers; and
2. **internal shell rank:** after Minkowski component rotations are quotiented, the
   ordered terminal shell cannot carry the independent internal backward/Dirichlet
   rank forced by the pure survivor while $`G+E<c_0B`$.

The first is now a packing/covering/grafting theorem.  The second is now a
componentwise ordered matroid/Ferrers theorem.  Neither is a first-order rigidity
problem.

No theorem in v1.2.0 closes both statements, and no infinite sequence of triangle-free
**global** minimizers is known.  No proof or disproof is claimed.

---
