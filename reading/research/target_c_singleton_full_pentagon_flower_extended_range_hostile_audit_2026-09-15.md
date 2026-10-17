> Generated reading edition · [exact source](../../research/target_c_singleton_full_pentagon_flower_extended_range_hostile_audit_2026-09-15.md) · source SHA-256 `39efb5e62b964a61965edc99852725ec850de6a3a385d0dc275af7e7fafe321d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "fe86ad385421d97acdb4fc44ab8ec28a5ceba298", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_singleton_full_pentagon_flower_extended_range_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7c509c05a8ab27afe477b2d1daf27dfc316c7460bccb88004515080583beefb8"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — singleton/full-rhombic-pentagon-flower dichotomy through `t<=2.02`

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_singleton_full_pentagon_flower_extended_range_2026-09-15.md`  
**Disposition:** **PASS at its stated full-core train-measure scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate propagates the recently proved singleton/full-pentagon-flower dichotomy beyond its originally tabulated `t<=1.8623` range.  The danger is scope leakage from the O--O path program, because several earlier high-`t` path claims were retracted.  This audit checks that none of those path results enter the flower argument.

## 1. The pentagon floor is uniform and path-independent

The hostile audit of the `g=0.007707` matched all-train theorem explicitly records its scope as the canonical full-core Type-II train-measure branch, with no upper `t` cutoff.  The extended pentagon-sea audit separately verifies

```math
P_5/D\ge p_5(X)-o(1),
\qquad
p_5(X)=C_{707}+\pi-{5X\over2}
```

for every fixed endpoint `t<=X` where this lower bound is used.

Thus the flower argument may use the pentagon floor above `1.8623` without importing any retracted path theorem.

**Verdict:** PASS.

## 2. The finite incidence inequality has no hidden phase hypothesis

Let `F_5^{full}` count pentagons having a strict rhombus across all five sides and let `S` count singleton stopped trains, i.e. contact edges incident to no strict-rhombus face.

If a pentagon is not fully rhombic, some boundary edge has a non-rhombus face on the other side.  Since the pentagon side itself is also non-rhombic, that edge is incident to no strict rhombus at all and is therefore a singleton train.  One singleton edge has only two face sides, so it can witness non-fullness of at most two pentagons.

Hence finitely

```math
P_5-F_5^{full}\le2S.
```

No phase concentration, path topology, or asymptotic assumption appears.

**Verdict:** PASS.

## 3. The balancing constant is optimal for this two-term inequality

For a known lower bound `P_5>=pD-o(D)`, suppose one wants a common lower floor `sD-o(D)` for the alternative

```math
S\ge sD-o(D)
\quad\text{or}\quad
F_5^{full}\ge sD-o(D).
```

If `S<sD`, the finite inequality gives

```math
F_5^{full}> (p-2s)D-o(D).
```

Thus one needs `p-2s>=s`, i.e.

```math
s\le p/3.
```

The candidate takes exactly

```math
s(X)=p_5(X)/3,
```

so no balancing slack is lost beyond the already rounded pentagon floor.

**Verdict:** PASS.

## 4. The train-slack consequence uses the correct branch condition

The exact modern identities are

```math
\rho_{rec}=2S,
\qquad
2\tau_D=\rho_{rec}+\sigma_R,
```

and the hostile-audited uniform train-slack theorem gives

```math
\tau_D\ge(\tau_0-o(1))D,
\qquad
\tau_0=0.7467921.
```

On the **full-flower side** of the balanced dichotomy, the singleton alternative has failed, so

```math
S<s(X)D+o(D).
```

Therefore

```math
\sigma_R
=2\tau_D-2S
>2[\tau_0-s(X)]D-o(D).
```

The inequality is used only conditionally on failure of the singleton branch.  The theorem does not assert this large `sigma_R` in every source.

**Verdict:** PASS.

## 5. Mantel-deficit propagation is exact

The strict-rhombus stopped-train crossing graph satisfies

```math
\sigma_R=2T_R-4\sqrt{R_4}.
```

Solving for `T_R` and substituting gives the finite identity

```math
{T_R^2\over4}-R_4
={\sigma_R\sqrt{R_4}\over2}+{\sigma_R^2\over16}.
```

Since `R_4/D^2->Delta_2`, a lower bound `sigma_R/D>=s_0-o(1)` gives

```math
\liminf D^{-2}\left({T_R^2\over4}-R_4\right)
\ge {s_0\sqrt{\Delta_2}\over2}+{s_0^2\over16}.
```

No convergence of `sigma_R/D` is assumed.

**Verdict:** PASS.

## 6. Fully rhombic flowers force the stated number of terminal trains

Each fully rhombic pentagon supplies five terminal face-side occurrences belonging to non-singleton rhombic trains.  One complete stopped train has at most two terminal occurrences.  Hence

```math
N_{full}\ge{5\over2}F_5^{full}.
```

This remains valid if one train terminates twice on the same flower or on two different flowers; the division by two already allows the worst reuse.

The merged isolate-host theorem independently makes every bounded pentagon source-empty, so the flower population consists of actual empty holes rather than chambers containing rattlers.

**Verdict:** PASS.

## 7. Exact arithmetic

The companion exact-`Fraction` certificate uses the standard Machin enclosure for `pi`, integer-square-root enclosures for `sqrt(Delta_2)`, and the exact rational `tau_0`.  An independent Pyroam run reproduced the representative rows:

```text
T      common floor   sigma_R floor   Mantel floor   N_full floor
1.88   .117975...     1.257634...     .697683...     .294937...
1.90   .101308...     1.290967...     .718864...     .253271...
1.92   .084641...     1.324300...     .740185...     .211604...
1.95   .059641...     1.374300...     .772425...     .149104...
1.96   .051308...     1.390967...     .783242...     .128271...
2.00   .017975...     1.457634...     .826855...     .044937...
2.02   .001308...     1.490967...     .848870...     .003271...
```

All displayed theorem constants round downward.  The positive common-floor threshold is the same pentagon threshold and has exact lower enclosure above `2.0215`.

**Verdict:** PASS.

## 8. Scope limitation

The theorem extends only the global train/flower dichotomy.  It does **not** extend the corrected O--O dual path, common diameter-routing hub, or finite switching-strip normal form above their independently proved endpoint (`t<=1.860` at this audit point).

It also does not assign a uniform angular or metric defect to one fully rhombic flower; explicit near-lattice flower regressions remain compatible with arbitrarily small local defects.

**Final verdict:** **PASS.** The singleton/full-flower dichotomy and its train-slack/Mantel consequences extend throughout the positive uniform pentagon range. C-II remains open.
