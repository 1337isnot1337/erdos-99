> Generated reading edition · [exact source](../../../docs/reports/target_c_dominant_edge_contact_direction_energy_2026-09-05.md) · source SHA-256 `8509662d5118bede298e02fcf3fd1b9addbb7b6b1542a6fe111d5991c8496651`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-037C1676161C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C dominant-edge contact-direction energy

**Date:** 2026-09-05  
**Run type:** exact KKT coordinate-energy theorem  
**Target:** C98 near-one diameter edge; quantitative precursor to C19/C97  
**LEVEL I STATUS:** STILL OPEN

## 1. Exact coordinate Dirichlet identity

Fix any normalized KKT stress `(alpha,beta)` on a source of diameter `D`, with `C_+` and `H_+` its positive contact and diameter supports. For a unit vector `u`, put

`x_v=p_v dot u`.

KKT equilibrium at vertex `v` is

`sum_(vw in C_+) alpha_vw(p_v-p_w)=sum_(vh in H_+) beta_vh(p_v-p_h)`.

Dot with `u`, multiply by `x_v`, and sum over all vertices. Grouping each undirected edge at its two endpoints gives the exact scalar identity

`sum_(ij in C_+) alpha_ij (x_i-x_j)^2`

`= sum_(hk in H_+) beta_hk (x_h-x_k)^2`.      (1.1)

This is the coordinatewise Dirichlet-energy form of KKT equilibrium.

Because every positive contact has Euclidean length one, the normalized virial identity gives

`sum_(ij in C_+) alpha_ij = D^2`,

so the left side is at most `D^2` for every `u`.

## 2. Dominant diameter edge forces contact alignment

Let `za in H_+` be a diameter edge with

`beta_za=b`,

and set

`u=(p_a-p_z)/D`.

Its contribution to the right side of (1.1) is exactly

`bD^2`.

All other terms are nonnegative. Hence

`sum_(ij in C_+) alpha_ij [(p_i-p_j) dot u]^2 >= bD^2`.     (2.1)

Subtract from the virial identity `sum alpha=D^2` to obtain:

### Theorem — dominant-edge transverse contact-energy bound

`sum_(ij in C_+) alpha_ij [1-((p_i-p_j) dot u)^2]`

`<= (1-b)D^2`.                                      (2.2)

If `theta_ij` is the acute projective angle between the unit contact edge `ij` and the dominant diameter direction `u`, then

`1-((p_i-p_j) dot u)^2 = sin^2 theta_ij`,

so equivalently

`sum_(ij in C_+) alpha_ij sin^2 theta_ij <= (1-b)D^2`.        (2.3)

For every fixed `theta_0>0`, the total positive contact stress carried by edges whose projective angle from `u` is at least `theta_0` satisfies

`sum_(theta_ij>=theta_0) alpha_ij`

`<= (1-b)D^2/sin^2 theta_0`.                        (2.4)

Thus C98's `b=1-o(1)` conclusion forces all but `o(D^2)` of the entire positive contact-stress mass into every fixed angular cone about one line.

## 3. Exact full-support endpoint

If `b=1`, (2.3) gives

`sum_(ij in C_+) alpha_ij sin^2 theta_ij=0`.

Every `alpha_ij>0` on `C_+`, so every positive contact edge is parallel to `u`. Since the positive contact support is connected, all of its vertices lie on one line.

For an arbitrary sparse KKT stress this only says that **that stress support** is one-dimensional. It does not by itself identify the canonical maximal-support force hull, because other constraints might receive positive weight in another stress.

In the C65/C98 setting, however, the chosen relative-interior stress has full canonical support: its positive contact support is the entire canonical force-visible contact graph and its positive diameter support is the entire canonical diameter graph. Therefore `b=1` would make that canonical positive contact hull one-dimensional. C19 excludes a one-dimensional canonical force hull for every contact-minimal triangle-free global minimizer with `D>1`.

Hence:

### Corollary — no exact one-edge endpoint in the C65 full-support stress

For the relative-interior full-support stress used in C65-C101,

`max_(h in H) beta_h < 1`.

This exact exclusion does **not** require the pure simply connected rhombic model used by C97. It should not be generalized to arbitrary sparse KKT stresses without an additional maximal-support argument.

## 4. Quantitative significance

C98 gives one edge with `b=1-o(1)` in the C71-B near-zero phase. The theorem here upgrades that to a global mechanical concentration statement on the full positive contact graph:

`transverse positive-contact stress energy = o(D^2)`.

This is stronger than merely obtaining one near-geodesic contact path. It applies to the entire full-support positive contact network and the inequality itself does not use pure-rhombic train geometry.

The remaining quantitative problem is explicit:

> prove a uniform lower bound on transverse contact-stress energy for every genuinely two-dimensional full-support contact-minimal global minimizer, or show that `o(D^2)` transverse energy permits a finite same-diameter deformation that contradicts contact minimality/global optimality.

A bound of the form

`sum_C alpha_e sin^2 theta_e >= c D^2`

for some absolute `c>0` would immediately exclude C71-B once C98 gives `b->1`. No such bound is proved here.

## 5. Handoff

```text
Exact identity for every direction u:
  sum_C+ alpha_e (e dot u)^2
    = sum_H+ beta_h (r_h dot u)^2.

If za is a diameter edge of beta weight b and u=(a-z)/D:
  sum_C+ alpha_e sin^2 angle(e,u) <= (1-b)D^2.

Hence C98 beta=1-o(1) forces o(D^2) total transverse contact-stress energy globally.
At beta=1 the full-support C65 positive contact graph is collinear, so its canonical force hull is 1D, contradicting C19.

Scope warning: the beta=1/C19 conclusion is for the relative-interior full-support stress, not an arbitrary sparse KKT stress.

Next target: quantitative 2D-force-hull lower bound on this transverse contact energy, or a deformation theorem from o(D^2) transverse energy.
```
