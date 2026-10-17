> Generated reading edition · [exact source](../../../docs/audits/target_c_contact_budget_diameter_exchange_independent_audit_2026-10-06.md) · source SHA-256 `f89b587fe6aa451666666b347bbe0ef31cab5b1da98b4d373ad0bcb7b5e6ef5e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AC3A3A2E5A42","canonical":true,"claim_ids":["C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT","C-ONE-SITE-CONTACT-SURROUND","C-TWO-CONTACT-PACKET-OPENING"],"claim_statuses":{"C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT":"canonical","C-ONE-SITE-CONTACT-SURROUND":"canonical","C-TWO-CONTACT-PACKET-OPENING":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — finite contact-budget / diameter exchange endpoint

**Date:** 2026-10-06  
**Audit base:** ae6697b649d5516cfe36cc855a89948940f9ce14  
**Starting state:** 2026-10-06.audit.63  
**Source branch:** research/target-c-residual-closure-20261005  
**Audited snapshot:** ed535f5a3a45e3921d91a29c38a0cb37f1d27921  
**Source artifacts:** `docs/reports/target_c_contact_budget_diameter_exchange_2026-10-05.md`; `docs/reports/target_c_one_spare_site_contact_minimality_endpoint_2026-10-05.md`  
**Verdict:** PASS for three finite statements below. The packet-existence applications remain unproved.  
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

The PR #722 branch is a fixed snapshot at the commit above. Its finite exchange report was added at `34a2cbcb`; the branch tip has not changed since the refreshed inventory. The branch was not modified. Main had advanced one promotion past its last merge base; audit.63 does not change the exact finite lexicographic argument below.

## 1. Exact finite exchange endpoint

Let A be a finite triangle-free global minimum-diameter source of cardinality n, selected first with the fewest unit contacts among all such minimizers and then with the fewest actual diameter pairs among those. Let D be its diameter, C its unit-contact edges, and H its actual distance-D pairs. Contact-isolated points remain in A.

Choose a subset R of A and a finite inserted set Y with |Y|=|R|. Let A' be the configuration obtained by deleting R and inserting Y. Define:

- $t$: the number of edges of $C$ incident to $R$, counted once;
- $d$: the number of edges of $H$ incident to $R$, counted once;
- j: the number of unit-distance pairs in the new configuration that have at least one endpoint in Y, including packet-to-retained pairs.

Assume:

1. every pair in Y, and every pair from Y to a retained point in A minus R, has distance at least 1;
2. all those new-involving distances are strictly less than $D$;
3. $A'$ is triangle-free;
4. j <= t; and
5. either j < t or d > 0.

Then no such packet exists.

**Independent proof.** The lower bound makes $A'$ a set of the same cardinality: inserted points cannot collide with one another or with retained points. Its diameter is at most $D$. If it were below $D$, it would contradict global minimality. Otherwise it is another triangle-free global minimizer. Retained-retained pairs are unchanged, so the contact count is exactly

$$
|C(A')|=|C|-t+j.
$$

If j < t, this contradicts contact minimality. If j=t, condition 5 gives d>0; strict upper bounds prevent any new diameter pair, so

$$
|H(A')|=|H|-d<|H|,
$$

contradicting the secondary diameter-pair minimum. This uses actual diameter pairs and counts every inserted-to-retained contact. It does not use a local-motion argument or delete any isolate from the source bookkeeping.

The strict upper assumption is a genuine hypothesis on the packet. It is automatic if every inserted site lies in the interior of the convex hull of A: an interior point cannot be at distance D from any point of that compact convex hull.

## 2. At most two new contacts can be opened

Consider any finite retained configuration and a finite inserted packet. Suppose every inserted-involving distance is at least $1$ and strictly below the applicable upper bound $D$, and at most two inserted-involving pairs are exactly unit. Then an arbitrarily small finite perturbation of the inserted points alone can make every new unit distance strictly greater than $1$, while preserving all old pairs, all other strict lower bounds, and every strict upper bound.

For active squared-distance functions $g_i(z)=|p_i(z)-q_i(z)|^2-1$, their gradients are rows on the inserted coordinates. If no vector strictly increases both active constraints, the two rows have a nonzero nonnegative dependence. A single row cannot vanish. For two distinct rows to be negatively proportional, their inserted-coordinate supports must be the same single point: the contacts join one inserted point to two retained points. Equality of the row norms then makes the retained points opposite unit neighbors of that inserted point. Move that point perpendicular to their line; both squared distances become $1+ε^2$. In every other support pattern, strict separation gives a direction with positive derivative for each active distance. A sufficiently small step preserves the finitely many remaining strict inequalities.

Consequently, a contact-budget exchange that removes an old contact and has strict upper slack cannot rely on only one or two new contacts to balance the lost budget: those contacts can be opened, leaving $j=0<t$, which is excluded by Section 1.

## 3. One-site surrounding condition

For one inserted site x strictly inside the convex hull of A, let N(x) be its retained unit neighbors. Assume every other new lower constraint is strict. If the displacement vectors from x to the points in N(x) do not have the origin in the interior of their convex hull, a separating line gives a nonzero vector w with

$$
(x-a)\cdot w\ge0\qquad(a\in N(x)).
$$

For every sufficiently small positive ε,

$$
|x+\epsilon w-a|^2
=1+2\epsilon(x-a)\cdot w+\epsilon^2|w|^2>1.
$$

All other lower constraints and all upper constraints remain strict by finiteness and the interior location. Thus any one-site packet with no strict-opening direction must have at least three unit neighbors whose displacement vectors strictly surround the origin. This is a local necessary condition only; it does not produce such a site or override the canonical strict-safe saturation theorem.

## 4. Reconciliation with the one-spare-site report

The one-spare-site endpoint in the companion report is a direct corollary of Section 1. If a packet has at least one extra strictly protected site and deletes a nonisolated contact vertex in addition to replacing its old population, choose exactly as many packet points as deleted labels. Then $j=0<t$, and the exact exchange endpoint rules it out. When the removed vertex already belongs to the original deletion set, no extra point beyond that set's size is needed for the same contradiction.

This canonicalizes the **exclusion implication** for any packet that actually meets the strict pair conditions. It proves no strict-safe site, packet, protected wall, or surplus exists. The companion report's existence target is still open. Its residual-cage composition and other source-specific applications were not audited here and remain noncanonical.

The result is complementary to audit.60's finite-motion endpoint: audit.60 handles simultaneous shortening while preserving old contacts; this theorem handles an arbitrary finite replacement with an explicit contact budget and strict upper diameter control.

## 5. Hostile scope checks and dispositions

- **All new contacts:** $j$ counts packet-internal and packet-to-retained unit pairs. Omitting cross contacts invalidates the contact count; none are omitted here.
- **Triangle-freeness:** it is an explicit hypothesis on $A'$. A forest among inserted points alone is insufficient to prove it.
- **Contact isolates:** every original source point is retained unless explicitly in $R$; no stress-kernel extension or isolate deletion is used.
- **Global versus local:** the contradiction uses the global minimum diameter D(n), then contact-minimality and diameter-pair-minimality among global minimizers.
- **Finite versus infinitesimal:** the exchange theorem assumes an actual finite packet. The opening lemma separately proves that its local direction integrates to a sufficiently small finite step using strict inactive margins. It does not promote a first-order stress condition to a finite obstruction.
- **Strict upper pairs:** if a new-involving pair can remain at $D$, the exact diameter-pair count need not decrease. This is why the hypothesis is retained.
- **No existence conclusion:** no source geometry in these reports realizes a protected packet in every canonical source. Positive residual and pinned equilibrium are not converted into spare capacity.

| Candidate | Verdict | Canonical disposition |
| --- | --- | --- |
| Finite contact-budget / diameter-pair exchange endpoint | PASS | Promote as `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT` |
| At-most-two-new-contact opening lemma | PASS | Promote as `C-TWO-CONTACT-PACKET-OPENING` |
| One-site surrounding condition | PASS | Promote as `C-ONE-SITE-CONTACT-SURROUND` |
| One-spare-site exclusion implication | PASS — SUBSUMED | Covered by the finite exchange endpoint; no separate ID |
| Existence of a strict packet or spare site in every source | UNPROVED | Not promoted |
| Residual-cage release/refill composition | NOT AUDITED | Remains unreviewed |

No change to the C-II or Level I status follows.
