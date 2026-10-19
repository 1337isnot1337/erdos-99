# Rotating a full rhombic source wall does not create capacity

**Status:** unreviewed exact geometric regression. It is not a canonical theorem
or a result about every global minimizer. **Date:** 2026-10-18. **Source main:**
`7d0a450fe66991036541023f95c44c064a04b6a8` (tree
`db766e0e25b562054df26aeec7e627d5a579dd6d`). **Theorem state:**
`2026-10-15.publication.2`; **priority:** `public-frontier.3`;
**catalogue:** `public-frontier.9`. **Task:**
`frontier-target-c-macroscopic-container-capacity-20261018`.

Prepared with OpenAI Codex (GPT-6 Luna xhigh). The originating agent produced
the proof reconstruction and exact checker. No independent mathematical audit
has occurred. This package is offered under Apache-2.0. It uses no copied
third-party material.

## Question, quantity, and candidate implication

Can rotating one specified generator wall, while moving the full labelled source
coherently, convert large Oler slack into at least one point that is at distance
at least one from every moved source label?

The exact quantity is the full-source strict-safe insertion capacity
\[
\mathcal C(A,K)=\{x\in K:|x-a|\ge1\text{ for every }a\in A\}.
\]
If nonempty, it supplies at least one site for a later population-restoration
argument. The candidate implication tested here is that a feasible moved-wall
path with superlinear Oler slack growth should make \(\mathcal C\) nonempty.
The theorem below refutes that implication in the stated family: the entire
moving container stays strictly covered by unit neighborhoods of all retained
labels even while the slack becomes quadratic.

## Exact theorem

For an integer \(m\ge7\), set
\[
d_m=m^2-6m-3,\qquad c_m=\frac{\sqrt{d_m}}{2m},\qquad
s_m=\frac{\sqrt3(m+1)}{2m}.
\]
Then \(c_m^2+s_m^2=1\) and \(0<c_m<1/2\). Let
\[
u=(1,0),\quad v_\theta=(\cos\theta,\sin\theta),\quad
\theta_m=\arccos(c_m),
\]
and for every \(\theta\in[\theta_m,\pi/2]\) define the fully labelled source
and its convex container by
\[
A_{m,\theta}=\{iu+jv_\theta:0\le i,j\le m,\ i,j\in\mathbb Z\},
\qquad K_{m,\theta}=\operatorname{conv}(A_{m,\theta}).
\]
This is a specified motion of the outer \(u\)-parallel wall
\(\{iu+mv_\theta:0\le i\le m\}\), with the opposite \(j=0\) wall fixed
and each intervening labelled row moved by the corresponding fraction of the
same rotation.

For the whole continuous path:

1. Every distinct pair of source labels has distance at least one. The exact
   unit-contact graph is the \((m+1)\)-by-\((m+1)\) rectangular grid, hence is
   triangle-free and includes every label.
2. The actual diameter is
   \[
   D_{m,\theta}=m\sqrt{2+2\cos\theta}
   \le D_{m,\theta_m}=m\sqrt{2+2c_m}.
   \]
   Thus every pair also obeys the original upper bound throughout the motion;
   for \(\theta>\theta_m\) the endpoint is strictly sub-\(D_{m,\theta_m}\).
3. The entire container is strictly covered by unit neighborhoods of the full
   source: \(\mathcal C(A_{m,\theta},K_{m,\theta})=\varnothing\).
4. With \(Q=m^2\sin\theta\), perimeter \(p=4m\), and all-label population
   \(n=(m+1)^2\), the all-label Oler slack is
   \[
   S_{m,\theta}=\frac{Q}{\sqrt3/2}+\frac p2+1-n
   =m^2\left(\frac{2}{\sqrt3}\sin\theta-1\right).
   \]
   It increases from \(S_{m,\theta_m}=m\) to
   \(S_{m,\pi/2}=(2/\sqrt3-1)m^2\). Since \(D_{m,\pi/2}=\sqrt2m\),
   the terminal slack is quadratic in the diameter.

This is an exact counterexample to the moved-wall inference that growing Oler
slack alone supplies a full-source insertion site. It is a source-wide motion,
not a fixed-wall count: all labels are retained and all lower and original
diameter upper bounds are checked.

The population ledger deletes zero labels and restores zero labels: all
\((m+1)^2\) indexed labels remain. The active-contact ledger changes zero
pairs: exactly \(2m(m+1)\) grid edges stay at unit distance throughout. The
full pair formulas above cover every lower constraint and every upper
constraint, including the initial diameter pair.

## Proof

The identity \(d_m+3(m+1)^2=4m^2\) gives
\(c_m^2+s_m^2=1\). For \(m\ge7\), \(d_m>0\) and \(d_m<m^2\), so
\(0<c_m<1/2\).

Write \(c=\cos\theta\). On this path \(0\le c\le c_m<1/2\), and
\(\sin\theta=\sqrt{1-c^2}\) increases as \(\theta\) increases. A label
difference has the form \(au+bv_\theta\), where \(a,b\) are integers with
\(|a|,|b|\le m\), and
\[
|au+bv_\theta|^2=a^2+b^2+2ab c.
\]
If one coordinate is zero, every nonzero difference has length at least one,
with equality only for a unit coordinate step. If \(ab>0\), the squared
length is greater than one. If \(ab<0\), put \(r=|a|\), \(t=|b|\); then
\[
|au+bv_\theta|^2=(r-t)^2+2rt(1-c)>(r-t)^2+rt\ge1.
\]
Therefore only the coordinate steps are unit contacts. Checkerboard parity
\(i+j\pmod2\) bipartitions this exact grid.

