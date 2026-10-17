> Generated reading edition · [exact source](../../../docs/reports/target_c_multishear_traffic_domination_2026-10-05.md) · source SHA-256 `450d2712b3f24bb25e842502636d61e61f93d56111b92e820f6973c9ad066644`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-9D20AE47BD77","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — exact traffic domination and equality modes in finite multishear

**Date:** 2026-10-05. **Checkpoint:** d3dfbc49; audit.54 import 316b7e33.
**State:** 2026-10-05.audit.54.
**Classification:** proved structural candidate awaiting independent audit.
Unreviewed and noncanonical. **LEVEL I STATUS: STILL OPEN.**

## 1. Exact expression changed

The finite multishear formula formerly left its quadratic traffic term
without a sign. For the **canonical PSD stress**, its sign and entire
scalar kernel are exact:
```math
\boxed{\mathcal B\preceq\operatorname{diag}(A_e),\qquad
\dim\ker(\operatorname{diag}A-\mathcal B)
=2-\operatorname{rank}\operatorname{span}\{w_c:c\text{ unselected}\}.}
\tag{D.1}
```
Consequently every finite multishear has nonincreasing weighted actual
diameter-square sum. If the unselected contacts span two directions, every
nonzero train increment strictly decreases that sum. This disposes of a
mean-energy sign question; it does not dispose of the maximum diameter.

The intended chain is actual PSD stress + actual train cutsets
$`\longrightarrow`$ exact traffic domination and finite mean loss
$`\longrightarrow`$ a common upper-constraint theorem still required
$`\longrightarrow`$ a strict same-cardinality competitor.
Neither generic stress matrices nor virtual cuts are substituted for source
cutsets. This does not assert PSD for arbitrary KKT stresses.

## 2. Canonical inputs and cut coordinates

Use the connected nonisolated positive-contact core $`V`$, full actual
diameter graph $`H`$, and the particular canonical normalized stress
```math
\Omega=L_C^\alpha-L_H^\beta\succeq0,\quad
\ker\Omega=\operatorname{span}\{\mathbf1,p_x,p_y\},\quad
\sum_H\beta_h=1.
```
These are [Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md).
All $`\alpha_c,\beta_h`$ are positive. Isolates stay in the full source
and outside this core matrix.

Take $`r`$ pairwise disjoint proper outer-to-outer stopped-train crosscuts,
with the actual cutset and dual-tree hypotheses of the
[finite multishear chart](target_c_laminar_outer_train_multishear_2026-09-15.md).
Root its complementary-region tree. Let $`S_e`$ be the child shore and
```math
R_{ve}=\mathbf1_{\{v\in S_e\}},\qquad
A_e=\sum_{c\in\tau_e}\alpha_c.
```
For an oriented actual diameter $`h=ij`$, put
```math
\varepsilon_{he}=R_{je}-R_{ie},\qquad
\mathcal B_{ef}=\sum_{h\in H}\beta_h\varepsilon_{he}\varepsilon_{hf}.
\tag{D.2}
```
Its support is the actual dual-tree path. A contact in selected train
$`e`$ has indicator difference $`\pm e_e`$; every unselected contact
has zero difference. Thus
```math
R^TL_C^\alpha R=\operatorname{diag}(A_e),\qquad
R^TL_H^\beta R=\mathcal B.
```
Every dual region incident to a selected cut contains a core endpoint of
one of its cut contacts. Choosing one core representative per region and
subtracting adjacent root-path values proves that $`R`$ has full column
rank. The root representative has value zero.

Therefore the exact source compression is
```math
\boxed{W:=\operatorname{diag}A-\mathcal B=R^T\Omega R\succeq0.}
\tag{D.3}
```
This is a joint constraint, not just a collection of diagonal estimates.
It uses the canonical PSD stress on this same source.

## 3. Complete kernel classification

For $`x\in\mathbb R^r`$, positive semidefiniteness and Section 57 give
```math
Wx=0
\iff Rx=b+\ell\cdot p
```
for a scalar $`b`$ and vector $`\ell\in\mathbb R^2`$.
Since $`Rx`$ is constant across every unselected contact,
$`\ell\cdot w_c=0`$ on all those contacts.
Across a selected contact oriented toward its child shore, its original
vector is $`u_e`$, so $`x_e=\ell\cdot u_e`$.

Conversely take any $`\ell`$ orthogonal to every unselected contact
direction and set $`x_e=\ell\cdot u_e`$. Across every contact edge the
difference of $`Rx`$ equals the difference of $`\ell\cdot p`$.
Connectedness of the core makes their difference a constant. Hence
$`Rx\in\ker\Omega`$ and $`Wx=0`$.

