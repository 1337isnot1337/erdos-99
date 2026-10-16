# Hostile audit — branch-aware iterative-pruning atomic gap `0.0071`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_branch_aware_iterative_pruning_atomic_gap_0071_2026-09-15.md`
- `research/verify_target_c_branch_aware_atomic_gap_0071.py`

**Disposition:** **PASS at the stated proof-only matched all-train/rhombic scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate strengthens the matched atomic gap from `0.0052` to `0.0071` by using
the conditional `1/10` branch of the already-audited iterative-pruning pair theorem on
part of the dominant-orbit center-imbalance interval.  It does not alter the train
geometry theorem itself.

The main audit risks are:

1. using the `1/10` branch without proving its ratio hypothesis simultaneously for both
   leaf families;
2. losing the direction of monotonicity when replacing the actual dominant mass `W` by
   its lower bound inside the square-root ratio;
3. allowing a phase family to exceed the pair theorem cap `K=2/sqrt(3)`;
4. smuggling the old `g=0.0050` or `0.0052` conclusion into the proof of the stronger
   gap; and
5. transferring the all-train argument to the strict-rhombus graph by deletion rather
   than by an independent application of the physical pair theorem.

All five checks pass.

---

## 1. The contradiction setup is independent of the old atomic-gap value

The candidate assumes only

\[
A\le\bar A=2s+g,
\qquad s=\sqrt{\Delta_2},
\qquad g=0.0071.
\]

The generic orbit inequalities give

\[
4\Delta_2\le\sum_rM_r^2\le WA,
\]

so

\[
W\ge W_0={4s^2\over\bar A}.
\]

This uses no previous positive gap.

For the dominant orbit, with

\[
\delta={W^2\over4}-E,
\qquad R=A-W,
\]

the residual crossing mass is at most `R^2/4`, hence

\[
s^2\le {W^2\over4}-\delta+{R^2\over4}
\le {A^2\over4}-\delta.
\]

Therefore

\[
\delta\le {A^2\over4}-s^2
\le sg+g^2/4=d_0.
\]

This is exactly the generic deficit reduction used before `g=0.0050`; no stronger gap
has been assumed.

**Verdict:** PASS.

---

## 2. The center/leaf weighted correlation is inherited unchanged

Write the dominant exact orbit as

\[
C\ge U\ge V\ge0,
\qquad C+U+V=W,
\]

and let

\[
x=CU-e(C,U),
\qquad y=CV-e(C,V).
\]

The audited dominant-orbit triangle-free calculation gives

\[
C e(U,V)\le Vx+Uy.
\]

With

\[
a=1-V/C,
\qquad b=1-U/C,
\]

this is

\[
a x+b y\le h,
\qquad h=C(U+V)-E.
\]

Putting `z=C-W/2`,

\[
h=\delta-z^2\le d_0-z^2.
\]

The candidate neither strengthens nor changes this correlation.

The denominator later used in the weighted average is positive.  The exact certificate
has

\[
C>0.866,
\qquad W<1.912,
\]

through the contradiction box, so in particular `3C-W>0`; alternatively this follows
from the actual ordering `C>=U>=V` away from the equal-three-class boundary, which the
much narrower `|z|<0.083` domain excludes.

**Verdict:** PASS.

---

## 3. The conditional pair branch is valid for both leaves

The load-bearing new step is the ratio test.

For either leaf `L in {U,V}`, since `C>=L`, the iterative-pruning pair theorem has

\[
m=L,
\qquad e_L=(C+L-K)_+.
\]

The certificate proves throughout the contradiction domain

\[
C<K,
\]

so, on the oversized branch, the function

\[
{e_L\over L}=1-{K-C\over L}
\]

is increasing in `L`.  Both leaves satisfy

\[
L\le U+V=W-C.
\]

Consequently

\[
{e_L\over L}
\le {W-K\over W-C}.
\]

Thus the strong branch condition

\[
e_L/L\le r:=\sqrt{20/29}
\]

holds simultaneously for **both** leaves whenever

\[
(1-r)W+rC\le K.
\]

With `C=W/2+z`, this becomes

\[
(1-r/2)W+r z\le K.
\]

The contradiction hypothesis gives `W<=A<=bar A`, so it is enough that

\[
z\le z_*={K-(1-r/2)\bar A\over r}.
\]

The outward certificate obtains

\[
z_*>0.04428390253.
\]

Therefore the candidate is entitled to use `lambda=sqrt(10)` on every interval lying
wholly below the certified threshold.  It uses `sqrt(29/2)` everywhere else, including
the one grid interval that could straddle the threshold.

There is no hidden assumption that `U=V`, and no individual leaf-size lower bound is
needed.

**Verdict:** PASS.

---

## 4. All phase families remain below the pair-theorem cap

The pair theorem requires each selected family mass to be at most

