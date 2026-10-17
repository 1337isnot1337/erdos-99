> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_second_order_pocket_rigidity_2026-09-11.md) · source SHA-256 `215f316a49caab47fdca566ce4abd5aa10266d6c2a6fc3f3c20ede5f01e74fe1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5945D6C0AE38","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — second-order rigidity of the cyclic atomic endpoint

**Date:** 2026-09-11  
**Target:** Target C, C-II, cyclic $`s_Z=d_H=0`$ branch  
**Status:** unpromoted research report; route-map status unchanged  
**LEVEL I STATUS:** STILL OPEN

This report sharpens the cyclic pocket endpoint already isolated by CP. At the
formal atomic value $`\nu_D\to\lambda_A`$, almost every missing force-hull side
is bounded by a two-edge unit path. The new point is that the exact perimeter
defect is the sum of the chord deficits of those paths. Consequently the
non-collinearity angles of the linear family of two-edge paths have square-sum
$`o(D)`$, not merely pointwise convergence along a subsequence.

The degree-three force-balance estimate is also exact enough to identify the next
obstruction: at a degree-three pocket vertex the third-edge stress is controlled
by a *stress-weighted* angular defect, whereas the perimeter argument controls
only the unweighted square-sum. A pocket vertex may have additional contacts
entering the force hull; those forces can cancel, so no individual bound is
asserted at such a vertex. No available theorem bounds concentration of
reciprocal edge lengths, so this does not close the cyclic branch.

## 1. Setup and exact endpoint hypotheses

Let $`A_D`$ be an unbounded sequence of cyclic post-ZF C-II survivors with
$`s_Z=d_H=0`$. Use the notation of CP:

* $`F_D`$ is the actual force hull;
* $`P_D=\operatorname{per}F_D`$;
* $`b_D`$ is the outer contact-face walk length;
* $`a_D`$ is the number of missing force-hull sides;
* $`P`$ ranges over the $`a_D`$ outer pockets and $`k_P\ge3`$ is its graph
  boundary degree;
* $`Q_D`$ is the bounded-face degree defect;
* $`\nu_D=(e_{BB}+2s_C)/D`$.

Assume the atomic endpoint

```math
 \nu_D\longrightarrow\lambda_A,
 \qquad
 \lambda_A=
 \frac{\pi}{\sqrt{\pi^2+(5/4-\sqrt{\pi/(2\sqrt3)})^2}}.
 \tag{SP.1}
```

The promoted/dated cyclic inputs give

```math
 \frac{P_D}{D}\to\pi,
 \qquad
 \frac{b_D-P_D}{D}\to0,
 \tag{SP.2}
```

and CP gives

```math
 \frac{Q_D}{D}\to\lambda_A,
 \qquad
 \frac{e_{BB}}D\to\lambda_A,
 \qquad
 \frac1D\sum_P(k_P-3)\to0.
 \tag{SP.3}
```

The conclusion below uses only these endpoint statements and the exact outer
pocket augmentation; it does not impose hull saturation on the C-II selection.

## 2. Exact chord-defect identity

For an outer pocket $`P`$, let $`\Gamma_P`$ be its contact-graph boundary path
between the two endpoints of the added force-hull side, and let $`\ell_P`$ be
the Euclidean length of that added side. The augmentation has one added side
per pocket, so

```math
 |\Gamma_P|=k_P-1.
 \tag{SP.4}
```

Here $`|\Gamma_P|`$ is the sum of the unit lengths of the contact edges in the
path, with multiplicity. The common portions of the augmented boundary and the
force-hull boundary cancel in the perimeter difference. Hence the exact finite
identity is

```math
 b_D-P_D
 =\sum_P\bigl((k_P-1)-\ell_P\bigr).
 \tag{SP.5}
```

Every summand is nonnegative by the triangle inequality. In particular, if
$`k_P=3`$, then $`\Gamma_P`$ consists of two unit edges and

```math
 2-\ell_P\ge0.
 \tag{SP.6}
```

The identity remains valid when the outer contact boundary has repeated edges:
both $`b_D`$ and the left side of (SP.5) count boundary occurrences, while each
pocket path is counted with its actual multiplicity.

## 3. Second-order pocket rigidity

### Theorem SPR

Under (SP.1), for the subfamily $`\mathcal T_D=\{P:k_P=3\}`$, write
$`\delta_P\in[0,\pi]`$ for the non-collinearity angle of the two unit contact
edges of $`\Gamma_P`$: the internal path angle is $`\pi-\delta_P`$. Then

```math
 \boxed{\sum_{P\in\mathcal T_D}\delta_P^2=o(D).}
 \tag{SP.7}
