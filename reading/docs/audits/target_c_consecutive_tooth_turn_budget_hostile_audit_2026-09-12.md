> Generated reading edition · [exact source](../../../docs/audits/target_c_consecutive_tooth_turn_budget_hostile_audit_2026-09-12.md) · source SHA-256 `8a452561d6ccdf7a5c0f071428ad2473542cd9280a1eb3000efc3b2254e1e938`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8966C86E6B04","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — hostile audit of the consecutive-tooth turn budget

**Date:** 2026-09-12
**Artifact audited:** `research/target_c_consecutive_tooth_turn_budget_2026-09-12.md`
**Verdict:** finite consecutive-tooth inequality passes; no C-II closure.
**Base state:** audit.46; C-I closed, C-II open, Level I open.

This audit checks the orientation, apex-separation, cyclic summation, and convexity
steps in the post-126 tooth-turn candidate. It does not treat a local tooth cycle as a
global minimizer and does not infer an exact unit triangle from a limiting equality.

## 1. Local angle convention

Let three consecutive counterclockwise loaded-hull vertices be `p_i,p_{i+1},p_{i+2}`.
Write

```math
 b_i=|p_{i+1}-p_i|=1+e_i,
 \qquad
 \beta_i=\arccos(b_i/2).
```

For a tooth apex on the inward side of the first hull side, the ray from `p_{i+1}`
to its apex makes angle `pi-beta_i` with the directed preceding side. For the next
tooth the corresponding ray makes angle `alpha_i+beta_{i+1}`, where `alpha_i` is the
exterior hull turn. Both rays lie in the common interior wedge, so their smaller
separation is

```math
 \gamma_i=\pi-\alpha_i-eta_i-eta_{i+1}\ge0.
\tag{1}
```

The wedge condition is essential: without it, the displayed difference could be an
oriented angle rather than the smaller separation. For actual convex-cell tooth
pockets, inwardness supplies the condition.

## 2. Unit separation gives the exact turn inequality

The two apices are distinct source points. Unit separation and the equal unit radii
give

```math
 1\le|x_i-x_{i+1}|=2\sin(\gamma_i/2).
```

Since `0<=gamma_i<pi`, this implies `gamma_i>=pi/3`. Substitution into (1) yields

```math
 \alpha_i
 \le {2\pi\over3}-\beta_i-\beta_{i+1}
 =f(e_i)+f(e_{i+1}),
```

where

```math
 f(e)={\pi\over3}-\arccos((1+e)/2).
```

This verifies the candidate's Lemma TT.1. Strict triangle-freeness makes the apex
separation strictly greater than one, but it supplies no uniform positive margin, so
the non-strict inequality is the correct asymptotic statement.

## 3. Run and cycle summation

Summing the local inequality over a run `r,...,s` counts interior base errors twice
and endpoint errors once:

```math
 \sum_{i=r}^{s-1}\alpha_i
 \le f(e_r)+2\sum_{i=r+1}^{s-1}f(e_i)+f(e_s).
```

For a cyclic all-tooth hull, every base error occurs twice and the exterior turns sum
to `2pi`, hence

```math
 \sum_i f(e_i)\ge\pi.
\tag{2}
```

There is no endpoint term on the cycle and no missing turn at the cyclic cut.

## 4. Convexity converts turn to base excess

Differentiate on `[0,1)`:

```math
 f'(e)={1\over\sqrt{4-(1+e)^2}}>0,
 \qquad
 f''(e)={1+e\over(4-(1+e)^2)^{3/2}}>0.
```

Thus `f` is increasing and strictly convex, with `f(0)=0` and
`lim_{e->1-}f(e)=pi/3`. Convexity places the graph below its endpoint chord,

```math
 f(e)\le {\pi\over3}e.
```

Combining this with (2) gives the exact finite lower bound

```math
 \boxed{\sum_i e_i\ge3.}
```

If `e_i<=eta<1`, the tangent bound

```math
 f(e_i)\le f'(\eta)e_i
 ={e_i\over\sqrt{4-(1+\eta)^2}}
```

instead gives

```math
 \boxed{\sum_i e_i\ge\pi\sqrt{4-(1+\eta)^2}.}
```

The accompanying floating-point verifier reproduces these constants and is only an
arithmetic diagnostic; the derivative calculation above is the proof.

## 5. Scope and closure barrier

The audited claim is a valid **audited-working, proof-only** local theorem:

> A consecutive pair of actual two-edge teeth must spend hull turn against the
> combined base errors, and a cyclic all-tooth boundary has at least three total
> base-excess units.

The result does not imply a fixed positive excess per tooth. For a cycle with
`Theta(D)` sides, the required total excess is only `O(1)`, while the canonical
Section-125 source-level budgets permit `O(D)` total excess. The strict inequality
between source points therefore does not force an exact unit equilateral triangle.

The theorem also assumes the post-124/125 fact that tooth bases are actual global
loaded-hull sides; it does not prove that fact. Contact-isolated points are retained,
and no source-preserving strict diameter decrease is constructed.

**Disposition:** pass at proof-only scope; theorem state unchanged and C-II remains
open.
