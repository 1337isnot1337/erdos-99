> Generated reading edition · [exact source](../../../docs/reports/target_c_attachment_perimeter_and_cyclic_exceptional_floor_2026-09-11.md) · source SHA-256 `2afc64da088d4eb1900d3d8c315c0196fdb6f8de5f081ebb148354066e659bab`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BC71FA06957D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — linear attachment perimeter and a universal cyclic exceptional-face floor

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** C-II exact consequence / closing-proof attempt  
**Target:** Target C / Level I  
**Active prompt:** `docs/prompts/erdos_problem_99_target_c_full_solution_prompt.md`  
**External web search:** used only to verify public problem status; no external theorem imported  
**Computation:** decimal evaluation only; proofs below are symbolic

## LEVEL I STATUS

`STILL OPEN`.

This report records two consequences that were not extracted in the existing Target C ledger.

First, the total perimeter correction in the harmonic attachment-cell Oler decomposition is only boundary order:

$$
\sum_r \operatorname{per}(P_r)=O(D),
\qquad P_r=\operatorname{conv}(A_r).
$$

The earlier cellwise-Oler report used the cellwise bound `per(P_r)<=pi D`, leaving a potentially quadratic `D c_I` correction.  The component-diameter ledger instead makes the sum linear.

Second, in the post-ZF cyclic circuit branch `s_Z=d_H=0`, the existing cyclic atomic-incidence inequalities already imply the universal defect floor

$$
\boxed{
\liminf_{D\to\infty}{Q\over D}
\ge
\frac45\sqrt{\frac{\pi}{2\sqrt3}}
=0.7618502454911658\ldots .
}
$$

This does not assume the low-surplus regime `nu<1`.  It eliminates the entire `Q=o(D)` cyclic circuit subbranch, including `Q=0`.

Neither theorem settles C-II: the first leaves contact-isolated source points and the area outside the attachment cells; the second still permits a linear family of exceptional stopped-train faces.

## 1. Starting endpoint

C-II retains three branches:

1. cyclic diameter topology with `s_Z=0`;
2. forest diameter topology with `s_Z=0`;
3. positive mixed surplus `s_Z>0`.

The cyclic reports prove `P_F/D->pi`, `b-P_F=o(D)`, disk convergence of `F/D`, `E=O(D)` for the total rhombus angular-area excess, and the atomic endpoint inequalities.  The cellwise Oler report separately bounds the harmonic attachment cells but leaves a `D c_I` perimeter correction.

The desired implications investigated here were

```text
component graph diameter -> total cell perimeter O(D) -> sharpen full-core packing capacity,

cyclic atomic endpoint capacity -> quantitative Q-floor -> eliminate low-Q cyclic topology.
```

Both implications are proved.  Neither is a Level I closure.

## 2. The total harmonic attachment perimeter is O(D)

Use the standard post-ZF notation.  Let `I_r` be the unloaded positive-contact components, let `A_r` be their distinct loaded attachment sets, put

$$
P_r:=\operatorname{conv}(A_r),
$$

let `delta_r` be the internal contact-graph diameter of `I_r`, let `c_I` be the number of unloaded components, and put

$$
k=d_H+s_Z.
$$

The harmonic-component diameter theorem gives

$$
\operatorname{diam}(A_r)\le \delta_r+2.
\tag{AP.1}
$$

Cauchy's perimeter-diameter inequality for a planar convex body therefore gives

$$
\operatorname{per}(P_r)
\le \pi\operatorname{diam}(P_r)
=\pi\operatorname{diam}(A_r)
\le\pi(\delta_r+2).
\tag{AP.2}
$$

Summing over all unloaded components,

$$
\boxed{
\sum_r\operatorname{per}(P_r)
\le
\pi\left(\sum_r\delta_r+2c_I\right).
}
\tag{AP.3}
$$

The exact ZK component-diameter ledger is

$$
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C.
\tag{AP.4}
$$

All omitted terms on the left are nonnegative, so

$$
\sum_r\delta_r
\le6+e_{BB}+2s_C-3k.
\tag{AP.5}
$$

Hence the finite explicit bound

$$
\boxed{
\sum_r\operatorname{per}(P_r)
\le
\pi\bigl(6+e_{BB}+2s_C-3k+2c_I\bigr).
}
\tag{AP.6}
$$

The post-ZF pinned-contact identity

$$
c_I+e_{BB}+s_C=q-2+k
\tag{AP.7}
$$

and `q<=per(F)<=pi D` show that every term in AP.6 is `O(D)`.  Therefore

$$
\boxed{
\sum_r\operatorname{per}(P_r)=O(D).
}
\tag{AP.8}
$$

This is uniform over all post-ZF branches and does not require `s_Z=0`.

### 2.1 Sharpened cellwise Oler consequence

