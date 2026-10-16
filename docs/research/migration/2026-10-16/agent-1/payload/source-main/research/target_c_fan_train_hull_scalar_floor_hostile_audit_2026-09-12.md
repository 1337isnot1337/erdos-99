# Hostile audit — fan/train/hull scalar floor (retracted)

**Date:** 2026-09-12  
**Audited source:** `target_c_fan_train_hull_scalar_floor_2026-09-12.md`  
**Disposition:** REJECTED for the density-floor conclusion; finite imported lemmas remain valid.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This audit checks the new convex elimination and the directions of every imported
inequality. It does not promote the result or claim a geometric realization.

**Critical correction:** the imported fan inequality was normalized incorrectly. Since
`f=O(D)` and `T=O(D)`, `20f/D^2=o(1)`, not `20(f/D)`. The scalar endpoint
elimination therefore does not follow.

## 1. Imported bounds and directions

The bounded-face fan theorem gives the finite pair inequality

`20 f <= T(T-1)-2R`.

After division by `D^2`, `R/D^2 -> Delta_2`, and `T/D=t+2 phi`, this gives
`H_t(phi) >= -o(1)`.

The two-half-disk atomic theorem is used in its actual normalization
`(T-q/2)/D >= C-o(1)`. Substituting `q/D=t+kappa` gives

`phi >= C/2-t/4+kappa/4-o(1)`,

so dropping the nonnegative `kappa/4` is valid. The Type-II outer estimate is used
only as `Q/D <= 2t-pi+o(1)`, not as the stronger and generally false equality
`Q/D=2t-pi`. Since `f<=Q`, the upper endpoint `phi<=2t-pi+o(1)` is in the correct
direction.

## 2. Endpoint interval

If the lower and upper `phi` bounds are incompatible, there is already no survivor.
Otherwise their limiting interval has

`a(t)=C/2-t/4 <= b(t)=2t-pi`,

which is equivalent to `t>=t_0=(2C+4pi)/9`. No lower bound from the earlier
fan-only floor is silently imported.

## 3. Convexity and endpoint signs

`H_t(phi)` has second derivative `8`, so on a closed interval its value is at most
the chord joining the endpoint values. It is therefore negative throughout an
interval when both endpoint values are negative.

At the lower endpoint, the displayed formula is increasing because its derivative is
`t/2+C+5>0`. Certified arithmetic gives its value at `t_*` below `-0.56`.

At the upper endpoint the expression is the convex quadratic

`J(t)=(5t-2pi)^2-20(2t-pi)-2Delta_2`.

The endpoint `t_0` has `J(t_0)<-5.15`, and the larger root is `t_*`. Convexity in
`t` puts `J(t)` below the chord from `t_0` to `t_*`, hence `J(t)<0` for
`t_0<=t<t_*`. The certified interval script checks the constant enclosures and the
larger-root formula.

The asymptotic `o(1)` errors are harmless for any fixed limiting value strictly below
`t_*`; endpoint negativity has a positive margin. This is a liminf statement, not
a finite-`D` strict inequality.

## 4. Scope checks

- The result is conditional on the proof-only two-half-disk alternative and its
  groupwise atomic train floor.
- It does not use `b/D=pi`, equality uniqueness, or a source-level construction.
- It does not rule out Type-II limits at or above `t_*`.
- It does not address the Type-I inactive-container branch.
- Contact-isolated source points are not removed from the source; they simply do not
  enter the train pair count.

**Final audit verdict:** REJECTED as a Type-II scalar-floor candidate; only the finite
fan pair accounting survives. C-II remains open.