The map $`\ell\mapsto(\ell\cdot u_e)_e`$ is injective on that orthogonal
space: a vector in its kernel is orthogonal to **all** contact directions,
which span the plane because the connected core has a two-dimensional hull.
Thus
```math
\boxed{\ker W=
\{(\ell\cdot u_e)_e:\ell\perp w_c\text{ for all unselected }c\}.}
\tag{D.4}
```
This proves D.1, including the case where no contacts are unselected.
In particular $`W\succ0`$ exactly when the unselected directions span
the plane. The scalar statement is not extended to isolated coordinates.

## 4. Exact finite energy and strict one-cut coefficients

For train angles $`\theta_e`$, let
$`\Delta_e=R_{\theta_e}u_e-u_e`$ and translate each full-source
region by its root-path sum. Every contact is preserved exactly.
The finite source may cease to satisfy other lower constraints at large
angles; the following labelled-coordinate identity remains exact:
```math
\boxed{
\sum_{h\in H}\beta_h|p'_i-p'_j|^2
=D^2-\sum_{\nu=1}^2\Delta_\nu^TW\Delta_\nu.}
\tag{D.5}
```
Here $`\Delta_\nu=(\Delta_{e,\nu})_e`$.
This follows either from D.3 and the canonical stress-energy identity,
or from the exact shore-resultant formula in the multishear report.
For sufficiently small angles, every strict noncontact in the full
source, including pairs involving isolates, retains positive slack.

For one selected cut, write
```math
B_e=\sum_{\text{diameters crossing }S_e}\beta_h.
```
Then $`A_e\ge B_e`$. Equality is possible only when the indicator
$`\mathbf1_{S_e}`$ is affine on the core, so the core lies in two
parallel lines. Each line contains at most $`\lfloor D\rfloor+1`$
unit-separated core points. Therefore
```math
\boxed{|V|>2\lfloor D\rfloor+2\ \Longrightarrow\ A_e>B_e.}
\tag{D.6}
```
In particular this is eventually strict in the full-core Type-II regime.
For any nontrivial one-cut rotation its weighted diameter sum is exactly
```math
D^2-2(A_e-B_e)(1-\cos\theta)<D^2.
\tag{D.7}
```
There is no uniform lower gap asserted for $`A_e-B_e`$ or the smallest
eigenvalue of $`W`$.

## 5. Every finite one-cut constraint is an explicit quadratic

The mean loss is not the endpoint criterion. For one cut take any
crossing **actual source pair**, orient its vector $`r`$ from root
shore toward child shore, and put
```math
\ell^2=|r|^2,\qquad a=r\cdot u,\quad b=r\cdot Ju,\quad
t=\tan(\theta/2).
```
The exact squared change is
```math
|r+R_\theta u-u|^2-\ell^2
=\frac{4t}{1+t^2}\,[b+(1-a)t].\tag{D.8}
```
Thus the full lower constraint is precisely
```math
(\ell^2-1)+4bt+[\ell^2-1+4(1-a)]t^2\ge0,\tag{D.9}
```
and the full upper constraint is precisely
```math
(\ell^2-D^2)+4bt+[\ell^2-D^2+4(1-a)]t^2\le0.\tag{D.10}
```
Same-shore pairs do not move. At $`\theta=\pi`$, test the leading
coefficients separately. Contacts have $`\ell^2=a=1,b=0`$, so D.9
is identically zero. Actual diameters have $`\ell^2=D^2`$, reducing
D.10 to $`4t[b+(1-a)t]\le0`$.

Checking all those inequalities, and strict D.10 where needed for a
strict competitor, is necessary. Inactive old upper pairs cannot be
dropped in a nonlocal rotation. D.9 checks every lower constraint and
ensures distinct final points and unchanged cardinality. The formulas
give exact finite feasibility cells when coordinates are algebraic;
they do not show that such a cell with strictly smaller global diameter
exists in every canonical source.

## 6. Certificate, equality regressions and live obligation

    python3 research/verify_target_c_multishear_traffic_domination_2026_10_05.py

The exact rational packets have positive actual-contact/diameter stresses,
PSD core matrices with precisely the affine scalar kernel, and actual
parallel contact cutsets. They check the entire compressed matrix,
all principal minors, the direction/kernel formula, finite rotated
contacts, every source lower pair and D.5.

The square cut realizes an affine equality mode. Cross packets realize
both strict domination and a nontrivial affine kernel. These are small
source geometries, not large canonical C-II global minimizers; in
particular the cross is not a mixed-rigid canonical counterexample.

For the canonical source, mixed rigidity and positive KKT stress still
give a locally isolating cusp in the **maximum** active diameter.
D.3--D.7 control its mean energy exactly but do not remove that cusp or
the noncontact angular barriers. The live missing bridge is a nonlocal
common upper contraction inside the full lower feasibility cells,
or a collective wall replacement using the canonical disjoint bank.
No canonical branch is closed by the traffic sign alone.