```

Moreover, fix any $`\delta_0<\pi/3`$. If the internal vertex has contact degree
exactly three, if $`\alpha_{P,1},\alpha_{P,2}`$ are the positive KKT
coefficients of the two path edges, and $`\gamma_P`$ is the coefficient of the
unique third contact edge, then for every triangular pocket with
$`\delta_P\le\delta_0`$,

```math
 \boxed{
 \gamma_P
 \le c(\delta_0)^{-1}
       \min\{\alpha_{P,1},\alpha_{P,2}\}\sin\delta_P
 \le c(\delta_0)^{-1}
       \min\{\alpha_{P,1},\alpha_{P,2}\}\delta_P,
 \qquad
 c(\delta_0):=\sin(2\pi/3+\delta_0)>0.
 }
 \tag{SP.8}
```

Thus the third-edge stress on the degree-three small-angle subfamily obeys the
exact available bound

```math
 \boxed{
 \sum_{\substack{P\in\mathcal T_D\\\delta_P\le\delta_0}}\gamma_P
 \le c(\delta_0)^{-1}
 \sum_{\substack{P\in\mathcal T_D\\\delta_P\le\delta_0}}
 \min\{\alpha_{P,1},\alpha_{P,2}\}\delta_P.
 }
 \tag{SP.9}
```

No unweighted replacement of the right side by $`o(D)`$ is valid without an
additional stress-concentration theorem.

There is a degree-uniform force-balance inequality that is useful even when the
internal vertex has four or five contacts. If $`\Gamma_P`$ denotes the sum of
the positive coefficients of *all* contacts at that vertex other than the two
path edges, then

```math
 \boxed{
 \Gamma_P\ge
 \left|\alpha_{P,1}u_{P,1}+\alpha_{P,2}u_{P,2}\right|
 \ge
 (\alpha_{P,1}+\alpha_{P,2})\sin(\delta_P/2).
 }
 \tag{SP.9a}
```

The first inequality is equilibrium and the triangle inequality. For the
second, the angle between the two path rays is $`\pi-\delta_P`$, so

```math
 \left|\alpha u+\beta v\right|^2
 =(\alpha-\beta)^2+4\alpha\beta\sin^2(\delta_P/2)
 \ge(\alpha+\beta)^2\sin^2(\delta_P/2).
```

Thus higher internal degree does not invalidate the geometric transverse-force
constraint; it only replaces one third-edge coefficient by an uncontrolled sum.

### Proof

By (SP.3), the number of nontriangular pockets is $`o(D)`$. For a triangular
pocket, the law of cosines gives

```math
 \ell_P=2\cos(\delta_P/2).
 \tag{SP.10}
```

Since

```math
 2-\ell_P=2(1-\cos(\delta_P/2))
 \ge \frac{2}{\pi^2}\delta_P^2
 \quad(0\le\delta_P\le\pi),
 \tag{SP.11}
```

the exact identity (SP.5), nonnegativity of all other pocket defects, and
(SP.2) imply

```math
 \sum_{P\in\mathcal T_D}\delta_P^2
 \le \frac{\pi^2}{2}(b_D-P_D)=o(D).
 \tag{SP.12}
```

This proves (SP.7).

For (SP.8), restrict to the degree-three subfamily. Let $`u_1,u_2,w`$ be the
three unit rays from the internal vertex, with positive equilibrium coefficients
$`\alpha_1,\alpha_2,\gamma`$. The
triangle-free unit-contact condition makes each angular gap between consecutive
rays at least $`\pi/3`$. If $`u_1,u_2`$ are the two nearly opposite path rays,
their smaller angular separation is $`\pi-\delta_P`$. Taking the scalar cross
product of

```math
 \alpha_1u_1+\alpha_2u_2+\gamma w=0
 \tag{SP.13}
```

with $`u_2`$ gives

```math
 \gamma\,|w\times u_2|
 =\alpha_1\sin\delta_P.
 \tag{SP.14}
```

The two gaps adjacent to $`w`$ are at least $`\pi/3`$, and their sum is
$`\pi+\delta_P`$. If $`\delta_P\le\delta_0`$, each is at most
$`2\pi/3+\delta_0<\pi`$, so each sine is at least
$`c(\delta_0)=\sin(2\pi/3+\delta_0)`$. Therefore

```math
 \gamma\le c(\delta_0)^{-1}\alpha_1\sin\delta_P.
 \tag{SP.15}
