> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_matching_split_separation_2026-09-11.md) · source SHA-256 `b20305b197a8319b6d3aafd4e0ef3288bba9dbe381054950f4d305fcdfe45a7b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A4A59386F3E7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact zero-transfer matching exclusion

**Date:** 2026-09-11  
**Status:** report-level theorem; unpromoted  
**Target:** Target C, C-II  
**Dependencies:** promoted C53/C50 circular-planar split representation, C56 zero-transfer localization, C58 source-preserving additive-response separator, triangle-free unit-contact degree bound

## Level-I status

`STILL OPEN`.

This report closes one exact residual subbranch that was not closed by the
anti-matching inequality.  A C56-zero-transfer stress whose positive diameter
graph is a pairwise-crossing matching cannot have four or more diameter edges.
The proof is an equality argument in the circular split cone, followed by the
source-preserving separator theorem.  It does **not** exclude zero-transfer
forests containing two-edge or larger star components, nor does it address
generic transfer or `s_Z>0`.

The conclusion is

```math
\boxed{\text{C56-Z + matching + triangle-free source}\quad\Longrightarrow\quad |H|\le3.}
```

For the fully force-visible C-II representative, the loaded degree cap improves
this to `|H|<=2`.

Thus the matching branch is not merely quantitatively non-optimal: its exact
zero-transfer limit is incompatible with the bounded-degree source geometry at
linear diameter scale.

## 1. Setup

Let `H` be the positive diameter graph of a two-dimensional C56-Z stress.  Write
its matching edges as

```math
e_i=t_i u_i,\qquad 0\le i<h.
```

Because the diameter drawing is a convex geometric thrackle, pairwise-disjoint
edges cross.  After choosing a cyclic cut and reversing individual orientations
if necessary, the boundary order is

```math
t_0,t_1,\ldots,t_{h-1},u_0,u_1,\ldots,u_{h-1},
\tag{M.1}
```

and the directed diameter chords are in the same strict projective order as
the indices `0,...,h-1`.  The latter order is invariant under a strict convex
deformation: two pairwise-crossing chords cannot become parallel, and it can be
checked on the regular `2h`-gon.

Put `Q=(e_{t_i}-e_{u_i})_i`, `R=\Lambda^+`, and

```math
K=Q^{\mathsf T}RQ.
```

C56-Z gives

```math
K=B_H^{-1},
\qquad K_{ij}=0\quad(i\ne j).
\tag{M.2}
```

The C50 circular-planar resistance theorem gives a nonnegative interval-split
representation of the effective-resistance metric.  For an interval `A` on
the terminal circle write

```math
z_i(A)=\mathbf 1_A(t_i)-\mathbf 1_A(u_i).
\tag{M.3}
```

Modulo a sum matrix (which contributes only an additive terminal metric), its
contribution to `K` is `z(A)z(A)^{\mathsf T}`.  C56.7 says that every positive
split occurring in the zero-transfer representation has

```math
\operatorname{supp}z(A)\subseteq\{i\}
\quad\text{or}\quad
\operatorname{supp}z(A)\subseteq\{i,i+1\}.
\tag{M.4}
```

The indices in the second alternative are ordinary adjacent indices in the
linear projective order, not the two ends of the order.

## 2. The interval-sign lemma

### Lemma M.1

Assume (M.1).  If a proper cyclic interval `A` satisfies

```math
\operatorname{supp}z(A)\subseteq\{i,i+1\}
```

for an ordinary adjacent pair `0\le i<h-1`, and both coordinates are nonzero,
then

```math
z_i(A)=z_{i+1}(A).
\tag{M.5}
```

If the support has one coordinate, `A` or its complement is a singleton
terminal interval.

#### Proof

Traverse the cyclic word (M.1).  An interval has exactly two boundary
transitions in this word.  A matching pair contributes a nonzero coordinate of
`z` precisely when exactly one of its two letters lies between the two
transitions.

For the support to be contained in `{i,i+1}`, every pair with index outside
`{i,i+1}` must have both letters on the same side of both transitions.  In the
word (M.1), the only way to separate precisely the two consecutive pairs is to
take, up to complement, one of the four two-letter intervals

```math
\{t_i,t_{i+1}\},\quad
\{u_i,u_{i+1}\},
```

with the same conclusion after a cyclic relabeling at the ends of a block.
For the first interval both coordinates are `-1`; for the second both are
`+1`.  Thus (M.5) holds.

If only coordinate `i` is nonzero, the same transition argument says that all
other pairs are wholly on one side.  A proper cyclic interval with that
property can contain only one of `t_i,u_i`, and no other terminal; otherwise
the first and last included letters would separate another matching pair.
Hence `A` or its complement is the singleton containing `t_i` or `u_i`.
$`\square`$

The statement can also be checked directly by writing the four indicator
sequences in the two blocks of (M.1); no metric or generic-position assumption
is used.

## 3. Diagonal zero transfer removes every two-coordinate split

Let the nonnegative coefficient of an interval split `A` be `\lambda_A`.
For an ordinary adjacent pair `i,i+1`, Lemma M.1 gives

```math
z_i(A)z_{i+1}(A)=1
```

whenever the split has both coordinates in its support.  Every other split
has zero product on that pair.  Therefore the split representation gives

```math
K_{i,i+1}
 =\sum_A\lambda_A z_i(A)z_{i+1}(A)
 =\sum_{A:\,\operatorname{supp}z(A)\supseteq\{i,i+1\}}\lambda_A
 \ge0.
