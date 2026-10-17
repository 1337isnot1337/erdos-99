> Generated reading edition · [exact source](../../research/target_c_high_t_collar_pentagon_transport_2026-10-03.md) · source SHA-256 `980b892f97cd2edc3681622529e195d9ee74c4f56c7b3516379993ed42cd7224`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "7a4a970b8d026bf323efd2f834a9f4cb5029da4c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_collar_pentagon_transport_2026-10-03.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "87464df313df17a39cc50c64581e67a559f5212d0e51f9c96800f3a7619e27ba"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: collar-to-pentagon train transport

Date: 2026-10-03
Base main: af24b1f7dad924fa564786b2796010bbbdda717e
Status: proof-only candidate, noncanonical. C-II and Level I remain open.

Scope: current Target-C full-core/no-macroscopic-container Type-II high-t,
low-outer-walk, square-root-diameter-matching branch only.

Let t_D=(q-k)/D and let S=N4_boundary be the selected strict boundary-rhombus
count from target_c_high_t_boundary_rhombus_floor_2026-10-02.md. Let f be the
number of bounded nonquadrilateral contact faces and
Q=sum_G(deg(G)-4). Let x_B=b_out-q, nu=nu(H), and P_F=per(F).

Define I5_coll to be the number of terminal face-side occurrences on bounded
pentagons belonging to collar trains whose other end is a selected good loaded-hull
collar side, after the O(1) double-good-end trains from the corrected good-end
theorem are discarded.

The new finite inequality is

    I5_coll >= S - 2 x_B - 4 - 6(Q-f).                 (1)

Combining it with the finite collar floor and the exact outer-face ledger gives

    I5_coll
      >= 10 P_F - 18 t_D D + 6 f - 6 nu - 11 x_B - 12. (2)

Consequently, if t_D <= T+o(1) in the current high-t scope, then

    liminf I5_coll/D
      >= 10 pi + 3(rho+g) + 6 sqrt(Delta_2) - 21 T,     (3)

where rho=cos(rho), g=0.007707, and Delta_2=pi/(2 sqrt(3)).

At the current endpoint T=1.860 this is greater than 0.3101. Therefore

    I5_coll > 0.3101 D - o(D),                           (4)

and at least 0.0620 D-o(D) distinct bounded pentagons are hit by these
hull-to-pentagon collar trains.

## Proof of the finite capacity inequality

The corrected collar good-end theorem gives

    E_exc_coll >= S - 2 x_B - 4,                         (5)

where E_exc_coll counts terminal incidences of collar trains on bounded
exceptional faces.

Let P5 be the number of pentagons and N6=f-P5. The total boundary-occurrence
capacity of all exceptional faces of degree at least six is

    C6 = 4 N6 + (Q-P5)
       = 4f + Q - 5P5.                                  (6)

Since every degree-at-least-six face contributes at least two to Q,

    Q >= P5 + 2(f-P5) = 2f-P5,

so P5 >= 2f-Q. Hence

    C6 <= 6(Q-f).                                       (7)

Even if every available degree-at-least-six occurrence absorbs a collar endpoint,
the remaining incidences must land on pentagons. Equations (5) and (7) prove (1).

## Insert the collar and outer ledgers

The current collar theorem gives

    S >= 4 P_F - 6 t_D D - 6 nu - 9 x_B - 8.            (8)

Substitute (8) in (1):

    I5_coll
      >= 4 P_F - 6 t_D D - 6 nu - 11 x_B - 12
         - 6Q + 6f.                                      (9)

The exact loaded-hull face identity b_out+Q=2 t_D D and b_out>=P_F give

    Q <= 2 t_D D - P_F.                                 (10)

Equation (10) in (9) proves (2).

## Asymptotic high-t specialization

The modern train-slack theorem gives

    liminf tau_D/D >= rho+g,
    tau_D = t_D D + 2f - 2 sqrt(R4),

and Type II gives sqrt(R4)/D -> sqrt(Delta_2). Therefore

    6f/D
      >= 3(rho+g-t_D+2 sqrt(Delta_2)) - o(1).            (11)

In the current square-root branch P_F/D->pi, nu=o(D), and x_B=o(D).
Divide (2) by D and use (11):

    I5_coll/D
      >= 10 pi + 3(rho+g) + 6 sqrt(Delta_2)
         - 21 t_D - o(1),                                (12)

which proves (3).

The coefficient at T=1.850 is greater than 0.5201, at T=1.855 greater than
0.4151, and at T=1.860 greater than 0.3101. It stays positive through
T<1.8747, but no extension of the present collar/fan scope is claimed.

After removing the O(1) double-good-end trains, each incidence counted by
I5_coll belongs to a different complete collar train: its other terminal occurrence
is the selected good hull side. A pentagon has five boundary occurrences, so the
number of distinct pentagons reached is at least I5_coll/5. This gives the 0.0620
coefficient in (4).

This is stronger localization than a generic pentagon-sea statement: the forced
pentagons are connected to selected good loaded-hull collar sides by a linear family
of actual complete stopped trains.

Remaining Target-C bottleneck: use the cyclic order and train-direction labels of
this hull-to-pentagon transport to force a crossing/rank obstruction, a
source-preserving strict diameter decrease, or a charge exceeding the remaining
high-t face/interface budget.

No numerical search, verifier execution, or CI result is a proof premise. The
decimals only evaluate the symbolic coefficient (3).

Classification: proved candidate awaiting hostile audit; theorem-state authority
unchanged. C-II and Level I remain open.
