> Generated reading edition · [exact source](../../../docs/reports/global_separable_distortion_obstruction_2026-10-12.md) · source SHA-256 `de71af209c8ea4753862de88d0a9029ab4d209dc4ce439096547ad8aad56a439`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-089B3ADFC540","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — a global obstruction to separable distance transformations

**Date:** 2026-10-12
**Repository base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Run type:** global closing-proof research / exact regression
**Target:** Level I, direct whole-source comparison
**Classification:** proved candidate awaiting promotion; method limitations are regressions
**Artifact lifecycle:** unreviewed, noncanonical
**Active prompt:** current whole-problem launch prompt, after canonical bootstrap
**External literature:** web reconnaissance; no external theorem imported
**Computation:** `research/verify_global_separable_distortion_obstruction.py`

## Level I status

**STILL OPEN.** The examples below are explicitly nonglobal. This report rules out
one whole-source transformation family; it does not solve the conjecture.

## 1. Global closure test

The desired bridge was:

```text
every sufficiently large triangle-free global minimizer
-> one whole-source conformal transformation with improved diameter/separation ratio
-> normalize minimum separation to one
-> strict same-cardinality sub-D competitor.
```

That universal transformation bridge is not proved. The obstruction below survives
adding a quadratic population of triangle-free source labels. Every lower and upper
source pair is retained in the transformed ratio.

## 2. Exact obstruction and converse for formal arrays

Let A={p_1,...,p_n} have minimum distance one and diameter D>1. Write
q_ij=|p_i-p_j|^2, C={ij:q_ij=1}, and H={ij:q_ij=D^2}. For an edge ij, let
v_ij in R^n have entries one at i and j and zero elsewhere.

For positive vertex factors s_i, define the **formal** squared-distance array

    q'_ij=q_ij s_i s_j.

Such an array need not be realizable by planar points.

**Candidate theorem.** The following statements are equivalent:

1. For every positive factor vector s,
   max_ij q'_ij / min_ij q'_ij >= D^2.
2. conv{v_e:e in C} intersects conv{v_f:f in H}.
3. There are probability weights a_e on C and b_f on H with equal vertex marginals:

       sum_{e in C, i in e} a_e = sum_{f in H, i in f} b_f   for every i.

The equivalence concerns the full formal array. It does not assert that a factor
vector violating statement 1 yields a Euclidean comparison configuration.

### Proof

Statements 2 and 3 are the definition of a common point of the two convex hulls.
Assume 3, and denote the common marginal at vertex i by nu_i. Then

    sum_C a_e log q'_e = sum_i nu_i log s_i,
    sum_H b_f log q'_f = log D^2 + sum_i nu_i log s_i.

The global maximum log q' is at least its H-weighted average, and the global
minimum is at most its C-weighted average. Subtracting proves statement 1.
This uses every source pair for the maximum and minimum, so new extrema among
previously inactive pairs cannot evade the obstruction.

Conversely, if the compact convex hulls in 2 are disjoint, strict hyperplane
separation supplies x in R^n with

    min_{ij in C}(x_i+x_j) > max_{ij in H}(x_i+x_j).

Set s_i(t)=exp(t x_i). Every formal log squared distance is the affine function
log q_ij+t(x_i+x_j). At t=0, only C attains the minimum and only H attains the
maximum. The finitely many other pairs have strictly positive gaps. Thus for
all sufficiently small t>0 the extrema still occur within C and H, and

    log(max q'(t)/min q'(t))
    =log D^2+t[max_H(x_i+x_j)-min_C(x_i+x_j)]
    <log D^2.

This contradicts 1 and proves the equivalence. No planar realization was used.

## 3. Planar realizability: the entire family is Möbius

**Candidate classification.** If two finite planar configurations with distinct
labels satisfy q'_ij=q_ij s_i s_j for positive s_i on every pair, one Möbius
map, possibly composed with reflection, sends all original labels to their
primed counterparts. This is a statement about actual planar realizations, not
arbitrary formal arrays.

To prove it, anchor at label 0 and invert both sources about their anchors:

    r_i=(p_i-p_0)/|p_i-p_0|^2,
    u_i=(p'_i-p'_0)/|p'_i-p'_0|^2,       i != 0.