\tag{M.6}
```

But C56-Z gives `K_{i,i+1}=0`.  Hence every coefficient in (M.6) vanishes:
no positive split has two-coordinate support.  Combining this with Lemma M.1,
every positive split is a singleton terminal cut (or its complement).

The possible sum-matrix term is itself additive and can be absorbed into the
same terminal weights.  Consequently the full effective-resistance metric on
the `2h` diameter terminals has the additive form

```math
\boxed{
W_{xy}=r_x+r_y\qquad(x\ne y),
}
\tag{M.7}
```

with nonnegative `r_x`.  Indeed, a singleton cut at `x` contributes `1` exactly
to pairs having exactly one endpoint `x`, and the sum of such cut metrics is
`r_x+r_y`.

This is the point where the exact diagonal identity is essential.  The general
near-matching inequality only controls the total off-diagonal defect and cannot
delete the two-coordinate split mass.

## 4. Source-preserving separator contradiction

The C58 additive-response separator theorem applies to a circular-planar
positive contact network whose terminal resistance metric has the form (M.7).
For `2h\ge4`, it supplies a source vertex `z` such that every component of
the positive contact graph with `z` deleted contains at most one of the `2h`
diameter terminals.  Therefore

```math
\deg_C(z)\ge 2h-1
\quad\text{if }z\text{ is a terminal},
\qquad
\deg_C(z)\ge 2h
\quad\text{otherwise}.
\tag{M.8}
```

The source is triangle-free.  Six unit neighbors of any source point would
have six angular gaps at least `\pi/3`, hence all gaps exactly `\pi/3`; two
consecutive neighbors would then form a unit equilateral triangle with the
center.  Thus every source contact degree is at most five.  From (M.8),

```math
2h-1\le5,
```

so `h\le3`.

This proves the triangle-free-source version.  In the C-II representative one
also has `\deg_C(b)<=3` at a loaded terminal and `\deg_C(v)<=5` at a nonterminal.
If `h>=3`, then `2h>=6`; (M.8) requires degree at least six at a nonterminal
or at least five at a terminal.  Both violate these C-II caps.  Therefore

```math
\boxed{\text{fully force-visible C-II + C56-Z + matching}\quad\Longrightarrow\quad |H|\le2.}
\tag{M.9}
```

This proves the strengthened C-II theorem.

## 4A. A second C-II consequence: the star degree drops from five to four

Apply the same separator theorem to one C58 star component with `k` leaves,
so it has `q=k+1` diameter terminals.  If `k=5`, then `q=6`.  A separator
terminal would need contact degree at least `q-1=5`, contradicting the loaded
degree cap `3`; a nonterminal separator would need degree at least `q=6`,
contradicting the triangle-free source degree cap `5`.  Therefore every
zero-transfer C-II star has

```math
\boxed{k\le4.}
\tag{M.10}
```

For a zero-transfer forest, Woodall's forest branch has exactly `d_H` star
components.  Hence

```math
h\le4d_H,
\qquad
d_H\ge h/4.
\tag{M.11}
```

The post-ZF edge/diameter comparison `h\ge\lceil D\rceil` then gives

```math
\boxed{d_H\ge D/4+O(1).}
\tag{M.12}
```

In the audited zero-transfer forest circuit subbranch, where

```math
\nu_D=\frac{e_{BB}+2s_C-3d_H}{D}
\ge0.597+\varepsilon_{597},
```

this improves the retained surplus currency to

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge0.597+\varepsilon_{597}+\frac34-o(1).
}
\tag{M.13}
```

This is still not a contradiction: no opposing upper bound on
`(e_{BB}+2s_C)/D` is available in the forest branch.  The improvement is a
valid C-II branch charge, not a closure.

## 5. What this closes and what it does not

The theorem removes the exact C56-Z matching branch with `h\ge3` in C-II,
including the perfect-matching regression and every unbounded matching support.
The bare triangle-free version is compatible with `h=2,3`; the fully visible
C-II version is compatible only with `h=1,2`.  The six-terminal star separator
equality recorded in C58 is not a matching and is unaffected.

It does not apply to:

* a zero-transfer forest with two-edge or larger star components;
* a generic C56 phase before the exact zero-transfer equality;
* a positive mixed surplus `s_Z>0`;
* a stress whose positive diameter support is not a matching.

In the remaining zero-transfer forest branch, C58 still gives stars of degree
at most five.  The new result says that the residual many-component matching
escape cannot be the whole support; the unresolved possibility is a linear
number of bounded stars with at least one shared-endpoint pair.

## 6. Regression audit

* **Six-terminal star:** not a matching; C58 permits degree five and this report
  does not touch it.
* **Regular odd shell:** not C56-Z and not a global-optimality certificate; it
  remains outside the theorem.
* **Isolated source points:** C58 is applied to the actual positive contact
  graph and its loaded terminals; no isolate is deleted or called diametral.
* **Repeated outer walks and exceptional faces:** absent from the response
  equality argument; no outer-face simplification is assumed.
* **Shared diameter endpoints:** excluded by the matching hypothesis, not
  silently folded into it.
* **Common contact block:** the separator theorem is source-preserving; it does
  not replace a multi-edge cut by a bridge transfer.

## 7. Exact remaining C-II obstruction after this theorem

The branch ledger is sharpened as follows:

1. cyclic `s_Z=0`: the cyclic high-surplus/exceptional-face problem remains;
2. forest `s_Z=0`, exact zero transfer: all components are stars of degree at
   at most four in C-II, and if the diameter support is a matching with
   `h\ge3` it is now impossible in C-II; hence a surviving unbounded forest
   has a linear number of shared-endpoint diameter incidences;
3. forest `s_Z=0`, nonzero transfer: the caterpillar/hub response tradeoff
   remains;
4. `s_Z>0`: no zero-transfer identity may be imported.

No global Level-I conclusion follows yet.
