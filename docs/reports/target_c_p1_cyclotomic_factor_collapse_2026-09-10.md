<!-- theorem-state: {"artifact_id":"ART-56D3B8B2E842","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — P1 cyclotomic factor collapse by Ramanujan sums

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-d2-transversality-2026-09-10`  
**Run type:** exact arithmetic reduction / cyclotomic-factor classification  
**Target:** cyclic primitive phase `d_H=1`, parallel endpoint P1  
**Depends on:** SC P1 Littlewood obstruction and PR P1 fixed-angle equation from PR #118  
**External literature:** only standard Ramanujan-sum identities; no irreducibility theorem imported  
**Computation:** none in the proof

## LEVEL I STATUS

`STILL OPEN`

The P1 endpoint has the exact angle equation, with

\[
m:=q-2,
\qquad z=e^{i\delta},
\]

\[
\cos(m\delta)+4\cos\delta-3=0.
\tag{CF.1}
\]

Equivalently `z` is a root of the reciprocal five-term polynomial

\[
\boxed{
F_m(z)
:=z^{2m}+4z^{m+1}-6z^m+4z^{m-1}+1.
}
\tag{CF.2}
\]

SC simultaneously requires `z` to be a root of a Littlewood polynomial of degree `m-1`.

The main theorem here completely removes the cyclotomic ambiguity from CF.2.

### Theorem CF — complete cyclotomic-factor classification

For every integer `m>=1`,

\[
\boxed{
\Phi_r(z)\mid F_m(z)
\iff
r=6\ \text{and}\ 6\mid m.
}
\tag{CF.3}

\]

Thus the complete cyclotomic part of `F_m` is

\[
\boxed{
\operatorname{cyc}(F_m)=
\begin{cases}
\Phi_6(z)=z^2-z+1,&6\mid m,\\
1,&6\nmid m.
\end{cases}
}
\tag{CF.4}

\]

The physical P1 root has `0<delta<pi/m`, hence for every sufficiently large Target C source it is not a primitive sixth root. Therefore its minimal polynomial is a **noncyclotomic reciprocal factor** of `F_m`.

Consequently P1 is reduced exactly to the following arithmetic endpoint:

> prove that every noncyclotomic reciprocal irreducible factor of `F_m` containing a unit-circle root in the physical P1 arc has degree at least `m` (indeed exact factor experiments suggest degree `2m`, or `2m-2` after removing `Phi_6`).

Any bound `>m-1` closes P1 because SC supplies a Littlewood annihilator of degree only `m-1`.

---

## 1. Derive the reciprocal five-term polynomial

PR/SC gives the P1 equation

\[
\cos(mx)=2\sin x,
\qquad x=\delta/2.
\tag{1.1}
\]

Squaring and using `cos(2mx)=2cos^2(mx)-1` gives

\[
\cos(m\delta)
=3-4\cos\delta,
\]

which is CF.1. Multiplying

\[
z^m+z^{-m}+4(z+z^{-1})-6=0
\tag{1.2}
\]

by `z^m` gives CF.2.

Two useful exact rewrites are

\[
\boxed{
F_m(z)=(z^m+1)^2+4z^{m-1}(z-1)^2,
}
\tag{1.3}
\]

and

\[
\boxed{
F_m(z)=(z^m-1)^2+4z^{m-1}(z^2-z+1).
}
\tag{1.4}
\]

The second identity already shows the `Phi_6` factor when `6|m`, but it does not exclude other cyclotomic factors. The exclusion is the content of Sections 2-3.

---

## 2. Galois trace over one cyclotomic orbit

Assume

\[
\Phi_r\mid F_m.
\tag{2.1}
\]

Let `xi` run through all primitive `r`th roots of unity. Because `Phi_r` is irreducible over `Q`, every such `xi` is a root of `F_m`. Dividing `F_m(xi)=0` by `xi^m` gives

\[
\xi^m+\xi^{-m}+4\xi+4\xi^{-1}-6=0.
\tag{2.2}
\]

Sum (2.2) over the complete primitive `r`th-root orbit.

Write

\[
c_r(k):=\sum_{\substack{1\le a\le r\\(a,r)=1}}
 e^{2\pi iak/r}
\]

for the Ramanujan sum. Then

\[
c_r(-m)=c_r(m),
\qquad
c_r(1)=\mu(r),
\]

and the number of primitive roots is `phi(r)`. Hence (2.2) gives the exact integer identity

\[
2c_r(m)+8\mu(r)-6\phi(r)=0,
\]

or

\[
\boxed{
c_r(m)+4\mu(r)=3\phi(r).
}
\tag{2.3}

\]

This trace identity is much stronger than testing individual roots.

---

## 3. The totient squeeze leaves only `r=6`

A Ramanujan sum is the sum of `phi(r)` complex numbers of modulus one, so

\[
|c_r(m)|\le\phi(r).
\tag{3.1}
\]

Also

\[
|\mu(r)|\le1.
\tag{3.2}
\]

Taking the upper bound in (2.3),

\[
3\phi(r)
=c_r(m)+4\mu(r)
\le\phi(r)+4.
\]

Therefore

\[
\boxed{\phi(r)\le2.}
\tag{3.3}
\]

The only positive integers with Euler totient at most two are

\[
r\in\{1,2,3,4,6\}.
\tag{3.4}
\]

We now check these five possibilities in the exact trace identity.

- `r=1`: `c_1(m)=1`, `mu(1)=1`, so the left side of (2.3) is `5`, not `3`.
- `r=2`: `mu(2)=-1`, `phi(2)=1`, and `c_2(m)=(-1)^m`; the left side is `-3` or `-5`, never `3`.
- `r=3`: `mu(3)=-1`, `phi(3)=2`, and `c_3(m)<=2`; the left side is at most `-2`, never `6`.
- `r=4`: `mu(4)=0`, `phi(4)=2`, and `|c_4(m)|<=2`; it cannot equal `6`.
- `r=6`: `mu(6)=1`, `phi(6)=2`, so (2.3) requires
  \[
  c_6(m)=2.
  \tag{3.5}
  \]

The sum `c_6(m)` is the sum of two unit complex numbers. Equality to `2` forces both summands to equal `1`, equivalently every primitive sixth root satisfies `xi^m=1`. Thus

\[
\boxed{6\mid m.}
\tag{3.6}
\]

Conversely, if `6|m`, then for a primitive sixth root `xi`,

\[
\xi^m=1,
\qquad
\xi+\xi^{-1}=1,
\]

and (2.2) reads

\[
2+4-6=0.
\]

Hence every primitive sixth root is a root of `F_m`, so `Phi_6|F_m`.

This proves CF.3-CF.4. `square`

---

## 4. Trace-variable formulation

Put

\[
y=z+z^{-1}.
\]

Let `C_m(y)` be the monic trace Chebyshev polynomial defined by

\[
C_0=2,
\qquad C_1=y,
\qquad C_{m+1}=yC_m-C_{m-1},
\]

so that

\[
C_m(z+z^{-1})=z^m+z^{-m}.
\]

Then

\[
\boxed{
z^{-m}F_m(z)=H_m(y),
\qquad
H_m(y):=C_m(y)+4y-6.
}
\tag{4.1}

\]

The cyclotomic factor `Phi_6(z)=z(z+z^{-1}-1)` corresponds exactly to the linear trace factor

\[
\boxed{y-1.}
\tag{4.2}
\]

Thus CF is equivalently

\[
\boxed{
H_m(y)\text{ has a trace-cyclotomic factor iff }6\mid m,
\text{ in which case it is exactly }y-1.
}
\tag{4.3}

\]

No other root-of-unity trace can occur.

---

## 5. Consequence for the SC Littlewood obstruction

SC proves that a P1 survivor requires a Littlewood polynomial

\[
P(z)=\sum_{k=0}^{m-1}\varepsilon_kz^k,
\qquad
\varepsilon_k\in\{+1,-1\},
\tag{5.1}
\]

with

\[
P(e^{i\delta})=0.
\tag{5.2}
\]

Let

\[
z_0=e^{i\delta}
\]

be the physical P1 root and let `R_m` be its minimal polynomial over `Q`. Since `F_m` is monic with constant term one, `z_0` is an algebraic unit and

\[
R_m\mid F_m.
\tag{5.3}
\]

Since `P(z_0)=0`,

\[
R_m\mid P,
\]

so

\[
\boxed{\deg R_m\le m-1.}
\tag{5.4}
\]

Because `z_0` lies on the unit circle and `R_m` has real rational coefficients, `z_0^{-1}=\overline{z_0}` is another root. Irreducibility then makes `R_m` reciprocal.

For a P1 source,

\[
m\delta+\Delta_2=\pi,
\qquad
\Delta_2>0,
\]

so

\[
0<\delta<\pi/m.
\tag{5.5}
\]

In the large Target C regime `m>=4`, this excludes `delta=pi/3`. By CF, `z_0` is therefore noncyclotomic.

Hence every P1 survivor forces:

\[
\boxed{
\begin{array}{l}
R_m\text{ noncyclotomic and reciprocal},\\
R_m\mid F_m,\\
\deg R_m\le m-1,\\
R_m\text{ has the physical unit-circle root }e^{i\delta}.
\end{array}}
\tag{CF.5}
\]

This is the exact remaining arithmetic obstruction.

---

## 6. Two modular identities for the remaining factor problem

Although they do not yet prove irreducibility, the same five-term polynomial has unusually rigid reductions:

\[
\boxed{
F_m(z)\equiv z^{2m}+1=(z^m+1)^2\pmod2,
}
\tag{6.1}
\]

and

\[
\boxed{
F_m(z)
\equiv
z^{2m}+z^{m+1}+z^{m-1}+1
=(z^{m-1}+1)(z^{m+1}+1)
\pmod3.
}
\tag{6.2}
\]

SC's Littlewood polynomial satisfies

\[
P(z)\equiv1+z+\cdots+z^{m-1}\pmod2.
\tag{6.3}
\]

Thus any hypothetical low-degree common factor `R_m` is simultaneously constrained by the square `z^m+1` modulo two, the adjacent binomials `z^{m-1}+1,z^{m+1}+1` modulo three, and the geometric unit-circle condition CF.5.

This is the next exact arithmetic target.

---

## 7. Regression audit

- The proof classifies **cyclotomic factors of `F_m`**, not all rational factors.
- A noncyclotomic reciprocal polynomial can have unit-circle roots; no false `|z|=1 => cyclotomic` implication is used.
- The P1 equation was squared in deriving CF.1 from SC. The physical P1 root satisfies the original positive-sign equation, so every physical root is still a root of `F_m`; the extra squared branch only enlarges `F_m` and cannot invalidate the necessary-condition argument.
- `Phi_6` is a genuine algebraic factor when `6|m`, but its roots have `delta=pi/3` and are outside the large-P1 physical arc `0<delta<pi/m`.
- No computational factorization is used in Theorem CF.

---

## 8. Next theorem

The shortest P1 closing statement is now:

> **P1-NC:** every noncyclotomic reciprocal irreducible factor of `F_m` that meets the unit circle in the physical arc `0<arg z<pi/m` has degree at least `m`.

P1-NC would contradict SC's degree bound `deg R_m<=m-1` and eliminate the entire P1 endpoint.

Exact factorizations for moderate `m` strongly suggest the stronger global statement

\[
F_m\text{ is irreducible if }6\nmid m,
\]

and

\[
F_m/\Phi_6\text{ is irreducible if }6\mid m,
\]

but this report deliberately does not promote that computational pattern to a theorem.

The most promising proof inputs are the reciprocal structure (4.1), the exact cyclotomic classification CF, and the simultaneous mod-2/mod-3 constraints (6.1)-(6.3).

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P1: m=q-2, z=e^{i delta}.  Fixed-angle geometry implies
    F_m(z)=z^(2m)+4z^(m+1)-6z^m+4z^(m-1)+1=0.
Also
    F_m=(z^m-1)^2+4z^(m-1)Phi_6(z).

New exact theorem: Phi_r divides F_m iff r=6 and 6|m.
Proof: if Phi_r|F_m, sum
    xi^m+xi^-m+4(xi+xi^-1)-6=0
across primitive rth roots.  Ramanujan sums give
    c_r(m)+4 mu(r)=3 phi(r).
Since |c_r(m)|<=phi(r), |mu(r)|<=1,
    3phi(r)<=phi(r)+4,
so phi(r)<=2 and r in {1,2,3,4,6}.  Directly only r=6 survives,
and then c_6(m)=2 forces 6|m.  Converse is immediate.

SC requires a Littlewood annihilator of degree m-1.  Therefore the physical P1
root would have a noncyclotomic reciprocal minimal polynomial R dividing F_m with
    deg R <= m-1.
This is now the only arithmetic escape.

Useful reductions:
    F_m mod 2 = (z^m+1)^2,
    F_m mod 3 = (z^(m-1)+1)(z^(m+1)+1).
Next: prove every noncyclotomic reciprocal factor meeting 0<arg z<pi/m has degree >=m.
```
