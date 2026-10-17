> Generated reading edition · [exact source](../../research/target_c_woodall_vertex_cover_sqrt_braid_2026-10-02.md) · source SHA-256 `9c1a537a97abe0d24a0a9446245613fc42fd51c526bea0d26b717b08147104ce`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C: Woodall vertex covers double the square-root diameter braid constant

**Date:** 2026-10-02  
**Remote main rechecked before writing:** \`3bad7c12bf5133665be466d0396362108fadef2c\`  
**Research branch parent:** \`research/global-diameter-leaf-core-dichotomy-2026-10-02\`  
**Status:** proof-only candidate. Level I and C-II remain open.

## 1. Input

Current main proves the unreviewed cubic incidence inequality for the full actual
diameter graph $H$:

$$
(J-N)_+^3<\mathcal B_DN^2,
\qquad
\mathcal B_D={12\pi\sqrt3\over D a_D^3},
\qquad
a_D=2\arcsin{1\over2D},
\tag{1}
$$

for every set $S$ of $N$ actual diameter vertices receiving $J$ endpoint
incidences from any specified family of actual diameter edges. Also

$$
{\mathcal B_D\over D^2}\longrightarrow12\pi\sqrt3.
\tag{2}
$$

Canonical ZF gives

$$
h:=|E(H)|\ge\lceil D\rceil.
\tag{3}
$$

The parent square-root braid note used the $2\nu(H)$ endpoints of a maximal
matching as a vertex cover. Canonical C-WOODALL lets us replace that cover by one
of size at most $\nu(H)+1$.

## 2. Woodall gives a near-König vertex cover

Let

$$
\nu:=\nu(H),\qquad \tau:=\tau(H)
$$

denote the matching and vertex-cover numbers.

### Lemma 2.1

For the canonical planar diameter graph,

$$
\boxed{\tau\le\nu+1.}
\tag{4}
$$

In the Woodall forest branch,

$$
\boxed{\tau=\nu.}
\tag{5}
$$

### Proof

If $H$ is a forest, the equality $\tau=\nu$ is the elementary forest case of
König's theorem. For completeness, it follows by induction. Choose a leaf $u$
with neighbor $v$. Some maximum matching contains $uv$: if a maximum matching
does not use $uv$, either $v$ is unmatched and $uv$ can be added, or $v$
is matched to another neighbor and that edge can be replaced by $uv$. Hence

$$
\nu(H)=1+\nu(H-v),
$$

where $u$ is isolated in $H-v$. A minimum vertex cover can likewise be chosen
to contain $v$ rather than $u$, so

$$
\tau(H)=1+\tau(H-v).
$$

Induction proves (5) componentwise.

If $H$ is in the Woodall cyclic branch, choose any vertex $v$ of the unique odd
cycle. The graph $H-v$ is a forest. A minimum cover of $H-v$, together with
$v$, covers $H$. Therefore

$$
\tau(H)
\le1+\tau(H-v)
=1+\nu(H-v)
\le1+\nu(H),
$$

which proves (4). QED.

No property of the contact graph is used here.

## 3. Improved square-root matching theorem

### Theorem 3.1

Along every unbounded canonical post-ZF C-II sequence,

$$
\boxed{
\nu(H)\ge
\left({1\over\sqrt{12\pi\sqrt3}}-o(1)\right)\sqrt D.
}
\tag{6}
$$

This doubles the constant in the parent maximal-matching-endpoint argument.

### Proof

Let $S$ be a minimum vertex cover of $H$, and put

$$
N:=|S|=\tau(H).
$$

Every actual diameter edge has at least one endpoint in $S$, so its endpoint
incidence count on $S$ satisfies

$$
J:=\sum_{v\in S}d_H(v)\ge h\ge D.
\tag{7}
$$

Apply (1) to $S$.

Choose a subsequence on which $\nu/\sqrt D$ tends to its liminf. If that liminf is
infinite, (6) is immediate. Otherwise $\nu=O(\sqrt D)$, and Lemma 2.1 gives

$$
N\le\nu+1=O(\sqrt D),
\qquad
{N\over D}\to0.
\tag{8}
$$

For large $D$, $N<D\le J$. Hence

$$
(D-N)^3
\le(J-N)^3
<\mathcal B_DN^2.
\tag{9}
$$

Divide by $D^3$ and use (2), (8):

$$
1
\le
12\pi\sqrt3\,
\liminf {N^2\over D}.
$$

Thus

$$
\liminf {N\over\sqrt D}
\ge {1\over\sqrt{12\pi\sqrt3}}.
\tag{10}
$$

Finally Lemma 2.1 gives $\nu\ge N-1$, so the same lower bound holds for
$\nu/\sqrt D$. QED.

### Finite form

If $N\le D/2$, then (9) and the current-main bound
$\mathcal B_D\le12\pi\sqrt3D^2$ give

$$
{D^3\over8}
<
12\pi\sqrt3D^2N^2,
$$

hence

$$
\boxed{
\nu
\ge N-1
>
{\sqrt D\over\sqrt{96\pi\sqrt3}}-1.
}
\tag{11}
$$

If $N>D/2$, then $\nu\ge N-1>D/2-1$.

The asymptotic constant in (6) is the sharper statement because the hard branch has
$N/D\to0$.

## 4. Improved global crossing braid

Take a maximum matching of size $\nu$. Its edges have pairwise disjoint endpoints,
so every pair crosses properly by the planar diameter-thrackle property.

The exact cyclic-order lemma from the parent note therefore applies without change:
if the $2\nu$ selected endpoints are listed cyclically as

$$
x_0,x_1,\ldots,x_{2\nu-1},
$$

then after cyclic relabeling

$$
\boxed{
M=\{x_ix_{i+\nu}:0\le i<\nu\}.
}
\tag{12}
$$

Consequently current main plus C-WOODALL now yields an exact two-shore actual-diameter
braid of size

$$
\boxed{
\left({1\over\sqrt{12\pi\sqrt3}}-o(1)\right)\sqrt D.
}
\tag{13}
$$

The current-main midpoint-energy theorem still places all these braid midpoints in

$$
B\!\left(s,{3\over2}D^{2/3}\right),
\tag{14}
$$

so

$$
|x_{i+\nu}-(2s-x_i)|<3D^{2/3}.
\tag{15}
$$

Thus the improvement is simultaneously combinatorial and geometric: twice the
previous asymptotic braid constant, with the same exact crossing order and common
$O(D^{2/3})$ midpoint core.

## 5. Interaction with the leaf-saturated hard branch

The companion leaf/core theorem on this branch gives

$$
\ell\ge h-2\nu-1,
\tag{16}
$$

where $\ell$ is the number of degree-one diameter vertices. Hence if the matching
remains on the square-root scale,

$$
\nu=O(\sqrt D),
$$

then

$$
\ell=D-O(\sqrt D).
\tag{17}
$$

The improved lower bound (6) shows that the hard regime has a genuine square-root
carrier scale on both sides:

$$
\boxed{
\nu=\Theta(\sqrt D)
\quad\Longrightarrow\quad
\begin{cases}
D-O(\sqrt D) & \text{diameter leaves},\\
\Theta(\sqrt D) & \text{matching / carrier scale}.
\end{cases}
}
\tag{18}
$$

The companion theorem further reduces the normalized KKT stress in this regime to
either a linear aggregate contact load at the pendant terminals or a
$D^{-1/2}$-scale core diameter multiplier.

## 6. Remaining obstruction

The theorem still does not close C-II.

The square-root scale is compatible with the cubic star moment: a formal family of
$\Theta(\sqrt D)$ diameter carriers each supporting $\Theta(\sqrt D)$ pendant
diameters has total cubic star cost $\Theta(D^2)$. The new theorem says that any
canonical survivor near this hard scale must realize essentially that topology while
also satisfying the contact/KKT alternatives in the companion leaf/core report.

The next source-level attack should therefore use one of:

1. the $D-O(\sqrt D)$ pendant diameter terminals against the canonical outer-walk
   detour and ball-hull loaded-leaf geometry;
2. the $D^{-1/2}$-scale core multiplier against the common 2-edge-connected contact
   hub;
3. the enlarged exact crossing braid against the two-shore contact/outer-walk order.

No computation, numerical search, verifier execution, or CI output is used here.
