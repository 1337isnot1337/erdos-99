> Generated reading edition · [exact source](../../../docs/reports/target_c_p1_power_two_eisenstein_exclusion_2026-09-10.md) · source SHA-256 `3de472d2403a37530e27f45201e9cac4097ca2c187339e94de6c6a07ef9f3eb1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-B7CB396F1460","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — P1 is impossible when `q-2` is a power of two

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-d2-transversality-2026-09-10`  
**Run type:** exact arithmetic phase exclusion  
**Target:** cyclic primitive phase `d_H=1`, parallel endpoint P1  
**Depends on:** SC P1 Littlewood obstruction from PR #118; CF cyclotomic-factor report on this branch  
**External literature:** none  
**Computation:** none in the proof

## LEVEL I STATUS

`STILL OPEN`

This report closes an infinite arithmetic subfamily of the P1 endpoint exactly.

### Theorem PE — power-of-two P1 exclusion

Let

```math
m:=q-2.
```

If

```math
\boxed{m=2^{r+1}\qquad(r\ge0),}
\tag{PE.1}
```

then no cyclic P1 source exists.

Equivalently, the P1 phase is impossible whenever

```math
\boxed{q=2^{r+1}+2.}
\tag{PE.2}
```

The proof uses the unsquared P1 angle equation and Eisenstein's criterion at `2`.

---

## 1. Convert the exact P1 equation to one polynomial in `u=1/D`

SC gives the exact P1 equation

```math
\cos(m x)=2\sin x,
\qquad
x=\delta/2.
\tag{1.1}
```

Put

```math
u:=2\sin x=\frac1D.
\tag{1.2}
```

Assume `m` is even and write

```math
m=2n.
```

Then

```math
\cos(mx)=\cos(2nx)=T_n(\cos 2x).
```

Since

```math
\cos 2x=1-2\sin^2x=1-\frac{u^2}{2},
```

(1.1) becomes

```math
T_n\!\left(1-\frac{u^2}{2}\right)=u.
\tag{1.3}
```

Let

```math
C_n(y):=2T_n(y/2).
\tag{1.4}
```

Then `C_n` is the monic integer trace-Chebyshev polynomial characterized by

```math
C_0(y)=2,
\qquad C_1(y)=y,
\qquad C_{k+1}(y)=yC_k(y)-C_{k-1}(y).
```

Equation (1.3) is exactly

```math
\boxed{
G_n(u):=C_n(2-u^2)-2u=0.
}
\tag{PE.3}
```

The degree of `G_n` is `2n=m` and its leading coefficient is `(-1)^n`.

---

## 2. Power-of-two trace Chebyshev is a monomial modulo two

The standard doubling identity is

```math
\boxed{C_{2k}(y)=C_k(y)^2-2.}
\tag{2.1}
```

It follows directly from

```math
z^k+z^{-k}=C_k(z+z^{-1})
```

by squaring.

Suppose now

```math
n=2^r.
```

Modulo two, (2.1) becomes

```math
C_{2k}(y)\equiv C_k(y)^2\pmod2.
```

Starting from `C_1(y)=y` and iterating gives

```math
\boxed{C_n(y)\equiv y^n\pmod2.}
\tag{2.2}
```

Substitute `y=2-u^2`. In characteristic two,

```math
2-u^2\equiv u^2,
```

so

```math
C_n(2-u^2)\equiv u^{2n}=u^m\pmod2.
```

The term `-2u` vanishes modulo two. Therefore

```math
\boxed{G_n(u)\equiv u^m\pmod2.}
\tag{2.3}
```

Thus every nonleading coefficient of `G_n` is divisible by two.

On the other hand

```math
G_n(0)=C_n(2)=2,
\tag{2.4}
```

because `T_n(1)=1`. Hence the constant term is divisible by two but not by four.

The leading coefficient `(-1)^n` is not divisible by two.

Eisenstein's criterion at the prime `2` now gives:

### Lemma PE.1

If `n` is a power of two, then

```math
\boxed{G_n(u)\text{ is irreducible over }\mathbb Q.}
\tag{PE.4}
```

Consequently the physical P1 value

```math
u=1/D
```

has algebraic degree

```math
\boxed{[\mathbb Q(u):\mathbb Q]=m.}
\tag{PE.5}
```

---

## 3. Squaring does not lower the degree

SC constrains the phase variable

```math
z=e^{i\delta},
```

not directly `u`. We therefore need the degree of `u^2`.

The polynomial `G_n` is the sum of an even polynomial and the term `-2u`:

```math
G_n(u)=C_n(2-u^2)-2u.
```

Hence

```math
G_n(-u)-G_n(u)=4u.
\tag{3.1}
```

No root of `G_n` is zero because `G_n(0)=2`. Therefore `G_n` has no pair of roots `alpha,-alpha`.

Since `G_n` is irreducible of degree `m`, the `m` Galois conjugates

```math
\alpha_1,\ldots,\alpha_m
```

