> Generated reading edition · [exact source](../../../docs/reports/target_c_external_rattler_floor_2026-09-09.md) · source SHA-256 `d10bc0a423dfbe98ad4460d1d48a55407a8eeefdc4a6b1590070e42bb1db3399`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 6 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-6FDE6FD015D3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — external force-hull population floor from ZF and OP

**Date:** 2026-09-09  
**Repository state:** current main through `58420d2f13ba3f75ea943d8b60e90b2984287081`, combined with PR #112  
**Run type:** exact source-population consequence  
**Target:** Target C C-II / external completion shell  
**Computation:** numerical constants only; proof analytic

## LEVEL I STATUS

`STILL OPEN`

The OP theorem on current main absorbs every source point lying inside the force hull into the ordinary Oler capacity of that hull. The new post-ZF diameter-direction theorem in PR #112 gives `per(F)<=2h`. Together with the isoperimetric inequality this yields an explicit quadratic lower bound on the population that must lie **outside** the force hull whenever the diameter graph has fewer than `(pi/2)D` edges.

This localizes the low-diameter-edge obstruction sharply: near the new general endpoint `h/D=tau_*`, a positive quadratic population is forced into the external completion shell, not merely into unspecified contact-isolated regions.

## 1. Setup

Use the C65 lexicographically normalized hypothetical triangle-free global minimizer. Let

- `F` be the force hull of the positive nonisolated contact core;
- `v` be the number of positive-core vertices;
- `Z_def` be contact-isolated source points in bounded contact faces;
- `Z_in` be contact-isolated source points in the outer contact face but still lying in `F`;
- `Z_ext` be source points outside `F`.

Then

```math
n=v+Z_{def}+Z_{in}+Z_{ext}.
\tag{1.1}
```

OP proves the exact internal-capacity estimate

```math
\boxed{
 v+Z_{def}+Z_{in}
\le
\frac{2}{\sqrt3}\operatorname{area}(F)
+\frac12\operatorname{per}(F)+1.
}
\tag{1.2}
```

The post-ZF survivor satisfies

```math
b+Q\le2h
\tag{1.3}
```

and the outer contact walk contains the force-hull vertices, so

```math
\operatorname{per}(F)\le b\le b+Q\le2h.
\tag{1.4}
```

## 2. Exact finite external-population inequality

The planar isoperimetric inequality gives

```math
\operatorname{area}(F)
\le
\frac{\operatorname{per}(F)^2}{4\pi}.
\tag{2.1}
```

Insert (1.4):

```math
\operatorname{area}(F)
\le
\frac{h^2}{\pi}.
\tag{2.2}
```

Subtract (1.2) from (1.1).

### Theorem ZX.1 — finite external rattler floor

Every post-ZF C65 survivor satisfies

```math
\boxed{
Z_{ext}
\ge
n-\frac{2h^2}{\pi\sqrt3}-h-1.
}
\tag{ZX.1}
```

### Proof

By (1.1) and OP,

```math
Z_{ext}
\ge
n-\frac{2}{\sqrt3}\operatorname{area}(F)
-\frac12\operatorname{per}(F)-1.
```

Use (2.2) and `per(F)<=2h`. QED.

No isolated point is declared diametral. The theorem is about the actual external population in the original C65 lexicographic source.

## 3. Asymptotic form

The global packing bounds give

```math
\frac{n}{D^2}\to
\Delta:=\frac{\pi}{2\sqrt3}.
\tag{3.1}
```

Pass to a subsequence with

```math
\frac hD\to x.
\tag{3.2}
```

Divide ZX.1 by `D^2`.

### Corollary ZX.2

```math
\boxed{
\liminf\frac{Z_{ext}}{D^2}
\ge
\Delta-\frac{2x^2}{\pi\sqrt3}.
}
\tag{ZX.2}
```

The right side is positive exactly when

```math
\boxed{x<\frac\pi2.}
\tag{ZX.3}
```

Thus every hypothetical sequence with

```math
\limsup h/D<\pi/2
```

