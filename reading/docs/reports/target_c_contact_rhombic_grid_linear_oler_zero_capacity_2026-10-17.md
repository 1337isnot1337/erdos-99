> Generated reading edition · [exact source](../../../docs/reports/target_c_contact_rhombic_grid_linear_oler_zero_capacity_2026-10-17.md) · source SHA-256 `e89ab07f491ce279c5466f13b13f32cda18dd0c3267b5694e4fc0dfa5467efb7`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-B3CFF2AC8B1D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — linear Oler allowance with zero fixed-wall capacity

**Date:** 2026-10-17  
**Repository base:** `e396ea07887dd0528b817ce4e656ff0e6b01f8fb` (`origin/main`)  
**State version:** `2026-10-15.publication.2`  
**Run type:** exact finite geometric regression  
**Target:** Target C, macroscopic-container capacity  
**Starting status:** canonical C-II container-transfer and static-packet barriers; arbitrary-container capacity remains open  
**External literature search:** not used  
**Computation:** `research/verify_target_c_contact_rhombic_grid_capacity_2026_10_17.py`

## LEVEL I STATUS

**STILL OPEN.**

## 1. Starting canonical endpoint

Audit.108, [the coupled Delaunay container-transfer audit](../audits/target_c_coupled_delaunay_container_transfer_independent_audit_2026-10-07.md), bounds auxiliary population in any convex container by its all-label Oler slack and controls contained-triangle excess. It does not turn that allowance into a source-preserving replacement site. Audit.110, [the exterior static-packet barrier](../audits/target_c_exterior_static_packet_barrier_independent_audit_2026-10-07.md), excludes a static exterior packet under its exact hypotheses, but provides no interior capacity. The current [Target C frontier](../targets/target-c/CURRENT.md) leaves arbitrary-container capacity and a full-source finite move open.

This report tests one tempting fixed-wall inference: that macroscopic diameter, a triangle-free contact-rich source, and a linearly growing all-label Oler allowance should force even one additional fixed-wall site. The construction below refutes that implication for a parallelogram container. It does not test a moved wall or an equal-cardinality source replacement.

## 2. Strongest genuinely new result

**Classification:** exact nonglobal regression; this report and its verifier are unreviewed research artifacts.

### Theorem

Let $`m\ge7`$ be an integer and put

```math
d_m=m^2-6m-3,\qquad c_m=\frac{\sqrt{d_m}}{2m},\qquad
s_m=\frac{\sqrt3(m+1)}{2m}.
```

Then $`c_m^2+s_m^2=1`$, $`0<c_m<1/2`$, and $`\theta_m=\arccos c_m`$ lies in $`(\pi/3,\pi/2)`$. With

```math
u=(1,0),\qquad v=(c_m,s_m),\qquad
A_m=\{iu+jv: i,j\in\{0,\ldots,m\}\},\qquad K_m=\operatorname{conv}(A_m),
```

the following statements hold:

1. $`A_m`$ is unit-separated. Its unit-contact graph is exactly the
   $`(m+1)`$-by-$`(m+1)`$ rectangular grid. Thus it is bipartite, has
   $`2m(m+1)`$ contacts, and every label has contact degree at least two.
2. For area $`Q_m=\operatorname{area}(K_m)`$, perimeter $`p_m`$, and total
   source size $`n_m=|A_m|`$, the all-label Oler slack is exactly
   
   ```math
   S_m:=Q_m/(\sqrt3/2)+p_m/2+1-n_m=m.
   ```

3. The container diameter satisfies
   
   ```math
   D_m=m\sqrt{2+2c_m},\qquad \sqrt2m<D_m<\sqrt3m,
   ```

   so $`Q_m=\Theta(D_m^2)`$, $`p_m=\Theta(D_m)`$, and $`S_m=\Theta(D_m)`$.
