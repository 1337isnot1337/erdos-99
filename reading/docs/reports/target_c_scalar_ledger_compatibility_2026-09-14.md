> Generated reading edition · [exact source](../../../docs/reports/target_c_scalar_ledger_compatibility_2026-09-14.md) · source SHA-256 `73e743240a602ad7dc3b68f2ade1d3b0f66b48baafc0a1e331845a21d62b8adb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-194DE1FE1661","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C-II scalar-ledger compatibility audit

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** Target C-II closing-proof / exact scalar-regression computation
**Target:** C-II / Level I
**Starting status:** canonical C-II frontier through normalized Sections 122–123
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used for status only; no external theorem imported
**Computation:** used — `research/verify_target_c_scalar_ledger_compatibility.py`

## Bootstrap snapshot

The authoritative checkout used for this run was the full project checkout; a separate
migration-stage copy was incomplete and had no usable Git `HEAD`/configuration or full state tree.
Local filesystem paths and the local branch name are omitted from this imported copy. At
bootstrap:

```text
git rev-parse HEAD: ef941ab2b44aa393bdc461926769247b45754202
git branch: local research branch (name omitted)
working tree: clean, tracking its origin research branch
theorem-state: 2026-09-12.audit.46
Level I: OPEN
Target A: OPEN (current endpoint Section 177)
Target B: OPEN
Target C-I: CLOSED
Target C-II: OPEN (canonical frontier Sections 122–123)
```

A separate untracked full-core vanishing-shear regression appeared during the run;
it was preserved and not overwritten. The only files authored for this report are
the report itself, its exact certificate, the research index entry, and the
corresponding `research/README.md` entry.

## LEVEL I STATUS

`STILL OPEN`

No part of this report constructs a source configuration, proves global
minimum-diameter optimality, or settles the original every-minimizer quantifier.

## 1. Starting canonical endpoint

The run started from the full-core Type-II endpoint in canonical Sections 122–123,
the promoted diameter-budget floor, and the subsequently promoted loaded-chord/train
surplus floor:

```math
 \liminf_{D\to\infty}{1\over D}
 \sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
 \ge {\pi\over2}(2-\sqrt3),
 \tag{1}
```

and

```math
 \sum_rP_{{\rm exc},r}\le10(e_{BB}-k),
 \qquad k=d_H+s_Z.
 \tag{2}
```

The intended implication chain was

```text
an upper bound on the same aggregate outer detour
    -> contradiction with (1) after the payment (2)
    -> exclusion of the Type-II full-core branch
    -> C-II and Level I closure after the macroscopic-container branch
```

The exact question tested here was whether scalar elimination from the listed
promoted loaded-hull, pinned-ledger, difference-body, primitive-split, train/interface,
and 122–123 inequalities already supplies that upper bound. It does not. This is a no-go for
that displayed scalar package; it is not a claim that every conceivable scalar
consequence of the entire repository has been enumerated.

## 2. Strongest genuinely new result

**Classification:** proved finite identity plus exact scalar compatibility regression;
unreviewed and noncanonical.

### Statement

For every canonical harmonic component `I_r` with attachment set `A_r`, let

- `n_r=|I_r|`;
- `a_r=|A_r|`;
- `s_r=e_r+t_r-2n_r-1` be its pinned-contact surplus;
- `c_r` be the number of loaded-loaded contact edges whose endpoints lie in `A_r`;
- `f_r` be the number of bounded nonquadrilateral faces of its induced graph;
- `Q_r` be the sum of `deg(f)-4` over those faces; and
- `L_r` be the occurrence-counted outer-face walk length.

Then the exact local Euler identity is

```math
 \boxed{L_r+Q_r=4a_r-6-2s_r-2c_r,}
 \tag{3}
```

and therefore

```math
 \boxed{
 L_r+P_{{\rm exc},r}
 =4a_r-6-2s_r-2c_r+4f_r,
 }
 \tag{4}
