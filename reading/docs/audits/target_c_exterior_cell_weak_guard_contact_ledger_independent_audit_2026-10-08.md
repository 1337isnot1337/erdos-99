> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_cell_weak_guard_contact_ledger_independent_audit_2026-10-08.md) · source SHA-256 `a156df4bd684eed4a39239e1f02e7bf33f07d020844b4a14466de094d9325f06`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-89E65B1AAE54","canonical":true,"claim_ids":["C-EXTERIOR-CELL-WEAK-GUARD-LEDGER"],"claim_statuses":{"C-EXTERIOR-CELL-WEAK-GUARD-LEDGER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: weak guards and the exterior-cell contact ledger

**Date:** 2026-10-08  
**Audit base:** origin/main=c4a42cf1748788b41901d8f1ceb929eb53c64959, state 2026-10-08.audit.140  
**Frozen source:** research/sol/target-c-exterior-cap-closure-20261006 at f4a362727779f6afc0f01738015112c04fdb73d5  
**Source report:** docs/reports/target_c_exterior_cap_mixed_boundary_wall_capacity_2026-10-06.md, SHA-256 601865a16cd7c444696606e9cca2b09a47c494448d7aa050152baa3bad38a484

## Verdict

**PASS — promote C-EXTERIOR-CELL-WEAK-GUARD-LEDGER.** In an actual hull-augmented cell, weak unit guards at every path vertex except one internal vertex protect all retained source points. Any new unit contacts can only involve inserted sites internally or retained path vertices. The canonical contact/diameter endpoint then excludes the exact equal-cardinality packet under its full contact and diameter-pair ledger hypotheses.

This is the nonstrict counterpart to Audit.140. It allows exact contacts to remain in the packet and counts them rather than opening them by dilation. It still supplies no packet, does not establish triangle-freeness from the packet alone, and does not cover a move of the cell walls.

## Exact audited statement

Let A be a finite contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with diameter D. Put K=conv(A). Let Q be a bounded hull-augmented face cell whose boundary is one source-hull arc and a simple path of actual unit-contact edges. Let W_Q be the vertices of that path and S_Q=(A intersect Q) minus W_Q. Let v be an internal path vertex, so both incident path sides are actual unit contacts. Define

```math
N_{Q,v}=\{x\in\operatorname{int}(Q): |x-w|\ge1\text{ for every }w\in W_Q\setminus\{v\}\}.
```

Take a deletion set R containing S_Q union {v}; any additional deleted labels form T. Keep the weak guards at every old wall vertex in W_Q minus {v}, including vertices in T. Suppose Y is a finite unit-separated packet in N_{Q,v} with |Y|=|R|, and form A'=(A minus R) union Y. Define:

- t as the number of old unit-contact edges incident to R, counted once;
- d as the number of old actual diameter-D pairs incident to R, counted once;
- j as the number of new unit pairs in A' with at least one endpoint in Y, including packet-internal and packet-to-retained pairs.

Then:

1. A' is unit-separated, and every pair involving Y is strictly shorter than D.
2. A new unit pair touching Y can only be internal to Y or join Y to a retained wall vertex in W_Q minus {v}.
3. If R covers every old actual diameter pair, no such replacement exists by global minimality.
4. Otherwise, no such replacement exists if A' is triangle-free, j<=t, and either j<t or d>0.

This is one exact claim: the weak shield supplies all lower constraints and localizes j; the existing canonical contact-budget endpoint supplies the last contradiction.

## Independent proof of the weak full-source shield

Fix x in N_{Q,v}. Source points in Q off the unit path belong to S_Q and are deleted. A retained source point on the path is at distance at least one from x by the guard. Let q be any retained source point outside Q. Since x is interior to K and q lies in K, the open segment from x to q stays in int(K). It cannot exit Q through a source-hull side before q. A source label in the relative interior of a unit path side is impossible by unit separation from that side's endpoints.

Write a,b for the two unit path neighbors of v, translate v to the origin, and let K_v be the convex cone on the Q side between the unit rays a and b. Put r=|x-v|.

If r>1, x is at least one from every path vertex, including v. If the segment xq first crosses the interior of a unit path side cd at z=(1-s)c+sd, then q and x are each at least one from c and d. The identity

```math
|p-z|^2=(1-s)|p-c|^2+s|p-d|^2-s(1-s)
```

shows |x-z| and |q-z| are at least sqrt(3)/2. Thus |x-q|>=sqrt(3)>1. If the first exit is at a retained path vertex w other than v, then q is distinct from w because q lies outside Q; both |x-w| and |q-w| are at least one, so |x-q|>=2. If the first exit is at v, then |x-v|>1 and q is a distinct source point with |q-v|>=1, so |x-q|>1.

