<!-- theorem-state: {"artifact_id":"ART-0EE8A3655412","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# A global moment obstruction to macroscopic one-step reflected scaling

**Date:** 2026-10-12
**Base commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Target:** full-source Level I comparison, with no contact-core restriction
**Classification:** proved candidate awaiting promotion; artifact unreviewed
**Level I status:** open

The preceding reflected-scale certificate escapes an affine/stress obstruction.
This report tests the construction against the actual leading density of global
minimizers. It proves a restriction applying to **all** minimizers, without
triangle-free, lattice, selected-stress, shell, or phase hypotheses. It does
not give the exact nonattainment statement required for Level I.

## 1. Statement

Let `P_j` be finite unit-separated planar sources with all `n_j` labels,
diameter `D_j->infinity`, and

\[
\frac{n_j}{D_j^2}\longrightarrow\eta_0:=\frac{\pi}{2\sqrt3}.
\]

Center each source at its empirical centroid. Choose arbitrary unit normal and
tangent coordinates `X_i,Y_i`, line offset `c_j`, and positive squared scales
`A_j,B_j`. For arbitrary independent signs let

\[
q_i=(\sqrt{A_j}\,\sigma_i|X_i-c_j|,\sqrt{B_j}\,Y_i).
\]

Suppose these actual planar endpoints retain every label, are unit-separated,
and have diameter at most `(1+o(1))D_j`. Then

\[
\boxed{A_j\longrightarrow1,\qquad B_j\longrightarrow1.}
\]

No a priori bound on the offsets or scales is assumed. In particular the
statement applies to every unbounded global-minimizer sequence and any
proposed one-step full-source endpoint of diameter at most its source diameter.
It also applies to nonglobal sources with the same leading density.

This rules out a fixed macroscopic anisotropic scale as a one-step closure
mechanism. It leaves source-dependent scales tending to one and arbitrary
nonlocal sign assignments. It is not an impossibility theorem for strict
lower-order diameter improvement.

## 2. Full-source empirical disk limit

Use canonical Oler Lemma 21.1 in
[`../theory/03-oler-shell.md`](../theory/03-oler-shell.md):

\[
N\le |K|/a_0+\operatorname{per}(K)/2+1,\qquad a_0=\sqrt3/2.
\]

For a diameter-`D_j` source, Cauchy's perimeter bound and the isodiametric
inequality imply

\[
a_0n_j-O(D_j)\le |\operatorname{conv}P_j|\le\pi D_j^2/4.
\]

Thus the centered normalized convex hulls have area tending to `pi/4` and
diameter at most one. They lie in a fixed compact ball because their centroid
is in their hull. Every Hausdorff subsequential limit is a convex body of area
`pi/4` and diameter at most one, hence a radius-`1/2` disk by the equality case
of the isodiametric inequality.

The point population, not just its hull, is uniformly distributed in that
disk. Indeed, for any fixed rectangle `R`, Oler applied to the source labels
in the convex intersection `D_j R intersect conv(P_j)` for an open rectangle
`R` (using its closure for the finite bound) gives, after division
by `D_j^2`, the upper local density `1/a_0`, with boundary error tending to
zero. The normalized counting measures therefore have density at most
`1/a_0` on the limit hull. Their total mass is exactly its area divided by
`a_0`, so equality holds throughout. Normalizing by the point count gives
the uniform probability measure on the disk. The empirical centroid is zero,
so the disk center is zero. Compact support gives convergence of all moments.
Uniqueness of this limit removes the need to pass to a subsequence.

The same proof applies to the endpoints after centering at their empirical
centroid and dividing by `D_j`: their diameter is at most `1+o(1)`, they have
the same count, and are unit-separated. Their probability measures converge
to the same radius-`1/2` disk. This includes all contact isolates.

Every global minimizer has the stated leading population. A translated
triangular lattice in a disk of radius `sqrt(a_0 n/pi)` has some translate
containing at least `n` sites, by fundamental-cell averaging. Hence
`D(n)<=2sqrt(a_0 n/pi)`. Combined with the Oler upper bound on `n` in terms
of `D(n)`, this gives `n/D(n)^2->eta_0`. The stronger canonical positive
population reserves are not needed here.

## 3. Second and fourth moments determine both scales

Divide all coordinates and the offset by `D_j`. The source coordinates have
zero mean exactly. Unit normals may vary with `j`; disk isotropy makes their
limiting moments independent of those directions. For the uniform disk put

\[
s=\mathbb E X^2=\mathbb E Y^2=1/16,\quad
t=\mathbb E X^2Y^2=1/384,\quad
\mathbb E XY^2=0.
\]

The endpoint tangent centroid is exactly zero. Its tangent variance is
`B_j E Y^2`, while the empirical disk limit makes it tend to `s`. Therefore
`B_j->1`.

First suppose the normalized offsets `gamma_j=c_j/D_j` remain bounded.
The variance of the signed normal coordinate is at least

\[
A_j\operatorname{Var}(|X-\gamma_j|),
\]

because its absolute mean cannot exceed `sqrt(A_j) E|X-gamma_j|`.
The latter variance has a uniformly positive limit on any compact offset
interval: the uniform disk's normal marginal is continuous and `|X-gamma|`
is never constant on its support. The endpoint diameter bounds its variance,
so `A_j` is bounded above. It is bounded away from zero because otherwise
its entire bounded-offset normal coordinate range would vanish, contradicting
the endpoint disk limit. The normal centroid `m_j=E q_x` is also bounded.

Take a subsequence with limits `A,gamma,m`. Absolute normal coordinate
preservation gives two equations, regardless of the signs:

\[
A(s+\gamma^2)=s+m^2,
\qquad
A(t+\gamma^2s)=t+m^2s.
\]

The first is the second normal moment. The second is the normal-square times
tangent-square moment; the source and endpoint centered odd mixed moments
vanish in the limit. Eliminating `m^2` gives

\[
(A-1)(t-s^2)=0,\qquad t-s^2=-1/768\ne0.
\]

Hence every subsequential limit is `A=1`, and `m^2=gamma^2`.

For completeness, suppose instead `|gamma_j|->infinity`. The line is then
outside the source hull, so `|X-gamma_j|` is affine in `X`. Its variance tends
to `s`, proving again that `A_j` is bounded above. If `sqrt(A_j)->0` along
a subsequence, the centered endpoint normal marginal would be supported in
two intervals of lengths tending to zero (one for each sign). Their support
positions are bounded whenever used because the endpoint is centered and
has bounded diameter. A weak limit would have at most two atoms, contradicting
the continuous uniform-disk normal marginal. Thus the normal scale stays
bounded away from zero. Using both signs would now produce normal distance
at least `2sqrt(A_j)(|gamma_j|-1)`, which diverges. All labels must have the
same sign eventually. The map is then affine on every source label, and its
normal variance is `A_j E X^2`. The two disk limits force `A_j->1`.
Splitting arbitrary offset sequences into bounded or diverging subsequences
finishes the proof. QED.

## 4. An exact finite moment identity

For a centered finite source, write

\[
S_x=\mathbb EX^2,\quad S_y=\mathbb EY^2,\quad
T=\mathbb EX^2Y^2,\quad U=\mathbb EXY^2.
\]

For its reflected-scale endpoint write `m=E q_x`,
`V_x=E(q_x-m)^2`, `V_y=E q_y^2`,
`W=E(q_x-m)^2q_y^2`, and `L=E(q_x-m)q_y^2`. Then exactly

\[
\boxed{
W+2mL-V_xV_y=AB(T-S_xS_y-2cU).
}
\]

This follows by expanding the uncentered mixed fourth moment and eliminating
`m^2=A(S_x+c^2)-V_x`. It shows the specific finite odd-moment terms that
can support a deviation from the disk-limit scale restriction. No rate for
those terms, sign assignment, or strict improvement follows from the identity.
The paired exact verifier checks it on the entire 157-label certificate.

## 5. Audit of the unrestricted composition idea

Any prescribed individual point relocation is a selective reflection across
the perpendicular bisector of its old and desired positions; every other label
chooses its unchanged position. Thus, allowing infeasible intermediate states,
at most `n` selective reflections realize any proposed `n`-label competitor,
up to harmless overall rigid motions. Unrestricted composition representability
is therefore not a new bridge to Level I. An existence theorem must extract
the improved target using global source geometry or prove a bounded, coherent
packet reassembly result. The representation alone supplies neither.

## 6. Literature, classification, and remaining obligation

The only repository inequality imported is canonical Oler Lemma 21.1 and its
recorded perimeter/diameter application. The isodiametric equality statement
was checked in the original author-hosted paper by Maggi, Ponsiglione, and
Pratelli, *Quantitative stability in the isodiametric inequality via the
isoperimetric inequality*, introduction, equation (1.1): bounded measurable
sets maximize area at fixed diameter exactly for disks up to null sets.
For a compact convex hull this gives the actual disk. Source:
[author PDF](https://cvgmt.sns.it/media/doc/paper/898/IsodiametricMPP.pdf).
No quantitative stability rate or equality uniqueness from RSR is imported.

The disk-limit and scale-restriction proofs are unreviewed candidates. The
composition observation rejects a proposed shortcut, not another report's
canonical theorem. There is no promotion or theorem-state change.

The exact global obligation remains: construct a same-cardinality planar
unit-separated strict-sub-`D` competitor for every sufficiently large
triangle-free global minimizer. A new construction must overcome the
full-source disk-limit moment constraint; no exact triangle conclusion or
nonattainment theorem follows from this asymptotic restriction.

## Autonomous audit (2026-10-15)

The [PR #959 AI audit](../audits/pr959_autonomous_proof_audit_2026-10-15.md)
records the full proof scope and computational repairs. This remains a
noncanonical artifact; the destination's independent exact-head AI-agent mathematical audit has not been completed. Claims remain unreviewed and unpromoted.
