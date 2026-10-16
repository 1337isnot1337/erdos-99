# Target C-II — low-`t` boundary-atom and curvature squeeze

**Date:** 2026-09-14  
**Status:** proof-only structural consequence; theorem-state authority unchanged  
**Scope:** canonical full-core near-disk Type-II branch; low-`t` numerical corollaries additionally use the proof-only minimax atomic gap `0.0021` / §171  
**LEVEL I STATUS:** `STILL OPEN`

The current low-`t` endpoint has two boundary descriptions that have so far been used
separately:

1. the exact outer-route decomposition into direct unit loaded-hull sides and two-edge
   teeth; and
2. the contact-curvature identity for loaded and unloaded positive-core vertices.

Combining them removes the diffuse `long-side` interpretation from one part of the
frontier.  The resulting quantities are actual source objects: exact loaded-loaded unit
contacts, actual two-edge outer teeth, loaded contact-degree slack, and unloaded
trivalent vertices.

Use the canonical notation

\[
q=|B|,\qquad k=d_H+s_Z,\qquad x_B=b-q,
\]

where `B` is the loaded force-hull vertex set and `b` is the occurrence-counted old
outer contact walk.  For consecutive loaded hull vertices let

\[
s_i=|b_i-b_{i+1}|,
\]

and put

\[
m=\#\{i:s_i>1\},\qquad U_1:=q-m.
\]

Thus `U_1` is the number of consecutive loaded-hull sides of exact length one.  Every
such side is an actual unit contact.  Let `N_2` be the number of genuine two-edge outer
teeth from Section 126, and let

\[
u_B:=x_B-m\ge0.
\]

In the canonical full-core near-disk branch, loaded-chord elimination gives

\[
\boxed{U_1=e_{BB}},
\tag{BA.1}
\]

because every loaded-loaded unit contact is a loaded hull side and every unit loaded
hull side is a contact.

## 1. Exact boundary-atom inequality

Audited Section 126 gives

\[
0\le m-N_2\le u_B.
\tag{BA.2}
\]

Therefore

\[
N_2\ge m-u_B.
\tag{BA.3}
\]

On the other hand

\[
U_1=q-m.
\tag{BA.4}
\]

Adding (BA.3) to twice (BA.4) cancels the hidden integer route variable:

\[
\begin{aligned}
N_2+2U_1
&\ge m-u_B+2q-2m\\
&=2q-(m+u_B)\\
&=2q-x_B\\
&=3q-b.
\end{aligned}
\]

Hence the finite source-level inequality

\[
\boxed{N_2+2U_1\ge3q-b.}
\tag{BA.5}
\]

Using (BA.1), the full-core near-disk form is

\[
\boxed{N_2+2e_{BB}\ge3q-b.}
\tag{BA.6}
\]

In particular

\[
\boxed{\max\{N_2,e_{BB}\}\ge {3q-b\over3}.}
\tag{BA.7}
\]

This is stronger for the present endpoint than the preceding
`max{N_2,L_{>2}}` dichotomy.  It does not merely force metric length somewhere on the
boundary: it forces one of two actual contact structures.

## 2. Low-`t` quantitative form

On a convergent Type-II subsequence write

\[
t={q-k\over D},\qquad \kappa={k\over D},\qquad
\delta={b-P_F\over D}.
\]

Type II gives `P_F/D -> pi`, so

\[
{q\over D}=t+\kappa,
\qquad
{b\over D}=\pi+\delta+o(1).
\tag{BA.8}
\]

The proof-only minimax atomic-gap theorem and audited §171 squeeze give

\[
2\delta+{\kappa\over2}\le R(t),
\qquad
R(t):={9t\over2}-2\pi-C_0,
\tag{BA.9}
\]

where

