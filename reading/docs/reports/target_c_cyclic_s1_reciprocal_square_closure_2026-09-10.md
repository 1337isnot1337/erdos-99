> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_s1_reciprocal_square_closure_2026-09-10.md) · source SHA-256 `6db0d84cd89736b2a136d51a683795e3b849fa2e8bde777ec9f6c38a21321c93`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 22 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-0109063AA653","canonical":true,"claim_ids":["C-S1-RSQ"],"claim_statuses":{"C-S1-RSQ":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — cyclic S1 reduces to an exact reciprocal-square Littlewood equation

**Date:** 2026-09-10  
**Run type:** exact algebraic reduction  
**Target:** primitive cyclic `d_H=1,s_Z=1`, S1 endpoint  
**Depends on:** D1 one-defect difference-body normal form; AC canonical short antipodal completion; SC signed shell closure on PR #118  
**External literature:** none  
**Computation:** none in the proof

## 1. Result

The S1 shell-closure equations can be compressed to one exact reciprocal-square identity.

Use

```math
q=m+2,
\qquad
x:=\frac\delta2,
\qquad
z:=e^{2ix}=e^{i\delta},
```

where

```math
\delta=2\arcsin\frac1{2D}.
```

Normalize the two signs adjacent to the unique short antipodal state by

```math
\varepsilon_0=1,
\qquad
\varepsilon_1=-1,
```

and define the remaining length-`m` Littlewood polynomial

```math
\boxed{
Q(Z):=\sum_{k=0}^{m-1}a_kZ^k,
\qquad
 a_k:=\varepsilon_{k+2}\in\{\pm1\}.
}
\tag{RSQ.1}
```

Let `tau` be the angle between the two unit difference-body edges adjacent to the unique short vertex, as in SC. Then S1 closure is equivalent to

```math
\boxed{
z^{-(m-1)/2}Q(z)=2\sin\frac\tau2>0.
}
\tag{RSQ.2}
```

Here the half-power is only shorthand for the actual unit complex phase `e^{-i(m-1)x}`; no algebraic choice of a square root of `z` is needed.

Consequently:

### Theorem RSQ — reciprocal-square closure

Every S1 survivor satisfies both

```math
\boxed{
Q(z)=Q^*(z),
\qquad
Q^*(Z):=Z^{m-1}Q(Z^{-1}),
}
\tag{RSQ.3}
```

and

```math
\boxed{
F_m(z)=(z-1)^2Q(z)^2,
}
\tag{RSQ.4}
```

where

```math
\boxed{
F_m(Z):=(Z^m+1)^2+4Z^{m-1}(Z-1)^2.
}
\tag{RSQ.5}
```

The polynomial `F_m` is exactly the reciprocal geometric polynomial that appears at the P1 endpoint. The difference is decisive:

- P1 requires `F_m(z)=0` and `Q(z)=0`;
- genuine S1 requires the nonzero square identity RSQ.4 together with the phase condition RSQ.3.

Thus the entire S1 endpoint is reduced to the following finite algebraic problem:

> Find or exclude a Littlewood polynomial `Q` of length `m` and a unit-circle point `z=e^{i delta}` in the strict S1 interval such that `Q(z)=Q^*(z)` and `F_m(z)=(z-1)^2Q(z)^2`.

This reduction uses no path/Euler-trail inference and is independent of the d_H=2 issue audited in PR #151.

---

## 2. Reindex the exact signed shell closure

SC on PR #118 gives the S1 half-boundary edge directions

```math
\theta_0=-\frac\tau2,
\qquad
\theta_1=\frac\tau2,
```

and, for `2<=j<=q-1`,

```math
\theta_j
=\frac\pi2+(2j-q-1)x.
\tag{2.1}
```

The two defect-edge signs are opposite. After global sign reversal if necessary,

```math
\varepsilon_0=1,
\qquad
\varepsilon_1=-1.
```

Their contribution to primal closure is

```math
e^{-i\tau/2}-e^{i\tau/2}
=-2i\sin\frac\tau2.
\tag{2.2}
```

For the remaining terms write

```math
j=k+2,
\qquad
0\le k\le m-1,
\qquad
q=m+2.
```

