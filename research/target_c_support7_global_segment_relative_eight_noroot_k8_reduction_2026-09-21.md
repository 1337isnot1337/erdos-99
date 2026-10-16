<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "03257a276b29d2dea9b6f1fff3477f3184064ecc", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k8_reduction_2026-09-21.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "99a1b2b23b59ab146053a235a8290110024a5b11c7f413dd81acc2038723baa9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: eight-no-root `k=8` reduction

Date: 2026-09-21

Status: rigorous structural reduction of the rank-zero eight-no-root layer. Nine of its eleven arithmetic boundary cases are excluded. The only remaining `k=8` cases are

```text
D=-2, d=0, p=14;
D=-1, d=0, p=15.
```

Companion arithmetic checker:

- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k8_reduction_2026_09_21.py`

## 1. Deletion theorem after the seven-no-root closure

The preceding commit proves

> every four-cycle family with at most seven no-root cycles has `D=|A|-3 delta(A)>=0`.

Let `B=R union E`, `|E|=8`, be a hypothetical eight-no-root counterexample. Delete any external row `e`. As in the six- and seven-row deletion arguments,

`m_e=delta(B)-delta(B\{e}) in {0,1}`

and

`D(B\{e})=D(B)-1+3m_e`.

The seven-no-root theorem rules out `m_e=0`, so every external row is an `M`-coloop and a `Q`-noncoloop. Hence

`D(B) in {-2,-1}`.

Write

`k=8-(r_Q(B)-r_Q(R))`

and let `d` be the complete-root-block deficiency. Exactly as in the seven-row reduction,

`delta(B)=delta(R)+k`

and

`D(B)=8+p+3d-3k`.

This note treats `k=8`. Then the external quotient rank is zero and the coefficient-constraint space is zero. Every deletion of external coordinates therefore preserves quotient rank.

The exact arithmetic boundary is

```text
D=-2: (d,p)=(0,14),(1,11),(2,8),(3,5),(4,2)
D=-1: (d,p)=(0,15),(1,12),(2,9),(3,6),(4,3),(5,0).
```

## 2. Triple deletions remove seven cases immediately

Delete any three external rows. The resulting five-row state has

```text
k=5,
D_5=D(B)+6.
```

Thus `D_5=4` for `D=-2` and `D_5=5` for `D=-1`.

The committed exact five-row theorem says every `k=5` state with `p<=9` has `D>=7`. Therefore every triple shadow has `p>=10`.

The congruence

`D_5 == 5+p_5 (mod 3)`

then gives

```text
D=-2: p_5 in {11,14,...}
D=-1: p_5 in {12,15,...}.
```

Since deletion cannot increase `p`, all branches with global `p<11` in the first line or `p<12` in the second line are impossible. Seven of the eleven `k=8` cases disappear, leaving

```text
D=-2: (d,p)=(0,14),(1,11)
D=-1: (d,p)=(0,15),(1,12).
```

Moreover, in the `p=11` and `p=12` cases every triple shadow must preserve `p` exactly.

## 3. Close `D=-2,d=1,p=11`

Because every triple deletion preserves `p=11`, no selected incomplete block can be supported on three or fewer of the eight external cycles. Otherwise deleting a triple containing its complete external support would make that block untouched and reduce `p`.

Thus every incomplete block has external support at least four.

Delete any two external rows. The resulting six-row shadow has

```text
k=6,
D_6=2,
p_6=11,
```

and every incomplete block is still touched by at least two external cycles.

For the global state,

`delta(B)=c-d+k=c+7<=15`,

so `c<=8`, and the pair shadow also has at most eight complete touched blocks.

The committed exact six-row rank-zero census gives

`p=11, c<=9, incomplete support>=2 => D>=8`.

This contradicts `D_6=2`. Therefore

`D=-2,d=1,p=11`

is impossible.

## 4. Close `D=-1,d=1,p=12`

Again every triple deletion preserves `p`, so every incomplete block has external support at least four. Every pair deletion has

```text
k=6,
D_6=3,
p_6=12,
```

with incomplete support at least two and `c_6<=8`.

The seven-no-root `k=7` closure derived, directly from the exact six-row `p=10,11` census,

`p=12, c<=8, incomplete support>=2 => D>=6`.

Hence `D_6>=6`, contradicting `D_6=3`. Thus

`D=-1,d=1,p=12`

is impossible.

## 5. Remaining rank-zero branches

Only

```text
D=-2,d=0,p=14;
D=-1,d=0,p=15
```

remain in the eight-no-root `k=8` layer.

Triple shadows satisfy

```text
p=14 branch: p_5 in {11,14};
p=15 branch: p_5 in {12,15}.
```

So the exact remaining issue is the pattern of three-row losses of incomplete root cost.

There is also a useful six-row bound for the next attack. Suppose a six-row rank-zero shadow arising in either residual has every incomplete block touched at least twice. Six cycles supply 24 block incidences, so the number `q` of incomplete blocks is at most 12. Write `s` for its singleton count; then `p=2q-s`.

At `p=14`, `q<=12` guarantees at least two pair blocks. Completing two pairs maps the profile to a `p=10` profile on the same all-complete superfamily and raises `c` by two. Since the residual global deficiency is zero, ambient dimension gives `c<=7`, so the transformed profile has `c<=9`. Comparing the exact all-complete defect bounds gives

`p=14, c<=7, support>=2 => D>=5`.

Likewise, at `p=15` there are at least two pair blocks. Completing two pairs maps to `p=11,c<=9`, giving

`p=15, c<=7, support>=2 => D>=6`.

These conditional bounds mean a residual pair shadow can have the required defect `2` or `3` only if some incomplete block has six-row support one. Equivalently, the next finite/combinatorial target is forced into global incomplete blocks supported on at most three of the eight external cycles.

## 6. Current consequence and next target

The `k=8` eight-no-root layer is reduced from eleven arithmetic cases to two deficiency-zero cases. No eight-row orbit enumeration was used.

The next target is to classify the low-support incomplete-block cost hypergraph in those two residuals. For every triple `S` of external coordinates, deletion loses either

```text
p=14: 0 or 3 rows;
p=15: 0 or 3 rows,
```

because the five-row shadow values are respectively `{14,11}` and `{15,12}`. Any pair shadow without a support-one incomplete block is already excluded by the conditional six-row bounds above. This should permit a support-hypergraph obstruction analogous to the graph argument that closed the final seven-no-root `p=13` branch.

The direct C-II endpoint remains independently at

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.
