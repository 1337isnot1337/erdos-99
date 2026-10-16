# Target C-II — first-order critical high-`t` multishears live exactly on antipodal phase blocks

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural classification  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` fixed cusp chain; high-`t` multirow cusp injectivity; exact laminar finite multishear; audited Section-157 cut resultants; one-sided diameter-hub interval support  
**Certificate:** `research/verify_target_c_high_t_critical_phase_block_classification_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The multirow cusp-injectivity theorem shows that if every adjacent high-`t` row phase is distinct, every nonzero exact-full-support cancellation tangent has a force-visible first-order cusp. This note classifies the complementary degenerate case exactly.

Take any fixed `r>=2` high-`t` cusp chain

\[
\tau_0,\ldots,\tau_r
\tag{PB.1}
\]

on one side of the common diameter-routing hub. Write the coherent real row vectors as

\[
u_j=(\cos\alpha_j,\sin\alpha_j)
\tag{PB.2}
\]

and partition the indices into maximal consecutive **phase blocks**

\[
B_1,\ldots,B_s
\tag{PB.3}
\]

such that `u_j` is exactly constant on each block and adjacent blocks have different directions. The common phase window is `o(1)`, so for sufficiently large `D` different blocks are genuinely nonparallel, not opposite representatives of the same projective line.

Assume `s>=2`, so the row vectors span the plane and the exact-full-support cancellation manifold has tangent space

\[
\mathcal K
=\left\{c\in\mathbb R^{r+1}:\sum_{j=0}^r c_ju_j=0\right\}.
\tag{PB.4}
\]

Let `T(c)=(D_0(c),...,D_{r-1}(c))` be the interface KKT-derivative map from the multirow theorem:

\[
D_i(c)
=-2(F_{i+1}-F_i)\cdot JP_i(c),
\qquad
P_i(c)=\sum_{j=0}^ic_ju_j.
\tag{PB.5}
\]

Then the entire aggregate critical space is explicit.

### Theorem PB.1 — exact critical-space classification

For `c in K`,

