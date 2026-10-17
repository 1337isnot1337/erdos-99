> Generated reading edition · [exact source](../../../docs/reports/target_c_typeii_section146_density_consequence_2026-09-12.md) · source SHA-256 `015724959a0c113157bbaaaf31d627efb1e3f843540555ad31930c61df79e25c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E73A2FDE6868","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Type-II consequence of the audited §146 density chain

**Date:** 2026-09-12
**Classification:** unreviewed candidate; noncanonical
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note derives a scalar consequence of the audited-working §§142--146 route
module. The route module is not canonical, so this note is not a promotion of
theorem state.

Let

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
C_{146}:={4\over9}\left(\pi+\sqrt{\Delta_2}\right)
=1.8195135379794445\ldots .
```

Write

```math
t={q-k\over D},\qquad
d={d_H\over D},\qquad
s={s_Z\over D},\qquad
y={h\over D},\qquad
\kappa={k\over D}=d+s,\qquad
f={\#\{\text{bounded nonquadrilateral faces}\}\over D}.
```

The exact identities $`q=h+d_H`$ and $`k=d_H+s_Z`$ give

```math
{q-k\over D}=y-s.
\tag{146C.1}
```

## 1. Loaded-density floor inherited from §146

Audited-working §146.5 states

```math
\liminf_{D\to\infty}
\left(y-{d\over9}-{10s\over9}\right)
\ge C_{146}.
\tag{146C.2}
```

Using (146C.1),

```math
t
=\left(y-{d\over9}-{10s\over9}\right)
  +{d\over9}+{s\over9}.
```

All displayed defect densities are nonnegative. Therefore the route-local candidate
is

```math
\boxed{\liminf_{D\to\infty}{q-k\over D}\ge C_{146}
=1.8195135379794445\ldots .}
\tag{146C.3}
```

More exactly, $`d+s=\kappa`$, so (146C.2) is the joint tradeoff

```math
\boxed{\liminf_{D\to\infty}\left(t-{\kappa\over9}\right)
\ge C_{146}.}
\tag{146C.3a}
```

Since $`q/D=t+\kappa\le\pi+o(1)`$, any sequence saturating the lower $`t`$-window
has

```math
\limsup \kappa\le {9\over10}(\pi-C_{146})
=1.1898712040\ldots .
\tag{146C.3b}
```

This is stronger than the corrected canonical-input floor
$`2(\pi+\sqrt{\Delta_2})/5=1.6375621842\ldots`$, but it is not canonical because
§146 remains audited-working.

## 2. The accompanying face/interface tradeoff

Audited-working §146.2 gives

```math
f\ge\sqrt{\Delta_2}-{y\over4}+{d\over4}+{s\over2}.
\tag{146C.4}
```

Since $`y=t+s`$, this becomes

```math
\boxed{t+4f\ge4\sqrt{\Delta_2}+d+s.}
\tag{146C.5}
```

The outer-walk inequality in §146.4 is

```math
Q+2s\le2y-\pi,
```

so, after $`y=t+s`$,

```math
\boxed{Q\le2t-\pi.}
\tag{146C.6}
```

At the smallest density permitted by (146C.3), and with $`d=s=0`$, equations
(146C.5)--(146C.6) force the scalar window

```math
f\ge\sqrt{\Delta_2}-{C_{146}\over4}
=0.4974344224\ldots,
\qquad
Q\le2C_{146}-\pi
=0.4974344224\ldots .
```

Thus the formal low-$`t`$ endpoint carries a linear bounded-face/outer-walk
population. The equalities are only a scalar endpoint description; they do not
construct or exclude a source.

More generally, at the lower boundary $`t=C_{146}+\kappa/9`$, the two displayed
inequalities become

```math
f\ge\sqrt{\Delta_2}-{C_{146}\over4}+{2\kappa\over9},
\qquad
Q\le2C_{146}-\pi+{2\kappa\over9}.
```

The constants are equal, so $`f=Q`$ is forced at this scalar boundary. This is a
first-order saturation statement only; it does not identify the corresponding
faces or provide a global descent.

## 3. Interaction with augmented defect

The audited interface/augmented-defect dichotomy gives

```math
(q-k)+J_{\rm aug}\ge2\sqrt{R_4},
\qquad
{R_4\over D^2}\to\Delta_2.
```

Consequently, on any Type-II subsequence satisfying

```math
{q-k\over D}\le C_{146}+\varepsilon+o(1),
```

one has the conditional lower payment

```math
\boxed{
{J_{\rm aug}\over D}
\ge
2\sqrt{\Delta_2}-C_{146}-\varepsilon-o(1)
=0.0851120751\ldots-\varepsilon-o(1).
}
\tag{146C.7}
```

This does not contradict the scalar endpoint: the augmented defect can be linear.
It identifies the remaining branch as a coupled high-density/defect branch rather
than a free $`q-k`$ minimization.

## 4. Classification and exact gap

Equations (146C.3)--(146C.7) are unreviewed candidates obtained by algebra from
audited-working §§142--146 and the audited interface dichotomy. They do not imply a
unit equilateral triangle, a strict same-cardinality sub-$`D`$ competitor, or the
Level-I conclusion. A closing theorem must still exclude the scalar endpoint
with linear bounded-face/augmented-defect currency, or convert that currency into a
finite global diameter descent.
