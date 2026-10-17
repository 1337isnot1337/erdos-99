> Generated reading edition · [exact source](../../../../docs/targets/target-a/09-activation-orthant.md) · source SHA-256 `5f60284a8f4d13bda37ce928dd4ce377a3137fb0d1846429effbb7ce1020983c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — exact activation-deactivation orthant

This audited addendum strengthens the monotone-activation theorem of Sections
142–145 and the KKT-stress no-go of Section 153. The entire set of active pairs
created by a monotone activation sequence is not merely zero-stressed: it is an
exactly and independently releasable forest. The terminal representative lies at
the corner of an affine orthant consisting entirely of triangle-free global
minimizers.

The result rules out an activation-only critical-cone locking argument. It does not
transport any direction into the independently constructed Schur response.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 156. Exact affine deactivation orthant

Take a monotone activation sequence from Theorem 142.1 and rename its terminal
index to avoid conflict with the canonical surplus
$s=\Delta_\Lambda-d_{\rm int}$:

$$
A_0,A_1,\ldots,A_\ell.
\tag{156.1}
$$

All configurations have the same labels, cardinality, and globally minimum
diameter $D$. At step $i$, a currently strict rattler $r_i$ moves, all
other points remain fixed, every old active pair persists, and exactly one new
active pair

$$
e_i=r_iq_i
\tag{156.2}
$$

is created. Put

$$
E_0=C_0\cup H_0,
\qquad
F=\{e_0,\ldots,e_{\ell-1}\},
\tag{156.3}
$$

where $C_0$ and $H_0$ are the initial unit-contact and diameter-pair sets.
Here $D>1$: if $D=1$, every pair in a unit-separated set is at distance one,
so any three points form a unit equilateral triangle. Since the Target A source is
triangle-free and has $N\ge3$, this is impossible. Thus a pair cannot be both a
unit contact and a diameter pair.

## 156.1 The full created-pair graph is a singly anchored forest

> **Lemma 156.1 (full activation forest).** The graph $F$ of **all** active
> pairs created in (156.1), including both unit and diameter activations, is a
> forest. Every component of $F$ contains at most one vertex incident to an
> initial active pair in $E_0$. Moreover, the terminal active-pair set is the
> disjoint union
> 

$$

> \boxed{C_\ell\cup H_\ell=E_0\,\dot\cup\,F.}
> \tag{156.4}
> 
$$



### Proof

Immediately before step $i$, the moved point $r_i$ is strict. It is therefore
incident to no pair in

$$
E_0\cup\{e_0,\ldots,e_{i-1}\}.
\tag{156.5}
$$

Thus $e_i=r_iq_i$ adds an edge with an isolated endpoint. Such an addition
cannot create a cycle, proving that $F$ is a forest.

The same induction proves the root assertion. The new endpoint $r_i$ is not
incident to $E_0$. If $q_i$ already lies in a component of $F$, the new
edge merely adds the leaf $r_i$ to that component. If $q_i$ does not yet lie
in $F$, the new two-vertex component contains an initial-active vertex only if
$q_i$ is one, and then it contains exactly that one. No step merges two existing
components.

Finally, Theorem 142.1 preserves every old active pair and creates exactly the one
new pair $e_i$ at step $i$. Iteration gives (156.4). $\square$

The forest in Lemma 156.1 is generally larger than the recorded unit-activation
subforest of Section 144. It includes every activation step and retains the exact
unit/diameter type of each created pair.

## 156.2 Independent exact release of every created pair

Write the terminal coordinates as $p_v$. In each component of $F$, choose as
root its unique vertex incident to $E_0$, if such a vertex exists; otherwise
choose any vertex. Orient every edge away from the root. For an oriented edge
$e=uv$, with parent $u$ and child $v$, put

$$
d_e=p_v-p_u,
\qquad
\sigma_e=
\begin{cases}
+1,&e\in C_\ell,\\
-1,&e\in H_\ell.
\end{cases}
\tag{156.6}
$$

> **Theorem 156.2 (exact activation-deactivation orthant).** There is
> $\varepsilon>0$ and an affine embedding
> 

$$

> \Psi:[0,\varepsilon)^{F}\longrightarrow (\mathbb R^2)^N
> \tag{156.7}
> 
$$


> with $\Psi(0)=A_\ell$ such that every $\Psi(\theta)$ is a triangle-free
> global minimizer of diameter $D$, every initial active pair remains active,
> and, for each $e\in F$,
> 

$$

> \boxed{
> |e|_{\Psi(\theta)}=
> \begin{cases}
> 1+\theta_e,&e\text{ is a created unit contact},\\
> D(1-\theta_e),&e\text{ is a created diameter pair}.
> \end{cases}}
> \tag{156.8}
> 
$$


> Consequently, any prescribed subset of the created active pairs can be made
> strict while all remaining created pairs and all initial active pairs stay
> exact.

### Proof

For a parameter vector $\theta=(\theta_e)_{e\in F}$, fix every chosen root and
every vertex outside $F$. If $v$ lies in a rooted component of $F$, define
its displacement by

$$
w_v(\theta)=
\sum_{e\in P(v)}\sigma_e\theta_e d_e,
\tag{156.9}
$$

where $P(v)$ is the oriented root-to-$v$ path. Set

$$
p_v(\theta)=p_v+w_v(\theta).
\tag{156.10}
$$

For an oriented edge $e=uv$, the two root paths differ only by $e$, so

$$
p_v(\theta)-p_u(\theta)
=d_e+\sigma_e\theta_e d_e
=(1+\sigma_e\theta_e)d_e.
\tag{156.11}
$$

If $e$ is a unit contact then $|d_e|=1$, while if it is a diameter pair then
$|d_e|=D$. Equation (156.11) proves the exact length formulas (156.8).

Every vertex incident to $E_0$ is fixed: if it belongs to $F$, Lemma 156.1
makes it the chosen root of its component, and otherwise it was fixed by
definition. Hence all pairs in $E_0$ retain their exact terminal lengths.

Every other pair is inactive in $A_\ell$, and there are only finitely many such
pairs. Their distances lie strictly between $1$ and $D$. By continuity, there
is a uniform $\varepsilon>0$ such that all of those strict inequalities persist
throughout $[0,\varepsilon)^F$. Shrink $\varepsilon$, if necessary, so that

$$
\varepsilon<\min\left\{D-1,\,1-\frac1D,\,1\right\}.
\tag{156.12}
$$

Then every released unit edge stays below $D$, and every released diameter
edge stays above $1$. Thus every $\Psi(\theta)$ is unit-separated and has
diameter at most $D$.

At least one diameter pair belongs to $H_0$, because $A_0$ has diameter
$D$. Its two endpoints are fixed, so every $\Psi(\theta)$ still has diameter
exactly $D$. Since $D=D(N)$, every member of the family is a global
minimizer.

No terminally inactive pair becomes a unit contact, and the unit contacts retained
from $A_\ell$ form a subset of its contact graph. Because $A_\ell$ is
triangle-free, every $\Psi(\theta)$ is triangle-free as well.

Finally, the labeled length of each created edge recovers its own coordinate
$\theta_e$ from (156.8). Hence $\Psi$ is injective and is an affine embedding.
Choosing $\theta_e>0$ exactly on any desired subset gives the last assertion.
$\square$

## 156.3 Simultaneous recovery of the initial strict-rattler stratum

Let $V_0$ be the set of vertices incident to $E_0$. The strict rattlers of
$A_0$ are exactly $V\setminus V_0$. If every coordinate $\theta_e$ is
positive, (156.8) makes every pair in $F$ strict, while the only remaining
active pairs are those in $E_0$. Therefore:

> **Corollary 156.3 (simultaneous deactivation).** The relative interior of the
> orthant (156.7) consists of triangle-free global minimizers whose strict-rattler
> set is exactly the strict-rattler set of $A_0$. In particular, all activation
> constraints can be released simultaneously; no sequential compatibility loss is
> present.

The coordinate axes give more: one created pair can be released while every other
created pair stays exact. Thus the terminal feasible/global-optimum tangent cone
contains the full signed coordinate orthant prescribed by the activation forest.
Section 153's universal zero-multiplier theorem is consistent with, and is now
accompanied by, this exact finite-amplitude geometry.

## 156.4 Exact no-go and remaining Target A endpoint

The theorem removes one proposed repair left open after Section 153. The independent
activation rows do not form an unweighted locking system at the terminal
representative. They are the coordinate facets of a realizable affine orthant of
global optima. Consequently, the specific repair that treats the independent
activation rows as an unweighted terminal cage is unavailable:

$$
\boxed{
\text{the activation forest is not a terminal locking system:}
\quad
\text{its full signed release orthant is feasible}.}
\tag{156.13}
$$

This statement is deliberately scoped:

1. $\varepsilon$ need not have a uniform lower bound; long-chain and small-slack
   regressions remain active.
2. The orthant supplies no extra same-hull point and no strict smaller-diameter
   competitor.
3. It does not identify the genuine source with the independently constructed
   smaller optimum or scaffold.
4. It does not apply to a locked first-triangle transition that creates several
   simultaneous constraints; Theorem 142.1 creates exactly one pair at each step.
5. It does not rule out a theorem using finite collision walls beyond the local
   orthant, the global relation between different optimum cardinalities, or an exact
   source-to-scaffold transport invariant.

Accordingly, the authoritative endpoint remains

$$
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
}
\tag{156.14}
$$

equivalently

$$
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{156.15}
$$

In the very-super-boundary subbranch of Section 155, the shortest remaining bridge
is the two-shadow compatibility lemma. In the general branch, any surviving
activation route must use information not present in the local activation orthant.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
