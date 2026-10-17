> Generated reading edition · [exact source](../../../docs/reports/target_c_full_support_redundant_rigidity_circuits_2026-09-09.md) · source SHA-256 `cfcf33513470607006322fdf7b682d89e24ec727673982d9b97b3400d088e10d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8D4D08A7005C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_full_support_redundant_rigidity_circuits_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=37143384fb60bf054a5f8d13c0e97ea7dfdc25bc; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-support KKT stress makes every mixed bar redundant

**Date:** 2026-09-09  
**Repository base:** PR #115 continuation  
**Run type:** exact rigidity-matroid consequence  
**Target:** Target C C-II / post-ZR/ZF structure  
**LEVEL I STATUS:** STILL OPEN

ZR/ZF use a relative-interior normalized KKT stress whose coefficient is nonzero on
every actual contact and every actual diameter bar. ZF also proves that the equality
bar framework on

```math
E=C\cup H
```

has full planar infinitesimal-rigidity rank `2v-3`.

Those two facts imply more than the row-count inequality `e+h>=2v-2`: every active
bar is redundant. In the minimal mixed-stress case `s_Z=0`, the entire active row set
is one rigidity-matroid circuit, giving exact `(2,3)` sparsity on every proper edge
subset. This note records the finite consequences and the local attachment-cell
inequalities they impose.

## 1. Full-support stress dependence

Let `R` be the ordinary equality-bar rigidity matrix of the nonisolated core on the
edge set `E=C union H`. ZF gives

```math
\boxed{\operatorname{rank}R=2v-3.}
\tag{RR.1}
```

The relative-interior KKT stress gives one left-kernel vector `omega` with

```math
\omega_e=\alpha_e>0\quad(e\in C),
\qquad
\omega_h=-\beta_h<0\quad(h\in H).
\tag{RR.2}
```

Because the support is full,

```math
\boxed{\omega_a\ne0\quad(a\in E).}
\tag{RR.3}
```

## 2. Theorem RR — every active bar is redundant

### Theorem RR.1

For every active bar `a in E`, deleting its row leaves the rigidity rank unchanged:

```math
\boxed{
\operatorname{rank}R_{E\setminus\{a\}}=2v-3.
}
\tag{RR.4}
```

Hence the mixed equality framework is redundantly infinitesimally rigid.

### Proof

The stress dependence says

```math
\sum_{x\in E}\omega_xR_x=0.
```

Fix `a`. Since `omega_a!=0`,

```math
R_a
=-\frac1{\omega_a}
\sum_{x\ne a}\omega_xR_x.
```

Thus row `a` is in the span of all other rows. Deleting it does not change the row
span or rank. `square`

This conclusion uses only the one full-support dependence; no genericity is required.

## 3. Mixed minimum degree

### Corollary RR.2

Every core vertex has mixed active degree at least three:

```math
\boxed{
\deg_C(x)+\deg_H(x)\ge3.
}
\tag{RR.5}
```

### Proof

Suppose a vertex `x` had mixed degree at most two. If the degree is zero or one, the
full framework is visibly not infinitesimally rigid: move `x` perpendicular to its
single incident bar, fixing all other vertices.

If the degree is two, delete either incident bar. RR.1 says the remaining framework
is still infinitesimally rigid, but now `x` has degree one, giving the same
perpendicular flex. Contradiction. `square`

For unloaded vertices this is already implied by C26. The new content is at loaded
vertices. Since every loaded vertex has at least one diameter edge,

```math
\boxed{
\deg_H(b)=1\Longrightarrow\deg_C(b)\ge2.
}
\tag{RR.6}
```

C35 also gives `deg_C(b)<=3`.

## 4. Exact count consequence at diameter leaves

The full diameter graph has no isolated loaded vertices and

```math
h=q-d_H.
```

Let `n_1` be the number of loaded vertices of diameter degree one. Since

```math
\sum_b(\deg_H(b)-1)=2h-q=q-2d_H,
```

and every vertex of degree at least two contributes at least one to the left side,
there are at most `q-2d_H` such vertices. Therefore

```math
\boxed{n_1\ge2d_H.}
\tag{RR.7}
```

RR.6 then gives the loaded contact-degree lower bound

```math
\boxed{
 e_{BI}+2e_{BB}
 =\sum_{b\in B}\deg_C(b)
 \ge q+2d_H.
}
\tag{RR.8}
```

This is exact. It is compatible with the ZK degree-slack ledger and does not by
itself close the face inequality.

## 5. The `s_Z=0` endpoint is one rigidity circuit

The mixed row-nullity is

```math
|E|-\operatorname{rank}R
=(e+h)-(2v-3)
=1+s_Z.
\tag{RR.9}
```

If

```math
\boxed{s_Z=0,}
\tag{RR.10}
```

then the left kernel of `R` is one-dimensional. RR.3 says its unique nonzero
relation has support all of `E`.

### Theorem RR.3 — full mixed circuit

Under `s_Z=0`, `E=C union H` is a single circuit of the actual planar rigidity row
matroid. In particular

```math
\boxed{|E|=2v-2}
\tag{RR.11}
```

and every proper edge subset `E' proper subset E` is row-independent.

