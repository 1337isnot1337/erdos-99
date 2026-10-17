> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_odd_r1_second_order_2026-09-10.md) · source SHA-256 `dc96a5f49829d66d008a313efe7621539a932a01f6812f0c29abb26f88c14885`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-88295321F945","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — the odd P1 residue cluster is ramified except at residue order nine

**Date:** 2026-09-10  
**Run type:** exact mod-four / unramified 2-adic lift obstruction  
**Target:** cyclic primitive `d_H=1`, P1 endpoint with `r=1`  
**Depends on:** PR #152 residue localization; SR2 local notation on this branch; standard Teichmüller/Witt length-two arithmetic in an unramified 2-adic field  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

SR2 proves doubled ramification for every nonzero odd-order residue cluster when

$$
r=2^k\ge2,
$$

except for the separate order-three cluster.  The proof deliberately left `r=1` open because the explicit `X` perturbation and the integral lifting error have the same valuation.

That coincidence can be resolved exactly modulo four.

### Theorem OR1 — odd-cluster ramification criterion

Let `u` be odd.  Let `xi` be a nontrivial residue `u`-th root of unity of order

$$
d\ne3,
$$

let

$$
\tau=\xi+\xi^{-1},
$$

and consider the local trace cluster of

$$
G_u(T)=C_u(T)+4T-6
$$

over the unramified 2-adic trace field of `tau`.

If

$$
\boxed{d\ne9,}
\tag{OR1.1}
$$

then the local double cluster is one ramified quadratic factor.  Equivalently every root in that cluster has ramification index two over the unramified trace field.

The only residue order at which the first mod-four obstruction vanishes is

$$
\boxed{d=9.}
\tag{OR1.2}
$$

No claim is made here about whether the order-nine cluster ultimately splits or ramifies at a higher lifting stage.

Combining OR1 with SR2 gives the uniform local cost

$$
\boxed{2r f_d}
\tag{OR1.3}
$$

for every `r=2^k>=1` and every nonzero residue order `d` other than `3` and, only when `r=1`, `9`.

### Prime-family corollary

A prime residue order `p>=5` is never `3` or `9`.  Therefore the maximal-projective-order prime exclusion from SR2 extends from `k>=1` to all

$$
\boxed{k\ge0.}
\tag{OR1.4}
$$

Thus if

$$
q-2=2^k p,
\qquad p\ge5\text{ prime},
\qquad
\min\{f:2^f\equiv\pm1\pmod p\}=\frac{p-1}{2},
$$

then P1 is impossible for every `k>=0`.

---

## 1. Local expansion at a nonzero odd-order trace

Let `K/Q_2` be the unramified trace field.  Choose the Teichmüller lift `zeta` of `xi` and put

$$
a=\zeta+\zeta^{-1}.
$$

Then

$$
C_u(a)=2.
$$

As in SR2,

$$
U(X):=C_u(a+X)-2
=cX^2+d_3X^3+O(X^4),
\tag{1.1}
$$

where `c` is a unit.  The coefficients can be computed from the parametrization

$$
T(s)=\zeta e^s+\zeta^{-1}e^{-s}.
$$

At `s=0`,

$$
T'(0)=\zeta-\zeta^{-1},
\qquad
T''(0)=a,
$$

while

$$
C_u(T(s))=e^{us}+e^{-us}.
$$

The first derivative vanishes and the second/third chain rules give

$$
\boxed{
c=\frac{u^2}{a^2-4},}
\tag{1.2}
$$

$$
\boxed{
d_3=-\frac{u^2a}{(a^2-4)^2}.}
\tag{1.3}
$$

For `d!=3`, the residue trace is not one, so `a-1` is a unit.

The first Newton segment of

$$
G_u(a+X)=U(X)+4(a-1)+4X
$$

is therefore

$$
(0,2)\longrightarrow(2,0),
$$

so every root in the cluster has

$$
\boxed{v(X)=1.}
\tag{1.4}
$$

Write

$$
X=2W,
\qquad v(W)=0.
$$

Dividing by four gives

$$
0=(a-1)+cW^2+2W+2d_3W^3+O(4).
\tag{1.5}
$$

The question is whether this repeated residual root can lift in an unramified extension.

---

## 2. Length-two Witt arithmetic

Let `kappa` be the residue field of `K`.  Modulo four, every element has a unique Teichmüller expansion

$$
[x_0]+2[x_1],
\qquad x_0,x_1\in\kappa.
$$

