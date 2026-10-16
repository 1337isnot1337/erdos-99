<!-- migration-source: path=docs/reports/target_c_nearcircle_laminar_cap_capacity_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=c376078579c6425be2ab9b091cca99a91546ac58; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — laminar circular-cap capacity sharpens the near-circle harmonic component

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** asymptotic noncrossing convex-cap theorem  
**Target:** UF near-circle harmonic-cell branch after CH  
**Depends on:** DC disk convergence, C49 pairwise interior-disjoint attachment cells, C36/C44 attachment hull containment/diameter, AR cell Oler lower bound  
**Computation:** decimal root evaluation only

## LEVEL I STATUS

`STILL OPEN`

CH uses only the fact that every attachment cell of diameter at most `mu D` misses one common central disk. That produces the area upper bound `pi mu^2 D^2/4`, but it allows different cells to occupy the same circular cap in the comparison geometry.

C49 supplies more: the attachment-cell interiors are pairwise disjoint. In the disk limit, the minimal circular arcs supporting those cells form a laminar family. Grouping nested cells under the inclusion-maximal supporting arcs converts the problem into a one-dimensional cap-packing optimization on the outer circle.

The resulting capacity function is strictly smaller than CH's annulus bound for every fixed `0<mu<1`.

At UF's worst population crossover, the mandatory single-component graph diameter improves from

`0.6208918647... D`

to

\[
\boxed{0.7591662335\ldots D.}
\]

---

## 1. Circular cap notation

Normalize the limiting force hull to the disk

\[
B_{1/2}=\{x:|x|\le1/2\}.
\]

For an arc of central angle `theta in [0,pi]`, let `Cap(theta)` be the closed circular segment between that minor arc and its chord.

Its area is

\[
\boxed{
A_{cap}(\theta)
=\frac18(\theta-\sin\theta).
}
\tag{LC.1}
\]

Indeed the usual radius-`R` circular-segment formula is

\[
\frac{R^2}{2}(\theta-\sin\theta),
\]

and here `R=1/2`.

The function

\[
g(\theta):=\theta-\sin\theta
\]

is increasing and strictly convex on `(0,pi)` because

\[
g'(\theta)=1-\cos\theta>0,
\qquad
g''(\theta)=\sin\theta>0.
\tag{LC.2}
\]

---

## 2. Every short attachment cell lies in one cap

Let `Q` be the Hausdorff limit of a sequence of normalized attachment cells `P_r/D`, and suppose

\[
\operatorname{diam}Q\le\mu<1.
\]

All extreme points of `Q` come from limits of force-hull terminals, hence lie on `partial B_{1/2}`.

By CH.1, those boundary points lie in a circular arc of angular length at most

\[
\boxed{
\theta_\mu:=2\arcsin\mu<\pi.
}
\tag{2.1}
\]

Let `I(Q)` denote the unique minimal closed arc of length `<pi` containing the boundary support of `Q`. Then

\[
\boxed{
Q\subseteq Cap(|I(Q)|).
}
\tag{2.2}
\]

The uniqueness follows because a subset of a circle of circular diameter `<pi` has a unique shortest containing arc unless it is a singleton; singleton/degenerate limits have zero area and may be ignored.

---

## 3. Noncrossing cells give laminar minimal arcs

### Lemma LC.1 — laminarity

Let `Q_1,Q_2` be two positive-area convex hulls of boundary subsets of `B_{1/2}`, each of diameter `<1`, and assume

\[
\operatorname{int}Q_1\cap\operatorname{int}Q_2=\varnothing.
\]

Then their minimal arcs `I(Q_1),I(Q_2)` are either

1. interior-disjoint, or
2. one is contained in the other.

They cannot partially overlap without containment.

### Proof

Suppose the arcs partially overlap. Write their four extreme arc endpoints in cyclic order as

\[
a,c,b,d,
\]

where `a,b` are the endpoints of `I(Q_1)` and `c,d` those of `I(Q_2)`.

Because each arc has length below `pi`, all other support points of `Q_1` lie on the minor arc from `a` to `b`. The chord `ab` is therefore an edge of `Q_1`; similarly `cd` is an edge of `Q_2`.

The endpoints alternate on the circle, so the chords `ab` and `cd` cross properly in the disk. Since each cell has positive area and lies on the arc side of its base chord, a small neighborhood of the crossing on the appropriate sides lies in both convex hulls. Hence their interiors intersect, contradiction.