```

where `P_{{\rm exc},r}=4f_r+Q_r`.

More importantly for the current endpoint, there is an explicit sequence of
**abstract scalar ledger points** satisfying, with strict room, all of the following
scalar conditions:

1. the pinned ledger `c_I+e_{BB}+s_C=q-2+k`;
2. the loaded-hull split `q-x_B=Q+2k` and
   `e_{BB}=Q+2k+u_B+c_B`;
3. the exact identity `c_I+s_C+c_B=m+k-2`;
4. the triangle-free loaded outerplanar cap `2e_{BB}+m\le3q-4`;
5. the promoted renormalized-surplus floors, including the new full-core
   train-coupled floor; the repaired near-disk witness has the exact margin
   `mu_D=2.2-10/D>2`;
6. the promoted primitive split lower bound at the displayed `rho` scale;
7. Type-II subquadratic component count `c_I=o(D)`;
8. the local Section-122 zero-host inequalities for two cells with diameters
   `D` and `19D/20`, with total rhombus area `\pi D^2/4-D` in the scalar model;
9. the aggregate Section-122 detour floor;
10. the Section-123 payment with the selected total `P_{{\rm exc}}=5D/4`;
11. the canonical Section-85 train-end and Oler-weighted chamber inequalities; and
12. the canonical Section-89 area--train inequality at the displayed cell scales.

The scalar data leave a positive aggregate outer detour of `1.629988D` at
`D=10^6`, while the exact Section-122 lower constant is less than `11/21<0.53`
using only `3<\pi<22/7` and `5/3<\sqrt3`. Thus no contradiction follows from
these scalar constraints. This is not a geometric counterexample: the witness does
not realize a planar contact graph, a KKT stress, a source hull, or global
optimality.

### Scope

The local identity (3) is finite and applies to the induced harmonic graphs under the
canonical C-II hypotheses, with repeated outer-walk vertices and bridge occurrences
counted as occurrences. It retains all source points; it does not count contact-
isolated points as vertices of the positive-contact core.

The compatibility realization is deliberately weaker: it is an abstract assignment
to the scalar variables of the promoted ledgers. It is a regression against a
scalar-only closing argument, not a feasible packing and not a theorem about any
global minimizer.

### Proof of the exact local identity

The induced graph on `I_r\cup A_r` is connected. Its vertex and edge counts are

```math
 V_r=n_r+a_r,
 \qquad
 E_r=e_r+t_r+c_r=2n_r+1+s_r+c_r.
 \tag{5}
```

Let `F_{b,r}` be its number of bounded faces. Euler gives

```math
 F_{b,r}=E_r-V_r+1=n_r+2+s_r+c_r-a_r.
 \tag{6}
```

The outer face has walk length `L_r`. Bounded quadrilateral faces contribute four to
face incidence, and a bounded nonquadrilateral face of degree `d_f` contributes
`4+(d_f-4)`. Consequently

```math
 2E_r=L_r+4F_{b,r}+Q_r.
 \tag{7}
```

Substituting (5) and (6) into (7) and cancelling `n_r` gives

```math
 L_r+Q_r
 =2(2n_r+1+s_r+c_r)
  -4(n_r+2+s_r+c_r-a_r)
 =4a_r-6-2s_r-2c_r,
```

which is (3). Since

```math
 P_{{\rm exc},r}=4f_r+Q_r,
```

adding `4f_r` to (3) gives (4). No asymptotic estimate, simple-boundary assumption,
or global injectivity of local outer walks is used.

### Proof of scalar compatibility

Take any multiple `D` of `400` and set

```math
 q={3D\over2},\quad d_H=0,\quad s_Z=2,\quad k=2,
 \quad c_I=2,\quad s_C=0,
 \quad e_{BB}=q-2.
 \tag{8}
```

For the loaded-hull decomposition put

```math
 Q=0,\quad x_B=q-4,\quad m=2,\quad u_B=q-6,\quad c_B=0.
 \tag{9}
```

Then, exactly,

```math
 c_I+e_{BB}+s_C=q=q-2+k,
```

```math
 q-x_B=4=Q+2k,
 \qquad
 e_{BB}=4+(q-6)=Q+2k+u_B+c_B,
```

and

```math
 c_I+s_C+c_B=2=m+k-2.
```

The loaded outerplanar cap holds because

```math
 2e_{BB}+m=3q-6\le3q-4.
