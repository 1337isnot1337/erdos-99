# Target C — Newton–Hoffman Gate C-I closure

**LEVEL I STATUS: STILL OPEN. GATE C-I: CLOSED.**

This module records C63 from
`docs/reports/target_c_newton_hoffman_gate_ci_closure_2026-08-31.md`.
It resolves the jet-stitching obstruction left by C62.

## C63 exact quadratic correction

On the maximal KKT-supported active set `E_*`, write the signed feasibility map exactly as

`g_*(x) = A_* x + Q_*(x)`.

Here contacts use `|r+d|^2-1` and diameter rows use `D^2-|r+d|^2`, so `Q_*` is the signed squared edge-difference map.

For every nonnegative left multiplier

`lambda >= 0`, `lambda^T A_* = 0`,

a nonzero `lambda` has positive total diameter weight and normalizes to a genuine KKT stress. C54 universal PSD therefore gives

`lambda^T Q_*(x) >= 0`

for every displacement field `x`, not merely for critical directions.

Consequently, at every current displacement `x`, Farkas' lemma makes the linear correction system

`A_* y >= -g_*(x)`

feasible. The fixed-matrix Hoffman bound supplies such a correction with

`|y| <= H |[g_*(x)]_-|`.

Because the constraints are exactly quadratic,

`|Q_*(x+y)-Q_*(x)| <= L(|x||y|+|y|^2)`.

Starting from a critical tangent `x_0=t v`, C6 gives `A_*v=0`, hence the initial violation is `O(t^2)`. For small `t`, each Hoffman correction multiplies the violation by `O(t)`. The correction series converges geometrically and has total size `O(t^2)`.

Thus for every critical velocity there are actual nearby displacements

`x(t)=t v+O(t^2)`

satisfying every strong active inequality.

## Gate C-I consequence

Choose the C6 relative-interior critical velocity. Every weak active row has strict signed first variation, so its `Theta(t)` margin survives the `O(t^2)` Newton–Hoffman correction. Every inactive pair has fixed strict slack and also remains inactive.

The resulting configuration is unit-separated and has diameter at most `D`. Since `D=D(n)` is globally minimal, its diameter is exactly `D`.

If a weak unit contact existed, all weak unit contacts would open and no new unit contact would appear. This contradicts the contact-minimal choice of the global minimizer. Therefore

`C=C_*`.

Every unit contact is KKT-supported.

## Why C62's stitching issue disappears

C62 chooses one second-order acceleration and then must reconcile it with an exact body-bouquet motion on the frozen support. C63 does not prescribe one acceleration. It re-solves the full strong-row linear correction problem after every exact quadratic residual. Universal PSD guarantees every correction problem is feasible; Hoffman bounds the correction size. No separate support saturation, bouquet stitching, or higher-order formal series is needed.

## Remaining Target C task

Only Gate C-II remains: exclude a triangle-free globally minimum-diameter configuration in the fully force-visible phase `C=C_*`.

The next work should use the existing fully-visible bridge, pinned-block, force-hull, separator, degree, and response frontiers with the weak-contact alternative removed.
