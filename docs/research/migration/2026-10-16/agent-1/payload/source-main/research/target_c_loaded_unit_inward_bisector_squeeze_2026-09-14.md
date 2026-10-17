# Target C-II — exact loaded-unit boundary to inward-contact squeeze

**Date:** 2026-09-14  
**Status:** proof-only structural theorem; theorem-state authority unchanged  
**Scope:** canonical full-core near-disk C-II branch; low-`t` constants use the proof-only minimax atomic gap `0.0021` / §171  
**LEVEL I STATUS:** `STILL OPEN`

The current boundary-atom theorem contains one remaining boundary-only currency,
`e_BB`, the number of exact unit contacts between consecutive loaded force-hull
vertices.  In fact every loaded vertex incident to such a side already forces one of
two source-level objects:

1. one unit of loaded contact-degree slack; or
2. a distinct loaded-to-unloaded unit contact pointing within less than `pi/6` of the
   inward hull-angle bisector.

This converts the whole `e_BB` population, not only endpoints of missing-side runs or
double-unit corners.

Let

\[
s_B:=\sum_{b\in B}(3-\deg_C b),
\]

and let `E_bis` be the set of selected strongly inward loaded-to-unloaded contacts
defined below.  Then

\[
\boxed{s_B+|E_{bis}|\ge e_{BB}.}
\tag{IB.1}
\]

Combining this with the exact boundary-atom theorem

\[
N_2+2e_{BB}\ge3q-b
\]

gives

\[
\boxed{
N_2+2s_B+2|E_{bis}|\ge3q-b.
}
\tag{IB.2}
\]

Thus at the current low-`t` floor at least one of actual two-edge outer teeth, loaded
degree slack, or strongly inward loaded-to-unloaded contacts has density about
`0.464D`.

The shallow-tooth theorem then converts the first currency as well, leaving a two-way
burden between loaded degree slack and an unweighted physical population of strongly
inward unit contacts.

## 1. Unit-side endpoints have degree two or three

Let `v` be a loaded force-hull vertex incident to at least one exact unit hull side.
The loaded degree cap gives

\[
\deg_C(v)\le3.
\tag{IB.3}
\]

The missing-hull-side equilibrium lemma gives the complementary lower bound: a unit
hull-side contact cannot be the only contact at a loaded vertex.  Hence

\[
\boxed{2\le\deg_C(v)\le3.}
\tag{IB.4}
\]

If `deg_C(v)=2`, then `v` contributes exactly one unit to `s_B`.

It remains to classify `deg_C(v)=3`.

## 2. Degree three forces a contact near the inward angle bisector

Let the convex hull interior angle at `v` be

\[
\theta_v\in(0,\pi),
\]

and let `n_v` be the inward unit angle-bisector direction.

All contact rays from `v` lie in the closed hull tangent cone of angle `theta_v`.
Because `v` is incident to a unit hull side, one of its three contact rays is one
boundary ray of that cone.  Reflect the picture if necessary and measure contact-ray
angles from that boundary ray.  Write the three contact directions in increasing
order as

\[
0,\quad \alpha,\quad \beta,
\qquad 0<\alpha<\beta\le\theta_v.
\tag{IB.5}
\]

Triangle-freeness and unit separation say that any two consecutive contact neighbors
on the unit circle around `v` have angular separation strictly greater than `pi/3`.
Therefore

\[
\alpha>{\pi\over3},
\qquad
\beta-\alpha>{\pi\over3}.
\tag{IB.6}
\]

Since `beta<=theta_v`,

\[
{\pi\over3}<\alpha<\theta_v-{\pi\over3}.
\tag{IB.7}
\]

The interval in (IB.7) is centered at `theta_v/2`, so

\[
\left|\alpha-{\theta_v\over2}\right|
< {\theta_v\over2}-{\pi\over3}
< {\pi\over6}.
\tag{IB.8}
\]

Let `w` be the middle contact neighbor corresponding to angle `alpha`.  Then

\[
\boxed{
(w-v)\cdot n_v
>\cos\left({\theta_v\over2}-{\pi\over3}\right)
>{\sqrt3\over2}.
}
\tag{IB.9}
\]

