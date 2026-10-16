<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "4b3d2c92f48fcf27d2c6ae0cd7ddfe8b83478f32", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_two_flex_charge_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "10da021da3187ed31e3a31024d0d309029c46596a37ed859cbdb45be1edc5ca7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — collapsed support-six blocks carry two internal contact flexes

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion audit; theorem-state authority unchanged  
**Scope:** degree-pure collapsed support-six blocks in the canonical stopped-train
angle system, at the infinitesimal contact-flex level  
**Certificate:** `research/verify_target_c_support6_collapsed_two_flex_charge_2026_09_18.py`  
**Classification:** proved candidate awaiting audit; C-II remains open

The collapsed support-six branch carries more contact flexibility than the previously
recorded one-dimensional host-anchor charge suggests. For every actual degree-pure
collapsed block, the twelve internal relation trains form a (12\times12) face-closure
submatrix. Its two coordinate row sums vanish because every internal train occurs at
two endpoint faces with opposite oriented side vectors. Consequently its kernel has
dimension at least two. These are genuine non-Euclidean infinitesimal contact flexes
with all six outside-host train rates fixed.

If `c` pairwise disjoint collapsed blocks occur, the new directions are independent
across blocks and independent of the peeled pair-shield directions and of the common
angle directions used in the existing dual-component flex theorem. Write `nu_D` for
the dimension of the non-Euclidean infinitesimal contact-flex space. On the already
regular exact products, `nu_D` agrees with the finite-flex dimension `m_D` used by the
existing notes. The first-order KKT locking argument requires only `nu_D`, not
nonlinear integration of the newly added directions. Thus the tangent transfer is


\[
\boxed{
 \nu_D\ge {b-f\over2}
 +{1\over4}\bigl(\sigma_C-(Q-f)\bigr)_+-1+2c.
}
\tag{TF.1}
\]

In the live terminal window this gives

\[
\boxed{
 {\nu_D\over D}>1.1988388040
 +{1\over4}{\sigma_C\over D}+2{c\over D}-o(1).
}
\tag{TF.2}
\]

The result is an infinitesimal contact-flex statement; it does not claim that the
two-dimensional local nonlinear family certified elsewhere globally embeds. It uses
only the actual global stopped-train system of a putative source, so it is not defeated
by the local-realization regression.

## 1. The internal block matrix

Let `B` be one degree-pure collapsed support-six block. Its six bounded faces have the
relation graph (R_B=K_6\setminus M), so there are twelve internal complete trains.
Each has both terminal nonquadrilateral occurrences in `B`; the remaining one train
incident with each face is an outside host train. Let `u_ij` be the oriented unit side
vector of the internal train joining faces `i` and `j`. The restriction of the
linearized face-closure map to the twelve internal train-angle rates has one column
of the form

\[
  \begin{array}{c|cc}
  &i&j\\ \hline
  C_B(ij)&J u_{ij}&-J u_{ij}
  \end{array}
\]

and zero entries in the other face rows. This is an exact occurrence-counted formula;
rhombus closure has already been eliminated by complete-train coordinates.

Summing the first-coordinate row of all six face closures annihilates every internal
column, because its two endpoint occurrences have opposite vectors. The same holds
for the second-coordinate rows. Therefore

\[
 \operatorname{rank} C_B\le 10,
 \qquad
 \dim\ker C_B\ge2.
\tag{TF.3}
\]

No local numerical root, regularity assumption, sign/order classification, or metric
realization is used in (TF.3). It holds for every actual collapsed block in the
global stopped-train system.

## 2. Extension to global contact flexes

Take a vector in `ker C_B`, assign its rate to every edge of the corresponding
complete internal train, and assign rate zero to every other train. Every strict
rhombus closure remains satisfied by opposite-side cancellation. The only bounded
nonquadrilateral faces touched by these trains are the six faces of `B`, and their
linearized closures vanish by definition. Hence the resulting train-angle vector lies
in `ker C_face`, and the audited face-cycle integration theorem gives an infinitesimal
contact flex of the whole positive-contact core.

Neither of these directions is Euclidean rotation: all six outside host trains have
rate zero, whereas a nonzero global rotation has rate one on every train. The two
directions are also independent across blocks.

The existing pair-shield/peeled coordinates freeze every residual-internal train. The
new block directions therefore have zero intersection with that previously counted
subspace. They also have zero intersection with a common-angle rotation of any
nonzero one-anchor relation component: each such component rotation changes an outside
host train, and distinct components have distinct host-train columns. Thus the new
two-dimensional subspaces can be added before the single conservative global-rotation
loss in the existing count.

This gives, with `g` the number of sealed nonzero one-anchor relation components and
`c` the number of collapsed blocks,

\[
 \nu_D\ge {b-f\over2}+a_F+{x_A\over2}+{n_0+n_2\over2}+p_U
 +(g-1)_+ +2c.
\tag{TF.4}
\]

## 3. Elimination and live propagation

The existing degree-excess argument gives

\[
g\ge\bigl(\sigma_C-2n_0-n_2-x_U\bigr)_+,
\qquad x_U\le Q-f.
\]

The same elementary optimization used in the existing dual-component flex note gives

\[
 {n_0+n_2\over2}
 +\bigl(\sigma_C-x_U-2n_0-n_2\bigr)_+
 \ge {1\over4}(\sigma_C-x_U)_+.
\]

Dropping nonnegative terms and using the conservative global-rotation loss yields

\[
 \nu_D\ge {b-f\over2}
 +{1\over4}\bigl(\sigma_C-(Q-f)\bigr)_+-1+2c,
\]

which is (TF.1).

In the current terminal window, the audited correlated pair-shield ledger supplies

\[
 {b-f\over2D}
 \ge 1.1988388040+{Q-f\over2D}-o(1).
\]

The pointwise inequality

\[
 {r\over2}+{1\over4}(s-r)_+\ge {s\over4}
\]

with (r=(Q-f)/D), (s=\sigma_C/D), gives (TF.2).

## 4. Consequence and exact scope

At the pair-shield endpoint, a linear collapsed-block population is therefore even
more expensive in the positively locked diameter system than the previous one-charge
statement recorded. In particular, any terminal sequence with

\[
 \nu_D/D\le1.1988388040+\eta+o(1)
\]

obeys

\[
 {\sigma_C\over D}+8{c\over D}\le4\eta+o(1).
\]

This is a genuine shrinkage of the low-flex C-II frontier. It does not by itself
exclude collapsed blocks, because the remaining full-core obstruction may have
`m_D/D` above the pair-shield endpoint. It also does not promote the local
two-parameter certificate to a global source realization.

**Dependency chain:**

\[
\text{actual collapsed block}
\to \operatorname{rank}C_B\le10
\to 2\text{ internal contact-flexes/block}
\to \text{positive diameter locking}
\to \text{(TF.1)--(TF.2)}.
\]

**Disposition:** new proved candidate at the infinitesimal stopped-train scope; no
theorem-state change; C-II remains open.
