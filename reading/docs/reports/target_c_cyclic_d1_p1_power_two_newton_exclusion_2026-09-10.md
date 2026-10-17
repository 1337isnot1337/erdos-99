> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_p1_power_two_newton_exclusion_2026-09-10.md) · source SHA-256 `d3bc158b6a3b80ad960aba2ce81b68a40fb13e20999db255d869d079b067f7df`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

> Source formatting note: 5 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-04524C14BE8F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — a 2-adic Newton obstruction excludes infinitely many `d_H=1` P1 endpoints

**Date:** 2026-09-10  
**Run type:** exact arithmetic exclusion inside the cyclic `d_H=1` endpoint  
**Target:** P1 branch of the exact one-defect difference-body normal form  
**Depends on:** D1 P1 geometry and SC P1 Littlewood closure on PR #118  
**External theorem:** only the standard Newton-polygon valuation theorem, reproved at the degree level needed below  
**Computation:** not used in the proof

## 1. Result

Write

```math
n:=q-2.
```

D1/SC prove that every P1 survivor supplies an angle

```math
\delta\in(0,\pi)
```

such that, with

```math
x=\frac\delta2,
\qquad
z=e^{i\delta},
```

one has

```math
\cos(nx)=2\sin x
\tag{PA.1}
```

and simultaneously a Littlewood polynomial

```math
P(z)=\sum_{j=0}^{n-1}\varepsilon_jz^j,
\qquad
\varepsilon_j\in\{+1,-1\},
\tag{PA.2}
```

with

```math
P(z)=0.
\tag{PA.3}
```

The new theorem is:

### Theorem PA — power-of-two P1 exclusion

If

```math
\boxed{q-2=2^k}
```

for some integer `k>=1`, then the cyclic `d_H=1` P1 endpoint is impossible.

Equivalently, every P1 survivor has

```math
\boxed{q-2\ne2^k.}
\tag{PA.4}
```

This excludes an infinite family of terminal counts exactly. It does **not** yet exclude arbitrary P1 terminal counts.

The mechanism is stronger than ordinary Eisenstein: the P1 geometric root has algebraic degree at least `n=q-2`, while SC requires it to have degree at most `n-1`.

---

## 2. The geometric reciprocal polynomial

Square PA.1. Since

```math
2\cos^2(nx)=1+\cos(2nx),
\qquad
8\sin^2x=4(1-\cos2x),
```

we obtain

```math
\cos(n\delta)+4\cos\delta-3=0.
\tag{2.1}
```

With `z=e^{i delta}`, multiply

```math
z^n+z^{-n}+4(z+z^{-1})-6=0
```

by `z^n`. Thus `z` is a root of

```math
\boxed{
G_n(Z)
:=Z^{2n}+4Z^{n+1}-6Z^n+4Z^{n-1}+1.
}
\tag{2.2}
```

A useful exact form is

```math
\boxed{
G_n(Z)
=(Z^n+1)^2+4Z^{n-1}(Z-1)^2.
}
\tag{2.3}
```

No implication is reversed here: PA.1 implies `G_n(z)=0`. Squaring may introduce additional roots of `G_n`, but that causes no problem for a necessary-condition argument.

---

## 3. Shift to the 2-adic center

Assume now

```math
n=2^k.
```

Put

```math
Y:=Z-1
```

and define

```math
Q_n(Y):=G_n(1+Y).
```

From (2.3),

```math
\boxed{
Q_n(Y)
=\bigl((1+Y)^n+1\bigr)^2
+4(1+Y)^{n-1}Y^2.
}
\tag{3.1}
```

Because `n` is a power of two, every interior binomial coefficient

```math
\binom nj,
\qquad1\le j\le n-1,
```

is even. Therefore for some `B(Y) in Z[Y]`,

```math
(1+Y)^n+1
=Y^n+2+2B(Y).
\tag{3.2}
```

Squaring modulo four gives

```math
\bigl((1+Y)^n+1\bigr)^2
\equiv Y^{2n}\pmod4.
```

The second term in (3.1) is itself divisible by four. Hence

