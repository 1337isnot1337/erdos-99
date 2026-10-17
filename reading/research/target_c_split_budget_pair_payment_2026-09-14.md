> Generated reading edition · [exact source](../../research/target_c_split_budget_pair_payment_2026-09-14.md) · source SHA-256 `4dd6d3e289a4fefd65d04f0c068498abdd66eaf2407e4379f3c24d0a9761a98c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Erdős Problem #99 — split-budget sharpening of the atomic per-pair payment

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r9`  
**Claim class:** proof-only strengthening of the TL69 / AG47 per-pair missing-budget lemma  
**LEVEL I STATUS:** `STILL OPEN`

TL69 uses the pairwise payment

```math
\rho\ge
\left({(a+b-K)_+\over4+\sqrt2}\right)^2,
\qquad K={2\over\sqrt3},
```

for two atomic stopped-train families of normalized masses `a,b` whose limiting projective axes differ by `pi/3`.

The coefficient `4+sqrt(2)` is not sharp even inside the existing chain-cover proof. It charges the full missing-pair budget once to the phase-inversion cover and then charges the same full budget again to degree pruning and the two selected corner deficits. Those are not independent budgets: every inversion is itself a missing pair, and after an inversion cover is removed, all inversion edges have disappeared from the residual missing graph.

Keeping that correlation lowers the loss constant to `3 sqrt(2)` and proves

```math
\boxed{
\rho\ge{(a+b-K)_+^2\over18}.
}
\tag{SB.1}
```

This is a factor

```math
{(4+\sqrt2)^2\over18}=1.628539\ldots
```

increase in the forced missing payment for a fixed oversized pair.

---

## 1. Setup

Let `A_D,B_D` be stopped-train atom families with

```math
{|A_D|\over D}\to a,
\qquad
{|B_D|\over D}\to b,
\tag{SB.2}
```

whose shrinking projective direction windows converge to axes separated by `pi/3`. Assume

```math
a\le K,
\qquad b\le K,
\tag{SB.3}
```

and let the number of missing `A_D`--`B_D` pairs be

```math
M_D=(\rho+o(1))D^2.
\tag{SB.4}
```

As in AG47/TL69, choose the projective lifts and phase coordinates. Every phase inversion is a missing pair, and the inversion graph is a chain graph.

Pass to a further subsequence so the normalized inversion-edge count has a limit

```math
{I_D\over D^2}\to u,
\qquad0\le u\le\rho.
\tag{SB.5}
```

Put

```math
v:=\rho-u.
\tag{SB.6}
```

---

## 2. The inversion cover consumes only the inversion part of the budget

For a chain graph with `I` edges, the minimum vertex-cover size is at most

```math
\sqrt{2I}+O(1).
```

This is the AG47 Ferrers/Koenig estimate: a matching of size `r` forces at least `r(r+1)/2` edges.

Therefore all phase inversions can be removed by deleting, in total across both families,

```math
(\sqrt{2u}+o(1))D
\tag{SB.7}
```

trains.

The key bookkeeping point is that the residual missing graph does **not** still have budget `rho`. Every one of the `I_D` inversion edges is incident to the chosen cover and is gone. Hence after the cover deletion the remaining missing-pair count is at most

```math
M_D-I_D
=(v+o(1))D^2.
\tag{SB.8}
```

Any additional non-inversion missing edges incident to the cover only improve this bound.

---

## 3. Residual degree pruning costs `4 sqrt(v)`, not `4 sqrt(rho)`

If `v>0`, delete every remaining train whose residual missing degree exceeds

```math
(\sqrt v+o(1))D.
```

By (SB.8), this deletes at most

```math
(\sqrt v+o(1))D
```

trains from each family. If `v=0`, no such deletion is needed.

Every retained train therefore misses at most `(sqrt(v)+o(1))D` opposite retained trains.

Assume first that

```math
\min\{a,b\}>\sqrt{2u}+4\sqrt v.
\tag{SB.9}
```

Even if the entire inversion-cover loss falls on the smaller family, after residual degree pruning each retained family has normalized mass greater than

```math
3\sqrt v+o(1).
\tag{SB.10}
```

Consequently every pair and every triple on either retained shore has a common neighbor on the other. The same actual-`K_{2,2}` consistency and triple-neighbor transitivity argument used in Section 163, AG47, and TL69 therefore globalizes the crossing orders. No new pseudosegment theorem is being invoked.

Take the usual opposite-corner two-leg path. Relative to the original pair masses `a+b`, its selected degree sum loses at most

- `sqrt(2u)` from the inversion cover, total across both shores;
- `2 sqrt(v)` from residual degree pruning, one `sqrt(v)` allowance per shore;
- `2 sqrt(v)` from the two selected corner missing-degree deficits.

Thus the Section-76 projection estimate gives

```math
1\ge{\sqrt3\over2}
\left[a+b-\sqrt{2u}-4\sqrt v\right]-o(1).
\tag{SB.11}
```

Equivalently,

```math
a+b-K\le\sqrt{2u}+4\sqrt v.
\tag{SB.12}
```

---

## 4. Collapse the split budget by Cauchy

Since `u,v>=0` and `u+v=rho`, Cauchy gives

```math
\begin{aligned}
\sqrt{2u}+4\sqrt v
&=(\sqrt2,4)\cdot(\sqrt u,\sqrt v)\\
&\le\sqrt{2+16}\sqrt{u+v}\\
&=3\sqrt2\,\sqrt\rho.
\end{aligned}
\tag{SB.13}
```

Therefore the large-family case (SB.9) implies

```math
(a+b-K)_+\le3\sqrt2\,\sqrt\rho.
\tag{SB.14}
```

If (SB.9) fails, then

```math
\min\{a,b\}
\le\sqrt{2u}+4\sqrt v
\le3\sqrt2\sqrt\rho.
\tag{SB.15}
```

Because `max{a,b}<=K`,

```math
(a+b-K)_+\le\min\{a,b\},
```

so (SB.14) holds in the small-family case as well.

Squaring (SB.14) proves

```math
\boxed{
\rho\ge{(a+b-K)_+^2\over18}.
}
```

`square`

---

## 5. Why the improvement is legitimate

The argument does not assume that inversion and non-inversion missing pairs are statistically independent. It only uses the deterministic set inclusion

```math
E_{inv}\subseteq E_{miss}.
```

Once a vertex cover of `E_inv` is deleted, every inversion edge is absent from the residual graph. Therefore the residual missing count is bounded by `M_D-I_D`, regardless of how the remaining missing edges are arranged.

The old coefficient `4+sqrt(2)` corresponds to replacing both `u` and `v` by the full `rho`. Equation (SB.13) is the exact correction for that double charge.

Within this bookkeeping architecture, the coefficient `3sqrt(2)` is the worst-case Cauchy envelope, attained at the budget split

```math
u:\!v=1:\!8.
```

Further improvement would have to correlate the Ferrers shape of the inversion graph with the residual missing-degree distribution, or sharpen the opposite-corner loss itself.

---

## 6. Scope

- Same pairwise train-measure scope as TL69/AG47.
- Same phase-inversion chain-graph theorem.
- Same Section-163 `K_{2,2}` consistency and triple-neighbor globalization.
- Same Section-76 opposite-corner projection contradiction.
- No outer-detour, disk-topology, or source-deletion assumption.
- The only new step is the disjoint accounting `M_res<=M-I` before degree pruning.

**Disposition:** proof-only strengthening of the per-pair missing-payment lemma. C-II and Level I remain open.