4. Every point $`x\in K_m`$ is at distance strictly less than one from at
   least one label of $`A_m`$. Therefore the fixed-wall insertion capacity
   
   ```math
   \{x\in K_m: |x-a|\ge1\ \text{for all }a\in A_m\}
   ```

   is empty, even though $`S_m=m\to\infty`$.
5. $`A_m`$ is not a global minimum-diameter packing of its cardinality: the
   square grid with the same $`(m+1)^2`$ labels is unit-separated and has
   diameter $`\sqrt2m<D_m`$.

In particular, the listed macroscopic scale, contact graph, and Oler slack data do not imply any fixed-wall spare site, even for a triangle-free contact-rich source. This is a fixed-coordinate regression only.

### Proof

Since

```math
d_m+3(m+1)^2=4m^2,
```

we have $`c_m^2+s_m^2=1`$. The polynomial $`m^2-6m-3`$ is positive at $`m=7`$ and increasing for $`m\ge7`$; also $`d_m<m^2`$. Hence $`0<c_m<1/2`$. The specified positive $`s_m`$ is consequently $`\sin\theta_m`$ for the unique $`\theta_m\in(0,\pi/2)`$, and $`s_m>\sqrt3/2`$ gives $`\theta_m>\pi/3`$.

For integers $`a,b`$,

```math
|au+bv|^2=a^2+b^2+2ab c_m.
```

If one coordinate is zero, a nonzero difference has length at least one, with equality exactly for the unit coordinate steps. If $`ab>0`$, then $`a^2+b^2+2ab c_m>1`$. If $`ab<0`$, set $`r=|a|\ge1`$, $`t=|b|\ge1`$. Since $`2c_m<1`$,

```math
|au+bv|^2=(r-t)^2+2rt(1-c_m)>(r-t)^2+rt\ge1.
```

The final inequality follows because $`(r-t)^2\ge0`$ and $`rt\ge1`$. Thus equality occurs only for differences $`(a,b)=(\pm1,0),(0,\pm1)`$. Within the index square these are precisely the rectangular-grid edges. Checkerboard parity $`i+j\pmod2`$ is a bipartition, and the degree assertion follows from the four-neighbor grid (including its corners).

The convex hull is the parallelogram spanned by $`mu,mv`$, so

```math
Q_m=m^2s_m=\frac{\sqrt3}{2}(m^2+m),\qquad p_m=4m,
\qquad n_m=(m+1)^2.
```

Substitution into the stated all-label slack gives

```math
S_m=(m^2+m)+2m+1-(m^2+2m+1)=m.
```

The squared norm $`a^2+b^2+2c_mab`$ is convex in $`(a,b)`$. Its maximum on the square $`[-m,m]^2`$ is attained at a corner; same-sign corners give the larger value. Therefore

```math
D_m^2=m^2(2+2c_m)=2m^2+m\sqrt{d_m}.
```

The strict bounds $`0<c_m<1/2`$ imply the claimed diameter bounds. Since $`Q_m=m^2s_m`$ with $`s_m`$ bounded away from zero and $`p_m=4m`$, the scale comparisons follow.

For the capacity statement, tile $`K_m`$ by its $`m^2`$ unit-edge rhombi. Split each rhombus along its shorter diagonal, whose length is

```math
|u-v|=\sqrt{2-2c_m}.
```

Each resulting triangle has two unit sides with included angle $`\theta_m`$. Its circumradius $`R_m`$ obeys

```math
R_m=\frac{|u-v|}{2\sin\theta_m},\qquad
R_m^2=\frac{2-2c_m}{4(1-c_m^2)}=\frac{1}{2(1+c_m)}<\frac12.
```

Let $`w_1,w_2,w_3\in A_m`$ be the vertices of one such triangle, and let $`x=\sum_{i=1}^3\lambda_iw_i`$ be any point in it, where $`\lambda_i\ge0`$ and $`\sum_i\lambda_i=1`$. If $`o`$ is its circumcenter, the weighted square identity gives

