> Generated reading edition · [exact source](../../../docs/audits/target_c_paired_cap_spoke_global_comparison_independent_audit_2026-10-07.md) · source SHA-256 `bc6bbd031431da0c3e92fd7f466d9177dc9391797d62b84d48b2e0018fee6c70`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3FE10E06DD6A","canonical":false,"claim_ids":["C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION"],"claim_statuses":{"C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: paired exterior-cap source and strict smaller-diameter comparison

Date: 2026-10-07. Audit base: `9fa9f2e33112842f611b40231f143f06997401d3`, state `2026-10-07.audit.93`; Target C C-II remains open. Frozen source: Worker 2 branch `research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5`. Source report SHA-256 `34bba5b5cf68b10bdad90d77ce61601e50cb51c1cd427f971f14eb76bfb2c179`; verifier SHA-256 `84d2341e7b980d6aba5a40dbe5a770c3d4d0ee62e781ea6b8f9721f2e3e6ff9a`; source certificate SHA-256 `f66ec8f27877a76a77d3f24853d701d66aa89921c367ec7571f82634823ba5e8`.

## Verdict

**REGRESSION VALID — promote** `C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION` for the explicit integer family below. It has a triangle-free contact graph, actual loaded diameter endpoints, a positive KKT stress on every contact and diameter, six antipodally paired exterior caps with quadratic area and isolate populations, only boundary-order Oler capacity slack, and a radius-`3/5` cover of each cap's depth-one region by actual contact isolates. Nevertheless, an exact guard-count injection gives a same-cardinality unit-separated competitor of diameter at most `D-1/2` for every `M>=20`.

The source is deliberately not a global minimizer and does not satisfy the canonical mixed-rigidity or linear loaded-diameter population conditions. This regression shows that the listed reduced exterior-cap geometry and positive equilibrium alone do not imply global optimality or a canonical cap extraction. It does not refute a theorem that uses the full canonical source hypotheses, and it has no C-II or Level I closure consequence.

Two local proof repairs are recorded in the reproduced source report. First, from a unit ball contained in `B(0,M)` one obtains `|x|<=M-1`, not necessarily the strict inequality printed in the source report. Second, scaling a nearest lattice point contributes a displacement term: `|s*ell-x|<=1/sqrt(3)+(s-1)*|ell|`, rather than `s/sqrt(3)`. Since `|ell|<M` and `M>=20`, this is below `3/5`; the direct unscaled estimate also proves `dist(ell,T_M)>1`. Both repairs preserve the claimed cap cover and regression.

## Exact statement audited

Let

```text
Lambda = {(i,j) in Z^2 represented by i*e1+j*e2},
e1=(1,0), e2=(1/2,sqrt(3)/2),
v0,...,v5 = the six cyclic unit directions,
T_M = {k*v_j : 1<=k<=M, 0<=j<6},
s = 1 + 1/(100*M^2), R0=M-1/4,
L_M = Lambda intersect closed_disk(0,R0),
G_M = {ell in Lambda : dist(ell,T_M)<=1},
I_M = L_M \ G_M,
A_M = T_M union s*I_M.
```

For every integer `M>=20`, `A_M` is unit-separated and triangle-free, has exactly `6M` contact edges and exactly three diameter pairs, all six points `M*v_j` are actual loaded diameter endpoints, and `D(A_M)=2M`. The equal contact weights `alpha=2M/3` and diameter weights `beta=1/3` give positive KKT equilibrium; all cloud points `s*I_M` are retained contact isolates with strict lower and upper distance slack.

Let `F_M=conv{M*v_j}` and `K_M=conv(A_M)`. For `n_j=(v_j+v_(j+1))/sqrt(3)`, define `C_j=K_M intersect {x : n_j dot x >= sqrt(3)*M/2}`. These six convex exterior caps occur in exact antipodal pairs. Their interiors are disjoint: two neighboring cap normals are separated by `pi/3`; satisfying both strict outside halfplanes would require a point of norm greater than `(sqrt(3)*M/2)/(cos(pi/6))=M`, contrary to `K_M subset closed_disk(0,M)`. Larger normal separations require at least as large a norm. As `M` tends to infinity, each cap has

```text
area(C_j)/D^2 -> (pi/3 - sqrt(3)/2)/8 > 0,
z_j = |s*I_M intersect C_j| = area(C_j)/(sqrt(3)/2) + O(D),
```

so each contains `Theta(D^2)` actual contact isolates, and `z_j=z_(j+3)` exactly. Since every cap perimeter is `O(D)`, its finite Oler upper-bound allowance above the existing isolate population is nonnegative and `O(D)`. Every point in the cap at distance greater than one from its boundary lies within `3/5` of an actual isolate in that same cap.

