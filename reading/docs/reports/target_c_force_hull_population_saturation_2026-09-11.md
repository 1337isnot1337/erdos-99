> Generated reading edition · [exact source](../../../docs/reports/target_c_force_hull_population_saturation_2026-09-11.md) · source SHA-256 `18fd81eba2ac2b961379c0642a9561edec39c3273f73eea601df8dab28dda007`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-5962F2BAE078","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_force_hull_population_saturation_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=17a0f7f78b20e714d5d0297afd9b21e4cef3380c; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — force-hull population saturation

**Date:** 2026-09-11
**Target:** Target C, C-II
**Status:** new proved theorem, hold report
**Dependencies:** C65 full diameter visibility, C67 force-hull area floor, the promoted annular Voronoi capacity theorem AV, Oler's finite inequality, and the strict translated-lattice comparison

## Statement

Let (A) be the C65 lexicographically selected triangle-free source, let
(D=\operatorname {diam}A), let (K=\operatorname {conv}A), and let (F) be the
force hull of the relative-interior positive contact stress. Put

```math
N_F:=|A\cap F|,\qquad Z_{\rm ext}:=|A\setminus F|,\qquad
A_F:=\operatorname {area}F.
```

The source points in (A\cap F) are the full population in the force hull. They are
not assumed to lie in the positive contact core.

For every sufficiently large C-II source,

```math
\boxed{a_0N_F>A_F-2\pi D-\pi+a_0,}
\tag{FH.1}
```

where (a_0=\sqrt3/2). Oler gives the opposite boundary-order inequality

```math
\boxed{a_0N_F\le A_F+c_0\operatorname {per}F+a_0,}
\tag{FH.2}
```

with (c_0=\sqrt3/4). Consequently

```math
\boxed{|a_0N_F-A_F|=O(D).}
\tag{FH.3}
```

Thus the entire source population in the force hull, including all contact-isolated
points there, is asymptotically Oler-saturated. This is a population statement; it is
not a statement that the positive contact core contains a quadratic number of points.

There is also a two-sided whole-source form. Oler applied to (Asubset K), together
with the isodiametric and perimeter bounds, gives

```math
a_0n\le \frac{\pi D^2}{4}+c_0\pi D+a_0.
\tag{FH.3a}
```

Combining this with the strict translated-lattice lower bound and (FH.3) yields

```math
\boxed{
a_0n=\frac{\pi D^2}{4}+O(D),
\qquad
a_0Z_{\rm ext}=\frac{\pi D^2}{4}-A_F+O(D).
}
\tag{FH.3b}
```

Thus both the source population in (F) and the source population in the annulus
(K\setminus F) saturate their leading area capacities to boundary order. The
second identity uses (Z_{\rm ext}=n-N_F), not a replacement source or scaffold.

Using the promoted C67 area floor

```math
\liminf_{D\to\infty} A_F/D^2\ge
\frac12\sin(1/4)=0.1237019796\ldots,
```

we obtain the unconditional consequence

```math
\boxed{\liminf_{D\to\infty}N_F/D^2
\ge \frac{\sin(1/4)}{\sqrt3}=0.1428\ldots .}
\tag{FH.4}
```

If the separately audited FSDB force-hull floor is admitted, the same theorem
improves (FH.4) to

```math
\liminf N_F/D^2\ge
\frac{2}{\sqrt3}\frac{2\rho+\sin(2\rho)}4
=0.714148\ldots,
\qquad \rho=\cos\rho.
\tag{FH.5}
```

The proof of (FH.1)--(FH.4) uses only promoted inputs. Equation (FH.5) is an
additional consequence of the unpromoted FSDB report and is labelled accordingly.

## Proof

The strict translated-lattice comparison for a diameter minimizer is

```math
a_0(n-1)>\frac{\pi D^2}{4}.
\tag{1}
```

The external source set (A\setminus F) is contained in
(K\setminus\operatorname {int}F), and remains unit-separated. The promoted AV
theorem therefore gives

```math
a_0Z_{\rm ext}
\le A_K-A_F+P_K+P_F+\pi,
\tag{2}
```

where (A_K=\operatorname {area}K) and (P_K,P_F) are the two perimeters.
Subtracting (2) from (1), with (N_F=n-Z_{\rm ext}), gives

```math
a_0N_F>
\frac{\pi D^2}{4}+a_0-A_K+A_F-P_K-P_F-\pi.
\tag{3}
```

The isodiametric inequality gives (A_K\le\pi D^2/4), and Cauchy's
perimeter-diameter inequality gives (P_K,P_F\le\pi D). Equation (3) therefore
implies (FH.1).

Oler's finite inequality applied to the unit-separated set (A\cap F\subset F) gives

```math
a_0N_F\le A_F+c_0P_F+a_0,
```

which is (FH.2). The lower bound (FH.1) and this upper bound differ from (A_F) by
at most a constant times (D), proving (FH.3). In particular (FH.1) gives

```math
N_F\ge A_F/a_0-O(D).
\tag{4}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
Oler applied to all of (A\) in (K) gives (FH.3a), while (1) gives its matching
boundary-order lower bound. Subtracting (FH.3) from this two-sided whole-source
estimate proves (FH.3b).
```



Inserting C67 into (4), and using (1/a_0=2/\sqrt3), proves (FH.4). Inserting the
finite FSDB estimate instead proves (FH.5) after division by (D^2). No
contact-isolated source point was removed in any step. (square)

## Exact effect on C-II

This theorem removes one weak form of the isolate escape: the force hull cannot contain
only a subquadratic number of source points. More strongly, its full source population
has the same leading density as the force-hull area.

It does not imply that the positive contact core is quadratic. The remaining possible
configuration is a quadratic population of points in (F) with every distance to the
positive core strictly greater than one. Such a population can have arbitrarily small
positive separation slack, so Oler saturation alone gives no uniform contact or KKT
conclusion.

The unpromoted FSDB floor makes the remaining population statement quantitative. At
its floor, (FH.5) says that at least (0.714148D^2-o(D^2)) source points lie in (F),
while the force-visible core may still be smaller. This is exactly the source-specific
gap that a valid inactive-cloud competitor or a core-to-source transport theorem must
address.

## Regression audit

- Contact-isolated points inside (F) are counted in (N_F); they are not treated as
  force-visible points.
- Points outside (F) are handled by AV as an annular unit-separated set.
- No hull saturation is imposed on the C65 secondary representative.
- The regular odd-shell plus cloud regression is compatible with FH.3: a nearly
  triangular inactive cloud can be Oler-saturated without being a positive contact
  core. Its separate global competitor does not prove the general case.
- The theorem uses no (s_Z=0) identity, so it applies to cyclic, forest, and
  (s_Z>0) branches whenever C65/C67 apply.

## Remaining obstruction

FH.3 supplies the missing population scale but not the missing contact transport. To
close C-II one still needs one of:

1. a theorem that a force-hull population with Oler slack (O(D)) and a quadratic
   positive-contact subcore must contain a unit equilateral triangle;
2. a source-preserving reduction that converts a quadratic inactive population into a
   valid smaller-diameter competitor; or
3. a second-order packing inequality whose strict deficit exceeds the remaining
   (O(D)) interface terms.

The new theorem advances the source-capacity ledger but does not settle the global
problem.
