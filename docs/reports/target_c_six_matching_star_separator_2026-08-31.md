<!-- theorem-state: {"artifact_id":"ART-C2D26585088E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: star equality forces a high-degree terminal separator

**Date:** 2026-08-31
**Repository state:** `b5edaea` (`origin/main` before this promotion)
**Run type:** proof / literature import / C-II equality reduction
**Target:** Target C-II, selected three-edge six-terminal matching
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`
**External web search:** used for the exact circular-minor and Gallai \(T\)-path statements
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The K6 response inequality leaves only its \(\rho=1\) equality mode in the convex
six-terminal matching. EQ6 and CONC6 identify that mode with a star-equivalent
boundary response. The theorem below shows that such a response is incompatible
with the established degree caps in the fully force-visible branch \(C=C_*\).
It does not settle C-I, where the selected stress need not have the maximal
contact support, and it does not address larger diameter supports.

## 1. Starting endpoint

For a selected normalized stress with three opposite diameter pairs on a strictly
convex six-terminal boundary, K6 gives

\[
\rho_s\le 1.
\]

EQ6 says that equality forces an additive effective-resistance metric, and CONC6
places its weighted barycenter in all three matching chords. The exact implication
needed here is

```text
\rho_s=1+\text{C-II degree caps}
\quad\Longrightarrow\quad\text{star boundary response}
\quad\Longrightarrow\quad\text{no two disjoint terminal paths}
\quad\Longrightarrow\quad\text{one high-degree terminal separator}
\quad\Longrightarrow\quad\text{contradiction}.
```

## 2. Strongest genuinely new audited theorem

### Theorem SEP6 (star equality has a high-degree separator)

Let \(G\) be a connected positive circular-planar electrical network embedded in a
closed disk, with six distinct boundary terminals

\[
T=(t_0,t_1,t_2,t_3,t_4,t_5)
\]

in cyclic order. Suppose its response matrix has an additive resistance metric

\[
W_{ij}=r_i+r_j\qquad(i\ne j),
\]

with \(r_i>0\). Then there is a vertex \(z\in V(G)\) such that every component of
\(G-z\) contains at most one terminal. Consequently,

\[
\deg_G(z)\ge
\begin{cases}
6,&z\notin T,\\
5,&z\in T.
\end{cases}
\tag{SEP6.1}
\]

In particular, a six-terminal star-equivalent response is impossible if every
nonterminal has degree at most \(5\) and every terminal has degree at most \(3\).

### Scope

This is a finite graph/network theorem. It applies to the actual circular-planar
contact network represented by the C11 response; it does not replace that network
by a geometrically embedded star. The final degree contradiction additionally
requires the C-II hypothesis \(C=C_*\), a relative-interior contact stress, and
the C26/C35 degree bounds.

### Proof

For disjoint ordered terminal lists \(P=(p_1,p_2)\) and \(Q=(q_1,q_2)\) forming a
circular pair, the star response associated with the additive resistance metric is

\[
\Lambda_{ij}=-\frac{g_i g_j}{\Gamma}\quad(i\ne j),
\qquad
g_i=r_i^{-1},\quad \Gamma=\sum_{k=0}^5g_k.
\]

Indeed, the star with conductance \(g_i\) on its \(i\)-th terminal leg has
effective resistance \(r_i+r_j\) between terminals \(i\) and \(j\); equivalently,
the centered resistance matrix is \(J\operatorname{diag}(r)J\), whose inverse on
\(\mathbf 1^\perp\) is the displayed response. Thus this is the response forced
by the additive metric, not an alteration of the source network.

Therefore

\[
\det \Lambda[P;Q]
=\frac{g_{p_1}g_{p_2}g_{q_1}g_{q_2}}{\Gamma^2}
 -\frac{g_{p_1}g_{p_2}g_{q_2}g_{q_1}}{\Gamma^2}
=0.
\tag{SEP6.2}
\]

For a positive circular-planar network, the circular-minor connection theorem
says that a size-two circular minor is strict exactly when the network contains a
two-connection for that circular pair: two vertex-disjoint paths joining the
corresponding terminal pairs, with no terminal in the interior of either path.
The sign convention is immaterial here because the minor has size two. Hence
(SEP6.2) rules out every such two-connection.

Now call a path with two distinct endpoints in \(T\) and no internal vertex in
\(T\) a \(T\)-path. If two vertex-disjoint \(T\)-paths existed, their four distinct
boundary endpoints would be joined in a noncrossing pairing: an alternating
pairing would force two arcs in the disk to intersect. Thus the two paths would
form a size-two circular connection, contradicting (SEP6.2). The maximum number
\(\nu_T(G)\) of vertex-disjoint \(T\)-paths is therefore one. It is at least one
because \(G\) is connected and \(|T|=6\).

Apply Gallai's \(T\)-path min-max theorem:

\[
\nu_T(G)=
\min_{X\subseteq V(G)}
\left(
|X|+\sum_{K\in\operatorname{Comp}(G-X)}
\left\lfloor\frac{|T\cap K|}{2}\right\rfloor
\right).
\tag{SEP6.3}
\]

The minimum is one. The choice \(X=\varnothing\) has value
\(\lfloor 6/2\rfloor=3\), since \(G\) is connected. A minimizing \(X\) must
therefore have \(|X|=1\), and the sum in (SEP6.3) must be zero. Writing
\(X=\{z\}\), every component of \(G-z\) contains at most one terminal.

If \(z\notin T\), the six terminals lie in six distinct components of \(G-z\).
Since \(G\) is connected, each of those components has a neighbor of \(z\), and
the neighbors are distinct across components. Thus \(\deg_G(z)\ge6\). If
\(z\in T\), the other five terminals lie in five distinct components, giving
\(\deg_G(z)\ge5\). This proves (SEP6.1). \(\square\)

## 3. Exact Target C-II implication

Assume \(C=C_*\) and choose a relative-interior normalized KKT stress. Then the
positive contact network is the full nonisolated contact graph. C26 and C35 give

\[
\deg_C(v)\le5\quad(v\notin B_+),
\qquad
\deg_C(b)\le3\quad(b\in B_+).
\tag{SEP6.4}
\]

Consider the six-endpoint matching case \(H_s=\{03,14,25\}\). If
\(\rho_s=1\), EQ6 and CONC6 give the positive additive resistance parameters and
the star response required by SEP6. The boundary terminals are precisely the six
vertices \(B_+\), while all other contact vertices are nonterminals. SEP6 then
requires either an unloaded vertex of degree at least six or a loaded vertex of
degree at least five, contradicting (SEP6.4).

Therefore, in this fully force-visible six-terminal subcase,

\[
\boxed{\rho_s<1.}
\tag{SEP6.5}
\]

The selected K6 response obstruction is consequently strict in the only equality
mode left by the Kalmanson argument. This is an exact C-II subcase reduction, not
a general PSD comparison for arbitrary diameter support.

## 4. Dependencies and literature imports

- `docs/reports/target_c_six_matching_equality_star_2026-08-31.md`, Theorem EQ6:
  equality gives the additive resistance metric.
- `docs/reports/target_c_six_matching_equality_concurrency_2026-08-31.md`,
  Theorem CONC6: the additive parameters are positive for the strictly convex
  six-terminal geometry.
- `docs/reports/target_c_force_polygon_2026-08-30.md`, Theorem C11:
  the response is the actual C11 contact-network response and obeys the affine
  force identity.
- `docs/reports/target_c_loaded_boundary_attachment_2026-08-31.md`, Theorem C35:
  loaded contact degree is at most three.
- The circular-minor connection statement is Lemma 3.4 in S. Forcey,
  [*Kalmanson-Kron reconstruction*](https://sforcey.github.io/sf34/kron.pdf),
  which records the Curtis--Ingerman--Morrow characterization: a circular minor
  is strict exactly when the corresponding nonintersecting connection exists.
  The present use is only the size-two case and the positive-conductance
  circular-planar hypotheses match C11.
- The \(T\)-path min-max formula (SEP6.3) is Theorem 2 in T. Kaiser,
  [*Disjoint T-paths in tough graphs*](https://iti.mff.cuni.cz/series/2005/270.pdf).
  We use the formula for an arbitrary finite connected graph; no toughness
  assumption is used.

## 5. Why it is new

EQ6 classified the equality response electrically, and CONC6 extracted a common
geometric chord point. SEP6 is the first source-network consequence: it converts
the vanishing of all size-two circular minors into a one-vertex terminal separator,
then uses the C-II degree caps to exclude that separator. It is stronger than a
literal-star heuristic because it applies to the actual contact graph through its
response minors.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Star equality makes every disjoint two-by-two circular minor zero | proved | Direct determinant calculation from the additive/star response. |
| A two-connection gives a strict circular minor | literature import | Forcey Lemma 3.4, with positive conductances and circular-planar embedding. |
| Two disjoint \(T\)-paths give a circular two-connection | proved | Their disk embedding forces the endpoint pairing to be noncrossing. |
| Six terminals force a one-vertex separator when no two \(T\)-paths are disjoint | proved with literature input | Gallai's exact formula and connectedness reduce the minimizer to one vertex. |
| C-II six-terminal equality is impossible | proved | SEP6 plus C26/C35 degree caps. |
| Equality is impossible for every selected stress in C-I | not proved | The maximal-support degree caps need not apply to an arbitrary selected stress. |
| The physical contact graph is a literal star | rejected | Only the boundary response is star-equivalent; electrical equivalence does not preserve the embedded source. |
| Target C is closed | not proved | Larger diameter supports, support selection, C-I, and the remaining C-II bulk branches remain. |

## 7. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Six-leaf star network | yes | It has a degree-six interior hub, exactly the SEP6 conclusion. |
| Star with the hub itself a terminal | yes | The hub has degree at least five to the other terminal components. |
| A path network with six terminals | yes | It has two disjoint \(T\)-paths and hence a positive circular minor; it is not star-equivalent. |
| Three-terminal triangle | yes | The six-terminal hypothesis is essential; Gallai's formula gives a different \(X=\varnothing\) value. |
| Regular centrally symmetric six-endpoint geometry | yes | Geometry alone allows equality, but the fully force-visible degree caps rule out its actual six-terminal contact network. |
| C33 abstract sign-cone matrix | yes | It is not circular-planar and so need not obey the strict circular-minor implication. |

## 8. Failed routes and no-go results

### Treating electrical star equivalence as a geometric star

The proof never inserts a hub into the source. It uses only the zero circular
minors of the boundary response and the all-minors connection theorem. This is why
the conclusion survives arbitrary interior Kron reductions.

### Extending SEP6 to C-I without maximal support

The degree contradiction uses C26/C35 for the full \(C=C_*\) contact graph. A
selected stress in C-I may have a smaller positive contact support and may not
inherit those degree bounds. SEP6 therefore does not eliminate the diameter-shear
separator or solve support selection.

## 9. Exact remaining lemma

The highest-value continuation is now one of:

1. extend the SEP6 separation argument to a larger positive diameter support or to
   the direction-dependent support-selection stress; or
2. prove a C-II transport theorem that forces the remaining strict K6 response
   defect into the C41/C42 global packing contradiction.

The six-terminal equality mode itself is no longer a live C-II obstruction.

## 10. Canonical promotion recommendation

**Promote now — proof audited and frontier changes.**

Promote the result into:

- `docs/targets/target-c/01-force-hull-and-shear.md`;
- `docs/targets/target-c/README.md`; and
- `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`.

## 11. Compact handoff

```
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
In a connected six-terminal circular-planar network, an additive/star-equivalent
boundary response forces a vertex whose deletion leaves at most one terminal per
component. That vertex has degree at least six if unloaded and at least five if it
is a terminal.

Exact C-II effect:
Under \(C=C_*\), C26/C35 cap unloaded degrees at five and loaded degrees at three.
Therefore the K6 \(\rho=1\) equality mode is impossible for the actual six-terminal
fully force-visible contact network; \(\rho<1\) in that subcase.

Binding limitation:
The argument is source-preserving but C-II-only. It does not control arbitrary
selected stresses in C-I, larger diameter supports, or the remaining force-bulk
and bridge branches.

Highest-value next lemma:
Transport the strict six-terminal response defect, or generalize the separator
argument to larger support, into a global packing contradiction.
```
