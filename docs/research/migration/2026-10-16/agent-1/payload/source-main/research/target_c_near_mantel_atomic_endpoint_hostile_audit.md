# Hostile audit — Target C near-Mantel atomic endpoint exclusion

**Date:** 2026-09-12  
**Audited files:**

- `research/target_c_near_mantel_atomic_endpoint_exclusion.md`
- `research/target_c_near_mantel_atomic_endpoint_proof_repair.md`

**Verdict:** **PASS at proof-only scope after the explicit repair note.**  
**Theorem-state authority:** unchanged; canonical Target C remains audit.46 through §123.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The audit attempted to break the endpoint theorem at its four nontrivial transitions:

1. scalar §146 equality -> equality in the §142 phase-atom chain;
2. phase-measure equality -> a finite near-Mantel physical train graph;
3. graph near-Mantel stability -> one central phase atom plus at most two leaves;
4. near-complete physical train pair -> a source-diameter contradiction without an
   exact biclique.

No fatal gap remains after the repair note separates the train-order coordinate from
the diameter projection and spells out the equality case of the §142 measure sandwich.

---

## 1. Scalar endpoint algebra

Let

\[
\Xi_D={1\over D}\left(h-{d_H\over9}-{10s_Z\over9}\right),
\qquad
k=d_H+s_Z,
\qquad
t={q-k\over D}.
\]

The identity

\[
\Xi_D={q-10k/9\over D}=t-{k\over9D}
\]

is correct.

Assume `Xi_D -> C_146` and pass to `k/D -> kappa`. Then

\[
t\to C_{146}+\kappa/9,
\qquad
q/D\to C_{146}+10\kappa/9.
\]

Audited-working §146.2 gives, after substituting
`h/D=t+s_Z/D`,

\[
\liminf f/D
\ge \sqrt{\Delta_2}-{t\over4}+{\kappa\over4},
\]

while the §146 outer-walk inequality gives

\[
\limsup Q/D\le2t-\pi.
\]

At the assumed endpoint both bounds equal

\[
F_0+{2\kappa\over9},
\qquad
F_0={8\sqrt{\Delta_2}-\pi\over9}
=0.497434422369096\ldots .
\]

Since `f<=Q`, the squeeze to

\[
f/D,Q/D\to F_0+2\kappa/9
\]

is valid. No sign reversal is hidden here.

Using `T=q+2f-k`, direct substitution gives

\[
{T-q/2\over D}\to2\sqrt{\Delta_2}.
\]

This was recomputed independently; the `kappa` coefficient cancels exactly.

**Disposition:** PASS.

---

## 2. Equality in the phase-atom argument

Audited-working §142 gives

\[
2\sqrt{\Delta_2}\le x\rho
\]

and

\[
y\le2(1-\rho),
\]

with `x=T/D`, `y=q/T`, and `rho` total atomic phase mass. Therefore

\[
x\rho
\le x(1-y/2)
={T-q/2\over D}+o(1).
\]

At the scalar endpoint the right side tends `2sqrt(Delta_2)`. Hence

\[
x\rho=2\sqrt{\Delta_2}.
\]

Since §142's weighted-Mantel inequality is

\[
{\Delta_2\over x^2}\le{\rho^2\over4},
\]

the two sides are then exactly equal.

The initial proof compressed the next implication too aggressively. The repair note
makes the necessary measure sandwich explicit: §142 bounds the limiting crossing
measure first by product-measure capacity on the exact `pi/3` phase relation and then
by weighted Mantel on the atomic relation graph. Equality at the two ends forces no
limiting crossing mass to be lost to the nonatomic phase population or outside the
atomic `pi/3` relation. Exhausting the atoms by finite zero-boundary neighborhoods and
diagonalizing therefore gives a **physical induced train graph** with

\[
n=(2\sqrt{\Delta_2}+o(1))D,
\qquad
e={n^2\over4}-o(D^2).
\]

The argument does not require finitely many limiting atoms and does not identify
contact-isolated source points with train vertices.

**Disposition:** PASS after repair.

---

## 3. Near-Mantel graph stability

The proof's self-contained stability lemma is valid.

For a triangle-free graph,

\[
d(u)+d(v)\le n
\]

on every edge. Summing gives

\[
\sum_wd(w)^2\le ne.
\]

Cauchy gives

\[
\sum_wd(w)^2\ge{4e^2\over n}.
\]

When `e=n^2/4-o(n^2)`, the edge-weighted average of `d(u)+d(v)` is
`n-o(n)`, so one edge `uv` has this degree-sum. The neighborhoods

\[
U=N(u),\qquad V=N(v)
\]

are disjoint independent sets, cover `n-o(n)` vertices, and all edges outside the
`U x V` pair are incident to the `o(n)` uncovered vertices. Thus

\[
|U|=|V|=n/2+o(n)
\]

and the number of missing `U x V` pairs is `o(n^2)`.

No external stability theorem is needed.

**Disposition:** PASS.

---

## 4. Phase support of the two stability shores

The near-complete `U x V` product rules out positive mass of the same phase atom on
both shores: sufficiently narrow neighborhoods of one projective direction cannot
cross at all.

For distinct positive-mass atoms on opposite shores, their projective separation must
be exactly `pi/3`:

- separation `<pi/3` forbids strict-rhombus crossings;
- separation `>pi/3` by a fixed amount would create a positive quadratic population of
  fixed-positive angular defects, contradicting the Type-II `o(D^2)` total defect
  regime used in §142.

