> Generated reading edition · [exact source](../../research/target_c_free_terminal_live_universal_flex_reservoir_2026-09-18.md) · source SHA-256 `96e9000d3f59e289011b7a3c417fbe66ea353a9aa9916c5b4e5e8d060e3f193e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e05f21ed8aea6de0371b4960f47c57612075414e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_live_universal_flex_reservoir_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6a9bdd1aab985010599ecc5d69e16c764f9de0eaa1b9894f0adf64d785bf638a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every live terminal FREE survivor has a linear exact contact-flex reservoir

**Date:** 2026-09-18  
**Status:** proof-only structural refinement; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE subsequences with `limsup t_D <= mu_*+0.00710`  
**Depends on:** correlated exact-`t` stability; terminal transport/fan ladder; hostile-audited shared routewise retention; dominant outer directional-energy bound; exact train-angle/exceptional-face closure representation; exact arbitrary O--O multishear; live diameter-locking theorem  
**Certificate:** `research/verify_target_c_free_terminal_live_universal_flex_reservoir_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current live terminal theorem still leaves a formal singleton branch because its local
three-spoke flex was stated only for **fully rhombic** pentagons. That restriction is
unnecessary for contact closure.

A pentagon with three complete trains running from the pentagon to the actual outer face
already has a local exact train-angle degree of freedom, even when one or more of the
three selected trains is singleton. A selected pentagon-to-outer train has only one
bounded exceptional endpoint, namely that pentagon. Rotating its train direction can
therefore affect no other bounded exceptional-face closure equation; strict rhombi on a
non-singleton selected train close identically by opposite-side cancellation, while a
singleton selected train has no rhombus equation at all.

This removes the singleton escape from the live window. Put

```math
c_*:=0.31805.
\tag{UF.1}
```

Every terminal full-core Type-II FREE survivor sequence satisfying

```math
\limsup t_D\le\mu_*+0.00710
=1.960362849540479\ldots
\tag{UF.2}
```

has an exact contact-preserving local product manifold `M_D` with

```math
\boxed{
\dim M_D\ge(c_*-o(1))D.
}
\tag{UF.3}
```

There is no alternative involving a large singleton population.

Applying the already proved live diameter-locking lemma to this product gives a
first-diameter-derivative matrix `G_D` of full column rank and a matching saturating all
flex coordinates. Consequently there are at least

```math
\boxed{
(c_*-o(1))D
}
\tag{UF.4}
```

pairwise distinct actual diameter bars participating in the locking system, and the
signed derivative incidence counts obey

```math
\boxed{
I_+\ge(c_*-o(1))D,
\qquad
I_-\ge(c_*-o(1))D.
}
\tag{UF.5}
```

Thus the live terminal window can no longer avoid a macroscopic exact contact-flex
space by moving mass into singleton trains. The remaining obstruction is entirely on
the active-diameter side.

---

## 1. Three pentagon-to-outer trains are enough

Let `P` be any bounded pentagonal contact face. Suppose at least three incident complete
stopped trains have terminal faces `P` and the actual outer face `O`. Choose three such
trains and orient their pentagon side vectors cyclically as

```math
u_1,u_2,u_3.
```

Let the two unselected pentagon side vectors be `v_1,v_2`. At the original placement,

```math
u_1+u_2+u_3+v_1+v_2=0.
\tag{1.1}
```

For train-angle parameters `theta=(theta_1,theta_2,theta_3)`, define

```math
\Phi(\theta)
:=R_{\theta_1}u_1+R_{\theta_2}u_2+R_{\theta_3}u_3+v_1+v_2.
\tag{1.2}
```

The equation `Phi(theta)=0` is exactly the vector closure equation for `P` after the
three selected train directions are changed.

### Lemma 1.1 — the local zero set contains a nonconstant curve

There is a nonconstant continuous, in fact smooth away from the elementary folded
case, one-parameter curve through `theta=0` on which `Phi=0`.

If `u_1,u_2,u_3` span the plane, then

```math
D\Phi(0)(a_1,a_2,a_3)
=J(a_1u_1+a_2u_2+a_3u_3)
\tag{1.3}
```

has rank two. The implicit-function theorem therefore gives a one-dimensional smooth
zero set through the origin.

It remains only to handle rank one. Then the three selected unit vectors are all
projectively parallel. They cannot all have the same oriented direction: their sum
would have norm three, while by (1.1)

```math
|u_1+u_2+u_3|=|v_1+v_2|\le2.
```

Hence two selected vectors are opposite; after relabeling, `u_2=-u_1`. Setting

```math
\theta_1=\theta_2=s,
\qquad
\theta_3=0
\tag{1.4}
```

preserves their cancellation exactly:

```math
R_su_1+R_su_2=0.
```

Thus (1.2) remains zero for every sufficiently small `s`. This is an explicit exact
nonconstant local curve. No convexity or near-orbit hypothesis is required.

### Lemma 1.2 — the local curve extends to the entire contact graph

