> Generated reading edition · [exact source](../../../docs/audits/target_c_two_halfdisk_physical_interface_hostile_audit_2026-09-13.md) · source SHA-256 `818c92c4b7e95fbf8c2a926dc0dd87c1a0fa2b2a6c45712a9fe0b7be6c2a7355`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E50274A823EB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — two-half-disk physical boundary and interface locality

**Date:** 2026-09-13  
**Base state:** `2026-09-12.audit.46`  
**Reviewed:**

- `research/target_c_two_halfdisk_physical_interface_2026-09-12.md`;
- `research/target_c_two_halfdisk_interface_sublinear_locality_2026-09-12.md`.

**Disposition:** PASS at the stated proof-only two-half-disk scope. The scalar
inequalities are valid and do not close C-II. Canonical state is unchanged.

## 1. Separate group boundary floors

The reviewed argument assumes the audited two-half-disk alternative, so each dominant
strict-rhombus group has area

$$
A_{i,D}=(\pi/8-o(1))D^2
$$

inside a half-disk of ambient diameter `D`, with complement area `o(D^2)`. The imported
physical-boundary transport theorem therefore gives
`sum_j rho_{i,j,D} >= D-o(D)` and

$$
D\left(P_{i,D}-2\sum_j\rho_{i,j,D}\right)
>(4-2\sqrt3)A_{i,D}.
$$

Dividing by `D` gives

$$
P_{i,D}\ge
\left(2+\frac\pi8(4-2\sqrt3)-o(1)\right)D.
$$

The two applications are separate and do not identify the two group boundaries. The
constant `gamma=pi(4-2sqrt(3))/8` is correct.

## 2. Physical-boundary injection

For the full strict-rhombus complex, an edge occurrence on the physical boundary of a
dominant group has a rhombus on one side. If its other side is another strict rhombus,
that rhombus is either local to the same harmonic cell label or is a missing/nonlocal
rhombus. The reviewed proof uses the audited finite labeling fact:

- a shared edge with an unloaded endpoint joins the same unloaded contact component;
- a shared loaded-loaded edge is a force-hull side in Type II, and two bounded rhombi
  cannot lie on opposite sides of a force-hull side.

Thus local rhombi from different harmonic-cell groups cannot share a full edge. A
boundary occurrence of either dominant group is consequently a distinct physical
boundary occurrence of the full strict-rhombus complex. Repeated vertices do not
matter because the count is by edge occurrences. Hence

$$
P_{1,D}+P_{2,D}\le P_{R,D}.
$$

Every full-complex boundary edge has either the unbounded face or a bounded
nonquadrilateral face on its other side. Therefore

$$
P_{R,D}\le b_D+4f_D+Q_D.
$$

Using the exact Type-II ledger `b_D+Q_D=2(q_D-k_D)` gives

$$
2\frac{q_D-k_D}{D}+4\frac{f_D}{D}
\ge4+2\gamma-o(1),
$$

or equivalently

$$
\frac{q_D-k_D}{D}+2\frac{f_D}{D}
\ge2+\gamma-o(1).
$$

No interface term has been silently discarded; it is removed only by the explicit
same-label/no-cross-edge argument.

**Verdict for the global boundary floor:** PASS at proof-only scope.

## 3. Sublinear interface locality

The second report defines `R_i` to contain all local strict-rhombus faces in group
`G_i`, not a truncated area subfamily. Section 129 supplies

$$
N_{miss}=R_4-\sum_rR_r\le3c_I+5=o(D).
$$

If an occurrence in the boundary of `R_1` or `R_2` has a strict rhombus on the other
side outside its group, that opposite rhombus cannot be local: if it were local, the
shared-edge label argument would put it in the same harmonic component and hence the
same dominant group. Thus every such occurrence is incident to one of the `N_miss`
missing rhombi. Four side occurrences per missing rhombus give

$$
I_D\le4N_{miss}\le12c_I+20=o(D).
$$

This remains valid when one missing rhombus borders both groups; the estimate counts
side occurrences rather than distinct rhombi or edges.

## 4. Scalar consequence and limits

The imported physical-interface transport inequality gives

$$
\frac{I_D}{D}\ge
\left[4+2\gamma-2\frac{q-k}{D}-4\frac fD-o(1)\right]_+.
$$

Combining this with `I_D=o(D)` yields the displayed
`(q-k)/D+2f/D >=2+gamma-o(1)`. The endpoint arithmetic verifier was also rerun and
shows substantial slack at the surviving scalar endpoint; the inequality therefore
does not close the branch.

The conclusions are conditional on the audited two-half-disk alternative, full local
cell labeling, Type-II loaded-hull localization, and physical-boundary transport.
They do not apply to arbitrary Type-II survivors, do not delete contact-isolated
points, and do not produce a strict diameter descent or exact unit triangle.

**Final verdict:** PASS as two proof-only half-disk reductions. C-II remains open.
