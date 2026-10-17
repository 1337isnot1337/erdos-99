> Generated reading edition · [exact source](../../research/target_c_long_side_sector_multiplicity_2026-09-15.md) · source SHA-256 `e911d425feb2424e071eded28b259eb4a4aaa38b186c9d05b459b25eaff73a11`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c0a9f39a80fb6b8ceaabc3f7088fed4d182ba18e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_long_side_sector_multiplicity_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e49c051466d832b556241387d1692fb354cb7d404d54e9eee118d28ee9c6cf46"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — angular-sector multiplicity for long-side straight events

**Date:** 2026-09-15  
**Repository base:** `a2170a1688bf1adfd13ab9eebd2dea4309e1623e`  
**Status:** proved proof-only strengthening of the bridge-suppressed long-side branch; theorem-state authority unchanged  
**Scope:** no-container Type-II full positive-contact core  
**LEVEL I STATUS:** `STILL OPEN`

The preceding straight-event theorem bounded the number of relevant outer-face
occurrences at one branching contact vertex by the full triangle-free contact-degree
cap `5`. That loses a large constant. A `beta`-straight occurrence already carries
much stronger angular information: its predecessor and successor rays are almost
opposite, so the outer-face sector between them is large. For `beta<=pi/6`, one
physical vertex supports at most two such occurrences.

Together with bridge suppression, this raises the current long-side transverse-contact
floor from `0.039045D` to `0.097613D`.

## 1. Straight occurrences consume outer-face angular sectors

Orient a distinguished long-side route `W_i` along its loaded-hull chord direction
`u_i`. At a `beta`-straight internal occurrence at a physical vertex `x`, both adjacent
oriented route-edge vectors differ from `u_i` by angle strictly less than `beta`.

From `x`, the ray to the predecessor is the negative of the incoming oriented edge,
while the ray to the successor is the outgoing oriented edge. Therefore the smaller
angular separation `gamma` of those two contact rays satisfies

```math
\boxed{\gamma>\pi-2\beta.}
\tag{SM.1}
```

At one occurrence of `x` on the unbounded-face walk, the predecessor and successor
edge sides delimit one angular sector occupied by the unbounded face. Since the
smaller angle between the rays is `gamma`, either sector between them has angular
measure at least `gamma`. Hence every `beta`-straight occurrence consumes an
outer-face sector of size strictly greater than

```math
\pi-2\beta.
\tag{SM.2}
```

Different occurrences of the same physical vertex correspond to distinct disjoint
face sectors in the cyclic rotation around that vertex. Their angular measures sum to
at most `2pi`.

### Lemma SM.1 — two-occurrence cap

If

```math
0<\beta\le\pi/6,
```

then one physical vertex supports at most two `beta`-straight outer-face occurrences.

### Proof

By (SM.2), each such occurrence uses a sector strictly larger than

```math
\pi-2(\pi/6)=2\pi/3.
```

Three disjoint sectors of that size would have total angular measure strictly larger
than `2pi`. QED.

This is purely local plane-embedding geometry. It does not use KKT weights or a
contact-degree cap.

## 2. Improved occurrence-to-edge conversion

Let

- `S_beta` be the total number of `beta`-straight internal occurrences on long-side
  routes;
- `S_2(beta)` be the subcount whose physical vertex has full contact degree exactly
  two;
- `B_beta` be the number of distinct physical degree-at-least-three vertices supporting
  at least one such occurrence;
- `E_perp(beta)` be the number of distinct physical extra contact edges obtained by
  choosing one strongly transverse extra edge at every vertex counted by `B_beta`.

For `beta<=pi/6`, Lemma SM.1 gives

```math
S_\beta-S_2(\beta)\le2B_\beta.
\tag{SM.3}
```

One selected undirected extra contact can be selected at at most its two endpoints, so

```math
B_\beta\le2E_\perp(\beta).
\tag{SM.4}
```

Thus

```math
S_\beta-S_2(\beta)\le4E_\perp(\beta).
\tag{SM.5}
```

For degree-two events, the same sector cap gives at most two occurrences per physical
vertex. The bridge-suppression theorem shows every such physical vertex is incident to
outer bridges and gives `V_2(beta)<=B_o`. Hence

```math
S_2(\beta)\le2V_2(\beta)\le2B_o.
\tag{SM.6}
```

Combining (SM.5)--(SM.6),

```math
\boxed{
2B_o+4E_\perp(\beta)\ge S_\beta.
}
\tag{SM.7}
```

The earlier coefficient `10` is replaced by `4`.

## 3. Insert the long-side and bridge bounds

The exact directional-energy argument gives

```math
S_\beta
\ge
L_{>2}-{2d_{out}\over1-\cos\beta}.
\tag{SM.8}
```

In the full-core Type-II branch, bridge-subtracted isoperimetry and
`P_F/D->pi` give on every convergent subsequence

```math
\limsup {2B_o\over D}\le\delta,
\qquad
\delta:=\lim {d_{out}\over D}.
\tag{SM.9}
```

Therefore, for `beta<=pi/6`,

```math
\boxed{
\liminf {4E_\perp(\beta)\over D}
\ge
\liminf {L_{>2}\over D}
-\delta\left(1+{2\over1-\cos\beta}\right).
}
\tag{SM.10}
```

At each selected contact, triangle-freeness gives transverse component strictly larger
than

```math
\sin(\pi/3-\beta)
```

relative to the corresponding loaded-hull side direction.

## 4. Current low-`t` long-side consequence

At `t=t_42`, the rounded long-side alternative gives

```math
{L_{>2}\over D}
\ge0.4363893718701161781\ldots-o(1),
```

and the low-`t` squeeze gives

```math
\delta\le0.002883975.
```

Set

```math
\beta={\pi\over6}.
```

Then the near-straight occurrence floor is

```math
{S_{\pi/6}\over D}
\ge0.3933368069590823665\ldots-o(1).
\tag{SM.11}
```

Using (SM.9) in (SM.7) gives

```math
\boxed{
{E_\perp(\pi/6)\over D}
\ge0.09761320798977059163\ldots-o(1).
}
\tag{SM.12}
```

Every selected edge has absolute transverse component strictly greater than `1/2`.

Thus the rounded long-side branch now forces almost `0.098D` distinct robustly
transverse physical contacts. The improvement is combinatorial, not numerical: it
uses the angular size of an outer-face occurrence to prevent one physical vertex from
absorbing five straight events.

## 5. Updated low-`t` physical normal form

At the current floor every full-core Type-II survivor obeys one of:

```text
tooth branch:
    >= 0.2127872328 D-o(D) distinct inward contacts,
    inward component > 0.5011115;

rounded long-side branch:
    >= 0.09761320799 D-o(D) distinct transverse contacts,
    transverse component > 1/2.
```

The remaining gap is no longer boundary-event multiplicity. It is how a linear family
of these transverse contacts is routed through the stopped-train / pentagon network.
A long coherent rhombic strip can absorb many such contacts on one train, while many
short strips create train/interface endpoints. That train-occupancy dichotomy is the
next source-level target.

## 6. Reproducibility

Run

```bash
python3 research/verify_target_c_long_side_sector_multiplicity.py
```

for the Decimal constant checks.
