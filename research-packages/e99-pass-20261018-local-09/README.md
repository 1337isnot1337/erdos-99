# Independent audit of POPRESERVE-TWELVE-ARC-PR1008

**Verdict: PASS for the twelve-arc linear reserve theorem and its effective
$D/600$ consequence at the pinned destination bytes.** The audit does not cover
the report's separate reconstruction of the older $D^{2/3}$ argument or its
literature-priority assessment. This is an independent AI-agent proof audit, not a theorem-state or
claim-lifecycle update. The candidate remains marked **unreviewed** in the
theorem and candidate registries; Level I and Target C-II remain open.

Reviewer: OpenAI Codex, GPT-6 Luna xhigh, fleet worker `local-09`. I did not
author or modify the candidate proof or its original verifier. I reconstructed
the analytic argument, checked the global-minimizer reduction, challenged the
full-packing geometry, and replayed the published finite verifier. No external
human review is implied.

Originating assistance is recorded as OpenAI Codex in source PR #1008; that PR
states its exact model setting was not verified. This audit's model and role
are identified above.

## Exact source, claim and scope

- Destination scientific base: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- State / priority / catalogue: `2026-10-15.publication.2` /
  `public-frontier.3` / `public-frontier.9`.
- Frozen source PR: [e-99 PR #1008](https://github.com/1337isnot1337/e-99/pull/1008),
  draft head `ad1bda373a5cbd8c666040f64b4f6ecd83223e31`, base
  `eb51394f371aee958b0d9332f80faf75ae694b9e`.
- Recorded source report SHA-256 before destination transformation:
  `ab25b59f63556860b4014c8dc49c4bf800471851333a6820d4c93fc4bb5041fb`.
- Destination report SHA-256:
  `280ad14b9ab8e265903cdbb55970934b6cde112e9fda511c9d361fa261b322eb`.
- Exact verifier SHA-256:
  `bc3da909fac877d7d08c9ef55d3d0d5df286af3062e92218b4bc213d2e21b8e6`.
- Exact fixture SHA-256:
  `c41fb5e75f4b44a4f317a1703d791fac14043a3605e770304014cac6874a0f36`.

The hashes above were computed from the destination working-tree files and match
the candidate registry. The report is the one destination-transformed artifact;
the verifier and fixture are byte-identical to the frozen source files.

The audited statement is: for every finite planar unit-separated $n$-point
global diameter minimizer of diameter $D>16384$,

\[
g_A=n-1-\frac{\pi D^2}{2\sqrt3}
\ge \gamma D-\frac{\sqrt D}{4\sqrt2}-60,
\qquad
\gamma=\frac{3(576b-65)}{114695a},\quad
a=\frac{\sqrt3}{2},\quad b=\sqrt3-\frac{98}{65}.
\]

The claimed effective consequence is $g_A\ge D/600$ for $D\ge10^6$.
There is no triangle-free premise, source-lattice identification, optimality
claim for $\gamma$, C-II endpoint, or Level I conclusion.

**Named audit question.** Do the twelve simultaneous shallow-arc replacements
indeed give a unit-separated disk packing with the stated all-radius
population lower bound, and does strict-sub-diameter global minimality transfer
that comparison to every minimizer? The exact quantity affected is the
all-minimizer reserve $g_A$; if accepted later, its larger linear term could
alter a Target C comparison only if a separate source-specific upper bound is
proved. The falsification checks were (i) recompute the net row gain and all
error constants exactly, (ii) check every same-frame and different-frame pair
class, including retained old labels, and (iii) test whether the limiting
comparison ever uses a diameter-$D$ competitor. I would stop this review if a
load-bearing pair class or inequality failed, or if an existing exact-head
agent audit already covered this new twelve-arc implication.

## Existing review coverage and current overlap

The candidate registry has `existing_checks: []` and explicitly requests an
independent audit of the analytic averaging proof and globality reduction. The
completed [PR #20](https://github.com/1337isnot1337/erdos-99/pull/20) is
destination-preservation work: its body verifies provenance, hashes, structural
checks and the finite replay, and explicitly says the math is unreviewed. It is
not an independent proof audit. Canonical Audit.243 checks the
older triangular-lattice conflict-deletion $D^{2/3}$ argument; it does not
cover this twelve-arc boundary construction. The source PR #1008 is still draft
and has no reviews or comments.

I read Discussion #83 and the launch overlap handoffs; none concerns this
candidate. The launch overlap snapshot reports complete pagination (97 closed
PRs, one open PR, zero issues, eight discussions). A live check found only
[destination PR #102](https://github.com/1337isnot1337/erdos-99/pull/102) open,
on the Target A source-image Hall overlap formula, a disjoint question. Source
PR #1008 remains a draft without comments or reviews. No source or candidate
lifecycle was changed.

## Independent proof reconstruction

Let $a=\sqrt3/2$, and write a translated triangular lattice in row
coordinates as
\[
\{(t_x+j+l/2,t_y+la):j,l\in\mathbb Z\}.
\]
For a crop disk of radius $R\ge8192$, set $f(z)=\sqrt{R^2-z^2}$. Use
six lattice-symmetry frames. In each frame select rows
$\beta R\le y\le R-a$, where
\[
h=56/65,\quad p=1-a,\quad q=98/65-a,\quad
b=a-q=\sqrt3-98/65,\quad
s=256/16385,\quad \beta=16383/16385.
\]
On a selected row put $u=f(y+a)$, $v=f(y+q)$, and
$\ell=v-u$. Delete old lattice labels in the right interval
[u,v], and insert
\[
(u+1+ih,y+\eta_i),\quad
0\le i\le\left\lfloor\frac{\ell-2}{h}\right\rfloor,
\qquad \eta_i=p\ (i\text{ even}),\ q\ (i\text{ odd}),
\]
with the reflected packet on the left.

### Whole-packing feasibility

Adjacent new points are exactly unit-separated because
$h^2+(q-p)^2=(56/65)^2+(33/65)^2=1$; points two or more steps apart
have horizontal separation at least $2h>1$. Since $\ell>14$, packets
are nonempty and their rightmost point is at most $v-1$. Thus all new points
are strictly inside the disk: $y+\eta_i\le y+q$ implies
$f(y+\eta_i)\ge f(y+q)=v$, while $x\le v-1<v$.

For a right packet, an old point on the same row and retained outside
$[u,v]$ is at least one unit away horizontally. Old rows below $y$ are
separated vertically by at least $a+p=1$. Every old row at or above
$y+a$ has horizontal extent at most $u=f(y+a)$; new points have
$x\ge u+1$, so that entire higher-row family is at least one unit away.
This argument checks inserted points against every original lattice point,
not only labels on that packet's row. For two selected rows in the same frame,
row heights differ by at least $a$. If $y_2\ge y_1+a$, then
$v(y_2)<u(y_1)$, leaving at least two horizontal units between their
right packets; the left packets obey the reflected bound. Opposite-side
packets are separated by at least two units.

The identity $s^2+\beta^2=1$, together with
$|x|\le sR$ and $y\ge\beta R$, gives $|x|/y\le s/\beta=\tan(\arcsin s)$.
Thus each packet and deletion arc lies inside one of six disjoint cones of
half-angle $\phi=\arcsin(s)$.
Different-frame new points have radii at least $\beta R$ and angular
separation at least $\pi/3-2\phi$, so their distance is at least
\[
2\beta R\sin(\pi/6-\phi)
=\beta R(\beta-\sqrt3s)>R/2>1.
\]
The exact inequality $\beta(\beta-\sqrt3s)>1/2$ is independently
checked in `verify.py`. The disjoint cones also prevent different-frame
deletion arcs from counting the same point. Even if deletion sets overlapped,
counting each deleted label once per arc would only lower the population bound;
the geometric cone separation supplies the stronger stated fact. Unchanged
old-old pairs retain their lattice separation. Hence the simultaneous
replacement, not just each isolated arc, is a unit-separated packing.

### Translation-averaged population

At fixed vertical row phase, the horizontal phase is uniform modulo one, so
the expected number deleted from an interval of length $\ell$ is exactly
$\ell$. The number inserted is
$K=\lfloor(\ell-2)/h\rfloor+1\ge(\ell-2)/h$. The *net* row gain is
therefore
\[
K-\ell\ge(1/h-1)\ell-2/h=k\ell-C,
\qquad k=9/56,\quad C=65/28.
\]
This subtraction is essential: $k$ is not the insertion coefficient
$1/h$. Averaging the vertical phase unfolds rows into a Lebesgue integral;
the six rotations are lattice symmetries, and no independence between their
phases is needed. The disk count has mean $\pi R^2/a$, so the expected
modified count is at least
\[
\frac{\pi R^2}{a}+\frac{12}{a}
\int_{\beta R}^{R-a}(k\ell(y)-C)\,dy.
\]
All counts are finite and measurable over a compact translation domain; an
integer-valued realization is at least this mean.

### Integrated arc and exact errors

With $I=\int_{\beta R}^{R-a}\ell(y)\,dy$, changes of variables give
the exact oriented-integral identity
\[
I=\int_{\beta R+q}^{\beta R+a} f(z)\,dz
  -\int_{R-b}^{R}f(z)\,dz.
\]
It remains valid if the two displayed intervals overlap. Monotonicity of
$f$ bounds the first term below by $b f(\beta R+a)$. For the second,
putting $t=R-z$ gives
\[
\int_{R-b}^{R}f(z)\,dz
\le \int_0^b\sqrt{2Rt}\,dt
=\frac23\sqrt{2R}\,b^{3/2}.
\]
Since $\beta R+a\le R$ for $R\ge8192$, the identity
$f(\beta R+a)^2=s^2R^2-2\beta aR-a^2$ and
$\sqrt{x-t}\ge\sqrt{x}-t/\sqrt{x}$ imply
\[
f(\beta R+a)\ge sR-\frac{2\beta a}{s}-\frac{a^2}{sR}.
\]
Substitution yields the exact lower-bound form
\[
\mathbb E N_{\rm new}\ge
\frac{\pi R^2}{a}+2\gamma R-A\sqrt R-B_0+12C,
\]
where
\[
\gamma=\frac6a\{kbs-C(1-\beta)\},\quad
A=\frac{8\sqrt2}{a}k b^{3/2},\quad
B_0=\frac{12}{a}kb\left(\frac{2\beta a}{s}
                    +\frac{a^2}{8192s}\right).
\]
The positive $12C$ may be discarded. Exact rational interval arithmetic in
`verify.py` gives
\[
0.00193<\gamma<0.00194,\qquad A^2<1/16,\qquad B_0<60,
\]
which proves the disk bound
\[
N_{\rm new}\ge\frac{\pi R^2}{a}+2\gamma R-\frac{\sqrt R}{4}-60.
\]
In particular, the square-root error check is on the net gain coefficient
$k=9/56$, after subtracting the deleted row population.

The effective coefficient simplifies exactly: with $1-\beta=2/16385$,
\[
\gamma=\frac6a\left(\frac9{56}b\frac{256}{16385}
                       -\frac{65}{28}\frac2{16385}\right)
=\frac{3(576b-65)}{114695a}.
\]

### Transfer to every global minimizer

For a global $n$-point minimizer of diameter $D>16384$, choose any
$8192\le R<D/2$. The constructed competitor has diameter at most $2R<D$.
If it had at least $n$ points, an $n$-point subset would contradict global
minimality. Its integer population is therefore at most $n-1$, for each
such $R$. Letting $R\uparrow D/2$ in the continuous lower bound gives
\[
g_A\ge\gamma D-\frac{\sqrt D}{4\sqrt2}-60.
\]
The limit does not assert a diameter-$D$ competitor. No source point,
including any contact isolate, is moved, removed, or identified with the
comparison lattice.

The exact bounds $\gamma>193/100000$ and
$1/(4\sqrt2)<1/5$ give, for $x=\sqrt D\ge1000$,
\[
g_A-D/600\ge\frac{79}{300000}x^2-\frac{x}{5}-60.
\]
At $x=1000$ this is $10/3>0$, and its derivative is positive for every
larger $x$. Thus the stated $D/600$ consequence follows.

## Adversarial scope and predecessor comparison

The independent lattice is used only as a competitor in the cardinality
contradiction. The proof retains the universal quantifier over every global
minimizer at every stated $D$, and does not assume triangle-freeness or any
contact/stress condition. The report's separate stretched-packing example is
only a feasible nonglobal triangle-free high-reserve regression; it is
consistent with this global-minimizer theorem and does not provide a
counterexample to it.

The candidate credits PR #956 for an earlier, weaker $D/320000$ linear
reserve; the twelve-arc proof has its own constants and does not depend on
acceptance of that PR. Canonical Audit.243 remains the distinct earlier
$D^{2/3}$ comparison. The candidate improves the order of the lower
reserve if accepted, but supplies no upper bound on $g_A$ for triangle-free
global minimizers and no same-cardinality source-specific strict-sub-$D$
replacement. Consequently it changes no Level I or C-II conclusion.

These predecessor results are credited, not imported as proof premises. This
audit contains no third-party copied material and is contributed under the
repository's Apache-2.0 contribution terms.

## Reproduction and limits

The audit arithmetic checker uses exact rational arithmetic and certified
rational endpoints for $\sqrt3$:

```sh
python research-packages/e99-pass-20261018-local-09/verify.py
```

It returned `PASS`: the exact interval for $\gamma$ lies in
$(193/100000,194/100000)$, the square-root error coefficient has squared upper
bound below $1/16$, the constant error is below $60$, and the different-frame
clearance exceeds $1/2$ in units of $R$. The negative control that incorrectly
uses the insertion coefficient $1/h$ as the net row gain is rejected.

The pinned candidate verifier is not an execution dependency of this package;
the package's arithmetic checker is self-contained and does not import it. The
candidate verifier was run separately as listed below.

The published finite verifier was independently replayed with `--extended`.
It checked five radius/phase cases (1,052 packets total), 31,374 inserted
labels, 19,659 retained-neighbor checks, 42,969 inserted-neighbor checks,
150 lattice rotations, 169 sign controls and two rejected collision controls.
The saved replay output is external to the repository. Those finite cases
check implementation and constants; the all-radius conclusion comes from
the analytic averaging proof above, not from finite enumeration.

Required full repository-wide theorem-certificate replay is deferred to the
merging agent if the planner requires it. No manifest, theorem state,
candidate lifecycle, scientific priority, release setting or other PR branch
is changed by this package.

## Open next question

The downstream decision is whether the reserve can exclude every sufficiently
large triangle-free global minimizer. The exact quantity needed is a uniform
upper estimate $g_A\le cD+o(D)$ with fixed $c<\gamma$, derived from the
full source while retaining all labels and pair constraints. A proof would
contradict the audited reserve for large $D$; a counterexample would block
this upper-reserve route and require another source-specific strict-diameter
construction. The first useful action is to derive that upper estimate from
actual source geometry. The current blocker is that this candidate compares
the source cardinality with an independent lattice packing but supplies no
source-to-lattice extraction or transport theorem.
