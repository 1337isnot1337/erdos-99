<!-- theorem-state: {"artifact_id":"ART-5E0F561236A8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — mixed-surplus/difference-body coupling

**Date:** 2026-09-11  
**Run type:** Target C C-II closing attempt / exact branch coupling  
**Status:** `STILL OPEN`  
**Promotion:** report only; no route-map theorem status is changed

## Result

This note couples the all-phase renormalized-surplus inequality with the
post-ZF difference-body inequality.  The coupling is useful specifically in the
linear-(s_Z) subbranch of the mandatory branching alternative; it is not a Level I
closure.

Write

\[
 \mu_D=\frac{e_{BB}+2s_C-3(d_H+s_Z)}D,
 \qquad y_D=\frac hD,
 \qquad p_D=\frac{P_F}{D}.
\]

Let \(\rho\) be the positive solution of \(\rho=\cos\rho\), and let

\[
 c_* \text{ be the positive solution of }
 c_* = \cos(3c_*/2),
 \qquad c_*=0.6099043189\ldots .
\]

The post-ZF train/difference-body theorem gives, after passing to a subsequence if
needed,

\[
 \liminf \frac{2h-q}{D}\ge c_* .
\tag{1}
\]

Since \(2h-q=x_B+Q+2s_Z\), the elementary three-way split has an infinite
subsequence in one of three branches; the branch treated here is

\[
 \liminf \frac{s_Z}{D}\ge \sigma_0:=\frac{c_*}{6}
 =0.1016507198\ldots .
\tag{2}
\]

In that branch, every post-ZF subsequential limit satisfies

\[
 \boxed{\liminf\mu_D\ge 0.60727\ldots}
\tag{3}
\]

and therefore

\[
 \boxed{
 \liminf\frac{e_{BB}+2s_C}{D}
 \ge 0.60727\ldots+3\sigma_0
 =0.91222\ldots .}
\tag{4}
\]

The numerical values in (3)--(4) are only evaluations of the exact monotone
functions below.  The conclusion is a necessary lower bound, not an upper bound and
not a contradiction.

## Proof

Let

\[
 a_D=\arcsin\frac1{2D}.
\]

The difference body of the force hull contains the centrally symmetric polygon formed
by the actual diameter directions.  The exact perimeter minimization over their
projective gaps gives

\[
 Q+2s_Z
 \le h+1-2D\cos((h-1)a_D).
\tag{5}
\]

Because \(Q\ge0\), any subsequence with \(s_Z/D\to\sigma\) and \(h/D\to y\)
satisfies

\[
 2\sigma\le y-2\cos(y/2).
\tag{6}
\]

The function on the right is strictly increasing on \([0,\pi]\).  Thus, if
\(\sigma\ge\sigma_0\),

\[
 y\ge y_0,
 \qquad
 y_0-2\cos(y_0/2)=2\sigma_0.
\tag{7}
\]

For the value in (2),

\[
 y_0=1.5980867220\ldots .
\tag{8}
\]

The all-phase cavity calculation supplies, for every subsequential limit
\((\mu,y,p)\),

\[
 A_*(y,p)-\frac\pi4\mu^2
 \le \frac{(\mu+p/2)^2}{4\pi},
\tag{9}
\]

where

\[
 A_*(y,p)=\max\left\{
 \frac{y+\sin y}{4},
 \frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2
 \right\},
\tag{10}
\]

and the exact domain is

\[
 2\rho\le y\le p\le\pi,
 \qquad p\le2y.
\tag{11}
\]

For fixed \(y\), let \(R(y,p)\) be the least nonnegative \(u\) for which (9)
holds with \(\mu=u\).  The same derivative calculation used in the all-phase
renormalization theorem shows that for \(y\ge y_R\), where

\[
 y_R=1.5100171437\ldots
\]

solves

\[
 \frac{y+\sin y}{4}
 =\frac\pi{(\pi-2)^2}(y-1)^2,
\tag{12}
\]

the minimum over the allowed perimeter variable is attained at the crossover

\[
 p_e(y)=2+2\sqrt{
 \frac{(y+\sin y)/4}{\pi/(\pi-2)^2}}
\tag{13}
\]

and this minimized root is strictly increasing in \(y\).  Since (8) is larger than
\(y_R\), (7)--(13) give

\[
 \mu\ge R(y_0,p_e(y_0))
 =0.6072748575\ldots .
\tag{14}
\]

This proves (3).  Finally, by definition of \(\mu_D\),

\[
 \frac{e_{BB}+2s_C}{D}
 =\mu_D+3\frac{d_H+s_Z}{D}
 \ge\mu_D+3\frac{s_Z}{D},
\]

which, with (2) and (14), proves (4).  \(\square\)

## What this does and does not remove

The coupling eliminates no full branch.  It gives the following sharpened ledger:

| subbranch | proved consequence | still missing |
|---|---|---|
| (x_B\ge c_*D/3) | linear outer-walk excess | a source-specific upper tradeoff or strict competitor |
| (Q\ge c_*D/3) | linear exceptional-face defect | control of internal face currency without discarding exceptional faces |
| (s_Z\ge c_*D/6) | (h/D\ge1.59808\ldots), (mu\ge0.60727\ldots), and (L/D\ge0.91222\ldots) for (L=e_{BB}+2s_C) | no upper bound on (L), and no support-to-motion theorem for the omitted rows |

The last numerical lower bound does not cross one.  Even a bound crossing one would
not by itself contradict a global minimizer, because (L) is a lower-bound currency,
not a quantity known to satisfy (L<D).

The same obstruction is visible in the exact stress-polytope interpretation.  If
ZF and the full-support KKT theorem are invoked, (s_Z) is the affine dimension of
the normalized stress polytope.  An extreme stress omits at least (s_Z) actual
rows, but an omitted row can remain geometrically strong under another stress; the
lexicographic active-face theorem therefore supplies no release.  The missing
implication is still a genuine support-to-motion or global-population theorem.

## Regression audit

- The cyclic (s_Z=0) branch is not touched; regular odd shells remain admissible to
  this calculation.
- The forest (s_Z=0) branch is not touched; its (3d_H) charge remains an upper-
  tradeoff problem.
- Contact-isolated source points are retained: the derivation uses only the loaded
  force hull and the full-source definition of (D), and does not delete isolates.
- No hull saturation is imposed together with the secondary diameter-pair minimum.
- The (s_Z>0) conclusion is conditional on the report-level ZF/ZK and all-phase
  cavity stack; it is not promoted to the canonical route map.

## Exact next obstruction

To settle C-II, one still needs at least one of:

\[
 \sum_r(\delta_r+r_r)+s_B<u_\pi D-o(D),
\]

for the high-defect population branch; a common-2-connected-hub response/bypass
inequality in the forest branch; a finite feasible release/competitor from the
linear-(s_Z) support omission; or a global source-capacity theorem excluding a
quadratic population of contact-isolated points.  None follows from (1)--(14).

## A precise obstruction to the common-hub response route

The surviving common contact block cannot be treated as a bridge with a uniformly
positive transfer.  The multi-edge analogue is false even for an exact
circular-planar penny graph.

Take the six vertices of a regular hexagon with side length one.  Its positive
contact graph is the six-cycle, and its three opposite pairs are the three crossing
diameter chords.  With unit conductances on the contact cycle, the response kernel
on the oriented pairs

\[
 (0,3),\quad(1,4),\quad(2,5)
\]

is, by solving the cycle Laplacian with zero-sum normalization,

\[
 K=
 \begin{pmatrix}
  3/2&1/2&-1/2\\
  1/2&3/2&1/2\\
  -1/2&1/2&3/2
 \end{pmatrix}.
\tag{15}
\]

Thus a 2-edge-connected common block can have a negative off-diagonal transfer.
The bridge proof cannot be extended by replacing a bridge resistance with an
effective multi-edge-cut resistance.  The example is not a C-II counterexample: it
is finite and does not satisfy the large-source ZF/global-optimality hypotheses.  It
does, however, falsify the exact local implication needed by a hub-only response
closure and identifies the additional ingredient such a theorem would have to use.
