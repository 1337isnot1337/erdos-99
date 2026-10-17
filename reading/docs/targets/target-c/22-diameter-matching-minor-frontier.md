> Generated reading edition · [exact source](../../../../docs/targets/target-c/22-diameter-matching-minor-frontier.md) · source SHA-256 `b48090a824e8f3492ca7105254af14ff0048de19b957ed94668006219819c19c`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — diameter-matching circular-minor frontier

**LEVEL I STATUS: STILL OPEN.**

Full proof: [target_c_diameter_matching_circular_minor_transport_2026-08-31.md](../../reports/target_c_diameter_matching_circular_minor_transport_2026-08-31.md).

## C66 — disjoint diameter weight cannot survive a near-zero response defect

Let

`epsilon = sum_(b<k)c_bk - 1 = tr(Lambda-L_H)/2`.

For cyclic terminals `a,b,c,d`, circular-minor positivity gives

`c_ac c_bd <= c_ab c_cd`,

`c_ac c_bd <= c_ad c_bc`.

If `ac` and `bd` are disjoint diameter edges, C43 implies one of the two noncrossing side pairings consists of two uniformly short pairs. Thus that short pairing has total response conductance at least

`2 sqrt(c_ac c_bd)`.

For a diameter matching `J`, the side edges forced by different unordered pairs of matching edges are distinct. C41 therefore gives the aggregate transport inequality

`epsilon >= 2 gamma_0 sum_{e<f in J} sqrt(c_e c_f)`.

PSD of `M=Lambda-L_H` gives `|c_e-beta_e|<=sqrt(M_uu M_vv)` on a diameter edge `e=uv`. Matching endpoints are disjoint, so

`sum_(e in J)|c_e-beta_e| <= epsilon`.

Hence two disjoint diameter edges with `beta>=tau` force

`epsilon >= kappa_0 tau`,

where `kappa_0=2gamma_0/(1+2gamma_0)`.

Therefore, if `epsilon<kappa_0 tau`, every `tau`-heavy diameter edge intersects every other. C43 excludes diameter triangles, so all heavy edges share one vertex.

The Hopf-Pannwitz planar diameter bound and hull perimeter give

`|H|<=|B|<=pi D`.

Taking `tau=2epsilon/kappa_0` yields one diameter vertex `z` with

`sum_(e incident z) beta_e >= 1-(2pi/kappa_0)D epsilon`.

Thus any C-II sequence with `D epsilon -> 0` has its **mechanical normalized diameter stress** concentrated on one star. The abstract near-star electrical regression is no longer a general obstruction in this regime; the only surviving near-zero phase is a mechanical stress-star phase.

## Next target

Exclude that stress-star phase using the unit-contact equilibrium equations, terminal degree at most three, fixed total contact-stress tensor, and `Theta(D)` full diameter endpoints; equivalently prove `epsilon=Omega(1/D)` there.