of the physical root `u` are distinct. Their squares are also distinct: equality

```math
\alpha_i^2=\alpha_j^2
```

would imply `alpha_i=alpha_j` or `alpha_i=-alpha_j`, and the latter is impossible by (3.1).

Therefore `u^2` has at least `m` distinct conjugates. Since it lies in `Q(u)`, it has degree at most `m`. Thus

```math
\boxed{[\mathbb Q(u^2):\mathbb Q]=m.}
\tag{PE.6}
```

This step is necessary: irreducibility of a polynomial in `u` alone would not automatically give the same degree for `u^2`.

---

## 4. Transfer the degree obstruction to `z=e^{i delta}`

By definition

```math
u=2\sin(\delta/2).
```

Hence

```math
u^2=4\sin^2(\delta/2)=2-2\cos\delta
=2-(z+z^{-1}).
\tag{4.1}
```

Therefore

```math
\boxed{u^2\in\mathbb Q(z).}
\tag{4.2}
```

PE.6 implies

```math
[\mathbb Q(z):\mathbb Q]
\ge
[\mathbb Q(u^2):\mathbb Q]
=m.
\tag{4.3}
```

But SC proves that every P1 survivor requires a Littlewood polynomial

```math
P(z)=\sum_{k=0}^{m-1}\varepsilon_kz^k,
\qquad\varepsilon_k\in\{+1,-1\},
```

with

```math
P(z)=0.
```

Thus the minimal polynomial of `z` over `Q` has degree at most

```math
\boxed{m-1.}
\tag{4.4}
```

Equations (4.3) and (4.4) contradict each other.

This proves Theorem PE. `square`

---

## 5. Scope

The argument closes the complete P1 phase for every

```math
q=2^{r+1}+2.
```

It does not assume that the reciprocal five-term polynomial `F_m` from CF is globally irreducible. It works directly with the **unsquared** P1 relation and a different degree-`m` polynomial `G_n` in `u=1/D`.

The CF cyclotomic theorem is therefore not logically needed for PE, but it remains useful for all other arithmetic classes. PE and CF attack the same P1 endpoint from complementary directions.

The power-of-two condition is used exactly in (2.2). For a general `n`, `C_n(y) mod 2` need not be a monomial, so this particular Eisenstein proof does not extend automatically.

---

## 6. Immediate generalization target

For arbitrary even `m=2n`, the same exact polynomial

```math
G_n(u)=C_n(2-u^2)-2u
```

annihilates `u=1/D`.

Therefore any arithmetic class for which one can prove

```math
\deg_{\mathbb Q}(u^2)\ge m
```

also excludes P1 immediately.

Possible next routes:

1. classify irreducibility of `G_n` beyond powers of two;
2. factor `n=2^r s` and use the Chebyshev composition
   
   ```math
   C_n=C_s\circ C_{2^r}
   ```

   together with the linear `-2u` perturbation;
3. use modulo-three or modulo-five Newton polygons after a suitable translation;
4. combine CF's exclusion of all cyclotomic factors with the fixed physical root interval to control noncyclotomic factors.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exact polynomial `G_n(u)=0` | proved | unsquared P1 equation |
| `C_(2k)=C_k^2-2` | standard exact identity | trace Chebyshev |
| `C_(2^r)(y)=y^(2^r) mod 2` | proved | induction from doubling identity |
| `G_n` Eisenstein at two | proved | all nonleading coefficients even; constant exactly two mod four |
| degree of `u^2` remains `m` | proved | no opposite root pair |
| transfer to degree of `z` | proved | `u^2=2-(z+z^-1)` |
| P1 for `q-2` power of two | excluded exactly | degree contradiction with SC |
| general P1 | open | irreducibility/degree bound not yet proved for arbitrary `m` |
| Level I | still open | other arithmetic P1 classes and S1/D2/global phases remain |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P1 exact equation: m=q-2, x=delta/2, u=2sin x=1/D.
If m=2n then
    T_n(1-u^2/2)=u.
With C_n(y)=2T_n(y/2):
    G_n(u)=C_n(2-u^2)-2u=0,
    deg G_n=2n=m.

If n=2^r, C_(2k)=C_k^2-2 gives modulo 2
    C_n(y)=y^n,
so
    G_n(u)=u^m mod 2.
Every nonleading coefficient is even, while G_n(0)=2 is not divisible by 4.
Eisenstein at 2 => G_n irreducible, hence deg_Q(u)=m.
Also G_n(-u)-G_n(u)=4u, so no two conjugates are negatives of one another;
therefore their squares remain m distinct conjugates and
    deg_Q(u^2)=m.
But
    u^2=2-(z+z^-1) in Q(z), z=e^{i delta},
so deg_Q(z)>=m.
SC requires a Littlewood annihilator of degree m-1, hence deg_Q(z)<=m-1.
Contradiction.

Thus P1 is impossible whenever
    q-2=2^(r+1).
```
