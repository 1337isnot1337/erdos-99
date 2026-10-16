<!-- theorem-state: {"artifact_id":"ART-15B1A8F79BC2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — annular packing excludes the post-ZF perfect-matching branch

**Date:** 2026-09-10  
**Repository state:** branch `research/2026-09-10-c2-annular-matching-exclusion` from `7693076f09aac9d530d086c7ca445575fcedd515`  
**Run type:** closing proof / branch elimination / adversarial audit  
**Target:** Target C, C-II after ZF  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`, with the controlling September 9 update  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

This report proves the annular finite-packing theorem left open in the immediately preceding FS-symmetry report and uses it to eliminate the entire post-ZF branch in which the **full actual diameter graph is a perfect matching**.

The new geometric input is elementary but has the required sharp bulk coefficient. If `F subset K` are convex bodies of diameter at most `D` and `S subset K\F` is unit-separated, then

\[
\boxed{
|S|\le\frac2{\sqrt3}\bigl(\operatorname{area}K-\operatorname{area}F\bigr)
+O(D^{3/2}).
}
\tag{AP.1}
\]

The proof tiles by squares of side `sqrt(D)`: Oler is applied only to squares wholly inside the annulus, while the `O(sqrt(D))` squares meeting either convex boundary are charged by a crude local disk-packing bound. This preserves the triangular-lattice bulk coefficient and loses only `o(D^2)` points.

In the perfect-matching branch, MB requires at least

\[
\left(\frac\pi{2\sqrt3}-\frac{\pi^2}{16}\right)D^2-o(D^2)
\]

external isolated source points outside the force hull. FSDB gives

\[
\operatorname{area}F\ge A_{FS}D^2-o(D^2),
\qquad
A_{FS}=\frac{2\rho+\sin(2\rho)}4,\quad \rho=\cos\rho.
\]

AP therefore gives an asymptotic upper bound strictly below the MB lower bound. The contradiction is certified without decimal arithmetic by the coarse estimates

\[
\frac23<\rho<\frac\pi4,
\qquad
A_{FS}>\frac13+\frac{\sqrt3}{8},
\]

and

\[
\frac{2}{3\sqrt3}+\frac14-\frac{\pi^2}{16}>0.
\]

Level I remains open because nonmatching diameter graphs still survive.

---

## 1. Starting endpoint

The report
`docs/reports/target_c_matching_branch_externalization_2026-09-09.md`
proves, under the audited post-ZF stack, that if the full actual diameter graph is a perfect matching then:

1. the positive contact core is a pure simply connected strict-rhombic disk;
2. all contact-isolated source points lie outside the force hull `F`;
3. if `v` is the core population, then
   \[
   v\le\frac{q^2}{16}+\frac q2+1,
   \]
   with `q<=pi D`; and consequently
4. the external population `Z_ext=n-v` satisfies
   \[
   \boxed{
   \liminf\frac{Z_{ext}}{D^2}
   \ge
   \Delta-\frac{\pi^2}{16},
   \qquad
   \Delta:=\frac\pi{2\sqrt3}.
   }
   \tag{1.1}
   \]

The new September 10 FS-symmetry report proves for every unbounded post-ZF survivor sequence

\[
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_{FS}:=
\frac{2\rho+\sin(2\rho)}4,
\qquad
\rho=\cos\rho.
}
\tag{1.2}
\]

Since the full source hull `K` has `area(K)<=pi D^2/4`, the missing implication was exactly a sharp-leading-term packing bound for the nonconvex annulus `K\setminus F`:

```text
all matching-branch isolates lie in K\F
    + area(K\F) <= (pi/4-A_FS)D^2+o(D^2)
    + sharp-bulk annular packing
    -> too few positions for MB's required external population
    -> perfect-matching branch impossible.
```

The annular theorem below supplies this implication with an explicit `O(D^(3/2))` error.

---

## 2. Strongest genuinely new audited theorem

### Theorem AP — sharp-bulk packing in a convex annulus

Let `D>=1`. Let `F subset K` be compact convex planar sets with

\[
\operatorname{diam}K\le D.
\]

Let `S subset K\setminus F` be finite and unit-separated. Then

\[
\boxed{
|S|
\le
\frac2{\sqrt3}
\bigl(\operatorname{area}K-\operatorname{area}F\bigr)
+O(D^{3/2}),
}
\tag{AP.2}
\]

where the implied constant is universal. In particular, for any sequence with `D->infinity`,

\[
\boxed{
|S|
\le
\frac2{\sqrt3}
\operatorname{area}(K\setminus F)
+o(D^2).
}
\tag{AP.3}
\]

No contact, KKT, triangle-free, or global-optimality hypothesis is used in AP.

### Proof

Put

\[
L=\sqrt D.
\tag{2.1}
\]

Choose a translate of the axis-parallel square grid of side `L` such that no point of `S` lies on a grid line and no nontrivial line segment of `partial K` or `partial F` lies on a grid line. This is possible because only finitely many translations are forbidden for the point condition, and the boundary-segment coincidences occupy a measure-zero set of translations.

Assign each point of `S` to its unique open grid square.

Call a square **bulk** if the entire square is contained in `K\setminus F`. Every occupied square that is not bulk meets `partial K` or `partial F`: indeed it contains a point of `K\setminus F`; if some point of the same convex square lies outside `K`, the segment between the two points crosses `partial K`, while if some point lies in `F`, the segment crosses `partial F`.

#### Step 1: number of boundary squares

We use the following elementary grid-crossing count.

**Lemma AP.1.** If `C` is convex with diameter at most `D`, the number of open side-`L` grid squares meeting `partial C` is at most

\[
\boxed{4D/L+5.}
\tag{2.2}
\]

To prove this, traverse `partial C`. A vertical grid line meets the boundary of a convex body at at most two points, and only at most `D/L+1` vertical grid lines can meet `C`, because its horizontal width is at most `D`. Thus there are at most `2(D/L+1)` vertical crossings. The same bound holds for horizontal crossings. Between consecutive grid-line crossings the boundary stays in one open square. Hence the number of visited squares is at most the total number of crossings plus one, which gives (2.2). The generic grid translation removes coincident boundary segments; tangencies only reduce the crossing count. `square`

Apply AP.1 to both `K` and `F`. The total number `B` of occupied nonbulk squares therefore satisfies

\[
\boxed{B\le 8D/L+10.}
\tag{2.3}
\]

#### Step 2: sharp Oler count in bulk squares

Let `Q` be a bulk square and put `N_Q=|S cap Q|`. Oler's finite packing inequality applied to the closed side-`L` square gives

\[
N_Q
\le
\frac2{\sqrt3}L^2+2L+1.
\tag{2.4}
\]

The bulk squares have disjoint interiors and lie in `K\setminus F`. If `G` is their number, then

\[
GL^2\le\operatorname{area}(K\setminus F).
\tag{2.5}
\]

Summing (2.4) and using (2.5),

\[
\begin{aligned}
N_{bulk}
&\le
\frac2{\sqrt3}\operatorname{area}(K\setminus F)
+(2L+1)G\\
&\le
\frac2{\sqrt3}\operatorname{area}(K\setminus F)
+\left(\frac2L+\frac1{L^2}\right)
\operatorname{area}(K\setminus F).
\end{aligned}
\tag{2.6}
\]

Since `area(K)<=pi D^2/4`, the last term is `O(D^2/L)`.

#### Step 3: crude count in boundary squares

For any side-`L` square `Q`, put `M_Q=|S cap Q|`. The radius-`1/2` disks centered at these points are pairwise interior-disjoint and lie in the Euclidean `1/2`-parallel body of `Q`. By Steiner's formula for the square,

\[
M_Q\frac\pi4
\le
L^2+2L+\frac\pi4.
\]

Thus

\[
\boxed{
M_Q\le\frac4\pi L^2+\frac8\pi L+1.
}
\tag{2.7}
\]

Combining (2.3) and (2.7),

\[
N_{bdry}
\le
\left(\frac{8D}{L}+10\right)
\left(\frac4\pi L^2+\frac8\pi L+1\right)
=O(DL+L^2+D).
\tag{2.8}
\]

#### Step 4: choose the mesoscopic scale

With `L=sqrt(D)`, equations (2.6) and (2.8) give

\[
N_{bulk}
\le
\frac2{\sqrt3}\operatorname{area}(K\setminus F)
+O(D^{3/2}),
\]

and

\[
N_{bdry}=O(D^{3/2}).
\]

Adding them proves AP.2, and `D^(3/2)=o(D^2)` proves AP.3. `square`

### Scope

AP is a general finite packing theorem for a convex body with one nested convex forbidden body. It allows points arbitrarily close to either boundary. The inner boundary need not be smooth or strictly convex. The only asymptotic scale assumption used in AP.3 is `D->infinity`.

For Target C, take `K=conv A`, take `F` to be the force hull, and take `S` to be the source points known to lie outside `F`. Both bodies have diameter at most the source diameter `D`.

### Dependencies

- `docs/theory/03-oler-shell.md`, Lemma 21.1, applied separately to full bulk grid squares.
- elementary convexity and the disk-area packing bound in a square parallel body.
- Cauchy's diameter-area bound `area(K)<=pi D^2/4`, only to simplify the error term.

No external theorem is imported beyond the convex parallel-body formula already used in the current Target C report stack.

### Why it is new

The canonical Oler inequality applies to a convex container and cannot simply subtract the area of an empty inner convex body. AP provides the missing subtraction at the leading coefficient by localizing Oler away from the two boundaries. The only cells for which the annular nonconvexity matters are the `O(D/L)` boundary cells, so a mesoscopic choice `1<<L<<D` makes their cost subquadratic while the bulk Oler boundary term is also subquadratic.

The immediately preceding FSDB report stated AP.3 as its exact missing theorem for the matching branch; AP proves it with the stronger explicit `O(D^(3/2))` error.

---

## 3. The perfect-matching branch is excluded

### Theorem MEX — no unbounded post-ZF perfect-matching survivor sequence

Assume the audited/report-level post-ZF hypotheses used by MB and FSDB. There is no unbounded sequence of lexicographically normalized triangle-free global minimizers for which the **full actual diameter graph** is a perfect matching.

Equivalently, along every sufficiently large post-ZF survivor sequence, the full actual diameter graph has at least one vertex of diameter degree at least two.

### Proof

Suppose such a sequence exists. Let `K=conv A`, let `F` be the force hull, let `v` be the nonisolated contact-core population, and put

\[
Z_{ext}=n-v.
\]

MB proves that every one of these `Z_ext` source points lies in `K\setminus F` and that

\[
\liminf\frac{Z_{ext}}{D^2}
\ge
\Delta-\frac{\pi^2}{16},
\qquad
\Delta=\frac\pi{2\sqrt3}.
\tag{3.1}
\]

FSDB proves

\[
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_{FS}
:=\frac{2\rho+\sin(2\rho)}4,
\qquad
\rho=\cos\rho.
\tag{3.2}
\]

The source hull satisfies the isodiametric inequality

\[
\operatorname{area}K\le\frac\pi4D^2.
\tag{3.3}
\]

Apply AP to the unit-separated external population. Equations (3.2)-(3.3) give

\[
\limsup\frac{Z_{ext}}{D^2}
\le
\frac2{\sqrt3}\left(\frac\pi4-A_{FS}\right).
\tag{3.4}
\]

It remains to prove that the right side of (3.4) is strictly smaller than the right side of (3.1).

Define `f(x)=x-cos x`. On `[0,pi/2]`,

\[
f'(x)=1+\sin x>0.
\]

Also

\[
\cos\frac23\ge1-\frac12\left(\frac23\right)^2
=\frac79>\frac23,
\]

so `f(2/3)<0`. On the other hand

\[
\cos\frac\pi4=\frac{\sqrt2}{2}<\frac34<\frac\pi4,
\]

using `pi>3`; hence `f(pi/4)>0`. Therefore

\[
\boxed{\frac23<\rho<\frac\pi4.}
\tag{3.5}
\]

Thus

\[
\frac{4}{3}<2\rho<\frac\pi2.
\]

Since `pi<4`, one has `4/3>pi/3`. Sine is increasing on `[0,pi/2]`, so

\[
\sin(2\rho)>\sin\frac\pi3=\frac{\sqrt3}{2}.
\]

Consequently

\[
\boxed{
A_{FS}
>\frac{4/3+\sqrt3/2}{4}
=\frac13+\frac{\sqrt3}{8}.
}
\tag{3.6}
\]

Insert this lower bound into (3.4):

\[
\begin{aligned}
\limsup\frac{Z_{ext}}{D^2}
&<
\frac2{\sqrt3}
\left(
\frac\pi4-\frac13-\frac{\sqrt3}{8}
\right)\\
&=
\Delta-\frac{2}{3\sqrt3}-\frac14.
\end{aligned}
\tag{3.7}
\]

Compare this with (3.1). Their lower-minus-upper gap is

\[
\frac{2}{3\sqrt3}+\frac14-\frac{\pi^2}{16}.
\tag{3.8}
\]

Using the classical elementary bound `pi^2<10`,

\[
\frac{2}{3\sqrt3}+\frac14-\frac{\pi^2}{16}
>
\frac{2}{3\sqrt3}-\frac38.
\]

Finally

\[
\frac{2}{3\sqrt3}>\frac38
\quad\Longleftrightarrow\quad
16>9\sqrt3,
\]

and squaring the positive sides gives `256>243`. Hence (3.8) is strictly positive.

Therefore the asymptotic upper bound (3.7) is strictly below the MB lower bound (3.1), a contradiction. `square`

### Quantitative margin

For orientation only, the exact constants are approximately

\[
A_{FS}=0.6184708847\ldots,
\]

\[
\Delta-\frac{\pi^2}{16}=0.2900494070\ldots,
\]

while AP plus FSDB gives

\[
\frac2{\sqrt3}\left(\frac\pi4-A_{FS}\right)
=0.1927510185\ldots.
\]

The resulting asymptotic population margin is about `0.0972983885 D^2`. These decimals are not used in the sign proof.

---

## 4. Exact target implication

Before this report, the post-ZF perfect-matching endpoint was

```text
H perfect matching
    -> pure strict-rhombic force-visible core
    -> at least 0.290049... D^2 external isolates outside F
    -> [open annular population theorem].
```

It is now

```text
H perfect matching
    -> MB external population lower bound
    + FSDB force-hull area lower bound
    + AP sharp-bulk annular packing
    -> contradiction.
```

Thus the perfect-matching branch is removed from C-II under the same report-level ZF/MB/FSDB dependencies.

Using the exact branching-defect identity from DB,

\[
2h-q=x_B+Q+2s_Z
=\sum_{b\in B_+}(\deg_H(b)-1),
\tag{4.1}
\]

MEX says the zero value of this common quantity is impossible on every sufficiently large survivor. Since it is an integer,

\[
\boxed{
2h-q=x_B+Q+2s_Z\ge1
}
\tag{4.2}
\]

for every sufficiently large source in the audited post-ZF class.

This is only a one-unit strictness statement at present. The remaining general branch can have sparse branching, exceptional faces, outer-walk surplus, or extra mixed dependencies.

---

## 5. Exact remaining lemma

The shortest continuation is no longer “exclude a perfect matching.” A stronger branch theorem must turn the **amount** of diameter branching into source-capacity loss.

One sufficient formulation is:

> **Branched annular capacity theorem.** For every sufficiently large post-ZF survivor, use
> \[
> r_H:=2h-q=x_B+Q+2s_Z\ge1
> \]
> together with the full-source FS/PW geometry and the difference-body constraints to prove either
> \[
> n-1\le\frac\pi{2\sqrt3}D^2
> \]
> or construct an `n`-point unit-separated competitor of diameter `<D`.

A more concrete near-matching subtarget is to prove a positive **linear** lower bound `r_H>=cD`; DB.1 would then force `h/D` above its minimum by a fixed amount, and FSDB's force-hull area constant would improve accordingly. MEX alone gives only `r_H>=1`, so such a linear upgrade is not claimed here.

---

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| AP sharp-bulk annular packing | proved | mesoscopic square localization of Oler with explicit boundary-cell count |
| AP error can be `O(D^(3/2))` | proved | choose square side `L=sqrt(D)` |
| MB external population lies in `K\F` | audited dependency used | matching topology gives pure rhombic core and excludes internal isolates |
| FSDB force-hull area lower bound | audited dependency used | current main report; FS.4 symmetry + complete diameter-direction difference body |
| MEX: unbounded perfect-matching branch impossible | proved under MB/FSDB post-ZF dependencies | asymptotic lower/upper external population bounds have an exact positive gap |
| `2h-q>=1` for sufficiently large post-ZF survivors | proved under same dependencies | DB exact branching identity + MEX + integrality |
| `2h-q=Omega(D)` | not proved | MEX excludes only the exact zero-branching endpoint |
| C-II / Level I | not proved | nonmatching diameter graphs remain |

---

## 7. Regression tests

### Regular odd shell

The canonical odd-shell regression is not a perfect matching: its diameter graph is an odd cycle. AP itself applies to any nested convex annulus, but MEX does not classify the shell as a contradiction. The shell therefore remains available against response-level matching/trace shortcuts.

### Dense isolated filling of an odd shell

The filled-shell regression puts its isolated population **inside** the shell force hull. MB's matching topology forces every isolate outside `F`, so the decisive hypothesis separating MEX from this regression is not merely density or response PSD; it is the exact post-ZF perfect-matching contact/topology consequence.

### Arbitrary convex annuli

AP does not claim an `O(D)` error. The `O(D^(3/2))` loss is deliberately loose but subquadratic, which is all the fixed quadratic MB/FSDB margin requires. Thin annuli and polygonal inner boundaries are allowed.

### Six-vertex noncentrally-symmetric matching polygon

MB records an exact equilateral convex hexagon family whose diameter graph is a perfect matching but whose polygon is not centrally symmetric. MEX does not use matching-to-central-symmetry. It uses the post-ZF contact ledger, full-source FS symmetry, and annular source population.

### Heptagon plus isolated center

The rejected force-bulk localization is not revived. AP allows arbitrary points outside or inside a force hull; only MB, under the much stronger perfect-matching topology, supplies `S subset K\F`. No general statement that all isolates are external is made.

---

## 8. Failed routes and no-go results

1. A direct Oler inequality on `K` cannot subtract the empty force-hull area. AP succeeds only by localizing Oler to mesoscopic cells wholly outside `F` and paying separately for cells meeting either boundary.
2. A fixed-size cell decomposition would lose `Theta(D^2)` through Oler's per-cell boundary term. The cell side must satisfy `L->infinity`.
3. A macroscopic cell size `L=Theta(D)` would make the boundary-cell loss quadratic. The scale must also satisfy `L=o(D)`. The choice `L=sqrt(D)` balances the two errors.
4. MEX does not imply near-matching supports are impossible. A diameter graph with `2h-q=1` survives this proof in principle.

---

## 9. Literature imported

None.

---

## 10. Computation and reproducibility

No computation is a proof dependency. The decimal constants in the orientation paragraph are evaluations of closed forms already present in MB/FSDB; the contradiction is proved with the exact inequalities in Section 3.

---

## 11. Canonical promotion recommendation

**Hold as report pending independent dependency audit.** AP itself is self-contained modulo canonical Oler and is promotable as a shared finite-packing lemma. MEX additionally depends on the report-level post-ZF chain MB and FSDB. It should not be promoted into the Target C route map until those dependencies are accepted under the repository's promotion procedure.

No Level I status change is warranted.

---

## 12. Next run

The highest-value continuation is to quantify how far every survivor must lie from the matching endpoint. Write

\[
r_H=2h-q=x_B+Q+2s_Z.
\]

MEX gives `r_H>=1`. The next useful theorem would prove `r_H>=cD` for an absolute `c>0`, or else show that `r_H=o(D)` preserves enough of MB's pure-rhombic/external-population structure for the same annular argument to survive with `o(D^2)` losses. The second route is especially attractive: an `o(D)` defect changes only `o(D^2)` train/rhombic capacity at the scale relevant to the fixed MEX population margin.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Strongest new theorem AP:
For convex F subset K of diameter at most D and unit-separated S subset K\F,
  |S| <= (2/sqrt(3))(area K-area F)+O(D^(3/2)).
Proof: side-sqrt(D) square grid; Oler on bulk squares; only O(sqrt(D)) squares
meet each convex boundary; crude disk packing handles those boundary squares.

New post-ZF branch elimination MEX:
If the full actual diameter graph is a perfect matching, MB requires
  Z_ext/D^2 >= Delta-pi^2/16-o(1).
FSDB gives
  area(F)/D^2 >= A_FS-o(1),
  A_FS=(2rho+sin2rho)/4, rho=cos rho.
AP and area(K)<=pi D^2/4 give
  Z_ext/D^2 <= (2/sqrt(3))(pi/4-A_FS)+o(1).
The upper constant is strictly smaller. Hence no unbounded perfect-matching
post-ZF survivor sequence exists.

Exact new consequence:
  2h-q=x_B+Q+2s_Z>=1
for every sufficiently large survivor in the audited post-ZF class.

Remaining branch:
Quantify the nonmatching defect r_H=2h-q. A linear lower bound, or a stability
version showing r_H=o(D) retains MB's annular contradiction, would remove a
substantially larger class.

Files:
docs/reports/target_c_annular_packing_matching_exclusion_2026-09-10.md
Dependencies:
docs/reports/target_c_matching_branch_externalization_2026-09-09.md
docs/reports/target_c_fs_symmetric_difference_body_area_2026-09-10.md
```
