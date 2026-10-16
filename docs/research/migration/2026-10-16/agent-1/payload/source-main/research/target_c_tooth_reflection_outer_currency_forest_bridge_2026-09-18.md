# Target C-II — block separators pay the canonical outer currency or force a common lower obstruction

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; proof-only bridge from the fixed-pair FREE forest obstruction to the canonical outer-pocket currency  
**Scope:** the `PAIR-REUSE` branch for the two extreme all-inactive FREE modules  
**Dependencies:** fixed-pair lossless common runs; all-run forest-union identity; block-aware boundary/forest theorem; two-normal directional defect; two-sided outer-face localization; OP outer-pocket Oler absorption; common-trunk two-normal cone theorem  
**Certificate:** `research/verify_target_c_tooth_reflection_outer_currency_forest_bridge_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The block-aware fixed-pair theorem has one residual branch which is not yet expressed in canonical source currency: many maximal upper blocks. That theorem converted those blocks into a near-diameter matching. The truncation-free outer-population theorem, however, already shows that upper gates themselves cost outer-face population. Combining the two facts removes the separate `BLOCK-UPPER` output entirely.

The resulting finite theorem has three outputs only:

1. excess in the canonical outer-pocket population/area currency;
2. bounded-face cycle rank in the union of the two lower-run forests; or
3. Euclidean drift on one common lower trunk.

No external-population hypothesis is used.

Fix a constant

\[
K>h_*:=\frac{\sqrt{303}}{52}.
\]

On the `PAIR-REUSE` side of the two extreme FREE modules, let `N_1,N_2` be their canonical support normals, let

\[
\theta:=\angle(N_1,N_2)\in(0,\pi),
\]

and let `E_*` be the common set of distinct lower-gate edges. Put

\[
E:=|E_*|.
\]

The fixed-pair theorem gives

\[
E\ge\left(\frac{\alpha_K}{2}-o(1)\right)D,
\qquad
\alpha_K:=1-\frac{h_*}{K},
\tag{OB.1}
\]

and

\[
1<|e|\le1+\frac KD\qquad(e\in E_*),
\tag{OB.2}
\]

while the extreme-normal geometry gives

\[
c_*-o(1)\le\theta\le\frac\pi2+o(1),
\qquad
c_*=0.129220199818177\ldots .
\tag{OB.3}
\]

For ancestry `i`, let

- `L_i` be its number of lower gates;
- `U_i` its number of upper gates;
- `A_i` its net support-depth traverse;
- `S_i` its terminal activation time; and
- `B_i` its number of maximal nonempty upper-gate blocks.

Put

\[
B:=B_1+B_2.
\tag{OB.4}
\]

Thus

\[
B\le U_1+U_2.
\tag{OB.5}
\]

## 1. An exact angle-adaptive common-edge defect floor

For one common edge, the two-normal directional-defect calculation gives, according to whether the two ancestries traverse it in the same or opposite direction,

\[
\epsilon_1(e)+\epsilon_2(e)
\ge
2-2\left(1+\frac KD\right)\cos\frac\theta2,
\tag{OB.6}
\]

or

\[
\epsilon_1(e)+\epsilon_2(e)
\ge
2-2\left(1+\frac KD\right)\sin\frac\theta2.
\tag{OB.7}
\]

Since every directional defect is itself nonnegative, define the finite common floor

\[
\boxed{
 d_D(\theta,K)
 :=
 \max\left\{
 0,
 2-2\left(1+\frac KD\right)
 \max\left(\cos\frac\theta2,\sin\frac\theta2\right)
 \right\}.
}
\tag{OB.8}
\]

Then every edge of `E_*`, independently of its traversal orientation, satisfies

\[
\boxed{
\epsilon_1(e)+\epsilon_2(e)\ge d_D(\theta,K).
}
\tag{OB.9}
\]

The exact two-boundary support identity gives

\[
L_i
=A_i-S_i+
\sum_{e\in E_{{\rm low},i}}\epsilon_i(e)
+B_i^{\rm back},
\qquad B_i^{\rm back}\ge0.
\tag{OB.10}
\]

Summing over the two ancestries, discarding all noncommon lower defects and both nonnegative backtracking sums, and using (OB.9),

\[
\boxed{
L_1+L_2
\ge
A_1+A_2-S_1-S_2+d_D(\theta,K)E.
}
\tag{OB.11}
\]

Unlike the uniform `delta_*` asymptotic, (OB.11) is finite and keeps the actual extreme-pair angle.

## 2. Upper blocks are paid by the canonical outer-pocket currency

Let

\[
\boxed{
\mathfrak O
:=
Z_{\rm ext}
+\frac{2}{\sqrt3}H_{\rm out}
-\frac{b-P_F}{2}.
}
\tag{OB.12}
\]

Here `Z_ext` is the source population outside the force hull, `H_out` is the total OP outer-pocket area inside the force hull, `b` is the old unit-contact outer-walk length, and `P_F=per(F)`.

Every vertex of each ancestry is an old fully inactive source point in the original outer contact face. The vertices along one ancestry are distinct. Hence, writing `Z_in` for the inactive outer-face population inside `F`,

\[
Z_{\rm in}+Z_{\rm ext}
\ge
\max_{i=1,2}(L_i+U_i+1)
\ge
\frac{L_1+L_2+U_1+U_2}{2}+1.
\tag{OB.13}
\]

The exact OP inequality is

\[
Z_{\rm in}\le\frac{2}{\sqrt3}H_{\rm out}-\frac{b-P_F}{2},
\tag{OB.14}
\]

so (OB.11)--(OB.14) imply

\[
\boxed{
\mathfrak O
\ge
\mathcal B_D+\frac{U_1+U_2}{2},
}
\tag{OB.15}
\]

where the exact reflection baseline is

\[
\boxed{
\mathcal B_D
:=
\frac{A_1+A_2-S_1-S_2}{2}
+\frac{d_D(\theta,K)}{2}E
+1.
}
\tag{OB.16}
\]

Define the outer residual

\[
\boxed{
\mathcal R_D:=\mathfrak O-\mathcal B_D.
}
\tag{OB.17}
\]

Then

\[
\boxed{
\mathcal R_D\ge\frac{U_1+U_2}{2}\ge\frac B2.
}
\tag{OB.18}
\]

This is the key conversion. A maximal upper block no longer needs to survive as a separate near-diameter matching alternative: every such separator is already charged to the same canonical outer-pocket population/area scalar used in Section 67.

## 3. The same upper-block count is the exact forest correction

Keep every maximal lower run from either ancestry which contains at least one edge of `E_*`, and let their unions be the path forests `\mathcal P,\mathcal Q`. Put

\[
H:=\mathcal P\cup\mathcal Q,
\qquad
I:=\mathcal P\cap\mathcal Q.
\]

Deleting `B_i` maximal upper blocks leaves at most `B_i+1` maximal lower runs. Thus, if `p,q` are the component counts of the retained path forests,

\[
p+q\le B+2.
\tag{OB.19}
\]

The exact two-forest Euler identity gives

\[
\beta(H)=c_H-p-q+c_I,
\]

where `c_H,c_I` are the component counts of `H,I`. Since `E>0`, `c_H>=1`, hence

\[
\boxed{
\beta(H)\ge c_I-B-1.
}
\tag{OB.20}
\]

All edges of `H` lie in the short-edge plane source graph, so `beta(H)` is exactly the number of bounded faces of `H`.

## 4. Every long intersection component has angle-adaptive two-normal drift

Put

\[
\boxed{
 b_D(\theta)
 :=
 \min\left(\sin\frac\theta2,\cos\frac\theta2\right).
}
\tag{OB.21}
\]

An edge-containing component of `I` is traversed either in the same direction throughout or in the opposite direction throughout. The two-normal cone theorem therefore gives, for the component endpoint displacement `X_C` and its appropriate normalized two-normal axis `V_C`,

\[
X_C\cdot V_C
>
|E(C)|\,b_D(\theta).
\tag{OB.22}
\]

Fix a real threshold `s>=1`. If some component contains at least `s` edges of `E_*`, then

\[
\boxed{
X_C\cdot V_C>b_D(\theta)s.
}
\tag{OB.23}
\]

Otherwise the `E` common edges occupy more than `E/s` distinct components of `I`, so (OB.20) gives

\[
\boxed{
\beta(H)+1>\frac Es-B.
}
\tag{OB.24}
\]

At the same time (OB.18) gives

\[
\mathcal R_D\ge\frac B2.
\tag{OB.25}
\]

For every `B>=0`,

\[
\boxed{
\max\left\{\frac Es-B,\frac B2\right\}
\ge\frac{E}{3s}.
}
\tag{OB.26}
\]

Thus, if no `s`-edge common trunk exists,

\[
\boxed{
\max\{\beta(H)+1,\mathcal R_D\}
>\frac{E}{3s}.
}
\tag{OB.27}
\]

Balance (OB.23) and (OB.27) by choosing

\[
 s=\sqrt{\frac{E}{3b_D(\theta)}}.
\tag{OB.28}
\]

For the asymptotic fixed-pair branch `E=Theta(D)`, this threshold is larger than one for all sufficiently large `D`. The result is the finite outer/forest/trunk bridge

\[
\boxed{
\max\left\{
\mathcal R_D,
\beta(H)+1,
\sup_C X_C\cdot V_C
\right\}
>
\sqrt{\frac{b_D(\theta)E}{3}}.
}
\tag{OB.29}
\]

The supremum is over edge-containing common components, with the appropriate bisector axis for SAME traversal and difference axis for OPPOSITE traversal.

Equation (OB.29) replaces the previous `BLOCK-UPPER` alternative by direct excess in the canonical outer currency.

## 5. Universal square-root consequence

The extreme-pair angle range (OB.3) implies

\[
b_D(\theta)\ge b_*-o(1),
\qquad
b_*:=\sin(c_*/2)
=0.0645651571904745\ldots .
\tag{OB.30}
\]

Using (OB.1), define

\[
\boxed{
C_K^{\rm out}:=
\sqrt{\frac{\alpha_Kb_*}{6}}.
}
\tag{OB.31}
\]

Then `PAIR-REUSE` forces at least one of

1. **OUTER-PAYMENT**
   \[
   \mathfrak O\ge\mathcal B_D+(C_K^{\rm out}-o(1))\sqrt D;
   \tag{OB.32}
   \]
2. **LOWER-FACE**
   \[
   \beta(H)\ge(C_K^{\rm out}-o(1))\sqrt D;
   \tag{OB.33}
   \]
3. **LOWER-TRUNK**: one common inactive lower component has actual two-normal endpoint drift at least
   \[
   (C_K^{\rm out}-o(1))\sqrt D.
   \tag{OB.34}
   \]

For `K=1`,

\[
\boxed{
C_1^{\rm out}=0.0846090036211229\ldots .
}
\tag{OB.35}
\]

For `K=400`,

\[
\boxed{
C_{400}^{\rm out}=0.103691147605043\ldots .
}
\tag{OB.36}
\]

Taking the fixed-`K` envelope after the asymptotic argument gives

\[
\boxed{
C_\infty^{\rm out}
=\sqrt{\frac{b_*}{6}}
=0.103734562859954\ldots .
}
\tag{OB.37}
\]

The reflection baseline itself has the first-order lower envelope

\[
\mathcal B_D\ge
\left(1+\frac{\delta_*\alpha_K}{4}-o(1)\right)D,
\qquad
\delta_*:=2(1-\cos(c_*/2)),
\tag{OB.38}
\]

but (OB.32) should be read against the exact finite baseline (OB.16), not as an unconditional `+C sqrt(D)` refinement of the coarser asymptotic expression (OB.38). The convergence error in (OB.38) is not known to be `o(sqrt(D))`.

## 6. Angle-sensitive frontier

The finite theorem retains more information than the universal constants. Ignoring the vanishing `K/D` term, define

\[
 d(\theta)
 =2-2\max\left(\cos\frac\theta2,\sin\frac\theta2\right),
\qquad
 b(\theta)
 =\min\left(\sin\frac\theta2,\cos\frac\theta2\right).
\tag{OB.39}
\]

Then the same extreme-pair angle simultaneously controls

- the linear common-edge contribution `d(theta)E/2` already absorbed into the exact outer baseline; and
- the square-root forest/trunk/outer-residual scale `sqrt(b(theta)E/3)`.

At the weakest permitted angle `theta=c_*`, these reduce to the constants above. As the extreme FREE normals separate farther, both quantities improve until `theta=pi/2`. At `theta=pi/2`,

\[
d(\pi/2)=2-\sqrt2,
\qquad
b(\pi/2)=\frac1{\sqrt2}.
\tag{OB.40}
\]

Thus the fixed-pair obstruction is now an angle-adaptive two-scale law rather than a separate forest-versus-upper-matching fork.

## 7. Frontier effect

Combining this theorem with the fixed-pair reuse dichotomy gives the proof-only normal form

```text
EXACT-BRAID
or
LINEAR-LOWER: Theta(D) inverse-D inactive matching
or, in PAIR-REUSE,
    OUTER-PAYMENT: canonical OP currency exceeds its exact reflection baseline
                   by Theta(sqrt(D));
    LOWER-FACE:    Theta(sqrt(D)) bounded faces in the common lower network; or
    LOWER-TRUNK:   Theta(sqrt(D)) actual two-normal common-trunk drift.
```

The previous `BLOCK-UPPER` branch has disappeared: its separator count is already paid by `mathfrak O`. This is the direct bridge that was missing between the block-aware FREE network and the canonical Section-67 outer-pocket currency.

C-II remains open. The remaining step is to upper-bound `mathfrak O-mathcal B_D` from the canonical force-hull/outer-walk ledger, or convert the square-root lower-face/lower-trunk alternatives into the same ledger or a strict diameter-decreasing source deformation. No theorem-state authority is changed.

**Disposition:** combined the exact two-boundary support identity, all-run forest Euler correction, upper-block count, and OP population absorption into one finite minimax. The same upper blocks which fragment the common lower forest now pay the canonical outer currency, eliminating the separate near-diameter `BLOCK-UPPER` obstruction.
