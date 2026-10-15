<!-- theorem-state: {"artifact_id":"ART-9C7F5B37F2C1","canonical":true,"claim_ids":["C-SIX-SIDED-WALL-HIGHEST-POPULATION-LIMIT"],"claim_statuses":{"C-SIX-SIDED-WALL-HIGHEST-POPULATION-LIMIT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: Oler equality pins the highest wall population

Date: 2026-10-07. Source branch: research/sol/target-c-owner-order-closure-20261006, audited theorem snapshot 0d3b0182c064f73d2a6a64452ee01d140f1b1475. The source report remains docs/reports/target_c_sorted_rate_packet_classification_2026-10-06.md with lifecycle unreviewed; only the limiting reduction below is promoted.

**Verdict: PASS WITH NARROWED SCOPE — promote the Oler equality limit, not the finite local classification or highest-population exclusion.**

## Exact statement

Fix \(M\ge3\), set \(N=3M^2-3M+1\), and use the six-sided curved wall \(W_{M,\theta}\) from the canonical one-corner wall construction. Each of its six sides has \(M\) unit edges, its perimeter is \(6M\), and as \(\theta\downarrow0\) its vertices converge to the vertices and unit-spaced side points of the regular hexagon \(H_M\) of side length \(M\).

For any sequence \(\theta_k\downarrow0\), let \(X_k\) consist of the \(6M\) wall vertices together with exactly \(N\) additional points in the closed wall, with every pair in \(X_k\) at distance at least one. Then there is a subsequence and relabeling of the additional points for which
\[
X_k\longrightarrow P_M=\{iu+jv:\max(|i|,|j|,|i+j|)\le M\},
\]
where \(u,v\) are unit triangular-lattice generators aligned with the limiting wall. Consequently, the \(N\) additional points converge as an unordered set to the strict interior chart \(P_{M-1}\).

Equivalently, for every \(\varepsilon>0\), all sufficiently small \(\theta>0\) placements in this wall class are within \(\varepsilon\) of \(P_{M-1}\), after relabeling. This is only an asymptotic localization. It gives no \(O(\theta)\) rate, no exact finite-\(\theta\) classification, and no triangle-free exclusion.

## Independent proof

At \(\theta=0\), \(W_{M,\theta}\) tends to \(H_M\). Its area and perimeter are
\[
\operatorname{area}(H_M)=\frac{3\sqrt3}{2}M^2,
\qquad \operatorname{per}(H_M)=6M.
\]
The total number of points in \(X_k\) is
\[
N+6M=3M^2+3M+1
=\frac{2}{\sqrt3}\operatorname{area}(H_M)
 +\frac12\operatorname{per}(H_M)+1.
\]

The sets are uniformly bounded. Passing to a subsequence, every wall point and every additional point converges. Pairwise distances at least one are closed under limits, so the limiting set has \(3M^2+3M+1\) distinct unit-separated points in \(H_M\). It attains equality in the finite Oler inequality.

For the equality case, the audit checked K. J. Böröczky and I. Z. Ruzsa, *Note on an inequality of Wegner*, page 2, equation (2) and the paragraph following it. The paper states the Thue–Groemer/Oler equality alternative: a segment case, or a convex hull triangulable using all centers into regular triangles with edge length two when the nonoverlapping disks have radius one and centers are separated by two. Scaling coordinates by one half gives unit separation and edge-one triangles. The segment case is impossible because \(H_M\) has positive area. The equality case therefore triangulates \(H_M\) into unit equilateral triangles using all limiting points as vertices.

A consecutive pair of limiting wall vertices along a side is a unit edge. Its direction fixes the triangular lattice orientation. In a connected triangulation, each neighboring equilateral triangle's third vertex is one lattice step in one of the two \(\pm60\)-degree directions, so propagation across the triangulation puts every vertex in that lattice. The regular hexagon \(H_M\) contains exactly
\[
1+\sum_{r=1}^{M}6r=3M^2+3M+1
\]
lattice points, namely \(P_M\). The equality set has this many distinct points and is contained in \(P_M\), so it is all of \(P_M\). Its \(6M\) prescribed wall points are the boundary layer; the additional \(N\) points are exactly \(P_{M-1}\).

Every convergent subsequence has the same limiting set. If the uniform-neighborhood formulation failed, a countersequence with \(\theta_k\downarrow0\) would have a convergent subsequence with this same limit, a contradiction. This proves the stated localization without a quantitative rate.

## Literature scope and adversarial checks

The equality source is the Thue–Groemer equality case reported by Böröczky and Ruzsa as a reliable transcription of Groemer's result; it is not the Rogalski–Saint Raymond disk-equality claim rejected elsewhere in the repository. The source PDF is preserved at papers/related/boroczky-ruzsa-2007-note-on-wegner.pdf, SHA256 95db9d8f80f91b4f34ee25e61866b57b6e1676f6326af6b01de88ca29d9d9467; the paper is also available [from the authors' institute](https://www.renyi.hu/~carlos/wegner.pdf).

This proof uses only the limiting regular hexagon and the equality case. It does not classify placements for positive \(\theta\), prove a stress continuation, imply that a nearby placement is one of the sorted-rate packets, or show that it contains a triangle. It applies to the selected wall vertices and \(N\) enclosed points, even if a larger source has additional points outside the wall; those outside points are simply not used in the Oler equality count. It makes no claim about the general \(z=N-1\) population.

## Canonical disposition

Promote C-SIX-SIDED-WALL-HIGHEST-POPULATION-LIMIT at the exact sequential/asymptotic scope above. Keep the finite sorting classification and the arbitrary \(z=N\) triangle exclusion unreviewed. The \(z=N\) branch now reduces to the local problem near \(P_{M-1}\); the C-II wall extraction and the exact finite packet classification remain open.
