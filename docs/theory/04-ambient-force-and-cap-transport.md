# Shared theory — ambient force geometry and exterior-cap capacity

**Promoted integrator audit: 2026-09-09. Level I remains open.**

This module transports Target A's global source-hull estimate and Target B's
shared Oler accounting into Target C's actual force hull. Promotion is limited
to AG/AR/AS/AP and EC/EP/ES below. Post-ZF rigidity, topology, and numerical
specializations are not promoted by association.

Complete proofs and regression audits are in the promoted scopes of:

- [Ambient-force geometry](../reports/integrator_ambient_force_geometry_2026-09-09.md),
  Sections 1–6 and 8; Section 7's DB specialization remains conditional.
- [Exterior-cap capacity](../reports/integrator_exterior_cap_capacity_2026-09-09.md),
  Sections 1–5 and 7; its numerical Section 6 remains conditional.

## 1. Every diameter-support hull inherits ambient roundness

Let `A` be any global unit-separated minimum-diameter source with
`D>16sqrt(3)`, let `K=conv A`, and translate its circumcenter to zero. Put

\[
\eta=3^{1/4}\sqrt D,\qquad \mu=\sqrt{D\eta+\eta^2}=o(D).
\]

[Target A Section 155](../targets/target-a/08-prescribed-phase-alignment.md)
gives `K subset B(0,D/2+eta)`. This source-only estimate does **not** require
its additional very-super-boundary condition for embedding a smaller optimum.

For any nonempty collection `J` of actual source diameter pairs, define

\[
F_J=\operatorname{conv}V(J),\qquad
P_J=(D/2)\operatorname{conv}\{\pm u_e:e\in J\}.
\]

**AG.** Every diameter midpoint has norm at most `mu`, and

\[
d_H(F_J,P_J)\le\mu,\qquad d_H(F_J,-F_J)\le2\mu,
\qquad D/2\le R(F_J)\le D/2+\eta.
\]

For endpoints `b=m+(D/2)u`, `k=m-(D/2)u`, the parallelogram identity gives
`|m|^2+D^2/4<=(D/2+eta)^2`. Convex combinations give the Hausdorff bounds;
inclusion in `K` gives the circumradius bound. Every normalized limiting hull
is the convex hull of a closed antipodal subset of the radius-`1/2` circle.
It need not be the whole disk.

## 2. All KKT stresses and all diameter stars

For a normalized KKT stress take `J=H_+`. The promoted C10 theorem identifies
`F_J` with its force hull and gives `D^2/R(F_J)<=P_*<=2D`.

**AR.** Uniformly over all normalized stresses,

\[
\frac{D^2}{D/2+\eta}\le P_*\le2D,
\qquad 0\le2D-P_*\le\frac{4D\eta}{D+2\eta}<4\eta.
\]

Thus `P_*/D -> 2`. No estimate on omitted source population is needed.

**AS.** Once `2mu<D`, every angle between two actual diameter pairs sharing
an endpoint satisfies

\[
\theta\le2\arcsin(2\mu/D)=O(D^{-1/4}).
\]

Their opposite endpoints differ by twice the difference of their midpoints,
so have distance at most `4mu`; the chord formula proves the claim. The old
C18 fixed ceiling remains valid but is asymptotically weaker.

Neither conclusion implies a matching diameter graph. Regular odd shells have
linearly many branching diameter vertices and `P_*/D -> 2`.

## 3. Actual force-hull area/perimeter transport

Let `g_i` be the cyclic projective gaps of the distinct directions in `J`,
summing to `pi`. The centered polygon satisfies

\[
\operatorname{per}(P_J)=2D\sum_i\sin(g_i/2),\qquad
\operatorname{area}(P_J)=D^2\sum_i\sin g_i/4.
\]

Perimeter of a degenerate segment is twice its length.

**AP.** The parallel-body identities and AG give

\[
|\operatorname{per}(F_J)-\operatorname{per}(P_J)|\le2\pi\mu,
\]

\[
|\operatorname{area}(F_J)-\operatorname{area}(P_J)|
\le\pi D\mu+\pi\mu^2.
\]

The inequality `g-sin g<=4(g-2sin(g/2))` on `[0,pi]` additionally gives

\[
\operatorname{area}(F_J)\ge D\operatorname{per}(F_J)-3\pi D^2/4
-3\pi D\mu-\pi\mu^2.
\]

Thus limiting normalized area and perimeter obey `a>=p-3pi/4`. A force hull
with `P_F/D -> pi` has disk limit and `area(F)/D^2 -> pi/4`, not merely an
arbitrary constant-width limit. No conductance estimate follows.

## 4. Exact exterior population and independent cap capacities

Let `E` be any subset of the extreme vertices of `K` with a two-dimensional
hull `F=conv E`. Supported diameter endpoint sets qualify by the shared
[extreme-endpoint lemma](01-local-structure.md). Set `Z=|A\setminus F|` and
`a_0=sqrt(3)/2`.

Noncommon source-hull arcs between consecutive vertices of `F`, closed by
their chords, form `k` convex caps with disjoint interiors. If `P_com` is
the common-side length, then

\[
\sum_i\operatorname{area}(K_i)=\operatorname{area}(K)-\operatorname{area}(F),
\qquad\sum_i\operatorname{per}(K_i)=P_K+P_F-2P_{\rm com}.
\]

**EC.** Oler applied to each cap's `z_i` external points and its two chord
endpoints gives

\[
Z\le\frac{\operatorname{area}(K)-\operatorname{area}(F)}{a_0}
+\frac{P_K+P_F}{2}-P_{\rm com}-k.
\]

**EP.** Oler inside `F` and the strict global lattice comparison give

\[
-\pi D/2-1<Z-\frac{\pi D^2/4-\operatorname{area}(F)}{a_0}\le\pi D.
\]

Thus exterior density equals missing force-hull area density to `O(D^-1)`
after division by `D^2`. Points inside `F` need not belong to the positive core.

**ES.** Write `sigma(L,N)=area(L)/a_0+per(L)/2+1-N`. For actual populations
`n`, `n-Z`, and `z_i+2`, the exact identity is

\[
\sigma_F+\sum_i\sigma_i
=\sigma_K+P_F-P_{\rm com}-k<3\pi D/2+1.
\]

This also bounds the sum of independent container-capacity deficits because
`alpha_1(L)-N<=sigma(L,N)`. Separate optimal cap packings need not be compatible
across their interfaces.

## 5. Promotion boundary and live endpoint

These theorems require no simultaneous hull saturation and secondary
diameter-count minimum. They do not prove A's Schur bound, B's exact shell
stability, or the C-II contradiction.

The [conditional cavity report](../reports/integrator_joint_cavity_exclusion_2026-09-09.md)
uses unpromoted post-ZF inputs to obtain the `0.593235...` surplus floor. That
consequence and the DB-specialized `0.618470...` area floor are **not promoted**
by this module. The numerical computations are finite checks of separate
analytic proofs, not global-optimality certificates.