```math
\boxed{Q_n(Y)\equiv Y^{2n}\pmod4.}
\tag{3.3}
```

Also

```math
\boxed{Q_n(0)=4}
\tag{3.4}
```

and `Q_n` is monic of degree `2n`.

Consequently, if

```math
Q_n(Y)=\sum_{j=0}^{2n}a_jY^j,
```

then

```math
v_2(a_0)=2,
\qquad
v_2(a_j)\ge2\quad(1\le j<2n),
\qquad
v_2(a_{2n})=0.
\tag{3.5}
```

---

## 4. One-segment Newton polygon

Plot the coefficient points

```math
(j,v_2(a_j)).
```

The endpoints are

```math
(0,2),
\qquad
(2n,0).
```

Every intermediate coefficient point has height at least two. The line joining the endpoints has equation

```math
y=2-\frac jn,
```

which is strictly below two for every `j>0`. Hence every intermediate coefficient point lies strictly above that line.

Therefore the lower 2-adic Newton polygon of `Q_n` consists of the single segment

```math
\boxed{(0,2)\longrightarrow(2n,0)}
\tag{4.1}
```

of slope

```math
\boxed{-\frac1n.}
\tag{4.2}
```

The standard Newton-polygon root theorem now says that every root `y` of `Q_n` in an algebraic closure of `Q_2` has normalized valuation

```math
\boxed{v_2(y)=\frac1n.}
\tag{4.3}
```

For completeness, only the following degree consequence is needed. If

```math
L=\mathbb Q_2(y),
```

its value group is contained in

```math
\frac1e\mathbb Z,
```

where `e` is the ramification index of `L/Q_2`. Since `1/n` is in lowest terms and belongs to this value group, one must have

```math
n\mid e.
```

As

```math
e\le[L:\mathbb Q_2],
```

we get

```math
\boxed{[\mathbb Q_2(y):\mathbb Q_2]\ge n.}
\tag{4.4}
```

Thus this argument does **not** need full irreducibility of `Q_n`; it only needs the denominator of its unique Newton slope.

---

## 5. Global algebraic degree of the P1 root

Our geometric root `z` of `G_n` gives

```math
y=z-1,
\qquad
Q_n(y)=0.
```

Choose any embedding of `Q(z)=Q(y)` into an algebraic closure of `Q_2` corresponding to a prime above two. The resulting local degree cannot exceed the global degree:

```math
[\mathbb Q_2(y):\mathbb Q_2]
\le
[\mathbb Q(y):\mathbb Q].
```

Using (4.4),

```math
\boxed{
[\mathbb Q(z):\mathbb Q]
=[\mathbb Q(y):\mathbb Q]
\ge n.
}
\tag{5.1}
```

This is the decisive arithmetic lower bound.

---

## 6. Contradiction with the SC Littlewood closure

SC requires a nonzero polynomial

```math
P(Z)=\sum_{j=0}^{n-1}\varepsilon_jZ^j
\in\mathbb Z[Z]
```

of degree exactly `n-1` satisfying

```math
P(z)=0.
```

Therefore the minimal polynomial of `z` over `Q` divides `P`, so

```math
[\mathbb Q(z):\mathbb Q]
\le n-1.
\tag{6.1}
```

But (5.1) gives

```math
[\mathbb Q(z):\mathbb Q]
\ge n.
```

Contradiction.

Thus no P1 survivor exists when

```math
n=q-2=2^k.
```

This proves Theorem PA. `square`

---

## 7. Why this is not ordinary Eisenstein

A tempting shortcut is to work with the trace variable

```math
t=z+z^{-1}
```

and the polynomial

```math
H_n(t)=D_n(t,1)+4t-6,
```

where `D_n(t,1)=z^n+z^{-n}` is the Dickson polynomial. For `n=2^k`, reduction modulo two gives the monomial behavior expected from Frobenius, but the constant coefficient of `H_n` is generally divisible by four; ordinary Eisenstein at two does **not** apply.

The shifted reciprocal polynomial `Q_n(Y)=G_n(1+Y)` is the correct object. Its one Newton slope still supplies exactly the degree obstruction needed for P1.

