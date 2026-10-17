> Generated reading edition · [exact source](../../../docs/reports/target_c_component_slack_cancellation_2026-09-09.md) · source SHA-256 `63dbd695889bb72f91cc590f53edba3a8fcaf30933305121988c3f0efeebeb04`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-22036F3A6AA1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — component Eppstein/stress slack cancellation

**Date:** 2026-09-09  
**Repository base:** current PR #110 post-ZF incidence branch  
**Run type:** exact algebraic sharpening  
**Target:** Target C Gate C-II / Level I  
**LEVEL I STATUS:** STILL OPEN

The post-ZF incidence identity ZI contains the attachment surplus

```math
U=\sum_r(t_r-\delta_r-3).
```

This note resolves `U` exactly. Each unit of excess attachment beyond C40's minimum is
either an extra pinned-contact stress dimension or an ordinary Eppstein edge slack
inside the unloaded component. Substitution improves the coefficient of `s_C` in the
main post-ZF graph-diameter bound from three to two.

## 1. Component slacks

For one unloaded component `I_r`, write

- `n_r=|I_r|`;
- `e_r` for internal contact edges;
- `t_r` for contacts from `I_r` to the loaded set `B_+`;
- `delta_r` for the graph diameter of `C[I_r]`, zero for a singleton.

The pinned rigidity block has `2n_r` columns and full rank. Its left nullity is

```math
\ell_r=e_r+t_r-2n_r.
\tag{1.1}
```

The positive KKT contact stress supplies one mandatory relation, so define

```math
\boxed{s_r:=\ell_r-1=e_r+t_r-2n_r-1\ge0.}
\tag{1.2}
```

The global pinned-contact surplus is exactly

```math
\boxed{s_C=\sum_rs_r.}
\tag{1.3}
```

Indeed the row sets are disjoint over the unloaded components and

```math
s_C=(e-e_{BB})-2(v-q)-c_I.
```

Eppstein's connected triangle-free penny-graph bound on `C[I_r]` gives

```math
e_r\le2n_r-\delta_r-2.
```

Define its exact nonnegative slack

```math
\boxed{r_r:=2n_r-\delta_r-2-e_r\ge0.}
\tag{1.4}
```

and put

```math
\boxed{R_I:=\sum_rr_r\ge0.}
\tag{1.5}
```

## 2. Theorem ZK — exact cancellation

### Theorem ZK.1

For every unloaded component,

```math
\boxed{
t_r-\delta_r-3=s_r+r_r.
}
\tag{ZK.1}
```

Consequently

```math
\boxed{U=s_C+R_I.}
\tag{ZK.2}
```

### Proof

Direct substitution gives

```math
\begin{aligned}
s_r+r_r
&=(e_r+t_r-2n_r-1)
 +(2n_r-\delta_r-2-e_r)\\
&=t_r-\delta_r-3.
\end{aligned}
```

Summing and using (1.3) proves ZK.2. `square`

This equality is stronger than the separate inequalities `t_r>=delta_r+3` and
`s_r>=0`: there is no third source of component attachment surplus.

## 3. Sharpened post-ZF diameter ledger

ZI proved

```math
\sum_r\delta_r+U+s_B+3k
=6+e_{BB}+3s_C,
\qquad
k=d_H+s_Z,
```

where

```math
s_B=3q-e_{BI}-2e_{BB}\ge0.
```

Insert ZK.2 and cancel one `s_C` from both sides.

### Theorem ZK.2 — sharpened component ledger

```math
\boxed{
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+e_{BB}+2s_C.
}
\tag{ZK.3}
```

Hence

```math
\boxed{
\sum_r\delta_r
\le
6-3(d_H+s_Z)+e_{BB}+2s_C
\le6+e_{BB}+2s_C,
}
\tag{ZK.4}
```

and

```math
\boxed{
3(d_H+s_Z)\le6+e_{BB}+2s_C.
}
\tag{ZK.5}
```

