<!-- theorem-state: {"artifact_id":"ART-DE7149C55F0C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: additive response is impossible with six or more force-visible terminals

**Date:** 2026-08-31
**Repository state:** `c3a5b9a` (`origin/main` before this promotion)
**Run type:** proof / literature import / C-II equality generalization
**Target:** Target C-II, additive-response equality modes
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`
**External web search:** not used beyond the already audited circular-minor and Gallai inputs
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

SEP6 treated six terminals. The same argument works for any \(q\ge4\) boundary
terminals. Combined with C34, it excludes every additive/star-equivalent response
in the fully force-visible canonical branch once \(D\ge9\), because then
\(|B_+|\ge6\). This does not assert that equality for a larger diameter support is
additive; proving or excluding such non-additive equality remains open.

## 1. Starting endpoint

The K6/EQ6 route identifies the six-terminal \(\rho=1\) mode with an additive
effective-resistance metric. SEP6 then excludes it under C-II degree caps. The
general implication is

```
additive response on q terminals, q >= 4
    -> no two disjoint terminal paths
    -> one separator of degree at least q or q-1
    -> C26/C35 contradiction when q >= 6.
```

## 2. Strongest genuinely new audited theorem

### Theorem SEPq (additive response has a high-degree separator)

Let \(G\) be a connected positive circular-planar electrical network embedded in a
closed disk, with \(q\ge4\) distinct boundary terminals \(T\) in cyclic order.
Suppose the effective-resistance matrix is additive:

\[
W_{ij}=r_i+r_j\qquad(i\ne j),
\]

where the effective-resistance parameters satisfy \(r_i\ge0\). Then there is a
vertex \(z\in V(G)\) such that every component of \(G-z\) contains at most one
terminal. Consequently,

\[
\deg_G(z)\ge
\begin{cases}
q,&z\notin T,\\
q-1,&z\in T.
\end{cases}
\tag{SEPq.1}
\]

In particular, if every nonterminal has degree at most \(5\) and every terminal
has degree at most \(3\), an additive response is impossible for \(q\ge6\).

### Scope

This is a finite graph/network theorem. It applies to the actual C11
circular-planar contact network and preserves its source graph. It does not
construct or substitute a geometric star. The C-II corollary additionally uses a
relative-interior stress, \(C=C_*\), and the C26/C35 degree bounds.

### Proof

For \(q\ge3\), additivity and the effective-resistance triangle inequality imply
\(r_i\ge0\). Effective resistance between distinct terminals of a connected
positive network is strictly positive. Thus at most one \(r_i\) can vanish:
two zero parameters would give \(W_{ij}=r_i+r_j=0\). This avoids confusing
\(W\), which is conditionally negative definite, with its positive centered
form \(R=-JWJ/2\).

If all \(r_i>0\), set \(g_i=r_i^{-1}\) and
\(\Gamma=\sum_i g_i\). With \(J=I-\mathbf1\mathbf1^{\mathsf T}/q\), additivity
gives \(R=-\tfrac12 JWJ=J\operatorname{diag}(r)J\). Direct multiplication on
\(\mathbf1^\perp\) then shows that the response determined by \(W\) is the
star-equivalent response

\[
\Lambda_{ij}=-\frac{g_i g_j}{\Gamma}\quad(i\ne j).
\]

If one parameter, say \(r_z\), is zero, take the limit \(r_z\downarrow0\) in this
formula. For every pair of disjoint ordered terminal lists
\(P=(p_1,p_2)\) and \(Q=(q_1,q_2)\), all entries of the \(2\times2\) submatrix
\(\Lambda[P;Q]\) still have rank at most one: away from \(z\) they are
\(-g_i g_j/\Gamma\), and the limiting row or column involving \(z\) has the same
rank-one limit. Hence in either case

\[
\det\Lambda[P;Q]=0
\tag{SEPq.2}
\]

for every size-two circular pair.

For a positive circular-planar network, the circular-minor connection theorem
says that a size-two circular minor is strict exactly when the corresponding
two-connection exists: two vertex-disjoint paths join the two terminal pairs and
have no terminal in their interiors. Thus (SEPq.2) rules out every such
two-connection.

Call a path with two distinct endpoints in \(T\) and no internal vertex in \(T\) a
\(T\)-path. If two vertex-disjoint \(T\)-paths existed, their four boundary
endpoints would be paired noncrossingly: an alternating pairing would force the
two embedded arcs in the disk to intersect. They would therefore form a
size-two circular connection, which has just been ruled out. Thus the maximum
number \(\nu_T(G)\) of vertex-disjoint \(T\)-paths is one. It is at least one
because \(G\) is connected and \(q\ge2\).

Gallai's \(T\)-path min-max theorem gives

\[
\nu_T(G)=
\min_{X\subseteq V(G)}
\left(
|X|+\sum_{K\in\operatorname{Comp}(G-X)}
\left\lfloor\frac{|T\cap K|}{2}\right\rfloor
\right).
\tag{SEPq.3}
\]

The minimum is one. For \(X=\varnothing\), connectedness gives the value
\(\lfloor q/2\rfloor\ge2\), since \(q\ge4\). Therefore a minimizing set must have
\(|X|=1\), and the sum in (SEPq.3) must be zero. Writing \(X=\{z\}\), every
component of \(G-z\) contains at most one terminal.

If \(z\notin T\), the \(q\) terminals occupy \(q\) distinct components of \(G-z\).
Each component has a neighbor of \(z\), and neighbors belonging to distinct
components are distinct, so \(\deg_G(z)\ge q\). If \(z\in T\), the other \(q-1\)
terminals occupy distinct components, so \(\deg_G(z)\ge q-1\). This proves
(SEPq.1). \(\square\)

## 3. Exact Target C-II implication

In the fully force-visible branch \(C=C_*\), choose a relative-interior normalized
KKT stress. C26 and C35 give

\[
\deg_C(v)\le5\quad(v\notin B_+),
\qquad
\deg_C(b)\le3\quad(b\in B_+).
\tag{SEPq.4}
\]

C34 gives the same stress and boundary set the exact count

\[
2|B_+|\ge\lceil D\rceil+2.
\tag{SEPq.5}
\]

If \(D\ge9\), then \(\lceil D\rceil\ge9\), so (SEPq.5) implies
\(|B_+|\ge6\). Applying SEPq to an additive C11 response on \(B_+\) would
require either an unloaded contact vertex of degree at least six or a loaded
terminal of degree at least five. Both contradict (SEPq.4). Therefore

\[
\boxed{
D\ge9,\ C=C_*
\quad\Longrightarrow\quad
\text{the canonical C11 response is not additive.}
}
\tag{SEPq.6}
\]

Thus any larger-support equality analysis that produces the same additive
resistance normal form is already incompatible with C-II for all sufficiently
large minimizers. SEPq does not rule out a non-additive equality mode, nor does it
address arbitrary non-maximal stresses in C-I.

## 4. Dependencies and literature imports

- `docs/reports/target_c_six_matching_star_separator_2026-08-31.md`, Theorem
  SEP6: the six-terminal source-preserving separator argument.
- `docs/reports/target_c_six_matching_equality_star_2026-08-31.md`, Theorem EQ6:
  the additive resistance normal form in the K6 equality case.
- `docs/reports/target_c_force_visible_endpoint_count_2026-08-31.md`, C34:
  \(2|B_+|\ge\lceil D\rceil+2\).
- `docs/reports/target_c_loaded_boundary_attachment_2026-08-31.md`, C35, and
  the C26 result recorded in the Target C bridge frontier: the degree caps.
- The circular-minor connection statement is Lemma 3.4 in S. Forcey,
  [*Kalmanson-Kron reconstruction*](https://sforcey.github.io/sf34/kron.pdf).
- The \(T\)-path min-max formula (SEPq.3) is Theorem 2 in T. Kaiser,
  [*Disjoint T-paths in tough graphs*](https://iti.mff.cuni.cz/series/2005/270.pdf).
  Its stated formula applies to arbitrary finite graphs; no toughness assumption is
  used here.

## 5. Why it is new

SEP6 established the degree contradiction only for the six-terminal matching left
by K6. SEPq makes the separator theorem independent of the number of terminals and
combines it with the C34 linear endpoint count. The new C-II consequence is a
global exclusion of all additive/star-equivalent canonical responses once \(D\ge9\),
not merely the selected three-edge six-terminal equality.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Additive effective-resistance parameters are nonnegative | proved | They are obtained from the effective-resistance triangle inequality. |
| Additive response has rank-one off-diagonal cross-minors, including one zero parameter | proved | Direct star formula and its one-parameter limit. |
| No two disjoint terminal paths | proved with literature input | Circular-minor strictness and disk noncrossing. |
| One-vertex separator and degree lower bounds | proved with literature input | Gallai's exact formula and connectedness. |
| No additive canonical response for \(D\ge9\) in C-II | proved | SEPq, C34, C26, and C35. |
| Every larger-support equality mode is additive | not proved | This is precisely the remaining response-equality question. |
| C-I is closed | not proved | Maximal support and degree caps are not available for arbitrary selected stresses. |
| Target C is closed | not proved | Non-additive larger supports and the C-I/remaining C-II branches remain. |

## 7. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| \(q=3\) terminal triangle | yes | \(X=\varnothing\) has Gallai value one; \(q\ge4\) is essential. |
| Six-leaf star | yes | Its degree-six hub realizes the SEPq lower bound. |
| Five-terminal star with degree-five hub | yes | This explains why the degree-cap contradiction begins at \(q=6\). |
| Six-terminal path | yes | It has two disjoint \(T\)-paths and cannot have additive circular-planar response. |
| C33 abstract sign-cone matrix | yes | It is outside the circular-planar response cone. |

## 8. Failed routes and no-go results

### Promoting additive equality to a theorem for larger supports

SEPq only says that additive equality is impossible under C-II when there are at
least six force-visible terminals. It does not prove that a general response
equality must be additive. The remaining larger-support equality analysis must
retain non-additive circular-planar possibilities.

### Applying the degree contradiction to C-I

C26/C35 use the fully force-visible relative-interior contact graph. A non-maximal
selected stress in C-I may have a smaller positive support and does not inherit
the same degree caps. SEPq is therefore not a C-I separator theorem.

## 9. Exact remaining lemma

The shortest next statement is:

> **Non-additive equality exclusion.** In the fully force-visible branch with
> \(D\to\infty\), every equality case in the selected response inequality either
> has an additive resistance normal form (now excluded by SEPq) or yields an exact
> C41/C42/global-packing contradiction.

This is narrower than the original “larger support” target because the additive
branch has been removed.

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
For any connected circular-planar response on q >= 4 boundary terminals, additive
effective resistance forces a vertex whose deletion leaves at most one terminal per
component. Its degree is at least q if unloaded and q-1 if terminal.

Exact C-II effect:
C34 gives 2|B_+| >= ceil(D)+2. Hence D >= 9 implies |B_+| >= 6. C26/C35
then exclude every additive/star-equivalent canonical C11 response.

Binding limitation:
This removes the additive part of larger-support equality, not non-additive equality.
It is C-II-only and does not solve C-I or the remaining bridge/bulk branches.

Highest-value next lemma:
Exclude non-additive equality in larger supports by connecting the circular-planar
response defect to C41/C42 and global packing.
```
