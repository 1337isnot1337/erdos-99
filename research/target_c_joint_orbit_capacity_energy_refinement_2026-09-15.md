<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b12f10adf2c9751e6da294116161520a586d18c1", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_joint_orbit_capacity_energy_refinement_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "20601056d78ec99dfb3c38aed60869a8af18de91508ee727a3889860139b27eb"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — joint orbit-capacity / phase-energy refinement

**Date:** 2026-09-15  
**Repository base:** after the dominant-orbit outer-energy theorem  
**Status:** proof-only low-`t` Type-II strengthening; theorem-state authority unchanged  
**Scope:** same full-core/no-container Type-II scope as `target_c_dominant_orbit_outer_energy_2026-09-15.md`  
**LEVEL I STATUS:** `STILL OPEN`

The first dominant-orbit outer-energy theorem deliberately separated two exact facts on
one outer route:

1. orbit-window occurrences have an angular mismatch cost relative to the loaded-hull
   chord; and
2. the number of outer occurrences can exceed the Euclidean hull-side length only by
   spending route detour.

It then discarded up to `d_out` occurrence mass before applying the angular cost.
That is safe but not sharp.  The same route detour pays both constraints
**simultaneously**, so the correct local relaxation is the maximum of the two costs,
not their sequential subtraction.

Solving that convex relaxation exactly replaces

\[
F(z)=z-6\sin(z/6)
\]

by the stronger joint cost

\[
\boxed{
\Phi(z)
=z-6\arcsin(\tanh(z/6)).
}
\]

At the current scalar endpoint this raises the safe proof-only floor from `1.82428`
to

\[
\boxed{
\liminf {q-k\over D}\ge1.82434.
}
\]

The numerical root of the joint relaxation is about `1.824348869...`; only the round
value `1.82434` is claimed.

---

## 1. Inputs retained from the first orbit-energy theorem

Use the same normalized Type-II variables

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
\]

and

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_0=2\sqrt{\Delta_2}+0.00042,
\]

\[
U={9t\over2}-2\pi-2\delta-{\kappa\over2}.
\]

AG42 and the §171 envelope give

\[
C_0\le C={T-q/2\over D}\le U,
\tag{JC.1}
\]

so

\[
2\delta+{\kappa\over2}\le
R(t):={9t\over2}-2\pi-C_0.
\tag{JC.2}
\]

The audited §142/168 orbit argument and the exposed-hull inequality give one dominant
`pi/3` atomic orbit whose normalized outer terminal-occurrence count satisfies

