> Generated reading edition · [exact source](../../../../docs/targets/target-a/10-quantitative-kuperberg-rate.md) · source SHA-256 `84014aee1e919d5c9e930817a84746e50831c0475d95d93cc100290c90efc96e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — exact quantitative Kuperberg five-block rate

This audited addendum promotes the exact support-radius rate derived from the aligned
five-block rearrangement of G. Kuperberg, K. Kuperberg, and W. Kuperberg. It replaces
the previously open quantitative statement in Section 150 for the **free aligned-gap**
model. It does not solve exterior compatibility in a genuine embedded Target A monomer
domain.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 157. Exact five-block gain and support-radius rate

Use the canonical triangular-lattice normalization with minimum center distance one.
For an aligned gap of width $`d>0`$, let $`W(d)`$ be the minimum support radius, up to
translation parallel to the gap, of a finite positive-gain rearrangement as defined in
Section 150.

It is convenient to do the local calculation first in the paper normalization, where
minimum center distance is two. The center lattice is

```math
\Lambda_2=\{(2i+j,\sqrt3j):i,j\in\mathbb Z\},
```

and the upper half-lattice is translated by $`(0,d)`$. The Kuperberg five-block move
uses two outer upward $`\Delta_n`$ blocks, two downward $`\nabla_n`$ blocks, and one
middle upward $`\Delta_{n-1}`$ block. The moves are:

1. move both outer $`\Delta_n`$ blocks vertically down by $`d`$;
2. move the two $`\nabla_n`$ blocks symmetrically down and outward by magnitude $`u`$,
   at $`60^\circ`$ from vertical;
3. move the middle $`\Delta_{n-1}`$ block vertically upward by $`v`$.

The exact lattice-coordinate reconstruction and complete nearest-neighbor enumeration
are recorded in
[`../../reports/exact_kuperberg_five_block_rate_2026-08-30.md`](../../reports/exact_kuperberg_five_block_rate_2026-08-30.md)
and reproduced by
[`../../../research/kuperberg_five_block_exact.py`](../../../../research/kuperberg_five_block_exact.py).

> **Theorem 157.1 (exact one-step five-block gain).** In the paper normalization,
> after the full first move, the only controlling second-stage margin is
> 

```math
> F_d(u)=u^2-(2\sqrt3+d)u+d^2.
> \tag{157.1}
> 
```
> Hence the maximal continuous second move is the smaller root
> 

```math
> \phi(d)=
> \frac{2\sqrt3+d-\sqrt{(2\sqrt3+d)^2-4d^2}}2.
> \tag{157.2}
> 
```
> After setting $`u=\phi(d)`$, the only controlling third-stage margin is
> 

```math
> G_u(v)=v^2-(2\sqrt3-u)v+u^2,
> \tag{157.3}
> 
```
> so the maximal upward move of the middle block is the smaller root
> 

```math
> \psi(u)=
> \frac{2\sqrt3-u-\sqrt{(2\sqrt3-u)^2-4u^2}}2.
> \tag{157.4}
> 
```
> Therefore the gap gain is
> 

```math
> \delta(d)=\psi(\phi(d))
> =\frac{\sqrt3}{72}d^4-\frac1{72}d^5+O(d^6).
> \tag{157.5}
> 
```
> In particular
> 

```math
> \boxed{\delta(d)\sim\frac{\sqrt3}{72}d^4.}
> \tag{157.6}
> 
```

### Proof

Rigid translation preserves all within-block distances. At $`d=0`$, every pair that
is not a triangular-lattice nearest neighbor has distance at least $`2\sqrt3`$, so
for all sufficiently small $`d`$ only original nearest-neighbor pairs can become
active during the three moves.

The complete cross-boundary nearest-neighbor enumeration gives the following
nonconstant squared-distance margins, up to symmetry and repetition:

```math
\begin{gathered}
 d^2,\quad d(d+2\sqrt3),\quad 0,\quad
 F_d(u),\quad F_d(u)+2\sqrt3d,\\
 d^2-du+u^2+2\sqrt3d,\quad
 u^2,\quad u(u+2\sqrt3),\quad u(3u+4\sqrt3),\\
 G_u(v),\quad
 u^2+uv+v^2+2\sqrt3u,\quad
 (d+v)(d+v+2\sqrt3).
