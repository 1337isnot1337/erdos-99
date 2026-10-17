> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_complete_ramification_exclusion_2026-09-10.md) · source SHA-256 `9c4bedb4ba829091f9f3a40cdec76194d0c29235c4b2c565c18799f1fdb3a9f7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-ED21F6CF119E","canonical":true,"claim_ids":["C-P1-PRX"],"claim_statuses":{"C-P1-PRX":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — complete cyclic P1 exclusion by reciprocal 2-adic ramification

**Date:** 2026-09-10  
**Run type:** exact global arithmetic closure of the P1 endpoint  
**Target:** primitive cyclic `d_H=1,s_Z=1`, parallel-side endpoint P1  
**Depends on:** P1 signed Littlewood closure and reciprocal geometric equation from PR #150/#118; RL zero-residue exclusion; O3 order-three exclusion; FRM local nonexceptional Newton segment  
**External literature:** standard local-field ramification and Newton-polygon facts only  
**Computation:** none

## 1. Result

The cyclic `d_H=1` P1 endpoint is impossible for every sufficiently large source.

### Theorem PRX — complete P1 exclusion

Let

$$
m:=q-2,
\qquad
z=e^{i\delta}
$$

be the P1 arithmetic parameter. The P1 geometry and signed shell closure imply simultaneously:

1. a Littlewood annihilator
   $$
   P(Z)=\sum_{j=0}^{m-1}\varepsilon_jZ^j,
   \qquad \varepsilon_j\in\{\pm1\},
   \qquad P(z)=0;
   \tag{PRX.1}
   $$
2. the reciprocal geometric equation
   $$
   \boxed{
   F_m(z)=0,
   \qquad
   F_m(Z)=(Z^m+1)^2+4Z^{m-1}(Z-1)^2.
   }
   \tag{PRX.2}
   $$

No algebraic number `z` can satisfy both conditions in the P1 parameter range. Therefore

$$
\boxed{\text{P1 does not occur}.}
\tag{PRX.3}

This closes the entire parallel-side subbranch of the primitive cyclic `d_H=1` phase. The only cyclic `d_H=1` endpoint left is S1.

The proof splits according to the parity of `m`.

---

## 2. Minimal polynomial and mod-two Littlewood reduction

Multiply `P` by `-1` if necessary so that it is monic. Let

\[
M(Z)\in\mathbb Z[Z]
$$

be the monic irreducible minimal polynomial of `z` over `Q`. Since `P` is primitive and `M|P` over `Q[Z]`, Gauss's lemma gives

$$
\boxed{M\mid P\quad\text{in }\mathbb Z[Z].}
\tag{2.1}

Modulo two every Littlewood coefficient becomes one, so

\[
\boxed{
P(Z)\equiv S_m(Z):=1+Z+\cdots+Z^{m-1}\pmod2.
}
\tag{2.2}

Hence

\[
\boxed{\overline M\mid S_m\quad\text{in }\mathbb F_2[Z].}
\tag{2.3}

Write

\[
m=ru,
\qquad
r=2^k,
\qquad
u=u\text{ odd}.
$$

In characteristic two,

$$
Z^m-1=(Z^u-1)^r.
$$

Therefore:

- `Z=1` occurs in `S_m` with multiplicity exactly `r-1`;
- every nontrivial `u`-th root of unity occurs in `S_m` with multiplicity exactly `r`.

These exact multiplicities are the arithmetic capacity against which the ramification forced by PRX.2 will be compared.

---

## 3. Odd `m`: the root field contains `i`

Assume first that

$$
m\text{ is odd}.
$$

Equation PRX.2 gives

$$
(z^m+1)^2=-4z^{m-1}(z-1)^2.
\tag{3.1}
$$

The P1 root satisfies `z ne0,1`. Because `m-1` is even, the element

$$
\boxed{
\iota:=
\frac{z^m+1}
{2z^{(m-1)/2}(z-1)}
\in\mathbb Q(z)
}
\tag{3.2}
$$

satisfies

$$
\boxed{\iota^2=-1.}
\tag{3.3}
$$

Thus

$$
\boxed{\mathbb Q(i)\subseteq\mathbb Q(z).}
\tag{3.4}
$$

### 3.1 The Littlewood reduction says two is unramified

When `m` is odd, the polynomial

$$
Z^m-1
$$

is squarefree over `F_2`, because its derivative is

$$
mZ^{m-1}=Z^{m-1}.
$$

The factor `Z-1` occurs exactly once, so

$$
\boxed{S_m\text{ is squarefree over }\mathbb F_2.}
\tag{3.5}

By (2.3), `overline M` is a factor of this squarefree polynomial and is itself squarefree. Hence

\[
\operatorname{disc}(M)\not\equiv0\pmod2.
\tag{3.6}
$$

Let

$$
K:=\mathbb Q(z).
$$

Since `z` is an algebraic integer and `M` is its monic minimal polynomial,

$$
\operatorname{disc}(M)
=\operatorname{disc}(K)
[\mathcal O_K:\mathbb Z[z]]^2.
$$

Equation (3.6) implies

$$
\boxed{2\nmid\operatorname{disc}(K),}
\tag{3.7}
$$

so every prime of `K` above two is unramified over `Q_2`.

### 3.2 But containing `Q(i)` forces ramification at two

The prime two is ramified in

$$
\mathbb Q(i)/\mathbb Q:
\qquad
(2)=(1+i)^2\cdot(-i).
$$

For any prime `mathfrak P` of `K` above the unique prime `mathfrak p=(1+i)` of `Q(i)` above two, ramification indices multiply in the tower

$$
K/\mathbb Q(i)/\mathbb Q:
$$

$$
e(\mathfrak P/2)
=e(\mathfrak P/\mathfrak p)e(\mathfrak p/2),
$$

and

$$
e(\mathfrak p/2)=2.
$$

Thus

$$
e(\mathfrak P/2)\ge2,
$$

contradicting (3.7).

Therefore:

### Corollary PRX.1

$$
\boxed{m\text{ odd}\Longrightarrow\text{P1 impossible}.}
\tag{3.8}

This includes every odd part with `k=0`; no factorization theorem for `G_m` is required.

---

## 4. Even `m`: the root field contains a square root of `-z`

Now assume

\[
m=ru\text{ is even}.
$$

Because `u` is odd, this means

$$
r=2^k\ge2.
$$

Since `m-2` is even, PRX.2 gives the element

$$
\boxed{
s:=
\frac{z^m+1}
{2z^{(m-2)/2}(z-1)}
\in\mathbb Q(z)
}
\tag{4.1}
$$

with

$$
\boxed{s^2=-z.}
\tag{4.2}

This square root supplies one extra factor of two in the local ramification beyond the `r` already forced by the P1 trace geometry.

---

## 5. Choose a local residue root of the minimal polynomial

Let

\[
K=\mathbb Q(z).
$$

Choose any irreducible factor of `M` over `Q_2` and one corresponding local root, still denoted `z`, in a finite extension

$$
L/\mathbb Q_2.
$$

Its residue

$$
\bar z=\omega
$$

is a root of `overline M`, hence by (2.3) a root of `S_m`.

RL proves that the physical trace factor has no zero trace residue. In reciprocal language this means no root of `overline M` is

$$
\omega=1,
$$

because in characteristic two

$$
1+1^{-1}=0.
$$

O3 proves that no root of `overline M` is a primitive third root, because those and only those nontrivial roots have trace residue

$$
\omega+\omega^{-1}=1.
$$

Thus every residue root of `overline M` has

$$
\boxed{
\omega^u=1,
\qquad
\omega\ne1,
\qquad
\omega\text{ not of order }3.
}
\tag{5.1}

In particular its trace residue

\[
\bar t=\omega+\omega^{-1}
$$

satisfies

$$
\boxed{\bar t\ne0,1.}
\tag{5.2}

If there is no residue root satisfying (5.1), then `overline M` has no root at all, impossible for a nonconstant polynomial; so in that case P1 is already excluded by RL+O3. We may therefore assume such `omega` exists.

---

## 6. The trace Newton segment gives exact depth `1/r`

Let

\[
\widehat\omega
$$

be the Teichmuller lift of `omega` in `L`, and put

$$
t_0:=\widehat\omega+\widehat\omega^{-1}.
$$

FRM proves for every nonexceptional trace residue that the local expansion of the trace polynomial has Newton segment

$$
(0,2)\longrightarrow(2r,0)
$$

of slope

$$
-\frac1r.
$$

Therefore the local trace

$$
t:=z+z^{-1}
$$

satisfies

$$
\boxed{
v_2(t-t_0)=\frac1r.}
\tag{6.1}

Normalize the valuation by

\[
v_2(2)=1.
$$

Write

$$
z=\widehat\omega(1+x),
\qquad v_2(x)>0.
$$

Then

$$
\begin{aligned}
t-t_0
&=\widehat\omega x
+\widehat\omega^{-1}\big((1+x)^{-1}-1\big)\\
&=(\widehat\omega-\widehat\omega^{-1})x+O(x^2).
\end{aligned}
\tag{6.2}

The coefficient is a unit because its residue is

\[
\omega-\omega^{-1}
=\omega+\omega^{-1}
=\bar t\ne0
$$

in characteristic two. Hence

$$
\boxed{
v_2(x)=v_2(t-t_0)=\frac1r.}
\tag{6.3}

This is the exact local radial depth of the P1 root above its odd-order Teichmuller residue.

---

## 7. The square root `s^2=-z` halves the valuation again

Equation (4.2) holds inside the same local field `L`.

The residue field of `L` is finite and therefore perfect. Let

\[
\bar\eta^2=\omega
$$

be the unique residue square root of `omega`, and let

$$
\eta
$$

be its Teichmuller lift. Then

$$
\eta^2=\widehat\omega.
\tag{7.1}

Since

\[
s^2=-z=-\widehat\omega(1+x),
$$

the unit

$$
u:=s/\eta
$$

satisfies

$$
\boxed{u^2=-(1+x).}
\tag{7.2}

Modulo the maximal ideal, `-1=1` and `u^2=1`. In characteristic two the equation `X^2=1` has the unique solution `1`, so

\[
u\equiv1.
$$

Write

$$
u=1+y,
\qquad v_2(y)>0.
$$

Equation (7.2) becomes

$$
(1+y)^2=-1-x,
$$

or

$$
\boxed{y^2+2y+2+x=0.}
\tag{7.3}

Now

\[
v_2(x)=\frac1r<1
$$

because `r>=2`. Put

$$
a=v_2(y)>0.
$$

The four terms in (7.3) have valuations

$$
2a,
\qquad
1+a,
\qquad
1,
\qquad
\frac1r.
$$

The last two terms `2y` and `2` have valuation strictly larger than `1/r`. In a nonarchimedean field the minimum valuation in a vanishing sum must occur at least twice. Therefore `y^2` must tie `x` for the minimum:

$$
2a=\frac1r.
$$

Hence

$$
\boxed{
v_2(y)=\frac1{2r}.}
\tag{7.4}

If `e=e(L/Q_2)` is the ramification index, the normalized value group is

\[
\frac1e\mathbb Z.
$$

Since it contains `1/(2r)` in lowest terms,

$$
\boxed{2r\mid e.}
\tag{7.5}

Thus every local factor of `M` above such a residue root has ramification index at least `2r`.

---

## 8. Ramification exceeds the Littlewood multiplicity budget

Let

\[
\mu(Z)\in\mathbb Z_2[Z]
$$

be the monic irreducible local factor of `M` containing the chosen root `z`. Its reduction has the form

$$
\overline\mu=g(Z)^a
$$

for one irreducible `g in F_2[Z]` having `omega` as a root.

Let `f_L` be the residue degree of the local field `L=Q_2(z)` and let

$$
f_0:=\deg g=[\mathbb F_2(\omega):\mathbb F_2].
$$

Then

$$
f_0\mid f_L
$$

and

$$
\deg\mu=e f_L=a f_0.
$$

Therefore

$$
\boxed{
a=e\frac{f_L}{f_0}\ge e\ge2r.}
\tag{8.1}

So `overline M` contains the residue root `omega` with multiplicity at least `2r`.

But `overline M|S_m` by (2.3), while every nontrivial `u`-th root has multiplicity exactly `r` in `S_m`. Therefore

\[
\boxed{a\le r.}
\tag{8.2}

Equations (8.1) and (8.2) contradict each other.

Thus:

### Corollary PRX.2

\[
\boxed{m\text{ even}\Longrightarrow\text{P1 impossible}.}
\tag{8.3}

Together with Corollary PRX.1 this proves Theorem PRX. `square`

---

## 9. Why the argument is genuinely stronger than the earlier family exclusions

PR #150 proved P1 impossible for

\[
m=2^k
$$

and

$$
m=3\cdot2^k
$$

by detailed trace-factor Newton polygons.

RL, FRM, and O3 then classified the possible mod-two support of an arbitrary physical trace factor.

PRX adds the missing global coupling: the reciprocal geometric equation itself forces an extra ramified square root inside the **same root field**.

- for odd `m`, that square root is `i`;
- for even `m`, it is `sqrt(-z)` and doubles the already forced local denominator from `r` to `2r`.

The Littlewood reduction has only multiplicity `r` available. Hence no odd part survives.

This is not a full irreducibility theorem for `G_m`; it is stronger for the Target C application because it excludes a common root of the geometric polynomial and **any** degree-`m-1` Littlewood closure directly.

---

## 10. Independence from the invalid path inference

PR #151 correctly identifies a gap in a recent `d_H=2` argument:

```text
consecutive diameter states share an endpoint
    does not imply
