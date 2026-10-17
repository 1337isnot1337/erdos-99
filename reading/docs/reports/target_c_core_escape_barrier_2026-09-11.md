> Generated reading edition · [exact source](../../../docs/reports/target_c_core_escape_barrier_2026-09-11.md) · source SHA-256 `95c7062c20ef947b8671a15533825bcb45438418cdaa3de8d27d4d0a91dd9d50`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-998321132797","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — a finite escape barrier for the C-II contact core

**Date:** 2026-09-11  
**Repository commit:** `67f66ac` after refreshing from `origin/main` (starting checkout `c7a8615`)  
**State version:** `2026-09-11.audit.33`  
**Run type:** closing-proof attempt / scope audit  
**Target:** C-II  
**Classification:** proved candidate awaiting independent audit; noncanonical  
**Active prompt:** [current Target C prompt](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md)  
**External literature search:** not used  
**Mathematical computation:** not used

## LEVEL I STATUS

**STILL OPEN. C-II is not resolved by this report.**

## 1. Starting endpoint and proposed contradiction

The refreshed canonical frontier splits into a macroscopic inactive-container branch
and an asymptotic full-core, near-disk rhombic branch. A closing construction must retain
all source points and either force a triangle or give a unit-separated competitor of
diameter strictly below the actual `D`.

One proposed use of the inactive chamber is to close its many deep near-unit pairs,
then move the loaded core. This report checks that exact implication. Its conclusion
is an obstruction: arbitrary continuous feasible rearrangements of the isolates,
including contact activation, cannot unlock the original post-ZF core at diameter `D`.
The obstruction is uniform over the positions of the isolates for a fixed core; it
does not assert a uniform constant over different cores or growing `D`.

The underlying infinitesimal rigidity is already canonical. The new packaging here
is a finite quantitative escape inequality and its continuation through arbitrary
changes in the isolated-point contact graph. It is not a new rigidity proof or a
global-optimality certificate for the core.

## 2. General finite-core theorem

Let `P=(p_1,...,p_m)` be a labeled, noncollinear unit-separated planar configuration
of diameter `D>1`. Let `C` and `H` be its actual unit pairs and diameter pairs. Assume:

1. there is an equilibrium stress with `alpha_c>0` for every `c in C` and
   `beta_h>0` for every `h in H`, with `sum_H beta_h=1`;
2. the mixed bar rigidity matrix on `C union H` has rank `2m-3`.

No global optimality, density, circular-planar response, or triangle-free hypothesis
is required once these two assumptions have been supplied.

Use the Euclidean norm on the full `2m`-dimensional displacement space. Let `T` be the
three-dimensional space of translations and infinitesimal rotations of `P`, and put
`S=T^perp`. Define signed squared-length derivatives

```math
\phi_c(u)=2(p_i-p_j)\cdot(u_i-u_j),\qquad
\phi_h(u)=-2(p_i-p_j)\cdot(u_i-u_j).
```

Define the source-specific constant

```math
\kappa(P):=
\min_{\substack{u\in S\\\|u\|=1}}
\max_{e\in C\cup H}\{-\phi_e(u)\}.
\tag{EB.1}
```

For another labeled core configuration `X`, let

```math
r(X):=\inf_{g\in SE(2)}\|gX-P\|.
\tag{EB.2}
```

Here `SE(2)` consists of translations and rotations; no relabeling is allowed.

### Theorem EB — escape inequality

The constant `kappa(P)` is strictly positive. Every unit-separated `X` with

```math
0<r(X)<\kappa(P)/2
```

satisfies

```math
\boxed{\operatorname{diam}(X)^2\ge D^2+\kappa(P)r(X).}
\tag{EB.3}
```

In particular, every unit-separated `X` of diameter strictly below `D` must satisfy

```math
\boxed{r(X)\ge\kappa(P)/2.}
\tag{EB.4}
```

### Proof

Equilibrium gives the exact row dependence

```math
\sum_{c\in C}\alpha_c\phi_c(u)
+\sum_{h\in H}\beta_h\phi_h(u)=0.
\tag{EB.5}
```

If every signed derivative were nonnegative, strict positivity of all the
coefficients would force every derivative to vanish. The mixed rigidity rank then
makes `u` an infinitesimal Euclidean motion. No unit vector in `S` has that property.
Consequently the maximum in (EB.1) is positive at every point of the compact unit
sphere in `S`. Continuity proves `kappa(P)>0`, and homogeneity gives

```math
\max_e\{-\phi_e(u)\}\ge\kappa(P)\|u\|
\qquad(u\in S).
\tag{EB.6}
```

Choose a minimizing rigid alignment in (EB.2). Such a minimum exists: remove the
centroid difference first and minimize over the compact rotation group. Write the
aligned configuration as `P+u`. First-order optimality with respect to translations
gives `sum_i u_i=0`. First-order optimality with respect to rotation gives

```math
0=\sum_i u_i\cdot J(p_i+u_i)
=\sum_i u_i\cdot Jp_i,
```

because `u_i dot Ju_i=0`. Hence `u in S` and `||u||=r(X)`.

Set `tau=diam(X)^2-D^2`; initially `tau` may have either sign. For an original unit
pair, unit separation of `X` and the exact squared-length expansion give