Every selected train has terminal faces `P` and `O`. Therefore it appears in no other
bounded exceptional-face terminal equation. Assign the varied unit direction to every
contact edge of that complete train.

- A strict rhombus crossed by selected trains closes identically: opposite sides belong
  to the same complete train and remain opposite after the train direction changes.
- If a selected train is singleton, it crosses no strict rhombus and creates no extra
  closure equation.
- The only bounded nonquadrilateral closure equation containing a selected train as a
  terminal train is the equation for `P`, already enforced by `Phi=0`.
- Every other bounded exceptional face is unchanged.

The bounded face walks generate the real cycle space of the plane contact graph.
Hence the changed unit edge vectors integrate to actual vertex positions, unique up to
translation on each contact component. Every old contact remains exactly unit length.
For each finite source, all old noncontacts have strict length greater than one, so a
small enough product neighborhood preserves all lower-distance constraints by
continuity. Contact-isolated source points may be held fixed.

Thus every such pentagon supplies one exact non-Euclidean contact-flex coordinate.

---

## 2. Different three-spoke pentagons give independent coordinates

Let `Y_3` be the terminal transport count

```math
Y_3=\#\{P:\ P\text{ is a bounded pentagon with at least three incident }P\!\!\to O
\text{ trains}\}.
\tag{2.1}
```

For every `P` counted by `Y_3`, choose three `P`-to-`O` trains and one local curve from
Section 1.

The chosen train triples for distinct pentagons are disjoint. A complete `P`-to-`O`
train has exactly one bounded terminal occurrence, so it cannot simultaneously be a
`P'`-to-`O` train for a different bounded face `P'`.

Therefore the local closure maps use disjoint train-angle variables. Their curves form
an exact local product of dimension `Y_3`. In particular,

```math
\boxed{
\text{three outer spokes per pentagon}\quad\Longrightarrow\quad
\dim M_D\ge Y_3.
}
\tag{2.2}
```

This is the point where the earlier fully-rhombic restriction disappears. Full
rhombicity is useful for rhombus-complex incidence statements, but it is not needed for
three-spoke contact closure.

The product contains no global infinitesimal rotation direction. Each local coordinate
varies only three train directions and leaves the other two pentagon side vectors
fixed. Any nonzero Euclidean rotation would rotate every fixed nonzero contact vector.

---

## 3. Correlated terminal fan bound without singleton subtraction

Retain the live-window variables

```math
r=\lim{Q-f\over D},
\qquad
\delta=\lim{b-P_F\over D},
\qquad
a=\lim\left({\tau_D\over D}-{\pi\over2}-0.007707\right),
\tag{3.1}
```

with

```math
\boxed{
a+2(r+\delta)\le5\varepsilon,
\qquad
\varepsilon=0.00710.
}
\tag{3.2}
```

Let

```math
\ell:=\lim {L_O\over D},
```

where `L_O` is the number of complete outer-to-outer stopped trains. The exact terminal
fan ledger at `k=3` gives

```math
\liminf {Y_3\over D}
\ge
A_3-{2\over3}\ell
+{7\over15}\delta
-{6\over5}r
-{4\over15}a,
\tag{3.3}
```

where

```math
M_*=4\sqrt{\frac\pi{2\sqrt3}}+2(0.007707),
\qquad
p_*={M_*\over5},
\qquad
A_3={\pi-2p_*\over3}
=0.537242187535821\ldots .
\tag{3.4}
```

The negative defect terms preserve more of the correlation than the previous
`-3epsilon` display. Since

```math
{6\over5}r+{4\over15}a
\le {3\over5}(a+2r)
\le {3\over5}(5\varepsilon-2\delta),
\tag{3.5}
```

(3.3) yields

```math
\boxed{
\liminf {Y_3\over D}
\ge
A_3-{2\over3}\ell+{5\over3}\delta-3\varepsilon.
}
\tag{3.6}
```

Unlike the old fully-rhombic fan estimate, no `-2S/D` term appears.

---

## 4. Small outer-loop count feeds back into a positive detour floor

Let `p` be the retained complement O--O pair mass from shared routewise retention. It
is a fractional mass supported on actual O--O trains, with every train carrying weight
at most one. Therefore

```math
\boxed{p\le\ell.}
\tag{4.1}
```

Set

```math
c_*={6361\over20000}=0.31805,
\qquad
d_*={213\over25000}=0.00852.
\tag{4.2}
```

Suppose first that `ell>=c_*`. The exact arbitrary O--O multishear immediately gives
an exact contact-flex product of dimension at least `(c_*-o(1))D`, proving (UF.3).

It remains to consider

```math
\ell<c_*.
\tag{4.3}
```

Then by (4.1), `p<c_*`. The live correlated two-bin envelope gives

```math
R\le\rho(\delta)
:=r_2\bigl(2s_2+0.007707+5\varepsilon-2\delta\bigr),
\tag{4.4}
```

where

