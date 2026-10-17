> Generated reading edition · [exact source](../../research/target_b_min_degree_phase_polytope_determinant_2026-10-02.md) · source SHA-256 `db0b9e6cd050067ed18c91040d92a329a04496b669ca9b4b717a03d75dc4ee5a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f1767a431b283cf03db49670ba682ea6cc692afe", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_b_min_degree_phase_polytope_determinant_2026-10-02.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2d47e0686b88cf3849eebd3808d982e8092944e249f8079339ee352daeffe3e8"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target B - minimum-degree phase-polytope cross-grain bound

Date: 2026-10-02
Base main: `6bd2f8044952e339dab735bdc0def1fd5669bd24`
Status: proved candidate, noncanonical. Target B remains open.

This note strengthens `research/target_b_exact_three_phase_cross_grain_determinant_2026-10-02.md`.

Let `H` be a Section-50 retained component with phase-class sizes
`n = (n_0,n_1,n_2)` and minimum degree `delta > 0`.
The phase graph has no same-class edges and no transversal triangle, hence it is
triangle-free.

For every pair of phase classes,

    n_r + n_s >= delta.                                    (1)

If the complementary class is nonempty, take a vertex in it. If it is empty,
the remaining graph is bipartite and each shore has size at least `delta`.

Also,

    n_0 + n_1 + n_2 >= 2 delta.                            (2)

Indeed, choose a vertex `v` of degree `q >= delta`. Its neighborhood is
independent. For `u in N(v)`, triangle-freeness gives
`N(u) subset V(H) minus N(v)`, so

    delta <= deg(u) <= |V(H)| - q.

Define

    P_delta = conv{(0,delta,delta),
                   (delta,0,delta),
                   (delta,delta,0)}.

Equivalently,

    P_delta = {p in [0,delta]^3 : p_0+p_1+p_2 = 2 delta}.

## Lemma 1

There is `p in P_delta` with `p_r <= n_r` for every `r`.

Put

    l_r = max(0, delta - n_r).

Equations (1)-(2) imply

    l_0 + l_1 + l_2 <= delta.

If all `n_r <= delta`, then

    sum_r l_r = 3 delta - sum_r n_r <= delta.

If, say, `n_0 >= delta`, then

    l_1 + l_2 <= 2 delta - (n_1+n_2) <= delta.

Choose `q_r >= l_r`, `0 <= q_r <= delta`, with
`q_0+q_1+q_2 = delta`, and set

    p_r = delta - q_r.

Then `p in P_delta` and `p_r <= n_r` coordinatewise.

## The determinant floor

For phase vectors `x,y`, define the ideal determinant mass

    G_theta(x,y)
      = sum_(r,s in Z/3)
          x_r y_s |sin(theta + (s-r) pi/3)|.              (3)

All coefficients are nonnegative, so `G_theta` is coordinatewise monotone.

For distinct retained components `H_i,H_j`, Lemma 1 gives

    p <= n(H_i),   q <= n(H_j),

with `p in P_(delta_i)` and `q in P_(delta_j)`.
The minimum of the bilinear form (3) on
`P_(delta_i) x P_(delta_j)` occurs at a pair of vertices:
for fixed `q` minimize the linear function in `p` at a vertex, then for that
`p` minimize the linear function in `q` at a vertex.

Each vertex has exactly two nonzero coordinates, both equal to its minimum
degree. The four phase products therefore have absolute-sine multiplicities
`(2,1,1)`, up to cyclic permutation. The four-direction inequality from
the preceding cross-grain note gives, for every real `theta`,

    G_theta(n(H_i), n(H_j))
      >= sqrt(3) delta_i delta_j.                          (4)

This bound is sharp at the phase-polytope level: two two-phase vectors, for
example `(0,delta_i,delta_i)` and `(0,delta_j,delta_j)`, attain the
four-direction minimum for a suitable relative phase.

## Return to actual train directions

Let `epsilon_D = o(1)` be the Section-50 phase-coherence radius and let
`E_hi(H_i,H_j)` be the high-defect crossing set between the two retained
vertex sets.

Replacing actual directions by ideal phase directions changes one absolute sine
by at most `2 epsilon_D`. Hence the total coherence loss is at most

    2 epsilon_D |H_i| |H_j|.

A physical crossing between a train of `H_i` and a train of `H_j` must be an
initial high-defect deletion: both train vertices survived pruning, so any
retained low-defect crossing would join the two vertices and put them in the same
retained component.

Therefore

    W_ij
      >= sqrt(3) delta_i delta_j
         - 2 epsilon_D |H_i| |H_j|
         - |E_hi(H_i,H_j)|.                               (5)

For fixed pruning parameter `lambda`,

    delta_i, delta_j >= lambda D,

the component sizes are `O(D)`, `epsilon_D = o(1)`, and the total
high-defect crossing count is `o(D^2)`. Thus

    W_ij >= sqrt(3) lambda^2 D^2 - o(D^2).                (6)

The preceding full-phase note obtained only

    W_ij >= (sqrt(3)/4) lambda^2 D^2 - o(D^2)

from the second-largest-class estimate `b >= lambda D/2`. Equation (6)
improves that coefficient by a factor of four. The gain comes from using
triangle-freeness and minimum degree simultaneously.

## Global form

Let the retained components be `H_1,...,H_k` and set

    V_cross = sum_(i<j) W_ij.

For fixed `lambda` there are only `O_lambda(1)` retained components, so
the coherence losses in (5) are summable. The sets `E_hi(H_i,H_j)` are
disjoint over unordered component pairs. Hence

    V_cross
      >= sqrt(3) sum_(i<j) delta_i delta_j - o(D^2)
      >= sqrt(3) lambda^2 D^2 binom(k,2) - o(D^2).        (7)

The exact virtual-zonotope identity and the same pure-disk area bounds used in the
preceding notes give

    V_cross <= T^2/pi - pi D^2/4 + o(D^2).

Writing `x = T/D`,

    sqrt(3) lambda^2 binom(k,2)
      <= x^2/pi - pi/4 + o(1).                            (8)

## Scope and remaining bottleneck

This is proof-only. No numerical search, finite verifier, or CI result is used.

Equation (8) does not close Target B. The Section-50 quantifier order fixes
`lambda > 0` before `D -> infinity`; taking `lambda` small keeps the pruning loss
small, while the cross-grain penalty in (8) is quadratic in `lambda`. Several
macroscopic retained grains are still compatible with the present global
constants.

The next target is to remove that `lambda^2` bottleneck. The audited phase-coarea
decomposition obtains coherent physical grains after only boundary-order crossing
deletion, without minimum-degree pruning. A useful next theorem would replace the
minimum-degree product in (5) by a quantity controlled by each coarea grain's
actual crossing density, so retained physical crossing mass and cross-grain
virtual determinant mass enter one inequality without the coarse
`lambda D^2` pruning term.
