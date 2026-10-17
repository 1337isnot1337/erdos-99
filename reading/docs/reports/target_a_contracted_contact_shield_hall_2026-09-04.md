> Generated reading edition · [exact source](../../../docs/reports/target_a_contracted_contact_shield_hall_2026-09-04.md) · source SHA-256 `9432d5c127259871743106117155c3875a554ce9c6cba070ca7b3990ae192e87`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5ecf10fbc70f871ac77b454e5190c167865d6fe6", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_a_contracted_contact_shield_hall_2026-09-04.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d890fb7d9ba56ed18def9de9bc9907aca86b56ba1d2f2ea0cf80614432780790"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — Target A contracted contact-shield Hall theorem

**Date:** 2026-09-04  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact strengthening of Section 173  
**Target:** locked stress-fan Schur branch  
**Status:** LEVEL I STILL OPEN

## 1. Section 173 needs no contact-vertex path charge after contraction

Retain the Section 173 contact shield

`R_Sigma=(union_{q in V(Sigma)} N_Lambda(q)) cap Y_in`.

Let

`mu_0:B->Z`

be the fixed `Z`-perfect basis matching of Section 113 and contract each matched directed edge `z->b` to one internal gammoid vertex.

Shield in the contracted graph:

- every matched pair whose `Z` endpoint lies in `R_Sigma cap Z`;
- every terminal in `C^partial cap V(Sigma)`;
- every exterior sink in `R_Sigma cap O`.

There is no separate basis-vertex cost for `B cap V(Sigma)`: if `b` is a contact vertex, then its matched site `z=mu_0(b)` satisfies `|b-z|<1`, hence `z in R_Sigma` already.

A contact vertex in `C^circ` cannot occur on a directed Schur path at all.

Thus the contracted shield path capacity is

`|R_Sigma| + |C^partial cap V(Sigma)|`.

## 2. Sector trapping survives

Take a Schur path avoiding the contracted shield. Every internal right vertex lies in `Z\R_Sigma`. By Lemma 173.1 / Lemma 169.5, every surviving response edge avoids `|Sigma|`. Therefore every internal matched pair and every internal alternating step lies in one component `D_i` of `K^*\|Sigma|`.

The final exterior sink may be adjacent to several sectors; Section 173's coarse sector graph `H_Sigma` handles this overlap exactly. Let

`nu_Sigma`

be its maximum matching and

`delta_Sigma=sum_i |C_i|-nu_Sigma`

its Hall deficiency, equivalently

`delta_Sigma = max_{J subseteq {1,...,k}} (sum_{i in J}|C_i| - |union_{i in J} O_i|)_+`.

## 3. Improved Schur rank and nullity

### Theorem CH1 — contracted contact-shield rank

`rank S <= |R_Sigma|+|C^partial cap V(Sigma)|+nu_Sigma`.

### Proof

In a maximum vertex-disjoint directed Schur linkage, at most one path uses each shielded contracted `B-Z` pair, each shielded sink, or each shielded terminal. The first two kinds together are indexed by the distinct right vertices in `R_Sigma`, so at most `|R_Sigma|` paths use them. At most `|C^partial cap V(Sigma)|` further paths start at shielded terminals.

Delete these paths. Every remaining path is internally trapped in one geometric sector and induces one edge in the coarse sector-sink matching of Section 173. Hence at most `nu_Sigma` paths remain. QED.

Now

`|C^partial|=|C^partial cap V(Sigma)|+sum_i |C_i|`.

Subtract the rank bound and cancel the shielded terminal count:

### Corollary CH2 — contracted contact-shield nullity

`zeta >= delta_Sigma-|R_Sigma|`.

This strictly improves promoted (173.18), which charged

`|W_Sigma\C^partial|=|R_Sigma|+|V(Sigma)\C^partial|`.

All nonterminal contact vertices disappear from the Schur path penalty.

## 4. Explicit fan bound

A generic response point has at most four strict triangular-lattice neighbors, so Section 173 already proves

`|R_Sigma|<=4|V(Sigma)|`.

Therefore

`zeta >= delta_Sigma-4|V(Sigma)|`.

For the locked three-channel fan, a sufficient exact theorem is now

`delta_fan >= s+|R_Sigma|`,

or crudely

`delta_fan >= s+4|V(Sigma)|`.

This replaces the Section 173 sufficient bound

`delta_fan >= s+|R_Sigma|+|V(Sigma)\C^partial|`

and also dominates the thicker Section 174 tube-shield route for purposes of Schur rank: sink overlap is retained in `delta_fan` rather than removed by a larger geometric tube.

## 5. Frontier

The locked branch is reduced to one finite three-sector Hall inequality with a pure right-shore shielding cost:

`delta_fan >= s+|R_Sigma|`.

The remaining geometry must force enough sector Hall deficiency. Basis closure, basis-vertex count, and contact-vertex count are no longer independent losses.
