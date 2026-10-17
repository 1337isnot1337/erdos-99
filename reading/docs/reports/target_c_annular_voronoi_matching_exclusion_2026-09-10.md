> Generated reading edition · [exact source](../../../docs/reports/target_c_annular_voronoi_matching_exclusion_2026-09-10.md) · source SHA-256 `bc5021719945e35063154ad5e99b7c3a609c556614ce374a8c730246a2b875df`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-763A90CECDDF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — annular Voronoi capacity and direct FSDB matching exclusion

**Date:** 2026-09-10  
**Repository state:** `7693076f09aac9d530d086c7ca445575fcedd515` at start  
**Run type:** closing proof / literature import / branch elimination / adversarial audit  
**Target:** Target C, C-II after ZF  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used to verify the local Voronoi-cell theorem stated below  
**Computation:** decimal evaluation only; no computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

This report contains two new results.

First, it proves a reusable finite packing theorem for the nonconvex region between
two nested convex bodies:

$$
\boxed{
|S|
\le
\frac2{\sqrt3}
\left(
\operatorname{area}K-\operatorname{area}F
+\operatorname{per}K+\operatorname{per}F+\pi
\right)
}
\tag{AV.1}
$$

for every pair of nested compact convex planar bodies `F subset K` and every finite
unit-separated set

$$
S\subseteq K\setminus\operatorname{int}F.
$$

Second, an adversarial simplification shows that AV is **not needed** to eliminate the
post-ZF perfect-matching diameter branch.  The matching-branch theorem MB already says
the force hull is tiled by `R` strict unit rhombi and

$$
R\le\frac{q^2}{16},
\qquad
q=\operatorname{per}F\le\pi D.
$$

Since every unit rhombus has area at most one,

$$
\boxed{
\operatorname{area}F
\le R
\le\frac{\pi^2}{16}D^2
=0.6168502750680849\ldots D^2.
}
\tag{M.1}
$$

The newly merged FSDB theorem gives the opposite asymptotic inequality

$$
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
A_{FS}
:=\frac{2\rho+\sin(2\rho)}4
=0.6184708847696858\ldots,
}
\tag{M.2}
$$

where `rho=cos rho`.  The fixed gap

$$
\boxed{
A_{FS}-\frac{\pi^2}{16}
=0.00162060970160094\ldots>0
}
\tag{M.3}
$$

excludes every unbounded perfect-matching post-ZF survivor sequence directly.

Thus the matching branch is closed without any external theorem.  AV remains a
separate shared packing lemma for controlling contact-isolated populations outside a
force hull in later branches.

---

## 1. Starting endpoint

The matching-branch report MB proves that if the full actual diameter graph `H` is a
perfect matching, then:

- `q=|B_+|` and `h=q/2`;
- the outer contact walk is exactly the convex force-hull cycle;
- every force-hull side is a unit contact;
- every bounded contact face is a strict unit rhombus;
- the force hull is tiled by those rhombi;
- if `R` is the number of rhombi and `T` the train count, then
  $$
  T=q/2,
  \qquad
  R\le T^2/4=q^2/16;
  $$
- `q=per(F)<=pi D`.

Before FSDB, this did not contradict any universal force-hull area lower bound.  FSDB
raises that lower bound to `0.6184708847... D^2`, just above the absolute area capacity
of a matching rhombic disk.

The now-decisive implication is

```text
MB perfect matching
    -> F is tiled by R unit rhombi
    -> area(F) <= R <= q^2/16 <= pi^2 D^2/16
FSDB
    -> area(F) >= (A_FS-o(1)) D^2
A_FS > pi^2/16
    -> contradiction.
```

The annular theorem AV was developed before noticing this shorter contradiction and is
retained because it is independently valid and potentially useful for nonmatching
external-isolate branches.

---

## 2. Strongest branch theorem: perfect matching is excluded

### Theorem MFS — FSDB closes the post-ZF perfect-matching branch