Despite these properties, writing `N_M=|A_M|`, there are at least `N_M` points of `Lambda` in the disk of radius `R0`; any `N_M` of them form a unit-separated set of diameter at most `2R0=D-1/2`. Hence `A_M` is not globally diameter-minimizing.

## Independent proof reconstruction

### Contact graph, separation, and diameter

In triangular-lattice coordinates,

```text
|i*e1+j*e2|^2 = i^2+i*j+j^2.
```

The six rays form the central six-cycle plus six radial chains. On adjacent rays the squared distance between `k*v_j` and `l*v_(j+1)` is `k^2+l^2-k*l`, which is one only for `k=l=1`; on rays separated by `120` degrees it is `k^2+l^2+k*l>1`, and opposite rays are farther still. Along a single ray only consecutive points are unit neighbors. Thus the core has exactly `6M` contacts and its contact graph has no triangle.

The lattice norm form is `0` or `1` modulo `3`, so a nonzero lattice vector has length `1` or at least `sqrt(3)`. If `ell` is unguarded, then `dist(ell,T_M)>1`, hence it is at least `sqrt(3)`. Also

```text
|(s-1)*ell| <= (s-1)*R0 < 1/(100*M).
```

Therefore each scaled cloud point is still farther than one from every core vertex. Distinct cloud points are separated by at least `s>1`. The cloud is a set of genuine contact isolates, and it adds no unit triangles.

Every core point has radius at most `M`; every cloud point has radius at most `s*R0<M`. Only the six outer ray endpoints have radius `M`. Consequently the diameter is `2M`, attained exactly by the three opposite outer pairs. These are actual source diameter pairs, not prescribed or auxiliary endpoints.

### Positive full-source KKT stress

Use the stationarity convention that a contact contributes its outward contact vector and a diameter contributes the negative of its upper-distance vector. At a radial-chain interior point, the two contact vectors cancel. At a central hexagon vertex `v_j`, the two hexagon vectors sum to `v_j` while the outward radial edge contributes `-v_j`, before multiplication by the common contact weight. At an outer endpoint, the single contact contribution is `alpha*v_j`; its opposite diameter contributes `-2M*beta*v_j`. With `alpha=2M/3` and `beta=1/3`, these cancel. Every contact and diameter coefficient is positive, and the three diameter coefficients sum to one. Isolate rows are zero and all source points remain in the configuration.

### Paired macroscopic caps and capacity order

I independently checked the support estimate

```text
closed_disk(0,M-4) subset K_M subset closed_disk(0,M).
```

For a unit direction `n`, let `delta<=pi/6` be its angle from a nearest ray. If `delta<=4/(M-3)`, the loaded ray endpoint gives support at least

```text
M*cos(delta) >= M - 8*M/(M-3)^2 >= M-1.
```

Otherwise take `x=(M-3)*n`. Its distance from each nearest spoke line is greater than `8/pi>2`. A nearest triangular-lattice point `ell` has `|ell-x|<=1/sqrt(3)`, lies in `L_M`, and is farther than one from `T_M`; hence it is unguarded. Its scaled source point has support greater than `M-3-1/sqrt(3)>M-4`. The support-function criterion gives the disk inclusion.

After division by `D=2M`, the convex hulls `K_M` converge to the radius-`1/2` disk, while `F_M/D` is the fixed regular hexagon of circumradius `1/2`. Each exterior cap therefore converges in area to the corresponding circular segment, whose central angle is `pi/3`; its normalized area is `(pi/3-sqrt(3)/2)/8`.

Each cap is convex, contained in the radius-`M` disk, and has perimeter `O(M)`. A triangular-lattice Voronoi-cell count gives `area(C_j)/(sqrt(3)/2)+O(M)` lattice sites in it. Passing to the scaled lattice changes density by `s^-2=1+O(M^-2)` and changes the area count by `O(1)`. Restricting indices to `L_M` removes at most the `O(M)` outer annulus; deleting guards removes at most seven lattice sites per core vertex, also `O(M)`. Thus `z_j=area(C_j)/(sqrt(3)/2)+O(M)`. Central symmetry of `T_M`, `L_M`, and `G_M` gives exact equality of opposite cap populations and areas.

For the finite Oler bound in [Lemma 21.1](../theory/03-oler-shell.md),

```text
N_pack(C_j) <= area(C_j)/(sqrt(3)/2) + perimeter(C_j)/2 + 1.
```

The existing cap isolates are a feasible packing and have population `area(C_j)/(sqrt(3)/2)+O(M)`. Therefore the Oler allowance above this population is nonnegative and `O(M)`. This is a boundary-order capacity statement, not a positive refill surplus.

