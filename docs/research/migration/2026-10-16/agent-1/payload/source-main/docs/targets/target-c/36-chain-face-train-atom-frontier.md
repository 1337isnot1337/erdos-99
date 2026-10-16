# Target C — C80 exact chain-face train atom frontier

**LEVEL I STATUS: STILL OPEN.**

Full proof: [target_c_chain_face_train_atom_2026-08-31.md](../../reports/target_c_chain_face_train_atom_2026-08-31.md).

C76 classifies an exact KKT star face as one straight `D`-edge unit-contact chain
`z=x_0,...,x_D=a`, with `beta_za=1` and every chain contact stress `alpha=D`.

In the pure simply connected rhombic train-coordinate setting of Target B, C80 proves:

- the `D` chain contacts belong to `D` distinct train tracks;
- those `D` tracks are exactly the tracks separating `z` and `a`;
- all have the chain direction;
- the chain diameter gradient is identically zero on train-angle space.

If `P` is this `D`-track atom, then the exact chain-bar Hessian is

`H_h[v,v] = -D sum_(tau in P)(v_tau-mean_P(v))^2`.

Thus the chain bar has negative rank `D-1` and no positive train-angle curvature. Its
kernel consists exactly of modes in which the `D` chain tracks co-rotate.

## Cross-route consequence

Target B's first-order-neutral train space `L` remains macroscopic because the chain
bar contributes no gradient row. Every

`v in L` that is nonconstant on `P`

strictly shortens the chain diameter to second order. Any local/global minimizer with
the exact C76 face must therefore obtain all compensating second/higher-order blocking
from other active diameter bars, even though they carry zero beta weight in the C76
stress.

This identifies the correct operator for a near-face stability theorem. If
`S_z=1-o(1)` can be shown to preserve an `Omega(D)`-dimensional negative spectral
subspace of the KKT-weighted train Hessian, the Target B Sections 42--43 blocker
network would have to overcome it using only the vanishing residual beta mass.

## Limitation

C80 is exact and pure-rhombic. It does not yet provide uniform stability across
changing configurations, and C66 does not by itself concentrate beta on one diameter
edge.