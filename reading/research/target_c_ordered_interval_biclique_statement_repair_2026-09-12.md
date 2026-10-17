> Generated reading edition · [exact source](../../research/target_c_ordered_interval_biclique_statement_repair_2026-09-12.md) · source SHA-256 `2cae3713d59f64eaef1b68a8a0da8149f275ab31837ea4ac048b9189a84c95cd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "fe2689a49b6b215fe6ddc5ca7764b5b51c60c73f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_ordered_interval_biclique_statement_repair_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "697d909791c1463765819169a84fa32f39cff5021209cebfeee3cdb0b39c4674"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — repair of the ordered interval-biclique criterion

**Date:** 2026-09-12  
**Scope:** binding repair for `target_c_ordered_interval_biclique_sharpening_2026-09-12.md`.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The original exact interval-block theorem omitted the necessary existence condition
`k<=b`, where `b` is the size of the ordered shore. Without it the displayed numerical
condition can be vacuous. For example,

$$
a=b=e=1,
\qquad k=2,
$$

satisfies

$$
e+a=2=k(a+b-k+1),
$$

but the ordered shore has no consecutive two-block and hence no `K_{2,2}`.

The actual Section-91 applications in the research file are unaffected: their chosen
`k` is automatically at most both shore sizes whenever it is positive. The finite
regression script already tests the theorem only for

$$
1\le k\le\min(a,b).
$$

## Corrected exact theorem

Let `G=(A,B,E)` be bipartite, let `|A|=a`, `|B|=b`, fix a linear order on `B`, and
assume every row neighborhood `N(x)`, `x in A`, is an interval in that order. Let

$$
1\le k\le b.
$$

If

$$
\boxed{
e+a\ge k(a+b-k+1),
}
\tag{IB.1}
$$

then `G` contains a `K_{k,k}` whose `B` shore is one consecutive `k`-block.

### Proof

For one row of degree `d_x`, the number of consecutive `k`-blocks contained in its
interval neighborhood is

$$
\max(d_x-k+1,0).
$$

Thus the total row/block incidence count satisfies

$$
I_k
=\sum_x\max(d_x-k+1,0)
\ge e-a(k-1).
$$

By (IB.1),

$$
e\ge k(a+b-k+1)-a,
$$

and therefore

$$
I_k
\ge k(a+b-k+1)-a-a(k-1)
=k(b-k+1).
$$

Since `k<=b`, we have `b-k+1>=1`, so

$$
k(b-k+1)>(k-1)(b-k+1).
$$

There are exactly `b-k+1` consecutive `k`-blocks on `B`. If every such block occurred
in at most `k-1` row neighborhoods, then

$$
I_k\le(k-1)(b-k+1),
$$

contradicting the preceding strict inequality. Hence some consecutive `k`-block is
contained in at least `k` rows, giving the required `K_{k,k}`.

## The floor corollary is safe

Let

$$
k_0:=\left\lfloor{e\over a+b}\right\rfloor.
$$

If `k_0>=1`, then automatically

$$
k_0\le {e\over a+b}\le {ab\over a+b}<\min(a,b),
$$

because `e<=ab`. Thus the missing size hypothesis is automatic. Also

$$
e\ge k_0(a+b),
$$

which implies (IB.1). Therefore the useful corollary

$$
\boxed{
K_{k_0,k_0}\subseteq G
}
$$

remains valid exactly as used downstream.

## Asymptotic Section-91 form

If

$$
a,b\le CD,
\qquad e\ge\varepsilon D^2,
$$

and `k=floor(cD)` with

$$
c<C-\sqrt{C^2-\varepsilon},
$$

then the edge lower bound itself forces

$$
a,b\ge {\varepsilon\over C}D.
$$

Moreover

$$
C-\sqrt{C^2-\varepsilon}
={\varepsilon\over C+\sqrt{C^2-\varepsilon}}
\le {\varepsilon\over C}.
$$

After choosing `c` strictly below the endpoint, `k<=min(a,b)` for all sufficiently
large `D`. The interval-block extraction therefore remains valid and is linear, rather
than quadratic, in the edge-density parameter.

**Disposition:** the theorem statement is repaired; the Section-91 biclique
sharpening and its regression survive. Any future citation to the exact criterion must
include `1<=k<=b` (or the symmetric stronger condition `k<=min(a,b)`).