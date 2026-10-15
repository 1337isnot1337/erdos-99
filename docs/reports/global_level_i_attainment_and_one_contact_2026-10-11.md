<!-- theorem-state: {"artifact_id":"ART-8664DD3819F2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global Level I: attainment and an explicit one-contact approximation

- **Date:** 2026-10-11
- **Repository commit:** ab6dd3336f9f8d440f2bada76edb32153391cddc
- **State version:** 2026-10-10.audit.234
- **Run type:** independent global proof investigation
- **Target:** Level I / shared
- **Claim classification:** proved candidate awaiting promotion; registry lifecycle unreviewed
- **Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`
- **External literature search:** problem-status check and primary-source verification of the finite n=8 theorem
- **Computation:** exact finite checks, `research/verify_global_one_contact_2026_10_11.py`

## Level I status

**STILL OPEN.** Neither proposition below proves or disproves the conjecture.
This run investigates the whole configuration and the exact global quantifiers,
without using a selected Target A/B/C subbranch as a premise. All source labels,
including contact-isolated labels, are retained.

## 1. Starting endpoint and attempted implication

The endpoint is the statement in `docs/problem/statement.md`: every global
diameter minimizer contains a unit triangle for all sufficiently large n.

The initially tempting chain is

```text
positive uniform diameter gap at each n for triangle-free packings ->
no triangle-free global minimizer -> Level I
```

Proposition 1 disproves the first premise at every fixed cardinality. The
remaining global route is instead

```text
nonattainment of the triangle-free diameter infimum for all sufficiently
large n -> no triangle-free global minimizer -> Level I
```

No claim of that nonattainment is made here. This distinction matters even
before asymptotics, source geometry, stress selection, or lattice extraction.

## 2. Explicit approximation with exactly one contact

### Proposition 1

Let A be any finite unit-separated planar set of cardinality n >= 2 with
minimum pair distance exactly one and diameter D. Given epsilon > 0 there
is a unit-separated n-point set A_epsilon with exactly one unit-contact
edge, hence no unit triangle, and

\[
\operatorname{diam}(A_\varepsilon)\le D+\varepsilon.
\]

The construction retains all n labels and converges to A as epsilon tends
to zero. It is a whole-source construction, not a scaffold or a subset.

### Proof

Choose an actual contact pair a,b, set u=b-a (so |u|=1), and choose

\[
0<t<\tfrac12.
\]

Replace just these two positions by

\[
a_t=a+tu,\qquad b_t=b-tu,
\]

and leave every other position fixed. Call the resulting labeled set B_t.
The chosen distance is exactly 1-2t. Every other distance involving a moved
endpoint is at least 1-t, by the reverse triangle inequality. Distances
between two unchanged labels are at least one. In particular the labels
remain distinct, and a_t,b_t are the unique closest pair.

Both moved endpoints belong to the old segment [a,b], so
conv(B_t) is contained in conv(A). Convexification preserves diameter:
if x and y are convex combinations of old points, expressing x-y as a
convex combination of old pair differences gives |x-y| <= D. Thus
diam(B_t) <= D.

Dilate B_t about the old midpoint m=(a+b)/2 by factor (1-2t)^(-1):

\[
A_t=m+\frac{B_t-m}{1-2t}.
\]

The selected distance is now one, and every other distance is strictly
greater than one. Moreover diam(A_t) <= D/(1-2t). Set

\[
t=\frac{\varepsilon}{2(D+\varepsilon)}.
\]

Then 0<t<1/2 and D/(1-2t)=D+epsilon. This proves the assertion. Since
t tends to zero, every labeled position converges to its old position.
The selected endpoints actually return to a,b after the midpoint dilation;
the other labels expand about m. No genericity argument is required. QED.

### Corollary 1: equality of three infima

For every integer n >= 2,

\[
\begin{aligned}
D(n)
&=\inf\{\operatorname{diam}A: |A|=n,\ A\text{ unit-separated and triangle-free}\}\\
&=\inf\{\operatorname{diam}A: |A|=n,\ A\text{ unit-separated with exactly one unit contact}\}.
\end{aligned}
\]

To justify applying Proposition 1, a global minimizer exists: translate one
label to the origin, use any finite feasible competitor for an upper
diameter bound, and minimize over the resulting closed bounded set of
labeled configurations. Unit separation preserves distinctness in the
limit. Its minimum separation is one; otherwise uniform contraction would
strictly improve its diameter. Proposition 1 applied to that minimizer
gives both upper infimum bounds, and inclusion in the feasible class gives
both lower bounds.

### Corollary 2: the exact global question is nonattainment

For each fixed n, the conjectured conclusion at n holds if and only if the
triangle-free infimum displayed above is not attained. This is just
Corollary 1 and the definition of global minimizer; it supplies no proof of
nonattainment.

### Corollary 3: closed continuous inequalities transfer to all packings

If a continuous function of labeled configurations is nonnegative on all
unit-separated one-contact configurations, it is nonnegative on every
unit-separated configuration with minimum separation one. Relabeling or
isometry invariance is unnecessary for this statement: use the labeled
convergence in Proposition 1.

In particular there cannot be a positive number eta_n such that all
triangle-free feasible n-point sets have diameter at least D(n)+eta_n.
This excludes diameter-gap arguments even when eta_n depends on n and
decays arbitrarily fast. It does not exclude discontinuous exact-contact
arguments, inequalities restricted to global minimizers, or a proof of
nonattainment by a source-level motion. A strict pointwise inequality
`diam(A)>D(n)` on the triangle-free class remains possible: it is exactly
the desired conclusion at n. Continuity does not transfer strict
inequalities to limits. The rejected premise above is a positive uniform
gap, not that strict pointwise inequality.

## 3. Exactly one contact cannot attain the optimum for n >= 3

### Proposition 2

Every unit-separated planar n-point set with exactly one unit contact and
n >= 3 has a same-cardinality unit-separated competitor with strictly
smaller diameter. Consequently the one-contact infimum in Corollary 1 is
not attained for any n >= 3.

### Proof

Translate the midpoint of the unique contact a,b to the origin and write
a=-u/2, b=u/2, |u|=1. Keep a,b fixed and contract every other label x
to (1-s)x, with s > 0 small.

For such a label, both old endpoint distances are strictly greater than
one. Squaring the smaller one gives

\[
|x|^2+\tfrac14-|x\cdot u|>1,
\quad\text{hence}\quad |x|^2>\tfrac34+|x\cdot u|.
\]

For e=a or e=b, the derivative at s=0 is

\[
\left.\frac{d}{ds}|(1-s)x-e|^2\right|_{s=0}
=-2(|x|^2-x\cdot e)<0,
\]

because |x dot e| <= |x dot u|/2. Every distance between two contracted
labels also strictly decreases, and the sole fixed-fixed distance stays
one. There are finitely many pairs, so every nonfixed distance strictly
decreases for one common sufficiently small positive s. Their strict old
lower slack simultaneously ensures that all remain greater than one.

Since n >= 3 the old diameter is greater than one. Every pair realizing
that diameter involves a contracted label and strictly shortens; indeed
every other nonfixed pair also shortens. The new diameter is therefore
strictly smaller. This proves the claimed feasible finite competitor. QED.

## 4. Why this does not close Level I

Triangle-free does not mean one-contact. Proposition 2 cannot be extended
to all triangle-free contact graphs by the same contraction: additional
unit contacts can shorten, invalidating separation. Repository regressions
in `docs/theory/02-nonlinear-and-regressions.md`, Sections 13--14, already
rule out a universal local-descent assertion for triangle-free sets.
Their statements are binding warnings here, not proof dependencies.

Proposition 1 is also not a disproof. Its diameter bound is D+epsilon,
and it makes no assertion of global optimality. A limit may restore all the
old triangles. Proposition 2 shows explicitly that these one-contact
approximants do not attain the optimum when n >= 3.

The remaining lemma for this independent route is:

> There exists n0 such that for every n >= n0 the triangle-free feasible
> n-point class does not attain its unrestricted diameter infimum D(n).

This is equivalent to Level I, not a newly proved reduction to an easier
lemma. A useful next bridge must add an actual global equality condition
or a valid same-cardinality finite competitor for a larger contact class.

## 5. Checks, dependencies, and limits

### Exact global hostile regressions at n=4 and n=5

**Classification:** regression. These elementary finite classifications are
included to test proposed generalizations of Proposition 2, not as new
solutions of Level I.

First, if a label x of a unit-separated source is not an extreme point,
then its diameter is at least sqrt(3). To see this without a literature
premise, write x as a convex combination of at most three other labels.
Such a three-label expression follows by reducing any convex combination
in the plane along an affine dependence until at most three coefficients
are positive. A two-label expression puts x on their segment and their
distance is at least two. In a genuinely three-label expression, the three
ray gaps about x are at most pi and sum to 2pi. One gap is at least
2pi/3. The corresponding two labels have distances at least one from x;
the cosine rule gives their squared distance at least three.

For four labels in convex position, one quadrilateral angle is at least
pi/2. The diagonal opposite that corner therefore has squared length at
least two. Nonconvex sources have the stronger bound just proved. The
unit square attains sqrt(2), so D(4)=sqrt(2). At equality every corner
angle is at most pi/2, hence all four are pi/2, and the diagonal bound
forces all four sides to be one. Thus the global minimizers are exactly
the unit squares, up to congruence, and are triangle-free.

For five labels, a nonconvex source has diameter at least sqrt(3). In a
convex pentagon one corner angle is at least 3pi/5. Since both adjoining
sides are at least one and cos(3pi/5)<0, the opposite two-step diagonal
has squared length at least

\[
2-2\cos(3\pi/5)=\frac{3+\sqrt5}{2}=\varphi^2,
\qquad \varphi=\frac{1+\sqrt5}{2}<\sqrt3.
\]

The regular unit pentagon attains phi. Thus D(5)=phi. At equality every
corner angle is at most 3pi/5, so all five equal 3pi/5; equality of the
diagonal inequalities forces all sides to equal one. Hence every global
five-point minimizer is a regular unit pentagon and is triangle-free.

These examples certify actual global optimality, in contrast with a local
or pinned-shell regression. They show why replacing “one contact” by
“triangle-free connected contact graph” in Proposition 2 is false. They
also give genuine attained triangle-free infima in Corollary 1. For n=3,
D(3)=1 and the minimizer is a unit equilateral triangle, so that infimum
is not attained. This small-n distinction does not determine eventual
nonattainment.

### Attempt ledger: a subsumed stress-component route

A second global candidate considered during this run was to bound the
diameter of every positive-contact stress component by using its balanced
diameter-edge endpoint distributions and a planar variance bound. This
does not improve the canonical state: `64-extreme-circuit-transfer-audit.md`,
Section 64.3, already proves that every normalized KKT stress has one
connected positive-contact support spanning the full diameter D. That
statement explicitly applies to arbitrary normalized stresses. The weaker
component estimate is discarded as a research route; no new claim or
canonical change is attached to it.

The next investigation must use a global equality condition beyond
positive-support connectivity. The finite square and pentagon above are
binding regressions against connectivity-only assertions.

### A connected family of global optima changes triangle status at n=8

**Classification:** regression. This checks the exact “every minimizer”
quantifier; it is a finite family, not an unbounded-cardinality disproof.

The primary-source premise here is Bezdek--Fodor, Theorem 1.1, printed
page 106: D(8)=1/(2 sin(pi/14)), and every minimizing hull is a regular
unit heptagon. The authors explicitly leave the eighth point nonunique.
The original paper was inspected, at
`papers/primary/1-s2.0-S0097316598928898-main.pdf`, with the theorem also
read in `extracted/text/1-s2.0-S0097316598928898-main.txt`, lines 93--101.
[Publisher DOI](https://doi.org/10.1006/jcta.1998.2889).
No equality statement beyond that theorem is imported.

Here is an exact reconstruction of a particular full-source family.
Put theta=pi/7, R=1/(2 sin(theta)), H=R cos(theta), and let the
regular unit heptagon have vertices

\[
v_k=(R\sin((2k+1)\theta), R\cos((2k+1)\theta)),
\qquad k=0,\ldots,6.
\]

The top adjacent pair is v_0=(1/2,H), v_6=(-1/2,H). Since
theta<pi/6, R>1 and H>sqrt(3)/2. Define

\[
s=H-\frac{\sqrt3}{2}>0,\qquad
A_t=\{v_0,\ldots,v_6,(0,t)\},\qquad 0\le t\le s.
\]

The eighth label lies on the segment from the center to the top-edge
midpoint, so the convex hull stays fixed. For either top endpoint its
squared distance from that label is

\[
\tfrac14+(H-t)^2\ge\tfrac14+(H-s)^2=1.
\]

Every other heptagon vertex has y-coordinate strictly less than H.
For t>0 its squared distance R^2+t^2-2t y is therefore strictly greater
than the distance to a top endpoint. At t=0 all seven distances are
R>1. All heptagon nonadjacent distances are also greater than one.
Thus A_t is unit-separated throughout the interval. Its hull, hence
diameter, stays equal to D(8), so every A_t is a global minimizer.

For 0<=t<s the contact graph is C_7 plus one isolated label and has
no triangle. At t=s the eighth label has unit distance to v_0 and v_6;
their mutual distance is one, so they form a unit triangle. This gives
a connected set of actual global minimizers in which the property changes.
It falsifies the following unrestricted inference:

```text
triangle-bearing optimum reached by a feasible optimal motion ->
every starting optimum contains a unit triangle
```

It also falsifies making triangle existence an open-and-closed property
on connected components of the minimizing configuration space without
a separate theorem. An eventual version needs a substantive large-n
hypothesis and proof. All eight labels, including the initially isolated
one, are retained in this argument.

### Verification scope

Propositions 1--2 and the square/pentagon classifications use only Euclidean
distances, elementary compactness and the definition in
`docs/problem/statement.md`. The n=8 regression additionally uses exactly
the primary-source theorem identified above. No unreviewed report is used
as a mathematical premise.

The exact verifier checks all pair distances in several rational sources,
the unique-contact transformation, the diameter bound, and the common
small finite contraction in Proposition 2. It also checks the equilateral
three-point example symbolically: for t in (0,1/2), its normalized squared
diameter is

\[
\frac{1-t+t^2}{(1-2t)^2}
=1+\frac{3t(1-t)}{(1-2t)^2}>1.
\]

It also checks every pair in an exact regular unit pentagon using arithmetic
in Q(sqrt(5)) for the squared distances. The proofs above, rather than
those finite metric checks, establish global optimality at n=4 and n=5.

The verifier is a finite regression check. The preceding proofs establish
the universally quantified propositions. Neither the checks nor the
proofs settle Level I. No theorem-state promotion is requested here.

**External status locator checked:** [Erdős Problems #99](https://www.erdosproblems.com/99).
Its open-status listing is context only, not evidence for either proposition.

The n=8 interval's feasibility is proved symbolically above, using the
cosine formula and monotonicity on the stated exact angle range. The finite
script does not certify that literature theorem or numerically solve the
heptagon family.

**Promotion recommendation:** preserve as unreviewed global research;
independently audit before admitting either proposition to the canonical
ledger. The canonical frontier and state version stay unchanged.

The 2026-10-15 [substantive audit](../audits/pr955_autonomous_proof_audit_2026-10-15.md)
made unit separation explicit in Corollary 1's second infimum. The exact
checker now refuses optimized Python, validates the planar label domain,
actual selected contact and parameter range, and requires a genuinely unique
contact before descent. Four invalid-input controls pass. The cited n=8
theorem was checked again in the actual primary journal PDF; its use remains
limited to that finite global-minimizer regression.
