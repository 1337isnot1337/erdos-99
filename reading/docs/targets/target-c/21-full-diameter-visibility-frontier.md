> Generated reading edition · [exact source](../../../../docs/targets/target-c/21-full-diameter-visibility-frontier.md) · source SHA-256 `d6d46cbb91e16b40dbe2699f837bc835da5a62407fea38c84f69a1bad118da74`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — full-diameter-visibility frontier

**LEVEL I STATUS: STILL OPEN.**

Full proof: [target_c_secondary_diameter_visibility_2026-08-31.md](../../reports/target_c_secondary_diameter_visibility_2026-08-31.md).

## C65 — every actual diameter pair can be made force-visible

Choose a triangle-free global minimizer minimizing first the number of unit contacts and then, within that class, the number of diameter pairs.

Gate C-I gives `C=C_*`.

If a weak diameter row remained, C6 supplies a relative-interior critical velocity that vanishes on every strong row and strictly shortens every weak diameter row. C63 integrates that velocity to an actual nearby global minimizer while preserving all strong rows; weak rows remain strict and inactive rows retain strict slack.

The new contact graph is a subgraph of `C_*=C`. Primary contact minimality prevents any contact loss, so the contact graph is unchanged. The diameter graph is a strict subgraph of the original, contradicting the secondary normalization.

Therefore

`C=C_*` and `H=H_*`.

A relative-interior normalized KKT stress is positive on the entire actual contact graph and the entire actual diameter graph.

## Rattler consequence

Every positive diameter endpoint belongs to the unique nontrivial positive contact component. Since every actual diameter edge is positive, a contact-isolated source point cannot be a diameter endpoint.

Hence every point outside the force-visible contact core satisfies

`1 < |p_i-p_j| < D`

for every other source point. The residual non-core population consists only of fully inactive rattlers; there are no hidden weak diameter endpoints.

## Updated C-II problem

The response boundary is the full actual diameter-endpoint set. All diameter-thrackle structure and all C53-C64 response inequalities apply to the complete source diameter graph.

The remaining bulk gap is sharper: either eliminate a macroscopic fully inactive rattler population or derive a contradiction directly from the now-fully-visible contact/diameter framework.
