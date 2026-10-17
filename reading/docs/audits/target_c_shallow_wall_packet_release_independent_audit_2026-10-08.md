> Generated reading edition · [exact source](../../../docs/audits/target_c_shallow_wall_packet_release_independent_audit_2026-10-08.md) · source SHA-256 `5a5becacbaaf6a4ff5e4774b2c3f0f9c1535466c1477d5a79edef0bf09707616`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-AF6BEB84F0FF","canonical":true,"claim_ids":["C-EXTERIOR-SHALLOW-WALL-RELEASE-CAPACITY","C-LARGER-TURN-COLLECTIVE-TRANSLATION-REGRESSION"],"claim_statuses":{"C-EXTERIOR-SHALLOW-WALL-RELEASE-CAPACITY":"canonical","C-LARGER-TURN-COLLECTIVE-TRANSLATION-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: shallow-wall packet release and collective-translation regression

**Date:** 2026-10-08  
**Audit base:** `origin/main=aa69d18020979fdca53d23b7c80d68c58c746584`, state `2026-10-08.audit.171`  
**Target:** C-II; C-II and Level I remain open.  
**Frozen source:** `origin/research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f`.  
**Source candidate commit:** `4583329a0eebd5b489f34185ec4ebdc16cabd353`.  
**Source report:** `docs/reports/target_c_collective_shallow_wall_packet_release_2026-10-08.md`, SHA-256 `1eab31772c03aabae60944b5de4b718ed81a70d128698dee4c49c209e521fe2e`.  
**Source verifier:** `research/verify_target_c_collective_shallow_wall_release_2026_10_08.py`, SHA-256 `5f7e3aded179c1105c1f3de1c186b4678033148182945d4ddf3095e0fe424b4e`.  
**Exact-arithmetic helper:** `research/verify_target_c_three_direction_corner_barrier_2026_10_06.py`, SHA-256 `179f20fb42827f6b3aa3b7afa5b982b16ff4da49abb77373edaf1a48bd514252` (identical at the frozen source and audit base).

## Verdict

**PASS — promote `C-EXTERIOR-SHALLOW-WALL-RELEASE-CAPACITY`, with the threshold strengthened to `T <= 2*pi/3`.** For an actual convex hull-augmented cell with a monotone unit-contact path of total turn at most `2*pi/3`, every finite unit-separated packet that is weakly clear of all internal path vertices and strictly clear of both tips can be translated and slightly dilated into the fully strict path-clear region. The canonical strict cell-capacity theorem then gives the exact weak capacity `|S_Q|`.

**REGRESSION VALID — promote `C-LARGER-TURN-COLLECTIVE-TRANSLATION-REGRESSION`.** The exact 529-site rational fixture has turn strictly above `2*pi/3`, one wall contact per contacted packet site, and three wall-contact vectors that strictly surround the origin. It has no nonzero common translation feasible to first order, despite every individual packet site having a non-surrounding wall-contact set. A separate exact finite rotation, translation, and dilation opens all packet contacts. The fixture is nonglobal and is not a counterexample to C-II.

The audit does not assert that arbitrary canonical cells have shallow walls or contain a packet of any specified size. The full-source exchange consequence is retained only under the exact lexicographic-improvement cases stated below.

## 1. Exact theorem and dependency chain

Let `A` be a canonical triangle-free global minimum-diameter source, selected contact-minimal and then actual-diameter-pair-minimal. Let `K=conv(A)`. Let `Q` be an actual convex hull-augmented face cell with one source-hull arc and one simple path of actual unit-contact edges

`W=(v_0,...,v_m)`, `m>=1`.

Orient the path with `Q` on its left. Lift its unit-edge directions monotonically as `theta_0 <= ... <= theta_(m-1)` and put `T=theta_(m-1)-theta_0`. Assume `T <= 2*pi/3`. Write

`S_Q=(A intersect Q) minus W`

so every source label assigned to the cell away from the path is counted, including hull-arc isolates. Define the weak region

`Wweak={x in int(Q): |x-v_j|>=1 for 0<j<m, and |x-v_0|>1, |x-v_m|>1}`

and the strict region

`E_Q={x in int(Q): |x-v_j|>1 for 0<=j<=m}`.

Then:

