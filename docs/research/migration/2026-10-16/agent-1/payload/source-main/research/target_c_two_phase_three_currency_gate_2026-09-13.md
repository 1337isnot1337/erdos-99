# Target C-II — three-currency gate for a near-disk two-phase survivor

**Date:** 2026-09-13  
**Classification:** proved candidate awaiting independent audit; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note composes three already audited proof-only ingredients in the one regime where
their geometric hypotheses are simultaneous: (i) two-phase determinant variation, (ii)
the occurrence-safe exceptional-face/outer-bridge charge, and (iii) the
bridge-subtracted rhombus isoperimetric inequality.  The resulting gate replaces the
uncontrolled outer-bridge population by the actual outer detour and the refined
loaded-boundary surplus. In the canonical no-container Type-II full core, the
near-disk area sandwich also removes the exceptional-face term from the
bridge-subtracted isoperimetry; that stronger coefficient is recorded below.

The candidate implication is

```text
near-disk + near-geodesic + global two-phase purity
 -> delta+rho + 10(e_BB-2k) >= 4-pi
 -> [full core: delta+rho + 5(e_BB-2k) >= 4-pi]
 -> no cheap simultaneous bridge/defect escape.
```

It is a source-level subbranch exclusion, not a C-II closure: the remaining scalar
region permits large `e_BB-2k` or large outer detour.

## 1. Hypotheses and normalized currencies

Let `W` be the occurrence-counted outer walk of the connected Type-II contact graph.
Assume all bounded quadrilateral faces are strict rhombi using only two projective unit
directions `[u]` and `[v]`. Write

- `N_o` for outer-walk occurrences in neither selected direction;
- `P_exc` for the total degree of bounded nonquadrilateral faces;
- `B_o` for physical outer-visible bridge edges;
- `b=length(W)`;
- `k=d_H+s_Z`; and
- `e_BB` for the loaded-loaded unit-side count.

Assume the selected walk has both reciprocal widths `D-o(D)` and
`b<=pi D+o(D)`. These are the explicit near-disk/near-geodesic hypotheses of the
audited outer-variation candidate; they are not asserted for every C-II survivor.

Use the normalized notation

\[
 P={P_{exc}\over D},\quad B={B_o\over D},\quad
 \delta={b-\operatorname{per}(F)\over D},\quad
 \rho={\operatorname{per}(F)-\pi D\over D}.
\]

The detour appearing in the bridge-subtracted estimate is
`(b-pi D)/D=delta+rho`. In the Type-II near-disk limit `rho=o(1)`, but it is
kept explicitly below so the two perimeter normalizations are not conflated.

In the Type-II augmented-cell scope, the independently audited sharp payment is

\[
 P\le 5{(e_{BB}-2k)\over D}+o(1).
\tag{1.1}
\]

The identity `e_BB-2k=Q+u_B` is exact in the same `c_B=0` normalization; it is useful
because it separates the surplus from topology defect `k`.

## 2. Derivation of the gate

The determinant-variation estimate for the two selected directions gives

\[
 N_o\ge (4-\pi)D-o(D).
\tag{2.1}
\]

The occurrence-safe planar charge is

\[
 N_o\le P_{exc}+2B_o.
\tag{2.2}
\]

Therefore

\[
 (4-\pi)D-o(D)\le P_{exc}+2B_o.
\tag{2.3}
\]

The bridge-subtracted rhombus-area argument gives, for the strict-rhombus carrier
scope,

\[
 2B_o\le (b-\pi D)+P_{exc}+o(D).
\tag{2.4}
\]

Substituting (2.4) into (2.3) yields the first exact source-level form

\[
\boxed{
 (4-\pi)D-o(D)\le (b-\pi D)+2P_{exc}.
}
\tag{2.5}
\]

After division by `D`,

\[
\boxed{\delta+\rho+2P\ge4-\pi.}
\tag{2.6}
\]

After division by `D`, insert the sharpened augmented-cell payment (1.1):

