# Hostile audit — direct dominant/complement outer-energy tradeoff

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_direct_dominant_complement_energy_tradeoff_2026-09-15.md`
- `research/verify_target_c_direct_dominant_complement_energy_tradeoff.py`

**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate replaces the previous two-stage dominant/complement argument by one
optimization over the **actual** dominant-window outer-terminal count `K`.  It uses the
hostile-audited atomic gap `g=0.0050` and claims the safe floor

\[
\boxed{\liminf(q-k)/D\ge1.83236.}
\]

The audit focuses on coupling errors: whether the same dominant-orbit estimate is used
in incompatible ways, whether occurrence capacity is double-spent, whether dominant
and complement edge energies overlap, and whether the scalar minimum really lies in
the smooth interior claimed by the proof.

---

## 1. The two dominant-orbit inequalities are simultaneously valid

Let `C=(T-q/2)/D`, let `M` be absolute train mass in a dominant exact `pi/3` atomic
orbit, and let `K` be its outer terminal occurrence density after frozen phase windows.
Audited §§142/168 give

\[
M\ge4\Delta_2/C.
\]

Thus

\[
K\ge
\pi+\delta-t-\kappa-2C+8\Delta_2/C
\]

and the number of complement trains satisfies

\[
N_c\le
C+(t+\kappa)/2-4\Delta_2/C.
\]

Both inequalities hold for the **same actual** `C` and `M`.  Replacing `C` by the
common upper bound `U` is conservative in both places because

\[
-2C+8\Delta_2/C
\]

is decreasing, while

\[
C-4\Delta_2/C
\]

is increasing.  Hence the simultaneous pair

\[
K\ge K_L(U),
\qquad
N_c\le N_*(U)
\]

is valid; it does not combine two incompatible extremizers.

**Verdict:** PASS.

---

## 2. The dominant `F(K-delta)` term is an actual edge-energy sum

On route `i`, if `n_i` dominant-window terminal occurrences are present, retain total
fractional occurrence weight

\[
m_i=\min(n_i,s_i),
\]

where `s_i` is physical loaded-hull side length.  Since `n_i<=ell_i`,

\[
n_i-m_i\le ell_i-s_i=d_i.
\]

Total retained mass is therefore at least `K-delta`.  The retained measure is dominated
by the projective loaded-hull perimeter measure, which tends Lebesgue by Type-II
near-disk geometry.  Every retained dominant-window occurrence contributes its own
route directional energy.  The three-orbit bathtub minimum gives

\[
E_{dom}\ge F(K-\delta),
\qquad
F(z)=z-6\sin(z/6).
\]

This is the simpler additive edge-energy theorem, not the joint `Phi` route relaxation.
That distinction is essential because the complement energy will be added to it.

**Verdict:** PASS.

---

## 3. Complement pair mass is exactly the remaining outer allocation

The total outer terminal occurrence density is `pi+delta`.  After assigning `K` of it
to the dominant windows, complement trains carry `pi+delta-K` occurrences.

If `N_c` complement trains exist and `P_c` of them have two outer terminals, then

\[
\pi+\delta-K\le N_c+P_c.
\]

Therefore

\[
P_c\ge\pi+\delta-K-N_*.
\]

The hostile-audited pair-retention lemma loses at most `delta` total pair weight when
both endpoint measures are truncated to hull-side length capacity.  Hence

\[
p\ge\pi-K-N_*.
\]

The cancellation of `delta` is legitimate: the positive `delta` came from **extra
outer occurrence length**, while the negative `delta` is the maximum excess of those
occurrences over physical side-length capacity.  No energy payment has yet been made
with that scalar.

**Verdict:** PASS.

---

## 4. Dominant and complement energy supports are disjoint

Every outer contact-edge occurrence belongs to exactly one complete stopped train.
The dominant `F` term uses only occurrences whose trains lie in the frozen dominant
orbit windows.  The complement `J` term uses terminal occurrences of trains outside
those windows.

Thus no outer edge occurrence is included in both selected energy sums.  A physical
bridge traversed twice remains one train and cannot belong to both populations.
Fractional retention changes weights but not this support disjointness.

Consequently

\[
\delta\ge E_{dom}+E_{comp}
\]

is valid.

**Verdict:** PASS.

---

## 5. The `J(p)` formula is used only where valid

The complement bracing theorem proves

\[
J(p)=2p-6\sin(p/3)
\]

for retained pair mass `0<=p<=1`.  The direct optimization eventually lies near
`p=0.571`, but the proof must still control the other regimes.

Across the whole candidate interval,

\[
\delta<0.0265.
\]

If `p>=1`, retain only unit pair mass.  Then

\[
E_{comp}\ge J(1)=0.0368318\ldots>0.0265>\delta,
\]

so such a source is already impossible.

If `p<=0`, then `K>=pi-N_*`.  The uniform bound `N_*<1.083` gives

\[
K-\delta
>\pi-1.083-0.0265
>2.032,
\]

and therefore

\[
F(K-\delta)>0.0386>\delta.
\]

So the only potentially minimizing regime is indeed

\[
0<p<1.
\]

**Verdict:** PASS.

---

## 6. The lower constraint `K>=K_L` is inactive

The proof claims a unique unconstrained minimizer in `(1.5,1.7)`.  This must be checked
uniformly over the feasible `(t,delta,kappa)` region.

The network constraint and `g=0.0050` give

\[
1.82515\le t\le1.83236,
\qquad
2\delta+\kappa/2\le R(t).
\]

The companion certificate proves

\[
0.9225<N_*<1.083,
\qquad
\delta<0.0265.
\]

For

\[
K_L=\pi+\delta-t-\kappa-2U+8\Delta_2/U,
\]

both partial derivatives with respect to `delta,kappa` are positive.  Therefore its
maximum occurs on the network boundary.  On that boundary `U=C0` and
`kappa=2R-4delta`, so

\[
{dK_L\over d\delta}=5>0.
\]

Thus maximum `K_L` occurs at `kappa=0,delta=R/2`; that boundary value increases with
`t` at rate `5/4`.  At `t=1.83236`,

\[
K_L=1.3156633762\ldots<1.32<1.5.
\]

Hence any minimizer in `(1.5,1.7)` automatically satisfies the actual dominant-count
lower bound.

**Verdict:** PASS.

---

## 7. The split minimum is uniquely interior

In the smooth regime define

\[
H(K)=F(K-\delta)+J(\pi-K-N_*).
\]

Then

\[
H''(K)
={1\over6}\sin((K-\delta)/6)
+{2\over3}\sin((\pi-K-N_*)/3)>0.
\]

So `H` is strictly convex.

Using the uniform `N_*` and `delta` bounds, the verifier obtains

\[
H'(1.5)<-0.003,
\qquad
H'(1.7)>0.008.
\]

Thus the unique global minimizer of the potentially feasible regime lies in
`(1.5,1.7)`.  There

\[
0<\pi-K-N_*<0.72<1,
\]

so the smooth `J` formula is valid and the preceding `p<=0`/`p>=1` branches cannot
compete.

**Verdict:** PASS.

---

## 8. The feasible triangle is minimized at `kappa=0`, maximal detour

Let

\[
G(t,\delta,\kappa)=\min_K H(K)-\delta.
\]

The unique interior optimizer permits direct use of the envelope theorem.

For

\[
N_*=U+(t+\kappa)/2-4\Delta_2/U,
\]

one has

\[
\partial_\kappa N_*=-2\Delta_2/U^2<0.
\]

Thus

\[
\partial_\kappa G
={2\Delta_2\over U^2}J'(p)>0,
\]

so the weakest point has `kappa=0`.

Also

\[
\partial_\delta N_*
=-2(1+4\Delta_2/U^2).
\]

Hence

\[
\partial_\delta G
=-F'(z)
+2(1+4\Delta_2/U^2)J'(p)-1.
\]

Because `C0>2sqrt(Delta2)`, the coefficient of `J'` is strictly below four.  At the
split minimizer `p<0.72`, and the certificate gives `J'(0.72)<0.058`.  Therefore

