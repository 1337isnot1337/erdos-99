> Generated reading edition · [exact source](../../../../docs/targets/target-a/12-toeout-kuperberg-improvement.md) · source SHA-256 `e4f5620b9f4a4ebe2fd46e1fda47adcd3bb0c435812f3dd4f59da373fa157592`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target A — toe-out Kuperberg improvement

This audited addendum strengthens the free aligned-gap theorem of Section 157.  It
uses the same five rigid triangular blocks, but allows the two outer blocks to move a
small horizontal distance while they descend.  That extra degree of freedom increases
the leading quartic gap gain by a factor of eight and makes the support exponent
constant explicit.  The exponent `d^{-3}` itself is unchanged.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 160. Toe-out five-block widening and the borderline logarithmic-strain regime

Work first in the Kuperberg paper normalization, where nearest-neighbor center
distance is two and

```math
\Lambda_2=\{(2i+j,\sqrt3j):i,j\in\mathbb Z\}.
```

The upper half-lattice is shifted by `(0,d)`, `d>0`, and the five blocks
`B_1,\ldots,B_5` are exactly those of Section 157.  Rigidly translate them by

```math
\begin{aligned}
B_1&:\ (-a,-b),&
B_2&:\ (-c,-e),&
B_3&:\ (0,v),\\
B_4&:\ (c,-e),&
B_5&:\ (a,-b).
\end{aligned}
\tag{160.1}
```

Thus the outer pair descends and toes outward, the inner pair descends and toes
outward farther, and the middle block rises vertically.

## 160.1 Five active contacts determine an analytic widening branch

Impose the following five squared-distance equalities:

```math
\begin{aligned}
F_1&=(2-a)^2+b^2-4=0,\\
F_2&=(1-a)^2+(\sqrt3+d-b)^2-4=0,\\
F_3&=(-2+c-a)^2+(e-b)^2-4=0,\\
F_4&=(1-c)^2+(\sqrt3+e)^2-4=0,\\
F_5&=(1+c)^2+(\sqrt3-e-v)^2-4=0.
\end{aligned}
\tag{160.2}
```

They correspond respectively to an outer/fixed-upper contact, an outer/lower
contact, an outer/inner contact, an inner/fixed-upper contact, and an
inner/middle contact.  At `d=0` the solution

```math
a=b=c=e=v=0
```

recovers the triangular lattice.  The Jacobian of `(F_1,\ldots,F_5)` with respect to
`(a,b,c,e,v)` at that point is

```math
\begin{pmatrix}
-4&0&0&0&0\\
-2&-2\sqrt3&0&0&0\\
4&0&-4&0&0\\
0&0&-2&2\sqrt3&0\\
0&0&2&-2\sqrt3&-2\sqrt3
\end{pmatrix},
```

whose determinant is

```math
384\sqrt3\ne0.
\tag{160.3}
```

The implicit-function theorem therefore gives unique real-analytic functions
`a(d),b(d),c(d),e(d),v(d)` near zero satisfying (160.2).  Coefficient comparison in
(160.2) gives

```math
\begin{aligned}
a(d)&=\frac14d^2-\frac{\sqrt3}{24}d^3
      +\frac1{24}d^4-\frac{\sqrt3}{144}d^5+O(d^6),\\
b(d)&=d-\frac{\sqrt3}{12}d^2+\frac1{24}d^3
      -\frac1{144}d^5+O(d^6),\\
c(d)&=\frac12d^2-\frac{\sqrt3}{6}d^3
      +\frac5{24}d^4-\frac{\sqrt3}{18}d^5+O(d^6),\\
e(d)&=\frac{\sqrt3}{6}d^2-\frac16d^3
      +\frac{\sqrt3}{72}d^4+\frac1{18}d^5+O(d^6),\\
v(d)&=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6).
\end{aligned}
\tag{160.4}
```

In particular all five parameters are positive for sufficiently small `d>0`.

## 160.2 Complete nearest-neighbor feasibility audit

Rigid translation preserves within-block distances.  As in Section 157, it is enough
for sufficiently small `d` to check original triangular-lattice nearest neighbors:
all other pairs start at distance at least `2\sqrt3`, while every translation in
(160.1) is `O(d)`.

Expanding the six nearest-neighbor directions across every moved/moved and
moved/fixed interface gives exactly the following fifteen squared-distance margins,
up to left-right symmetry and repetition:

