> Generated reading edition · [exact source](../../../docs/reports/target_c_eppstein_zf_surplus_diameter_coupling_2026-09-11.md) · source SHA-256 `a95dc5ca9f177dc2e653ed8abe42f78f6c0d677ba9563d79675bb7442a4f8f04`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AB776F7EE86A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Eppstein–ZF surplus-to-diameter coupling

**Date:** 2026-09-11  
**Run type:** Target C C-II closing attempt / exact mixed-row coupling  
**Status:** unpromoted research report; route-map status unchanged

## LEVEL I STATUS

STILL OPEN.

This report proves a new exact coupling between the mixed-rigidity surplus $`s_Z`$
and the number $`h`$ of actual diameter pairs in the nonisolated contact core. It
uses the sharp triangle-free penny-graph edge deficit together with the exact ZF
identity; it does not interpret zero stress coordinates as weak geometric rows and
does not change the C-II representative.

The resulting inequality is

```math
h\ge s_Z+c_E\sqrt v-O(1),
\qquad c_E=\frac12\sqrt{2\pi\sqrt3},
\tag{EZ.1}
```

where $`v`$ is the actual nonisolated-core population. In particular, on any
subsequence with $`v/D^2\to\nu`$, $`s_Z/D\to\sigma`$, and
$`n/D^2\to\Delta_2=\pi/(2\sqrt3)`$,

```math
\liminf\frac hD\ge \sigma+c_E\sqrt\nu.
\tag{EZ.2}
```

If the contact-isolated population is subquadratic, then $`\nu=\Delta_2`$, and
the constant simplifies exactly:

```math
\boxed{\liminf\frac hD\ge\frac\pi2+\liminf\frac{s_Z}{D}.}
\tag{EZ.3}
```

This removes a possible low-diameter explanation of a positive $`s_Z`$ branch when
the positive core is population-spanning. It does **not** exclude the branch: the
known force-hull upper bound is only $`h/D\le\pi+o(1)`$, and the isolate-heavy
alternative remains available.

## 1. Exact finite inequality

Let $`G`$ be the connected nonisolated positive contact core of the C-II source.
Write

```math
v=|V(G)|,\qquad e=|E(G)|,\qquad h=|H|,
\qquad s_Z=e+h-(2v-2)\ge0.
\tag{1.1}
```

The graph $`G`$ is a connected triangle-free penny graph. Eppstein’s sharp
triangle-free penny-graph theorem gives

```math
e\le 2v-c_E\sqrt v+C_E,\qquad
c_E=\frac12\sqrt{2\pi\sqrt3},
\tag{1.2}
```

for an absolute constant $`C_E`$. The $`O(1)`$ form in the supplied theorem is
all that is needed; no equality classification is invoked.

### Theorem EZ — surplus-to-diameter coupling

Every C-II post-ZF source satisfying these hypotheses obeys

```math
\boxed{h\ge s_Z+c_E\sqrt v-(C_E+2).}
\tag{1.3}
```

### Proof

Rearrange the definition of $`s_Z`$:

```math
h=2v-2+s_Z-e.
```

Insert (1.2):

```math
\begin{aligned}
h
&\ge 2v-2+s_Z-(2v-c_E\sqrt v+C_E)\\
&=s_Z+c_E\sqrt v-(C_E+2).
\end{aligned}
```

This is (1.3). $`\square`$

The proof retains the exact $`s_Z`$ coefficient $`+1`$; dropping it would lose the
new coupling.

## 2. Normalized consequences

For a global minimum-diameter sequence, the planar lattice comparison gives

```math
\frac n{D^2}\longrightarrow
\Delta_2=\frac\pi{2\sqrt3}.
\tag{2.1}
```

Let $`v/D^2\to\nu`$ and $`s_Z/D\to\sigma`$ along a convergent subsequence. Divide
Theorem EZ by $`D`$. Since $`C_E+2=O(1)`$,

```math
\boxed{\liminf\frac hD\ge \sigma+c_E\sqrt\nu.}
\tag{2.2}
```

If the contact-isolated population $`z=n-v`$ is $`o(D^2)`$, then
$`\nu=\Delta_2`$. The coefficient is exact:

```math
\begin{aligned}
c_E\sqrt{\Delta_2}
&=\frac12\sqrt{2\pi\sqrt3}\sqrt{\frac\pi{2\sqrt3}}\\
&=\frac\pi2.
\end{aligned}
```

Therefore (2.3) follows:

```math
\boxed{\liminf\frac hD\ge\frac\pi2+\sigma.}
\tag{2.3}
```

This is stronger than the $`s_Z=0`$ Eppstein consequence $`h/D\ge\pi/2`$,
and unlike a stress-polytope support count it applies to the actual full contact
and diameter rows of the selected C-II source.

## 3. The finite upper tradeoff that follows

The loaded vertices are vertices of the force hull $`F`$, and every diameter pair
has both endpoints among them. Unit separation along the convex hull and Cauchy’s
diameter-perimeter inequality give

```math
q\le P_F+O(1)\le\pi D+O(1),\qquad h\le q,
\tag{3.1}
```