Apply Oler to the unit-separated set `I_r union A_r` in `P_r` and sum over the pairwise interior-disjoint attachment cells:

$$
{\sqrt3\over2}(n_I+a_{inc}-c_I)
\le
\operatorname{area}(F)-G
+{\sqrt3\over4}\sum_r\operatorname{per}(P_r),
\tag{AP.9}
$$

where `n_I=sum_r|I_r|`, `a_inc=sum_r|A_r|`, and

$$
G=\operatorname{area}(F)-\sum_r\operatorname{area}(P_r).
$$

If `v=n_I+q` is the nonisolated-core population, quotient connectivity gives `q-q_used<=e_BB`, while `a_inc>=q_used`.  Thus

$$
n_I+a_{inc}-c_I
\ge v-e_{BB}-c_I.
$$

Using AP.3,

$$
\boxed{
{\sqrt3\over2}(v-e_{BB}-c_I)
\le
\operatorname{area}(F)-G
+{\sqrt3\pi\over4}\left(\sum_r\delta_r+2c_I\right).
}
\tag{AP.10}
$$

Equivalently,

$$
\boxed{
v
\le
{2\over\sqrt3}(\operatorname{area}(F)-G)
+e_{BB}+c_I
+{\pi\over2}\left(\sum_r\delta_r+2c_I\right).
}
\tag{AP.11}
$$

The entire correction after the area term is `O(D)`.  This replaces the earlier `O(D c_I)` correction.  It is a genuine packing-capacity upgrade for the nonisolated core.

### Scope and remaining obstruction

AP.11 counts the actual nonisolated core.  It does not count contact-isolated source points, and it does not prove that the uncovered area `G` is large or small.  Thus it cannot by itself be substituted for a full-source Oler contradiction.

## 3. A local attachment-stress inequality

There is a related exact local inequality that is useful for auditing how pinned-contact surplus can be paid.

Fix one unloaded component `I_r`.  Let

- `n_r=|I_r|`;
- `a_r=|A_r|`;
- `e_r` be its internal contact count;
- `t_r` be the number of contact edges from `I_r` to `A_r`;
- `s_r=e_r+t_r-2n_r-1>=0` be its component stress surplus;
- `c_r` be the number of actual loaded-loaded unit contacts whose two endpoints lie in `A_r`;
- `c_r^partial` be the number of those contacts that are sides of `P_r=conv(A_r)`.

Consider the straight-line contact graph induced on `I_r union A_r`, including the `c_r` loaded-loaded contacts.  It is connected, planar, and triangle-free.  C36 puts `I_r` inside `P_r`; every attachment vertex is an extreme vertex of `P_r` because the loaded terminals lie in strictly convex position.

Let `L_r` be the outer-face walk length of this induced graph.  Between two consecutive vertices of `A_r` on `partial P_r`, the outer-face route has one edge exactly when that side is one of the `c_r^partial` direct contacts; otherwise it has at least two edges.  Hence

$$
L_r\ge c_r^\partial+2(a_r-c_r^\partial)
=2a_r-c_r^\partial.
\tag{AS.1}
$$

A connected triangle-free plane graph with `N` vertices, `M` edges, and outer-face length `L` satisfies

$$
M\le2N-2-{L\over2},
\tag{AS.2}
$$

by Euler plus the fact that every bounded face has length at least four.  Here

$$
N=n_r+a_r,
\qquad
M=e_r+t_r+c_r=2n_r+1+s_r+c_r.
$$

Insert AS.1 into AS.2:

$$
2n_r+1+s_r+c_r
\le2n_r+2a_r-2-a_r+{c_r^\partial\over2},
$$

so

$$
\boxed{
s_r+c_r-{c_r^\partial\over2}
\le a_r-3.
}
\tag{AS.3}
$$

In particular

$$
\boxed{s_r\le a_r-3.}
\tag{AS.4}
$$

Summing gives

$$
\boxed{
s_C\le u_A:=\sum_r(|A_r|-3).
}
\tag{AS.5}
$$

Combining AS.5 with the exact ZJ identity

$$
s_C+r_Q=k+u_A+p_A+(s-1)
$$

gives

$$
\boxed{
r_Q\ge k+p_A+(s-1)+(u_A-s_C)\ge k+s-1.
}
\tag{AS.6}
$$

Thus mixed defect cannot be paid solely by hidden pinned-contact self-stress; it forces loaded-quotient connectivity slack unless extra attachment incidence is present.

This inequality is independent of AP and of the `s_Z=0` circuit sparsity lemma.  The latter has a different hypothesis and counts all mixed edges among attachments.

## 4. Cyclic circuit branch: exceptional defect is at least 0.761850 D

Assume now

$$
s_Z=d_H=0
$$

and pass to an unbounded cyclic Woodall sequence.  Use the notation of the cyclic atomic-incidence report:

