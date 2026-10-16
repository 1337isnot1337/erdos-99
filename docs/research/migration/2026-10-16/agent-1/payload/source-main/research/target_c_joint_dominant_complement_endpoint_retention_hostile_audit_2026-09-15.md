# Hostile audit — joint dominant/complement endpoint retention

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_joint_dominant_complement_endpoint_retention_2026-09-15.md`
- `research/verify_target_c_joint_dominant_complement_endpoint_retention.py`

**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate strengthens the hostile-audited direct dominant/complement energy
tradeoff by replacing two independent outer-capacity truncations with one truncation of
their disjoint union. It claims

\[
\boxed{\liminf(q-k)/D\ge1.83279.}
\]

The numerical gain is modest. The potentially dangerous point is structural: pair
retention is not the same currency as endpoint retention, so one must check that a
single discarded endpoint budget really controls both the dominant occurrence loss and
the complement **pair** loss.

---

## 1. The selected occurrence families are disjoint on every route

The dominant family consists of outer edge occurrences whose complete stopped trains
lie in the frozen dominant atomic-orbit windows. The complement family consists of the
two terminal outer occurrences of complete trains outside those windows that have two
outer terminals.

Every outer edge occurrence belongs to exactly one complete stopped train. Therefore
the two selected occurrence sets are disjoint, including bridge occurrences. A bridge
may appear twice on the outer facial walk, but both appearances belong to the same
train class and remain distinct occurrence-capacity slots.

Consequently, on each Section-63 route `W_i`, the union count is at most the full route
occurrence length `ell_i`.

**Verdict:** PASS.

---

## 2. One routewise truncation loses at most `d_out`

Write

\[
\ell_i=s_i+d_i,
\qquad d_i\ge0.
\]

Give the union of selected occurrences on route `i` total retained fractional weight
at most `s_i`. If the selected count is `c_i`, the required discard is

\[
(c_i-s_i)_+\le(\ell_i-s_i)=d_i.
\]

Summing over routes gives total discarded selected endpoint/occurrence weight at most

\[
\sum_i d_i=d_{out}.
\]

This is a purely finite occurrence-level statement. It does not use an energy estimate
and therefore does not spend `d_out` as directional-energy currency a second time.

**Verdict:** PASS.

---

## 3. Complement pair loss is bounded by complement endpoint loss

For one complement outer-to-outer train let the retained weights of its two terminal
occurrences be `a,b in[0,1]`. Retain the train pair with weight

\[
w=\min(a,b).
\]

Then

\[
1-w\le(1-a)+(1-b).
\]

Thus the loss in total pair mass is at most the loss in total complement endpoint
weight. If `x` is discarded dominant weight and `y` discarded complement endpoint
weight, the single truncation gives

\[
x+y\le\delta.
\]

With dominant outer count `K` and raw complement two-outer train count `P_c`, the
retained masses satisfy

\[
z\ge K-x,
\qquad
p\ge P_c-y.
\]

The parent theorem gives

\[
P_c\ge\pi+\delta-K-N_*.
\]

Therefore

\[
\begin{aligned}
z+p
&\ge K+P_c-(x+y)\\
&\ge K+\pi+\delta-K-N_*-\delta\\
&=\pi-N_*.
\end{aligned}
\]

The cancellation of `K` and `delta` is exact. No assumption about how the routewise
discard is split between the two populations is needed.

**Verdict:** PASS.

---

## 4. Joint truncation preserves both measure dominations

The total retained selected weight on route `i` is at most `s_i`. Hence the retained
dominant submeasure alone is bounded by the loaded-hull side-length measure. The
projective three-orbit bathtub theorem therefore still yields

\[
E_{dom}\ge F(z).
\]

Likewise each of the two complement-pair endpoint measures is bounded by the retained
complement endpoint measure, which is itself bounded by the same side-length measure.
The physical oriented-perimeter domination used in the complement-bracing theorem
therefore remains valid and yields

\[
E_{comp}\ge J(p)
\]

in the smooth `p<=1` regime.

The two edge-occurrence supports are disjoint by Section 1, so these actual weighted
edge-energy sums add. Joint retention has not created an overlap that was absent in the
parent theorem.

**Verdict:** PASS.

---

## 5. Infimal convolution is a legitimate relaxation

The actual retained masses obey

\[
z,p\ge0,
\qquad z+p\ge S:=\pi-N_*.
\]

Both `F` and `J` are increasing on the positive range. Therefore

\[
F(z)+J(p)
\ge
\min_{z'+p'=S}[F(z')+J(p')]
=:H(S).
\]

The minimizing split need not correspond to the actual `K`; this only weakens the
lower bound, so no feasibility condition on the optimizer is required.

On the relevant range the objective is strictly convex because

\[
F''(z)={1\over6}\sin(z/6)>0,
\qquad
J''(p)={2\over3}\sin(p/3)>0.
\]

The unique interior optimizer satisfies

\[
F'(z)=J'(p).
\]

**Verdict:** PASS.

---

## 6. The complement smooth regime is safe

The current direct-tradeoff audit already gives `N_*>0.9225` on the interval in
question, so

\[
S=\pi-N_*<2.22.
\]

At `p=0.72`, one has `z=S-p<1.50`. The exact verifier gives

\[
J'(0.72)=0.05732405\ldots,
\]

while `F'(1.50)` is strictly smaller. Hence the derivative of
`F(S-p)+J(p)` is positive by `p=0.72`, so the minimizer satisfies

