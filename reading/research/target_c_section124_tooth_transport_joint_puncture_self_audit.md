> Generated reading edition · [exact source](../../research/target_c_section124_tooth_transport_joint_puncture_self_audit.md) · source SHA-256 `776ea3c855054f4938db80c45585912c909bb4bd3d024e582235af8c69b3cc2c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3b5d5fe78872d867d6943d0331ba5c051fc4011d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section124_tooth_transport_joint_puncture_self_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e87d5691108f064aba08c180f35ce39cf28a098a3521ea0df3d5c31ce0293ec0"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Target C Section 124 tooth transport and joint puncture

**Date:** 2026-09-12  
**Artifact:** `research/target_c_section124_tooth_transport_joint_puncture.md`  
**State lock:** audit.46; theorem authority unchanged  
**Verdict:** **PASS at proof-only scope.**

## 1. Tooth-pocket construction

Canonical Section 82 adds missing attachment-polygon sides and makes the augmented harmonic graph 2-connected. Therefore the face adjacent to a missing side has a simple boundary. Its old-contact portion is exactly the corresponding occurrence-counted outer interval. Summed over consecutive attachments,

$$
\sum_i\ell_i=L_r,
\qquad
\sum_i s_i=per(P_r).
$$

This is an occurrence identity: old bridge repetitions are not collapsed.

A direct loaded-loaded polygon-side contact has `ell_i=s_i=1` and contributes zero tooth currency.

**Verdict:** valid.

## 2. Hidden-source audit

A nondegenerate tooth interior contains no vertex of its own unloaded component because it is a face of the augmented graph.

It contains no loaded vertex outside the attachment set: `B=Vert(F)`, and an extreme force-hull vertex not in `A_r` cannot lie in `conv(A_r)`.

It contains no unloaded vertex of another harmonic component: such a vertex lies in `int(P_s)`, while the tooth lies in `int(P_r)`, contradicting canonical Section 83's pairwise interior-disjointness.

Hence every source point in an open tooth interior is contact-isolated. Boundary source points on the artificial chord are deliberately omitted from the interior count and retained globally.

**Verdict:** valid.

## 3. Local Oler normalization

A tooth route of `ell_i` unit edges has `ell_i+1` distinct route vertices. Together with `z_i` interior isolates, Oler sees

$$
N_i=ell_i+1+z_i,
\quad
P_i=ell_i+s_i.
$$

Thus

$$
a_0(ell_i+z_i)\le A_i+c_0(ell_i+s_i),
$$

and because `a_0=2c_0`,

$$
A_i-a_0z_i\ge c_0(ell_i-s_i).
$$

There is no missing endpoint, `+1`, or factor two.

Defining the exact Oler slack

$$
omega_i=A_i+c_0(ell_i+s_i)+a_0-a_0(ell_i+1+z_i)
$$

gives

$$
omega_i=A_i-a_0z_i-c_0(ell_i-s_i)\ge0.
$$

**Verdict:** valid.

## 4. Global disjointness and full-source tooth puncture

Open tooth interiors are disjoint within one augmented harmonic graph because they are distinct bounded faces. Across cells they are disjoint because each lies in its cell and canonical Section 83 gives disjoint cell interiors.

Pairwise interior-disjoint convex polygons have no proper boundary crossings. Their constrained boundary segments can therefore be included in a straight triangulation without Steiner points; segment overlaps are subdivided at existing source endpoints, and remaining source points are inserted by standard source-vertex subdivisions.

Puncturing one closed polygonal disk down to its retained boundary circle lowers Euler characteristic by one, regardless of how many interior source vertices were in its triangulation. For the canonical GWZ perimeter invariant, every punctured side occurrence raises the edge multiplicity by exactly one. This remains true for shared sides and for sides originally on the source-hull boundary, where a once-counted boundary edge becomes a twice-counted nonbounding edge.

Therefore

$$
alpha_0=n-Z_{tooth},
\quad A=A_K-G_{tooth},
$$

$$
P=P_K+\sum_i(ell_i+s_i),
\quad chi=1-M.
$$

GWZ yields

$$
a_0(n-1)\le A_K+c_0P_K-\Omega_{tooth}+a_0H_{chord}.
$$

Equivalently,

$$
\Omega_{tooth}-a_0H_{chord}\le\mathscr O_A.
$$

**Verdict:** valid.

## 5. The chord correction is necessary

For a retained artificial chord of length `s`, subdivision of a packing region changes the sum of local Oler residuals by exactly `a_0(s-1)`. Therefore the term

$$
a_0H_{chord}=a_0\sum_i(s_i-1)
$$

cannot be dropped by algebra alone.

Direct contact sides have `s=1`, so

$$
H_{chord}=\sum_r(per(P_r)-a_r)
$$

is correct.

**Verdict:** theorem is stated with the necessary correction.

## 6. Joint rhombus/tooth puncture

A global unloaded-only strict rhombus has a connected four-cycle of unloaded vertices, so all four vertices belong to one unloaded component. It remains a bounded face of that component's induced harmonic graph. Tooth pockets in that cell split only the old outer face; tooth pockets in other cells lie in disjoint cell interiors. Thus the two puncture families have disjoint open interiors.

If a rhombus and a tooth share an edge, jointly puncturing both sides makes the retained edge nonbounding. The GWZ invariant counts it twice, exactly one side occurrence per puncture.

For `r_0=|R_4^0|`, the rhombus contribution is

$$
-A_4^0+4c_0r_0-a_0r_0=-E_4^0,
$$

because `A_4^0=a_0r_0+E_4^0` and `4c_0=2a_0`.

Adding the audited tooth contribution gives

$$
a_0(n-1)
\le A_K+c_0P_K-E_4^0-\Omega_{tooth}+a_0H_{chord},
$$

hence

$$
E_4^0+\Omega_{tooth}-a_0H_{chord}\le\mathscr O_A.
$$

Loaded-incident rhombi are intentionally excluded; no disjointness theorem for them is silently assumed.

**Verdict:** valid.

## 7. Composition with canonical Sections 122--123

Canonical Section 122 gives

$$
\liminf D^{-1}\sum_r(L_r+P_{exc,r}-2d_r)\ge R_0.
$$

The exact decomposition

$$
L_r+P_{exc,r}-2d_r
=(L_r-per(P_r))+(per(P_r)-2d_r)+P_{exc,r}
$$

has three nonnegative terms. Section 124 gives

$$
\sum_r(L_r-per(P_r))
\le {G_{tooth}-a_0Z_{tooth}\over c_0},
$$

while canonical Section 123 gives

$$
\sum_rP_{exc,r}\le10(e_{BB}-k).
$$

Replacing the first and third terms by these upper payments gives

$$
\liminf D^{-1}\left[
{G_{tooth}-a_0Z_{tooth}\over c_0}
+\sum_r(per(P_r)-2d_r)
+10(e_{BB}-k)
\right]\ge R_0.
$$

The inequality direction is correct: an aggregate lower demand forces any larger payment budget to be at least as large.

**Verdict:** valid.

## 8. Quantifier and source-retention audit

- No source point is deleted from any competitor; omissions occur only in auxiliary finite packing complexes.
- Every contact-isolated source point outside the punctured open tooth interiors remains a vertex of the auxiliary complex, including exterior source points outside the force hull.
- No affine-kernel statement is applied to isolates.
- The finite tooth and puncture theorems hold before asymptotics.
- Only the final three-currency corollary invokes the canonical Type-II aggregate theorem.
- Audit.46 remains the theorem-state authority through Section 123.

## 9. Surviving obstruction

Section 124 does not cap the three-currency payment below `R_0D`. In particular:

1. nearly Oler-saturated tooth pockets can carry linear tooth detour with small `omega_i`;
2. a convex oblique rhombic patch can have zero tooth/exceptional terms but positive cell shape excess; and
3. `e_BB-k` may itself be linear.

The joint puncture theorem additionally prevents rhombus defect and tooth Oler slack from spending independent full-source allowances, but does not by itself bound the tooth detour.

**Final audit verdict:** proof-valid, frontier-changing structural bridge; C-II remains open.