For any proper vertex set `X` with at least two vertices, the induced active bars obey

```math
\boxed{
|E(X)|\le2|X|-3.
}
\tag{RR.12}
```

### Proof

One-dimensional left kernel plus a dependence nonzero on every row means there is no
proper dependent row subset: such a dependence would be linearly independent from the
full-support dependence after extending by zero to the missing row. Thus `E` is a
matroid circuit.

For a proper vertex set `X`, the induced edge set is a proper subset of `E` and is
therefore independent. Its rigidity rows live on `2|X|` coordinate columns and
annihilate the three Euclidean infinitesimal motions on `X`, so their rank is at most
`2|X|-3`. Independence gives RR.12. `square`

Thus the endpoint `s_Z=0` is combinatorially a Laman circuit even though the source
coordinates need not be generic.

## 6. Attachment-cell circuit inequality

Fix one unloaded component `I_r`, with

- `n_r=|I_r|`;
- attachment set `A_r` of size `a_r`;
- internal contacts `e_r`;
- attachment contacts `t_r`;
- pinned stress surplus
  ```math
  s_r=e_r+t_r-2n_r-1\ge0.
  
  ```

Let

- `h_r` be the number of diameter edges with both endpoints in `A_r`;
- `b_r` be the number of loaded-loaded unit contacts with both endpoints in `A_r`.

Assume `s_Z=0` and `I_r union A_r` is a proper vertex subset of the core. Its induced
active bars include all `e_r+t_r` component contacts plus the `h_r+b_r` loaded-loaded
bars. RR.12 gives

```math
e_r+t_r+h_r+b_r
\le2(n_r+a_r)-3.
```

Insert `e_r+t_r=2n_r+1+s_r`.

### Corollary RR.4

```math
\boxed{
 h_r+b_r+s_r\le2a_r-4.
}
\tag{RR.13}
```

For the common three-attachment case,

```math
\boxed{
a_r=3
\Longrightarrow
h_r+b_r+s_r\le2.
}
\tag{RR.14}
```

Since C43 excludes a diameter triangle, `h_r<=2` independently; RR.14 says that
attaining those two local diameter edges leaves **zero** room for a loaded-loaded
contact or an extra pinned stress relation in that component.

This is a genuine new local coupling between the diameter graph and the harmonic
attachment cells. It does not yet force a contradiction globally.

## 7. What redundancy does not imply

- A redundantly rigid non-generic framework need not satisfy every theorem stated for
  generic globally rigid graphs.
- RR does not imply a second independent KKT stress; at `s_Z=0` there is exactly one.
- The mixed graph is not planar because diameter bars cross contact faces; planar
  Laman-circuit classifications cannot be imported without preserving this geometry.
- RR.12 counts **induced active bars**, not edges crossing a vertex cut.

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| every active bar redundant | proved | Full-support KKT row dependence. |
| mixed minimum degree at least 3 | proved | Delete one row at a degree-2 vertex. |
| `n_1>=2d_H` and RR.8 | proved | Degree sum + redundancy. |
| `s_Z=0` gives one rigidity circuit | proved | Unique full-support dependence. |
| proper induced sparsity RR.12 | proved | Circuit independence + planar rigid-motion kernel. |
| attachment inequality RR.13 | proved | Apply RR.12 to one component plus attachments. |
| circuit endpoint impossible | not proved | Current inequalities admit examples. |
| Level I | still open | Need global coupling/cavity or weight theorem. |

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Relative-interior KKT stress is one row dependence with nonzero coefficient on every
bar of E=C union H. ZF gives rank R=2v-3. Therefore deleting any one active bar
preserves rank: the mixed equality framework is redundantly rigid and every mixed
vertex has degree at least 3.

If s_Z=0, stress-space dimension is one, so the full edge set is a single rigidity
circuit. Every proper vertex subset X obeys
    |E(X)|<=2|X|-3.
For an unloaded component with attachment set A_r:
    h_r+b_r+s_r <= 2|A_r|-4.
In particular |A_r|=3 implies h_r+b_r+s_r<=2.
```
