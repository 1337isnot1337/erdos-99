> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_nonzero_residue_saturation_2026-09-10.md) · source SHA-256 `1c3dc95814993fc36281510cc9f733123493c15b786e0f6299826348aa391666`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7E29FFAFBF42","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — cyclic P1 nonzero 2-adic residue blocks are all-or-nothing

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-p1-residue-saturation-2026-09-10`  
**Run type:** exact 2-adic Newton / Littlewood multiplicity theorem  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** PR #152 residue localization, PR #150 P1 arithmetic setup, SC P1 Littlewood closure from PR #118  
**External literature:** standard Newton-polygon theorem only  
**Computation:** none

## 1. Result

Write

```math
m=ru,
\qquad r=2^k,
\qquad u\text{ odd}.
```

For a hypothetical P1 survivor let

```math
z=e^{i\delta}
```

be the physical root, let `M(Z)` be its monic minimal polynomial over `Q`, and put

```math
F_m(Z)=Z^{2m}+4Z^{m+1}-6Z^m+4Z^{m-1}+1.
```

The P1 geometry and Littlewood closure give

```math
M\mid F_m,
\qquad
M\mid P,
\qquad
P(Z)=\sum_{j=0}^{m-1}\varepsilon_jZ^j,
\quad \varepsilon_j\in\{\pm1\}.
```

Hence modulo two

```math
\overline M\mid S_m(Z):=1+Z+\cdots+Z^{m-1}.
```

PR #152 already proves that `Z+1` does not divide `bar M` and therefore every residue root of `M` has nontrivial odd order dividing `u`.

The new theorem determines the multiplicity of every residue block except the order-three block.

### Theorem NRS — non-order-three residue saturation

Let

```math
\phi(Z)\in\mathbf F_2[Z]
```

be a monic irreducible factor of `S_u(Z)` whose roots have odd order `t>1`, with

```math
t\ne3.
```

If

```math
\phi\mid\overline M,
```

then in fact

```math
\boxed{\phi^r\parallel\overline M.}
\tag{NRS.1}
```

Moreover the corresponding local factor of `M` is totally ramified of exact ramification index `r` over the unramified residue extension defined by `phi`.

Thus a hypothetical P1 factor cannot use part of a nonzero non-order-three residue cluster. It either avoids the cluster completely or consumes the entire multiplicity `r` available from the Littlewood reduction.

In particular, if

```math
3\nmid u,
```

then there is a squarefree self-reciprocal divisor

```math
B(Z)\mid S_u(Z),
\qquad Z+1\nmid B,
```

such that

```math
\boxed{\overline M(Z)=B(Z)^r.}
\tag{NRS.2}
```

Consequently

```math
\boxed{\deg M=r\deg B,}
\tag{NRS.3}
```

so the characteristic-zero degree is quantized in blocks of size `r` times complete mod-two reciprocal cyclotomic blocks.

This is strictly stronger than PR #152's residue localization. PR #152 says where the residue roots may lie; NRS says that, away from order three, every residue block that occurs must occur with the full Littlewood multiplicity.

---

## 2. Exact mod-two Littlewood multiplicities

Since `m=ru` and `r` is a power of two, Frobenius gives in characteristic two

```math
Z^m-1=(Z^u-1)^r.
```

Therefore

```math
\boxed{
S_m(Z)
=(Z+1)^{r-1}S_u(Z)^r
\quad\text{in }\mathbf F_2[Z].
}
\tag{2.1}
```

Because `u` is odd, `Z^u-1` is separable over `F_2`. Hence

```math
S_u(Z)=\frac{Z^u-1}{Z-1}
```

is squarefree and is coprime to `Z+1`.

Thus every irreducible factor `phi` of `S_u` occurs in `S_m` with **exact** multiplicity

```math
\boxed r.
\tag{2.2}
```

Since `M|P` over `Z` and `bar P=S_m`, every such factor can occur in `bar M` with multiplicity at most `r`.

The rest of the proof supplies the matching lower bound `r` whenever the factor occurs at all.

---

## 3. Reciprocal P1 polynomial and a mod-four power lemma

Use the exact reciprocal form

```math
\boxed{
F_m(Z)=(Z^m+1)^2+4Z^{m-1}(Z-1)^2.
}
\tag{3.1}
```

We need one elementary congruence.

### Lemma 3.1

For every power of two `r` and every indeterminate `W`,

```math
\boxed{
(W^r+1)^2\equiv(W+1)^{2r}\pmod4.
}
\tag{3.2}
```

#### Proof

For `r=1` there is equality. Suppose the statement holds for `r`. Put `Y=W^r`. Then

```math
(Y^2+1)^2-(Y+1)^4
=-4Y(Y^2+Y+1),
```

so

```math
(W^{2r}+1)^2\equiv(W^r+1)^4\pmod4.
```

Squaring the induction congruence preserves it modulo four, giving

```math
(W^r+1)^4\equiv(W+1)^{4r}\pmod4.
```

This is the claim for `2r`. `square`

With `W=Z^u`, Lemma 3.1 gives

```math
\boxed{
F_m(Z)\equiv(Z^u+1)^{2r}\pmod4.
}
\tag{3.3}
```

The second summand in (3.1) disappears modulo four.

---

## 4. Move to one nonzero residue root

Let `phi` be as in NRS and let

```math
f:=\deg\phi.
```

Choose a root

```math
\xi\in\mathbf F_{2^f}
```

of `phi`. Its multiplicative order is the odd integer `t|u`, with `t>1` and `t!=3`.

Let `K/Q_2` be the unramified extension of degree `f` with residue field containing `xi`, and let

```math
\zeta\in\mathcal O_K
```

be the Teichmüller lift of `xi`. Then

```math
\zeta^t=1,
\qquad
\zeta^u=1,
\qquad
\zeta^m=1.
\tag{4.1}
```

Set

```math
Z=\zeta+X.
```

The constant term of the local expansion is exact. By (3.1),

```math
\begin{aligned}
F_m(\zeta)
&=4+4\zeta^{m-1}(\zeta-1)^2\\
&=4\left(1+\zeta^{-1}(\zeta-1)^2\right)\\
&=4(\zeta+\zeta^{-1}-1).
\end{aligned}
\tag{4.2}
```

The residue of the parenthesis vanishes exactly when

```math
\xi+\xi^{-1}=1,
```

i.e.

```math
\xi^2+\xi+1=0,
```

which is exactly the order-three case. Since `t!=3`, the parenthesis is a 2-adic unit. Therefore

```math
\boxed{v_2(F_m(\zeta))=2.}
\tag{NRS.4}
```

This is the only point at which the order-three residue is exceptional.

---

## 5. The local Newton edge is `(0,2)->(2r,0)`

Put

```math
g(X):=(\zeta+X)^u+1.
```

Since `zeta^u=1`,

```math
g(X)=2+XU(X),
\qquad
U(0)=u\zeta^{u-1}\in\mathcal O_K^\times.
\tag{5.1}
```

Equation (3.3) remains valid after translation:

```math
F_m(\zeta+X)\equiv g(X)^{2r}\pmod4.
\tag{5.2}
```

Expand

```math
g(X)^{2r}
=\sum_{j=0}^{2r}
\binom{2r}{j}2^{2r-j}X^jU(X)^j.
\tag{5.3}
```

For every coefficient of degree `n<2r`, only terms with `j<=n` contribute.

- If `j<=2r-2`, then the explicit factor `2^(2r-j)` is divisible by four.
- If `j=2r-1`, its multiplier is
  ```math
  \binom{2r}{2r-1}2=4r,
  
  ```
  again divisible by four.

Hence every coefficient of

```math
X,X^2,\ldots,X^{2r-1}
```

in `g^(2r)` is divisible by four. By (5.2), the same is true for `F_m(zeta+X)`.

For degree `2r`, the `j=2r` term contributes

```math
U(0)^{2r},
```

which is a unit modulo two; every contribution with smaller `j` is even. Thus the coefficient of `X^(2r)` in `F_m(zeta+X)` is a 2-adic unit.

Combine this with NRS.4:

- constant coefficient has valuation exactly `2`;
- coefficients in degrees `1,...,2r-1` have valuation at least `2`;
- the degree-`2r` coefficient has valuation `0`.

Therefore the lower Newton polygon begins with the single edge

```math
\boxed{(0,2)\longrightarrow(2r,0),}
\tag{NRS.5}
```

whose slope is

```math
\boxed{-1/r.}
\tag{NRS.6}
```

All subsequent coefficients are integral, so no later point lies below the horizontal ray starting at `(2r,0)`.

---

## 6. Local degree forces full residue multiplicity

Every root of `F_m(zeta+X)` with positive `X`-valuation belonging to the Newton edge NRS.5 has

```math
v_2(X)=1/r.
```

If an irreducible factor over `K` contains such a root, the value group of the corresponding field extension contains `1/r`. Hence its ramification index, and therefore its degree over `K`, is divisible by `r`.

Now assume

```math
\phi\mid\overline M.
```

Then some `K`-local factor of `M` contains a root reducing to `zeta`. Let its degree be `e`. The Newton edge gives

```math
\boxed{e\ge r.}
\tag{6.1}
```

All roots of this local factor reduce to `zeta`, so its reduction is

```math
(Z-\xi)^e.
```

Applying the unramified Frobenius conjugates over `Q_2` shows that

```math
\boxed{\phi(Z)^e\mid\overline M(Z).}
\tag{6.2}
```

But Section 2 gives the opposite multiplicity bound

```math
e\le r
```

because `bar M|S_m` and `phi` occurs exactly `r` times in `S_m`.

Therefore

```math
\boxed{e=r.}
\tag{6.3}
```

Equations (6.2)-(6.3) prove

```math
\phi^r\parallel\overline M.
```

They also show that the chosen local factor is totally ramified of exact ramification index `r` over the unramified residue extension. This proves NRS.1. `square`

---

## 7. Global form when `3` does not divide the odd part

Assume now

```math
3\nmid u.
```

PR #152 excludes `Z+1` from `bar M`. Every remaining irreducible factor of `bar M` lies in the squarefree polynomial `S_u`, and none has order three. NRS therefore applies to every factor.

Let `B` be the product of the distinct irreducible factors that occur. Then

```math
\overline M=B^r,
\qquad
B\mid S_u,
\qquad
B\text{ squarefree}.
```

The characteristic-zero polynomial `M` is reciprocal, so `bar M` is reciprocal. Since `r` is a power of two and `B` is squarefree, uniqueness of factorization forces `B` itself to be self-reciprocal.

This proves NRS.2.

Taking degrees gives

```math
\deg M=r\deg B,
```

which is NRS.3.

Since the SC Littlewood polynomial has degree `m-1=ru-1`,

```math
r\deg B\le ru-1.
```

Thus `deg B<=u-1`, as expected from `B|S_u`; the point is not this coarse inequality but the exact block quantization. A rational P1 factor cannot take a fractional part of any mod-two odd-order block to lower its degree.

---

## 8. Interaction with the cyclotomic-factor theorem on PR #153

PR #153 independently proves that the reciprocal polynomial `F_m` has no cyclotomic factor except

```math
\Phi_6
```

when `6|m`; the physical P1 factor is always noncyclotomic.

NRS is complementary. It says that this **noncyclotomic characteristic-zero factor** nevertheless has a highly cyclotomic reduction modulo two:

- PR #152: every residue root has nontrivial odd order dividing `u`;
- NRS: every non-order-three residue irreducible that occurs is saturated to multiplicity `r`;
- PR #153: none of these residue cyclotomic blocks lifts to a characteristic-zero cyclotomic factor of the physical polynomial.

Thus the remaining P1 factor must be a noncyclotomic reciprocal lift assembled from complete, maximally ramified odd-cyclotomic residue blocks.

This is a substantially narrower factorization problem than arbitrary reducibility of `F_m`.

---

## 9. The exceptional order-three block

If

```math
3\mid u,
```

then `S_u` contains the residue block

```math
Z^2+Z+1.
```

For its roots `xi`, the Teichmüller lift satisfies

```math
\zeta+\zeta^{-1}=-1,
```

so the constant in (4.2) is

```math
F_m(\zeta)=-8,
```

with valuation `3`, not `2`. The Newton polygon therefore has a different first layer. When `r>=2`, the same residue class also contains the characteristic-zero primitive-sixth-root factor `Phi_6` whenever `6|m`, which PR #153 identifies explicitly.

NRS deliberately does not claim saturation for this exceptional block. PR #150 completely excludes the special family `u=3`; for general `3|u`, separating the genuine `Phi_6` lift from any noncyclotomic order-three residue lift is the next local problem.

---

## 10. Regression audit

- NRS concerns the minimal polynomial `M` of the physical P1 root, not every factor of `F_m`.
- The local field `K` is unramified and is introduced only to split one irreducible mod-two residue block; no global irreducibility is assumed.
- The Newton denominator gives a lower bound on local ramification. The exact equality `e=r` uses the **independent Littlewood multiplicity ceiling** from `M|P`; Newton theory alone does not give equality.
- Order three is excluded from the theorem because the constant valuation changes from `2` to `3`; it is not silently treated by the generic edge.
- The congruence modulo four is valid for every `r=2^k`, including `r=1`.
- `S_u` is squarefree because `u` is odd; this is essential for the exact multiplicity `r` in `S_m`.
- NRS does not yet exclude P1 for arbitrary odd part. A noncyclotomic factor with reduction `B^r` remains arithmetically possible.

---

## 11. Exact next lemmas

The remaining arithmetic endpoint is now split cleanly.

### NRS-A — remove the order-three exceptional lift

When `3|u`, factor out the known characteristic-zero `Phi_6` factor when present and determine the residual Newton polygon over the order-three unramified residue field. The target is to show that a noncyclotomic physical factor either cannot use the order-three block or must again consume a forbidden multiplicity.

### NRS-B — link complete mod-two blocks using mod three

PR #153 gives

```math
F_m(Z)\equiv(Z^{m-1}+1)(Z^{m+1}+1)\pmod3.
```

For `3\nmid u`, NRS gives

```math
\overline M=B^r
```

with `B` a squarefree self-reciprocal divisor of `S_u`. A closing arithmetic theorem would show that no noncyclotomic reciprocal characteristic-zero factor can simultaneously have this saturated mod-two reduction, divide the adjacent-binomial product modulo three, and have degree at most `m-1` while containing the distinguished physical unit-circle root.

The immediate finite target is therefore no longer generic irreducibility of `F_m`; it is incompatibility of these two exact local factorization types.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P1: m=ru, r=2^k, u odd.  Let M be the physical root's minimal polynomial.
SC gives M|P with
    P mod2 = S_m = (Z+1)^(r-1) S_u^r,
and PR #152 excludes Z+1 from M mod2.

Take an irreducible phi|S_u with residue-root order t!=3.  Over the unramified
2-adic field containing a Teichmuller lift zeta of a root xi of phi:
    F_m(zeta)=4(zeta+zeta^-1-1),
so v2(F_m(zeta))=2 exactly.
For r a power of two,
    (W^r+1)^2 == (W+1)^(2r) mod4,
therefore
    F_m(Z) == (Z^u+1)^(2r) mod4.
Writing Z=zeta+X and (zeta+X)^u+1=2+XU(X), U(0) a unit, gives:
    constant valuation =2,
    degrees 1,...,2r-1 valuation >=2,
    degree 2r valuation =0.
Thus the Newton edge is
    (0,2)->(2r,0), slope -1/r.
Any local factor above phi has ramification/degree >=r.  Hence phi appears in M mod2
with exponent >=r.  But M|P and S_m contains phi with exact exponent r, so
    phi^r || M mod2.

If 3 does not divide u, every residue block is generic and
    M mod2 = B^r
for a squarefree self-reciprocal B|S_u.  Thus deg M=r deg B exactly.
PR #153 separately says M is noncyclotomic in characteristic zero.
Remaining target: exceptional order-3 lift, then combine saturated mod2 blocks with
F_m mod3=(Z^(m-1)+1)(Z^(m+1)+1).
```