1. Every finite unit-separated `Y subset Wweak` has a common translation followed by a sufficiently small dilation that places it in `E_Q` and makes every internal packet distance strictly greater than one.
2. Using the canonical `Pack_1(E_Q)=|S_Q|` theorem, `Pack_1(Wweak)=Pack_1(E_Q)=|S_Q|`.
3. For a full-source replacement with `R subset A`, `S_Q subset R`, and `|R|=|Y|`, the released packet has no new unit contacts to any retained source point and all inserted-involving distances are strictly below `D`. The canonical endpoint forbids this replacement if `R` deletes an old contact, or if it deletes no old contact but removes an old diameter pair, or if it covers every old diameter pair. No contradiction is claimed when the deletion is neutral for both lexicographic counts and leaves an old diameter pair.

Dependencies for the canonical capacity and exchange conclusions are `C-EXTERIOR-HULL-AUGMENTED-CELLS`, `C-EXTERIOR-CAP-STRICT-PACKET-CAPACITY`, and `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`. The angular release itself is independently proved below.

The required implication chain is:

```text
common shallow-wall release -> exact weak cell capacity |S_Q|
-> no extra fixed-cell weak packet capacity -> the weak-contact surplus route is unavailable in this scope
```

It does not produce a packet, move the wall, or give a strict sub-`D` competitor.

## 2. Independent proof of the collective release

Take a unit wall contact between `x in Y` and an internal path vertex `v_j`, and set `u=x-v_j`, so `|u|=1`. Let `alpha` be a lifted angle for `u`. Since `x` is in the interior wedge at `v_j`,

`theta_j < alpha < theta_(j-1)+pi`.

The weak guards at the two adjacent path vertices give

`|u-e_(theta_j)|^2 >= 1` and `|u+e_(theta_(j-1))|^2 >= 1`.

Both angle differences lie in `(0,pi)`. Expanding the squares therefore yields

`alpha >= theta_j+pi/3` and `alpha <= theta_(j-1)+2*pi/3`.

Across every internal wall contact this implies

`alpha in [theta_0+pi/3, theta_(m-1)+2*pi/3]`.

The interval width is `T+pi/3 <= pi`. Let `n` be its unit bisector. Every contact vector satisfies `n dot u >= 0`. This includes the equality case `T=2*pi/3`: the source report used a strictly positive lower bound for `T<2*pi/3`, but at equality the lower bound is zero and the quadratic term still opens the contact. For every sufficiently small `t>0`,

`|x+tn-v_j|^2 = 1 + 2t(n dot u) + t^2 > 1`.

If there are no wall contacts, any direction works. All initially strict wall margins, strict tip guards, and membership in `int(Q)` persist for a sufficiently small common translation, by finiteness. Translation preserves every packet-internal distance. A sufficiently small dilation of the translated packet about any fixed center then multiplies every internal distance by a factor greater than one, while preserving its strict wall margins and keeping it in `int(Q)`. Thus it lies in `E_Q` with all internal distances strict. No triangle-free assumption on the original packet is used.

This also gives a more general geometric criterion: whenever the finite set of inward unit wall-contact vectors of a packet has the origin outside the interior of its convex hull, a separating direction has nonnegative dot product with every contact vector; translation in that direction opens all contacts by the same `t^2` term. The shallow-turn bound guarantees this criterion uniformly for every packet satisfying the wall guards.

## 3. Full-source shielding and the exact exchange scope

For the canonical cell, every retained source point in `Q` lies on `W`, because `R` contains `S_Q`. Consider a retained source point `q` outside `Q` and a packet point `x` in `int(Q)`. The segment from `x` to `q` lies in `K`; except possibly at `q`, it is in `int(K)`, so it cannot leave through the actual source-hull arc before reaching `q`. Its first exit from `Q` is through a unit path side or a path vertex.

If it crosses a unit side `cd` at `z=(1-s)c+sd`, weak unit separation of both `x` and `q` from the source endpoints `c,d` gives, for `p=x` and for `p=q`,

`|p-z|^2=(1-s)|p-c|^2+s|p-d|^2-s(1-s) >= 1-s(1-s) >= 3/4`.

Since `z` lies between `x` and `q`, `|x-q|>=sqrt(3)>1`. If the segment exits at a path vertex, both segment pieces have length at least one, so `|x-q|>=2`. A retained label on the source-hull arc belongs to `S_Q` and was deleted. Thus before the small motion every retained point outside `Q` is strictly clear; the motion preserves this finite margin. The translation opens all contacts to retained path vertices, and the dilation opens all packet-internal contacts.

Every released packet point remains in `int(Q) subset int(K)`. If `x in int(K)` and `z in K`, then `|x-z|<D`: otherwise a small move of `x` away from `z` inside `K` would create a pair longer than `diam(K)=D`. Hence every inserted-involving upper pair is strictly below `D`.

