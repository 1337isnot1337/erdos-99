> Generated reading edition · [exact source](../../research/target_c_open_cell_strong_scc_one_host_cap_2026-10-04.md) · source SHA-256 `19784796af2b6276f8cdd41204fa4e96c2dab17ed477a3fb5fa4ccc2da8c13ad`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9402b55402c56a8376652c6b6ea2c04f3322a65a", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_open_cell_strong_scc_one_host_cap_2026-10-04.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "fac552ffce61c61db54462b1efb6eb972c6f404026af81d8ca635ef119e3cac9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: strong open-cell SCC forces one macroscopic host cap

Date: 2026-10-04
Base main: bb5f95e52fc5a7d0728ad29a01b7fbb3e92ba303
Status: proof-only Target C-II candidate; theorem-state authority unchanged.
LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.

This note stays entirely inside the nonconstant open-witness-cell strong-SCC Target C route.

Current main proves that the strong branch has a common maximal staircase of m nonempty actual-diameter support types, each with a physical representative of each strict transverse sign, and that all support types contain one common selected cut c. Choose one representative of each sign over each support type. These are 2m distinct actual diameter bars. Every chosen bar crosses tau_c, so the physical graph F of the chosen bars is bipartite. Canonical C-WOODALL implies that this bipartite diameter subgraph is a forest. Hence
$$
|V(F)|=2m+c(F)\ge 2m+1. \tag{1}
$$

For the retained complete O--O rectangle, current main gives four disjoint resolved outer-boundary host intervals in cyclic order
$$
I_A^+,\ I_B^+,\ I_A^-,\ I_B^- . \tag{2}
$$
The endpoint resolution is away from source vertices. Every actual diameter endpoint is an extreme source-hull vertex, so every vertex of F belongs to exactly one host interval. Therefore one host X_* contains at least
$$
\boxed{r_*:=|V(F)\cap X_*|\ge\left\lceil{2m+1\over4}\right\rceil} . \tag{3}
$$

Let Q_*=V(F)\cap X_* and C_*=\operatorname{conv}Q_*. The diameter-endpoint capacity theorem already on main is independent of threshold phase. For r>=8 distinct actual diameter endpoints in a unit-separated diameter-D source it gives
$$
\operatorname{width}(C)>{r^2\over256(D+r)}, \tag{4}
$$
$$
\operatorname{area}(C)>{r^4\over2\cdot256^2(D+r)^2}. \tag{5}
$$
Thus, for m>=14,
$$
\boxed{\operatorname{width}(C_*)>{r_*^2\over256(D+r_*)}}, \tag{6}
$$
$$
\boxed{\operatorname{area}(C_*)>{r_*^4\over2\cdot256^2(D+r_*)^2}} . \tag{7}
$$

For the global minimum-diameter source, the same current-main theorem gives
$$
\boxed{|P\cap C_*|>{2\over\sqrt3}\operatorname{area}(C_*)-2\pi D+1}. \tag{8}
$$
The population is full-source population; contact-isolated points are retained.

The current complete-grid extraction gives
$$
m\ge(c_*-o(1))D,\qquad
c_*={\kappa^4\over16\pi^3 C_KM_K}>0. \tag{9}
$$
Put rho=c_*/2. Then r_*/D>=rho-o(1), and (6)--(8) imply
$$
\boxed{\liminf{\operatorname{width}(C_*)\over D}
\ge{\rho^2\over256(1+\rho)}>0}, \tag{10}
$$
$$
\boxed{\liminf{\operatorname{area}(C_*)\over D^2}
\ge{\rho^4\over2\cdot256^2(1+\rho)^2}>0}, \tag{11}
$$
$$
\boxed{\liminf{|P\cap C_*|\over D^2}
\ge{\rho^4\over\sqrt3\,256^2(1+\rho)^2}>0}. \tag{12}
$$

Therefore every sufficiently large strong nonconstant open-cell survivor has one complete-grid host containing Omega(D) distinct actual diameter endpoints, whose convex hull has macroscopic width, quadratic area, and quadratic full-source population.

This applies before the latest main split into the pure one-sided staircase star, the A-full/B-proper packet, and the corner packet. In particular the pure-star case is already forced into this macroscopic one-host geometry, and corner multiplicity cannot hide the strong staircase on a bounded physical vertex set.

Adversarial scope checks:

- This does not identify C_* with an inactive chamber, harmonic cell, loaded-hull cell, or exterior cap.
- It does not force two disjoint quadratic host caps; one host may contain most physical vertices.
- No unmerged sign-to-side theorem is used.
- No KKT multiplier lower bound or bounded support multiplicity is used.
- No computation, verifier, numerical experiment, or CI result is a proof premise.

The exact remaining strong-branch obligation is to connect the macroscopic host cap C_* to the actual positive-contact/loaded-hull structure strongly enough to pay canonical Target-C face/train currency, or use it in a same-cardinality strict-diameter competitor. The separate non-strong condensation alternative remains the inverse-D inactive near-unit/near-diameter pair.

Disposition: proof-only Target C candidate. C-II and Level I remain open.
