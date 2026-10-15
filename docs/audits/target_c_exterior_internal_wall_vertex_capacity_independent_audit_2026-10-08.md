<!-- theorem-state: {"artifact_id":"ART-5AAE792D8B7D","canonical":true,"claim_ids":["C-EXTERIOR-INTERNAL-WALL-ONE-GUARD-CAPACITY"],"claim_statuses":{"C-EXTERIOR-INTERNAL-WALL-ONE-GUARD-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: one unguarded internal wall vertex in an exterior cell

**Date:** 2026-10-08  
**Audit base:** origin/main=023917ace0719d0050664a8a08fed1eb5cdb2013, state 2026-10-08.audit.139  
**Frozen source:** research/sol/target-c-exterior-cap-closure-20261006 at f4a362727779f6afc0f01738015112c04fdb73d5  
**Source report:** docs/reports/target_c_exterior_cap_mixed_boundary_wall_capacity_2026-10-06.md, SHA-256 601865a16cd7c444696606e9cca2b09a47c494448d7aa050152baa3bad38a484

## Verdict

**PASS — promote C-EXTERIOR-INTERNAL-WALL-ONE-GUARD-CAPACITY.** In a canonical full-source hull-augmented cell Q, omitting the strict distance guard at one internal vertex v of its actual unit-contact path does not increase the finite unit-separated packet capacity. The exact capacity remains |S_Q|, where S_Q includes every source isolate assigned to Q, including labels on its source-hull arc.

The one-extra-site packet proposed as a possible strict one-cell closure is therefore impossible in a canonical source. This does not settle packet release with moved walls, exact new contacts, multiple cells, or a changed deletion set. C-II remains open.

## Exact audited statement

Let A be a finite canonical triangle-free source: first minimize diameter, then contact count among global minimizers, then actual diameter-pair count. Let K=conv(A), let G be its positive-contact core, and augment G by the full source-hull boundary, retaining collinear hull labels. Take a bounded face cell Q whose boundary consists of one source-hull arc and a simple path of actual unit-contact edges, as guaranteed by C-EXTERIOR-HULL-AUGMENTED-CELLS.

Let W_Q be the vertices of the unit-contact path and S_Q=(A intersect Q) minus W_Q. Suppose v is an internal path vertex, so both Q sides incident with v are actual unit-contact edges. Define

\[
E_{Q,v}=\{x\in\operatorname{int}(Q): |x-w|>1\text{ for every }w\in W_Q\setminus\{v\}\}.
\]

For Pack_1 denoting the maximum cardinality of a finite unit-separated subset,

\[
\boxed{\operatorname{Pack}_1(E_{Q,v})=|S_Q|.}
\]

The lower bound is already canonical: the fully guarded region E_Q, with guards at every member of W_Q, has exact capacity |S_Q| by C-EXTERIOR-CAP-STRICT-PACKET-CAPACITY, and E_Q is contained in E_{Q,v}. The audited addition is the upper bound after omitting one internal path guard.

## Independent proof of the full-source shield

Fix x in E_{Q,v}. Every retained source point in W_Q minus {v} is strictly more than one from x by definition. Every other retained source point q lies outside Q: all source labels in Q not on the path belong to S_Q and are deleted in the replacement.

The source hull K is convex, and x lies in int(Q), hence in int(K). For q in A outside Q, the open segment from x to q lies in int(K). Its first exit from Q cannot pass through a source-hull side before q. A source label in the relative interior of an actual unit wall side is impossible, since it would be less than one from an endpoint. Thus an exit before q is through an actual unit side or a path vertex.

Write a,b for the unit path neighbors of v. First suppose |x-v|>1. Every endpoint of an actual unit side is then strictly farther than one from x: this follows from the guards for vertices other than v, and from the case assumption for v. If the first exit is through the interior of a unit side cd at z=(1-s)c+sd, the weighted-square identity

\[
|p-z|^2=(1-s)|p-c|^2+s|p-d|^2-s(1-s)
\]

places x more than sqrt(3)/2 from z. The retained source point q is at least one from c and d, so it is at least sqrt(3)/2 from z. Since z lies between x and q, |x-q|>sqrt(3)>1. An exit at a retained path vertex is safe by the strict guard there and source separation; an exit at v is safe because |x-v|>1 and q is a distinct source point from v. A path-vertex exit therefore gives |x-q|>1 as well.

Now suppose |x-v|<=1. Translate v to the origin, let a and b be the unit vectors toward its two path neighbors, and let K_v be the convex cone between those rays on the Q side. Put r=|x|. The strict guards at a and b give

\[
x\cdot a<r^2/2,\qquad x\cdot b<r^2/2.
\]

If q is outside the interior of K_v, source separation gives q=t u with t>=1 and |u|=1. Since x is inside the cone, the largest value of x dot u over exterior directions occurs on one of its boundary rays. Therefore x dot u<r^2/2. Using t>=1 and r<=1,

\[
|x-q|^2=r^2+t^2-2t(x\cdot u)>1.
\]

If q is inside K_v but outside Q, the segment from x to q stays inside K_v. It cannot first leave through either side incident with v, and cannot reach a source-hull side before q because it stays in int(K). It consequently exits through another actual unit side or a retained path vertex. The previous crossing or vertex estimate gives |x-q|>1.

This proves that every x in E_{Q,v} is strictly separated from the entire retained source A minus (S_Q union {v}), including all outside contact isolates. The argument uses the special hull-augmented cell boundary: nonunit sides lie on partial(K), not inside K.

## One-extra-site contradiction

Suppose a finite unit-separated packet Y is contained in E_{Q,v} and |Y|>=|S_Q|+1. Keep exactly |S_Q|+1 sites. Dilate this finite packet by a factor just above one about a point in int(Q). Since Q is convex and the packet is finite and interior, the dilation can be chosen to keep every site in int(Q). Its internal distances become strictly greater than one, and all strict guards at W_Q minus {v} persist. The full-source shield just proved keeps every dilated packet point strictly more than one from every retained source point outside Q and from every retained path vertex.

Delete S_Q union {v}, insert the dilated packet, and apply the canonical C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT. At least the two distinct unit contacts on the sides incident with v are deleted. No new unit contact is created, so the new-contact count is zero and is strictly smaller than the old-contact loss. Every inserted-involving pair is strictly below D because each inserted point lies in int(K): if x is interior and q is any point of K, equality |x-q|=D would let us move x a small distance farther from q while staying in K, contradicting diam(K)=D. The old retained pairs remain at most D, and the contact graph is the old induced graph plus isolated new labels, hence remains triangle-free. This is forbidden by the canonical endpoint. Therefore no such packet exists.

Together with the existing exact lower bound for E_Q, this gives the asserted equality for E_{Q,v}.

## Adversarial scope checks and ledger

- **Internal versus hull-tip guard.** The vertex v must have two actual unit-contact sides. This is not a result for omitting a loaded hull-tip guard while allowing arbitrary distances to that tip; the canonical one-unit-side hull-tip shield has a different, explicit tip hypothesis.
- **Boundary requirement.** The nonunit side of Q must lie on the actual source-hull boundary. The canonical noncontact-wall regression at side threshold sqrt(3), and the exact rectangle-plus-isolate example in the frozen source report, show why an arbitrary nonunit interior side cannot be treated as a hull side. For the latter, A={(0,0),(1,0),(2,0),(0,1),(2,1),(1,17/10)} has minimum pair distance one; after deleting v=(1,0), x=(1,4/5) is strictly farther than one from the four retained unit-wall vertices (squared distances 41/25 and 26/25) but has squared distance 81/100 from the retained isolate (1,17/10). The top length-two side is inside conv(A), since the last source point lies above it. This exact check independently confirms the scope failure.
- **One deletion only.** The canonical two-deletion retained-isolate regression remains binding. This theorem removes one internal path guard and deletes its vertex; it says nothing about two unguarded vertices.
- **One cell only.** No cross-cell packet, shared-guard compatibility, moving-wall feasibility, or cap extraction is asserted. The exact shared-tip regression remains compatible.
- **Capacity is not a lower-bound construction.** Equality rules out a one-extra-site strict packet; it does not produce a packet of any prescribed geometry, a moved-core refill, or a strict sub-D competitor.
- **Macroscopic-cell vertex extraction.** The source report's additional argument that every occupied macroscopic cap cell has a qualifying internal path vertex is not needed for this theorem and was not promoted. Its loaded-cycle/occupied-cap dependency remains outside this audit.

| Candidate | Verdict | Disposition |
|---|---|---|
| One strict unguarded internal wall vertex in one canonical hull-augmented cell | PASS | Promote exact capacity identity |
| One-extra-site strict packet after deleting the cell isolates and that vertex | FAIL as a proposed canonical-source configuration | Ruled out by the promoted capacity theorem and canonical exchange endpoint |
| Extraction of a qualifying vertex from every occupied macroscopic cap cell | CONDITIONAL ONLY | Not audited or promoted |
| Moved-core, multi-cell, weak-contact, or nonstrict packet/refill applications | UNREVIEWED | Keep outside this promotion |

## Validation boundary and frontier effect

This is a finite geometric proof; no numerical verifier is needed for the new claim. The repository's registered certificate suite still checks the canonical cell-capacity and exchange-endpoint inputs. The promotion adds one exact capacity identity and narrows the exterior-cell refill route: a strict packet confined to one fixed cell cannot gain one extra site by unguarding a single internal wall vertex. A moved-core or contact-ledger argument is still required. No C-II or Level I status changes.
