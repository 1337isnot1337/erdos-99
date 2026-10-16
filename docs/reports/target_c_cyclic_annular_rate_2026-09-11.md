<!-- theorem-state: {"artifact_id":"ART-C93C429CD6D7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# SUPERSEDED / CONDITIONAL — cyclic annular-rate reduction for contact-isolated points

> **Audit correction.** This report is not an established theorem. Its Step 3 uses
> the inward outer-pocket estimate from the September 10 cyclic detour report. The
> current dependency audit shows that estimate's Reuleaux-cap containment is false:
> an inward OP pocket lies on the opposite side of its force-hull chord from the
> exterior Reuleaux cap. The six-point regular pentagon-plus-center global minimizer
> gives an explicit finite counterexample to the local inequality. Therefore the
> conclusions depending on Step 3 are withdrawn pending a replacement detour proof.

**Date:** 2026-09-11  
**Repository state:** `origin/main` at `053e1e1` for the September 10 report stack  
**Run type:** closing-proof attempt / exact branch reduction  
**Target:** Target C C-II, post-ZF cyclic branch  
**External web search:** not used for the proof  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

This report proves a quantitative full-source reduction in the cyclic `s_Z=0`
branch. It removes the quadratic outer-shell alternative from the isolate-population
ledger. A quadratic contact-isolated population, if present, must lie in a bounded
exceptional contact face whose perimeter is `Omega(D)`.

The giant exceptional-face alternative remains unresolved.

## 1. Starting endpoint

In the cyclic Woodall branch, the odd diameter cycle gives a Reuleaux container. The
September 10 reports prove

\[
 P_F=\pi D-O(\sqrt D),\qquad b-P_F=O(\sqrt D),
\tag{1.1}
\]

where `F` is the actual force hull and `b` is the outer contact-face walk length.
The existing isolate ledger allows two macroscopic possibilities: a quadratic
population in the outer contact face, or a quadratic population in a large bounded
exceptional face. The target here is the strict implication

```text
cyclic perimeter/detour rates
    -> all exterior and outer-face source population is o(D^2)
    -> any quadratic invisible population forces a linear-perimeter exceptional face.
```

## 2. Strongest genuinely new audited theorem

### Theorem CAR — quantitative cyclic isolate localization

Let `A_D` be an unbounded sequence of post-ZF triangle-free global minimizers in the
Woodall cyclic branch with `s_Z=0` and `d_H=0`, selected as in C-II and retaining all
source points. Let `D` be the diameter, `F` the actual selected force hull, and let
`Z_D` be the set of contact-isolated source points. Let `K=conv A_D`. Then there is an
absolute constant `C` such that, for all sufficiently large members of the sequence,

\[
\boxed{
 |Z_D\setminus F|+|Z_D\cap \operatorname{Out}(C_+)|
 \le C D^{7/4},
}
\tag{2.1}
\]

where `Out(C_+)` denotes the outer contact-face region inside `F` (equivalently, the
union of the outer pockets in the outer-pocket augmentation).

Consequently, if

\[
 |Z_D|\ge \eta D^2
\tag{2.2}
\]

along a subsequence for some fixed `eta>0`, then some bounded nonquadrilateral contact
face has perimeter at least

\[
\boxed{c_\eta D}
\tag{2.3}
\]

for all sufficiently large members of that subsequence, with `c_eta>0` depending
only on `eta` and the universal constants in the cyclic reports.

More quantitatively, if `K_D` is the largest bounded exceptional-face perimeter,
then

\[
\boxed{
 |Z_D|
 \le C D^{7/4}+C(K_D+1)D.
}
\tag{2.4}
\]

The theorem is a statement about the actual full source; no hull saturation is added
to the lexicographic choice and no source point is discarded.

### Proof

#### Step 1: force-hull area is within `O(D^{7/4})` of the disk bound

The full-source circumradius/response report supplies a centrally symmetric body `S`
associated with `F` such that

\[
\operatorname{diam}S=D,
\qquad \operatorname{per}S=\operatorname{per}F,
\tag{2.5}
\]

and, with `L_D=O(D^{3/4})`,

\[
0\le \operatorname{area}S-\operatorname{area}F
\le L_D\operatorname{per}F+\pi L_D^2.
\tag{2.6}
\]

The symmetric Rogalski--Saint Raymond inequality used in the September 10 joint
cavity report is

\[
\operatorname{area}S
\ge c_R\left(\frac{\operatorname{per}S}{2}-D\right)^2,
\qquad
c_R=\frac{\pi}{(\pi-2)^2}.
\tag{2.7}
\]

Write `s_D=\pi D-P_F`. By the cyclic Reuleaux perimeter theorem,
`0\le s_D=O(\sqrt D)`. Since `per S=P_F`, (2.7) gives

\[
\begin{aligned}
\operatorname{area}S
&\ge c_R\left(\left(\frac\pi2-1\right)D-\frac{s_D}{2}\right)^2\\
&=\frac\pi4D^2-O(D^{3/2}),
\end{aligned}
\tag{2.8}
\]

because

\[
c_R\left(\frac\pi2-1\right)^2=\frac\pi4.
\]

The error in (2.6) is `O(D^{7/4})`, so (2.8) yields

\[
\boxed{
\operatorname{area}F\ge\frac\pi4D^2-C_1D^{7/4}.
}
\tag{2.9}
\]

This is only a rate statement; it does not assert that the force hull is exactly a
disk or that the source hull is saturated.

#### Step 2: exterior source points are `O(D^{7/4})`

The full source hull `K` has diameter `D`, so the isodiametric inequality gives

\[
\operatorname{area}K\le\frac\pi4D^2.
\tag{2.10}
\]

Also `F\subseteq K`. Hence (2.9) gives

\[
\operatorname{area}K-\operatorname{area}F=O(D^{7/4}).
\tag{2.11}
\]

Use the finite annular Voronoi capacity theorem AV for the nested convex bodies
`F\subseteq K`. Its exact statement is

\[
|X|
\le\frac2{\sqrt3}\left(
\operatorname{area}K-\operatorname{area}F
 +\operatorname{per}K+\operatorname{per}F+\pi
\right)
\tag{2.12}
\]

for every unit-separated set `X\subseteq K\setminus\operatorname{int}F`.
Take `X=Z_D\setminus\operatorname{int}F`; boundary points may be assigned to `F`.
Both convex bodies have perimeter at most `\pi D`, by Cauchy's diameter-perimeter
inequality. Combining (2.11)--(2.12) gives

\[
\boxed{|Z_D\setminus F|=O(D^{7/4}).}
\tag{2.13}
\]

#### Step 3: the outer contact-face region has area `O(D^{7/4})`

Let `H_out` denote the area of the outer contact-face region, equivalently the sum of
the outer-pocket areas in the outer-pocket augmentation. The audited cyclic detour
estimate gives

\[
H_{out}\le\frac1{\sqrt6}(x_B+a)^{3/2}\sqrt{b-P_F},
\tag{2.14}
\]

where `x_B=b-q`, `a` is the number of missing force-hull sides, and `q` is the
number of loaded force-hull vertices. In the cyclic branch `q\le P_F\le\pi D`,
`b=O(D)`, and `a\le q`; consequently `x_B+a=O(D)`. By (1.1),
`b-P_F=O(\sqrt D)`. Therefore

\[
\boxed{H_{out}=O(D^{7/4}).}
\tag{2.15}
\]

The outer-face Oler estimate from the cyclic rhombus-transport report is

\[
Z_{outface}
\le \frac1{a_0}H_{out}+\frac{P_F-b}{2},
\qquad a_0=\frac{\sqrt3}{2}.
\tag{2.16}
\]

Since `P_F\le b`, the second term is nonpositive; retaining it only strengthens the
bound. From (2.15),

\[
\boxed{Z_{outface}=O(D^{7/4}).}
\tag{2.17}
\]

This is the promised elimination of the cyclic outer-shell phase at quadratic scale.

#### Step 4: exceptional faces and the largest perimeter

Let the bounded exceptional faces be `F_i`, with boundary perimeters `k_i` and let
`z_i` be the contact-isolated source points in `F_i`. The exact face-defect budget in
the cyclic circuit branch is

\[
Q=\sum_i(k_i-4)=O(D),
\tag{2.18}
\]

by the finite C42 face budget `B+Q\le4q-4` and `q\le\pi D`. Since each exceptional
face contributes at least one to `Q`, also `f\le Q` and
`\sum_i k_i=4f+Q\le5Q=O(D)`.

Oler applied to the convex equilateral `k_i`-gon `F_i` and its `z_i` interior source
points gives

\[
a_0(k_i+z_i-1)
\le \operatorname{area}(F_i)+c_0k_i,
\qquad c_0=\frac{a_0}{2}.
\tag{2.19}
\]

The isoperimetric inequality gives `area(F_i)\le k_i^2/(4\pi)`. Hence there is a
universal `C_2` such that

\[
z_i\le C_2(k_i^2+k_i+1).
\tag{2.20}
\]

Summing and using `\sum_i k_i=4f+Q=O(D)` and `k_i\le K_D` gives

\[
Z_{exc}:=\sum_i z_i
\le C_2\left(K_D\sum_i k_i+\sum_i k_i+f\right)
\le C_3(K_D+1)D.
\tag{2.21}
\]

Every source point not in the nonisolated contact core is either exterior to `F`, in
the outer contact-face region, or in a bounded exceptional face: strict quadrilateral
faces contain no additional unit-separated source point, and a point in a bounded
contact face with a unit contact would be a vertex of the actual contact graph.
Therefore

\[
|Z_D|\le |Z_D\setminus F|+Z_{outface}+Z_{exc}.
\tag{2.22}
\]

Substituting (2.13), (2.17), and (2.21) proves (2.4), after increasing the constant.

If `|Z_D|\ge\eta D^2`, then (2.4) implies

\[
C D^{7/4}+C(K_D+1)D\ge\eta D^2.
\]

For large `D`, the first term is at most `(eta/2)D^2`, so
`K_D\ge c_\eta D`, proving (2.3). `square`

## 3. Dependencies and scope audit

The proof uses the following precise inputs.

1. **Cyclic perimeter/detour:**
   `docs/reports/target_c_cyclic_reuleaux_perimeter_surplus_2026-09-10.md` and
   `docs/reports/target_c_cyclic_reuleaux_cap_detour_2026-09-10.md`, for (1.1) and
   (2.14).
2. **Finite central-symmetral transfer and RS inequality:**
   `docs/reports/target_c_symmetric_area_perimeter_joint_cavity_2026-09-10.md`,
   equations (1.2)--(1.4), including the finite `L_D=O(D^{3/4})` error and the
   exact constant `c_R=\pi/(\pi-2)^2`.
3. **Annular Voronoi capacity:**
   `docs/reports/target_c_annular_voronoi_matching_exclusion_2026-09-10.md`,
   Theorem AV. The proof there uses the stated scaled minimal Voronoi-cell theorem;
   its hypotheses are a maximal locally finite unit-separated extension and bounded
   cells, both checked in that report.
4. **Cyclic rhombus/exceptions:**
   `docs/reports/target_c_cyclic_rhombus_excess_transport_2026-09-10.md`, for the
   `Q=O(D)` circuit budget, the outer-face Oler estimate, and the complete source
   partition.

No claim is made that the unpromoted reports are canonical theorem modules. Each is
used only with the exact proof passage stated above.

## 4. Exact target implication

The previous cyclic population ledger had the alternative

```text
quadratic isolates in the outer contact face
or a bounded exceptional face of perimeter Omega(D).
```

Theorem CAR removes the first alternative and strengthens the second to the explicit
bound (2.4). Thus the cyclic branch has only these remaining possibilities:

1. the nonisolated contact core contains `n-O(D^{7/4})` source points; or
2. one bounded exceptional face has perimeter `Omega(D)` and carries the macroscopic
   contact-isolated population.

This does not close the branch. The giant face can still have perimeter `Theta(D)` and
contain a `Theta(D^2)` unit-separated population in principle; the current theorem
does not supply a strict diameter competitor or a quantitative density gap in that
face.

## 5. Exact remaining lemma

The shortest missing statement is now:

> **Cyclic giant-face exclusion.** In a cyclic `s_Z=0` C-II global minimizer with
> `P_F=\pi D-O(\sqrt D)`, a bounded exceptional contact face of perimeter `Theta(D)`
> cannot contain `Theta(D^2)` contact-isolated source points.

It must be proved using the actual full source and global minimum-diameter comparison;
ordinary isoperimetry, local jamming, or an independently optimized scaffold is not
enough.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
|---|---|---|
| `P_F=\pi D-O(\sqrt D)` and `b-P_F=O(\sqrt D)` | inherited proved report-level inputs | exact cyclic Reuleaux/detour arguments |
| finite symmetric-area transfer (2.6) | inherited proved report-level input | explicit Hausdorff/area estimate |
| (2.9) force-hull area rate | proved here | RS expansion plus (2.6) |
| exterior isolate bound (2.13) | proved here | AV applied to actual `K,F` |
| outer-face isolate bound (2.17) | proved here | DD.2 plus outer-face Oler |
| exceptional-face bound (2.21) | proved here | facewise Oler and `Q=O(D)` |
| complete source partition (2.22) | proved under C49/C51 face hypotheses | every remaining source point is isolated or a core vertex |
| giant-face exclusion | not proved | linear-perimeter face can hold quadratic near-unit packing |

## 7. Regression tests

| Regression | Result | Reason |
|---|---|---|
| contact-isolated points outside `F` | retained | AV counts them in the actual annulus `K\setminus F` |
| outer repeated-walk edges | retained | `b` counts edge occurrences and (2.14) uses `b-P_F` |
| exceptional faces | retained | all face perimeters and face populations are summed explicitly |
| regular odd shells | outside scope | they have `s_Z=2`, not the cyclic circuit hypothesis `s_Z=0` |
| common bridge block | irrelevant to rate proof | no bridge transfer is inferred |
| giant exceptional face | survives | (2.4) deliberately leaves `K_D=Theta(D)` open |
| near-equilateral equality well | survives | no fixed angular-density gap is assumed |

## 8. Failed route

The tempting implication

```text
P_F=pi D-O(sqrt D) -> area(F)=pi D^2/4-O(D^{3/2})
```

is not used. It is false for general diameter-`D` convex bodies without the finite
central-symmetral transfer: a Reuleaux-type body can have perimeter close to `pi D`
while its area is bounded away from the disk area. The proof uses the actual response
transport (2.5)--(2.6), which is why it is specific to the C-II global source stack.

## 9. Canonical promotion recommendation

**Hold as report.** The theorem is auditable but depends on several unpromoted
September 10 reports. It should not change the route map until those dependencies are
promoted or independently audited.

## 10. Next run

Attack the giant-face branch by a source-specific annular/face comparison. The most
promising exact target is to combine the facewise Oler inequality with the global strict
lattice comparison and the cyclic `E=O(D)` rhombus-defect transport, retaining the
quadratic population inside the one giant face rather than replacing it by an
independently chosen scaffold.

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New Theorem CAR (cyclic s_Z=0,d_H=0):
  P_F=pi D-O(sqrt D), b-P_F=O(sqrt D), and finite central-symmetral transfer give
      area(F)>=pi D^2/4-O(D^(7/4)).
  Annular Voronoi capacity applied to K=conv A and F gives
      #source points outside F = O(D^(7/4)).
  The outer-pocket detour bound gives H_out=O(D^(7/4)); outer-face Oler then gives
      #outer-face isolated points = O(D^(7/4)).
  If K_D is the largest bounded exceptional-face perimeter and Q=O(D), facewise Oler
  gives
      #isolates in exceptional faces <= O((K_D+1)D).
  Therefore
      #all contact-isolated points <= O(D^(7/4))+O((K_D+1)D).

  A quadratic invisible population forces K_D=Omega(D), so the cyclic branch has no
  diffuse/outer-shell population phase. The sole remaining population obstruction is
  one linear-perimeter exceptional face containing a quadratic isolated packing.

Remaining exact lemma:
  exclude that giant exceptional face using the actual global minimizer and all source
  points; no local-density or scaffold argument suffices.
```