\[
\boxed{
 \delta+\rho+10{(e_{BB}-2k)\over D}
 \ge 4-\pi-o(1).
}
\tag{2.7}
\]

Equivalently, because `e_BB-2k=Q+u_B`,

\[
\boxed{
 \delta+\rho+10{(Q+u_B)\over D}
 \ge 4-\pi-o(1).
}
\tag{2.8}
\]

For the canonical no-container Type-II **full positive-contact core**, the
near-disk area sandwich gives the stronger bridge estimate. Let `U` be the union of
all bounded faces of the full core. Every strict-rhombus face is contained in `U`,
while `U` is contained in the convex force hull `F`. Canonical Type-II area saturation
and force-hull convergence therefore give

\[
 {A_4\over D^2}\to{\pi\over4},
 \qquad
 {\operatorname{area}(F)\over D^2}\to{\pi\over4},
 \qquad
 {\operatorname{area}(U)-A_4\over D^2}\to0.
\tag{2.9a}
\]

Applying the finite bounded-face-union inequality to `U` gives the stronger bridge estimate

\[
2B_o\le(b-\pi D)+o(D).
\tag{2.9}
\]

The same occurrence charge therefore gives

\[
\boxed{
\delta+\rho+P\ge4-\pi-o(1),
\qquad
\delta+\rho+5{(e_{BB}-2k)\over D}
\ge4-\pi-o(1).
}
\tag{2.10}
\]

This full-core refinement is not asserted for a selected carrier whose bounded-face
union does not carry the global near-disk area.

This is stronger than retaining an unconstrained `B_o` term: the bridge-rich
alternative must now consume either actual outer-walk detour or the loaded-boundary
surplus that pays the augmented exceptional faces.

## 3. Finite interpretation and closed subbranch

Before normalization, the three finite inequalities read

\[
 N_o\le P_{exc}+2B_o,
\qquad
 2B_o\le(b-\pi D)+P_{exc}+o(D),
\qquad
 P_{exc}\le5(e_{BB}-2k)+o(D).
\]

Consequently, any sequence in this simultaneous scope with

\[
 b-\pi D=o(D)
 \quad\text{and}\quad
 e_{BB}-2k=o(D)
\]

is impossible, since (2.7) would give `4-pi<=o(1)`. Thus the candidate completely
eliminates the **cheap bridge/cheap-defect** subbranch, including the case where
outer bridges are linearly numerous but both the global outer detour and the refined
loaded-boundary surplus are sublinear.

In the full-core scope, zero normalized total perimeter detour (`delta+rho=0`) gives
the explicit threshold

\[
 {e_{BB}-2k\over D}
 \ge {4-\pi\over5}
 =0.1716800012\ldots-o(1).
\tag{3.1a}
\]

In the weaker carrier scope, zero normalized total perimeter detour gives
the explicit threshold

\[
 {e_{BB}-2k\over D}
 \ge {4-\pi\over10}
 =0.0858400006\ldots-o(1).
\tag{3.1}
\]

No claim is made that this threshold is sharp, and it does not imply a lower bound on
`e_BB` alone when `k` is linear.

## 4. Why this still does not close C-II

The gate is conditional on the simultaneous near-disk, near-geodesic, and global
two-phase hypotheses. It does not control a survivor with many phase directions, a
large outer detour, or a carrier whose width is not global. Even the stronger full-
core inequality (2.10) allows a large `e_BB-2k`; the current endpoint scalar witness
has ample such surplus. The bridge-chain regression is also not contradicted because
its grid-plus-chain family is not a near-disk Type-II global minimizer and does not
satisfy the full-core hypotheses.

The remaining closing implication is therefore explicit:

\[
\text{three-currency gate}
\to\text{control }\delta\text{ or }e_{BB}-2k\text{ from the actual diameter graph}
\to\text{strict source descent or exact unit triangle}.
\]

Contact-isolated source points remain retained; no full-source affine-kernel extension
or selected-stress-to-global-minimizer inference is used.
