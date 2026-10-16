# Target C-II — residual-free flat teeth carry linear hidden-distance derivative rank

**Date:** 2026-09-15  
**Repository base:** branch `research/c2-orbit-routing-sol-20260915`  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** full-core Type-II survivor subsequence with `1.82516 < t=(q-k)/D <= 1.82570`  
**LEVEL I STATUS:** `STILL OPEN`

The orbit-purity/flat-tooth theorems on this branch remove the old true-face-residual hypothesis from the flat pentagon endpoint.  In the narrow band

\[
1.82516<t\le1.82570,
\]

they force at least

\[
\boxed{0.4374431D-o(D)}
\]

flat orbit-pure pentagons.  Their hidden near-unit diagonals are not first-order redundant with ordinary contact-face closure: after **all** bounded-face closure equations are imposed, at least

\[
\boxed{0.00108D-o(D)}
\]

independent hidden radial derivatives remain.

The scalar rank becomes zero only near

\[
1.8257050149\ldots,
\]

so `1.82570` is a safe round endpoint.

## 1. Local four-row rank at the flat tooth

Label one flat-tooth pentagon cyclically

\[
l,m,r,a,b
\]

and orient its unit side vectors

\[
e_1=lm,\ e_2=mr,\ e_3=ra,\ e_4=ab,\ e_5=bl.
\]

At the limiting flat trapezoid take

\[
e_1=e_2=(1,0),
\]

\[
e_3=(-1/2,\sqrt3/2),
\quad e_4=(-1,0),
\quad e_5=(-1/2,-\sqrt3/2).
\]

Let `omega_i` be the angular rate of the complete stopped train containing side `e_i`.  After an invertible quarter-turn, differentiated face closure gives the two rows

\[
C_x=(1,1,-1/2,-1,-1/2),
\]

\[
C_y=(0,0,c,0,-c),
\qquad c=\sqrt3/2.
\]

The hidden diagonals `ma=e_2+e_3` and `mb=-e_1-e_5` have first radial derivatives

\[
\dot d_{ma}=c(\omega_2-\omega_3),
\]

\[
\dot d_{mb}=c(\omega_5-\omega_1).
\]

Thus their derivative rows are

\[
H_a=(0,c,-c,0,0),
\qquad
H_b=(-c,0,0,0,c).
\]

The `4 x 4` minor of `(C_x,C_y,H_a,H_b)` on columns `1,2,3,4` has determinant

\[
\boxed{c^3={3\sqrt3\over8}>0.}
\tag{HR.1}
\]

Hence the four rows have rank four.  Their common kernel is exactly the all-ones line, corresponding to rigid rotation.

By continuity, after fixing one sufficiently small flat-tooth neighborhood, the same minor stays nonzero for every retained finite pentagon.

## 2. Five distinct train variables per pentagon

Every side of a bounded exceptional face is a terminal occurrence of one complete stopped train.

Current-main Section 128 excludes a nontrivial train whose two terminal sides lie on the same bounded face, including the singleton-loop convention.  Therefore the five sides of one pentagon belong to five distinct trains.

Current-main bounded-face endpoint simplicity excludes two distinct trains joining the same pair of bounded exceptional faces.  Hence for any family `P` of retained pentagons the internal face-to-face train graph is simple.

## 3. Rank on one pentagon component

Take one connected component of the pentagon/train incidence network containing `s` pentagons.  Let `e` be the number of trains joining two pentagons inside the component.

Each face contributes five terminal train incidences; an internal train is counted twice.  Thus the number `n` of distinct train variables appearing in the component is

