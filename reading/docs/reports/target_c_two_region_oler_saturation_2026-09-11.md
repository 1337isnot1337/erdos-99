> Generated reading edition · [exact source](../../../docs/reports/target_c_two_region_oler_saturation_2026-09-11.md) · source SHA-256 `1c5ee42a27b4ff7ed3b3ab357c8669afeacce4352d9b6dd3f06c184d04ca511c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-8415CECD6611","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — two-region source saturation in C-II

**Date:** 2026-09-11

**Target:** Target C, C-II

**Status:** new proved report; unpromoted

**Dependencies:** the sharp annular source ledger,
the strict translated-lattice comparison, Oler's finite packing inequality, and
the convex perimeter-diameter bound

## Statement

Let $`A`$ be the contact-minimal, diameter-pair-minimal C-II representative,
$`D=\operatorname{diam}A`$, $`K=\operatorname{conv}A`$, and
$`F=\operatorname{conv}B`$, where $`B`$ is the loaded force-hull vertex set. Put

```math
N=|A\cap F|,\qquad Z=|A\setminus F|,
\qquad a_0=\frac{\sqrt3}{2},\qquad c_0=\frac{\sqrt3}{4},
```

```math
\delta_K=\frac{\pi D^2}{4}-\operatorname{area}K,\qquad
\delta_F=\frac{\pi D^2}{4}-\operatorname{area}F,
```

and $`P_K=\operatorname{per}K`$, $`P_F=\operatorname{per}F`$. Assume that $`F`$
has nonempty interior. Then

```math
\boxed{
-c_0(P_K+P_F)
<
a_0N-\operatorname{area}F
\le c_0P_F+a_0.
}
\tag{TRS.1}
```

Moreover,

```math
\boxed{
\delta_F-c_0P_F
<
a_0Z
\le
\delta_F-\delta_K+c_0(P_K+P_F)+a_0-a_0q,
}
\tag{TRS.2}
```

where $`q=|B|`$. In particular,

```math
\boxed{\delta_K<c_0P_K\le c_0\pi D.}
\tag{TRS.3}
```

Both source regions are saturated to boundary order:

```math
\boxed{
a_0N=\operatorname{area}F+O(D),\qquad
a_0Z=\delta_F+O(D).
}
\tag{TRS.4}
```

The constants in the $`O(D)`$ terms are absolute. These conclusions retain every
contact-isolated source point and do not use cyclic, forest, or $`s_Z=0`$ identities.

## Proof

The strict translated-lattice comparison for a global minimum-diameter source is

```math
a_0|A|>\frac{\pi D^2}{4}+a_0.
\tag{TRS.5}
```

The full-source Oler inequality on the convex hull $`K`$ is

```math
a_0|A|\le\operatorname{area}K+c_0P_K+a_0.
\tag{TRS.6}
```

Subtracting (TRS.5) from (TRS.6), and using
$`\operatorname{area}K=\pi D^2/4-\delta_K`$, gives

```math
\delta_K<c_0P_K,
```

which is (TRS.3).

The sharp annular source ledger gives

```math
a_0(Z+q)
\le
\operatorname{area}K-\operatorname{area}F
+c_0(P_K+P_F)+a_0.
\tag{TRS.7}
```

Since $`N+Z=|A|`$, subtracting (TRS.7) from (TRS.5) gives

```math
a_0(N-q)>
\operatorname{area}F+\delta_K-c_0(P_K+P_F).
\tag{TRS.8}
```

Oler applied to all source points in $`F`$, including contact-isolated points, gives

```math
a_0N\le\operatorname{area}F+c_0P_F+a_0.
\tag{TRS.9}
```

Subtracting $`\operatorname{area}F`$ from (TRS.9) gives the upper bound in (TRS.1).
Adding $`a_0q`$ to (TRS.8) and using $`q\ge0`$, $`\delta_K\ge0`$, and
$`P_K,P_F\le\pi D`$ gives the lower bound in (TRS.1).

For the exterior population, the lower bound follows directly from (TRS.5) and
(TRS.9):

```math
\begin{aligned}
a_0Z
&=a_0|A|-a_0N\\
&>\frac{\pi D^2}{4}+a_0
 -\bigl(\operatorname{area}F+c_0P_F+a_0\bigr)\\
&=\delta_F-c_0P_F.
\end{aligned}
\tag{TRS.10}
```

The upper bound follows by rearranging (TRS.7):

```math
a_0Z
\le
\delta_F-\delta_K+c_0(P_K+P_F)+a_0-a_0q.
\tag{TRS.11}
```

Equations (TRS.10)--(TRS.11) prove (TRS.2). Since both perimeters are at most
$`\pi D`$, (TRS.1)--(TRS.2) imply (TRS.4).
$`\square`$

## Consequences

If $`\operatorname{area}F/D^2\to a>0`$, then

```math
\frac{N}{D^2}-\frac{\operatorname{area}F}{a_0D^2}\to0.
```

Thus the source set inside the force hull is Oler-saturated at the
triangular-lattice density. This is a statement about all source points, not
about the positive contact core.

If $`\delta_F=o(D^2)`$, then (TRS.2) gives

```math
Z=o(D^2).
\tag{TRS.12}
```

This recovers the subquadratic external population in the near-$`\pi`$ force-hull
perimeter regime, but the exact two-sided formula also shows what is missing away
from that regime: the external population can be as large as the disk area deficit
$`\delta_F/a_0`$, up to only $`O(D)`$.

If the unpromoted C67 force-hull floor is additionally assumed, then
```math
\liminf\frac{\operatorname{area}F}{D^2}\ge
\frac{2\rho+\sin(2\rho)}4
=0.6184708847\ldots,\qquad \rho=\cos\rho,
```
and the annular ledger gives conditionally
```math
N-q\ge0.7141486636\ldots D^2-O(D).
```
This does not identify those points as contact-core vertices.

## Exact failed closure

The theorem reduces the full-source problem to a boundary-order error. It does not
give a fixed density loss for triangle-free or contact-isolated points. A strict
oblique lattice with angle $`\pi/3+D^{-2}`$ has no unit equilateral triangle and
has only $`O(1)`$ bulk cell excess over the triangular lattice, while its finite
boundary loss is $`O(D)`$. Therefore the $`O(D)`$ terms in (TRS.1)--(TRS.4) cannot
be discarded by a generic packing argument.

The remaining global step must use one of the facts absent from this theorem:

1. a source-preserving strict sub-$`D`$ competitor;
2. a quantitative response inequality for the common 2-connected contact block;
3. a cyclic endpoint gap crossing the value $`1`$; or
4. a forest/$`s_Z>0`$ upper tradeoff that pays the linear defect currency.

No such implication is currently proved. The cyclic, forest, and positive-surplus
branches all survive this saturation theorem.

## Provenance

The annular inequality is proved by applying the finite simplicial-packing
inequality of Graham–Witsenhausen–Zassenhaus, Theorem 4, to a straight-line
triangulation of $`K\setminus\operatorname{int}F`$ whose edge endpoints are source
points. The primary source is
<https://msp.org/pjm/1972/41-3/pjm-v41-n3-p10-p.pdf>.

This report is not a route-map promotion and does not change the Level I status.