Therefore partial overlap is impossible. `square`

Thus the minimal supporting arcs of all positive-area limit cells form a laminar family.

---

## 4. Nested descendants stay inside the maximal cap

Let `I_*` be an inclusion-maximal arc in the laminar family. Every cell whose minimal arc lies inside `I_*` has all its boundary support inside `I_*`, hence its entire convex hull lies in the full cap `Cap(|I_*|)`.

Different inclusion-maximal arcs have disjoint interiors on the outer circle by laminarity. Therefore, if their angular lengths are

\[
\theta_1,\ldots,\theta_m,
\]

then

\[
0<\theta_j\le\theta_\mu,
\qquad
\sum_j\theta_j\le2\pi.
\tag{4.1}
\]

All cells are interior-disjoint by C49, so grouping them by maximal arc yields

\[
\boxed{
\sum_r\operatorname{area}(Q_r)
\le
\sum_{j=1}^m A_{cap}(\theta_j).
}
\tag{4.2}
\]

No assumption that attachment sets themselves are disjoint is needed. Shared boundary terminals correspond only to common arc endpoints or nested blocks and do not increase the cap union area.

---

## 5. Exact cap-budget optimization

We must maximize

\[
\sum_j g(\theta_j)
\]

subject to

\[
0\le\theta_j\le\theta_\mu,
\qquad
\sum_j\theta_j\le2\pi.
\]

Since `g` is increasing, a maximizer uses total angle `2pi`. Since `g` is convex, transferring angular mass from a smaller nonzero angle to a larger angle cannot decrease the sum until the larger angle reaches `theta_mu` or the smaller reaches zero.

Thus every maximizer has as many full `theta_mu` arcs as possible and at most one remainder arc.

Put

\[
\boxed{
k_\mu:=\left\lfloor\frac{2\pi}{\theta_\mu}\right\rfloor,}
\tag{5.1}
\]

and

\[
\boxed{
r_\mu:=2\pi-k_\mu\theta_\mu
\in[0,\theta_\mu).}
\tag{5.2}
\]

### Theorem LC.2 — normalized laminar cap capacity

Define

\[
\boxed{
\mathcal C(\mu)
:=
\frac18\left[
2\pi-k_\mu\sin\theta_\mu-\sin r_\mu
\right],
\qquad
\theta_\mu=2\arcsin\mu.
}
\tag{LC.3}
\]

Then any family of pairwise interior-disjoint positive-area convex hulls of subsets of the diameter-one circle, each of diameter at most `mu<1`, has total area at most

\[
\boxed{\mathcal C(\mu).}
\tag{LC.4}
\]

The bound includes arbitrarily deep nesting because nested descendants were grouped inside their maximal cap before the one-dimensional optimization.

For comparison, CH used only the common central hole and obtained `pi mu^2/4`. For every fixed `0<mu<1`, LC.4 is at least as strong and is strictly stronger away from degenerate limiting regimes.

---

## 6. Transfer back to the near-circle source

Suppose along a UF near-circle subsequence

\[
\limsup\frac{\delta_{\max}}D\le\mu<1.
\tag{6.1}
\]

DC gives Hausdorff convergence `F/D->B_{1/2}`. C44 gives

\[
\operatorname{diam}(P_r/D)
\le\frac{\delta_r+2}{D}
\le\mu+o(1).
\]

C49 gives pairwise interior-disjoint cells.

A compactness argument, discarding cells of vanishing normalized area and passing to finitely many positive-area limit cells at each fixed area threshold, applies LC.2. The discarded cells contribute arbitrarily little total area because the cells are disjoint inside a uniformly bounded hull.

Therefore:

### Corollary LC.3 — source cell-area upper bound

\[
\boxed{
\limsup
\frac1{D^2}
\sum_r\operatorname{area}(P_r)
\le\mathcal C(\mu).
}
\tag{LC.5}

\]

This is the noncrossing refinement of CH.4.

---

## 7. Compare with the AR Oler lower bound

AR/CH give in UF notation

\[
\boxed{
\liminf
\frac1{D^2}
\sum_r\operatorname{area}(P_r)
\ge
\frac\pi4\left(1-\frac\zeta\Delta\right).
}
\tag{7.1}
\]

Consequently every subsequential limit `mu` of `delta_max/D` below one must satisfy

