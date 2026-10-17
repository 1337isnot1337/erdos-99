> Generated reading edition · [exact source](../../research/target_c_low_t_pentagon_object_amplification_2026-09-14.md) · source SHA-256 `0b4226803f343c5776021b367f2c1590303d7fd25b56f9da740bd04af2e2dc3b`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6b359ad5630139c8bde5c8220a48c6a55e8bacad", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_low_t_pentagon_object_amplification_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3d74d98d7f76c9ee32cf483b9c57a05ee1238e123e1f36ba8e1d1cf293bc7996"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - low-t pentagon source-object amplification

**Date:** 2026-09-14  
**Target:** C-II, canonical full-core Type-II branch  
**Dependencies:** low-t pentagon-sea theorem; empty-pentagon trapezoid stability; pentagonal two-contact-tooth extraction; flat-pentagon contact-chain extraction  
**Claim class:** proof-only structural composition awaiting independent audit  
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The low-`t` pentagon-sea theorem gives a substantially larger pentagon population than
the coarse all-Type-II exceptional-face floor used by the existing pentagon source-object
extractions. On the small true-residual branch this population can be fed directly into
the empty-pentagon stability theorem, because all but `o(D)` pentagons have arbitrarily
small residual.

Write

```math
\Delta_2={\pi\over2\sqrt3},\qquad
C_0:=2\sqrt{\Delta_2}+0.00042,
```

and on a convergent Type-II subsequence put

```math
t:=\lim {q-k\over D},\qquad
\delta:=\lim {b-P_F\over D},\qquad
\kappa:=\lim {k\over D}.
```

The low-`t` theorem gives

```math
\boxed{
{p_5\over D}
\ge
P(t,\delta,\kappa)-o(1),
\qquad
P(t,\delta,\kappa)
:=\pi+C_0-{5t\over2}+\delta+{\kappa\over2}.
}
\tag{LO.1}
```

Assume additionally

```math
R_F=o(D).
\tag{LO.2}
```

Then there is a scale `eta_D->0` such that the same pentagon population yields all of
the following actual source-level objects:

```math
\boxed{
{V_{flat}\over D}\ge {P(t,\delta,\kappa)\over5}-o(1),
}
\tag{LO.3}
```

```math
\boxed{
{H_{tooth}\over D}\ge {P(t,\delta,\kappa)\over9}-o(1),
}
\tag{LO.4}
```

and

```math
\boxed{
{C_{flat}\over D},\ {T_{tooth}\over D}
\ge {P(t,\delta,\kappa)\over13}-o(1).
}
\tag{LO.5}
```

Here:

- `V_flat` counts distinct positive-core vertices that are the middle of an exact
  two-edge unit-contact chain with angle `pi-o(1)`;
- `H_tooth` is an endpoint-disjoint matching of hidden chords of length `1+o(1)`, each
  chord having a common positive-core vertex joined to both endpoints by exact unit
  contacts;
- `C_flat` counts pairwise vertex-disjoint near-straight three-vertex unit-contact
  chains; and
- `T_tooth` counts pairwise vertex-disjoint near-equilateral triples with two exact
  unit-contact sides and one inactive side of length `1+o(1)`.

Thus the current low-`t`, small-residual branch carries several macroscopic local
obstructions simultaneously. Near the current proof-only `t` floor the best guaranteed
three-vertex population is about three times the coefficient obtained from the coarse
face floor alone.

## 1. Low-t pentagons survive the residual cut

Let `p_5` be the number of bounded pentagonal exceptional faces. Equation (LO.1) is
exactly the low-`t` pentagon-sea bound.

Fix `eta>0`. The empty-pentagon theorem supplies a positive threshold
`theta(eta)>0` such that a pentagon with

```math
r(P)<\theta(\eta)
```

has no assigned interior isolate and is sufficiently close to the unique flat
unit-trapezoid equality shape to support both source objects used below:

1. its almost-flat middle vertex has two consecutive exact unit-contact neighbors with
   angle greater than `pi-eta`;
2. either leaf gives a two-contact tooth with two exact unit sides and hidden third
   side in `(1,1+eta)`.

All face residuals are nonnegative and sum to `R_F`. Under (LO.2), the number of
pentagons failing the fixed threshold is at most

```math
{R_F\over\theta(\eta)}=o(D).
```

Therefore, if `G_eta` is the number of pentagons simultaneously good for the two local
normal forms,

```math
\boxed{
{G_\eta\over D}
\ge P(t,\delta,\kappa)-o(1).
}
\tag{LO.6}
```

Unlike the earlier weighted formulas `X+G_eta>=f_*D-o(D)`, this composition does not
subtract `X=Q-f`: the low-`t` theorem has already counted actual pentagons after paying
all higher-degree exceptional faces.

## 2. Distinct flat centers

Choose the distinguished almost-flat middle vertex from every good pentagon. A source
vertex of a triangle-free unit-contact graph has contact degree at most five and hence
belongs to at most five bounded face sectors. Therefore no source vertex can be chosen
as the middle of more than five good pentagons. Consequently

```math
5V_{flat}(\eta)\ge G_\eta.
\tag{LO.7}
```

Combining with (LO.6) proves the fixed-`eta` form of (LO.3).

## 3. Endpoint-disjoint two-contact teeth