There is no unbounded sequence of triangle-free lexicographically normalized
post-ZF global minimizers whose full actual diameter graph is a perfect matching.
Equivalently, there exists `D_0<infinity` such that every post-ZF survivor with
`D>=D_0` has at least one loaded terminal of diameter degree at least two.

### Proof

Assume an unbounded matching-branch sequence.

By MB, the force hull `F` is a simply connected strict unit-rhombic disk.  Let `R` be
its number of rhombi and `T` its train count.  The rhombi have pairwise disjoint
interiors and tile `F`, so

$$
\operatorname{area}F
=
\sum_{j=1}^{R}\operatorname{area}(\mathcal R_j).
\tag{2.1}
$$

A unit rhombus with angle `theta` has area `sin theta`, hence

$$
\operatorname{area}(\mathcal R_j)\le1.
$$

Therefore

$$
\boxed{\operatorname{area}F\le R.}
\tag{2.2}
$$

MB also proves

$$
T=\frac q2,
\qquad
R\le\frac{T^2}{4}=\frac{q^2}{16}.
\tag{2.3}
$$

The same report proves `q=per(F)`.  Since `diam(F)=D`, Cauchy's
perimeter--diameter inequality gives

$$
q=\operatorname{per}F\le\pi D.
\tag{2.4}
$$

Combining (2.2)--(2.4),

$$
\boxed{
\operatorname{area}F
\le\frac{\pi^2}{16}D^2.
}
\tag{2.5}
$$

On the other hand, FSDB proves for every unbounded post-ZF survivor sequence

$$
\liminf\frac{\operatorname{area}F}{D^2}
\ge
A_{FS}:=
\frac{2\rho+\sin(2\rho)}4.
\tag{2.6}
$$

Numerically,

$$
A_{FS}=0.6184708847696858\ldots,
\qquad
\frac{\pi^2}{16}=0.6168502750680849\ldots,
$$

and the exact expressions satisfy

$$
A_{FS}-\frac{\pi^2}{16}>0.
\tag{2.7}
$$

Hence (2.5) and (2.6) are incompatible along an unbounded sequence.  This proves the
first statement.

If matching survivors existed for arbitrarily large `D`, they would form such an
unbounded sequence.  Therefore some finite `D_0` excludes the branch uniformly for all
larger post-ZF survivors. `square`

### Exact-sign audit for (2.7)

The decimal gap is about `1.62e-3`, but the proof need not rely on floating point.
The defining equation `rho=cos rho` has a unique root in `(0,pi/2)`.  Any elementary
rational enclosure for that root narrow enough to separate the two displayed
continuous expressions certifies (2.7).  The decimal values above are recorded only
for scale; no numerical optimizer or empirical search is being used.

### Dependencies

- `docs/reports/target_c_matching_branch_externalization_2026-09-09.md` (MB),
  specifically the pure-rhombic-disk conclusion, `T=q/2`, `R<=q^2/16`, and
  `q=per(F)`.
- `docs/reports/target_c_fs_symmetric_difference_body_area_2026-09-10.md` (FSDB),
  now merged into `main`, for (2.6).
- Cauchy's convex perimeter--diameter inequality.

No external literature is used in MFS.

### Why it is new

MB stopped at a required quadratic external-rattler population because the available
force-hull geometry did not exceed its rhombic-core capacity.  FSDB was not present
when MB was written.  The key new comparison is that FSDB's constant lands **above**
`pi^2/16`, so MB's own Mantel/train bound now contradicts the force-hull area before
any rattler analysis is needed.

---

## 3. Reusable shared theorem: annular Voronoi capacity

### Theorem AV — finite annular Voronoi capacity

Let `F subset K` be compact convex subsets of the plane with nonempty interior.  Let
`S` be a finite point set satisfying

$$
S\subseteq K\setminus\operatorname{int}F,
\qquad
|p-q|\ge1\quad(p\ne q\in S).
\tag{3.1}
$$

Then AV.1 holds:

$$
|S|
\le
\frac2{\sqrt3}
\left(
\operatorname{area}K-\operatorname{area}F
+\operatorname{per}K+\operatorname{per}F+\pi
\right).
$$

