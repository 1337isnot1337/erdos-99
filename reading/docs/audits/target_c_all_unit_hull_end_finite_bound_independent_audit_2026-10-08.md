> Generated reading edition · [exact source](../../../docs/audits/target_c_all_unit_hull_end_finite_bound_independent_audit_2026-10-08.md) · source SHA-256 `5b5394960db06fe385ccbf2d30f8ea8dd9230e8b892810b8fff0e8beb981bd36`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EA36147E2364","canonical":true,"claim_ids":["C-FINITE-HULL-END-ANGULAR-DEFECT-BOUND","C-PENTAGON-FIVE-HULL-END-REGRESSION"],"claim_statuses":{"C-FINITE-HULL-END-ANGULAR-DEFECT-BOUND":"canonical","C-PENTAGON-FIVE-HULL-END-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit of PR #663: finite hull-end depletion and pentagon regression

Date: 2026-10-08. Audit base: origin/main `7eb287be7a0ce813c4ab2a743ed330c72fb3358a`, state `2026-10-08.audit.124`. Target C C-II remains open.

Frozen source: PR #663, branch `research/sol-collar-pentagon-rank-20261004`, tip `70e2f6a95adcc5bac1ade91da9ea26ffdfe78cfd`. Source report SHA-256 `c09e455a9a538dee325247bc1fd3b7fe55ab114b2372cb92c3dc865221461712`; verifier SHA-256 `e910d8e95802f38d322716c5544d3623984c9e28ebe853ec78b0bee9be4ce40d`.

## Verdicts

- **PASS — promote `C-FINITE-HULL-END-ANGULAR-DEFECT-BOUND`.** The finite angular estimate survives independent reconstruction under its explicit annulus hypothesis.
- **REGRESSION VALID — promote `C-PENTAGON-FIVE-HULL-END-REGRESSION`.** A certified 15-point flower has five distinct trains from one physical pentagon face, each ending at an actual unit hull side. Thus a local capacity claim of at most two such hull-ended trains is false.
- **PASS — already subsumed.** The source's all-unit-hull-end finite ledger identity and global asymptotic surplus conclusion are already the exact finite identity and stronger sequence theorem in canonical `C-FULLCORE-HULL-DEPLETION-FLOOR`. They receive no duplicate claim ID. The source's alternative product-measure proof is not imported as a premise.
- **No frontier change.** C-II and Level I remain open. The bound is a reusable finite inequality; it supplies neither a source motion nor a strict sub-D competitor.

## 1. Exact finite theorem audited

Take a canonical contact-minimal, then diameter-pair-minimal C-II source, retain every source point, and let $D$ be its diameter. Let $F$ be the actual loaded force hull. After translation, assume

$$
B\bigl(0,(1/2-\sigma)D\bigr)\subset F\subset B\bigl(0,(1/2+\sigma)D\bigr),\qquad 0\le\sigma<1/2.
$$

Let $\mathcal T$ be all complete stopped trains in the canonical positive-contact core, including singleton trains, and put $T=|\mathcal T|$. Select exactly one exterior outer-face occurrence from each actual unit side of $F$; each physical contact side belongs to one train. Let $H\subset\mathcal T$ be the trains with at least one selected side and $N_0=T-|H|$. Let $R_4$ be the number of bounded strict-rhombus faces and

$$
A_{\rm ang}=\sum_{R}(\alpha_R-\pi/3),
$$

where $\alpha_R\in(\pi/3,\pi/2]$ is the acute projective side angle. For $0<\varepsilon<\pi/6$, define

$$
C(\varepsilon,\sigma)=4\left[(1/2+\sigma)\tan\varepsilon+\frac{\sqrt{2\sigma}}{\cos\varepsilon}\right].
$$

If $E_H$ is the number of rhombus crossings incident to at least one train in $H$, then

$$
\boxed{E_H\le \frac{A_{\rm ang}}{\varepsilon}+2TD C(\varepsilon,\sigma)},
\qquad
\boxed{N_0\ge 2\sqrt{\max\left(0,R_4-\frac{A_{\rm ang}}{\varepsilon}-2TD C(\varepsilon,\sigma)\right)}}.
$$

This is finite and conditional on the displayed annulus. It counts actual hull sides and actual train crossings. Contact-isolated source points remain in the source and are not counted as trains or removed.

## 2. Independent reconstruction

### Unit hull sides in a direction window

Write $r=(1/2-\sigma)D$ and $R=(1/2+\sigma)D$. At a point $p$ on a hull side with outward unit normal $n'$, its support height is at least $r$, while $\lVert p\rVert\le R$. In the decomposition

$$
p=h n'+sJ n',
$$

we have $h\ge r$ and

$$
|s|\le\sqrt{R^2-r^2}=D\sqrt{2\sigma}.
$$

For normals in an oriented interval of radius $\varepsilon$ about $n$, projection onto $Jn$ therefore satisfies

