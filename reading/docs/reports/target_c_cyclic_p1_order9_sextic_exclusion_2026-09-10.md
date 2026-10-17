> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_order9_sextic_exclusion_2026-09-10.md) · source SHA-256 `5f6a3b72b23b736c4bb9204aebef88b04b687953d7e4d785c199dde98ba2e622`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C752F3655B0D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exclude the final order-nine sextic and close cyclic P1

**Date:** 2026-09-10  
**Run type:** exact mod-four lift + endpoint-value divisor contradiction  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** EC even/odd residue collapse on this branch; OR1 order-nine lifting calculation; PR #155 O3X order-three exclusion  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`, but the entire cyclic P1 subbranch is now excluded.

EC reduces every possible P1 survivor to one final arithmetic state:

```math
m=q-2\text{ is odd},
\qquad
9\mid m,
```

and the physical trace minimal polynomial is a monic cubic

```math
h(T)=T^3+AT^2+BT+C\in\mathbb Z[T]
```

with

```math
\overline h(T)=T^3+T+1
\qquad\text{over }\mathbf F_2.
```

Equivalently the reciprocal minimal polynomial is a nonconstant sextic reducing to `Phi_9` modulo two.

The order-nine mod-four lift is rigid enough to contradict the two trivial endpoint values of the P1 trace polynomial.

### Theorem O9X — final P1 exclusion

No cyclic P1 endpoint exists.

More precisely, the only EC survivor would have to satisfy

```math
\boxed{
h(T)\equiv T^3+2T^2+T+1\pmod4.}
\tag{O9X.1}
```

But every odd `m` has

```math
G_m(2)=4,
\qquad
G_m(-2)=-16,
```

and `h|G_m`.  The congruence O9X.1 makes these two divisibility constraints incompatible.

Therefore

```math
\boxed{\text{P1 is impossible for every sufficiently large cyclic Target C source}.}
\tag{O9X.2}
```

The remaining `d_H=1` cyclic endpoint is only S1.

---

## 1. Recall the unique remaining residue

EC proves:

1. every even `m` P1 is impossible;
2. every odd P1 must have `9|m`;
3. in that branch
   
   ```math
   \deg h=3,
   \qquad
   \overline h(T)=q_9(T):=T^3+T+1.
   \tag{1.1}
   ```


Let

```math
\tau\in\mathbf F_8
```

be a root of `q_9`.  Thus

```math
\boxed{\tau^3+\tau+1=0.}
\tag{1.2}
```

OR1 identified this polynomial exactly as the trace residue of primitive ninth roots.

Let `K/Q_2` be the unramified cubic trace field and let

```math
a=\zeta+\zeta^{-1}
```

be the Teichmüller ninth-root trace lift, so `a` reduces to `tau`.

---

## 2. The order-nine root modulo four

OR1 analyzes the `r=1` local equation.  Write the trace root as

```math
T=a+X,
\qquad X=2W.
```

For the residual root `omega=bar W`, OR1 gives

```math
\omega^2=\tau^2(\tau+1)
\tag{2.1}
```

and the mod-four lifting obstruction vanishes exactly because (1.2) holds.

In the order-nine case the explicit value of `omega` is

```math
\boxed{\omega=\tau^2+1.}
\tag{2.2}
```

Indeed OR1's vanishing relation gives

```math
\omega=\tau(\tau^2+\tau+1)
=\tau^3+\tau^2+\tau
=\tau^2+1
```

using `tau^3=tau+1` in characteristic two.

Use the same length-two Witt notation as OR1: modulo four, write an unramified integer as

```math
(x_0,x_1)=[x_0]+2[x_1].
```

OR1 proves

```math
\boxed{a=(\tau,1).}
\tag{2.3}
```

Since

```math
2W\equiv(0,\omega)\pmod4,
```

we obtain

```math
T=a+2W
=(\tau,1+\omega)
=(\tau,\tau^2).
\tag{2.4}
```

Thus every root in the remaining order-nine cubic branch has, modulo four, the Frobenius conjugates of the Witt element

```math
\boxed{t=(\tau,\tau^2).}
\tag{2.5}
```

There is no branch choice at this precision.

---

## 3. Compute the unique monic cubic lift

Define

```math
H_4(T):=T^3+2T^2+T+1
\qquad\text{in }(\mathbb Z/4\mathbb Z)[T].
```

We verify directly that

```math
H_4(t)=0.
```

The length-two Witt multiplication rule gives

```math
t^2=(\tau^2,0),
\tag{3.1}
```

and

```math
t^3=(\tau^3,\tau^6).
\tag{3.2}
```

First compute

```math
t^3+t+1.
```

Using the Witt addition carry and `tau^3+tau+1=0`, the first coordinate vanishes and the second coordinate is

```math
\tau^6+\tau^2+\tau^4+1.
```

Now

```math
\tau^4=\tau^2+\tau,
\qquad
\tau^6=(\tau^3)^2=\tau^2+1,
```

so

```math
\tau^6+\tau^2+\tau^4+1
=\tau^2+\tau.
```

Hence

```math
\boxed{t^3+t+1=(0,\tau^2+\tau).}
\tag{3.3}
```

On the other hand multiplication by the integer two gives

```math
2t^2=(0,\tau^4)
=(0,\tau^2+\tau).
\tag{3.4}
```

Adding (3.3) and (3.4) gives zero. Therefore

```math
\boxed{H_4(t)=0.}
\tag{3.5}
```

Now let `h_4` be the reduction modulo four of the characteristic-zero cubic `h`.  It is monic of degree three and has `t` as a root.

