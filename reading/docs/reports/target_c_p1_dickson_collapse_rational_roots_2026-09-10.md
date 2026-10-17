> Generated reading edition · [exact source](../../../docs/reports/target_c_p1_dickson_collapse_rational_roots_2026-09-10.md) · source SHA-256 `17f58aec3fbcd4c90c0a7dba3be1f26a43d86fd09f840f4f04a48ce9d7f213f4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F53DFCF59DCB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — P1 even case collapses to a Dickson linear perturbation

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-d2-transversality-2026-09-10`  
**Run type:** exact arithmetic normalization / rational-factor classification  
**Target:** cyclic primitive phase `d_H=1`, P1  
**Depends on:** SC P1 fixed-angle equation; PE on this branch  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

For even

```math
m=q-2=2n,
```

the auxiliary polynomial introduced in PE is not ad hoc. It is exactly a standard trace-Chebyshev/Dickson polynomial with one linear perturbation.

Let

```math
C_k(x)=2T_k(x/2),
```

so

```math
C_a(C_b(x))=C_{ab}(x),
\qquad
C_k(-x)=(-1)^kC_k(x).
```

The P1 physical parameter

```math
u=2\sin(\delta/2)=1/D
```

satisfies

```math
G_n(u):=C_n(2-u^2)-2u=0.
```

Because

```math
2-u^2=-C_2(u),
```

we obtain the exact collapse

```math
\boxed{
G_n(u)=(-1)^nC_{2n}(u)-2u
      =(-1)^nC_m(u)-2u.
}
\tag{DC.1}

```

Define

```math
\boxed{
J_m(u):=(-1)^{m/2}C_m(u)-2u.
}
\tag{DC.2}

```

Then every even-`m` P1 source satisfies `J_m(1/D)=0`.

The rational roots of `J_m` can be classified exactly.

### Theorem DC — rational-root classification

For even `m=2n`, `J_m` has a rational root if and only if `3|n`. In that case it has exactly one rational root,

```math
\boxed{
u=(-1)^{n/3}\in\{+1,-1\}.}
\tag{DC.3}

```

Equivalently,

- if `n=0 mod 6`, the unique rational root is `u=1`;
- if `n=3 mod 6`, the unique rational root is `u=-1`;
- if `3` does not divide `n`, there is no rational root.

Since every large P1 source has

```math
0<u=1/D<1,
```

the physical P1 root is never rational.

Thus the experimentally observed linear factor when `3|n` is completely explained and is irrelevant to the physical branch.

---

## 1. Dickson composition identity

The trace-Chebyshev family satisfies

```math
C_k(z+z^{-1})=z^k+z^{-k}.
```

Applying this twice gives the composition identity

```math
\boxed{C_a(C_b(x))=C_{ab}(x).}
\tag{1.1}
```

Also

```math
C_k(-x)=(-1)^kC_k(x).
\tag{1.2}
```

Now

```math
C_2(u)=u^2-2,
```

so

```math
2-u^2=-C_2(u).
```

Therefore

```math
\begin{aligned}
C_n(2-u^2)
&=C_n(-C_2(u))\\
&=(-1)^n C_n(C_2(u))\\
&=(-1)^n C_{2n}(u).
\end{aligned}
```

Substituting into PE.3 proves DC.1-DC.2.

This normalization matters because all remaining even-P1 arithmetic is now a factor problem for one standard Dickson/Chebyshev polynomial minus a linear term.

---

## 2. Integral and constant-term structure

For every `m`, `C_m(x)` is monic with integer coefficients. For even `m=2n`,

```math
C_m(0)=2\cos(m\pi/2)=2(-1)^n.
```

Hence

```math
\boxed{J_m(0)=2.}
\tag{2.1}
```

The leading coefficient of `J_m` is `(-1)^n`, so the rational-root theorem implies every rational root lies in

```math
\{\pm1,\pm2\}.
\tag{2.2}
```

---

## 3. Evaluate the four candidates

It is cleaner to use the equivalent PE form

```math
J_m(u)=G_n(u)=C_n(2-u^2)-2u.
```

At `u=1`,

```math
J_m(1)=C_n(1)-2
=2\cos(n\pi/3)-2.
```

Therefore