```

The displayed primitive split is satisfied with room because
`\max(e_{BB},x_B)/D>1`, while the canonical root obeys `\rho<3/4`, so
`4\rho/3<1`. The renormalized surplus is

```math
 {e_{BB}+2s_C-3k\over D}
 ={q-8\over D}
 ={3\over2}-{8\over D}>0.9604
```

for `D\ge10^6`. Also `h=q` and `q/D=3/2<\pi`, while the fixed `c_I=2` is
`o(D)` and hence compatible with the Type-II subquadratic component conclusion.

For the local part, use two abstract cells with

```math
 d_1=D,
 \qquad d_2={19D\over20},
 \qquad
 A_{4,1}=A_{4,2}={\pi D^2\over8}-{D\over2},
 \qquad
 P_{{\rm exc},1}=P_{{\rm exc},2}={5D\over8}.
 \tag{10}
```

Choose `a_1=a_2=3D/4`, `s_i=0`, `f_i=Q_i=D/8`, and

```math
 c_i={147D\over400}.
 \tag{11}
```

The exact identity (3) then gives the common outer-walk length

```math
 L_i=4a_i-6-2c_i-Q_i={107D\over50}-6,
```

and hence

```math
 E_1=L_1+P_{{\rm exc},1}-2d_1
 ={153D\over200}-6,
 \qquad
 E_2=L_2+P_{{\rm exc},2}-2d_2
 ={173D\over200}-6.
 \tag{12}
```

The elementary bounds `\sqrt3>5/3` and `\pi<22/7` imply

```math
 (4-2\sqrt3){\pi D^2\over8}
 <{11\over42}D^2
 <d_jE_j
 \qquad (j=1,2)
 \tag{13}
```

for `D\ge10^6`. Thus each local Section-116/122 inequality is compatible with the
chosen local detour. Summing (12), the aggregate detour is

```math
 \sum_iE_i={163D\over100}-12.
\tag{14}
```

The Section-89 scalar area--train inequality is also satisfied. Indeed,
`2A_{4,i}=\pi D^2/4-D<11D^2/14`, while

```math
 d_j\left(6a_j-15-3c_j\right)>{11D^2\over14}
 \qquad (j=1,2).
```

Thus the local train-budget consequence does not remove this scalar witness either.

The finite Section-85 train-end inequality is also compatible with this same
assignment. The scalar family has total nonquadrilateral-face count
`2f_i=D/4`, so

```math
q-k+2(2f_i)=2D-2.
```

For the Type-II leading rhombus ratio, choose the compatible scalar
correction

```math
R_4={\pi\over2\sqrt3}D^2-2D.
```

Take also the near-disk perimeter annotation `P_F=\pi D`. With
$`a_0=\sqrt3/2`$, the total rhombus area above satisfies
```math
A_4={\pi D^2\over4}-D
=a_0R_4+(\sqrt3-1)D,
```
so its rhombus excess is nonnegative and the ratio still tends to the
canonical Type-II limit. Moreover,

```math
{R_4\over D^2}<{\pi\over2\sqrt3}
<{33\over35}<\left({49\over50}\right)^2,
```

the right side of (85.1) is bounded by `(49/25)D` in this scalar
comparison, whereas `2D-2>(49/25)D` for `D>50`.
Thus the Section-85 train-end floor does not remove the witness either. This
same assignment also passes the area/population consequence (85.3). Annotate
the Type-II chamber surplus by `A_ch=D` and `Z_ch=0`; this is linear, hence
compatible with the `o(D^2)` inactive-chamber scale. Since `\sqrt3<2`,
`3c_0/5<3/10`, while `P_F>3D` and
`\sqrt{R_4}<(49/50)D`, the right side of (85.3) is less than
`(3/10)(23D/25)=69D/250<D=A_ch-a_0Z_ch`. This checks the scalar
area/population floor but does not construct an actual chamber or population.
All face and population symbols remain an abstract ledger assignment.

The same elementary bounds imply

```math
 {\pi\over2}(2-\sqrt3)<{11\over21}< {163\over100}-{12\over D}
 \tag{15}
