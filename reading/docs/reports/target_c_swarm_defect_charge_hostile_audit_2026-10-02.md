> Generated reading edition · [exact source](../../../docs/reports/target_c_swarm_defect_charge_hostile_audit_2026-10-02.md) · source SHA-256 `c719e34ff5826a5ec76b405895b137d7d8677a109b35cf3da069cdbae202b500`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A6DD7DF86ABC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — independent audit of the all-cell convex-bank defect charge

**Date:** 2026-10-02  
**Root research base:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`  
**State:** `2026-09-14.audit.51`  
**Audited candidate:** [PR #611](https://github.com/1337isnot1337/e-99/pull/611),
commit `79d898192b119bfdc56e8e5066b158d22ff64699`, report
`docs/reports/target_c_global_convex_bank_defect_audit_2026-10-02.md` on that branch.  
**Disposition:** scoped independent audit passes; audited-working at the
declared full-core near-disk scope, awaiting promotion. No canonical state change.  
**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

```text
all-cell convex-bank capacity -> actual aggregate Z_D+Q_D
-> positive full-core boundary-order defect floor
-> contradiction requires a smaller upper account for those same quantities.
```

This audit reconstructs the new bridge against canonical objects rather than
accepting the candidate because another agent or a merged report says it is proved.
It is not an audit of all older Target C theorems, a promotion transaction, or a
Level I settlement.

## 1. Exact audited claim

For canonical full-core near-disk Type-II sources retain each actual unloaded
component `I_r`, its loaded attachments `A_r`, induced graph
`H_r=C[I_r union A_r]`, attachment polygon `P_r=conv(A_r)`, and its
occurrence-counted outer contact walk `L_r`. Set

$$
Z_D=\sum_r(L_r-\operatorname{per}P_r),\qquad
Q_D=\sum_r\sum_{f\text{ bounded in }H_r}(\deg f-4).
$$

In particular, `Q_D` is the induced face defect, not the augmented local
defect in Section 123 and not a phase-trim defect. The candidate concludes

$$
\liminf (Z_D+Q_D)/D\ge1/26000.
\tag{1.1}
$$

All source points remain in the full configuration. The proof obtains its
quadratic rhombic area from the canonical full-core branch and supplies no
bound on isolated population outside that scope.

## 2. Canonical objects and proof checks

The audit checked the required passages in canonical Sections
[62](../targets/target-c/62-attachment-incidence-currency-audit.md),
[82](../targets/target-c/82-harmonic-cell-near-quadrangulation-audit.md),
[83](../targets/target-c/83-attachment-cell-disjoint-tiling-audit.md),
[68](../targets/target-c/68-punctured-packing-phase-audit.md),
the near-disk input in
[80](../targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md),
and [shared Theorem 10.6](../theory/01-local-structure.md).
No proof-only fixed-star extraction, current rooted numerical threshold,
or exact-phase staircase is used.

### 2.1 Bank occurrences and strict terminal order

Deleting an attachment from `H_r` leaves its connected unloaded component
and all other attachments connected. An attachment therefore has one
outer occurrence. A repeated unloaded bank vertex would cut off an
attachment-free excursion; the positive-coordinate maximum principle
with that vertex as sole boundary collapses the excursion. Distinct
points rule it out. Different banks may still share unloaded articulation
vertices; the audit retains their separate occurrences.

Section 82's actual hull augmentation is 2-connected with convex faces.
Every missing attachment-polygon side bounds one outer pocket, because
the actual edge to the unloaded component at each attachment separates
the two polygon-side sectors. The opposite bank turns clockwise.

Equal directions at two distinct rhombic terminal edges on one bank would
force a straight intervening bank. At an unloaded endpoint, every contact
neighbor lies in the opposite closed half-plane. Positive equilibrium
then forces all those contacts onto the line. The incident rhombus gives
a nonparallel contact, contradicting this. Direct attachment-to-attachment
banks have just one unit edge. Thus strict terminal order is justified;
no uniform positive angle or force floor is asserted.

The exact bank identity is

$$
\ell_i-d_i=\sum_{e\in W_i}(1-e\cdot t_i).
$$

It charges bad terminal occurrences by `Z_r/(1-cos epsilon)` without
identifying repeated vertices or discarding a boundary term.

### 2.2 Pair of banks and full-hull polar estimate

A phase family of width `w` cannot have two good ends on the same bank
when `w+2epsilon<pi/2`: induced boundary orientations at a train's two
ends differ by `pi`, while good bank directions lie in one narrow cone.
The centerline endpoints can be extended through the empty convex outer
pockets to the attachment polygon, preserving order. Noncrossing paths
between two boundary intervals have reversed endpoint order. Strict
clockwise terminal-direction order on both banks forbids two family
members connecting the same bank pair.

The near-disk estimate uses the **actual loaded hull** `F_D`, with
`B(0,r_D) subset F_D subset B(0,R_D)` and both radii divided by `D`
tending to `1/2`. It does not assume that every `P_r` is a near disk.
For any support point, `n dot p>=r_D` implies the normal's radial error
is at most `acos(r_D/R_D)`. A short consecutive attachment chord has
minor endpoint polar separation `O(eta)`; the associated actual hull arc
has tangents in the same polar cone. At most one attachment gap can use
the major hull arc, and its short chord is paid separately by `eta D`.

The short hull arcs are disjoint within one component. Their projections
in the two permitted polar bands bound their total chord length, hence
the number of unit good ends after the bank-excess charge. Long bank
pairs contribute only `O(eta^-2)`. The resulting bound is uniform in the
component and phase-bin direction:

$$
\frac{M_r}{D}\le
\left(1+\frac1{1-\cos\epsilon}\right)\frac{Z_D}{D}
+\eta+2\tan(\epsilon+w+4\eta)+o(1).
\tag{2.1}
$$

Its error is used as a **maximum** over all cells, not summed once per
cell. The constant `O(eta^-2)` times the total `O(D)` train count is
`O(D)` at fixed `eta`, hence negligible only at the quadratic crossing
scale where it is used. This avoids a false `c_I eta D` argument.

### 2.3 Independent tripartite bound

For three positive part sizes `a,b,c`, average over all triples with one
vertex in each part. Triangle-freeness gives

$$
\frac{E_{AB}}{ab}+\frac{E_{AC}}{ac}+\frac{E_{BC}}{bc}\le2.
$$

Each density is at most one. The linear relaxation is maximized by filling
the two largest products; they share the largest part. Hence

$$
E\le\max\{a(b+c),b(a+c),c(a+b)\}\le\frac{2M}{3}(a+b+c)
$$

when all part sizes are at most `M`. Empty parts are direct. The last
ratio is increasing in all three sizes and reaches `2M/3` at equal
sizes. This independently checks the candidate's symmetrization proof.

### 2.4 All-cell transport and scales

The physical rhombic boundary is at most `L_r+5Q_r`. Thus the total
complete local train count is at most half the summed boundary. Trains
with an exceptional-face end are at most `5Q_D`, because every such end
uses a distinct physical boundary edge. A train's incident rhombic area
equals its transverse endpoint span, at most `D`. Removing these trains
loses at most `5Q_D D` area, including loaded rhombi; overcounting overlaps
is in the valid direction.

The remaining trains have locally outer-to-outer ends. Canonical reduced
phase cutting loses `O(D)` rhombi, and a randomly shifted **fixed-width**
bin loses `O(D/w)` more. For fixed `w`, both are quadratic-scale errors.
Inside each component/bin, the three labels give a triangle-free
tripartite crossing graph. Each train enters one bin only, so using the
uniform maximum (2.1) yields a valid all-cell count.

Section 83 supplies `pi D^2/4-o(D^2)` unloaded-only rhombic area, and
cell disjointness bounds the full local area by the full hull area.
Section 68 supplies only `O(D)` total rhombic excess. Together with
Section 62's `sum per(P_r)<=2pi^2 D+O(1)`, this gives exactly the
candidate's one-parameter inequality

$$
\frac\pi4\le5q+\frac{\sqrt3}{6}(2\pi^2+z+5q)
\left[\left(1+\frac1{1-\cos\epsilon}\right)z
+2\tan\epsilon\right].
\tag{2.2}
$$

The order of limits is `D`, then `eta`, then bin width `w`, at fixed
`epsilon`. It is not a conversion of `o(D^2)` error to `o(D)`.

## 3. Arithmetic verification and what it proves

The auditor read and independently executed the verifier from the pinned
candidate commit. Results: 2,349 triangle-free tripartite graphs; 12 sharp
finite cases; rational cubic coefficient margin `443/120054`; final
area margin `84146693/28665000000`. Exact Machin-series bounds verify
the pi estimates, and rational square/cube checks verify the radical
bounds used in the floor.

With `z<=1/66`, choosing `epsilon=(66z)^(1/3)/3` reduces (2.2) to

$$
\frac\pi4\le5q+\frac{\sqrt3}{6}(2\pi^2+z+5q)(66z)^{1/3}.
$$

If `z+q<=1/26000`, the verified rational upper bound is strictly below
the verified lower bound for `pi/4`, proving (1.1). The proof handles
`z=0` by first letting `epsilon` tend to zero. Normalized `Z_D,Q_D`
are bounded by the exact local incidence ledger, so the subsequential
argument covers all canonical full-core sequences.

The finite verifier encodes neither bank geometry nor global optimality.
Those parts were checked in the human argument above. No computer
certificate is misrepresented as a source-level optimizer.

## 4. Tested closing implication and exact surviving gap

The candidate verifier exhibits `q=0,z=1/100` satisfying the relaxed
area account. Reconstructing that test confirms that (1.1) supplies a
lower cost, not an upper account or finite deformation. Positive-defect
full-core sources therefore survive this argument.

Conditionally importing the current rooted ledger

$$
Z_D/2+Q_D/2\le\Delta(\lambda)D+o(D)
$$

would force `Delta(lambda)>=1/52000` in that branch. This excludes its
zero-defect endpoint, but its ledger is unpromoted, the inequality does
not cover arbitrary full-core sources, and it does not address macroscopic
inactive containers. No stronger conclusion is recorded here.

The root's [phase-threshold candidate](target_c_phase_swap_rhombus_threshold_currency_2026-10-02.md)
spends **crossing omissions**. Neither (1.1) nor (2.2) gives an upper
bound on that different currency. Missing same-part crossings cannot be
called Mantel deficit. Combining the two packets without an actual
cross-part assignment/payment theorem would be an invalid synthesis.

**Disposition:** the all-cell defect charge survives this independent
bridge audit at its stated scope and is audited-working, awaiting the
repository's promotion contract. No canonical file is changed. The next
obligation is an actual upper payment for `Z_D+Q_D`, or a full-source
finite move converting its unavoidable bank/exceptional-face contribution
to strict diameter descent. The source omission-payment and active-swap
branches remain separate and open.