where $`q`$ is the number of loaded vertices. Combining this with (1.3) yields

```math
\boxed{s_Z+c_E\sqrt v\le\pi D+O(1).}
\tag{3.2}
```

In normalized form, $`\sigma+c_E\sqrt\nu\le\pi`$. This is a genuine upper
tradeoff, but it is not contradictory. In the population-spanning case it only
gives $`\sigma\le\pi/2`$, while the difference-body inequality allows $`s_Z/D`$
on that scale.

## 4. Interaction with the mandatory C-II branches

The exact diameter-topology relation is $`q=h+d_H`$, so (1.3) also implies

```math
q\ge d_H+s_Z+c_E\sqrt v-O(1).
\tag{4.1}
```

Consequently, in a population-spanning subsequence,

```math
\frac qD\ge\frac\pi2+\frac{d_H+s_Z}{D}-o(1).
\tag{4.2}
```

For the three required branches:

* In the cyclic $`s_Z=0`$ branch this gives $`h=q\ge(\pi/2-o(1))D`$
  when the core is population-spanning. It does not improve the known cyclic
  currency floor $`(e_{BB}+2s_C)/D\ge\lambda_A+\varepsilon_A`$ to a
  contradiction, because no upper bound below $`D`$ for that currency is known.
  The regular odd-shell regression has $`h=q\sim\pi D`$ and is compatible.

* In the forest $`s_Z=0`$ branch it gives
  $`q/D\ge\pi/2+d_H/D-o(1)`$ when the core is population-spanning. The inherited
  forest lower bound for $`(e_{BB}+2s_C)/D`$ still has no opposing hub-block
  upper tradeoff.

* If $`s_Z/D\to\sigma>0`$ and the contact-isolated population is subquadratic,
  then
  ```math
  q/D\ge\pi/2+\sigma+d_H/D-o(1).
  \tag{4.3}
  
  ```
  This rules out interpreting a linear $`s_Z`$ as a purely sparse-diameter
  phenomenon. It does not authorize a release: a row omitted by an extreme
  stress may remain strong under the relative-interior stress.

## 5. Conditional cyclic population consequence

The cyclic annular-rate report supplies, subject to its listed cyclic detour and
central-symmetral-transfer inputs, the report-level estimate

```math
z\le C D^{7/4}+C(K_D+1)D,
\tag{5.1}
```

where $`z=n-v`$ is the contact-isolated population and $`K_D`$ is the largest
bounded exceptional-face perimeter. A local full-source audit has identified a
containment gap in one supplied detour proof, so (5.1) is not promoted here.

If $`K_D=o(D)`$, (5.1) gives $`z=o(D^2)`$, and Theorem EZ yields
```math
h/D\ge\pi/2-o(1)
```
in the cyclic branch. Conversely, if $`h/D\le\pi/2-\eta`$ along a subsequence,
the same inequalities force a positive quadratic core deficit whenever the
population estimate is available; (5.1) then forces
```math
K_D=\Omega_\eta(D).
\tag{5.2}
```

Thus this combined, explicitly conditional reduction leaves a linear-perimeter
exceptional face as the only escape from the population-spanning
$`h\ge\pi D/2`$ regime. The giant-face branch is not excluded.

## 6. Why the coupling does not settle the problem

To close C-II from Theorem EZ one would still need one of:

1. a source-specific upper bound forcing $`h/D<\pi/2+\sigma-o(1)`$ in the
   population-spanning $`s_Z>0`$ branch;
2. a response or finite-motion theorem converting the resulting large diameter
   support into a strict sub-$`D`$ competitor; or
3. a global exclusion of $`z=\Theta(D^2)`$, including the single exceptional face
   allowed by the cyclic report-level reduction.

None follows from Cauchy’s perimeter bound, the Woodall classification, the C53
PSD identities, or the exact ZF ledger. In particular, regular odd shells have
$`s_Z=2`$, not $`s_Z=0`$, and remain a regression against any attempt to turn
positive $`s_Z`$ alone into a release.

## 7. Regression and provenance audit

- Contact-isolated points are retained in $`z=n-v`$; no isolate is declared a
  diameter endpoint.
- The cyclic/forest relation $`q=h+d_H`$ is used only as stated.
- Regular odd shells, exceptional faces, common 2-connected hubs, and high pinned
  surplus are not discarded.
- No zero-multiplier-to-release implication is used.
- The only external mathematical input beyond the promoted stack is Eppstein’s
  published triangle-free penny-graph edge bound, already recorded in
  docs/problem/literature_baseline.md. The ZF identity retains its report-level
  dependency status.

## 8. Handoff

The proved new statement is (EZ.1), with normalized consequences (EZ.2)--(EZ.3).
It converts mixed-rigidity surplus directly into diameter-edge demand while
retaining all contact-isolated source points. The exact surviving obstruction is
the three-way alternative:

```math
\text{population-spanning core with }h\ge\pi D/2,\quad
\text{isolate-heavy core},\quad
\text{or a giant exceptional face in the cyclic reduction}.
```

No complete proof or disproof of Erdős Problem #99 follows.