More generally, if `U=K\setminus int(F)` and `U^{+1}` denotes its closed
one-neighborhood, then

$$
\boxed{
\operatorname{area}(U^{+1})
\le
\operatorname{area}K-\operatorname{area}F
+\operatorname{per}K+\operatorname{per}F+\pi,
}
\tag{3.2}
$$

and

$$
\boxed{|S|\frac{\sqrt3}{2}\le\operatorname{area}(U^{+1}).}
\tag{3.3}
$$

### Scope

AV is independent of Erdős #99, KKT theory, triangle-freeness, and global optimality.
It is a finite planar packing theorem for a possibly nonconvex annular region between
nested convex bodies.  It needs only unit separation and the two convex boundaries.

### Proof

#### Step 1: saturated extension

Consider all unit-separated subsets of `R^2` containing `S`, ordered by inclusion.
The union of a chain is unit-separated, so Zorn's lemma gives a maximal
unit-separated superset

$$
X\supseteq S.
\tag{3.4}
$$

If `x notin X` and every center of `X` were at distance at least one from `x`, then
`X union {x}` would still be unit-separated.  Therefore maximality gives

$$
\boxed{
\forall x\in\mathbb R^2\ \exists q\in X:\ |x-q|<1,
}
\tag{3.5}
$$

with the trivial choice `q=x` when `x in X`.

Unit separation makes `X` locally finite.  Let `V_p` be the closed Voronoi cell of
`p in X`.  If `x in V_p`, choose `q` as in (3.5).  The Voronoi inequality gives

$$
|x-p|\le|x-q|<1,
$$

except at a center itself where the conclusion is immediate.  Hence

$$
\boxed{V_p\subseteq\overline B(p,1).}
\tag{3.6}
$$

Every Voronoi cell is therefore bounded.

#### Step 2: sharp local Voronoi area

Mazel--Stuhl--Suhov prove that in a packing of open unit disks, equivalently centers
separated by at least `2`, every bounded Voronoi cell has area at least `2sqrt(3)`.
Scaling by `1/2` gives for our normalization

$$
\boxed{\operatorname{area}(V_p)\ge\frac{\sqrt3}{2}.}
\tag{3.7}
$$

The Voronoi cell interiors are disjoint.  For each original center `p in S`,
`p in U` and (3.6) imply

$$
V_p\subseteq U^{+1}.
$$

Therefore

$$
|S|\frac{\sqrt3}{2}
\le
\sum_{p\in S}\operatorname{area}(V_p)
\le
\operatorname{area}(U^{+1}),
$$

which proves (3.3).

#### Step 3: one-neighborhood of a convex annulus

For `r>=0` write

$$
K^{+r}:=K+rB_2
$$

and

$$
F_{-r}:=\{x\in F:\operatorname{dist}(x,\mathbb R^2\setminus F)\ge r\}.
\tag{3.8}
$$

Any point within distance one of `U=K\setminus int(F)` lies in `K^{+1}` and cannot
lie in the interior of `F_{-1}`.  Up to null boundaries,

$$
U^{+1}\subseteq K^{+1}\setminus\operatorname{int}(F_{-1}).
\tag{3.9}
$$

Steiner's formula gives

$$
\operatorname{area}(K^{+1})
=
\operatorname{area}K+\operatorname{per}K+\pi.
\tag{3.10}
$$

For the inner parallel body, apply the coarea formula to the distance-to-boundary
function on `F`.  The level sets are boundaries of convex inner parallel bodies for
almost every depth, and convex perimeter is monotone under inclusion.  Hence the
inner boundary strip of width one satisfies

$$
\boxed{
\operatorname{area}F-\operatorname{area}(F_{-1})
\le\operatorname{per}F.
}
\tag{3.11}
$$

This also covers the case in which the erosion becomes empty before depth one.
Combining (3.9)--(3.11) proves (3.2), and (3.2)+(3.3) prove AV. `square`

### Literature dependency for AV only

