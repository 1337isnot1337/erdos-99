<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b0d444a18078a52e2d2806a54088ad1e6397113a", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_common_transversal_rooted_shore_sign_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b00e0fa63ed89ff2c9bdd678c0cb8fac96f79a0704d81cbdf3ca63b0ec9f044e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a common oriented transversal fixes the Euclidean sign of rooted leaf-shore vectors

**Date:** 2026-09-15  
**Status:** proof-only orientation bridge / dependency repair  
**Scope:** any ordered family of pairwise noncrossing leaf trains crossed by one canonically oriented transversal train in the phase-pure Section-76 crossing regime  
**Dependencies:** canonical Section 76.1--76.3; complement-dual path/rooted shore coordinates  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Several adjacent-cut arguments use two orientation systems for the same leaf train:

1. a real phase representative `beta_j` and its oriented unit edge vector `v_j`; and
2. the rooted-shore vector `u_j` used in Section-157 cut resultants and exact O--O shears.

Projective phase alone does **not** determine whether `u_j=v_j` or `u_j=-v_j`. The common transversal train fixes that sign.

### Theorem TS — transversal/rooted-shore sign

Let `gamma` be a canonically oriented train which crosses, in order, pairwise noncrossing leaf trains

\[
\tau_1,\ldots,\tau_m.
\]

Assume every `gamma x tau_j` crossing lies in the phase-pure Section-76 regime, and let `v_j` be the oriented leaf unit-edge vector supplied by the real lift there. Root the complement-dual path at the region containing the incoming end of the oriented centerline of `gamma`.

Then for every selected leaf cut,

\[
\boxed{u_j=v_j.}
\tag{TS.1}
\]

In particular, if `beta_j` is the real argument of `v_j`, then

\[
\boxed{\arg u_j=\beta_j\pmod{2\pi},}
\tag{TS.2}
\]

not merely modulo `pi`.

---

## Proof

Canonical Section 76.3 gives the local crossing sign exactly. At a crossing of an `A`-train with oriented unit edge vector `u_a` and a `B`-train with oriented unit edge vector `v_b`, the local **forward centerline displacement on the canonically oriented A-train is `v_b`**.

Apply this with `A=gamma` and `B=tau_j`. As the oriented centerline of `gamma` passes through the crossing rhombus, it moves from the complement region immediately before the leaf cut to the complement region immediately after it by a vector parallel to, and with the same Euclidean sign as, `v_j`.

Because the selected leaves are pairwise noncrossing and `gamma` crosses each exactly once, their complement regions met by `gamma` form the simple dual path

\[
R_0\xleftrightarrow{\tau_1}R_1
\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m
\]

in this forward order. Root the path at `R_0`. Removing dual edge `tau_j` leaves a root-side component containing `R_0` and a far-side component containing `R_j,\ldots,R_m`.

The Section-157/rooted-shore convention orients the train contact vector from the root-side shore into the far-side shore. But the forward crossing of `gamma` across `tau_j` is exactly from the root-side region to the far-side region, and Section 76.3 says that forward displacement has Euclidean sign `v_j`. Therefore the rooted-shore contact vector is

\[
u_j=v_j.
\]

This proves (TS.1)--(TS.2). `square`

---

## Consequence for adjacent physical strips

For the physical layer between consecutive nested cuts `tau_j,tau_{j+1}`, orient both boundary contacts from the fixed exterior into the middle layer. The left boundary vector is

\[
a=u_j=v_j,
\]

while the right boundary vector is

\[
b=-u_{j+1}=-v_{j+1}.
\]

Hence, whenever the real leaf phases satisfy

\[
|\beta_{j+1}-\beta_j|<\pi,
\]

the physical contact-opening cone has angular width exactly

\[
\boxed{
\pi-\angle(a,b)
=|\beta_{j+1}-\beta_j|.
}
\tag{TS.3}
\]

This validates the physical-sign step used by `target_c_phase_optimized_two_bar_localization_2026-09-15.md`.

---

## Scope audit

- Nested-shore orientation by itself does not determine Euclidean train-vector signs; the common **oriented transversal** is essential.
- The theorem uses the actual Section-76 local crossing orientation, not projective closeness alone.
- Reversing the orientation of `gamma` reverses the dual-path root and all corresponding shore signs consistently, so the statement is root-choice invariant in the required sense.
- No new numerical or C-II closure claim is made.

**Disposition:** proved the missing Euclidean-sign bridge between real phase lifts and rooted Section-157 leaf vectors on a common-transversal path.