Choose one leaf tooth in every good pentagon, and retain only its hidden chord. Each
endpoint lies on at most five selected bounded faces. Thus a chosen hidden chord
conflicts with at most four other chosen chords through each endpoint, for conflict
degree at most eight. Greedy matching gives

```math
9H_{tooth}(\eta)\ge G_\eta.
\tag{LO.8}
```

Together with (LO.6), this proves the fixed-`eta` form of (LO.4).

Every hidden chord is strictly longer than one in the actual source. Equality would be
a nonconsecutive unit contact across a convex contact face, splitting the face and, in
the local leaf triple, producing a forbidden unit equilateral triangle.

## 4. Vertex-disjoint chains and teeth

For the flat-chain object, retain the three vertices `l-m-r`. For the tooth object,
retain its three vertices. In either conflict graph a selected object has three source
vertices, and through each source vertex at most four other selected objects arise from
other bounded faces. Hence the maximum conflict degree is at most twelve. A greedy
independent set gives

```math
13C_{flat}(\eta)\ge G_\eta,
\qquad
13T_{tooth}(\eta)\ge G_\eta.
\tag{LO.9}
```

Combining with (LO.6) proves the fixed-`eta` version of (LO.5).

The two independent sets need not be the same family of pentagons. Equations (LO.5)
assert two simultaneous lower bounds on the maxima of the two extraction problems;
they do not assert `2P/13` disjoint objects in one common packing.

## 5. Vanishing-gap diagonalization

Apply the preceding fixed-`eta` theorem to `eta_j=1/j`. Since `R_F/D->0`, choose a
nondecreasing `j(D)->infinity` slowly enough that

```math
{R_F\over D\,\theta(\eta_{j(D)})}\to0.
```

Set `eta_D=eta_{j(D)}`. Then `eta_D->0` and the same first-order coefficients in
(LO.3)--(LO.5) survive. In particular the flat-chain turn tends to zero and the tooth
hidden-side excess tends to zero.

## 6. Numerical consequences

The current proof-only orbit/detour floor is

```math
t_{42}
={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0013751
=1.8208886379794447\ldots .
```

At the most permissive `delta=kappa=0`, the low-`t` theorem gives

```math
P(t_{42},0,0)=0.4944166723690961\ldots .
\tag{LO.10}
```

Hence, on the small-residual branch at that profile,

```math
\boxed{{V_{flat}\over D}\ge0.0988833344738192\ldots-o(1),}
\tag{LO.11}
```

```math
\boxed{{H_{tooth}\over D}\ge0.0549351858187884\ldots-o(1),}
\tag{LO.12}
```

and

```math
\boxed{
{C_{flat}\over D},\ {T_{tooth}\over D}
\ge0.0380320517206997\ldots-o(1).
}
\tag{LO.13}
```

The old coarse flat-chain/tooth coefficient was

```math
{f_*\over13}=0.0128557418051160\ldots,
```

so (LO.13) improves that three-vertex extraction by a factor greater than `2.95` at
the current `t_42` profile.

Conditionally on any small-residual subsequence with

```math
t\le1.8585,
```

and again dropping the nonnegative `delta,kappa` bonuses, one has

```math
P\ge0.4003882673177079\ldots,
```

therefore

```math
{V_{flat}\over D}\ge0.0800776534635415\ldots-o(1),
```

```math
{H_{tooth}\over D}\ge0.0444875852575231\ldots-o(1),
```

and

```math
{C_{flat}\over D},\ {T_{tooth}\over D}
\ge0.0307990974859775\ldots-o(1).
\tag{LO.14}
```

This `t<=1.8585` statement is conditional only; it does not extend the separate
endpoint/common-cap exclusion theorem to arbitrary Type-II sequences.

## 7. Frontier effect

This composition removes a bookkeeping loss, not the final geometric obstruction. In
the low-`t`, small-residual region, the survivor must now realize simultaneously:

```text
~0.1 D distinct nearly straight positive-core contact centers,
~0.055 D endpoint-disjoint hidden 1+o(1) chords with two-contact support,
~0.038 D vertex-disjoint nearly straight exact-contact chains,
~0.038 D vertex-disjoint two-contact near-equilateral teeth,
```

at the current `t_42` profile, before any positive `delta` or `kappa` bonus is used.

The next closing theorem should exploit a relation between these local pentagonal
objects and the global diameter system. A promising finite target is the loaded/unloaded
split of the flat middle vertices: an unloaded middle must have an additional positive
contact by the canonical degree-`3,4,5` theorem, whereas a loaded middle lies on the
force hull and has contact degree at most three. The almost-flat face angle strongly
restricts where such additional contact rays can lie.

No exact hidden contact, unit equilateral triangle, or same-cardinality strict sub-`D`
competitor is proved here.

## 8. Scope audit

- The theorem is conditional on the proof-only AG42 low-`t` theorem and on `R_F=o(D)`.
- `p_5` in (LO.1) is the actual pentagon count; no second payment by `Q-f` is made.
- Wegner first-jump and empty-pentagon stability ensure the good pentagons have no
  assigned interior source points.
- Every counted vertex is an actual source vertex in the positive-contact core.
- The factors `5`, `9`, and `13` are the same source-incidence/conflict constants
  already used in the independently stated pentagon extraction theorems.
- The low-`t` and small-residual hypotheses are both retained; neither is inferred from
  the other.
- C-II and Level I remain open.
