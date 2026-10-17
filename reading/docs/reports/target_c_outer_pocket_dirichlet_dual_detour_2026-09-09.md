> Generated reading edition · [exact source](../../../docs/reports/target_c_outer_pocket_dirichlet_dual_detour_2026-09-09.md) · source SHA-256 `05ca12ba5ffa53b9fd84c6d0dcb93f1e4e4be7afcd7e80b4fd1465e8c782a643`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1C88DB966B1B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Dirichlet-dual sharpening of outer-pocket detour area

**Date:** 2026-09-09  
**Repository base:** `79c92247ac460e94761938f9d44fb6ba2e3e4087`  
**Run type:** exact analytic sharpening  
**Target:** Target C C-II / outer-pocket cavity capacity  
**Depends on:** OP/PC pocket geometry and the exact chain–chord detour identities  
**External input:** none  
**LEVEL I STATUS:** STILL OPEN

WD bounded one convex OP outer pocket by

$$
area(P)
\le
\frac{\sqrt2}{\pi}\ell^{3/2}\sqrt{\ell-s},
$$

where `ell` is the length of the old unit-contact boundary chain and `s` is the length of its force-hull chord.

A sharper direct functional estimate is available.  The area is controlled by the **mean transverse height**, not its `L^2` norm.  The exact Dirichlet dual of the mean functional gives

$$
\boxed{
area(P)
\le
\frac1{\sqrt6}
\ell^{3/2}\sqrt{\ell-s}.
}
\tag{DD.1}
$$

The constant improves from

$$
\frac{\sqrt2}{\pi}=0.4501581580\ldots
$$

to

$$
\frac1{\sqrt6}=0.4082482904\ldots .
$$

No fixed-endpoint Dido theorem or calculus-of-variations classification is required.

---

## 1. Arclength setup

Fix one OP outer pocket `P`.  Its boundary consists of

1. a simple old-contact chain from `A` to `B`, of total length `ell`;
2. the force-hull side `BA`, of length `s=|A-B|`.

OP proves the pocket is convex.  Translate and rotate so

$$
A=(0,0),
\qquad
B=(s,0),
$$

and `P` lies in the closed upper half-plane.

Parameterize the contact chain from `A` to `B` by arclength:

$$
\gamma(t)=(x(t),y(t)),
\qquad 0\le t\le\ell.
$$

Then

$$
y(t)\ge0,
\qquad
y(0)=y(\ell)=0,
\tag{DD.2}
$$

and almost everywhere

$$
\boxed{x'^2+y'^2=1.}
\tag{DD.3}
$$

Also

$$
\int_0^\ell x'(t)\,dt=s.
\tag{DD.4}
$$

---

## 2. Chord deficit bounds transverse derivative energy

Exactly as in WD,

