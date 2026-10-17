> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_seven_noroot_k7_closure_2026-09-21.md) · source SHA-256 `dc7494e96950e19e477710b42649b7cb1f2ec334529ff7ccab47a8f5f2216168`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cb5ca4fd7ad76527f7e907da9259c0dcefdf464b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_seven_noroot_k7_closure_2026-09-21.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "97ee402e7716b7db2a294aa33bb8435144f0cea86aa17e84b044b82c3529eeb5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the seven-no-root `k=7` layer

Date: 2026-09-21

Status: exact structural closure. Together with the committed `k=3,4,5,6` closures, this finishes the entire seven-no-root factor-three rank-density layer.

Companion arithmetic/combinatorial checker:

- `research/verify_target_c_support7_global_segment_relative_seven_noroot_k7_closure_2026_09_21.py`

## 1. Starting point

Let

`B = R union E`, `|E|=7`,

be a hypothetical seven-no-root counterexample and write

`D(X)=|X|-3 delta(X)`.

The committed seven-no-root deletion theorem gives

`D(B) in {-2,-1}`

and shows that every external row is an `M`-coloop and a `Q`-noncoloop. The exact root-block formula is

`D(B)=7+p+3d-3k`.

This note treats the last coefficient-nullity layer `k=7`. Here the external quotient rank is zero, equivalently the coefficient-constraint space `P` has rank zero. Hence every deletion of external rows also has quotient-rank drop zero.

The ten arithmetic cases are

```text
D=-2: (d,p)=(0,12),(1,9),(2,6),(3,3),(4,0)
D=-1: (d,p)=(0,13),(1,10),(2,7),(3,4),(4,1).
```

The two exact lower-bound inputs used below are already committed:

1. every five-no-root `k=5` state with `p<=9` has `D>=7`;
2. for a six-no-root rank-zero (`k=6`) state in which every incomplete block is touched by at least two external cycles, the exact all-complete census gives

   ```text
   p=10, c<=9  => D>=7,
   p=11, c<=9  => D>=8.
   ```

The second result is the exact census from `target_c_support7_global_segment_relative_six_noroot_k6_closure_2026-09-20.md`.

## 2. Every pair shadow has at least ten incomplete rows

Delete any two external rows. Since `P=0`, quotient rank does not drop. Since all external rows are `M`-coloops, the five-row shadow has

```text
k=5,
D_5=D(B)+4.
```

Thus `D_5=2` in the `D=-2` branch and `D_5=3` in the `D=-1` branch.

The exact five-row `k=5,p<=9` theorem gives `D_5>=7` whenever `p_5<=9`. Therefore every pair shadow satisfies

`p_5>=10`.

Also, for a five-row block-reduced state,

`D_5 == 5+p_5 (mod 3)`.

Combining this with `p_5<=p(B)` gives:

- for `D=-2,p=12`, every pair shadow has exactly `p_5=12`;
- for `D=-1,p=10`, every pair shadow has exactly `p_5=10`;
- for `D=-1,p=13`, every pair shadow has `p_5 in {10,13}`.

All seven arithmetic cases with global `p<=9` are therefore impossible immediately. Only

```text
D=-2, d=0, p=12;
D=-1, d=1, p=10;
D=-1, d=0, p=13
```

remain.

## 3. Two six-row bounds inherited from the exact `p=10,11` census

For a rank-zero six-row local state, every touched incomplete block is either a compatible singleton or a two-row pair. Write

- `q` for the number of incomplete blocks;
- `s` for the number of singleton incomplete blocks;
- `c` for the number of complete touched blocks.

Then

`p=2q-s`.

Assume every incomplete block is touched by at least two of the six external cycles. Since six cycles have only 24 block incidences, `q<=12`.

The already certified `p=10,11` all-complete census implies two further bounds without a new orbit scan.

### `p=12, c<=8`

If `s=0`, make any one pair block complete. The count profile becomes

`(q-1,0,c+1,p=10)`.

The all-complete superfamily and its rank are unchanged. The `p=12` defect lower bound is exactly one less than the transformed `p=10` lower bound. Since `c+1<=9` and the certified `p=10` minimum is seven,

`D>=6`.

If `s>0`, parity forces `s>=2`. Make one singleton block complete. The profile becomes

`(q-1,s-1,c+1,p=11)`.

The `p=12` lower bound is exactly two less than the transformed `p=11` lower bound. Hence again

`D>=8-2=6`.

Therefore

> every rank-zero six-row state with `p=12`, `c<=8`, and incomplete-block support at least two has `D>=6`.

### `p=13, c<=8`

Here `q<=12` implies

`s=2q-13 <= q-1`,

so at least one incomplete block is a pair. Make one pair complete. The transformed profile is

`(q-1,s,c+1,p=11)`.

The `p=13` lower bound is exactly one less than the certified `p=11` lower bound, giving

> every rank-zero six-row state with `p=13`, `c<=8`, and incomplete-block support at least two has `D>=7`.

No new modular rank computation is used in these deductions; they are count-profile transformations of the already exact six-row census.

## 4. Close `D=-2,d=0,p=12`

