<!-- theorem-state: {"artifact_id":"ART-FCE82DCA5F72","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — P1 Littlewood obstruction halves in the real trace field

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-d2-transversality-2026-09-10`  
**Run type:** exact arithmetic reduction  
**Target:** cyclic primitive phase `d_H=1`, P1  
**Depends on:** SC P1 Littlewood obstruction; CF on this branch  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The prior P1 arithmetic target asked for a degree-`m` irreducibility theorem. That is stronger than necessary.

Put

\[
m=q-2,
\qquad z=e^{i\delta},
\qquad y=z+z^{-1}=2\cos\delta.
\]

CF gives the trace polynomial

\[
\boxed{
H_m(Y):=C_m(Y)+4Y-6,
\qquad H_m(y)=0,
}
\tag{TH.1}
\]

where `C_m(Y)=2T_m(Y/2)`.

SC requires a Littlewood polynomial of degree `m-1` to vanish at `z`. Therefore

\[
[\mathbb Q(z):\mathbb Q]\le m-1.
\tag{TH.2}
\]

But the real trace field has exact index two in the P1 phase:

\[
\boxed{
[\mathbb Q(z):\mathbb Q(y)]=2.
}
\tag{TH.3}
\]

Hence every P1 survivor must satisfy

\[
\boxed{
[\mathbb Q(y):\mathbb Q]\le\frac{m-1}{2}.
}
\tag{TH.4}
\]

Equivalently, the physical root `y=2cos(delta)` must lie in an irreducible factor of `H_m` of degree at most `floor((m-1)/2)`.

Thus the shortest remaining arithmetic closure is only a **half-degree exclusion**:

> every irreducible factor of `H_m` meeting the physical P1 interval has degree greater than `(m-1)/2`.

No full irreducibility theorem is required.

---

## 1. Exact trace equation

CF derives from the squared P1 angle equation

\[
\cos(m\delta)+4\cos\delta-3=0.
\]

Since

\[
C_m(2\cos\delta)=2\cos(m\delta),
\]

putting

\[
y=2\cos\delta
\]

gives

\[
C_m(y)+4y-6=0.
\]

This is TH.1.

The physical root satisfies

\[
0<\delta<\pi/m,
\]

so

\[
2\cos(\pi/m)<y<2.
\tag{1.1}
\]

In particular `y` is real and `z=e^{i delta}` is nonreal.

---

## 2. The trace extension has degree exactly two

The element `z` satisfies

\[
X^2-yX+1=0
\tag{2.1}
\]

over `Q(y)`. Hence

\[
[\mathbb Q(z):\mathbb Q(y)]\le2.
\]

Equality is forced by reality. Under the distinguished embedding determined by the physical root, every element of

\[
\mathbb Q(y)
\]

is real because `y` is real. But

\[
z=e^{i\delta}\notin\mathbb R
\]

for `0<delta<pi`.

Therefore

\[
z\notin\mathbb Q(y),
\]

and (2.1) is irreducible over `Q(y)`. Thus

\[
\boxed{[\mathbb Q(z):\mathbb Q(y)]=2.}
\]

This argument avoids any discriminant-square subtlety: the physical embedding alone rules out `z in Q(y)`.

---

## 3. SC gives the half-degree bound

SC proves that P1 requires

\[
P(z)=0
\]

for a nonzero Littlewood polynomial

\[
P(Z)=\sum_{k=0}^{m-1}\varepsilon_kZ^k,
\qquad \varepsilon_k\in\{+1,-1\}.
\]

Therefore the minimal polynomial of `z` over `Q` divides `P`, so

\[
[\mathbb Q(z):\mathbb Q]\le m-1.
\]

The tower law and TH.3 give

\[
2[\mathbb Q(y):\mathbb Q]
=[\mathbb Q(z):\mathbb Q]
\le m-1.
\]

Hence TH.4.

Since the degree is an integer,

\[
\boxed{
[\mathbb Q(y):\mathbb Q]
\le\left\lfloor\frac{m-1}{2}\right\rfloor.
}
\tag{TH.5}
\]

---

## 4. Factor formulation

Let `R_m(Y)` be the minimal polynomial of the physical trace

\[
y=2\cos\delta.
\]

Then

\[
R_m\mid H_m
\]

and P1 forces

\[
\boxed{
\deg R_m\le\left\lfloor\frac{m-1}{2}\right\rfloor.
}
\tag{TH.6}
\]

CF already proves that the only trace-cyclotomic factor is `Y-1`, occurring exactly when `6|m`. The physical root lies in `(2cos(pi/m),2)`, so for large `m` it is not `1`.

Thus the remaining factor, if it exists, is noncyclotomic and has degree at most half of `H_m`.

This is substantially more restrictive than CF's earlier `deg minimal(z)<=m-1` formulation.

---

## 5. Interaction with PE

PE proves a stronger degree statement when `m` is a power of two: the auxiliary physical quantity `u^2` already has degree `m`, giving immediate contradiction.

TH explains what must be shown for general `m`. It is enough to establish

\[
\deg R_m>\frac{m-1}{2},
\]

not `deg R_m=m`.

This opens several weaker but potentially tractable routes:

1. modular factor-degree exclusion using two or more good primes;
2. a root-location theorem showing every rational factor containing the largest real root of `H_m` contains more than half the roots;
3. a Galois-orbit lower bound for the physical trace without full irreducibility;
4. a direct resultant obstruction with the restricted P1 sign word.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `H_m(2cos delta)=0` | proved | CF trace equation |
| `Q(y)` is real in the physical embedding | immediate | `y` real |
| `[Q(z):Q(y)]=2` | proved | quadratic equation plus nonreal `z` |
| SC implies `deg_Q(z)<=m-1` | proved | Littlewood annihilator |
| physical trace degree `<=floor((m-1)/2)` | proved | tower law |
| full irreducibility of `H_m` needed | false | half-degree exclusion suffices |
| general P1 | open | no uniform half-degree factor theorem yet |

---

## Compact handoff

```text
P1: m=q-2, z=e^{i delta}, y=z+z^-1=2cos delta.
Trace polynomial:
    H_m(Y)=C_m(Y)+4Y-6,
    H_m(y)=0.
SC requires a Littlewood polynomial of degree m-1 vanishing at z, hence
    [Q(z):Q] <= m-1.
But z satisfies X^2-yX+1 over Q(y), and z is nonreal while Q(y) is real under the
physical embedding. Thus
    [Q(z):Q(y)] = 2.
Therefore
    [Q(y):Q] <= floor((m-1)/2).
So P1 can be closed by proving only that the irreducible factor of H_m containing the
physical largest trace root has degree > (m-1)/2. Full irreducibility is unnecessary.
```
