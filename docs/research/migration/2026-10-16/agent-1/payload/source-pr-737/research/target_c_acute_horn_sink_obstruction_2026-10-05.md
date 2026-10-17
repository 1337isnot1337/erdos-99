# Target C-II — acute lower clauses force sink-obstruction witness multiplicity

**Date:** 2026-10-05
**Base main:** \`0351c2c3aecd34c0427d0ad081afae563468d401\` (\`2026-10-05.audit.61\`)
**Status:** proof-only Target C reduction; theorem-state unchanged. C-II and Level I remain open.

This attacks the audit.61 full-core finite-motion obstruction after upper exceptions
and explicit unary-rhombus tests are separated. Concurrent PR #722 already records
the generic zero-state Horn/SCC reduction; it is not a premise here. The new step
is geometric: acute owner translations make reduced Horn clauses physically
irreducible, forcing a distinct-source-pair cost for every obstructed sink SCC.

## 1. Exact acute truth-table identity

Let $p\in L_i$, $q\in L_j$, $i\ne j$, $r=q-p$, and let the owner
translations be $\Delta_i,\Delta_j$. For $a,b\in\{0,1\}$, put

$$
\Phi_{ab}=|r+b\Delta_j-a\Delta_i|^2-1.
$$

The old pair is a noncontact, so $\Phi_{00}>0$. Direct expansion gives

$$
\boxed{\Phi_{11}-\Phi_{10}-\Phi_{01}+\Phi_{00}
=-2\Delta_i\cdot\Delta_j.}
\tag{1}
$$

Assume the audit.61 acute-owner condition
$\Delta_i\cdot\Delta_j>0$. If both singleton states violate the strict
lower bound, $\Phi_{10}\le0$ and $\Phi_{01}\le0$, then

$$
\boxed{\Phi_{11}\le-\Phi_{00}-2\Delta_i\cdot\Delta_j<0.}
\tag{2}
$$

Thus one source pair can never have bad-state set exactly $\{10,01\}$.
Moreover

$$
1-|r+\Delta_j-\Delta_i|^2
\ge (|r|^2-1)+2\Delta_i\cdot\Delta_j>0.
\tag{3}
$$

## 2. One physical lower pair has one reduced binary role

Since state $00$ is good, the possible nonempty bad sets are only

$$
\{10\},\{01\},\{11\},\{10,11\},\{01,11\},\{10,01,11\}.
$$

Exact 2-SAT compilation simplifies these to, respectively,

$$
i\to j,\quad j\to i,\quad \neg(x_i\wedge x_j),\quad
\neg x_i,\quad \neg x_j,\quad \neg x_i\wedge\neg x_j.
\tag{4}
$$

For example

$$
(\neg x_i\vee x_j)\wedge(\neg x_i\vee\neg x_j)\iff\neg x_i.
$$

Hence, after simplification, one acute two-owner lower pair contributes at
most one directed implication or one incompatibility edge; otherwise it
contributes unary forced-zero information. One physical pair cannot supply
both implication directions, or both an implication and an incompatibility.

## 3. Sink-obstruction cost

Let $Q$ be the reduced implication digraph, $Z$ the forced-zero owners,
and $K$ the reduced incompatibility graph. Contract SCCs of $Q$.

If $S$ is a sink SCC, setting exactly the variables of $S$ to one satisfies
every implication. Therefore it is a lower-formula model unless either
$S\cap Z\ne\varnothing$ or $K$ has an edge with both endpoints in $S$.
Thus if zero is the only lower-formula model, every sink SCC contains an
internal obstruction.

Let $m=|S|\ge2$. A strongly connected simple digraph on $m$ vertices has
at least $m$ distinct directed arcs. Choose one physical lower-pair witness
for each such implication arc and one additional physical witness for the
internal obstruction. By (4), the additional witness cannot coincide with any
chosen implication witness. Therefore every obstructed sink SCC of size
$m\ge2$ requires at least

$$
\boxed{m+1}
\tag{5}
$$

distinct physical lower-pair witnesses.

If unary lower blockers have already been eliminated, the internal obstruction
must be an incompatibility. The smallest binary-only sink obstruction has two
owners and needs at least three different old noncontacts:

$$
\boxed{A\to B,\qquad B\to A,\qquad A\not\sim B.}
\tag{6}
$$

For disjoint sink SCCs $S_1,\ldots,S_t$ with no unary lower blockers, the
internal witnesses are distinct across sinks, so

$$
\boxed{N_{\rm sink}\ge\sum_a(|S_a|+1)=M_{\rm sink}+t.}
\tag{7}
$$

## 4. Audit.61 consequence

After audit.61 inactive-upper exceptions are handled, active-diameter
requirements for the chosen packet are handled, and unary rhombus tests are
safe, canonical \`C-OO-LOWER-BLOCKER-LOCALIZATION\` puts every remaining
intergroup lower clause on an actual outer-face near-unit source pair.

For an acute owner subfamily, a zero-only lower system therefore forces every
sink implication SCC to contain an internal obstruction. If no unary lower
blockers remain, each sink SCC $S$ spends at least $|S|+1$ distinct
outer-face near-unit source pairs.

The remaining geometric target is narrower than "exclude owner cycles": pay or
exclude these obstructed sink SCC packets using outer-face occurrence order,
loaded-hull geometry, loaded-return paths, or active-diameter coordinates. In
the minimal two-owner case the target is the three-distinct-pair pattern (6).

No such outer-face payment is proved here. Different clauses may use different
source vertices of the same owner, so source-level planarity alone does not
collapse (5). The macroscopic-container branch remains separate.

Everything above is an analytic finite proof. No computation, verifier,
numerical evidence, CI result, or unexecuted verifier is a proof premise.