```

for `D\ge10^6`, so the aggregate Section-122 demand holds. Finally the selected
total exceptional perimeter is `P_{{\rm exc}}=5D/4`; Section 123's inequality
still holds because `5D/4<10(e_{BB}-k)=15D-40` for `D\ge10^6`.

This proves the stated compatibility. The certificate checks the same arithmetic
with integer `D=10^6` and rational comparisons.

### Compatibility with the repaired Type-II payment

The same abstract point also satisfies the stronger Type-II bookkeeping proposed
for the no-interior-loaded-chord regime. For each of the two cells set


```math
 T_i=0,
 \qquad Q_i^+=a_i-6,
 \qquad Q_{M,i}=Q_i^+-Q_i,
 \qquad Q_{C,i}=Q_i,
 \qquad Q_{I,i}=0,
 \qquad c_i^\partial=c_i,
 \qquad h_i=a_i-c_i.
```

Define

```math
 X_i=a_i-T_i+Q_i^+,
 \qquad
 M_i=h_i-T_i+Q_{M,i}.
```

Then the augmented-cell identity is exact:

```math
 a_i-3-s_i
 =\frac{a_i-T_i+Q_i^+}{2},
 \qquad
 X_i=M_i+c_i^\partial+Q_{C,i}+Q_{I,i}.
```

In the present values,

```math
 X_i=\frac{3D}{2}-6,
 \qquad
 M_i=\frac{403D}{400}-6,
 \qquad
 L_i-2a_i=M_i-c_i^\partial=\frac{16D}{25}-6.
```

The polygon-dissection deficit is

```math
 d_{\rm tile}=q-2-2(a_i-2)=2,
```

and hence

```math
 e_{BB}-k=\frac12\sum_iX_i+d_{\rm tile}.
```

Writing `M_{\rm miss}=\sum_iM_i` and
`C_\partial=\sum_ic_i^\partial`, the repaired aggregate payment has equality:

```math
\begin{aligned}
 \sum_i(L_i+P_{{\rm exc},i}-2a_i)
 &=10(e_{BB}-k-d_{\rm tile})
   -4M_{\rm miss}-6C_\partial\\
 &=\frac{253D}{100}-12.
\end{aligned}
```

Adding `2\sum_i(a_i-d_i)=-9D/10` gives the repaired upper bound for the actual
Section-122 detour,

```math
 \sum_i(L_i+P_{{\rm exc},i}-2d_i)
 \le \frac{163D}{100}-12.
```

This is exactly the value already selected in (14), and it is still strictly larger
than `11D/21`, which is an upper bound for the canonical Section-122 lower
constant. Thus the repaired Type-II payment is also compatible with the scalar
data. This remains an abstract scalar regression: the symbols `Q_i^+`,
`Q_{M,i}`, and `M_i` are not asserted to come from an embedded augmented
plane graph.

### Compatibility after imposing the near-disk perimeter scale

The preceding witness only imposed `q/D<pi`; it did not encode the perimeter limit
of the near-disk loaded hull. An adversarial audit caught that the first draft of
this subsection, with `q=3D/2`, was incompatible with the exact decomposition
`x_B=(P_F-q)+(b-P_F)`: it forced `x_B=3D/2-4`, but required
`x_B\ge(\pi-3/2)D`. That draft is withdrawn. The corrected scalar obstruction
persists after adding

```math
 P_F=\pi D,
 \qquad c_B=0,
\qquad q={17D\over10},
 \qquad m={D\over2},
\qquad e_{BB}=q-m={6D\over5},
\qquad x_B=q-4={17D\over10}-4.
\tag{16}
```

Here `m` is the number of nonunit force-hull sides. The `q-m=6D/5` unit sides
have total length `6D/5`; the `m=D/2` nonunit sides may be assigned total length
`(pi-6/5)D`, with each side longer than one. The basic metric decomposition is
also respected, since

```math
 P_F-q=(\pi-17/10)D<{43D\over35}<x_B,
 \qquad b-P_F=x_B-(P_F-q)>0.
```

This is only a scalar perimeter assignment: no convex polygon realizing all other
ledgers is claimed. Rational approximants to `pi` give the same asymptotic scalar
point if a rational sequence is preferred.

The exact pinned ledger then forces

```math
 s_C={D\over2}-2
