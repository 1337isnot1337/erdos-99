<!-- theorem-state: {"artifact_id":"ART-B3CED042B34C","canonical":false,"claim_ids":["C-THIRD-CONTACT-FAN-REFLECTION-COLLISION-REGRESSION"],"claim_statuses":{"C-THIRD-CONTACT-FAN-REFLECTION-COLLISION-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C third-contact fan reflection collision: independent audit

Date: 2026-10-07. Audit base: `39a6158cb50e18048864448f2cd0f24a3c02601b` (`2026-10-07.audit.101`).

Primary source: PR #722 branch `research/target-c-residual-closure-20261005` at frozen commit `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`; `docs/reports/target_c_generic_isolate_anchor_localization_2026-10-05.md`, SHA-256 `2efbbfcc67e50f12cf218ea00d17ba9a1bc4a20b2cd40e9dd22edaab23936ca3`. The same strict-interior geometry appears as unreviewed Theorem LF.4 in `docs/reports/target_c_leaf_fan_stopped_train_and_collar_2026-10-02.md` at audit-base main, SHA-256 `7ab7d76f59762041a16b4cc7124ef27414b8eb3789a93b3c326fd35253626886`. I audit only the common strict-interior geometry and its fan-reflection consequence; LF.4's additional contact-degree `3,4,5` assertion and the reports' train/population consequences are not included.

## Exact finite statement

Let `A` be a finite unit-separated planar source of diameter `D>=2`. Suppose it contains distinct points `p,a,p_-,p_+,z` with

```text
|p-a|=|p_--a|=|p_+-a|=D,
|p-p_-|=|p-p_+|=|p-z|=1.
```

Then `z` lies strictly inside `conv{a,p_-,p_+}`. In particular `z` is not an actual diameter endpoint. Reflecting `p` across the line `p_-p_+` gives the standard fan point

```text
p' = p + (a-p)/D^2.
```

This reflection preserves the two old unit contacts and every source diameter upper bound, but it makes the third contact fail:

```text
|p'-z|^2 - 1 = -(D^2-|z-a|^2)/D^2 < 0.
```

Thus the two-neighbor fan reflection cannot be extended to this third-contact case as a unit-separated move. No global minimizer, KKT, large-source extraction, or Level I claim is part of the statement.

## Independent proof

Apply a rigid motion so that `p=0`, `a=-D u`, where `u` is a unit vector, and let `t` be a perpendicular unit vector. Solving the two circle equations `|p_±|=1` and `|p_±-a|=D` gives

```text
epsilon=1/(2D),  tau=sqrt(1-epsilon^2),
p_+=-epsilon*u+tau*t,  p_-=-epsilon*u-tau*t.
```

Write `z=-r*u-s*t`, where `r^2+s^2=1`. The source upper bound `|z-a|<=D` and lower bounds `|z-p_±|>=1` give, respectively,

```text
r>=epsilon,
epsilon*r + tau*|s| <= 1/2.
```

Set `theta=arcsin(epsilon)` and `phi=arcsin(|s|)`. Since `D>=2`, `0<theta<=arcsin(1/4)<pi/6`; also `tau=cos(theta)`, `r=cos(phi)`, and `|s|=sin(phi)`. The second inequality is `sin(theta+phi)<=1/2`. Here `theta+phi<2pi/3<5pi/6`, so it forces `theta+phi<=pi/6`. Therefore

```text
r >= (epsilon+sqrt(3)*tau)/2 > epsilon,
|s| <= (tau-sqrt(3)*epsilon)/2 < tau/2.
```

Define

```text
lambda=(r-epsilon)/(D-epsilon),
mu=(D-r)/(D-epsilon),
beta=(mu-s/tau)/2,
gamma=(mu+s/tau)/2.
```

Then `lambda>0`, `lambda+mu=1`, and `mu>1/2`: using `r<=1`,
`2(D-r)>D-epsilon` follows from `D-2+epsilon>0`. Since `|s|/tau<1/2`, both `beta,gamma` are positive. Directly comparing the `u` and `t` coordinates gives

```text
z=lambda*a + beta*p_+ + gamma*p_-,
lambda+beta+gamma=1.
```

All three barycentric coefficients are strictly positive, proving strict interior. Such a point is interior to the source convex hull and cannot be an actual diameter endpoint. In particular `mu=beta+gamma<1`, so

```text
|z-a| = |beta*(p_+-a)+gamma*(p_--a)|
       <= (beta+gamma)*D = mu*D < D.
```

The line `p_-p_+` is the line with `u`-coordinate `-epsilon`; reflecting `p=0` across it gives `p'=-2epsilon*u=-u/D=p+(a-p)/D^2`. The two contacts to `p_±` are fixed in length by reflection. Also `p'=(1-D^-2)p+D^-2a`; convexity of the norm and the old diameter bound show `|p'-q|<=D` for every fixed source point `q`. The unchanged pairs `a-p_±` remain at distance `D`, so the new diameter upper bound is preserved exactly.

Finally, with `|z-p|=1`, expand in these coordinates (or use the exact fan identity):

```text
|p'-z|^2-1 = -2r/D + 1/D^2
            = -(D^2-|z-a|^2)/D^2 < 0.
```

This is a strict lower-bound collision. The reflection preserves upper bounds and the two fan contacts, but cannot retain the third contact.

## Scope audit and disposition

The proof uses only finite-source unit separation, diameter `D>=2`, and the five displayed equalities. It does not use global optimality or the canonical full-core stress theorem. Since `z` is strictly interior to a triangle of source points, it cannot be a diameter endpoint. The claim is compatible with canonical `C-CENTERED-FAN-REFLECTIONS`, whose selected leaves have exactly two unit contacts; it explains why adding a third old contact is not a feasible extension of that move.

**REGRESSION VALID — promote** `C-THIRD-CONTACT-FAN-REFLECTION-COLLISION-REGRESSION`. Do not promote the source reports' contact-degree `3,4,5` assertion, stopped-train conclusions, or a population bound from this local geometry. No verifier is needed: the result is proved for the full real range `D>=2` by the analytic coordinate and barycentric argument above.