The replacement is triangle-free: the retained old source was triangle-free and every pair involving the packet is now strictly longer than one. If `R` deletes a contact, the new contact count is zero on packet-involving pairs and the old contact count strictly falls. If no old contact is deleted but an old diameter pair is, the contact count is unchanged and the actual diameter-pair count falls. If all old diameter pairs are deleted, every remaining and inserted-involving pair is strictly below `D`, so the new diameter is strictly smaller. These are precisely the cases that contradict the canonical endpoint. Deleting only contact-isolated, non-diameter labels while preserving both lexicographic counts is neutral and is not ruled out by this audit.

## 4. Exact weak-capacity consequence

For any finite unit-separated `Y subset Wweak`, the release above produces a same-size unit-separated subset of `E_Q`. Therefore `Pack_1(Wweak) <= Pack_1(E_Q)`. Since `E_Q subset Wweak`, the reverse inequality holds. Audit.84 canonically proves `Pack_1(E_Q)=|S_Q|` for the same actual hull-augmented cell, with all cell isolates retained. Consequently

`Pack_1(Wweak)=Pack_1(E_Q)=|S_Q|`.

This closes only the fixed-wall, all-path-guards, shallow-turn weak-packet surplus. Audit.140's one-omitted-guard strict-capacity result is a different statement; this audit neither removes a guard nor moves any wall.

## 5. Independent audit of the larger-turn regression

At the frozen source, I inspected the `Fraction` / `Q(sqrt(3))` arithmetic helper and the complete pair-checking code, then reran the verifier. The rational 529-site fixture has 567 wall vertices and 529 packet vertices. Its wall turn is `2 arccos(16/65)`, strictly between `2*pi/3` and `pi` because `0<16/65<1/2`.

A separate exact rational pair census found exactly three packet-to-wall contacts, on three distinct packet vertices, with inward vectors

`(264,-23)/265`, `(-264,-23)/265`, and `(0,1)`.

The first two vectors plus `(46/265)(0,1)` sum to zero with all weights positive, and the vectors span the plane. Hence the origin is strictly inside their triangle. Any common packet translation with all contact derivatives nonnegative must make all three derivatives zero, which forces the translation to be zero. The same exact enumeration confirms that each contacted packet vertex has wall degree one.

The verifier independently checks positive pinned equilibrium at all 529 moving vertices, the full 1,097 unit-contact rows, triangle-freeness, every old and endpoint pair, a finite rational rotation/translation/dilation that opens every packet-involving contact, and an explicit smaller square-grid competitor. It passes 600,060 old-pair checks and 600,060 endpoint-pair checks. The source has one actual diameter pair of length `528+32/65`; the 34-by-33 square grid has enough sites and diameter squared `2113`, so the source is nonglobal. This is a regression against deriving a common packet translation from sitewise non-surrounding or against treating positive pinned equilibrium as a finite-release obstruction. It does not refute finite nonlinear release; the same fixture has one. It is not a C-II counterexample.

The verifier also checks the ten-site shallow-wall fixture, including an initial unit triangle and a retained outside isolate, across 1,128 old and endpoint pairs. This is finite corroboration only. Neither fixture certifies the analytic wall theorem or any global-minimizer claim.

## 6. Validation, scope limits, and frontier

- Source branch and source report were frozen at the exact commits and hashes above; the source branch was not changed.
- `python3 research/verify_target_c_collective_shallow_wall_release_2026_10_08.py` passed in the frozen source worktree. Its registered copy supports only the exact finite examples; it is not a verifier for the analytic theorem.
- The weak-capacity theorem narrows the fixed-cell weak-contact route to no surplus when `T<=2*pi/3`; it does not establish that a canonical large-cap cell has this turn bound, nor that a packet of size `|S_Q|+1` is extracted from any source.
- C-II's full-source finite-move/payment obligation and Level I are unchanged. The next obligation remains a source-realized, cardinality-restoring finite move or a strict-diameter competitor that checks every original source pair, including contact isolates.

## Claim classification

- `C-EXTERIOR-SHALLOW-WALL-RELEASE-CAPACITY`: **PASS — promote**, with the boundary threshold `T<=2*pi/3` and the canonical cell/strict-capacity dependencies explicit.
- `C-LARGER-TURN-COLLECTIVE-TRANSLATION-REGRESSION`: **REGRESSION VALID — promote** at the exact rational nonglobal fixture scope.
- No arbitrary-source extraction, globality, strict-sub-`D` competitor, C-II closure, or Level I conclusion is claimed.
