<!-- theorem-state: {"artifact_id":"ART-D8C7BC5BC3FA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — all even P1 endpoints are impossible; odd P1 reduces to one order-nine factor

**Date:** 2026-09-10  
**Run type:** exact synthesis of 2-adic ramification and Littlewood multiplicity  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** PR #152 zero-residue exclusion; SR2 and OR1 on this branch; PR #155 O3X order-three exclusion; PR #153 cyclotomic-factor classification  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`, but the P1 endpoint is now reduced to a single explicit odd residue case.

Write

\[
m=q-2=ru,
\qquad r=2^k,
\qquad u\text{ odd}.
\]

Let `h(T)` be the minimal polynomial of the P1 trace

\[
Y=z+z^{-1}=2\cos\delta,
\]

and

\[
M(Z)=Z^{\deg h}h(Z+Z^{-1})
\]

the reciprocal minimal polynomial of the physical root `z=e^{i\delta}`.

The P1 Littlewood closure gives

\[
M\mid P,
\qquad
\overline P=S_m=(Z+1)^{r-1}S_u(Z)^r.
\tag{EC.1}
\]

Thus every nontrivial odd-order irreducible factor of `S_u` is available in `bar P` with exponent exactly `r`.

SR2/OR1 show that, except for two explicitly isolated residue types, a local trace cluster is twice as ramified as the first Newton segment alone indicates.  That doubles the exponent after reciprocal lift from `r` to `2r`, which is already incompatible with EC.1.

### Main theorem EC

1. If
   \[
   r\ge2,
   \]
   then P1 is impossible for every odd part `u`.

2. If
   \[
   r=1
   \]
   and `9` does not divide `u`, then P1 is impossible.

3. Therefore every surviving P1 candidate must satisfy
   \[
   \boxed{m=q-2\text{ odd and }9\mid m.}
   \tag{EC.2}
   \]

4. In that remaining case the physical reciprocal minimal polynomial has exact degree six and exact mod-two reduction
   \[
   \boxed{
   \deg M=6,
   \qquad
   \overline M(Z)=\Phi_9(Z)=Z^6+Z^3+1.
   }
   \tag{EC.3}
   \]
   Equivalently
   \[
   \boxed{
   \deg h=3,
   \qquad
   \overline h(T)=T^3+T+1.
   }
   \tag{EC.4}
   \]

5. PR #153 shows the characteristic-zero factor `M` is noncyclotomic.  Thus the only P1 escape is a **noncyclotomic reciprocal sextic** reducing to `Phi_9` modulo two and dividing the sparse P1 polynomial `F_m` for an odd multiple `m` of nine.

This is a finite-degree endpoint, independent of `m`.

---

## 1. Local trace multiplicity for a nonzero residue block

Let `q(T)` be an irreducible trace factor over `F_2` associated with a nontrivial odd-order root `xi`, modulo inversion.  Let

\[
f=\deg q.
\]

The characteristic-two identity

\[
C_u(Z+Z^{-1})=Z^u+Z^{-u}
=Z^{-u}(Z^u+1)^2
\]

shows that every nontrivial trace root occurs with multiplicity exactly two in `C_u(T)`.  The trace map

\[
Z\mapsto Z+Z^{-1}
\]

is étale at every nontrivial odd-order residue root, since

\[
1-Z^{-2}\ne0.
\]

Hence

\[
\boxed{q(T)^2\parallel C_u(T).}
\tag{1.1}
\]

Because

\[
G_{ru}(T)\equiv C_u(T)^r\pmod2,
\]

the complete trace cluster above `q` has mod-two multiplicity

\[
\boxed{2r}
\tag{1.2}
\]

and total degree

\[
2rf.
\]

---

## 2. SR2 forces the entire trace cluster into one local factor

Assume first

\[
r\ge2
\]

and the residue order is not three.

SR2 proves that every `Q_2`-irreducible factor in this trace cluster has degree at least

\[
2rf.
\tag{2.1}
\]

But Section 1 shows that the whole cluster itself has total degree exactly `2rf`.  Therefore the cluster is one local irreducible factor and its reduction is exactly

\[
\boxed{q(T)^{2r}.}
\tag{2.2}
\]

This is stronger than a degree lower bound: occurrence of the residue block forces **all `2r` copies** of its trace factor into the local factor.

For `r=1`, OR1 gives the identical conclusion

\[
\boxed{q(T)^2}
\tag{2.3}
\]

for every residue order other than `3` and `9`.

---

## 3. Reciprocal lift preserves the doubled exponent

Let

\[
Q_q(Z):=Z^f q(Z+Z^{-1}).
\]

Over `F_2`, `Q_q` is the reciprocal lift of the trace orbit.  Depending on whether inversion lies in the Frobenius orbit of the underlying odd root, `Q_q` is either irreducible or the product of two reciprocal-conjugate irreducibles.  In either case it is squarefree, because the trace map is étale at the nontrivial roots.

If a local factor of `h` reduces as

\[
q(T)^{2r},
\]

then the corresponding factor of the reciprocal lift `M` reduces as

\[
\boxed{Q_q(Z)^{2r}.}
\tag{3.1}
\]

Thus **every irreducible reciprocal residue factor occurring in `Q_q` appears in `bar M` with exponent `2r`.**

But EC.1 gives

\[
\overline M\mid S_m=(Z+1)^{r-1}S_u^r.
\]

Every nontrivial odd-order factor of `S_u` occurs on the right with exponent exactly

\[
r.
\]

Therefore

\[
2r>r
\]

is an immediate contradiction.

We obtain:

### Corollary EC.1

For `r>=2`, the physical P1 factor cannot use **any** nontrivial residue order other than the exceptional order-three block.

For `r=1`, it cannot use any nontrivial residue order other than `3` or `9`.

Notice that no global trace-degree ceiling is needed here.  The multiplicity contradiction is strictly stronger.

---

## 4. Remove residue orders one and three

PR #152 proves that the zero trace cluster, equivalently the reciprocal residue `Z=1`, never occurs in the physical P1 factor.

PR #155 O3X proves that the order-three reciprocal block

\[
Z^2+Z+1
\]

never occurs either.  Its proof treats both parities:

- for `r=1`, the local Newton segment has slope `-3/2`, requiring at least two copies while the Littlewood reduction supplies one;
- for `r>=2`, the unique slope-`-1` branch is the characteristic-zero cyclotomic `Phi_6` root, excluded from the physical factor by PR #153, and every remaining branch requires at least `2r-1>r` copies.

Therefore:

- when `r>=2`, no residue block is left at all;
- when `r=1`, only the OR1 exceptional order-nine block remains.

This proves EC items 1-3.

In particular:

\[
\boxed{m\text{ even}\Longrightarrow\text{P1 impossible}.}
\tag{4.1}
\]

This is a complete parity-class closure, with no restriction on the odd part of `m`.

---

## 5. Odd P1 requires 9|m

Now let

\[
r=1,
\qquad m=u\text{ odd}.
\]

The Littlewood reduction is squarefree:

\[
\overline P=S_m.
\]

Sections 3-4 eliminate every residue order except nine.  If

\[
9\nmid m,
\]

then `S_m` has no primitive ninth-root factor, so `bar M` would have no nonconstant factor.  This is impossible.

Hence

\[
\boxed{9\mid m.}
\]

This proves EC.2.

---

## 6. The remaining factor has exact degree six

For odd `m` divisible by nine, the primitive ninth roots occur in `S_m` exactly once.  Over `F_2`,

\[
\boxed{
\Phi_9(Z)=Z^6+Z^3+1
}
\tag{6.1}
\]

is irreducible, because

\[
\operatorname{ord}_9(2)=6.
\]

Its trace polynomial is

\[
\boxed{q_9(T)=T^3+T+1.}
\tag{6.2}
\]

Indeed

\[
Z^3q_9(Z+Z^{-1})=Z^6+Z^3+1.
\]

Every other irreducible factor of `S_m` belongs to a residue order already excluded.  Since `M` is nonconstant and `bar M|S_m`, the only possibility is

\[
\boxed{\overline M=\Phi_9.}
\]

Reduction preserves the degree of a monic polynomial.  Hence

\[
\deg M=6,
\qquad
\deg h=3,
\]

and the trace reduction is exactly

\[
\overline h=q_9.
\]

This proves EC.3-EC.4.

---

## 7. Characteristic-zero interpretation

PR #153 classifies every cyclotomic factor of the P1 reciprocal polynomial

\[
F_m(Z)=Z^{2m}+4Z^{m+1}-6Z^m+4Z^{m-1}+1.
\]

The only cyclotomic factor is `Phi_6`, and only when `6|m`.  Our remaining branch has `m` odd, so `6` does not divide `m`; in fact `F_m` has no cyclotomic factor at all.

Therefore the surviving sextic `M` must be noncyclotomic.

The entire P1 endpoint is now reduced to:

> `m` is an odd multiple of nine and `F_m` has a noncyclotomic reciprocal irreducible sextic factor `M` such that
> \[
> \overline M=\Phi_9\pmod2
> \]
> and whose physical unit-circle root lies in the P1 arc `0<arg z<pi/m`.

This is much smaller than the previous arbitrary-degree factor problem.

---

## 8. Next exact target

There are several concrete ways to attack the sextic endpoint.

### A. Cubic trace remainder

Write

\[
h(T)=T^3+aT^2+bT+c,
\]

with

\[
a\equiv0,
\quad b\equiv1,
\quad c\equiv1
\pmod2.
\]

Since

\[
h\mid G_m(T)=C_m(T)+4T-6,
\]

reduce the Chebyshev recurrence modulo `h`.  For `m\equiv0 mod9`, prove no integral cubic with the displayed parity can make the remainder vanish while containing the distinguished P1 real root near `2`.

### B. Mod-three sparse factorization

PR #153 gives

\[
F_m(Z)\equiv(Z^{m-1}+1)(Z^{m+1}+1)\pmod3.
\]

Classify reciprocal sextic divisors of this product compatible with

\[
M\equiv\Phi_9\pmod2.
\]

### C. Unit-circle cubic trace geometry

For odd `m`, `G_m(T)` has no real root outside `[-2,2]`.  A cubic factor containing the P1 root therefore has tightly constrained conjugate geometry.  Combine this with noncyclotomic reciprocity and the P1 positive-sign equation.

Any exclusion of this one sextic class closes P1 completely.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| nontrivial trace root multiplicity is two in `C_u mod2` | proved | reciprocal identity + étale trace map |
| SR2/OR1 force full `q^(2r)` local trace cluster | proved in their stated residue ranges | degree lower bound equals total cluster degree |
| reciprocal exponent becomes `2r` | proved | reciprocal lift of the monic local factor |
| Littlewood supplies only exponent `r` | proved | exact factorization of `S_m mod2` |
| all even `m` P1 | excluded, conditional only on audited O3X dependency | no residue block remains |
| odd `m` with `9 not divide m` P1 | excluded | no allowed residue block remains |
| remaining `M mod2=Phi_9`, degree six | proved | squarefree odd `S_m`, unique surviving residue order |
| odd multiples of nine | still open | order-nine first lifting obstruction cancels |
| Level I | still open | S1 and broader Target C remain |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P1 Littlewood: M|P and P mod2=S_m=(Z+1)^(r-1) S_u^r, r=2^k.
For a nontrivial odd residue trace factor q(T), q^2 exactly divides C_u mod2, hence
q^(2r) is the whole corresponding trace cluster of G_ru mod2.

SR2 (r>=2, order !=3) gives local degree >= total cluster degree 2r deg q, so any
occurrence forces the whole q^(2r) cluster into h.  OR1 gives the same q^2 conclusion
for r=1 except orders 3 and 9.  Reciprocal lift therefore puts the corresponding
odd-cyclotomic factor into M mod2 with exponent 2r.  But S_m supplies exponent only r.
Contradiction.

PR #152 separately removes order 1.  PR #155 O3X removes order 3.  Therefore:
  r>=2 (m even): no residue block remains -> P1 impossible for every u.
  r=1 (m odd): only residue order 9 remains.
Hence odd P1 requires 9|m.  Since S_m is squarefree and Phi_9 is irreducible mod2,
  M mod2=Phi_9=Z^6+Z^3+1,
  deg M=6,
  h mod2=T^3+T+1,
  deg h=3.
PR #153 says the characteristic-zero M is noncyclotomic.

Thus all of P1 is reduced to one endpoint: odd m divisible by 9 and a noncyclotomic
reciprocal sextic factor of F_m reducing to Phi_9 mod2.  Kill that sextic and P1 is closed.
```