We denote this pair by `(x_0,x_1)`.  The only length-two formulas needed are

$$
(x_0,x_1)+(y_0,y_1)
=(x_0+y_0,\ x_1+y_1+x_0y_0),
\tag{2.1}
$$

and

$$
(x_0,x_1)(y_0,y_1)
=(x_0y_0,\ x_0^2y_1+y_0^2x_1).
\tag{2.2}
$$

These follow immediately by comparing the first two Witt ghost components.  They are included here so no black-box local-field computation is hidden in the proof.

Since `zeta=[xi]` and `zeta^{-1}=[xi^{-1}]`, writing

$$
\tau=\xi+\xi^{-1}
$$

gives

$$
\boxed{a=(\tau,1).}
\tag{2.3}
$$

Also

$$
-1=(1,1),
$$

so

$$
\boxed{a-1=(\tau+1,\tau).}
\tag{2.4}
$$

Because `u` is odd,

$$
u^2\equiv1\pmod8.
$$

Modulo four, `a^2-4` is simply `a^2`, and (2.2) shows that the square of any Witt unit `(x_0,x_1)` has second coordinate zero.  Hence

$$
\boxed{c\equiv a^{-2}=(\tau^{-2},0)\pmod4.}
\tag{2.5}
$$

From (1.3), only the residue of `d_3` is needed:

$$
\boxed{\overline{d_3}=\tau^{-3}.}
\tag{2.6}
$$

---

## 3. The unique residual square root

Reduce (1.5) modulo two.  If

$$
\omega:=\overline W,
$$

then

$$
\tau^{-2}\omega^2+(\tau+1)=0,
$$

or

$$
\boxed{\omega^2=\tau^2(\tau+1).}
\tag{3.1}
$$

The residue field is perfect, so `omega` is uniquely determined.

Suppose the local root could lie in an unramified extension of `K`.  Its residue is still `omega`, which already belongs to the base residue field.  Modulo four we may therefore replace `W` by the Teichmüller lift

$$
[\omega]=(\omega,0),
$$

because changing `W` by a multiple of two changes `W^2` only by a multiple of four, and changes the terms already multiplied by two only by a multiple of four.

Using (2.5) and (3.1),

$$
c[\omega]^2=(\tau+1,0).
$$

Adding this to (2.4) with (2.1) gives

$$
(a-1)+c[\omega]^2
=
(0,\tau+(\tau+1)^2).
$$

Thus

$$
\boxed{
\frac{(a-1)+c[\omega]^2}{2}
\equiv \tau^2+\tau+1
\pmod2.
}
\tag{3.2}
$$

The remaining valuation-one correction in (1.5) is

$$
W+d_3W^3.
$$

Modulo two, (2.6) and (3.1) give

$$
\begin{aligned}
\omega+\tau^{-3}\omega^3
&=\omega\left(1+\tau^{-3}\omega^2\right)\\
&=\omega\left(1+\frac{\tau+1}{\tau}\right)\\
&=\boxed{\frac\omega\tau}.
\end{aligned}
\tag{3.3}
$$

Therefore an unramified lift can exist only if

$$
\boxed{
\tau^2+\tau+1+\frac\omega\tau=0.
}
\tag{3.4}
$$

This condition is independent of the chosen unramified extension.

---

## 4. The obstruction vanishes exactly at residue order nine

Assume (3.4).  Then

$$
\omega=\tau(\tau^2+\tau+1).
$$

Square and use (3.1):

$$
\tau^2(\tau+1)
=
\tau^2(\tau^2+\tau+1)^2.
$$

Since `tau!=0`, divide by `tau^2`:

$$
\tau+1=\tau^4+\tau^2+1.
$$

Hence

$$
\tau^4+\tau^2+\tau=0,
$$

and therefore

$$
\boxed{\tau^3+\tau+1=0.}
\tag{4.1}
$$

Conversely, if (4.1) holds, the two sides defining `omega` have the same square; the Frobenius square map is injective in the residue field, so (3.4) follows.  Thus the mod-four obstruction vanishes exactly when (4.1) holds.

Now take the reciprocal lift of the cubic:

$$
\begin{aligned}
Z^3\left[(Z+Z^{-1})^3+(Z+Z^{-1})+1\right]
&=Z^6+Z^3+1\\
&=\frac{Z^9-1}{Z^3-1}
\end{aligned}
$$

in characteristic two.

Its roots are exactly the roots of unity of order nine.  Therefore

