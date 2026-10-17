> Generated reading edition · [exact source](../../../docs/audits/target_c_actual_normal_separate_face_independent_audit_2026-10-09.md) · source SHA-256 `0dbfc348521100935dfd1e7308fabefda17d96d9a38e691517616836daadbe64`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F03C5D8903EA","canonical":true,"claim_ids":["C-ALL-BRANCH-SEPARATE-FACE-FLOOR","C-CII-ACTUAL-DIAMETER-NORMAL-ATOMLESS"],"claim_statuses":{"C-ALL-BRANCH-SEPARATE-FACE-FLOOR":"canonical","C-CII-ACTUAL-DIAMETER-NORMAL-ATOMLESS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit of actual diameter normals and all-branch face cancellation

Date: 2026-10-09  
Audit base: `origin/main` `662ca0d40e7fc28cbc64b2f0caf35bc2dd1704ca`, state `2026-10-09.audit.198`  
Frozen source: `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`  
Source artifact: Sections 10.1–10.2 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.

## Claims and verdicts

**PASS — promote `C-CII-ACTUAL-DIAMETER-NORMAL-ATOMLESS`.** For every unbounded canonical post-ZF C-II source sequence, choose one actual diameter partner for each loaded endpoint (p), put (n_p=(p-p')/D), and set

$$
\nu_D=D^{-1}\sum_{p\in B}\delta_{n_p}.
$$

Every weak limit of these measures is atomless, uniformly over all partner choices. Moreover, for consecutive loaded endpoints (p,q) with (|p-q|\le L) for any fixed (L), their forward chord direction approaches (Jn_p). Neither conclusion uses a Type-II disk limit.

**PASS — promote `C-ALL-BRANCH-SEPARATE-FACE-FLOOR`.** For every such C-II sequence, in either exhaustive global branch and retaining every source point, with (z=b-P_F\ge0),

$$
f-k\ge\frac65\sqrt{R_4}-o(D),
$$

$$
2(q-k)-k-z\ge P_F+\frac65\sqrt{R_4}-o(D),
$$

$$
q-k\ge\frac12P_F+\frac35\sqrt{R_4}+\frac{k+z}{2}-o(D).
$$

These are sequence-asymptotic inequalities with no uniform finite error rate. Type II specializes to the already promoted Audit.174 result. Type I retains its actual (P_F,R_4); the result does not infer a disk, face width, vacancy, finite motion, or strict-D competitor.

## Independent reconstruction

### Strict support, normal windows, and oriented chords

For a diameter pair `p,p'`, with `n=(p-p')/D`, and any other source point `x`,

$$
n\cdot(x-p)\le-\frac{|x-p|^2}{2D}<0.
$$

Thus (p) is a strict exposed vertex of the full-source hull, including when there are contact-isolated points. The canonical full-source midpoint localization gives a common center and radius (L_D=o(D)) for all actual diameter midpoints. Ordering selected support normals around the full-source convex boundary and projecting the exposed endpoints onto the tangent direction gives, for any oriented normal window of half-width (t<\pi/2\),

$$
\#\{p:n_p\text{ in the window}\}\le 1+\frac{D\sin t+2L_D}{\cos t}.
$$

This bound is independent of partner choices. After division by (D), continuous majorants of a point in successively smaller windows show that any weak limit of $\nu_D$ has no atoms. Canonical C-ZRF supplies (q\ge\lceil D\rceil), and the loaded hull perimeter gives (q\le\pi D).

For consecutive loaded vertices (p,q) with (|p-q|\le L), the midpoint identity gives

$$
D(n_p-n_q)=2(p-q)-2(m_p-m_q),
$$

so their chosen normals differ by (o(1)). The cyclic order of strict supporting normals agrees with the cyclic hull-vertex order. If the forward interval from (n_p) to (n_q) were the long interval, all other loaded normals would lie in the complementary (o(1)) window. The window estimate would imply (q=o(D)), contradicting C-ZRF. The short forward normal interval is therefore used; convexity places the forward chord tangent between its rotated endpoint normals, with the positive orientation. This proves the oriented-chord assertion.

### Atomic train population

Take any subsequence on which (R_4/D^2\to r), and jointly extract a weak limit of the empirical train-direction measures with mass (1/D) per complete physical train, including singleton contacts. Their total mass is (O(1)); let (a) be the total atomic mass of a limit. Count each edge of the simple actual train-crossing graph once as an unordered pair. The symmetrized unordered product measure, one half the pushforward of the ordered product train measure, has mass (D^{-2}) on every unordered pair of distinct train labels, so it dominates this crossing measure. By C-PUNCTURED-PHASE, (E_4=O(D)); the rhombus area excess controls the angular deviation from the projective (60^\circ) relation, so the limiting crossing measure is supported on that relation. The unordered product measure charges it only at pairs of atoms.

For any finite collection of atoms, the induced relation graph is triangle-free: no three projective directions can be pairwise separated by (pi/3). At each unordered pair, crossing mass is at most the product of its two atomic masses. Weighted Mantel (equivalently, the weighted Motzkin–Straus bound) gives total crossing mass at most one quarter of the square of the total atomic mass. Exhausting the atoms yields

$$
r\le a^2/4,\qquad a\ge2\sqrt r.
$$

Diagonal shrinking neighborhoods select complete trains (A_D) with (|A_D|/D\to a) and with only (o(D^2)) crossings incident to the complement. Since a train's terminal-midpoint separation is at most its crossing degree, Markov's inequality leaves only (o(D)) complementary trains whose terminal separation exceeds $\epsilon_DD$, for some $\epsilon_D\to0$. Singleton trains have coincident terminal midpoints.

### Boundary recipients and cancellation

Make a finite multigraph with one recipient for every actual outer contact chain between consecutive loaded vertices and a separate recipient for each bounded physical nonquadrilateral contact face. Each complementary train gives an edge between its two actual terminal recipients. Loops and parallel edges remain. This is only an incidence graph; no component is a source path or finite motion.

Fix recipient-count cutoff (M) and recipient-degree cutoff (L). The total recipient and terminal-occurrence counts are (O(D)), so components exceeding either cutoff number (O(D/M)+O(D/L)). Components containing a long complementary train number (o(D)). In every remaining boundary component, a spanning tree uses at most (M-1) train edges; each has terminal-midpoint separation (o(D)). Each recipient has at most (L) boundary occurrences. Consequently all outer-chain bases and facial occurrences in that component are within (o(D)) of one another. The actual-normal identity above gives one common limiting normal and, by the oriented-chord result, one common oriented tangent for all forward outer chords. Each such chord has length in ([1,L]).

Every bounded facial boundary has zero displacement, and the two terminal vectors of every complementary train cancel. Therefore, exactly,

$$
\sum_{W_i\text{ in the component}}(b_{i+1}-b_i)
=\sum_{\text{selected atomic terminal occurrences in the component}}e.
$$

The left side has nonzero limiting vector: there is at least one outer chain and all its boundedly many forward chords have a common oriented tangent and length at least one. Mark the component by one chain-base normal and its ordered list of selected atomic terminal vectors. For fixed (M,L), each list has at most (ML) entries. Every coordinate marginal is dominated by the selected terminal-vector measure and hence is supported in the countable signed direction set of train atoms. There are countably many such finite lists. The exact cancellation identity determines the limiting normal from the normalized, nonzero list sum, so the normal marginal is countably supported. Distinct components choose distinct chain bases, so this same marginal is dominated by $\nu_D$; every limit of the latter is atomless. The marginal must vanish. Thus, for fixed cutoffs, the retained boundary-component count is (o(D)). The discarded-component bounds followed by (M,L\to\infty) give

$$
c_{\partial}=o(D).
$$

### Exact face ledger, including interior-only components

Let (f_{\partial}) be the number of exceptional faces in boundary components, (N_{\partial}) and (N_\circ) the complementary-train edge counts in boundary and interior-only components, and (Q_\circ) the exceptional-face excess in the latter. Connectivity of the recipient multigraph, including loops and parallel edges, gives

$$
N_{\partial}\ge q+f_{\partial}-c_{\partial}.
$$

Occurrence-counted terminal handshake gives the nonnegative boundary remainder

$$
0\le a_{\partial}=b+4f_{\partial}+Q-Q_\circ-2N_{\partial}
\le2f_{\partial}-Q_\circ-2k+2c_{\partial}.
$$

Every interior-only exceptional face contributes at least one unit to (Q_\circ), hence (Q_\circ\ge f-f_{\partial}), and therefore

$$
3f_{\partial}\ge f+2k-2c_{\partial}.
$$

The exact interior-only atomic terminal population is (4(f-f_{\partial})+Q_\circ-2N_\circ). Adding it to (a_{\partial}), dividing by two, and using the previous inequality yields

$$
3(|A_D|+N_\circ)\le5(f-k+c_{\partial}).
$$

Divide by (D), use (|A_D|/D\to a\ge2\sqrt r\), (N_\circ\ge0), and (c_{\partial}=o(D)). This gives $\liminf(f-k)/D\ge6\sqrt r/5$ along every joint-limit subsequence. Every subsequence has a further subsequence with (R_4/D^2\) convergent, proving the first bound. Finally, with (z=b-P_F\), the canonical train/face identity gives

$$
2(q-k)-k-z=P_F+Q-k\ge P_F+f-k,
$$

which implies the two scalar bounds.

## Adversarial checks and certificate scope

- The recipient graph is not confused with the source-level train graph. Loops, parallel edges, repeated singleton-bridge occurrences, and interior-only components are retained with facial multiplicity.
- The bounded-component argument uses a spanning tree, so an arbitrary number of parallel edges cannot invalidate the distance control; degree cutoffs bound the total terminal occurrences separately.
- Strict diameter normals are formed using the full source and its actual partners. Contact-isolated source points remain in all source constraints, hulls, and diameter calculations.
- The proof does not infer spare capacity from area, a finite feasible move from a first-order or cancellation identity, or a global minimizer conclusion from the auxiliary graph.
- The old Type-II proof's disk surface measure and near-disk population equality are not premises here. Audit.174 remains a correct Type-II specialization, while this theorem retains actual (P_F) and (R_4) in Type I.
- Inspected and reran `research/verify_target_c_terminal_cancellation_interior_2026_10_08.py`: PASS with exact `Fraction` arithmetic, 8 nonglobal fixtures, 7,252 all-source lower-pair checks, 108 physical terminal-pair checks, 52 interior terminal occurrences, 4 singleton trains, 8 repeated outer-bridge occurrences, 354 auxiliary selections, 620 component identities, 354 separate-face graph selections, and 886 cancellation checks. It verifies finite facial identities only; it does not prove the asymptotic normal, atom-selection, or global-optimality statements.

## Canonical dependencies and frontier effect

The audited proof uses `C-FS-GEOM`, `C-ZRF`, `C-WOODALL`, `C-LOADED-HULL`, `C-TRAIN-INTERFACE-CURRENCY`, `C-LINEAR-NONMATCH`, `C-RHOMBUS-POP`, and `C-PUNCTURED-PHASE`. In particular, C-ZRF and Woodall give `q>=D`, which is needed to orient consecutive loaded chords. The proof does not depend on the Type-II near-disk theorem or on the Type-II atomic boundary-cost theorem. The added face floor applies in both exhaustive C-II branches and sharpens the Type-I ledger when (R_4) is substantial. It supplies no uniform positive increment when (R_4=o(D^2)), no capacity, and no source competitor. C-II and Level I remain open; the active obligation is to convert the remaining branch-specific train/face quantities into capacity or a source improvement.

The frozen source hash and branch tip were rechecked after the audit. No discovery-worker branch or worktree was changed.

## Promotion transaction

Theorem-bearing PR #906 head `1e7e6eb70288fdeb6181bfbad5551c9670e39186` merged as `0e72a5215ba9249b6e0ab5113f331eeea7a4739a`. Protected `state-consistency` run `37968342311` passed in 7m02s, including all 94 registered certificates and patch-whitespace validation.
