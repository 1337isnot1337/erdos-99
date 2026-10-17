> Generated reading edition · [exact source](../../research/target_c_two_halfdisk_scalar_regression_2026-09-12.md) · source SHA-256 `ae5cba9e1ad288dd3cb9d360ff8816a0128d511b610b539e3b4a7a0918a92347`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — two-half-disk scalar regression after perimeter rigidity

**Date:** 2026-09-12  
**Status:** audited arithmetic regression; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The perimeter-rigidity candidate raises the two-half-disk boundary floor to
`T/D >= 1+pi/2`. This note checks that the strengthened floor is still compatible
with the September 12 normalized Type-II ledgers listed below. The witness is algebraic; it
is not claimed to come from an actual source or global minimizer.

## 1. Normalized variables and retained inequalities

Use

```text
t      = (q-k)/D
kappa  = k/D
S      = sum_r d_r/D
G      = G_D/D
mu     = S+G
m      = mu-t
e      = e_BB/D = 2*t+kappa-mu
u      = u_B/D
Q      = Q/D = e-2*kappa-u
f      = f/D
T      = t+2*f = (q+2f-k)/D
```

The test retains the exact surplus/moment identity, nonnegative currencies, the
Type-II loaded-hull bound `q/D=t+kappa<=pi`, the half-disk remainder floor
`S+G>=pi/sqrt(2)`, the retained §161 inequality, the half-disk stopped-train floor

$$
T-\frac{t+\kappa}{2}\ge2\sqrt{2\Delta_2},
\qquad
\Delta_2=\frac{\pi}{2\sqrt3},
$$

the strict stopped-train phase floor `2f-kappa>2sqrt(Delta_2)-pi/2`, the new
perimeter floor `T>=1+pi/2`, and the §123 payment `4f+Q<=10(e-kappa)`.

## 2. Exact rational witness

Take

```text
t=21/10,       kappa=0,
S=14/5,        G=3/10,       mu=31/10,
m=1,           e=11/10,
u=1/10,        Q=1,
f=9/10,        T=39/10.
```

The identities check exactly:

```text
mu=S+G,
m=mu-t,
e=2*t+kappa-mu,
Q+u=e-2*kappa,
T=t+2*f,
q/D=t+kappa=m+e.
```

The key margins are visible without a numerical optimizer:

```text
T - q/(2D) = 57/20 = 2.85,
T          = 39/10 = 3.9,
S+G        = 31/10 = 3.1,
5*t        = 21/2 = 10.5,
S+2*mu     = 9,
4*f+Q      = 23/5 = 4.6,
10*(e-k)   = 11.
```

Thus the perimeter floor and stopped-train floor are both satisfied with room to
spare; the moment/remainder and payment ledgers do not force a contradiction.

## 3. Irrational comparisons

Using `pi<3.14160` and `sqrt(3)>1.73205`, the verifier checks

```text
t < pi,
S+G > pi/sqrt(2),
5*t > S+2*mu + pi*(2-sqrt(3))/4,
T-q/(2D) > 2*sqrt(2*pi/(2*sqrt(3))),
2*f > 2*sqrt(pi/(2*sqrt(3))) - pi/2,
T > 1+pi/2,
u+mu+kappa > pi.
```

The perimeter line is the new rigidity floor, and the final line is the §172 sign
condition that the corrected witness now satisfies. All comparisons are made with
conservative rational bounds in the accompanying script.

### September 30 certificate correction and scope

The verifier previously tested `mu > pi/(2 sqrt(2))` in place of the stated
`mu > pi/sqrt(2)`, and tested the stopped-train margin against a lower bound
for its required right-hand side. Those tests did not certify the displayed
claims. The witness itself satisfies both stronger inequalities. The repaired
verifier checks the full remainder quotient, uses positive squaring with an
upper bound for `4*pi/sqrt(3)`, and certifies its pi interval from rational
alternating-series bounds in Machin's identity. The square-root lower bounds
are checked by rational squaring, as is the retained `1.905` upper bound for
the phase radical. No floating-point arithmetic is used.

This is a certificate for the historical scalar system listed here. It is not
a witness for every later current-main inequality: in particular its
`sum d_r/D = 14/5` exceeds the September 29 shape-detour bound
`sum d_r/D <= 1+pi/2+o(1)`. It must not be used as evidence that the complete
September 30 full-core system is compatible.

## 4. Implication boundary

This regression proves only that

```text
listed historical scalar Type-II ledgers + half-disk perimeter rigidity
    -> no algebraic contradiction.
```

It does not construct a geometric half-disk rhombus complex, certify global
optimality, or weaken the perimeter theorem. A C-II closure still needs a geometric
correlation, source-preserving diameter descent, or exact unit triangle.

**Classification:** regression; audited arithmetic only.
