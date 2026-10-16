<!-- theorem-state: {"artifact_id":"ART-9826F802D49F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — every cyclic P1 factor avoids the zero 2-adic trace cluster

**Date:** 2026-09-10  
**Run type:** exact 2-adic/local-factor reduction  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** PR #150 P2/P3 arithmetic setup and P1 Littlewood closure from PR #118  
**External literature:** standard Newton-polygon theorem only  
**Computation:** none

## 1. Result

Put

\[
m:=q-2=2^k u,
\qquad u\text{ odd},
\qquad r:=2^k.
\]

For a hypothetical P1 survivor, let

\[
z=e^{i\delta},
\qquad
Y=z+z^{-1}=2\cos\delta,
\]

and let

\[
h(T)\in\mathbb Z[T]
\]

be the monic irreducible minimal polynomial of `Y`, of degree `d`.

The P1 signed closure gives a Littlewood polynomial of length `m`, so as in P2/P3

\[
\boxed{d\le\frac{m-1}{2}.}
\tag{RL.1}
\]

The new structural theorem is:

### Theorem RL — zero-trace cluster exclusion

No 2-adic irreducible factor of `h` can have roots reducing to

\[
\boxed{T=0\pmod2.}
\tag{RL.2}
\]

Equivalently,

\[
\boxed{T\nmid \overline h(T)\in\mathbb F_2[T].}
\tag{RL.3}
\]

Since

\[
G_m(T):=C_m(T)+4T-6
\equiv C_m(T)
\equiv C_u(T)^r
\pmod2,
\tag{RL.4}
\]

all mod-two roots of `h` must therefore lie among the **nonzero** roots of `C_u`.

Passing to the reciprocal lift

\[
M(Z)=Z^d h(Z+Z^{-1}),
\]

which is the minimal polynomial of `z`, every mod-two root of `M` is a nontrivial odd-order root of unity of order dividing `u`.

Thus:

\[
\boxed{
\text{every mod-2 conjugate of the P1 root }z
\text{ has nontrivial odd order dividing }u.
}
\tag{RL.5}

This unifies the power-of-two case: when `u=1` there is no nontrivial odd-order residue root, so P1 is impossible. For general `u`, it removes the entire zero-trace cluster and reduces the arithmetic endpoint to the nontrivial odd divisor structure of `u`.

---

## 2. The Littlewood multiplicity budget at `Z=1`

The P1 closure gives

\[
P(Z)=\sum_{j=0}^{m-1}\varepsilon_jZ^j,
\qquad
\varepsilon_j\in\{\pm1\},
\qquad
P(z)=0.
\]

Modulo two,

\[
\boxed{
\overline P(Z)=S_m(Z):=1+Z+\cdots+Z^{m-1}.
}
\tag{2.1}

Because `m=ru` with `r=2^k`, Frobenius in characteristic two gives

\[
Z^m-1=(Z^u-1)^r.
\]

The odd polynomial `Z^u-1` has a simple root at `Z=1`. Therefore

\[
S_m(Z)=\frac{Z^m-1}{Z-1}
\]

has `Z=1` with exact multiplicity

\[
\boxed{r-1.}
\tag{2.2}

Let `M` be the minimal polynomial of `z`. Since `M|P` in `Z[Z]`, reduction modulo two gives

\[
\boxed{\overline M\mid S_m.}
\tag{2.3}

Hence the total multiplicity of `Z+1` in `\overline M` is at most

\[
\boxed{r-1.}
\tag{2.4}

The proof of RL will show that a single `T=0` 2-adic trace factor would already force at least `r` copies of `Z+1` into `\overline M`.

---

## 3. Mod-two trace structure

The trace-Chebyshev polynomials satisfy

\[
C_{ab}=C_a\circ C_b
\]

and

\[
C_{2n}=C_n^2-2.
\]

Therefore, modulo two,

\[
C_r(X)\equiv X^r
\]

for every power of two `r`, and hence

\[
\boxed{
C_m(T)=C_r(C_u(T))
\equiv C_u(T)^r
\pmod2.
}
\tag{3.1}

Since `4T-6` is even,

\[
\boxed{G_m(T)\equiv C_u(T)^r\pmod2.}
\tag{3.2}

For odd `u`, `C_u` is an odd polynomial. Its linear coefficient is

\[
(-1)^{(u-1)/2}u,
\]

which is odd. Thus

\[
\boxed{T\text{ is a simple factor of }\overline{C_u}(T).}
\tag{3.3}

Consequently `T=0` is a mod-two root of `G_m` of exact multiplicity `r`.

The issue is whether the particular rational factor `h` containing the geometric root can use any part of that cluster. The next sections show it cannot.

---

## 4. Case `k>=2`: the zero cluster has local degree at least `r/2`

Assume

\[
r=2^k\ge4.
\]

For powers of two at least four, repeated doubling gives

\[
\boxed{C_r(X)-2\equiv X^r\pmod4.}
\tag{4.1}

Indeed `C_4(X)-2=X^4-4X^2`, and if `C_r-2\equiv X^r mod4`, then

\[
C_{2r}-2=(C_r-2)(C_r+2)
\equiv X^{2r}\pmod4.
\]

Using `C_m=C_r\circ C_u`,

\[
\begin{aligned}
G_m(T)
&=C_r(C_u(T))+4T-6\\
&=[C_r(C_u(T))-2]+4T-4.
\end{aligned}
\tag{4.2}

By (4.1),

\[
C_r(C_u(T))-2\equiv C_u(T)^r\pmod4.
\]

Because `C_u(T)` has zero constant term and odd linear coefficient, `C_u(T)^r` has no term below degree `r`, and its `T^r` coefficient is odd.

Therefore in `G_m(T)`:

- the constant coefficient is exactly `-4`, with `v_2=2`;
- every coefficient of degrees `1,...,r-1` has 2-adic valuation at least `2`;
- the coefficient of `T^r` is odd.

Thus the lower Newton polygon begins with the segment

\[
\boxed{(0,2)\longrightarrow(r,0)}
\tag{4.3}

of slope

\[
\boxed{-\frac2r=-\frac1{r/2}.}
\tag{4.4}

Every `Q_2`-irreducible factor whose roots reduce to `T=0` has degree divisible by the denominator `r/2` of this slope. In particular its degree `d_0` satisfies

\[
\boxed{d_0\ge r/2.}
\tag{4.5}

---

## 5. Case `k=1`: the zero cluster has local degree at least two

Now

\[
r=2,
\qquad m=2u,
\qquad u\text{ odd}.
\]

Use

\[
C_{2u}=C_u^2-2.
\]

Then

\[
\boxed{G_m(T)=C_u(T)^2+4T-8.}
\tag{5.1}

Since `C_u(T)` has odd linear coefficient and no constant term:

- the constant term of `G_m` is `-8`, valuation `3`;
- the coefficient of `T` is exactly `4`, valuation `2`;
- the coefficient of `T^2` is odd.

The line from `(0,3)` to `(2,0)` has height `3/2` at degree one, below the actual height two. Thus the initial Newton polygon is the single segment

\[
\boxed{(0,3)\longrightarrow(2,0)}
\tag{5.2}

of slope `-3/2` in lowest terms. Any irreducible local factor in the zero cluster therefore has even degree:

\[
\boxed{d_0\ge2.}
\tag{5.3}

---

## 6. Case `k=0`: the zero cluster still cannot occur

Finally let

\[
r=1,
\qquad m=u\text{ odd}.
\]

The polynomial `C_m(T)` is odd, with linear coefficient

\[
(-1)^{(m-1)/2}m.
\]

Hence

\[
G_m(T)=C_m(T)+4T-6
\]

has

- constant term `-6`, valuation `1`;
- linear coefficient `(-1)^{(m-1)/2}m+4`, which is odd.

Thus the zero cluster begins with

\[
\boxed{(0,1)\longrightarrow(1,0),}
\tag{6.1}

so every local factor there has degree at least one:

\[
\boxed{d_0\ge1.}
\tag{6.2}

---

## 7. Reciprocal lift doubles zero-cluster multiplicity

Suppose for contradiction that `h` has a `Q_2`-irreducible factor `h_0` of degree `d_0` lying in the `T=0` cluster.

Because all roots of `h_0` have positive 2-adic valuation,

\[
\boxed{\overline{h_0}(T)=T^{d_0}.}
\tag{7.1}

The minimal polynomial of `z` is the reciprocal lift

\[
M(Z)=Z^d h(Z+Z^{-1}).
\tag{7.2}

At the level of the contribution from `h_0`, reduction modulo two gives

\[
Z^{d_0}h_0(Z+Z^{-1})
\equiv
Z^{d_0}(Z+Z^{-1})^{d_0}
=(Z^2+1)^{d_0}
=(Z+1)^{2d_0}.
\tag{7.3}

Therefore

\[
\boxed{
(Z+1)^{2d_0}\mid\overline M(Z).
}
\tag{7.4}

But Section 2 gives multiplicity at most `r-1` in `\overline M`.

Now compare the cases:

- `k>=2`: `2d_0>=r>r-1` by (4.5);
- `k=1`: `2d_0>=4>1=r-1` by (5.3);
- `k=0`: `2d_0>=2>0=r-1` by (6.2).

Every case contradicts (2.4).

Therefore no such local factor exists. This proves RL.2-RL.3. `square`

---

## 8. Interpret the surviving residues as nontrivial odd roots of unity

Equation (3.2) says every mod-two root `tau` of `h` satisfies

\[
C_u(\tau)=0.
\]

Choose `xi` in an algebraic closure of `F_2` with

\[
\tau=\xi+\xi^{-1}.
\]

Then

\[
0=C_u(\tau)=\xi^u+\xi^{-u}.
\]

In characteristic two this means

\[
\xi^{2u}=1.
\]

The multiplicative group of every finite extension of `F_2` has odd order, so there is no nontrivial 2-primary torsion. Hence

\[
\boxed{\xi^u=1.}
\tag{8.1}

If `tau=0`, then `xi+xi^{-1}=0`, so `xi^2=1`, forcing `xi=1`; conversely `xi=1` gives `tau=0`.

RL has excluded `tau=0`. Therefore every surviving `xi` is a **nontrivial** `u`-th root of unity.

This proves RL.5.

---

## 9. Consequences

### 9.1 Power-of-two case recovered conceptually

If

\[
u=1,
\]

there is no nontrivial odd-order residue root at all. Therefore no P1 factor can exist.

This recovers the qualitative P2 exclusion for `m=2^k`. P2 remains quantitatively stronger because it obtains the full one-edge Newton polygon and degree floor directly.

### 9.2 General P1 arithmetic lives entirely in the odd part

All 2-primary residue behavior is now removed. The only possible mod-two residue orders of the P1 root are nontrivial divisors of

\[
\boxed{u=\operatorname{oddpart}(q-2).}
\]

Thus future local-factor arguments may be organized divisor-by-divisor over the odd part rather than over all roots of `G_m`.

### 9.3 Prime odd part

If `u=p` is an odd prime, every mod-two reciprocal conjugate of `z` has exact order `p`. Hence

\[
\boxed{\overline M(Z)\mid\Phi_p(Z)^r}
\tag{9.1}

in `F_2[Z]`, with no `(Z+1)` factor.

This does not itself exclude the branch, but it leaves a single odd cyclotomic residue class. For `p=3`, PR #150 P3 uses the finer Newton structure of that single class to obtain a contradiction. The next natural cases are `p=5,7,...`.

---

## 10. Audit and regressions

### The zero cluster is a local statement

RL does not say `h(0)` is nonzero as an integer for a superficial parity reason. It proves that **no `Q_2` factor of `h`** can lie in the positive-valuation zero cluster, then concludes `T` does not divide `bar h`.

### Newton-slope denominators

The argument uses only local factor-degree divisibility from the initial Newton segment. It does not claim global irreducibility of `G_m`.

### Reduction of the reciprocal lift

The doubling from `d_0` to `2d_0` is essential. A trace root `T=0` corresponds to the ramified reciprocal point `Z=1` in characteristic two, because

\[
Z+Z^{-1}=0
\iff
(Z+1)^2=0.
\]

This is exactly why the Littlewood multiplicity budget is one unit too small.

### `u>1`

Nonzero odd-order clusters genuinely remain. RL does not claim they are impossible. That would require new arithmetic beyond the zero-cluster argument.

---

## 11. Exact next lemma

The P1 arithmetic endpoint is now:

> Let `m=2^k u`, `u>1` odd. The geometric trace factor `h` has degree at most `(m-1)/2`, and every mod-two reciprocal root has nontrivial order dividing `u`. Prove that no such factor of
> \[
> G_m(T)=C_m(T)+4T-6
> \]
> can contain the distinguished largest real P1 root.

For prime odd part `p`, the residue support is reduced to the single cyclotomic family `Phi_p`. A useful next theorem would compute the 2-adic Newton polygon over the unramified trace extension attached to `p` and compare its required multiplicity with the exact `Phi_p^r` budget in `S_{pr}`.

---

## 12. Promotion recommendation

**Hold as a report-level theorem pending independent audit.**

RL is exact downstream of report-level P1 closure/P2/P3 and changes no canonical route map.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Write m=q-2=2^k u, u odd, r=2^k. A P1 Littlewood root z has trace Y=z+z^-1
with minimal trace polynomial h and reciprocal minimal polynomial M.
Modulo 2:
  P == S_m,
  mult_{Z=1} S_m = r-1,
  G_m(T) == C_u(T)^r,
and T is a simple factor of C_u mod 2.

Suppose a Q_2 factor h0 of h lies in the T=0 cluster, degree d0.
- k>=2: G_m at T=0 has initial Newton segment (0,2)->(r,0), so d0>=r/2.
- k=1: initial segment (0,3)->(2,0), so d0>=2.
- k=0: initial segment (0,1)->(1,0), so d0>=1.
Since h0 mod2=T^d0, its reciprocal lift contributes
  (Z+1)^(2d0)
inside M mod2. In every case 2d0>r-1, contradicting M|P and the exact Z=1
multiplicity r-1 in S_m.

Therefore no trace conjugate reduces to T=0. All surviving mod-2 reciprocal roots are
nontrivial odd-order roots of unity of order dividing u=oddpart(m). For u=1 this
recovers P2; for prime u=p the entire residue support lies in Phi_p^r.
```
