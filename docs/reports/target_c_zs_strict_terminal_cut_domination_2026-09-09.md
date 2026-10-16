<!-- theorem-state: {"artifact_id":"ART-C7F7BEB3BB2A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — Target C ZS: maximal terminal defect rank forces strict cut domination

**Date:** 2026-09-09  
**Repository state:** `4bc7c9baddb38d12cbadde8394992c0e9f708104`  
**Run type:** closing-proof continuation / dependency audit  
**Target:** Target C, C-II / Z route  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`, with the September 9 C–Z continuation directive  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The new result below strengthens the C64 response-cut theorem in the generic C-II phase. It does not prove the exact boundary/face inequality and does not settle Erdős Problem #99.

## 1. Starting endpoint

The September 9 campaign leaves the following audited report-level chain:

```text
Theorem Z
  -> ZC excludes C56-Z for the relative-interior C-II stress when D >= 9
  -> C56-G
  -> ZR: ker Omega = span{1,P_x,P_y}, rank Omega = v-3
  -> ZF: e+h >= 2v-2
  -> h >= delta >= ceil(D).
```

For the connected nonisolated contact core, write

- `v,e` for its vertex and contact-edge counts;
- `h=|H|` for the number of active diameter pairs;
- `b` for the outer-face walk length;
- `Q=sum_F(deg(F)-4)` over bounded contact faces.

Euler gives

\[
e=2v-2-\frac{b+Q}{2}.
\]

Thus the shortest retained scalar closing theorem is

\[
\boxed{b+Q>2h,}
\]

equivalently `e+h<2v-2`, contradicting ZF.

The response side still had an exact equality subcase. C64 proves only

\[
\mathbf 1_S^T(\Lambda-L_H)\mathbf 1_S\ge0
\]

for every boundary cut and shows that at least `2|B|/5` singleton cuts are strict. The new theorem removes every cut-equality case once ZR is available.

If this lemma is proved, it eliminates every exact response-cut equality in the generic C-II branch, because ZR gives `ker(Lambda-L_H)=Aff(B)`, while a nontrivial cut indicator on a strictly convex terminal set with at least six vertices is not affine.

## 2. Strongest genuinely new audited theorem

### Theorem ZS — strict terminal response-cut domination

Assume the audited September 9 C-II hypotheses used by ZC and ZR. In particular, let `A` be a triangle-free global minimum-diameter source chosen first to minimize its number of unit contacts and then its number of diameter pairs, let the relative-interior normalized KKT stress have full supports `C=C_*` and `H=H_*`, and assume `D>=9`.

Let `B=B_+` be the loaded terminal set of the connected positive contact network, let `q=|B|`, let `Lambda` be its Dirichlet response, and let `L_H` be the positive-diameter weighted Laplacian. Put

\[
M_B:=\Lambda-L_H.
\]

Then:

1. the terminal defect has maximal affine kernel,
   \[
   \boxed{\ker M_B=\operatorname{span}\{\mathbf1,P_x,P_y\},\qquad
   \operatorname{rank}M_B=q-3;}
   \tag{ZS.1}
   \]
2. if `S subset B` and `|B\setminus S|>=3`, then the principal submatrix `M_B[S,S]` is positive definite;
3. for every nonempty proper terminal set `S subsetneq B`, response domination across the cut is strict:
   \[
   \boxed{
   \sum_{b\in S,\ k\notin S}c_{bk}
   >
   \sum_{b\in S,\ k\notin S}\beta_{bk};}
   \tag{ZS.2}
   \]
4. in particular every loaded terminal has strict local response excess,
   \[
   \boxed{d_b>s_b\qquad(b\in B).}
   \tag{ZS.3}
   \]

Here `c_bk=-Lambda_bk`, `d_b=sum_{k!=b}c_bk`, and `s_b=sum_{k!=b}beta_bk`.

### Scope

This is an exact theorem for the same large, lexicographically normalized hypothetical C-II global minimizer and the same relative-interior stress used by ZC/ZR. It is not a theorem about arbitrary circular-planar networks, arbitrary PSD matrices, arbitrary feasible packings, or isolated source points. It gives strict positivity but no uniform lower bound on the cut excesses or on `tr M_B`.

### Proof

ZC excludes C56-Z for this relative-interior stress when `D>=9`. Therefore the stress lies in C56-G.

The ZR proof already performs the required terminal-space nullity calculation before Schur elimination to the full scalar stress. On the zero-sum terminal space it sets

\[
Y=\Lambda^{-1/2}QB_H^{1/2}.
\]

C56-G gives a two-dimensional zero eigenspace for `I-Y^T Y`. The singular-value identity gives the same zero-eigenvalue multiplicity for `I-YY^T`. Congruence identifies the latter with `M_B=Lambda-L_H` on the zero-sum terminal space. Restoring constants adds one kernel dimension. Hence

\[
\dim\ker M_B=3.
\]

The affine response identities give

\[
M_B\mathbf1=0,
\qquad
M_BP_x=0,
\qquad
M_BP_y=0.
\]

The force hull is two-dimensional, so `1,P_x,P_y` are linearly independent. This proves (ZS.1).

Now let `S subset B` with `|B\setminus S|>=3`. Suppose `M_B[S,S]` were not positive definite. Since `M_B` is PSD, there would be a nonzero vector `x` supported on `S` with

\[
x^TM_Bx=x_S^TM_B[S,S]x_S=0.
\]

For a PSD matrix, zero quadratic energy implies `M_Bx=0`. By (ZS.1), there is an affine function

\[
f(p)=a+u p_x+v p_y
\]

whose values on the terminal points equal `x`. But `x` vanishes on every point of `B\setminus S`. The loaded terminals are vertices of a strictly convex polygon, so any three distinct terminals are noncollinear. Since the complement contains at least three terminals, `f` vanishes at three noncollinear points and is therefore identically zero. This contradicts `x!=0`. Thus `M_B[S,S]` is positive definite.

For a nonempty proper cut `S`, C64's Laplacian identity is

\[
\mathbf1_S^TM_B\mathbf1_S
=
\sum_{b\in S,\ k\notin S}(c_{bk}-\beta_{bk}).
\tag{ZS.4}
\]

It remains only to prove the left side is nonzero. If it were zero, PSD would imply `1_S in ker M_B`, so by (ZS.1) the binary terminal function `1_S` would be affine. Because `q>=6`, at least one of `S` and `B\setminus S` contains three terminals. If three terminals lie in `S`, the affine function `1_S` equals one at three noncollinear points and hence is identically one, contradicting the nonempty complement. If three terminals lie in the complement, the same argument with value zero makes the function identically zero, contradicting nonempty `S`. Therefore

\[
\mathbf1_S^TM_B\mathbf1_S>0,
\]

which is exactly (ZS.2).

Taking `S={b}` gives

\[
M_{B,bb}=d_b-s_b>0,
\]

proving (ZS.3). QED.

### Dependencies

The proof uses only the following existing inputs.

- `docs/targets/target-c/56-ci-restored-frontier.md`: the promoted lexicographic normal form, universal PSD, and finite integration state.
- `docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md`: Theorem Z, ZC, and the terminal SVD/nullity step in ZR.
- `docs/reports/target_c_minimum_transfer_kernel_collapse_2026-08-31.md`: C56-G/C56-Z.
- `docs/reports/target_c_psd_response_cut_domination_2026-08-31.md`: `M_B>=0`, the affine response identities, and the cut-energy formula.
- Canonical force-hull geometry: `B` is the strictly convex loaded terminal set, and ZC/C34 gives `q>=6` for `D>=9`.

No new external theorem and no computation are required.

### Why it is new

C64 states non-strict domination for every cut and proves strict singleton excess only on a set of size at least `2|B|/5`. The September 9 ZR report proves the full scalar core rank and contains the terminal nullity calculation as an intermediate step, but it does not extract the principal-minor or all-cut strictness consequences above. No current Target C module or report found in the dependency audit states (ZS.2) or (ZS.3) for every terminal.

## 3. Exact target implication

ZS removes the entire exact cut-equality set from the generic C-II response problem:

```text
old C64 state:
    M_B >= 0;
    every cut has response >= diameter load;
    at least 2q/5 terminals have d_b>s_b;
    zero-excess rows may remain.

new ZS state, after ZC/ZR:
    ker M_B = Aff(B), rank M_B=q-3;
    every proper nonempty cut has response > diameter load;
    every terminal has d_b>s_b;
    every principal block grounded at >=3 other terminals is positive definite.
```

This removes the zero-row/equality-terminal subbranch and every exact saturated boundary cut from any continuation of C64/C66.

It does **not** provide a quantitative cut gap. The exact global face endpoint remains

\[
\boxed{b+Q>2h.}
\]

Equivalently, using the stopped-train identity

\[
T=\frac{b+Q}{2}+2f,
\]

the missing inequality remains

\[
\boxed{T-h>2f.}
\]

## 4. Exact remaining lemma

### Global boundary/face inequality

There exists `n_0` such that every triangle-free global `n`-point minimum-diameter source with `n>=n_0`, chosen first to minimize contacts and then diameter pairs, satisfies on its nonisolated contact core

\[
\boxed{
 b+\sum_{F\text{ bounded}}(\deg F-4)>2|H|.
}
\tag{GF}
\]

This is still the shortest scalar Level I endpoint. ZS is useful only if its strict response cuts can be converted into an exact combinatorial or geometric surplus contributing to (GF); mere positivity with no lower magnitude is insufficient.

A comparably strong substitute would also suffice, for example an exact stopped-train theorem

\[
T-|H|>2f_{\rm exc}.
\]

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Theorem Z | proved and report-level audited | The September 9 consolidated review accepts the circular-split/all-gap proof with the `m>=3` and terminal-cover hypotheses. |
| ZC | proved under stated C-II inputs | `D>=9` gives at least six terminals; Theorem Z plus SEPq excludes C56-Z on the actual source network. |
| ZR | proved under audited C56 input | The terminal SVD and Schur-congruence argument gives scalar core kernel `span{1,P_x,P_y}`. |
| ZF | proved under ZR and promoted finite integration | Lexicographic minimality plus PSD reduces every mixed flex to Euclidean motion, giving `e+h>=2v-2`. |
| ZB | proved under its explicit pure-disk hypotheses | ZF gives `h>=T`, while the audited Target B exposed-hull theorem gives `T>q>=h` with a positive linear margin. |
| ZS | proved in this report | It is the strict-cut/principal-minor consequence of the terminal rank already present inside the ZR proof. |
| ZS gives a uniform trace or cut gap | false as an inference from ZS alone | Strict positivity and fixed rank do not supply a uniform lower eigenvalue or conductance scale. |
| ZS proves the face inequality | conditional route only | A source-specific transport from strict response cuts to `T-h-2f` is still missing. |

## 6. Regression tests

### Two-edge crossing square

The mandatory Theorem Z regression is unchanged. A two-edge crossing support can have diagonal transfer without an additive terminal resistance metric. ZS does not use Theorem Z outside its `m>=3` large-C-II range; ZC already ensures the generic branch before ZS is invoked.

### Exact regular unit hexagon: maximal terminal rank is not itself a contradiction

Let

\[
p_j=(\cos(j\pi/3),\sin(j\pi/3)),\qquad j=0,\ldots,5.
\]

The six consecutive sides have length one and the three opposite pairs have length `D=2`. Put contact weight

\[
\alpha=\frac23
\]

on every cycle edge and diameter weight

\[
\beta=\frac13
\]

on every opposite pair. Then

\[
\sum_C\alpha=6\cdot\frac23=4=D^2,
\qquad
\sum_H\beta=3\cdot\frac13=1.
\]

At each vertex the two contact vectors sum to the radial vector `p_j`, while the opposite diameter vector is `2p_j`, so equilibrium is

\[
\frac23p_j=\frac13(2p_j).
\]

Thus this is an exact normalized KKT stress on the contact cycle and opposite matching.

Let `P` be the orthogonal projector in `R^6` onto the complement of

\[
\operatorname{span}\{\mathbf1,P_x,P_y\}.
\]

Its entries are

\[
P_{ij}=\delta_{ij}-\frac16-\frac13\cos((i-j)\pi/3).
\]

Hence

- `P_ii=1/2`;
- `P_ij=-1/3` for adjacent vertices;
- `P_ij=0` at cyclic distance two;
- `P_ij=1/6` for opposite vertices.

The signed stress matrix is therefore exactly

\[
L_C(2/3)-L_H(1/3)=2P.
\]

It is PSD, has rank `3=q-3`, has affine kernel, and is strict on every nontrivial cut. Its positive off-diagonal entries occur exactly on the diameter matching. Therefore maximal affine-kernel PSD plus the contact/diameter off-diagonal sign pattern is algebraically and mechanically consistent.

This does not challenge ZS or Level I: the regular unit hexagon has diameter `2`, while the known exact optimum is

\[
D(6)=2\sin72^\circ<2.
\]

It is not a global six-point minimizer. The regression shows that a closing theorem cannot come from terminal rank and sign pattern alone; it must use the large-`D` global-minimum geometry.

### Regular heptagon plus isolated center

The exact `n=8` global-minimizer regression remains binding for source-population arguments. ZS concerns only the loaded nonisolated terminal response and does not classify or discard contact-isolated source points.

### Cycle-with-leaves near-star response

The existing circular-planar regression still blocks a magnitude inference from topology alone. ZS removes exact cut equality in the actual ZR source but does not stop a sequence of strictly positive cut excesses from tending to zero.

### DP strict pentagons

The defect-face report's strict unit pentagons still show that no fixed positive Oler excess can be charged to each exceptional face. ZS does not alter that face-local regression.

## 7. Failed routes and no-go results

### 7.1 Maximal terminal rank plus thrackle sign pattern directly contradicts PSD

**Proposed implication:** `rank M_B=q-3`, affine kernel, and positive off-diagonal support confined to diameter chords should be impossible.

**Failure:** the regular-hexagon projector above is an exact counterexample at the algebraic/mechanical level. The route is dead without additional large-`D` global-minimum hypotheses such as C43/C66 transport, unit-source capacity, or shell geometry.

### 7.2 A higher-dimensional KKT stress cone should force `e+h=2v-2`

**Proposed implication:** if the mixed rigidity matrix has more than one independent KKT row dependence, move to a boundary stress with a zero coefficient and delete that active row, forcing the active rows to form one rigidity circuit.

**Failure point:** C6 support duality defines a strong row by membership in the support of **some** nonnegative KKT dependence, equivalently by being frozen on the whole fixed-`D` critical cone. A row can have zero coefficient in one boundary KKT stress and remain strong because another stress supports it. Moving inside the stress polytope therefore does not create the finite release required by contact or diameter-pair minimality. No equality `e+h=2v-2` follows.

### 7.3 Strict cuts imply a quantitative response defect

**Proposed implication:** if every terminal cut is strict, summing the inequalities gives an absolute lower bound on `epsilon=(1/2)tr M_B`.

**Failure point:** strictness is qualitative. The existing near-star/cycle-with-leaves regressions show why positive circular-planar couplings can have arbitrarily small aggregate mass under abstract topology. ZS supplies no spectral gap and does not change that limitation.

### 7.4 Face-local area charging

The DP pentagon family remains decisive: exceptional convex unit faces can have Oler excess tending to zero. The linear exceptional-face branch cannot be closed by assigning a uniform independent area penalty to each face.

## 8. Literature imported

No new external literature was imported in this run.

The theorem inherits the already-audited circular-planar response/Kalmanson input through Theorem Z and the existing C53/C56/ZR stack. The September 9 Gorbounov–Kazakov literature note provides independent provenance for circular-planar Kalmanson metrics but is not used as a new logical dependency here.

The exact value `D(6)=2 sin 72 degrees` used to scope the hexagon regression is already part of the repository's supplied-literature baseline (Bateman–Erdős).

## 9. Computation and reproducibility

No computation is a proof dependency and no new script is required.

The regular-hexagon regression is exact and can be checked directly from the displayed trigonometric projector entries. The September 9 campaign's existing exact scripts and unit suite are not rerun or reclassified by this report.

## 10. Canonical promotion recommendation

**Hold as report.**

The proof is short and exact, but ZS depends on the report-level ZR/C56 chain rather than only on currently promoted Target C modules. It should receive an independent dependency review before changing canonical route maps.

If that review passes, update precisely:

1. `docs/targets/target-c/20-psd-response-cut-frontier.md` — replace the C64 terminal-count endpoint by the ZS all-cut strictness theorem in the ZR regime, while retaining C64 as the pre-ZR statement;
2. `docs/targets/target-c/README.md` — add the audited Z/ZC/ZR/ZF/ZS consequence without claiming C-II closure;
3. `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md` — remove exact zero-excess/cut-equality subcases from the generic C-II branch and retain the magnitude/global-face obstruction;
4. `docs/reports/campaign_ledger_2026-09-09.md` — record the strengthened response endpoint and the regular-hexagon no-go regression.

Do not modify module 56 or promote the global face inequality.

## 11. Next run

The highest-value next theorem remains the exact global boundary/face inequality (GF), equivalently `T-h>2f_exc`.

Two routes remain compatible with the audits:

1. **strict-cut to stopped-train transport:** combine ZS with C66 circular-minor transport and DT's exact general-topology train decomposition to construct a non-overcounted map from exceptional-face/train endpoints to response cuts, with an exact surplus beyond the `2f_exc` loss;
2. **source-capacity closure:** combine C52's absorption of bounded-face rattlers with the outer-shell population geometry, keeping all contact-isolated source points, to exclude the quadratic invisible-population alternative left by DF.

A proof that only gives a positive but uncontrolled response defect is insufficient. A proof that only gives `O(D)` face loss is also insufficient; the integer inequality must cross the exact `2f_exc` threshold.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Strongest new theorem:
ZS. In the audited generic C-II ZR regime, the terminal response defect
M_B=Lambda-L_H has ker M_B=span{1,P_x,P_y}, rank q-3. Every principal
submatrix grounded by at least three other terminals is positive definite.
Consequently every proper nonempty boundary cut is strictly response-dominated,
and every terminal satisfies d_b>s_b.

Exact endpoint now:
The exact global closure is still
    b + sum_F(deg F-4) > 2h,
or equivalently, with stopped trains,
    T-h > 2f_exc.
ZS deletes every exact response-cut equality subcase but gives no quantitative gap.

Binding regressions/no-go results:
- regular unit hexagon: exact maximal-rank PSD affine-kernel stress with the allowed
  contact/diameter sign pattern, but not globally optimal;
- higher-dimensional KKT stress cone does not make strong rows weak;
- cycle-with-leaves blocks magnitude from topology alone;
- DP pentagons block uniform face-local Oler charge;
- isolated source points remain and cannot be discarded.

Highest-value next lemma:
Prove the global boundary/face inequality, preferably by a non-overcounted
ZS+C66+DT strict-cut/stopped-train transport, or close the C52 outer-shell
source-capacity alternative.

Authoritative files:
- docs/targets/target-c/56-ci-restored-frontier.md
- docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md
- docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md
- docs/reports/campaign_defect_train_extension_2026-09-09.md
- docs/reports/target_c_minimum_transfer_kernel_collapse_2026-08-31.md
- docs/reports/target_c_psd_response_cut_domination_2026-08-31.md
- this report
```