The exact inversion distance identity and the assumed pair factors give

    |u_i-u_j|^2=q'_ij/(q'_i0 q'_j0)
               =q_ij/(q_i0 q_j0 s_0^2)
               =|r_i-r_j|^2/s_0^2.

Thus the two inverted finite configurations are similar: there is an orthogonal
matrix O and a translation t with u_i=s_0^(-1)O r_i+t. Indeed, subtract one
inverted label and use the polarization identity to recover every vector Gram
entry from the complete distance array; the resulting inner-product isometry
extends to an orthogonal map of the plane, even when the source spans a line.

Composing anchor inversion, this similarity, and the inverse of the primed
anchor inversion gives the required Möbius or reflected Möbius map. The
original anchor is sent to infinity by the first inversion and to p'_0 by the
last, so it too is mapped correctly. No source label is a pole: each prescribed
image is finite and distinct. For a two-label source the same argument uses an
arbitrary similarity aligning the single inverted label.

Conversely, every such map has positive separable distance factors by the
formula below. Therefore the planar realizable separable family is exactly the
finite-source Möbius family, including reflection.

### Regular odd rims

Identify the plane with C. For a nonsingular Möbius map

    f(z)=(az+b)/(cz+d),       ad-bc != 0,

whose pole is not a source label, direct subtraction gives

    |f(z_i)-f(z_j)|^2
    =|z_i-z_j|^2 |ad-bc|^2 / (|cz_i+d|^2 |cz_j+d|^2).

This has the theorem's form, with s_i=|ad-bc|/|cz_i+d|^2. Similarities,
inversions, and compositions with reflection also have this distance form.
Consequently, a common vertex-marginal certificate rules out **every** such
transformation as a strictly improving source replacement. It also rules out
every subsequent uniform rescaling.

For odd m>=5, put a regular unit-side m-gon on its circumcircle of radius

    R=1/(2 sin(pi/m)).

Its diameter is D=2R cos(pi/(2m)). The unit contacts are the cyclic adjacent
pairs. The longest chords join i to i+(m-1)/2 modulo m. Each family has m
distinct edges and degree two at every vertex. Uniform weights 1/m on each
family therefore give equal marginals 2/m at every rim vertex.

Now add any finite unit-separated interior population with all pair distances
at most D and with no rim distances below one. The original rim C/H edges
remain actual unit contacts and actual diameter pairs. Extend both probability
families by zero on every other edge. The marginal equality remains valid,
including zero at every added label. Even arbitrary off-lattice contact isolates
are accounted for: they are present in the full source and in every transformed
pair maximum/minimum.

This is a geometric transformation obstruction, with no assumption of local or
global optimality and no KKT premise.

## 4. Unbounded dense triangle-free nonglobal examples

The obstruction is compatible with quadratic source population and asymptotically
optimal leading density. Here is a complete construction for every odd m>=33.

Keep the regular unit m-rim. Let a0=sqrt(3)/2, eta=1/a0=2/sqrt(3), and
t=1+R^(-2). In an open concentric disk of radius R-1, choose

    N=floor(eta*pi*(R-1)^2/t^2)

points from one translated t-dilate of the triangular lattice. Such a translation
exists by averaging the lattice population of that open disk over a fundamental
cell; its average is the quantity inside the floor. Retain exactly N points.

Interior pairs are at least t>1 apart. Every rim-interior distance exceeds one
by the reverse triangle inequality. Interior-interior distances are below
2(R-1), and rim-interior distances are below 2R-1. Both are below the rim's D:
indeed, with x=pi/(2m),

    2R-D=2R(1-cos x)=tan(x/2)/(2 cos x)<1   (m>=5).

For example x<=pi/10<pi/6 gives tan(x/2)<1 and 2 cos x>1. The complete
source therefore has minimum distance one, diameter D, and exactly the rim
cycle as its contact graph. It is triangle-free and all interior labels are
contact-isolated.

Its cardinality n=m+N satisfies

    n=eta*pi*R^2+O(R),      D=2R+O(1/R),
    n/D^2 -> pi/(2 sqrt(3))=:Delta2.

