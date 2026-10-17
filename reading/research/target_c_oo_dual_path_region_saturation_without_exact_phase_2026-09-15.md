> Generated reading edition · [exact source](../../research/target_c_oo_dual_path_region_saturation_without_exact_phase_2026-09-15.md) · source SHA-256 `c82170d97a30bbc44ce9c2147ecbecc81e520146eca99561c4848df0f7b322a0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "83d9801a46be6a591ec90618fa893c64d2b48604", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_oo_dual_path_region_saturation_without_exact_phase_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1e6cc61a49e98f7b02850fb9e1fe688351710e84b238b2af19e4d56cd405b64e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every region of a canonical O--O dual path contains a diameter endpoint

**Date:** 2026-09-15  
**Status:** proof-only exact structural strengthening  
**Scope:** any canonical simple complement-dual path of outer-to-outer complete stopped trains  
**Dependencies:** exact laminar interval support; finite adjacent-strip layer translation; canonical contact-minimality; audited Section 157 two-sided bracing  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current live high-`t` path theorem selects trains in one **shrinking** phase window, not one finite-source exact phase.  The existing exact-phase region-saturation theorem therefore does not directly apply to that selected family.

There is a simpler source-level argument which needs no exact phase and no rank factorization: every complementary region of **any** canonical O--O dual path is forced to contain an endpoint of an actual diameter edge.

Let

```math
R_0\xleftrightarrow{\tau_1}R_1
\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m
\tag{PRS.1}
```

be the complement dual path of pairwise disjoint O--O complete stopped trains.

### Theorem PRS — phase-free path-region saturation

For every `0<=i<=m`, the region `R_i` contains at least one endpoint of an actual diameter pair:

```math
\boxed{
R_i\cap B\ne\varnothing
\qquad(0\le i\le m),
}
\tag{PRS.2}
```

where `B` is the actual diameter-endpoint set.

The proof is finite and exact.  Internal regions are forced by contact-minimality of a one-layer translation; the two end regions are forced by Section 157 bracing of the extreme O--O cuts.

## 1. Exact interval coordinates

Root the path at `R_0` and use the nested shores from the exact laminar O--O multishear theorem.  If a source pair has endpoint regions

```math
R_a,R_b,
\qquad a<b,
```

then its selected-cut support is exactly

```math
\boxed{I_{ab}=\{a+1,\ldots,b\}.}
\tag{PRS.3}
```

For an internal boundary between consecutive cuts `tau_i,tau_{i+1}`, the unique source layer between the two cuts is `R_i`.

A source pair changes selected-cut incidence between columns `i` and `i+1` if and only if one endpoint region is `R_i`.  Indeed, by (PRS.3), a change there is exactly an interval start `a=i` or interval end `b=i`.

Thus for actual diameter pairs the switching set at boundary `i` is

```math
\boxed{
H_{sw,i}
=\{xy\in H:\rho(x)=R_i\text{ or }\rho(y)=R_i\}.
}
\tag{PRS.4}
```

The other endpoint may lie on either side; no common-hub assumption is used here.

## 2. Every internal region must have a switching diameter

Fix `1<=i<=m-1` and suppose for contradiction that

```math
H_{sw,i}=\varnothing.
\tag{PRS.5}
```

Translate the entire source layer `R_i` by a sufficiently small vector `v`, leaving every other source point fixed.

The audited adjacent-strip opening argument applies to the two physical boundary train families `tau_i,tau_{i+1}`.  If their outside-to-layer unit contact vectors are `a,b`, there are arbitrarily small nonzero translations opening both families:

- if `a+b!=0`, take `v=s(a+b)` for small `s>0`;
- if `b=-a`, take a small nonzero `v` perpendicular to `a`, which opens both contacts quadratically.

Every old contact outside those two boundary train families has both endpoints moved together or both fixed and is unchanged exactly.  The two boundary families become strictly longer than one.

For an arbitrary source pair, the relative-displacement change is determined by the difference of the two adjacent shore indicators.  Hence every nonswitching pair is invariant exactly under this one-layer translation.  Under (PRS.5), **every old actual diameter pair is nonswitching**, so every old diameter distance stays exactly `D`.

All old strict noncontact lower-distance inequalities and strict nondiameter upper-distance inequalities remain strict after choosing `v` sufficiently small, because the source is finite.

The translated source is therefore

- unit-separated;
- of the same cardinality;
- of diameter exactly `D`; and
- has strictly fewer unit contacts, since both boundary train contact families have opened and no new unit contact is created for sufficiently small `v`.

This contradicts the canonical contact-minimal choice among global diameter minimizers.

Therefore

```math
\boxed{H_{sw,i}\ne\varnothing\qquad(1\le i\le m-1).}
\tag{PRS.6}
```

By (PRS.4), each internal region `R_i` contains an actual diameter endpoint.

## 3. The two end regions are loaded by Section 157

Consider the extreme cut `tau_1`.  Audited Section 157 proves that every O--O train is crossed by actual diameter edges with both transverse signs; in particular at least one actual diameter pair crosses `tau_1`.

If its endpoint regions are `R_a,R_b` with `a<b`, crossing the first selected cut means

```math
1\in\{a+1,\ldots,b\}.
```

Therefore `a=0`, so one endpoint lies in `R_0`.

Likewise any actual diameter edge crossing the last cut `tau_m` must have `b=m`, so one endpoint lies in `R_m`.

Thus

```math
R_0\cap B\ne\varnothing,
\qquad
R_m\cap B\ne\varnothing.
\tag{PRS.7}
```

Together with (PRS.6), this proves (PRS.2).

## 4. Interaction with a common diameter-routing hub

Suppose in addition that one region

```math
R_*=R_k
```

lies on the endpoint-region path of every actual diameter pair, as in the high-`t` Helly-hub theorem.  Then every actual diameter edge with endpoint regions `R_a,R_b` satisfies

```math
a\le k\le b.
\tag{PRS.8}
```

The already-proved one-sided-switch theorem says:

- for `i<k`, every switching diameter incident to `R_i` goes toward the hub side;
- for `i>k`, every switching diameter incident to `R_i` goes toward the hub side from the other direction.

The present theorem adds that **there is at least one such switching edge at every nonhub internal region**, not merely at the count-optimized strip.  Hence every nonhub path layer is an active layer-to-hub diameter interface.

The hub region itself is also diameter-endpoint loaded by (PRS.2), although its adjacent switching set may contain both orientations.

## 5. Live high-`t` consequence through `t<=1.859`

The current low-energy high-`t` theorem supplies, for every full-core survivor with

```math
1.844<t\le1.859,
```

a simple O--O dual path with

```math
m>0.0007D-o(D).
```

The selected trains lie only in a shrinking phase window, so exact-phase finite-source factorization is unavailable.  Theorem PRS nevertheless applies directly and gives

```math
\boxed{
\text{all }m+1\text{ complementary regions contain actual diameter endpoints.}
}
\tag{PRS.9}
```

Because one source point belongs to one complementary region, these are at least `m+1` distinct diameter endpoints.  More structurally, every one of the `m-1` internal path layers has a nonempty actual-diameter switching set; away from the common hub those switching sets are one-sided toward the hub.

Thus the live high-`t` normal form strengthens to

```text
linear shrinking-window O-O dual path
+ every complementary path region is diameter-endpoint loaded
+ every internal layer has a nonempty diameter switching interface
+ every nonhub switching interface points toward the common hub
+ active diameter sets are nested toward the hub on both sides.
```

This conclusion is exact despite the lack of finite-source exact phase equality.

## 6. Scope and non-implications

- No exact-phase assumption is used.
- No KKT coefficient lower bound is used.
- The theorem does not say that every diameter endpoint in `R_i` participates in a switch at boundary `i`; it proves existence of at least one switching diameter and therefore at least one endpoint there.
- One actual diameter edge can account for two endpoint regions, so (PRS.2) does not give `m+1` distinct diameter edges.
- The result does not bound the number or KKT mass of switching edges at an individual layer.
- It does not by itself contradict the Woodall diameter-thrackle or force a unit triangle.

The next closing target is to exploit the simultaneous **region saturation + common hub + one-sided interval nesting**.  In particular, the loaded endpoint in each nonhub region must send a diameter edge across the hub direction, while all such endpoints lie in the cyclic convex-hull order constrained by the two separated terminal arcs of the selected O--O path.

**Disposition:** proved exact phase-free diameter-endpoint saturation of every region on a canonical O--O dual path. C-II and Level I remain open.
