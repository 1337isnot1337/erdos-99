> Generated reading edition · [exact source](../../research/target_c_flat_pentagon_unloaded_stress_through_2026-09-14.md) · source SHA-256 `4fa4b6bf6ec290d31287975f300c225396205bb4cea79138187e87542a021c53`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8aa02ce6ccd778090e37c406719aee0f72c63954", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_flat_pentagon_unloaded_stress_through_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6f43b75ba7d609020c3f39e22f2aa2db2e556a979588bd8e7eb11b9386a354c4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — unloaded flat-pentagon middles are asymptotic stress-through couplers

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Depends on:** positive KKT contact equilibrium and `target_c_flat_pentagon_middle_degree_stress_dichotomy_2026-09-14.md`  
**Claim class:** exact local strengthening; proof-only global application

## LEVEL I STATUS

`STILL OPEN`

The preceding flat-middle theorem separated unloaded degree three from unloaded degree four. Positive equilibrium actually unifies them: for either degree, every contact ray other than the two nearly antipodal pentagon-chain rays lies in the opposite open half-plane. The tiny transverse component of one chain ray must balance all of those external forces.

Consequently every unloaded flat pentagon middle is an asymptotic **stress-through coupler**:

$$
\boxed{
{\text{total external contact weight}\over
 \text{two through-chain contact weights}}
=O(\varepsilon),
}
\tag{ST.1}
$$

and the two through-chain weights agree to relative error `O(epsilon)`. This holds for degree three and degree four. In degree four the earlier triangular-fan / three-hidden-chord conclusion remains valid simultaneously.

---

## 1. Coordinate normalization

Let `m` be an unloaded positive-contact-core vertex. Suppose `l,m,r` are consecutive boundary vertices of a bounded face and

$$
|m-l|=|m-r|=1,
\qquad
\theta:=\angle lmr=\pi-\delta,
\qquad
0\le\delta\le\varepsilon<\pi/6.
\tag{ST.2}
$$

Rotate coordinates so

$$
u_l=(1,0),
\qquad
u_r=(-\cos\delta,\sin\delta).
\tag{ST.3}
$$

The open bounded face lies in the sector swept counterclockwise from `u_l` to `u_r`. Every other contact ray at `m` lies in the complementary sector.

Triangle-freeness gives a strict angular gap greater than `pi/3` between every two consecutive contact rays. As proved in the companion note, `deg_C(m)<=4`. Thus there are either one or two external contact rays.

---

## 2. Every external ray has a definite negative transverse component

### Degree three

Let the unique external ray have angle `xi` measured from the positive `x` axis. The two complementary gaps adjacent to it are both greater than `pi/3`, so

$$
{4\pi\over3}-\delta<\xi<{5\pi\over3}.
\tag{ST.4}
$$

For `delta<=epsilon<pi/6`, this interval lies inside `(7pi/6,5pi/3)`. Hence

$$
\boxed{\sin\xi\le-\frac12.}
\tag{ST.5}
$$

### Degree four

Write the three complementary gaps as

$$
{\pi\over3}+a,
\qquad
{\pi\over3}+b,
\qquad
{\pi\over3}+c,
$$

with `a,b,c>0` and

$$
a+b+c=\delta.
\tag{ST.6}
$$

The two external ray angles are therefore

$$
\xi_x={4\pi\over3}-(b+c),
\qquad
\xi_y={5\pi\over3}-c.
\tag{ST.7}
$$

Again `delta<pi/6` gives

$$
\boxed{
\sin\xi_x\le-\frac12,
\qquad
\sin\xi_y\le-\frac12.
}
\tag{ST.8}
$$

So in either degree case every external contact ray contributes a negative `y` component of magnitude at least one half of its contact weight.

---

## 3. Transverse equilibrium kills external stress

Let `alpha_l,alpha_r>0` be the KKT contact coefficients on `ml,mr`, and let

$$
W_{ext}:=\sum_{mx\in E_{ext}(m)}\alpha_{mx}
$$

be the sum over the one or two external contact edges.

Because `m` is unloaded, there is no diameter-force term in its KKT equilibrium:

$$
\alpha_lu_l+\alpha_ru_r
+\sum_{mx\in E_{ext}(m)}\alpha_{mx}u_{mx}=0.
\tag{ST.9}
$$

Take `y` components. The `l` ray contributes zero, the `r` ray contributes `alpha_r sin delta`, and every external term is at most `-alpha_{mx}/2`. Therefore

