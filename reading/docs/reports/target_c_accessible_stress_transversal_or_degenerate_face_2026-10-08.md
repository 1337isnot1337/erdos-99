> Generated reading edition · [exact source](../../../docs/reports/target_c_accessible_stress_transversal_or_degenerate_face_2026-10-08.md) · source SHA-256 `ea2cec250f35fc49ad477af1a62a343f2555ca7edfdd46b5b1a191d76d4059cc`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C2AF91A93C57","canonical":true,"claim_ids":["C-ACCESSIBLE-STRESS-FACE-DICHOTOMY","C-SEVEN-SITE-TAGGED-STRESS-MASS-REGRESSION"],"claim_statuses":{"C-ACCESSIBLE-STRESS-FACE-DICHOTOMY":"canonical","C-SEVEN-SITE-TAGGED-STRESS-MASS-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C: accessible stress transversals or a degenerate exceptional face

Date: 2026-10-08.
Run base: `9029db9a`.
Canonical base: `2010296d3c00903423b67d96d70ae369d56b9e26`.
State: `2026-10-08.audit.147`.
Independent Audit.170 disposition: the finite stress-face dichotomy is canonical;
the seven-site mass example is a regression; the grid-access specialization remains
conditional on the separate unreviewed uniform-cell candidate. C-II and Level I remain open.

## 1. Exact implication to the finite-source gate

The question is whether actual grid-accessible loaded vertices can be
chosen as the stress-killing deletion, rather than obtaining a deletion
with no relation to the source grids.

    supplied accessible loaded set W
      -> either a stress transversal U inside W with |U|<=s_Z+1
      -> canonical strict motion of the reduced full source
      -> Level I only if a verified packet restores |U| labels;

    or an exceptional stress face
      -> every extreme circuit of that face has a large explicit
         bar-flex deficiency
      -> Level I only after a whole-source completion contradiction.

Neither last arrow is proved here. An accessible contact path is not
refill capacity, and a selected bar flex is not a feasible full-source
motion.

For the transversal step one does not need a uniform lower bound on
KKT mass at accessible vertices. The exact question is whether a
normalized stress can have zero mass at all of them.

## 2. Canonical source and the accessible set

Use the canonical contact-minimal, then diameter-pair-minimal
triangle-free source with `D>=9`, `C=C_*` and `H=H_*`.
Retain every source label, including contact isolates.
Let `P` be the normalized nonnegative KKT stress polytope.
Canonical [Section 64](../targets/target-c/64-extreme-circuit-transfer-audit.md)
gives compactness and

```math
\dim_{\rm aff}P=s_Z.
\tag{AT1}
```

Let `W subset B` be any supplied set of actual loaded vertices.
In the intended application each `b in W` has a certified short
actual contact path to a nearby same-component complete grid. The
finite theorem needs only the set `W`, not that additional geometry.
Define

```math
f_b(\alpha,\beta)=\sum_{e\in H:e\ni b}\beta_e,\qquad
F_b=P\cap\{f_b=0\},\qquad
P_0=\bigcap_{b\in W}F_b.
\tag{AT2}
```

Each `f_b` is affine and nonnegative on `P`, so `F_b` and `P_0`
are exposed faces, possibly empty. Put

```math
E_0=H[B\setminus W],\qquad b_0=|E_0|.
\tag{AT3}
```

Every stress in `P_0` has its positive diameter support in `E_0`.
This uses all actual source diameter pairs, not a selected substitute.

## 3. Empty exceptional face gives a small accessible deletion

Suppose `P_0` is empty. Apply finite Helly in the affine hull of `P`
to the faces `F_b`. There is `U subset W` with

```math
\boxed{|U|\le s_Z+1,\qquad \bigcap_{b\in U}F_b=\varnothing.}
\tag{AT4}
```

Thus every normalized source stress has positive diameter reaction
incident to some deleted `b in U`. At a loaded exposed hull vertex,
zero diameter reaction would force every contact reaction there to
be zero by the strict supporting-functional argument. Consequently
restriction and zero extension identify surviving stresses with
source stresses avoiding `U`. No surviving normalized stress exists.

Canonical [Audit.87](../audits/target_c_contact_opening_transversal_independent_audit_2026-10-07.md)
then gives a velocity on all retained source labels that strictly
opens every surviving actual unit contact and strictly shortens
every surviving old-`D` pair. A sufficiently small straight step
preserves all inactive pairs and has diameter strictly below `D`.
All contact isolates remain in this reduced source.

The reduced source must be nonempty, as required by Audit.87. This
is automatic in the Type-II grid application because deletion is
confined to `B` and quadratic unloaded populations remain. Otherwise
nonemptiness is an explicit finite hypothesis.

Compactness also gives a positive source-dependent minimum of
`sum_{b in W}f_b`. There is no uniform asymptotic lower bound claimed.
For the finite transversal and strict-motion conclusion the positive
minimum is not needed: emptiness of `P_0` already suffices.

This strengthens where the deletion can be selected. It does not
strengthen its size beyond `s_Z+1` and does not restore cardinality.

## 4. Nonempty exceptional face forces a large circuit defect

Suppose `P_0` is nonempty and `1<=b_0<=D`. Every extreme point of
this exposed face is an extreme point of `P`. Choose any such point,
and write `h_*,e_*,v_*,sigma_*` as in Section 64. Then

