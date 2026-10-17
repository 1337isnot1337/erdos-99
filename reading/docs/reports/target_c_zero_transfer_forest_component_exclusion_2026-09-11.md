> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_forest_component_exclusion_2026-09-11.md) · source SHA-256 `c1b0258cbf4da0883541632ddb8708dc2e1cd7cb29575967e55aa0fc58a6c223`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-05DFB9D5D3BE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — zero-transfer forest component exclusion

**Date:** 2026-09-11  
**Status:** report-level theorem; unpromoted  
**Target:** Target C, C-II  
**Dependencies:** C34 loaded-endpoint count, C53 interval-sign lemma, C56 zero-transfer localization, C58 zero-transfer star theorem, SEPq source-preserving separator, and the C-II degree caps

## Level-I status

`STILL OPEN`.

The exact zero-transfer **forest** branch can now be excluded for large diameter.
The key point is to apply the additive-response separator to three diameter edges
chosen from three distinct star components, rather than to the whole diameter
graph.

The resulting theorem is

$$
\boxed{
\text{C-II, }s_Z=0,\text{ C56-Z, and forest }H
\quad\Longrightarrow\quad d_H\le2, h\le8, q\le10.
}
\tag{ZF-M.1}
$$

Since promoted C34 gives `2q\ge\lceil D\rceil+2`, this rules out the complete
zero-transfer forest branch for `D>18`.  It leaves the cyclic `s_Z=0` branch,
nonzero-transfer forest branch, and all `s_Z>0` branches untouched.

The result is unpromoted because the three-component response restriction and
its use of C56/C58/SEPq still require an explicit audit and promotion.  No
ZR/ZF input is used in the finite or asymptotic contradiction.

## 1. Exact statement of the response lemma

Let `H` be a C56-Z positive diameter forest in a fully force-visible C-II
source.  C58 says every component of `H` is a star.  Suppose `H` has at least
three nontrivial components.  Choose one edge from each of three components,
call them `e_0,e_1,e_2`, and let `T` be the six endpoints.

The claim is that the effective-resistance matrix restricted to `T` is
additive:

$$
W_{xy}=r_x+r_y\qquad(x\ne y, x,y\in T).
\tag{ZF-M.2}
$$

SEPq then contradicts the C-II degree caps, because a separator for six
terminals needs degree at least six if it is not one of `T`, and at least five
if it is in `T`; all source vertices have contact degree at most five, while
the loaded vertices in `T` have contact degree at most three.

## 2. Three components give an additive six-terminal restriction

Orient the three selected diameter edges in the consistent C53 projective order.
They are vertex-disjoint and therefore pairwise crossing.  Write their edge
incidence columns as `q_0,q_1,q_2` and restrict the full C56 split vectors to
these three coordinates.

C56.7 says that every positive interval split vector in the full diameter-edge
space has support on one edge or on two adjacent projective directions.  Thus
its restriction to the selected three coordinates has support of size at most
two.

We show that a restricted two-coordinate support has equal signs.  Suppose a
positive split has restricted support on two selected edges `e_i,e_j`.  Its
full support has no other diameter edge, so C56 makes `e_i,e_j` adjacent in
the full projective order.  Let `e_k` be the third selected edge.  The three
selected chords are pairwise intersecting.  Apply the audited C53 interval-sign
lemma to them in their projective order.

If the adjacent supported pair is the first two, then the third coordinate is
zero and

$$
z_0(z_2-z_1)\le0
\quad\Longrightarrow\quad
z_0z_1\ge0.
$$

If it is the last two, the other C53 inequality gives the same conclusion.
The two supported coordinates are nonzero, so their signs agree.  Therefore a
positive split contributes a nonnegative amount to the corresponding off-
diagonal entry of

$$
K_T:=Q_T^{\mathsf T}RQ_T.
$$

But C56-Z gives `K=B_H^{-1}` on the full edge space, hence every off-diagonal
entry of `K_T` is zero.  Nonnegative split coefficients imply that no positive
split can have two selected coordinates in its support.

Consequently every restricted split has support at most one.  There is no
nonempty proper restricted interval with support zero: in the two-block word
`t_0,t_1,t_2,u_0,u_1,u_2`, an interval containing both endpoints of every
selected pair that it meets would have to pass through the endpoint of another
selected pair.  Equivalently, the two boundary transitions of a proper interval
separate at least one of the three crossing pairs.

