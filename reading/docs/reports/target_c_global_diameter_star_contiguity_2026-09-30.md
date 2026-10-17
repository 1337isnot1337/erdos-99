> Generated reading edition · [exact source](../../../docs/reports/target_c_global_diameter_star_contiguity_2026-09-30.md) · source SHA-256 `06825be785ac079585d7a44dfecdc52a4a7a708677f47221298b1ab0beca4453`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A8D152E6EFCE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_global_diameter_star_contiguity_2026-09-30.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=212376b679e212e277591f4df04ab7ec79eb21a5; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C-II — global diameter-star contiguity

**Date:** 2026-09-30
**Base main:** af823f5f8b998aadf652df9aed01b2dbc2882e75
**Status:** proof-only; C-II remains open

## Theorem

Let $H=(B,E_H)$ be the loaded diameter graph of a planar configuration of
diameter $D$. Order the distinct projective directions of $E_H$ cyclically.
For every $v\in B$, all diameter edges incident with $v$ occur in one
contiguous block of that order.

Hence, for every sufficiently large canonical non-star Target C survivor,

$$
\boxed{t_v=1\text{ for every }v,\qquad R_D=0,\qquad m_D=d_H=q-h.}
\tag{1}
$$

This removes the incidence-mass loophole left by
target_c_rooted_direction_reentry_defect_2026-09-30.md: there are no
re-entrant diameter stars.

## Proof

Fix $v$. If $vx,vy$ are diameter edges, then

$$
|vx|=|vy|=D,\qquad |xy|\le D.
$$

Writing $\theta=\angle xvy$,

$$
2D\sin(\theta/2)=|xy|\le D,
$$

so

$$
\theta\le\pi/3.
\tag{2}
$$

Thus all rays from $v$ to its diameter neighbors lie in one ordinary cone
$C_v$ of aperture at most $\pi/3<\pi$. Its projective image is an arc
$I_v$. Distinct incident diameter edges have distinct projective directions.

If $\deg_H(v)=1$, contiguity is immediate. Otherwise choose incident edges
$vx_-$, $vx_+$ on the two extreme rays of $C_v$, and let $ab$ be any
diameter edge not incident with $v$.

Canonical C-WOODALL records the planar diameter-thrackle property: two diameter
edges with four distinct endpoints cross properly, while edges sharing an
endpoint meet there. Hence $ab$ meets both $vx_-$ and $vx_+$.
After translating $v$ to the origin, write the intersections as

$$
p=r_-u_-,\qquad q=r_+u_+,
$$

with $r_\pm>0$. A direction vector for $ab$ is

$$
q-p=-r_-u_-+r_+u_+.
\tag{3}
$$

Because the angle between $u_-$ and $u_+$ is less than $\pi$, a
projective direction belongs to the closed cone $C_v$ exactly when one of its
two orientations has nonnegative coefficients in the basis
$(u_-,u_+)$. The coefficients in (3) have opposite signs, and reversing
orientation merely reverses both signs. Therefore

$$
\operatorname{dir}_{\rm proj}(ab)\notin I_v.
\tag{4}
$$

Boundary equality is impossible as well: a nonincident diameter edge parallel
to an extreme incident edge could not meet it as required by the thrackle
property; if they shared the opposite endpoint, distinct collinear
length-$D$ segments would either coincide or put their other endpoints
$2D$ apart.

Thus every diameter-edge direction inside $I_v$ is incident with $v$.
The incident edges form one consecutive projective block.

## Direction-ledger consequences

Current main defines $t_v$ as the number of maximal cyclic runs of positions
incident with $v$, and

$$
R_D=\sum_v(t_v-1).
$$

Canonical Section 66 excludes the pure star for all sufficiently large
survivors, so every incident block is proper. The theorem gives $t_v=1$ for
all $v$, hence $R_D=0$. The exact identity already proved on main,

$$
R_D=m_D-d_H,
$$

then yields $m_D=d_H$.

Therefore every vertex-disjoint consecutive direction pair is a transition
between diameter components; star re-entry creates none.

With $a_D=\arcsin(1/(2D))$, Section 66 gives gap at least $2a_D$ for a
shared pair and $4a_D$ for a disjoint pair. Hence

$$
\pi\ge2a_D(h-d_H)+4a_Dd_H
=2a_D(h+d_H)=2a_Dq,
$$

so

$$
\boxed{q\le{\pi\over2a_D}.}
\tag{5}
$$

Each connected component of $H$ also occupies one contiguous direction
block: star blocks of adjacent vertices overlap in their common edge, so their
union along a graph path is connected. In the Woodall forest branch the
$d_H$ caterpillar components therefore occur as $d_H$ projective blocks,
with exactly the $d_H$ disjoint transitions counted by $m_D$.

## Audit and scope

Earlier S1/DC reports obtained contiguous stars only under special endpoint
saturation hypotheses. The proof here uses only the diameter-neighbor cone
bound and the canonical diameter-thrackle property.

The regular odd shell satisfies the theorem. A pure diameter star also satisfies
contiguity, but $m_D=d_H$ is not asserted for its whole-circle center block;
Section 66 already excludes that case for large canonical survivors. No
Euler-trail inference is made, so arbitrarily long star runs remain allowed.

No computation, verifier, or CI result is used.

The previous next target of bounding the edge mass carried by $o(D)$
re-entrant vertices is unnecessary: there are no re-entrant vertices. The live
endpoint task is now to couple exact contiguous star/component blocks directly
to the near-complete diameter-V hull cover and the inverse-phase harmonic train
families.

C-II and Level I remain open.
