# Target C-II — corrected `g=0.0076` endpoint controls residual exact-orbit mass

**Date:** 2026-09-15  
**Status:** proof-only structural stability lemma  
**Scope:** canonical full-core Type-II train-measure branch  
**Dependencies:** hostile-audited corrected `g=0.0076` one-orbit capacity theorem; generic two-bin dominant-orbit bound  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_{76}:=2\sqrt{\Delta_2}+0.0076.
\]

Let `M` be the mass of a dominant exact projective `pi/3` orbit and let `U` be any upper bound for the total exact atomic train mass.  On the full interval

\[
\boxed{C_{76}\le U\le2.013,}
\]

every feasible atomic crossing measure satisfies

\[
\boxed{
0\le U-M\le1.05\,(U-C_{76}).
}
\tag{RS76.1}

This is the `g=0.0076` version of the earlier phase-star residual-stability lemma, but its wider `U` range is large enough to cover the complete feasible triangle used by the current low-`t` scalar optimization.  No preliminary localization bootstrap is needed.

---

## 1. Full physical one-orbit capacity

Let `Psi(W)` be the maximum possible strict-rhombus crossing mass in one exact three-phase orbit of total mass `W`, using the scope-corrected physical capacity theorem:

1. on the strong center/leaf branch, use the `1/10` iterative-pruning deficit;
2. on the in-scope fallback branch, use the universal `2/29` deficit;
3. for center mass above `K=2/sqrt(3)`, use only the generic triangle-free capacity `C(W-C)`.

The hostile-audited corrected `g=0.0076` theorem proves

\[
\boxed{\Psi(C_{76})<\Delta_2.}
\tag{RS76.2}

The same branch derivatives used in that theorem also give a uniform lower slope for `Psi` just below `C76`.

---

## 2. Generic residual and dominant-mass interval

The ordinary two-bin bound gives

\[
M\ge m_2(U):=
{U+\sqrt{8\Delta_2-U^2}\over2}.
\tag{RS76.3}

On the interval `U>=C76>2sqrt(Delta2)`, the residual

\[
r_2(U):=U-m_2(U)
\]

is increasing.  At `U=2.013`, the exact companion certificate gives

\[
\boxed{
r_2(2.013)<0.112.}
\tag{RS76.4}

Hence every feasible pair `(U,M)` in the stated range has

\[
M>1.9013,
\qquad
R:=U-M<0.112.
\tag{RS76.5}

---

## 3. Uniform slope of the full physical capacity

For `W` in the only interval relevant when `M<C76`, namely

\[
1.9013<W<C_{76},
\]

the three possible capacity branches all increase with derivative greater than `0.60`.

### Strong branch

At the unique strong-branch optimizer `C_*(W) in (W/3,W/2)`, the envelope derivative is

\[
\Psi_1'(W)=\partial_W\Phi_{1/10}(W,C_*(W)).
\]

The corrected capacity proof gives

\[
\partial_W\Phi_{1/10}
\ge C_*-{1\over10}qr,
\]

with `C_*>=W/3`, `q<=1`, and

\[
r\le{3C_{76}\over4}-{2\over\sqrt3}.
\]

Therefore

\[
\Psi_1'(W)
\ge {1.9013\over3}
-{1\over10}\left({3C_{76}\over4}-{2\over\sqrt3}\right)
>0.60.
\tag{RS76.6}

### In-scope fallback branch

At the moving strong/fallback boundary `C_s(W)`, the derivative contribution from `C_s'(W)` is positive because both `C_s'(W)` and the fallback `Phi_C` are negative.  Thus

\[
B_0'(W)
\ge \partial_W\Phi_{2/29}(W,C_s(W)).
\]

The coarse bounds from the corrected capacity proof yield

\[
B_0'(W)
\ge {1.9013\over2}
-{4\over29}\left(C_{76}-{2\over\sqrt3}\right)
>0.84>0.60.
\tag{RS76.7}

### High-center branch

The generic high-center capacity is

\[
B_H(W)=K(W-K),
\]

so

\[
B_H'(W)=K>1.15>0.60.
\tag{RS76.8}

Since `Psi` is the maximum of these branch capacities and each branch minus `0.60W` is increasing,

\[
\boxed{
\Psi(C_{76})-\Psi(W)
\ge0.60(C_{76}-W)
}
\tag{RS76.9}

for every `W in[1.9013,C76]`.

---

## 4. Residual mass is proportional to endpoint slack

The exact orbit crossing decomposition and generic square capacity of all non-dominant exact orbits give

\[
\Delta_2
\le \Psi(M)+{(A-M)^2\over4}
\le \Psi(M)+{(U-M)^2\over4}.
\tag{RS76.10}

Put

\[
h:=U-C_{76}\ge0,
\qquad
R:=U-M.
\]

If `M>=C76`, then immediately

\[
R\le h.
\]

Suppose `M<C76`.  Equations (RS76.2), (RS76.9), and (RS76.10) imply

\[
0.60(C_{76}-M)
< {R^2\over4}.
\]

Since

\[
C_{76}-M=R-h,
\]

\[
R-h<{R^2\over2.4}.
\tag{RS76.11}

By (RS76.4)--(RS76.5), `R<0.112`, hence

\[
R-h
<{0.112\over2.4}R.
\]

Therefore

\[
R
< {h\over1-0.112/2.4}
<1.05h.
\]

This proves (RS76.1).

---

## 5. Consequences for shared retention and rhombus incidence

The two quantities that matter in the current low-`t` stack now depend on the same endpoint slack `h=U-C76`.

The complement complete-train density obeys

\[
N_c
\le U+{t+\kappa\over2}-M
\le {t+\kappa\over2}+1.05h.
\]

Hence joint endpoint retention gives

\[
\boxed{
z+p
\ge
\pi-{t+\kappa\over2}-1.05h-o(1).}
\tag{RS76.12}

Likewise the exact atomic mass outside the dominant orbit is at most `R<=1.05h`, so the complement-rhombus incidence budget improves to

\[
\boxed{
{1\over2}(1.05h)^2.}
\tag{RS76.13}

At `h=0` both complement allowances vanish simultaneously.  This is the key correlation: the generic two-bin residual `r_2(C76)≈0.007615` is not an independent budget at the matched endpoint.

The next theorem propagates (RS76.12)--(RS76.13) through the restored-energy scalar optimization.

**Disposition:** proved proof-only endpoint stability lemma; C-II and Level I remain open.
