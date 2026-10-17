> Generated reading edition · [exact source](../../research/target_c_exact_two_face_network_2026-09-14.md) · source SHA-256 `dd99667e193a23d80d5cf04d4bce99e7b9831e80f9d72ce20a9a509ca1ac23c3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9c3b3fa52149db5dad548151bd8d25420486c4e4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_exact_two_face_network_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0f27c82778b926e594416d399369d1265af6da949fc53192770244db3038f820"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - exact-two flat-face network near the weighted endpoint

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** weighted outer-flex near-equality theorem; bounded-face loop exclusion; bounded-face endpoint simplicity; exact flat-pentagon phase-star theorem
**Claim class:** proof-only structural reduction awaiting independent audit

## LEVEL I STATUS

`STILL OPEN`

Near the sharp weighted outer-flex endpoint, almost every bounded exceptional face is a good pentagon carrying exactly two outer-to-flat trains. The other three terminal trains of each such pentagon therefore run to other bounded faces. Bounded-loop and repeated-endpoint exclusion turn those remaining trains into an almost cubic simple graph on the flat pentagons.

On an `R_F=o(D)` low-`t` subsequence let

$$
q={Q\over D}=2t-\pi-\delta+o(1),
$$

and assume the near-equality branch

$$
{\dim K_{out}\over D}\le F(t,\delta,\kappa)+\eta+o(1)
\tag{FN.1}
$$

for fixed `eta>0`. Let `V_2` be the set of good flat pentagons carrying exactly two outer-to-flat trains. The weighted stability theorem gives

$$
\boxed{{|V_2|\over D}\ge q-2\eta-o(1).}
\tag{FN.2}
$$

Define `Gamma_2` with vertex set `V_2`, joining two vertices when one complete stopped train has one terminal occurrence on each face. Then `Gamma_2` is finite, simple, loop-free, has maximum degree three, and satisfies

$$
\boxed{{|E(\Gamma_2)|\over D}\ge {3q\over2}-9\eta-o(1),}
\tag{FN.3}
$$

$$
\boxed{{|\{v\in V_2:\deg_{\Gamma_2}v=3\}|\over D}\ge q-14\eta-o(1),}
\tag{FN.4}
$$

and

$$
\boxed{{\beta_1(\Gamma_2)\over D}\ge {q\over2}-9\eta-o(1).}
\tag{FN.5}
$$

At `t=t_21`, `delta=kappa=0`, and `eta=0.005`,

$$
|V_2|>0.4908901D-o(D),
$$

$$
|E(\Gamma_2)|>0.7063352D-o(D),
$$

$$
|\{\deg=3\}|>0.4308901D-o(D),
$$

and

$$
\boxed{\beta_1(\Gamma_2)>0.2054450D-o(D).}
\tag{FN.6}
$$

Every vertex simultaneously carries the exact finite flat-pentagon phase-star signature: its five terminal train axes split into a majority triple and minority pair whose possible strict-rhombus crossings form a subgraph of `K_{3,2}`. Thus the weighted near-equality model reduces to a simple near-cubic graph with linear cycle rank and a five-half-edge local phase label at every vertex.

This does not by itself contradict mixed rigidity. It identifies a concrete next target: control phase holonomy or diameter locking around the linear cycle space of `Gamma_2`.

## 1. High-degree excess collapses automatically

The exact-two faces are bounded exceptional faces, so `|V_2|<=f<=Q`. Combining with (FN.2) gives

$$
0\le {Q-f\over D}\le2\eta+o(1),
\qquad
0\le {f-|V_2|\over D}\le2\eta+o(1).
\tag{FN.7}
$$

Let `I_bad` be the total number of bounded-face boundary incidences belonging to exceptional faces outside `V_2`. Since `sum_F deg F=Q+4f` and every face in `V_2` is a pentagon,

$$
I_{bad}=Q+4f-5|V_2|=(Q-f)+5(f-|V_2|),
$$

so

$$
\boxed{I_{bad}\le(12\eta+o(1))D.}
\tag{FN.8}
$$

## 2. Three bounded-to-bounded stubs at every exact-two face

The train-star theorem says the five boundary sides of every good flat pentagon belong to five distinct complete stopped trains. Exactly two have their other terminal occurrence on the actual outer face. The remaining three therefore have their other terminal occurrence on a bounded stopping face.

At most `I_bad` of the resulting `3|V_2|` bounded-to-bounded stubs can end outside `V_2`. All remaining stubs pair between two `V_2` faces. Hence

$$
2|E(\Gamma_2)|\ge3|V_2|-I_{bad},
$$

and (FN.2), (FN.8) prove (FN.3).

## 3. Simplicity and degree-three population

A complete train cannot return to the same bounded face, so `Gamma_2` has no loops. Bounded-face endpoint simplicity says two distinct complete trains cannot join the same pair of bounded faces, so it has no repeated edges.

Each `V_2` face has exactly three bounded-to-bounded stubs, so `deg v<=3`. The total deficit from degree three is

$$
\sum_{v\in V_2}(3-\deg v)=3|V_2|-2|E(\Gamma_2)|\le I_{bad}\le(12\eta+o(1))D.
$$

Every vertex of degree at most two contributes at least one unit. Equations (FN.2), (FN.8) prove (FN.4).

## 4. Linear cycle rank

For any finite graph with `c` connected components,

$$
\beta_1=|E|-|V|+c\ge|E|-|V|.
$$

Using (FN.3) and `|V_2|<=Q=qD+o(D)` gives (FN.5).

At `t=t_21`, `delta=0`, `q_0=2t_21-pi=0.500890222369096...`; setting `eta=0.005` yields (FN.6).

## 5. Exact local phase decoration

The exact flat-pentagon phase-star theorem applies at every vertex of `V_2` after the common slow flatness diagonal is chosen. Three majority axes are pairwise on the noncrossing side of the `pi/3` threshold, the two minority axes are also on the noncrossing side, and every possible strict-rhombus crossing among the five is majority-to-minority.

An edge of `Gamma_2` is one physical complete train and therefore has one projective axis seen from both endpoint pentagons. This theorem does not claim that full three-phase frames agree globally along long graph paths; flatness error can accumulate. It records only the exact finite local `K_{3,2}` crossing-eligibility signature and the large graph cycle space on which a future phase-holonomy theorem can act.

## 6. Scope audit

- The theorem is a near-equality consequence of the weighted outer-flex theorem, not an unconditional statement about all low-t survivors.
- `V_2` contains actual good flat pentagons and exactly two actual outer-to-flat complete trains per face.
- `I_bad` uses occurrence-counted face degree; repeated boundary vertices cause no error.
- Simplicity imports both bounded-face loop exclusion and bounded-face endpoint simplicity.
- The cycle-rank estimate is purely graph-theoretic and does not identify endpoint cycles with rhombic holes.
- No global phase frame is propagated around long cycles; only the finite local phase-star signature is asserted.
- No exact unit triangle or same-cardinality strict sub-D competitor is produced.

**Disposition:** new proof-only near-equality network reduction. C-II and Level I remain open.