$$
y'^2
=1-x'^2
=(1-x')(1+x')
\le2(1-x'),
$$

because `x'<=1`.  Integrating and using DD.4 gives

$$
\boxed{
\int_0^\ell y'^2\,dt
\le2(\ell-s).
}
\tag{DD.5}
$$

This step is valid even if the convex boundary chain backtracks in the chord direction.

---

## 3. The mean-height Dirichlet inequality

Define

$$
g(t):=\frac12t(\ell-t).
\tag{DD.6}
$$

Then

$$
-g''(t)=1,
\qquad
 g(0)=g(\ell)=0,
$$

and

$$
g'(t)=\frac\ell2-t.
$$

For any absolutely continuous `y` with zero endpoint values, integration by parts gives

$$
\int_0^\ell y(t)\,dt
=\int_0^\ell y'(t)g'(t)\,dt.
\tag{DD.7}
$$

Cauchy–Schwarz therefore yields

$$
\left|\int_0^\ell y\right|^2
\le
\left(\int_0^\ell y'^2\right)
\left(\int_0^\ell g'^2\right).
\tag{DD.8}
$$

A direct calculation gives

$$
\int_0^\ell g'(t)^2\,dt
=
\int_0^\ell\left(\frac\ell2-t\right)^2dt
=\frac{\ell^3}{12}.
\tag{DD.9}
$$

Hence

$$
\boxed{
\left|\int_0^\ell y(t)\,dt\right|
\le
\sqrt{\frac{\ell^3}{12}
\int_0^\ell y'^2}.
}
\tag{DD.10}
$$

This is the sharp `H_0^1` dual norm of the mean functional.

---

## 4. Area is at most mean transverse height

Orient the pocket boundary by traversing the upper contact chain from `A` to `B` and then the horizontal chord from `B` back to `A`.  This orientation is clockwise.  Green's theorem gives

$$
area(P)
=\int_0^\ell y(t)x'(t)\,dt,
\tag{DD.11}
$$

because the closing chord has `y=0`.

Pointwise,

$$
y(t)\ge0,
\qquad
x'(t)\le1.
$$

Therefore

$$
\boxed{
area(P)
\le
\int_0^\ell y(t)\,dt.
}
\tag{DD.12}
$$

No monotonicity of `x(t)` is assumed.  Portions with `x'<0` only decrease the integral in DD.11 relative to the mean-height upper bound.

Combine DD.5, DD.10, and DD.12:

$$
\begin{aligned}
area(P)
&\le
\sqrt{\frac{\ell^3}{12}
\,2(\ell-s)}\\
&=
\boxed{
\frac1{\sqrt6}\ell^{3/2}\sqrt{\ell-s}
}.
\end{aligned}
$$

This proves DD.1.

---

## 5. Sum over all outer pockets

OD proves the exact global identities

$$
\sum_P\ell_P=x_B+a,
\qquad
\sum_P(\ell_P-s_P)=b-P_F.
\tag{DD.13}
$$

Applying DD.1 pocketwise and Cauchy–Schwarz as in OD gives

### Theorem DD.2 — global Dirichlet-dual detour bound

$$
\boxed{
H_{out}
\le
\frac1{\sqrt6}
(x_B+a)^{3/2}
\sqrt{b-P_F}.
}
\tag{DD.14}
$$

Using the exact PC variables,

$$
\boxed{
H_{out}
\le
\frac1{\sqrt6}
\bigl(2h-Q-2s_Z-e_{BB}+c_B\bigr)^{3/2}
\sqrt{2h-Q-2s_Z-P_F}.
}
\tag{DD.15}
$$

This strictly supersedes WD.11/WD.12.

---

## 6. Consequences

All OD/WD qualitative stability consequences remain valid with the improved constant. In particular, if

$$
H_{out}\ge\gamma D^2
$$

and

$$
x_B+a\le LD,
$$

then DD.14 gives

$$
\boxed{
\frac{b-P_F}{D}
\ge
\frac{6\gamma^2}{L^3}.
}
\tag{DD.16}
$$

Thus any quadratic outer cavity pays a quantitatively larger minimum linear detour than previously certified by WD.

---

## 7. Why the new constant is natural

For a nearly straight chain, write its small transverse displacement as `y(t)`. To leading order,

$$
\ell-s\sim\frac12\int y'^2,
$$

while the enclosed area is approximately

$$
\int y.
$$

The extremizer of the linear functional `integral y` at fixed Dirichlet energy solves

$$
-y''=\text{constant},
$$

so the leading profile is parabolic and the dual norm is exactly `ell^3/12`. This is why the coefficient `1/sqrt(6)` appears.

DD does not claim that an exact finite polygonal pocket attains equality; several inequalities in the derivation can be strict.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| transverse-energy bound DD.5 | proved | arclength identity + chord deficit |
| mean-height dual bound DD.10 | proved | explicit Dirichlet test function |
| area <= mean height DD.12 | proved | convex one-sided pocket + `x'<=1` |
| one-pocket DD.1 | proved | DD.5 + DD.10 + DD.12 |
| global DD.14 | proved | OD exact sums + Cauchy |
| optimal exact finite-pocket constant | not claimed | DD is sufficient, not an extremal classification |
| Level I | still open | high-surplus branch remains |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For one convex OP pocket, put the hull chord on the x-axis and arclength-parameterize
the old contact chain gamma=(x,y), 0<=t<=ell. Then y>=0,
    x'^2+y'^2=1,
    integral x'=s,
so
    integral y'^2 <= 2(ell-s).

Let g=t(ell-t)/2. Since -g''=1 and y vanishes at the endpoints,
    integral y = integral y'g',
and
    integral g'^2=ell^3/12.
Hence
    integral y <= sqrt[(ell^3/12) integral y'^2].
Green gives area(P)=integral y x', and y>=0, x'<=1 imply
    area(P)<=integral y.
Therefore
    area(P)<=ell^(3/2)sqrt((ell-s)/6).
Summing gives
    H_out <= (1/sqrt6)(x_B+a)^(3/2)sqrt(b-per(F)).
```
