> Generated reading edition · [exact source](../../../docs/reports/target_c_mu4_train_pairing_endpoint_exclusion_2026-09-12.md) · source SHA-256 `0e84c74095c030d6ee5005b71e31c5be0913af3dd512777732b6295d333f34ef`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0979E8CA8A01","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_mu4_train_pairing_endpoint_exclusion_2026-09-12.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=54eba7f3c570455763f6dd58d16b7721424fbaf9; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C — train-pairing exclusion of the Section-96 `mu_4` endpoint

**Date:** 2026-09-12  
**Target:** C-II  
**Classification:** unreviewed conditional candidate; unpromoted endpoint audit

## Candidate implication

```text
Section-96 equality at mu_4, with endpoint support saturation
 -> saturated attachment support and exact carrier area
 -> three outer routes have distinct projective directions
 -> their train endpoints pair only within the same route, up to o(D)
 -> same-route trains have o(D) transverse span
 -> 2 area(P) <= alpha_4 mu_4 D^2 + o(D^2)
 -> contradiction with the endpoint carrier area.
```

This is an endpoint exclusion, not a claim that every wrapping cell is impossible.
It uses no KKT coefficient lower bound and retains all source points.

## 1. Endpoint data

Use the canonical Section-96 wrapping notation. Let `P_D=conv(A_D)` be a
wrapping harmonic cell, `d_D=diam(P_D)`, and `a_D=|A_D|`. Assume

$$
 d_D/D\to\mu_4,
 \qquad
 \theta_4=2\arcsin\mu_4,
 \qquad
 \phi_4=2\pi-2\theta_4.
$$

The Section-96 equality equation is

$$
 \alpha_4:=3\theta_4-2\pi={3\over2}\sin\theta_4,
 \qquad
 \mu_4=0.936215741409583\ldots .
$$

The endpoint outer-walk audit gives

$$
 {a_D\over D}\to\alpha_4,
 \qquad
 Q_D+s_D+c_D=o(D),
 \qquad
 L_D=4\alpha_4D+o(D),
$$

and three distinguished outer routes with chord length
`sin(theta_4)D+o(D)` and total path excess `o(D)`.

The endpoint support-saturation argument gives a normalized attachment measure equal
to one-half of Lebesgue measure on the six allowed arcs, whose total angular measure
is `2 alpha_4`. Consequently

$$
 {\operatorname{area}(P_D)\over D^2}
 \longrightarrow
 A_4:= {\pi\over4}-{3\over8}(\phi_4-\sin\phi_4)
 =0.618374879828757\ldots .
\tag{E.1}
$$

The local rhombic deficit is `o(D^2)`, so the strict-rhombus complex in this cell
has the same limiting area.

## 2. Boundary train endpoints; bridge edges are irrelevant

Let `mathcal R_D` be the strict-rhombus complex in the carrier. The exact train
decomposition gives two boundary ends per train. Define `b_D` to be the number of
outer-walk edge occurrences incident to no strict rhombus. The Section-82 face ledger
shows that the part of `b_D` facing bounded nonquadrilateral faces is `O(Q_D)=o(D)`;
the remaining part consists of outer-face bridge occurrences. These bridge occurrences
are not train ends: an edge incident to no strict rhombus belongs to no local train.
Every actual train end is incident either with the outer face of the induced carrier
graph or with a bounded nonquadrilateral face. Since the latter contribute at most
`5Q_D=o(D)` edge occurrences, we have, without any assumption on `b_D`,

$$
\boxed{\text{all but }o(D)\text{ train ends lie on the outer attachment routes}.}
\tag{E.2a}
$$

This is the only endpoint accounting used below. A linear family of outer-face
bridges may remain, but it removes train ends rather than creating an additional
train-pairing case.

Call the three long routes `W_{1,D},W_{2,D},W_{3,D}`. Their chord directions have
limits given by the midpoints of the three forbidden arcs. A unit path with `o(D)`
excess over a chord has all but `o(D)` of its edge directions in every fixed
neighborhood of the chord direction: this follows from

$$
 \sum_k(1-q\cdot z_k)=\ell-|u-v|=o(D)
$$

and `1-cos(t)\ge c_eta` outside an `eta`-neighborhood.

The endpoint count gives the needed stronger gap stability. Let `h_{i,D}` be the
ordinary cyclic attachment gaps inside the six allowed arcs. The annular
unit-separation estimate gives, uniformly,

$$
h_{i,D}\ge \ell_D:={r_D\over R_D^2},\qquad D\ell_D\to2.
\tag{E.2b}
$$

The saturated support has total allowed angular length `2alpha_4`, while
`a_D=alpha_4D+o(D)`. Hence

$$
\sum_i(h_{i,D}-\ell_D)=o(1).
\tag{E.2c}
$$

Consequently, after deleting `o(D)` ordinary intervals, their gaps satisfy
`h_{i,D}=(2+o(1))/D`; after also deleting `o(D)` intervals, their routes have
exactly two edges. The next local step uses convexity, not annular convergence
alone. Saturated support implies

$$
 D^{-1}P_D\longrightarrow P_4:=\operatorname{conv}(U_4)
\tag{E.2d}
$$

