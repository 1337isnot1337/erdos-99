<!-- theorem-state: {"artifact_id":"ART-98AB06F9B50D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global stress and density: an independent obstruction test

**Classification:** proved candidate awaiting promotion; the family below is a
**regression**, not a family of global minimizers. **Level I remains open.**

## Run lock and intended implication

- Baseline: `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
- State: `2026-10-10.audit.234`.
- Owned branch: `research/sol/global-independent-20261011`.
- Objective: independently settle the full Level I quantifiers without consulting
  Claude's solution or research artifacts.
- Global candidate under test: positive full-support stress, scalar stress PSD,
  mixed infinitesimal rigidity, and near-circular full-source geometry force a
  leading-order population loss for triangle-free sources.
- Intended chain: such a loss -> population below the translated triangular
  lattice competitor -> exclusion of every normalized triangle-free minimizer.

The calculation below rejects that proposed leading-order bridge. All the listed
properties coexist with the optimal leading population coefficient. The missing
information must operate below quadratic order or use global optimality directly.
This is an independent derivation; no novelty claim relative to the archive is made.

Canonical inputs used to frame the question are the exact problem statement,
Target C modules 56 and 57 (full support, PSD, and core rigidity), and module 58
(the strict translated-lattice comparison). The construction and spectral proofs
below are elementary and do not assume that the constructed sources are canonical.

## 1. The regular odd contact ring

Let `q>=5` be odd, `m=(q-1)/2`, and put

\[
x={\pi\over2q},\quad z=e^{4ix},\quad
R={1\over2\sin(2x)},\quad p_j=Rz^j\quad(0\le j<q).
\]

The shortest nonzero chords are exactly the consecutive sides, of length one.
The longest chords are exactly the pairs at cyclic step `m`, of length

\[
D={1\over2\sin x}=2R\cos x.
\tag{1}
\]

Thus the unit-contact graph is `C_q`, and the actual diameter graph is also a
`q`-cycle, with step `m`. In particular the contact graph is triangle-free.

Give every diameter edge weight `beta=1/q`, and every contact edge weight

\[
\alpha={1-\cos(4mx)\over q(1-\cos(4x))}
       ={D^2\over q}.
\tag{2}
\]

The total diameter weight is one. At every vertex both contact neighbors have
radial resultant `2alpha(1-cos(4x))p_j`, and both diameter neighbors have radial
resultant `2beta(1-cos(4mx))p_j`. Equation (2) gives equilibrium. Every actual
contact and diameter edge has strictly positive weight.

## 2. Exact stress spectrum

Let `Omega=alpha L_1-beta L_m`, where `L_k` is the unweighted cyclic step-`k`
Laplacian. Its Fourier eigenvalue at frequency `l` is

\[
\lambda_l=4\alpha\sin^2(2lx)-4\beta\sin^2(2mlx).
\]

For `1<=l<=q-1`, division by the positive factor
`4beta sin^2(2lx)` gives

\[
{\lambda_l\over4\beta\sin^2(2lx)}
=D^2-
\begin{cases}
1/(4\sin^2(lx)),&l\text{ odd},\\
1/(4\cos^2(lx)),&l\text{ even}.
\end{cases}
\tag{3}
\]

Here `0<lx<pi/2`. The odd case is zero precisely at `l=1`; the even
case is zero precisely at `l=q-1`. Every other value is positive.
Frequency zero is the constant kernel. Consequently

\[
\Omega\succeq0,\qquad
\ker\Omega=\operatorname{span}\{1,P_x,P_y\},\qquad
\operatorname{rank}\Omega=q-3.
\tag{4}
\]

This conclusion is an exact formula for all odd `q`, not a numerical eigenvalue
test or an appeal to the canonical global-minimizer theorem.

## 3. Exact mixed rigidity

Write a real velocity as `u_j=z^j(a_j+i b_j)`. The zero first variation of a
step-`k` bar, after division by its nonzero sine factor, is

\[
\tan(2kx)(a_j+a_{j+k})+b_{j+k}-b_j=0,
\quad k\in\{1,m\}.
\tag{5}
\]

Complexify the two real sequences and take frequency `l`. The two equations
have coefficient rows

\[
(\tan(2kx)(1+e^{4ilkx}),\ e^{4ilkx}-1).
\]

Up to nonzero phase and constant factors, their determinant is

\[
T_l=\tan(2x)\cos(2lx)\sin(2mlx)
    -\cot(x)\cos(2mlx)\sin(2lx).
\]

For odd `l`, up to an irrelevant sign this factors as

\[
2(\tan(2x)+\cot x)\cos(lx)
       (\sin^2x-\sin^2(lx));
\tag{6}
\]

for even nonzero `l`, up to sign it factors as

\[
2(\tan(2x)+\cot x)\sin(lx)
       (\sin^2x-\cos^2(lx)).
\tag{7}
\]

The identity used in both factorizations is
`tan(2x)/(2(tan(2x)+cot x))=sin^2 x`.
Thus only frequencies `1` and `q-1` have a nontrivial kernel; each has
complex dimension one. At frequency zero, (5) forces `a=0` and leaves the
one rotational mode. The real flex space therefore has dimension three,
and consists of translations and rotation:

\[
\operatorname{rank}R_{C\cup H}=2q-3.
\tag{8}
\]

## 4. Local optimality, with its exact scope

These rings are isolated locally among configurations of the same labels having
all separations at least one and diameter at most `D`, modulo Euclidean motions.
To see this, suppose a sequence of different feasible rings converges to the given
ring. Align each by the minimizing Euclidean motion. Divide its displacement by
its norm and pass to a unit limit orthogonal to the three rigid velocities.
First-order feasibility puts this limit in the signed critical cone. Pairing
with the strictly positive stress forces every active first variation to vanish.
Equation (8) then makes the limit a rigid velocity, a contradiction.

This proves local diameter minimality. It does not prove global diameter
minimality. Adding strictly separated interior points leaves the local ring
obstruction intact, while those extra labels remain freely movable.

## 5. Quadratic population, including every contact isolate

Put `a=pi/(2sqrt(3))`. For all sufficiently large odd `q`, define

\[
n_q=\lfloor a(D-4)^2\rfloor,\qquad s=1+q^{-2},\qquad r=D/2-2.
\tag{9}
\]

A triangular lattice of spacing `s` has covolume `sqrt(3)s^2/2`.
Translation averaging over one fundamental cell gives a translate containing at
least

\[
\left\lceil{\pi r^2\over(\sqrt3/2)s^2}\right\rceil
=\left\lceil{a(D-4)^2\over s^2}\right\rceil
\tag{10}
\]

points in the radius-`r` disk. The difference between `a(D-4)^2` and the
unrounded expression in (10) stays bounded as `q` grows, because `D/q->1/pi`.
Hence this disk supplies at least `n_q-q` points for all sufficiently large `q`.
Retain exactly that many and adjoin them to the ring.

All isolate-isolate distances exceed one. Every ring-isolate distance is at
least `R-r>2`. The radius-`r` disk is strictly inside the regular polygon for
large `q`, since its inradius is `R cos(2x)=D/2-O(1/D)`. Thus all
isolate-involving upper distances are strictly less than `D`: a strict interior
point of the polygon has distance strictly below its diameter from every point
of the polygon. No new contact or diameter edge is created.

The full source has exactly `n_q` labels and

\[
{n_q\over D^2}\longrightarrow {\pi\over2\sqrt3}.
\tag{11}
\]

Its hull is the regular polygon, whose inradius and circumradius differ from
`D/2` by `O(1/D)`. Its active core retains (2), (4), and (8), with all actual
contacts and diameter edges strong. The additional zero rows of the full stress
matrix are precisely the contact isolates; no affine-kernel claim is made for
the full source.

The sources are nevertheless **strictly nonglobal**. The strict
translated-triangular-lattice comparison gives, for their cardinalities,

\[
D(n_q)^2 < {n_q-1\over a} < (D-4)^2.
\tag{12}
\]

Therefore a competing source of the same cardinality has diameter less than
`D-4`. This also supplies an explicit reason these sources are compatible with
the open Level I problem. Their relative diameter inefficiency tends to zero,
while their absolute diameter inefficiency is bounded below by four. For the
relative assertion, finite Oler and the perimeter-diameter inequality give
`n<=a d^2+(pi/2)d+1` at the true optimum `d=D(n)`, hence
`d>=sqrt(n/a)-O(1)`; combine this with (9) and `d<=D`.

## 6. Consequence for the global strategy

There is no uniform `epsilon>0` such that full support, scalar PSD, mixed core
rigidity, local diameter optimality, asymptotically circular hull, and retention
of all source labels imply

`n <= (pi/(2sqrt(3))-epsilon) D^2`.

The construction satisfies all those hypotheses and violates every such bound
eventually. An argument using those inputs must resolve the boundary-order
population comparison, extract additional consequences of **global** optimality,
or construct a finite same-cardinality competitor. The theorem does not rule out
such a global argument, a refined population estimate, or Level I closure.

## Verification and status

The universal spectrum, rigidity, isolation, and population claims have the
analytic proofs above. `research/verify_global_stress_density_regression_2026_10_11.py`
checks independent finite instances with rational interval bounds and exact
triangular-lattice squared-distance arithmetic. A separate exact cyclotomic
remainder calculation checks the original Fourier-row determinants independently
of their factorizations. The script is not a universal
proof, an independent audit, or a global-optimality certificate.

No theorem-state promotion is requested by this report.
