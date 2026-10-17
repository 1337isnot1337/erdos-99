> Generated reading edition · [exact source](../../../docs/reports/target_c_threshold_packet_reaction_floor_2026-10-02.md) · source SHA-256 `df17398c2f1de2655b4038f1a10a4c8d109d282c4bcdbd810fac05832de99556`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-371701FB74F8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: quantitative packet reactions and the unique weak pivot

**Phase 2 preservation provenance:** PR #618, branch swarm/sol/threshold-rail-packet-20261002, audited source head 9e042ddb7144cbc2f47baac0fa63e9a8ac316761. Preserve the finite packet-reaction result and its threshold application as unreviewed/conditional; the exact verifier is finite and does not realize the complete source stack.

**Date:** 2026-10-02
**Starting checkout:** `78a65968d51af7871a0ce5a865bf2db1a2c2e0ec`
**Research base:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`
**State:** `2026-09-14.audit.51`
**Mission/branch:** threshold source geometry;
`swarm/sol/threshold-rail-packet-20261002`. No assigned coordination issue was
available. The other open reaction, curvature, and rail-cap lanes were inspected.

Classification: **proved candidate awaiting independent audit/promotion** for the
finite geometric lemmas; **conditional** for their threshold application;
**regression** for the examples. Artifact lifecycle remains unreviewed.
Level I and C-II remain **OPEN**.

```text
endpoint separation + full-source circumradius
 -> packet axial load versus multiplier mass, with only one possible weak pivot
 -> exact KKT cut pressures and localization of source blockers
 -> still requires a feasible finite move or a unit triangle; no closure claimed
