<!-- theorem-state: {"artifact_id":"ART-3A37D57A294B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdős Problem #99 — Target B explicit balanced coherent phase gap

**Date:** 2026-09-05  
**Run type:** quantitative stability / explicit balanced constant  
**Target:** dense coherent three-phase global deficit-transfer gate  
**Depends on:** balanced tripartite stability; dual-tree dense-grid correction; trimmed-grid phase-star diameter theorem  
**LEVEL I STATUS:** STILL OPEN

## 1. Statement

Let a coherent three-phase train component have three phase classes

`A,B,C`

of equal size `m`. Assume:

1. the phase crossing graph has no transversal triangle;
2. the three phase directions are `o(1)`-coherent around the triangular projective directions;
3. crossings involving trains outside this coherent component are `o(m^2)`;
4. `T=O(m)`.

Let `E` be the crossing count inside the component and put

`epsilon = 2-E/m^2`.

### Theorem 1 — explicit balanced phase deficit

Every sufficiently large admissible component satisfies

`E <= (2-10^(-7)+o(1))m^2`.

Equivalently,

`liminf (2m^2-E)/m^2 >= 10^(-7)`.

The constant is conservative and is chosen to leave visible numerical slack.

## 2. Explicit balanced tripartite stability constant

The balanced stability proof can be made quantitative with a clean constant.

Suppose

`E >= (2-epsilon)m^2`.

For a transversal triple define its defect

`d(a,b,c)=2-[1_(ab)+1_(bc)+1_(ca)] >=0`.

Then

`D_3=sum d <= epsilon m^3`.

### Lemma 2 — one pair has at most `4sqrt(epsilon)m^2` nonedges

Some pair among `A-B`, `A-C`, `B-C` has at most

`4sqrt(epsilon)m^2`

missing crossings.

### Proof

If `A-B` already has at most that many nonedges, stop.

Otherwise call an `A` or `B` vertex slice-bad when its slice defect exceeds

`sqrt(epsilon)m^2`.

There are at most `sqrt(epsilon)m` bad vertices on each shore. Hence fewer than

`2sqrt(epsilon)m^2`

`A-B` nonedges touch a bad vertex, leaving more than `2sqrt(epsilon)m^2` good-good nonedges.

Averaging `D_3` over those good-good nonedges gives one absent pair `a_0b_0` with

`sum_c d(a_0,b_0,c) <= sqrt(epsilon)m/2`.

Thus their common `C`-neighbor set `C_*` satisfies

`|C_*| >= (1-sqrt(epsilon)/2)m`.

For the present application `epsilon<=10^(-7)`, so in particular `|C_*|>=m/2`.

Put

`A_1=N(b_0) cap A`, `B_1=N(a_0) cap B`.

Every triple in `A_1 x B_1 x C_*` has defect at least one, so

`|A_1||B_1||C_*| <= epsilon m^3`.

Hence

`min(|A_1|,|B_1|) <= sqrt(2epsilon)m`.

Assume `|A_1|` is the smaller quantity. Missing `A-C` edges are contained in:

1. pairs incident with `A_1`, at most `sqrt(2epsilon)m^2`;
2. pairs incident with `C\C_*`, at most `(sqrt(epsilon)/2)m^2`;
3. missing `A_0-C_*` pairs, at most `sqrt(epsilon)m^2` because the `b_0` slice is good.

Therefore the `A-C` missing count is at most

`(sqrt(2)+3/2)sqrt(epsilon)m^2`

`<3sqrt(epsilon)m^2`

`<4sqrt(epsilon)m^2`.

The `B_1` case is symmetric. `square`

Let

`mu <= 4sqrt(epsilon)`                                      (2.1)

be the missing density of the resulting coherent phase pair.

## 3. Quantitative dual-tree rectangle

Apply the audited dual-tree extraction to that pair. Put

`r=sqrt(mu)`.

There is a complete crossing grid `A' x B'` with

`|A'| >= (1-r)m`,

`|B'| >= (1-mu-2r)m-O(1)`.

Therefore the total normalized number of omitted trains from those two phase classes is at most

`L=3r+mu+o(1)`.                                           (3.1)

Using (2.1),

`r <= 2 epsilon^(1/4)`,

and hence

`L <= 6 epsilon^(1/4)+4sqrt(epsilon)+o(1)`.              (3.2)

As in the explicit unique-max theorem, omitted trains may themselves separate the chosen grid diagonal, so the diameter argument must pay this loss twice.

## 4. Balanced diameter margin

For equal full phase sizes the trimmed-grid constrained minimum has

`F(1,1)=3`.

The third phase is allowed its full worst signed cancellation of magnitude at most `m+o(m)`; this is already included in the value three.

The complete-grid vector shortening costs at most `L`, and arbitrary contributions from the omitted two-phase trains cost another `L`. Truly external trains cost only `o(m)` after a further fixed-fraction central trim and the penetration-depth lemma.

Therefore

`D/m >= sqrt(3)-2L-o(1)`,

so

`D^2/m^2 >= 3-4sqrt(3)L-o(1)`.                          (4.1)

Let

`c=2sqrt(3)/pi=1.1026577908...`.

A balanced component with crossing deficit `epsilon m^2` and only `o(m^2)` external rhombi has

`R/m^2=2-epsilon+o(1)`,

hence

`n/m^2=2-epsilon+o(1)`.

The strict triangular-lattice comparison gives

`D^2/m^2 < c(2-epsilon)+o(1) <=2c+o(1)`.                (4.2)

The full balanced squared-diameter margin is

`3-2c =0.7946844183...`.                                (4.3)

## 5. Insert `epsilon_0=10^(-7)`

For

`epsilon_0=10^(-7)`,

(3.2) gives

`L <= 6 epsilon_0^(1/4)+4sqrt(epsilon_0)+o(1)`

`<0.107962+o(1)`.

Thus

`4sqrt(3)L <0.7480+o(1)`.

Comparing with (4.3) leaves more than

`0.046`

of normalized squared-diameter slack. Hence (4.1) gives

`D^2/m^2 > 2c+0.04`

for sufficiently large terms, contradicting (4.2).

Therefore `epsilon<=10^(-7)` is impossible, proving Theorem 1.

## 6. Use in the global phase program

The balanced phase endpoint now carries an explicit local deficit currency:

`2m^2-E >= 10^(-7)m^2-o(m^2)`.

Together with the explicit unique-max bound

`M(a+b)-E >= 8*10^(-5) kappa tau M^2-o(M^2)`,

the only remaining quantitative interpolation is the two-largest-nearly-tied regime. Once that regime is assigned an explicit coefficient, the entire coherent phase stability theorem can be inserted into a global optimization without compactness constants.

## 7. Audit cautions

- The original false global interval-order lemma is not used; the complete grid comes from the dual-tree backbone theorem.
- The `4sqrt(epsilon)` pairwise missing bound is derived explicitly here; no hidden big-O constant remains.
- Omitted trains from the two extracted phase classes are charged as possible diagonal cancellation.
- The third phase receives its full worst coherent cancellation.
- External train error is controlled only under the stated `o(m^2)` non-core crossing hypothesis.
