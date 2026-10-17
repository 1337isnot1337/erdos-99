> Generated reading edition · [exact source](../../../docs/reports/target_c_branchwise_response_beta_matching_2026-09-09.md) · source SHA-256 `d36b687e9c7b0d2544d8679966576668e82b3d7557d81d44e011bc4e8dd9cc92`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-F41D1D9F173E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — BRM: response and diameter reaction match branch-by-branch at the near-zero star center

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** exact PSD cut theorem / C66-C71 branch reconciliation  
**Target:** Target C C-II, near-zero response phase  
**Depends on:** C35, C64, C66, C70/C71, harmonic response decomposition  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

C66 says the mechanical diameter reaction becomes a star around one loaded terminal `z` when `D epsilon ->0`. C70 says the total electrical response also becomes a star around `z`. Those two statements do not by themselves say that the mechanical and electrical masses use the same physical components of `C-z`.

BRM proves exactly that.

Delete `z` from the positive contact graph and let `R` be any connected component of `C-z`. Put

```math
B_R:=B_+\cap R.
```

Define

```math
r_R:=\sum_{k\in B_R}c_{zk},
\tag{BRM.1}
```

the response mass from `z` into branch `R`, and retain C71's mechanical quantities

```math
w_R:=\sum_{\substack{zk\in H\\k\in R}}\beta_{zk},
\tag{BRM.2}
```

```math
\lambda_R:=
\sum_{\substack{ab\in H,\ a\in B_R,\ b\notin B_R\\z\notin\{a,b\}}}
\beta_{ab}.
\tag{BRM.3}
```

Then the full response/diameter PSD comparison gives the exact finite estimate

```math
\boxed{
0
\le
r_R-(w_R+\lambda_R)
\le
2\varepsilon |B_R|.
}
\tag{BRM.4}
```

Since `|B_R|<=q<=pi D`,

```math
\boxed{
0
\le
r_R-(w_R+\lambda_R)
\le
2\pi D\varepsilon.
}
\tag{BRM.5}
```

At the C66 center,

```math
0\le\lambda_R\le\delta_z
:=\sum_{h\not\ni z}\beta_h
\le\frac{723\pi}{49}D\varepsilon.
\tag{BRM.6}
```

Therefore, under

```math
D\varepsilon\to0,
```

every physical branch satisfies uniformly

```math
\boxed{r_R-w_R=o(1).}
\tag{BRM.7}
```

In particular the electrically dominant and mechanically dominant physical branches coincide asymptotically.

Combined with NLC, any branch carrying nonvanishing star beta mass must contain a harmonic component with an attachment pair at distance `D-o(D)` and graph diameter `D-o(D)`. Combined with C71, the single-port branch has both `1-o(1)` mechanical star mass and `1-o(1)` electrical response mass whenever the multi-port branch carries `o(1)` star mass.

---

## 1. There is no response coupling between different components of `C-z`

Take two distinct components `R,S` of `C-z`, and loaded terminals

```math
a\in B_R,
\qquad b\in B_S.
```

There is no direct contact edge `ab`, because that would connect `R` and `S` in `C-z`.

There is also no unloaded harmonic component attached to both `a` and `b`: such a component gives an `a-b` contact path whose internal vertices are unloaded and which avoids `z`, again connecting `R` and `S` in `C-z`.

C41's response decomposition is the sum of direct loaded-loaded contact responses and harmonic-component responses. Hence

```math
\boxed{c_{ab}=0}
\qquad
(a\in B_R,\ b\in B_S,\ R\ne S).
\tag{BRM.8}
```

Thus the only response conductance crossing the terminal cut `(B_R,B_+\setminus B_R)` is the response between `B_R` and `z`:

```math
\boxed{
\sum_{\substack{a\in B_R\\b\notin B_R}}c_{ab}=r_R.
}
\tag{BRM.9}
```

---

## 2. The matching diameter cut is exactly `w_R+lambda_R`

The diameter edges crossing `(B_R,B_+\setminus B_R)` split into two disjoint types:

1. star edges `zk` with `k in R`, of total beta mass `w_R`;
2. nonstar diameter edges with exactly one endpoint in `B_R`, of total beta mass `lambda_R`.

Therefore

```math
\boxed{
\sum_{\substack{a\in B_R\\b\notin B_R}}
\beta_{ab}
=w_R+\lambda_R.
}
\tag{BRM.10}
```

---

## 3. PSD controls every terminal cut from both sides

C64 gives

```math
M:=\Lambda-L_H\succeq0,
\qquad
\operatorname{tr}M=2\varepsilon.
\tag{3.1}
```

Let `x=1_{B_R}` be the indicator of the terminal subset `B_R`. For a weighted Laplacian, the quadratic form of an indicator is exactly the weight crossing the cut. Hence BRM.9-BRM.10 give

```math
x^TMx
=r_R-(w_R+\lambda_R).
\tag{3.2}
```

PSD gives the lower bound

```math
x^TMx\ge0.
\tag{3.3}
```

For the upper bound, every eigenvalue of a PSD matrix is at most its trace, so

```math
\lambda_{max}(M)\le\operatorname{tr}M=2\varepsilon.
```

Therefore

```math
x^TMx
\le
2\varepsilon\|x\|^2
=2\varepsilon |B_R|.
\tag{3.4}
```

