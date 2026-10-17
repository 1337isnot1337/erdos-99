> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_p1_quadratic_residue_obstruction_2026-09-10.md) · source SHA-256 `cdc1a88ae61c186aa5aab47ccc89776edeebea5b8625fbc49bd5d9dbe2c25bea`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-36392B4B7FDF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — audit correction: the proposed P1 quadratic-residue obstruction is automatic

**Date:** 2026-09-10  
**Run type:** rejected-route audit / exact identity  
**Target:** cyclic `d_H=1` P1 arithmetic endpoint  
**Depends on:** PA trace polynomial notation  
**External literature:** none  
**Computation:** none

## 1. Disposition

An earlier version of this report derived, from the P1 Littlewood closure, the field-square conditions

$$
z^2-z+1\in\mathbb Q(z)^{\times2}
$$

and

$$
(t+2)(t-1)\in\mathbb Q(t)^{\times2},
\qquad t=z+z^{-1}.
$$

Those identities are correct, but the interpretation as an **independent arithmetic obstruction** was wrong.

They already follow from the squared P1 geometric equation

$$
\boxed{H_n(t)=D_n(t,1)+4t-6=0}
\tag{AQ.1}
$$

alone. Therefore they cannot distinguish a trace factor that also admits a Littlewood annihilator.

The proposed QR route is rejected as redundant. This correction is recorded explicitly so later work does not spend time testing an automatic square condition.

---

## 2. Exact automatic square identity in the trace field

Let

$$
x:=\frac t2.
$$

The Dickson/Chebyshev relation is

$$
D_n(t,1)=2T_n(x).
$$

Equation AQ.1 therefore gives

$$
T_n(x)=3-4x.
\tag{2.1}
$$

Use the standard identity

$$
T_n(x)^2-1=(x^2-1)U_{n-1}(x)^2,
\tag{2.2}
$$

where `U_{n-1}` is the Chebyshev polynomial of the second kind.

Substituting (2.1),

$$
\begin{aligned}
(x^2-1)U_{n-1}(x)^2
&=(3-4x)^2-1\\
&=16x^2-24x+8\\
&=8(2x-1)(x-1).
\end{aligned}
$$

The distinguished P1 root has `t<2`, hence `x!=1`; cancel `x-1`:

$$
(x+1)U_{n-1}(x)^2=8(2x-1).
$$

Returning to `t`,

$$
\boxed{
(t+2)U_{n-1}(t/2)^2=16(t-1).
}
\tag{AQ.2}

Consequently

\[
\boxed{
(t+2)(t-1)
=
\left(
\frac{t+2}{4}U_{n-1}(t/2)
\right)^2.
}
\tag{AQ.3}

Thus `(t+2)(t-1)` is a square in the residue field of **every** nontrivial root of `H_n`, whether or not any Littlewood polynomial vanishes there.

---

## 3. The cyclotomic square is automatic as well

Let

\[
z+z^{-1}=t.
$$

Then

$$
t+2=\frac{(z+1)^2}{z}
$$

and

$$
z^2-z+1=z(t-1).
$$

Let

$$
s:=\frac{t+2}{4}U_{n-1}(t/2),
\qquad
s^2=(t+2)(t-1)
$$

from AQ.3. Since `z!=-1` in the P1 geometry,

$$
\boxed{
u:=\frac{zs}{z+1}}
$$

satisfies

$$
\begin{aligned}
u^2
&=\frac{z^2}{(z+1)^2}(t+2)(t-1)\\
&=z(t-1)\\
&=z^2-z+1.
\end{aligned}
$$

Therefore

$$
\boxed{z^2-z+1\in\mathbb Q(z)^{\times2}}
\tag{3.1}
$$

is also automatic from `H_n(t)=0`.

---

## 4. What remains valid from the original derivation

The earlier Littlewood/discriminant calculation was algebraically correct: if

$$
P=S_n-2A,
\qquad P(z)=0,
$$

and `B=(z-1)A(z)`, then eliminating `z^n` indeed produces a quadratic in `B` whose discriminant is

$$
4(z-1)^2(z^2-z+1).
$$

What failed was the novelty inference. AQ.2-AQ.3 show that this discriminant is already forced to be a square by the geometric trace equation itself.

Hence none of the following can be used as a P1 exclusion criterion:

- `z^2-z+1` being a square in `Q(z)`;
- `(t+2)(t-1)` being a square in `Q(t)`;
- the corresponding norm-square condition;
- the corresponding real-signature condition.

They are identities on the complete P1 trace variety, not filters selecting Littlewood-compatible points.

---

## 5. Surviving arithmetic frontier

The valid arithmetic stack on this PR is therefore:

1. **PA:** if `n=q-2` is a power of two, the shifted reciprocal polynomial has one 2-adic Newton segment of slope `-1/n`, forcing algebraic degree at least `n`; this contradicts the degree-`n-1` Littlewood annihilator.
2. **TR:** for arbitrary `n`, a P1 Littlewood root forces the distinguished trace root `t` to have degree at most
   $$
   \left\lfloor\frac{n-1}{2}\right\rfloor.
   $$
3. **Open:** prove the distinguished factor of
   $$
   H_n(T)=D_n(T,1)+4T-6
   $$
   has degree at least `ceil(n/2)`, or exploit additional sign-word structure not already encoded by `H_n=0`.

The QR square route is removed from that frontier.

---

## 6. Regression value

This correction is useful beyond bookkeeping. The factorization

$$
(t+2)U_{n-1}(t/2)^2=16(t-1)
$$

explains why substitutions based on

$$
r^2=\frac{t+2}{t-1}
$$

produce apparent low-degree splittings of transformed P1 polynomials: the square root is built into the Chebyshev equation. Such splittings are therefore not evidence of an additional Littlewood obstruction.

---

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

AUDIT CORRECTION: the earlier QR condition is true but automatic.

H_n(t)=0 gives, with x=t/2,
  T_n(x)=3-4x.
Using
  T_n(x)^2-1=(x^2-1)U_{n-1}(x)^2,
one obtains
  (t+2)U_{n-1}(t/2)^2=16(t-1),
so
  (t+2)(t-1)=((t+2)U_{n-1}(t/2)/4)^2.
Thus the proposed trace-field square condition holds for every root of H_n and is
not an independent P1 filter. The corresponding Phi_6(z)=z^2-z+1 square is automatic
too.

Keep PA and TR. Discard QR as an exclusion route.
Next valid target: prove the distinguished trace factor degree >=ceil(n/2), or use
sign-word information beyond H_n=0.
```
