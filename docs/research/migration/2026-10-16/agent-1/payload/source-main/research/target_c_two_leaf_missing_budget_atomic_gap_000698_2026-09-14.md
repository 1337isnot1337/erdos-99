# Erdős Problem #99 — two-leaf missing-budget amplification of the atomic gap

**Date:** 2026-09-14  
**Repository base:** `d03ba81c` on `research/c2-gluing-sol-20260914`  
**Target:** Target C-II, canonical full-core Type-II branch  
**Claim class:** proof-only strengthening of AG47 / audited-working §168  
**External input:** none beyond the existing stopped-train and robust-grid stack

## LEVEL I STATUS

`STILL OPEN`

AG47 sharpened the all-regime atomic train gap to `0.00047` by replacing phase-Markov deletion with the exact chain-graph cover. Its own method ceiling was about `0.00047649` because it selected only one center-to-leaf atom pair from the dominant three-direction orbit and pessimistically allowed the entire Mantel missing-pair budget to damage that one pair.

That loss is avoidable. After the dominant-orbit Mantel partition and majority assignment, one shore consists of one atom class while the other shore consists of the remaining one or two atom classes. Every center-to-leaf pair must separately pay enough missing crossings to avoid the same Section-76 diameter contradiction. The two missing budgets are disjoint subsets of the global cross-shore missing budget, so their required payments add.

The resulting gain is

\[
\boxed{
 x\sigma\ge 2\sqrt{\Delta_2}+0.000698,
 \qquad
 \Delta_2={\pi\over2\sqrt3}.
}
\tag{TL.1}
\]

Thus, at the same proof-only scope, one may take

\[
\boxed{\eta_{\rm grid}=0.000698.}
\tag{TL.2}
\]

This is a roughly 48 percent increase over AG47 and is not obtained by retuning the old one-pair inequality.

---

## 1. A per-pair missing-budget payment lemma

Consider two stopped-train atom families `A_D,B_D` with

\[
{|A_D|\over D}\to a,
\qquad
{|B_D|\over D}\to b,
\tag{TL.3}
\]

whose projective direction windows shrink to axes separated by `pi/3`. Let at most

\[
(\rho+o(1))D^2
\tag{TL.4}
\]

cross-family pairs be missing. Put

\[
K:={2\over\sqrt3},
\qquad
L:=4+\sqrt2.
\tag{TL.5}
\]

Assume

\[
a\le K,
\qquad
b\le K.
\tag{TL.6}
\]

### Lemma TL.1 — each oversized pair must pay quadratic missing mass

\[
\boxed{
\rho\ge
\left({(a+b-K)_+\over L}\right)^2.
}
\tag{TL.7}
\]

Here `(t)_+=max(t,0)`.

### Proof

If

\[
\min\{a,b\}\le L\sqrt\rho,
\]

then, because `max{a,b}<=K`,

\[
(a+b-K)_+
\le \min\{a,b\}
\le L\sqrt\rho,
\]

which is (TL.7).

It remains to consider

\[
\min\{a,b\}>L\sqrt\rho.
\tag{TL.8}
\]

Use the AG47 chain-cover argument with the actual pairwise missing budget `rho`, rather than the global dominant-orbit bound.

Choose projective lifts `x_u,y_v` as in §§163/168. Every phase inversion is a missing pair, and the inversion graph is a chain graph. If it has `m` edges, its minimum vertex cover has size at most `sqrt(2m)`. Therefore all inversions are removed after deleting, in total across the two shores,

\[
(\sqrt{2\rho}+o(1))D
\tag{TL.9}
\]

trains.

The remaining missing-pair count is still at most `(rho+o(1))D^2`. Delete every remaining train missing more than `(sqrt(rho)+o(1))D` opposite trains. Markov deletes at most

\[
(\sqrt\rho+o(1))D
\]

trains from each shore.

By (TL.8), even if the entire chain-cover deletion falls on the smaller shore, its retained normalized size exceeds

\[
L\sqrt\rho-(\sqrt2+1)\sqrt\rho
=3\sqrt\rho.
\]

Hence every two and every three retained trains on one shore have a common neighbor on the other. The actual-`K_{2,2}` consistency argument of §163 therefore gives one global crossing order on each retained shore.

Take the usual opposite-corner two-leg path. Relative to the original pair sizes, the selected degree sum loses at most

- `sqrt(2rho)` from the chain cover;
- `2sqrt(rho)` from degree pruning; and
- `2sqrt(rho)` from the two corner degree deficits.

Thus the Section-76 projection estimate gives

\[
1\ge {\sqrt3\over2}
\left[a+b-(4+\sqrt2)\sqrt\rho\right].
\tag{TL.10}
\]

Equivalently,

\[
a+b-K\le L\sqrt\rho,
\]

which proves (TL.7). `square`

The point of TL.1 is that it remains valid even when a family is too small for the robust-grid pruning: failure of the size hypothesis already costs at least the same missing mass.

---

## 2. Dominant-orbit constants at `eta=0.000698`

Put

\[
s_2:=\sqrt{\Delta_2},
\qquad
\eta:=0.000698,
\qquad
\bar A:=2s_2+\eta.
\tag{TL.11}
\]

Assume for contradiction that the total absolute atomic train mass satisfies

\[
A=x\sigma\le\bar A.
\tag{TL.12}
\]

Use exactly the dominant-orbit reduction of §168/AG47. A dominant three-direction projective orbit has mass at least

\[
M_0={4s_2^2\over\bar A},
\tag{TL.13}
\]

and the total atomic mass outside it is at most

\[
R_0=\bar A-M_0.
\tag{TL.14}
\]

A conservative upper bound for the dominant-orbit Mantel deficit is

\[
d_0={\bar A^2\over4}-s_2^2+{R_0^2\over4}.
\tag{TL.15}
\]