```math
h_*\le b_0,\qquad
\sigma_*=2v_*-2-(e_*+h_*),\qquad
\operatorname{rank}R_*=e_*+h_*-1.
\tag{AT5}
```

Thus its velocity kernel has dimension `3+sigma_*`, and
`sigma_*` is the excess over Euclidean motions.

Canonical equation (64.10), with `Q_*>=0`, gives

```math
\sigma_*\ge
D\cos((h_*-1)a_D)-{h_*+1\over2},
\qquad a_D=\arcsin{1\over2D}.
\tag{AT6}
```

The right side decreases with `h_*` on `1<=h_*<=b_0<=D`.
Therefore every extreme circuit in the exceptional face satisfies

```math
\boxed{\sigma_*\ge
D\cos((b_0-1)a_D)-{b_0+1\over2}.}
\tag{AT7}
```

If `b_0<=eta D` with fixed `0<eta<1`, this implies

```math
\liminf{\sigma_*\over D}\ge\cos(\eta/2)-\eta/2.
\tag{AT8}
```

If `b_0=o(D)`, the lower bound is `(1-o(1))D`.
For a completely rational weaker bound, `a_D<=1/D` and
`cos x>=1-x^2/2` give

```math
\sigma_*\ge D-{(b_0-1)^2\over2D}-{b_0+1\over2}.
\tag{AT9}
```

Canonical excess degeneracy is
`kappa_*=2(v-v_*)+sigma_*>=sigma_*`.
Hence an exceptional stress cannot be dismissed by the low-degeneracy
extreme-transfer theorem. Its bar-flex defect alone is already linear,
whether or not it omits many source-core vertices.

These are selected-support statements. Omitted actual contact and
diameter rows still constrain the full source. No selected flex is
extended across them.

## 5. Conditional use of the actual grid-access candidate

The unreviewed
the separate unreviewed uniform-cell and global diameter-access candidate
supplies, in Type II and for fixed `lambda,eta>0`, actual accessible
vertices `W` such that fewer than `eta D` actual diameter edges fail
to have both endpoints in `W`. In particular `b_0<=eta D`.

If that candidate's analytic theorem is accepted under its full
hypotheses, the present dichotomy gives:

- an accessible loaded stress transversal of at most `s_Z+1` labels,
  each with an actual short contact route to a nearby complete grid;
- or an exceptional face whose every extreme circuit has the explicit
  near-linear defect AT7–AT8.

No premise from that candidate is declared canonical. The finite
Helly/stress-face theorem itself is independent of grid extraction.
Taking `eta` small does not prove which alternative occurs. Even
in the first alternative the grids and paths can overlap and give
no independent refill capacity.

## 6. Exact seven-site regression against generic mass inheritance

Take the six vertices `p_j=(cos(j pi/3),sin(j pi/3))` of the unit
regular hexagon and its center. The complete actual contact set is
the six perimeter edges and six spokes. The complete diameter set
is the three opposite pairs, all at `D=2`. This fixture contains
six unit triangles; no global-optimality certificate is claimed.
It is not a triangle-free canonical-source counterexample.

Every normalized nonnegative equilibrium stress has one common
perimeter weight `c` and opposite-equal spoke weights
`alpha_j=2 beta_j-c`, where

```math
\beta_0+\beta_1+\beta_2=1,\qquad
0\le c\le2\min_j\beta_j.
\tag{AT10}
```

The complete stress polytope is a tetrahedron. Its vertices are the
three straight-diameter stresses with `beta_i=1,c=0`, and the
perimeter stress with `beta_j=1/3,c=2/3`. Barycentric coordinates are
`w_j=beta_j-c/2` and `w_P=3c/2`.

All four stress matrices are PSD. The straight-diameter matrices have
rank one and energy `(z_i+z_{i+3}-2z_center)^2`. The perimeter
matrix has rank three and, on the six outer coordinates, is twice
the orthogonal projection off `span{1,P_x,P_y}`. Any relative-interior
mixture has rank four and exactly the three affine scalar kernel modes.
The complete mixed rigidity rank is eleven, so `s_Z=3`.

Tag the endpoints of the other two diameter pairs as `W`. The
straight stress on the remaining pair lies in `P_0`. For mixture
weights `(1-3epsilon,epsilon,epsilon,epsilon)`, all actual contact
and diameter multipliers are positive, the scalar affine kernel is
exact, and the untagged pair carries mass `1-8epsilon/3`.
That mass tends to one.

Thus full relative-interior support and a maximal-rank PSD affine
kernel do not by themselves force coverage or mass on a prescribed
tagged set. The missing inference must use triangle-free source
geometry or whole-source optimality. This finite example is not an
asymptotic counterexample to the grid-access candidate.

## 7. Certificate scope and remaining obligation

The exact checker reconstructs all seven-site pairs, the complete
four-vertex stress polytope, all equilibria, PSD and rigidity ranks,
and the mass-concentrating relative-interior samples. It also checks
small simplex/cube face covers and rational AT9 arithmetic.
Those polytopes are abstract checks, not planar-source models.

The analytic proofs are Sections 2–4. Computation does not establish
the grid-access premise, eliminate the exceptional face, construct a
refill packet, or prove global optimality. Both C-II branches and
the full Level I objective remain open.