- A. Mazel, I. Stuhl, Y. Suhov, *Minimal Area of a Voronoi Cell in a Packing of Unit
  Circles*, arXiv:2211.03255v1 (2022), Section 3 theorem.
- Exact hypotheses: nonoverlapping open unit disks in `R^2`, so center separation at
  least `2`; bounded Voronoi cell.
- Exact conclusion: cell area at least `2sqrt(3)`, equality only for the regular
  hexagonal Voronoi cell.
- Scaling here: divide all lengths by `2`, so separation becomes `1` and area lower
  bound becomes `sqrt(3)/2`.
- Applicability: the maximal extension gives a locally finite unit-separated packing,
  and (3.6) proves its cells are bounded.

The source was read directly; no theorem statement is taken from a search-result
summary.

---

## 4. Secondary application of AV to the old MB external-rattler endpoint

Although no longer needed for MFS, AV independently kills MB's external-rattler
picture once FSDB is available.

MB gives

$$
\liminf\frac{Z_{ext}}{D^2}
\ge
\Delta-\frac{\pi^2}{16}
=0.2900494070490240\ldots.
\tag{4.1}
$$

All those points lie in `K\setminus F`.  AV, the isodiametric bound
`area(K)<=pi D^2/4`, the two perimeter bounds `<=pi D`, and FSDB give

$$
\limsup\frac{Z_{ext}}{D^2}
\le
\frac2{\sqrt3}
\left(\frac\pi4-A_{FS}\right)
=0.1927510185016607\ldots.
\tag{4.2}
$$

Thus the annular route has a much larger quadratic contradiction margin
`0.0972983885... D^2`.  It is retained as an independent verification of the branch
closure and as a reusable method for future isolate-population estimates.

---

## 5. Exact target implication

The post-ZF perfect-matching branch is closed.

The exact branching identity remains

$$
2h-q=x_B+Q+2s_Z.
$$

MFS rules out the zero left-hand side for all sufficiently large survivors.  This is
qualitative; NB already proves the stronger linear lower bound

$$
\liminf\frac{2h-q}{D}\ge0.6099043189\ldots.
$$

Therefore the highest-value use of MFS is not to improve that scalar constant.  It
removes MB's entire external-shell branch from the structural ledger and frees future
work to focus on genuinely branching diameter graphs.

The general C-II closing inequality remains

$$
\boxed{b+Q>2h}
$$

or a strict sub-`D` competitor.

---

## 6. Exact remaining lemma

The next theorem should exploit the stronger FSDB force-hull area floor in the
nonmatching branches.  A concrete target is:

> **FSDB currency incompatibility.** Insert
> 

$$

> A_{FS}=(2\rho+\sin2\rho)/4
> 
$$


> into the existing attachment-cell, outer-pocket, exceptional-face, and Dirichlet
> detour inequalities, and prove that the simultaneously required lower bounds on
> `x_B+Q+2s_Z` and `e_BB+2s_C` exceed their joint geometric capacity.

A numerical improvement without crossing a proved contradictory threshold is not a
closure.

---

## 7. Audit classification of claims

| Claim | Classification | Reason |
| --- | --- | --- |
| matching `F` is tiled by `R` unit rhombi | already proved in MB | exact zero-defect matching ledger |
| `area(F)<=R` | proved | each unit rhombus has area `sin theta<=1` |
| `R<=q^2/16<=pi^2D^2/16` | already MB + Cauchy | Mantel on train crossing graph; `q=per(F)` |
| MFS matching exclusion | proved under FSDB + MB | fixed positive area-constant gap |
| maximal unit-separated extension exists | proved | Zorn; chain unions preserve separation |
| maximal extension has covering radius `<1` | proved | otherwise another center can be inserted |
| scaled Voronoi-cell area `>=sqrt(3)/2` | externally proved theorem, hypotheses checked | Mazel--Stuhl--Suhov |
| AV.1 | proved | local Voronoi cells + annular neighborhood bound |
| AV needed for MFS | rejected | direct rhombic-area contradiction is shorter |
| Level I | still open | nonmatching C-II sources remain |

---