```

Taking the cross product with $`u_1`$ gives the same bound with $`\alpha_2`$.
Taking the smaller of the two bounds and using
$`\sin\delta_P\le\delta_P`$ proves (SP.8), and summing over the small-angle
subfamily proves (SP.9). The square-sum theorem implies that the number of
pockets with $`\delta_P>\delta_0`$ is $`o(D)`$ for every fixed
$`\delta_0>0`$, but it gives no upper bound on the stress concentrated on those
pockets. If the pocket vertex has contact degree four or five, the three-vector
equation (SP.13) is unavailable: additional interior-contact forces may cancel.
Thus (SP.8)--(SP.9) are not asserted for those pockets.
$`\square`$

## 4. What SPR does and does not imply

The reciprocal force polygon has total edge length $`P_*=O(D)`$, so all
individual contact coefficients satisfy $`\alpha_e\le P_*=O(D)`$. Even on the
degree-three, small-angle subfamily where (SP.9) applies, combining (SP.7)
with this coarse bound gives only

```math
 \sum_{\substack{P\in\mathcal T_D,\ \deg(v_P)=3\\\delta_P\le\delta_0}}\gamma_P
 \le O(D)\sum_{P\in\mathcal T_D}\delta_P
 \le O(D)\sqrt{D\sum_{P\in\mathcal T_D}\delta_P^2},
\tag{SP.16}
```

which is only $`o(D^2)`$, far too weak compared with the $`O(D)`$ reciprocal
perimeter scale. A weighted Cauchy estimate would need a bound on
$`\sum_P\alpha_{P,i}\delta_P^2`$, and none is supplied by (SP.2)--(SP.3).
The degree-uniform inequality (SP.9a) does not improve this: it is a lower
bound proportional to the path stress, and the path stresses themselves may
vanish along the thin boundary family while the reciprocal perimeter is carried
by other contacts.

The obstruction is genuine at the local level. For any $`0<\delta<\pi/3`$,
take two path rays at angle $`\pi-\delta`$, and a third ray in the complementary
arc with all three gaps at least $`\pi/3`$. The unique positive equilibrium
coefficients have the third coefficient proportional to $`\sin\delta`$. A
rhombic unit-contact patch generated by two unit vectors with angle
$`\pi/3+\varepsilon`$ is triangle-free for $`\varepsilon>0`$, and its boundary
has exactly this vanishing-angle mechanism. Thus positivity of each finite
coefficient does not furnish a uniform lower bound.

The valid missing statement is specifically a global one:

> If a linear family of triangular outer pockets satisfies (SP.7) in a cyclic
> C-II global minimizer, then either the stress-weighted quantity in (SP.9) is
> forced to be $`o(D)`$ by a reciprocal concentration theorem, or the family
> admits a simultaneous strict sub-$`D`$ reconfiguration.

Neither implication is presently proved. SPR therefore narrows the cyclic
atomic endpoint but does not settle it.

## 5. Branch and regression audit

* **Forest topology:** SPR uses the cyclic identities $`d_H=0`$ and
  $`b-P_D=o(D)`$; it says nothing about the forest $`3d_H`$ charge.
* **$`s_Z>0`$:** not used. The identity (SP.5) is an outer augmentation identity,
  but the endpoint squeezing (SP.3) is cyclic $`s_Z=0`$ data.
* **Exceptional faces:** they are retained through $`Q_D`$ and the $`o(D)`$ count of
  nontriangular pockets; no face is silently treated as a pocket.
* **Higher internal contact degree:** (SP.8)--(SP.9) are not applied to degree-four
  or degree-five internal vertices, but the degree-uniform aggregate constraint
  (SP.9a) retains all their extra positive rays.
* **Repeated outer-walk edges:** (SP.5) counts them with multiplicity.
* **Contact-isolated sources:** they are irrelevant to the perimeter identity and
  are not discarded from the global source; SPR makes no population assertion.
* **Shared diameter endpoints and odd shells:** no diameter matching is assumed;
  regular shells lie outside the atomic CP endpoint hypothesis.

## 6. Status

SPR is a proved, unpromoted second-order endpoint theorem. It does not change the
route-map status. The global C-II ledger remains:

1. cyclic $`s_Z=0`$, with the stress-weighted endpoint obstruction (SP.9);
2. forest $`s_Z=0`$, with no hub-block upper tradeoff for the $`3d_H`$ charge;
3. $`s_Z>0`$, with no support-to-motion theorem for sparse extreme stresses.

Theorem-level closure still requires one of those three missing global results or a
genuine global competitor.