Thus the middle contact penetrates strongly into the force hull.

This argument also covers a double-unit corner.  If both hull sides are contacts, the
three contact directions are the two hull-boundary rays plus the middle ray.  If the
hull interior angle is at most `2pi/3`, three contacts are impossible because two
successive gaps would have total greater than `2pi/3`; the vertex is then degree two
and pays `s_B` instead.  No finite exceptional set of high-turn corners is needed.

## 3. The middle contact is loaded-to-unloaded and selections are distinct

The selected middle contact is not a hull-side contact.  Canonical full-core
loaded-chord elimination says every loaded-loaded unit contact is a loaded hull side.
Therefore the other endpoint `w` is unloaded.

Choose the middle contact at every degree-three loaded vertex incident to a unit hull
side.  Different loaded vertices give different selected edges: every selected edge
has exactly one loaded endpoint, and those loaded endpoints are distinct.

Let `V_U` be the number of loaded vertices incident to at least one exact loaded-unit
hull side.  Partition these vertices into degree-two and degree-three vertices.  The
first group contributes one each to `s_B`; the second contributes one distinct edge
to `E_bis`.  Hence

\[
\boxed{s_B+|E_{bis}|\ge V_U.}
\tag{IB.10}
\]

## 4. The unit-side graph has at least `e_BB` nonisolated vertices

The loaded-unit hull-side graph is a subgraph of the cyclic hull graph, so its maximum
degree is two.  Every path component with `r` edges has `r+1` nonisolated vertices,
and a cyclic component has equally many vertices and edges.  Therefore

\[
\boxed{V_U\ge e_{BB}.}
\tag{IB.11}
\]

Combining (IB.10) and (IB.11) proves (IB.1).

The inequality is sharp for an all-loaded unit cycle at the purely combinatorial
level: there `V_U=e_BB=q`.

## 5. Eliminate `e_BB` from the boundary-atom theorem

The exact low-`t` boundary-atom theorem gives

\[
\boxed{N_2+2e_{BB}\ge3q-b.}
\tag{IB.12}
\]

Equation (IB.1) gives

\[
2e_{BB}\le2s_B+2|E_{bis}|.
\]

Therefore

\[
N_2+2s_B+2|E_{bis}|
\ge N_2+2e_{BB}
\ge3q-b,
\]

which is (IB.2).

Unlike the earlier endpoint-attachment inequality, no run count, `J_BI`, or additive
constant is required.  All selected inward contacts satisfy the quantitative
projection (IB.9).

## 6. Low-`t` quantitative consequence

On a convergent Type-II subsequence write

\[
t={q-k\over D},\qquad
\kappa={k\over D},\qquad
\delta={b-P_F\over D}.
\]

The proof-only minimax/§171 squeeze is

\[
2\delta+{\kappa\over2}\le R(t),
\qquad
R(t)={9t\over2}-2\pi-C_0,
\qquad
C_0=2\sqrt{\Delta_2}+0.0021.
\tag{IB.13}
\]

As in the boundary-atom theorem,

\[
{3q-b\over D}
=3t+3\kappa-\pi-\delta+o(1).
\]

At fixed `t`, the minimum of `3kappa-delta` subject to (IB.13) occurs at
`kappa=0`, `delta=R(t)/2`.  Hence

\[
\boxed{
\liminf {3q-b\over D}
\ge B(t):=3t-\pi-{R(t)\over2}
={3t\over4}+{C_0\over2}.
}
\tag{IB.14}
\]

Put

\[
M_{IB}:=\max\{N_2,s_B,|E_{bis}|\}.
\]

The coefficients on the left of (IB.2) sum to five, so

\[
\boxed{
\liminf {M_{IB}\over D}
\ge {B(t)\over5}
={3t\over20}+{C_0\over10}.
}
\tag{IB.15}
\]

At the current proof-only floor

\[
t_{21}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0017279
=1.82124143797944\ldots,
\]

one has

\[
B(t_{21})=2.3192938853\ldots,
\]

and therefore

