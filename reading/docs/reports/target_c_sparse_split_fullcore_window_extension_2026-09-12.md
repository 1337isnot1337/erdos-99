> Generated reading edition · [exact source](../../../docs/reports/target_c_sparse_split_fullcore_window_extension_2026-09-12.md) · source SHA-256 `59f2bf8ca933efbaafc946cd22cfd5d0340f25986bb40030fc131b85504c5557`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-61ACE6FC9705","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — scalar extension of the sparse full-core exclusion

**Date:** 2026-09-12  
**Lifecycle:** proof-only candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The audited sparse/directional signed-return split excludes the proof-only full-core
window `sigma <= 0.0088`. The same inequalities have room to extend the scalar
arithmetic to

```math
\boxed{\sigma\le 0.0100},
```

provided the inherited Section-118 geometric hypotheses are valid on that slightly
larger interval. This note supplies the endpoint bounds and monotonicity checks. It
does not promote the extension or change the canonical route.

## 1. Scalar quantities

Use the notation of the sparse/directional report
`target_c_sparse_split_fullcore_closure_2026-09-12.md`. Let

```math
\sigma(\theta)=3\theta-2\pi-\sin(\theta/2)-2\sin\theta,
\quad
\lambda(\theta)=\sin(\theta/2),
\quad
U(\theta)=3\theta-2\pi.
```

Let `theta_8` be the canonical Section-101 root and
`phi_8=2pi-2theta_8`. At the proposed endpoint `s_0=0.0100`, the unique root of
`sigma(theta)=s_0` satisfies

```math
\theta_0=2.705034336685808\ldots,
\quad
U_0=1.831917702877839\ldots,
\quad
\lambda_0=0.976271542787591\ldots .
```

The tooth equation

```math
\sin Q+\sqrt3(1-\cos Q)-Q=y/2
```

has `Q(0.0100)=0.076568479487787...<0.077`.

Put `G(t)=(t-sin(t))/8` and

```math
A_0={\pi\over4}-G(\theta_0)
 -2G\left(\phi_8+{10s_0\over3}\right)
 -G\left({10s_0\over3}\right).
```

Direct evaluation gives

```math
A_0=0.469929027209250\ldots>0.4699.
```

## 2. Correlated product bound at `s_0`

For the slack simplex `x+y+z+w<=s_0`, the sparse split uses

```math
C=U_0-x-y+2z,
\qquad
B=Q(y)+{10s_0\over3}-{7x\over3}-{7y\over3}-{10z\over3}.
```

The endpoint bounds give `C>=U_0-s_0>1.8219` and `B<0.077+10s_0/3<0.1104`.
Consequently

```math
\partial_x(CB)=-B-{7C\over3}<0,
\qquad
\partial_z(CB)=2B-{10C\over3}<0.
```

The maximum is therefore at `x=z=0`. On that edge,

```math
P(y)=(U_0-y)\left(Q(y)+{10s_0\over3}-{7y\over3}\right).
```

For `0<=y<=s_0`, `Q(y)<=0.077` and
`Q'(y)=1/(2F'(Q(y)))>1/(2sqrt(3)0.077)>3.7`, where
`F'(q)=cos(q)+sqrt(3)sin(q)-1`. Hence the second factor has derivative greater than
`3.7-7/3>1.36`, and `P'(y)>0` from the preceding bounds. Thus

```math
CB\le P(s_0)
 =(U_0-s_0)(Q(s_0)+s_0)
 =0.157720645290016\ldots<0.158.
```

## 3. Strict scalar margin

The sparse signed-return contradiction subtracts `lambda z/(2-sqrt(3))` from the
return bracket. On the whole simplex, the coefficient bound is

```math
10+{1\over2-\sqrt3}>{25\over3}>{1\over2}.
```

Using the conservative endpoint bounds `lambda<=0.977`, `A_*(x,w)>=A_0>0.4699`,
`CB<0.158`, and `x+y+z+w<=0.0100`, the residual is strictly bounded below by

```math
\begin{aligned}
J-{\lambda z\over2-\sqrt3}
&>0.4699
 -0.977\left(10+{1\over2-\sqrt3}\right)(0.0100)
 -2(0.158)\\
&>0.0177.
\end{aligned}
```

Therefore the same necessary inequality
`lambda z >= (2-sqrt(3)) [J]_+` is impossible throughout this scalar simplex.

## 4. Scope and classification

This is a **proved candidate awaiting independent audit**, conditional only on the
already audited sparse/directional geometric inequalities continuing through
`sigma<=0.0100`. The extension uses no new source deletion, no affine-kernel claim
for contact-isolated points, and no global-optimality inference from the scalar
certificate. It removes at most an additional proof-only full-core slack interval;
the full-core regime above `0.0100` and the Type-I inactive-container branch remain
open.

The companion verifier is
`research/verify_target_c_sparse_split_fullcore_window_extension.py`.