\[
\boxed{n=5s-e.}
\tag{HR.2}

Impose, on every pentagon, its two closure rows and two hidden-diagonal derivative rows.  The local calculation above forces all five incident train rates of one pentagon to be equal.  Connectivity propagates that equality through every shared train.  Therefore the common kernel on this component is exactly one-dimensional and the stacked rank is

\[
\boxed{n-1=5s-e-1.}
\tag{HR.3}

The internal face graph is simple and has degree at most five, so

\[
e\le\min\left\{{s\choose2},\left\lfloor{5s\over2}\right\rfloor\right\}.
\]

For `s=1,...,5` direct substitution gives rank lower bounds `4,8,11,13,14`; for `s>=6`,

\[
5s-e-1\ge{5s\over2}-1\ge{7s\over3}.
\]

Hence every component, and therefore every pentagon family `P`, satisfies

\[
\boxed{
\operatorname{rank}
\begin{bmatrix}C_P\\H_P\end{bmatrix}
\ge {7|P|\over3}.
}
\tag{HR.4}

## 4. Remove all ordinary face-closure equations

Let `C_face` be the full stopped-train closure matrix over every bounded nonquadrilateral face.  Current-main Section 156 gives

\[
\operatorname{rank}C_{face}=2f-\sigma_C,
\qquad 0\le\sigma_C\le s_Z.
\tag{HR.5}

For two maps with common domain,

\[
\operatorname{rank}(H|_{\ker C})
=
\operatorname{rank}
\begin{bmatrix}C\\H\end{bmatrix}
-\operatorname{rank}C.
\]

Adding the closure rows from faces outside `P` cannot decrease stacked rank.  Therefore

\[
\boxed{
\operatorname{rank}(H_P|_{\ker C_{face}})
\ge {7|P|\over3}-2f+\sigma_C.
}
\tag{HR.6}

Under the standard train-angle/contact-flex isomorphism, this is the rank of the hidden pair-distance derivatives on actual contact-preserving infinitesimal source motions modulo translations.

## 5. Insert the residual-free orbit-pure population

Let `p=|P|/D` for the orbit-pure flat-tooth family.  The bounded-endpoint purity theorem gives, at the maximal-detour endpoint,

\[
p(t)
\ge
\pi+C_0-{5t\over2}
-
\left[\Psi(R(t)/2)-K_0(t)\right],
\tag{HR.7}
\]

where

\[
C_0=2\sqrt{\Delta_2}+0.0050,
\qquad
R(t)={9t\over2}-2\pi-C_0,
\]

and `Psi=Phi^{-1}` for the exact joint orbit dual.

The bracketed nondominant bounded-terminal cap is strictly increasing in `t`; the pentagon term is strictly decreasing.  Thus `p(t)` is decreasing throughout the present interval.  The companion certificate gives

\[
\boxed{
p(1.82570)>0.43744312.
}
\tag{HR.8}

Every bounded nonquadrilateral face has degree at least five, so `f<=Q`.  The exact low-`t` identity is

\[
{Q\over D}=2t-\pi-\delta.
\]

Discard the nonnegative `delta` and `sigma_C` terms in (HR.6):

\[
{1\over D}\operatorname{rank}(H_P|_{\ker C_{face}})
\ge
{7p\over3}-4t+2\pi-o(1).
\tag{HR.9}

At `t=1.82570`, using (HR.8),

\[
\boxed{
{7p\over3}-4t+2\pi
>0.0010859.
}
\tag{HR.10}

The right side decreases with `t` on the certified interval.  Therefore:

### Theorem HR.1 — residual-free hidden-rank floor

Every survivor subsequence with

\[
1.82516<t\le1.82570
\]

has

\[
\boxed{
\operatorname{rank}(H_P|_{\ker C_{face}})
\ge0.00108D-o(D).
}
\tag{HR.11}

The scalar expression in (HR.9), with the exact purity cap, vanishes only near

\[
1.8257050149\ldots .
\]

## 6. What this does and does not close

This removes a major false escape: the linear hidden near-contact sea cannot be explained as first-order redundancy of ordinary contact-face closure.  Even with every bounded-face closure equation imposed, a linear block of independent hidden radial coordinates remains.

It does **not** give sign control, and it does not prove that a contact flex realizing those hidden derivatives is nonincreasing on all actual diameter rows.  Mixed rigidity can still lock the remaining contact-flex directions through the diameter graph.

The next closing question is therefore precise:

> Can the near-extremal Woodall diameter thrackle lock an `Omega(D)` block of independent hidden-pair derivatives arising from vertex-local flat teeth without either producing a unit activation or admitting a diameter-nonincreasing combination?

That is now a mixed contact/diameter problem, not a pentagon-shape or contact-closure problem.

**Disposition:** proof-only structural strengthening. C-II and Level I remain open.