These sources are **not globally optimal**, as the following explicit bound
shows. Since m<=2*pi*R and t>=1,

    n <= eta*pi*R^2 - 2*pi*(eta-1)*R + eta*pi.

Also R^2 sin^2(pi/(2m))=1/(16 cos^2(pi/(2m)))<1/8, so

    Delta2*D^2 > eta*pi*R^2-eta*pi/8.

For m>=33, R>=m/(2*pi)>5. Since
eta/(eta-1)=4+2 sqrt(3)<8, this gives

    2*(eta-1)*R > 9*eta/8,
    n < Delta2*D^2.

Finally, average the **unit** triangular-lattice population in an open disk of
radius (1/2)*sqrt(n/Delta2). The average is n, so some translation supplies at
least n points; retain n. The finite retained set has diameter strictly below
sqrt(n/Delta2), which is itself strictly below the source D. This is a genuine
whole-source n-point planar competitor. It does not lie in the source's
Möbius orbit, because Section 3 forbids improvement in that orbit.

Thus increasing source population to the optimal leading quadratic coefficient
does not make this transformation family a globally complete search space.
The examples do not satisfy the stronger canonical all-minimizer population
reserve, and no claim is made that they do.

## 5. Formal improvement does not imply planar realization

Take four collinear points at 0,1,2,3 and factors (1,2,3,1). In the order
01,02,03,12,13,23, the transformed squared distances are

    (2,12,9,6,8,3).

The squared diameter/separation ratio drops from 9 to 6. However, their
5-by-5 Cayley--Menger determinant is -72. Four planar points always have
zero such determinant, so no planar configuration realizes this array.

This rejects the implication “the incidence convex hulls are disjoint, therefore
a planar strict competitor exists.” The theorem's converse supplies formal
factors only. Realizability is a separate global condition.

## 6. Dependencies and exact verification

The proofs above are elementary and self-contained: finite convex separation,
logarithms, the Möbius subtraction identity, cyclic degree counts, and lattice
averaging. The unit-lattice comparison is also the argument in the canonical
literature baseline Section 2.2 and shared local-structure Theorem 10.9.
Canonical KKT Theorem 4.1 and stress-midpoint Theorem 11.3 explain why a
first-order conformal attempt was unattractive, but neither is a proof dependency
of this report's new theorem.

Run:

    python3 research/verify_global_separable_distortion_obstruction.py

The script checks 499 odd-rim incidence certificates (m=5,...,1001), every pair
for exact Möbius transformations of m=5,7,9,11 circumcircles in cyclotomic
quotient fields, and the exact nonplanarity determinant in Section 5.
It uses rational and exact symbolic algebra only. Finite output does not prove
the universal theorem or the asymptotic construction; the analytic proofs do.
It certifies no source's global optimality and gives no Level I closure.

## 7. Claim audit and frontier effect

| Claim | Classification | Scope |
| --- | --- | --- |
| Equal vertex marginals characterize universal separable-distortion obstruction | Proved candidate awaiting promotion | Full formal source array |
| All planar realizable separable distance transformations are Möbius, possibly reflected | Proved candidate awaiting promotion | Complete pair array, all source labels |
| The certificate blocks every nonsingular finite-source Möbius map | Proved candidate awaiting promotion | Actual transformed planar configurations |
| Unbounded dense triangle-free sources can have this certificate and a strict independent competitor | Regression | Explicitly nonglobal examples |
| Formal vertex factors alone produce planar replacements | Rejected implication | Exact four-label nonplanarity certificate |
| Every sufficiently large global minimizer is triangular | Open | Not proved here |

No canonical state, A/B/C frontier, or prompt changes are proposed. Preserve this
artifact as unreviewed research. A future independent audit may promote the method
limitation at its precise scope.

## 8. Global continuation

The original closure obligation is unchanged: exclude exact triangle-free
attainment at D(n) for all sufficiently large n. The next global attempt must
permit source replacements beyond separable vertex-distance factors and must
prove their planar realizability, full pair feasibility, retained cardinality,
and strict diameter gain. A formal energy decrease or a dense nonglobal example
does not meet that obligation.
