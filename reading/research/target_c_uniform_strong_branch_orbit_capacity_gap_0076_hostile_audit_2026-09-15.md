> Generated reading edition · [exact source](../../research/target_c_uniform_strong_branch_orbit_capacity_gap_0076_hostile_audit_2026-09-15.md) · source SHA-256 `14dfe5443ad8ea13cbe1f346e75873a5906843572d119ebacd90e150b5de6c88`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b79fcc2ba6f73a37424daeaa500f283b29fcca2a", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_uniform_strong_branch_orbit_capacity_gap_0076_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d2e331baee97ba625b56d48b77a29dc4b4f71bf76f9b9c31227221e8d21c22a9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — corrected uniform strong-branch orbit-capacity gap `0.0076`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_uniform_strong_branch_orbit_capacity_gap_0076_2026-09-15.md`
- `research/verify_target_c_uniform_strong_branch_orbit_capacity_gap_0076.py`

**Disposition:** **PASS at stated proof-only matched all-train/rhombic scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

An initial version inherited the same scope hazard found by the concurrent correction of the `0.0052` phase-star theorem: it wrote the physical pair bound beyond the required family-size cap `K=2/sqrt(3)`.  That version was not safe.  Commits `57107ce` and `a3cef8b` repair the issue by splitting the dominant-orbit center mass into three regimes:

1. strong pair branch, with `C<=C_s(W)<K`;
2. unconditional pair fallback, with `C_s(W)<=C<=K`;
3. high center `C>K`, where no pair theorem is used and the generic bound `E<=C(W-C)` applies.

The corrected theorem still proves the matched gap `0.0076`.

## 1. Strong-branch ratio and size scope

For `C<=W/2`, every leaf mass `L` satisfies `L<=C`, so

```math
{(C+L-K)_+\over L}
\le 2-{K\over C}
\le2-{2K\over W}
\le2-{2K\over A_0}.
```

The exact certificate gives

```math
2-{2K\over A_0}<0.793<\sqrt{20/29}.
```

Also `C<=A_0/2<K`, so the physical pair theorem is in scope.

For `C>W/2`, define

```math
C_s(W)=W-{W-K\over\sqrt{20/29}}.
```

The certificate proves over the entire dominant-mass interval

```math
1.0000<C_s(W)<1.0032<K=1.1547\ldots .
```

Thus both center/leaf pairs satisfy the strong `1/10` branch throughout the entire interval used to locate the capacity maximizer, without violating the pair theorem's size hypothesis.

**Verdict:** PASS after repair.

## 2. Strong capacity maximizer

On `W/3<=C<=W/2`, the strong capacity is

```math
\Phi_{1/10}(W,C)
=C(W-C)-{1\over10}{3C-W\over C}
\left({W+C\over2}-K\right)^2.
```

Its second derivative is at most `-2`, its derivative at `C=W/3` is uniformly above `0.6255`, and its derivative at `C=W/2` is negative.  Hence it has one maximizer strictly in `(W/3,W/2)`, entirely inside the strong pair branch and below `K`.

The strong-concavity tangent certificate at `c_0=0.935343` gives

```math
\Delta_2-\Psi_1(A_0)>9.84\times10^{-5}.
```

**Verdict:** PASS.

## 3. Pair-theorem fallback

On `C_s(W)<=C<=K`, the universal coefficient `2/29` is valid because every phase family is at most `C<=K`.  Since `C_s(W)>W/2`, the corresponding capacity is strictly decreasing in `C`; its maximum occurs at the left boundary.

The moving boundary satisfies `C_s'(W)<0`, while `Phi_C<0`, so its contribution to the `W` derivative is positive.  After the residual-orbit derivative is deducted, the exact lower bound remains

```math
Q_0'(W)>0.8364.
```

At `W=A_0`,

```math
\Delta_2-B_0(A_0)>1.49\times10^{-3}.
```

**Verdict:** PASS.

## 4. High-center scope branch

For `C>K`, the corrected proof uses no physical pair theorem.  Since `A_0<2K`, one has `K>W/2` throughout the contradiction domain.  Therefore

```math
E\le C(W-C)\le K(W-K).
```

Including the residual orbit capacity gives

```math
Q_H(W)=K(W-K)+{(A_0-W)^2\over4}.
```

Its derivative is

```math
K-{A_0-W\over2}>1.147,
```

so its maximum is at `W=A_0`.  The exact endpoint margin is

```math
\Delta_2-K(A_0-K)>0.03218.
```

The repaired branch is therefore much farther from saturation than either low-center branch.

**Verdict:** PASS.

## 5. Global dominant-orbit reduction

The generic square argument gives

```math
W\ge M_0={4\Delta_2\over A_0}
```

and residual exact-orbit crossing mass at most `(A_0-W)^2/4`.  Each of the three possible dominant-orbit capacities, after this residual term is added, is strictly increasing in `W`:

```math
Q_1'(W)>0.5968,
\qquad
Q_0'(W)>0.8364,
\qquad
Q_H'(W)>1.147.
```

Thus all three are worst at `W=A_0`, where the residual mass vanishes.  The three certified endpoint deficits are respectively

```math
9.84\times10^{-5},
\qquad
1.49\times10^{-3},
\qquad
3.21\times10^{-2}.
```

No incompatible endpoint choices are combined.

**Verdict:** PASS.

## 6. Independent exact rerun

A disposable Pyroam exact-rational rerun of the repaired certificate returned:

```text
PASS corrected g=.0076
strong ratio upper 0.7922967561048989
cs min 1.000044629666146
cs max 1.0031416866586613
K lower 1.1547005383792515
strong margin 9.841163263676663e-05
fallback margin 0.0014949525015728487
high-center margin 0.03218506977622449
net strong slope 0.5968201754182958
net fallback slope 0.8364567952152777
net high slope 1.147115641199647
```

All asserted signs are separated from zero by large rational margins relative to the numerical enclosure width.

## 7. Rhombic transfer

The proof is rerun on the strict-rhombus train graph, not inferred by deleting singleton trains.  The pair theorem is used only on phase families inside its `<=K` size scope; the high-center branch again uses only triangle-freeness.  Hence

```math
T_R/D\ge2\sqrt{\Delta_2}+0.0076-o(1)
```

and the standard exact transfer gives

```math
\sigma_R/D\ge0.0152-o(1).
```

**Verdict:** PASS.

## Final disposition

The repaired theorem validly establishes

```math
\boxed{(T-q/2)/D\ge2\sqrt{\Delta_2}+0.0076-o(1)},
```

```math
\boxed{T_R/D\ge2\sqrt{\Delta_2}+0.0076-o(1),\qquad
\sigma_R/D\ge0.0152-o(1)}.
```

The initial center-size scope bug is closed.  The next useful work is downstream propagation into the current energy-restored complement-rhombus-incidence and dominant-boundary structure, not further decimal tuning of the atomic capacity.

**Final verdict:** PASS at proof-only scope. C-II remains open.