$$
\xi=\lim {Q\over D},
\qquad
\varphi=\lim {f\over D},
\qquad
w=\xi-\varphi\ge0,
\tag{CQ.1}
$$

along an arbitrary convergent subsequence.  Here `f` is the number of bounded exceptional faces.  Since `f<=Q<=q<=pi D+o(D)`, one has

$$
0\le w\le\pi.
\tag{CQ.2}
$$

The same report proves the rhombus-area lower bound

$$
r:=\lim {R\over D^2}
\ge
r_{min}(w)
:={\pi^2-w^2\over2\pi\sqrt3}
=\Delta\left(1-{w^2\over\pi^2}\right),
\qquad
\Delta={\pi\over2\sqrt3},
\tag{CQ.3}
$$

and the actual stopped-train endpoint-capacity inequality

$$
4\sqrt r\le\xi+4\varphi.
\tag{CQ.4}
$$

Since `xi=w+varphi`, CQ.4 and CQ.3 give

$$
w+5\varphi\ge4\sqrt{r_{min}(w)},
$$

hence

$$
\xi=w+\varphi
\ge
{4\over5}\left(w+\sqrt{r_{min}(w)}\right).
\tag{CQ.5}
$$

It remains only to minimize the right side without importing the low-surplus condition used later in the atomic report.

Write `x=w/pi in [0,1]`.  Then

$$
w+\sqrt{r_{min}(w)}
=
\pi x+\sqrt\Delta\sqrt{1-x^2}.
\tag{CQ.6}
$$

The right side is a concave function of `x` on `[0,1]`.  A concave function on an interval attains its minimum at an endpoint.  The endpoint values are

$$
\sqrt\Delta
\quad\text{and}\quad
\pi.
$$

Since `sqrt(Delta)<pi`, CQ.6 yields

$$
w+\sqrt{r_{min}(w)}\ge\sqrt\Delta.
\tag{CQ.7}
$$

Substitute into CQ.5:

$$
\boxed{
\xi\ge {4\over5}\sqrt\Delta
={4\over5}\sqrt{\frac\pi{2\sqrt3}}.
}
\tag{CQ.8}
$$

Because the initial convergent subsequence was arbitrary, this proves:

### Theorem CQ — universal cyclic exceptional-face floor

Every unbounded sequence of post-ZF cyclic circuit survivors satisfies

$$
\boxed{
\liminf_{D\to\infty}{Q\over D}
\ge
{4\over5}\sqrt{\frac\pi{2\sqrt3}}
=0.7618502454911658\ldots .
}
\tag{CQ.9}
$$

The decimal is not used in the proof.

### Immediate consequences

Because `Q<=e_BB`,

$$
\liminf {e_{BB}\over D}
\ge {4\over5}\sqrt{\frac\pi{2\sqrt3}}.
\tag{CQ.10}
$$

In particular the cyclic circuit branch has `Q=Omega(D)` and `e_BB=Omega(D)` independently of whether `nu=(e_BB+2s_C)/D` is below or above one.  Thus `Q=0`, `Q=o(D)`, and the pure-rhombic cyclic circuit subbranch are all impossible for sufficiently large survivors.

## 5. Why CQ is not already the 0.9955 surplus theorem

The cyclic atomic-incidence report uses CQ.3-CQ.4 together with the low-surplus cavity inequality

$$
w\ge\pi\sqrt{1-\nu^2}
$$

and `xi<=nu` to force `nu>=0.995540...`; its endpoint is then excluded qualitatively.

CQ instead removes `nu` entirely and minimizes the train/area inequalities directly.  It therefore applies to the unrestricted high-surplus cyclic circuit branch, where the existing 0.9955 theorem explicitly leaves an obstruction.  It is weaker numerically as a bound on `nu` but stronger structurally as a universal lower bound on the actual exceptional-face defect `Q`.

## 6. Regression audit

- **Regular odd shell:** has `s_Z=2`, not the circuit phase; CQ does not apply.
- **Pure rhombic disk:** has `Q=0`; CQ excludes it only under the full cyclic post-ZF/global-optimum hypotheses used by the atomic-incidence theorem.
- **Many pentagonal exceptional faces:** allowed.  They can realize `Q=Theta(D)` and are the principal surviving CQ regression.
- **One giant exceptional face:** allowed away from the 0.9955 endpoint.  The endpoint-exclusion report rules out only the equality geometry where its boundary directions are simultaneously forced uniform and three-atomic.
- **Contact-isolated source points:** retained.  CQ uses the full-source cyclic Reuleaux/cap geometry already built into its inherited dependencies.
- **Positive mixed surplus:** outside CQ's scope; AP and AS remain valid post-ZF there.

## 7. Failed routes from this run