Equations (3.2)--(3.4) prove BRM.4. Since `|B_R|<=q<=pi D`, BRM.5 follows.

---

## 4. Near-zero branchwise matching

At the C66 center, every nonstar crossing edge counted by `lambda_R` contributes to the total off-star diameter mass

```math
\delta_z=1-S_z.
```

Thus

```math
\lambda_R\le\delta_z.
```

E43R gives

```math
\delta_z\le\frac{723\pi}{49}D\varepsilon.
```

From BRM.4,

```math
0\le r_R-w_R
=\lambda_R+x^TMx
\le
\left(\frac{723\pi}{49}+2\pi\right)D\varepsilon.
\tag{4.1}
```

The right side is independent of the branch. Hence if `D epsilon->0`,

```math
\sup_R|r_R-w_R|\to0,
```

which proves BRM.7.

Because `deg_C(z)<=3`, there are at most three nonempty physical branches. No loss accumulates by summing them.

---

## 5. Combine with NLC

NLC shows that the total `z`-incident response mass on pairs longer than `D-1` is `1-o(1)`.

Let `R` be a physical branch with

```math
w_R\ge c>0
```

along a subsequence. BRM gives

```math
r_R\ge c-o(1).
```

The global response mass on pairs of length at most `D-1` is `o(1)`, so all but `o(1)` of `r_R` is carried by pairs `zk` with

```math
|z-k|>D-1.
```

Those pairs cannot be direct contacts. Therefore some unloaded harmonic component contained in `R` is attached to both `z` and such a `k`. C40 then gives

```math
\boxed{
\delta_r>D-3.
}
\tag{BRM.11}
```

Thus every physical branch with nonvanishing mechanical star mass contains an actual depth-`D` harmonic response carrier.

By the same coordinate-energy argument as NLC, a branch with asymptotic response/star mass `w_R` contains total component contact stress at least

```math
(w_R-o(1))(D-1)^2.
\tag{5.1}
```

So branchwise beta mass, electrical response mass, and mechanical contact-stress fraction all agree asymptotically in the near-zero regime.

---

## 6. Reconcile with C71

C71 splits components of `C-z` into single-port and at most one multi-port component.

For single-port branches, C71 proves that the second-largest star beta mass is `o(1)` in the C66 phase. BRM transfers this directly to response:

```math
\boxed{
\text{among single-port branches, at most one can carry nonvanishing response mass.}
}
\tag{BRM.12}
```

If the multi-port component carries `o(1)` star mass, then one single-port branch has

```math
w_R=1-o(1).
```

BRM gives

```math
r_R=1-o(1),
```

and NLC/HSR give

```math
S_R=D^2-o(D^2),
```

with an internal harmonic component of graph diameter `D-O(1)`.

If the multi-port component carries a nonvanishing fraction, BRM says it carries the same nonvanishing electrical fraction. Any additional nonvanishing single-port fraction creates a second depth-`D` harmonic branch, and NLC then forces pinned/contact slope at least two.

This is the precise remaining split.

---

## 7. Regression audit

- BRM uses components of the **full physical graph `C-z`**, not unloaded harmonic components. The two decompositions are related but not identical.
- `lambda_R` is retained explicitly; branch response is not asserted equal to star beta mass at finite `D`.
- The upper cut error uses `|B_R|`; the passage to `o(1)` needs the strong phase `D epsilon->0`, not merely `epsilon->0`.
- PSD gives response cut >= diameter cut. The reverse approximation is from the trace bound, not another Loewner inequality.
- A multi-port return component remains possible. BRM does not by itself exclude it.

## 8. Next target

The near-zero phase is reduced to two physical cases:

1. **single-port:** one component of `C-z` carries `1-o(1)` beta star mass, response mass, and contact-stress mass, and contains a depth-`D` harmonic carrier;
2. **return/multi-port:** one component using two or three contacts at `z` carries nonvanishing beta/response/stress mass; if another branch is also nonvanishing, NLC forces pinned/contact slope at least two.

The single-port case should now be attacked with C72/C74 radial coarea plus the depth-`D` harmonic component. The return case should be attacked by the angular separation of its two unit ports and the fact that its response cut is quantitatively matched to its star beta load.

## 9. Compact handoff

```text
BRM branchwise matching.
Delete C66 center z from contact graph. For component R of C-z let
    B_R=B+ intersect R,
    r_R=sum_{k in B_R} c_zk,
    w_R=sum_{zk in H,k in R} beta_zk,
    lambda_R=nonstar beta cut mass of B_R.
There is no response between terminals in different C-z branches, so response cut(B_R)=r_R.
Diameter cut(B_R)=w_R+lambda_R.
With M=Lambda-L_H PSD, trM=2epsilon,
    0 <= r_R-(w_R+lambda_R)
      =1_{B_R}^T M 1_{B_R}
      <=2epsilon |B_R|
      <=2pi D epsilon.
At C66 center lambda_R<=delta_z=O(D epsilon), hence
    r_R=w_R+o(1)
uniformly when D epsilon->0.
So mechanical and electrical star masses use the same physical branches.
Any branch with w_R>=c>0 has long z-response c-o(1), contains a harmonic component with delta>D-3, and carries >=(c-o(1))D^2 contact stress.
C71 then leaves one dominant single-port branch or a genuine multi-port return branch.
```
