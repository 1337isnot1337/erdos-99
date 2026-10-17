> Generated reading edition · [exact source](../../../docs/reports/target_c_inactive_cloud_global_competitor_2026-09-11.md) · source SHA-256 `404571b9e0a792d0d179e6f2bc51136bbfc6bcf37635b1f42e77983fc01e86b8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3B08CE62F4DD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_inactive_cloud_global_competitor_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=8540ebd929c44a582f55cd67ed9d75bcc5959082; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — the inactive expanded-lattice shell regression is not globally optimal

**Date:** 2026-09-11
**Status:** new proved theorem, hold report
**Target:** C-II strict-negative response regressions with contact-isolated bulk

## Statement

The regular-polygon-plus-cloud configurations used in the strict-negative response
regressions are not global minimum-diameter configurations once the polygon order is
large. More precisely, let $D\to\infty$, put $R=D/2$, and let $2k$ be chosen so
that a regular $2k$-gon of circumradius $R$ has side length one. Let

$$
s=1+D^{-1},
$$

and let $N_D$ be the number of points in a triangular lattice of nearest-neighbor
spacing $s$ lying in $B(0,R-2)$. Form a source by adjoining those $N_D$ points
to the $2k$ polygon vertices, as in the earlier shell regressions. Then, for all
sufficiently large $D$, there is a unit-separated $N_D+2k$-point configuration
of diameter strictly smaller than $D$. Consequently the shell-plus-cloud family
cannot be a global minimizer for its cardinality.

The proof is a finite global competitor, not an asymptotic density comparison.

## Proof

Let

$$
\Delta={2\over\sqrt3},
\qquad a_0={1\over\Delta}={\sqrt3\over2}.
$$

For a triangular lattice of spacing $t$, the Voronoi cells are regular hexagons of
area $a_0t^2$ and circumradius $t/\sqrt3$. The Voronoi cells give, for every
$r>t/\sqrt3$, the upper bound

$$
M_t(r)\le {\Delta\pi\over t^2}(r+t/\sqrt3)^2.
\tag{1}
$$

For the lower bound used below, average translates of a unit triangular lattice over
one fundamental cell. The mean number of lattice points in a disk of radius $r$ is
exactly $\Delta\pi r^2$, so some translate contains at least

$$
\left\lfloor\Delta\pi r^2\right\rfloor
\tag{2}
$$

points in that disk. This translation-average argument has no boundary-error term.

Apply the upper bound in (1) with $t=s$ and $r=R-2$. The number $N_D$ of
cloud points obeys

$$
N_D\le {\Delta\pi\over s^2}
\left(R-2+{s\over\sqrt3}\right)^2.
\tag{3}
$$

The polygon relation is

$$
D={1\over\sin(\pi/(2k))},
$$

so $2k/D\to\pi$. Since $R=D/2$ and $s=1+D^{-1}$, expansion of (3) gives

$$
N_D+2k
\le
\Delta\pi R^2-
\Delta\pi
\left(\frac52-\frac1{\sqrt3}-\frac1\Delta\right)D+O(1).
\tag{4}
$$

Indeed,

$$
{1\over s^2}\left(R-2+{s\over\sqrt3}\right)^2
=R^2-\left(\frac52-\frac1{\sqrt3}\right)D+O(1),
$$

and $2k=\pi D+O(D^{-1})=\Delta\pi D/\Delta+O(D^{-1})$.

Now use the translation-average bound (2) for a unit triangular lattice in the disk
of radius $R-1$. The resulting count is at least

$$
\Delta\pi(R-1)^2-1
=\Delta\pi R^2-\Delta\pi D+O(1).
\tag{5}
$$

The coefficient comparison with (4) is strict. Put

$$
B=\frac52-\frac1{\sqrt3}-\frac1\Delta.
$$

Since $1/\Delta=\sqrt3/2$,

$$
B-1=\frac32-\frac1{\sqrt3}-\frac1\Delta
=\frac{9-5\sqrt3}{6}>0.
\tag{6}
$$

The last inequality follows from $81>75$. Equations (4)--(6) imply that the count
in (5) is greater than $N_D+2k$ for all sufficiently large $D$.

Select any $N_D+2k$ of these lattice points. Their mutual distances are at least
one, and their diameter is at most

$$
2(R-1)=D-2<D.
$$

This is a strict same-cardinality diameter improvement, proving the theorem.
$\square$

## A general buffered-source competitor

The same calculation gives a configuration-independent criterion. Let $A$ be any
unit-separated source of diameter $D$, put $R=D/2$, and suppose that for some
center $o$, constants $a,b>0$, and $C$,

$$
\bigl|A\setminus B(o,R-a)\bigr|\le bD+C.
\tag{7}
$$

If

$$
a>{\sqrt3\over4}+{b\sqrt3\over2\pi},
\tag{8}
$$

then $A$ is not a diameter minimizer for its cardinality once $D$ is large.

Indeed, Oler's finite packing inequality applied to the points of $A$ inside
$B(o,R-a)$ gives

$$
|A\cap B(o,R-a)|
\le
\Delta\pi(R-a)^2+\pi(R-a)+1.
\tag{9}
$$

On the other hand, translation averaging gives a unit triangular lattice translate
with at least $\lfloor\Delta\pi(R-c)^2\rfloor$ points in a disk of radius $R-c$,
for every fixed $c>0$. Choose $c>0$ so small that

$$
c<a-{\sqrt3\over4}-{b\sqrt3\over2\pi}.
$$

Combining (7) and (9), the lattice count exceeds $|A|$ by

$$
\left(\Delta\pi(a-c)-{\pi\over2}-b\right)D+O(1),
$$

which is positive for all sufficiently large $D$. Selecting $|A|$ lattice points
inside that disk gives diameter $D-2c<D$, a contradiction.

For the shell-plus-cloud family, take $a=2$ and $b=\pi+o(1)$, since
$2k/D\to\pi$. The right side of (8) is

$$
{\sqrt3\over4}+{\sqrt3\over2}={3\sqrt3\over4}<2,
$$

so the general criterion already supplies a strict global competitor. The more exact
count above records the stronger margin for this particular family.

## Scope and exact effect

The theorem removes the explicit family in which a regular even or odd polygon is
combined with a cloud of spacing $1+D^{-1}$ placed two units inside the polygon's
diameter disk. It supplies the missing global-optimality certificate in that
negative-transfer regression: the displayed diameter is not $D(n)$.

It does **not** prove that every isolate-heavy triangle-free configuration is
nonoptimal. The argument uses the two-unit radial margin and the exact boundary
population $2k\sim\pi D$. An arbitrary global minimizer may have contact-isolated
points distributed through a different container, with a different second-order
boundary count. The unresolved C-II source-capacity problem is precisely to control
those arbitrary configurations.

It also does not affect the regular polygon alone, which has only $O(D)$ points, or
the strict-negative response sign calculation. Those local response regressions
remain valid.

## Regression checks

- The competitor has the required minimum separation because it is a subset of a
  unit triangular lattice.
- Its diameter is strictly smaller, not merely no larger.
- The comparison counts the $2k$ shell vertices; they are not discarded.
- No assertion is made that the competitor preserves the original contact graph or
  diameter graph. A global competitor is allowed to relocate all points.
- The proof is independent of the unpromoted C56 kernel-collapse package and does not
  alter the C-II branch ledger.

## Remaining obstruction

The response branch still has arbitrary global minimizers whose contact-isolated
population is not known to occupy a two-unit-inset lattice cloud. To close C-II one
still needs a source-preserving capacity theorem or a strict competitor for that full
class, together with the cyclic, forest, and $s_Z>0$ branches.
