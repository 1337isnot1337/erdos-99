<!-- theorem-state: {"artifact_id":"ART-6109EE730595","canonical":true,"claim_ids":["C-LOADED-EXTERIOR-CAP-CHORD-THRESHOLD","C-LOADED-ONLY-STRESS-CYCLE-OBSTRUCTION"],"claim_statuses":{"C-LOADED-EXTERIOR-CAP-CHORD-THRESHOLD":"canonical","C-LOADED-ONLY-STRESS-CYCLE-OBSTRUCTION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.111 — loaded cap chord and stress-cycle scope

**Date:** 2026-10-07

**Audit base:** origin/main=5984251d03c1d3f5ad40e39baa4d66ae08780ea4, tree 249a149a9c2702d2b11fd2b7dfa5828d03380ce3, state 2026-10-07.audit.110

**Target:** C-II; C-I is closed, C-II and Level I are open

**External literature / computation:** not used

## 1. Frozen source and audited units

The Worker 2 source is origin/research/sol/target-c-exterior-cap-closure-20261006 at f4a362727779f6afc0f01738015112c04fdb73d5. This audit covers only Theorems E.4 and E.5 in Sections 4–5 of docs/reports/target_c_exterior_packet_release_and_unloaded_core_cut_2026-10-06.md, SHA-256 6b8722e95d92cfc1c32f7bcc6d4ba5cd71f6138df657d73ce5be982d8299fa08.

E.6 was independently audited and promoted in Audit.110. The antipodal pairing, Theorems E.1–E.3, and later packet/refill applications are excluded here. The loaded-only stress-cycle statement from Audit.90 is reconstructed at its widened finite-source scope. E.5 is checked against its already canonical theorem and receives no duplicate ID.

## 2. Finite loaded exterior-cap chord threshold

Let A be a finite unit-separated planar set of diameter D>0. Suppose a,b∈A have length ℓ=|a-b|<D. Let c,d∈A be actual diameter partners of a,b, respectively, so |a-c|=|b-d|=D. Assume c,d lie in one closed half-plane bounded by line ab, and some z∈A lies strictly in the opposite half-plane. Then

~~~text
(1 + D^-2) ℓ^2 + 2ℓ/D ≥ 3,
ℓ ≥ τ_D := 3D / (sqrt(3D^2 + 4) + 1).
~~~

The partners c,d may coincide. The claim uses neither optimality nor equilibrium. In particular, τ_D>3/2 for D≥6.

### Independent proof

Apply a rigid motion so a=(-ℓ/2,0), b=(ℓ/2,0), and the partner half-plane is y≤0. Since |c-a|=D≥|c-b|, subtracting squared distances gives c_x≥0; write c-a=(A0,-C), where A0≥ℓ/2 and C≥0. Similarly, |d-b|=D≥|d-a| gives d-b=(-B0,-E), where B0≥ℓ/2 and E≥0.

Let α,β∈[0,π/2] be the angles these two diameter vectors make from the downward vertical toward the right and left, respectively, and set θ=α+β. Directly,

~~~text
|(c-a) - (d-b)| = 2D sin(θ/2).
~~~

Because (c-a)-(d-b)=c-d+(b-a), the diameter bound and triangle inequality imply

~~~text
2D sin(θ/2) ≤ |c-d| + ℓ ≤ D + ℓ < 2D.
~~~

Thus θ<π and sin(θ/2)≤(1+ℓ/D)/2.

Write z=(x,y) with y>0. The diameter-disk constraints |z-c|≤D=|a-c| and |z-d|≤D=|b-d| imply the tangent half-plane inequalities

~~~text
-A0(x+ℓ/2) + Cy ≤ 0,
B0(x-ℓ/2) + Ey ≤ 0.
~~~

Together with y≥0, these put z in the triangle bounded by those tangent lines and ab, allowing a vertical side when C=0 or E=0. Indeed, they give x≥-ℓ/2+(C/A0)y and x≤ℓ/2-(E/B0)y; C/A0+E/B0 is positive because θ<π, so the region is bounded. The triangle's base angles are α,β; its apex angle is π-θ. Since z lies inside it, the two base angles of triangle azb are at most α,β, so its angle φ=∠azb is at least π-θ.

Unit separation gives r=|z-a|≥1 and s=|z-b|≥1. The cosine rule yields

~~~text
ℓ^2 = r^2+s^2-2rs cos(φ)
    ≥ (r-s)^2 + 2rs(1+cos(θ))
    ≥ 4 cos^2(θ/2)
    ≥ 4 - (1+ℓ/D)^2.
~~~

Rearranging gives (1+D^-2)ℓ^2+2ℓ/D≥3. Its positive root is τ_D. For D≥6, τ_D>3/2. This proof covers coincident partners and one vertical tangent side; θ<π excludes both tangent sides being parallel vertical lines.

For a side ab of the full-dimensional actual loaded hull F=conv(B), all actual diameter partners lie in F, on the inward side of its supporting line. An occupied exterior cap supplies z on the opposite side. Thus every such closing chord satisfies |ab|≥τ_D if |ab|<D; if |ab|=D and D≥6, it is also nonunit. In a canonical C-II source D≥9, every occupied cap therefore closes along a nonunit loaded-hull side.

**Verdict:** PASS — promote C-LOADED-EXTERIOR-CAP-CHORD-THRESHOLD as a finite source-geometry theorem. It is separate from C-LOADED-HULL-CAP-BUDGET: that theorem controls cap arc/perimeter allocations and does not assert this lower bound on an occupied cap's base chord.

## 3. Loaded-only stress-cycle obstruction: widened finite scope

Let A be any finite unit-separated planar source of diameter D≥6, let B be the set of all endpoints of actual diameter pairs, and assume F=conv(B) has positive area. Let C(A) be all unit pairs and H(A) all diameter pairs. A normalized nonnegative equilibrium stress is a pair of coefficient families α≥0, β≥0 satisfying the canonical contact-positive/diameter-negative force balance Rᵀ(α,-β)=0 and Σ(h∈H(A)) β_h=1. Let P be their polytope and define

~~~text
P_B = {(α,β)∈P : α_e=0 whenever e∈C(A)
      is incident to A\B}.
~~~

If any side of the loaded hull F is nonunit, then P_B=∅. If P_B≠∅, the positive contact support of every stress in it is the entire loaded-hull cycle, with positive weight on every side, and positive diameter support is incident to every loaded vertex.

This statement does not assume global minimality, triangle-freeness, a full-core regime, or a near-disk sequence. It applies to any such finite source carrying a normalized nonnegative equilibrium stress. Contact-isolated source points remain part of A and are not assigned stress rows.

### Independent reconstruction

By canonical C-LOADED-NEAR-UNIT-ADJACENCY, a unit pair of loaded endpoints must be a side of F: a nonconsecutive pair at length 1<D would have length at least τ_D>3/2. Therefore every positive contact coefficient in a stress in P_B lies on the simple loaded-hull cycle.

Every point p∈B is an exposed vertex of F: if q is an actual diameter partner, p uniquely maximizes the linear functional in direction p-q, since |x-q|≤D=|p-q| for all x∈A, with equality in that direction only at x=p. Thus the loaded hull is a strictly convex polygon with no collinear intermediate vertices.

The virial identity gives

~~~text
Σ(e∈C(A)) α_e = D^2 Σ(h∈H(A)) β_h = D^2,
~~~

so the positive loaded contact graph is nonempty. If it is a proper subgraph of a cycle, one path component has a leaf p with sole positive contact neighbor b. Let n be the outward normal of the loaded-hull side pb. The contact force at p is tangent to that side. Every actual diameter partner q of p is another loaded vertex, distinct from p,b, since D≥6>1. Strict convex-polygon support then gives n·(p-q)>0. The normal component of equilibrium forces every diameter coefficient incident to p to vanish, leaving a single nonzero contact force that cannot balance. This contradiction shows that the positive contact graph is the entire cycle.

If any loaded-hull side is nonunit, its contact coefficient must be zero, contradicting full-cycle support. If all sides are unit, every vertex has two positive side-contact forces that are not opposite because F is a strictly convex polygon with its listed hull vertices; equilibrium then requires positive diameter support at that vertex.

No planarity-only or selected-stress-to-full-diameter-graph inference is used: the only loaded unit edges considered are actual source contacts, and every diameter partner is an actual endpoint in B.

**Verdict:** PASS WITH SCOPE EXTENSION for C-LOADED-ONLY-STRESS-CYCLE-OBSTRUCTION. Replace the old full-core C-FULLCORE-LOADED-CHORD premise by the finite C-LOADED-NEAR-UNIT-ADJACENCY theorem, at the exact finite-source scope above.

## 4. Worker 2 Theorems E.4 and E.5

For the frozen canonical C-II source, D≥9 and F=conv(B) has positive area. If an actual exterior cap is occupied, Section 2 says its closing side is nonunit. Section 3 therefore gives P_B=∅. This validates the complete E.4 implication; its only previously implicit step was the occupied-cap chord threshold, now explicit and canonical.

E.5 is already exactly covered by C-UNLOADED-KKT-STRESS-TRANSVERSAL. With the loaded-only face empty, the canonical finite-dimensional transversal selects U⊂V\B,

~~~text
|U|≤s_Z+1,   s_Z=dim_aff(P)=e+h-(2v-2),
~~~

that kills every normalized stress. The reduced (|A|-|U|)-point source has a small straight motion opening all retained actual contacts and shortening every old actual diameter pair. Contact isolates stay in the full source and are fixed at their original coordinates under the full-source strict-margin check. This is a reduced-cardinality descent; it supplies no refill, packet capacity, or same-cardinality competitor. Do not create a duplicate E.5 theorem ID.

## 5. Hostile scope checks and disposition

- B is the full set of actual diameter endpoints, not selected stressed endpoints. Every actual partner lies in B.
- The stress graph is contained in the loaded-hull cycle because the unit-contact threshold is applied to every loaded pair; planarity alone is not used.
- The occupied-cap conclusion is a base-chord lower bound proved by diameter disks. The cap-budget theorem's arc-length budget alone would not imply it.
- The stress-cycle theorem needs only D≥6; the Worker 2 application uses the canonical D≥9 source. The loaded hull is explicitly two-dimensional.
- Theorem E.5 deletes only unloaded positive-contact-core vertices. It does not delete contact isolates or claim they have affine stress coordinates.
- The reduced source has fewer labels. No refill, triangle-free global competitor, C-II closure, or Level I conclusion follows.
- The preselected-loaded-endpoint refinement remains at its prior narrower scope.

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Finite diameter-disk threshold for an occupied exterior loaded-hull chord | PASS | Promote C-LOADED-EXTERIOR-CAP-CHORD-THRESHOLD |
| Loaded-only stress face lies on the full loaded cycle; a nonunit hull side empties it | PASS WITH SCOPE EXTENSION | Widen C-LOADED-ONLY-STRESS-CYCLE-OBSTRUCTION to finite sources carrying normalized stresses |
| Worker 2 E.4 occupied-cap application | PASS | Record as a consequence of the two claims above |
| Worker 2 E.5 unloaded transversal and strict reduced-source descent | PASS — ALREADY CANONICAL | Reuse C-UNLOADED-KKT-STRESS-TRANSVERSAL; no duplicate ID |
| Packet/refill, spare capacity, finite activation, C-II or Level I closure | NOT ESTABLISHED | Do not promote |

The result narrows the Worker 2 frontier only to a refill/independent cardinality comparison after E.5. It does not resolve the live full-source refill requirement or change the overall C-II / Level I status.
