> Generated reading edition · [exact source](../../research/target_c_flat_pentagon_activation_matching_refinement_2026-09-14.md) · source SHA-256 `b94e5b6bcc59373c18df432da4244c3345e479f5600b5e40ae9d5286dbf2d5ab`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0babe91d9c63ebd73f37132785dcf4a03f940f20", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_flat_pentagon_activation_matching_refinement_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e94d96fed5dff581256654bd9c19e95648a93d511377ca0a65f56a34efcf71da"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - flat-pentagon activation matching refinement

**Date:** 2026-09-14
**Target:** C-II, canonical contact-minimal full-core Type-II branch
**Dependencies:** low-t flat-center amplification; pentagon hidden-contact gap budget; triangle-free contact-angle separation
**Claim class:** proof-only structural refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The current low-`t` endpoint contains a large population of cheap pentagons. Two
separate committed theorems record complementary information about them:

1. the flat-center theorem gives strong angular sectors at the middle and shoulders;
2. the hidden-gap theorem shows that pentagon residual pays linearly for opening the
   two missing center-to-shoulder contacts.

Keeping both pieces simultaneously improves the extraction constants. On a convergent
Type-II subsequence write

$$
t=\lim{q-k\over D},\qquad
\delta=\lim{b-P_F\over D},\qquad
\kappa=\lim{k\over D},
$$

and put

$$
\Delta_2={\pi\over2\sqrt3},\qquad
C_0=2\sqrt{\Delta_2}+0.00042,
$$

$$
A(t,\delta,\kappa)
=\pi+C_0-{5t\over2}+\delta+{\kappa\over2}.
\tag{AM.1}
$$

Fix any constant

$$
0<c<{2\over3}.
\tag{AM.2}
$$

There is a fixed residual threshold `theta_c>0` such that, after deleting at most
`R_F/theta_c` pentagons, every retained pentagon has:

- a flat-center sector larger than `11pi/12`;
- both shoulder sectors larger than `7pi/12`;
- two hidden center-to-shoulder diagonals `x,y>1`; and
- residual

$$
r(P)\ge c[(x-1)+(y-1)].
\tag{AM.3}
$$

Let `G_c` be the retained population. The low-`t` pentagon floor gives

$$
\boxed{
G_c\ge A(t,\delta,\kappa)D-{R_F\over\theta_c}-o(D).
}
\tag{AM.4}
$$

Choose from every retained pentagon the shorter hidden center-to-shoulder chord and
the corresponding two-contact tooth. Then there are simultaneously:

- an endpoint-disjoint hidden-chord family `H_act`;
- a vertex-disjoint two-contact-tooth family `T_act`; and
- a vertex-disjoint near-straight middle-chain family `C_flat`;

satisfying

$$
\boxed{|H_{act}|\ge {G_c\over4},}
\tag{AM.5}
$$

$$
\boxed{|T_{act}|\ge {G_c\over12},\qquad
       |C_{flat}|\ge {G_c\over12}.}
\tag{AM.6}
$$

The activation families also keep the global `L^1` gap budget

$$
\boxed{
\sum_{e\in H_{act}}(|e|-1)
\le {R_F\over2c},
\qquad
\sum_{\tau\in T_{act}}g(\tau)
\le {R_F\over2c}.
}
\tag{AM.7}
$$

For example `c=3/5` gives the safe coefficient `5R_F/6` in (AM.7). Since `c` may be
chosen arbitrarily close to `2/3`, the coefficient may be taken arbitrarily close to
`3/4`, at the cost of shrinking the fixed residual threshold.

Equivalently, the finite-source tradeoffs are

$$
\boxed{
4|H_{act}|+{R_F\over\theta_c}
\ge A(t,\delta,\kappa)D-o(D),
}
\tag{AM.8}
$$

$$
\boxed{
12|T_{act}|+{R_F\over\theta_c}
\ge A(t,\delta,\kappa)D-o(D),
}
\tag{AM.9}
$$

and the same factor-12 inequality holds for `C_flat`.

## 1. Residual-to-gap estimate with the shorter hidden chord

Use the flat-trapezoid cyclic labels `l,m,r,a,b`, where `m` is the almost-flat
middle and `a,b` are the two shoulders. Put

$$
x=|m-a|,\qquad y=|m-b|.
$$

The committed hidden-gap theorem gives the exact area parametrization

$$
A(P)=F(x)+G(x,y)+F(y)
$$

and endpoint derivatives

$$
\partial_x r(1,1)=\partial_y r(1,1)={2\over3}.
$$

Therefore for every fixed `c<2/3`, continuity gives a neighborhood in which (AM.3)
holds. Tighten the flat-pentagon residual threshold so that retained pentagons lie in
that neighborhood and have the angular bounds used below.

If

$$
g(P)=\min\{x-1,y-1\},
$$

then

$$
g(P)\le{(x-1)+(y-1)\over2}\le {r(P)\over2c}.
\tag{AM.10}
$$

Choose the corresponding shorter hidden chord. Summing (AM.10) over all retained
pentagons and using nonnegativity of the face residuals gives

$$
\sum_{P\in G_c}g(P)\le {R_F\over2c}.
\tag{AM.11}
$$

Every subsequent extraction is a subset of this chosen family, so the same upper
bound survives and proves (AM.7).

## 2. Endpoint-disjoint hidden chords lose only a factor four

Every chosen hidden chord joins a flat center to one shoulder of its pentagon.

At its center endpoint the current pentagon occupies a sector larger than
`11pi/12`. Any other chosen hidden chord using that vertex must come from a pentagon
where the vertex is either a center or a shoulder, and hence occupies a sector larger
than `7pi/12`. The complementary angular room is smaller than `13pi/12`, so at most
one such additional sector fits. Thus the center endpoint has chosen-chord incidence
at most two.

