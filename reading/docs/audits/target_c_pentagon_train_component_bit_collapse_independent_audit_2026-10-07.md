> Generated reading edition · [exact source](../../../docs/audits/target_c_pentagon_train_component_bit_collapse_independent_audit_2026-10-07.md) · source SHA-256 `ddeef9c5cee6cbcd6bf3f3cb4e5510b35842ec22c92ddde5922b9a98c2ef16b6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-495A00D49347","canonical":true,"claim_ids":["C-PENTAGON-TRAIN-COMPONENT-BIT-COLLAPSE"],"claim_statuses":{"C-PENTAGON-TRAIN-COMPONENT-BIT-COLLAPSE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: independent audit of pentagon train-component bit collapse

Date: 2026-10-07. Audit base: `origin/main=08c3b0684e83e3ac108ec9c61ca13ff2acb75edf`, state `2026-10-07.audit.97`.

## Frozen source and audit boundary

The source is Worker 1 branch `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`, report `docs/reports/target_c_common_angle_train_closure_and_full_endpoint_2026-10-06.md` (Git blob `fdad9f22b57acceb7b63cadde489f7684254f4c2`, SHA-256 `176b0eae82355d398d6674ce0e047446e443feb6ea11d31e4f1e9f9d45df9233`). The same report blob is present at the fetched overnight branch tip `c6a75bd708e553c4feb3a540e0b17f3b65e22a82`.

This audit evaluates source §3 only. The local balance lemma and the component incidence count are exact. The source's suggestion that a component with linearly many physical pentagons actually occurs in a canonical source is not established; the promoted statement is conditional on an existing component and does not assert such a source family.

## Audited statement

Let `F` be a physical strictly convex unit-pentagon face of the canonical triangle-free contact core, and orient its five unit side vectors `w_1,...,w_5` around its boundary. For a train-bit assignment `x_i in {0,1}`, suppose the common-angle face-closure equation holds:

`sum_i x_i*w_i = 0`.

Then all five side bits are equal. For a common angle with `theta` not in `2*pi*Z`, this equation is exactly the face-closure condition, since the original face closes (`sum_i w_i=0`) and `Rot(theta)-I` is invertible.

Now form the graph whose vertices are these physical pentagon faces and whose edges are complete stopped trains with both terminal faces in the family. On every connected component `P` of this graph, all incident train bits have one common value. If `P` has `f>=2` faces and `E` internal trains, canonical reciprocal-train sparsity gives `E<=2f-3`. If `O` is the number of pentagon-side terminal occurrences whose other train endpoint is outside `P`, then

`O = 5f - 2E >= f+6`.

All those `O` outside terminal occurrences carry the same one component bit. For `f=1`, there are five outside terminal occurrences, again carrying one bit.

This count is about incidences and bit equality. It neither proves that large connected pentagon components occur in canonical sources nor gives a linear count of independently selectable train bits.

## Independent proof

The whole pentagon boundary closes, so a selected proper nonempty set of sides would be a nonempty proper balanced subset of the five vectors. A one-vector subset cannot sum to zero. A four-vector subset cannot sum to zero either, because its complementary one-vector subset would then sum to zero. A two-vector subset sums to zero only if its two unit vectors are antiparallel, giving a projectively parallel side pair; canonical `C-CONTACT-FACE-REGULARITY` excludes such a pair on a physical triangle-free unit pentagon. A three-vector balanced subset has a balanced two-vector complement and is excluded for the same reason. Thus only the empty and full selected sets close, proving the all-equal bit conclusion.

When two pentagon faces share a complete stopped train, its single train bit appears on both faces. The local equalities therefore propagate along every path in the pentagon/train component. Each face contributes five terminal occurrences. A train internal to `P` has exactly two such occurrences, one at each terminal face; all other occurrences leave `P`. Hence `O=5f-2E`. For `f>=2`, the internal train graph on this face subset is a connected induced subgraph of the canonical reciprocal train endpoint graph. Its `(2,3)` sparsity gives `E<=2f-3`, so `O>=5f-2(2f-3)=f+6`.

## Scope audit and verdict

- The physical-face premise matters: the no-parallel-side lemma is canonical only for actual strictly convex triangle-free unit-pentagon faces. It is not a claim about an abstract unit-vector pentagon or a scaffold.
- The graph count uses `C-RECIPROCAL-TRAIN-GRAPH` on actual bounded augmented face endpoints. It does not identify an arbitrary sparse graph with a source realization.
- A path on `f` abstract pentagon nodes satisfies the numerical sparsity bound with `E=f-1` and has `O=3f+2` outside occurrences. This shows that the `E<=2f-3` count alone does not force bounded component size. It is an abstract graph illustration only, not a canonical-source regression or an existence construction.
- Even when `O>=f+6`, those terminals all have the same bit. Counting terminal occurrences as independent binary choices is invalid. Conversely, this does not show that a large physical component or a forbidden-bit propagation of linear multiplicity occurs in a canonical source.
- The claim that a large actual component exists is therefore **conditional/unproved** and is not promoted. The exact local equalization and incidence theorem are promoted as `C-PENTAGON-TRAIN-COMPONENT-BIT-COLLAPSE`.

**Verdict: PASS WITH NARROWED SCOPE.** The component theorem is a canonical C-II restriction on common-angle bit systems, not a component-existence theorem, a bounded-suppression theorem, or a finite competitor. C-II remains open.

**Exact next obligation:** construct a source-realized nonconstant common-angle bit state that satisfies the full source pair ledger and clears Audit.97's actual-diameter amplitude threshold, or prove no such endpoint exists under stronger canonical hypotheses. No terminal-count argument alone supplies this endpoint.
