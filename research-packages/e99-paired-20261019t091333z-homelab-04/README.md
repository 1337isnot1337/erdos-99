# Safe-core vacancy as a conditional annular source packet

**Classification:** unreviewed conditional lemma and exact finite regression.
It establishes no universal extraction for global minimizers and no Level I
closure.

- Exact investigation: global-annular-source-packet-paired-20261019
- Scope key: b0e191c537f21698e04eeb1f
- Broad catalogue card: global-joint-phase-source-extraction
- Destination base: 7d0a450fe66991036541023f95c44c064a04b6a8
- Theorem state / priority / catalogue: 2026-10-15.publication.2 /
  public-frontier.3 / public-frontier.9
- Annular candidate: GLOBAL-LEVEL-I-ANNULAR-MATCHING-PR955, unreviewed
- Frozen source PR #955 head: d5afc236a7b1de9567dcb6dda65d957ed91c726b
- Destination report SHA-256:
  c564b3577562e3aeec1bf4ea2e7a800e4014fad6d5ebe7a2844daad6a3d61e5c
- Destination exact-packet JSON SHA-256:
  b7ea9aa0e49a390575b8576c0b4eb9e931967a68174408b18d8ffb93687d4c08
- Destination source-verifier SHA-256:
  4cf5b2a2c6caf787ce92a892dabb694d9ffce13ab621e724820759635cc8fb8b
- Canonical D^(2/3) reserve audit SHA-256:
  5134f4c246286fec50530e0c6855d6b370ed2b2252e8918680b8a0e1b177aa4a

Prepared by OpenAI Codex (GPT-6 Luna xhigh) as an AI-generated proof and
checker. Independent mathematical review remains outstanding. The contribution
is first-party and Apache-2.0-compatible; predecessor attribution is retained.

## Exact condition and result

Let A be a finite unit-separated planar source with n labels and diameter D.
A minimum enclosing disk has either two antipodal support points, giving radius
at most D/2, or three support points whose triangle contains its center. In the
latter case the triangle is acute or right, its largest angle is between 60 and
90 degrees, and its largest side is at least sqrt(3) times the circumradius.
Thus in every case A lies in a closed disk centered at o of radius
R = D/sqrt(3). Let G_D(A) be the graph on all source labels, with
an edge exactly for every pair at distance at least D. Since diam(A)=D, these
are all actual diameter pairs, including ties. Write tau_D(A) for its minimum
vertex-cover size.

Define the safe-core vacancy number v_D(A,o) as the largest size of a finite
set Y satisfying all three geometric conditions:

1. Y lies in the open disk B(o,D-R);
2. distinct points of Y are at least one apart;
3. every point of Y is at least one from every label of A.

**Conditional source-extraction lemma.** If
v_D(A,o) >= tau_D(A), choose such a Y with |Y| >= tau_D(A) and set X=A union
Y. Then X is an admissible annular comparison packet inside B(o,S) for any
sufficiently small S>D/sqrt(3) with S<D/sqrt(2), and

    M_D(X) = |X| - tau(G_D(X)) = n + |Y| - tau_D(A) >= n.

Indeed, D-R < R, so X lies in the Jung disk. For y in the safe core and a in
A, |y-a| < (D-R)+R = D; for two points of Y, |y-y'| < 2(D-R) < D. Thus the
full annular conflict graph of X consists of the source's complete
actual-diameter graph plus isolated vertices from Y. The pinned PR #955
identity for M_D then gives the displayed count. Every source label,
including contact isolates, is retained in X; every lower pair constraint
and every new or old upper pair is accounted for.

For a global minimizer, M_D(X) >= n supplies an n-label unit-separated subset
of diameter strictly below D, a contradiction. Therefore this condition is a
useful sufficient source hypothesis, and every global source must fail it
for each such Jung center. The proof does not establish that the condition
holds for any large global source.

The canonical reserve is the distinct all-global statement
g_A = n-1-pi*D^2/(2*sqrt(3)) >= kappa*D^(2/3). It supplies no bound here on
the source-dependent safe-core vacancy or on tau_D(A). This lemma uses no
stronger unreviewed reserve.

