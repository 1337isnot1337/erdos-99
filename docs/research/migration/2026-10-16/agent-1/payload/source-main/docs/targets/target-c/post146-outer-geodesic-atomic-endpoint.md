# Target C — §154 outer-geodesic atomic endpoint exclusion

**Date:** 2026-09-12  
**Lifecycle:** audited-working route module; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module records the hostile-audited content of former proof-only PR #402 under a
noncolliding research-tail label. It composes the audited-working stopped-train/phase
theorem §142 with the canonical Type-II force-hull limit and the audited-working
§146 density chain.

Its mechanism is structural. If the old outer contact walk is asymptotically geodesic
around the near-circular force hull, then its occurrence-counted projective edge
direction measure converges to uniform Lebesgue measure and is therefore atomless.
But the quadratic strict-rhombus density forces a positive atomic mass in the stopped-
train direction measure. Exact train endpoint incidence then forces the atomic trains
to spend linear endpoint capacity on bounded defect faces. This produces a stronger
`q-k` lower bound and excludes the formal §146 endpoint.

No rejected exterior-Reuleaux-cap argument is used. The zero-detour hypothesis is
explicit in the first theorem and is derived from §146 endpoint saturation only in the
second theorem.

Put

\[
\Delta_2={\pi\over2\sqrt3},\qquad
s_2:=\sqrt{\Delta_2},\qquad
C_{146}:={4\over9}(\pi+s_2)=1.8195135379794445\ldots .
\]

Use the standard Type-II notation:

- `F` is the loaded force hull, `P_F=per(F)`;
- `b` is the occurrence-counted outer contact-face walk length;
- `Q=sum_F(deg F-4)` over bounded nonquadrilateral faces and `f` is their count;
- `T` is the complete stopped-train count;
- `q` is the loaded force-hull vertex count;
- `k=d_H+s_Z`;
- `R_4` is the strict-rhombus face count.

Canonical Type II gives, after translation,

\[
{P_F\over D}\to\pi,
\qquad {R_4\over D^2}\to\Delta_2,
\qquad D^{-1}F\to B_{1/2}
\]

in Hausdorff distance. The exact outer-walk ledger is

\[
\boxed{b+Q=2(q-k).}
\tag{154.1}
\]

Audited-working §142 gives the exact stopped-train endpoint incidence

\[
\boxed{2T=b+Q+4f}
\tag{154.2}
\]

and the following atomic crossing statement. Along every subsequence on which
`T/D->x` and the empirical probability measure on projective train directions
converges to a measure `mu` with total atomic mass `sigma`, one has

\[
\boxed{x\sigma\ge2s_2.}
\tag{154.3}
\]

## 154.1 Near-geodesic outer walks have uniform projective direction measure

Assume along a Type-II subsequence that

\[
\boxed{b-P_F=o(D).}
\tag{154.4}
\]

Define the occurrence-counted projective outer-direction measure

\[
\mu_D^{out}:={1\over D}
\sum_{e\in\partial_{out}C}^{occ}\delta_{[e]}.
\tag{154.5}
\]

Bridge and articulation repetitions are retained. Its total mass is

\[
\mu_D^{out}(\mathbb R/\pi\mathbb Z)={b\over D}\to\pi.
\tag{154.6}
\]

For a unit direction `u_alpha`, let `w_F(alpha)` be the width of `F`. Project the
closed outer walk onto `u_alpha`. A closed real-valued walk visiting both extremes of
an interval of length `w` has total variation at least `2w`; therefore

\[
\int |\cos(\theta-\alpha)|\,d\mu_D^{out}(\theta)
\ge {2w_F(\alpha)\over D}.
\tag{154.7}
\]

The Type-II Hausdorff limit gives `w_F(alpha)/D->1` uniformly in `alpha`. Let
`mu_out` be any weak limit of `mu_D^{out}`. Then

\[
C\mu_{out}(\alpha):=
\int |\cos(\theta-\alpha)|\,d\mu_{out}(\theta)\ge2
\quad\text{for every }\alpha.
\tag{154.8}
\]

Fubini and

\[
\int_0^\pi|\cos(\theta-\alpha)|\,d\alpha=2
\]

give

\[
\int_0^\pi C\mu_{out}(\alpha)\,d\alpha
=2\mu_{out}(\mathbb R/\pi\mathbb Z)=2\pi.
\tag{154.9}
\]

The continuous function `C mu_out-2` is nonnegative and has integral zero, hence it
vanishes identically. The Fourier expansion

\[
|\cos t|={2\over\pi}
+{4\over\pi}\sum_{n\ge1}{(-1)^n\over1-4n^2}\cos(2nt)
\tag{154.10}
\]

has nonzero coefficient in every nonconstant projective Fourier mode. Thus the
projective cosine transform is injective on finite measures. Since `mu_out` has total
mass `pi`,

\[
\boxed{\mu_D^{out}\Rightarrow d\theta.}
\tag{154.11}
\]

In particular, for any fixed finite set of limiting projective directions, the
normalized number of outer endpoint occurrences in shrinking neighborhoods of those
directions tends to zero when the source limit is taken first and the neighborhoods
are shrunk second.

## 154.2 Atomic train directions require bounded-face endpoint capacity

Continue under (154.4). Pass further so `T/D->x` and the empirical train-direction
probability measures converge to `mu`, whose total atomic mass is `sigma`.

Fix `epsilon>0`. Choose finitely many atoms carrying mass at least `sigma-epsilon`.
Choose pairwise disjoint small projective arcs `U` around them with `mu`-null
boundaries and with total non-atomic `mu` mass at most `epsilon`. Then, for all large
sources,