\tag{17}
```

when `c_I=2` and `k=2`. Use two abstract cells with

```math
 a_i={3D\over4},qquad d_i=D,qquad s_i={D\over4}-1,qquad c_i=0,
\tag{18}
```

and put all augmented degree excess on missing sides:

```math
 Q_i^+=Q_{M,i}={D\over4}-4,qquad Q_{C,i}=Q_{I,i}=T_i=0.
\tag{19}
```

Then

```math
 M_i=X_i=D-4,qquad
 L_i={5D\over2}-4,qquad
 P_{{\rm exc},i}=0.
\tag{20}
```

The polygon-dissection deficit is now
`d_tile=q-2-2(a_i-2)=D/5+2`, and the exact payment gives

```math
\begin{aligned}
   e_{BB}-k&={6D\over5}-2={1\over2}(X_1+X_2)+d_{\rm tile},\\
 \sum_i(L_i-2a_i)&=2D-8\\
 &=10(e_{BB}-k-d_{\rm tile})-4\sum_iM_i-6\sum_i c_i^\partial.
\end{aligned}
\tag{21}
```

Moreover $`q-k=17D/10-2`$, which is above the promoted train-coupled lower
constant $`1.637562\ldots D`$; the certificate checks the stronger rational
condition $`q-k+2f>2D`$ against the near-disk $`R_4`$ annotation. The exact
renormalized surplus is

```math
\mu_D={e_{BB}+2s_C-3k\over D}={22\over10}-{10\over D}>2.
```

Adding 2 sum_i(a_i-d_i)=-D leaves
Adding `2 sum_i(a_i-d_i)=-D` leaves

```math
 \sum_i(L_i+P_{{\rm exc},i}-2d_i)=D-8.
\tag{22}
```

For `D>=10^6`, each local Section-122 demand holds because
`D(D/2-4)>(11/42)D^2`, and the aggregate demand holds because
`D-8>(11/21)D`. The renormalized surplus and primitive loaded-hull lower bound
also hold with linear room. Thus adding the corrected near-disk perimeter scalar and the
no-interior-chord condition still does not produce the missing detour upper bound.

This is again an abstract scalar regression. It does not assert a planar embedding,
actual cell dissection, KKT equilibrium, source cardinality, or global optimality.

## 3. Exact frontier effect

The C-II route is not advanced to a closure. The new result is a certified negative
answer to four scalar mechanisms:

```text
the displayed promoted scalar package alone
    -/-> an upper bound on sum_r(L_r-2d_r)
    -/-> contradiction with the Section-122 lower bound.

the repaired Type-II missing-side/attachment payment alone
    -/-> an upper bound below the Section-122 lower bound.

the repaired payment plus the near-disk perimeter scale
    -/-> an upper bound below the Section-122 lower bound.

the repaired payment plus the Section-85 train-end/chamber floors
    -/-> an upper bound below the Section-122 lower bound.
