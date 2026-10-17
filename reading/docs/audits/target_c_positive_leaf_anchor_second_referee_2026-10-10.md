> Generated reading edition · [exact source](../../../docs/audits/target_c_positive_leaf_anchor_second_referee_2026-10-10.md) · source SHA-256 `08a363adb26216a9d5893891bae50d597b309341d7b146c97311a3b7b7102257`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-31F8080C75A6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C Audit.247 second referee — positive-leaf anchor localization

Date: 2026-10-10\
Audit base: origin/main ab6dd3336f9f8d440f2bada76edb32153391cddc, state 2026-10-10.audit.234\
Frozen source: origin/research/level-i-fused-review-20261009 at 6132201c1d3056ca68a222217094acb819f5b4d7\
First audit: [Audit.247](target_c_positive_leaf_anchor_sharpening_independent_audit_2026-10-10.md)\
Related dependency audit: [Audit.246 second referee](target_c_midpoint_mean_tail_second_referee_2026-10-10.md)

## Verdict

**PASS — corroborate the $O(D^{-2/3})$ boundary-distance estimate.** The proof is valid under the exact hypotheses and dependencies recorded in Audit.247. This check adds no second claim or theorem ID. Audit.246's near-diameter pair estimate is in the same proposed dependency-ordered promotion transaction; neither proposed increment is canonical on main until that transaction merges.

## Independent reconstruction

Translate the full-source circumcenter to the origin and write $R\le D/2+\eta$, where $\eta=3^{1/4}\sqrt D$. Since $p$ has a diameter partner, $|p|\ge D-R$. For any $x$ with $d=|p-x|\ge D-2$, put $\nu=(p-x)/d$. Audit.246's $s=2$ pair estimate bounds the component of $p$ perpendicular to $\nu$ by $13D^{2/3}+4D^{1/3}$. The support function satisfies $h(\nu)\ge d-R\ge D/2-\eta-2$, and the pair's support deficit at $p$ is at most two, so $p\cdot\nu\ge h(\nu)-2\ge D/2-\eta-4$. Thus $\nu$ lies within $O(D^{-1/3})$ of $e=p/|p|$. Applying the same estimate with $s=0$ puts every actual diameter normal at $p$ in that cone.

At $p$, the full-source KKT balance and the unique positive contact multiplier express the contact unit normal $n=p-a$ as a positive combination of those diameter normals. A positive combination of vectors in an angular cone of width $O(D^{-1/3})<\pi/2$ stays in that cone. Therefore $n\cdot\nu\ge1-O(D^{-2/3})$ for every such $x$. The identity

$$
|a-x|^2=d^2+1-2d(n\cdot\nu)
$$

then yields $|a-x|\le D-1+O(D^{-2/3})$ because $d\le D$ and $d\ge D-2$. For $d<D-2$, triangle inequality gives $|a-x|\le d+1<D-1$. This holds for every source label, including contact isolates.

For the boundary-distance step, let $z$ be the midpoint of an actual diameter pair and set $c_*=1-\sqrt3/2$. The two radius-$D$ endpoint disks imply $|x-z|\le\sqrt3D/2$ for every source point, hence $B(z,c_*D-1)\subset K_D$, where $K_D=\bigcap_x\overline B(x,D-1)$. Put $W_D=\bigcap_x\overline B(x,D)$. Then $K_D+B_1\subset W_D$. The KKT positive combination is in the normal cone of $W_D$ at $p$, so $h_{W_D}(n)=n\cdot p$, while $h_{K_D}(n)+1\le h_{W_D}(n)$. Since $p=a+n$, this gives $h_{K_D}(n)\le n\cdot a$: the anchor is on or outside a supporting line of $K_D$.

Let $r=c_*D-1$, choose $\delta=O(D^{-2/3})$ large enough for the preceding radius bound, and set $\theta=r/(r+\delta)$. The contracted point $y=\theta a+(1-\theta)z$ satisfies, for every source point $x$,

$$
|y-x|\le\theta(D-1+\delta)+(1-\theta)(D-r-1)=D-1,
$$

since $\theta\delta=(1-\theta)r$. Thus $y\in K_D$. Also $|a-z|=O(D)$, so $|a-y|=(1-\theta)|a-z|=O(D^{-2/3})$. The segment from $a$ to $y$ meets $\partial K_D$, proving the claimed distance. The strict common interior point supplied by $z$ also justifies the finite convex-intersection normal-cone rule for $W_D$.

## Hostile checks

- The support lower bound uses only $d\ge D-2$, $R\le D/2+\eta$, and the one-sided support deficit at $p$; its error terms are uniform over $x$.
- The circumcenter and diameter-midpoint centers have distinct roles. $K_D$ is full-dimensional for large $D$ by the explicit inball. If $a\in K_D$, the support inequality puts it on the boundary; otherwise the contraction segment reaches the boundary from outside.
- No pair count, multiplier lower bound, spare site, source motion, or C-II closure follows. No finite verifier encodes this analytic proof.

**Disposition:** no correction or scope reduction is required. Keep the existing claim ID C-POSITIVE-LEAF-ANCHOR-INNER-BALL-BOUNDARY and its explicit dependence on Audit.246. Frontier effect remains none.
