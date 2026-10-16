<!-- theorem-state: {"artifact_id":"ART-FE4EBE9736DD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C37: planar attachment incidence is almost a partition

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C33-C36 and planar Euler counting  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Contract each unpinned component `I_r` to one interior node and retain one incidence edge to each distinct loaded attachment `b in A_r`. The resulting simple bipartite graph `J` is planar with all loaded-side vertices on the boundary of the force hull.

Let

- `q_used` be the number of loaded vertices used by at least one attachment set;
- `c_I` be the number of unpinned components; and
- `s` be the number of connected components of `J` containing an interior node.

Then

\[
\boxed{
\sum_r|A_r|\le q_{used}+2c_I-2s.}
\]

Equivalently, if `m_b` is the number of distinct unpinned components attached to a used loaded vertex `b`,

\[
\boxed{
\sum_{b\in B_{used}}(m_b-1)\le2c_I-2s.}
\]

Thus at most `2c_I-2s` used loaded vertices can belong to multiple attachment sets.

---

## 1. Incidence graph

Let

\[
B_{used}:=\bigcup_r A_r.
\]

Construct `J` with bipartition `B_used` and one interior node `x_r` per `I_r`, with edge `b x_r` iff `b in A_r`. Multiple unit contacts between the same loaded vertex and component produce only one incidence edge. Hence

\[
|E(J)|=\sum_r|A_r|.
\tag{C37.1}
\]

Starting from the plane contact graph, contract a spanning tree inside each `I_r` and delete parallel duplicate attachment edges. Planarity is preserved. The loaded vertices retain their cyclic order on the boundary of `F`.

Let the connected components of `J` containing interior nodes be `J_1,...,J_s`. For one component write `q_j,c_j,e_j` for its loaded vertices, interior nodes, and incidence edges.

---

## 2. Outer-face length

Every loaded vertex of `J_j` lies on the outer face and has positive degree. Because `J_j` is bipartite, its outer-face boundary walk alternates loaded and interior nodes. Every loaded vertex occurs at least once on that walk. Therefore its outer-face walk length `L_j` satisfies

\[
L_j\ge2q_j.
\tag{C37.2}
\]

Every bounded face walk of the simple bipartite plane graph has length at least four.

Let `f_j` count all faces. Summing face-walk lengths,

\[
2e_j\ge L_j+4(f_j-1)
\ge2q_j+4(f_j-1).
\tag{C37.3}
\]

Euler gives

\[
q_j+c_j-e_j+f_j=2.
\tag{C37.4}
\]

Eliminating `f_j` yields

\[
\boxed{e_j\le q_j+2c_j-2.}
\tag{C37.5}
\]

Summing over `j` proves:

### Theorem C37.1

\[
\boxed{
\sum_r|A_r|
\le q_{used}+2c_I-2s.}
\tag{C37.6}
\]

Since C36 gives `|A_r|>=3`, also

\[
\boxed{c_I+2s\le q_{used}.}
\tag{C37.7}
\]

---

## 3. Excess attachment multiplicity

For a used loaded vertex `b`, let

\[
m_b:=|\{r:b\in A_r\}|.
\]

Then

\[
\sum_bm_b=\sum_r|A_r|.
\]

Every used vertex has `m_b>=1`, so C37.6 gives

\[
\boxed{
\sum_{b\in B_{used}}(m_b-1)
\le2c_I-2s.}
\tag{C37.8}
\]

Therefore the number of used loaded vertices belonging to two or more distinct attachment sets is at most

\[
\boxed{2c_I-2s.}
\tag{C37.9}
\]

The incidence cyclomatic number is

\[
\kappa(J)=|E(J)|-(q_{used}+c_I)+s,
\]

so C37.6 also gives

\[
\boxed{\kappa(J)\le c_I-s.}
\tag{C37.10}
\]

---

## 4. Near-minimal implication before quotient connectivity

C33 says `c_I+e_BB<=sigma_B`. Thus if `sigma_B=o(D)`, then `c_I=o(D)` and the attachment incidence has only `o(D)` excess multiplicity and `o(D)` independent incidence cycles.

C38 will show that unused loaded vertices are also charged by `e_BB`, completing the asymptotic-partition statement.

---

## 5. Regression audit

- One interior component attached to all used boundary vertices: `c_I=s=1`, equality in C37.6.
- Two components sharing two loaded pins: allowed and uses the full excess multiplicity budget in the smallest connected case.
- Three shared loaded pins between two disjoint interior components are impossible by C37.9/planarity.

```text
C37:
Contract each unpinned component to one interior node, keeping one edge to each
distinct loaded attachment.  The planar bipartite incidence graph has all loaded nodes
on its outer face.  Euler plus outer-face length >=2q_j gives per connected piece
    e_j<=q_j+2c_j-2.
Thus
    sum |A_r|<=q_used+2c_I-2s,
    sum_b(m_b-1)<=2c_I-2s,
    kappa(J)<=c_I-s.
```
