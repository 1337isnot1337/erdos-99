> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_full_nonexceptional_residue_multiplicity_2026-09-10.md) · source SHA-256 `d171eb624d8ddd8f49fc428512223092d73d1c7a788931eea8c70414085ae3d4`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 20 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-EAFD3207F3A1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — P1 nonexceptional 2-adic trace orbits occur at full multiplicity

**Date:** 2026-09-10  
**Run type:** exact local 2-adic factor rigidity  
**Target:** cyclic primitive `d_H=1`, P1 arithmetic endpoint  
**Depends on:** P2/P3 arithmetic reduction in PR #150; RL zero-residue exclusion in this branch  
**External literature:** standard Newton-polygon root theorem only  
**Computation:** none

## 1. Result

Put

```math
m=q-2=r u,
\qquad
r=2^k,
\qquad
u=u\text{ odd},
```

and use the P1 trace polynomial

```math
G_m(T)=C_m(T)+4T-6,
```

where

```math
C_j(z+z^{-1})=z^j+z^{-j}.
```

Let

```math
Y=2\cos\delta
```

be the distinguished P1 trace root and let

```math
h(T)\in\mathbb Z[T]
```

be its monic irreducible minimal polynomial. The P1 Littlewood closure gives the reciprocal minimal polynomial

```math
M(Z)=Z^d h(Z+Z^{-1}),
\qquad d=\deg h,
```

with

```math
M\mid P,
\qquad
P(Z)\equiv S_m(Z):=1+Z+\cdots+Z^{m-1}\pmod2.
```

RL already proves that `h mod 2` has no `T` factor, so the zero trace residue is absent.

The remaining nonzero residue traces are roots of the odd-part trace polynomial. Exactly one residue is exceptional for the local calculation below: `T=1`, corresponding to primitive third roots of unity and present only when `3|u`.

### Theorem FRM — full residue multiplicity

Let

```math
f(T)\in\mathbb F_2[T]
```

be an irreducible factor occurring in the nonzero part of `G_m mod 2`, and suppose

```math
f\ne T+1.
```

If `f` divides `h mod 2`, then in fact

```math
\boxed{f(T)^r\mid h(T)\pmod2.}
\tag{FRM.1}
```

and the exponent is exactly `r`: if

```math
f^a\Vert h\pmod2,
```

then

```math
\boxed{a=r.}
\tag{FRM.2}
```

Equivalently, every nonexceptional odd-order trace orbit is binary:

```text
absent from the physical P1 factor,
or present with the full multiplicity r=2^k.
```

No partial multiplicity is possible.

The proof has two halves:

1. a local Newton polygon forces `r|a`;
2. the Littlewood reduction forces `a<=r`.

Thus the arithmetic factor problem becomes a subset-of-residue-orbits problem, apart from the single order-three trace orbit.

---

## 2. Mod-two odd-part factorization

Repeated doubling gives

```math
C_{2j}(T)=C_j(T)^2-2.
```

Modulo two,

```math
C_{2j}(T)\equiv C_j(T)^2.
```

Hence

```math
\boxed{C_m(T)\equiv C_u(T)^r\pmod2.}
\tag{2.1}
```

For odd `u`, the nonzero roots of `C_u mod 2` are exactly the traces

```math
\bar\omega+\bar\omega^{-1}
```

of nontrivial odd-order `u`-th roots of unity in `\overline{\mathbb F}_2`.

More explicitly one may write

```math
\boxed{C_u(T)=TQ_u(T)^2\quad\text{in }\mathbb F_2[T],}
\tag{2.2}
```

where `Q_u` is squarefree of degree `(u-1)/2`. Squarefreeness follows because `Z^u-1` is squarefree in characteristic two for odd `u`, and the trace map identifies precisely the inverse pair `omega,omega^{-1}` among nontrivial roots.

Since `4T-6` vanishes modulo two,

```math
\boxed{
G_m(T)\equiv T^r Q_u(T)^{2r}\pmod2.
}
\tag{2.3}
```

RL excludes the `T^r` cluster from the physical factor `h`. We now analyze one irreducible factor `f|Q_u`.

---