\[
\boxed{
M_{IB}\ge0.4638587770\,D-o(D).
}
\tag{IB.16}
\]

This supersedes the weaker four-currency `0.38655D` consequence of the endpoint-
attachment note.

## 7. Convert the tooth currency too

For every fixed

\[
0<\eta<2(1-\cos(\pi/12)),
\]

the shallow-tooth penetration theorem gives

\[
E_{pen}(\eta)
\ge {1\over4}\left(N_2-{d_{out}\over\eta}\right),
\qquad d_{out}=b-P_F.
\tag{IB.17}
\]

Equivalently,

\[
N_2\le4E_{pen}(\eta)+{d_{out}\over\eta}.
\]

Insert this upper bound for the same positive currency into (IB.2):

\[
\boxed{
4E_{pen}(\eta)+2s_B+2|E_{bis}|
\ge3q-b-{d_{out}\over\eta}.
}
\tag{IB.18}
\]

Let

\[
E_{str}(\eta):=E_{pen}(\eta)\cup E_{bis}.
\]

Then both contact sets on the left are contained in `E_str`, so

\[
4|E_{str}|+2|E_{str}|+2s_B
\ge
4E_{pen}+2|E_{bis}|+2s_B.
\]

Therefore

\[
\boxed{
6|E_{str}(\eta)|+2s_B
\ge3q-b-{d_{out}\over\eta}.
}
\tag{IB.19}
\]

Every edge in `E_str` is a physical unit contact with a strong inward projection
relative to one local boundary feature: edges from `E_bis` have projection
`>sqrt(3)/2` relative to the hull-angle bisector, while edges from `E_pen` have the
explicit tooth-normal lower bound from the shallow-tooth theorem.

Consequently

\[
\boxed{
\liminf {1\over D}\max\{s_B,|E_{str}(\eta)|\}
\ge {B(t)-R(t)/(2\eta)\over8}.
}
\tag{IB.20}
\]

At `t=t_21`, `R(t_21)/2=0.002837775...`.  Taking `eta=0.06` gives

\[
\boxed{
\max\{s_B,|E_{str}(0.06)|\}
\ge0.2839997044\,D-o(D).
}
\tag{IB.21}
\]

For `eta=0.06`, the shallow-tooth contacts have inward normal component at least

\[
Y_{0.06}=\sin\!\left({\pi\over3}-\arccos(0.97)\right)
=0.71849218\ldots,
\]

while the bisector contacts have component greater than `sqrt(3)/2`.

Thus the low-`t` endpoint now contains either a macroscopic loaded-degree deficit or a
macroscopic unweighted population of genuinely inward unit contacts.

## 8. Frontier effect

The surviving endpoint can no longer hide the exact-unit loaded boundary inside a
shell-like cycle without paying interior geometry.  Even the regular odd-shell local
pattern has every loaded boundary vertex incident to unit sides; in a canonical full
core, any degree-three realization must send a third unit contact strongly inward,
while a degree-two realization pays `s_B`.

The remaining closing problem is therefore narrower:

```text
low t
  -> either s_B = Omega(D)
     or E_str = Omega(D) strongly inward unit contacts
  -> ? force train/interface area, response rank, or source-preserving descent.
```

The theorem is deliberately unweighted.  No KKT multiplier floor on the inward
contacts is assumed.

## 9. Scope audit

- The proof uses the exact unit hull side as one tangent-cone boundary ray.  No
  near-circle or small-turn hypothesis is used.
- Triangle-freeness is used only through strict `>pi/3` separation of consecutive unit
  contact directions.
- Loaded-chord elimination is used to make the selected middle contact
  loaded-to-unloaded.
- Selected middle edges are distinct because each has a different loaded endpoint.
- `V_U>=e_BB` is pure cycle/path combinatorics and remains valid for the all-unit
  cyclic case.
- The shallow-tooth conversion keeps its own explicit `eta` scope.
- Numerical constants inherit the proof-only minimax-atomic-gap lifecycle.
- No exact unit equilateral triangle or strict same-cardinality sub-`D` competitor has
  been produced.

**Disposition:** proof-only structural theorem.  C-II and Level I remain open.
