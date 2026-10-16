# Erdős Problem #99 — iterative-pruning six-pair atomic gap `0.0035`

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r9`  
**Claim class:** proof-only strengthening of the atomic robust-grid theorem  
**LEVEL I STATUS:** `STILL OPEN`

The iterative-pruning per-pair theorem improves the strong missing-payment branch to

\[
\rho\ge {(a+b-K)_+^2\over 10},
\qquad K={2\over\sqrt3},
\]

whenever

\[
{(a+b-K)_+\over\min(a,b)}\le\sqrt{20\over29}.
\]

On the equal-trimmed dominant three-label shores used by the six-pair theorem, that strong branch applies uniformly. Combining it with the already proved sharp three-label minimization gives

\[
\boxed{
 x\sigma\ge 2\sqrt{\Delta_2}+0.0035,
 \qquad
 \Delta_2={\pi\over2\sqrt3}.
}
\tag{IP35.1}
\]

Thus at the same proof-only Type-II train-measure scope one may take

\[
\boxed{\eta_{grid}=0.0035.}
\tag{IP35.2}
\]

This supersedes the branch value `0.00234`.

---

## 1. Reuse the exact six-label minimizer with coefficient `1/10`

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
+{1\over10}\sum_{i\ne j}(x_i+y_j-K)_+^2.
\tag{IP35.3}
\]

The proof of the sharp three-label minimizer in
`target_c_six_pair_missing_budget_atomic_gap_001625_2026-09-14.md`
uses only the curvature conditions

\[
12c<2,
\qquad
16c<2.
\]

For `c=1/10` these become

\[
1.2<2,
\qquad
1.6<2,
\]

so the same concavity argument applies without modification. Therefore for

\[
{2K\over3}<s<K
\]

one has

\[
\boxed{
\Phi_s(x,y)
\ge {1\over5}\left({3s\over2}-K\right)^2.
}
\tag{IP35.4}
\]

Equality is still attained, up to relabeling and exchanging shores, by

\[
x=(s,0,0),
\qquad
y=(0,s/2,s/2).
\tag{IP35.5}
\]

So no new numerical optimization is hidden here: only the per-pair coefficient changes.

---

## 2. Dominant-orbit trimming

Assume for contradiction

\[
A:=x\sigma\le \bar A:=2s_2+\eta,
\qquad
s_2:=\sqrt{\Delta_2},
\qquad
\eta=0.0035.
\]

Use the audited dominant-orbit Mantel reduction. Put

\[
M_0={4s_2^2\over\bar A},
\qquad
R_0=\bar A-M_0,
\]

\[
d_0={\bar A^2\over4}-s_2^2+{R_0^2\over4},
\]

and trim the two Mantel shores to equal dominant-orbit mass

\[
\boxed{
s_0={M_0\over2}-\sqrt{d_0}.
}
\tag{IP35.6}
\]

The selected cross-shore missing-pair mass is at most

\[
(2d_0+o(1))D^2.
\tag{IP35.7}
\]

Write the three label masses on the selected shores as

\[
x_1,x_2,x_3,
\qquad
y_1,y_2,y_3,
\qquad
\sum_i x_i=\sum_i y_i=s_0.
\]

Same-label blocks are completely missing. Distinct-label axes differ by exactly `pi/3`.

---

## 3. The conditional strong branch is automatic after trimming

The iterative-pruning pair theorem gives the simple coefficient `1/10` whenever the family cap `S` satisfies

\[
2-{K\over S}\le\sqrt{20\over29}.
\tag{IP35.8}
\]

Every selected label family has mass at most `s_0`, so take `S=s_0`.
The exact interval certificate gives

\[
\begin{aligned}
\bar A&=1.908125613727914\ldots,\\
M_0&=1.901132033640687\ldots,\\
R_0&=0.006993580087227\ldots,\\
d_0&=0.00334838486463296\ldots,\\
s_0&=0.892700786633011\ldots .
\end{aligned}
\tag{IP35.9}
\]

It verifies

\[
{2K\over3}<s_0<K
\]

and, more strongly,

\[
2-{K\over s_0}<0.706509,
\]

whose square is below `0.49916`, whereas

\[
{20\over29}=0.689655\ldots .
\]

Therefore every oversized distinct-label block lies in the iterative-pruning strong branch. Hence the full missing budget obeys

\[
2d_0
\ge
\sum_i x_i y_i
+{1\over10}\sum_{i\ne j}(x_i+y_j-K)_+^2.
\tag{IP35.10}
\]

Apply (IP35.4):

\[
2d_0
\ge
{1\over5}\left({3s_0\over2}-K\right)^2.
\]

Equivalently a survivor would require

\[
\boxed{
d_0\ge
{1\over10}\left({3s_0\over2}-K\right)^2.
}
\tag{IP35.11}
\]

But the exact interval certificate gives

\[
{1\over10}\left({3s_0\over2}-K\right)^2
>0.00339851590473685,
\]

while

\[
d_0<0.00334838486463297.
\]

Thus the contradiction margin exceeds

\[
\boxed{5.0\times10^{-5}.}
\tag{IP35.12}
\]

This proves (IP35.1).

---

## 4. Scalar ceiling of this architecture

Keeping the same iterative-pruning coefficient and exact six-label minimizer, the scalar endpoint is the root of

\[
d_0(\eta)
={1\over10}
\left({3s_0(\eta)\over2}-K\right)^2.
\]

Numerically,

\[
\boxed{
\eta_*=0.00353466439218\ldots .
}
\tag{IP35.13}
\]

Thus `0.0035` is close to the scalar ceiling of the present architecture. Further decimal tuning is not useful. A further atomic gain requires new information beyond the total inversion/residual missing masses or beyond disjoint six-block payment.

---

## 5. Immediate propagation

Every proof-only consequence depending only on the atomic train gap may now use

\[
\boxed{g=0.0035.}
\]

In particular,

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.0035,
}
\tag{IP35.14}
\]

and the rhombic/correlated transfers become

\[
\boxed{
\liminf {\sigma_R\over D}\ge0.007,
}
\tag{IP35.15}
\]

\[
\boxed{
\liminf {\rho_{rec}+\sigma_R-q\over D}\ge0.007.
}
\tag{IP35.16}
\]

The Section-171 endpoint and all low-`t` pentagon/network/tooth constants should be recomputed from `g=0.0035`; the `0.00234` propagation is now superseded on this branch.

---

## 6. Scope audit

- Same full-core Type-II train-measure scope as audited Section 168 and the prior six-pair notes.
- Same dominant three-direction orbit and finite Mantel partition.
- Same physical equal-shore trimming.
- The new input is only the iterative-pruning conditional pair-payment theorem.
- Its conditional strong branch is verified uniformly after trimming, rather than assumed.
- The sharp six-label minimizer remains analytic; the script certifies only the final scalar inequalities.
- No outer-detour, disk-topology, pseudosegment biclique, source deletion, or KKT coefficient floor is added.

Run

```bash
python3 research/verify_target_c_iterative_pruning_six_pair_atomic_gap_0035.py
```

for the exact rational interval checks.

**Disposition:** proof-only atomic strengthening. C-II and Level I remain open.