Now suppose r<=1. The weak guards at a and b imply

```math
x\cdot a\le r^2/2,\qquad x\cdot b\le r^2/2.
```

If q is outside the interior of K_v, write q=tu with t=|q-v|>=1 and |u|=1. The maximum of x dot u over exterior directions occurs on one of the two boundary rays, so x dot u<=r^2/2. Therefore

```math
|x-q|^2=r^2+t^2-2t(x\cdot u)\ge t^2+r^2(1-t)\ge1.
```

The final expression is increasing for t>=1 because its derivative is 2t-r^2>=1. Equality in the distance estimate can occur only when t=1 and u is an extremal boundary ray a or b; then q is one of the guarded path neighbors.

If q lies in the interior of K_v but outside Q, the segment xq stays in the cone interior and cannot leave through either side incident with v. It also cannot reach the source-hull arc before q. Its first exit is through another unit path side or a retained path vertex w other than v. A side crossing gives |x-q|>=sqrt(3)>1 by the weighted-square identity. At a vertex exit, q is distinct from w because it lies outside Q, and |x-q|=|x-w|+|w-q|>=2.

Thus x is at least one from every retained old source point. Equality can occur only at a guarded path vertex. This checks every retained isolate outside Q; it uses that the nonunit part of the cell boundary lies on the actual boundary of K.

## Exact contact and diameter ledger

Because Y is unit-separated and its members are at least one from every retained source point, A' is a same-cardinality feasible source. Every y in Y lies in int(K). If |y-z|=D for some z in K, moving y a small distance away from z while staying in K would give a pair in K longer than D. Hence all Y-involving pairs are strictly below D.

The weak shield is strict for every retained source point outside the path. Source points of Q off the path are deleted. Consequently a new unit pair touching Y can only be another pair within Y or a pair to a retained path vertex. This proves the stated localization of j without discarding any packet-internal or packet-to-wall contact.

If R covers all old diameter pairs, no old distance D remains after deletion and every inserted-involving distance is below D. Since the replacement is finite, its diameter is strictly below D, contradicting global minimality; no triangle-free hypothesis is needed in this case.

Otherwise, the canonical contact-budget endpoint applies when the full new contact graph is triangle-free. If j<t, the replacement has fewer contacts than A. If j=t and d>0, no new diameter pair can involve Y, while d old diameter pairs are removed; the replacement has the same contact count and fewer actual diameter pairs. Both contradict the canonical lexicographic choice. The theorem does not infer triangle-freeness from an internally triangle-free packet: all triangles through retained wall anchors remain part of the explicit A' check.

## Hostile scope checks and dispositions

- **Weak versus strict guards.** The result permits equality only at guarded path vertices. It does not imply the strict capacity statement beyond Audit.140 or open new contacts at no cost.
- **Full-source isolates.** Every retained outside isolate is checked through the actual source-hull boundary. Labels on the cell's hull arc belong to S_Q and must be deleted or paid for.
- **Interior nonunit sides.** The canonical noncontact-wall regression and the exact rectangle-plus-isolate example from the frozen report refute treating an arbitrary nonunit interior side as a hull boundary. Here such sides must lie on partial(K).
- **Full contact ledger.** j includes packet-internal contacts and every contact to a retained wall anchor. Triangle-freeness must be checked on A', not only on Y.
- **No packet construction.** This is an obstruction criterion for a packet that satisfies the stated hypotheses. It does not supply Y, establish an area capacity, or prove the source has a useful R.
- **No wall motion or multi-cell composition.** All cell walls are fixed, only one internal guard is omitted, and no compatibility between cells is asserted.
- **One internal vertex.** The statement does not extend to two omitted wall guards; the canonical retained-isolate regression remains binding.

| Candidate | Verdict | Disposition |
|---|---|---|
| Weak full-source shield for one omitted internal wall vertex | PASS | Promote within hull-augmented cell scope |
| Exact contact/diameter ledger for an equal-cardinality packet | PASS | Promote with every new contact and triangle checked |
| Packet existence, area capacity, or moved-wall refill | UNPROVED | Not promoted |
| Macroscopic-cap extraction of an eligible internal vertex | NOT AUDITED | Remains outside this result |

## Validation boundary and frontier effect

No numerical verifier is needed for this analytic finite-source statement. The registered certificate suite checks its canonical cell and contact-budget dependencies; it does not encode the weak-shield proof. Audit.141 adds a contact-preserving packet test to the exterior-cell frontier: exact new contacts are allowed only when the complete replacement pays them against t and the actual-diameter loss d. This does not supply a packet or close C-II/Level I.
