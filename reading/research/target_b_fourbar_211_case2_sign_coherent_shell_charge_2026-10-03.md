> Generated reading edition · [exact source](../../research/target_b_fourbar_211_case2_sign_coherent_shell_charge_2026-10-03.md) · source SHA-256 `33f6d2ccf57df5e9a5e2aeb7d2737131093f839287c66f5879e6462d17e63a82`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "755b2537187188697a9f155cc43bdfa540a9f8ce", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_b_fourbar_211_case2_sign_coherent_shell_charge_2026-10-03.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "59cf9a8c05ad906e7fc0170e958f02d809007ba8739d2444664deb2f7e2c842a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target B: case-2 sign coherence and terminal charge

Date: 2026-10-03
Base main: fba1e3ad197e5dec3f7c18065bc7c84a922e6075
Status: proof-only candidate, noncanonical. Target B and Level I remain open.

Continue case 2 of `target_b_fourbar_211_phase_group_reduction_2026-10-03.md`.
Bars h1,h2 have repeated potential A; h3,h4 are singleton classes B,C.
Normalize

    t_A=0, t_B=p, t_C=q,

with distinct nonzero coprime integers p,q. The case-2 phase rows are

    N_1B=n1 q, N_1C=-n1 p,
    N_2B=n2 q, N_2C=-n2 p,                         (1)

where n1,n2 are nonzero, and the unique positive stress obeys

    mu1 n1 + mu2 n2 = 0.                            (2)

Thus n1,n2 have opposite signs.

Canonical §50.1 gives ordered tangent sign coherence: for a fixed diameter bar
h, every tangent separating train has the same oriented contribution sign,

    a_(h,tau)=sigma_h J e_h.                         (3)

Hence there is no signed cancellation among tangent trains assigned to one
destination class.

## Sign-coherent phase restriction

For each repeated bar hi, both counts in (1) are nonzero. By (3), N_iB and
N_iC have the same sign. Therefore

    sgn(n_i q)=sgn(-n_i p),

so

    p q < 0.                                         (4)

The singleton potential levels therefore lie on opposite sides of A.

Moreover the actual numbers of moving tangent trains are exactly

    m_iB=|N_iB|=|n_i||q|,
    m_iC=|N_iC|=|n_i||p|.                            (5)

The four transfer sets are pairwise disjoint. B and C are different destination
classes. A train also cannot be tangent to both h1 and h2, because its edge
direction would be perpendicular to two distinct nonparallel diameter directions.
Thus the exact number M of distinct moving tangent trains is

    M=(|n1|+|n2|)(|p|+|q|).                          (6)

Every such train is tangent to and separates its source diameter. Canonical §42.3
therefore makes both terminal boundary edges non-hull. Distinct complete trains
have distinct terminal occurrences. Hence case 2 forces at least

    2(|n1|+|n2|)(|p|+|q|)                            (7)

distinct non-hull terminal boundary edges.

This is a direct phase-to-shell conversion. It does not by itself close the shell
inequality because the count can be O(1).

## Arithmetic gap and the minimum-charge core

Since p,q are nonzero coprime integers with pq<0,

    |p|+|q| >= 2,

with equality only for {p,q}={1,-1}. Since n1,n2 are nonzero integers of opposite
sign,

    |n1|+|n2| >= 2,

with equality only for {n1,n2}={1,-1}. Consequently

    M>=4.                                             (8)

If M is not 4, one factor in (6) is at least 3, so

    M>=6.                                             (9)

Thus every nonsymmetric case-2 survivor has at least six moving tangent trains and
at least twelve forced non-hull terminal edges.

The only minimum-charge case is, up to signs and relabeling,

    p=1, q=-1, n1=1, n2=-1.                           (10)

Then (2) gives mu1=mu2. The sign-frustration identity already proved on main,

    v3 dot v4=(mu1^2-mu2^2)/sin(theta_12)^2,

gives

    v3 perpendicular v4.                              (11)

There is exactly one moving tangent train in each ordered transfer
h1->B, h1->C, h2->B, h2->C.

For either repeated bar, the two moving trains have the same oriented sign by
(3) and relative speeds +delta(v),-delta(v). In the rotating frame, exact TC6
therefore gives, with x=t delta(v),

    |r_i(t)|^2-D^2 = 4(1-cos x)^2,  i=1,2.            (12)

The singleton bars remain exactly flat on the backward-kernel slice. Hence the
minimum shell-charge survivor is exactly a pair of identical two-train quartic
blockers coupled to two flat perpendicular singleton bars. Same-class tangent
trains, if present, have zero relative speed and do not affect (12).

## Terminal-bank consequence

Rows 3 and 4 of the phase matrix vanish. Sign coherence implies that a moving
tangent family from h3 or h4 to another potential class could not cancel within
that destination class. Therefore h3 and h4 have no moving tangent trains to
another class: B and C are terminal potential classes.

Canonical §50.2 then gives disjoint complete separator sets Sigma_3,Sigma_4 with

    |Sigma_3|>=D,  |Sigma_4|>=D.                       (13)

Every transfer to h3 lies in Sigma_3 and every transfer to h4 lies in Sigma_4.
Thus the four-bar algebraic obstruction is embedded in two disjoint macroscopic
terminal separator banks. The diameter-thrackle regression on main does not encode
this train-bank structure.

Remaining target: charge the marked transfer trains and their ordered positions in
Sigma_3,Sigma_4 into the exact shell/Oler residual, or exclude the symmetric
four-moving-train normal form (10)-(12) by terminal-bank pseudoline order.

No numerical computation, verifier output, or CI result is a proof premise.