The maximum-degree Mantel partition has shore imbalance at most `sqrt(d_0)D+o(D)` and at most `(2d_0+o(1))D^2` missing cross-shore pairs. Majority assignment of the at most three atom windows discards at most `sqrt(6d_0)D+o(D)` total atom mass. Therefore each shore retains assigned atom mass at least

\[
\boxed{
S_0={M_0\over2}-\sqrt{d_0}-\sqrt{6d_0}.
}
\tag{TL.16}
\]

Exact interval arithmetic gives

\[
\begin{aligned}
\bar A&=1.905323613727914\ldots,\\
M_0&=1.903927869434607\ldots,\\
R_0&=0.001395744293307\ldots,\\
d_0&=0.000665323165724\ldots,\\
S_0&=0.862988282428460\ldots .
\end{aligned}
\tag{TL.17}
\]

Every atom family lies inside one Mantel shore. Also

\[
{\bar A\over2}+\sqrt{d_0}
<0.978456
<K=1.1547005\ldots,
\tag{TL.18}
\]

so the size hypothesis (TL.6) is automatic for every center-to-leaf atom pair below.

---

## 3. One center atom versus the two leaf atoms

After majority assignment, every positive dominant-orbit atom is assigned to exactly one Mantel shore. Both shores have assigned mass at least `S_0`. Since the orbit contains at most three atom windows, one shore contains exactly one assigned atom class after possibly renaming the shores. Call its normalized mass `a`. Call the one or two classes on the opposite shore `b,c`, allowing `c=0` if only two atom classes are present.

Then

\[
\boxed{
a\ge S_0,\qquad b+c\ge S_0.}
\tag{TL.19}
\]

Let `rho_b,rho_c` be the normalized missing-pair masses between the center class and the two leaf classes. These pair sets are disjoint subsets of the Mantel cross-shore missing pairs, hence

\[
\boxed{
\rho_b+\rho_c\le2d_0.
}
\tag{TL.20}
\]

Apply Lemma TL.1 separately to the two center-to-leaf pairs:

\[
\rho_b\ge { (a+b-K)_+^2\over L^2},
\qquad
\rho_c\ge { (a+c-K)_+^2\over L^2}.
\tag{TL.21}
\]

The function

\[
\phi_a(t):=(a+t-K)_+^2
\]

is convex and nondecreasing in both `a` and `t`. Therefore (TL.19), Jensen's inequality, and monotonicity give

\[
\begin{aligned}
\phi_a(b)+\phi_a(c)
&\ge \phi_{S_0}(b)+\phi_{S_0}(c)\\
&\ge 2\phi_{S_0}\left({b+c\over2}\right)\\
&\ge2\phi_{S_0}\left({S_0\over2}\right).
\end{aligned}
\tag{TL.22}
\]

The exact certificate verifies

\[
{3S_0\over2}>K,
\tag{TL.23}
\]

so (TL.22) becomes

\[
\boxed{
\rho_b+\rho_c
\ge
2\left({3S_0/2-K\over L}\right)^2.
}
\tag{TL.24}
\]

Combine (TL.20) and (TL.24): every survivor under (TL.12) would have to satisfy

\[
\boxed{
d_0\ge
\left({3S_0/2-K\over L}\right)^2.}
\tag{TL.25}
\]

But exact rational interval arithmetic gives

\[
\left({3S_0/2-K\over L}\right)^2
>0.0006665473748734,
\tag{TL.26}
\]

while

\[
d_0<0.0006653231657242.
\tag{TL.27}
\]

The gap is more than

\[
1.22\times10^{-6}.
\tag{TL.28}
\]

Contradiction. Therefore (TL.1) holds.

---

## 4. Why this beats the AG47 ceiling

AG47 chose one leaf atom of mass at least `S_0/2` and charged the entire missing-pair budget `2d_0` to that one pair. Its closing expression was

\[
{\sqrt3\over2}
\left[{3S_0\over2}-(4+\sqrt2)\sqrt{2d_0}\right]>1,
\]

whose numerical root is about `0.00047649`.

The present proof instead observes that both center-to-leaf pairs must individually avoid a diameter contradiction. If the two leaf classes split the opposite-shore mass evenly, which is the worst case by convexity, they must each consume missing-pair budget. This replaces the effective `sqrt(2d_0)` loss by `sqrt(d_0)` after the two payments are combined. The new method ceiling is near `0.00069865`, so `0.000698` is deliberately kept below the root.

No additional geometric hypothesis is introduced.

---

## 5. Immediate propagation

Every proof-only propagation that depends only on the atomic gain may replace `0.00047` by `0.000698`. In particular,

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.000698,
}
\tag{TL.29}
\]

and the rhombic-only transfer gives

\[
\boxed{
\liminf {\sigma_R\over D}\ge0.001396.
}
\tag{TL.30}
\]

The correlated stopped-train identity similarly becomes

\[
\boxed{
\liminf {\rho_{rec}+\sigma_R-q\over D}\ge0.001396.
}
\tag{TL.31}
\]

Downstream `q-k`, chamber, and residual constants should be recomputed from these stronger inputs rather than copied from the earlier AG42/AG47 values.

---

## 6. Scope audit

- The theorem is full-core Type-II and inherits the §142 train-measure scope.
- It uses the same dominant-orbit and finite Mantel-stability bounds as audited-working §168 and AG47.
- The new step is only the disjoint payment of the two center-to-leaf missing budgets.
- The phase-inversion cover is the exact chain-graph cover from AG47.
- No complete pseudosegment biclique theorem, no disk topology, no outer-detour hypothesis, and no source deletion are used.
- Contact-isolated source points remain in the source throughout.
- The result is proof-only pending independent audit/promotion.

C-II and Level I remain open.
