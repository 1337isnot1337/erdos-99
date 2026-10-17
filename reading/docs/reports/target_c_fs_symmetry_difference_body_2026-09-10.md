> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_symmetry_difference_body_2026-09-10.md) · source SHA-256 `3d3bb0570adad6f2345e442d801241903ef787f15bddd5f0abd734e84831f29c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2AFBCBF490F8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — FS central symmetry sharpens the difference-body area floor

**Date:** 2026-09-10  
**Repository base:** `3f37ef0eab4407a411f9a6d51d016ba600302be7`  
**Run type:** exact/asymptotic cross-report theorem  
**Target:** Target C, C-II  
**Depends on:** FS.4 from `target_c_full_source_circumradius_response_2026-09-10.md`; DA.1–DA.5 from `target_c_difference_body_area_metric_fork_2026-09-09.md`; DB/NB only for the universal numerical corollary  
**External web search:** only for checking whether a sharper unrelated diameter/circumradius area theorem was already standard; no external theorem is used below  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The September 9 difference-body area theorem used the worst-case planar Rogers–Shephard estimate

$$
\operatorname{area}(F-F)\le6\operatorname{area}(F),
$$

which is sharp for triangles. FS.4 supplies information unavailable when DA was written: every selected C-II force hull is `o(D)`-Hausdorff-close to its own half-turn. That makes the factor `6` asymptotically impossible. The correct factor on the present source is `4+o(1)`, the centrally symmetric value.

This raises the post-ZF force-hull area floor from

$$
\frac{y+\sin y}{6}
$$

to

$$
\boxed{\frac{y+\sin y}{4}},
\qquad y=\lim h/D.
$$

In particular, using DB's `y>=2rho`, every unbounded post-ZF survivor satisfies

$$
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge A_{SC}
:=\frac{2\rho+\sin(2\rho)}4
=0.6184708847696858\ldots,
}
$$

where `rho=cos rho=0.7390851332...`. This eliminates the entire previously allowed force-hull area interval below `0.61847 D^2`; it is not merely another scalar stress bound.

---

## 1. Setup and exact FS error scale

Use the same lexicographically normalized C-II source as FS and DA. Translate by the common source circumcenter `o` and write

$$
F_0:=F-o.
$$

FS.4 gives

$$
\boxed{
d_H(F_0,-F_0)\le\varepsilon_D,
\qquad
\varepsilon_D:=2L_D,
}
\tag{SC.1}
$$

with

$$
L_D=\sqrt{D\eta+\eta^2},
\qquad
\eta=3^{1/4}\sqrt D,
\qquad
L_D=O(D^{3/4})=o(D).
\tag{SC.2}
$$

The force hull has diameter exactly `D`, hence

$$
\operatorname{per}(F)\le\pi D.
\tag{SC.3}
$$

No assertion `F=conv A` or small-isolate hypothesis is used.

---

## 2. Near half-turn symmetry forces a `4+o(1)` difference-body factor

### Theorem SC.1 — exact finite near-symmetric difference-body bound

Every selected force hull satisfying SC.1 obeys

$$
\boxed{
\operatorname{area}(F-F)
\le
4\operatorname{area}(F)
+2\varepsilon_D\operatorname{per}(F)
+\pi\varepsilon_D^2.
}
\tag{SC.4}
$$

Consequently

$$
\boxed{
\operatorname{area}(F-F)
\le
4\operatorname{area}(F)+o(D^2).
}
\tag{SC.5}
$$

#### Proof

Hausdorff distance at most `epsilon_D` means

$$
-F_0\subseteq F_0+\varepsilon_D B,
$$

where `B` is the unit Euclidean disk. Therefore

$$
F-F
=F_0+(-F_0)
\subseteq
F_0+(F_0+\varepsilon_D B)
=2F_0+\varepsilon_D B.
\tag{SC.6}
$$

Area is monotone under inclusion. Steiner's formula for a planar convex body gives

$$
\operatorname{area}(2F_0+\varepsilon_D B)
=
\operatorname{area}(2F_0)
+\varepsilon_D\operatorname{per}(2F_0)
+\pi\varepsilon_D^2.
$$

Homogeneity gives

$$
\operatorname{area}(2F_0)=4\operatorname{area}(F),
\qquad
\operatorname{per}(2F_0)=2\operatorname{per}(F),
$$

which proves SC.4.

By SC.2–SC.3,

$$
2\varepsilon_D\operatorname{per}(F)
=O(D^{7/4}),
\qquad
\pi\varepsilon_D^2=O(D^{3/2}),
$$

both `o(D^2)`. This proves SC.5. `square`

The factor four is asymptotically sharp: for a centrally symmetric force hull, `F-F=2F` exactly.

---

## 3. Insert all actual diameter directions

DA defines the projective diameter-direction gaps

$$
g_1,\ldots,g_h,
\qquad
\sum_i g_i=\pi,
\qquad
g_i\ge2a_D,
\qquad
a_D:=\arcsin\frac1{2D},
\tag{SC.7}
$$

and the centrally symmetric diameter polygon

$$
P_H=D\operatorname{conv}\{\pm u_e:e\in E(H)\}
\subseteq F-F.
\tag{SC.8}
$$

Its exact area is

$$
\operatorname{area}(P_H)
=D^2\sum_i\sin g_i.
\tag{SC.9}
$$

Concavity of `sin` under SC.7 gives DA.5:

$$
\sum_i\sin g_i
\ge
(h-1)\sin(2a_D)
+
\sin(2(h-1)a_D).
\tag{SC.10}
$$

Combine SC.4 and `P_H subset F-F`.

### Theorem SC.2 — finite FS-corrected difference-body area floor

$$
\boxed{
\begin{aligned}
\operatorname{area}(F)
\ge{}&
\frac{D^2}{4}
\left[(h-1)\sin(2a_D)
+\sin(2(h-1)a_D)\right]\\
&-\frac{\varepsilon_D}{2}\operatorname{per}(F)
-\frac{\pi}{4}\varepsilon_D^2.
\end{aligned}
}
\tag{SC.11}
$$

Using `epsilon_D=2L_D` and `per(F)<=pi D`, a completely explicit weaker form is

$$
\boxed{
\operatorname{area}(F)
\ge
\frac{D^2}{4}
\left[(h-1)\sin(2a_D)
+\sin(2(h-1)a_D)\right]
-\pi DL_D-\pi L_D^2.
}
\tag{SC.12}
$$

#### Proof

SC.8–SC.10 give

$$
D^2\left[(h-1)\sin(2a_D)+\sin(2(h-1)a_D)\right]
\le\operatorname{area}(F-F).
$$

Apply SC.4 and rearrange. SC.12 follows from SC.3 and `epsilon_D=2L_D`. `square`

---

## 4. Asymptotic area theorem

Take any unbounded post-ZF subsequence on which

$$
\frac hD\to y.
$$

Since

$$
2Da_D\to1,
$$

SC.10 gives

$$
(h-1)\sin(2a_D)\to y,
\qquad
2(h-1)a_D\to y.
$$

The error terms in SC.11 are `o(D^2)`. Therefore:

### Theorem SC.3 — symmetry-corrected diameter-density area floor

$$
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge
A_{sym}(y):=\frac{y+\sin y}{4}.
}
\tag{SC.13}
$$

On `0<=y<=pi`,

$$
A_{sym}'(y)=\frac{1+\cos y}{4}\ge0.
\tag{SC.14}
$$

DB gives

$$
\liminf h/D\ge2\rho,
\qquad\rho=\cos\rho.
$$

Hence every unbounded post-ZF survivor sequence satisfies

$$
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge
A_{SC}:=A_{sym}(2\rho)
=0.6184708847696858\ldots .
}
\tag{SC.15}
$$

For comparison, the older universal floors were

$$
\frac{\sqrt3}{4}=0.4330127019\ldots
$$

from DB and

$$
A_{PI}=\frac12\sin(2\rho)=0.4978566363\ldots
$$

from PI. SC.15 is strictly stronger than both.

The isodiametric maximum is `pi/4=0.785398...`, so SC.15 also gives

$$
\boxed{
\frac{\pi D^2}{4}-\operatorname{area}(F)
\le
(0.1669272787\ldots+o(1))D^2.
}
\tag{SC.16}
$$

---

## 5. Structural effect on the September 9 fork

The DA/DM report had an asymptotic fork:

1. missing loaded hull sides carry at least `0.207258...D` metric excess; or
2. `area(F)>=0.446477...D^2`.

SC.15 makes branch 2 automatic with a much larger constant. Thus the low-area side of that fork disappears after the full-source FS information is brought into the post-ZF geometry.

Likewise, any post-ZF argument whose only area input was DB's `sqrt(3)/4` or PI's `A_PI` may now use SC.15, provided it does not require a representative change that loses FS.4.

---

## 6. Consequence for the pinned/contact-surplus branch

Let

$$
\lambda:=\lim\frac{e_{BB}+2s_C}{D}
$$

along a convergent post-ZF subsequence. The GU component-area argument uses only an area floor for `F` and gives

$$
\liminf\frac GD^2
\ge
A_0-\frac\pi4\lambda^2
\tag{SC.17}
$$

whenever `A_0D^2-o(D^2)` is a valid force-hull area floor. With SC.15,

$$
\boxed{
\liminf\frac GD^2
\ge
L_{SC}(\lambda):=
A_{SC}-\frac\pi4\lambda^2.
}
\tag{SC.18}
$$

The JC joint pocket/face capacity argument implies the necessary condition

$$
L_{SC}(\lambda)
\le
\frac{(\lambda+\pi/2)^2}{4\pi}.
\tag{SC.19}
$$

The left side decreases and the right side increases. Their unique positive intersection is

$$
\lambda_{JC,SC}=0.5688589938734753\ldots .
\tag{SC.20}
$$

Therefore

$$
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.5688589938734753\ldots .
}
\tag{SC.21}
$$

This is a downstream numerical consequence, not the main theorem. The structural advance is SC.13–SC.15, which eliminates a force-hull area class. Further finite scalar iteration is intentionally not treated as an endpoint.

---

## 7. Diameter-cardinality matching corollary

FS.3 also gives a separate cardinality consequence that does not use KKT weights. Put

$$
\Delta_H(D):=
1+\left\lfloor
\frac{\min\{\pi/3,\Theta_D\}}
{2\arcsin(1/(2D))}
\right\rfloor,
$$

where `Theta_D` is FS.3's shared-endpoint angle cap. Then

$$
\Delta(H)\le\Delta_H(D)=O(D^{3/4}).
$$

Any maximal matching `M` in a graph of maximum degree `Delta` covers every edge, and the two endpoints of one matching edge are incident with at most `2Delta-1` edges. Hence

$$
h\le|M|(2\Delta(H)-1).
$$

ZF gives `h>=ceil(D)`, so

$$
\boxed{
\nu(H)
\ge
\left\lceil
\frac{\lceil D\rceil}{2\Delta_H(D)-1}
\right\rceil
=\Omega(D^{1/4}).
}
\tag{SC.22}
$$

The matching edges are pairwise geometrically crossing because `H` is a diameter thrackle. This is new cardinality information but does not by itself control the matching's KKT weight. The odd-shell regression remains compatible with it.

---

## 8. Regression audit

### Regular odd shells

A regular odd shell is asymptotically centrally symmetric, has `h/D->pi`, and its force hull tends to the radius-`D/2` disk. SC.13 gives `A_sym(pi)=pi/4`, exactly consistent with the shell limit. Thus SC does not smuggle global optimality into a false local exclusion.

### Dense isolated fillings

FS.4 and therefore SC.4 remain valid when many KKT-invisible isolated points are present. The proof never sets `n=v`, never bounds the isolate count, and never identifies `F` with the full source hull.

### Response trace / matching weight

SC uses only the geometric Hausdorff half-turn estimate from FS.4. It does not infer an operator norm, a small response trace, or a positive lower bound on individual diameter weights.

### Representative scope

The argument stays on the same contact/diameter-lexicographically normalized source used by FS, ZF, DB, and DA. It does not pass to RA's contact-richer representative.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| SC.4 finite difference-body upper bound | proved | FS.4 Hausdorff inclusion + Steiner formula |
| SC.11 finite force-hull area floor | proved | actual diameter polygon + SC.4 |
| SC.13 asymptotic `(y+sin y)/4` floor | proved | exact DA gap minimization + `epsilon_D=o(D)` |
| SC.15 universal `0.6184708847...` floor | proved conditional on report-level DB | monotonicity + `y>=2rho` |
| SC.21 `0.56885899...` surplus floor | proved conditional on GU/JC candidate chain | substitute SC.15 into their unchanged inequalities |
| `Omega(D^(1/4))` actual diameter matching | proved conditional on FS.3+ZF | maximal-matching count |
| Level I | still open | high-area/high-surplus sources and full population capacity remain possible |

---

## 10. Exact remaining obligation after SC

SC removes the low-force-hull-area branch. A surviving post-ZF source is now simultaneously:

- force-hull area at least `0.6184708847...D^2-o(D^2)`;
- asymptotically half-turn symmetric at Hausdorff error `o(D)`;
- full-diameter graph density `h/D>=2rho-o(1)` with `Omega(D^(1/4))` vertex-disjoint diameter edges;
- pinned/contact surplus at least `0.56885899...D-o(D)` if the GU/JC candidate chain is retained;
- still allowed to carry a large KKT-invisible source population.

The remaining closing theorem must use this high-area/high-surplus geometry to force the whole-source capacity inequality

$$
n-1\le\frac\pi{2\sqrt3}D^2
$$

or a strict sub-`D` competitor. SC alone does not supply that population transfer.