```math
\begin{array}{rcl}
M_1&=&a^2-2a+b^2+2\sqrt3b,\\
M_2&=&a^2-4a+b^2,\\
M_3&=&a^2-2a+b^2-2bd-2\sqrt3b+d^2+2\sqrt3d,\\
M_4&=&a^2+2a+b^2-2bd-2\sqrt3b+d^2+2\sqrt3d,\\
M_5&=&a^2-2ac+4a+b^2-2be+c^2-4c+e^2,\\
M_6&=&a^2-2ac+2a+b^2-2be+2\sqrt3b+c^2-2c+e^2-2\sqrt3e,\\
M_7&=&c^2+4c+e^2+2ev+v^2,\\
M_8&=&c^2-2c+d^2-2de+2\sqrt3d+e^2-2\sqrt3e,\\
M_9&=&c^2+2c+d^2-2de+2\sqrt3d+e^2-2\sqrt3e,\\
M_{10}&=&c^2+2c+e^2+2ev-2\sqrt3e+v^2-2\sqrt3v,\\
M_{11}&=&(d+v)(d+v+2\sqrt3),\\
M_{12}&=&a^2+2a+b^2+2\sqrt3b,\\
M_{13}&=&c^2+2c+e^2+2\sqrt3e,\\
M_{14}&=&c^2-2c+e^2+2\sqrt3e,\\
M_{15}&=&4c(c+2).
\end{array}
\tag{160.5}
```

The five defining equalities (160.2) are exactly

```math
M_2=M_3=M_5=M_{10}=M_{14}=0.
\tag{160.6}
```

Substitution of (160.4) into the remaining ten margins gives

```math
\begin{array}{rclcrcl}
M_1&=&2\sqrt3d+O(d^2),&&
M_4&=&d^2+O(d^3),\\
M_6&=&2\sqrt3d+O(d^2),&&
M_7&=&2d^2+O(d^3),\\
M_8&=&2\sqrt3d+O(d^2),&&
M_9&=&2\sqrt3d+O(d^2),\\
M_{11}&=&2\sqrt3d+O(d^2),&&
M_{12}&=&2\sqrt3d+O(d^2),\\
M_{13}&=&2d^2+O(d^3),&&
M_{15}&=&4d^2+O(d^3).
\end{array}
\tag{160.7}
```

Hence every nonactive nearest-neighbor margin is strictly positive for all
sufficiently small `d>0`, while the five active families remain exactly at distance
two.  The originally non-neighboring pairs remain farther than two after shrinking
the allowed `d` once more.  Therefore (160.1) is a genuine packing rearrangement.

The exact truncated-series enumeration behind (160.5)--(160.7) is reproduced by
[`../../../research/kuperberg_five_block_toeout_exact.py`](../../../../research/kuperberg_five_block_toeout_exact.py).
The proof itself is the analytic calculation above; the script is only an arithmetic
audit.

## 160.3 Eightfold larger quartic gain

The middle block is a rigid translate of the original `\Delta_{n-1}` block.  Along
its base, the upper row has moved from height `d` to height `d+v(d)` while the lower
half-lattice is unchanged.  Thus the new local aligned gap is

```math
d'=d+\delta_{\rm toe}(d),
\qquad
\delta_{\rm toe}(d)=v(d).
```

By (160.4),

```math
\boxed{
\delta_{\rm toe}(d)
=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6)
}
\tag{160.8}
```

in the paper normalization.  Section 157's prescribed three-motion construction had
leading coefficient `\sqrt3/72`.  Therefore

```math
\boxed{
\frac{\delta_{\rm toe}(d)}{\delta_{157}(d)}\longrightarrow8.
}
\tag{160.9}
```

No optimality claim is made for (160.8) among all rigid-block or finite packing
rearrangements.  It is an explicit improved feasible branch.

## 160.4 Recursive support with an explicit exponent constant

The factor-three nesting geometry of Lemma 157.2 is unchanged because the block
partition is unchanged.  For recursion, use a fixed one-ring safety margin around
each child template inside its parent middle block.  This changes

```math
3m\le n-2
```

to

```math
3m+C\le n
\tag{160.10}
```

for an absolute constant `C`, and therefore still gives initial block size

```math
n_0=O(3^k)
\tag{160.11}
```

after `k` widening stages.  The safety ring ensures that every child
nearest-neighbor interaction sees exactly the same local upper/lower gap geometry;
points beyond the ring are original non-neighbors and remain separated for small
width.

Let

```math
x_{j+1}=x_j+\delta_{\rm toe}(x_j),
\qquad x_0=d.
```

Put `K=\sqrt3/9`.  From (160.8),

```math
\delta_{\rm toe}(x)=Kx^4+O(x^5).
\tag{160.12}
```

Until a fixed positive gap width is reached,

```math
x_j^{-3}-x_{j+1}^{-3}=3K+O(x_j).
\tag{160.13}
```

