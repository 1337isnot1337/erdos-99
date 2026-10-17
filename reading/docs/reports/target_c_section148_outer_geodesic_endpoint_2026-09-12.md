> Generated reading edition · [exact source](../../../docs/reports/target_c_section148_outer_geodesic_endpoint_2026-09-12.md) · source SHA-256 `dfb9b1bedb32c70b453033ec33c3a3c7fdc40b35d42bcfd0586610150da534b8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-893C69089C90","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C §148 — outer-geodesic endpoint exclusion

**Date:** 2026-09-12
**Classification:** proof-only audited-working candidate; noncanonical
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note composes audited-working §§142--143 with the Type-II force-hull limit and
the audited §146 density chain. It does not assert that the outer contact walk is
always geodesic.

Let

$$
\Delta_2={\pi\over2\sqrt3},\qquad s_2=\sqrt{\Delta_2},
$$

and use $b,P_F,Q,f,T,q,k=d_H+s_Z$ for the occurrence-counted outer walk,
force-hull perimeter, bounded-face degree excess, bounded nonquadrilateral-face
count, stopped-train count, loaded-hull population, and canonical defect.
Canonical Type II gives

$$
{P_F\over D}\to\pi,\qquad {R_4\over D^2}\to\Delta_2,
\qquad b+Q=2(q-k).
\tag{148.1}
$$

Audited §142 gives, on a subsequence with $T/D\to x$, an atomic train-direction
mass $\sigma$ satisfying

$$
x\sigma\ge2s_2,
\tag{148.2}
$$

and the exact endpoint capacity

$$
2T=b+Q+4f.
\tag{148.3}
$$

## 1. Conditional outer-geodesic theorem

Assume

$$
b-P_F=o(D).
\tag{148.4}
$$

Normalize the occurrence-counted outer-edge directions by $D$. Projection of
the closed outer walk onto any unit direction has total variation at least twice
the force-hull width. Near-disk convergence therefore gives, for every projective
angle $\alpha$,

$$
\int|\cos(\theta-\alpha)|\,d\mu_{\rm out}(\theta)\ge2.
$$

The outer measure has total mass $\pi$, and integrating in $\alpha$ gives
equality. Injectivity of the projective cosine transform then yields the uniform
limit

$$
\mu_{\rm out}\Rightarrow d\theta.
\tag{148.5}
$$

Thus every fixed finite set of atomic train-direction windows contains only
$o(D)$ outer endpoint occurrences. The two endpoint incidences of those trains
must be absorbed by bounded nonquadrilateral faces. Taking the atomic windows
through the §142 limit gives

$$
Q+4f\ge2x\sigma D-o(D)
\ge4s_2D-o(D).
\tag{148.6}
$$

Since $f\le Q$,

$$
\boxed{\liminf {Q\over D}\ge{4\over5}s_2.}
\tag{148.7}
$$

Using (148.1) and (148.4),

$$
\boxed{
\liminf {q-k\over D}
\ge{\pi\over2}+{2\over5}s_2
=1.9517214495404795\ldots .
}
\tag{148.8}
$$

This is conditional on (148.4); it is not an unconditional Type-II floor.

## 2. The §146 lower endpoint forces zero outer detour

Let

$$
C_{146}={4\over9}(\pi+s_2)=1.8195135379794445\ldots .
$$

The audited §146 consequence is

$$
\liminf\left({q-k\over D}-{k\over9D}\right)\ge C_{146}.
\tag{148.9}
$$

If $(q-k)/D\to C_{146}$, then $k/D\to0$. The same §146 face inequalities
give

$$
{f\over D}\to r_{146},\qquad {Q\over D}\to r_{146},
\qquad
r_{146}=2C_{146}-\pi=0.49743442236909585\ldots .
\tag{148.10}
$$

The exact identity $b+Q=2(q-k)$ then gives $b/D\to\pi$. Since
$P_F/D\to\pi$ and $b\ge P_F$,

$$
{b-P_F\over D}\to0.
\tag{148.11}
$$

Applying (148.8) contradicts $(q-k)/D\to C_{146}$, because
$1.9517214495\ldots>C_{146}$.

Therefore no Type-II survivor in this audited-working scope can attain the
formal §146 lower endpoint. A qualitative positive gap above $C_{146}$ exists,
but no numerical gap size is proved here.

## 3. Scope and remaining obstruction

The argument retains bridges, repeated outer occurrences, singleton trains, and
contact-isolated source points. It uses no inward-pocket/Reuleaux-cap containment,
full-source affine-kernel extension, or KKT coefficient floor.

It does not rule out a sequence with linear outer detour $b-P_F$, which can host
atomic train endpoints. The remaining full-core task is to charge that detour to
the canonical §122 aggregate detour currency and the §§134--140 joint-payment
ledger. The macroscopic inactive-container branch remains open.