```math
\sum_i\lambda_i|x-w_i|^2
=\sum_i\lambda_i|o-w_i|^2-|x-o|^2
=R_m^2-|x-o|^2\le R_m^2.
```

At least one of the three squared distances is at most this weighted average. Consequently some $`w_i`$ satisfies

```math
|x-w_i|\le R_m<1.
```

The triangles cover the whole parallelogram, including cell boundaries. This proves that every point of $`K_m`$ is strictly within one unit of an original label, so no additional fixed-wall label is feasible.

Finally, the ordinary square grid $`\{(i,j):0\le i,j\le m\}`$ has the same cardinality, minimum separation one, and diameter $`\sqrt2m`$. It is strictly smaller than $`D_m`$, proving the fixture is nonglobal for the minimum-diameter objective.

### Scope and dependencies

The proof uses only Euclidean geometry, exact algebra, and the definitions displayed here; it imports no unreviewed or external theorem. The contact graph contains every source label, so no contact isolate is discarded. The square-grid comparison is an independent same-cardinality feasibility witness, not a replacement of any old source labels under the C-II pair constraints.

This family is distinct from [Audit.156](../audits/target_c_one_deficit_diffuse_strain_independent_audit_2026-10-08.md): there the oblique basis has $`\sin\theta=(\sqrt3/2)(1+1/m^2)`$, producing one unit of all-label Oler slack; here the strain is of order $`1/m`$, and the exact all-label allowance is $`m`$. Both are nonglobal fixed-coordinate saturation regressions. This report strengthens the allowance scale, without claiming canonical source relevance.

## 3. Exact frontier effect

This refutes the fixed-wall inference “$`S\to\infty`$ at macroscopic scale implies at least one feasible insertion” under the explicit parallelogram hypotheses above. It does not refute Audit.108 or Audit.110, whose conclusions are different. It supplies no moved-core motion, source-specific packet, or equal-cardinality exchange.

## 4. Exact remaining lemma

For a canonical C-II full source, construct a source-specific moved-core or multi-cell equal-cardinality endpoint that checks every lower pair and every actual-diameter upper pair, keeps all contact isolates, and meets the untouched macroscopic-container restoration obligation. No fixed-wall count or local saturation calculation supplies this endpoint.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| The displayed family has exactly the asserted unit-contact graph for every integer $`m\ge7`$. | Unreviewed regression | This report; exact-vector verifier at the listed sample parameters | Universal proof above; verifier is finite corroboration. |
| Its all-label Oler slack is exactly $`m`$. | Unreviewed regression | Formulae in this report | Direct exact substitution. |
| Its fixed-wall insertion capacity is zero. | Unreviewed regression | Rhombus triangulation and circumradius cover in this report | Covers every point of the full convex container by strict unit neighborhoods. |
| The fixture disproves a fixed-wall spare-site inference from those statistics. | Unreviewed regression | The three claims above | Direct counterexample; it is not a canonical minimizer. |
| Target C-II or Level I is closed. | Not claimed | None | The source-specific finite endpoint remains open. |

## 6. Reproducible verification

Run:

```sh
python3 research/verify_target_c_contact_rhombic_grid_capacity_2026_10_17.py
```

The standard-library-only verifier uses integers for the radicand and exact squared comparisons in $`\mathbb Q(\sqrt{d_m})`$. It checks the algebraic parameter identities, exhaustively checks all source-pair distances and contact counts for (m=7,8,12,24), and checks the exact slack and diameter formulae. The infinite-(m) conclusions come from the proof above, not from these four enumerations. The continuous cover is proved analytically above and is not approximated by a mesh.

The verifier does not encode global minimization, a moved wall, actual-diameter upper constraints on an exchange, or canonical extraction.

## 7. Lifecycle and limitations

This artifact is unreviewed unless and until an independent audit promotes it. It does not change theorem-state or any canonical claim lifecycle. **LEVEL I remains open.**