1. A provisional attempt to derive a `pi/3` cyclic surplus floor was rejected.  It incorrectly identified the attachment-incidence count `sum_r|A_r|` with the unrelated outer-pocket count `a`.  No such bound is used here.
2. The common bridge block does not force CR4's vertex-disjoint terminal paths through that block; CR4 therefore gives no linear port contradiction.
3. The signed `K_4^o/K_3^=` minor consequence is too weak for geometric closure.  A unit square already realizes the `K_4^o` switching pattern with four contact sides and two diameter diagonals.
4. The five-sector rhombic regression cannot be excluded by positive pinned stress alone; its missing global feature is the large set of nonextreme pinned boundary vertices.

## 8. Exact remaining obstruction

After CQ, the cyclic circuit branch cannot hide in a rhombic or sublinear-defect topology.  It must carry at least

$$
0.76185024549\ldots D
$$

units of bounded exceptional-face degree defect.  The unresolved cyclic mechanism is therefore a boundary-order family of stopped-train exceptional faces, potentially mostly near-pentagonal, that absorbs the atomic train endpoints while preserving the global source-capacity inequalities.

AP simultaneously removes the old many-cell perimeter obstruction from harmonic-cell Oler accounting.  The remaining AP obstruction is source population outside the nonisolated attachment cells, especially contact-isolated points in exceptional/outer/cap regions.

A Level I closure still requires an exact full-source inequality or admissible finite motion that handles those regions, plus the forest `s_Z=0` and `s_Z>0` branches.

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| AP.3/AP.6 total attachment perimeter bound | proved | C44 component diameter + Cauchy + ZK |
| AP.11 core cellwise-Oler correction is O(D) | proved | AP plus quotient connectivity |
| AS.3 local attachment/contact inequality | proved | planar Euler + exact outer-face lower bound |
| AS.5 `s_C<=u_A` | proved | sum of AS.4 |
| CQ.9 cyclic `Q/D` floor | proved | inherited atomic area/endpoint inequalities + concave one-variable minimization |
| cyclic branch closed | not proved | linear exceptional-face family remains |
| forest circuit branch closed | not proved | common 2-connected hub + caterpillar forest remains |
| `s_Z>0` reduced to circuit phase | not proved | conformal circuit extraction does not preserve full source/global hypotheses |
| Level I | still open | all quantifiers not settled |

## 10. Promotion recommendation

**Hold as report pending independent audit.**  The statements materially sharpen C-II, but they combine several unpromoted post-ZF/cyclic reports.  Do not update the authoritative Target C route map until their dependency chain and the new algebra have been audited explicitly.

## 11. Next run

The highest-value next theorem is a quantitative exceptional-face endpoint-capacity inequality stronger than the raw incidence count `Q+4f`, using the convex unit-edge geometry of the exceptional faces.  CQ proves a linear exceptional population is unavoidable; a successful theorem must show that such faces cannot absorb the required atomic stopped-train endpoints at the global disk/low-rhombus-defect scale.

In parallel, for the forest circuit branch, combine the common 2-connected bridge block with the exact bridge-cut bypass law `t=3+delta_A+delta_B` and Woodall's caterpillar decomposition.  Any summable cut deficit that forces `d_H` or `e_BB+2s_C` beyond the exact ZK/PC capacity would be decisive.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New AP theorem:
For every post-ZF C-II source and every unloaded component attachment polygon
P_r=conv(A_r), diam(P_r)<=delta_r+2. Hence
    sum per(P_r) <= pi(sum delta_r+2c_I)
                 <= pi(6+e_BB+2s_C-3(d_H+s_Z)+2c_I)
                 = O(D).
Thus the summed cellwise-Oler boundary correction is O(D), not O(D c_I).

New AS theorem:
For one unloaded component, if c_r counts loaded-loaded contacts inside A_r and
c_r^partial counts those on partial conv(A_r), planar triangle-free Euler counting gives
    s_r+c_r-c_r^partial/2 <= |A_r|-3.
In particular s_C<=sum_r(|A_r|-3)=u_A.

New CQ theorem:
In cyclic s_Z=d_H=0, atomic-incidence gives
    r >= r_min(w)=Delta(1-w^2/pi^2),
    4sqrt(r) <= xi+4phi,
where xi=Q/D, phi=f/D, w=xi-phi, Delta=pi/(2sqrt3).
Thus
    xi >= (4/5)(w+sqrt(r_min(w))).
For 0<=w<=pi the bracket is concave in w/pi, so its minimum is sqrt(Delta).
Therefore
    liminf Q/D >= (4/5)sqrt(pi/(2sqrt3))
               = 0.7618502454911658...
without assuming nu<1.

Exact surviving cyclic obstruction:
a linear family of bounded exceptional stopped-train faces can still absorb the
atomic endpoints. Forest s_Z=0 and s_Z>0 remain open as well.
```