```math
\boxed{J_m(1)=0\iff n\equiv0\pmod6.}
\tag{3.1}
```

At `u=-1`,

```math
J_m(-1)=C_n(1)+2
=2\cos(n\pi/3)+2,
```

so

```math
\boxed{J_m(-1)=0\iff n\equiv3\pmod6.}
\tag{3.2}
```

At `u=2`, use `C_m(2)=2` in the Dickson form:

```math
J_m(2)=2(-1)^n-4\in\{-2,-6\},
```

never zero.

Since `m` is even, `C_m(-2)=2`, and

```math
J_m(-2)=2(-1)^n+4\in\{2,6\},
```

also never zero.

Thus the only possible rational roots are exactly those in (3.1)-(3.2). Combining them gives DC.3.

---

## 4. The linear factor is physically irrelevant

For every P1 source,

```math
u=1/D>0.
```

In the sufficiently large Target C regime, `D>1`, so

```math
0<u<1.
```

Therefore neither of the two possible rational roots `+1,-1` is physical.

When `3|n`, define

```math
\varepsilon_n:=(-1)^{n/3}.
```

Then

```math
J_m(u)=(u-\varepsilon_n)K_m(u)
```

for an integer polynomial `K_m` of degree `m-1`, and the physical root must lie in `K_m`.

Exact factor experiments suggested that this quotient is irreducible for the tested values, but that observation is **not** used here.

---

## 5. Relation to the power-of-two theorem PE

If `m=2^{r+1}`, then `n=2^r` is never divisible by three, so DC says `J_m` has no rational factor at all.

PE proves much more in that case: `J_m` is Eisenstein at two after the equivalent composition normalization, hence irreducible of degree `m`, and P1 is impossible.

DC isolates what changes for general even `m`: the only degree-one obstruction is the explicit extraneous factor at `u=+/-1`. Any physical P1 survivor must therefore be carried by a nonlinear irreducible factor.

---

## 6. Sharpened next target

Combine DC with TH. The physical trace

```math
y=2\cos\delta=2-u^2
```

would have algebraic degree at most

```math
\left\lfloor\frac{m-1}{2}\right\rfloor.
```

For even `m`, all arithmetic now sits in

```math
J_m(u)=(-1)^{m/2}C_m(u)-2u.
```

The next sufficient theorem can be stated in either of two equivalent forms:

1. every nonlinear irreducible factor of `J_m` containing a real root in `(0,1)` has degree greater than `m-1`; or
2. the corresponding root of `H_m(y)=C_m(y)+4y-6` in the physical interval has degree greater than `(m-1)/2`.

The second is weaker and is the preferred target.

The exact Dickson form makes finite-field factor-degree and composition methods available without the extra quadratic substitution from PE.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `G_n=(-1)^n C_(2n)-2u` | proved | parity + Dickson composition |
| `J_m` monic up to sign, constant two | proved | standard `C_m` values |
| all rational roots are among `+/-1,+/-2` | proved | rational-root theorem |
| `+1` root iff `n=0 mod 6` | proved | `C_n(1)=2cos(n pi/3)` |
| `-1` root iff `n=3 mod 6` | proved | same identity |
| `+/-2` never roots | proved | `C_m(+/-2)=2` for even `m` |
| physical P1 root rational | excluded | `0<u<1` |
| nonlinear quotient irreducible | not claimed | experimental only |
| general P1 | open | nonlinear factor-degree obstruction remains |

---

## Compact handoff

```text
Even P1: m=2n, u=1/D.
PE polynomial:
    G_n(u)=C_n(2-u^2)-2u.
Since 2-u^2=-C_2(u), parity and C_a(C_b)=C_ab give
    G_n(u)=(-1)^n C_(2n)(u)-2u
          =(-1)^n C_m(u)-2u=:J_m(u).
Thus even P1 is exactly a Dickson/Chebyshev-minus-linear factor problem.

J_m has constant term 2 and leading coefficient +/-1, so rational roots can only be
+/-1,+/-2.  Directly:
    J_m(1)=2cos(n pi/3)-2,
    J_m(-1)=2cos(n pi/3)+2,
while +/-2 are never roots.
Hence a rational root exists iff 3|n, and it is uniquely
    u=(-1)^(n/3).
This is +/-1, so never the physical root 0<u=1/D<1.
```