in Hausdorff distance, where `U_4` is the six-arc circle support. Away from the
finitely many arc endpoints, `P_4` has the circle as a supporting boundary arc.
Thus a short side `pq` of `P_D` whose angular midpoint stays in such a compact
subarc has a supporting line converging to the corresponding circle tangent. For
the two-edge route `p-x-q`, the side length is at most two. In tangent/normal
coordinates for its supporting line, the normalized endpoints converge to the
same circle point, their tangential coordinates differ by at most two, and their
normal coordinate is `(1/2+o(1))D`; hence `||p|-|q||=o(1)`. Together with
`arg(q)-arg(p)=(2+o(1))/D`, this gives

$$
 |p-q|=1+o(1).
\tag{E.2e}
$$

For a fixed endpoint-neighborhood width `epsilon`, the annular density bound gives
`O(epsilon D)+o(D)` intervals there; let `epsilon` tend to zero after taking the
normalized limit. Thus, outside a family of `o(D)` intervals, the two contact
directions are, up to `o(1)`, the two directions
obtained from the local circle tangent by the fixed `60`-degree offsets. The
saturated attachment density is bounded on each allowed arc. Therefore, for any
fixed projective direction `v` and any `eta>0`, the ordinary route edges whose
directions lie within `eta` of `v` are bounded by `O(eta D)+o(D)`: their attachment
endpoints lie in finitely many angular windows of width `O(eta)+o(1)`. Letting
`eta` tend to zero gives

$$
\boxed{\text{only }o(D)\text{ ordinary route edges approach any fixed projective direction}.}
\tag{E.2d}
$$

## 3. The three long directions are distinct

The forbidden arcs have length

$$
 \phi_4=1.4363743902\ldots <\pi/2.
$$

Two equal-length circular chords have the same projective direction exactly when
their arc midpoints are antipodal. If two of the three forbidden arcs had antipodal
midpoints, their complements would contain two antipodal allowed subarcs, each of
length `pi-phi_4`. The third forbidden arc has length `phi_4`, and cannot meet both
of those complementary subarcs in a way that removes every antipodal pair. Hence the
allowed support would contain antipodal points, contradicting its diameter
`mu_4<1`.

Therefore the three limiting long-route projective directions are pairwise distinct.
In particular, after deleting `o(D)` exceptional edges, a train cannot have long
route ends on two different long routes: opposite train edges are parallel.

## 4. Long-route trains have negligible span

If both ends of a train lie on the same `W_{j,D}`, their edge directions and the
route itself are within `o(D)` of one chord segment. The transverse distance between
the two terminal edge midpoints is consequently `o(D)`. The train's exact transverse
span is at most this distance, so the total span of all same-route long trains is
`o(D^2)`.

An ordinary-route end can pair with a long-route end only among the `o(D)` ordinary
edges whose projective directions approach that long direction. Since every train
span is at most `d_D=O(D)`, all such mixed trains contribute `o(D^2)` in total.

After also discarding the `o(D)` nonquadrilateral boundary ends, all remaining
non-negligible-span trains have two ordinary-route ends. There are at most

$$
 a_D+o(D)=\alpha_4D+o(D)
$$

such trains, because the ordinary routes contain `2a_D+o(D)` boundary edges and
each train has two ends.

## 5. Area contradiction

For each train, the sum of its rhombus transverse advances equals its exact
transverse span. Every terminal edge midpoint lies in `P_D`, so every train span is
at most `d_D`. Each strict rhombus belongs to two trains. Thus

$$
 2\operatorname{area}(P_D)-o(D^2)
 \le
 (\alpha_4D+o(D))d_D+o(D^2).
$$

Dividing by `D^2` and using (E.1) gives the necessary endpoint inequality

$$
 2A_4\le\alpha_4\mu_4.
\tag{E.2}
$$

But exact arithmetic gives

$$
 2A_4=1.236749759657516\ldots,
 \qquad
  \alpha_4\mu_4=0.924074023352554\ldots,
$$

so (E.2) is false by a fixed positive margin. Therefore no canonical Type-II
wrapping-cell sequence satisfying the endpoint support-saturation hypotheses can
converge to the Section-96 endpoint `mu_4`.

## 6. Scope and remaining gap

The result gives a qualitative strict improvement for the endpoint-saturated branch:

$$
 \liminf {\operatorname{diam}(P_D)\over D}>\mu_4
$$

for any family of wrapping cells satisfying the endpoint compactness and
support-saturation hypotheses. The argument does not supply an explicit gap and does
not address wrapping limits strictly above `mu_4` or the macroscopic inactive-container
branch. A linear rhombus-free/bridge boundary corridor is harmless to this particular
endpoint pairing argument, although it remains relevant to other endpoint-count
arguments.

The next canonical quantity is the first wrapping-cell diameter above `mu_4`; a
quantitative stability version of the same train-pairing estimate could raise the
current threshold explicitly.

## Claim classification

| Claim | Classification |
|---|---|
| endpoint support and area formulas | proved candidate, dependent on the endpoint-saturation audit |
| distinct long-route projective directions | proved candidate |
| train-pairing area contradiction at `mu_4` | proved candidate, conditional on support saturation |
| exclusion of the bridge branch for other arguments | open |
| global exclusion of the `mu_4` endpoint | open pending support-saturation audit |
| C-II closure | open |
