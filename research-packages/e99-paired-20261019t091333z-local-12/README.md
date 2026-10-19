# Independent destination review: global one-contact candidate

**Review date:** 2026-10-19  
**Candidate:** GLOBAL-LEVEL-I-ONE-CONTACT-PR955  
**Review scope:** destination bytes at 7d0a450fe66991036541023f95c44c064a04b6a8  
**Result:** No mathematical defect found in the one-contact propositions or the finite regressions, conditional on the cited external value of D(8). This is review evidence only. The repository candidate remains unreviewed and noncanonical; Level I remains open.

## Question and scope

Audit this claim: for every finite planar unit-separated labeled n-point set, n >= 2, with minimum pair distance one and an actual contact, pinching one contact and dilating about its midpoint gives a labeled unit-separated set with exactly one unit-contact edge and diameter at most D + epsilon, for every epsilon > 0. Also check the consequences for the triangle-free infimum, nonattainment, the one-contact descent, and the finite global-minimizer controls.

The canonical quantity affected is D(n) and the restricted infimum over triangle-free n-point sets. This result changes only the fixed-n reformulation of Level I as nonattainment of that restricted infimum. It does not establish nonattainment for any n, let alone all sufficiently large n.

**Falsification test:** account for every labeled pair after each deformation, including pairs between a moved endpoint and an unmoved label; check the contact graph and diameter-realizing pairs; then replay the exact rational controls. A counterexample to a lower-pair margin, diameter estimate, compactness step, or quoted n=8 dependency would stop acceptance. Stop after a complete pairwise proof and replay with no missing labels; do not generalize past the stated hypotheses.

## Destination provenance and lifecycle

The pinned destination report SHA-256 is 944b5b3e155586f0edc78e22eeb9bdfb3f954e4e7cbfbd51afa2f2768c125d58; its finite checker SHA-256 is 6c221e1893ac6fa0bbaeac651099f22182d97c46554fa41460a8823e4959025f. The destination artifact index identifies the report as ART-8664DD3819F2, canonical=false, no claim IDs, status=unreviewed. The candidate registry also records it as unreviewed. It has no canonical-claim dependency; its relation to the annular-matching candidate is navigational, and neither that candidate nor Oler is used in this proof.

At this review base, theorem state is 2026-10-15.publication.2, priority is public-frontier.3, and catalogue is public-frontier.9. Level I, A, B, and C-II remain open; C-I remains closed.

The existing docs/audits/pr955_autonomous_proof_audit_2026-10-15.md is the historical source PR #955 audit. It explicitly describes itself as provenance, not a destination exact-head review. Live overlap found merged migration/map PR #26, which preserves the candidate as unreviewed. No exact destination audit appeared in the cached Discussion #83/predecessor handoffs or the live pull-request list (144 records checked; #26 was the only exact candidate match). PR #26 has no GitHub review records. It does not complete the requested destination review.

**Prior-audit exposure:** I reconstructed the geometry below and replayed the candidate checker before opening the historical audit. I read that audit afterward only to distinguish its source-head scope and compare its findings. I do not treat its source-head lifecycle as a destination promotion.

## Independent proof reconstruction

### Pinch, dilate, and retain every label

Let A=(a_1,...,a_n) be a labeled finite subset of R^2, let D=diam(A), and choose a,b at distance one. Put u=b-a, so |u|=1. For 0<t<1/2 replace just those two positions by

$$
a_t=a+tu,\qquad b_t=b-tu.
$$

Their distance becomes 1-2t. For any other label x, reverse triangle inequality gives

$$
|x-a_t|\ge |x-a|-t\ge 1-t>1-2t,
$$

and the same holds for b_t. Pairs of unchanged labels still have distance at least one, so a_t b_t is the unique closest pair. The moved positions lie on the old segment [a,b], hence all labels of B_t lie in conv(A). For convex combinations p=sum_i alpha_i a_i and q=sum_j beta_j a_j,

$$
p-q=\sum_{i,j}\alpha_i\beta_j(a_i-a_j),\qquad
|p-q|\le\sum_{i,j}\alpha_i\beta_jD=D.
$$

Therefore diam(B_t)<=D.

Dilate every position of B_t about m=(a+b)/2 by lambda=1/(1-2t). The selected pair returns to length one. Every other pair touching a moved label had length at least 1-t before dilation; untouched pairs had length at least one. Since lambda>1 and (1-t)/(1-2t)>1, every nonselected pair becomes strictly longer than one. The result is unit-separated with exactly one unit-contact edge, and its diameter is at most D/(1-2t). Since D>=1, choose

$$
t=\frac{\varepsilon}{2(D+\varepsilon)}\in(0,1/2),
\qquad
\frac{D}{1-2t}=D+\varepsilon.
$$

As t tends to zero, every label converges to its original position. The selected endpoints in fact return exactly to their original positions after dilation. No label is discarded or identified with a scaffold.

### Compactness and infimum consequences

For fixed n>=2, translate label 1 to the origin and use n equally spaced collinear points as a finite diameter bound. The feasible configurations below that bound form a closed bounded subset of R^(2n), so a minimizer exists. Its minimum pair distance must equal one: if it were r>1, scaling all positions by 1/r would preserve feasibility and strictly lower the positive diameter.

Let I_tf(n) denote the infimum over triangle-free unit-separated sets, and I_1(n) the infimum over sets with exactly one unit contact. Class inclusion and Proposition 1 applied to an unrestricted minimizer give

$$
D(n)\le I_{\rm tf}(n)\le I_1(n)\le D(n).
$$