The monic cubic `H_4` is unique with this property and reduction `q_9` modulo two.  To see this without invoking any factorization theorem, subtract two such cubics.  The difference has degree at most two and vanishes at `t`.  Reducing modulo two gives a polynomial of degree at most two vanishing at `tau`, whose minimal polynomial over `F_2` has degree three; hence every coefficient is even.  Divide the difference by two and repeat the same reduction argument.  All coefficients are divisible by four.

Thus

```math
\boxed{h(T)\equiv T^3+2T^2+T+1\pmod4.}
```

This proves O9X.1.

In coefficient form,

```math
\boxed{A\equiv2,\qquad B\equiv1,\qquad C\equiv1\pmod4.}
\tag{3.6}
```

---

## 4. Evaluate at T=2

The P1 trace polynomial is

```math
G_m(T)=C_m(T)+4T-6.
```

For every `m`,

```math
C_m(2)=2.
```

Therefore

```math
\boxed{G_m(2)=4.}
\tag{4.1}
```

Since `h` is monic and divides the monic integer polynomial `G_m`, Gauss's lemma gives an integer quotient.  Hence

```math
\boxed{h(2)\mid4.}
\tag{4.2}
```

But (3.6) gives

```math
\begin{aligned}
h(2)
&=8+4A+2B+C\\
&\equiv3\pmod4.
\end{aligned}
```

Thus `h(2)` is an odd divisor of four congruent to three modulo four.  The only possibility is

```math
\boxed{h(2)=-1.}
\tag{4.3}
```

Consequently

```math
8+4A+2B+C=-1,
```

so

```math
\boxed{C=-9-4A-2B.}
\tag{4.4}
```

---

## 5. Evaluate at T=-2 and contradict divisibility

The remaining EC branch has `m` odd.  Therefore

```math
C_m(-2)=-2,
```

and hence

```math
\boxed{G_m(-2)=-16.}
\tag{5.1}
```

Again integer divisibility gives

```math
\boxed{h(-2)\mid-16.}
\tag{5.2}
```

Use (4.4):

```math
\begin{aligned}
h(-2)
&=-8+4A-2B+C\\
&=-8+4A-2B-9-4A-2B\\
&=\boxed{-17-4B.}
\end{aligned}
\tag{5.3}
```

Since

```math
B\equiv1\pmod4,
```

we get

```math
\boxed{h(-2)\equiv-21\equiv11\pmod{16}.}
\tag{5.4}
```

But `h(-2)` is odd by (5.3).  The only odd integer divisors of `-16` are

```math
\pm1,
```

which are congruent to

```math
1\quad\text{or}\quad15\pmod{16},
```

never `11`.

Contradiction.

Therefore the order-nine cubic cannot exist.  Combined with EC, no P1 endpoint exists. `square`

---

## 6. Consequence for the cyclic d_H=1 phase

The exact D1 classification on PR #118 splits `d_H=1` into

```text
P1: one parallel-side pair, no genuine off-circle antipodal vertex pair;
S1: no parallel sides, one genuine short antipodal pair.
```

O9X eliminates P1 completely.

Thus every sufficiently large cyclic `d_H=1` survivor must lie in

```math
\boxed{\text{S1 only}.}
\tag{6.1}
```

This is a genuine branch closure, not a density or asymptotic constant improvement.

---

## 7. Dependency note

The only sibling-PR dependency not reproved in this report is O3X from PR #155, which excludes the exceptional order-three residue block.  The O3X proof is independent of the invalid `d_H=2` Euler-trail/path inference flagged in PR #151.  It uses only the reciprocal P1 polynomial, its local Newton polygon at the Teichmüller cube root, and PR #153's exact cyclotomic-factor classification.

Everything from the order-nine reduction onward is proved here directly.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| remaining P1 state is odd `9|m`, cubic trace factor | proved in EC, using #152/SR2/OR1/#155 |
| order-nine trace root mod four is `(tau,tau^2)` | proved | OR1 residual root + Witt lift |
| unique cubic lift `T^3+2T^2+T+1 mod4` | proved | direct Witt evaluation + degree-three uniqueness |
| `h(2)=-1` | proved | `h(2)|4` and mod-four class |
| `h(-2)` contradiction | proved | exact elimination of `C`, mod-16 residue vs divisor of 16 |
| P1 | excluded | all residue cases exhausted |
| cyclic `d_H=1` | not closed | S1 remains |
| Level I | still open | S1 and other post-ZF/global branches remain |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN, but P1 is closed.

EC leaves only odd m divisible by 9, with trace minimal polynomial
  h=T^3+A T^2+B T+C,
  h mod2=T^3+T+1.
Let tau^3+tau+1=0 be the primitive-order-9 trace residue.  OR1 gives the residual
correction omega=tau^2+1.  Since the Teichmuller trace lift has Witt digits a=(tau,1),
the actual trace root modulo 4 is
  t=(tau,tau^2).
Direct length-two Witt arithmetic gives
  t^2=(tau^2,0),
  t^3+t+1=(0,tau^2+tau)=2t^2,
so
  t^3+2t^2+t+1=0 mod4.
Degree-three uniqueness therefore forces
  h(T)=T^3+2T^2+T+1 mod4,
so A=2, B=1, C=1 mod4.

Because h|G_m and G_m(2)=4,
  h(2)|4.
But h(2)=3 mod4, hence h(2)=-1 and
  C=-9-4A-2B.
For odd m, G_m(-2)=-16, so h(-2)|-16.  Yet
  h(-2)=-17-4B=11 mod16,
and it is odd.  The only odd divisors of 16 are +/-1, residues 1 or 15 mod16.
Contradiction.

Therefore P1 is impossible.  The cyclic d_H=1 endpoint is reduced to S1 only.
```
