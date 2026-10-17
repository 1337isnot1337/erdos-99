> Generated reading edition · [exact source](../../research/target_c_allregime_fan_train_floor_hostile_audit_2026-09-12.md) · source SHA-256 `38221a7c71d3e4356674805ee783281e98a3d66538b15000adff6e9339ed5360`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0c8e454927ebe023555fde0e1c4d1326e273962b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_allregime_fan_train_floor_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6298bea8befe15d6b7d67ac60d98b31c61c55351bd25c938837f68da8b8c46fc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — all-regime fan/train scalar floor (retracted)

**Date:** 2026-09-12  
**Audited source:** `target_c_allregime_fan_train_floor_2026-09-12.md`  
**Disposition:** REJECTED for the density-floor conclusion; finite pair accounting remains valid.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Scope and imported directions

The fan input is the finite inequality

`20 f <= T(T-1)-2R`,

which normalizes to `H_t(phi)>=-o(1)`. The train input is the audited all-Type-II
base floor `(T-q/2)/D>=2 sqrt(Delta_2)-o(1)`, not the stronger two-half-disk floor.
The outer input is used only in the direction `Q/D<=2t-pi+o(1)`; `f<=Q` therefore
gives the upper endpoint `phi<=2t-pi+o(1)`. No equality for the outer-walk length is
assumed.

**Critical correction:** `20f<=T(T-1)-2R` cannot be normalized to a nonzero
`20(f/D)` term when `f,T=O(D)`. The endpoint obstruction consequently has no valid
asymptotic input.

## 2. Lower endpoint with nonzero kappa

The train floor yields

`phi>=s-t/4+kappa/4-o(1)`.

The admissible `kappa` range is `0<=kappa<=pi-t+o(1)` because `q/D=t+kappa<=pi`.
At the lower endpoint, the train count is at most `pi/2+2s+o(1)<5`, so the
derivative of `H_t` with respect to `phi`, namely `4(t+2phi)-20`, is negative.
Consequently the largest lower-endpoint value occurs at `kappa=0`; dropping
`kappa/4` is valid here. This is the point that would fail if the endpoint were
already to the right of the vertex of the convex quadratic.

If the lower and upper phi bounds are incompatible, there is no survivor. Otherwise
the limiting interval begins at `t_0=4(s+pi)/9`.

## 3. Endpoint signs and root

The lower endpoint expression is

`(t/2+2s)^2-20(s-t/4)-2 Delta_2`.

Its derivative is `t/2+2s+5>0`, and its positive root is

`t_ar=sqrt(8s^2+160s+100)-4s-10`.

At the upper endpoint the expression is the convex quadratic `J(t)`. The arithmetic
certificate checks `J(t_0)<-3.84` and `J(t_ar)<-3.72`; convexity places `J` below
the chord between these negative endpoint values throughout the interval.

Thus both endpoint values are negative for every limiting `t<t_ar`. Convexity of
`H_t` puts the entire admissible interval below zero, contradicting the fan budget.
The sequence-level `o(1)` terms cannot repair a fixed limiting strict gap.

## 4. Classification and limitations

The former result was conditional on the audited global train-floor module, but the
normalization correction removes its Type-II floor. It does not use the two-half-disk
alternative, does not address Type-I, and excludes no Type-II limits. Contact-isolated
source points are not removed.

**Final audit verdict:** REJECTED as an asymptotic scalar-floor candidate; the finite
fan pair lemma remains valid and C-II remains open.
