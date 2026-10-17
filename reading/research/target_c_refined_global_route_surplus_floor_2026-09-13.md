> Generated reading edition · [exact source](../../research/target_c_refined_global_route_surplus_floor_2026-09-13.md) · source SHA-256 `603fa593d6da51391ed9e66a6c8348c74a28e2c13b04dcc795d4925ff9421326`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "116bf437cb4da1daf6ee7bc529ba31df6da9b89e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_refined_global_route_surplus_floor_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b7f7953e42416e4914365b64944cac512707e51f2d9593a2b6a9c7792de82ece"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — refined global route-surplus floor

**Date:** 2026-09-13  
**Status:** proof-only arithmetic refinement; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The repaired Section-149 phase atomization and the audited all-regime outer-atom
bound imply a slightly stronger explicit floor for the global route surplus. The old
published split gave `1/10`. The same `N=2` Fejér estimate can be optimized on the
short-detour interval to give `153/1250`.

Let

```math
S_D:={b-\operatorname{per}(F)+Q+4f\over D},
\qquad
\lambda_D:={b-\operatorname{per}(F)\over D},
```

in the Type-II full-core branch. Section 155, with the repaired finite-to-limit
atomization lemma, gives for `N=2` and every subsequential limit `lambda>=0`

```math
\liminf {Q+4f\over D}
\ge\left(4\sqrt{\Delta_2}-\sqrt{U_2(\lambda)}\right)_+,
\tag{RG.1}
```

where

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
U_2(\lambda)={ (\pi+\lambda)^2+1225\lambda^2\over2}.
\tag{RG.2}
```

## Theorem RG — explicit `0.1224` route-surplus floor

Every Type-II survivor sequence satisfies

```math
\boxed{
\liminf_{D\to\infty}S_D\ge {153\over1250}=0.1224.
}
\tag{RG.3}
```

### Proof

Set `r=153/1250` and `c=4\sqrt{\Delta_2}`. The function `U_2` is increasing on
`[0,infinity)`. For `0<=lambda<=r`, define

```math
H(\lambda):=(c+\lambda-r)^2-U_2(\lambda).
```

Its quadratic coefficient is `-612`, so `H` is concave. The elementary rational
enclosures

```math
\pi<3.14160,
\qquad
4\sqrt{\Delta_2}>3.8092
```

give

```math
H(0)>(3.8092-0.1224)^2-{3.14160^2\over2}>8.65>0,
```

and

```math
H(r)>3.8092^2-
{(3.14160+0.1224)^2+1225(0.1224)^2\over2}>0.006>0.
```

Concavity gives `H(lambda)>=min{H(0),H(r)}>0` throughout `[0,r]`. Also
`c+lambda-r>0`, so `sqrt(U_2(lambda))<=c+lambda-r` and therefore

```math
\lambda+4\sqrt{\Delta_2}-\sqrt{U_2(\lambda)}\ge r.
\tag{RG.4}
```

Take a subsequence realizing the liminf of `S_D`. If `lambda_D>=r` along a further
subsequence, then `S_D>=r` there. Otherwise pass to a limit `lambda<r` and apply
(RG.1) and (RG.4), obtaining `liminf S_D>=r`, a contradiction to any value below
`r`. This proves (RG.3). `square`

The floor is deliberately conservative. Numerical minimization of the unrounded
`N=2` expression gives approximately `0.12245`, but no sharper decimal is used here.

## Consequence and scope

The source-level route system must satisfy

```math
(b-\operatorname{per}(F))+P_{exc}\ge0.1224D-o(D),
\qquad P_{exc}=Q+4f,
```

in Type II. This improves the existing `0.1D` proof-only floor but remains compatible
with the current high-detour scalar regression. It does not give an upper bound on
the same route currency, a source-preserving strict diameter decrease, or a forced
unit equilateral triangle. Type I is untouched.

**Classification:** proved candidate awaiting hostile audit; proof-only. C-II remains
open.
