> Generated reading edition · [exact source](../../research/target_c_phase_star_endpoint_residual_stability_2026-09-15.md) · source SHA-256 `f0bf23d856b11740f1d6fc6041191eec0d3f83d8164b5ece11e4ac9ed10ec097`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 9 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b43c75c9170976f9c7e4f3ff5cf7680c60c79bd2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_phase_star_endpoint_residual_stability_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "24d0e1f0d45a6044ab762e88a8bfbddff5abd4ff510d6c76a36db28af248f8bc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — phase-star endpoint controls residual exact-orbit mass

**Date:** 2026-09-15  
**Status:** proof-only structural stability lemma  
**Scope:** canonical full-core Type-II train-measure branch  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The corrected phase-star theorem gives the safe atomic-capacity floor

```math
C_{534}=2\sqrt{\Delta_2}+0.00534,
\qquad
\Delta_2={\pi\over2\sqrt3}.
```

Near that endpoint, the theorem gives substantially more than `U>=C534`.  Let `M` be
the mass of a dominant exact `pi/3` orbit and let `U` be any upper bound for the total
atomic capacity scalar, as in the Section-171 envelope.  On

```math
\boxed{C_{534}\le U\le1.911,}
```

every feasible atomic crossing measure satisfies

```math
\boxed{
0\le U-M\le1.003\,(U-C_{534}).
}
\tag{RS.1}
```

Thus essentially every increment of allowed mass above the phase-star endpoint can go
outside the dominant orbit only once.  There is no independent `0.005--0.006` two-bin
residual at this scale.

## 1. Full physical orbit capacity

Let `Psi(W)` denote the maximum physical crossing mass of one exact three-phase orbit
of total mass `W`, using the scope-corrected phase-star capacity theorem:

- for center mass `C<=K=2/sqrt(3)`, use the physical pair-deficit penalty;
- for `C>K`, use only `E<=C(W-C)`.

The corrected `g=0.00534` theorem proves

```math
\boxed{\Psi(C_{534})<\Delta_2.}
\tag{RS.2}
```

On the interval needed here the maximizing center lies in `(W/3,W/2)`, so the envelope
derivative satisfies

```math
\Psi'(W)
\ge {W\over3}
-{2\over29}\left({3U\over4}-{2\over\sqrt3}\right).
\tag{RS.3}
```

The generic two-bin bound below gives `M>1.904`, so on `U<=1.911` the right side is
larger than `0.61`.  Hence

```math
\boxed{\Psi'(W)>0.61}
\tag{RS.4}
```

throughout the relevant dominant-mass interval.

## 2. Generic residual is already below `0.007`

The ordinary two-bin theorem remains available independently of the phase-star
strengthening.  It gives

```math
M\ge m_2(U):=
{U+\sqrt{8\Delta_2-U^2}\over2}.
```

Since `U-m_2(U)` is increasing here, at `U<=1.911`,

```math
\boxed{
R:=U-M\le U-m_2(U)<0.006386<0.007.
}
\tag{RS.5}
```

This coarse bound is used only to linearize the sharper phase-star estimate.

## 3. Phase-star deficit forces proportional residual

The exact crossing decomposition and generic square capacity of all non-dominant
orbits give

```math
\Delta_2
\le \Psi(M)+{(A-M)^2\over4}
\le \Psi(M)+{(U-M)^2\over4}.
\tag{RS.6}
```

Put

```math
h:=U-C_{534}\ge0,
\qquad
R:=U-M.
```

If `M>=C534`, then immediately

```math
R=U-M\le U-C_{534}=h.
```

Suppose instead `M<C534`.  By (RS.2)--(RS.4),

```math
\Delta_2-\Psi(M)
>\Psi(C_{534})-\Psi(M)
>0.61(C_{534}-M).
```

Using (RS.6),

```math
0.61(C_{534}-M)<{R^2\over4}.
```

But

```math
C_{534}-M=R-h,
```

so

```math
R-h<{R^2\over2.44}.
```

By (RS.5), `R<0.007`, hence

```math
R-h<{0.007\over2.44}R.
```

Therefore

```math
R< {h\over1-0.007/2.44}
<1.003h.
```

This proves (RS.1).

## 4. Consequences for the low-`t` stack

Two quantities in the current shared-retention/rhombus-incidence proof improve
simultaneously.

First, the complement complete-train ceiling becomes

```math
N_c
\le U+{t+\kappa\over2}-M
\le {t+\kappa\over2}+1.003(U-C_{534}).
\tag{RS.7}
```

Thus the joint retained mass obeys

```math
z+p
\ge \pi-{t+\kappa\over2}
-1.003(U-C_{534})-o(1).
\tag{RS.8}
```

Second, the exact atomic mass outside the dominant orbit is at most `U-M`, so the
complement-rhombus incidence budget improves from the generic `r_2(U)^2/2` to

```math
\boxed{
{1\over2}[1.003(U-C_{534})]^2.
}
\tag{RS.9}
```

Both gains vanish at the same endpoint `U=C534`, where the dominant exact orbit must
carry all allowed atomic mass.  This correlation is what was missing from the earlier
scalar optimizations.

**Disposition:** proved proof-only endpoint stability lemma; C-II and Level I remain open.