### Every depth-one cap point has an actual nearby isolate

Take `x` in a cap with distance greater than one from its boundary. Its closed unit disk lies in `K_M subset closed_disk(0,M)`, so `|x|<=M-1`. The cap halfplane condition and `|x|<=M` put its direction within `pi/6` of the side normal, hence inside the sector between the adjacent spokes. Its orthogonal projection onto the closing side lies on that side segment: the tangent coordinate has magnitude at most `sqrt(M^2-(sqrt(3)*M/2)^2)=M/2`, the half-length of the segment. Thus distance greater than one from the cap boundary gives closing-side height greater than one. In coordinates `x=t*v_j+y*Jv_j`, this gives

```text
y > sqrt(3)*(M-t)+2.
```

Since `t<=|x|<=M-1`, this implies `y>sqrt(3)+2`; the symmetric estimate holds for the other spoke line. The nearest of the three distinct spoke lines is one of those two, so `dist(x,T_M)>sqrt(3)+2`.

Choose `ell in Lambda` with `|ell-x|<=1/sqrt(3)`. Then

```text
|ell| <= M-1+1/sqrt(3) < M-1/4,
dist(ell,T_M) > sqrt(3)+2-1/sqrt(3) > 1.
```

Thus `ell in I_M`. The actual source isolate `q=s*ell` satisfies

```text
|q-x| <= |ell-x|+(s-1)*|ell| <= 1/sqrt(3)+(s-1)*R0 < 3/5.
```

Because `x` is more than one from the cap boundary, `q` remains in that same cap. This proves the claimed depth-one cover without borrowing a cap-pair theorem or treating a scaffold site as a source point.

### Exact global cardinality trade

Inside `L_M`, the two disjoint families

```text
{ k*v_j : 1<=k<M },
{ k*v_j+v_(j+1) : 0<=j<6, 1<=k<=M-2 }
```

contain `6(M-1)` and `6(M-2)` points, respectively. The first family is in `T_M`. The second-family points lie strictly inside their respective six open 60-degree sectors, are distinct as `k` varies, and none lies on a first-family ray; they are also unit lattice neighbors of `k*v_j` in `T_M`. For `k<=M-2`, their squared norm `k^2+k+1` is at most `(k+1)^2< R0^2`, so all points belong to `L_M`. Hence

```text
|G_M intersect L_M| >= 12M-18 >= 6M.
```

Since the source has `N_M=6M+|L_M|-|G_M intersect L_M|` points, `N_M<=|L_M|`. Choose exactly `N_M` lattice sites in `L_M`. The triangular lattice has minimum spacing one, and all these points lie in the radius-`R0` disk, so their diameter is at most `2R0=2M-1/2`. This strict same-cardinality competitor proves nonoptimality for every `M>=20`. The positive-contact core has `v=e=6M` and `h=3`, so `e+h=6M+3<12M-2=2v-2` and `h<D`; it fails the canonical mixed-rigidity and loaded-diameter-density hypotheses.

## Certificate and hostile scope checks

I inspected and ran the frozen integer verifier. It uses exact triangular-basis integer norms, independently checks the Cartesian radical formula, and tests every source and competitor pair for `M=5,8,12,20,32`. The combined run passed 6,224,805 source-pair checks and 6,224,805 competitor-pair checks; the certificate output exactly matches the source branch's JSON hash. It also checks the contact and diameter lists, triangle-freeness, every KKT equation, strict isolate margins, exact opposite-cap area/population equality, the guard injection, and the finite competitor. The `M=5,8,12` cases are auxiliary and outside the promoted `M>=20` statement.

The verifier does not establish any all-`M` asymptotic assertion, Oler capacity claim, depth-one cover, canonical-source hypothesis, or global-minimizer conclusion. Those universal claims use the analytic arguments above; the competitor proof establishes the opposite of global optimality for this explicit family.

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Exact triangle-free source with actual diameter pairs and positive KKT stress | PASS | Include in the regression scope |
| Antipodal quadratic exterior caps, `O(D)` Oler allowance, and depth-one isolate cover | PASS | Include at the explicit family scope |
| Same-cardinality strict sub-diameter competitor for every `M>=20` | REGRESSION VALID | Promote `C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION` |
| `O(sqrt(D))` support-distance claim for each isolate hull | Not needed for the regression and not audited here | Do not promote |
| Antipodal cap extraction for canonical global minimizers | Not claimed by the family | Remains a separate open proof obligation |
| C-II closure or Level I consequence | NOT PROVED | Both remain open |
