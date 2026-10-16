<!-- theorem-state: {"artifact_id":"ART-A6C5C06A3938","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — source-backbone Hall obstruction

**Date:** 2026-08-30
**Repository state:** `origin/main` at `bd5c534`; work branch
`research/activation-flat-2026-08-30` (merged with the promoted Section 157 rate)
**Run type:** theorem audit / Target A promotion
**Target:** A
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.5_FINAL_CONTINUATION_PROMPT.md`
**External web search:** not used
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

The response endpoint is

\[
\dim\ker S\ge \Delta_\Lambda-d_{\rm int}.
\]

The proposed source theorem had to add a global obstruction unavailable from the exact
fixed-hull Hall capacity bound. It does so through the source diameter graph, but no
map to the Schur response is obtained.

## 2. Audited theorem

Let \(A=P\sqcup R\) be a unit-separated source minimizer with

\[
|A|=N,\quad |P|=m=N-|R|,\quad D=\operatorname{diam}A,
\]

where every point of \(R\) is a strict rattler. Let \(X_m\) be an \(m\)-point global
optimum of diameter \(d\). Let \(\mathcal D_P(A)\) be the graph on \(P\) consisting
of the diameter-\(D\) pairs, and let \(\tau_D(A)\) be its vertex-cover number. For
\(\delta>0\), join \(x\in X_m\) to \(p\in P\) when \(|x-p|<\delta\). If

\[
d+2\delta\le D,
\]

then

\[
\boxed{\max_{Q\subseteq X_m}(|Q|-|N_P^\delta(Q)|)\ge\tau_D(A).}
\]

If \(N_-:=\min\{q:D(q)=D\}\) and \(p_N=N-N_-\), then

\[
\boxed{\tau_D(A)\ge p_N+1.}
\]

In the Section 155 common placement, with \(d+2<D\), a maximizing set \(Q\) obeys

\[
|N_R(Q)|\ge h-\widehat p_H,
\qquad h=|Q|-|N_P(Q)|,
\]

and \((P\setminus N_P(Q))\cup Q\) is a unit-separated subset of the source hull
of cardinality \(m+h\).

### Proof

Consider a matching in the strict \(\delta\)-conflict graph. If matched backbone
points \(p,q\) formed a diameter edge, with distinct partners \(x,y\), then

\[
|p-q|\le |p-x|+|x-y|+|y-q|<\delta+d+\delta\le D,
\]

contradicting \(|p-q|=D\). The matched backbone vertices are therefore an
independent set in \(\mathcal D_P(A)\), of size at most
\(m-\tau_D(A)\). Hence the matching number is at most that quantity. The deficiency
form of Hall's theorem gives the first bound.

For the cover bound, if a vertex cover \(C\) of \(\mathcal D_P(A)\) had size
\(c\le p_N\), then \(A\setminus C\) would have \(N-c\ge N_-\) points and diameter
strictly below \(D\). Since \(D(q)=D\) throughout \(N_-\le q\le N\), this contradicts
the definition of \(D(N-c)\). Thus every cover has size at least \(p_N+1\).

In the common placement, apply the exact source Hall inequality to a maximizing \(Q\):

\[
\widehat p_H\ge |Q|-|N_A(Q)|
=h-|N_R(Q)|.
\]

The displayed lower bound follows. The set \(Q\) is internally unit-separated and has
no strict conflict with \(P\setminus N_P(Q)\), proving the final feasibility and
cardinality statement. \(\square\)

## 3. Exact target implication

This is a genuine global source/smaller-optimum relation and survives the non-global
Section 152 regression. It does not exceed the fixed-source capacity ceiling because
the required deficiency is absorbed by \(N_R(Q)\). It therefore changes neither
\(d_{\rm sc}\) nor \(\dim\ker S\).

## 4. Remaining lemma

Combine the diameter-cover witness, the captured strict rattlers, and the Section
156 activation flat with the co-phased scaffold to obtain either a rank-\(s\) subspace
of the Schur kernel or an \(N\)-point packing of diameter strictly below \(D\). The
needed source-to-response map is not constructed.

## 5. Audit classification and regressions

| Claim | Classification | Reason |
| --- | --- | --- |
| Diameter matching can use only a diameter-independent backbone set | proved | Triangle inequality with the strict \(\delta\) margins. |
| Source diameter-cover number is at least \(p_N+1\) | proved | Removing a cover would beat the entire left \(D\)-plateau. |
| Backbone Hall deficiency alone contradicts capacity | rejected | Strict rattler conflicts absorb it under the exact fixed-source Hall bound. |
| The witness is already a Schur-kernel vector | unproved | Source and scaffold terminals remain independent. |
| Regular shells/diameter stars force a super-boundary cover | rejected | Their cover number may be boundary-order or small. |

## 6. Canonical promotion

**Promote now** through `docs/targets/target-a/10-source-backbone-hall-obstruction.md`
and the route/documentation maps. No external theorem or computation is used.

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

New theorem:
For d+2δ≤D, matching an m-point smaller optimum to the m-point source backbone
has Hall deficiency at least the source diameter-graph cover number, itself at least
p_N+1. In the common placement, the excess is captured by strict rattlers.

Remaining endpoint:
Map this captured source witness, together with the activation flat, to s independent
Schur null directions or a strict sub-D replacement.
```
