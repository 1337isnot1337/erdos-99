# Erdős Problem #99 — split-budget six-pair atomic gap `0.00234`

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r9`  
**Claim class:** proof-only strengthening of the six-pair theorem via the split-budget per-pair lemma  
**LEVEL I STATUS:** `STILL OPEN`

The split-budget per-pair theorem improves the TL69 missing payment from

\[
{(a+b-K)_+^2\over(4+\sqrt2)^2}
\]

to

\[
\boxed{
{(a+b-K)_+^2\over18},
\qquad K={2\over\sqrt3}.
}
\tag{SBS.1}
\]

The sharp six-label minimization proved in `target_c_six_pair_missing_budget_atomic_gap_001625_2026-09-14.md` is unchanged when the coefficient `c` is raised from `(4+sqrt(2))^{-2}` to `1/18`: its concavity requirements are only `12c<2` and `16c<2`, both of which remain strict.

Combining the two results gives

\[
\boxed{
 x\sigma\ge2\sqrt{\Delta_2}+0.00234,
 \qquad
 \Delta_2={\pi\over2\sqrt3}.
}
\tag{SBS.2}
\]

Thus at the same proof-only Type-II train-measure scope one may take

\[
\boxed{\eta_{grid}=0.00234.}
\tag{SBS.3}
\]

This is `2.6x` the LA90 value `0.0009` and approximately `44%` above the first six-pair value `0.001625`.

---

## 1. Sharp six-label lower payment with the new coefficient

Let

\[
x_i,y_i\ge0,
\qquad
\sum_i x_i=\sum_i y_i=s,
\]

and define

\[
\Phi_s(x,y)
:=\sum_i x_i y_i
+{1\over18}
\sum_{i\ne j}(x_i+y_j-K)_+^2.
\tag{SBS.4}
\]

For

\[
{2K\over3}<s<K,
\]

the same anti-diagonal concavity proof as SP.1 gives

\[
\boxed{
\Phi_s(x,y)
\ge {1\over9}
\left({3s\over2}-K\right)^2.
}
\tag{SBS.5}
\]

Equality remains, up to relabeling and shore exchange,

\[
x=(s,0,0),
\qquad
y=(0,s/2,s/2).
\tag{SBS.6}
\]

For completeness, the two curvature bounds used in that proof become

\[
-2+12/18=-{4\over3}<0
\]

for the general anti-diagonal redistribution, and

\[
-2+16/18=-{10\over9}<0
\]

for the one-common-label/two-exclusive reduction. Thus the stronger payment coefficient does not threaten the minimizing-pattern proof.

---

## 2. Dominant-orbit reduction

Assume for contradiction

\[
A:=x\sigma\le\bar A:=2s_2+\eta,
\qquad
s_2=\sqrt{\Delta_2},
\qquad
\eta=0.00234.
\tag{SBS.7}
\]

Use the same dominant-orbit Mantel reduction as Section 168, LA90, and the first six-pair theorem:

\[
M_0={4s_2^2\over\bar A},
\qquad
R_0=\bar A-M_0,
\]

\[
d_0={\bar A^2\over4}-s_2^2+{R_0^2\over4},
\tag{SBS.8}
\]

and equal trimmed shore mass

\[
\boxed{
s_0={M_0\over2}-\sqrt{d_0}.}
\tag{SBS.9}
\]

The total missing cross-shore pair budget is at most

\[
(2d_0+o(1))D^2.
\tag{SBS.10}
\]

Physically trim each shore inside its three atom windows to total mass `s_0D+o(D)`, and write the resulting label masses as `x_iD,y_iD`.

The three same-label blocks are completely missing. For every distinct-label block, the axes differ by `pi/3`, so the split-budget pair theorem gives missing mass at least

\[
{(x_i+y_j-K)_+^2\over18}D^2-o(D^2).
\]

Because the nine label-pair blocks are disjoint, the global missing budget implies

\[
2d_0
\ge
\sum_i x_i y_i
+{1\over18}\sum_{i\ne j}(x_i+y_j-K)_+^2.
\tag{SBS.11}
\]

Applying (SBS.5),

\[
\boxed{
d_0\ge
{1\over18}
\left({3s_0\over2}-K\right)^2.}
\tag{SBS.12}
\]

---

## 3. Exact contradiction at `eta=0.00234`

The exact interval certificate

`research/verify_target_c_split_budget_six_pair_atomic_gap_00234.py`

computes outward bounds for the same Mantel quantities and verifies

\[
\begin{aligned}
\bar A&=1.906965613727914\ldots,\\
M_0&=1.902288485095893\ldots,\\
R_0&=0.004677128632021\ldots,\\
d_0&=0.00223524975112181\ldots,\\
s_0&=0.903865814579984\ldots .
\end{aligned}
\tag{SBS.13}
\]

It also verifies the pair-lemma cutoff and minimization range

\[
{2K\over3}<s_0<K,
\]

with the stronger original-family bound

\[
{\bar A\over2}+\sqrt{d_0}<1.000762<K.
\]

The forced half-payment is

\[
{1\over18}
\left({3s_0\over2}-K\right)^2
=0.00224669330018161\ldots,
\tag{SBS.14}
\]

whereas

\[
d_0=0.00223524975112181\ldots .
\]

Hence

\[
\boxed{
{1\over18}
\left({3s_0\over2}-K\right)^2-d_0
>1.14\times10^{-5}.
}
\tag{SBS.15}
\]

This contradicts (SBS.12), proving (SBS.2).

---

## 4. Ceiling of the improved architecture

The six-label minimization is exact, so the remaining scalar ceiling of this architecture is the equality

\[
d_0(\eta)
={1\over18}
\left({3s_0(\eta)\over2}-K\right)^2.
\tag{SBS.16}
\]

Numerically,

\[
\boxed{
\eta_*=0.00234870846813\ldots .
}
\tag{SBS.17}
\]

Thus decimal tuning can recover less than `9e-6` beyond the certified `0.00234`. The next atomic improvement would need one of:

- a stronger correlation between the Ferrers inversion shape and residual missing degrees;
- a smaller opposite-corner loss than `4 sqrt(v)`;
- or a global coupling among the six distinct-label missing blocks beyond disjointness.

---

## 5. Immediate propagation

Every proof-only consequence depending only on the atomic train gain may now use

\[
\boxed{g=0.00234.}
\]

In particular,

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.00234,
}
\tag{SBS.18}
\]

and the rhombic-only/correlated transfers become

\[
\boxed{
\liminf {\sigma_R\over D}\ge0.00468,
}
\tag{SBS.19}
\]

\[
\boxed{
\liminf {\rho_{rec}+\sigma_R-q\over D}\ge0.00468.
}
\tag{SBS.20}
\]

The Section-171 endpoint and the low-`t` pentagon/network/tooth constants must be recomputed from `g=0.00234`; the SP1625 numbers are now superseded.

---

## 6. Scope audit

- Same full-core Type-II train-measure scope as Section 168/TL69/LA90.
- Same dominant three-direction orbit and finite Mantel stability.
- Same physical trimming argument used in the first six-pair theorem.
- The new per-pair input is exactly `target_c_split_budget_pair_payment_2026-09-14.md`.
- The six-label minimizer is unchanged and remains proved analytically, not numerically guessed.
- The exact script only certifies the final scalar inequalities; it is not used to establish the minimizer structure.
- No outer-detour, disk-topology, pseudosegment biclique, or source-deletion assumption is added.

**Disposition:** proof-only atomic strengthening. C-II and Level I remain open.