The norm-square is convex in \((a,b)\), so its maximum on
\([-m,m]^2\) occurs at a corner. The same-sign corners give the maximum
\(m^2(2+2c)\), which decreases along the path. This proves both the actual
diameter formula and the original upper-pair bound.

Each of the \(m^2\) unit rhombi in \(K_{m,\theta}\) is split along its shorter
diagonal \(u-v_\theta\). Either resulting triangle has circumradius \(R\)
with
\[
R^2=\frac{|u-v_\theta|^2}{4\sin^2\theta}
    =\frac{2-2c}{4(1-c^2)}=\frac1{2(1+c)}\le\frac12<1.
\]
For any point \(x\) in one such triangle with vertices \(w_1,w_2,w_3\),
write its barycentric coordinates as \(\lambda_i\), and let \(o\) be the
circumcenter. The weighted square identity gives
\[
\sum_i\lambda_i|x-w_i|^2=R^2-|x-o|^2\le R^2.
\]
At least one vertex is therefore at distance at most \(R<1\) from \(x\).
The triangles cover the closed container, including its boundary, and all
vertices are source labels. Hence no strict-safe insertion site exists anywhere
in the moved container.

Finally, the parallelogram area is \(m^2\sin\theta\), its perimeter is
\(4m\), and it contains all \((m+1)^2\) labels. Substitution gives the stated
slack formula. The initial identity
\(\sin\theta_m=\sqrt3(m+1)/(2m)\) gives slack \(m\); at \(\pi/2\) the
formula gives the quadratic terminal value.

## Falsification test and exact checker

The theorem would fail if any path angle or any integer difference produced a
pair shorter than one, a pair longer than the initial diameter, or a point in a
cell farther than one from all its vertices. `verify.py` uses exact integer and
quadratic-surd comparisons to enumerate every difference vector for
\(m=7,8,12,24\), checks the diameter equality and slack identities, and checks
the cover-radius bound. It also verifies a negative control: extending the
cosine past \(1/2\) makes \(|u-v|^2<1\), so the path restriction is substantive.
The finite checker corroborates the formulas at those sample sizes; the
continuous-in-\(\theta\), all-\(m\) conclusions follow from the proof above.

Run from the repository root:

```sh
python research-packages/e99-pass-20261018-homelab-05/verify.py
```

## Predecessor comparison and limits

The predecessor [PR #97](https://github.com/1337isnot1337/erdos-99/pull/97)
and its [`target_c_contact_rhombic_grid_linear_oler_zero_capacity_2026-10-17.md`](../../docs/reports/target_c_contact_rhombic_grid_linear_oler_zero_capacity_2026-10-17.md)
prove zero insertion capacity for the starting fixed container with slack
exactly \(m\). This package changes the hypothesis: the generator wall moves
and every full-source label follows a specified coherent path. It proves zero
capacity for every intermediate container, including the square endpoint whose
Oler slack is quadratic. The construction and square-grid comparison in PR #97
show this source family is nonglobal; no canonical source extraction is
claimed. [Audit.108](../../docs/audits/target_c_coupled_delaunay_container_transfer_independent_audit_2026-10-07.md)
supplies container-transfer bookkeeping, while
[Audit.110](../../docs/audits/target_c_exterior_static_packet_barrier_independent_audit_2026-10-07.md)
blocks a scoped static exterior packet; neither gives a moved-wall result or
capacity here. The independently audited
[moved-core refill](../../docs/audits/target_c_exterior_cap_moved_core_refill_independent_audit_2026-10-09.md)
in a different six-spoke family has a strict endpoint; this package instead
isolates a family where a full feasible wall path creates no safe site.

Open [PR #102](https://github.com/1337isnot1337/erdos-99/pull/102) is a Target A
source-image Hall-overlap result; it concerns incidence matching and does not
overlap this Euclidean moved-container proof.

The result does not show that every wall motion fails, and it does not exclude
nonuniform row motion, multi-cell refill, or a motion whose container is not
covered by these rhombi. It is not an endpoint extracted from a canonical
C-II source and it does not close the macroscopic-container restoration
branch, C-II, or Level I.

## Open next question

- **Downstream decision and quantity:** can a canonical macroscopic container
  yield a source-preserving finite endpoint? The quantity is the strict-safe
  full-source capacity after a specified motion, together with the complete
  population, lower-pair, and actual-diameter upper-pair ledgers.
- **Changed hypothesis:** replace this coherent generator rotation by an
  explicitly nonuniform guard or multi-cell motion extracted from the actual
  canonical source; a different angle or a larger Oler deficit alone is not a
  new hypothesis.
- **What either outcome enables:** a positive capacity with all source pairs
  checked gives a candidate restoration input; a zero-capacity theorem for an
  extracted wall class eliminates that class without claiming a global result.
- **First feasible action:** take a canonical candidate guard and compute the
  exact source-wide lower/upper distance ledger under its proposed displacement.
- **Blocker:** no theorem currently extracts a guard whose source geometry and
  all-label displacement satisfy such a ledger.

Required repository-wide theorem-certificate replay is **deferred to the
merging agent**; it is not claimed passed.