\[
\#\{\tau:[u_\tau]\in U\}
\ge(\sigma-2\epsilon)T.
\tag{154.12}
\]

Every stopped train has two terminal face-side occurrences and both have the train's
projective contact direction. By (154.11), after taking the source limit and then
shrinking the fixed arcs, the number of outer endpoint occurrences in `U` is `o(D)`.
All remaining endpoint incidences in `U` must therefore be absorbed by bounded
nonquadrilateral faces. Their exact endpoint capacity is `Q+4f` by (154.2). Hence

\[
2(\sigma-2\epsilon)T\le Q+4f+o_U(D).
\tag{154.13}
\]

Divide by `D`, take the source limit, shrink `U`, then let `epsilon->0`:

\[
\liminf {Q+4f\over D}\ge2x\sigma.
\tag{154.14}
\]

Using (154.3),

\[
\boxed{
\liminf {Q+4f\over D}\ge4s_2.
}
\tag{154.15}
\]

Every bounded nonquadrilateral face has degree at least five, so `f<=Q` and therefore
`Q+4f<=5Q`. Thus

\[
\boxed{
\liminf {Q\over D}\ge{4\over5}s_2.
}
\tag{154.16}
\]

Finally (154.1), (154.4), and `P_F/D->pi` give

\[
\boxed{
\liminf {q-k\over D}
\ge {\pi\over2}+{2\over5}s_2
=1.9517214495404795\ldots .
}
\tag{154.17}
\]

### Theorem 154.A — outer-geodesic atomic endpoint capacity

Every Type-II survivor subsequence in the audited-working §142 scope satisfying
`(b-P_F)/D->0` obeys (154.15)--(154.17).

This theorem is occurrence-safe. A singleton train contributes its two physical
face-side occurrences; a bridge may contribute two outer occurrences. No train-to-
face injection is required.

## 154.3 The formal §146 endpoint is impossible

The audited-working §146 consequence can be written

\[
\liminf\left({q-k\over D}-{k\over9D}\right)\ge C_{146}.
\tag{154.18}
\]

Assume for contradiction that a Type-II survivor sequence satisfies

\[
{q-k\over D}\to C_{146}.
\tag{154.19}
\]

Because `k>=0`, (154.18) forces

\[
{k\over D}\to0.
\tag{154.20}
\]

The same audited §146 chain supplies

\[
{q-k\over D}+4{f\over D}
\ge4s_2+{k\over D}-o(1)
\tag{154.21}
\]

and

\[
{Q\over D}\le2{q-k\over D}-\pi+o(1).
\tag{154.22}
\]

The identity

\[
s_2-{C_{146}\over4}=2C_{146}-\pi
\tag{154.23}
\]

and `f<=Q` squeeze both normalized quantities to

\[
{f\over D},{Q\over D}
\to r_{146}:=2C_{146}-\pi
=0.49743442236909585\ldots .
\tag{154.24}
\]

Then (154.1) gives `b/D->pi`. Since Type II also gives `P_F/D->pi` and always
`b>=P_F`,

\[
{b-P_F\over D}\to0.
\tag{154.25}
\]

Theorem 154.A applies and forces

\[
\liminf {q-k\over D}
\ge1.9517214495404795\ldots>C_{146},
\]

contradicting (154.19).

### Theorem 154.B — §146 endpoint exclusion

There is no unbounded audited-working Type-II survivor sequence with

\[
{q-k\over D}\to C_{146}.
\tag{154.26}
\]

Equivalently, the formal smallest §146 density endpoint cannot be attained.

A qualitative positive separation follows in the sequence/diagonal sense. If there
were Type-II survivor sequences with limiting `(q-k)/D` values approaching
`C_146`, choose a diagonal sequence with Type-II normalized container errors tending
to zero and `(q-k)/D->C_146`; Theorem 154.B forbids it. No finite explicit inequality
of the form `q-k>=(C_146+eta)D-C` and no numerical value of `eta` is asserted here.

## 154.4 Hostile checks and surviving obstruction

The load-bearing points were independently rechecked.

1. **Repeated outer walk.** The convex hull of the occurrence-counted outer-walk image
   is exactly `F`; repetitions only increase projection variation.
2. **Cosine-transform injectivity.** Every nonconstant projective Fourier coefficient
   of `|cos|` is nonzero, so constant cosine transform with fixed mass forces uniform
   Lebesgue measure.
3. **Order of limits.** Atomic neighborhoods are finite and fixed before the source
   limit; they are shrunk only afterward. No interchange of `D->infinity` and window
   width `->0` is used.
4. **Endpoint incidence.** The exact multigraph identity `2T=b+Q+4f` counts physical
   face-side occurrences, including singleton trains and bridge repetitions.
5. **Factors of two.** `x sigma>=2s_2` and two endpoints per atomic train give
   `Q+4f>=4s_2 D-o(D)`.
6. **Zero detour.** It is never assumed globally. It is a theorem hypothesis in
   Theorem 154.A and follows from the §146 equality squeeze in Theorem 154.B.
7. **Source scope.** Contact-isolated source points are retained; no full-source
   Section-57 affine-kernel extension is used.
8. **Rejected geometry.** No inward-pocket/exterior-Reuleaux-cap containment or other
   withdrawn cyclic shortcut is used.

The theorem does not close Type II away from the endpoint. A genuine survivor may
retain linear outer-walk detour `b-P_F`; that detour can host atomic train endpoints.
The next closing target is an all-regime quantitative charge of atomic outer endpoint
mass to `b-P_F`, composed with the canonical §122 aggregate harmonic-detour floor and
the normalized §§134--140 payment chain.

The macroscopic inactive-container branch remains open.