Moreover `\sum_jx_j=O(d^{-2})`, for example by comparison with
`dx/dj\asymp x^4`.  Summing (160.13) therefore yields

```math
\boxed{
k(d)=\sqrt3\,d^{-3}+O(d^{-2})
}
\tag{160.14}
```

stages to reach any fixed small positive width.  Only `O(1)` additional stages are
then needed, exactly as in Section 157.  Combining (160.11) and (160.14), the paper
normalization has support radius `R_{\rm toe}(d)` satisfying

```math
\boxed{
\limsup_{d\downarrow0}d^3\log R_{\rm toe}(d)
\le\sqrt3\log3.
}
\tag{160.15}
```

In canonical minimum-distance-one normalization, `d_{\rm paper}=2d` and support
radii scale by one half.  Since `W(d)` is the minimum support radius over all finite
positive-gain aligned-gap witnesses, (160.15) gives the stronger canonical theorem

> **Theorem 160.1 (explicit aligned support constant).**
> ```math
> \boxed{
> \limsup_{d\downarrow0}
> d^3\log W(d)
> \le\frac{\sqrt3\log3}{8}.
> }
> \tag{160.16}
> ```

Equivalently, for every `\varepsilon>0` and all sufficiently small `d>0`,

```math
W(d)
\le
\exp\left[
\left(\frac{\sqrt3\log3}{8}+\varepsilon\right)d^{-3}
\right].
\tag{160.17}
```

For reference, the canonical one-step gain of the new branch is

```math
\boxed{
\delta_{{\rm toe},\rm can}(d)
=\frac{8\sqrt3}{9}d^4-\frac{32}{9}d^5+O(d^6).
}
\tag{160.18}
```

The old Section 157 construction would give the corresponding leading support
constant `\sqrt3\log3`; (160.16) divides that constant by eight.

## 160.5 A new borderline logarithmic-strain same-hull theorem

Return to the fixed full-dimensional triangular-lattice polygon `K` of Sections
148 and 150 and choose `r>0` with

```math
r\mathbb B\subset K.
```

The row split creates canonical aligned gap width

```math
d_L=r\alpha_L.
```

Section 150 reduces the same-hull add-one conclusion to

```math
W(r\alpha_L)=o(L).
\tag{160.19}
```

Theorem 160.1 now reaches a genuine borderline scale that Corollary 157.4 did not.

> **Corollary 160.2 (borderline logarithmic strain).** If
> ```math
> \boxed{
> \limsup_{L\to\infty}
> \frac{\alpha_L^{-3}}{\log L}
> <
> \frac{8r^3}{\sqrt3\log3},
> }
> \tag{160.20}
> ```
> then, for all sufficiently large `L`,
> ```math
> \boxed{
> \alpha_1(H_{L,\alpha_L})\ge |P_L|+1.
> }
> \tag{160.21}
> ```

Indeed, (160.16) gives

```math
\log W(r\alpha_L)
\le
\left(\frac{\sqrt3\log3}{8}+o(1)\right)
 r^{-3}\alpha_L^{-3}.
```

Under (160.20), the right side is at most `\theta\log L` for some fixed
`\theta<1`, so `W(r\alpha_L)\le L^\theta=o(L)`.  Apply (160.19).

In particular the theorem includes

```math
\alpha_L=A(\log L)^{-1/3}
```

whenever

```math
A>
\left(\frac{\sqrt3\log3}{8r^3}\right)^{1/3}.
\tag{160.22}
```

This is strictly stronger than the earlier sufficient condition
`\alpha_L^{-3}=o(\log L)`.

## 160.6 Scope and remaining Target A obligation

Theorem 160.1 is still a **free aligned-gap** theorem.  It does not protect the
nested blocks from source/scaffold points immediately outside a genuinely embedded
Target A monomer region.  The exponent remains `d^{-3}`, so it also does not reach a
power-law accumulated strain `\alpha_L=L^{-\beta}`.

Thus the direct Target A endpoint remains

```math
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}
}
```

or an actual `N`-point unit-separated competitor of diameter strictly below `D`.
The geometric continuation is now quantitatively sharper:

> **Exterior-compatible finite-gap lemma after Section 160.** At an aligned gap scale
> actually arising from a global Target A monomer domain, either protect a toe-out
> witness with support bounded by (160.17) from all exterior blockers, or replace it
> with an architecture whose gain has order strictly below four and hence a smaller
> support exponent.

The toe-out theorem does not weaken any activation, cage, Hall-capacity, or
source/scaffold regression.  It only strengthens the free finite-gap branch.
