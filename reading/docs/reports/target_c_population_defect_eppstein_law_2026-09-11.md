> Generated reading edition · [exact source](../../../docs/reports/target_c_population_defect_eppstein_law_2026-09-11.md) · source SHA-256 `a430743e11fb67af12e7d8af13bbd7a3ba13c10c73cd74694b9b4a963da58d5d`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DB3969E7B608","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — population-defect law for the post-ZF C-II source

**Date:** 2026-09-11  
**Run type:** Target C C-II closing attempt / contact-isolated population coupling  
**Status:** unpromoted research report; route-map status unchanged

## LEVEL I STATUS

`STILL OPEN`.

This report proves a new all-branch quantitative dichotomy.  It couples the
exact post-ZF defect variables to the number of contact-isolated source points;
it does not delete those points or assume that they are diameter endpoints.

Let

```math
 z=n-v
```

be the number of contact-isolated source points, and put

```math
 R:=x_B+Q+d_H+s_Z.
```

For every sequence of post-ZF C-II representatives with $`D\to\infty`$, every
subsequence on which $`z/n\to\zeta\in[0,1]`$ satisfies

```math
\boxed{\displaystyle
 \liminf\frac{R}{D}\ge \frac{\pi}{2}\sqrt{1-\zeta}.}
\tag{PD.1}
```

In particular, population-spanning contact cores obey

```math
 z=o(n)\quad\Longrightarrow\quad
 \liminf\frac{x_B+Q+d_H+s_Z}{D}\ge\frac\pi2.
\tag{PD.2}
```

Equivalently, for every fixed $`0<\eta<\pi/2`$, if

```math
 x_B+Q+d_H+s_Z\le(\pi/2-\eta)D
```

along an infinite subsequence, then along that subsequence

```math
\boxed{\displaystyle
 z\ge \Delta_2\left(\frac{4\eta}{\pi}-\frac{4\eta^2}{\pi^2}\right)D^2-o(D^2),
 \qquad \Delta_2=\frac{\pi}{2\sqrt3}.}
\tag{PD.3}
```

Thus a low total ZF/diameter defect is possible only with a positive-density
population outside the nonisolated contact core.  This is a genuine new
population-versus-boundary alternative, but it does not rule out the
isolate-heavy branch and hence does not settle Erdős Problem #99.

## 1. Hypotheses and exact identities

Use the C-II representative selected first by minimum contacts and then by
minimum diameter-pair count, with all source points retained.  Let $`G`$ be the
connected nonisolated positive contact core, with

```math
 v=|V(G)|,\qquad e=|E(G)|,
```

and let $`h=|H|`$, $`q`$ be the number of loaded vertices,
$`d_H=q-h`$ the diameter-forest defect, and $`s_Z\ge0`$ the ZF circuit
surplus.  The exact post-ZF incidence identities are

```math
 q=x_B+Q+2(d_H+s_Z),
 \tag{PD.4}
```

and

```math
 h=q-d_H.
 \tag{PD.5}
```

Combining them gives

```math
 h=x_B+Q+d_H+2s_Z,
 \qquad
 R=h-s_Z.
 \tag{PD.6}
```

The second equality is the point at which the positive-surplus branch is
retained exactly; no $`s_Z=0`$ identity is being extended to that branch.

## 2. Eppstein lower bound for the actual core

The connected triangle-free penny graph $`G`$ obeys the supplied Eppstein
edge bound

```math
 e\le 2v-c_E\sqrt v+C_E,
 \qquad c_E=\frac12\sqrt{2\pi\sqrt3},
 \tag{PD.7}
```

for an absolute constant $`C_E`$.  By definition of the ZF surplus,

```math
 s_Z=e+h-(2v-2),
```

so

```math
 h=2v-2+s_Z-e
 \ge s_Z+c_E\sqrt v-(C_E+2).
 \tag{PD.8}
```

Subtracting $`s_Z`$ and using (PD.6) yields the finite inequality

```math
\boxed{\displaystyle
 R=x_B+Q+d_H+s_Z\ge c_E\sqrt v-(C_E+2).}
\tag{PD.9}
```

This is valid in the cyclic branch $`(d_H=0)`$, the forest branch
$`(d_H>0)`$, and the positive-surplus branch $`(s_Z>0)`$.  It also retains
the isolated population through the exact relation $`v=n-z`$.

## 3. Normalized population law

For global minimum-diameter sequences, the standard triangular-lattice
comparison gives

```math
 \frac n{D^2}\longrightarrow \Delta_2=\frac{\pi}{2\sqrt3}.
 \tag{PD.10}
```

Take a subsequence with $`z/n\to\zeta`$.  Then

```math
 \frac v{D^2}=\frac{n-z}{D^2}
 \longrightarrow \Delta_2(1-\zeta).
 \tag{PD.11}
```

