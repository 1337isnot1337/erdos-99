> Generated reading edition · [exact source](../../../docs/reports/target_c_exceptional_face_train_tradeoff_2026-09-11.md) · source SHA-256 `d94e0b1de558e029712c1c6953122d6b6b3ae0e7a83ca1a591ea0d2606ce3f15`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-3369D12EA14A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exceptional-face area cannot share the train bonus

**Date:** 2026-09-11  
**Run type:** exact all-branch face-capacity refinement  
**Target:** Target C C-II, post-ZF  
**Status:** unpromoted research report

## LEVEL I STATUS

STILL OPEN.

The full-source defect-floor calculation has two competing uses of the exceptional
faces. If $`f`$ is the number of exceptional faces and $`Q`$ is their total degree
defect, then $`f\le Q`$. The stopped-train count gains $`2f`$, while the
isoperimetric area allowance is largest when the defect is concentrated in one face,
which makes $`f=o(D)`$. The earlier bound used both $`2Q`$ and $`Q^2/(4\pi)`$
simultaneously, although those endpoint regimes are incompatible.

Retaining the exact tradeoff gives the stronger conditional all-branch statement

```math
 \boxed{
 \liminf_{D\to\infty}\frac{x_B+Q}{D}
 \ge \varepsilon_{\rm ef}=0.0651358704\ldots .}
\tag{EF.1}
```

The improvement is small and does not settle the linear-defect regime. Its value is
that it removes one artificial scalar escape and leaves a concrete unresolved
alternative: a giant exceptional face versus a macroscopic population of
face-terminated trains.

The proof uses only the report-level FSDB and FSCS bounds, the full-source outer-pocket
estimate, and elementary facewise isoperimetry. It applies to cyclic, forest, and
$`s_Z>0`$ branches and retains contact-isolated source points.

## 1. Facewise tradeoff

Use the notation of the all-ZF cell-slack calculation:

```math
 X=\frac{x_B}{D},\quad Y=\frac QD,\quad r=X+Y,\quad
 k=\frac{d_H+s_Z}{D},\quad F=\frac fD.
```

The exact identities are

```math
 \frac qD=r+2k,\qquad
 \frac hD=r+\frac{d_H}{D}+2\frac{s_Z}{D}\ge r+k,
\tag{EF.2}
```

```math
 \frac TD= r+k+2F+o(1),
\tag{EF.3}
```

where the harmless $`o(1)`$ permits integer rounding. Since
$`q\le\operatorname{per}F\le\pi D`$,

```math
 0\le r\le\pi,\qquad 0\le k\le\frac{\pi-r}{2},\qquad 0\le F\le Y.
\tag{EF.4}
```

Let the exceptional faces have degrees $`m_i\ge5`$ and defects
$`q_i=m_i-4\ge1`$, so $`\sum_iq_i=Q`$. Each face is a convex equilateral
polygon with perimeter $`m_i`$, hence

```math
 A_i\le\frac{m_i^2}{4\pi}=\frac{(q_i+4)^2}{4\pi}.
\tag{EF.5}
```

For fixed $`Q`$ and $`f`$, convexity of $`u\mapsto(u+4)^2`$ gives

```math
 \sum_i(q_i+4)^2
 \le (Q-f+5)^2+25(f-1)
 = (Q-f)^2+O(Q+f).
\tag{EF.6}
```

The error is uniform because $`Q\le\pi D`$. Therefore, after division by $`D^2`$,

```math
 \limsup\frac{A_{\rm exc}}{D^2}
 \le\frac{(Y-F)^2}{4\pi}.
\tag{EF.7}
```

Mantel applied to the stopped-train crossing graph and FSCS give

```math
 \limsup\frac{A_{\rm quad}}{D^2}
 \le\frac{a_0}{4}(r+k+2F)^2,
 \qquad a_0=\frac{\sqrt3}{2}.
\tag{EF.8}
```

The full-source pocket estimate is
$`\limsup A_{\rm out}/D^2\le9X^2/\pi`$. Thus

```math
 A_F/D^2\le
 V(k,X,Y,F):=
 \frac{a_0}{4}(r+k+2F)^2+
 \frac{9X^2}{\pi}+\frac{(Y-F)^2}{4\pi}.
\tag{EF.9}
```

FSDB supplies

```math
 A_F/D^2\ge\Phi(y),\qquad
 \Phi(y)=\frac{y+\sin y}{4},
 \qquad y=h/D.
\tag{EF.10}
```

