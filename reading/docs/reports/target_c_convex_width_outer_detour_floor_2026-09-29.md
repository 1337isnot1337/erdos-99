> Generated reading edition · [exact source](../../../docs/reports/target_c_convex_width_outer_detour_floor_2026-09-29.md) · source SHA-256 `19e3a7081039aece805716cb9e66a4e0f7bafbc44250b529fbe1536d5f492278`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7071E9C9A3DD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — convex-width outer-detour floor

**Date:** 2026-09-29  
**Base main:** \`ab14e4e418c71cebf113517ccb91ec334d069fe4\`  
**Status:** proof-only current-main composition; theorem-state authority unchanged  
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

## 1. Result

On the current canonical full-core Type-II branch, write
```math
S_{\rm out}:=\sum_r(L_r-2d_r),\qquad
S_D:=\sum_r d_r,\qquad
X_D:=q-k-S_D,
```
with $`d_r=\operatorname{diam}P_r`$, $`P_r=\operatorname{conv}(A_r)`$, and
$`k=d_H+s_Z`$. Current main proves
```math
0\le S_{\rm out}
\le 2X_D+4c_I-4-Q_{\rm loc}.
\tag{1.1}
```

The new conclusion is
```math
\boxed{\liminf_{D\to\infty} S_{\rm out}/D
\ge 0.1810260594\ldots}
\tag{1.2}
```
and hence
```math
\boxed{\liminf_{D\to\infty} X_D/D
\ge 0.0905130297\ldots .}
\tag{1.3}
```

This more than doubles the previously recorded strict aggregate-moment gap
$`\pi(2-\sqrt3)/20=0.0420893607\ldots`$.  More importantly, it forces a
positive linear amount of genuine outer-walk detour rather than only a positive
gap in $`q-k-S_D`$.

## 2. Convex width lemma

Let $`K`$ be a planar compact convex body with diameter $`d>0`$, area $`A`$,
and perimeter $`p`$. Then
```math
\boxed{p\ge2\sqrt{d^2+(A/d)^2}.}
\tag{2.1}
```

Choose a diameter pair and place it at $`a=(0,0)`$, $`b=(d,0)`$.  Every point
of $`K`$ has first coordinate in $`[0,d]`$; otherwise it would be farther than
$`d`$ from one of $`a,b`$.

Let $`h_+`$ and $`h_-`$ be the maximal distances of $`K`$ from the diameter
line in the two closed half-planes.  The two boundary arcs from $`a`$ to $`b`$
have lengths at least
```math
\sqrt{d^2+4h_+^2},\qquad \sqrt{d^2+4h_-^2}.
```
Indeed, an arc reaching height $`h`$ through $`(x,h)`$ has length at least
```math
\sqrt{x^2+h^2}+\sqrt{(d-x)^2+h^2}
\ge \sqrt{d^2+4h^2},
```
the last expression being minimized at $`x=d/2`$.

Since $`h\mapsto\sqrt{d^2+4h^2}`$ is convex,
```math
p\ge2\sqrt{d^2+(h_++h_-)^2}.
```
Also $`K\subset[0,d]\times[-h_-,h_+]`$, so $`A\le d(h_++h_-)`$. This proves
(2.1).

Put
```math
\rho:=\sqrt{1+\pi^2/16}.
```
Planar isodiametry gives $`A/d^2\le\pi/4`$. Therefore
```math
\begin{aligned}
p-2d
&\ge2d\left(\sqrt{1+(A/d^2)^2}-1\right)\\
&\ge \frac{2A^2}{(1+\rho)d^3}.
\end{aligned}
\tag{2.2}
```

## 3. Apply the lemma to harmonic cells

Write $`A_r:=\operatorname{area}(P_r)`$ and
$`p_r:=\operatorname{per}(P_r)`$. Harmonic trapping puts every unloaded
vertex of the induced component graph inside $`P_r`$, while the attachment
vertices contain all extreme vertices of $`P_r`$. Thus the convex hull of the
occurrence-counted outer-face walk is $`P_r`$. Any closed polygonal walk has
length at least the perimeter of its convex hull, so
```math
L_r\ge p_r.
\tag{3.1}
```

By (2.2),
```math
L_r-2d_r\ge
\frac{2A_r^2}{(1+\rho)d_r^3}.
```
Summing and applying Cauchy--Schwarz gives
```math
\boxed{
S_{\rm out}
\ge
\frac{2}{1+\rho}\,
\frac{\left(\sum_rA_r\right)^2}{\sum_rd_r^3}.
}
\tag{3.2}
```
Degenerate zero-area cells contribute zero and can be omitted.

Canonical full-core attachment-cell area saturation gives
```math
\sum_rA_r=\frac{\pi}{4}D^2-o(D^2).
\tag{3.3}
```

## 4. First bootstrap

From (1.1), $`S_{\rm out}\ge0`$, and $`c_I=o(D)`$,
```math
X_D\ge-o(D).
\tag{4.1}
```
Since $`q\le\operatorname{per}(F)\le\pi D`$ and $`k\ge0`$,
```math
S_D=q-k-X_D\le\pi D+o(D).
\tag{4.2}
```
Every $`d_r\le D`$, hence
```math
\sum_rd_r^3\le D^2S_D\le(\pi+o(1))D^3.
\tag{4.3}
```

Insert (3.3) and (4.3) into (3.2):
```math
S_{\rm out}/D
\ge \frac{\pi}{8(1+\rho)}-o(1).
\tag{4.4}
```
Define
```math
\beta:=\rho-1=\frac{\pi^2}{16(1+\rho)}.
```
Then (4.4) is $`S_{\rm out}/D\ge2\beta/\pi-o(1)`$.  Combining this with
(1.1) gives
```math
\boxed{
X_D/D\ge\beta/\pi-o(1)
=0.0864384104\ldots-o(1).
}
\tag{4.5}
```

## 5. Cubic-moment bootstrap

Put $`x_r=d_r/D`$. Then $`0\le x_r\le1`$, and (4.5) implies
```math
\sum_rx_r=S_D/D
\le \pi-\beta/\pi+o(1)
=3.0551542431\ldots+o(1).
\tag{5.1}
```

For numbers $`0\le x_i\le1`$ with total mass at most $`B\in[3,4)`$, convexity
of $`t^3`$ implies
```math
\sum_i x_i^3\le3+(B-3)^3.
\tag{5.2}
```
Indeed, transferring mass from a smaller fractional coordinate to a larger
one increases the cube sum until at most one fractional coordinate remains.

Define
```math
M_0:=
3+\left(\pi-3-\frac{\beta}{\pi}\right)^3
=3.0001677786\ldots .
\tag{5.3}
```
Then
```math
\sum_rd_r^3\le(M_0+o(1))D^3.
\tag{5.4}
```
Returning to (3.2),
```math
S_{\rm out}/D
\ge
\frac{\pi^2}{8(1+\rho)M_0}-o(1)
=
\frac{2\beta}{M_0}-o(1)
=
0.1810260594\ldots-o(1).
```
This proves (1.2).  Applying the upper bound (1.1) once more gives
```math
X_D/D\ge\frac{\beta}{M_0}-o(1)
=0.0905130297\ldots-o(1),
```
which proves (1.3).

The exact constant is
```math
\boxed{
\alpha_{\rm width}
=
\frac{\sqrt{1+\pi^2/16}-1}{
3+\left(
\pi-3-\frac{\sqrt{1+\pi^2/16}-1}{\pi}
\right)^3
}.
}
```

## 6. Remaining obstruction

The full-core branch now has the unconditional proof-only floor
```math
\liminf D^{-1}\sum_r(L_r-2d_r)\ge0.1810260594\ldots .
```
Thus the Section-122 aggregate demand cannot be hidden entirely in exceptional
faces.

This does not close C-II.  The current upper bound still permits this forced
detour whenever $`q-k-S_D`$ carries at least $`0.090513D`$.  A closing bridge
must therefore do one of the following:

1. upper-bound $`q-k-S_D`$ below $`0.090513D`$;
2. charge the forced $`0.181026D`$ outer detour to the actual diameter topology
   strongly enough to obtain a contradiction; or
3. convert that detour into a source-preserving strict diameter decrease or an
   exact unit equilateral triangle.

The macroscopic inactive-container branch is untouched.

## 7. Scope

- Remote \`main\` was rechecked before this report.
- No Section-122 lower bound is used to prove (1.2)--(1.3).
- Local exceptional-face quantities are not identified with global ones.
- Contact-isolated source points remain retained.
- No full-source extension of the core affine-kernel theorem is used.
- No rejected Euler-path, FB4, Reuleaux-cap, or Section-121 scaling inference is used.
- No numerical search or unexecuted verifier is load-bearing.
- The theorem-state manifest is unchanged.
