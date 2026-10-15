<!-- theorem-state: {"artifact_id":"ART-94AC16B801A9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: exact hull-side train capacity and the empty October high-t branch

Date: 2026-10-04. Base: `419c9bec2ed8fa2cc105a80803a279339e7bea9e`.
State: `2026-09-14.audit.51`. Target: C-II.
Classification: proved candidates awaiting independent audit and promotion;
rejected interpretation of the October high-t branch as a surviving regime.
Artifact lifecycle: unreviewed. C-II and Level I remain open.

## 1. Obligation and result

The run began with the proposed high-t collar-to-pentagon transport route.
Its October scope requires Type II, `x_B=O(sqrt(D))`, and
`t_D=(q-k)/D <= 1.860+o(1)`. Before using that transport, this report tests

```text
exact actual hull-side train-end accounting
  -> 5 t_D D + x_B + m_B >= 3 per(F) - 2
  -> exclusion of every Type-II sequence with x_B=o(D),
     limsup t_D < 3 pi/5
  -> the stated October high-t collar branch is empty.
```

The new finite accounting improves the previously available `2x_B` term to
`x_B+m_B`. It also improves the September full-core surplus tradeoff from
`2u_B-3m_B` to `u_B-3m_B` without importing an unpromoted theorem.
The asymptotic threshold `3pi/5` itself is prior work, not a new constant.

Use the actual canonical contact-minimal, then diameter-pair-minimal source,
with full contact and diameter support. Retain all source points, including
contact isolates. Write

\[
b=q+x_B,\quad k=d_H+s_Z,\quad t_DD=q-k,\quad
P_F=\operatorname{per}(F),\quad
m=m_B,\quad u_B=x_B-m.
\]

Here `b` counts occurrences on the global positive-contact outer walk, `m`
counts nonunit sides of the loaded force hull, `Q` is the bounded exceptional
face excess, and `f` is the number of those faces. Let `N_tr` count complete
stopped trains, including singleton contact-edge trains.

The finite conclusions are

\[
\boxed{q\le x_B+2m+4f+Q+4},                         \tag{1}
\]
\[
\boxed{5t_DD+x_B+m\ge3P_F-2}.                      \tag{2}
\]

In the canonical full-core near-disk branch, additionally put
`mu_D D=e_BB+2s_C-3k` and let `c_I` count unloaded contact components. Then

\[
\boxed{5\mu_DD+u_B-3m+10c_I+22\ge3P_F}.             \tag{3}
\]

None of (1)--(3) assumes a small diameter matching. The finite train statement
needs no near-disk limit. The asymptotic applications use canonical Type II.

## 2. Every unit hull side is exactly a good outer interval

Let `b_i,b_{i+1}` be consecutive loaded force-hull vertices. Use the
distinguished exterior occurrences in canonical Sections 61 and 63, namely
the corners meeting the exterior of the convex hull. Let `W_i` be the
corresponding interval on the outer walk, of occurrence length `ell_i`.

**Lemma.**

\[
\ell_i=1\quad\Longleftrightarrow\quad |b_i-b_{i+1}|=1. \tag{4}
\]

The forward implication is a unit contact. For the converse, a unit hull side
is an actual contact because `C=C_*` contains all source contacts. All core
vertices and contact edges lie in `F`: unloaded coordinates are harmonic
convex combinations of their loaded attachments. No other source point can
lie in the relative interior of this unit segment, by unit separation.

The open half-plane outside `F` along the segment meets the unbounded contact
face. At either endpoint, this hull-side ray is an extreme ray of the
incident contact edges. All other incident rays lie in the inward tangent
cone of the strictly convex hull vertex. The outer face corner adjoining
the hull-side half-edge therefore contains the exterior hull sector. It is
the distinguished exterior occurrence at that vertex. Thus this one edge
joins the two distinguished occurrences, and `W_i` has length one.

This argument uses occurrences, not an assertion that each loaded vertex
occurs only once on the entire outer walk. An articulation may have other
outer occurrences in its inward sector. They do not interrupt the hull-side
half-edge joining the exterior occurrences.

For a nonunit hull side, the polygonal route inequality gives `ell_i>=2`.
Consequently the bad intervals are exactly the `m` nonunit hull intervals,
and their total edge-occurrence count is exactly

\[
\boxed{B_{\rm bad}=\sum_{i:\ell_i>1}\ell_i=x_B+m}.    \tag{5}
\]

The generic Section-61 bound `B_bad<=2x_B` discarded the information that
the direct hull side is present. Formula (5) restores it. It also gives

\[
u_B=\sum_{i:\,|b_i-b_{i+1}|>1}(\ell_i-2).             \tag{6}
\]

In particular `m=0` forces `x_B=u_B=0`. A source with positive global
outer-walk excess needs an actual nonunit loaded-hull side.

## 3. Complete finite capacity proof

Canonical Section 61 proves that the train-link graph is a forest: midpoint
steps have strictly increasing projection in the common normal direction.
Two trains cross at most once, and three cannot cross pairwise. This uses
the strict triangle-free rhombus angle range `(pi/3,pi/2]`.

Two trains with two good hull ends have alternating end pairs on the convex
hull, hence cross. Thus at most two complete trains have two good hull ends.
Singleton trains are included in this count and in the exact train identity

\[
N_{\rm tr}=\frac{b+Q}{2}+2f.                        \tag{7}
\]

Every other train has at least one end in a bad outer interval or on a bounded
exceptional face. These terminal incidences are distinct. The respective
capacities are (5) and the exact exceptional face perimeter `4f+Q`. Hence

\[
N_{\rm tr}-2\le x_B+m+4f+Q.                       \tag{8}
\]

Substitution of (7), with `b=q+x_B`, gives (1). Since `f<=Q`,

\[
q\le x_B+2m+5Q+4.                                  \tag{9}
\]

The canonical exact face identity is

\[
b+Q=2(q-k)=2t_DD.                                  \tag{10}
\]

Insert `Q=2t_DD-q-x_B` in (9):

\[
5t_DD\ge3q+2x_B-m-2
          =3b-x_B-m-2
          \ge3P_F-x_B-m-2.
\]

This proves (2). Both inequalities retain every occurrence and every
exceptional face. Define the nonnegative exact capacity slack

\[
\sigma=x_B+m+4f+Q-(N_{\rm tr}-2)\ge0.
\]

No dropped term is hidden:

\[
\boxed{
5t_DD+x_B+m-3P_F+2
=\sigma+2(Q-f)+3(b-P_F).
}                                                    \tag{11}
\]

## 4. Stronger full-core surplus payment

For the near-disk full-core branch, the canonical loaded-chord theorem gives
`e_BB=q-m`. The canonical pinned ledger gives

\[
s_C=m+k-c_I-2,
\qquad
\mu_DD=t_DD+m-2c_I-4.                              \tag{12}
\]

Equations (2) and (12), with `x_B=m+u_B`, prove (3). Equivalently (11) is

\[
5\mu_DD+u_B-3m+10c_I+22-3P_F
=\sigma+2(Q-f)+3(b-P_F).                            \tag{13}
\]

Since canonical component deatomization gives `c_I=o(D)` and Type II gives
`P_F/D -> pi`, every full-core survivor sequence satisfies

\[
\liminf\left(5\mu_D+\frac{u_B-3m}{D}\right)\ge3\pi.
\tag{14}
\]

If `limsup mu_D<=mu_0<3pi/5`, then

\[
\boxed{\liminf\frac{u_B-3m}{D}\ge3\pi-5\mu_0>0}.    \tag{15}
\]

This is a stronger source payment than the September report's
`liminf (u_B-3m/2)/D >= (3pi-5mu_0)/2`.
It does not identify global `u_B` with the harmonic-cell walks `L_r`.

## 5. The purported October high-t survivor is empty

If `x_B=o(D)`, then `0<=m<=x_B` also gives `m=o(D)`. Dividing (2) by `D`
and using the Type-II perimeter limit proves

\[
\boxed{\liminf t_D\ge\frac{3\pi}{5}=1.8849555921\ldots}. \tag{16}
\]

Therefore there is no unbounded canonical Type-II sequence with
`x_B=O(sqrt(D))` and `t_D<=1.860+o(1)`. The diameter matching bound
`nu(H)=O(sqrt(D))` is unnecessary for this contradiction.

The numerical fan, collar, two-cell-strip, and collar-to-pentagon populations
claimed at that endpoint cannot describe an actual surviving source regime.
Their conditional inequalities are not refuted; their antecedents cannot
hold along an unbounded sequence. In fact the asserted positive two-cell
coefficient requires `t<3pi/5`, exactly the threshold excluded by (16).

The same issue affects the entire positive collar-to-pentagon coefficient
window, not only the endpoint `1.860`. Its coefficient is

\[
A(t)=10\pi+3(\rho+g)+6\sqrt{\Delta_2}-21t,
\quad \rho=\cos\rho,\quad g=0.007707,\quad
\Delta_2=\frac{\pi}{2\sqrt3}.
\]

For `t>=3pi/5`,

\[
A(t)\le3(\rho+g)+6\sqrt{\Delta_2}-\frac{13\pi}{5}< -0.2.
\tag{18}
\]

An exact certification uses `rho<0.74`, `sqrt(Delta_2)<0.953`, and
`pi>3.14159`. Thus the proposed positive pentagon transport window is entirely
below the canonical low-excess threshold. Raising the endpoint slightly
cannot rescue that structural conclusion. The one-cell collar coefficient
`4pi-6t` can still be positive above `3pi/5`; no rejection of its finite
statement or of a correctly scoped later collar argument is asserted.

For every fixed `T<3pi/5`, the same proof excludes Type-II sequences with
`limsup t_D<=T` and `x_B=o(D)`. If `t_D<=T+o(1)` is retained while the
small-excess hypothesis is removed, (2) instead forces

\[
\liminf\frac{x_B+m}{D}\ge3\pi-5T,
\qquad
\liminf\frac{x_B}{D}\ge\frac{3\pi-5T}{2}.             \tag{17}
\]

At `T=1.860`, the latter coefficient is `0.0623889803...`.
Allowing this linear excess invalidates every use of `x_B=o(D)` in the
October endpoint evaluations. Section 7 supplies an exact scalar regression
against assuming the positive collar transport persists after that change.

## 6. Dependencies and authority

Only the following canonical inputs are load-bearing:

| Input | Path and use |
| --- | --- |
| `C-LINEAR-NONMATCH` | [Section 61](../targets/target-c/61-linear-nonmatching-excess-audit.md), train geometry, exact train count, at most two good-to-good trains |
| `C-LOADED-HULL` | [Section 63](../targets/target-c/63-loaded-hull-slack-audit.md), distinguished exterior occurrences, metric route inequality, face identity |
| `C-ATTACH-CURRENCY` | [Section 62](../targets/target-c/62-attachment-incidence-currency-audit.md), harmonic trapping and pinned ledger |
| `C-FULLCORE-LOADED-CHORD` | [Promoted report](target_c_fullcore_loaded_chord_elimination_2026-09-14.md), only for (3), (12)--(15) |
| `C-COMP-DEATOMIZATION` | [Section 75](../targets/target-c/75-all-phase-component-deatomization-audit.md), `c_I=o(D)` only |
| `C-FULLCORE-NEAR-DISK` | [Section 80](../targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md), `P_F/D -> pi` only |

The September [outer-walk/surplus report](target_c_outerwalk_surplus_mu_tradeoff_2026-09-25.md)
is prior art, independently checked here, not a theorem premise. The five October
high-t files are the subjects of the scope audit, not mathematical premises.
PR #624's mixed-core rigidity and the current strong open-cell chain are not used.

No affine-kernel statement is extended to isolated coordinates. The result counts
the actual core and its actual outer walk while leaving all source points in place.
No competitor or finite deformation is claimed.

## 7. Hostile checks and remaining frontier

The constant term in (2) cannot be improved uniformly: the exact unit square has
`q=b=P_F=4`, `m=x_B=Q=f=0`, `N_tr=2`, `k=2`, and `t_DD=2`. Equation (2)
is equality. This is a finite check, not an asymptotic survivor.

Run

```sh
python3 research/verify_target_c_hull_side_train_capacity_2026_10_04.py
```

The exact `Fraction` verifier checks all connected, two-dimensional subsets
of two specified 3-by-3 unit lattices, plus an additional rational star:
383 actual unit-separated triangle-free sources. Of those, 354 lattice
packets have repeated outer occurrences and 225 checked packets have repeated
occurrences of a strict hull vertex. All actual contacts, facial walks,
distinguished exterior occurrences, and complete stopped train components
are reconstructed, including singleton trains. The verifier checks (4)--(9)
and the corresponding exact slack identity with `P_F` replaced by `b`.
The report's metric step from `b` to `P_F` is the analytic triangle inequality.

The hostile star is

\[
(0,0),\ (5/13,12/13),\ (1,0),\ (5/13,-12/13).
\]

Its actual contact graph is the three-edge star centered at the strict hull
vertex `(0,0)`, which has three outer occurrences. Its unit hull sides still
join the distinguished occurrences in one step. Here `x_B=m=2`, so the bad
capacity is four, as (5) states. This packet tests the articulation issue;
it is not claimed to satisfy global minimality or canonical KKT.

The scalar regression after dropping `x_B=o(D)` has leading normalized data

\[
t=93/50,\quad x=m=1/5,\quad P=b=\pi,\quad
q=\pi-1/5,\quad Q=93/25-\pi,\quad f=9/20,
\]
\[
k=q-t,\quad e_{BB}=q-m,\quad s_C=m+k,\quad \mu=103/50.
\]

It satisfies the exact normalized face, pinned, train-capacity, and surplus
ledgers, the modern train-slack lower bound, and the finite fan/collar bounds
with the constant terms dropped at leading order. Set `nu/D=c_I/D=0` and
`S=I5_coll=0`. The collar lower expression is

\[
4\pi-6(93/50)-9/5=4\pi-324/25<0.
\]

The good-end and pentagon-capacity lower bounds are negative as well, so they
allow this zero transport. Thus the positive transport cannot be deduced
from these inequalities after relaxing the small-excess hypothesis. This is
an exact regression of the scalar inference, not an actual source example.
It omits geometric realization, integrality at each finite cardinality,
canonical KKT, and global optimality. It neither proves the linear-excess
regime exists nor refutes a theorem with additional geometric hypotheses.

Arithmetic bounds for pi use the alternating arctangent series and the
identity `pi=16 atan(1/5)-4 atan(1/239)`. Decimal output is for display only.
No numerical search or floating arithmetic is a proof premise.

The [full-core depletion continuation](target_c_fullcore_hull_train_depletion_floor_2026-10-04.md)
uses the audited exterior-occurrence lemma to remove all good-hull-end trains
before applying Mantel. It further raises the candidate full-core surplus floor
and excludes its endpoint. Those stronger conclusions remain unreviewed.
The real low-t target is a source-preserving payment of the **linear** global
outer-walk excess. The Type-I macroscopic-container and strong open-cell
deep-port/grid branches remain separate and open.

Promotion recommendation: independent audit of the exterior-occurrence lemma
before any state change. The branch exclusion follows even from the weaker
existing canonical end capacity, so it does not depend on accepting the new
sharpening. This report removes the stated October high-t scope as a research
target; it does not settle C-II or Level I.
