# Erdős Problem #99 — three-label concentration raises the atomic train gap to 0.00109

**Date:** 2026-09-14  
**Repository base:** `ca7e8d2b` on `research/c2-gluing-sol-20260914`  
**Target:** Target C-II, canonical full-core Type-II branch  
**Claim class:** proof-only strengthening of TL69 / audited-working §168  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`

TL69 improved the all-regime atomic train gap to `0.000698` by charging both center-to-leaf pairs in the dominant three-direction orbit. It still inherited the old majority-assignment loss: before using those two pair payments, it discarded the minority population of every atom window.

With only three phase labels, that discard is unnecessary. If the same-label overlap across a near-Mantel partition is small, one of the two shores is automatically almost concentrated on one label. The contamination of that same label on the opposite shore is then bounded directly by the overlap product. This keeps nearly the entire opposite shore as the two leaf families.

The resulting safe gain is

\[
\boxed{
 x\sigma\ge2\sqrt{\Delta_2}+0.00109,
 \qquad
 \Delta_2={\pi\over2\sqrt3}.
}
\tag{TC109.1}
\]

Thus all proof-only uses of the atomic train gap may take

\[
\boxed{\eta_{grid}=0.00109.}
\tag{TC109.2}
\]

This is more than twice the audited-working `0.0004` constant and about 56 percent larger than TL69.

---

## 1. A sharp three-label concentration lemma

Let

\[
p=(p_1,p_2,p_3),\qquad q=(q_1,q_2,q_3)
\]

be nonnegative probability vectors, and put

\[
\sigma:=p\cdot q.
\]

Define the concentration deficits

\[
r_p:=1-\max_i p_i,
\qquad
r_q:=1-\max_i q_i.
\]

### Lemma 1.1

If `sigma<1/4`, then

\[
\boxed{\min\{r_p,r_q\}\le\sqrt\sigma.}
\tag{TC109.3}
\]

### Proof

First suppose `r_p,r_q<=1/2`.

If the maximizing coordinates of `p` and `q` agree, then

\[
\sigma\ge(1-r_p)(1-r_q)\ge r_pr_q.
\]

If their maximizing coordinates are different, rename them `1` for `p` and `2` for `q`, and write

\[
p=(1-r_p,\ r_p-a,\ a),
\qquad
q=(r_q-b,\ 1-r_q,\ b),
\]

with `0<=a<=r_p`, `0<=b<=r_q`. The difference

\[
p\cdot q-r_pr_q
\]

is bilinear in `(a,b)`, so its minimum on the rectangle occurs at a corner. At the four corners its values are

\[
r_p+r_q-3r_pr_q,
\qquad
r_p(1-2r_q),
\qquad
r_q(1-2r_p),
\qquad
0,
\]

all nonnegative when `r_p,r_q<=1/2`. Hence again

\[
\sigma\ge r_pr_q.
\tag{TC109.4}
\]

Therefore if both deficits are at most `1/2`, at least one is at most `sqrt(sigma)`.

Next suppose both deficits exceed `1/2`. Then every coordinate of both probability vectors is strictly below `1/2`. The polytope of probability triples with all coordinates at most `1/2` is the convex hull of the three permutations of

\[
(1/2,1/2,0).
\]

The bilinear form `p dot q` attains its minimum over the product of these two polytopes at a pair of vertices. Two such vertices have scalar product at least `1/4`. Thus `sigma>=1/4`, contrary to the hypothesis.

Finally suppose, without loss of generality,

\[
r_p>1/2,
\qquad
r_q\le1/2.
\]

Then every coordinate of `p` is below `1/2`. For fixed `q`, the minimum of `p dot q` under that cap is obtained by putting weight `1/2` on each of the two smallest coordinates of `q`. Their sum is exactly `r_q`, so

\[
\sigma\ge {r_q\over2}\ge r_q^2.
\]

Hence `r_q<=sqrt(sigma)`. The other asymmetric case is identical. This proves the lemma. `square`

### Corollary 1.2 — unnormalized form

Let nonnegative triples `x_i,y_i` have totals `X,Y>0`, and put

\[
S:=\sum_i x_i y_i.
\]

If `S<XY/4`, then one of the shores, say the `x` shore after relabeling, has a label `i` satisfying

\[
\boxed{
x_i\ge X-\sqrt{S X/Y}.}
\tag{TC109.5}
\]

For that same label,

\[
y_i\le {S\over x_i},
\tag{TC109.6}
\]

so the other two labels on the opposite shore have total mass at least

\[
\boxed{Y-{S\over x_i}.}
\tag{TC109.7}
\]

---

## 2. Dominant-orbit envelope at `eta=0.00109`

Put

\[
s_2:=\sqrt{\Delta_2},
\qquad
\eta:=0.00109,
\qquad
\bar A:=2s_2+\eta.
\]

Assume for contradiction that the total absolute atomic train mass satisfies

\[
A=x\sigma\le\bar A.
\tag{TC109.8}
\]

Use the audited §168 dominant-orbit reduction exactly as before. The dominant three-direction projective orbit has mass at least

\[
M_0={4s_2^2\over\bar A},
\tag{TC109.9}
\]

while the total mass outside that orbit is at most

\[
R_0=\bar A-M_0.
\]

Its conservative Mantel deficit is

\[
\boxed{
d_0={\bar A^2\over4}-s_2^2+{R_0^2\over4}.}
\tag{TC109.10}
\]

The maximum-degree Mantel partition of the finite dominant-orbit graph has shores `X_D,Y_D` satisfying, after normalization by `D`,

\[
X,Y\ge u_0:= {M_0\over2}-\sqrt{d_0},
\tag{TC109.11}
\]

and

\[
X,Y\le v_0:= {\bar A\over2}+\sqrt{d_0},
\tag{TC109.12}
\]

with at most

\[
(m_0+o(1))D^2,
\qquad
m_0:=2d_0,
\tag{TC109.13}
\]

missing cross-shore pairs.

For the three atom windows write normalized shore populations `x_i,y_i`. Same-window trains do not cross, so every same-label cross pair is missing and

\[
S:=\sum_i x_i y_i\le m_0+o(1).
\tag{TC109.14}
\]

The exact certificate verifies

\[
{m_0\over u_0^2}<0.00246<\frac14,
\tag{TC109.15}
\]

so Corollary 1.2 applies.

---

## 3. Recover one center label without majority discard

After swapping shores if necessary, Corollary 1.2 yields one center atom class of normalized mass

\[
a\ge X-\sqrt{S X/Y}.
\]

Using `X>=u_0`, `X<=v_0`, `Y>=u_0`, and `S<=m_0`, we have the uniform lower bound

\[
\boxed{
a\ge a_0:=u_0-\sqrt{m_0v_0/u_0}.}
\tag{TC109.16}
\]

The same label occupies at most `S/a<=m_0/a_0` mass on the opposite shore. Hence the other two labels there, the two leaf families, have total normalized mass

\[
\boxed{
b+c\ge B_0:=u_0-{m_0\over a_0}.}
\tag{TC109.17}
\]

No atom population was deleted to obtain these bounds.

The exact interval certificate gives

\[
\begin{aligned}
d_0&=0.0010395054050289\ldots,\\
u_0&=0.919526756872364\ldots,\\
v_0&=0.985099168575723\ldots,\\
a_0&=0.872332824651825\ldots,\\
B_0&=0.917143479811929\ldots .
\end{aligned}
\tag{TC109.18}

Also

\[
v_0<{2\over\sqrt3},
\tag{TC109.19}
\]

so every center-to-leaf pair satisfies the size hypothesis in the TL69 per-pair payment lemma.

---

## 4. Both leaf families must pay missing-pair budget

Let `rho_b,rho_c` be the normalized missing-pair masses between the center family and the two leaf families. They are disjoint subsets of the global missing cross-shore pairs, hence

\[
\rho_b+\rho_c\le m_0=2d_0.
\tag{TC109.20}
\]

TL69 proves for each pair, with

\[
K={2\over\sqrt3},
\qquad
L=4+\sqrt2,
\]

that

\[
\rho_b\ge{(a+b-K)_+^2\over L^2},
\qquad
\rho_c\ge{(a+c-K)_+^2\over L^2}.
\tag{TC109.21}
\]

The function `(a+t-K)_+^2` is convex and nondecreasing in both variables. Therefore (TC109.16)--(TC109.17) and Jensen give

\[
\rho_b+\rho_c
\ge
2\left({a_0+B_0/2-K\over L}\right)^2.
\tag{TC109.22}
\]

The positive-part symbol can be removed because the exact certificate gives

\[
a_0+{B_0\over2}-K
>0.17620.
\tag{TC109.23}
\]

Combining (TC109.20) and (TC109.22) would require

\[
d_0\ge
\left({a_0+B_0/2-K\over L}\right)^2.
\tag{TC109.24}
\]

But exact rational interval arithmetic proves

\[
\left({a_0+B_0/2-K\over L}\right)^2
>0.0010591583402899,
\]

while

\[
d_0<0.0010395054050290.
\]

The contradiction margin exceeds

\[
1.9\times10^{-5}.
\tag{TC109.25}
\]

Therefore the assumption (TC109.8) is impossible, proving (TC109.1).

---

## 5. Immediate consequences

Every downstream proof-only statement depending only on the atomic gap can replace the previous value by `0.00109`. In particular,

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.00109,
}
\tag{TC109.26}
\]

and the rhombic-only transfer becomes

\[
\boxed{
\liminf {\sigma_R\over D}\ge0.00218.
}
\tag{TC109.27}
\]

The correlated stopped-train identity similarly gives

\[
\boxed{
\liminf {\rho_{rec}+\sigma_R-q\over D}\ge0.00218.
}
\tag{TC109.28}
\]

The §171 `q-k` endpoint and all chamber/residual coefficients should be rerun with `g=0.00109`; the older TL69 propagation is no longer numerically current.

---

## 6. Scope audit

- The only new combinatorics is the three-label concentration lemma; it is finite and exact.
- Same-label pairs are used only as a subset of missing Mantel cross edges.
- No majority assignment or deletion of atom windows is used.
- The center label may lie on either Mantel shore; the proof swaps shores after applying Lemma 1.1.
- The two leaf labels may have arbitrarily unequal masses, including one zero mass; Jensen handles that endpoint.
- The TL69 per-pair payment lemma already covers small leaf families, so no hidden minimum-size hypothesis is introduced.
- No new pseudosegment theorem, outer-detour hypothesis, or source deformation is used.
- The result remains proof-only pending independent audit/promotion.

C-II and Level I remain open.