On `R/pi Z`, the exact-distance-`pi/3` relation decomposes into 3-cycles

\[
\{\phi,\phi+\pi/3,\phi+2\pi/3\}.
\]

It has no `K_{2,2}`. Since every positive-mass atom on one near-complete shore must be
related to every positive-mass atom on the other, one shore support is a singleton and
the other has at most its two neighbors.

Both stability shores have mass `(sqrt(Delta_2)+o(1))D`. Therefore the central atom
has that full mass and one opposite leaf atom has at least half of it.

This argument was checked against the right-angle endpoint: a fixed positive mass of
right-angle crossings would have a fixed positive rhombus-area defect and is therefore
outside the endpoint regime.

**Disposition:** PASS.

---

## 5. Near-complete signed-monotone train lemma

This was the highest-risk step.

### 5.1 Order coordinate

The original proof could be misread as using the `pi/6` diameter projection to order
both train families. That would be wrong without a full phase threshold. The repair
note uses a different coordinate.

With contact directions near `alpha_0` and `alpha_0+pi/3`, the **canonical** midpoint
displacement cones of the two families together have width

\[
2\pi/3+o(1)<\pi.
\]

Hence one linear coordinate `X` strictly increases along every selected train in its
canonical orientation, independent of which possible cross pairs are missing.
Actual cross-family rhombi all have the same sign because a crossing in these narrow
windows must have lifted phase difference `pi/3+positive`.

### 5.2 Global order from near completeness

After pruning `o(D)` trains, every retained train misses `o(D)` opposite trains.
Therefore every pair and every triple on one shore has a common neighbor on the other
shore.

For a pair of same-shore trains, the canonical Lemma-76 graph argument applied to any
common opposite neighbor fixes their relative crossing order. The result is independent
of the chosen common neighbor. A common neighbor of each triple makes the pairwise
relations transitive. This produces one total order on each shore, and every train sees
its actual neighbors in the induced opposite order.

This is stronger than generic interval-neighborhood density and is exactly where the
`o(D^2)` missing-pair hypothesis is used.

### 5.3 Two-leg path

Take the maximal `B` train and the maximal `A` neighbor of it. The canonical order says
their mutual crossing is the last retained crossing on both canonical trains. Follow
the `A` train canonically to that crossing, then reverse the `B` train and follow it to
its first retained `A` crossing.

The path endpoints are rhombus centers inside `conv(A)`, so their separation is at
most `D`.

For the diameter estimate use a **second** direction, at angle
`alpha_0+pi/6`. Selected crossing vectors on the two legs are respectively the `B`
contact vectors and the `A` contact vectors, each projecting by

\[
\sqrt3/2-o(1).
\]

Arbitrary intervening rhombi contribute at worst `-O(rho_D)` each. A complete train
crosses at most `2D/sqrt3` rhombi because the canonical transverse coordinate grows by
at least `sqrt3/2` per rhombus and its terminal edge midpoints lie in the source hull of
diameter `D`. Thus the total intervening loss is `o(D)`.

The endpoint half-vector loss is `O(1)`. Since the two selected trains each have all
but `o(D)` opposite neighbors, the result is

\[
D\ge(\sqrt3/2-o(1))(|A|+|B|).
\]

**Disposition:** PASS after repair.

---

## 6. Final numerical contradiction

The central family has size

\[
(\sqrt{\Delta_2}+o(1))D
\]

and the selected leaf family at least

\[
(\sqrt{\Delta_2}/2-o(1))D.
\]

Therefore the train lemma gives

\[
1\ge {3\sqrt3\over4}\sqrt{\Delta_2}-o(1).
\]

Direct evaluation gives

\[
{3\sqrt3\over4}\sqrt{\Delta_2}
=1.237090624640176\ldots,
\]

a fixed margin of about `0.23709`. The contradiction is not a rounding artifact.

**Disposition:** PASS.

---

## 7. Regression checks

- **Sliding interval graph:** does not refute the theorem. Its missing-pair fraction is
  bounded away from zero unless the interval width tends to the full opposite shore.
  The endpoint here has `o(D^2)` missing pairs after Mantel stability.
- **Balanced five-phase `C_5` blow-up:** has crossing density `n^2/5`, a fixed deficit
  from Mantel's `n^2/4`; it cannot occur in the endpoint equality case.
- **Oblique near-triangular two-family grid:** locally realizes coherent near-complete
  crossings, but if its two shore sizes have the endpoint sum, the new two-leg path
  makes its source diameter exceed `D`. Smaller oblique grids remain valid regressions.
- **Holes and bounded defect faces:** the path is internal to the selected physical
  trains and uses only the ambient source diameter. No disk or boundary-crosscut
  hypothesis is introduced.
- **Contact-isolated source points:** retained globally and unused in the core train
  algebra.
- **Exact unit triangle:** not inferred from a limiting phase equality; the theorem
  obtains a diameter contradiction instead.

---

## 8. Scope of what is proved

The audited proof-only conclusion is only:

> the exact lower surface
> \[
> h-d_H/9-10s_Z/9=C_{146}D+o(D)
> \]
> of audited-working §146 is impossible in Type II.

A compactness/diagonal argument therefore gives some absolute positive gap above that
surface, but this audit does not extract a numerical value for the gap.

This does **not** close all Type-II full-core survivors, does not touch the exterior or
internal macroscopic-container branch, and does not alter canonical theorem authority.

**Final verdict:** PASS at proof-only scope after the repair note.
