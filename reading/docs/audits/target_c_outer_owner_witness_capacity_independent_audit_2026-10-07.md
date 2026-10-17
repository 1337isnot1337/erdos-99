> Generated reading edition · [exact source](../../../docs/audits/target_c_outer_owner_witness_capacity_independent_audit_2026-10-07.md) · source SHA-256 `6d931987d6a6c2a3ff8d7c3d1a159b46b03b98d264fd2aac342bde1d9be8fea4`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-41F4346A9F94","canonical":true,"claim_ids":["C-OO-LOWER-WITNESS-OWNER-CAPACITY"],"claim_statuses":{"C-OO-LOWER-WITNESS-OWNER-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.106 — outer-owner lower-witness capacity

**Date:** 2026-10-07  
**Base:** `origin/main=cee30cfed7a530677b1644fe4603f070bef288a8`, state `2026-10-07.audit.105`  
**Target:** C-II; C-I closed, C-II and Level I open  
**Verdict:** **PASS WITH NARROWED SCOPE — promote `C-OO-LOWER-WITNESS-OWNER-CAPACITY`.**

## Frozen source and audit boundary

I audited the generic §4 owner count and its Type-II §5 refinement in
`docs/reports/target_c_loaded_neighbor_outer_owner_bound_2026-10-05.md` from the
immutable PR #722 source snapshot
`research/target-c-residual-closure-20261005` at
`ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. The artifact SHA-256 is
`73fcdb63e60c7104eede09e47d9dca9e82f7b0b5fb3bc89631de04d6d5863bff`.

The endpoint-incidence lemmas in §§2–3 were independently audited and promoted as
`C-DIAMETER-ENDPOINT-LOCAL-DEGREE-TWO` and
`C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE` in Audit.104. This audit treats those
exact canonical statements as inputs. The source report's §4.3 extension from the
surviving owner count to an original proposal count after deleting up to `2d_H`
owners is not promoted; its post-deletion compatibility hypotheses are separate.
The alternative §5 simplification using `m_B<=x_B` is also not needed for the
promoted result.

## Exact promoted statement

Let `A` be a sufficiently large canonical contact-minimal, then diameter-pair-minimal,
triangle-free C-II source with `C=C_*`, `H=H_*`. Use the canonical O–O setting of
`C-OO-LOWER-BLOCKER-LOCALIZATION`: actual disjoint owner sets on the nonisolated
positive-contact core, selected cuts inducing the stated layer translations, all
contact isolates retained and assigned by the canonical dispatch, and the theorem's
small translation-cloud bound. For general multishear applications, retain its
projective-direction-width hypothesis.

Fix `1<t<sqrt(2)`. Consider a finite family of nonzero owner proposals such that:

1. every old unit contact remains exactly unit under every binary owner selection;
2. each counted singleton proposal preserves all old diameter upper bounds and keeps
   every old nondiameter strictly below `D`;
3. each counted singleton passes every unary strict-rhombus test and strictly shortens
   at least one old diameter pair; and
4. every old noncontact pair that becomes a lower equality or violation in a counted
   singleton had old length at most `t`.

Let `k` be the number of these counted owners, `B` the actual diameter endpoints,
`q=|B|`, `b` the occurrence-counted length of the core's old outer contact walk,
`x_B=b-q`, `m_B` the number of nonunit sides of `conv(B)`, and `Z_out` the number
of contact isolates on the old outer contact face. Then

```math
\boxed{k\le 2m_B+3(x_B+Z_{out}).}
```

In the Type-II near-disk branch of `C-FULLCORE-NEAR-DISK`, let `a=m_B` and let `N`
count the distinct contact isolates within `5/4` of any Section-67 outer pocket or
Section-77 nondegenerate exterior-cap boundary. Audit.105 gives `N<=48(x_B+a)` and
localizes every isolate lower-witness endpoint to this collar. Therefore the sharper
conclusion is

```math
\boxed{k\le 2a+3(x_B+N)\le147x_B+146a\le147(x_B+a).}
```

Consequently, in a Type-II sequence with `x_B+a=o(D)`, any such counted family has
`k=o(D)`. This is a capacity bound on an already specified owner family; it does not
extract that family or prove `x_B+a=o(D)` for canonical sources.

## Independent reconstruction

### Each counted owner needs a lower witness

Activate only one owner. If every old noncontact remains strictly above one, all old
contacts stay exactly unit and no new contact is created. The singleton is then a
unit-separated source with the same contact count, all old diameters at most `D`, all
old nondiameters below `D`, and at least one old diameter pair removed. If no old
diameter remains, it has diameter below the global minimum `D`; otherwise it is another
diameter-`D` global minimizer with the same contact count and fewer diameter pairs.
Both contradict the canonical lexicographic choice. Since upper-diameter and unary
rhombus failures are excluded by the hypotheses, each counted owner must have an old
noncontact pair that reaches distance at most one. Equality is included because it
would create a new contact.

Canonical `C-OO-LOWER-BLOCKER-LOCALIZATION` puts these intergroup lower witnesses in
the old outer contact face after bounded-face isolates move with their common owner;
its remaining non-outer exception is the unary strict-rhombus case, already excluded.
Because the displacement cloud is small, every such witness has old length at most
the fixed `t`. A condition `1+2s<t`, where `s` bounds each singleton endpoint
displacement, is sufficient; the canonical cloud-diameter bound also makes this hold
eventually for every fixed `t>1`.

### Count owners by their actual witness endpoints

Let `U_out` be the distinct unloaded positive-contact core vertices on the outer
contact face, and put `W=U_out union Z_out`. Each loaded hull vertex appears at least
once in the outer walk. Every distinct `U_out` point also appears at least once, so
```math
|U_{out}|\le b-q=x_B.
```

Choose one lower witness for every counted owner, and charge that owner to an endpoint
whose motion is relative to the other endpoint in the singleton state.

- **Both endpoints loaded.** Their old distance is in `(1,t]`. By
  `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE`, they are consecutive full-source hull
  vertices, hence consecutive loaded hull vertices; since the pair is a noncontact it
  is one of the `m_B` nonunit loaded-hull sides. A fixed pair can be charged to at
  most its two endpoint owners, for at most `2m_B` owners.
- **The relatively moving endpoint is in `W`.** Distinct owners have disjoint moving
  sets, so a fixed vertex belongs to at most one counted owner. This contributes at
  most `|U_out|+|Z_out|` owners.
- **The relatively moving endpoint is loaded and the other endpoint is in `W`.** By
  `C-DIAMETER-ENDPOINT-LOCAL-DEGREE-TWO`, each fixed source point has at most two
  actual diameter endpoints within distance `t`. Each such loaded endpoint belongs
  to at most one owner. This contributes at most `2(|U_out|+|Z_out|)` owners.

These cases exhaust all witnesses: by canonical O--O localization, every remaining
intergroup lower clause lies in the outer contact face, with only the unary rhombus
exception already excluded. Its nonloaded vertices are exactly the counted outer
core points and contact isolates. Adding the three bounds and using
`|U_out|<=x_B` proves `k<=2m_B+3(x_B+Z_out)`.

### Replace the isolate population by the collar population in Type II

For the selected singleton witnesses, retain only the distinct outer-face isolates
that actually appear as an endpoint, and call this set `Z_*`. Audit.105's collar
localization applies to each lower equality/violation, so `|Z_*|<=N`. Re-run the
three endpoint charges with `Z_*` in place of `Z_out`:
```math
k\le2m_B+3(x_B+N).
```
In Type II, `m_B=a` and `N<=48(x_B+a)`, giving
```math
k\le2a+3x_B+144(x_B+a)=147x_B+146a\le147(x_B+a).
```
This argument bounds distinct owner witnesses even if one isolate blocks several
proposals: isolate-to-loaded incidence is at most two, and an isolate used as a
moving endpoint belongs to only one owner. It does not presume simultaneous
feasibility of the singleton proposals.

## Adversarial checks and limits

- The loaded-loaded count excludes old unit contacts because every old contact is
  required to remain unit; only noncontact sides can be lower blockers.
- The source-level witness graph need not be a forest. The proof uses neither source
  planarity-to-owner-planarity nor any acyclicity claim, so it is compatible with the
  canonical owner-contraction-cycle regression.
- The count is not a simultaneous assignment theorem: each owner is tested only in its
  singleton state. It therefore does not infer that individually feasible moves can
  be combined.
- A fixed isolate can appear in many proposals. In the Type-II refinement, Audit.104
  limits its nearby loaded endpoints to two; owners charged through a moving isolate
  are distinct because moving sets are disjoint.
- `x_B+a=o(D)` is an additional low-defect hypothesis, not a consequence of Type II
  alone. The macroscopic-container branch, an O–O family extraction, original-family
  deletion by `2d_H`, and Level I closure are outside this theorem.

No new numerical verifier is claimed. The proof is finite incidence counting from the
canonical geometry. Relevant canonical certificates were run through the full
70-certificate suite on the promotion branch; the exact local-conflict and isolate
dispatch certificates were also independently rerun during the preceding audit cycle.

## Dependency chain and frontier effect

Canonical dependencies are `C-OO-LOWER-BLOCKER-LOCALIZATION`,
`C-DIAMETER-ENDPOINT-LOCAL-DEGREE-TWO`,
`C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE`, and
`C-OO-OUTER-ISOLATE-COLLAR-BOUND`.

```math
\text{singleton upper/unary safety + strict old-diameter shortening}
\to\text{one outer lower witness per owner}
\to k\le2m_B+3(x_B+Z_{out})
\to\text{Type-II collar replacement }k\le147(x_B+a).
```

This rules out a linear already-specified O–O singleton family in the conditional
low-defect Type-II subcase `x_B+a=o(D)`. The active C-II finite-move obligation is
unchanged because neither the family nor the low-defect condition is currently
guaranteed.