Then

```math
2j-q-1
=2k-(m-1),
```

so

```math
\begin{aligned}
e^{i\theta_{k+2}}
&=i e^{i(2k-(m-1))x}\\
&=i e^{-i(m-1)x}z^k.
\end{aligned}
\tag{2.3}
```

Therefore the sum of all nondefect primal side vectors is

```math
\boxed{
i e^{-i(m-1)x}Q(z).
}
\tag{2.4}
```

Adding (2.2) and imposing polygon closure gives

```math
-2i\sin\frac\tau2
+i e^{-i(m-1)x}Q(z)=0.
```

Divide by `i`:

```math
\boxed{
e^{-i(m-1)x}Q(z)=2\sin\frac\tau2.
}
\tag{2.5}
```

Since `z=e^{2ix}`, equation (2.5) is RSQ.2.

The right side is strictly positive in genuine S1 because D1 gives

```math
2\delta<G<\Delta_2,
```

so the short difference-body vertex is strict and `0<tau<pi`.

---

## 3. The phase equation is reciprocal equality

Equation RSQ.2 says the centered value

```math
e^{-i(m-1)x}Q(z)
```

is real. Taking complex conjugates and using `|z|=1` gives

```math
e^{-i(m-1)x}Q(z)
=e^{i(m-1)x}Q(z^{-1}).
```

Multiply by `e^{i(m-1)x}`:

```math
Q(z)
=z^{m-1}Q(z^{-1}).
```

Thus

```math
\boxed{Q(z)=Q^*(z).}
```

This proves RSQ.3.

Equivalently,

```math
\boxed{(Q-Q^*)(z)=0.}
\tag{3.1}
```

If `Q` is not palindromic, `Q-Q^*` is a nonzero anti-reciprocal integer polynomial of degree at most `m-1`. Since every anti-reciprocal polynomial vanishes at `Z=1`,

```math
\boxed{
B_Q(Z):=\frac{Q(Z)-Q^*(Z)}{2(Z-1)}\in\mathbb Z[Z]
}
\tag{3.2}
```

is well defined and nonzero, and

```math
\boxed{B_Q(z)=0.}
\tag{3.3}
```

The factor two divides every coefficient because the coefficients of `Q-Q^*` belong to `{0,+-2}`.

Hence every **nonpalindromic** S1 candidate has an integral annihilator of degree at most

```math
\boxed{m-2.}
\tag{3.4}
```

This is a useful algebraic-degree restriction, but no contradiction is claimed from it alone.

---

## 4. Convert the S1 geometry to the same trace polynomial as P1

Let

```math
t:=z+z^{-1}=2\cos\delta=2\cos(2x).
```

Let `C_m(T)` be the trace-Chebyshev polynomial

```math
C_m(2\cos\theta)=2\cos(m\theta),
```

and define

```math
\boxed{
G_m(T):=C_m(T)+4T-6.
}
\tag{4.1}
```

The reciprocal lift is

```math
\boxed{
z^mG_m(z+z^{-1})=F_m(z),
}
\tag{4.2}
```

with `F_m` as in RSQ.5.

We now express the S1 amplitude in terms of `G_m`.

D1/SC give

```math
G=\pi-m\delta
=\pi-2mx,
\tag{4.3}
```

and

```math
\eta=\arcsin\left(D\sin\frac G2\right),
\qquad
\tau=\pi-2\eta.
\tag{4.4}
```

Therefore

```math
\sin\frac\tau2
=\cos\eta
=\sqrt{1-D^2\sin^2\frac G2}.
\tag{4.5}
```

But

```math
\sin\frac G2
=\sin\left(\frac\pi2-mx\right)
=\cos(mx),
```

and

```math
D=\frac1{2\sin x}.
```

Hence

```math
4\sin^2\frac\tau2
=4-\frac{\cos^2(mx)}{\sin^2x}.
\tag{4.6}
```

Now

```math
\cos^2(mx)
=\frac{2+C_m(t)}4,
\qquad
\sin^2x
=\frac{2-t}4.
```

Substituting into (4.6),

