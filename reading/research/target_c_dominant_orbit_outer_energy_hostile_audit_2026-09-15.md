> Generated reading edition · [exact source](../../research/target_c_dominant_orbit_outer_energy_hostile_audit_2026-09-15.md) · source SHA-256 `ce83aae44cf6a3625b88b5608e5f25fe22baafd521ec1669df6a10ac900d5a09`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "7312e492bc908445f7ece8b8bc79458ab311e8a7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_dominant_orbit_outer_energy_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "89d58634f2fff2bc84940a1ce7bec4322e57d7240637328a3764e853ca4d2dc1"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — dominant atomic orbit / outer directional-energy exclusion

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_dominant_orbit_outer_energy_2026-09-15.md`
- `research/verify_target_c_dominant_orbit_outer_energy.py`

**Disposition:** **PASS at proof-only low-`t` Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate raises the current proof-only floor for

```math
t=(q-k)/D
```

from `t42=1.8208886379...` to the safe explicit value `1.82428` by coupling the
atomic train-phase orbit structure to the uniformly rotating perimeter measure of the
near-disk loaded force hull.

The audit below targets the places where a false proof would most naturally enter:
normalization of atomic mass, occurrence multiplicity on the outer walk, replacement
of edge directions by projective train phase, domination by the perimeter measure,
the bathtub optimization, and the two-parameter scalar minimization.

---

## 1. The absolute atomic mass is bounded by the same scalar `C`

Audited §142 uses

```math
x=T/D,
\qquad y=q/T,
```

and proves

```math
y\le2(1-\sigma),
```

where `sigma` is total atomic mass of the probability train-phase measure.  Hence

```math
x\sigma\le x(1-y/2)
={T-q/2\over D}=C.
```

Thus the candidate's `A=x sigma<=C` is exactly the audited exposed-hull inequality in
absolute-mass units.  No new semicontinuity claim is inserted.

**Verdict:** PASS.

---

## 2. The dominant orbit lower bound has the correct normalization

For the exact `pi/3` atomic orbits, audited §168 supplies

```math
E_r\le M_r^2/4,
\qquad
\sum_rE_r=\Delta_2,
\qquad
\sum_rM_r=A.
```

If `M=max M_r`, then

```math
4\Delta_2
\le\sum_rM_r^2
\le M\sum_rM_r=MA.
```

Therefore

```math
M\ge4\Delta_2/A\ge4\Delta_2/C.
```

The factor is `4 Delta2`, not `2 sqrt(Delta2)`: `M` is absolute train population in
one orbit, while the latter is the total atomic-Mantel floor.  The units are
consistent.

**Verdict:** PASS.

---

## 3. A train can consume at most two outer occurrences

The stopped-train auxiliary graph is a forest of paths.  Every complete train has two
terminal face incidences, with singleton trains included by the same endpoint
convention.  The exact identity

```math
2T=b+Q+4f
```

is precisely the count of these terminal incidences.

Hence a train outside the frozen dominant-orbit phase windows can account for at most
two occurrences in the outer-walk term `b`.  Bridge multiplicity does not break this:
a singleton bridge may contribute its two outer incidences, but that still saturates,
rather than exceeds, the factor two.

Thus if `(M-o(1))D` complete trains lie in the dominant-orbit windows,

```math
K_D\ge b-2(T-MD)-o(D)
```

is valid.

**Verdict:** PASS.

---

## 4. Freezing phase windows does not assume atomic-mass semicontinuity

Choose one limiting train-phase measure first.  The dominant orbit consists of at most
three atoms.  Around those atoms choose disjoint open windows whose boundaries carry
zero limiting mass.  Weak convergence then gives the finite-source train population
inside the windows with an `o(D)` error.

Only after this choice are finite sources taken.  The window radius is sent to zero
last.  This is the same order-of-limits discipline as audited §§164/168.

**Verdict:** PASS.

---

## 5. The route-capacity subtraction is exact even with real side lengths

On loaded-hull interval `i`, let

```math
n_i=\text{dominant-window outer occurrences},
\qquad
s_i=|b_i-b_{i+1}|,
\qquad
\ell_i=|W_i|.
```

Then `n_i<=ell_i`.  Define the real retained mass

```math
m_i=\min(n_i,s_i).
```

Although `s_i` need not be integral, fractional retention is legitimate because the
argument is an inequality on nonnegative edge energies: distribute total weight
`m_i` among the `n_i` selected occurrences with each individual weight at most one.

Moreover

```math
n_i-m_i=(n_i-s_i)_+
\le(\ell_i-s_i)=d_i.
```

After summing,

```math
\sum_i m_i\ge K_D-d_{out}.
```

No integer rounding term is omitted.

**Verdict:** PASS.

---

## 6. The retained measure really is dominated by hull perimeter measure

Place mass `m_i/D` at the projective direction `theta_i` of hull side `i`.  Since
`m_i<=s_i`, the resulting measure satisfies pointwise

```math
\nu_D\le
\mu_D:={1\over D}\sum_i s_i\delta_{\theta_i}.
```

The Type-II near-disk argument already used in audited §142 gives

```math
\mu_D\Rightarrow d\theta
```

on the projective direction circle, with total mass `pi`.  If
`nu_D=>nu` along a subsequence, then for every nonnegative continuous test function
`phi`,

```math
\int\phi\,d\nu
\le\int\phi\,d\theta.
```

Hence `nu<=dtheta` as measures.  Its total mass is at least `K-delta` by the preceding
section.

This is the key domination step; it uses side **length**, not side count.  That is
necessary because the limiting circular perimeter measure is length-weighted.

**Verdict:** PASS.

---

## 7. Projectivizing edge directions can only weaken the energy lower bound

For an oriented route edge `v` and chord unit vector `u`, its exact contribution to
outer detour is

```math
1-u\cdot v.
```

If `d` is the projective angular distance between their directions, then

```math
|u\cdot v|=\cos d,
```

and therefore

```math
1-u\cdot v
\ge1-|u\cdot v|
=1-\cos d.
```

So an edge pointing backward along its route does not evade the estimate; it pays
more energy.  If its train phase lies within projective distance `rho` of the dominant
orbit `O`, the triangle inequality gives the candidate's continuous lower integrand

```math
1-\cos(d(\theta,O)-\rho)_+.
```

Sending `rho->0` yields

```math
\delta\ge\int[1-\cos d(\theta,O)]\,d\nu.
```

**Verdict:** PASS.

---

## 8. The three-orbit bathtub formula is exact

On `R/pi Z`, the full orbit `O` has three equally spaced points.  The Voronoi radius is
`pi/6`.  For `0<=a<=pi/6`, the union of the three radius-`a` neighborhoods has length
`6a`.

For a submeasure `0<=nu<=dtheta` of mass `z`, the minimum of the integral of the
nonnegative increasing distance cost is obtained by filling the lowest-cost directions
first.  With `a=z/6`,

```math
\begin{aligned}
F(z)
&=3\cdot2\int_0^a(1-\cos u)\,du\\
&=z-6\sin(z/6).
\end{aligned}
```

This remains a valid lower bound if fewer than all three orbit atoms have positive
mass, because allowing all three orbit directions can only lower the cost.

**Verdict:** PASS.

---

## 9. The `delta` cancellation is not double counting

The dominant-orbit occurrence count is

```math
K\ge
\pi+\delta-t-\kappa-2C+8\Delta_2/C.
```

The route-capacity reduction retains mass at least `K-delta`.  These two occurrences
of `delta` come from different exact facts:

- `+delta` appears because the outer walk has `b/D=pi+delta` occurrences;
- `-delta` is the maximum amount of those occurrences that can exceed the physical
  hull-side length capacity, since `sum(ell_i-s_i)=delta D`.

Their cancellation is therefore exact, not reuse of one budget with the wrong sign.

**Verdict:** PASS.

---

## 10. Replacing `C` by its upper envelope has the correct direction

Set

```math
g(C)=-2C+{8\Delta_2\over C}.
```

Then

```math
g'(C)=-2-{8\Delta_2\over C^2}<0.
```

Since `C<=U`,

```math
g(C)\ge g(U).
```

Thus replacing `C` by `U` weakens the lower bound on dominant-orbit outer mass and is
safe.

**Verdict:** PASS.

---

## 11. The two-variable minimization is at `kappa=0, delta=R/2`

Put

```math
k=\pi-t-\kappa-2U+{8\Delta_2\over U},
\qquad
U={9t\over2}-2\pi-2\delta-\kappa/2.
```

For fixed `t,delta`,

```math
{\partial k\over\partial\kappa}
={4\Delta_2\over U^2}>0.
```

Since `F` is increasing, the contradiction margin `F(k)-delta` is smallest at
`kappa=0`.

For fixed `t,kappa`,

```math
{\partial k\over\partial\delta}
=4+{16\Delta_2\over U^2}<8
```

because `U>=C0>2sqrt(Delta2)`.

A minor implicit point in the candidate is that `k` is positive throughout the only
interval being excluded.  Its minimum there occurs at `delta=kappa=0` and the largest
`t`, namely `t=1.82428`; direct substitution gives

```math
k>1.23.
```

Also

```math
k<\pi-t\le\pi-t_{42}=1.320705\ldots .
```

Hence

```math
F'(k)=1-\cos(k/6)<0.024129.
```

The independent Decimal certificate gives

```math
\left(4+{16\Delta_2\over C_0^2}\right)
[1-\cos((\pi-t_{42})/6)]
<0.193<1.
```

Therefore

```math
{\partial\over\partial\delta}[F(k)-\delta]<0.
```

The margin is minimized by taking the largest allowed `delta`.  With `kappa=0`,
`U>=C0` is exactly

```math
\delta\le R(t)/2.
```

Thus the global minimum is indeed

```math
\kappa=0,
\qquad
\delta=R(t)/2,
\qquad
U=C_0.
```

**Verdict:** PASS.  The positivity detail above should be regarded as an explicit
completion of the terse sentence in the candidate, not a change to the argument.

---

## 12. Scalar certificate

At the weakest feasible point define

```math
k_0(t)=\pi-t-2C_0+8\Delta_2/C_0,
```

```math
H_0(t)=k_0(t)-6\sin(k_0(t)/6)-R(t)/2.
```

Then

```math
H_0'(t)=-[1-\cos(k_0(t)/6)]-9/4<0.
```

The committed high-precision Taylor certificate gives

```math
H_0(1.82428)
=2.808709054\times10^{-6}>0,
```

and brackets the zero by

```math
1.82428123517075213
<t_*
<1.82428123517075215.
```

A separate Pyroam execution reproduced the signs at `1.82428`, `1.8242812`, and
`1.8242813`.

**Verdict:** PASS.

---

## 13. Regression checks

### Long one-rhombus-thick strip

This is the binding regression for the preceding penetration theorem.  It does not
break the present result: even if one strip absorbs many inward contacts, its train
phase remains in a fixed projective direction while the loaded-hull tangent direction
rotates.  The mismatch is charged by outer directional energy before penetration
occupancy is considered.

### Backtracking outer route

A backward-oriented contact occurrence has larger `1-u dot v` than the projective
lower cost, so backtracking only helps the contradiction.

### Extra occurrence multiplicity

A route may have `ell_i>s_i`; exactly that excess is paid by `d_i=ell_i-s_i`.  The
measure construction discards at most `sum d_i=d_out` units of occurrence mass before
invoking round-hull measure domination.  No simplicity assumption is needed here.

### Non-dominant continuous phase mass

It is counted among trains outside the dominant orbit and can absorb at most two outer
occurrences per complete train.  The proof never assumes all train mass is atomic.

**Verdict:** PASS.

---

## 14. Final disposition

The new implication is valid at the stated proof-only scope:

```text
AG42 + audited train-phase orbit decomposition
  -> one pi/3 orbit has mass M >= 4 Delta2/C
  -> it must carry many outer terminal occurrences
  -> only delta D of those occurrences can exceed hull length capacity
  -> the remaining occurrence mass is dominated by round-hull perimeter measure
  -> three fixed projective directions incur F(z)=z-6 sin(z/6) energy
  -> old low-t network detour budget fails
  -> liminf (q-k)/D >= 1.82428.
```

This is a genuine new branch exclusion, but it does not close C-II.  The natural next
step is to re-optimize the pentagon/train/penetration ledgers at the new floor and see
whether their joint populations force a second independent detour or phase-energy
payment.

**Final verdict:** PASS at proof-only low-`t` Type-II scope. C-II and Level I remain
open.
