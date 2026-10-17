> Generated reading edition · [exact source](../../../docs/reports/target_c_global_phase_access_integrable_branch_exclusion_2026-10-05.md) · source SHA-256 `48b9c5883ff1c697bc855b816fdb23123fcd8d2f05bb7f16b0a2adef92e0b06d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-398B64032790","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — global phase access closes the integrable-degree, small-residual branch

**Date:** 2026-10-05
**Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f
**Preceding checkpoint:** 3aa04059ec728f07f36e34ceea1a09ba59fa59ba
**State:** 2026-09-14.audit.51
**Classification:** conditional branch-elimination proof candidate awaiting
independent audit. Artifact unreviewed; no canonical promotion.
**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Exact statement and changed frontier

**Theorem GA.1.** There is no sequence of canonical triangle-free full-core
Type-II sources, with $`D_j\to\infty`$, satisfying all three conditions

```math
R_F/D\to0,
\tag{H1}
```

```math
\lim_{M\to\infty}\limsup_{D\to\infty}
 D^{-1}\sum_{F:\deg F>M}\deg F=0,
\tag{H2}
```

and

```math
\lim_{M\to\infty}\limsup_{D\to\infty}
 D^{-1}\sum_{P:\ell_P>M}\ell_P=0.
\tag{H3}
```

Here $`F`$ ranges over the physical bounded nonquadrilateral contact faces;
$`P`$ ranges over the hull-augmented outer pockets; $`\ell_P`$ is its actual
unit-contact path length. $`R_F`$ is the exact fixed-boundary residual,
including every assigned isolated source point.

In particular the full-core branch with small residual and uniformly
bounded exceptional-face and pocket degrees is excluded. Uniform bounds
are sufficient, not necessary: the theorem uses the two normalized tails.

The source-level mechanism is

1. mixed rigidity makes the internal train columns independent;
2. their incidence structure gives an outward cut of at least $`Q_S+4`$
   for every nonempty exceptional-face family $`S`$;
3. this bounds average face-graph distance to the outer walk;
4. small residual makes each bounded-degree face preserve reduced phase;
5. integrable degree tails control every fixed-radius bad neighborhood;
6. hull phase dispersion therefore reaches almost every actual train;
7. all trains would carry $`o(D^2)`$ rhombi, contrary to Type II.

This supplies the missing global ingredient in the bounded-degree Groemer
branch. No hidden near-contact is declared active, and no numerical
triangle or local deformation is substituted for global optimality.

## 2. Canonical source and dependencies

Use the contact-minimal, then diameter-pair-minimal canonical source.
Every source point, including all isolates, is retained. The matrices
below are only on the nonisolated positive-contact core.

Canonical inputs are [Section 57 mixed rigidity](../targets/target-c/57-zr-zf-rigidity-audit.md),
[Section 67 convex chamber decomposition](../targets/target-c/67-rhombus-population-transport-audit.md),
[Section 69 phase bins](../targets/target-c/69-coherent-grain-interface-audit.md),
and Type-II full-core disk/rhombus saturation. In particular

```math
R_4/D^2\to\Delta_2=\pi/(2\sqrt3)>0,\quad
Q\le P_F=(\pi+o(1))D,\quad f\le Q,\quad T\le3\pi D.
\tag{2.1}
```

The personally checked proof-only inputs are the exact chamber residual
conservation and the #699 uniform hull-side normal-capacity estimate.
The fixed-degree direction lemma is proved in
[the outer-pocket Groemer report](target_c_outer_pocket_groemer_phase_depletion_2026-10-05.md),
using the original Groemer equality classification.
[Outer-train determination](target_c_outer_train_rank_groemer_bank_synthesis_2026-10-05.md)
is reproduced at its needed finite scope below. No draft-branch theorem,
Maxwell reciprocal extension, standard graph separator theorem, or
numerical search is a premise.

## 3. The actual face-end train graph has sparse internal columns

Form a multigraph $`\mathcal G`$ with one vertex per exceptional physical
face and one outside vertex $`o`$. Each stopped train joins its two
terminal face occurrences. An outer occurrence is assigned to $`o`$.
Keep outer-to-outer trains separately; they are loops at $`o`$ and have
no exceptional-face incidence. All other edges remain actual trains.

For a train joining distinct exceptional faces $`F,G`$, its two oriented
boundary side vectors are opposite, $`w`$ at $`F`$ and $`-w`$ at $`G`$.
For a singleton this is the two-side face incidence. For a nonsingleton,
the opposite unit sides of each intervening rhombus preserve this sign
through the entire chain. Its closure column is therefore

```math
(\ldots,Jw\text{ at }F,\ldots,-Jw\text{ at }G,\ldots)^T.
\tag{3.1}
```

For a train ending twice on one bounded face the same calculation would
give a zero column.

The columns of **all** bounded-to-bounded trains are linearly independent.
Otherwise nonzero train rates supported on them would satisfy every
exceptional-face closure. Rhombus closures already hold for opposite-side
rates. Integration along contact paths gives a contact flex. Every outer
train rate is zero, so all loaded velocities coincide along the entire
outer walk. Subtract that translation. The velocity becomes a mixed
contact/diameter flex vanishing at two loaded points; mixed rigidity makes
it zero. Its train rates must then all be zero, contradiction.

Consequently there are no bounded-face loops. For any nonempty face set
$`S`$, let $`e(S)`$ count trains whose two ends are in $`S`$. The columns
are independent and supported on $`2|S|`$ scalar rows. Their coordinate
sums are zero by (3.1), giving two row dependencies. Hence

```math
\boxed{e(S)\le2|S|-2.}
\tag{3.2}
```

This permits repeated face pairs; no unsupported simplicity theorem is
needed. It is not a generic matrix rank assumption.

Every face $`F`$ has exactly $`\deg F`$ terminal occurrences, all counted
once. Therefore its train-graph valence is $`\deg F\ge5`$. If
$`\partial S`$ counts actual trains with exactly one end in $`S`$, including
returns to $`o`$, then

```math
\begin{aligned}
|\partial S|
&=\sum_{F\in S}\deg F-2e(S)\\
&\ge\sum_{F\in S}(\deg F-4)+4.
\end{aligned}
```

Thus

```math
\boxed{|\partial S|\ge Q_S+4\ge|S|+4.}
\tag{3.3}
```

This is an actual simultaneous outward-train currency. It does not identify
source-contact path lengths with face defect.

## 4. Almost every face is a bounded number of transfers from the outside

Every exceptional face is connected to $`o`$, or (3.3) would fail for its
connected component. Let $`d(F)\ge1`$ be its graph distance to $`o`$,
counting the last mixed outer/face train. Set

```math
S_r=\{F:d(F)\ge r\}\qquad(r\ge2).
```

Edges leaving $`S_r`$ join consecutive distance layers $`r,r-1`$, so these
cuts are disjoint for different $`r`$. They contain only bounded-to-bounded
trains. By (3.3),

```math
\sum_{r\ge2}|S_r|
\le\sum_{r\ge2}|\partial S_r|
\le e(\mathcal F)\le2f-2.
\tag{4.1}
```

In particular

```math
\boxed{|S_r|\le2f/(r-1)\le(2\pi+o(1))D/(r-1).}
\tag{4.2}
```

The degree tails convert this face-count bound into a terminal-count bound.
Condition (H2) implies the uniform small-set property

```math
|A_D|/D\to0\quad\Longrightarrow\quad
D^{-1}\sum_{F\in A_D}\deg F\to0.
\tag{4.3}
```

More quantitatively, for every fixed cutoff $`M`$,

```math
D^{-1}\sum_{F\in A}\deg F
\le M|A|/D+
 D^{-1}\sum_{\deg F>M}\deg F.