```math
\phi_c(u)+|u_i-u_j|^2\ge0,
\qquad
-\phi_c(u)\le |u_i-u_j|^2\le2\|u\|^2.
\tag{EB.7}
```

For an original diameter pair, its new squared length is at most `D^2+tau`, giving

```math
-\phi_h(u)+|u_i-u_j|^2\le\tau,
\qquad
-\phi_h(u)\le\tau.
\tag{EB.8}
```

Combine (EB.6)--(EB.8):

```math
\kappa(P)r\le\max\{2r^2,\tau\}.
\tag{EB.9}
```

When `0<r<kappa(P)/2`, the first entry on the right is strictly smaller than the
left. Thus `tau>=kappa(P)r`, proving (EB.3). If `r=0`, the cores are congruent and
have diameter `D`; together with (EB.3) this proves (EB.4). `square`

## 3. All source points retained: a continuous rearrangement barrier

Let a full unit-separated source contain the labeled core `P`, as well as any number
of additional points. Those additional points need not remain isolated in subsequent
configurations. They may move, acquire contacts, lose contacts, or change components.
The following argument always restricts to the same original core labels.

### Corollary EB-C — the connected feasible component preserves the core

In the space of labeled unit-separated full-source configurations of diameter at
most `D`, every connected subset containing the original source has its original
core congruent to `P`.

Indeed, the function `r` of the restricted core is continuous. By (EB.3) its values
on this space avoid `(0,kappa(P)/2)`. Its image on a connected subset containing
the source is connected and contains zero, so that image is `{0}`.

In particular every continuous diameter-nonincreasing motion preserves all distances
between original core vertices, even if new contacts appear elsewhere. No condition
on how many activation events occur is necessary, and no differentiability of the
motion is assumed.

### Corollary EB-M — a positive diameter excursion is necessary

Any continuous unit-separated full-source path from the original source to a
configuration whose core has `r>=kappa(P)/4` passes through a source of diameter at
least

```math
\boxed{\sqrt{D^2+\kappa(P)^2/4}>D.}
\tag{EB.10}
```

Proof: continuity supplies a point with `r=kappa(P)/4`. Apply (EB.3) to its core;
the full-source diameter is at least the core diameter. `square`

Thus a hypothetical strict sub-`D` competitor, whose core must satisfy (EB.4), cannot
be reached through unit-separated configurations without first exceeding `D`.
This does not rule out a separately constructed competitor.

## 4. Application to the canonical C-II representative

For `D>=9`, [Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md), theorem
`C-ZRF`, supplies mixed rigidity rank `2m-3` on the nonisolated core. The
[C-I restoration](../targets/target-c/56-ci-restored-frontier.md) supplies
`C=C_*` and `H=H_*`; a relative-interior stress is strictly positive on these
entire actual sets. Every actual diameter endpoint lies in the core.

The two hypotheses of Theorem EB therefore hold for this original core. Its proof
uses no extension of the stress kernel to isolated coordinates. It applies equally
in Type I and Type II, and in both Woodall diameter-topology branches.

The source-specific constant may tend to zero arbitrarily fast in a hypothetical
unbounded family. This report derives no lower bound in terms of `D`, the number of
contacts, a chamber population, or a near-contact gap.

## 5. Scope audit and remaining obligation

| Statement | Classification | Reason |
| --- | --- | --- |
| The original C-II core is infinitesimally rigid | Already canonical | `C-ZRF`; not new here |
| Every isolated point can be attached without creating a triangle | Already canonical | [Theorem 12.1](../theory/02-nonlinear-and-regressions.md); no novelty claimed |
| Deep near-unit pairs exist in the chamber | Already canonical | `C-INACTIVE-DEEP-MATCHING` |
| Isolate activation can unlock the old core along a diameter-nonincreasing path | Rejected under the EB hypotheses | Corollary EB-C |
| Every sufficiently small nonrigid displacement pays a linear squared-diameter increase | Proved candidate | Theorem EB |
| The core is globally optimal for its own cardinality | Not proved | Local growth and a finite escape barrier do not imply global optimality |
| C-II is closed | Not proved | Neither global branch has been excluded |

The unit square is compatible with the theorem: its four unit sides and two
diagonals carry positive equilibrium stress and have mixed rigidity rank five.
The heptagon-plus-center example is compatible: the center can move while the
rigid boundary core stays congruent. The theorem makes no assertion that the
center is diametral or stress-supported. Regular-shell local-minimum regressions
are likewise allowed; global optimization was deliberately not a premise of EB.

The exact remaining competitor obligation is now qualified as follows. If one
tries to contradict C-II by constructing a labeled `n`-point unit-separated set `X`
with `diam(X)<D`, its original core labels must be placed at distance at least
`kappa(P)/2` from the original congruence orbit. Such a construction must prove
every final cross-distance, including those involving the isolated population.
An alternative is a structural packing theorem proving that a core satisfying
these rigidity/stress hypotheses cannot coexist with either canonical population
branch. Merely adding contacts to the isolates is not that structural theorem.

**Promotion recommendation:** retain as an unreviewed report pending independent
audit. No canonical theorem status or active prompt is changed by this report.
