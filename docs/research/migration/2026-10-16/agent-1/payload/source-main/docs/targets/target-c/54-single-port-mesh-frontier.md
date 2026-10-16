# Target C — C98 single-port mesh concentration frontier

**LEVEL I STATUS: STILL OPEN.**

Proof: [target_c_single_port_mesh_defect_2026-09-05.md](../../reports/target_c_single_port_mesh_defect_2026-09-05.md).

Audit: [target_c_c98_single_port_mesh_audit_2026-09-05.md](../../audits/target_c_c98_single_port_mesh_audit_2026-09-05.md).

C98 closes the diffuse/multi-leaf escape in C71-B.

Let `R` be a component of `C-z` attached to the C66 star center `z` by one physical contact edge of stress `A`. Eliminating the unique port gives, for loaded terminals `s,t in R`,

`c_st >= c_zs c_zt/A`.

KKT cut equilibrium gives `A<=D`. If `a,b` are distinct diameter partners of `z`, C18 makes them uniformly subdiametral, with normalized squared-distance deficit at least

`Gamma_D=1-4 sin^2(Theta_D/2)>0`.

C41 therefore yields, for the `z`-star leaves `L_R` and `C_R=sum_(a in L_R)c_za`,

`D epsilon >= (Gamma_D/2)[C_R^2-sum_a c_za^2]`.

C64 gives `|beta_za-c_za|<=epsilon` on every diameter edge. Since the diameter graph has `O(D)` edges, aggregate star beta mass and response mass differ by `O(D epsilon)`.

In C71-B, `D epsilon->0` and the beta star mass in `R` tends to one. Hence `C_R->1`, the Herfindahl defect tends to zero, and one actual diameter edge has

`beta_(za_*)=1-o(1)`.

Equivalently C81's star-cancellation scalar tends to zero, so the star-to-leaf contact flow uses `D^2-o(D^2)` total contact-capacity mass.

## Current near-zero split

The `D epsilon->0` phase is reduced to:

1. **return/multi-port:** a component of `C-z` attached through at least two physical contacts carries nonvanishing star mass; or
2. **one-leaf near-chain:** one actual diameter edge has beta weight `1-o(1)` and an almost fully saturated depth-`D` contact flow joins its endpoints.

C97 excludes the exact pure-rhombic straight-chain endpoint of branch 2. The next theorem is quantitative stability of branch 2 or exclusion of branch 1.