```math
s_2=\sqrt{\frac\pi{2\sqrt3}},
\qquad
r_2(C)={C-\sqrt{8\Delta_2-C^2}\over2},
\qquad
\Delta_2={\pi\over2\sqrt3}.
```

Shared retention and dominant outer energy give

```math
z+p\ge{\pi\over2}-R-o(1),
\qquad
F(z):=z-6\sin(z/6)\le\delta.
\tag{4.5}
```

Thus a limiting survivor with `p<=c_*` must satisfy

```math
F\left({\pi\over2}-\rho(\delta)-c_*\right)\le\delta.
\tag{4.6}
```

The exact-rational certificate proves that the left-minus-right side of (4.6) is
strictly decreasing on `0<=delta<=0.01775` and is still positive at `delta=d_*`:

```math
\boxed{
F\left({\pi\over2}-\rho(d_*)-c_*\right)-d_*
>1.8\times10^{-6}.
}
\tag{4.7}
```

Consequently (4.3) forces

```math
\boxed{
\delta>d_*=0.00852.
}
\tag{4.8}
```

This uses the same hostile-audited retention and dominant-energy inputs as the current
`p>0.01` versus near-maximal-detour theorem, but chooses the threshold to optimize the
fan/flex handoff rather than to maximize pentagonal concentration.

---

## 5. The optimized handoff gives `0.31805D` exact dimensions in every case

Under (4.3) and (4.8), (3.6) gives

```math
\liminf {Y_3\over D}
>
A_3-{2\over3}c_*+{5\over3}d_*-3\varepsilon.
\tag{5.1}
```

The exact certificate proves

```math
A_3-{2\over3}c_*+{5\over3}d_*-3\varepsilon
>0.3181088
>c_*.
\tag{5.2}
```

Therefore

```math
\boxed{
\ell<c_*
\quad\Longrightarrow\quad
Y_3>(c_*-o(1))D.
}
\tag{5.3}
```

Section 2 turns these `Y_3` pentagons into an exact contact-flex product of dimension
at least `Y_3`. Together with the `ell>=c_*` O--O branch, this proves (UF.3).

For comparison, if the dominant-energy feedback (4.8) is omitted, the same direct
`Y_3` argument already gives the universal coefficient

```math
{3\over5}(A_3-3\varepsilon)
=0.3095653125\ldots .
\tag{5.4}
```

The shared-retention feedback raises the safe coefficient to `0.31805`.

A non-load-bearing numerical solve of the same scalar composition puts its fixed point
near `0.3180864`; the round value `0.31805` leaves a visible exact margin.

---

## 6. Diameter locking now applies without a singleton exception

Let `m_D=dim M_D`. The live diameter-locking proof uses only three facts about the
contact deformation product:

1. it is an exact contact-preserving local product;
2. its tangent coordinates are independent modulo Euclidean motions;
3. the canonical mixed contact/diameter rigidity theorem and strictly positive KKT
diameter stress apply.

Those facts hold for both products constructed above. Therefore the active-diameter
first-derivative matrix

```math
G_D\in\mathbb R^{H_D\times m_D}
```

has

```math
\operatorname{rank}G_D=m_D.
\tag{6.1}
```

KKT stationarity gives a strictly positive vector `beta` with

```math
G_D^T\beta=0.
\tag{6.2}
```

Hence the row vectors of `G_D` positively span `R^{m_D}`. Hall's theorem applied to the
nonzero pattern gives a matching saturating all `m_D` coordinates, so at least `m_D`
pairwise distinct actual diameter bars have nonzero matched derivatives. Positive
spanning also forces each coordinate column to contain both signs. Thus

```math
I_+\ge m_D,
\qquad
I_-\ge m_D.
\tag{6.3}
```

Combining with (UF.3) proves (UF.4)--(UF.5).

The result is structural rather than a diameter descent: positive spanning is exactly
the first-order cusp obstruction to choosing one tangent direction that shortens every
active diameter bar.

---

## 7. Remaining bottleneck

The previous live normal form had three possible carriers: singleton trains, O--O exact
shears, or fully-rhombic three-spoke pentagon flexes. The first carrier was not itself a
usable exact-flex reservoir.

That split is now gone in the whole `epsilon=0.00710` window. Every survivor has at
least `0.31805D-o(D)` independent exact contact-flex coordinates, whether or not
singletons are abundant. The active diameter system must lock all of them with full
column rank, positive spanning, and a coordinate-saturating matching to distinct
actual diameter bars.

The next closing theorem therefore does not need another contact-network case split.
It must use this large locked product to force one of the canonical source-level
outcomes: a positive lower payment into the aggregate `sum_r(L_r-2d_r)` / `e_BB-k`
currency strong enough to contradict the terminal ledger, or a source-preserving
finite deformation that passes through the diameter cusp and strictly reduces the
maximum distance.

No theorem-state file is changed.

**Disposition:** proved a universal live exact-flex reservoir and removed the singleton
escape from the terminal FREE window; C-II remains open.