```math
\begin{aligned}
4\sin^2\frac\tau2
&=4-\frac{C_m(t)+2}{2-t}\\
&=\frac{6-4t-C_m(t)}{2-t}\\
&=-\frac{G_m(t)}{2-t}.
\end{aligned}
```

Thus

```math
\boxed{
(2-t)\,4\sin^2\frac\tau2=-G_m(t).
}
\tag{4.7}
```

This identity is valid throughout S1 and degenerates to the P1 equation `G_m(t)=0` exactly when `tau=0`.

---

## 5. Square the centered closure and obtain RSQ.4

From RSQ.2,

```math
Q(z)Q(z^{-1})
=4\sin^2\frac\tau2.
\tag{5.1}
```

By RSQ.3,

```math
Q(z^{-1})
=z^{-(m-1)}Q(z).
\tag{5.2}
```

Also

```math
2-t
=2-z-z^{-1}
=-\frac{(z-1)^2}{z}.
\tag{5.3}
```

Insert (5.1)-(5.3) into (4.7):

```math
-\frac{(z-1)^2}{z}
\,z^{-(m-1)}Q(z)^2
=-G_m(t).
```

Therefore

```math
G_m(t)
=z^{-m}(z-1)^2Q(z)^2.
```

Multiply by `z^m` and use (4.2):

```math
\boxed{
F_m(z)=(z-1)^2Q(z)^2.
}
```

This proves RSQ.4. `square`

---

## 6. Exact endpoint checks

### Zero-defect Reinhardt endpoint

At

```math
s=0,
```

one has

```math
q\delta=\pi,
\qquad
x=\frac\pi{2q},
```

and the off-circle S1 vertex reaches the radius-`D` circle. Equation RSQ.2 becomes the ordinary Reinhardt signed closure written in centered coordinates.

RSQ therefore deliberately allows the known `d_H=0` Reinhardt regressions at the zero-defect boundary. It does **not** claim that every signed word is excluded.

### P1 endpoint

At

```math
s=s_P(D),
```

D1 gives

```math
\tau=0.
```

Then RSQ.2 forces

```math
Q(z)=0,
```

and RSQ.4 reduces to

```math
F_m(z)=0,
```

exactly the P1 arithmetic system used by PRs #150/#152.

Thus RSQ continuously interpolates between the Reinhardt equality boundary and the P1 arithmetic boundary with no discontinuous change of notation.

---

## 7. A useful coefficientwise congruence

Write the Littlewood word as

```math
Q=S_m-2A,
\qquad
S_m=1+Z+\cdots+Z^{m-1},
```

where

```math
A\in\mathbb Z[Z]
```

has coefficients in `{0,1}`.

Then a direct expansion gives

```math
\boxed{
F_m(Z)-(Z-1)^2Q(Z)^2
=4\left[
Z^m+(Z-1)^2\left(Z^{m-1}+S_m(Z)A(Z)-A(Z)^2\right)
\right].
}
\tag{7.1}
```

Hence the polynomial whose root is required by the S1 amplitude equation is divisible coefficientwise by four.

This congruence is exact but is not yet a contradiction. It is recorded because it is the natural starting point for a 2-adic attack analogous to PRX.

---

## 8. Palindromic versus nonpalindromic split

RSQ.3 produces a sharp algebraic dichotomy.

### Branch NP — nonpalindromic word

If

```math
Q\ne Q^*,
```

then `z` is a root of the nonzero integer polynomial `B_Q` in (3.2), with

```math
\deg B_Q\le m-2.
```

Together with RSQ.4, a survivor is a common root of two explicit integer polynomials:

```math
B_Q(Z),
\qquad
F_m(Z)-(Z-1)^2Q(Z)^2.
```

A complete NP exclusion can therefore be obtained by proving that every such common factor is cyclotomic/Reinhardt-boundary or P1-boundary.

### Branch P — palindromic word

If

```math
Q=Q^*,
```

then RSQ.3 is automatic. RSQ.2 becomes one scalar cosine equation.

If `m` is even,

```math
\boxed{
2\sum_{k=0}^{m/2-1}
a_k\cos((m-1-2k)x)
=2\sin\frac\tau2.
}
\tag{8.1e}
```

If `m` is odd,

