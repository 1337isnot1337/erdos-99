> Generated reading edition · [exact source](../../research/target_c_iterative_pruning_conditional_pair_payment_2026-09-14.md) · source SHA-256 `7ea4590a3e0d543b7bc4b10879208f189b45a4a40b94095c96b1af9a8097af8b`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Erdős Problem #99 — iterative-pruning conditional per-pair payment

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r9`  
**Claim class:** proof-only strengthening of the atomic pair-payment stack  
**LEVEL I STATUS:** `STILL OPEN`

The split-budget pair lemma already corrects one double charge by separating inversion missing mass from residual missing mass. Its residual step, however, still prunes high-missing-degree trains independently on the two shores. That double counts residual missing edges: once a train is deleted, all incident missing edges disappear and cannot justify another deletion later.

Iterative pruning across both shores removes this second double charge. It yields the following sharper dichotomy.

Let

```math
K={2\over\sqrt3}.
```

For two atom families of normalized masses `a,b<=K` whose limiting axes differ by `pi/3`, and normalized missing-pair mass `rho`, put

```math
g_*:=(a+b-K)_+,
\qquad m_*:=\min\{a,b\}.
```

Then

```math
\boxed{
\rho\ge
\min\left\{{g_*^2\over10},{2m_*^2\over29}\right\}.
}
\tag{IP.1}
```

In particular, whenever

```math
{g_*\over m_*}\le\sqrt{20\over29},
\tag{IP.2}
```

the stronger simple payment

```math
\boxed{
\rho\ge{g_*^2\over10}
}
\tag{IP.3}
```

holds.

---

## 1. Split inversion and residual missing mass

Use the same phase coordinates as AG47/TL69. Let the total missing count be

```math
M_D=(\rho+o(1))D^2,
```

and, after a subsequence, let the phase-inversion chain graph have

```math
I_D=(u+o(1))D^2,
\qquad0\le u\le\rho.
```

Put

```math
v:=\rho-u.
```

The exact chain-graph cover deletes all inversions using at most

```math
(\sqrt{2u}+o(1))D
\tag{IP.4}
```

trains in total across the two families. Since every inversion edge is itself missing and every inversion edge is incident to the cover, the residual missing graph has at most

```math
(v+o(1))D^2
\tag{IP.5}
```

edges.

---

## 2. Iterative residual pruning

Assume first `v>0` and set

```math
\tau:=\sqrt{v/2}.
\tag{IP.6}
```

Starting from the inversion-free families, repeatedly delete **either-shore** trains whose current residual missing degree exceeds `(tau+o(1))D`. Continue until no such train remains.

Each deletion removes more than `(tau+o(1))D` currently surviving missing edges. An edge is removed only once, at the first deletion of one of its endpoints. Therefore the **total** number of pruning deletions across both shores is at most

```math
\left({v\over\tau}+o(1)\right)D
=(\sqrt{2v}+o(1))D.
\tag{IP.7}
```

This is the improvement over independent Markov pruning, which charged `sqrt(v)D` separately to each shore.

At termination every retained train misses at most

```math
(\tau+o(1))D
=\left(\sqrt{v/2}+o(1)\right)D
\tag{IP.8}
```

retained trains on the opposite shore.

If `v=0`, skip this pruning step and interpret every `sqrt(v)` term below as zero.

---

## 3. Large-family branch: denominator `10`

Suppose

```math
m_*>
\sqrt{2u}+{5\over\sqrt2}\sqrt v.
\tag{IP.9}
```

Even if the entire inversion-cover loss and the entire iterative-pruning loss fall on the same shore, each retained family has normalized mass greater than

```math
{5\over\sqrt2}\sqrt v-\sqrt{2v}
={3\over\sqrt2}\sqrt v
=3\tau.
\tag{IP.10}
```

Since every retained train misses at most `tau D+o(D)` opposite trains, every pair and every triple on either retained shore has a common neighbor on the other. The existing actual-`K_{2,2}` consistency and triple-neighbor transitivity proof therefore gives global crossing orders exactly as in Section 163 / the near-Mantel repair.

Take the same opposite-corner two-leg path. Relative to the original pair masses `a+b`, its selected degree sum loses at most

- `sqrt(2u)` from the inversion cover;
- `sqrt(2v)` from all iterative-pruning deletions combined;
- `2 sqrt(v/2)=sqrt(2v)` from the two selected corner missing-degree deficits.

Thus the projection estimate gives

```math
g_*=a+b-K
\le\sqrt{2u}+2\sqrt{2v}.
\tag{IP.11}
```

By Cauchy,

```math
\sqrt{2u}+2\sqrt{2v}
\le\sqrt{2+8}\sqrt{u+v}
=\sqrt{10\rho}.
\tag{IP.12}
```

Therefore the large-family branch gives

```math
\boxed{
\rho\ge{g_*^2\over10}.
}
\tag{IP.13}
```

---

## 4. Small-family branch: denominator `29/2`

If (IP.9) fails, then

```math
m_*\le
\sqrt{2u}+{5\over\sqrt2}\sqrt v.
```

Again by Cauchy,

```math
\sqrt{2u}+{5\over\sqrt2}\sqrt v
\le
\sqrt{2+{25\over2}}\sqrt{u+v}
=\sqrt{{29\over2}\rho}.
\tag{IP.14}
```

Hence

```math
\boxed{
\rho\ge{2m_*^2\over29}.
}
\tag{IP.15}
```

Combining the two exhaustive branches proves (IP.1).

If (IP.2) holds, then

```math
{g_*^2\over10}
\le {2m_*^2\over29},
```

so the minimum in (IP.1) is the first term. This proves (IP.3). `square`

---

## 5. Uniform family-cap corollary

Suppose, in addition, that

```math
a,b\le S<K.
```

For an oversized pair `a+b>K`, with `m=min(a,b)` and `M=max(a,b)`,

```math
{a+b-K\over m}
=1-{K-M\over m}
\le2-{K\over S}.
\tag{IP.16}
```

Therefore every oversized pair automatically lies in the strong branch (IP.3) whenever

```math
\boxed{
2-{K\over S}\le\sqrt{20\over29}.
}
\tag{IP.17}
```

Equivalently,

```math
S\le {K\over2-\sqrt{20/29}}
=0.9873073199\ldots .
\tag{IP.18}
```

Under that cap, the pair-payment theorem simplifies uniformly to

```math
\boxed{
\rho\ge{(a+b-K)_+^2\over10}.
}
\tag{IP.19}
```

This cap will hold with substantial margin for the equal-trimmed three-label shores in the next six-pair application.

---

## 6. Method audit

The improvement uses no new geometric theorem. It changes only the residual missing-edge bookkeeping:

1. inversion edges are removed by the existing chain-graph vertex cover;
2. residual high-degree trains are deleted iteratively from either shore;
3. each residual missing edge can pay for at most one pruning deletion;
4. the final maximum missing degree gives the same pair/triple common-neighbor hypotheses used by the audited global-order proof;
5. the same opposite-corner path gives the diameter contradiction.

The coefficient `sqrt(10)` in the large-family branch is the optimum of this iterative-pruning projection loss: for a general threshold `tau=lambda sqrt(v)`, the residual projection coefficient is `1/lambda+2lambda`, minimized at `lambda=1/sqrt(2)`.

A further improvement within this route would have to use more than total inversion and residual missing mass, or weaken the triple-common-neighbor requirement.

**Disposition:** proof-only strengthening of the per-pair payment. C-II and Level I remain open.