contains a positive quadratic density of source points strictly outside the force hull.

PR #112 gives the universal post-ZF endpoint

```math
\tau_*=1.4781702664\ldots
\le\liminf h/D.
```

At `x=tau_*`, ZX.2 gives

```math
\boxed{
\Delta-\frac{2\tau_*^2}{\pi\sqrt3}
=0.1038019123\ldots .
}
\tag{ZX.4}
```

So a survivor asymptotically saturating the current diameter-edge lower endpoint would require at least

```math
(0.1038019-o(1))D^2
```

source points outside the force hull.

## 4. Relation to the broader PR #112 population bound

PR #112 independently proves, from stopped trains and Mantel,

```math
\liminf\frac{n-v}{D^2}
\ge
\Delta-\frac14(3x-4\cos(x/2))^2.
```

That lower bound concerns **all** points outside the positive core and remains positive until

```math
x_0=1.5754757611\ldots>\pi/2.
```

ZX is stronger in localization but weaker in range:

- for `x<pi/2`, it proves a definite quadratic population lies outside the force hull itself;
- for `pi/2<=x<x_0`, PR #112 still forces a quadratic inactive population, but current theorems do not force a positive fraction of it outside `F`.

Thus `pi/2` is a genuine population-localization threshold in the present stack.

## 5. Interaction with RA

RA proves that all C65 rattlers, including external ones, can be moved by finite first-contact motions to another same-cardinality, same-diameter triangle-free global minimizer in which no vertex is contact-isolated, while the original positive core remains fixed pointwise.

ZX therefore has the following representative-transfer interpretation:

> if `h/D<pi/2`, the C65 lexicographic source contains `Theta(D^2)` external rattlers, yet there exists another triangle-free global representative in which those degrees of freedom have been absorbed into ordinary zero-or-positive-multiplier contacts around the same fixed core.

This does not permit reuse of ZR/ZF on the contact-richer representative. The missing theorem is a representative-invariant capacity or topology statement that turns this massive external absorption into a contradiction.

## 6. Exact remaining branch split

After ZX, the post-ZF problem admits a useful finite-scale conceptual split:

1. **external-completion phase:** `h/D<pi/2`; a positive quadratic population must live outside `F`;
2. **high-diameter phase:** `h/D>=pi/2`; the external quadratic lower bound vanishes, and the diameter support itself is already very dense.

The direct Level I endpoint remains

```math
\boxed{b+Q>2h.}
```

A proof in phase 1 should now target the external completion shell or the RA representative transfer directly. A proof in phase 2 should use the dense diameter-thrackle/face ledger.

## 7. Regression audit

- The regular heptagon plus isolated center is not contradicted: its isolate lies inside its contact hull, not in the asymptotic post-ZF external phase, and the theorem is only useful at large `D`.
- Regular shells with dense interior fillings do not contradict ZX; their inactive population can lie inside the shell hull and they are not certified global minima in the large regime.
- No old force-bulk localization claim is revived. ZX derives external population from OP plus isoperimetric capacity, not from asserting that isolated points are diameter endpoints.
- RA is used only as a representative-transfer interpretation, not as a KKT-positive-contact theorem.

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

OP:
  v+Z_def+Z_in <= (2/sqrt3)area(F)+per(F)/2+1.

Post-ZF:
  per(F)<=b<=b+Q<=2h.
Isoperimetric:
  area(F)<=per(F)^2/(4pi)<=h^2/pi.

Therefore
  Z_ext >= n - 2h^2/(pi sqrt3) - h - 1.

If h/D -> x:
  liminf Z_ext/D^2
    >= pi/(2sqrt3) - 2x^2/(pi sqrt3).
This is positive exactly for x<pi/2.

At the current universal endpoint tau_*=1.4781702664...:
  Z_ext >= (0.1038019123...-o(1))D^2.

Next phase split:
  h/D<pi/2  -> quadratic external completion shell;
  h/D>=pi/2 -> dense diameter-support phase.

Direct Level I endpoint remains b+Q>2h.
```