Divide (PD.9) by $`D`$.  The additive constant vanishes, and

```math
\begin{aligned}
 \liminf\frac RD
 &\ge c_E\sqrt{\Delta_2(1-\zeta)}\\
 &=\left(c_E\sqrt{\Delta_2}\right)\sqrt{1-\zeta}\\
 &=\frac\pi2\sqrt{1-\zeta},
\end{aligned}
```

because

```math
 c_E\sqrt{\Delta_2}
 =\frac12\sqrt{2\pi\sqrt3}
  \sqrt{\frac\pi{2\sqrt3}}
 =\frac\pi2.
```

This proves (PD.1), and (PD.2) is its $`\zeta=0`$ case.

## 4. Explicit isolate-heavy alternative

Fix $`0<\eta<\pi/2`$, and suppose on a subsequence that

```math
 R/D\le\pi/2-\eta.
 \tag{PD.12}
```

From (PD.9),

```math
 c_E\frac{\sqrt v}{D}
 \le \frac\pi2-\eta+o(1).
 \tag{PD.13}
```

Squaring and using $`c_E^2\Delta_2=\pi^2/4`$ gives

```math
 \frac v{D^2}
 \le \Delta_2\left(1-\frac{2\eta}{\pi}\right)^2+o(1).
 \tag{PD.14}
```

Subtract this from (PD.10):

```math
\begin{aligned}
 \frac z{D^2}
 &=\frac n{D^2}-\frac v{D^2}\\
 &\ge \Delta_2\left[1-\left(1-\frac{2\eta}{\pi}\right)^2\right]-o(1)\\
 &=\Delta_2\left(\frac{4\eta}{\pi}-\frac{4\eta^2}{\pi^2}\right)-o(1).
\end{aligned}
```

This proves (PD.3).  The argument is finite-inequality based; it does not use
an asymptotic assumption about the exceptional faces, cyclic detours, or the
location of isolated points.

## 5. Branch and regression audit

* **Cyclic, $`s_Z=0`$:** (PD.9) reads $`x_B+Q+d_H\ge c_E\sqrt v-O(1)`$,
  and cyclicity sets $`d_H=0`$.  A population-spanning cyclic source must
  therefore have $`x_B+Q\ge(\pi/2-o(1))D`$.  The regular odd-shell regression
  remains compatible: it has a macroscopic isolated population, so (PD.3), not
  (PD.2), is the relevant alternative.

* **Forest, $`s_Z=0`$:** the result gives
  $`x_B+Q+d_H\ge(\pi/2-o(1))D`$ when the core is population-spanning.  It
  does not provide the missing upper bound coupling the forest-component charge
  $`3d_H`$ to the common bridge block.

* **Positive surplus, $`s_Z>0`$:** the exact term $`+s_Z`$ in $`R`$ is retained.
  The theorem rules out explaining linear surplus solely by a small diameter
  support when isolates are subquadratic, but it does not convert a zero stress
  coordinate into a releasable geometric motion.

* **Contact-isolated points:** they are counted in $`z=n-v`$, not silently
  removed from the source.  No claim is made that they lie on the force hull or
  carry diameter rows.

* **Common bridge block:** the common-block response obstruction is untouched.
  The theorem is a population/contact-core inequality and supplies no response
  sign for a multi-edge cut.

* **Exceptional faces and repeated outer-walk edges:** neither enters the proof.
  Consequently the argument cannot accidentally invoke the disputed cyclic
  cap-detour containment or a pure-disk transport through an exceptional face.

## 6. Exact obstruction after the new theorem

The theorem splits every putative C-II sequence into two possibilities.  Either

```math
 x_B+Q+d_H+s_Z\ge(\pi/2-o(1))D,
 \tag{PD.15}
```

or the nonisolated contact core loses a positive fraction of the full source
population.  The first alternative is not contradictory: the force-hull
perimeter bound permits $`q\le\pi D+O(1)`$, and the current cyclic/forest
surplus estimates supply no opposing upper bound below $`\pi D/2`$ for the
quantity in (PD.15).  The second alternative is precisely the isolate-heavy
branch that the force-bulk audit refuses to eliminate.

Closing the problem still requires at least one new theorem that either:

1. excludes positive-density contact-isolated sources in a global minimizer;
2. supplies an upper bound on $`x_B+Q+d_H+s_Z`$ below $`\pi D/2`$ in the
   population-spanning branch; or
3. turns the positive-density isolate alternative into a strict smaller-
   diameter competitor while preserving all unit separations.

None of those implications follows from (PD.1), C53/C63, Woodall topology, or
the existing circuit/area estimates.  Hence this is theorem-level progress, not
a settlement of the Level-I question.