ordered states form an Euler trail/path.
```

PRX does not use that inference, any `d_H=2` circle-center theorem, or any component-path claim.

It uses only the independently established P1 arithmetic equations and the audited 2-adic residue localization on this branch.

---

## 11. Regression audit

### Squaring the geometric equation

PRX.2 is a necessary equation obtained from the exact P1 angle equation. Squaring may introduce extra roots, but that cannot invalidate an exclusion: every actual P1 root still satisfies PRX.2.

### Denominators in the constructed square roots

The expressions in (3.2) and (4.1) lie in the number field `Q(z)` because `2`, `z`, and `z-1` are nonzero. They need not be algebraic integers. Integrality is not used.

### Odd-case discriminant argument

The implication `overline M squarefree => 2 unramified in Q(z)` is safe because the polynomial discriminant is odd, and the field discriminant divides it up to the square of the index.

### Even-case Teichmuller lift

A finite extension of `Q_2` contains the Teichmuller lifts of its residue-field units of odd order. Since the residue field is perfect, the square root of `omega` already lies in the same residue field, so `eta` is available inside `L`.

### Trace derivative

The passage from (6.1) to (6.3) requires the trace derivative to be a unit. This is why RL/O3 are invoked: `bar t ne0,1`, and in particular `omega ne1`. The coefficient `widehat omega-widehat omega^{-1}` reduces to the nonzero trace `bar t` in characteristic two.

### Local reduction exponent

For an irreducible local factor `mu`, its reduction is a power of one irreducible residue polynomial. The exponent is `deg(mu)/deg(g)=e f_L/f_0`, so it is at least the ramification index even if the residue of `z` does not generate the full residue field. Thus (8.1) does not assume monogenic residue generation.

---

## 12. Cyclic phase consequence

The primitive cyclic ledger has

$$
d_H+s_Z=2.
$$

The `d_H=1,s_Z=1` phase had two difference-body endpoints:

- S1: one genuine short antipodal pair and no parallel shell sides;
- P1: one parallel-side defect / doubled Minkowski edge.

PRX removes the second:

\[
\boxed{
\text{cyclic }d_H=1\Longrightarrow\text{S1 only}.
}
\tag{12.1}

The overall Level I problem remains open because S1, the exact `d_H=0` Reinhardt family, and the correctly audited `d_H=2` frontier remain to be resolved.

---

## 13. Promotion recommendation

**Hold as report-level theorem pending independent audit.**

If PRX survives audit, it should supersede the family-by-family P1 arithmetic frontier and be promoted as the complete P1 closure theorem. No canonical route-map file is changed in this commit.

---

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P1 gives both:
  P(z)=0 for a length-m Littlewood polynomial, so Mbar | S_m mod2;
  (z^m+1)^2=-4 z^(m-1)(z-1)^2.

Odd m:
  [(z^m+1)/(2 z^((m-1)/2)(z-1))]^2=-1,
so Q(z) contains i. But S_m is squarefree mod2, hence Mbar squarefree,
Disc(M) odd, and 2 is unramified in Q(z). A field containing Q(i) is ramified at 2.
Contradiction.

Even m=ru, r=2^k>=2:
RL+O3 force every residue root omega of Mbar to have nonexceptional trace.
FRM's local Newton segment gives, with z=omega_hat(1+x),
  v2(x)=1/r.
The reciprocal equation gives s in Q(z) with s^2=-z.
Divide by the Teichmuller square root eta of omega_hat and write s/eta=1+y:
  y^2+2y+2+x=0.
Since v2(x)=1/r<1, nonarchimedean cancellation forces
  v2(y)=1/(2r).
Thus every local factor has ramification index divisible by 2r and therefore
contributes residue multiplicity at least 2r to Mbar.
But Mbar|S_m, where every nontrivial u-th root has multiplicity exactly r.
Contradiction.

Hence P1 is impossible for every m=q-2.
Only S1 remains in cyclic d_H=1.
```
