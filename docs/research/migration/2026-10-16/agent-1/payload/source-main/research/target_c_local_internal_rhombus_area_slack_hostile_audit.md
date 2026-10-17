# Hostile audit — local internal-rhombus area/slack theorem

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_local_internal_rhombus_area_slack.md`  
**Disposition:** **PASS at proof-only Type-II scope.** C-II remains open.

## 1. The low-response hypothesis is not a hidden dependency

The candidate extracts only the local §§5–7 mechanism from the independently audited LRTQ theorem. In LRTQ, `epsilon_D -> 0` is used in §3 to select a cell with near-diameter attachment hull and later to obtain `gamma>=1`. It is not used in the following local facts:

1. HOF face preservation for `C[I_r]`;
2. the exact component identity `k_r+Q_r=2(delta_r+r_r)`;
3. the strict-rhombus boundary theorem `B_r>=4 sqrt(R_r)`;
4. recipient counting `B_r<=k_r+4f_r+Q_r<=k_r+5Q_r`;
5. `per(P_r)<=k_r+2pi`; or
6. Type-II local rhombus-area saturation.

The independent LRTQ hostile audit explicitly passes items 1–6. Therefore applying that local argument to an arbitrary selected Type-II harmonic component does not import the response assumption.

**Verdict:** PASS.

## 2. Recompute the local coefficient

From

\[
k_r+Q_r=2(\delta_r+r_r)
\]

and

\[
4\sqrt{R_r}\le B_r\le k_r+5Q_r,
\]

substitute `Q_r=2(delta_r+r_r)-k_r`:

\[
4\sqrt{R_r}
\le10(\delta_r+r_r)-4k_r.
\]

Hence

\[
\boxed{
\delta_r+r_r
\ge {2\over5}k_r+{2\over5}\sqrt{R_r}.
}
\]

The perimeter argument gives

\[
k_r\ge2\sqrt{\pi A_{4,r}^{int}}-2\pi.
\]

Type-II rhombus-area rigidity gives, for a macroscopic selected subfamily,

\[
A_{4,r}^{int}=a_0R_r+O(D),
\qquad a_0={\sqrt3\over2}.
\]

Thus when `A_{4,r}^{int}/D^2 -> A`, division by `D` gives

\[
\liminf {\delta_r+r_r\over D}
\ge
\left({4\over5}\sqrt\pi+{2\over5\sqrt{a_0}}\right)\sqrt A.
\]

Since

\[
r_r+\eta_r=(\delta_r+r_r)+2-d_r,
\]

and `d_r/D -> lambda`, the candidate conclusion follows:

\[
\boxed{
\liminf {r_r+\eta_r\over D}
\ge [C_{loc}\sqrt A-\lambda]_+.
}
\]

Independent numerical recomputation gives

\[
C_{loc}=1.8477910534538295\ldots .
\]

**Verdict:** PASS. The coefficients `2/5` and `4/5` are correct.

## 3. The internal rhombus area is the right area

HOF proves that bounded four-faces of `C[I_r]` are exactly the unloaded-only strict rhombi assigned to `I_r`. Therefore `R_r` in the train-boundary theorem and `A_{4,r}^{int}` in the area conversion refer to the same physical rhombus family.

Canonical Type-II area rigidity has nonnegative excess per strict rhombus and global total excess `O(D)`. Any selected subfamily therefore has excess at most `O(D)`; no averaging over a fixed cell is required. This remains valid for a `D`-dependent selected component.

**Verdict:** PASS.

## 4. Perimeter step and bridge multiplicity

The internal graph outer walk is occurrence-counted, so bridges appear twice. Its unit edge occurrences give an upper bound on the perimeter of `K_r=conv(I_r)`:

\[
per(K_r)\le k_r.
\]

Every attachment is within unit distance of `I_r`, hence

\[
K_r\subset P_r\subset K_r+B(0,1).
\]

Cauchy's perimeter formula for parallel bodies gives

\[
per(P_r)\le per(K_r)+2\pi\le k_r+2\pi.
\]

Planar isoperimetry then gives the stated lower bound on `k_r`. Articulation points and bridges cause no missing boundary term because `k_r` uses outer-face occurrences, exactly as in the independent LRTQ audit.

**Verdict:** PASS.

## 5. Wrapping-carrier specialization

The repaired Section-118 frontier/common-cap profile supplies the same wrapping component with

\[
A_{4,w}^{int}/D^2\ge A_*-o(1),
\qquad
A_*=0.4703752868004241\ldots,
\]

and

\[
d_w/D\to\lambda_*=0.9762439137425688\ldots .
\]

Therefore

\[
C_{loc}\sqrt{A_*}-\lambda_*
=0.2910434605114113\ldots>0.
\]

Normalized §160 gives the exact global remainder

\[
G_D=\sum_r r_r+s_B+\sum_r\eta_r.
\]

All terms are nonnegative, so the selected wrapping term gives

\[
G_D/D\ge0.2910434605114113\ldots-o(1).
\]

There is no double counting with the diameter moment `H_D=sum d_r`.

**Verdict:** PASS at the stated frontier-profile scope.

## 6. Scope and nonclaims

- The result is Type II only.
- The local theorem is all-profile; the numerical `0.291043...` specialization is Section-118 frontier/common-cap only.
- Contact-isolated source points remain in the full source and outside the internal component graph.
- No affine-kernel claim is made on isolated coordinates.
- The theorem does not imply a positive slack contribution from every complement-gap group; thin cap cells remain a valid obstruction.
- The theorem does not close Type II, Type I, C-II, or Level I.
- Theorem-state authority is unchanged.

**Final classification:** PASS as a proof-only local Type-II theorem, with the frontier-profile numerical corollary also passing under its explicit dependencies.
