# Target C-II — canonical three-cut kernel cusp below `40888`

**Date:** 2026-09-15  
**Status:** proof-only quantitative strengthening  
**Scope:** canonical full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** audited `0.7404D` smallest-leaf center fan; exact laminar interval/multishear theorem; `z>2.217` retention/diameter-edge bound; three-cut kernel theorem; C65 full actual-diameter visibility  
**Certificate:** `research/verify_target_c_three_cut_kernel_cusp_40888.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current three-cut kernel theorem produces three consecutive smallest-leaf O--O
cuts and a nonzero shear kernel

\[
c_1u_1+c_2u_2+c_3u_3=0
\]

such that every actual diameter row outside the two internal switching sets has zero
first squared-length derivative exactly.  Its original averaging argument bounded the
exceptional set, its normalized KKT mass, and the two adjacent phase gaps by `42400`.

The same proof with the current diameter-edge density and a rebalanced fan threshold
improves all three constants to

\[
\boxed{40888}.
\]

Because canonical C65 makes every actual diameter edge positive in a relative-interior
normalized KKT stress, the sharpened exceptional set necessarily contains force-visible
rows of both first-derivative signs.  There is no zero-KKT alternative at this scope.

## Theorem KC40888

Every unbounded canonical survivor sequence in the stated scope has three consecutive
smallest-leaf O--O cuts `tau_1,tau_2,tau_3` and a nonzero normalized kernel
`c=(c_1,c_2,c_3)` with

\[
\max_j|c_j|=1,
\qquad
c_1u_1+c_2u_2+c_3u_3=0,
\]

for which, setting

\[
H_{exc}=H_{sw,1}\cup H_{sw,2},
\]

one has

\[
\boxed{\#H_{exc}<40888+o(1),}
\tag{1}
\]

\[
\boxed{
\sum_{h\in H_{exc}}\beta_h
<{40888\over D}+o(D^{-1}),
}
\tag{2}
\]

and

\[
\boxed{
 d_{\mathbb{RP}^1}(u_1,u_2)
+d_{\mathbb{RP}^1}(u_2,u_3)
<{40888\over D}+o(D^{-1}).
}
\tag{3}
\]

Every diameter row outside `H_exc` has zero first derivative exactly.  On `H_exc`,

\[
\sum_{h\in H_{exc}}\beta_h\ell_h=0,
\qquad
\ell_h={d\over dt}|r_h(t)|^2\Big|_{t=0},
\tag{4}
\]

and canonical C65 gives `beta_h>0` for every actual diameter row.  Mixed infinitesimal
rigidity ensures some `ell_h` is nonzero, so (4) forces

\[
\boxed{
\exists h_+,h_-\in H_{exc}:\qquad
\ell_{h_+}>0>\ell_{h_-}.
}
\tag{5}
\]

If the three shore-oriented train directions span the plane, the parent
implicit-function argument still integrates the kernel to an exact finite multishear on
which every nonexceptional diameter row is unchanged exactly.

---

## 1. Rebalance the good-leaf path

Use the same audited fan inputs

\[
A=0.7404,
\qquad
P=0.0848,
\qquad
N_C<1.063D+o(D).
\]

Choose the fixed rational parameters

\[
\lambda={13553\over20000}=0.67765,
\qquad
r={9713\over20000}=0.48565.
\]

Weighted thresholding gives good-leaf density

\[
g={ (A-\lambda)P\over1.063-\lambda}
=0.013808745296\ldots .
\]

The top-block and lower-phase reserves are respectively

\[
d_{top}=\lambda-(1-r)(1.063)=0.13089595,
\]

\[
d_{low}=\lambda-r(1.063)=0.16140405.
\]

Both are positive.  The standard double count therefore gives one center train crossing
a complement-dual good-leaf path of density

\[
p={d_{top}g\over r(1.063)}
=0.00350125523288\ldots .
\tag{6}
\]

The lower-phase reserve yields the same angular-defect bound as before:

\[
\sum_j q_j
\le {C_{phase}\over d_{low}}+o(1),
\qquad
C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
\tag{7}
\]

---

## 2. Replace the old `2 pi D` switch budget

Every actual diameter interval row starts/stops at most twice along the selected path,
so

\[
\sum_iN_i\le2h_H,
\]

where `h_H` is the actual diameter-edge count.  Hopf--Pannwitz gives `h_H<=q`.

The current uniform retention theorem proves `z>2.217-o(1)` for `t<=1.844` and derives

\[
{q\over D}<1.848545513+o(1).
\]

Therefore

\[
\boxed{
\sum_iN_i<3.697091026D+o(D).
}
\tag{8}
\]

The normalized KKT interval budget remains

\[
\sum_i B_i\le2,
\tag{9}
\]

and (7) gives

\[
\sum_iD(q_i+q_{i+1})
\le {2C_{phase}\over d_{low}}D+o(D).
\tag{10}
\]

---

## 3. Two-boundary averaging

Define

\[
T_i=N_i+DB_i+D(q_i+q_{i+1}).
\]

From (6), (8)--(10), the exact outward one-boundary average is

\[
K={S_{switch}+2+2C_{phase}/d_{low}\over p},
\]

where the certificate evaluates the current algebraic/rational upper bound
`S_switch` from `z>2.217`.

Using the standard Machin enclosure for `pi`, integer-square-root bounds, alternating
Taylor bounds, and the existing outward rational bound on `C_phase`, the verifier gives

\[
K=20443.5596261\ldots .
\]

For consecutive triples put `U_i=T_i+T_{i+1}`.  Every boundary cost occurs in at most
two `U_i`, so some triple obeys

\[
U_i<2K+o(1).
\]

The exact certificate proves

\[
\boxed{
2K=40887.1192523\ldots<40888
}
\tag{11}
\]

with more than `0.8` units of outward-certified margin.

Since every term is nonnegative, the same triple satisfies the count, KKT-mass, and
phase inequalities (1)--(3).

---

## 4. Exact kernel consequences

After selecting the triple, the proof is the already-established three-cut kernel
argument.  Interval support says every row meeting neither all three selected cuts nor
none of them switches at one of the two internal boundaries, so every potentially
nonzero first derivative lies in `H_exc`.

The planar dependence among the three train directions kills the first derivative of
every row meeting all three cuts exactly.  Section 157 stationarity then yields (4).

Canonical mixed infinitesimal rigidity rules out all diameter derivatives vanishing,
while C65 gives strict positivity of every actual diameter coefficient.  Therefore the
exceptional set has both signs as in (5).  This is stronger than the original generic
dichotomy.

When the three directions span `R^2`, the same implicit-function theorem used in the
parent result produces a nonconstant exact angle curve with zero full three-cut
increment, so all nonexceptional diameter rows are unchanged exactly under a genuine
finite contact-preserving source motion.

---

## 5. Frontier

The canonical three-cut normal form is now

```text
three consecutive O-O cuts
+ exact nonzero shear kernel
+ every nonexceptional diameter derivative exactly zero
+ <40888 exceptional actual diameter rows
+ exceptional normalized KKT mass <40888/D + o(1/D)
+ total two-gap phase variation <40888/D + o(1/D)
+ positive-stress exceptional rows of both derivative signs
+ exact finite nonexceptional invariance in the rank-two case
```

This does not close C-II.  It is a quantitative tightening of the positive-stress cusp
that should be combined with the newer adjacent-strip one/two-bar reaction theorem and
the ordered diameter-thrackle interface.

**Disposition:** proved the canonical `40888` three-cut kernel strengthening. C-II and
Level I remain open.
