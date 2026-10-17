> Generated reading edition · [exact source](../../../docs/audits/target_c_sections100_101_promotion_audit_2026-09-12.md) · source SHA-256 `a2446e2eb9cf6635f597aecac6acdba24c3f65938776c7136316e4c3b8e97e3d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-83935F63EF37","canonical":true,"claim_ids":["C-WRAP-COMPLEMENT-CHORD"],"claim_statuses":{"C-WRAP-COMPLEMENT-CHORD":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Section 101 promotion audit with Section 100 dependency recheck

**Date:** 2026-09-12
**Verdict:** **PASS after one finite-to-limit repair in Section 101.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit rechecks canonical Section 100 as a dependency and independently audits
Section 101 complement-gap chord theorem before theorem-state promotion.  The Section
100 hostile audit already supplied an independent paired-piece proof.  The new work
here is a dependency audit of that result, a hostile re-check of Section 101, and a
repair of one finite-gap sentence whose intended conclusion is valid but whose written
justification was too weak.

The promoted conclusions are

```math
|S|\le 3\theta-2\pi,
\qquad
2\alpha\le |S|,
```

and, for every wrapping Type-II harmonic-cell limit,

```math
\sin(\theta/2)+2\sin\theta\le 3\theta-2\pi,
```

hence

```math
\boxed{
\lambda\ge \mu_8
=0.9760407652670519821\ldots .
}
```

The usual cap-family transfer then yields an actual macroscopic locally
rhombic-saturated harmonic carrier with

```math
\operatorname{diam}(P_*)\ge(\mu_8-o(1))D.
```

No claim here closes C-II or Erdős Problem #99.

---

## 1. Section 100: independent support-measure certification

Let `S` be a compact wrapping subset of the radius-`1/2` circle with pairwise minor
angular diameter at most `theta<pi`.  Write the three Section-88/94 anchor gaps as
`g_i` and `delta_i=theta-g_i`; the six allowed support pieces have paired lengths
`delta_1,delta_1,delta_2,delta_2,delta_3,delta_3`.

For the two pieces paired across anchor gap `g_i`, parameterize compact subsets
`A_i,B_i subset [0,delta_i]`.  If `a in A_i` and `b in B_i`, the circular minor-angle
condition keeps both alternatives

```math
a+b\le\delta_i
\quad\hbox{or}\quad
a+b\ge\delta_i+\phi,
\qquad
\phi=2\pi-2\theta.
```

Reflect `B_i` by `C_i=delta_i-B_i`.  Then

```math
(A_i-C_i)\cap(0,\phi)=\varnothing.
```

For every fixed `0<t<phi`, the sets `A_i` and `C_i+t` are disjoint and lie in an
interval of length `delta_i+t`, so

```math
|A_i|+|B_i|\le\delta_i+t.
```

Letting `t` decrease to zero and summing the three pairs gives

```math
\boxed{|S|\le\sum_i\delta_i=3\theta-2\pi.}
```

This is the same conclusion as the existing Section-100 hostile audit but uses the
paired-piece translation argument rather than relying on the original antipodal-
neighborhood presentation.

For the finite attachment sets, fix an open finite interval cover `U` of `S`.  Hausdorff
convergence puts all attachment angles in `U` for large `D`; the canonical near-circle
boundary packing estimate gives

```math
a_D\le\left({|U|\over2}+o(1)\right)D+O_U(1).
```

Outer regularity followed by `D->infinity` therefore gives

```math
\boxed{2\alpha\le |S|\le3\theta-2\pi.}
```

Combining this with canonical Section 96,
`alpha>=(3/2)sin(theta)`, reproduces the Section-100 scalar threshold
`0.9642670742838973...`.  The certificate
`research/verify_target_c_paired_six_cluster_density.py` protects that arithmetic.

**Section-100 verdict:** PASS.

---

## 2. Section 101 gap optimization: retain the support measure `m`

Put

```math
m:=|S|,
\qquad
\phi:=2\pi-2\theta,
\qquad
M:=3\theta-2\pi.
```

Write the connected components of the complement as angular gaps `gamma_j`.  The
canonical wrapping geometry and Section 100 give

```math
0<\gamma_j\le\theta,
\qquad
\sum_j\gamma_j=2\pi-m,
\qquad
m\le M,
```

and at least three distinct gaps satisfy `gamma_j>=phi`.

The report proves the sharp specialization at `m=M`.  A slightly stronger formulation
is useful for auditing the monotonic step.  Since `m<=M`,

```math
\theta-m\ge\theta-M=\phi.
```

For fixed `m`, the vector

```math
(\theta,\theta-m,\phi,0,0,\ldots)
```

has the correct total mass `2pi-m`, every positive entry lies in `[phi,theta]`, and it
majorizes every feasible complement-gap vector: the largest gap is at most `theta`,
and the sum of the two largest is at most total mass minus the required third gap
`phi`, namely `2theta-m`.

Because

```math
f(x)=\sin(x/2)
```

is increasing and strictly concave on `[0,theta]`, Karamata/majorization gives

```math
\boxed{
\sum_j\sin(\gamma_j/2)
\ge
\sin(\theta/2)
+\sin((\theta-m)/2)
+\sin\theta.
}
\tag{A.1}
```

The countable case follows by taking finite subfamilies containing the three protected
gaps and exhausting the total complementary measure.  No infinite outer-walk sum is
used before passing through finite subfamilies.

This two-variable form is stronger than the scalar statement recorded in Section 101
and will be retained as canonical auxiliary structure.

---

## 3. Finite-to-limit gap transfer: repair of the written Section-101 step

The only material audit defect is in the wording around original equations
(101.16)–(101.17).  The report writes only

```math
h_{j,D}\ge\gamma_j-o(1)
```

and then applies monotonicity of the chord function as though `h_{j,D}<pi` were already
known.  A cyclic gap larger than `pi` would invalidate that inference.

The intended stronger statement follows directly from Hausdorff convergence and fixes
the issue.

Fix one complementary component `G=(u,v)` of limiting angular length `gamma<pi`.
Because `u,v in S`, Hausdorff convergence supplies attachment angles
`u_D->u` and `v_D->v`.  Conversely, for every fixed compact subarc of `G`, Hausdorff
convergence implies that it contains no attachment for all sufficiently large `D`.
Choose the last attachment before the interior of `G` and the first attachment after
it.  Their angles converge to `u` and `v`; otherwise a subsequence would have a limit
point in the open complement.  Hence the corresponding consecutive cyclic attachment
gap satisfies

```math
\boxed{h_D=\gamma+o(1)<\pi.}
\tag{A.2}
```

For any fixed finite family of distinct limiting complement components these finite
gaps are distinct for all large `D`.  Type-II annular convergence then gives the
endpoint chord estimate

```math
\boxed{
|x_D-y_D|
\ge D\sin(\gamma/2)-o(D).
}
\tag{A.3}
```

Thus the Section-101 chord lower bound is correct after replacing the one-sided gap
statement by (A.2).  This is a repair of the proof text, not a change to the theorem.

---

## 4. Outer-walk ledger and the full complement chord currency

For any fixed finite family of limiting complement gaps, the corresponding outer-face
routes are distinct edge intervals of the Section-62 outer walk.  Each selected route
has length at least its endpoint chord.  Every unselected consecutive-attachment
interval contributes at least two edges unless it is a direct loaded-loaded polygon
side.

Using canonical Section 82,

```math
L_D+Q_D=4a_D-6-2s_D-2c_D,
```

and `c_D^partial<=c_D`, division by `D` gives, after the finite-family limit,

```math
2\alpha\ge
\sum_{j\in J_0}\sin(\gamma_j/2).
```

Exhaust the countable complement by finite subfamilies.  Monotone convergence yields

```math
\boxed{
2\alpha\ge\sum_j\sin(\gamma_j/2).
}
\tag{A.4}
```

All discarded local currencies have the favorable sign; no KKT coefficient floor or
unstated perimeter estimate enters this inequality.

Section 100 gives `2alpha<=m`, so (A.1) and (A.4) imply

```math
\boxed{
m\ge
\sin(\theta/2)+\sin((\theta-m)/2)+\sin\theta.
}
\tag{A.5}
```

Define

```math
H_\theta(m)
=m-\sin(\theta/2)-\sin((\theta-m)/2)-\sin\theta.
```

On the admissible interval,

```math
H_\theta'(m)=1+{1\over2}\cos((\theta-m)/2)>0.
```

Therefore the easiest admissible case is the largest support measure `m=M`.  Substituting
`M=3theta-2pi` and `theta-M=phi` into (A.5) gives exactly

```math
\boxed{
3\theta-2\pi
\ge
\sin(\theta/2)+2\sin\theta.
}
\tag{A.6}
```

---

## 5. Scalar threshold and actual-carrier transfer

Let

```math
F(\theta)=3\theta-2\pi-\sin(\theta/2)-2\sin\theta.
```

On `[2pi/3,pi)`,

```math
F'(\theta)=3-{1\over2}\cos(\theta/2)-2\cos\theta>0.
```

The unique zero is

```math
\theta_8=2.7029080296483676832\ldots,
\qquad
\mu_8=\sin(\theta_8/2)=0.9760407652670519821\ldots .
```

The certificate `research/verify_target_c_complement_chord_threshold.py` independently
checks the root, monotonicity, and the positive cap-capacity gap.  Hence every wrapping
Type-II harmonic-cell limit obeys

```math
\boxed{\lambda\ge\mu_8.}
```

For every fixed `mu<mu_8`, shorter macroscopic limits are cap type.  Canonical Section
88's cap-family capacity bound, the total harmonic-cell perimeter bound, and canonical
Section 83's summed `o(D^2)` rhombic deficit therefore select an actual macroscopic
locally rhombic-saturated cell with

```math
\boxed{
\operatorname{diam}(P_*)\ge(\mu_8-o(1))D.
}
```

The numerical cap gap at `mu_8` remains positive, so the diagonal passage is uniform.

**Section-101 verdict:** PASS after the finite-gap repair (A.2).

---

## 6. Endpoint consequences

At a sequence with `theta->theta_8`, every inequality in

```math
\sum_j\sin(\gamma_j/2)
\le2\alpha\le m\le M
```

must be asymptotically tight.  Consequently

```math
m\to M,
\qquad
2\alpha\to M,
```

and strict concavity in the majorization problem forces the macroscopic complement-gap
profile toward

```math
(\theta_8,\phi_8,\phi_8).
```

Equivalently, the limiting support is the sharp Section-100 model: one support arc of
length `M` together with two isolated wrapping anchor points.  The exact Section-82
ledger also forces

```math
s_D/D\to0,
\qquad c_D/D\to0,
\qquad Q_D/D\to0,
```

and saturation of (A.3) makes the three corresponding macroscopic outer-contact routes
asymptotically Euclidean-geodesic.  In particular the largest route has endpoint chord

```math
(\mu_8-o(1))D,
```

nearly the full global diameter.

This endpoint structure is auxiliary to the scalar threshold but is the more useful
next frontier: it must be coupled to the same carrier's quadratic near-rhombic interior
and Section-91 ordered train grid.

---

## 7. Dependency and scope audit

`C-WRAP-ANGULAR-MEASURE` uses canonical `C-HARMONIC-WRAPPING`,
`C-WRAP-THREE-GAP`, `C-WRAP-OUTER-WALK-GAP`, and `C-FULLCORE-NEAR-DISK`.

`C-WRAP-COMPLEMENT-CHORD` additionally uses canonical `C-ATTACH-CURRENCY`,
`C-HARMONIC-CARRIER-QUAD`, `C-HARMONIC-CELL-TILING`, and the promoted
`C-WRAP-ANGULAR-MEASURE`.

The proofs retain all source points.  They do not use the rejected
inward-pocket/exterior-Reuleaux-cap premise, a KKT coefficient floor, the conditional
Section-97/98 endpoint claims, or deletion of contact-isolated source points.

**Promotion recommendation:** promote Section 101 as `C-WRAP-COMPLEMENT-CHORD`.
Section 100 is already canonical under audit.40; Section 101 is valid with the explicit
finite-gap repair (A.2).  The live Type-II carrier threshold becomes `0.976040765267052...D`.
C-II remains open.