This distinction is recorded explicitly to prevent promotion of the false ordinary-Eisenstein shortcut.

---

## 8. Regression and scope audit

### `n` not a power of two

The parity step (3.2) fails in general. The theorem makes no claim for those terminal counts.

### Additional roots introduced by squaring

Harmless. The actual P1 root satisfies PA.1 and therefore certainly satisfies `G_n(z)=0`. The degree lower bound holds for every root of `G_n` when `n=2^k`, so it applies to the geometric root in particular.

### Root `z=1`

Impossible geometrically because `delta>0`; in any case `G_n(1)=4`.

### Local versus global degree

The proof only uses a local-degree lower bound. It does not claim that `G_n` or `H_n` is globally irreducible.

### Small `q`

The Target C cyclic endpoint is already a sufficiently-large-source theorem. PA is compatible with all small-case exceptions in the problem baseline.

---

## 9. Broader factor pattern: computational evidence only

The natural next question is whether the degree obstruction holds for **all** `n=q-2`.

Writing

```math
t=z+z^{-1},
```

one has

```math
z^{-n}G_n(z)
=H_n(t)
:=D_n(t,1)+4t-6.
\tag{9.1}
```

Finite symbolic factorization suggests the following stronger pattern:

```text
if 6 does not divide n:
    H_n(t) is irreducible over Q;

if 6 divides n:
    H_n(t)=(t-1) J_n(t),
    with J_n irreducible of degree n-1.
```

The factor `t-1` corresponds to the irrelevant primitive-sixth-root directions, not to the small P1 angle `delta~pi/q`.

This pattern has **not** been proved and is not used by PA. It is recorded as a precise candidate theorem because, if established, it would exclude the entire P1 branch: every geometric P1 root would have degree at least `n`, while SC always gives a degree-`n-1` Littlewood annihilator.

---

## 10. Exact next lemma

The most valuable arithmetic target is:

> Let `n>=2`, and let `z=e^{i delta}` be the unique small-angle root selected by the P1 equation
> ```math
> \cos(n\delta/2)=2\sin(\delta/2).
> ```
> Prove
> ```math
> [\mathbb Q(z):\mathbb Q]\ge n.
> ```

Full irreducibility of `G_n` is stronger than necessary. It is enough to rule out any factor of degree `<n` containing the small-angle root.

Promising continuations are:

1. obtain a suitable local Newton slope at a prime depending on the arithmetic of `n`;
2. prove the observed factor theorem for `H_n=D_n+4t-6`;
3. use SC's stronger sign-run restrictions rather than arbitrary Littlewood polynomials.

---

## 11. Promotion recommendation

**Hold as a report-level theorem pending independent audit.**

PA is exact downstream of report-level D1/SC. It eliminates infinitely many P1 terminal counts but does not settle the complete `d_H=1` phase or Level I.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P1 puts n=q-2 and supplies z=e^{i delta} satisfying
  cos(n delta/2)=2 sin(delta/2)
and a Littlewood polynomial P of degree n-1 with P(z)=0.
Squaring the geometric equation gives
  G_n(z)=0,
  G_n(Z)=(Z^n+1)^2+4Z^{n-1}(Z-1)^2.

If n=2^k, put Y=Z-1. Then
  Q_n(Y)=G_n(1+Y)
        =((1+Y)^n+1)^2+4(1+Y)^{n-1}Y^2.
All interior binomial coefficients C(n,j) are even, hence
  Q_n(Y) == Y^(2n) (mod 4),
while Q_n(0)=4 and Q_n is monic.
The 2-adic Newton polygon is one segment (0,2)->(2n,0), slope -1/n.
Thus every root y has v_2(y)=1/n, forcing local and hence global algebraic degree >=n.
But P(z)=0 with deg P=n-1 forces degree <=n-1. Contradiction.

Therefore P1 is impossible whenever q-2 is a power of two.

Next: prove degree >=n for the P1 small-angle root for arbitrary n; symbolic evidence suggests
H_n(t)=D_n(t,1)+4t-6 is irreducible unless 6|n, in which case only the irrelevant
factor t-1 splits off.
```
