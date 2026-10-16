<!-- theorem-state: {"artifact_id":"ART-E5222888FB83","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — attachment-cell perimeter compression

**Date:** 2026-09-10  
**Repository state:** `research/c2-full-source-2026-09-10` from `3f37ef0eab4407a411f9a6d51d016ba600302be7`  
**Run type:** closing proof / exact C-II capacity sharpening  
**Target:** Target C C-II / outer-shell force-bulk  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used only for a separate finite-packing literature check; no external theorem is used below  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

After C-I, work with the lexicographically selected triangle-free global source in C-II, retaining every contact-isolated source point.  Let

- `B_+` be the loaded diameter-endpoint set and `q=|B_+|`;
- `I_r` be the unloaded components of `C[V(C)\setminus B_+]`;
- `A_r` their distinct loaded attachment sets;
- `P_r=conv(A_r)` their harmonic attachment cells;
- `delta_r` the graph diameter of `C[I_r]`, with `delta_r=0` for a singleton;
- `c_I` the number of unloaded components;
- `e_BB` the number of loaded-loaded contacts;
- `s_C` the extra pinned-contact left-nullity;
- `d_H=q-h`, `s_Z=e+h-(2v-2)`, and `k=d_H+s_Z`;
- `R_I=sum_r r_r` the total Eppstein component slack from ZK;
- `s_B` the loaded contact-degree slack from ZK.

C52 has already reduced the source-wide population obstruction to contact-isolated points in the outer contact face.  C45's older cellwise Oler estimate used only `per(P_r)<=pi D`, producing an artificial `D c_I` perimeter loss.  The post-ZF component-diameter ledger gives enough information to remove that loss exactly.

The useful implication chain is

```text
component contact paths
 -> total attachment-cell perimeter O(D)
 -> cellwise Oler with only O(D) total boundary correction
 -> absorb every source isolate lying in attachment-cell interiors
 -> remaining invisible population is localized further into the outer-face region outside the cells.
```

This does not yet control that remaining outer-face population.

## 2. Attachment diameter and perimeter

The contact-path diameter estimate itself already appears in the September 9 ZG chain; the perimeter consequence and its exact post-ZF summation are the new points here.

### Lemma AP.1 — one-cell perimeter bound

For every unloaded component,

\[
\boxed{
\operatorname{diam}P_r\le \delta_r+2,
\qquad
\operatorname{per}P_r\le \pi(\delta_r+2).
}
\tag{AP.1}
\]

### Proof

Take any two attachment terminals `a,b in A_r`.  By definition there are vertices `x,y in I_r` with unit contacts `ax` and `yb`.  Since `I_r` is connected, an internal contact path from `x` to `y` has at most `delta_r` edges.  Concatenating gives a contact path from `a` to `b` of length at most `delta_r+2`.  Every edge has Euclidean length one, so

\[
|a-b|\le\delta_r+2.
\]

Taking the maximum over attachment terminals gives `diam(A_r)<=delta_r+2`, hence the same bound for `P_r=conv(A_r)`.

For every planar convex body, the perimeter-diameter inequality gives

\[
\operatorname{per}P_r\le\pi\operatorname{diam}P_r.
\]

Combining the two inequalities proves AP.1. `square`

## 3. Exact total-perimeter compression

ZK proves the exact component ledger

\[
\boxed{
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C.
}
\tag{AP.2}
\]

ZU gives

\[
\boxed{
c_I+e_{BB}+s_C=q-2+k.}
\tag{AP.3}
\]

Summing AP.1 and using AP.2 gives

\[
\sum_r\operatorname{per}P_r
\le
\pi\left(6+e_{BB}+2s_C-3k-R_I-s_B+2c_I\right).
\]

Substitute AP.3.  The `s_C` terms cancel exactly, as do all but one copy of the loaded-contact and mixed-defect currencies.

### Theorem AP.2 — exact harmonic-cell perimeter ledger

Every post-ZF C-II survivor satisfies

\[
\boxed{
\sum_r\operatorname{per}P_r
\le
\pi\bigl(2+2q-e_{BB}-k-R_I-s_B\bigr).
}
\tag{AP.4}
\]

In particular,

\[
\boxed{
\sum_r\operatorname{per}P_r\le 2\pi q+2\pi\le2\pi^2D+2\pi.
}
\tag{AP.5}
\]

The point is not the crude final constant.  The old cellwise estimate paid `pi D` once per component; AP.4 pays only one global linear boundary budget even when `c_I=Theta(D)`.

### Scope

AP.4 is finite and exact.  It uses only the actual post-ZF contact components and their actual loaded attachments.  It makes no assumption that isolates are negligible, that the force hull is hull-saturated, or that KKT weights have a quantitative lower bound.

## 4. Cell-interior isolate absorption

Let `Z_cell` be the number of contact-isolated source points lying in

\[
\bigcup_r\operatorname{int}P_r.
\]

The interiors of the `P_r` are pairwise disjoint by C43/C49, so every such isolated point belongs to a unique cell.  Write `Z_r` for the isolated source points in `int(P_r)` and put `z=sum_r|Z_r|=Z_cell`.

For each `r`, the set

\[
I_r\cup A_r\cup Z_r
\]

is unit-separated and lies in the convex body `P_r`.  Oler therefore gives

\[
\frac{\sqrt3}{2}
\bigl(|I_r|+|A_r|+|Z_r|-1\bigr)
\le
\operatorname{area}P_r
+
\frac{\sqrt3}{4}\operatorname{per}P_r.
\tag{AP.6}
\]

Sum over `r`.  Put `a_inc=sum_r|A_r|`, `n_I=sum_r|I_r|`, and `m=n_I+q`.  With the ZJ incidence slacks

\[
u_A=a_{inc}-3c_I,
\qquad
p_A=q_{used}+2c_I-2s-a_{inc},
\qquad
u_0=q-q_{used},
\]

ZJ gives

\[
e_{BB}+s_C-k=u_A+p_A+2(s-1)+u_0.
\tag{AP.7}
\]

From the definitions,

\[
n_I+z+a_{inc}-c_I
=m+z+c_I-2s-p_A-u_0.
\]

Using AP.7 to eliminate `2s+p_A+u_0` yields

\[
n_I+z+a_{inc}-c_I
=m+z+c_I-e_{BB}-s_C+k+u_A-2.
\tag{AP.8}
\]

Let

\[
A_{cell}:=\sum_r\operatorname{area}P_r
=\operatorname{area}F-G.
\]

Substituting AP.8 into the summed Oler inequality and then using AP.3 gives

\[
\boxed{
 m+Z_{cell}
\le
\frac{2}{\sqrt3}A_{cell}
+
\frac12\sum_r\operatorname{per}P_r
-q+4+2e_{BB}+2s_C-2k-u_A.
}
\tag{AP.9}
\]

Finally apply AP.4.

### Theorem AP.3 — cell-source capacity with compressed boundary

For `c_I>0`,

\[
\boxed{
\begin{aligned}
 m+Z_{cell}
\le{}&
\frac{2}{\sqrt3}(\operatorname{area}F-G)
+(\pi-1)q
+\left(2-\frac\pi2\right)e_{BB}
+2s_C\\
&-\left(2+\frac\pi2\right)k
-\frac\pi2(R_I+s_B)
-u_A
+\pi+4.
\end{aligned}
}
\tag{AP.10}
\]

Every omitted correction in the second line has the favorable sign.

Since `q<=pi D`, loaded degree at most three gives `e_BB=O(D)`, the exact terminal partition gives `k<=q/2`, and AP.3 gives `s_C=O(D)`.  Therefore AP.10 has the clean asymptotic consequence

\[
\boxed{
 m+Z_{cell}
\le
\frac{2}{\sqrt3}(\operatorname{area}F-G)+O(D).
}
\tag{AP.11}
\]

The `O(D)` is uniform over post-ZF survivors.

## 5. Exact target implication

C48/C49 already gave an `O(D)` force-core capacity estimate by strict-rhombus face charging.  AP.11 does not improve that core-only asymptotic statement.  Its new content is different:

1. the total attachment-cell perimeter itself is only `O(D)`, despite `Theta(D)` possible cells;
2. cellwise Oler can include contact-isolated **source** points in those cells at no quadratic boundary cost;
3. therefore a quadratic KKT-invisible population cannot hide inside a family of many harmonic cells unless those cells themselves carry the corresponding quadratic area.

C52 absorbs isolates in bounded contact faces.  AP.3 is transverse to that decomposition: it also absorbs outer-face isolates that happen to lie inside harmonic attachment cells.

Thus the outer-shell force-bulk endpoint can be narrowed to source points in the outer contact face lying outside the interiors of the attachment cells.

## 6. Exact remaining lemma

A Level I closure still requires a source-wide outer-shell theorem.  One sufficient form is:

> **Outer-shell capacity with loaded-boundary cancellation.**  For the lexicographic post-ZF source, bound the source points in the outer contact face and outside the harmonic-cell interiors so that, after adding AP.6/C52, the total source satisfies
> \[
> n\le \frac{\pi}{2\sqrt3}D^2+1.
> \]

By the canonical strict translated-triangular-lattice comparison, this is impossible for a global minimizer.  An equivalent proof may construct an explicit `n`-point configuration of diameter `<D`.

The remaining theorem must use information absent from dense isolated fillings.  AP.4 alone is only a boundary-complexity bound and does not use global optimality beyond the selected C-II theorem stack.

## 7. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `diam P_r<=delta_r+2` | already available report-level | used in the September 9 ZG attachment-area estimate |
| one-cell perimeter `per P_r<=pi(delta_r+2)` | proved | contact-path diameter plus convex perimeter-diameter inequality |
| exact sum AP.4 | proved | AP.1 + exact ZK and ZU identities |
| total cell perimeter `O(D)` | proved | AP.4 and `q<=pi D` |
| AP.9/AP.10 cell-isolate capacity | proved | facewise Oler on disjoint cell interiors plus exact ZJ incidence algebra |
| all contact-isolated source points lie in cells | false / not claimed | the outer contact face can contain a macroscopic cell-exterior region |
| Level I closure | open | outer-face cell-exterior population remains |

## 8. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | `c_I=0`; cell statement is vacuous and makes no response-trace claim |
| singleton tripod cells | yes | `delta_r=0`, so AP.1 gives `per P_r<=2pi`; the sharper geometric value is `<6`, consistent with AP.1 |
| many-cell triangulation incidence pattern | yes | arbitrary long diagonals cannot be charged independently: actual attachments to one component have diameter at most `delta_r+2`, and ZK controls the sum of `delta_r` |
| one component attached to all terminals | yes | AP.1 permits one `O(D)`-perimeter cell; no area gap is asserted |
| dense isolated filling outside the cells | yes | explicitly remains outside `Z_cell`; this is the live outer-shell obstruction |

## 9. Failed/no-go routes recorded during the run

1. A naive claim `sum_r per(P_r)=O(per(F))` from pairwise interior-disjointness is not justified and is false for arbitrary polygon triangulations; the contact-path diameter input is essential.
2. Near-maximal source perimeter is already canonical at the stronger finite scale `0<=pi D-P<pi sqrt(3)/2`; reproving a weaker `O(1)` deficit gives no progress.
3. The post-ZF face contradiction is exactly `s_Z<0`, while ZF gives `s_Z>=0`; Euler bookkeeping alone cannot change the sign.
4. Iterating the current `0.4702` scalar surplus lower bound is not pursued: the existing report explicitly lacks the complementary upper/global incompatibility.

## 10. Literature imported

No external theorem is logically used in AP.1--AP.11.  A separate search located Wegner's finite-packing inequality as a possible boundary-scale strengthening of Oler, but it is not imported here because no closing implication has yet been proved from it.

## 11. Canonical promotion recommendation

**Hold as report.**  AP.2/AP.3 are exact and useful, but they depend on the post-ZF ZU/ZJ/ZK report chain.  Promotion should follow only if that chain is promoted or jointly audited into the active C-II stack.

If promoted later, the natural target is the attachment-cell / outer-shell frontier, with AP.4 and AP.10 indexed from the Target C route map.

## 12. Next run

Attack the outer-shell cell-exterior population using the fact that every loaded diameter endpoint is an exposed vertex of the full source hull `K`, together with full-source perimeter saturation and FS's common-circumcenter diameter geometry.  The desired theorem must recover the full missing Oler boundary correction, not only an `o(D^2)` density statement.

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem AP:
For post-ZF harmonic attachment cells P_r=conv(A_r),
    per(P_r) <= pi(delta_r+2),
and the exact ZK/ZU ledgers collapse the sum to
    sum_r per(P_r)
      <= pi(2+2q-e_BB-(d_H+s_Z)-R_I-s_B)=O(D).

If Z_cell counts contact-isolated source points in the pairwise-disjoint cell
interiors, cellwise Oler plus ZJ gives the exact AP.10 bound and in particular
    m+Z_cell <= (2/sqrt3)(area(F)-G)+O(D).
Thus many harmonic cells do not create a D*c_I boundary-capacity loophole, and
cell-interior source isolates are absorbed at optimal leading density.

Remaining obstruction:
contact-isolated source points in the outer contact face and outside the harmonic
cell interiors.  Need a source-wide outer-shell capacity theorem strong enough to
force n <= pi D^2/(2sqrt3)+1, or a strict sub-D competitor.
```