\end{gathered}
\tag{157.7}
```

All terms other than $`F_d`$ and $`G_u`$ are manifestly nonnegative for
$`d,u,v\ge0`$ once the controlling inequalities hold. At $`u=0`$,
$`F_d(0)=d^2>0`$; the continuous motion first reaches equality at the smaller root
(157.2). Thus $`0\le u\le\phi(d)`$ is feasible and $`u=\phi(d)`$ is maximal for the
prescribed move. Expanding the root gives

```math
\phi(d)=\frac{d^2}{2\sqrt3}-\frac{d^3}{12}
+\frac{\sqrt3}{36}d^4+O(d^5).
\tag{157.8}
```

With this $`u>0`$, one has $`G_u(0)=u^2>0`$; the third move first reaches equality at
(157.4). Hence $`v=\psi(\phi(d))`$ is feasible and maximal for the prescribed move.
Expanding $`\psi`$ at zero and substituting (157.8) yields (157.5). The exact verifier
enumerates (157.7) for several block sizes using arithmetic in
$`\mathbb Q(\sqrt3)[d,u,v]`$, independently guarding the finite interface bookkeeping.
$`\square`$

## 157.1 Exact nesting ratio

> **Lemma 157.2 (factor-three nesting).** A size-$`m`$ five-block template fits along
> the base of the translated middle $`\Delta_{n-1}`$ block whenever
> 

```math
> \boxed{3m\le n-2.}
> \tag{157.9}
> 
```
> Consequently $`k`$ recursive widening stages require an initial block parameter
> 

```math
> n_0=O(3^k),
> \tag{157.10}
> 
```
> and therefore support radius $`O(3^k)`$.

### Proof

After translating lattice indices so the base begins at zero, a size-$`m`$ five-block
trapezoid occupies rows $`0\le j\le m-1`$ and satisfies
```math
0\le i\le3m-j.
```
The middle $`\Delta_{n-1}`$ block has rows $`0\le j\le n-2`$ and
```math
0\le i\le n-2-j.
```
The first region is contained in the second exactly when $`3m\le n-2`$. Iteration
then multiplies the required linear scale by at most a fixed factor three per stage.
$`\square`$

## 157.2 Explicit support-radius upper bound

> **Theorem 157.3 (explicit aligned support rate).** There exist constants
> $`C_1,C_2,d_*>0`$ such that in the canonical minimum-distance-one normalization,
> 

```math
> \boxed{
> W(d)\le C_1\exp(C_2d^{-3})
> \qquad(0<d<d_*).
> }
> \tag{157.11}
> 
```

### Proof

By Theorem 157.1, after rescaling if necessary there is $`c_*>0`$ such that the
one-step gain satisfies
```math
\delta(x)\ge c_*x^4
```
for all sufficiently small positive $`x`$. For the recurrence
```math
x_{j+1}=x_j+\delta(x_j),\qquad x_0=d,
```
the standard integral comparison with $`dx/dj=c_*x^4`$ gives
```math
k(d)=O(d^{-3})
```
stages to reach a fixed positive width. Once that width is reached, monotonicity of
the Kuperberg gain requires only $`O(1)`$ more stages to reach a gap wide enough to
insert an additional circle. Lemma 157.2 makes the support radius at most
```math
C3^{C'd^{-3}}\le C_1e^{C_2d^{-3}}.
```
Rescaling center distance two to one only changes the constants. $`\square`$

For reference, the canonical one-step gain is
```math
\delta_{\rm can}(d)=\frac{\sqrt3}{9}d^4+O(d^5).
\tag{157.12}
```

## 157.3 Vanishing accumulated homothetic strain

Section 150 proves that, for a fixed full-dimensional triangular-lattice polygon
$`K`$ with $`r\mathbb B\subset K`$, the same-hull add-one conclusion follows from
```math
W(r\alpha_L)=o(L),
```
where $`\alpha_L`$ is the accumulated homothetic strain.

> **Corollary 157.4 (explicit vanishing-strain regime).** If
> 

```math
> \boxed{\alpha_L^{-3}=o(\log L),}
> \tag{157.13}
> 
```
> then for all sufficiently large $`L`$,
> 

```math
> \boxed{
> \alpha_1(H_{L,\alpha_L})\ge |P_L|+1.
> }
> \tag{157.14}
> 
```

### Proof

Theorem 157.3 gives
```math
\log W(r\alpha_L)\le O(1)+Cr^{-3}\alpha_L^{-3}=o(\log L),
```
so $`W(r\alpha_L)=L^{o(1)}=o(L)`$. Apply Section 150. $`\square`$

This strictly extends the fixed-positive-accumulated-strain theorem of Section 148,
but does not reach $`\alpha_L=L^{-\beta}`$ for any fixed $`\beta>0`$.

## 157.4 Exact scope and remaining lemma

Theorem 157.3 is an upper bound for the free aligned-gap model. It is compatible with
Section 146, which proves that the deletion cardinality of any positive-gain witness
must diverge as $`d\downarrow0`$. The support bound also diverges.

The theorem does **not** show that the nested block motion can be executed when the
selected monomer domain has exterior source/scaffold points immediately outside the
block. Therefore the Target A endpoint remains

```math
\boxed{\dim\ker S\ge\Delta_\Lambda-d_{\rm int}}
```

or an actual $`N`$-point unit-separated competitor of diameter strictly below $`D`$.
The exact geometric continuation is:

> **Exterior-compatible finite-gap lemma.** At a gap scale that actually occurs in a
> globally derived Target A monomer domain, either protect a radius
> $`O(\exp(Cd^{-3}))`$ five-block witness from all exterior blockers with
> $`o(D)`$ support, or construct a different finite rearrangement with a smaller
> support cost and a strict diameter certificate.

The quartic bottleneck of the published architecture is now explicit:
```math
 d\longmapsto u=\Theta(d^2)\longmapsto v=\Theta(u^2)=\Theta(d^4).
```
Any alternative finite architecture with linear or quadratic final gain would
substantially improve the support regime.
