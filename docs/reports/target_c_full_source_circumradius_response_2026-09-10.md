<!-- theorem-state: {"artifact_id":"ART-CD17E84B56F8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — full-source circumradius transport into the C-II response

**Date:** 2026-09-10

**Repository state:** `main`, `5865724` at the start of the run

**Run type:** closing-proof attempt / exact bridge and regression audit

**Target:** C-II, retaining the entire source population

**Active prompt:** [Target C continuation](../prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md), with its controlling September 9 update

**External web search:** checked the already imported Bonnesen statement in Klain, Section 4, equation (6)

**Computation:** none used in the proofs

## LEVEL I STATUS

`STILL OPEN`.

This run does **not** find a C-II contradiction. It establishes a uniform
full-population-to-force-geometry bridge, then disproves two tempting ways to
complete that bridge at response level.

The new consequence for the indexed Target C frontier is

\[
\boxed{P_*=2D-O(\sqrt D)}
\]

for **every** normalized KKT stress of **every** global minimizer. The full
diameter graph also has maximum shared-endpoint angle `O(D^{-1/4})`, not merely
an asymptotic ceiling of `50.7608...` degrees. These facts allow arbitrarily
many contact-isolated source points.

The input is the existing full-source Bonnesen estimate, transported through
the elementary inclusion of the selected force hull in the source hull. No
new PSD theorem is asserted. With the restored PSD theorem, the conclusions
apply simultaneously to all actual selected circular-planar responses.

**Authority:** working proof report; not a promoted addendum. No route map or
active prompt is changed by this run.

## 1. Starting endpoint and attack

The controlling [C-I restoration](../targets/target-c/56-ci-restored-frontier.md)
reduces a hypothetical counterexample to a contact/diameter-lexicographically
minimal triangle-free global source with `C=C_*` and `H=H_*`, retaining all
isolates. The required C-II endpoint is a contradiction for that whole source,
not just its nonisolated core.

The attempted implication was

```text
full-source finite packing
    -> near-minimal source circumradius
    -> near-minimal circumradius for every selected force hull
    -> almost no diameter-reaction cancellation
    -> a response/finite-capacity contradiction.
```

The first four arrows are proved below. Two proposed versions of the last
arrow fail an exact regular-shell regression:

1. almost no reaction cancellation does not imply that all but vanishing
   diameter weight can be retained in a matching;
2. it does not imply a small C41 response trace defect, even when the actual
   unit-contact response is PSD and has exactly the affine scalar kernel.

For an exact whole-population target, put

\[
a_0=\frac{\sqrt3}{2},\quad c_0=\frac{\sqrt3}{4},\quad
K=\operatorname{conv}A,\quad P=\operatorname{per}K,
\]
\[
\delta_K=\frac{\pi D^2}{4}-\operatorname{area}K,\qquad
\mathscr O_A=\operatorname{area}K+c_0P-a_0(n-1).
\]

Oler and isodiametricity give `delta_K>=0` and `O_A>=0`. The canonical strict
translated-lattice comparison gives the exact global allowance

\[
\boxed{\delta_K+\mathscr O_A<c_0P.}                 \tag{1.1}
\]

A closing population/response theorem must overcome this allowance or give
a strict smaller-diameter competitor. The estimates below alone do neither.

## 2. Trusted dependencies and exact scope

Only the following mathematical inputs are used in the positive bridge:

- [Shared Oler inequality](../theory/03-oler-shell.md), Lemma 21.1,
  applied to **all `n` source points** in `K`.
- [Strict translated-lattice bound](../targets/target-b/01-jammed-rhombic-branch.md),
  Section 36.1: `D(n)^2 < (2sqrt(3)/pi)(n-1)`. This statement is unconditional;
  no jammed, rhombic, or Target B shell assumption is transported.
- The source-hull part of [Section 155](../targets/target-a/08-prescribed-phase-alignment.md):
  Bonnesen gives `R(K)-r(K)<3^(1/4)sqrt(D)`. This part uses only the preceding
  global bounds, not Target A's smaller optimum or very-super-boundary hypothesis.
- [KKT equilibrium](../theory/01-local-structure.md), Theorem 4.1;
  [force hull](target_c_force_hull_2026-08-30.md), C3–C4;
  [reciprocal perimeter and actual response](target_c_force_polygon_2026-08-30.md),
  C10–C11.
- For its application to the restored C-II class, the
  [September 9 audit](target_c_c53_orientation_and_ci_restoration_2026-09-09.md),
  Sections 4, 6, and 7. Its universal PSD/common-kernel statements are retained
  with exactly their stated hypotheses; the elementary bounds below do not
  need PSD to be proved again.

The shell regression uses [shared Propositions 14.1–14.2](../theory/02-nonlinear-and-regressions.md).
Its PSD rank and its two new no-go consequences are verified directly below.

## 3. Full-source circumradius transport

### Proposition FS.1 — a containing disk for every selected force hull

Let `A` be any noncollinear global `n`-point minimizer, with `D=D(n)`. Set

\[
\eta=3^{1/4}\sqrt D.
\]

Let `o` be a circumcenter of the **full** source hull `K`, and write `R=R(K)`.
Then

\[
\boxed{\frac D2\le R<\frac D2+\eta.}                \tag{3.1}
\]

For every normalized KKT stress `s`, let `B_s` be its positive diameter
endpoints and `F_s=conv(B_s)` its selected force hull. Then

\[
\boxed{
F_s\subseteq K\subseteq\overline B(o,R),\qquad
\frac D2\le R(F_s)\le R<\frac D2+\eta.
}                                                        \tag{3.2}
\]

#### Proof

Oler on the entire source gives

\[
\operatorname{area}K+c_0P\ge a_0(n-1)>\frac{\pi D^2}{4}.
\]

Since `P<=pi D`,

\[
P^2-4\pi\operatorname{area}K
<P^2-\pi^2D^2+4\pi c_0P
\le\pi^2\sqrt3D.
\]

Bonnesen therefore gives `R-r<eta`. Every inscribed disk has diameter at
most `D`, so `r<=D/2`; every enclosing disk has radius at least `D/2`.
This proves (3.1).

Every selected positive diameter endpoint is an actual source point, so
`F_s subset K`. Circumradius is monotone under containment. Finally
`sum beta=1` supplies a positive diameter edge, both of whose endpoints
belong to `F_s`; thus `diam(F_s)=D` and `R(F_s)>=D/2`. QED.

### Why the isolate distinction matters

The proof does not assert `F_s=K`, that the force hull has nearly maximal
area, or that `n-|V(C)|=O(D)`. Circumradius is an **upper** containment
quantity: even a small or thin subset inherits the containing disk of `K`.
A large unstressed population cannot invalidate (3.2).

Consequently, the conditional observation in Section 4 of the original C10
report can now be made unconditional: its missing near-minimal
**circumradius** follows from the full-source estimate. Near-maximal
**area** remains a different and unproved assertion for the force hull.

## 4. Uniform reciprocal-perimeter saturation

### Theorem FS.2

For every normalized KKT stress of `A`,

\[
\boxed{
\frac{2D}{1+2\eta/D}<P_*\le2D,
\qquad
0\le2D-P_*<\frac{4\eta}{1+2\eta/D}<4\eta.
}                                                        \tag{4.1}
\]

In particular `P_*/D -> 2` uniformly over all stresses and all global sources
as `n -> infinity`. No triangle-free hypothesis is needed.

#### Proof

Write

\[
s_b=\sum_k\beta_{bk},\qquad
g_b=\sum_k\beta_{bk}(p_b-p_k),\qquad
P_*=\sum_b|g_b|.
\]

Summing endpoint contributions gives the exact virial identity

\[
D^2=\sum_b(p_b-o)\cdot g_b\le R\sum_b|g_b|=RP_*.
\]

Also `|g_b|<=Ds_b` and `sum_b s_b=2`, so `P_*<=2D`.
Substitute (3.1) and rearrange. QED.

This excludes every asymptotic branch `P_*/D<=2-epsilon` with fixed
`epsilon>0`. It strengthens the earlier C16/C18 lower-endpoint bounds,
but does not turn near equality into the **exact** matching equality case.

## 5. The entire diameter graph has vanishing star angles

### Theorem FS.3

If distinct diameter pairs `by` and `bz` meet at `b`, their angle satisfies

\[
\boxed{
\theta<\Theta_D:=
2\arccos\!\left(\frac{D}{D+2\eta}\right),\qquad
\theta\le\frac\pi3.
}                                                        \tag{5.1}
\]

Thus uniformly over the full actual diameter graph,

\[
\theta=O(D^{-1/4}),\qquad
\Theta_D=(4\,3^{1/8}+o(1))D^{-1/4}.
\]

With `theta_cap=min(pi/3,Theta_D)` one also has

\[
\boxed{
\deg_H(b)\le
1+\left\lfloor
\frac{\theta_{\rm cap}}{2\arcsin(1/(2D))}
\right\rfloor
=O(D^{3/4}).
}                                                        \tag{5.2}
\]

#### Proof

The triangle `byz` has two sides `D`, apex angle `theta<=pi/3`, and base
`2D sin(theta/2)`. All its angles are acute. Its minimum enclosing circle
is therefore its circumcircle, of radius

\[
R_{byz}=\frac{D}{2\cos(\theta/2)}.
\]

It is contained in `K`, so `R_{byz}<=R(K)<D/2+eta`, proving (5.1).
The expansion of arccos at one gives the displayed rate.

All partners lie on the radius-`D` circle centered at `b`. Their directions
lie in an arc of width at most `theta_cap`: the diameter-graph sixty-degree
bound permits one consistent unwrapping, and (5.1) bounds its extreme pair.
Unit separation forces consecutive partner angles at least
`2arcsin(1/(2D))`. Counting the intervals proves (5.2). QED.

This is a bound on geometric chord directions, **not** on angular rates of a
critical velocity. It does not supply a Poincaré inequality for those rates.

## 6. A common center and actual-response radialization

Put

\[
T_D=D\eta+\eta^2,\qquad L_D=\sqrt{T_D}=O(D^{3/4}).
\]

### Theorem FS.4

For every actual diameter pair `bk`,

\[
\boxed{
\left|\frac{p_b+p_k}{2}-o\right|<L_D.
}                                                        \tag{6.1}
\]

For every selected normalized stress, simultaneously,

\[
\boxed{
|g_b-2s_b(p_b-o)|\le2s_bL_D,\qquad
\sum_b|g_b-2s_b(p_b-o)|\le4L_D.
}                                                        \tag{6.2}
\]

Let `X_B` have rows `(p_b-o)/D`, and let `S_B=diag(s_b)`. For the actual C11
response `Lambda`,

\[
\boxed{
\sum_b\left|(\Lambda X_B-2S_BX_B)_b\right|
\le\frac{4L_D}{D}=O(D^{-1/4}).
}                                                        \tag{6.3}
\]

Also

\[
\boxed{
d_{\rm Haus}(F_s-o,-(F_s-o))\le2L_D.
}                                                        \tag{6.4}
\]

Thus every normalized selected force-hull limit is centrally symmetric
about the common source circumcenter and is the convex hull of points on
the radius-`1/2` circle. This is not a claim that the limit is the disk.

#### Proof

The parallelogram identity gives, for the midpoint `m` of a diameter pair,

\[
|m-o|^2
=\frac{|p_b-o|^2+|p_k-o|^2}{2}-\frac{D^2}{4}
\le R^2-\frac{D^2}{4}<D\eta+\eta^2.
\]

Next,

\[
g_b-2s_b(p_b-o)
=-\sum_k\beta_{bk}(p_b+p_k-2o).
\]

Apply (6.1), then sum using `sum_b s_b=2`. C11 gives
`Lambda X_B=g/D`, which proves (6.3).

For every `b in B_s`, choose a positive diameter partner `k in B_s`.
Equation (6.1) places `-(p_b-o)` within `2L_D` of `p_k-o`. This works in
both directions; convex combinations give (6.4). Moreover each endpoint
satisfies `D-R<=|p_b-o|<=R`. After division by `D` these radii converge
uniformly to `1/2`, and `L_D/D -> 0`. Subsequential compact limits of the
endpoint sets, followed by convex hulls, prove the limit statement. QED.

The matrix estimate (6.3) concerns only the two affine coordinate fields.
It is **not** a bound on the response operator on arbitrary boundary data.

### Exact weighted partner-dispersion consequence

Define

\[
V_b=\sum_{k<l}\beta_{bk}\beta_{bl}|p_k-p_l|^2.
\]

Expansion gives `|g_b|^2=D^2s_b^2-V_b`, and hence

\[
\boxed{
\sum_b\frac{V_b}{s_b}
=\sum_b(Ds_b-|g_b|)\left(D+\frac{|g_b|}{s_b}\right)
\le2D(2D-P_*)<8D\eta.
}                                                        \tag{6.5}
\]

This supplies aggregate geometric coherence without any individual weight
floor. It still says nothing about the magnitude of a C41 circular minor.

## 7. Exact shell regression to the attempted response closure

Let `h>=5` be odd, `k=(h-1)/2`, `a=pi/(2h)`, and take a regular unit
`h`-gon. Its diameter is `D_h=1/(2sin a)`. Use the canonical stress

\[
\alpha_e=D_h^2/h\quad\text{on its sides},\qquad
\beta_e=1/h\quad\text{on its diameter cycle}.
\]

All vertices are loaded, so the actual circular-planar response is just the
weighted side-cycle Laplacian: `Lambda=L_C`.

### 7.1 Perimeter saturation with no weighted matching approximation

At each vertex the two diameter vectors make angle `pi/h=2a`. Therefore

\[
\boxed{
P_*=2D_h\cos a,\qquad
2D_h-P_*=\tan(a/2)\sim\frac1{4D_h}.
}                                                        \tag{7.1}
\]

Nevertheless the diameter graph is an odd cycle, not a matching. A matching
contains at most `(h-1)/2` of its edges, so the maximum diameter weight retained
by any matching is

\[
\boxed{\frac{h-1}{2h}\longrightarrow\frac12.}        \tag{7.2}
\]

Thus even `2D-P_* -> 0` does not allow deletion of only `o(1)` diameter
weight to reach a matching. Coalescing geometric directions are not the same
operation as deleting actual source constraints.

### 7.2 Saturation coexists with a quadratic response defect

The exact trace identity is

\[
\boxed{
\operatorname{tr}(\Lambda-L_H)=2D_h^2-2.
}                                                        \tag{7.3}
\]

Indeed the trace of a weighted Laplacian is twice its total edge weight;
the contact and diameter weight totals are `D_h^2` and one. This is exactly
the C41 defect, not a substituted or electrically equivalent network.

For completeness the defect is PSD, with exactly the affine kernel.
Its Fourier eigenvalues, for `j=0,...,h-1`, are

\[
\lambda_j=\frac4h
\left[D_h^2\sin^2\frac{\pi j}{h}
      -\sin^2\frac{\pi k j}{h}\right].                 \tag{7.4}
\]

The modes `j=0,1,h-1` have eigenvalue zero. For all other modes,

\[
D_h\sin\frac{\pi j}{h}
\ge D_h\sin\frac{2\pi}{h}
=2\cos\frac\pi h\cos\frac{\pi}{2h}>1.
\]

The last strict inequality holds already at `h=5` and increases with `h`.
The second squared sine in (7.4) is at most one, so every other eigenvalue
is positive. The three zero modes are precisely the constant and two
coordinate functions. Thus

\[
\boxed{
\Lambda-L_H\succeq0,\qquad
\ker(\Lambda-L_H)=\operatorname{span}\{1,P_x,P_y\}.
}                                                        \tag{7.5}
\]

There is no implication from FS.2/FS.4, circular planarity, unit contact
lengths, affine equilibrium, PSD, and the affine kernel to a small response
trace defect.

### 7.3 Restoring the whole population does not remove this local regression

Shared Proposition 14.2 fills these shells with strictly separated isolated
interior points, giving `n_h=Delta_2 D_h^2+o(D_h^2)`. These added points do not
change the stress, response, or formulas (7.1)–(7.5). Their stress rows are
zero and must be retained as free scalar coordinates in the full matrix.

For prime `h`, shared Proposition 13.1 also prevents a sufficiently small
feasible perturbation of the shell from decreasing its diameter. Hence an
argument using only these properties cannot promise a local strict release.

These filled shells have **no global minimum-diameter certificate**. They
do not disprove C-II, nor do they contradict FS.1–FS.4. In particular this
report does not assert the sharp global integer comparison (1.1) for the
regression fillings. The omitted global finite-capacity information is the
essential distinction.

## 8. Effect on the exact C-II target

There is now a rigorously justified necessary asymptotic geometry, available
without estimating or deleting the isolate population:

```text
whole-source global optimum
    -> R(K)=D/2+O(sqrt(D))
    -> all selected R(F_s)=D/2+O(sqrt(D))
    -> all P_*/D -> 2
    -> actual diameter-star angles -> 0
    -> selected loaded sets asymptotically antipodal
    -> actual response is nearly radial on coordinate fields.
```

This removes branches with a fixed force-perimeter deficit from two or a
fixed positive diameter-star angle. It does not bound the number of isolated
points, force-hull area deficit, response trace, individual stress weights,
or higher response eigenmodes.

The highest-value remaining bridge is a **whole-source capacity theorem in
this near-antipodal response regime**, not an abstract stability theorem
turning `P_* -> 2D` into matching support. An exact sufficient formulation is:

> **NC — full-population near-circular C-II exclusion.** For all sufficiently
> large contact/diameter-lexicographic triangle-free global sources, use their
> actual restored response and FS.1–FS.4 to prove
> `delta_K+O_A >= c_0 per(K)`, accounting for every source point, or construct
> an `n`-point unit-separated configuration of diameter `<D`.

The inequality contradicts (1.1) exactly. NC is **not proved** here; its
formula is an explicit target, not a new theorem. The added information is
that one may restrict the search to the uniform near-circular/near-antipodal
regime, and must survive the exact shell obstruction to the two attempted
response shortcuts.

## 9. Claim and regression audit

| Claim | Classification | Decisive reason |
| --- | --- | --- |
| Full-source `R-r<eta` | Already canonical | Source part of Section 155, rechecked with exact hypotheses |
| Every selected force hull has `R(F_s)<D/2+eta` | Proved consequence | Containment and a genuine diameter edge |
| Uniform `P_*=2D-O(sqrt(D))` | Proved consequence, not yet promoted | C10 virial bound plus source circumradius |
| Shared-endpoint angle `O(D^{-1/4})` | Proved | Acute isosceles triangle circumradius |
| Uniform radialization on coordinate fields | Proved | Exact midpoint identity and C11 |
| Near matching after deleting `o(1)` beta mass | Rejected under the tested response/geometric hypotheses | Odd-cycle shell loses asymptotically half the mass |
| Near-maximal force perimeter implies a small C41 defect | Rejected under the tested response/geometric hypotheses | Shell has trace `2D_h^2-2` |
| All isolates are diametral or boundary-order | Not asserted | Heptagon-center regression remains binding |
| Same-D hull saturation also minimizes diameter pairs | Not asserted | No source modification is used |
| Restored PSD applies to arbitrary planar statics | Not asserted | Actual C53 hypotheses retained |
| Generic near-star electrical regression is eliminated | Not asserted | No conductance or arbitrary-data operator bound supplied |
| Near-equilateral rhombi give a density gap | Not asserted | No Target B rhombic structure imported |
| C-II / Level I closed | Not proved | NC and finite competitor construction remain open |

## 10. Literature and verification

The only external item checked was the already imported classical Bonnesen
inequality as recorded by Daniel A. Klain, *An Error Estimate for the
Isoperimetric Deficit*, Illinois Journal of Mathematics 49 (2005), 981–992,
Section 4, equation (6), page 990:
[author PDF](https://faculty.uml.edu/dklain/Klain-Isoperimetric.pdf).

Its exact hypotheses are a compact convex planar body, circumradius `R`,
and inradius `r`; its conclusion is `P^2-4pi area >= pi^2(R-r)^2`.
The input is applied only to the full source convex hull. It supplies no
packing relocation or quantitative conductance theorem. The existing
[literature entry](../literature_review.md) already records this import.

All new calculations above are algebraic or elementary geometric proofs.
No numerical packing search, spectral sampling, or global-optimality
certificate is used. The proof of the shell PSD statement covers all odd
`h>=5`, rather than extrapolating a finite computation.

## 11. Promotion recommendation and handoff

**Hold as report for independent audit.** The positive statements and the
two regression consequences have complete proofs and a self-audit, but no
independent promotion audit has occurred. A later promotion should update
the C16/C18 quantitative frontier and annotate the conditional circumradius
discussion in C10. It must not promote NC or unrelated downstream C-II work.

```text
LEVEL I STATUS: STILL OPEN.

Proved in this report:
For every global source and every normalized KKT stress,
  eta=3^(1/4)sqrt(D),
  D/2 <= R(F_s) <= R(K) < D/2+eta,
  0 <= 2D-P_* < 4eta/(1+2eta/D),
  shared diameter-star angles < 2acos(D/(D+2eta)) = O(D^(-1/4)).
Diameter midpoints are O(D^(3/4)) from one source circumcenter;
the actual response is nearly radial on its coordinate fields.
All source points, including isolates, enter the initial Oler bound.

New audited obstruction within the working report:
Regular odd shells have 2D-P_* ~ 1/(4D), but any matching retains at
most asymptotically half their beta weight, and tr(Lambda-L_H)=2D^2-2.
Their actual response is PSD with affine kernel. Dense isolated filling
preserves this. No global-optimality certificate is claimed for the family.

Remaining exact target:
Prove the whole-population NC capacity inequality
  delta_K+O_A >= (sqrt(3)/4)per(K),
or produce a strict sub-D competitor in this near-antipodal C-II class.
No operator-norm, matching-support, or local-release shortcut is justified.

Authority:
The controlling September 9 C-I audit and existing route map remain unchanged.
This report is unpromoted; no claim that C-II is solved.
```
