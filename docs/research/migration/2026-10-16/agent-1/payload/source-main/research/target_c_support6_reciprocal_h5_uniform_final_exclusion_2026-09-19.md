# Target C-II — exact triangle identities plus the adjacent-turn lower bound eliminate the final uniform H5 branch

**Date:** 2026-09-19  
**Status:** proved exclusion of the final three uniform noncollapsed H5 support-six orbits; theorem-state authority unchanged  
**Scope:** the three uniform noncollapsed H5 sign/order orbits `P1,P2,P3` remaining after the simple-wall, double-wall, and uniform-angle exclusions  
**Depends on:** `target_c_support6_reciprocal_h5_triangle_angle_signature_collapse_2026-09-18.md`; `target_c_support6_pentagon_adjacent_lower_h5_p1_exclusion_2026-09-19.md`; the exact force cycles/signs in the current H5 reduction  
**Certificate:** `research/verify_target_c_support6_reciprocal_h5_uniform_final_exclusion_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding work reduced the noncollapsed degree-pure support-six endpoint to three uniform reciprocal `H5` sign/order orbits `P1,P2,P3`.  A new exact linear identity, combined with the just-proved lower bound on adjacent turns of every physical force pentagon, excludes all three at once.

For each of `P1,P2,P3`, the exact reciprocal triangle-angle equations force the same normalized turn sum

\[
\boxed{D=2.}
\tag{0.1}
\]

But the physical source inequalities force

\[
\boxed{D>2.}
\tag{0.2}
\]

Hence none of the three uniform H5 orbits is realizable.  Therefore

\[
\boxed{\text{the noncollapsed degree-pure support-six H5 endpoint is empty.}}
\tag{0.3}
\]

The collapsed support-six branch remains separate and is not excluded by this argument.

---

## 1. The common turn functional

As in the preceding triangle-angle note, normalize every force exterior turn by `pi`:

\[
x_{i,k}=\frac{\delta_{i,k}}{\pi}.
\]

Define

\[
\boxed{
\begin{aligned}
D={}&x_{0,0}+x_{0,1}\\
&+(x_{1,3}+x_{1,4})\\
&+(x_{2,4}+x_{2,0})\\
&+(x_{3,0}+x_{3,1}).
\end{aligned}}
\tag{1.1}
\]

The first two terms are two consecutive exterior gaps of the strict convex ground force hexagon.  Each parenthesized pair is a consecutive pair of exterior turns of one of the physical force pentagons `P1,P2,P3` at reciprocal vertices `1,2,3` respectively.

Let

\[
F_i=\sum_k x_{i,k}=2
\tag{1.2}
\]

be the force-polygon total-turn functional.  For every present reciprocal triangle `{i,j,k}`, let `T_ijk` be the normalized sum of its three ordinary raw reciprocal interior angles, written as the exact affine functional of the force gaps from the preceding note.  Then

\[
T_{ijk}=1.
\tag{1.3}
\]

No metric approximation enters (1.2)-(1.3).

---

## 2. P1 forces D=2

For the exact `P1` force cycles and reciprocal edge signs, coefficient reduction gives

\[
\boxed{
\begin{aligned}
D={}&-2+F_2-2F_3+F_6\\
&+T_{013}+T_{023}+T_{026}-T_{036}+T_{124}\\
&-T_{135}+T_{145}-T_{246}+T_{356}+T_{456}.
\end{aligned}}
\tag{2.1}
\]

Every triangle displayed in (2.1) is present in `K_7\\{16,25,34}`.  Substituting `F_i=2` and `T_ijk=1` gives

\[
D=-2+(2-4+2)+(1+1+1-1+1-1+1-1+1+1)=2.
\tag{2.2}
\]

Thus `P1` forces `D=2`.

---

## 3. P2 forces D=2

For `P2` the same target functional has the shorter exact identity

\[
\boxed{
D=-4+F_1+F_2+T_{012}+T_{023}.
}
\tag{3.1}
\]

Hence

\[
D=-4+2+2+1+1=2.
\tag{3.2}
\]

Thus `P2` also forces `D=2`.

---

## 4. P3 forces D=2

For `P3`, exact coefficient reduction gives

\[
\boxed{
\begin{aligned}
D={}&2-F_0+F_3+F_4-2F_5\\
&+T_{015}+T_{036}-T_{056}+T_{124}-T_{145}\\
&+T_{236}-T_{246}+T_{456}.
\end{aligned}}
\tag{4.1}
\]

Substituting the exact face and triangle values gives

\[
D=2-2+2+2-4+(1+1-1+1-1+1-1+1)=2.
\tag{4.2}
\]

Thus all three final uniform H5 candidates satisfy the same exact equality (0.1).

The companion verifier proves (2.1), (3.1), and (4.1) as identities of affine polynomials in the independent gap variables, not merely after substituting the target values.

---

## 5. The source inequalities force D>2

The ground force polygon in the uniform H5 branch is a strict convex equilateral hexagon.  Therefore every ground exterior turn is positive, in particular

\[
x_{0,0}+x_{0,1}>0.
\tag{5.1}
\]

The new adjacent-turn theorem for every strict physical equilateral force pentagon states

\[
\frac{2\pi}{3}<\delta_{i,k}+\delta_{i,k+1}<\pi.
\]

In normalized units this gives, for the three physical pairs appearing in `D`,

\[
\begin{aligned}
x_{1,3}+x_{1,4}&>\frac23,\\
x_{2,4}+x_{2,0}&>\frac23,\\
x_{3,0}+x_{3,1}&>\frac23.
\end{aligned}
\tag{5.2}
\]

Adding (5.1)-(5.2),

\[
\boxed{D>0+3\cdot\frac23=2.}
\tag{5.3}
\]

This contradicts the exact equality `D=2` from Sections 2-4.

There is no endpoint loophole: all three pentagon lower bounds are strict, and the ground contribution is also strictly positive.

---

## 6. Consequence for support six

The repository's preceding H5 exclusions already remove the nonuniform simple-wall mechanisms and reduce the surviving noncollapsed degree-pure support-six branch to exactly the three uniform candidates treated here.  Sections 2-5 eliminate each of those candidates.  Therefore

\[
\boxed{\text{no noncollapsed degree-pure support-six one-anchor component exists.}}
\tag{6.1}
\]

This is a stronger conclusion than the preceding surface-signature reductions: it removes `P1`, `P2`, and `P3` themselves rather than only individual cone signatures.

The collapsed support-six branch `y_1=...=y_6 != 0` remains.  Its exact local realization certificate shows that a purely local six-pentagon argument cannot remove it.  The remaining support-six task is therefore genuinely global: exclude the collapsed block using train/source integrability, its attachment to the activated/outer complex, or the diameter-locking/KKT system.

No theorem-state file is changed by this note.  C-II remains open.

**Disposition:** all three final uniform noncollapsed H5 support-six orbits are excluded by exact reciprocal triangle identities plus the strict adjacent-turn lower bound.  The noncollapsed degree-pure support-six endpoint is empty; only the collapsed support-six mechanism remains.