$$
\boxed{
\tau^3+\tau+1=0
\iff
\operatorname{ord}(\xi)=9.
}
\tag{4.2}
$$

This proves OR1.2.

If `d!=9`, condition (3.4) fails.  Hence no root of the local double cluster exists in any unramified extension of `K`.  The cluster has total degree two over `K`, so it must be one ramified quadratic factor.  This proves OR1.1. `square`

---

## 5. Uniform local-cost corollary

For `r>=2`, SR2 already proves ramification index divisible by `2r` for every non-order-three residue cluster, including order nine.

For `r=1`, OR1 proves ramification index two for every residue order other than three and nine.

Therefore a nonzero residue trace orbit of degree `f_d` has exact minimum local factor cost

$$
\boxed{2r f_d}
$$

throughout

```text
r>=2, d!=3;
or
r=1, d not in {3,9}.
```

For prime `d=p>=5`, both exceptional orders are absent, so this holds for every power of two

$$
r=2^k,\qquad k>=0.
$$

---

## 6. Maximal-projective-order primes are now fully excluded

Let

$$
u=p>=5
$$

be prime and suppose

$$
f_p=\frac{p-1}{2}.
$$

PR #152 says the P1 trace minimal polynomial must use a nonzero `p`-trace cluster.  OR1/SR2 give local degree at least

$$
2r f_p=r(p-1)
$$

for every `r=2^k`, including `r=1`.

RB gives the global degree ceiling

$$
\deg h\le\frac{r(p-1)}2.
$$

Contradiction.

Hence

$$
\boxed{
q-2=2^k p,
\ p>=5\text{ prime},
\ f_p=(p-1)/2
\Longrightarrow
\text{P1 impossible for every }k>=0.
}
\tag{6.1}
$$

This strictly strengthens SR2 by removing its `k>=1` restriction.

---

## 7. What remains

The exceptional residue orders are now concrete.

1. `d=3`: the constant `a-1` loses unit valuation, producing the separate cluster geometry used by PR #150.
2. `d=9` with `r=1`: the first mod-four obstruction cancels exactly.  A mod-eight or next Newton calculation is needed.
3. For prime odd parts with nonmaximal projective order, there are multiple nonzero trace residue orbits.  A rational P1 factor might in principle select one orbit whose exact local degree `2r f_p` fits inside RB's global degree budget.

The next useful arithmetic target is therefore either the order-nine next lift or a Galois/global argument coupling the multiple prime residue orbits.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exact coefficients `c,d_3` | proved | chain rule in root-of-unity parametrization |
| mod-four Witt coordinates of `a-1,c` | proved | length-two formulas |
| unramified-lift criterion (3.4) | proved | root equation modulo four |
| criterion equivalent to `tau^3+tau+1=0` | proved | residual square relation |
| reciprocal cubic corresponds exactly to order nine | proved | `Z^6+Z^3+1=(Z^9-1)/(Z^3-1)` |
| `r=1,d!=3,9` cluster is ramified quadratic | proved | no unramified root + total cluster degree two |
| maximal-projective-order prime P1 for all `k>=0` | excluded | OR1/SR2 local cost vs RB ceiling |
| `r=1,d=9` | open | first mod-four obstruction vanishes |
| Level I | still open | other P1/S1/global branches remain |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For r=1, at a nonzero odd-order residue trace tau lift a, write X=2W.  The local P1
equation divided by four is
  0=(a-1)+cW^2+2W+2d3 W^3 mod 4,
with
  c=u^2/(a^2-4), d3=-u^2 a/(a^2-4)^2.
In O_K/4, write Witt digits [x0]+2[x1].  For tau=xi+xi^-1:
  a=(tau,1),
  a-1=(tau+1,tau),
  c=(tau^-2,0).
The residual root omega satisfies
  omega^2=tau^2(tau+1).
An unramified lift would force
  tau^2+tau+1+omega/tau=0.
Squaring and using the residual equation gives
  tau^3+tau+1=0.
Its reciprocal lift is
  Z^6+Z^3+1=(Z^9-1)/(Z^3-1),
so cancellation occurs exactly at residue order 9.
Therefore every r=1 residue cluster with d not in {3,9} is ramified quadratic.
Combined with SR2, every prime p>=5 has local cost 2r f_p for all r=2^k.
If f_p=(p-1)/2, that cost exceeds RB's global P1 degree ceiling by factor two, so
P1 is impossible for every k>=0.
```