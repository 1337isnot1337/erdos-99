> Generated reading edition · [exact source](../../../docs/reports/target_c_d2_p2_cyclotomic_trace_collapse_2026-09-10.md) · source SHA-256 `5762011acc9c653601328ef954c8a93f005fe361466c885bbd53cb43207d3285`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-327E601736A9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — D2/P2 has only one extraneous cyclotomic trace

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-d2-transversality-2026-09-10`  
**Run type:** exact arithmetic factor classification  
**Target:** cyclic primitive `d_H=2`, P2 endpoint  
**Depends on:** D2C P2 angle equation from PR #118  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

Put

```math
m:=q-4,
\qquad z=e^{i\delta},
\qquad y=z+z^{-1}=2\cos\delta,
```

with

```math
\delta=2\arcsin\frac1{2D},
\qquad
\Delta_2=2\arcsin\frac1D.
```

In P2 both defect cells are parallel cells, so D2C gives the exact projective closure

```math
\boxed{m\delta+2\Delta_2=\pi.}
\tag{PCF.1}
```

This implies the trace equation

```math
\boxed{
K_m(y):=C_m(y)+16y^2-48y+34=0,
}
\tag{PCF.2}
```

where `C_m(2cos theta)=2cos(m theta)`.

The cyclotomic trace content of this polynomial is completely rigid.

### Theorem PCF

Suppose `xi` is a root of unity and

```math
K_m(\xi+\xi^{-1})=0.
```

Then

```math
\boxed{
\xi\text{ is a primitive sixth root and }m\equiv3\pmod6.
}
\tag{PCF.3}
```

Conversely, if `m=3 mod 6`, both primitive sixth roots satisfy the equation and the corresponding trace factor is exactly

```math
\boxed{y-1.}
\tag{PCF.4}
```

Thus `y-1` is the only trace-cyclotomic factor of `K_m`, and it occurs exactly for `m=3 mod 6`.

The physical P2 root satisfies `0<delta<pi/m`; for `m>=4`,

```math
y=2\cos\delta>2\cos(\pi/m)>1.
```

Hence the physical root never lies in this factor. Every true P2 source must therefore use a noncyclotomic factor of `K_m`.

---

## 1. Derive the P2 trace polynomial

The angle definitions give

```math
\sin\frac{\Delta_2}{2}=\frac1D
=2\sin\frac\delta2.
```

Therefore

```math
\begin{aligned}
\cos\Delta_2
&=1-2\sin^2(\Delta_2/2)\\
&=1-8\sin^2(\delta/2)\\
&=4\cos\delta-3\\
&=2y-3.
\end{aligned}
\tag{1.1}
```

From PCF.1,

```math
m\delta=\pi-2\Delta_2,
```

so

```math
\cos(m\delta)=-\cos(2\Delta_2)
=1-2(2y-3)^2.
```

Multiplying by two and using `C_m(y)=2cos(m delta)` yields

```math
C_m(y)=2-4(2y-3)^2
=-16y^2+48y-34.
```

This is exactly PCF.2.

---

## 2. Galois trace over a primitive cyclotomic orbit

Assume `xi` is a primitive `r`th root and

```math
K_m(\xi+\xi^{-1})=0.
```

Because `K_m` has rational coefficients, the same equation holds for every primitive `r`th root.

Using

```math
(\xi+\xi^{-1})^2=\xi^2+\xi^{-2}+2,
```

PCF.2 becomes

```math
\xi^m+\xi^{-m}
+16(\xi^2+\xi^{-2})
-48(\xi+\xi^{-1})
+66=0.
\tag{2.1}
```

Let

```math
c_r(k)=\sum_{(a,r)=1}e^{2\pi iak/r}
```

be the Ramanujan sum. Summing (2.1) over all primitive `r`th roots and dividing by two gives

```math
\boxed{
c_r(m)+16c_r(2)-48\mu(r)+33\phi(r)=0.}
\tag{2.2}
```

This integer identity controls every possible cyclotomic trace factor.

---

## 3. Totient squeeze

Use

```math
|c_r(m)|\le\phi(r),
\qquad
|c_r(2)|\le\phi(r),
\qquad
|\mu(r)|\le1.
```

Equation (2.2) gives

```math
33\phi(r)
\le17\phi(r)+48,
```

hence

```math
\boxed{\phi(r)\le3.}
\tag{3.1}
```

The only positive integers with totient at most three are

```math
r\in\{1,2,3,4,6\}.
```

Check them in (2.2).

- `r=1`: the left side is `1+16-48+33=2`.
- `r=2`: `c_2(2)=1`, `mu(2)=-1`; the left side is `c_2(m)+97`, never zero.
- `r=3`: `c_3(2)=-1`, `mu(3)=-1`; the left side is `c_3(m)+98`, never zero.
- `r=4`: `c_4(2)=-2`, `mu(4)=0`; the left side is `c_4(m)+34`, never zero.
- `r=6`: `c_6(2)=-1`, `mu(6)=1`, `phi(6)=2`; the equation reduces to
  
  ```math
  c_6(m)+2=0.
  ```


For a primitive sixth root `xi`,

```math
c_6(m)=\xi^m+\xi^{-m}.
```

This equals `-2` exactly when `xi^m=-1`, equivalently

```math
\boxed{m\equiv3\pmod6.}
```

This proves the necessary direction of PCF.3.

Conversely, if `m=3 mod 6`, then at `y=1`

```math
C_m(1)=2\cos(m\pi/3)=-2
```

and

```math
16-48+34=2,
```

so `K_m(1)=0`. This proves the converse and PCF.4. `square`

---

## 4. Physical root is not the cyclotomic trace

P2 has

```math
m\delta+2\Delta_2=\pi
```

with `Delta_2>0`, hence

```math
0<\delta<\pi/m.
```

For `m>=4`,

```math
2\cos(\pi/m)>1,
```

so the physical trace obeys

```math
\boxed{y=2\cos\delta>1.}
```

Therefore the only possible cyclotomic trace `y=1` is outside the physical P2 branch.

Thus every true P2 source forces a noncyclotomic irreducible factor of `K_m` containing its largest real root in `(2cos(pi/m),2)`.

---

## 5. Why this matters for SCE

In P2 the two midpoint-error vectors in SCE vanish, so shell closure is exact:

```math
P_A(z)+e^{i(L_A\delta+\Delta_2)}P_B(z)=0.
\tag{5.1}
```

The remaining arithmetic obstruction is therefore noncyclotomic from both sides:

1. the physical trace lies in a noncyclotomic factor of `K_m`;
2. the staircase closure supplies a low-complexity algebraic relation in `z=e^{i delta}`.

A factor-degree theorem for the physical factor of `K_m` can now close P2 without any root-of-unity exceptional cases except the explicitly removed `y=1` factor.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| P2 trace polynomial `K_m` | proved | exact angle identities |
| Ramanujan identity PCF.2 | proved | Galois trace over primitive roots |
| `phi(r)<=3` | proved | absolute-value squeeze |
| only cyclotomic trace is `y=1` | proved | finite `r` check |
| occurrence iff `m=3 mod 6` | proved | `c_6(m)=-2` |
| physical root equals `1` | excluded | physical interval is above `1` |
| general P2 | open | noncyclotomic factor-degree/SCE compatibility remains |

---

## Compact handoff

```text
P2: m=q-4 and m delta+2 Delta_2=pi.
With y=2cos delta and C_m(y)=2cos(m delta),
    cos Delta_2=2y-3,
so
    K_m(y)=C_m(y)+16y^2-48y+34=0.

If y=xi+xi^-1 for primitive rth root xi, summing the equation over its Galois orbit gives
    c_r(m)+16c_r(2)-48 mu(r)+33 phi(r)=0.
Bounds imply phi(r)<=3, so r in {1,2,3,4,6}. Direct substitution leaves only r=6,
and then c_6(m)=-2 iff m=3 mod 6. Conversely K_m(1)=0 in exactly that case.
Therefore y-1 is the only trace-cyclotomic factor, and the physical P2 root y>1 never lies there.
```
