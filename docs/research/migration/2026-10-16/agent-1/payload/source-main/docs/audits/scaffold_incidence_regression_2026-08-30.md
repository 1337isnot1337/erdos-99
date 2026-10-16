<!-- theorem-state: {"artifact_id":"ART-A40A5B61E5FE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Exact scaffold-incidence regression: hidden Hall nullity

This note records a finite, exact audit of the monomer--dimer incidence model used
in the Target A scaffold. It is a combinatorial regression only: the example is not
claimed to arise from a globally optimal packing.

## Statement

Use the integer triangular-lattice coordinates from
research/scaffold_cells.py. A monomer is one elementary triangle, and a legal
family has no repeated elementary triangle. For a selected family \(S\), write

\[
\delta(S)=|S|-|N(S)|,
\qquad
d(S)=|S|-\nu(S),
\]

where \(N(S)\) is the set of incident lattice vertices and \(\nu(S)\) is the maximum
cell-to-vertex matching size. The first quantity is the raw phase/Euler charge of
the entire selected family; the second is the Hall nullity, equivalently the maximum
deficiency over all subfamilies.

Consider the following 13 monomer triangles, written as
\((\text{orientation},i,j)\):

\[
\begin{aligned}
S_0=\{&(-,-1,-1),(+,-1,0),(-,-1,0),(+,-1,1),(-,-1,1),\\
       &(+,0,-1),(-,0,-1),(+,0,0),(-,0,0),(+,0,1),\\
       &(+,1,-1),(-,1,-1),(+,1,0)\}.
\end{aligned}
\]

The exact enumerator gives

\[
|S_0|=13,
\qquad |N(S_0)|=12,
\qquad \nu(S_0)=12,
\qquad \delta(S_0)=d(S_0)=1.
\]

Now add the remote monomer \(r=(+,4,4)\). The enlarged family

\[
S=S_0\cup\{r\}
\]

is still legal, but

\[
|S|=14,
\qquad |N(S)|=15,
\qquad \nu(S)=13,
\qquad \delta(S)=-1,
\qquad d(S)=1.
\]

The maximum-deficiency Hall witness returned by the alternating forest is exactly
the original core \(S_0\), with 13 cells, 12 vertices, and deficiency one. Thus the
full selected complex has negative raw deficiency even though its transversal
matroid still has positive left nullity.

## Interpretation for Target A

The cell-complex identity remains exact for every chosen subfamily:

\[
|Q|-|N(Q)|
=\frac{m_3(Q)-b(Q)}2-\chi(Q)
=\frac1{12}\sum_{v\in N(Q)}(4p_v(Q)+3q_v(Q)-12).
\]

What fails is the stronger substitution

\[
d_{\rm sc}\stackrel{?}{=}
\frac1{12}\sum_{v\in N(S)}(4p_v(S)+3q_v(S)-12)
\]

for the entire scaffold \(S\). The exact quantity is the maximum of that expression
over subfamilies \(Q\subseteq S\). A remote or otherwise low-charge part of the
scaffold can reverse the sign of the whole-complex charge without removing a dense
Hall core.

Consequently, any proposed proof of the Target A endpoint

\[
d_{\rm sc}\ge \Delta_\Lambda
\]

must either exhibit the deficient subfamily (or an equivalent transversal-matroid
certificate), or prove a source-specific reason that the relevant maximum cannot be
hidden in this way. The regression does not address the missing global-optimality
input and does not close or refute Erdős Problem #99.

The executable certificate is covered by
research/test_scaffold_cells.py,
test_hall_witness_can_hide_inside_negative_total_charge.