At the shoulder endpoint the current sector is larger than `7pi/12`, leaving less
than `17pi/12`. Every other chosen chord using that vertex again comes from a center
or shoulder sector larger than `7pi/12`. At most two additional such sectors fit, so
the shoulder endpoint has chosen-chord incidence at most three.

Hence one chosen chord conflicts with at most

$$
(2-1)+(3-1)=3
$$

other chosen chords. Greedy matching retains at least `G_c/4`, proving (AM.5).
This argument does not need a global bound of five on both endpoints; it uses the
actual flat-center/shoulder sector types.

## 3. Vertex-disjoint teeth lose only a factor twelve

A chosen tooth consists of three vertices:

1. the flat center `m`;
2. the chosen shoulder; and
3. the intervening boundary leaf joined by the two exact unit contacts.

Triangle-freeness implies every sector between consecutive contact rays is strictly
larger than `pi/3`.

At the flat center, the current sector exceeds `11pi/12`, leaving less than
`13pi/12`; therefore at most three other bounded-face sectors can occur there. A
selected tooth conflicts through its center with at most three other selected teeth.

At the shoulder, the current sector exceeds `7pi/12`, leaving less than `17pi/12`;
therefore at most four other sectors larger than `pi/3` can occur. This contributes
at most four conflicts.

At the leaf, the generic triangle-free contact-degree bound gives at most five face
incidences, hence at most four other selected teeth.

Thus the tooth-conflict graph has maximum degree at most

$$
3+4+4=11.
\tag{AM.12}
$$

A greedy independent set retains at least `G_c/12`, proving the first part of
(AM.6).

## 4. The same factor twelve improves flat-chain extraction

For the near-straight middle chain `l-m-r`, the middle vertex is again the flat
center and each endpoint is a generic boundary leaf. The same incidence bounds give
at most

$$
3+4+4=11
$$

conflicts with other selected middle chains. Therefore

$$
|C_{flat}|\ge {G_c\over12}.
\tag{AM.13}
$$

This improves the previous generic denominator `13`. No uniqueness theorem for flat
centers is required for this particular improvement; the large sector of the selected
pentagon already reduces the middle-vertex incidence by one.

## 5. Numerical low-t consequences

The current proof-only orbit/detour floor is

$$
t_{42}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0013751
=1.8208886379794447\ldots .
$$

At the permissive endpoint profile `delta=kappa=0`,

$$
A(t_{42},0,0)=0.4944166723690961\ldots .
$$

On `R_F=o(D)`, (AM.5)--(AM.6) give

$$
\boxed{{|H_{act}|\over D}
\ge0.1236041680922740\ldots-o(1),}
\tag{AM.14}
$$

$$
\boxed{{|T_{act}|\over D},\ {|C_{flat}|\over D}
\ge0.0412013893640913\ldots-o(1).}
\tag{AM.15}
$$

Throughout `t<=1.8585`, dropping the nonnegative `delta,kappa` bonuses gives

$$
A(t,\delta,\kappa)\ge0.4003882673177079\ldots,
$$

hence

$$
\boxed{{|H_{act}|\over D}
\ge0.1000970668294269\ldots-o(1),}
\tag{AM.16}
$$

$$
\boxed{{|T_{act}|\over D},\ {|C_{flat}|\over D}
\ge0.0333656889431423\ldots-o(1).}
\tag{AM.17}
$$

Thus the strongest current small-residual pentagon endpoint has, simultaneously, a
roughly `0.1236D` endpoint-disjoint near-contact matching with `O(R_F)` total gap and
a roughly `0.0412D` vertex-disjoint tooth/flat-chain family.

## 6. Quantile form of the activation budget

Let `N=|H_act|` and let

$$
B={R_F\over2c}.
$$

For every fixed `0<lambda<1`, Markov's inequality applied to the nonnegative hidden
gaps shows that at least `(1-lambda)N` chords satisfy

$$
|e|-1\le {B\over\lambda N}.
\tag{AM.18}
$$

For `c=3/5` and `lambda=1/2`, at least half of `H_act` has gap at most

$$
{5R_F\over3N}.
\tag{AM.19}
$$

Near `t_42`, using `N/D>=A(t_42,0,0)/4-o(1)`, this gives at least
`0.0618020840...D-o(D)` endpoint-disjoint hidden chords with gap at most

$$
\left({20\over3A(t_{42},0,0)}+o(1)\right){R_F\over D}
<13.49{R_F\over D}
\tag{AM.20}
$$

along the small-residual branch. This is stronger than a bare `1+o(1)` statement: the
near-contact scale is explicitly tied to the normalized residual.

## 7. Scope and remaining obstruction

- The low-`t` population constant inherits the proof-only AG42 input.
- The residual-to-gap estimate is local to sufficiently cheap isolate-free pentagons.
- The factor-four and factor-twelve losses are finite combinatorial consequences of
  angular sectors; no KKT multiplier lower bound is used.
- `H_act` is endpoint-disjoint in the hidden chord endpoints. `T_act` is fully
  vertex-disjoint in all three tooth vertices.
- The activation budget does not itself produce a legal simultaneous motion. The
  vertices belong to the positive contact core, so the protected-isolate motion
  theorem does not apply.
- No exact hidden contact, strict sub-`D` competitor, or C-II contradiction is claimed.

The next useful theorem must exploit the much denser activation-ready matching without
silently treating core vertices as free isolates. A viable route must either build a
core-compatible finite motion or charge these `O(R_F)` total hidden gaps against the
loaded/degree-three/degree-four KKT split.

C-II and Level I remain open.
