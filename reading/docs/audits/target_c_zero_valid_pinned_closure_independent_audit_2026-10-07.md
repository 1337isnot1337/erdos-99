> Generated reading edition · [exact source](../../../docs/audits/target_c_zero_valid_pinned_closure_independent_audit_2026-10-07.md) · source SHA-256 `25adddb249e4d922caadcd23f16a8ed4f9e0d7d194bd13ff348821eebdbf3bf9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C1C2989E044E","canonical":true,"claim_ids":["C-ZERO-VALID-PINNED-CLOSURE"],"claim_statuses":{"C-ZERO-VALID-PINNED-CLOSURE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: independent audit of zero-valid pinned 2-CNF closure certificates

Date: 2026-10-07. Audit base: `origin/main=e95729108a3993ada6fd9de92fd035b36c3d819c`, state `2026-10-07.audit.98`.

## Frozen source and audit boundary

The source is PR #722 branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`, report `docs/reports/target_c_zero_state_horn_closure_2026-10-05.md` (SHA-256 `fcadcf2a0da4eead99a9b57c629e893f7024fde9fc627120319ab7803b35fe2b`), and verifier `research/verify_target_c_zero_state_horn_closure_2026_10_05.py` (SHA-256 `15bfeaa98f45d77d9d2744f2896ab5913f96df80e310eb719e30da86b8c96746`). The source formula result is audited separately from its geometric application.

The general pinned-closure and sink-component proofs are exact for arbitrary finite instances of the stated Boolean form. The canonical source-move application uses only promoted `C-DISJOINT-SWAP-2SAT`. Neither result shows that canonical source geometry forbids the resulting path/fork obstructions.

## Audited theorem

Let `Q` be a finite directed implication graph on variables `x_1,...,x_k`, let `Z` be a set of unary-forbidden variables, and let `F` be a set of unordered forbidden pairs of distinct variables. Consider

`x_i -> x_j` for arcs `i -> j` in `Q`,

`not x_i` for `i in Z`, and

`not(x_i and x_j)` for `{i,j} in F`.

The all-zero assignment satisfies this formula. Given pins `P` forced true and `N` forced false, let `R(P)` be the forward-reachable closure of `P` in `Q`. The pinned formula is satisfiable exactly when

`R(P) intersects (Z union N) = empty`

and no pair in `F` has both endpoints in `R(P)`. If these conditions hold, setting exactly `R(P)` true and every other variable false is a model.

Every failed pin has a short certificate of one of two forms: a directed path from `P` to a variable in `Z union N`; or a forbidden pair `{i,j}` together with directed paths from `P` to `i` and from `P` to `j`. The origins of the two paths may coincide.

Without pins, a nonzero model exists exactly when some sink strongly connected component `S` of `Q` avoids `Z` and contains no pair from `F` internally. The indicator of such an `S` is a model. An acyclic `Q` with `Z` empty therefore always has a singleton model, because forbidden pairs are between distinct variables.

## Independent proof

Every model containing `P` must contain all variables reachable from `P`, since each implication `x_i -> x_j` forces `x_j` whenever `x_i` is true. Thus the two stated obstructions are necessary.

If neither obstruction occurs, set exactly `R(P)` true. It is closed under every implication by definition of reachability. It contains no unary-forbidden variable and no forbidden pair, so all negative clauses hold. Every variable in `N` is false, while every variable in `P` is in `R(P)` and true. This proves sufficiency and identifies an explicit model.

If the criterion fails through `Z` or `N`, a shortest path from a true pin reaches that obstruction. If it fails through a pair `{i,j}` in `F`, both endpoints lie in `R(P)`, so each has a path from some element of `P`. These are exactly the advertised path/fork certificates; no cycle condition is needed.

For the unpinned formula, any nonempty model is forward-closed in the condensation DAG of `Q`. Starting at one of its true components and following outgoing arcs reaches a sink component still in the model. The sink can contain neither a unary prohibition nor a forbidden pair internally. Conversely, the indicator of a sink component has no outgoing implication to a false variable and satisfies all negative clauses precisely under the two stated tests.

## Canonical finite-move application and limits

The promoted `C-DISJOINT-SWAP-2SAT` compilation produces a 2-CNF formula for pairwise disjoint source motions that preserve every old contact under every binary assignment. Its all-zero assignment is the original source, so the formula is zero-valid and has the form above after deleting tautologies and folding repeated-variable negative pairs into unary forbiddances. In a canonical source, a pinned state that locally shortens an old diameter cannot be satisfiable: `C-DISJOINT-SWAP-2SAT` would turn any such model into a strict global or lexicographic competitor. Thus whenever that canonical source-move compilation applies, each failed pinned shortening test has a path or fork certificate. This is a conditional application of the already promoted finite-move theorem, not a new geometric conclusion.

This is a certificate format, not a geometric contradiction. The paths need not be contiguous source paths, and cycles alone do not block a beneficial pin. The canonical owner-contraction regression remains binding: source-path acyclicity does not imply owner-graph acyclicity. The report's composition with outer-face geometry is conditional on its stated owner extraction, localized lower clauses, and harmless upper/unary tests; those conditions are not established here.

## Verifier audit and verdict

The inspected verifier enumerates all 4,131 zero-valid formulas through three variables and compares 110,887 pinned instances against complete truth-table enumeration. It also checks the sink criterion and the harmless implication cycle, harmless conflict triangle, and acyclic blocking fork. Its arithmetic is exact finite Boolean enumeration. It does not encode source geometry, owner extraction, beneficial diameter states, or canonical optimality; the arbitrary-finite-variable statements above are established by the analytic proofs, not by that enumeration.

**Verdict: PASS — promote `C-ZERO-VALID-PINNED-CLOSURE` as a reusable exact certificate theorem.** It refines the finite-move obstruction format without changing C-II or Level I status.

**Exact next obligation:** use canonical source geometry to rule out the path/fork certificates for every locally shortening pin in a source-realized motion family, while checking all old lower and upper pairs; otherwise pursue a different finite competitor route.