$$
{1\over2}W_{ext}
\le\alpha_r\sin\delta
\le\alpha_r\sin\varepsilon.
$$

Hence the finite bound

$$
\boxed{
W_{ext}\le2\sin\varepsilon\,\alpha_r.
}
\tag{ST.10}
$$

Since `alpha_l+alpha_r>=alpha_r`,

$$
\boxed{
{W_{ext}\over\alpha_l+\alpha_r}
\le2\sin\varepsilon.
}
\tag{ST.11}
$$

This is uniform over both unloaded degree possibilities.

---

## 4. The two through weights are asymptotically equal

Take `x` components in (ST.9):

$$
\alpha_l-\alpha_r\cos\delta
=-\sum_{mx\in E_{ext}(m)}\alpha_{mx}\cos\xi_x.
$$

Therefore

$$
|\alpha_l-\alpha_r\cos\delta|
\le W_{ext}.
$$

Use (ST.10) and `1-cos(delta)<=1-cos(epsilon)`:

$$
\boxed{
|\alpha_l-\alpha_r|
\le
\bigl(2\sin\varepsilon+1-\cos\varepsilon\bigr)\alpha_r.
}
\tag{ST.12}
$$

In particular

$$
\boxed{
{|\alpha_l-\alpha_r|\over\alpha_l+\alpha_r}
\le2\sin\varepsilon+1-\cos\varepsilon
=O(\varepsilon).
}
\tag{ST.13}
$$

Thus the two stopped-train terminal edges meeting at the flat middle carry asymptotically equal contact stress.

---

## 5. Terminal-train coupling interpretation

The two pentagon boundary edges `ml,mr` are terminal occurrences of complete stopped trains. For every actual nonflat pentagon they belong to distinct trains because a train has one fixed projective contact direction while the two edge directions differ by the positive angle `delta`.

Join those two train vertices by an **abstract terminal-coupling edge** at every unloaded flat middle. Since every complete stopped train has exactly two terminal incidences, this coupling graph has maximum degree two.

Along every coupling edge:

1. the two train projective contact directions differ by at most `epsilon`;
2. their terminal contact stresses differ by relative `O(epsilon)`;
3. the total contact stress leaving the two-ray through channel at the common source vertex is only `O(epsilon)` of the through stress.

This coupling graph does **not** geometrically concatenate the stopped-train centerline arcs. Those centerlines run through rhombus-edge midpoints and are generally transverse to the contact-edge direction. The valid conclusion is only about terminal contact directions and KKT weights. Along a coupling path of bounded combinatorial length, those terminal directions and weights vary by `o(1)` as `epsilon->0`; no embedded pseudosegment or new physical train is asserted.

A long coupling component needs separate control because `epsilon` times its length need not vanish.

---

## 6. Aggregate application

For any pairwise vertex-disjoint family of unloaded flat middles with a common flatness bound `epsilon_D->0`, summing (ST.10) gives

$$
\boxed{
\sum_m W_{ext}(m)
\le2\sin\varepsilon_D
\sum_m\alpha_{mr(m)}.
}
\tag{ST.14}
$$

and summing (ST.12) gives an analogous `o(1)` relative mismatch bound on the two through-edge stress totals.

Thus the small-residual pentagon branch has only two genuinely different local sinks for a flat middle:

- **loaded:** diameter forces may absorb the nearly straight contact stress;
- **unloaded:** the contact system cannot absorb it locally; it must pass through to the second pentagon edge with vanishing leakage.

The unloaded degree-four subcase additionally has the three hidden `1+o(1)` chords from the companion theorem.

This sharpens the next closing problem. A successful proof can now target either a linear population of loaded nearly-flat hull vertices or a max-degree-two network of near-direction, near-weight terminal couplings. The latter is much more rigid than an arbitrary collection of exceptional pentagons, but it is not itself a new train embedding.

---

## 7. Scope audit

- No lower bound on absolute contact stress is asserted.
- The theorem uses unloaded-vertex equilibrium only; loaded middles are deliberately excluded from (ST.9).
- External edges may be shared between different selected middles; the pointwise and summed inequalities remain valid.
- The terminal-coupling graph is a bookkeeping object on stopped trains, not a physical contact graph and not a geometric concatenation of train centerlines.
- No long-component straightness, simultaneous shear, exact hidden contact, or strict diameter decrease is claimed.

**Disposition:** exact local stress-through theorem with audited coupling scope. C-II remains open.