\[
p<0.72<1.
\]

At `p=0` the derivative is negative because `F'(S)>0`; therefore the minimizer is
strictly interior.

If an actual retained complement mass were at least one, truncating it to unit mass
would already give

\[
J(1)=0.0368318\ldots,
\]

larger than the full detour `delta<0.028` on the candidate interval. Such a source is
already contradictory. Thus no missing `p>1` branch can weaken the result.

**Verdict:** PASS.

---

## 7. Feasible-triangle reduction

With

\[
S=\pi-N_*,
\qquad
N_*=U+(t+\kappa)/2-4\Delta_2/U,
\]

the exact derivatives are

\[
{\partial S\over\partial\kappa}
={2\Delta_2\over U^2}>0,
\]

and

\[
{\partial S\over\partial\delta}
=2\left(1+{4\Delta_2\over U^2}\right)<4.
\]

At the unique split optimizer the envelope theorem gives

\[
H'(S)=F'(z)=J'(p)>0.
\]

Therefore the contradiction margin `H(S)-delta` increases with `kappa`; the weakest
point has `kappa=0`.

Also `p<0.72`, so

\[
H'(S)<J'(0.72)<0.058.
\]

Hence

\[
{\partial\over\partial\delta}[H(S)-\delta]
<4(0.058)-1<0.
\]

The weakest point has maximal detour, namely

\[
\delta=R(t)/2,
\qquad U=C_0.
\]

No incompatible extrema are combined.

**Verdict:** PASS.

---

## 8. Boundary monotonicity and exact certificate

At the worst corner,

\[
N_0(t)=C_0+t/2-4\Delta_2/C_0,
\qquad
S_0(t)=\pi-N_0(t),
\]

so

\[
S_0'(t)=-1/2.
\]

Also

\[
\delta_0'(t)=9/4.
\]

Thus the boundary margin

\[
G_0(t)=H(S_0(t))-\delta_0(t)
\]

has

\[
G_0'(t)
=-{1\over2}H'(S_0)-{9\over4}<0.
\]

The Decimal certificate gives at `t=1.83279`

\[
\begin{aligned}
\delta_0&=0.0273720395462494\ldots,\\
S_0&=2.2152107451611569\ldots,\\
z_0&=1.6372546931568777\ldots,\\
p_0&=0.5779560520042792\ldots,
\end{aligned}
\]

\[
F(z_0)=0.0202431425559765\ldots,
\qquad
J(p_0)=0.00713698378252219\ldots,
\]

and

\[
\boxed{
G_0(1.83279)
=0.00000808679224929794\ldots>0.
}
\]

The same verifier brackets the scalar crossing by

\[
\boxed{
1.83279356481905<t_*<1.83279356481906.
}
\]

An independent Pyroam Decimal run reproduced the endpoint values, equal marginal
costs, and both root signs.

**Verdict:** PASS.

---

## 9. Final disposition

The joint-retention theorem is valid at the same proof-only full-core Type-II scope as
its parents. It removes a real duplicated capacity loss and proves

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.83279.
}

It does not prove C-II or produce a same-cardinality strict sub-`D` competitor. The
remaining explicit loss is the complement bracing function `J(p)`, which uses only a
three-sector noncrossing partition and ignores the actual complement phase measure and
its crossing relations with the dominant orbit.

**Final verdict:** PASS. C-II and Level I remain open.
