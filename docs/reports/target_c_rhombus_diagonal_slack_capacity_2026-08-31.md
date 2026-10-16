<!-- theorem-state: {"artifact_id":"ART-781BB2082B0D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C75: rhombus diagonal-slack capacity

**Date:** 2026-08-31  
**Repository base:** `a76a3175` (main after C74 / PR #78)  
**Run type:** exact geometric capacity refinement  
**Target:** Target C Gate C-II, weight-free transverse geometry  
**Depends on:** C42 quadrangulation defect, C49 two-scale strict-rhombus capacity, C73 degree-four rhombic bulk  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C72-C74 show that one chosen KKT certificate can concentrate almost all stress on an
almost-radial carrier while geometrically essential transverse contacts remain
arbitrarily light. A closing argument therefore needs a weight-free geometric currency.

C75 refines C49's strict-rhombus area charge. C49 used only

\[
\operatorname{area}(f)>\frac{\sqrt3}{2}
\]

for every bounded quadrilateral contact face. C75 measures the amount of strictness.
If `s_f>1` is the short diagonal of a strict unit rhombus, then

\[
\operatorname{area}(f)-\frac{\sqrt3}{2}
\ge c_{\rm rh}(s_f-1),
\]

with an explicit universal constant

\[
c_{\rm rh}:=
\frac{1-\sqrt3/2}{\sqrt2-1}
=0.32344\ldots .
\]

Summing over the `m-O(D)` rhombic faces gives an exact core-capacity penalty
proportional to the total missing-diagonal slack, with no KKT weights.

---

## 1. Exact unit-rhombus area as a function of its short diagonal

Let `f` be a unit rhombus. Let `s` be the length of its shorter diagonal. Then

\[
1<s\le\sqrt2
\tag{C75.1}
\]

for a strict triangle-free contact face: `s=1` would be a unit diagonal contact and
split the face into contact triangles.

The two diagonals of a rhombus are perpendicular and satisfy

\[
s^2+\ell^2=4.
\]

Hence

\[
\boxed{
A(s):=\operatorname{area}(f)
=\frac12s\sqrt{4-s^2}.
}
\tag{C75.2}
\]

At the two endpoints,

\[
A(1)=\frac{\sqrt3}{2},
\qquad
A(\sqrt2)=1.
\tag{C75.3}
\]

A direct differentiation gives

\[
A'(s)=\frac{2-s^2}{\sqrt{4-s^2}},
\]

and

\[
A''(s)=
\frac{s(s^2-6)}{(4-s^2)^{3/2}}<0
\qquad(1\le s\le\sqrt2).
\tag{C75.4}
\]

Thus `A` is strictly concave on the full admissible interval.

A concave function lies above the chord joining its endpoint values. Therefore

### Lemma C75.1 — linear short-diagonal area charge

For every strict unit rhombus with short diagonal `s`,

\[
\boxed{
A(s)
\ge
\frac{\sqrt3}{2}
+c_{\rm rh}(s-1),
}
\tag{C75.5}
\]

where

\[
\boxed{
c_{\rm rh}
:=
\frac{1-\sqrt3/2}{\sqrt2-1}
=0.32344\ldots .}
\tag{C75.6}
\]

Equality in the chord bound occurs only at `s=1` or `s=sqrt(2)`; the contact-face
regime has `s>1`.

---

## 2. Sum the charge over the C42 rhombic bulk

Let `F_4` be the set of bounded quadrilateral contact faces and write, by abuse of
notation, `F_4:=|F_4|` for its cardinality when no ambiguity arises. Define the total
short-diagonal slack

\[
\boxed{
\Sigma_{\rm diag}
:=
\sum_{f\in F_4}(s_f-1)>0.
}
\tag{C75.7}
\]

The interiors of bounded plane-graph faces are disjoint and lie in the force hull `F`.
Hence Lemma C75.1 gives

\[
\operatorname{area}(F)
\ge
\sum_{f\in F_4}\operatorname{area}(f)
\ge
\frac{\sqrt3}{2}F_4
+c_{\rm rh}\Sigma_{\rm diag}.
\tag{C75.8}
\]

Therefore

\[
\boxed{
F_4
\le
\frac{2}{\sqrt3}\operatorname{area}(F)
-\lambda_{\rm rh}\Sigma_{\rm diag},
}
\tag{C75.9}
\]

where

\[
\boxed{
\lambda_{\rm rh}
:=\frac{2c_{\rm rh}}{\sqrt3}
=0.37348\ldots .}
\tag{C75.10}
\]

This is the quantitative version of C49's whole-hull strict-rhombus charge.

---

## 3. Insert the exact C42 face-count defect

Use the standard C-II notation:

- `m`: force-visible contact-core population;
- `q=|B|`: loaded boundary count;
- `c_I`: number of unpinned components after deleting `B`;
- `e_BB`: number of loaded-loaded contacts.

C42 gives

\[
F_4
\ge
m-5q+3c_I+3e_{BB}+5.
\tag{C75.11}
\]

Equivalently,

\[
m\le F_4+5q-3c_I-3e_{BB}-5.
\tag{C75.12}
\]

Substitute C75.9.

### Theorem C75 — diagonal-slack core-capacity theorem

In fully force-visible C-II,

\[
\boxed{
 m
\le
\frac{2}{\sqrt3}\operatorname{area}(F)
-\lambda_{\rm rh}\Sigma_{\rm diag}
+5q-3c_I-3e_{BB}-5.
}
\tag{C75.13}
\]

Using the isodiametric inequality and `q<=pi D`,

\[
\boxed{
 m
\le
\Delta_2D^2
-\lambda_{\rm rh}\Sigma_{\rm diag}
+5\pi D-3c_I-3e_{BB}-5,
}
\tag{C75.14}
\]

where

\[
\Delta_2:=\frac{\pi}{2\sqrt3}.
\]

C75.14 strictly refines the whole-hull member of C49 by retaining the complete
short-diagonal slack of every quadrilateral contact face.

---

## 4. Fixed-threshold version

For `tau in (0,sqrt(2)-1]`, let

\[
N_\tau
:=
|\{f\in F_4:s_f\ge1+\tau\}|.
\tag{C75.15}
\]

Then

\[
\Sigma_{\rm diag}\ge\tau N_\tau.
\]

Hence C75 immediately gives

### Corollary C75.1 — faces bounded away from a missing unit diagonal

\[
\boxed{
 m
\le
\Delta_2D^2
-\lambda_{\rm rh}\tau N_\tau
+5\pi D-3c_I-3e_{BB}-5.
}
\tag{C75.16}
\]

Thus a positive fraction of rhombi whose short diagonals stay a fixed amount above
one creates a genuine quadratic capacity deficit.

Conversely, if a sequence of force-visible cores satisfies

\[
m\ge\Delta_2D^2-CD
\tag{C75.17}
\]

for some fixed `C`, then C75.14 implies

\[
\boxed{
\Sigma_{\rm diag}=O(D),
}
\tag{C75.18}
\]

and, for every fixed `tau>0`,

\[
\boxed{N_\tau=O_\tau(D).}
\tag{C75.19}
\]

So a near-capacity quadratic core must have all but `O(D)` of its `Theta(D^2)`
rhombic faces with short diagonal below `1+tau`, for every fixed `tau`.

More generally, for any scale `tau_D>0`,

\[
N_{\tau_D}=O(D/\tau_D)
\tag{C75.20}
\]

under C75.17. For example `tau_D=D^{-1/2}` leaves only `O(D^{3/2})=o(D^2)` rhombi
outside the `1+D^{-1/2}` missing-diagonal regime.

---

## 5. Interaction with C73: a near-triangular missing-diagonal vertex bulk

C73 says all but `O(D)` force-core vertices are interior degree-four vertices incident
to four strict rhombi.

Under the near-capacity hypothesis C75.17, fix `tau>0`. Only `O_tau(D)` rhombi have
short diagonal at least `1+tau`. Each such face has four corners, so only `O_tau(D)`
additional vertices can be incident to one of those faces.

Therefore all but `O_tau(D)` force-core vertices have the following local structure:

- contact degree exactly four;
- four incident strict unit rhombi; and
- every one of those rhombi has a missing short diagonal in
  \[
  (1,1+\tau).
  \]

Thus the weight-free alternative to the C68-C74 anisotropic stress phase is not an
arbitrary rhombic mesh. A near-capacity core is forced into a **near-triangular
missing-diagonal bulk**: quadrilateral faces are almost split by an additional unit
contact, but remain strictly triangle-free.

This is exactly the geometric regime in which a future perturbation, stability, or
source-capacity theorem should work.

---

## 6. Why this is a second resource

C68-C74 use a chosen normalized KKT stress. They cannot charge contacts whose alpha
weights are tiny.

C75 does not use `alpha` or `beta` at all after the structural C42 face count. The
quantity

\[
\Sigma_{\rm diag}
\]

is purely geometric. A transverse rhombic face pays capacity according to how far its
missing diagonal is from becoming a new unit contact, regardless of how little stress
that face carries in the chosen certificate.

Therefore C75 gives the first direct weight-free quantitative complement to the
near-zero radial-carrier stack.

---

## 7. What remains

C75 does not by itself prove that the force-visible core has near-maximal population.
The old force-bulk gap remains: fully inactive rattlers can make `n-m` large.

The theorem sharpens that gap into a clean dichotomy.

1. **Core-capacity loss:** if `Sigma_diag` is large, the force-visible core loses an
   explicit amount of capacity.
2. **Near-triangular rhombic bulk:** if the core is near capacity, almost every rhombus
   has a missing diagonal at distance `1+o(1)`.

A full Target C closure can now attack either side by proving:

- `n-m=O(D)` or another force-bulk transfer estimate, so C75 applies to the whole
  source at boundary scale; or
- a perturbation/stability theorem showing that an `m-O(D)` family of unit rhombi with
  missing diagonals `1+o(1)` cannot occur in a contact-minimal globally
  diameter-minimizing triangle-free source.

The second route is a concrete bridge toward the finite-release machinery rather than
a generic density statement.

---

## 8. Regression audit

- Oblique rhombic grids with angles tending to 60 degrees are allowed; their diagonal
  slack tends to zero, exactly as C75 requires.
- A square grid pays a fixed positive area/slack charge per face and therefore a
  leading-order core-capacity loss.
- No uniform rhombus area gap is claimed.
- The short diagonal, not the long diagonal, is charged. The long diagonal may be
  close to `sqrt(3)` and carries no near-contact information.
- Fully inactive rattlers are not counted by `m`; the force-bulk problem remains
  explicit.
- No KKT weight lower bound, lattice periodicity, or reciprocal embedding is assumed.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C75 unit-rhombus charge:
For short diagonal s in (1,sqrt(2)],
  area = (1/2)s sqrt(4-s^2)
and concavity gives
  area - sqrt(3)/2 >= c_rh (s-1),
  c_rh=(1-sqrt(3)/2)/(sqrt(2)-1)=0.32344...

Let Sigma_diag=sum_(4-faces)(s_f-1). Then C42 + disjoint face area gives
  m <= (2/sqrt(3))area(F)
       -lambda_rh Sigma_diag
       +5q-3c_I-3e_BB-5,
  lambda_rh=2c_rh/sqrt(3)=0.37348...
and hence
  m <= Delta_2 D^2 -lambda_rh Sigma_diag +5pi D-...

If m>=Delta_2D^2-O(D), then Sigma_diag=O(D), so for every fixed tau>0 only O_tau(D)
rhombi have short diagonal >=1+tau. With C73, almost every core vertex is therefore
surrounded by four strict rhombi whose missing diagonals are arbitrarily near unit.

Next: force-bulk transfer, or a perturbation/stability theorem for this near-triangular
missing-diagonal bulk.
```