$$
|p\cdot Jn|\le D\left[(1/2+\sigma)\sin\varepsilon+\sqrt{2\sigma}\right].
$$

Those normals form one contiguous convex boundary chain. Every unit side in the chain advances that projection by at least $\cos\varepsilon$, so the chain contains at most

$$
\frac{2D[(1/2+\sigma)\sin\varepsilon+\sqrt{2\sigma}]}{\cos\varepsilon}
$$

unit sides. A projective window has two oriented chains; shifting normal direction by $\pi/2$ to side direction does not change the uniform bound. This yields at most $D C(\varepsilon,\sigma)$ unit hull sides in any projective window of radius $\varepsilon$.

This count includes only physical unit sides. Each such side is an actual contact and is assigned to one train; if a contact is a bridge, selecting one exterior occurrence prevents counting that same physical edge twice.

### Crossing charge and Mantel step

Every crossing with angular defect greater than $\varepsilon$ consumes more than $\varepsilon$ from $A_{\rm ang}$, so there are at most $A_{\rm ang}/\varepsilon$ of them. For any remaining crossing, the two train directions have projective separation in $(\pi/3,\pi/3+\varepsilon]$. Fix either train as an anchor: the other direction lies in one of the two projective windows centered at $\theta+\pi/3$ or $\theta-\pi/3$, each of radius $\varepsilon$. For a crossing incident to $H$, choose the non-$H$ endpoint as anchor when there is one; if both endpoints lie in $H$, choose either. The number of $H$-neighbors in these two windows is bounded by the number of selected hull sides there, at most $2DC(\varepsilon,\sigma)$. Summing over all $T$ possible anchors counts every such crossing at least once. This proves the bound for $E_H$; double counting $H$-to-$H$ crossings only enlarges the upper bound.

Delete $H$ from the canonical simple triangle-free train-crossing graph. The remaining $N_0$ vertices have exactly $R_4-E_H$ crossing edges. Mantel gives $R_4-E_H\le N_0^2/4$, hence the stated square-root inequality, including the zero-edge case through the positive part.

The constants, the two-window count, and the order of counting are valid at the endpoint cases $\sigma=0$ and $\varepsilon<\pi/6$; the former annulus is only vacuous for a finite polygon, while the inequality remains correct. The argument does not infer an annulus from any source theorem and does not assume a rate of convergence to a disk.

## 3. Exact pentagon regression

The frozen verifier uses exact rational arithmetic in
$\mathbb Q(\sqrt5,\sqrt{(5+\sqrt5)/8})$. It checks every pair distance in the regular unit pentagon and the five added outward unit squares, all exact contacts, the plane face walks, hull support, and train decomposition. The 15-point flower has 20 unit contacts, five strict square faces, one central pentagonal face, ten extreme hull vertices, and five actual unit hull sides. The five distinct trains incident to the central pentagon each contain exactly one selected unit hull side. Every pair is at least unit-separated and the contact graph has no triangle. Adding a distant retained isolate preserves the fixture.

Thus the following local statement is false: a convex physical pentagon with a strict rhombus on every side can be incident to at most two complete trains that have selected actual unit hull-side ends. This regression is compatible with canonical `C-FULL-FLOWER-PROJECTIVE-BLOCKER`, which allows five projectively distinct flower terminals. The trains in the fixture share pentagon vertices, and the fixture is not a canonical global minimizer; it says nothing about simultaneous motion, global wall capacity, or Level I.

The verifier was copied byte-for-byte from the frozen source snapshot and rerun. All six fixtures passed: square/additive-two-sharp; unit pentagon; two singleton bridges; nine-point grid/Mantel-sharp; five-hull-end pentagonal flower; and flower with a retained isolate. Its finite checks do not prove the analytic annular estimate, global optimality, or any asymptotic source theorem.

## 4. Duplicate and frontier dispositions

The source report's exact identity

$$
5t_DD+x_B+m_B+d=3b+2g_F+N_0
$$

is the same as the already promoted finite ledger in `C-FULLCORE-HULL-DEPLETION-FLOOR`: substitute $x_B=b-q$, $t_DD=q-k$, and $\mu_DD=t_DD+m_B-2c_I-4$ into its equation (A.11), then both reduce to

$$
4q+m_B+d=2b+2g_F+N_0+5k.
$$

The source's asymptotic $N_0\ge(2\sqrt{\Delta_2}-o(1))D$, full-core surplus floor, and low-$x_B$ high-$t_D$ exclusion are also already supplied by that canonical theorem. We do not import the source's separate product-measure proof or create duplicate IDs. The new finite annular estimate can reproduce the same asymptotic lower bound using $A_{\rm ang}=O(D)$, $T=O(D)$, and $\sigma=o(1)$, but it does not improve the active C-II endpoint.

The source's exploratory collar-to-pentagon transport note remains unreviewed. Its conditional application is not promoted. No discovery branch was modified.
