> Generated reading edition · [exact source](../../../docs/reports/target_c_outer_pocket_wirtinger_detour_2026-09-09.md) · source SHA-256 `9f3ae14d141260157b36a61db104a32820b8642b848e96689fba499b0bdc7647`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C056974BA3E0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Wirtinger sharpening of outer-pocket detour area

**Date:** 2026-09-09  
**Repository base:** current PR #138 branch after OD/DE  
**Run type:** exact analytic sharpening  
**Target:** Target C C-II / outer-pocket cavity capacity  
**Depends on:** OP/PC pocket geometry; elementary one-dimensional Wirtinger inequality  
**LEVEL I STATUS:** STILL OPEN

OD proved

```math
area(P)
\le
\frac\pi{4\sqrt2}\ell^{3/2}\sqrt{\ell-s}
```

for one convex outer pocket whose old unit-contact boundary chain has length `ell` and whose force-hull side has chord length `s`.

The ellipse argument is convenient but loses a constant.  A direct arclength calculation gives the stronger self-contained estimate

```math
\boxed{
area(P)
\le
\frac{\sqrt2}{\pi}
\ell^{3/2}\sqrt{\ell-s}.
}
\tag{WD.1}
```

Since

```math
\frac{\sqrt2}{\pi}
=0.450158158078553\ldots
<
\frac\pi{4\sqrt2}
=0.555360367269796\ldots,
```

this improves every OD detour-area consequence by about nineteen percent at the constant level.

---

## 1. Put the chord on the horizontal axis

Fix one OP outer pocket `P`.  By OP/OD its boundary consists of

1. a simple polygonal unit-contact chain from `A` to `B`, of total length `ell`;
2. the force-hull chord `BA`, of length `s=|A-B|`.

OP proves the pocket is convex.  Translate and rotate so

```math
A=(0,0),
\qquad
B=(s,0),
```

and the pocket lies in the closed upper half-plane.

Parameterize the contact chain by arclength:

```math
\gamma(t)=(x(t),y(t)),
\qquad
0\le t\le\ell.
```

The functions `x,y` are piecewise linear and absolutely continuous, with

```math
x(0)=0,
\quad x(\ell)=s,
\quad y(0)=y(\ell)=0,
\tag{WD.2}
```

and, almost everywhere,

```math
\boxed{x'(t)^2+y'(t)^2=1.}
\tag{WD.3}
```

---

## 2. Chord deficit controls transverse derivative energy

Integrating `x'` gives

```math
\int_0^\ell x'(t)\,dt=s.
```

Hence

```math
\ell-s
=\int_0^\ell(1-x'(t))\,dt.
\tag{WD.4}
```

From WD.3,

```math
y'^2=1-x'^2=(1-x')(1+x').
```

Since `x'<=1`,

```math
1+x'\le2.
```

Also `1-x'>=0`. Therefore pointwise almost everywhere,

```math
y'^2\le2(1-x').
```

Integrating and using WD.4 gives the exact transverse-energy estimate

```math
\boxed{
\int_0^\ell y'(t)^2\,dt
\le2(\ell-s).
}
\tag{WD.5}
```

This is the key gain over the ellipse containment: the chain–chord detour directly controls squared transverse slope.

---

## 3. One-dimensional Wirtinger inequality

For every absolutely continuous function `f:[0,ell]->R` with

```math
f(0)=f(\ell)=0,
```

the sharp Dirichlet Poincare/Wirtinger inequality is

```math
\boxed{
\int_0^\ell f(t)^2\,dt
\le
\frac{\ell^2}{\pi^2}
\int_0^\ell f'(t)^2\,dt.
}
\tag{WD.6}
```

For completeness, this follows by scaling to `[0,pi]` and applying the standard sine-series identity

```math
f(t)=\sum_{m\ge1}a_m\sin(mt),
```

for which

```math
\int f^2=\frac\pi2\sum a_m^2,
\qquad
\int(f')^2=\frac\pi2\sum m^2a_m^2
\ge\int f^2.
```

Piecewise linear `y` lies in `H_0^1`, so WD.6 applies directly.  Applying it to `y` and then WD.5 gives

