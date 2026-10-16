# Target C-II — direct dominant/complement energy allocation

**Date:** 2026-09-15  
**Status:** proof-only low-`t` Type-II strengthening; theorem-state authority unchanged  
**Scope:** fully force-visible no-container/full-core Type-II branch  
**Dependencies:** hostile-audited `g=0.0050` atomic gap; dominant-orbit additive outer-energy theorem; complement outer-train bracing theorem; audited Section 157  
**LEVEL I STATUS:** `STILL OPEN`

The current complement-bracing theorem first upper-bounds the actual dominant-orbit
outer-terminal population through the joint capacity theorem and then lower-bounds the
complement population.  That loses information because the dominant and complement
retained edge sets are physically disjoint.

There is a simpler exact coupling.  If `K` is the actual dominant-orbit outer-terminal
mass, then hull-capacity trimming retains at least `K-delta` dominant occurrences,
while the complement argument retains at least `pi-K-N_*` outer-to-outer train pairs.
The unknown `K` cancels in the sum:

\[
\boxed{z+p\ge W:=\pi-\delta-N_*.}
\]

The dominant retained occurrences pay the additive angular energy

\[
F(z)=z-6\sin(z/6),
\]

and the complement retained pairs pay the disjoint two-sided-bracing energy

\[
J(p)=2p-6\sin(p/3).
\]

Therefore the whole outer detour must satisfy the infimal-convolution bound

\[
\boxed{\delta\ge \mathcal E(W)},
\qquad
\mathcal E(W):=\min_{z+p=W}\{F(z)+J(p)\}.
\]

This avoids the double counting that would result from adding the joint-capacity
function `Phi(K)` to the complement energy.  With the hostile-audited atomic gap
`g=0.0050`, the new scalar floor is

\[
\boxed{\liminf {q-k\over D}\ge1.83236.}
\]

The scalar zero of this argument is

\[
1.8323676277438298975\ldots,
\]

but only the safely rounded value `1.83236` is claimed.

---

## 1. Low-`t` variables and the stronger atomic input

Pass to a convergent Type-II subsequence and write

\[
t={q-k\over D},\qquad
\kappa={k\over D},\qquad
\delta={d_{out}\over D}.
\]

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_0=2\sqrt{\Delta_2}+0.0050.
\]

Let

\[
C={T-q/2\over D}.
\]

The hostile-audited iterative-pruning theorem gives

\[
C\ge C_0-o(1).
\]

The Section-171 envelope gives

\[
C\le U+o(1),
\qquad
U={9t\over2}-2\pi-2\delta-{\kappa\over2}.
\tag{DA.1}
\]

Hence

\[
\boxed{2\delta+{\kappa\over2}\le
R_{50}(t):={9t\over2}-2\pi-C_0.}
\tag{DA.2}
\]

---

## 2. Complement train count

Freeze shrinking phase windows around a dominant exact `pi/3` atomic orbit.  Let `M`
be its absolute complete-train mass per `D`, and let `N_c` be the complete-train mass
outside those windows.

The orbit/Mantel inequality gives

\[
M\ge {4\Delta_2\over C}.
\]

Since

\[
{T\over D}=C+{t+\kappa\over2},
\]

we obtain

\[
N_c\le C+{t+\kappa\over2}-{4\Delta_2\over C}.
\]

The right side is increasing in `C`, so (DA.1) yields