\[
C_0:=2\sqrt{\Delta_2}+0.0021,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

Divide (BA.7) by `D`.  The numerator is

\[
{3q-b\over D}
=3t+3\kappa-\pi-\delta+o(1).
\]

Under (BA.9), the minimum of `3 kappa-delta` occurs at
`kappa=0`, `delta=R(t)/2`, so

\[
\liminf {1\over D}\max\{N_2,e_{BB}\}
\ge {3t-\pi-R(t)/2\over3}.
\]

Substituting the definition of `R(t)` cancels `pi` exactly and gives

\[
\boxed{
\liminf {1\over D}\max\{N_2,e_{BB}\}
\ge {t\over4}+{C_0\over6}.
}
\tag{BA.10}
\]

At the current proof-only floor

\[
t_{21}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0017279
=1.82124143797944\ldots,
\]

(BA.10) is approximately

\[
\boxed{
\max\{N_2,e_{BB}\}
\ge0.77309796\,D-o(D).
}
\tag{BA.11}
\]

The decimal is orientation only; the theorem is the exact expression in (BA.10).

## 3. Two concrete branches

### 3.1 Tooth branch

If the first alternative in (BA.10) occurs, then

\[
N_2\ge\left({t\over4}+{C_0\over6}-o(1)\right)D.
\tag{BA.12}
\]

The shallow-tooth penetration theorem applies directly.  For every fixed

\[
0<\eta<2(1-\cos(\pi/12)),
\]

it gives

\[
E_{pen}(\eta)
\ge {1\over4}\left(N_2-{d_{out}\over\eta}\right),
\qquad d_{out}=b-P_F.
\tag{BA.13}
\]

Thus the tooth branch is not merely a linear tooth count: after paying the already
small outer detour it produces a linear set of distinct strongly inward unit contacts.
For example `eta=0.06` is within the allowed geometric range.  At the current floor,
using `delta<=0.002837775+o(1)`, (BA.11)--(BA.13) give approximately

\[
E_{pen}(0.06)\ge0.18145\,D-o(D).
\tag{BA.14}
\]

Each selected edge retains the inward-component conclusion of the shallow-tooth
penetration theorem.  The displayed decimal is again non-authoritative orientation.

### 3.2 Exact loaded-unit branch

If the second alternative in (BA.10) occurs, then the source has at least

\[
\left({t\over4}+{C_0\over6}-o(1)\right)D
\]

actual unit contacts joining consecutive loaded diameter endpoints on the force hull.
The subgraph consisting of these hull sides is a subgraph of one cycle.  A union of
path runs with `E` edges has a matching of size at least `floor(E/2)`; the same is true
for the full cycle.  Hence the loaded-unit branch contains a pairwise vertex-disjoint
matching of size

\[
\boxed{
M_{BB}\ge {e_{BB}\over2}-O(1).
}
\tag{BA.15}
\]

At the current floor this is approximately

\[
\boxed{M_{BB}\ge0.38654\,D-o(D).}
\tag{BA.16}
\]

Every endpoint in this matching is an actual diameter endpoint, not merely a hull
vertex without diameter load.

## 4. Exact low-`t` contact-curvature identity

There is a second independent simplification at the same endpoint.

Let

\[
s_B:=\sum_{b\in B}(3-\deg_C b)
\]

be loaded contact-degree slack, and let `n_j` count unloaded positive-core vertices of
contact degree `j`.  Canonical full-force visibility gives loaded degree at most three
and unloaded degree in `{3,4,5}`.

For completeness, rederive the curvature identity.  If `v,e` are the contact-core
vertex and edge counts, Euler plus bounded-face incidence gives

\[
e=2v-2-{b+Q\over2}.
\tag{BA.17}
\]

Therefore

\[
\sum_{u\in V(C)}(4-\deg_Cu)=4v-2e=4+b+Q.
\tag{BA.18}
\]

The loaded vertices contribute `q+s_B`; the unloaded vertices contribute `n_3-n_5`.
Consequently

\[
s_B+n_3-n_5=4+(b-q)+Q.
\tag{BA.19}
\]

The exact outer ledger is

\[
b+Q=2(q-k).
\tag{BA.20}
\]

Substitution yields the exact finite identity

\[
\boxed{s_B+n_3-n_5=4+q-2k.}
\tag{BA.21}
\]

Since `n_5>=0`,

\[
\boxed{s_B+n_3\ge4+q-2k.}
\tag{BA.22}
\]

Normalized in the low-`t` notation,

\[
\liminf {s_B+n_3\over D}\ge t-\kappa.
\tag{BA.23}
\]

Using `kappa<=2R(t)` from (BA.9),

\[
\boxed{
\liminf {1\over D}\max\{s_B,n_3\}
\ge {t-2R(t)\over2}.
}
\tag{BA.24}
\]

At `t=t_21`, where `2R(t_21)=0.0113511`, this is approximately

\[
\boxed{
\max\{s_B,n_3\}
\ge0.90494516\,D-o(D).
}
\tag{BA.25}
\]

This is a low-`t` specialization of the contact-curvature ledger, not the older
`x_B=o(D)` near-circle corollary.  It uses the current outer identity and therefore
remains valid even though `x_B` is linear at the present endpoint.

## 5. Combined endpoint

Near the present low-`t` floor, every survivor must therefore realize simultaneously

```text
(A) either ~0.773D actual two-edge outer teeth
    or ~0.773D exact loaded-loaded unit hull contacts,

(B) either ~0.905D loaded contact-degree slack
    or ~0.905D unloaded trivalent vertices,

(C) the concurrently improved ~0.495D pentagon sea,
    near-extremal loaded diameter thrackle,
    and narrow total stopped-train band.
```

On the tooth side, (A) already upgrades to a macroscopic inward-contact population by
the shallow-tooth penetration theorem.  On the exact-unit side, loaded-chord
elimination makes the matching in (BA.15) a matching of actual hull contacts between
actual diameter endpoints; no interior loaded chord can absorb the count.

The remaining closing theorem is therefore a compatibility statement between these
boundary atoms and the near-extremal Woodall diameter graph / pentagon-dominated train
network.  This note does not provide that final source-preserving contradiction.

## 6. Scope audit

- `b` is occurrence-counted throughout; no simple outer-walk assumption is inserted.
- `U_1=q-m` counts exact Euclidean unit sides, not sides merely close to one.
- Section 126 is used only for `m-N_2<=u_B` and the actual two-edge-tooth
  interpretation.
- The replacement `U_1=e_BB` uses canonical full-core loaded-chord elimination and is
  therefore scoped to the full-core near-disk branch.
- Contact-isolated source points remain in the full source and are absent only from the
  positive-contact core matrices by definition.
- (BA.21) is rederived from Euler, face incidence, degree bounds, and the exact outer
  ledger; it does not import the older near-circle hypothesis.
- The numerical constants inherit the proof-only minimax-atomic-gap lifecycle.  No theorem-state
  promotion is claimed.
- No exact unit equilateral triangle or strict same-cardinality sub-`D` competitor has
  been produced.

**Disposition:** proof-only structural theorem.  C-II and Level I remain open.
