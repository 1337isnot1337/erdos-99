> Generated reading edition · [exact source](../../research/target_c_section149_phase_atomization_repair_2026-09-12.md) · source SHA-256 `33a5ba867d4e593874928e7aa2dbeb4e88e49412f4c35e73eebdd59629bbcf23`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5efe59cd28a3d7b57751ed6ebbb102710db8b75b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section149_phase_atomization_repair_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "108997119ef206f067243986e0fdd98769bcad6cccd8184304d0d8dfc2cf17c1"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C Section 149 repair — local Mantel atomization of phase-orbit crossings

**Date:** 2026-09-12  
**Status:** proof-only candidate awaiting hostile audit; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The hostile audit of Section 149 identified one missing finite-to-limit implication:
quadratic train crossings concentrated at projective separation `pi/3` must be
converted into an `ell^2` mass of **atomic** phase orbits. This note supplies that
conversion as a standalone local-Mantel lemma. It does not promote Section 149 or
close C-II; it supplies only the missing bridge, subject to checking that the
canonical §142 saturation input has the stated fixed-`epsilon` form.

## 1. Finite-to-limit lemma

Let `D_n -> infinity`. Let `G_n` be simple triangle-free graphs with vertex set
`V_n`, and let each vertex `i` have a label `xi_i` in a compact metric space `X`.
Assume

```math
\frac{|V_n|}{D_n}\to x<\infty,
\qquad
\mu_n:=\frac1{D_n}\sum_{i\in V_n}\delta_{\xi_i}
\rightharpoonup\mu.
\tag{A149R.1}
```

For `epsilon>0`, let `E_n^{far}(epsilon)` be the number of graph edges `ij` with
`d_X(xi_i,xi_j)>epsilon`. Suppose

```math
\frac{|E_n^{far}(epsilon)|}{D_n^2}\longrightarrow0
\quad\text{for every fixed }epsilon>0.
\tag{A149R.2}
```

Write `S_a=mu({a})` for the masses of the atoms of `mu`. Then

```math
\boxed{
\limsup_{n\to\infty}\frac{|E(G_n)|}{D_n^2}
\le\frac14\sum_{a\in X:\,\mu({a})>0}S_a^2.
}
\tag{A149R.3}
```

The sum is countable and finite.

### Proof

Fix `rho>0` and list the finitely many atoms with mass at least `rho` as
`a_1,...,a_m`. Choose pairwise disjoint small neighborhoods `U_j` of these atoms,
with boundaries of zero `mu`-mass, and then choose `epsilon` smaller than their
separation. The number of vertices in `U_j` is

```math
|V_n\cap U_j|/D_n\to\mu(U_j).
\tag{A149R.4}
```

The induced graph on `V_n\cap U_j` is triangle-free, so Mantel's theorem gives

```math
|E(G_n[V_n\cap U_j])|
\le\frac14|V_n\cap U_j|^2.
\tag{A149R.5}
```

All edges joining two distinct selected neighborhoods are counted by
`E_n^{far}(epsilon)` once `epsilon` is smaller than their separation. Edges touching
the complement are controlled by the local label mass. More explicitly, after first
fixing the selected neighborhoods and then taking `n->infinity`, the number of
non-far neighbors of a vertex with label `z` is at most

```math
D_n\,\mu_n(B_X(z,epsilon)).
\tag{A149R.6}
```

For the complement of the selected neighborhoods, compactness and weak convergence
give the uniform bound

```math
\limsup_{n\to\infty}\sup_{z\text{ in the complement}}
\mu_n(B_X(z,epsilon))
\le
\sup_{z\text{ in the complement}}
\mu(\overline B_X(z,2epsilon))+o_{epsilon}(1).
\tag{A149R.7}
```

The right side tends, as `epsilon downarrow0`, to at most `rho` after the selected
atom neighborhoods are removed: any remaining atom has mass `<rho`, and the
nonatomic part is uniformly small on sufficiently small balls. Summing (A149R.6)
over complement vertices therefore makes the normalized contribution of edges
touching the complement at most `rho x^2/2+o_rho(1)`. The annular pieces between a
selected atom and the complement are included in this same bound; their `mu`-mass
tends to zero as the neighborhoods shrink.

Consequently, first taking `n->infinity`, then shrinking the neighborhoods, and then
letting `rho downarrow0`, gives

```math
\limsup\frac{|E(G_n)|}{D_n^2}
\le\frac14\sum_{j=1}^m S_{a_j}^2+O(rho x^2).
\tag{A149R.8}
```

Finally let `rho downarrow0`. Since the omitted atomic tail satisfies
`sum_{S_a<rho}S_a^2 <= rho mu(X)`, (A149R.3) follows. `square`

The only graph input in the local estimate is triangle-freeness; no planarity or
global-minimality implication is hidden in the lemma.

## 2. Application to the Section-149 phase quotient

Take `X` to be the projective train-direction circle modulo the phase shift
`pi/3`. If a rhombus crossing has angle in

```math
\left(\frac\pi3,\frac\pi3+epsilon\right]
```

or the corresponding projective opposite interval, its two quotient labels have
distance at most `epsilon`. The audited-working §142 saturation input must be read in
the following fixed-`epsilon` form:

```math
\#\{\text{rhombus crossings with quotient distance}>epsilon\}=o(D^2)
\quad(epsilon>0\text{ fixed}).
\tag{A149R.9}
```

The stopped-train crossing graph is simple and triangle-free. If `T/D -> x` and
`R_4/D^2 -> Delta_2`, apply (A149R.3) to obtain, for the atomic quotient masses
`S_j`,

```math
\Delta_2\le\frac{x^2}{4}\sum_jS_j^2,
\qquad\text{hence}\qquad
\boxed{\sum_jS_j^2\ge\frac{4\Delta_2}{x^2}.}
\tag{A149R.10}
```

This is exactly the missing implication in Section 149. It is now separated from the
outer Fourier estimate and from the bounded-defect endpoint bookkeeping.

## 3. Scope and remaining dependencies

- The proof keeps occurrence multiplicity in the outer measure and does not remove
  bridges or contact-isolated source points.
- The lemma is a finite graph/measure statement. It does not assert that a local
  phase model embeds into a global minimizer.
- The application is valid only if §142 supplies (A149R.9), not merely a verbal
  support statement with no fixed-`epsilon` quantitative meaning.
- The endpoint-capacity inequality `2xS_j <= A_j+C_j` and the subsequent Section-149
  scalar tradeoff remain separate proof obligations.
- Type I is untouched, and no canonical theorem-state mutation is made.

**Classification:** repaired proof-only bridge, awaiting independent hostile audit.