```math
\boxed{
\int_0^\ell y^2
\le
\frac{2\ell^2}{\pi^2}(\ell-s).
}
\tag{WD.7}
```

---

## 4. Area estimate

Because the closing chord lies on the `x`-axis, Green's formula gives the pocket area as

```math
area(P)
=\left|\int_0^\ell y(t)x'(t)\,dt\right|.
\tag{WD.8}
```

Cauchy–Schwarz gives

```math
area(P)
\le
\left(\int_0^\ell y^2\right)^{1/2}
\left(\int_0^\ell x'^2\right)^{1/2}.
\tag{WD.9}
```

From WD.3,

```math
\int_0^\ell x'^2\le\ell.
\tag{WD.10}
```

Insert WD.7 and WD.10 into WD.9:

```math
area(P)
\le
\left(\frac{2\ell^2}{\pi^2}(\ell-s)\right)^{1/2}
\ell^{1/2}
=
\boxed{
\frac{\sqrt2}{\pi}
\ell^{3/2}\sqrt{\ell-s}
}.
```

This proves WD.1.

No monotonicity of the `x` coordinate is required.  Backtracking portions of the convex boundary chain are allowed; WD.4-WD.10 remain valid.

---

## 5. Sum over all outer pockets

Use OD's exact identities

```math
\sum_P\ell_P=x_B+a,
\qquad
\sum_P(\ell_P-s_P)=b-P_F.
```

Applying WD.1 pocketwise and repeating OD's Cauchy argument gives

### Theorem WD.2 — global Wirtinger detour bound

```math
\boxed{
H_{out}
\le
\frac{\sqrt2}{\pi}
(x_B+a)^{3/2}
\sqrt{b-P_F}.
}
\tag{WD.11}
```

In exact post-ZF variables,

```math
\boxed{
H_{out}
\le
\frac{\sqrt2}{\pi}
\bigl(2h-Q-2s_Z-e_{BB}+c_B\bigr)^{3/2}
\sqrt{2h-Q-2s_Z-P_F}.
}
\tag{WD.12}
```

This strictly supersedes OD.1/OD.17 wherever the latter are used only through their constants.

---

## 6. Immediate stability consequences

Every qualitative OD consequence survives with the smaller constant. In particular:

- if `b-P_F=o(D)`, then `H_out=o(D^2)`;
- if `H_out>=gamma D^2` and `x_B+a<=LD`, then
  
  ```math
  \boxed{
  \frac{b-P_F}{D}
  \ge
  \frac{\pi^2\gamma^2}{2L^3}.
  }
  \tag{WD.13}
  ```


The second formula is obtained by squaring WD.11 and rearranging.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| transverse energy WD.5 | proved | arclength identity + chord deficit |
| Dirichlet Wirtinger WD.6 | standard/self-contained proof given | sine expansion |
| one-pocket bound WD.1 | proved | Green + Cauchy + WD.5-WD.6 |
| global bound WD.11 | proved | OD exact sums + Cauchy |
| improvement over ellipse constant | proved | direct numerical comparison |
| optimal fixed-chain/chord constant | not claimed | Dido/circular-arc extremizer can improve further |
| Level I | still open | high-surplus branch remains |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For one OP pocket, put its force-hull chord on the x-axis and arclength-parameterize
the old contact chain gamma=(x,y), 0<=t<=ell. Then
    x'^2+y'^2=1,
    integral x'=s,
so
    integral y'^2
      = integral (1-x'^2)
      <= 2 integral(1-x')
      = 2(ell-s).
Dirichlet Wirtinger gives
    integral y^2 <= (ell^2/pi^2) integral y'^2.
Since area(P)=|integral y x'| and integral x'^2<=ell,
    area(P) <= (sqrt2/pi) ell^(3/2) sqrt(ell-s).
Summing:
    H_out <= (sqrt2/pi)(x_B+a)^(3/2)sqrt(b-per(F)).

Constant sqrt2/pi=0.450158... strictly improves the OD ellipse constant
pi/(4sqrt2)=0.555360....
```