## Exact controls

The verifier checks a positive rational toy instance of the implication:
A={(-1,0),(1,0)}, D=2, and Y={(0,1/2)} give one diameter conflict, one
vacancy label and M_D(A union Y)=2=|A|.

The adversarial control reconstructs the pinned PR #955 D=8 packet with
radius 17/4 and phase (1/4,1/4). It has 67 labels, 15 annular labels and
eight distance-at-least-8 conflicts. The exact minimum cover has four labels
{(-4,4),(-3,5),(1,4),(4,1)}. Deforming its unit basis to dot product
163/328 gives a 63-label triangle-free source A, with

- actual diameter squared 5193/82;
- an undeformed unit-separated same-label configuration of diameter squared
  63 < 5193/82, certifying that this control is nonglobal;
- two actual diameter pairs, full diameter-cover number tau_D(A)=2, and positive
  scalar excess g_A > 16883/4879 > 0;
- all source labels inside the Jung disk centered at the origin;
- 57 retained translated-lattice sites covering the entire Jung safe core
  within distance rho, where rho^2=164/491 < 9/25.

For this source D < 8, so
D(1-1/sqrt(3)) < 44/13; also rho < 3/5, and
44/13+3/5 = 259/65 < 4. The deformed basis angle theta lies between 60 and
90 degrees. Splitting each basis parallelogram along its shorter diagonal gives
acute Delaunay triangles with circumradius rho = 1/(2*cos(theta/2)), hence
rho^2 = 1/(2*(1+163/328)) = 164/491. Thus the translated lattice has covering
radius rho. Every point of the safe core is within rho<1 of a lattice site
whose radius is below four. The exact enumeration checks that all 57 possible
sites of radius below four are retained in A. The safe-core vacancy is zero
while tau_D(A)=2. This exact nonglobal control shows
that triangle-freeness and positive scalar excess do not imply the added
geometric condition. It is not a counterexample to the canonical reserve,
which is scoped to global minimizers, and it does not refute the lemma.

The checker reconstructs the conflict graph and minimum cover independently,
checks all 63 source pair distances as exact fractions, checks the two
diameter ties, tests the strict nonglobal comparator, and verifies the
finite lattice-site coverage certificate. A deliberate missing-site control
confirms the coverage check rejects an omitted source label.

## Predecessors and boundaries

- The annular matching and M_D identity are taken from the pinned PR #955
  candidate; this package does not reprove its supplied-packet theorem.
- Open PR #123 audits a separate PR #957 joint diameter-cover/matching
  identity and leaves universal successful-packet existence open. This
  contribution supplies a narrower source-derived packet under safe-core
  vacancy, without using its mixed cross-packet construction.
- Open PR #122 audits the separate, unreviewed twelve-arc D/600 population
  candidate. This package uses only the canonical D^(2/3) reserve and does
  not depend on PR #122.
- Live Discussion #83 and the three predecessor handoff files had no
  matching annular source-packet investigation.

## Reproduction and status

Run from the repository root:

    python research-packages/e99-paired-20261019t091333z-homelab-04/verify.py
    python scripts/research_package.py --package research-packages/e99-paired-20261019t091333z-homelab-04 --check-only

The exact checker uses Python 3.14's standard library only. Its result is
finite evidence for the stated packet and regression; it proves neither
safe-core vacancy for global sources nor eventual nonattainment. Required
repository-wide theorem-certificate replay is deferred to the merging agent.

## Open next question

Can the canonical global source geometry force
v_D(A,o) >= tau_D(A) for some Jung center, or can one prove the strict
opposite inequality for every large triangle-free global minimizer? The exact
quantity is v_D(A,o)-tau_D(A), which decides whether this annular packet
reaches M_D(X)>=n. A positive result gives an immediate strict-sub-D
contradiction; a negative theorem retires this safe-core architecture and
requires a packet using source labels outside the core. First action: bound
the unit-packing capacity of the Jung core's complement of the source's
radius-one neighborhoods against the full actual-diameter cover number.
The blocker is that neither the canonical scalar reserve nor the exact
nonglobal control determines this source-specific capacity for global
minimizers.