## 2. Eliminate $`k`$

For fixed $`r,X,Y,F`$, compare the right side of (EF.9) with
$`\Phi(\max\{2\rho,r+k\})`$, where $`\rho=\cos\rho`$. Before $`r+k`$ reaches
$`2\rho`$, the lower term is constant. After that point its derivative is at most
$`(1+\cos(2\rho))/4<1/2`$, while the derivative of the quadrilateral term is at
least

```math
 \frac{a_0}{2}(r+k+2F)\ge a_0\rho>\frac12.
```

Hence the difference is increasing in $`k`$, and feasibility at the actual $`k`$
implies feasibility at $`k_{\max}=(\pi-r)/2`$. Put

```math
 z=r+k_{\max}=\frac{\pi+r}{2}.
\tag{EF.11}
```

Since $`z\ge\pi/2>2\rho`$, every survivor must satisfy

```math
 L(r):=\frac{z+\sin z}{4}
 \le
 \frac{a_0}{4}(z+2F)^2+
 \frac{9X^2}{\pi}+\frac{(Y-F)^2}{4\pi}.
\tag{EF.12}
```

## 3. Optimize the face split

For fixed $`r`$ and $`X`$, the right side of (EF.12) is a convex quadratic in
$`F\in[0,Y]`$, so its maximum is at $`F=0`$ or $`F=Y`$. For each of those
choices it is convex in $`X\in[0,r]`$, so the maximum occurs at one of the four
corners:

```math
 A_0=\frac{a_0z^2}{4}+\frac{r^2}{4\pi},\qquad
 B_0=\frac{a_0(z+2r)^2}{4},
```

```math
 A_1=B_1=\frac{a_0z^2}{4}+\frac{9r^2}{\pi}.
\tag{EF.13}
```

For $`0\le r\le1/10`$, $`B_0`$ dominates the other three. Indeed,

```math
 B_0-A_0=a_0(zr+r^2)-\frac{r^2}{4\pi}>0,
```

and

```math
 B_0-A_1=r\left(a_0z+(a_0-9/\pi)r\right)>0,
```

using $`a_0\pi/2>1`$ and $`a_0-9/\pi>-2`$. Consequently the necessary inequality
reduces, for $`r\le1/10`$, to

```math
 L(r)\le U_{\rm ef}(r):=
 \frac{\sqrt3}{8}\left(\frac{\pi+r}{2}+2r\right)^2.
\tag{EF.14}
```

The function $`U_{\rm ef}-L`$ is strictly increasing on $`[0,1/10]`$: its
derivative is at least $`5a_0\pi/8>1`$, while
$`L'(r)\le1/8`$. At $`r=0`$,

```math
 U_{\rm ef}(0)=\frac{\sqrt3\pi^2}{32}
 <\frac{\pi/2+1}{4}=L(0),
```

whereas $`U_{\rm ef}(1/10)>L(1/10)`$ by the elementary bounds
$`3.14<\pi<22/7`$, $`0.866<\sqrt3/2`$, and $`\sin(1.62)>0.998`$.
There is therefore a unique root

```math
 U_{\rm ef}(\varepsilon_{\rm ef})=L(\varepsilon_{\rm ef}),
 \qquad
 \varepsilon_{\rm ef}=0.0651358704640\ldots .
\tag{EF.15}
```

If $`r<\varepsilon_{\rm ef}`$, (EF.12)--(EF.14) contradict FSDB. Unbounded $`r`$
is harmless, so (EF.1) follows.

## 4. Exact residual obstruction

The optimizing corner $`B_0`$ has

```math
 X=0,\qquad F=Y,
```

up to subsequences. It is the many-small-exceptional-face regime: the quadratic
exceptional-face area is only $`o(D^2)`$, while the $`2f`$ train bonus is maximal.
The opposite corner $`A_0`$ is the giant-face regime: it retains $`Q^2/(4\pi)`$
area but loses the linear train bonus. The theorem proves that the former is the
only endpoint relevant to the new floor near $`0.0651D`$; it does not exclude it.

The unresolved C-II alternatives remain $`x_B+Q=\Theta(D)`$, the cyclic and forest
$`s_Z=0`$ branches, $`s_Z>0`$, and contact-isolated populations. A closing theorem
must still charge the boundary of the exceptional-face region or produce a strict
sub-$`D`$ competitor. No such implication is claimed here.