\[
\boxed{
\mathcal C(\mu)
\ge
\frac\pi4\left(1-\frac\zeta\Delta\right).
}
\tag{LC.6}
\]

Define `mu_cap(zeta)` to be the smallest `mu in [0,1]` satisfying LC.6, with `mu_cap=1` if no value below one does.

### Theorem LC.4 — strengthened macroscopic-component bound

\[
\boxed{
\liminf\frac{\delta_{\max}}D
\ge\mu_{cap}(\zeta).
}
\tag{LC.7}
\]

Since `C(mu)<=pi mu^2/4`, LC.7 is at least as strong as CH.1.

---

## 8. UF crossover constant

At the UF worst crossover

\[
\zeta_*=0.5572837714\ldots,
\]

the required normalized cell area is

\[
\frac\pi4\left(1-\frac{\zeta_*}{\Delta}\right)
=0.3027762602\ldots .
\]

The equation

\[
\mathcal C(\mu)=0.3027762602\ldots
\]

has the relevant smallest solution

\[
\boxed{
\mu=0.7591662335\ldots .
}
\tag{8.1}
\]

At this value

\[
\theta_\mu=1.7240624121\ldots,
\qquad
k_\mu=3,
\qquad
r_\mu=1.1109980708\ldots .
\]

Hence

\[
\boxed{
\liminf\frac{\delta_{\max}}D
\ge0.7591662335\ldots
}
\tag{8.2}
\]

at the crossover, improving CH's `0.6208918647...`.

C40 and the near-circle hull-slot argument then give the same lower bound asymptotically for the number of distinct loaded attachments of this component.

---

## 9. Full-core endpoint

If `zeta=0`, the right side of LC.6 is `pi/4`, the entire disk area.

For every fixed `mu<1`, every term `sin theta_mu` and the nonzero remainder structure make

\[
\mathcal C(\mu)<\frac\pi4.
\]

Therefore

\[
\boxed{
\liminf\frac{\delta_{\max}}D\ge1,
}
\]

recovering CH.3. The LC proof explains the equality mechanism more sharply: to fill asymptotically the entire disk with disjoint boundary-vertex hulls, the maximum attachment-cell diameter must tend to the full disk diameter.

---

## 10. Binding configurations and caveats

- Nested noncrossing attachment blocks do **not** invalidate the cap estimate. Their minimal arcs are nested and all descendants remain inside the maximal cap.
- The theorem uses interiors disjoint, not disjoint terminal sets.
- Cells of zero or `o(D^2)` normalized area may be numerous; the compactness argument discards them at fixed area threshold and restores them after taking the threshold to zero.
- No claim is made that LC.4 is exactly attainable by a discrete unit-separated source. It is a valid continuum upper envelope.
- The cap bound is used only in the UF disk-limit branch. It is not a generic estimate for arbitrary force-hull shapes.

---

## 11. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| minimal arcs laminar for disjoint cell interiors | proved | partial overlap forces crossing base chords |
| nested descendants lie in maximal cap | proved | convex hull of boundary support inside containing arc |
| cap-budget optimizer | proved | convexity of `theta-sin theta` |
| LC.5 source transfer | proved asymptotically | DC compactness + C49 disjointness |
| crossover constant `0.759166...` | numerical evaluation of proved scalar equation | no proof dependence on decimal |
| full-core max component tends diameter scale | proved | capacity below `pi/4` for every fixed `mu<1` |
| Level I | still open | a `0.759D`--`D` harmonic component remains possible |

---

## 12. Next target

LC reduces the UF positive-density branch to a single very large harmonic component `I_*`.

At the crossover it has

\[
\delta_*/D\ge0.75916\ldots,
\qquad
|A_*|/D\ge0.75916\ldots .
\]

If its normalized diameter is `mu<1`, its attachments lie in an arc of normalized boundary length at most

\[
\arcsin\mu.
\]

At the crossover lower endpoint this is `0.86203...`, so the component occupies at least `88%` of all available terminal slots in its supporting arc.

The next exact geometric target is to show that such a densely pinned long harmonic component forces either

1. a second large attachment cell whose cap overlaps it (contradicting C49), or
2. enough exceptional-face perimeter inside the cap to exceed UF's global `Q` budget.

That is now a local cap problem rather than a source-wide diffuse-cell problem.