```

## 1. Dependencies and notation

Canonical input: [the full-source geometry audit](../targets/target-c/58-full-source-geometry-audit.md),
FS.1, for every global minimizer including all isolated source points. The geometric
results below do not assume global optimality except when applying that radius bound.

Unpromoted input: main's [paired staircase](target_c_exact_phase_threshold_paired_staircase_2026-10-01.md),
[rail saturation](target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md),
and [gap connectivity](target_c_exact_phase_gap_graph_connectivity_2026-10-01.md).
The exact cut law is KC.1 in
[the interval-shear curvature report](../../research/target_c_interval_shear_kkt_curvature_identity_2026-09-15.md).
The strict-resultant report on remote commit `6339db4f` was inspected: its
tree-cut balance and equal-flow decomposition are rederived here. Its claim of
positivity is not used as an unaudited premise.

For a staircase edge $`e=\{a,b\}`$, $`a<b`$, orient its diameter vectors from
the lower to the higher layer. Write $`r_h=d_hu+c_hJu`$, $`|r_h|=D`$,

```math
B_e=\sum_{h\in H_e}\beta_h,
\qquad R_e=\sum_{h\in H_e}\beta_hd_h.
```

The physical signs are (L_aU_b) for $`c_h>0`$, and (U_aL_b) for $`c_h<0`$.
The reference diameter is $`za=Du`$, with the two convex hull arcs (L,U)
ordered from $`z`$ to $`a`$. Every layer occurs on both arcs, using (z,a) at
the extreme layers. The common retained cut index is denoted by $`r`$.

## 2. Exact separation of two actual diameter directions

Put $`a_D=\arcsin(1/(2D))`$. For two distinct actual diameter segments,
their projective directions are separated by at least (2a_D). If their four
endpoints are distinct, the separation is at least (4a_D).

Here is a proof of the stronger assertion, also valid for any oriented angle
(\delta\in(0,\pi]) between their vectors. Put

```math
C=D\cos(\delta/2),\qquad S=D\sin(\delta/2).
```

Choose the vector-bisector coordinates and write the difference of chord
midpoints as ((a,b)). The two opposite-end pair distances at most $`D`$ give

```math
a^2+b^2+2C|a|\le S^2. \tag{1}
```

The smaller of the two corresponding-end pair distances has square

```math
a^2+(S-|b|)^2. \tag{2}
```

Set $`t=|b|\le S`$. From (1), $`|a|\le\sqrt{D^2-t^2}-C`$; hence (2) is at most

```math
2D^2-2C\sqrt{D^2-t^2}-2St\le2D(D-C).
```

For the last inequality, write $`t=D\sin\phi`$, $`0\le\phi\le\delta/2`$.
Then $`C\sqrt{D^2-t^2}+St=D^2\cos(\delta/2-\phi)\ge DC`$.
Unit separation therefore implies

```math
1\le 2D(D-C)=4D^2\sin^2(\delta/4),
```

which proves $`\delta\ge4a_D`$. Apply the assertion after reversing either
diameter orientation to obtain the projective statement. For a shared endpoint,
the two distinct partners are unit separated on the radius-$`D`$ circle; this
gives (2a_D), also after reversing orientation.

## 3. The packet reaction floor

For $`D\ge2`$, every staircase packet satisfies

```math
\boxed{R_e\ge g_D B_e,\qquad g_D=\sqrt{1-\frac1{4D^2}}.} \tag{3}
```

Tree-cut balance gives $`\sum_{H_e}\beta_hc_h=0`$. Both signs occur. Put
$`q_h=|c_h|`$, $`f_h=\beta_hq_h`$, and
$`W_e=\sum_{c_h>0}f_h=\sum_{c_h<0}f_h>0`$.
For each positive/negative pair (p,n), define

```math
\rho_{pn}=\frac{q_nd_p+q_pd_n}{q_p+q_n},\qquad
\mu_{pn}=\frac{f_pf_n}{W_e}\left(\frac1{q_p}+\frac1{q_n}\right)>0.
```

Direct summation gives $`\sum\mu_{pn}=B_e`$ and
$`\sum\mu_{pn}\rho_{pn}=R_e`$. Thus (R_e/B_e) is a convex average of the
pair reactions $`\rho_{pn}`$.

Write $`r_p=D(\cos\theta,\sin\theta)`$ and
$`r_n=D(\cos\psi,-\sin\psi)`$, where $`0<\theta,\psi<\pi`$.
Monotonicity of projection onto $`u`$ along both hull arcs gives

```math
d_p+d_n=[s(U_b)-s(U_a)]+[s(L_b)-s(L_a)]\ge0.
```

Consequently $`\theta+\psi\le\pi`$. Equality would make two distinct diameter
segments parallel, which is impossible in a diameter-$`D`$ set: the crossed
pair distances force equal transverse offsets for any two full-width parallel
segments. Put $`\delta=\pi-\theta-\psi>0`$. Then

```math
\rho_{pn}=\frac{D\sin(\delta/2)}{\cos((\theta-\psi)/2)}
\ge D\sin(\delta/2). \tag{4}
```

For four distinct endpoints Section 2 gives
$`\rho_{pn}\ge D\sin(2a_D)=g_D`$.
If the two segments share an endpoint, it must be $`z`$ or $`a`$, the only
intersection of (L,U). A diameter partner of $`z`$ has $`u`$-projection at
least (D/2), because its distance to $`a=z+Du`$ is at most $`D`$.
The analogous statement holds at $`a`$. Hence both longitudinal projections
are at least (D/2), and $`\rho_{pn}\ge D/2\ge g_D`$. Averaging proves (3).

This bounds reaction per multiplier mass. It does not bound an individual
multiplier away from zero.

## 4. A subunit pair forces two strict near-unit source pairs

Suppose $`\rho_{pn}<1`$. For $`D\ge2`$ the four endpoints are distinct.
In the bisector coordinates of Section 2, $`S\le\rho_{pn}<1`$. Put

```math
\ell_D=D-\sqrt{D^2-1},\quad
\epsilon_D=1-\sqrt{1-\ell_D^2},\quad
\eta_D=\sqrt{1+4\epsilon_D}.
```

Equation (1) gives $`|a|\le\ell_D`$. Unit separation in (2) gives

```math
|b|\le S-\sqrt{1-a^2}\le\epsilon_D.
```

Both corresponding-end pairs therefore have lengths at most
$`\sqrt{\ell_D^2+(1+\epsilon_D)^2}=\eta_D`$. In physical notation these are

```math
X=L_b-L_a,\qquad Y=U_b-U_a. \tag{5}
```

Neither can be a unit contact in the exact train-cut model. Every unit contact
joining different retained layers is an edge crossed by a retained train cut,
and has vector $`u`$ in the increasing-layer orientation. If, for instance,
$`X=u`$, then $`Y=r_p+r_n-u`$. With $`T=r_p+r_n`$, unit separation of $`Y`$
implies $`|T|^2\ge2T\cdot u`$. Substitution into (4) gives

```math
D\sin(\delta/2)\ge\cos((\theta-\psi)/2),\quad \rho_{pn}\ge1,
```

a contradiction. The same argument applies to $`Y=u`$. Thus

```math
\boxed{1<|X|,|Y|\le\eta_D=1+\frac1{4D^2}+O(D^{-4}).} \tag{6}
```

These are two originally inactive **actual source pairs**, not scaffolds.
For a simple bound, $`\eta_D\le1+2/D^2`$ for $`D\ge2`$, using
$`\ell_D\le1/D`$ and $`\epsilon_D\le\ell_D^2`$.
Also at least one of the other two, opposite-end pair distances is
$`\ge C\ge D-\ell_D`$: their squared distances are
$`(a\pm C)^2+b^2`$, whose maximum is at least (C^2).
It is either an actual diameter or an (O(D^{-1}))-near-diameter pair.

## 5. Short diameter-endpoint chords are full-source hull sides

Let a finite unit-separated diameter-$`D`$ source lie in a radius-$`R<D`$ disk
with center $`o`$. Put $`r_0=D-R>0`$. For actual diameter endpoints (x,y)
of separation $`s<2r_0`$, set

```math
\alpha=\arccos(r_0/R),\qquad
\gamma=2\arcsin(s/(2r_0)),\qquad \Delta=2\alpha+\gamma.
```

If $`\Delta<\pi/2`$ and $`s<2\cos(\Delta/2)`$, then (xy) is a side of the
convex hull of the **entire source**.

Proof: a diameter partner (x') gives an outward supporting unit normal
$`n_x=(x-x')/D`$, since $`n_x\cdot(p-x)\le-|p-x|^2/(2D)`$ for every source
point $`p\ne x`$. Also $`|x-o|\ge r_0`$ and

```math
(x-o)\cdot n_x
=\frac{|x-o|^2+D^2-|x'-o|^2}{2D}\ge r_0.
```

Thus the angle of $`n_x`$ from the radial direction at $`x`$ is at most
$`\alpha`$. The radial directions at (x,y) differ by at most $`\gamma`$.
Their chosen supporting normals differ by at most $`\Delta`$, and satisfy
$`n_x\cdot(y-x)<0<n_y\cdot(y-x)`$. Since $`\Delta<\pi/2`$, they bound a
triangle on the exterior side of the chord. Its base is (xy), its apex height
is at most $`(s/2)\tan(\Delta/2)`$, and its projection onto the chord lies in
the base segment. These follow from the two base angles $`v,w>0`$,
$`v+w\le\Delta`$, and $`\cot v+\cot w\ge2\cot((v+w)/2)`$.
Any point in this triangle is within $`s/[2\cos(\Delta/2)]<1`$ of one of
(x,y). Unit separation excludes every other source point on that side of
the chord. Therefore (xy) is a hull side. All source points were retained.

In particular, canonical FS.1 implies the explicit consequence

```math
\boxed{D\ge512,\quad s\le3/2
\quad\Longrightarrow\quad xy\text{ is a full-source hull side}.} \tag{7}
```

Indeed, $`3^{1/4}/\sqrt D<1/16`$, so take $`R<9D/16`$, $`r_0>7D/16`$.
Then $`\cos\alpha>7/9`$, $`\sin\alpha<6/9`$, and
$`t=s/(2r_0)<12/(7D)<1/256`$. Hence

```math
\cos(\Delta/2)\ge(7/9)\sqrt{1-t^2}-(6/9)t
>\frac{1779}{2304}>\frac34.
```

This also gives $`\Delta<\pi/2`$. The condition for (7) follows.
Unlike the canonical loaded-unit-chord theorem, (7) concerns near-unit chords,
the full source hull, and also the macroscopic-container branch.

## 6. Only the adjacent pivot packet can be weak

Assume the conditional threshold staircase source is a global minimizer with
$`D\ge512`$. If $`R_e<B_e`$, some pair in its convex-average decomposition
has $`\rho_{pn}<1`$. Its two source pairs in (5) are hull sides by (6)--(7).

If $`b-a\ge2`$, an intermediate layer $`j`$ has a diameter endpoint on each
hull arc. Monotone layer order places that endpoint strictly between the
corresponding endpoints of (5), contradicting the hull-side conclusion.
Thus $`b-a=1`$. Every tree interval contains the common retained cut $`r`$, so

```math
\boxed{R_e<B_e\ \Longrightarrow\ e=\{r-1,r\}.} \tag{8}
```

Moreover, the only possible pair with $`\rho_{pn}<1`$ consists of the four
vertices bounding the two hull sides across this adjacent pivot layer gap.
There is at most one such positive/negative row pair: the side containing each
arc's layer transition is unique, and its four endpoints determine the bars.

Let $e_*\$ be that pivot edge and put $`B_*=0`$ if no weak packet occurs.
Then the exact peak pressure obeys

```math
A_r=\beta_0D+\sum_eR_e
\ge\beta_0D+\sum_eB_e-(1-g_D)B_*.
\tag{9}
```

No lower bound on the individual $`B_e`$, and no feasible diameter-decreasing
motion, is inferred. The new structural information is that distributed
subunit reactions are impossible: all such behavior is confined to one actual
four-endpoint pivot with two strictly inactive near-unit hull sides.

## 6b. The weak pivot has no crossing contact ports at its four endpoints

The subunit pair also satisfies the exact estimates

```math
|X-u|^2,|Y-u|^2<8/D^2. \tag{10}
```

To check them, write the two same-arc vectors as $`X=Sw+t`$ and $`Y=Sw-t`$,
where $`w`$ is a unit vector, the angle from $`w`$ to $`u`$ is
$`(\theta-\psi)/2`$, and $`t`$ has components bounded by $`\ell_D`$ along the
diameter-vector bisector and $`\epsilon_D`$ perpendicular to it. Formula (4)
and $`\rho<1`$ give $`\cos((\theta-\psi)/2)>S\ge g_D`$ and
$`|\sin((\theta-\psi)/2)|<1/(2D)`$. Thus

```math
X\cdot u,Y\cdot u
\ge g_D^2-\ell_D/(2D)-\epsilon_D
\ge1-7/(4D^2).
```

Use $`|X|^2,|Y|^2\le1+4\epsilon_D`$ and $`\epsilon_D\le D^{-2}`$ to get
(10). For $`D\ge3`$, a source point at $`L_a+u`$ would be within distance
$`\sqrt8/D<1`$ of $`L_b`$, and a point at $`L_b-u`$ would be within that distance
of $`L_a`$. The same holds for $`U_a,U_b`$. Strict inactivity of the short pairs
ensures these hypothetical points do not coincide with the blocking vertices.

Every unit contact crossing the pivot cut has vector $`u`$ from its lower to
its higher layer. Therefore **none of the four weak-pair endpoints is incident
to a unit contact crossed by the pivot train**. The proof uses actual source
separation and the exact cut law. It does not identify diameter endpoints with
train terminals. It forces their positive load, if any, to be transmitted
through other contacts and actual vertices before reaching a crossing port.

## 7. Sharp regression and the failed stronger assertion

For $`D\ge3`$, put $`k=\sqrt{1-1/(4D^2)}`$, $`C=D-1/(2D)`$, $`a=1/(2D)`$,
and take

```math
L_a=(-k/2,-C/2),\ U_b=(k/2,C/2),\quad
U_a=(-k/2,C/2+a),\ L_b=(k/2,-C/2+a),
```

together with $`z=(-D/2,a/2)`$, $`w=(D/2,a/2)`$. The four actual diameter
edges are (L_aU_b,U_aL_b,L_aU_a,zw). The two short same-arc pairs have
length exactly one; the remaining vertical pair has length (D-1/D).
The reference-to-rectangle distances lie strictly between one and $`D`$.
Equal positive weights on the paired bars give normalized axial reaction $`k`$,
attaining (3). Its two unit contacts are oblique to $`u`$, so it lacks the
exact train-cut hypothesis. It is not a global minimizer or a KKT source.

There is also a strict-slack family. Keep the same formulas for the four points
but use $`k^2=1-1/(8D^2)`$, $`C=\sqrt{D^2-k^2}`$, $`a=1/(4D)`$.
For $`D\ge3`$, both short pairs have square $`1-1/(16D^2)<1`$, so **this
tempting choice fails unit separation and is rejected**. A valid replacement
uses $`a=1/(2D)-1/(8D^3)`$: both short squares are strictly greater than one,
and $`C+a<D`$. The only actual diameters are the two paired bars and (zw),
all other pairs are strict. Nevertheless $`R_e/B_e=k<1`$, and the extra long
pair is within (O(D^{-3})) of diameter activity. This kills an attempted
extension of (8) to exclude even the adjacent pivot by endpoint geometry and
strict slack alone. It omits actual contact trains, positive full KKT
equilibrium, global optimality, and a full near-disk source population.

## 8. Certificates, remaining gap, and scope audit

[The exact verifier](../../../research/verify_threshold_packet_reaction_2026_10_02.py)
checks polynomial/radical identities, the full 15 pair distances for the sharp
and strict-slack six-point examples, their contact/diameter graphs, the rejected
choice, 24 hypothetical-port distances, and the rational constants in (7).
The analytic general lemmas are not
proved by bounded numerical survival. No external literature was imported.

The next precise obligation is to use actual train face closure and positive
full-source equilibrium to exclude or finitely release the adjacent pivot in
(8), while also controlling the packets with $`R_e\ge B_e`$. The strict-slack
example shows exactly which missing source hypotheses matter; arbitrarily
small inactive gaps cannot be relabeled as contacts.

Open-cell exact phase, nonconstant phase, split-star O--O, inactive interfaces,
macroscopic inactive containers/exterior caps, and other higher-surplus
full-core sources remain open. No lifecycle promotion or canonical state
change is made. This report has full proofs for the new bridge, not a Level I
solution.