Thus both infima equal D(n), and no positive uniform diameter gap above D(n) can hold on the triangle-free class at fixed n. The triangle-free infimum is attained exactly when a triangle-free global minimizer exists. This is an equivalence, not a proof of eventual nonattainment. A strict pointwise inequality diam(A)>D(n) on triangle-free configurations remains compatible with equality of infima.

If a continuous function on labeled configurations is nonnegative on every exactly-one-contact configuration, applying it to the approximants and taking the labeled limit proves nonnegativity on every unit-separated source with minimum distance one. Continuity is essential; strict inequalities do not transfer by this argument.

### Strict descent from exactly one contact

For a source with exactly one contact and n>=3, translate its midpoint to the origin and write the fixed endpoints as a=-u/2 and b=u/2. Contract every other label x to (1-s)x. Since both endpoint distances exceed one,

$$
|x|^2+\frac14-|x\cdot u|>1,
\qquad
|x|^2>\frac34+|x\cdot u|.
$$

For either fixed endpoint e,

$$
\left.\frac{d}{ds}|(1-s)x-e|^2\right|_{s=0}
=-2(|x|^2-x\cdot e)<0,
$$

because |x dot e|=|x dot u|/2 and |x|^2>3/4+|x dot u|>|x dot e|. Distances between two contracted labels are multiplied by 1-s, while the fixed pair stays at one. There are finitely many pairs, every other pair has strict old slack above one, and each moving-involving distance has negative first derivative at zero. One common sufficiently small s>0 therefore preserves every lower constraint and strictly shortens every nonfixed pair. For n>=3 the old diameter exceeds one, so every diameter-realizing pair is nonfixed and the new diameter is strictly smaller. This proves nonattainment only for the exactly-one-contact class; with additional contacts this contraction need not preserve all lower constraints.

### Finite global controls

The square and pentagon classifications are valid global regressions. For a non-extreme label, planar Caratheodory reduces its convex representation to at most three other labels. A two-label representation forces endpoint distance at least two. With three positive weights the rays cannot lie in an open semicircle; one angular gap is in [2pi/3, pi], so the corresponding pair is at distance at least sqrt(3). For four extreme labels, some quadrilateral angle is at least pi/2, giving an opposite diagonal at least sqrt(2); equality forces a unit square. For five extreme labels, some pentagon angle is at least 3pi/5; adjacent sides at least one then give a two-step diagonal at least phi=(1+sqrt(5))/2. Equality forces all angles to be 3pi/5 and all sides one. The regular square and regular pentagon attain these bounds and are triangle-free global minimizers.

The n=8 family is conditional on the report-cited Bezdek-Fodor Theorem 1.1, p. 106, in *Minimal Diameter of Certain Sets in the Plane*, DOI [10.1006/jcta.1998.2889](https://doi.org/10.1006/jcta.1998.2889), for D(8)=1/(2 sin(pi/14)). The coordinates independently check out. With theta=pi/7, R=1/(2 sin(theta)), and H=R cos(theta), the seven listed vertices form a unit regular heptagon and its longest chord is 2R sin(3 theta)=1/(2 sin(pi/14)). The point (0,t), 0<=t<=H-sqrt(3)/2, lies inside the fixed hull. Its distances to the two top vertices are sqrt(1/4+(H-t)^2)>=1; all other vertex distances are strictly larger when t>0, and at t=0 all seven distances equal R>1. Nonadjacent heptagon chords exceed one because the shortest such chord is 2R sin(2 theta)=2 cos(theta)>1. Thus each set is feasible with diameter D(8), hence globally minimizing under the cited value. Before the endpoint the contact graph is C7 plus the eighth isolated vertex; at the endpoint the eighth point completes a triangle with the top edge. All eight labels remain. The characterization of every minimizing hull is not needed for this constructed family; the exact D(8) value suffices.

The n=8 value is an external literature premise, not proved here. The publisher DOI record identifies the article and says it determines D(8); the full-text endpoint returned HTTP 403 during this review. I therefore use the cited value as a conditional premise and do not claim a fresh full-text audit. The historical source audit records a direct primary-PDF check, but that source-head evidence is not recast as this destination review.

## Finite replay and limits

At the pinned destination bytes, ran:

~~~text
flock -x /home/cinna/.local/state/erdos99-host-compute.lock -c 'python research/verify_global_one_contact_2026_10_11.py'
~~~

Observed output:

~~~text
PASS: 16 rational whole-source transformations and descents; 4 exact equilateral checks; all 10 pentagon pairs in Q(sqrt(5)). No Level I claim.
PASS: parameter, actual-contact, planar-label and unique-contact guards
~~~

The checker uses exact rational arithmetic for its finite fixtures and exact Q(sqrt(5)) arithmetic for the regular pentagon. It agrees with the reconstructed proof and rejects malformed-input controls. It does not certify the universal analytic statements, compactness, global optimality of arbitrary sources, the external D(8) theorem, or Level I.

## Disposition

I found no defect in the destination one-contact proof or its stated fixed-n consequences. The n=4, 5, and 8 examples are finite regressions, not an asymptotic counterexample. The exact remaining lemma is to prove that for every sufficiently large n the triangle-free n-point class does not attain D(n), or to construct triangle-free global minimizers for arbitrarily large n. The one-contact result supplies neither outcome.

No theorem manifest, accepted claim lifecycle, candidate registry, priority, generated view, or certificate registration is changed. The candidate retains its existing unreviewed, canonical=false state until a maintainer records disposition under the project review policy. This PR supplies the requested destination audit evidence but does not itself perform a promotion transaction. Required repository-wide theorem-certificate replay is deferred to the merging agent; it is not a validation result of this note.

Prepared with GPT-6 Luna as an independent AI-agent review. This file contains original analysis, cites the external paper without reproducing its text, and preserves credit to source PR #955. No human mathematical review is implied.