Every pair shadow preserves `p=12`. Therefore no selected incomplete block can be touched by only one or two of the seven external cycles: deleting its whole support inside a two-coordinate deletion would make it untouched and reduce `p`.

Thus every incomplete block has seven-row support at least three.

Delete any one external row. The six-row shadow then has

```text
k=6,
D_6=0,
p_6=12,
```

and every incomplete block is still touched by at least two external cycles.

The relative rank is

`delta(B)=c-d+k=c+7`.

Since the ground-root space has dimension 15, `c<=8`. Deletion cannot increase the number of complete touched blocks, so `c_6<=8`.

Section 3 gives `D_6>=6`, contradicting `D_6=0`. Hence

`D=-2,d=0,p=12`

is impossible.

## 5. Close `D=-1,d=1,p=10`

Every pair shadow preserves `p=10`, so the same argument forces every incomplete block to have seven-row support at least three.

A one-row deletion has

```text
k=6,
D_6=1,
p_6=10,
```

with every incomplete block touched at least twice.

Now

`delta(B)=c-d+k=c+6<=15`,

so `c<=9`, and therefore `c_6<=9`.

The committed exact six-row `p=10` census gives `D_6>=7`, contradicting `D_6=1`. Thus

`D=-1,d=1,p=10`

is impossible.

## 6. The final `D=-1,d=0,p=13` support graph

Only

`D=-1,d=0,p=13`

remains.

For an incomplete block, call its external support the subset of the seven no-root cycles that touch it. Define

- `a_i`: total selected incomplete-row cost in blocks with exact support `{i}`;
- `b_ij`: total selected incomplete-row cost in blocks with exact support `{i,j}`.

A pair deletion has `p_5 in {10,13}`, so its lost incomplete-row cost is zero or three. Hence

`a_i+a_j+b_ij in {0,3}`.

A one-row deletion has `D_6=1`, and its `p_i` is at least ten because any further deletion gives a pair shadow with `p>=10`. Since

`D_6 == p_i (mod 3)`

and `p_i<=13`, we have `p_i in {10,13}`. Therefore

`a_i=13-p_i in {0,3}`.

Suppose `a_i=3`. For every `j`, the pair-loss equation forces

`a_j=0` and `b_ij=0`.

Deleting `i` then leaves a six-row state with `p=10` in which every remaining incomplete block is touched at least twice. Here `c<=8` because globally `d=0` gives `c+7<=15`. The exact six-row `p=10` bound gives `D>=7`, contradicting the required one-row defect `D_6=1`.

Hence

`a_i=0`

for all seven coordinates. Consequently every `b_ij` is either zero or three.

Form a simple graph `G` on the seven external coordinates, with edge `ij` exactly when `b_ij=3`.

If `i` were isolated, deleting `i` would leave `p=13`, and every incomplete block would still be touched at least twice. Section 3 would give `D_6>=7`, again contradicting `D_6=1`. Thus `G` has no isolated vertex.

On the other hand, the total incomplete-row budget is 13, so

`3|E(G)| <= 13`,

hence `|E(G)|<=4`.

A graph on seven vertices without isolated vertices needs at least four edges. Therefore `G` has exactly four edges. Its degree sum is eight and all seven degrees are positive, so its degree sequence is

`(2,1,1,1,1,1,1)`.

Thus `G` is a three-vertex path together with two disjoint edges.

Take a path `i-j-k`. Since `b_ij=3`, the exact-support `{i,j}` blocks carry total incomplete cost three. One incomplete root block contains at most two selected rows, so at least two distinct root blocks have exact external support `{i,j}`. Hence cycles `i` and `j` touch at least two common root blocks.

A no-root four-cycle on vertex support `S`, `|S|=4`, touches exactly the four root blocks indexed by the three-subsets of `S`. Two distinct four-subsets of the seven non-root vertices share at most one three-subset. Therefore two no-root cycles that share at least two root blocks must have the same underlying four-vertex support.

The edge `ij` forces cycles `i,j` to have the same four-vertex support. The edge `jk` forces `j,k` to have the same four-vertex support. Hence all three cycles on the path touch the same four root blocks.

But then every root block touched by both `i` and `j` is also touched by `k`. No block can have exact external support `{i,j}`, contradicting `b_ij=3`.

Therefore the `p=13` branch is impossible.

## 7. Conclusion

All ten `k=7` arithmetic branches are closed. Together with the committed closures of `k=3,4,5,6`, there is no seven-no-root counterexample:

> Every four-cycle family with at most seven no-root four-cycles satisfies
>
> `3 delta(A) <= |A|`.

Under the established 44-cycle sufficient-family reduction, sufficiency requires `delta=15`, so a sufficient 44-cycle family cannot have seven or fewer no-root rows. Therefore any hypothetical sufficient 44-cycle family must contain at least eight no-root four-cycles.

This still does not prove that 45 four-cycle identities are globally minimal. The next rank-density layer is eight no-root cycles. The independent direct C-II endpoint also remains

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`,

with the state-specific forced-segment-order / metric-compatibility route still available as a separate attack.
