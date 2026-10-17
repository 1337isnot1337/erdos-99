# Target C-II — phase-resolved paired remainder excludes the full-core branch through `t<=1.844`

**Date:** 2026-09-15
**Status:** proof-only full-core Type-II strengthening
**Scope:** full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.844`
**Dependencies:** scope-safe matched atomic gap `g=0.007707`; residual-stability theorem; hostile-audited two-leaf outer-energy architecture; repaired strong center/leaf branch; paired-remainder bathtub theorem
**Certificate:** `research/verify_target_c_phase_resolved_remainder_closure_t1844.py`
**LEVEL I STATUS:** `STILL OPEN. C-II STATUS REQUIRES GLOBAL BRANCH CHECK.`

The previous paired-remainder theorem excluded the full-core Type-II branch through

\[
t={q-k\over D}\le1.84370.
\]

Its final energy estimate still discarded information: after proving lower bounds on the retained outer-occurrence masses in all three exact phases, it replaced both leaf masses by one common floor before charging the leaf remainders. Near the structural endpoint `t=1.844` that replacement loses a macroscopic amount of retained occurrence mass.

Keeping the actual three phase masses gives a one-dimensional convex allocation problem. An exact outward-rational certificate then proves

\[
\boxed{
 t\le1.844
 \quad\Longrightarrow\quad
 \text{no full-core/no-container Type-II survivor.}
}
\tag{PR.1}
\]

The final contradiction margin is more than

\[
4\times10^{-6}D
\]

in normalized outer directional energy.

No global C-II closure is asserted in this note until the canonical branch decomposition is checked: (PR.1) closes the entire full-core low-`t` interval through the structural value `1.844`, but the repository must still certify that no independent branch lies outside this scope.

---

## 1. Exact endpoint package at `T=1.844`

Retain the standard notation

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_{707}=2\sqrt{\Delta_2}+0.007707,
\]

\[
x={\kappa\over2},
\qquad
h=U_{net}-C_{707},
\qquad
c={21\over20}=1.05,
\]

and

\[
2\delta+x+h
=R_t:={9t\over2}-2\pi-C_{707}.
\tag{PR.2}
\]

At

\[
T={461\over250}=1.844,
\]

the exact certificate uses

\[
H={1121\over500000}=0.002242.
\]

The inherited residual-localization argument remains in scope and gives

\[
\boxed{h<H-o(1).}
\tag{PR.3}
\]

The exact localization margin is

\[
>5.27\times10^{-7}.
\]

Consequently the dominant exact orbit obeys the safe rounded bounds

\[
\boxed{W=C+U+V<1.914575-o(1),}
\tag{PR.4}
\]

\[
\boxed{E_{dom}>0.90689828-o(1),}
\tag{PR.5}
\]

and the outer directional-energy budget has ceiling

\[
\boxed{
\delta<0.051241039547+o(1).
}
\tag{PR.6}
\]

The residual-stability scope gate is still well inside its audited range:

\[
U_{net}<1.956656<2.013.
\]

---

## 2. Retained dominant outer mass exceeds `2.217236D`

Let `z` denote the retained outer-occurrence mass in the dominant exact three-phase orbit, normalized by `D`. The retained-mass/complement-incidence system from the previous paired-remainder theorem is unchanged.

Set

\[
Z={554309\over250000}=2.217236.
\]

At the boundary `delta=F(Z)`, where

\[
F(s)=s-6\sin(s/6),
\]

the corresponding residual value satisfies

\[
0<h_*<H-10^{-6},
\]

and the capped survivor excess is strictly negative:

\[
\boxed{
Z+{c^2h_*^2\over2(1-F(Z))}
-\pi+{T\over2}+ch_*
<-6\times10^{-7}.
}
\tag{PR.7}
\]

The inherited monotonicity in `x,h` therefore gives

\[
\boxed{z>Z-o(1).}
\tag{PR.8}
\]

---

## 3. Every exact phase retains more than `0.6472D`

Write the retained phase masses as

\[
z_C,z_U,z_V,
\qquad
z_C+z_U+z_V=z.
\]

The one-well phase energy function is

\[
 f(s):=s-2\sin(s/2).
\tag{PR.9}
\]

It is increasing and convex on the present interval. The phasewise bathtub inequality gives

\[
\delta\ge f(z_C)+f(z_U)+f(z_V)-o(1).
\tag{PR.10}
\]

Set

\[
A={809\over1250}=0.6472.
\]

If one phase had mass at most `A`, convexity makes the cheapest allocation of the other two phases equal. Thus

\[
f(z_C)+f(z_U)+f(z_V)
\ge f(A)+2f\left({Z-A\over2}\right)-o(1).
\]

The exact certificate gives

\[
 f(A)+2f((Z-A)/2)-\delta_{max}
>1.84\times10^{-7}.
\]

Hence

\[
\boxed{z_C,z_U,z_V>A-o(1).}
\tag{PR.11}
\]

---

## 4. Both leaf train masses are below `0.59102D`

Set

\[
U_0={29551\over50000}=0.59102,
\qquad
W_0=1.914575,
\qquad
E_0=0.90689828.
\]

Assume one leaf train mass is at least `U_0`; call the larger leaf `U`. The repaired strong center/leaf theorem must be scope-checked on the original configuration before any adverse replacement. Since `z_V>A` and each train contributes at most two retained outer occurrences,

\[
V>{A\over2}-o(1).
\]

Therefore

\[
C+U=W-V<W_0-{A\over2}+o(1).
\]

On the contradiction branch `U>=U_0`, the strong-pair excess ratio is bounded by

\[
{W_0-A/2-2/\sqrt3\over U_0}<0.739<\sqrt{20/29}.
\tag{PR.12}
\]

Thus the physical `1/10` center/leaf correlation branch is valid for both leaves before replacement.

After making the adverse replacements `W->W_0`, `U->U_0`, put

\[
V=W_0-C-U_0
\]

and

\[
\begin{aligned}
G(C)=&\ C(W_0-C)\\
&-{1\over10}\left(1-{V\over C}\right)(C+U_0-K)^2\\
&-{1\over10}\left(1-{U_0\over C}\right)(C+V-K)^2,
\qquad K={2\over\sqrt3}.
\end{aligned}
\tag{PR.13}
\]

The exact inherited derivative identity gives `G''<-2` on the middle interval. The two generic-capacity tails are excluded separately. At

\[
c_0={23139\over25000}=0.92556,
\]

the tangent bound gives

\[
\max G
\le G(c_0)+{G'(c_0)^2\over4}
<E_0-5.8\times10^{-7}.
\tag{PR.14}
\]

This contradicts (PR.5). Therefore

\[
\boxed{U,V<U_0-o(1).}
\tag{PR.15}
\]

---

## 5. Total bad leaf-pair weight is below `0.05285D`

For a retained O--O train in either leaf phase, call it **bad** if its center crossing degree is at most half of the center family. The hostile-audited center/leaf correlation bounds total bad retained pair weight across both leaves by

\[
{2[C(W-C)-E_{dom}]\over C-U}+o(1).
\tag{PR.16}
\]

The denominator is positive in the current box. With the adverse constants `W_0,E_0,U_0`, set

\[
B={1057\over20000}=0.05285.
\]

The assertion that (PR.16) is below `B` reduces to a quadratic in `C`; the exact discriminant satisfies

\[
\boxed{\operatorname{disc}<-4.75\times10^{-5}.}
\tag{PR.17}
\]

Therefore the total bad weight across both leaves is less than

\[
BD+o(D).
\]

Put

\[
\boxed{S:=U_0+B=0.64387.}
\tag{PR.18}
\]

For the actual retained occurrence mass `z_i` in leaf `i`, the terminal-count inequality gives retained O--O pair weight at least `z_i-U_0-o(1)`. Charging the entire bad total `B` adversarially to either leaf leaves good pair weight

\[
\boxed{G_i\ge[z_i-S]_+-o(1).}
\tag{PR.19}
\]

---

## 6. The phase-resolved paired-remainder lemma

This is the new step.

Let

\[
a:=2-\sqrt3.
\]

The two leaf phases differ by exactly `pi/3`. Every good `U`-train and good `V`-train crosses more than half of the same center family, so every good cross-leaf pair shares a center neighbor. Triangle-freeness makes that complete cross-product noncrossing. The inherited cross-phase endpoint theorem therefore gives an energy cost at least `a` per unit common good-pair weight.

Order the leaf occurrence masses so

\[
z_U\le z_V.
\]

### 6.1 No forced pair: `z_U<=S`

Then use only the phasewise bathtub:

\[
E\ge f(z_C)+f(z_U)+f(z_V).
\]

Because `f` is increasing, a minimum under `z_C+z_U+z_V>=Z` lies on total mass `Z`. For fixed `z_U`, convexity equalizes the other two masses. Hence

\[
E\ge f(z_U)+2f((Z-z_U)/2).
\]

Since `S<Z/3`, the derivative

\[
f'(z_U)-f'((Z-z_U)/2)
\]

is negative for `0<=z_U<=S`. Thus the no-pair branch is minimized at `z_U=S`, which is exactly the value `E(0)` below.

### 6.2 Forced common pair: `z_U=S+g`

Suppose `g>0`. Equation (PR.19) gives at least `gD-o(D)` good pair weight in each leaf. Trim both good families to common weight `gD`.

The paired terminal submeasure uses occurrence mass `2gD` in each leaf. After removing it, the smaller-leaf remainder has mass

\[
z_U-2g=S-g.
\tag{PR.20}
\]

If the larger-leaf remainder is `r_V`, then ordering `z_V>=z_U` gives

\[
r_V\ge S-g.
\tag{PR.21}
\]

The paired terminal energy is at least

\[
agD-o(D).
\]

The two remainders are still submeasures of the retained phase occurrence measures, so each obeys the same one-well density cap and costs `f(remainder)`.

If

\[
0\le g\le G_{max}:=Z-3S=0.285626,
\tag{PR.22}
\]

then, after lowering total charged mass to `Z`, the center mass and the larger-leaf remainder have total at least

\[
Z-S-3g.
\]

Convexity equalizes them at

\[
R(g):={Z-S-3g\over2}.
\]

The condition `g<=G_max` is exactly the condition

\[
R(g)\ge S-g,
\]

so this equalization respects (PR.21). Therefore every configuration in this range pays at least

\[
\boxed{
\mathcal E(g)
=2f\left({Z-S-3g\over2}\right)
+f(S-g)+ag.
}
\tag{PR.23}
\]

The case `g=0` agrees with the no-pair minimum.

### 6.3 Larger pair weight: `g>=G_max`

For larger `g`, do not force the total charged mass down to `Z`. The center contribution is nonnegative and both leaf remainders have mass at least `S-g`. Hence

\[
E\ge \mathcal H(g):=2f(S-g)+ag.
\tag{PR.24}
\]

On the physically relevant range `G_max<=g<=S`,

\[
\mathcal H'(g)=a-2f'(S-g).
\]

The derivative is minimized at `g=G_max`. The exact certificate gives

\[
\mathcal H'(G_{max})>0.23,
\]

and

\[
\mathcal H(G_{max})-\delta_{max}>0.029.
\tag{PR.25}
\]

Thus the large-pair branch is very far from the endpoint. The only close case is (PR.23).

---

## 7. Exact minimization of the one-variable energy

For

\[
0\le g\le G_{max},
\]

write

\[
R(g)={Z-S-3g\over2},
\qquad
Q(g)=S-g.
\]

Then

\[
\mathcal E'(g)
=a-3f'(R(g))-f'(Q(g)),
\tag{PR.26}
\]

and

\[
\mathcal E''(g)
={9\over4}\sin(R(g)/2)
+{1\over2}\sin(Q(g)/2).
\tag{PR.27}
\]

Both `R(g)` and `Q(g)` decrease with `g`, so the minimum curvature occurs at `g=G_max`, where both remaining masses equal

\[
4S-Z=0.358244.
\]

The exact certificate obtains the uniform strong-convexity bound

\[
\boxed{\mathcal E''(g)>0.48.}
\tag{PR.28}
\]

Choose the rational test point

\[
g_0={31\over2500}=0.0124.
\]

Then

\[
R(g_0)=0.768083,
\qquad
Q(g_0)=0.63147.
\]

Outward Taylor enclosures for sine and cosine give

\[
|\mathcal E'(g_0)|<9\times10^{-6}.
\tag{PR.29}
\]

Strong convexity implies

\[
\min_g\mathcal E(g)
\ge
\mathcal E(g_0)
-{\mathcal E'(g_0)^2\over2(0.48)}.
\tag{PR.30}
\]

The exact rational/Taylor certificate evaluates the right side as

\[
>0.0512456120031,
\]

whereas (PR.6) gives

\[
\delta<0.0512410395463.
\]

Hence

\[
\boxed{
\min_g\mathcal E(g)-\delta_{max}
>4.57\times10^{-6}.
}
\tag{PR.31}

This contradicts the outer directional-energy budget.

---

## 8. Conclusion

Every full-core/no-macroscopic-container Type-II survivor with

\[
t={q-k\over D}\le1.844
\]

would satisfy the inherited residual, crossing, and retained-occurrence inequalities and therefore the phase-resolved lower bound above. Equation (PR.31) contradicts its total outer detour budget.

Thus

\[
\boxed{
\text{no full-core/no-container Type-II survivor exists with }t\le1.844.
}
\]

The improvement from `1.84370` to `1.844` uses no new geometric hypothesis. It uses only information already present in the paired-remainder proof but previously discarded by replacing the actual phase masses with one common floor.

**Disposition:** proof-only exclusion through the full numerical endpoint `1.844`; global C-II/Level-I status must be decided from the canonical branch ledger, not inferred from this note alone.
