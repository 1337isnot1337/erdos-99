> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_order_chamber_planar_obstruction_2026-09-18.md) · source SHA-256 `85932a8598dd03e612c33e878496e020bc3685bb527908c75c6a1e640d652665`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "61c63566baa6fdd6ef41ff7bae3a1f9473bde64c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_order_chamber_planar_obstruction_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "763e7d47c105fdae0e0c30c1c3bfa86f46fda332f186329d129c16e06d1c96a6"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — one collapsed support-six order chamber has no planar train routing

**Date:** 2026-09-18  
**Status:** proved conditional candidate; theorem-state authority unchanged  
**Scope:** the certified collapsed local closure box from `target_c_support6_collapsed_local_realization_2026-09-18.md`  
**Depends on:** the collapsed local contraction certificate; audited finite train primitives; the audited bounded-face endpoint-fan theorem  
**Certificate:** `research/verify_target_c_support6_collapsed_order_chamber_planar_obstruction_2026_09_18.py`  
**Classification:** local-order-chamber exclusion; C-II remains open

The certified collapsed branch is not globally realizable in its recorded cyclic-order
chamber, even after allowing train crossings. The obstruction is finite and exact:

$$
\boxed{\text{the certified six-face octahedral terminal rotation has no planar train
routing compatible with its allowed crossings}.}
$$

This does not exclude the collapsed branch universally. It excludes only the regular
local order chamber certified by the existing contraction box; other collapsed metric
components or order chambers still require analysis.

## 1. Terminal graph and fixed rotations

The twelve internal relation trains are the edges of

$$
G=K_6\setminus\{03,14,25\},
$$

the octahedral graph. Contract each bounded stopping face to a vertex and each complete
train to an edge. The certified face orders induce a cyclic rotation of the four
incident train ends at every vertex. With no crossings, the resulting rotation system
has

$$
(V,E,F)=(6,12,4),\qquad \chi=-2,
$$

and hence genus two.

## 2. Exact restrictions on allowable crossings

Two complete trains crossing in a strict rhombus must have projective direction gap
strictly greater than `pi/3`; the exact interval calculation in the verifier classifies
all 66 train pairs in the contraction box. It leaves seven pairs whose endpoint faces
are disjoint and whose angle gap passes this necessary threshold.

The endpoint-fan theorem independently forbids two trains sharing a bounded stopping
face from crossing. The train crossing graph is simple and triangle-free. Therefore a
legal routing may use only subsets of those seven candidate crossing pairs, with no
repeated crossing pair and no triangle in the crossing graph. A train may cross several
other trains, so the certificate also exhausts every possible order of multiple
crossings along each train.

## 3. Exact planarization enumeration

For each legal crossing subset, subdivide every crossed train at its crossing points.
For every train, enumerate all orders of its crossing points along the train. At each
crossing vertex, impose the alternating four-half-edge rotation required by a proper
crossing. The original six vertex rotations remain fixed.

The verifier computes the face permutation of every resulting rotation system using
integer combinatorics. A planar routing would have

$$
F=E-V+2=8+k
$$

faces when `k` crossings are inserted. Exhausting all `2^7` candidate subsets, all
legal crossing-graph choices, all multiple-crossing orders, and both alternating
crossing rotations gives zero planarizations.

Thus the recorded local cyclic order cannot be extended to a planar stopped-train
complex, even with all angle-eligible bounded-face-disjoint crossings. The result uses
no floating-point geometric decision.

## 4. Binding limitation

The contraction certificate proves one regular two-parameter local family, not every
collapsed solution of the octahedral closure equations. Consequently this result is a
genuine exclusion of one certified local chamber, not a global exclusion of collapsed
support six. A universal theorem must classify the remaining collapsed cyclic orders or
derive a chamber-independent global constraint.

**Disposition:** exact local-order-chamber planar obstruction; no theorem-state change.