\[
\boxed{
K\ge K_*:=
\pi+\delta-t-\kappa-2U+{8\Delta_2\over U}.
}
\tag{JC.3}

The only change below is how `K_*` is converted to a lower bound on `delta`.

---

## 2. One route has two simultaneous lower bounds on detour

Fix one distinguished loaded-hull route `W_i`.  Write

\[
s_i=|b_i-b_{i+1}|,
\qquad
\ell_i=|W_i|,
\qquad
d_i=\ell_i-s_i.
\]

Let `n_i` be the number of outer edge occurrences on `W_i` whose train phase lies in
shrinking windows about the dominant orbit.  Let

\[
g_i=1-\cos d_i^{\rm ph},
\]

where `d_i^{ph}` is the projective angular distance from the loaded-hull side direction
to the limiting three-point orbit.  For a fixed window radius `rho`, replace `g_i` by
the slightly smaller continuous value obtained from `(d_i^{ph}-rho)_+`; the
`rho->0` limit is understood below.

Every selected orbit occurrence contributes at least `g_i` to the exact directional
energy on this route.  Hence

\[
\boxed{d_i\ge n_i g_i-o_\rho(\ell_i).}
\tag{JC.4}
\]

Independently, `n_i<=ell_i=s_i+d_i`, so

\[
\boxed{d_i\ge n_i-s_i.}
\tag{JC.5}
\]

Thus, after the phase-window limit,

\[
\boxed{
d_i\ge
\max\{n_i g_i,\ n_i-s_i,\ 0\}.
}
\tag{JC.6}

This is stronger than first discarding `(n_i-s_i)_+` occurrences and then charging
angular energy to what remains.

---

## 3. Exact convex dual inequality

For `s>0`, put `r=n/s` and

\[
c_g(r):=\max\{gr,r-1,0\}.
\]

Then (JC.6) is `d>=s c_g(r)`.

For every `lambda in[0,1]`, the convex conjugate calculation gives

\[
\boxed{
c_g(r)
\ge
\lambda r-
{(\lambda-g)_+\over1-g}.
}
\tag{JC.7}

Indeed, for `0<=g<1`, the two positive linear pieces meet at

\[
r_*={1\over1-g}.
\]

For `lambda<g` the supremum of `lambda r-c_g(r)` is zero at `r=0`; for
`g<=lambda<=1` it occurs at `r_*` and equals

\[
{\lambda-g\over1-g}.
\]

Applying (JC.7) route by route, summing, dividing by `D`, and using the near-disk
perimeter-measure convergence from audited §142 yields

\[
\boxed{
\delta
\ge
\lambda K-
\int_{\mathbb R/\pi\mathbb Z}
{(\lambda-g(\theta))_+\over1-g(\theta)}\,d\theta,
}
\tag{JC.8}

where

\[
g(\theta)=1-\cos d_{\mathbb{RP}^1}(\theta,O)
\]

for the dominant three-point orbit `O`.

This dual form automatically retains any singular occurrence mass above hull-side
length capacity: the recession slope of `c_g` is one.

---

## 4. Evaluate the three-orbit dual exactly

Write

\[
\lambda=1-\cos a,
\qquad 0\le a\le\pi/6.
\]

The integrand in (JC.8) is nonzero exactly on the six half-arcs of radius `a` about
the three orbit directions.  On one half-arc at distance `u`,

\[
{\lambda-g(u)\over1-g(u)}
={\cos u-\cos a\over\cos u}
=1-\cos a\sec u.
\]

Therefore

\[
\int{(\lambda-g)_+\over1-g}\,d\theta
=6\left[a-\cos a\,L(a)\right],
\tag{JC.9}
\]

where

\[
L(a):=\int_0^a\sec u\,du
=\log(\sec a+\tan a).
\]

The right side of (JC.8) is consequently

\[
(1-\cos a)K-6a+6\cos a L(a).
\tag{JC.10}
\]

Its derivative with respect to `a` is

\[
\sin a\,[K-6L(a)].
\]

As long as

\[
K<6L(\pi/6)=3\log3,
\]

there is a unique interior maximizer determined by

\[
\boxed{K=6L(a).}
\tag{JC.11}

At that maximizer (JC.10) collapses to

\[
K-6a.
\]

The identity

\[
L(a)=\operatorname{artanh}(\sin a)
\]

gives

\[
\sin a=\tanh(K/6).
\]

Hence define

\[
\boxed{
\Phi(K)
:=K-6\arcsin(\tanh(K/6)).
}
\tag{JC.12}

The exact joint route relaxation gives the necessary condition

\[
\boxed{
\delta\ge\Phi(K_*).
}
\tag{JC.13}

For the low-`t` range here `K_*<1.4<3log3`, so the interior formula is valid with
large slack.

---

## 5. `Phi` is increasing and has a simple derivative

Let

\[
a(K)=\arcsin(\tanh(K/6)).
\]

Since

\[
\cos a=\operatorname{sech}(K/6),
\]

differentiation gives

\[
a'(K)={1\over6}\operatorname{sech}(K/6).
\]

Therefore

\[
\boxed{
\Phi'(K)=1-\operatorname{sech}(K/6)>0
}
\tag{JC.14}

for `K>0`.

---

## 6. The two-parameter feasible region again collapses to the detour endpoint

Define

\[
K_*(t,\delta,\kappa)
=
\pi+\delta-t-\kappa-2U+{8\Delta_2\over U}.
\]

At fixed `t,delta`,

\[
{\partial K_*\over\partial\kappa}
={4\Delta_2\over U^2}>0,
\tag{JC.15}
\]

so `Phi(K_*)-delta` is minimized at `kappa=0`.

At fixed `t,kappa`,

\[
{\partial K_*\over\partial\delta}
=5+{16\Delta_2\over U^2}<9
\tag{JC.16}
\]

because `U>=C0>2sqrt(Delta2)`.

Throughout the interval from the old `t42` floor through the new safe endpoint,
`K_*<1.33`.  Thus

\[
\Phi'(K_*)
=1-\operatorname{sech}(K_*/6)
<0.025.
\]

Hence

\[
{\partial\over\partial\delta}
[\Phi(K_*)-\delta]
<9(0.025)-1<0.
\tag{JC.17}

So the contradiction margin decreases with `delta`.  The worst feasible point is again

\[
\boxed{
\kappa=0,
\qquad
\delta={R(t)\over2},
\qquad
U=C_0.
}
\tag{JC.18}

At this point

\[
K_0(t)
=
\pi+{R(t)\over2}-t-2C_0+{8\Delta_2\over C_0}.
\tag{JC.19}

The one-variable contradiction margin is

\[
\boxed{
H_J(t)
:=\Phi(K_0(t))-{R(t)\over2}.
}
\tag{JC.20}

Since

\[
K_0'(t)={5\over4},
\]

\[
H_J'(t)
={5\over4}\Phi'(K_0(t))-{9\over4}<0
\]

throughout the relevant range.

---

## 7. Safe new floor

The independent high-precision certificate gives

\[
\boxed{
H_J(1.82434)
=1.9690280\times10^{-5}>0.
}
\tag{JC.21}

The scalar zero is

\[
1.824348869\ldots .
\tag{JC.22}

Therefore no convergent full-core Type-II survivor subsequence can have

\[
t\le1.82434.
\]

### Theorem JC.1 — joint orbit-capacity/energy floor

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge1.82434.
}
\tag{JC.23}

This supersedes the weaker `1.82428` numerical conclusion of the first
orbit-energy note, while leaving that note's simpler measure argument valid.

---

## 8. What this refinement exhausts

The local inequalities

\[
d_i\ge n_i g_i,
\qquad
d_i\ge n_i-s_i
\]

are now optimized jointly and exactly at the continuum level.  Further improvement of
this route cannot come from a better way of algebraically combining those two
inequalities.  It needs genuinely new information, for example:

- restrictions on how two outer terminal occurrences of one non-atomic train can be
  paired around the near-round hull;
- train-crossing topology for the almost-antipodal two-outer trains near exposed-hull
  equality;
- integer/rounded loaded-side information beyond the perimeter measure; or
- a source-level use of the signed penetration/reflection geometry.

The exposed-hull equality regime is especially rigid: at the worst point `C=C0`, the
AG42 atomic floor and `A<=C` force equality of the atomic scalar, while almost every
remaining train must spend both terminal incidences on the outer face.  That is the
next structural target.

## 9. Reproducibility

Run

```bash
python3 research/verify_target_c_joint_orbit_capacity_energy.py
```

for the high-precision one-variable endpoint and derivative checks.