## 3. Lift one nonexceptional residue trace

Let

```math
\bar t\in\overline{\mathbb F}_2
```

be a root of `f`. Choose an odd-order Teichmüller root of unity

```math
\omega
```

in an unramified extension of `Q_2` whose residue is an element `\bar\omega` with

```math
\bar\omega^u=1,
\qquad
\bar t=\bar\omega+\bar\omega^{-1}.
```

Put

```math
t_0:=\omega+\omega^{-1}.
```

Then exactly

```math
\boxed{C_u(t_0)=2.}
\tag{3.1}
```

Because `f ne T+1`, we have

```math
\bar t\ne1,
```

so

```math
\boxed{t_0-1\in\mathcal O^\times.}
\tag{3.2}
```

Here `mathcal O` is the ring of integers of the chosen unramified local field.

The nontrivial root `t_0` is a double root of `C_u(T)-2`. Indeed, if `T=z+z^{-1}`, then

```math
C_u(T)-2=z^u+z^{-u}-2
=\frac{(z^u-1)^2}{z^u}.
```

Since `u` is odd and `omega ne1`, the trace map is unramified at `omega`: `omega ne omega^{-1}`. Thus the trace root has multiplicity exactly two.

The reduction is also exactly double because `Q_u` is squarefree and `bar t ne0`. Therefore the quadratic coefficient is a 2-adic unit. Consequently there is a power series / polynomial unit

```math
V(X)\in\mathcal O[X],
\qquad V(0)\in\mathcal O^\times,
```

such that

```math
\boxed{
C_u(t_0+X)-2=X^2V(X).
}
\tag{3.3}
```

---

## 4. Power-of-two doubling at the value two

Define

```math
H_r(Y):=C_r(2+Y)-2.
```

For `r=1`,

```math
H_1(Y)=Y.
```

The doubling identity gives

```math
H_{2r}(Y)=H_r(Y)(H_r(Y)+4).
\tag{4.1}
```

Inductively, for every power of two `r`,

```math
\boxed{
H_r(Y)\equiv Y^r\pmod4.
}
\tag{4.2}
```

Also `H_r(0)=0` and `H_r` is monic of degree `r`. Hence we may write

```math
\boxed{
H_r(Y)=Y^r+4\sum_{j=1}^{r-1}a_jY^j
}
\tag{4.3}
```

for integers `a_j` (with the sum empty for `r=1`).

---

## 5. Exact Newton segment above `bar t`

By composition,

```math
C_m=C_r\circ C_u.
```

Substitute `T=t_0+X` and use (3.3):

```math
\begin{aligned}
G_m(t_0+X)
&=C_r(C_u(t_0+X))+4(t_0+X)-6\\
&=H_r(X^2V(X))+4(t_0-1)+4X.
\end{aligned}
\tag{5.1}
```

By (4.3):

- the constant coefficient is `4(t_0-1)` and has valuation exactly `2` by (3.2);
- every coefficient of degrees `1,...,2r-1` has valuation at least `2`;
- the coefficient of `X^(2r)` is a unit, because it receives the unit contribution `V(0)^r` from `(X^2V)^r` and every other contribution is divisible by four.

Therefore the lower Newton polygon above the residue root `bar t` begins with the single segment

```math
\boxed{(0,2)\longrightarrow(2r,0),}
\tag{5.2}
```

whose slope is

```math
\boxed{-\frac1r.}
\tag{5.3}
```

All `2r` roots reducing to `bar t` lie on this segment and have valuation

```math
v_2(T-t_0)=\frac1r.
\tag{5.4}
```

Let `K_0/Q_2` be the unramified field generated by `t_0`. Every irreducible local factor containing one of these roots has ramification index divisible by `r`; in particular its degree over `K_0` is divisible by `r`.

Now let

```math
f^a\Vert h\pmod2.
```

Over `K_0`, the exponent `a` is the total number of roots of `h` lying above the fixed residue root `bar t`, counted with multiplicity. It is a sum of degrees of local irreducible factors on the slope `-1/r`. Hence

```math
\boxed{r\mid a.}
\tag{5.5}
```

This is the first half of FRM.

---