\tag{4.4}
```

Take the source limit, then the small-set size to zero, then $`M\to\infty`$.
Combining (4.2)--(4.4), the normalized number of trains incident to a
depth-at-least-$`r`$ face tends uniformly to zero as $`r\to\infty`$.

## 5. Fixed-radius bad neighborhoods remain small without a tail rate

A key point is that (H2) is sufficient; no polynomial tail rate is assumed.

For a face set $`A`$, its neighbor count is at most
$`\sum_{F\in A}\deg F`$. Equation (4.4) therefore gives uniform absolute
continuity of neighbor degree mass. Iterating this statement a fixed
number $`r`$ of times proves:

> For each fixed $`r`$ and each $`\delta>0`$, there is $`\zeta>0`$
> such that a seed set incident with at most $`\zeta D`$ terminals has
> at most $`\delta D`$ terminals in its radius-$`r`$ face neighborhood,
> for all sufficiently large sources in the sequence.

One can choose successive size tolerances using (4.4), starting with the
target tolerance and working backward $`r`$ times. This avoids the invalid
estimate $`M^r\beta_M\to0`$, which does not follow from uniform
integrability.

There are three kinds of bad seeds:

- faces of degree greater than a fixed $`M`$;
- bounded-degree faces with residual above their fixed Groemer threshold;
- mixed outer trains ending on long or bad-residual pockets.

The first terminal mass becomes arbitrarily small by (H2). For fixed
$`M,\eta`$, the second is $`o(D)`$, because face residuals sum to
$`R_F=o(D)`$ and each bad face has residual at least a fixed positive
$`\sigma_M(\eta)`$. Short-pocket bad terminal mass is also $`o(D)`$ by the
same argument. Long-pocket terminal mass becomes arbitrarily small by
(H3). A bad outer-to-outer train is counted directly, without assigning
it to a nonexistent bounded endpoint.

Thus for each fixed transfer radius, bad seed neighborhoods consume
arbitrarily little normalized train cardinality when the cutoffs are
increased. All vertices here are auxiliary faces, not deleted source points.

## 6. Propagate Groemer phase to almost every train

Consider a train outside the deep-face family and every bad neighborhood.
If it has bounded endpoints, choose one and follow a shortest face-graph
path to $`o`$. It traverses fewer than $`r`$ faces. All these faces have
degree at most $`M`$ and residual below the fixed threshold.

The fixed-degree Groemer lemma applies to an exceptional face with any
chosen unit boundary edge as reference. Every boundary train on that
face has reduced projective phase within $`\eta`$ of the reference,
hence any two have phase distance at most $`2\eta`$ modulo $`\pi/3`$.
Successive actual trains on the return chain therefore transfer reduced
phase with total error at most $`2r\eta`$.

The last outer terminal either is a unit hull side or lies on a good
pocket of path length at most $`L`$. Its phase is within $`\eta`$ of that
pocket's added hull side. The original train is consequently within
$`(2r+1)\eta`$ of one actual hull-side anchor.

Overlap is controlled at the face level. A good face has valence at most
$`M`$, so one outer train can receive at most a fixed multiple of
$`M^{r+1}`$ chosen train paths of length at most $`r`$. A pocket anchor
has at most $`L`$ outer terminal occurrences. Therefore each hull side
anchors at most $`C_{r,M,L}`$ good train members. This is a cardinality
bound; no route length is being counted independently.

The uniform #699 hull-side normal estimate holds for all hull sides:
each has length at least one. In any shifted reduced interval of width
$`w`$, their count is $`(3w+o_w(1))D`$. Thus a phase bin of width
$`\epsilon`$ contains at most

```math
g_j\le C_{r,M,L}
 [\,3\epsilon+6(2r+1)\eta+o_{r,M,L,\epsilon,\eta}(1)\,]D
