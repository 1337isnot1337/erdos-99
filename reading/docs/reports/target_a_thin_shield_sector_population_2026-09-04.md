> Generated reading edition · [exact source](../../../docs/reports/target_a_thin_shield_sector_population_2026-09-04.md) · source SHA-256 `e8bc2c050b222be284e41bb1cbbd007b41b10f4bee33527cbc4d31373a9dc9e9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "23ced1e94200c4686cb9db7844ec5d5f07d7ef87", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_a_thin_shield_sector_population_2026-09-04.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ed1b73509cba276b9c3c97d783725595132147813fd079275d33dbab184ca6b2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — Target A thin-shield sector population identity

**Date:** 2026-09-04; corrected 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact population form of the contracted Section 173 theorem  
**Target:** locked stress-fan Schur branch  
**Status:** LEVEL I STILL OPEN

## 0. Audit correction

The original version of this report omitted one class of deleted left vertices after
contracting the fixed basis matching.  If a shielded interior lattice site
`z in R_Sigma cap Z` is matched to `b=mu_0^{-1}(z)`, then the contracted pair is
removed even when `b` is not itself a contact vertex of `Sigma`.  The old definition
`X_i=(X^*\V(Sigma)) cap D_i` therefore did not decompose as claimed.

The contracted Schur/Hall theorem

`zeta >= delta_Sigma-|R_Sigma|`

is unaffected.  Only the population rewrite TP2--TP3 required correction.  The
corrected statement below removes the matched basis partners explicitly and yields a
new all-sector dead-sink criterion.

## 1. Setup and the matched basis shield

Let `Sigma` be a finite unit-contact shield in the actual response optimum `X^*`. Use
the Section 173 right-shore shield

`R_Sigma=(union_{q in V(Sigma)} N_Lambda(q)) cap Y_in`.

Split it as

`R_Z=R_Sigma cap Z`,

`R_O=R_Sigma cap O`.

Fix the `Z`-perfect basis matching

`mu_0:B->Z`

and put

`B_R=mu_0^{-1}(R_Z)`.

Thus the contracted shield removes every matched pair `b--mu_0(b)` with
`b in B_R`, in addition to the nonbasis contact vertices on `Sigma`.

Every basis contact vertex belongs to `B_R`.  Indeed, if `b in B cap V(Sigma)` then
its matching edge satisfies `|b-mu_0(b)|<1`, so

`mu_0(b) in N_Lambda(b) subset R_Sigma`,

and because `mu_0(b) in Z`, it lies in `R_Z`.  Hence

`B cap V(Sigma) subset B_R`.

Let `D_1,...,D_k` be the components of `K^*\|Sigma|`.

For each sector define

`Z_i=(Z\R_Z) cap D_i`,

and let

`B_i=(B\B_R) cap D_i`.

## 2. Exact basis balance with the thin shield

### Lemma TP1

For every sector,

`|B_i|=|Z_i|`.

### Proof

Take `z in Z\R_Z` and put `b=mu_0^{-1}(z)`.  Since `z` is unshielded,
`b notin B_R`; in particular `b notin V(Sigma)` by the inclusion above.

If the matching segment `bz` crossed `|Sigma|`, Lemma 169.5 would put the right
endpoint `z` in the strict lattice neighborhood of a contact vertex of `Sigma`, hence
in `R_Sigma cap Z=R_Z`, contradiction.  Therefore `b,z` lie in one sector.

Conversely every `b in B\B_R` has `mu_0(b) in Z\R_Z`, and the same argument puts the
pair in one sector.  Restricting `mu_0` gives a bijection `B_i->Z_i`.  QED.

The full unit tube of Section 174 is unnecessary for basis balance.  Its extra role
was to make exterior sink sets disjoint.

## 3. Corrected thin-shield local population identity

Define the surviving left population in sector `i` by

`X_i^surv=(X^*\(V(Sigma) union B_R)) cap D_i`.

Also put

`C_i^circ=(C^circ\V(Sigma)) cap D_i`,

`C_i^partial=(C^partial\V(Sigma)) cap D_i`.

Because `B_R subset B` and every basis contact vertex is already in `B_R`, the three
families partition the surviving left shore:

`X_i^surv=B_i sqcup C_i^circ sqcup C_i^partial`.

Using Lemma TP1 gives the corrected identity.

### Proposition TP2

For every sector,

`|C_i^partial|=|X_i^surv|-|Z_i|-|C_i^circ|`.

Let `O_i` be the Section 173 set of surviving exterior sinks
`o in O\R_O` having at least one surviving response neighbor in sector `D_i`.  The
sets `O_i` may overlap.  Therefore

`|C_i^partial|-|O_i|`

`=|X_i^surv|-|Z_i|-|O_i|-|C_i^circ|`.

## 4. Exact coarse Hall deficiency in corrected population variables

Section 173 forms the coarse bipartite graph with `|C_i^partial|` left copies of
sector `i` and right vertex set `O\R_O`, where `o` is adjacent to sector `i` exactly
when `o in O_i`.  Its deficiency is

`delta_Sigma`

`=max_{J subseteq {1,...,k}}`

` [sum_{i in J}|C_i^partial|-|union_{i in J}O_i|]_+`.

Substitute Proposition TP2.

### Theorem TP3 — corrected thin-shield sector population formula

`delta_Sigma`

`=max_J [sum_{i in J}(|X_i^surv|-|Z_i|-|C_i^circ|)`

`         -|union_{i in J}O_i|]_+`.

The contracted Schur theorem remains

`zeta >= delta_Sigma-|R_Sigma|`.

Thus the locked branch closes if the corrected coarse Hall expression is at least

`s+|R_Sigma|`.

For the Section 172 locked fan, the pointwise common-neighbor theorem still gives

`|R_Sigma|<=3|V(Sigma)|`.

## 5. Exact all-sector sum and dead exterior sinks

Define

`O_dead=(O\R_O)\(union_i O_i)`

and

`d_dead=|O_dead|`.

These are unshielded exterior lattice sites with no surviving response neighbor in
any geometric sector after the contact vertices and contracted basis-shield pairs are
removed.

Take `J={1,...,k}` in the coarse Hall expression.  First,

`sum_i |C_i^partial|=|C^partial|-|C^partial cap V(Sigma)|`.

This also follows directly from the corrected population formula.  Explicitly,

`sum_i |X_i^surv|`

`=|X^*|-|V(Sigma) union B_R|`,

`sum_i |Z_i|=|Z|-|R_Z|`,

`sum_i |C_i^circ|=d_int-|C^circ cap V(Sigma)|`.

Since `|B_R|=|R_Z|` and

`B_R cap V(Sigma)=B cap V(Sigma)`, 

all matched-basis terms cancel, leaving exactly the displayed terminal count.

Also

`|union_i O_i|=|O|-|R_O|-d_dead`.

The sector-deficit duality identity SD1 gives

`|C^partial|-|O|=s-J_outer`,

where

`J_outer=rho^dagger-|Y_0|`

is the phasewise outer-collar demand.  Therefore the all-sector coarse Hall value is

### Theorem TP4 — exact dead-sink identity

`sum_i |C_i^partial|-|union_i O_i|`

`=s-J_outer-|C^partial cap V(Sigma)|+|R_O|+d_dead`.

Consequently

`delta_Sigma`

`>= [s-J_outer-|C^partial cap V(Sigma)|+|R_O|+d_dead]_+`.

The exterior shield population `|R_O|` appears with the favorable sign because those
sinks are removed from the coarse right shore.

## 6. A sufficient dead-sink closure criterion

Since

`|R_Sigma|=|R_Z|+|R_O|`,

Theorem TP4 reaches the sufficient threshold

`delta_Sigma>=s+|R_Sigma|`

whenever

### Corollary TP5 — dead-sink criterion

`d_dead >= J_outer + |C^partial cap V(Sigma)| + |R_Z|`.

Under TP5 the contracted Schur theorem gives `zeta>=s`, which closes Target A for that
phase.

This criterion is stricter than necessary because it uses only the all-sector Hall
set; a proper subset of sectors may give larger deficiency.  Its advantage is that it
contains no hidden basis population and the entire exterior shield term cancels.  The
only explicit shield cost is the number of shielded **interior** lattice sites `R_Z`,
plus the Schur terminals physically lying on `Sigma`.

## 7. Frontier and regression status

The old TP2/TP3 formulas using `X_i=(X^*\V(Sigma)) cap D_i` are retracted.  They
omitted basis vertices in `B_R\V(Sigma)` and must not be cited.

The following earlier results survive unchanged:

1. the contracted contact-shield Schur/Hall theorem
   `zeta>=delta_Sigma-|R_Sigma|`;
2. the pointwise bound `|R_Sigma|<=3|V(Sigma)|` for the locked connected fan;
3. the sector-deficit duality identity `|C^partial|-|O|=s-J_outer`;
4. the right-deficiency geometric-tube theorem, which is formulated directly in terms
   of right-shore tube vertices and does not use the erroneous TP2 population
   decomposition.

The new exact target supplied by this correction is geometric: force enough
unshielded dead exterior sinks, or obtain a stronger proper-sector Hall set, relative
to `J_outer`, the fan terminals, and the interior shield population.