The exact remainder after paying mixed defect is now split into two transparent
nonnegative quantities:

1. `R_I`, the sum of internal penny-graph edge deficits;
2. `s_B`, unused loaded contact-degree capacity.

## 4. Improved population bound

Set

```math
\boxed{L_2:=6-3(d_H+s_Z)+e_{BB}+2s_C\ge0.}
\tag{4.1}
```

Then `sum delta_r<=L_2`. Repeating the ZP packing argument gives

```math
\boxed{
 v\le2\pi D+4L_2^2+4L_2.
}
\tag{4.2}
```

If

```math
\lambda_2:=\limsup\frac{e_{BB}+2s_C}{D},
```

then

```math
\boxed{
\limsup\frac v{D^2}\le4\lambda_2^2
}
\tag{4.3}
```

and, using `n/D^2 -> Delta=pi/(2sqrt3)`,

```math
\boxed{
\liminf\frac{n-v}{D^2}
\ge
\Delta-4\lambda_2^2.
}
\tag{4.4}
```

In particular the previously proved implication

```math
e_{BB}+s_C=o(D)\Longrightarrow v=o(D^2)
```

remains valid with a stronger finite estimate.

## 5. Improved attachment-gap bound

The ZG attachment-cell estimate likewise improves by replacing its old `L` with
`L_2`:

```math
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4L_2^2+\pi L_2+\pi^2D.
\tag{5.1}
```

Therefore C67 gives, for

```math
\lambda_2=\limsup(e_{BB}+2s_C)/D,
```

```math
\boxed{
\liminf\frac G{D^2}
\ge
\frac12\sin(1/4)-\frac\pi4\lambda_2^2.
}
\tag{5.2}
```

Thus the macroscopic-gap threshold is controlled by `e_BB+2s_C`, not the weaker
`e_BB+3s_C` currency.

## 6. Interpretation of equality

Equation ZK.3 shows exactly what equality in the component-diameter bound means.
If

```math
\sum_r\delta_r
=6-3k+e_{BB}+2s_C,
```

then simultaneously

```math
R_I=0,
\qquad
s_B=0.
```

So every unloaded component saturates Eppstein's edge bound and every loaded terminal
uses all three available contact incidences. This gives a concrete rigidity target for
future stability work; no hidden attachment slack remains.

In the exact zero-surplus branch `e_BB=s_C=0`, ZJ already gives `k=0`, and ZK.3 becomes

```math
\sum_r\delta_r+R_I+s_B=6.
```

The ZQ area contradiction therefore survives unchanged and its six-unit defect budget
is now decomposed exactly.

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `s_C=sum s_r` | proved | Pinned block direct sum and rank-nullity. |
| `U=s_C+R_I` | proved | Exact component algebra. |
| sharpened ZK.3 | proved | Substitute into exact ZI. |
| population and gap coefficient improvement | proved | Same ZP/ZG arguments with smaller `L_2`. |
| linear `e_BB+2s_C` lower bound | not proved | Macroscopic cavity/shell can still absorb the force-hull area. |
| Level I | still open | Cavity and linear-surplus branches remain. |

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For each unloaded component:
    s_r=e_r+t_r-2n_r-1 >=0,
    r_r=2n_r-delta_r-2-e_r >=0.
Then exactly
    t_r-delta_r-3=s_r+r_r.
Summing:
    U=s_C+R_I.

Hence ZI sharpens to
    sum delta_r + R_I + s_B + 3(d_H+s_Z)
      = 6+e_BB+2s_C.
So with
    L_2=6-3(d_H+s_Z)+e_BB+2s_C,
we have
    sum delta_r<=L_2,
    v<=2pi D+4L_2^2+4L_2,
and
    liminf G/D^2 >= (1/2)sin(1/4) - (pi/4)lambda_2^2,
where lambda_2=limsup(e_BB+2s_C)/D.
```
