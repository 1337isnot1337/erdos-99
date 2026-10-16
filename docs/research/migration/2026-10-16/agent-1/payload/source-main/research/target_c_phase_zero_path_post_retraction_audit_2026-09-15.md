# Post-retraction hostile audit — the phase-zero path does not use the retracted branch inference

**Date:** 2026-09-15
**Reviewed:**
- `research/target_c_dominant_oo_phase_zero_path_t1860_2026-09-15.md`
- `research/target_c_phase_zero_path_t1865_2026-09-15.md`
- main retractions `287d0d5b`, `27f0962a`, `103ddf29`, `a5507f70`
- repaired live opposite-branch theorem `target_c_opposite_branch_dual_path_t18593_2026-09-15.md`
- audited Sections 156--157 and `target_c_complement_outer_train_bracing_energy_hostile_audit_2026-09-15.md`

**Disposition:** **PASS.**  The phase-zero marker argument supplies the oriented-branch step missing from the retracted low-energy path theorems.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Main correctly retracted several path claims after identifying a precise logical gap:
from a projective endpoint-energy estimate alone, one cannot infer that the two outer
terminal positions use opposite oriented normal branches.  Both terminals may a priori
use the same oriented representative of one projective normal class.

The phase-zero path theorem is materially different.  It does not infer branch
orientation from endpoint energy.  Instead it applies the exact Section-157 two-sided
diameter-bracing theorem separately to the two Jordan shores of each O--O train.  This
forces a zero of the *oriented* transverse function into each complementary shore
normal arc.  After deleting terminals near the phase-zero set, the two arcs contain
**different** zeros, hence the two antipodal oriented representatives.

That is exactly the missing branch argument.

---

## 1. What the retracted path proofs did not prove

The retracted files bounded endpoint deviations using expressions of the form

\[
e_\tau\ge(1-\cos\alpha)+(1-\cos\beta)-o(1).
\]

This is a projective statement.  At the former thresholds (`0.9`, `0.99`) it does not
exclude both terminal positions using the same oriented representative of the
projective normal direction.  Consequently two fixed opposite boundary arcs were not
justified, and the ensuing path/hub claims were correctly withdrawn.

The phase-zero theorem does not use this implication at all.  No terminal-energy
threshold appears in its path extraction.

**Verdict:** the retraction attacks a different premise.

---

## 2. Section 157 applies to either shore with the same transverse signs

Fix one outer-to-outer train `tau`.  Let its two Jordan shores be `S,T`.

Choose `S` and orient every train-cut contact from `T` into `S` by the common unit
vector `u`.  For every crossing actual diameter edge orient

\[
r_h=p_y-p_x,
\qquad x\in T,\ y\in S.
\]

Section 157 proves that the set of scalars

\[
\{r_h\cdot Ju:h\pitchfork\tau\}
\]

contains both signs.

Now exchange the two shores.  The canonical orientations become

\[
u'=-u,
\qquad
r_h'=-r_h.
\]

Therefore

\[
r_h'\cdot Ju'
=(-r_h)\cdot J(-u)
=r_h\cdot Ju.
\tag{RA.1}
\]

So the same two-sign conclusion holds when `T` is designated as the target shore.
This is exact, finite, and does not use endpoint energy.

**Verdict:** PASS.

---

## 3. Each shore normal arc contains an oriented phase zero

The hostile audit of the complement-bracing theorem establishes the needed near-disk
translation uniformly over actual diameter pairs.  If a crossing diameter is oriented
into a shore and its loaded endpoint there has outward radial normal `n_h`, then

\[
{r_h\over D}=n_h+o(1).
\tag{RA.2}
\]

Loaded diameter endpoints belonging to one shore occupy the single convex-hull boundary
arc between the two retracted O--O train terminals.  Thus the two signs supplied by
Section 157 give normals in that shore arc on both sides of a zero of

\[
g_u(n):=n\cdot Ju.
\]

By continuity, the shore normal-angle interval contains a zero up to a uniform
`o(1)` angular error.

Apply this once with `S` as target shore and once with `T` as target shore.  Hence
**both complementary terminal arcs contain a zero** of the same projective function.
The oriented zero set is exactly

\[
Z(u)=\{\arg u,\arg u+\pi\}
\quad(\bmod 2\pi).
\tag{RA.3}
\]

This is stronger than the projective endpoint-energy statement used in the retracted
proofs.

**Verdict:** PASS.

---

## 4. After marker-neighborhood deletion the two shore zeros must be distinct

This is the point that must be stated explicitly.

Let the two retracted train terminals divide the oriented normal circle into
complementary arcs `I_tau,J_tau`.  Their interiors are disjoint and their union with
the two terminal boundary points is the entire circle.

The selected shrinking phase window gives train-dependent zeros

\[
z_\tau^+,\ z_\tau^- = z_\tau^+ +\pi
\]

within `epsilon_D+eta_D` of fixed antipodal limiting markers

\[
\theta_+,	heta_-=	heta_++\pi.
\]

Choose

\[
\rho_D\downarrow0,
\qquad
\epsilon_D+\eta_D=o(\rho_D),
\]

