> Generated reading edition · [exact source](../../../docs/reports/target_c_large_near_triangular_fixed_wall_lock_2026-10-05.md) · source SHA-256 `d75246ed131d5a7a59765aee5e58882a2b55cdb34979555ea7154d92acbc6be1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A984E31FFD6D","canonical":false,"claim_ids":["C-LARGE-WALL-LOCK-REGRESSION"],"claim_statuses":{"C-LARGE-WALL-LOCK-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C — arbitrarily large near-triangular unit walls can forbid every strict refill

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Run checkpoint:** 364d63fd. **State:** 2026-09-14.audit.51.
**Classification:** registered regression in `2026-10-05.audit.54` as `C-LARGE-WALL-LOCK-REGRESSION`. **LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Mechanism killed and precise limits

Quadratic population behind a linear unit-contact wall, positive pinned
equilibrium, arbitrarily small angle excess and nearly unit hidden
diagonals do not guarantee a strict refill of the same population.
The obstruction survives at arbitrarily large patch sizes, beyond the
earlier one-interior-point wall example.

The configurations below are capacity-optimal in their **fixed convex
containers**. Their global minimum-diameter optimality is neither asserted
nor inferred. They have no certified actual diameter loads and do not
have a Type-II disk force hull. Thus this is not a negative settlement
of Erdős #99 or a regression against the canonical full-core exclusion.

The exact failed implication is

$$
\text{unit wall + quadratic population + positive pinned stress + near-triangular bulk}
\ \not\Longrightarrow\ \text{strict same-cardinality fixed-wall refill}.
$$

A source theorem must use additional actual minimum-diameter information,
a movable interface, a sufficient quantified angle/area excess, or
specific defects absent from these grids.

## 2. Actual unit-separated grids

Let $m,n\ge2$, $u=(1,0)$,
$v_\phi=(\cos\phi,\sin\phi)$, with
$\pi/3<\phi<\pi/2$. Define

$$
X_{m,n}(\phi)=\{iu+jv_\phi:0\le i\le m,\ 0\le j\le n\},
\quad K_\phi=\operatorname{conv}X_{m,n}(\phi).
$$

The fixed wall $W_\phi$ consists of the points with $i\in\{0,m\}$
or $j\in\{0,n\}$. Its consecutive edges all have unit length. There
are $2(m+n)$ wall points and $(m-1)(n-1)$ interior points.

The exact contacts are $\pm u,\pm v_\phi$ steps. To check this, for
integer coefficients $a,b$,

$$
|au+bv_\phi|^2=a^2+b^2+2ab\cos\phi.
$$

If $ab\ge0$, every nonbasis step has squared length greater than one.
If $ab<0$, writing $r=|a|,s=|b|\ge1$,

$$
r^2+s^2-2rs\cos\phi>r^2+s^2-rs
=(r-s)^2+rs\ge1.
$$

Thus the complete contact graph is the bipartite rectangular grid and
contains no unit triangle. Its hidden $u-v_\phi$ diagonals tend to
unit length as $\phi\downarrow\pi/3$. Giving every contact weight one
makes every interior vertex exactly equilibrated with positive weights.
The boundary is pinned, rather than falsely assigned diameter forces.

## 3. An explicit displacement gap for every fixed-wall alternative

Label the wall points at their original positions. Consider any labelled
unit-separated configuration $p'_{ij}$ with that wall unchanged and
the same number of interior points. Write
$\delta_{ij}=p'_{ij}-(iu+jv_\phi)$ and
$\rho=\max_{ij}|\delta_{ij}|$.

For every horizontal original contact, unit separation gives

$$
u\cdot(\delta_{i+1,j}-\delta_{ij})
\ge-\frac12|\delta_{i+1,j}-\delta_{ij}|^2
\ge-2\rho^2.
$$

Sum from the fixed left boundary to $(i,j)$, and separately to the
fixed right boundary. The resulting bounds are

$$
-2i\rho^2\le u\cdot\delta_{ij}\le2(m-i)\rho^2.
$$

Similarly
$-2j\rho^2\le v_\phi\cdot\delta_{ij}\le2(n-j)\rho^2$.
The dual basis to the two unit vectors has vector lengths
$1/\sin\phi$, so

$$
|\delta_{ij}|
\le\frac{|u\cdot\delta_{ij}|+|v_\phi\cdot\delta_{ij}|}{\sin\phi}
\le\frac{2(m+n)}{\sin\phi}\rho^2.
$$

Taking a maximizing point proves the global implication

$$
\boxed{\rho=0\quad\text{or}\quad
\rho\ge\frac{\sin\phi}{2(m+n)}
\ge\frac{\sqrt3}{4(m+n)}.}
\tag{L.1}
$$

No infinitesimal-rank inference is used: (L.1) checks the finite lower
constraints directly. The same gap holds at $\phi=\pi/3$. The
configuration need not remain a bar realization or retain any old contact.
It only has to retain the original wall and all lower separations.

## 4. The triangular-limit packing with this wall is unique

At $\phi_0=\pi/3$, the container has

$$
A(K_{\phi_0})=a_0mn,\quad P(K_{\phi_0})=2(m+n),
\quad N=(m+1)(n+1)=mn+m+n+1.
$$

Any $N$-point unit-separated packing in $K_{\phi_0}$ attains
equality in $N\le A/a_0+P/2+1$.
The two-dimensional Groemer equality case says its source-point convex
hull is the container and can be triangulated by unit equilateral
triangles using its source points. Connected triangles across shared
edges belong to one triangular lattice.

For a packing containing the prescribed wall, $0,u$ are prescribed
unit neighbors and fix that lattice to
$\mathbb Z u+\mathbb Z v_{\phi_0}$. Its points in the container are
exactly the $(m+1)(n+1)$ points of $X_{m,n}(\phi_0)$. All must
be used. The pinned packing is unique as an unlabelled set.

**External source check.** The equality statement is the reliable
transcription on page 2 of K. J. Böröczky and I. Z. Ruzsa,
[*Note on an Inequality of Wegner*](https://users.renyi.hu/~carlos/wegner.pdf),
author manuscript dated January 2, 2007; publication DOI
`10.1007/s00454-006-1277-4`. The authors state it for nonoverlapping unit
disks, whose centers are separated by two. Dividing their coordinates
by two gives precisely the normalization above. The author PDF was
retrieved and its page 2 read during this run. No disk-diameter equality
uniqueness from Rogalski–Saint Raymond is used.

## 5. A positive angle window with no alternative full packing

**Theorem L.2.** For each fixed $m,n\ge2$, there is
$\epsilon_{m,n}>0$ such that, for
$0<\phi-\pi/3<\epsilon_{m,n}$, every $N$-point unit-separated
packing in $K_\phi$ containing $W_\phi$ equals $X_{m,n}(\phi)$.

Suppose otherwise. Take positive angle excesses tending to zero and
different full packings. Their finite source populations lie in a common
compact region. Pass to a subsequence. Unit separation keeps every
limit point distinct; the limit contains the prescribed triangular wall.
Section 4 makes the limit exactly the triangular grid. After permuting
the interior labels, the alternative points therefore approach the
corresponding original grid points. Their $\rho$'s tend to zero.

But each $\rho$ is nonzero and obeys the uniform positive lower
bound $\sqrt3/[4(m+n)]$ in (L.1). Contradiction. This proves the
angle window. It is not claimed effective or uniform in patch size.

The unique grid retains interior unit contacts, so its interior
population cannot be repacked with all mutual/wall distances strictly
greater than one. This prohibits **every** strict refill, including a
far rearrangement, throughout the stated window.

Choosing $m=n\to\infty$ and a positive excess below each corresponding
window gives triangle-free examples with quadratic interior population
behind linear unit-wall size. The point sets are not being offered as
minimum-diameter sources. Their positive pinned equilibrium and exact
unit wall do not supply that missing hypothesis.

## 6. Explicit capacity-optimal containers without an unknown window

For an explicit algebraic family, put

$$
t=\frac1{100mn(m+n)},\qquad
\phi=\frac\pi3+2\arctan t.
$$

Then $u,v_\phi$ have coordinates in $\mathbb Q(\sqrt3)$. The Oler
residual of the grid in its parallelogram is

$$
r=mn\left(\frac{\sin\phi}{a_0}-1\right)>0.
$$

Writing $\delta=2\arctan t$,

$$
\frac{\sin\phi}{a_0}-1
=\cos\delta-1+\frac{\sin\delta}{\sqrt3}<2t,
\qquad
0<r<\frac1{50(m+n)}<1.
$$

Oler therefore forbids $N+1$ points anywhere in $K_\phi$, while
the triangle-free grid supplies $N$. These containers have exactly
capacity $N$. This explicit family has no spare slot even without
retaining its wall. Its displayed angle is **not** asserted to lie in
the unknown uniqueness window of Theorem L.2.

## 7. Exact checks, prior art and consequence for the live attack

[The finite verifier](../../../research/verify_target_c_large_near_triangular_wall_lock_2026_10_05.py)
checks 3,404 actual source pairs in eight quadratic-field grids, exact
triangle-free contact support, positive interior equilibrium, full pinned
rank on 82 interior points, residual formulas and 265 telescoping/radius
arithmetic checks. It also checks 1,444 exact residual floors for the
explicit capacity-optimal family. No finite sample is claimed to certify
the compactness angle window.

The earlier
[embedded-grain wall report](target_c_embedded_grain_wall_replacement_2026-10-02.md)
already gives a unique-center obstruction for a fixed two-face wall,
and a successful strict refill for sufficiently square seven-step walls.
The present regression extends the obstruction to arbitrary patch size
and to arbitrarily near-triangular walls. It preserves the successful
square-wall certificate at its stated scope.

The new disjoint terminal-pentagon bank does have physical defects not
present in these pure grids. A closing replacement must spend those
defects or actual diameter loading. It cannot discard them and apply a
universal large-grid strict-refill assertion. The high-degree, nonunit
hull and macroscopic inactive-source alternatives likewise still need
their own source argument.