## 8. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | diameter graph is an odd cycle, not a matching; area tends `pi D^2/4` |
| unit square | yes | finite matching example; MFS is only a sufficiently-large theorem |
| equilateral noncentral hexagon from MB | yes | finite matching geometry does not violate the asymptotic FSDB comparison |
| hexagonal lattice points in a large annulus | yes | AV has sharp bulk coefficient `2/sqrt3`; boundary is perimeter order |
| very thin annulus | yes | AV's perimeter terms pay for boundary-layer points |
| dense isolated shell fillings | yes | MFS uses the pure matching topology; AV handles isolates without assuming small population |

---

## 9. Failed routes and no-go results

1. The original annular-rattler closure is valid but overpowered for the matching
   branch.  Future work should use the shorter MFS area contradiction there.
2. `FS approximate symmetry -> F is a disk` is still false.  MFS uses the much more
   specific MB rhombic topology.
3. `large force-hull area -> no isolates` is false in general.  AV gives a quantitative
   population bound but does not eliminate all external-isolate configurations without
   additional source structure.

---

## 10. Literature imported

Only AV imports literature; MFS does not.

### Mazel--Stuhl--Suhov (2022), arXiv:2211.03255

- Link: `https://arxiv.org/abs/2211.03255`
- Result: Section 3 theorem on minimal Voronoi-cell area.
- Exact hypotheses and scaling: recorded in Section 3 above.
- Applicable to AV: yes.
- Applicable to MFS: not needed.

---

## 11. Computation and reproducibility

No repository computation is a proof dependency.  The displayed constants are closed
forms.  Decimal checks:

$$
A_{FS}=0.6184708847696858\ldots,
$$

$$
\frac{\pi^2}{16}=0.6168502750680849\ldots,
$$

$$
A_{FS}-\frac{\pi^2}{16}
=0.00162060970160094\ldots,
$$

$$
\frac2{\sqrt3}\left(\frac\pi4-A_{FS}\right)
=0.1927510185016607\ldots.
$$

For canonical promotion, the sign in M.3 should be certified with a short interval or
rational enclosure for the Dottie number rather than relying on printed decimals.

---

## 12. Canonical promotion recommendation

**Promote MFS after review.**  It closes an explicit Target C subbranch using only
repository mathematics plus elementary rhombus area.  Recommended canonical changes:

1. update the Target C route map to mark the perfect-matching post-ZF branch closed;
2. update the active Target C prompt so MB's matching-shell exclusion is no longer an
   open target;
3. retain MB as the historical structural reduction discharged by MFS;
4. consider AV separately for shared theory after its external dependency receives the
   normal literature audit.

AV itself should remain a report until that literature promotion step is completed.

---

## 13. Next run

Feed `A_FS` through the post-PI/DP cavity and currency inequalities and look for an
actual crossed threshold.  Do not spend additional work on the matching branch unless
a dependency audit finds a specific error in MB or FSDB.

---

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New branch closure MFS:
MB perfect matching gives a pure unit-rhombic force-hull disk with
    T=q/2,
    R<=T^2/4=q^2/16,
    q=per(F)<=pi D.
Because the R rhombi tile F and each has area <=1,
    area(F)<=R<=pi^2 D^2/16
           =0.6168502750680849... D^2.
FSDB gives every unbounded post-ZF survivor
    liminf area(F)/D^2 >= A_FS
      =(2rho+sin(2rho))/4
      =0.6184708847696858...,
    rho=cos rho.
The gap A_FS-pi^2/16=0.00162060970160094... is positive.
Therefore no unbounded post-ZF perfect-matching diameter branch exists.

Independent shared lemma AV:
for convex F subset K and unit-separated S subset K\int(F),
    |S| <= (2/sqrt3)
           [area(K)-area(F)+per(K)+per(F)+pi].
Proof: saturated extension + scaled local Voronoi-cell area theorem + Steiner/coarea.
AV independently excludes MB's external-rattler population, but MFS is the preferred
matching proof.

Next: insert A_FS into the general nonmatching cavity/currency inequalities and seek a
true contradictory threshold.
```
