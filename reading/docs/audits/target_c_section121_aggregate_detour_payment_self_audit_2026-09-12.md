> Generated reading edition · [exact source](../../../docs/audits/target_c_section121_aggregate_detour_payment_self_audit_2026-09-12.md) · source SHA-256 `76cd746740a4e503767642d4203bf3d48fe2dcc1ba646f7cf8dbfd7bb98781c2`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-36910E332E6F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — hostile self-audit of Section 121 aggregate detour payment

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Artifact audited:** `research/target_c_section121_aggregate_detour_payment.md`  
**Disposition:** proof passes this same-run hostile audit; theorem authority is unchanged.

This audit attacks the three places where Section 121 could silently overcount a
physical object: local rhombi, loaded-loaded contacts, and global contact edges.

## 1. Local quadrilateral faces really are global strict-rhombus faces

A quadrilateral face of one harmonic induced graph has four unit sides by definition
of the positive-contact graph. In a triangle-free unit-separated source neither
diagonal can have length one, and unit separation makes both diagonals at least one;
therefore both are strictly greater than one and the quadrilateral is a strict unit
rhombus.

The only possible local-to-global failure would be an omitted source point or omitted
contact chord inside that local face. Section 121's elementary rhombus argument rules
out an omitted point without invoking any full-source rigidity statement. Splitting a
unit rhombus by its center gives four triangles whose largest side is one; every
relative-interior point of one of those triangles is strictly within unit distance of
an endpoint of its unit side. Unit separation therefore excludes an omitted source
point. The rhombus diagonals are not unit, and straight-line contact planarity excludes
a crossing contact edge. Hence the four-cycle is a full-core face.

This argument is source-geometric and does not delete or reclassify contact isolates.

## 2. One physical local rhombus cannot be charged by two cells

Suppose one physical rhombus is a face of both `H_r` and `H_s`.

- If it has an unloaded vertex, that vertex would belong to both unloaded components,
  forcing `r=s`.
- If all four vertices are loaded, all four are in `A_r cap A_s`. Canonical Section
  83 already proves that two distinct components cannot share three attachments: the
  contracted incidence subgraph on two component nodes and three common loaded nodes
  is `K_{2,3}`, with six edges against the planar incidence ceiling five. Thus four
  common attachments are impossible.

So `R_loc<=R_4` and the local rhombus-area sum is physically injective.

A stronger statement that *every* loaded-touching global rhombus is local would be
false. With two opposite loaded vertices the two unloaded vertices can lie in distinct
components; with three loaded vertices the middle loaded vertex need not attach to the
component of the fourth vertex. Section 121 does not make that stronger claim.

## 3. Loaded-contact multiplicity is exactly scoped

For a loaded-loaded contact `uv`, Section 121 counts only the number of harmonic cells
whose attachment sets contain both endpoints.

If `uv` is a force-hull side, it is an exposed side of every such cell. All cells lie
on the same side of the supporting line. Two positive-area convex cells sharing the
full exposed segment on that same side overlap in a one-sided neighborhood of every
relative-interior point of the segment, contradicting canonical Section 83. Hence the
multiplicity is at most one.

If `uv` is not a hull side, multiplicity greater than one first forces `uv` to be a
side, not a diagonal, of every cell using it: the relative interior of a diagonal lies
in the cell interior and would immediately intersect any second cell containing the
same segment. Once it is a common side, pairwise interior-disjoint convex cells can
occupy at most one side each of its supporting line. Hence multiplicity is at most two.

The audit explicitly rejects the tempting stronger claim that a non-hull loaded
contact has multiplicity at most one. Two cells may legitimately share it from
opposite sides.

Therefore

```math
C_{\rm att}\le(q-m_B)+2c_B=e_{BB}+c_B
```

is valid.

## 4. Edge partition in the aggregate identity is exact

Every positive contact with an unloaded endpoint belongs to exactly one unloaded
component and therefore exactly one harmonic induced graph. Loaded-loaded contacts are
the only edges that can be repeated, and their total repetition is precisely
`C_att`. Thus

```math
\sum_rM_r=e_C-e_{BB}+C_{\rm att}
```

has no omitted or repeated non-loaded-loaded edge.

For each `H_r`, face-edge handshaking is

```math
2M_r=L_r+4R_r+P_{{\rm exc},r},
```

so its detour equals `2M_r-4R_r-2d_r`. Canonical mixed rigidity gives
`e_C=2m-2-q+k`, while the canonical face identity gives
`m=R_4+f+q-k+1`. Their substitution yields

```math
e_C=2R_4+2f+q-k.
```

Direct algebra then gives

```math
E_\Sigma
=4(R_4-R_{\rm loc})+4f
+2(q-k-e_{BB}+C_{\rm att})-2\sum_rd_r.
```

No asymptotic estimate enters this identity.

## 5. Section-75 elimination is valid in every component regime

Canonical Section 75 records

```math
e_{BB}=q-m_B+c_B
```

and the exact post-ZF ledger

```math
m_B+k=c_I+c_B+s_C+2.
```

The latter is not merely a Type-II asymptotic statement. Therefore substituting the
multiplicity ceiling into the exact aggregate identity gives

```math
E_\Sigma
\le4\Delta_R+4f
+2(q+m_B-c_I-s_C-2)-2d_\Sigma
```

without assuming `c_I=o(D)`. The Type-II limit is used only when this upper expression
is composed with proof-only Section 120's linear lower bound.

## 6. Contact-isolated source points and source cardinality

All objects in Section 121 live in the nonisolated positive-contact core because that
is the scope of Sections 62, 75, 82, and 83. No claim is made that this core equals the
full source. Contact-isolated source points remain present and untouched. Section 121
constructs no competitor and therefore makes no source-cardinality substitution.

## 7. Remaining non-implications

The audit rejects the following conclusions:

- `Delta_R=o(D)` has not yet been proved by Section 121 itself;
- `f=o(D)` and `m_B=o(D)` do not hold all-regime from the cited inputs;
- the sum of cell diameters is not known to be asymptotically maximal;
- the right side of (121.17) is not currently below the Section-120 lower coefficient;
- no inactive-container branch is eliminated;
- C-II is not closed.

The result is nevertheless a strict structural improvement over Section 120: the
local detour demand is now represented by an exact global face-incidence expression,
and loaded-contact reuse has a finite multiplicity theorem.

**Audit verdict:** Section 121 passes as a proof-only research theorem. Independent
review/promotion has not been attempted. The authoritative theorem state remains
unchanged and C-II remains open.