\[
\boxed{
N_c\le N_*:=
U+{t+\kappa\over2}-{4\Delta_2\over U}.
}
\tag{DA.3}

---

## 3. Retained dominant and complement populations

Let `K` be the normalized number of outer terminal occurrences carried by the
dominant-orbit windows.

### Dominant class

On loaded-hull route `i`, if `n_i` dominant occurrences are present, retain fractional
weight

\[
m_i=\min\{n_i,s_i\},
\]

where `s_i` is the loaded-hull side length.  Since

\[
(n_i-s_i)_+\le d_i=\ell_i-s_i,
\]

and `sum d_i=d_out`, the total retained dominant weight `z` obeys

\[
\boxed{z\ge K-\delta.}
\tag{DA.4}

The retained edge occurrences are dominated by the round loaded-hull perimeter
measure.  The dominant-orbit bathtub theorem therefore gives the **additive edge-energy**
payment

\[
\boxed{E_{dom}\ge F(z),
\qquad F(z)=z-6\sin(z/6).}
\tag{DA.5}

### Complement class

The total outer occurrence density is

\[
{b\over D}=\pi+\delta+o(1).
\]

Thus complement trains carry outer-terminal occurrence mass

\[
\pi+\delta-K+o(1).
\]

A complement train with fewer than two outer terminals contributes at most one such
occurrence.  Hence the number `P_c` of complement outer-to-outer trains satisfies

\[
P_c\ge \pi+\delta-K-N_c-o(1).
\]

Apply the endpoint-capacity trimming from the complement-bracing theorem.  At most
`delta+o(1)` pair mass is lost, so the retained complement pair mass `p` satisfies

\[
\boxed{p\ge \pi-K-N_c-o(1)
\ge \pi-K-N_*-o(1).}
\tag{DA.6}

The three-sector noncrossing/bracing theorem gives the additive terminal-edge payment

\[
\boxed{E_{comp}\ge J(p),
\qquad J(p)=2p-6\sin(p/3)}
\tag{DA.7}

on the present range `p<1`.

The edge occurrences used in (DA.5) belong to dominant-orbit trains.  The terminal
edges used in (DA.7) belong to trains outside the frozen dominant windows.  Therefore
the two selected edge sets are disjoint and their directional-energy payments add.

---

## 4. The unknown dominant-terminal count cancels

Equations (DA.4) and (DA.6) imply

\[
\begin{aligned}
z+p
&\ge (K-\delta)+(\pi-K-N_*)-o(1)\\
&=\pi-\delta-N_*-o(1).
\end{aligned}
\]

If either displayed individual lower bound is negative, replace it by zero.  Since
`max(a,0)+max(b,0)>=a+b`, the same summed inequality remains valid.  Define

\[
\boxed{
W(t,\delta,\kappa)
:=\pi-\delta-U-{t+\kappa\over2}+{4\Delta_2\over U}.
}
\tag{DA.8}

Then

\[
\boxed{z+p\ge W-o(1).}
\tag{DA.9}

Both `F` and `J` are nonnegative, increasing, and convex on the relevant intervals.
Thus the least possible disjoint additive energy for total retained mass `W` is

\[
\boxed{
\mathcal E(W)
:=\min_{\substack{z,p\ge0\\z+p=W}}
\left[F(z)+J(p)\right].
}
\tag{DA.10}

Consequently every survivor satisfies

\[
\boxed{
\delta\ge \mathcal E(W(t,\delta,\kappa)).
}
\tag{DA.11}

This is the main new inequality.

It is important that (DA.11) uses the additive dominant energy `F`, not the joint
capacity function `Phi`.  Adding `Phi` to `J` would be invalid because the derivation
of `Phi` already spends total route detour through the capacity constraint
`d_i>=n_i-s_i`.

---

## 5. Exact optimizer of the allocation

For `0<W<pi`, the minimizing split is interior in the present range.  Write

\[
p=W-z.
\]

Strict convexity gives the unique Euler equation

\[
\boxed{
F'(z)=J'(p),
}
\tag{DA.12}

that is,

\[
\boxed{
1-\cos(z/6)=2-2\cos(p/3).
}
\tag{DA.13}

The envelope derivative is the common marginal cost

\[
\boxed{
\mathcal E'(W)=
1-\cos(z/6)=2-2\cos(p/3).
}
\tag{DA.14}

This makes the outer feasible-region optimization elementary.

---

## 6. The feasible triangle again collapses to one endpoint

For fixed `t,delta`, differentiate (DA.8) with respect to `kappa`.  Since

\[
{\partial U\over\partial\kappa}=-{1\over2},
\]

we get

\[
\boxed{
{\partial W\over\partial\kappa}
={2\Delta_2\over U^2}>0.
}
\tag{DA.15}

Because `mathcal E` is increasing, the contradiction margin

\[
\mathcal H(t,\delta,\kappa)
:=\mathcal E(W(t,\delta,\kappa))-\delta
\]

is minimized at

\[
\kappa=0.
\]

For fixed `t,kappa`,

\[
\boxed{
{\partial W\over\partial\delta}
=1+{8\Delta_2\over U^2}
\le1+{8\Delta_2\over C_0^2}
=2.9895404540\ldots .
}
\tag{DA.16}

On `0<=W<=pi`,

\[
\mathcal E'(W)
\le F'(W)
\le F'(\pi)
=1-\frac{\sqrt3}{2}.
\]

Therefore

\[
\frac{\partial\mathcal H}{\partial\delta}
\le
\left(1-\frac{\sqrt3}{2}\right)
\left(1+{8\Delta_2\over C_0^2}\right)-1
< -0.5994.
\tag{DA.17}

So `mathcal H` decreases strictly with `delta`.  Under (DA.2), its weakest feasible
point is therefore

\[
\boxed{
\kappa=0,
\qquad
\delta={R_{50}(t)\over2},
\qquad
U=C_0.
}
\tag{DA.18}

At this endpoint put

\[
\delta_0(t)={R_{50}(t)\over2},
\]

\[
\boxed{
W_0(t)
=\pi-\delta_0(t)-C_0-{t\over2}+{4\Delta_2\over C_0}
=2\pi-{11t\over4}-{C_0\over2}+{4\Delta_2\over C_0}.
}
\tag{DA.19}

A survivor requires

\[
\boxed{
H_0(t):=\mathcal E(W_0(t))-\delta_0(t)\le0.
}
\tag{DA.20}

Since `W_0'(t)=-11/4`, `delta_0'(t)=9/4`, and `mathcal E'>=0`,

\[
H_0'(t)<0.
\tag{DA.21}

Thus there is at most one crossing.

---

## 7. Certified new floor

The Decimal certificate

`research/verify_target_c_direct_dominant_complement_energy_allocation.py`

solves (DA.13) by monotone bisection and evaluates (DA.20) at 80-digit precision.  It
finds

\[
H_0(1.83236)>1.7\times10^{-5}>0,
\]

while

\[
H_0(1.83237)<-5\times10^{-6}<0.
\]

The unique scalar root is bracketed at

\[
\boxed{
1.8323676277438298975\ldots .
}
\tag{DA.22}

Hence all Type-II survivors in the stated scope satisfy

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge1.83236.
}
\tag{DA.23}

This supersedes the `g=0.0050` joint-orbit floor `1.82515` and the earlier separate
complement-bracing floor.

At the scalar crossing, the minimizing allocation is approximately

\[
z=1.61787,
\qquad
p=0.57113,
\]

so both energy mechanisms are genuinely active; the improvement is not obtained by
throwing either population away.

---

## 8. Remaining obstruction

The new theorem exhausts the scalar information in the **total retained dominant plus
complement outer-terminal mass**.  It still does not use where the retained dominant
and complement edges sit relative to one another around the boundary, nor does it use
which actual diameter edges provide the two-sided bracing of the complement trains.

The next useful step should therefore be structural rather than another independent
worst-case scalar estimate.  Two live options are:

1. couple the cyclic order of complement outer-to-outer train endpoints to the Woodall
   diameter-thrackle order forced by Section 157; or
2. exploit the hostile-audited rhombic slack `sigma_R/D>=0.0100` to force enough
   exceptional-face endpoint demand that the complement outer-to-outer population
   cannot realize the minimizing allocation in (DA.22).

No exact equilateral triangle or same-cardinality strict sub-`D` competitor is claimed.
C-II remains open.