\[
K=2/\sqrt3.
\]

Since

\[
C={W\over2}+z,
\qquad W\le\bar A,
\qquad |z|\le\sqrt{d_0},
\]

one has

\[
C\le\bar A/2+\sqrt{d_0}.
\]

The exact certificate evaluates this outward and proves

\[
C<1.039<2/\sqrt3.
\]

Because `U,V<=C`, all three families satisfy the cap simultaneously.

**Verdict:** PASS.

---

## 5. The weighted minimax formula keeps the correct inequality direction

For a coefficient `lambda` valid for both leaf pairs, define

\[
F_U=C+U-\lambda\sqrt x,
\qquad
F_V=C+V-\lambda\sqrt y.
\]

The pair theorem gives

\[
F_U,F_V\le K.
\]

The existing weighted-average proof yields

\[
\max(F_U,F_V)
\ge {W+C\over2}
-\lambda\sqrt{h\,{C\over3C-W}}.
\]

Substitution `C=W/2+z` gives

\[
L(W,z,h)
={3W\over4}+{z\over2}
-\lambda\sqrt{h\,{W+2z\over W+6z}}.
\]

For `z<0`, put

\[
R(W,z)={W+2z\over W+6z}.
\]

Direct differentiation gives

\[
R_W={4z\over(W+6z)^2}<0,
\qquad
R_z={-4W\over(W+6z)^2}<0.
\]

Thus replacing `W` by its **lower** bound simultaneously lowers the positive raw term
and raises the square-root loss.  Both changes lower `L`, exactly the safe direction
for a contradiction certificate.

For `z>=0`, `R<=1` is a safe upper bound on the loss.  Also

\[
h\le d_0-z^2,
\]

so the interval verifier maximizes `h` at the point nearest zero.

**Verdict:** PASS.

---

## 6. Outward interval certificate

The committed verifier uses `Fraction` arithmetic for every asserted inequality and
integer-square-root outward enclosures for radicals.  It covers

\[
[-0.083,0.083]
\]

with `16600` intervals of width `10^{-5}`.  The cover is wider than the actual domain
because

\[
0.083^2>d_0.
\]

Its independently reproduced Pyroam output is:

```text
PASS branch-aware atomic gap g=0.0071
intervals 16600
W_lower 1.8975519825748026
d_upper 0.006774023428734097
strong_z_threshold_lower 0.04428390253112821
best_lower 1.1550669956587118
cap_upper 1.1547005383792515
margin_lower 0.00036645727946036413
worst (-0.0197, -0.01969, ...)
```

The load-bearing gap is therefore more than

\[
3.66\times10^{-4},
\]

not a floating-point sign accident.

**Verdict:** PASS.

---

## 7. The proof genuinely improves the `0.0052` route

The new `0.0052` orbit-capacity theorem uses only the universal relaxation

\[
\rho\ge {2\over29}(a+b-K)_+^2.
\]

The candidate uses the same audited physical pair theorem but retains its stronger
`1/10` branch wherever the leaf-to-excess ratio forces that branch.  The old universal
coefficient is still used on the complementary `z` interval.

Hence this is not an incompatible alternative hypothesis or a duplicated payment.  It
is a strictly stronger use of the same pair theorem before any outer-energy or rhombus
incidence budget is spent.

**Verdict:** PASS.

---

## 8. Rhombic-only transfer is independent, not a deletion argument

The candidate repeats the proof on the strict-rhombus train graph, as the previous
hostile-audited minimax theorem does.  The required facts are already established there
independently:

- non-singleton complete rhombic trains are the vertices;
- the graph is simple and triangle-free;
- its crossing mass is the strict-rhombus mass;
- exact crossing atoms again occur at projective separation `pi/3`; and
- the iterative-pruning physical pair theorem applies to its selected phase families.

The argument does **not** infer the rhombic statement by proving the all-train result
and then deleting singleton trains.

Thus

\[
T_R/D\ge2\sqrt{\Delta_2}+0.0071-o(1)
\]

and the standard exact rhombic transfer gives

\[
\sigma_R/D\ge0.0142-o(1).
\]

**Verdict:** PASS.

---

## 9. Final disposition

The candidate is a valid proof-only matched atomic strengthening:

\[
\boxed{
(T-q/2)/D\ge2\sqrt{\Delta_2}+0.0071-o(1),
}
\]

\[
\boxed{
T_R/D\ge2\sqrt{\Delta_2}+0.0071-o(1),
\qquad
\sigma_R/D\ge0.0142-o(1).
}
\]

It does not close C-II.  Its immediate value is that both quantities consumed by the
current outer-energy and complement-rhombus-incidence chains improve simultaneously.
Those downstream scalar/structural consequences should now be recomputed before a new
geometric mechanism is introduced.

**Final verdict:** PASS at stated proof-only scope.  C-II and Level I remain open.