```math
\boxed{
a_{(m-1)/2}
+2\sum_{k=0}^{(m-3)/2}
a_k\cos((m-1-2k)x)
=2\sin\frac\tau2.
}
\tag{8.1o}
```

The right side lies strictly between zero and its zero-defect Reinhardt value throughout genuine S1.

The palindromic branch therefore becomes a one-variable signed cosine extremum problem rather than an algebraic phase problem.

No monotonicity claim for arbitrary signs is made here.

---

## 9. What RSQ changes

Before RSQ, S1 was represented by two trigonometric equations with a nonlinear defect angle `tau`.

After RSQ, the exact endpoint is:

```text
m=q-2,
z=e^{i delta},
Q a length-m Littlewood polynomial,
Q(z)=Q*(z),
F_m(z)=(z-1)^2 Q(z)^2,
0<tau<pi.
```

The nonlinear geometry has been absorbed into the fixed reciprocal polynomial `F_m`, the same one already understood 2-adically at the P1 endpoint.

This makes the next proof target precise and finite.

---

## 10. Regressions and rejected shortcuts

1. **No Euler-trail/path inference.** RSQ uses only D1/SC signed edge directions and polygon closure. The d_H=2 path gap audited in PR #151 is irrelevant.
2. **No claim that every unit-circle Littlewood zero is cyclotomic.** False in general and not used.
3. **No claim that `Q` must be palindromic.** RSQ.3 is an equality only at the particular root `z`; it does not imply polynomial identity.
4. **No ordinary Eisenstein shortcut.** The coefficientwise factor four in (7.1) is only a 2-adic handle, not an irreducibility theorem.
5. **Reinhardt boundary retained.** At `s=0`, genuine Reinhardt shells must survive this algebra.
6. **P1 boundary retained algebraically.** At `tau=0`, RSQ becomes the P1 system; its impossibility is a separate report-level result on PR #152.

---

## 11. Exact next lemma

The shortest S1 closing statement is now:

> For every sufficiently large `m`, every length-`m` Littlewood polynomial `Q`, and every S1 point `z=e^{i delta}` with
> 

```math
> 0<s=q_R-q<s_P(D),
> 
```
> the simultaneous equations
> 

```math
> Q(z)=Q^*(z),
> \qquad
> F_m(z)=(z-1)^2Q(z)^2
> 
```
> are impossible.

A promising proof split is:

- NP: classify common factors of `B_Q` and `F_m-(Z-1)^2Q^2`;
- P: prove a strict signed-cosine inequality on the very short S1 interval.

Closing S1 together with audited PRX would eliminate the entire cyclic `d_H=1` phase.

---

## 12. Promotion recommendation

**Hold as report-level theorem pending independent audit.**

RSQ is an exact algebraic repackaging of established D1/SC equations. It changes no canonical route-map file.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

S1: q=m+2, x=delta/2, z=e^(2ix). Put
  Q(Z)=sum_{k=0}^{m-1} eps_{k+2} Z^k.
SC edge directions give exact closure
  e^(-i(m-1)x) Q(z)=2 sin(tau/2)>0.
Therefore
  Q(z)=Q*(z), Q*(Z)=Z^(m-1)Q(Z^-1).

Let t=z+z^-1 and G_m(T)=C_m(T)+4T-6. S1 geometry gives
  4 sin^2(tau/2)=-G_m(t)/(2-t).
Using 2-t=-(z-1)^2/z and the reciprocal phase relation yields
  F_m(z)=(z-1)^2 Q(z)^2,
where
  F_m(Z)=Z^mG_m(Z+Z^-1)
        =(Z^m+1)^2+4Z^(m-1)(Z-1)^2.

Thus every S1 survivor solves the exact pair
  Q(z)=Q*(z),
  F_m(z)=(z-1)^2Q(z)^2.

If Q is nonpalindromic, z also annihilates
  B_Q=(Q-Q*)/[2(Z-1)], deg B_Q<=m-2.
If Q is palindromic, phase is automatic and closure is one signed cosine equation.

At s=0 this recovers Reinhardt equality; at tau=0 it recovers P1.
Next: exclude interior S1 solutions in the NP and P branches separately.
```