## 6. Littlewood multiplicity gives the opposite inequality

The monic reciprocal lift

```math
M(Z)=Z^d h(Z+Z^{-1})
```

is the minimal polynomial of the nonreal P1 root `z=e^{i delta}` and divides its Littlewood annihilator `P` over `Z[Z]`.

Modulo two,

```math
P(Z)\equiv S_m(Z)=\frac{Z^m-1}{Z-1}.
```

Write

```math
m=ru.
```

In characteristic two,

```math
Z^m-1=(Z^u-1)^r.
```

Because `u` is odd, every nontrivial `u`-th root `bar omega` is simple in `Z^u-1`; therefore every such root occurs in `S_m` with multiplicity exactly

```math
\boxed r.
\tag{6.1}
```

If `bar t=bar omega+bar omega^{-1}` occurs with exponent `a` in `h mod 2`, then substitution `T=Z+Z^{-1}` gives both `bar omega` and `bar omega^{-1}` as roots of `M mod 2`, each with multiplicity exactly `a`. This statement is valid whether the two inverse roots lie in the same Frobenius orbit or in two reciprocal Frobenius orbits.

Since

```math
M\mid P,
```

we must have

```math
M\mid S_m\pmod2.
```

Comparing the multiplicity at `bar omega` gives

```math
\boxed{a\le r.}
\tag{6.2}
```

Together with (5.5), and `a>0`, this yields

```math
a=r.
```

This proves FRM. `square`

---

## 7. Immediate algebraic-unit consequence

RL says `T` does not divide `h mod 2`. Hence

```math
h(0)\not\equiv0\pmod2.
```

Since `2 congruent 0 mod 2`,

```math
\boxed{h(2)\text{ is odd}.}
\tag{7.1}
```

Because `h` is monic irreducible and divides the monic integer polynomial `G_m`, Gauss's lemma gives an integer quotient. Evaluating at two,

```math
G_m(2)=C_m(2)+8-6=4.
```

Thus `h(2)` is an odd divisor of four:

```math
\boxed{h(2)=\pm1.}
\tag{7.2}
```

For the physical P1 root,

```math
Y=2\cos\delta,
\qquad
2-Y=4\sin^2(\delta/2)=\frac1{D^2}.
```

Therefore

```math
\boxed{
N_{\mathbb Q(Y)/\mathbb Q}(D^{-2})
=N(2-Y)
=h(2)=\pm1.
}
\tag{7.3}
```

So the exact geometric quantity `D^{-2}` is an algebraic unit in the P1 trace field.

This is a consequence, not yet a contradiction.

---

## 8. Prime odd part with one trace orbit

FRM becomes especially rigid when the odd part is an odd prime `p>=5` for which the nonzero trace roots form one Frobenius orbit over `F_2`.

Let

```math
s_p:=\min\{j>=1:2^j\equiv\pm1\pmod p\}.
```

The trace roots of primitive `p`-th roots have orbit degree `s_p`. Thus the one-orbit condition is

```math
\boxed{s_p=\frac{p-1}{2}.}
\tag{8.1}
```

Assume

```math
u=p,
\qquad s_p=(p-1)/2.
```

There is no order-three exceptional trace. RL excludes the zero trace and FRM forces the unique nonzero trace factor to occur with exponent exactly `r`. Hence

```math
\boxed{
\deg h=r\frac{p-1}{2}.
}
\tag{8.2}
```

The reciprocal minimal polynomial has degree

```math
\boxed{
\deg M=r(p-1).
}
\tag{8.3}
```

while the P1 Littlewood polynomial has degree at most

```math
m-1=rp-1.
```

Therefore the integer quotient

```math
P=M Q
```

has

```math
\boxed{
\deg Q\le r-1.
}
\tag{8.4}
```

If the signed closure has its full allowed degree `m-1`, equality holds; otherwise the quotient is even shorter.

Modulo two,

```math
S_{rp}(Z)
=(Z+1)^{r-1}\Phi_p(Z)^r
```

and `M mod 2` contains exactly the `Phi_p^r` part, so

```math
\boxed{
Q(Z)\equiv(Z+1)^{r-1}\pmod2
}
\tag{8.5}
```