```

The exact remaining implication is therefore genuinely geometric. A future C-II
closure must add at least one of:

1. a bound on the same aggregate outer-walk detour that uses the actual embedding of
   the cells in the near-disk force hull;
2. a source-preserving deformation or strict sub-`D` competitor driven by the
   detour; or
3. an exact unit equilateral triangle forced by the carrier, loaded hull, or
   diameter geometry.

The macroscopic inactive-container branch is untouched. It still requires a
source-preserving global contradiction, not merely deep near-unit matching or contact
creation.

## 4. Exact remaining lemma

The sharp next C-II theorem is:

> **Embedded aggregate-detour theorem.** In every sufficiently large Type-II
> contact-minimal, diameter-pair-minimal triangle-free global minimizer, with the
> canonical harmonic cells and their occurrence-counted outer walks, prove an upper
> bound on
> `\sum_r(L_r-2d_r)` that, together with (2), contradicts (1); or give a theorem
> converting the forced detour into a source-preserving strict decrease of the
> global diameter.

The word “embedded” is essential: the scalar certificate shows that no argument
using only the displayed integer ledgers and asymptotic scalar floors can prove this
lemma.

The repaired Type-II payment does not change this endpoint at the scalar level: its
remaining positive term is the actual geometric quantity
`\sum_r(a_r-d_r)`, and the certificate realizes the payment with equality while the
Section-122 demand still survives. A closing proof must therefore constrain that
term, the missing-side credits, or the cell embeddings jointly; it cannot discharge
the obligation by optimizing the payment algebra in isolation.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| `L_r+Q_r=4a_r-6-2s_r-2c_r` | proved candidate | induced connected triangle-free planar harmonic graph; Euler | complete finite derivation above; occurrence multiplicity is retained |
| `L_r+P_exc,r=4a_r-6-2s_r-2c_r+4f_r` | proved candidate | previous identity; definition of `P_exc,r` | exact algebra |
| scalar conditions (8)–(15), including the repaired Type-II payment, are jointly compatible | regression / computational evidence | canonical scalar ledger formulas and the displayed repaired payment; rational certificate | abstract variables only; no geometric embedding |
| Section-85 train-end and chamber inequalities (85.1), (85.3) are compatible | regression / computational evidence | Type-II leading ratio, scalar face count, and linear chamber-surplus annotation; rational certificate | no actual chamber geometry or population is constructed |
| corrected near-disk perimeter witness (16)–(22) is compatible | regression / computational evidence | scalar `P_F=pi D`, `q=17D/10`, `c_B=0`, exact metric decomposition, pinned/payment ledgers, and the train-coupled floor; rational certificate | the perimeter is an annotation and no convex embedding is asserted; the withdrawn `q=3D/2` draft failed the metric decomposition |
| promoted Sections 122–123 close C-II by scalar elimination | rejected attempt | C-AGGREGATE-TWO-ARC-DETOUR; C-AUGMENTED-CELL-DEFECT-BUDGET | exact scalar witness leaves positive detour and satisfies every listed inequality |
| abstract ledger point is a C-II survivor | rejected | none | it is not a planar contact graph, KKT stress, or source configuration |
| Type-II branch is eliminated | not proved | none | no source-level contradiction obtained |
| Level I is solved or disproved | not proved | none | original global quantifiers remain open |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| C-II contact-isolated-source correction | pass | the scalar witness does not count isolated source points in the core; it makes no full-source ZR/ZF claim |
| C-AGGREGATE-TWO-ARC-DETOUR occurrence rule | pass | local `L_r` is explicitly occurrence-counted; the argument uses only scalar sums, never global boundary injectivity |
| C-AUGMENTED-CELL-DEFECT-BUDGET | pass | the selected total `P_exc=5D/4` is below the Section-123 payment; the augmented ledger does not reuse exceptional-face occurrences |
| C-PRIMITIVE-SPLIT and C-MU-09604 | pass | `e_BB/D` and the renormalized surplus exceed the promoted floors with room |
| Type-II `c_I=o(D)` | pass | the witness uses fixed `c_I=2`; this checks only scalar compatibility |
| near-geodesic interface regression | pass as a binding limitation | the existing exact two-chain face shows that linear face/outer-walk currency cannot by itself be converted to a uniform area contradiction; it lacks near-disk global embedding and KKT/global-minimality hypotheses |
| local/jammed versus global-minimizer warning | pass | the abstract realization and the near-geodesic model make no global-optimality claim |
| `G_loc=o(D^2) => G_loc/d=o(1)` correction | pass | no such normalization is used; the report uses only finite Section-122 inequalities |
| bridge/repeated-vertex multiplicity | pass | all local walk lengths are occurrence counts; no simplification to a simple boundary is made |

The exact certificate command is:

```sh
python3 research/verify_target_c_scalar_ledger_compatibility.py
```

## 7. Literature imports

No external theorem is imported. A targeted check of the official [Erdős Problems
entry for Problem #99](https://www.erdosproblems.com/99) still labels the problem
open and mentions the triangular-lattice construction only as an asymptotic benchmark.
It supplies no theorem with the required uniform threshold over all cardinalities and
all global minimizers. The proof and regression above use only repository-canonical
theorem IDs, elementary Euler counting, and rational inequalities.

## 8. Computation

### `research/verify_target_c_scalar_ledger_compatibility.py`

- **Proposition tested:** the promoted scalar C-II ledgers do not have an arithmetic
  contradiction; an abstract point satisfies their exact equalities and displayed
  inequalities.
- **Assumptions encoded:** the scalar equalities and floors listed in Section 2,
  the Type-II scalar condition `c_I=o(D)`, and conservative rational bounds for the
  Section-122 and Section-85 constants.
- **Assumptions omitted:** planar embedding, actual contact coordinates, KKT
  equilibrium, response realizability, source cardinality, and global
  minimum-diameter optimality.
- **Arithmetic:** exact Python `Fraction`; no floating-point arithmetic is used.
- **Command:** `python3 research/verify_target_c_scalar_ledger_compatibility.py`.
- **Certified output:** ten PASS lines, including local and aggregate detour margins,
  compatibility with the Section-85 train-end and chamber inequalities, the Section-89 area--train
  inequality, the repaired Type-II payment, and the exact repaired near-disk margin
  `mu_D>2`, plus the explicit statement that the
  witness is abstract.
- **Does not prove:** a triangle-free packing, a global minimizer, a disproof, or any
  new upper bound for actual embedded detours.

The repository-wide command `python3 tools/run_theorem_certificates.py` was also
attempted. It passed the first certificate it ran, then stopped at the existing
`research/target_c_s1_q13_shell_regression.py` because this checkout's Python
environment has no `sympy` module (`ModuleNotFoundError: No module named 'sympy'`).
This optional-dependency failure is unrelated to the new certificate; the theorem
state checker and its two test suites pass, and the exact certificate above runs
without third-party dependencies.

The script is a reusable regression certificate, not a load-bearing theorem
certificate for the canonical state.

## 9. Corrections / supersessions

This report does not alter a canonical theorem. It reinforces two existing binding
corrections:

1. Section 122's local walks must remain occurrence-counted; the proof never identifies
   repeated vertices or bridge occurrences across different cells.
2. Section 121's discarded normalized moment inference is not used. The scalar
   compatibility result therefore does not revive `G_loc=o(D^2) => G_loc/d=o(1)`.
3. The first near-disk scalar choice `q=3D/2` is withdrawn: it failed
   `x_B\ge P_F-q`. The certificate and equations (16)–(22) use the corrected
   `q=17D/10` choice and explicitly check this metric inequality, while also
   satisfying the promoted train-coupled floor.

The stale top-level `docs/README.md` sentence saying Target A is through Section 176
was observed during bootstrap; the higher-authority `docs/STATE.md`, manifest, and
Target A route map consistently control Section 177 and were not changed by this run.

## 10. Promotion recommendation

**unreviewed**

The exact Euler identity is suitable for future audit, and the scalar compatibility
certificate is useful as a route no-go regression. It should not be promoted into the
canonical theorem stack until an independent researcher confirms that the abstract
variables encode every scalar condition claimed here and that no omitted canonical
inequality is intended to be part of the proposed scalar closure. No state-version,
route-map, or active-prompt update is recommended now.

## 11. Handoff

1. **Strongest new theorem/regression:** the exact local identity (3)–(4), together
   with the exact abstract compatibility family showing that scalar 122–123
   elimination cannot close C-II.
2. **Canonical dependency chain:** `C-ZRF` → `C-ATTACH-CURRENCY` →
   `C-LOADED-HULL` → `C-FULLCORE-NEAR-DISK` / `C-HARMONIC-CELL-TILING` →
   `C-AGGREGATE-TWO-ARC-DETOUR` and `C-AUGMENTED-CELL-DEFECT-BUDGET`.
3. **Exact remaining lemma:** an embedded aggregate-detour upper bound, a
   source-preserving strict sub-`D` deformation, or exact triangle forcing in the
   Type-II near-disk branch; independently, a global source coupling in the
   macroscopic-container branch.
4. **Binding dead routes/regressions:** local near-geodesic faces, contact creation
   without force transfer, full-source ZR/ZF extension, and all listed rejected
   C-II routes remain binding.
5. **Files to read next:** `docs/targets/target-c/84-typeII-interface-collapse-audit.md`,
   `docs/targets/target-c/85-train-boundary-interface-currency-audit.md`,
   `docs/targets/target-b/README.md`, and the current Target A modules 175–177 if
   attempting a cross-route source/response transfer.