\tag{6.1}
```

good train vertices, uniformly in its position.

## 7. Contradiction, with explicit parameter order

Fix any target error $`\delta>0`$.

1. Use (4.2)--(4.4) to choose a fixed $`r`$ so deep-face trains number
   at most $`\delta D`$ eventually.
2. Use the fixed-radius neighborhood statement to choose a seed tolerance.
3. Choose fixed face and pocket cutoffs $`M,L`$ so high-degree and
   long-pocket seeds are below that tolerance, using (H2)--(H3).
4. Choose fixed positive $`\epsilon,\eta`$ sufficiently small for the
   good-bin bound (6.1) to be at most $`\delta D`$.
5. Finally take $`D`$ large. Condition (H1) handles the fixed residual
   thresholds; the near-disk estimate handles the uniform hull error.

Apart from at most $`C\delta D+o(D)`$ bad train vertices, every train obeys
the phase-bin bound. Section 69 removes $`O_\epsilon(D)`$ crossing edges
so each remaining crossing lies in one common phase bin. The crossing
graph is simple and $`T\le3\pi D`$. Good-incidence crossings number at most

```math
\sum_j g_jT_j\le(\max_j g_j)T\le3\pi\delta D^2.
```

Crossings incident to a bad train number at most its cardinality times
$`T`$, hence at most $`C'\delta D^2+o(D^2)`$. Adding the removed crossings,

```math
\limsup R_4/D^2\le C''\delta.
```

The target $`\delta`$ was arbitrary, so $`R_4=o(D^2)`$. This contradicts
the positive Type-II limit in (2.1), proving GA.1. □

## 8. Regressions, scope, and the exact surviving fork

- Generic rank is not a premise: internal-column independence uses actual
  source mixed rigidity and the full outer walk.
- No Euler trail is assumed. Face/edge occurrences, bridges, singleton
  ends and the outside vertex are counted explicitly.
- The two Groemer equality cases are both retained; limiting triangles
  supply directions only. No exact contact or force activation is inferred.
- Positive pinned large-face regressions lack actual global diameter
  loading/Type-II inputs. Their high-degree tails also fail (H2).
- A large near-grid disk has long hull pockets; small residual alone does
  not give (H3).
- Uniform integrability has no asserted rate. Fixed-radius neighborhoods
  are controlled by uniform small-set mass, not a cutoff power times its
  tail.
- The cut sparsity is only on the auxiliary face-end graph. Every original
  source point and every packing inequality remains in force.
- Contact isolates occur in the chamber residual and stay out of the
  core rigidity matrix, exactly as required by Section 57.

Consequently every full-core sequence with $`R_F=o(D)`$ must have a
persistent normalized degree tail in at least one of the two boundary
families. Equivalently it cannot have both tails vanishing. A positive
tail here is the failure of the displayed double-limit condition, not an
unproved single macroscopic face.

The positive-residual branch, persistent physical exceptional-face tails,
persistent outer-pocket tails, and the separate macroscopic-container
branch remain open. Level I is not closed.

**Subsequent extension in this run:** the [augmented train-rank theorem](target_c_augmented_train_phase_rank_small_residual_exclusion_2026-10-05.md)
removes both tail hypotheses and excludes the entire `R_F=o(D)` full-core
branch. The statement and proof above remain valid at their original scope;
the surviving obligation is now positive residual activation plus the
separate macroscopic-container branch.

The companion [finite verifier](../../../research/verify_target_c_global_phase_access_2026_10_05.py)
checks the cut/layer identities and actual unit-source train-column
contracts. It does not certify global optimality, compactness, uniform
integrability, the phase coarea theorem, or an asymptotic source family.
