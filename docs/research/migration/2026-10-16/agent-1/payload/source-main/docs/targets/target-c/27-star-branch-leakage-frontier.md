# Target C — mechanical star branch-leakage frontier

**LEVEL I STATUS: STILL OPEN.**

Full proof: [target_c_star_branch_angular_leakage_2026-08-31.md](../../reports/target_c_star_branch_angular_leakage_2026-08-31.md).

## C71 — near-zero star stress cannot split across independent physical ports

Let `z` be the C66 mechanical star center. Put

`S_z=sum_(h incident z) beta_h`,

`delta_z=1-S_z`.

For `D>=20`, C18 puts all diameter partners of `z` in an angular interval of width
`Theta_D<pi/3`. Two distinct unit-contact neighbors of `z` are separated by at least
`pi/3`.

Define

`eta_D=pi/3-Theta_D`,

`c_D=cos(Theta_D/2)`,

`q_D=c_D sin(eta_D/2)>0`.

Then `q_D->0.0727...`.

Delete `z` from the positive contact graph. If a component `R` is attached to `z`
through exactly one contact edge, let `w_R` be the total `z`-star diameter weight whose
other endpoint lies in `R`.

Summing KKT equilibrium over `R` gives an exact cut-force identity. The star part of
the cut resultant has magnitude at least

`D c_D w_R`,

while the entire non-star diameter error has magnitude at most

`D lambda_R`, with `lambda_R<=delta_z`.

If `R,S` are two distinct single-port components, their physical port directions are
at least `pi/3` apart, while their star resultants are at most `Theta_D` apart. Hence
one port must rotate by at least `eta_D/2`, which forces

`delta_z >= q_D min(w_R,w_S)`.

Therefore the second-largest single-port star mass satisfies

`w_2 <= delta_z/q_D`.

Because a loaded boundary vertex has contact degree at most three, at most one
component of `C-z` can have two or more contact ports. Let `W_multi` be the star mass
in that possible multi-port component. Some single-port component then has

`w_R >= S_z-W_multi-2delta_z/q_D`.

Its unique contact port satisfies

`alpha_port >= D(c_D w_R-delta_z)`.

C66 gives

`delta_z <= (2pi/kappa_0) D epsilon`.

Consequently, along any C-II sequence with `D epsilon ->0`, either

1. a multi-port return/cycle component carries nonvanishing star mass; or
2. one single contact port carries `1-o(1)` of the diameter-star mass and
   `alpha_port >= (0.90348...-o(1))D`.

## Interaction with C68-C70

C68 says the contact-stress measure is almost radial around the same `z`. C70 says the
boundary electrical response is also asymptotically a star at `z`. C71 adds the
missing physical-port statement: the mechanical star cannot be divided macroscopically
between two independent contact branches.

## Next target

The near-zero C-II branch is reduced to two local mechanisms:

- **return/cycle:** prove quantitative stability of the C58/C60 separator limit and
  force non-`z` response mass, contradicting C70;
- **single-port spine:** iterate the `Omega(D)` port cut law. Either a return event is
  reached or a long nearly radial high-stress spine forms. C26 forbids a truly neutral
  unloaded degree-two corridor, so the remaining problem is to charge the necessarily
  positive but potentially tiny side incidence using C42/C48/C68.

No uniform lower bound on individual side stresses is assumed.