in the full-degree case.

Thus trace-transitive prime odd parts reduce P1 from an arbitrary degree-`rp-1` Littlewood closure to a short cofactor problem of degree at most `r-1`.

No contradiction from (8.4)-(8.5) is claimed here.

---

## 9. Exceptional order-three residue

The hypothesis `f ne T+1` is essential.

The residue `T=1` corresponds to primitive third roots of unity. Its Teichmuller trace lift is `-1`, and

```math
-1-1=-2
```

is not a 2-adic unit. Consequently the constant term in (5.1) has valuation greater than two and the Newton polygon is different.

PR #150 exploits exactly this exceptional cluster to exclude the pure odd part `u=3` after a second Newton analysis and the Littlewood multiplicity budget.

For a general odd part divisible by three, the order-three cluster must still be handled separately. FRM makes every *other* residue orbit all-or-nothing.

---

## 10. Regression audit

### No ordinary irreducibility assumption

FRM does not assert that `G_m`, `h`, or any mod-two trace factor is irreducible beyond the explicitly chosen irreducible residue factor `f`.

### Residue trace versus root-of-unity orbit

A trace orbit may lift to one self-reciprocal root-of-unity orbit or two reciprocal root-of-unity orbits. Section 6 uses pointwise multiplicity at `bar omega`, so it is valid in both cases.

### Why exponent is `r`, not `2r`

`G_m mod 2` has trace multiplicity `2r`, but the P1 Littlewood polynomial has root-of-unity multiplicity only `r`. The reciprocal lift therefore rules out taking all `2r` trace multiplicity in the physical factor.

### Order three

Explicitly excluded from FRM and not silently treated by the unit-constant Newton segment.

### Zero residue

Handled by RL, not reproved here.

---

## 11. New arithmetic frontier

After RL + FRM, a hypothetical P1 factor is no longer an arbitrary low-degree divisor of `G_m`.

Write the squarefree odd-part trace polynomial as

```math
Q_u=(T+1)^\epsilon f_1\cdots f_s,
```

where `epsilon=1` iff `3|u`, and every `f_j` is nonexceptional. Then

```math
\boxed{
h(T)\pmod2
=(T+1)^a\prod_{j\in J}f_j(T)^r
}
\tag{11.1}
```

for some subset `J` and some exceptional exponent `a` only when `3|u`.

RL removes the zero cluster. FRM says every nonexceptional exponent is exactly `r`.

Thus the remaining arithmetic problem is finite and combinatorial at fixed odd part `u`: determine which subsets `J` can lift to the single rational irreducible factor containing the distinguished largest real P1 root while obeying

```math
\deg h\le\frac{ru-1}{2}.
```

A useful next target is to classify the exceptional order-three exponent for general `3|u`, and then couple the all-or-nothing residue pattern to a second prime or to the short Littlewood quotient.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

m=ru, r=2^k, u odd. RL excludes trace residue T=0 from the physical P1 factor h.
For a nonzero residue trace tbar !=1 choose Teichmuller trace lift t0. Then
  C_u(t0+X)-2 = X^2 V(X), V(0) a 2-adic unit.
For r=2^k,
  H_r(Y)=C_r(2+Y)-2 == Y^r mod 4.
Therefore
  G_m(t0+X)=H_r(X^2V)+4(t0-1)+4X
has initial Newton segment
  (0,2)->(2r,0), slope -1/r.
Hence if f^a || h mod2 at this residue orbit, r|a.

The reciprocal minimal polynomial M divides the P1 Littlewood P, and
  P mod2 = S_m.
Every nontrivial u-th root has multiplicity exactly r in S_m, so a<=r.
Thus a=r.

Consequences:
- every nonexceptional odd trace orbit is absent or present at full multiplicity r;
- h(2)=+-1, so D^{-2}=2-Y is an algebraic unit;
- if u=p>=5 and the primitive p trace roots form one Frobenius orbit, then
    deg h=r(p-1)/2,
    deg M=r(p-1),
  leaving a Littlewood quotient of degree at most r-1.

Only the order-three trace T=1 needs a separate local analysis.
```
