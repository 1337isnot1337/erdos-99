<!-- theorem-state: {"artifact_id":"ART-CA6AC6E61C76","canonical":true,"claim_ids":["C-FULLCORE-TRAIN-SURPLUS-FLOOR"],"claim_statuses":{"C-FULLCORE-TRAIN-SURPLUS-FLOOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — full-core train-coupled surplus floor

**Date:** 2026-09-14
**Repository commit audited:** ef941ab2b44aa393bdc461926769247b45754202
**State version consulted:** 2026-09-14.audit.49
**Artifact audited:** docs/reports/target_c_fullcore_train_coupled_surplus_floor_2026-09-14.md
**Verdict:** canonical promotion accepted in audit.49; not a Level-I closure.

## 1. Audit conclusion

The report's new geometric lemma is valid under the canonical full-core
near-disk hypothesis after repairing the projection step. The repaired proof
projects all directed sides of the short hull arc onto a common tangent axis;
it does not assume that the chord direction itself is tangent. If a unit chord
has an intervening hull vertex, that arc has at least two unit-separated side
occurrences, whose total projection is \(>1\), contradicting the chord length.

The subsequent scalar derivation is exact and uses only canonical ledgers:

\[
c_B=0,\quad e_{BB}=q-m_B,\quad
\mu_DD=q+m_B-k-2c_I-4,
\]
\[
q-k\ge \frac{P_F+Q}{2},\qquad
q-k+2f\ge2\sqrt{R_4},\qquad Q\ge f.
\]

Consequently, in the canonical full-core Type-II branch,

\[
\liminf_{D\to\infty}\mu_D
\ge
\frac{2\pi+2\sqrt{\pi/(2\sqrt3)}}5
=1.6375621841815\ldots.
\]

This is a genuine scalar-frontier improvement over the canonical
\(\liminf\mu_D\ge1\) floor. It is not a closure because it supplies neither
an upper bound on the aggregate outer-walk detour, an exact unit equilateral
triangle, nor a source-preserving strict diameter decrease. The macroscopic
container branch is also outside its scope.

## 2. Geometric audit

The canonical near-disk statement supplies, after translation,

\[
B(0,r_D)\subset F\subset B(0,R_D),\qquad
r_D/D\to\tfrac12,\quad R_D/D\to\tfrac12.
\]

Because the inner disk is contained in \(F\), \(F\) is strictly star-shaped about
the translation center, so radial order agrees with cyclic boundary order. For a
unit chord \(pq\) of the loaded convex hull, the inner disk gives
\[
2r_D\sin(\gamma_D/2)\le |p-q|=1,
\]
so the minor polar span \(\gamma_D\) is \(O(D^{-1})\). For a side on the
corresponding short boundary arc, an outward support normal \(n\) at a point
\(x\) satisfies \(n\cdot x\ge r_D\) and \(|x|\le R_D\). Thus
\[
\angle(n,x)\le\arccos(r_D/R_D)=o(1).
\]
After orienting all sides along the arc, their tangent vectors lie in a
single cone of width
\[
\tau_D=2\arccos(r_D/R_D)+O(D^{-1})=o(1).
\]
If an intervening hull vertex exists, there are \(N\ge2\) side occurrences.
For a unit axis \(t_0\) through the cone midpoint, unit separation gives
\[
t_0\cdot(q-p)
=\sum_{j=1}^N\ell_j(t_0\cdot t_j)
\ge N\cos\tau_D
\ge2\cos\tau_D>1
\]
for all sufficiently large \(D\), whereas
\(t_0\cdot(q-p)\le|q-p|=1\). This is a contradiction.

The argument remains valid for nonsmooth convex hulls: each side is handled
with one of its support normals, and no differentiability or unique normal is
used. If the chord were nonconsecutive on either boundary arc, the shorter
polar arc would contain an intervening vertex; reversing orientation handles
the opposite cyclic order. Therefore every unit pair of loaded hull vertices
is a hull side. No claim is made about contact-isolated source points.

## 3. Ledger audit

The canonical loaded-hull identities are
\[
e_{BB}=q-m_B+c_B,\qquad
c_I+s_C+c_B=m_B+k-2,\qquad k=d_H+s_Z.
\]
With \(c_B=0\),
\[
s_C=m_B+k-c_I-2,
\]
and therefore
\[
\mu_DD=e_{BB}+2s_C-3k
=q+m_B-k-2c_I-4.
\]
The canonical component-deatomization estimate \(c_I=O(D^{2/3})\), together
with \(m_B\ge0\), gives
\[
\mu_D\ge(q-k)/D-o(1).
\]

The occurrence-counted Section-63 identity is
\[
b+Q=2q-2k.
\]
Since the outer walk contains the convex-hull boundary in the projection-variation
sense, \(b\ge P_F\), hence
\[
q-k=\frac{b+Q}{2}\ge\frac{P_F+Q}{2}.
\]
No simple-walk or no-bridge assumption is inserted.

## 4. Train/interface audit

The canonical Section-85 inequality is
\[
q-k+2f\ge2\sqrt{R_4}.
\]
Every bounded nonquadrilateral face has degree at least five, so its contribution
\(\deg-4\) to \(Q\) is at least one and \(Q\ge f\). Setting
\[
u_D=(q-k)/D,\quad x_D=f/D,\quad
p_D=P_F/D,\quad r_D=R_4/D^2,
\]
the two exact lower bounds become
\[
u_D\ge p_D/2+x_D/2,\qquad
u_D\ge2\sqrt{r_D}-2x_D.
\]
Taking the convex combination with weights \(4/5\) and \(1/5\) cancels the
\(x_D\) term:
\[
u_D\ge\frac{2p_D+2\sqrt{r_D}}5.
\]
The Type-II limits \(p_D\to\pi\) and
\(r_D\to\pi/(2\sqrt3)\) give the reported exact floor. The weights and
constant are algebraically correct.

## 5. Scope and regression checks

- The theorem is asymptotic and uniform over every sequence in the canonical
  full-core Type-II branch; it does not assert a finite numerical threshold.
- The source remains the full source. Contact-isolated points are neither
  removed nor put into the affine ZR/ZF kernel.
- Repeated vertices and bridges in the outer walk are retained; only
  occurrence-counted \(b\ge P_F\) is used.
- No Euler-path conclusion is drawn from diameter edges.
- The sheared near-rhombus density family remains a regression against
  density-only or angle-gap closures; it does not contradict the present
  incidence floor because it is not a canonical global minimizer.
- A near-disk shell remains a feasibility/local-geometry regression, not a
  global-minimality counterexample.

The report therefore passes the mathematical audit for its stated scope.
Its canonical status does not close C-II, and the exact remaining source-level
obligation is unchanged:
\[
\text{couple the high-surplus train/interface currency to }
\sum_r(L_r-2d_r),
\]
or produce an exact triangle or a finite source-preserving strict competitor.

## 6. Promotion recommendation

The theorem-state manifest registers the canonical claim
`C-FULLCORE-TRAIN-SURPLUS-FLOOR`, depending on C-FULLCORE-NEAR-DISK,
C-LOADED-HULL, C-COMP-DEATOMIZATION, and C-TRAIN-INTERFACE-CURRENCY, with conclusion
\[
\liminf\mu_D\ge
\frac{2\pi+2\sqrt{\pi/(2\sqrt3)}}5.
\]
The route map and active Target-C prompt should replace the scalar floor \(1\)
with this stronger floor while retaining the same detour/deformation endpoint.