The six selected endpoints occur in the two-block order

$$
t_0,t_1,t_2,u_0,u_1,u_2
$$

after cyclic relabeling, because the three selected chords pairwise cross.  A
cyclic interval whose indicator changes on exactly one of these three matching
pairs is, on the restricted terminal set, a singleton terminal cut or its
complement.  Therefore every restricted split metric is a singleton cut metric.
The sum-matrix ambiguity in the circular split representation is additive as
well.  Summing the restricted representation gives (ZF-M.2).

This argument is deliberately restricted to three selected disjoint edges.  It
does not assume that the entire positive diameter graph is a matching, and it
does not apply a response identity to an arbitrary edge-color class.

## 3. Degree contradiction

Apply SEPq to the actual positive contact graph and the six-terminal set `T`.
It supplies a source vertex `z` such that each component of the contact graph
with `z` deleted contains at most one terminal of `T`.  If `z\notin T`, then
`deg_C(z)\ge6`; if `z\in T`, then `deg_C(z)\ge5`.

All source points are unit-separated and triangle-free, so a source point has
contact degree at most five.  In the C-II fully force-visible normalization,
every loaded source vertex has the sharper contact degree cap three.  The six
terminals in `T` are loaded, so both cases are impossible:

* `z\notin T`: degree at least six contradicts the global degree-five bound;
* `z\in T`: degree at least five contradicts the loaded degree-three bound.

Hence a C56-Z forest in C-II has at most two nontrivial components:

$$
\boxed{d_H\le2.}
\tag{ZF-M.3}
$$

## 4. Star size and the finite diameter bound

For completeness, C58 plus the same separator argument also lowers the largest
possible C-II star.  A star with five edges has six terminals.  SEPq would again
require degree at least six at a nonterminal separator or at least five at a
terminal separator, both impossible in C-II.  Thus every zero-transfer star
has at most four edges.

With at most two nontrivial star components,

$$
h\le4d_H\le8.
\tag{ZF-M.4}
$$

In the forest branch, `q=h+d_H`, so

$$
q\le8+2=10.
\tag{ZF-M.5}
$$

The promoted C34 endpoint count is

$$
2q\ge\lceil D\rceil+2.
\tag{ZF-M.6}
$$

Together with (ZF-M.5), this gives `\lceil D\rceil+2\le20`, hence `D\le18`.
Therefore the exact zero-transfer forest branch is absent for every C-II
survivor with `D>18`, with no ZR/ZF dependency.

## 5. Regressions and hypotheses

* **Perfect matching:** has many components, so it is excluded already by the
  three-component restriction; the earlier exact-matching theorem is the
  special case where the full graph is a matching.
* **Two-edge and four-edge stars:** individually allowed by the degree caps, but
  at most two such components can coexist in C56-Z.  The ZF edge count then
  excludes their total diameter support for large `D`.
* **Six-terminal star:** excluded in C-II by the loaded/nonloaded degree caps;
  the bare triangle-free version would allow the terminal degree-five equality,
  so the C-II cap is used essentially.
* **Shared endpoints:** they are allowed within each selected star; the three
  selected edges are chosen from different components to ensure disjointness
  and pairwise crossing.
* **Contact isolates:** SEPq uses the actual positive contact graph and its six
  loaded terminals. Isolated source points are not deleted, declared loaded, or
  used as separator vertices.
* **Cyclic topology:** the argument assumes the Woodall forest branch. It does
  not apply to the connected odd-unicyclic `d_H=0` branch.
* **Positive transfer:** C56-Z is used at the exact equality `K=B_H^{-1}`;
  no identity is extended to generic transfer.
* **ZF provenance:** no ZR/ZF statement is used.  The final finite contradiction
  uses promoted C34, while the response reduction itself is kept report-level
  pending the C56/C58/SEPq audit.

## 6. Exact branch ledger after this theorem

The C-II ledger is now:

1. cyclic diameter topology with `s_Z=0`;
2. forest topology with `s_Z=0` but nonzero transfer (the C56-Z subbranch is
   excluded for `D>18` by this report);
3. `s_Z>0`, where no zero-transfer identity may be imported.

The forest closure is therefore a genuine reduction: it no longer contains an
unbounded exact-zero-transfer star forest.  The unresolved obstruction is the
generic-transfer caterpillar/hub response tradeoff and the positive-surplus
branch, in addition to the cyclic exceptional-face/full-source problem.