and delete every train having either terminal in the `rho_D` neighborhoods of the two
fixed markers.

For every surviving train, each terminal is at angular distance at least `rho_D` from
either fixed marker, while each train-dependent zero differs from its fixed marker by
`o(rho_D)`.  Therefore neither train-dependent zero can be a terminal boundary point.
Both zeros lie in the interiors of the complementary arcs.

Section 3 says each of `I_tau,J_tau` contains at least one member of the two-point set
`{z_tau^+,z_tau^-}`.  Since the arc interiors are disjoint and neither zero lies on the
boundary, they cannot contain the same zero.  Thus, after relabeling,

\[
\boxed{
z_\tau^+\in\operatorname{int}I_\tau,
\qquad
z_\tau^-\in\operatorname{int}J_\tau.}
\tag{RA.4}
\]

This proves the **opposite oriented branch** conclusion directly.

**Verdict:** PASS.  This is the exact repair absent from the retracted main proofs.

---

## 5. Fixed limiting markers remain on opposite sides

Because

\[
d(z_\tau^\pm,\theta_\pm)=o(\rho_D)
\]

and the two train terminals avoid the larger `rho_D` marker neighborhoods, moving
`z_tau^+` to `theta_+` and `z_tau^-` to `theta_-` crosses no terminal in cyclic order.
Equation (RA.4) therefore implies

\[
\boxed{
\theta_+\in\operatorname{int}I_\tau,
\qquad
\theta_-\in\operatorname{int}J_\tau
}
\tag{RA.5}
\]

for every surviving train, after one consistent shore labeling.

Thus every surviving proper O--O crosscut separates the **same two fixed boundary
markers**.  This is stronger than merely saying that its endpoints lie in two broad
projective arcs.

The convex-pocket retraction used by the audited train system preserves cyclic order,
so (RA.5) transfers back to the original proper train crosscuts.

**Verdict:** PASS.

---

## 6. Same-marker separation really forces a dual path

Let `gamma,gamma'` be two disjoint proper disk crosscuts, each separating fixed boundary
markers `p,q`.  Let `P_gamma` denote the component closure on the `p` side of `gamma`.

Since `gamma'` is connected and disjoint from `gamma`, its interior is contained in
one component of the disk minus `gamma`.

- If `gamma'` lies in the `p` component, then because it still separates `p` from `q`,
  its `p`-shore satisfies
  \[
  P_{\gamma'}\subset P_\gamma.
  \]
- If it lies in the `q` component, the reverse containment holds.

Hence every pair of `p`-shores is comparable.  The finite family is totally ordered by
inclusion.  Complementary regions occur only before the first crosscut, between
successive crosscuts, and after the last crosscut.  Therefore the complement dual is a
simple path.

No claim that “crosscuts joining two arbitrary fixed arcs form a path” is used.  The
load-bearing hypothesis is the stronger common-marker separation (RA.5).

**Verdict:** PASS.

---

## 7. Weighted deletion remains legitimate at arbitrarily small path density

For a retained O--O pair define

\[
w_\tau=\min(a_\tau,b_\tau).
\]

Each pair endpoint measure is dominated by the corresponding retained outer-occurrence
measure, which is pointwise dominated by loaded-hull side-length measure.  Type-II
near-disk perimeter convergence is nonatomic in oriented normal angle, so the two
`rho_D` neighborhoods carry `o(D)` retained pair weight.

Therefore any fixed positive linear pair-weight floor `cD-o(D)` survives as

\[
cD-o(D)
\]

after marker deletion, even when `c` is as small as `0.0009`.  Since `w_tau<=1`, the
surviving actual train count is at least the surviving pair weight.

Thus the separate hostile-audited `t<=1.865` pair floor can feed the same path proof.
No low-energy Markov selection is needed.

**Verdict:** PASS.

---

## 8. Effect on the retracted frontier

Main's current safe live path through `t<=1.8593` uses a different repair: a small
enough energy threshold plus a quantitative Section-157 same-branch exclusion.  The
phase-zero route instead uses **both shore equations** and deletes shrinking marker
neighborhoods.  These are independent mechanisms.

The post-retraction logic is therefore:

```text
retained same-phase O-O pair weight cD
+ Section 157 on shore S
+ Section 157 on complementary shore T
+ uniform near-disk diameter-normal convergence
-> one antipodal phase zero in each shore

remove o(D) pair weight near the two limiting zeros
-> fixed antipodal markers lie on opposite shores of every surviving crosscut

pairwise noncrossing + common-marker separation
-> totally nested crosscuts
-> complement dual path.
```

This directly supplies the oriented-branch step that the retracted low-energy proofs
lacked.

**Final disposition:** **PASS.**  The phase-zero path theorem is not invalidated by the
September 15 path retractions.  Its two-shore Section-157 argument proves the missing
opposite-oriented-branch conclusion.  Consequently the separately audited retained
pair-weight extension through `t<=1.865` may be composed with it, subject to its own
numerical/path-interface audit.

C-II and Level I remain open.