\[
\boxed{
T(c)=0
\quad\Longleftrightarrow\quad
\sum_{j\in B_b}c_j=0
\text{ for every phase block }B_b.
}
\tag{PB.6}

Therefore

\[
\boxed{
\dim(\ker T\cap\mathcal K)
=\sum_{b=1}^s(|B_b|-1)
=(r+1)-s.
}
\tag{PB.7}

Since `dim K=r-1`, the quotient of exact-cancellation tangents by aggregate-critical tangents has dimension

\[
\boxed{s-2.}
\tag{PB.8}

The interpretation is direct:

- if every phase block is a singleton (`s=r+1`), the critical space is zero, recovering generic cusp injectivity;
- if exactly two distinct row directions occur (`s=2`), **every** exact-cancellation tangent is aggregate-critical;
- repeated equal-direction rows create all and only the first-order critical degrees of freedom.

### Theorem PB.2 — critical motion is supported only on exact-antipodal interfaces

If `c` satisfies (PB.6), then at every interface between two different phase blocks,

\[
\boxed{P_i(c)=0.}
\tag{PB.9}

Hence every switching diameter row at a non-antipodal interface has zero first relative velocity.

At an interface internal to a constant phase block, `u_i=u_{i+1}=v`. The physical strip boundary vectors are

\[
a_i=v,
\qquad
b_i=-v,
\tag{PB.10}
\]

so this is exactly the **antipodal strip** branch. There

\[
P_i(c)=\left(\sum_{j\in B_b,\,j\le i}c_j\right)v,
\tag{PB.11}
\]

and the switching rows move to first order along `+/- Jv`, exactly the antipodal opening line.

Thus

\[
\boxed{
\text{every first-order critical exact-cancellation multishear is carried entirely by exact-antipodal interfaces.}
}
\tag{PB.12}

This joins two previously separate live routes. The recent linear exact-antipodal/strong-TB1 fork is not merely a density dichotomy: within the exact-full-support multishear family, the strong non-antipodal branch cannot contribute a first-order critical degree of freedom at all. First-order criticality lives on the exact-antipodal side of the fork.

---

## 1. Phase blocks and the interface map

Let

\[
F_j=M_ju_j,
\qquad M_j>0,
\tag{PB.13}
\]

be the Section-157 cut resultants. The one-sided hub theorem and exact multishear give (PB.5) independently of which side of the hub contains the selected chain.

For a phase block

\[
B=[p,q]
\]

write its common unit vector as `v_B`. Suppose all earlier phase blocks have coefficient sum zero. Then

\[
P_{p-1}=0
\]

(with the evident convention at `p=0`) and for `p<=i<=q`,

\[
P_i
=\left(\sum_{j=p}^i c_j\right)v_B.
\tag{PB.14}
\]

For an internal interface `p<=i<q`, both resultants are parallel to `v_B`:

\[
F_{i+1}-F_i
=(M_{i+1}-M_i)v_B.
\]

Therefore

\[
D_i(c)=0
\tag{PB.15}
\]

**for every choice of the partial coefficient sum** inside the block.

At the terminal interface `q` of a nonlast block, let the next block direction be `w`, with `w` nonparallel to `v_B`. Then

\[
P_q
=\left(\sum_{j=p}^q c_j\right)v_B
\tag{PB.16}
\]

and

\[
\begin{aligned}
D_q(c)
&=-2(F_{q+1}-F_q)\cdot JP_q\\
&=-2M_{q+1}
\left(\sum_{j=p}^q c_j\right)
(w\cdot Jv_B).
\end{aligned}
\tag{PB.17}
\]

Because `M_{q+1}>0` and `w` is nonparallel to `v_B`, the last factor is nonzero. Hence

\[
\boxed{
D_q(c)=0
\quad\Longleftrightarrow\quad
\sum_{j\in B}c_j=0.
}
\tag{PB.18}

This is the block version of the coefficient-by-coefficient induction in the strict-phase theorem.

---

## 2. Proof of the critical-space classification

Assume first that `T(c)=0`.

Apply (PB.18) to the first phase block. Its coefficient sum is zero, so the prefix vector resets to zero at its terminal boundary. Apply the same argument to the second block, and continue. Every nonlast block has zero coefficient sum.

For the last block, the full-support kernel relation (PB.4), together with the vanishing sums of all previous blocks, becomes

\[
\left(\sum_{j\in B_s}c_j\right)v_{B_s}=0.
\]

Thus the last block sum also vanishes. This proves the forward implication in (PB.6).

Conversely, suppose every block coefficient sum is zero. At a block boundary the prefix vector is zero, so (PB.5) gives `D_i=0`. At an internal interface the prefix vector and the resultant difference are both parallel to the common block direction, so their `J`-pairing vanishes. Therefore `T(c)=0` on every interface. The same block-sum conditions also imply the full kernel equation (PB.4). This proves the reverse implication.

On a block of size `m`, the condition that its coefficients sum to zero leaves `m-1` independent coordinates. Summing over the `s` blocks proves (PB.7). Equation (PB.8) follows from `dim K=(r+1)-2=r-1`.

---

## 3. Why the moving critical interfaces are exactly antipodal

Take a critical tangent `c` satisfying (PB.6). At the end of every phase block, its coefficient sum is zero, hence `P_i=0`. The one-sided support normal form says that switching rows at interface `i` have first relative velocity `+JP_i` or `-JP_i`, depending only on the side of the hub. Therefore every switching row at a boundary between distinct row directions has zero first derivative vector.

Inside a phase block, write the common direction as `v`. The two physical boundary-contact vectors for the adjacent strip are

\[
a_i=u_i=v,
\qquad
b_i=-u_{i+1}=-v.
\]

Hence the opening cone is the antipodal line

\[
\Omega_i=\{tJv:t\in\mathbb R\}.
\tag{PB.19}
\]

The prefix vector has the form `P_i=s_i v`, so every switching-row velocity is

\[
\pm JP_i
=\pm s_iJv\in\Omega_i.
\tag{PB.20}
\]

Thus every interface at which a critical tangent can have a nonzero first switching velocity is exactly an antipodal interface. This proves (PB.12).

This is stronger than saying a critical tangent needs *some* phase equality. It classifies the whole tangent: after compressing each maximal equal-phase run to one block, all block-level coefficients vanish.

---

## 4. Second-order radial charge of a critical phase block

The classification also exposes the next finite-dimensional quantity.

Let a smooth exact-cancellation curve tangent to a critical vector have

\[
\theta_j(t)=t c_j+t^2d_j+o(t^2).
\tag{PB.21}
\]

On a phase block `B` with common unit direction `v_B`, use

\[
\sum_{j\in B}c_j=0.
\]

Expanding its contribution to the full-support displacement gives

\[
\begin{aligned}
\sum_{j\in B}(R_{\theta_j(t)}v_B-v_B)
&=t^2\left[
Jv_B\sum_{j\in B}d_j
-{1\over2}v_B\sum_{j\in B}c_j^2
\right]
+o(t^2).
\end{aligned}
\tag{PB.22}
\]

Define

\[
D_B:=\sum_{j\in B}d_j,
\qquad
Q_B:=\sum_{j\in B}c_j^2.
\tag{PB.23}
\]

Then exact full-support cancellation at second order requires

\[
\boxed{
\sum_{B}
\left(Jv_BD_B-{1\over2}v_BQ_B\right)=0.
}
\tag{PB.24}
\]

Every active critical phase block has `Q_B>0`, so it carries an unavoidable inward radial second-order charge `-(Q_B/2)v_B`. The exact finite manifold can cancel these charges only through the second-order mean-rotation variables `D_B` across the distinct phase blocks.

Equation (PB.24) is the correct second-order interface for the next curvature calculation. It is the multi-block version of the one-sided quadratic drift in the exactly parallel three-row regression.

---

## 5. Frontier effect

The current high-`t` first-order picture can now be stated sharply.

```text
exact full-support multishear tangent
        |
        +-- distinct adjacent phase interface
        |       -> no aggregate-critical degree of freedom there
        |
        +-- repeated exact phase block
                -> block coefficients may sum to zero
                -> first-order motion occurs only on internal antipodal strips
                -> each active block carries second-order radial charge Q_B/2
```

Consequences:

1. the strong-TB1 side of the linear blocker fork cannot be neutralized merely by adding more exact-cancellation coordinates; it remains a genuinely geometric diameter-thrackle/lattice-ladder obstruction;
2. the exact-antipodal side is the **only** branch that supports first-order critical exact-cancellation multishears;
3. the next multishear calculation should be second-order and blockwise, using (PB.24) together with the exact interval-Gram/KKT curvature identity and the antipodal switching geometry.

This does not close the exact-antipodal branch. It removes the generic non-antipodal branch from the first-order critical-kernel program and gives an exact normal form for what remains.

**Disposition:** proved proof-only classification of the aggregate-critical high-`t` exact-cancellation space; first-order critical multishears are supported exactly on constant-phase blocks and move only exact-antipodal interfaces. C-II and Level I remain open.
