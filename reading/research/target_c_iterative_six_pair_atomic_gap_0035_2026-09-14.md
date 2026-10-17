> Generated reading edition · [exact source](../../research/target_c_iterative_six_pair_atomic_gap_0035_2026-09-14.md) · source SHA-256 `0fbf854656ab9c9efc691090fcd9e1c65f2f6315eb543590ae73f3454842e1c6`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "64522eb193cb723f8fe2bd4228eda30d9b47447c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_iterative_six_pair_atomic_gap_0035_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "963399518d1be64d047f06c03825a3f64b6a0a55e65ea8c7105b53f406caf168"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — iterative-pruning six-pair atomic gap `0.0035`

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r10`  
**Claim class:** proof-only strengthening of the atomic train gap  
**LEVEL I STATUS:** `STILL OPEN`

The iterative-pruning pair theorem improves the missing-pair payment on the relevant
family-cap regime from

```math
\rho\ge {(a+b-K)_+^2\over18}
```

to

```math
\boxed{
\rho\ge {(a+b-K)_+^2\over10},
\qquad K={2\over\sqrt3}.
}
\tag{IS35.1}
```

Combining that stronger per-pair payment with the already proved sharp six-label
minimization yields

```math
\boxed{
 x\sigma\ge 2\sqrt{\Delta_2}+0.0035,
 \qquad \Delta_2={\pi\over2\sqrt3}.
}
\tag{IS35.2}
```

Thus at the same proof-only Type-II train-measure scope one may take

```math
\boxed{\eta_{grid}=0.0035.}
\tag{IS35.3}
```

This is a genuine strengthening of the `0.00234` split-budget theorem.  The gain comes
from iterative residual pruning, which makes each residual missing edge pay for at
most one deleted train.

---

## 1. Iterative-pruning input

For two atom families of normalized masses `a,b<=K`, with limiting projective axes
separated by `pi/3`, let `rho` be their normalized missing-pair mass.  Put

```math
g_*=(a+b-K)_+,
\qquad m_*=\min\{a,b\}.
```

The iterative-pruning theorem proves

```math
\rho\ge
\min\left\{{g_*^2\over10},{2m_*^2\over29}\right\}.
\tag{IS35.4}
```

In particular the strong branch

```math
\rho\ge{g_*^2\over10}
\tag{IS35.5}
```

holds whenever

```math
{g_*\over m_*}\le\sqrt{20\over29}.
\tag{IS35.6}
```

A uniform sufficient condition is that both family masses are at most

```math
S\le {K\over 2-\sqrt{20/29}}
=0.9873073199\ldots .
\tag{IS35.7}
```

The six-label reduction below physically trims both Mantel shores before applying the
pair theorem.  This point matters: the untrimmed atom families need not satisfy the
uniform cap at `eta=0.0035`, but every trimmed label family does.

---

## 2. The sharp six-label minimization remains valid at coefficient `1/10`

Let

```math
x_i,y_i\ge0,
\qquad
\sum_i x_i=\sum_i y_i=s,
\qquad {2K\over3}<s<K,
```

and define

```math
\Phi_s(x,y)
:=\sum_i x_i y_i
+{1\over10}\sum_{i\ne j}(x_i+y_j-K)_+^2.
\tag{IS35.8}
```

The proof of the sharp three-label lemma in
`target_c_six_pair_missing_budget_atomic_gap_001625_2026-09-14.md` is coefficient
parametric.  Its two strict-concavity requirements are

```math
12c<2,
\qquad16c<2.
```

They remain strict at `c=1/10`:

```math
12/10<2,
\qquad16/10<2.
```

The final one-common-label boundary argument only needs `c<1`, also true.  Therefore
exactly the same proof gives

```math
\boxed{
\Phi_s(x,y)
\ge {1\over5}\left({3s\over2}-K\right)^2.
}
\tag{IS35.9}
```

The minimizer is unchanged, up to simultaneous relabeling and shore exchange:

```math
\boxed{
x=(s,0,0),
\qquad y=(0,s/2,s/2).}
\tag{IS35.10}
```

Hence the six-label optimization is still exact rather than a numerical relaxation.

---

## 3. Dominant-orbit reduction and physical trimming

Assume for contradiction that a Type-II train-measure limit satisfies

```math
A:=x\sigma\le\bar A:=2s_2+\eta,
\qquad
s_2=\sqrt{\Delta_2},
\qquad
\eta=0.0035.
\tag{IS35.11}
```

Use the same dominant-orbit Mantel reduction as audited Section 168 and the preceding
six-pair theorems.  A dominant three-direction projective orbit has mass at least

```math
M_0={4s_2^2\over\bar A},
\tag{IS35.12}
```

with outside mass at most

```math
R_0=\bar A-M_0,
```

and conservative Mantel deficit

```math
d_0={\bar A^2\over4}-s_2^2+{R_0^2\over4}.
\tag{IS35.13}
```

The maximum-degree Mantel partition supplies two shores whose dominant-orbit masses
are each at least

```math
\boxed{s_0={M_0\over2}-\sqrt{d_0}}
\tag{IS35.14}
```

and whose total missing cross-shore pair mass is at most

```math
(2d_0+o(1))D^2.
\tag{IS35.15}
```

Physically trim trains inside the three atom windows on each shore until both retained
shores have normalized mass exactly `s_0+o(1)`.  Write the retained label masses as

```math
x_1,x_2,x_3,
\qquad y_1,y_2,y_3,
\qquad
\sum_i x_i=\sum_i y_i=s_0.
\tag{IS35.16}
```

Every individual trimmed family has mass at most `s_0`.

The exact certificate gives

```math
\boxed{s_0=0.892700786633011\ldots<0.9.}
\tag{IS35.17}
```

At the coarse uniform cap `S=0.9`,

```math
2-{K\over S}
=0.7169994\ldots
<\sqrt{20/29}.
\tag{IS35.18}
```

Therefore every oversized distinct-label pair in (IS35.16) lies in the strong branch
(IS35.5), with no assumption on the corresponding untrimmed atom populations.

For `i=j`, all `x_i y_iD^2+o(D^2)` same-window pairs are missing.  For `i ne j`, the
axes differ by exactly `pi/3`, so (IS35.5) gives missing mass at least

```math
{1\over10}(x_i+y_j-K)_+^2D^2-o(D^2).
```

The nine label-pair blocks are disjoint.  Hence the global Mantel missing budget gives

```math
2d_0
\ge
\sum_i x_i y_i
+{1\over10}\sum_{i\ne j}(x_i+y_j-K)_+^2.
\tag{IS35.19}
```

The certificate also verifies

```math
{2K\over3}<s_0<K,
```

so (IS35.9) applies and yields the necessary condition

```math
\boxed{
d_0\ge {1\over10}
\left({3s_0\over2}-K\right)^2.}
\tag{IS35.20}
```

---

## 4. Exact contradiction at `eta=0.0035`

The outward interval certificate

`research/verify_target_c_iterative_six_pair_atomic_gap_0035.py`

verifies

```math
\begin{aligned}
\bar A&=1.908125613727914\ldots,\\
M_0&=1.901132033640687\ldots,\\
R_0&=0.006993580087227\ldots,\\
d_0&=0.00334838486463296\ldots,\\
s_0&=0.892700786633011\ldots .
\end{aligned}
\tag{IS35.21}
```

The forced half-payment is

```math
{1\over10}
\left({3s_0\over2}-K\right)^2
=0.00339851590473685\ldots,
\tag{IS35.22}
```

whereas the available half-budget is only

```math
d_0=0.00334838486463296\ldots .
```

Thus

```math
\boxed{
{1\over10}
\left({3s_0\over2}-K\right)^2-d_0
>5.01\times10^{-5}.
}
\tag{IS35.23}
```

This contradicts (IS35.20), proving (IS35.2).

---

## 5. Ceiling of this scalar architecture

The six-label minimizer is exact and the strong pair-payment branch remains valid at
the endpoint.  Solving

```math
d_0(\eta)
={1\over10}
\left({3s_0(\eta)\over2}-K\right)^2
\tag{IS35.24}
```

numerically gives

```math
\boxed{\eta_*=0.00353466439218\ldots .}
\tag{IS35.25}
```

So decimal tuning beyond `0.0035` can recover less than `3.5e-5`.  A material next
atomic improvement must strengthen the iterative-pruning pair theorem, couple the six
distinct-label blocks globally, or use additional source geometry.

---

## 6. Immediate propagation

Every proof-only consequence depending only on the atomic train gain may now use

```math
\boxed{g=0.0035.}
```

In particular,

```math
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.0035,
}
\tag{IS35.26}
```

and the rhombic/correlated transfers become

```math
\boxed{
\liminf {\sigma_R\over D}\ge0.007,
}
\tag{IS35.27}
```

```math
\boxed{
\liminf {\rho_{rec}+\sigma_R-q\over D}\ge0.007.
}
\tag{IS35.28}
```

The Section-171 endpoint and the low-`t` pentagon/network/tooth ledgers should be
recomputed from `g=0.0035`; the `0.00234` constants are superseded at proof-only scope.

---

## 7. Scope audit

- Same full-core Type-II train-measure scope as Section 168 and the prior six-pair stack.
- Same dominant three-direction orbit and finite Mantel stability.
- The pair input is the iterative-pruning theorem at `a85427bc`.
- The strong pair branch is applied only after physical trimming; every selected label
  family has mass at most `s_0<0.9`.
- The sharp three-label minimizer is inherited with its strict curvature inequalities
  rechecked at `c=1/10`.
- The exact script certifies only scalar inequalities; it does not replace any
  combinatorial or geometric proof.
- No outer-detour, disk-topology, pseudosegment-biclique, or source-deletion assumption
  is introduced.

**Disposition:** proof-only atomic strengthening.  C-II and Level I remain open.
