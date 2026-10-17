> Generated reading edition · [exact source](../../../docs/audits/target_c_positive_leaf_anchor_sharpening_independent_audit_2026-10-10.md) · source SHA-256 `c46e90b1975345be2704b4df3085d63f5b84b15402ae6f9214a49faa3e3f32f7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B416A414FB53","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C Audit.247 — sharper positive-leaf anchor localization

> **Publication lifecycle:** this is an unreviewed proposal from source PR #947.
> Its historical PASS/promote language requests a change; the current publication
> manifest does not grant the proposed promotion or stronger scope. Use the exact
> current manifest entry for any inherited canonical premise.


Date: 2026-10-10\
Audit base: origin/main ab6dd3336f9f8d440f2bada76edb32153391cddc, state 2026-10-10.audit.234\
Frozen source: origin/research/level-i-fused-review-20261009 at 6132201c1d3056ca68a222217094acb819f5b4d7\
Source artifact: Section 17.3 of docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md, SHA-256 2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd.

## Verdict

**PASS — strengthen the canonical positive-leaf anchor bound.** Let A be any noncollinear global minimum-diameter source with D sufficiently large. Let p be an actual diameter endpoint with exactly one actual unit neighbor a, and suppose the contact pa has positive coefficient in some normalized full-source KKT stress. Retain every point of A in the definition of K_D. Under these hypotheses, the sole unit-neighbor anchor a satisfies

$$
\operatorname{dist}(a,\partial K_D)=O(D^{-2/3}),
\qquad
K_D=\bigcap_{x\in A}\overline B(x,D-1).
$$

This sharpens Audit.216's O(D^{-1/2}) estimate under the same source, leaf, contact, stress, and isolate-retention hypotheses. It changes no chart-count exponent: the local capacity count is governed by the chart error and remains O(D^(4/5)) for the stated fixed bounded-variation chart family. It supplies no vacancy, packet, source motion, or C-II closure.

This upgrade is audited jointly with Audit.246's near-diameter midpoint theorem, which is its new geometric input. The theorem-state entry for the existing positive-leaf claim is strengthened in place; no duplicate claim ID is introduced.

## Canonical dependencies

The strengthened estimate depends on C-FS-GEOM, C-FS-DIAMETER-MIDPOINT-D2-3, and C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND. The last theorem is audited as Audit.246 in the same dependency-ordered promotion transaction. No unreviewed report is a premise.

## Independent reconstruction

Let c be the full-source minimum-enclosing-circle center and let
$\eta=3^{1/4}\sqrt D$. Canonical C-FS-GEOM gives every source point radius at most $D/2+\eta$. Fix a loaded leaf p with unique actual unit neighbor a, and let $e=(p-c)/|p-c|$. The standard full-source radial lower bound gives $|p-c|\ge D-R\ge D/2-\eta$.

For any source point x with $d=|p-x|\ge D-2$, apply C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND from Audit.246 with s=2. With $\nu=(p-x)/d$, it gives

$$
|(p-c)\cdot J\nu|\le13D^{2/3}+4D^{1/3},
\qquad
(p-c)\cdot\nu\ge h(\nu)-2\ge D/2-2\eta-2.
$$

For sufficiently large D the second quantity is positive and of order D. Therefore the angle between $\nu$ and e is at most $C_0D^{-1/3}$ for an absolute $C_0$. Applying the same estimate with s=0 shows that every actual diameter normal incident to p lies in this same angular window about e.

Write n=p-a, a unit vector. At p the full-source KKT equilibrium is

$$
\alpha n=\sum_y\beta_y(p-y),\qquad \alpha>0,\quad\beta_y\ge0,
$$

where the sum is over actual diameter partners and each nonzero vector p-y has length D. Hence n is a positive combination of the actual diameter unit normals. Those normals all lie in an angular interval of width $O(D^{-1/3})<\pi/2$ about e, so n lies in the same cone. Every direction $\nu$ for a pair p,x with d at least D-2 consequently satisfies

$$
n\cdot\nu\ge1-C_1D^{-2/3}
$$

for an absolute C1.

For such x,

$$
|a-x|^2=|p-x-n|^2
=d^2+1-2d(n\cdot\nu)
\le(d-1)^2+2C_1dD^{-2/3}.
$$

Since d is large, taking square roots gives $|a-x|\le d-1+C_2D^{-2/3}$. For $d<D-2$, the triangle inequality gives $|a-x|\le d+1<D-1$. Thus, with $\delta=C_2D^{-2/3}$, every retained source point satisfies

$$
|a-x|\le D-1+\delta.
$$

It remains to convert this outer radius bound to distance from the boundary of K_D. Let z be the midpoint of any actual diameter pair and put $c_*=1-\sqrt3/2$. Since every source point lies within D of both endpoints of that pair, $|x-z|\le\sqrt3D/2$. Therefore

$$
\overline B(z,c_*D-1)\subset K_D.
$$

Set $W_D=\bigcap_{x\in A}\overline B(x,D)$. We have $K_D+\overline B(0,1)\subset W_D$. The positive KKT combination at p is a supporting normal of W_D there, so

$$
h_{K_D}(n)+1\le h_{W_D}(n)=n\cdot p,
\qquad
h_{K_D}(n)\le n\cdot a.
$$

Thus a lies on or outside a supporting line of K_D. Contract a toward z by the factor

$$
\theta=\frac{c_*D-1}{c_*D-1+\delta}.
$$

For each x in the full source, convexity of the norm gives

$$
|\theta a+(1-\theta)z-x|
\le\theta(D-1+\delta)+(1-\theta)\sqrt3D/2
=D-1.
$$

The contracted point belongs to K_D. Also $|a-z|=O(D)$, so its distance from a is
$$
(1-\theta)|a-z|=\frac{\delta}{c_*D-1+\delta}O(D)=O(D^{-2/3}).
$$

The segment from a to the contracted point meets $\partial K_D$, proving the claimed distance. Every disk and support inequality uses the full retained source, including contact-isolated points.

## Hostile checks and disposition

- The source pair may be any actual pair of length at least D-2; the bound is not restricted to stress-supported pairs.
- The contact direction uses only the positive-coefficient KKT equilibrium at the leaf. No multiplier lower bound is needed.
- The positive combination remains inside the narrow normal cone; the dot-product loss is quadratic in its angular width, yielding D^(-2/3).
- The radius expansion uses d>=D-2, so d>=2 for all sufficiently large D. Shorter pairs are handled separately by the triangle inequality.
- The K_D inball center is an actual diameter midpoint; the radial-direction estimates use the full-source circumcenter. These centers need not coincide.
- Contact isolates remain in every intersection defining K_D. No finite verifier encodes the analytic direction and contraction argument.
- Audit.216's O(D^(-1/2)) result remains a valid earlier proof of a weaker bound. The canonical statement is strengthened in place, and existing leaf-port consequences retain their hypotheses and follow from the stronger boundary estimate.

**Frontier effect: none.** This improves the anchor localization used by a local chart count but does not change the C-II capacity or strict-diameter competitor obligation.
