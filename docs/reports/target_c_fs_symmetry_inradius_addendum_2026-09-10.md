<!-- theorem-state: {"artifact_id":"ART-AB662DABDC75","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — FS full-hull scope and centered inradius addendum

**Date:** 2026-09-10  
**Repository base:** `3f37ef0eab4407a411f9a6d51d016ba600302be7`; follows `target_c_fs_symmetry_difference_body_2026-09-10.md` on the research branch  
**Run type:** dependency correction / geometric strengthening  
**Target:** Target C, C-II  
**Depends on:** promoted C65 relative-interior support restoration from `../targets/target-c/56-ci-restored-frontier.md`; FS.4 from `target_c_full_source_circumradius_response_2026-09-10.md`; DA/DB diameter-direction polygon from the September 9 post-ZF reports  
**External web search:** no external theorem used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This addendum makes one scope point in the preceding SC report explicit and extracts a second consequence of the same FS.4 half-turn estimate.

## 1. Scope correction: the selected FS hull can be the full actual force hull

In the lexicographically normalized C-II source, C65 supplies a relative-interior normalized KKT stress whose positive support is the full actual support:

\[
C_+=C=C_*,\qquad H_+=H=H_*.
\]

Choose this stress when applying FS.4. Its selected force hull is therefore

\[
F_s=\operatorname{conv}(B_s)=\operatorname{conv}(B_+)=:F,
\]

where `F` is exactly the full actual force hull used in DB and DA. Hence FS.4 gives, for that same full hull and the common source circumcenter `o`,

\[
\boxed{
d_H(F-o,-(F-o))\le2L_D,
}
\tag{SI.1}
\]

with

\[
L_D=\sqrt{D\eta+\eta^2},
\qquad
\eta=3^{1/4}\sqrt D,
\qquad
L_D=o(D).
\tag{SI.2}
\]

Thus the preceding SC difference-body argument really does apply to the full actual diameter-direction polygon `P_H`; it is not mixing two different selected supports.

## 2. The diameter polygon contains a large centered disk

Let

\[
a_D:=\arcsin\frac1{2D}.
\]

Order the `h` projective diameter directions cyclically and write their gaps as

\[
g_1,\ldots,g_h,
\qquad
\sum_i g_i=\pi,
\qquad
g_i\ge2a_D.
\tag{SI.3}
\]

Put

\[
P_H:=D\operatorname{conv}\{\pm u_e:e\in H\}.
\]

Let `g_max=max_i g_i`. Since the other `h-1` gaps are each at least `2a_D`,

\[
\boxed{
g_{\max}\le\pi-2(h-1)a_D.}
\tag{SI.4}
\]

The vertices of `P_H/2` lie on the circle of radius `D/2`. For a centrally symmetric inscribed polygon with largest successive angular gap `g_max`, its centered inradius is

\[
r(P_H/2)=\frac D2\cos\frac{g_{\max}}2.
\]

Indeed each side joining consecutive radius-`D/2` vertices is at distance `(D/2)cos(g/2)` from the origin, and the largest gap gives the nearest side. Hence SI.4 gives

\[
\boxed{
B\!\left(0,\frac D2\sin((h-1)a_D)\right)
\subseteq\frac12P_H.
}
\tag{SI.5}
\]

## 3. FS transports that disk into the actual force hull

The difference-body inclusion and FS half-turn estimate give

\[
P_H\subseteq F-F
\subseteq2(F-o)+2L_DB.
\]

Dividing by two,

\[
\boxed{
\frac12P_H\subseteq(F-o)+L_DB.
}
\tag{SI.6}
\]

For any unit vector `u`, support functions therefore satisfy

\[
h_{P_H/2}(u)\le h_{F-o}(u)+L_D.
\]

By SI.5,

\[
h_{P_H/2}(u)\ge\frac D2\sin((h-1)a_D)
\]

for every `u`. Hence

\[
h_{F-o}(u)
\ge
\frac D2\sin((h-1)a_D)-L_D
\qquad\text{for every unit }u.
\]

The support-function characterization of convex containment now gives the finite theorem:

### Theorem SI — common-center force-hull inradius

\[
\boxed{
B\!\left(
 o,
 \frac D2\sin((h-1)a_D)-L_D
\right)
\subseteq F,
}
\tag{SI.7}
\]

whenever the displayed radius is positive.

No symmetry of `F` is assumed; the only symmetry input is the quantitative FS.4 Hausdorff estimate.

## 4. Asymptotic consequence

Along any unbounded post-ZF subsequence with

\[
\frac hD\to y,
\]

we have

\[
(h-1)a_D\to\frac y2,
\qquad
\frac{L_D}{D}\to0.
\]

Therefore SI.7 gives

\[
\boxed{
\liminf\frac{r_o(F)}D
\ge\frac12\sin\frac y2,
}
\tag{SI.8}
\]

where `r_o(F)` is the radius of the largest disk centered at the common source circumcenter `o` and contained in `F`.

DB gives `y>=2rho`, where `rho=cos rho=0.7390851332...`, while every projective diameter-direction family has `y<=pi`. Since `sin(y/2)` is increasing on `[0,pi]`,

\[
\boxed{
\liminf\frac{r_o(F)}D
\ge
\frac12\sin\rho
=0.3368060145916074\ldots .
}
\tag{SI.9}
\]

Thus every post-ZF survivor force hull contains, about the same center that contains the entire source in radius `D/2+O(sqrt D)`, a concentric disk of radius at least `0.336806D-o(D)`.

## 5. Effect on the external-rattler branch

ER leaves the contact-isolated source population outside `F` as the force-bulk obstruction. SI shows that this population cannot occupy an arbitrary region inside the source circumdisk: every external point lies in the completion region

\[
K\setminus F
\subseteq
B\!\left(o,\frac D2+\eta\right)
\setminus
B\!\left(o,\frac D2\sin((h-1)a_D)-L_D\right).
\tag{SI.10}
\]

The annular area bound obtained by discarding the actual shape of `F` is still too weak to close the Oler population inequality. The new information is therefore a geometric localization theorem, not a completed external-population bound.

A closing completion theorem would need to use the fact that every external source point is also at distance at most `D` from every loaded terminal on `F`, together with unit separation, to beat ordinary Oler capacity in the region SI.10.

## 6. Regression audit

- **Regular odd shells:** their force hull tends to the radius-`D/2` disk, so SI.9 is safely below the true limiting inradius `D/2`.
- **Dense isolated fillings:** the proof does not bound or remove isolates and therefore does not fail on the mandatory filled-shell regression.
- **Response weights:** no lower bound on any `beta_h` is used.
- **Representative scope:** the relative-interior stress is chosen only inside the same C65 lexicographic source, so no RA or hull-saturated representative is substituted.

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| full-hull identification `F_s=F` for the chosen stress | canonical consequence | relative-interior support is full actual `H_*` |
| diameter-polygon disk SI.5 | proved | largest projective-gap bound |
| finite centered inradius SI.7 | proved | SI.5 + FS.4 support-function inclusion |
| universal `0.336806...D` centered inradius | proved conditional on report-level DB | DB `h/D>=2rho` |
| annular completion alone closes population | rejected | its coarse area remains quadratic and too large |
| Level I | still open | need a diameter-completion packing theorem or another strict global bridge |
