<!-- theorem-state: {"artifact_id":"ART-4FED2AB87E28","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — correction to DC loaded-boundary contact asymptotic

**Date:** 2026-09-09  
**Repository branch:** `research/disjoint-diameter-gap-2026-09-09`  
**Run type:** adversarial audit / correction  
**Target:** DC small-outer-walk endpoint  
**Depends on:** DC.7, ZU/ZT/HB only for the corrected downstream bounds  

## LEVEL I STATUS

`STILL OPEN`

The completion-shell report DC proves the exact finite inequality

\[
\boxed{e_{BB}\ge q-x_B.}
\tag{C1}
\]

It then states that in the `x_B=o(D)` endpoint, where `q/D->pi`, one has

\[
e_{BB}/D\to\pi.
\]

That conclusion does **not** follow from C1. C1 supplies only a lower bound. No matching upper bound `e_BB<=q+o(D)` is proved in DC.

The correct consequence is

\[
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}}D\ge\pi.
}
\tag{C2}
\]

or, equivalently,

\[
\boxed{e_{BB}\ge(\pi-o(1))D.}
\tag{C3}
\]

All claims in DC about the near-circle force hull, completion shell, and external population remain unchanged. Only the asserted convergence of `e_BB/D` is withdrawn.

---

## 1. What is actually proved

In the small-outer-walk branch,

\[
x_B=o(D),
\qquad
q/D\to\pi.
\]

The outer walk has `q` distinguished intervals between consecutive loaded hull vertices and total excess

\[
\sum_i(\ell_i-1)=x_B.
\]

Therefore all but `o(D)` intervals have length one, and each such interval is a direct unit contact between consecutive loaded hull vertices. Hence

\[
e_{BB}\ge q-o(D)=(\pi-o(1))D.
\]

This proves C2-C3.

Extra loaded-loaded unit chords are not excluded by this argument. The loaded degree-three cap allows a good hull vertex, which already uses its two hull-side contacts, to use one additional loaded-loaded contact. A separate geometric theorem would be needed to show that only `o(D)` such extra chords exist.

---

## 2. Safe upper bounds

ZU gives

\[
c_I+e_{BB}+s_C=q-2+k,
\qquad
k:=d_H+s_Z.
\]

Thus

\[
e_{BB}\le q-2+k.
\tag{2.1}
\]

ZT gives

\[
q=x_B+Q+2k,
\]

so `k<=q/2`. Consequently the current exact stack gives only

\[
e_{BB}\le\frac32q+O(1),
\]

before additional information is inserted. This is fully compatible with a linear number of extra loaded-loaded chords.

Therefore no current report should substitute `e_BB=pi D+o(D)` into an asymptotic ledger unless a new upper theorem is first proved.

---

## 3. A useful inequality that needs only the lower bound

Although equality is unavailable, the lower bound C1 still couples the AR residual ledger to the terminal defect.

Write again

\[
k=d_H+s_Z.
\]

ZU and C1 give

\[
\begin{aligned}
c_I+s_C
&=q-2+k-e_{BB}\\
&\le k+x_B-2.
\end{aligned}
\tag{3.1}

Up to the harmless finite constant, therefore

\[
\boxed{s_C\le k+x_B-c_I+O(1).}
\tag{3.2}
\]

AR gives

\[
S+R_I+s_B=x_B+Q+4-c_I+s_C,
\qquad S=\sum_r\delta_r.
\]

Insert (3.2) and discard `R_I,s_B>=0`:

\[
\boxed{
S
\le
Q+k+2x_B-2c_I+O(1).
}
\tag{3.3}
\]

Since ZT gives `q=x_B+Q+2k`, this may also be written

\[
\boxed{
S
\le
\frac{q+Q}{2}
+\frac32x_B
-2c_I
+O(1).
}
\tag{3.4}
\]

In the near-circle branch `x_B=o(D)`, `q/D->pi`, so

\[
\boxed{
\limsup\frac SD
\le
\frac12\left(\pi+\limsup\frac QD\right)
}
\tag{3.5}
\]

when the displayed limsup exists after subsequence extraction.

This inequality is safe: it uses only the proved lower bound on `e_BB`.

---

## 4. Downstream correction notice

The following phrase in `target_c_completion_shell_nearcircle_2026-09-09.md` is withdrawn:

> `e_BB/D -> pi`.

Replace it conceptually by

> `liminf e_BB/D >= pi`, equivalently there are `(pi-o(1))D` mandatory direct loaded hull-side contacts.

Reports that use only the fact that almost every hull interval is a direct unit contact remain valid. In particular the one-good-end train theorem and the CH/LC boundary-slot arguments do not require an upper bound on all loaded-loaded contacts.

Any report using `e_BB/D->pi` as an equality in ZU/ZK algebra must be re-audited.

---

## 5. Next target

A legitimate strengthening would be:

\[
\boxed{e_{BB}\le q+o(D)}
\]

in the near-circle branch.

This would require excluding a linear matching of extra unit chords among loaded hull vertices. Hausdorff convergence to a disk alone is not enough at unit scale; a proof must use the total turning budget, triangle-freeness, or another active-set property.

Until such a theorem exists, retain only C2-C3.