\[
\partial_\delta G
<4(0.058)-1<0.
\]

So the weakest point is maximal detour.  With `kappa=0`, this is exactly

\[
\delta=R(t)/2,
\qquad U=C0.
\]

**Verdict:** PASS.

---

## 9. One-variable endpoint and numerical certificate

At the boundary point define

\[
\delta_0=R(t)/2,
\qquad
N_0=C0+t/2-4\Delta_2/C0.
\]

The unique split optimizer solves

\[
F'(K_0-\delta_0)=J'(\pi-K_0-N_0).
\]

The boundary margin

\[
G_0(t)
=F(K_0-\delta_0)+J(\pi-K_0-N_0)-\delta_0
\]

has envelope derivative

\[
G_0'(t)
=-{9\over4}F'(K_0-\delta_0)
-{1\over2}J'(\pi-K_0-N_0)
-{9\over4}<0.
\]

At the advertised safe endpoint `t=1.83236`, the exact Decimal/Taylor certificate
gives

\[
\begin{aligned}
\delta_0&=0.0264045395462494\ldots,\\
K_0&=1.6442871060685511\ldots,\\
p_0&=0.5711386390926057\ldots,\\
F&=0.0195347667658293\ldots,\\
J&=0.0068876931759361\ldots,
\end{aligned}
\]

and

\[
G_0(1.83236)
=1.792039551596\times10^{-5}>0.
\]

It brackets the numerical zero by

\[
1.832367627743829897
<t_*<
1.832367627743829898.
\]

An independent Pyroam double-precision regression reproduced positive signs at
`1.83236` and `1.8323676277`, and a negative sign at `1.8323676278`.

**Verdict:** PASS.

---

## 10. Scope and final disposition

The theorem is proof-only because it uses the proof-only hostile-audited
`g=0.0050` atomic gap and proof-only complement train bracing stack.  It does not
change canonical theorem-state authority, produce an exact equilateral triangle, or
construct a same-cardinality strict sub-`D` source.

The new conclusion is valid:

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.83236.
}

This is a genuine structural composition rather than a free scalar improvement: both
the dominant atomic outer-terminal population and the diameter-braced complement
outer-to-outer population are simultaneously macroscopic at the minimizing endpoint.

**Final disposition:** **PASS at proof-only full-core Type-II scope. C-II and Level I remain open.**
