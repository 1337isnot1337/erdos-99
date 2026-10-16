# Target C: sharp five-no-root `k=2,p=3` singleton reduction

Date: 2026-09-20

Status: exact structural reduction for the sharp five-no-root `D=2,k=2,p=3` shadows that occur inside the remaining seven-no-root `D=-2,k=4,d=0,p=3` branch. This does not by itself close the seven-no-root branch and does not change the direct 3,874-cell generic-H6 endpoint.

Companion arithmetic/combinatorial checker:

`research/verify_target_c_support7_global_segment_relative_five_noroot_k2_p3_sharp_singletons_2026_09_20.py`

## 1. Input from the certified slack-two theorem

For five no-root rows with `k=2`, let `P <= Q^5` be the rank-three global coefficient-constraint space.

The preceding slack-two theorem proves the following whenever `P` is obtainable from empty-block constraints plus at most two singleton-block constraints. Form the virtual canonical state which leaves a touched block empty exactly when its empty-state constraint `E_b` is contained in `P`, and completes it otherwise. If `C` is its complete set and

`d = |C| - rank H(C)`,

then

- `d >= 1`, and
- the two external `null(P)` relation rows lie in `H(C)`.

For a compatible actual state, let `q` canonical-complete blocks become incomplete and let `p_t` be the number of selected rows in incomplete touched blocks. The certified theorem gives

`D(A_t) >= 5 + p_t + 3d - 3q`,

with `q <= p_t`, after harmless untouched incomplete root rows are stripped.

For the deletion-shadow application below it is useful to keep those root rows rather than strip them. If `u` selected rows lie in incomplete blocks untouched by the five no-root rows, they impose zero external coefficient constraint and contribute no relative `T` relation. Adding them back raises `|A|` by exactly `u` and leaves `delta` unchanged. Thus, with total incomplete-root cost

`p = p_t + u`,

the same inequality becomes

`D(A) >= 5 + p + 3d - 3q`,

still with `q <= p_t <= p`.

So the sharp argument below applies to the unstripped pair-deletion shadows with their original root-row set intact; it does not assume in advance that every selected incomplete block remains touched.

## 2. Sharp `p=3` theorem

Consider a five-no-root state with

`D=2, k=2, p=3`,

where `p` counts all selected rows in incomplete root blocks, including any block that may be untouched by the five no-root rows.

Then all three units of incomplete-root cost are singletons on three distinct touched blocks. No two-row pair state and no selected row on an untouched incomplete block occurs.

Moreover, for each of those three singleton blocks `b`,

`E_b not subset P`.

Equivalently, all three selected singleton blocks are canonical-complete relative to `P`.

### Proof: case 1, `P` is obtainable with at most two singleton constraints

Apply the extended slack-two inequality. Since `p=3` and `D=2`,

`2 >= 5 + 3 + 3d - 3q`.

Together with `d>=1` and `q<=3`, equality is possible only at

`d=1, q=3`.

Thus three canonical-complete touched blocks must become incomplete. Those three blocks consume at least one selected row each. Since the entire incomplete-root budget is exactly `p=3`, each changed block contains exactly one selected row. Hence all three are singleton blocks, and there is no selected pair state, no other selected incomplete block, and no cost left for an untouched root row.

Because each of those blocks was canonical-complete, its empty constraint is not contained in `P`.

### Proof: case 2, `P` is not obtainable with at most two singleton constraints

Empty states can contribute rank-one or rank-two coefficient constraints. Complete and pair states contribute zero coefficient constraint. A singleton contributes at most one coefficient-constraint line. A selected row in an untouched block also contributes zero coefficient constraint.

If an actual `p=3` realization used a pair plus one singleton, or spent any positive cost on an untouched incomplete block, then `P` would be obtainable from its empty constraints plus at most two singleton constraints, contrary to the case assumption. Therefore the only possible `p=3` cost pattern is three singleton blocks whose singleton constraints participate in the realization of `P`.

Fix one of those singleton blocks `b`. Its singleton constraint `L_b` is contained in the empty constraint space `E_b`, because `L_b` is one linear combination of the two empty-state coefficient rows. Compatibility gives `L_b subset P`.

If `E_b subset P`, replace the singleton at `b` by the empty state. The local constraint span can only increase, but it remains contained in `P`; because the original local constraints already spanned `P` and `L_b subset E_b`, the new local constraints still span exactly `P`. This produces `P` using only the other two singleton blocks, again contradicting the case assumption.

Hence `E_b not subset P` for all three singleton blocks. In particular no such block is untouched, because an untouched block has `E_b=0 subset P`.

This proves the theorem in both cases.

## 3. Local quotient line at a sharp singleton

At any sharp singleton block, write `L_b <= E_b` for the singleton and empty local coefficient-constraint spaces.

We have

`L_b subset P`,

but

`E_b not subset P`.

The quotient image

`W_b = (E_b + P) / P`

is therefore nonzero. In fact `dim W_b = 1`.

There are only two possibilities.

1. `rank E_b = 1`. If `L_b` were nonzero then `L_b=E_b`, contradicting `L_b subset P` and `E_b not subset P`. Thus `L_b=0`, `E_b intersect P=0`, and `dim W_b=1`.
2. `rank E_b = 2`. The singleton row is a nontrivial determinant combination of the two independent empty-state rows, so `L_b` is a nonzero line. Thus `L_b <= E_b intersect P`. Since `E_b` is not contained in `P`, the intersection has dimension exactly one. Again `dim W_b=1`.

So every sharp singleton block carries one distinguished nonzero quotient direction outside `P`.

## 4. Consequence for the remaining seven-no-root branch

Now return to the remaining branch

`D=-2, k=4, d=0, p=3`.

Deleting any two no-root rows keeps the root-row set `R` unchanged. The established depth-two synchronization gives

`D=2, k=2`

for the resulting five-no-root family. Since `d` and `p` are parameters of the fixed root-row set, the unstripped shadow still has

`d=0, p=3`.

The sharp theorem above applies even if some root block becomes untouched after deletion, and in fact rules that possibility out for every selected incomplete block.

### 4.1 The seven-row root state has exactly three singleton blocks

The global `p=3` cost pattern is either

- three singletons, or
- one singleton plus one pair.

Suppose a pair block and singleton block occurred. Each is touched by at least one of the seven no-root rows in the original seven-row state; otherwise its selected rows are inert and deleting them would make the negative defect even smaller. Choose one touching row from each block. Among seven coordinates there are always two other coordinates available to delete, so both blocks remain touched in that pair-deletion shadow. The shadow still has the pair-plus-singleton `p=3` pattern, contradicting the sharp five-row theorem.

Therefore the seven-row state contains exactly three selected singleton blocks and no selected pair block.

### 4.2 Each singleton is touched by at least three no-root rows

Fix one of the three singleton blocks and let `S` be the set of no-root rows touching it. If `|S|<=2`, delete all rows of `S` and, if necessary, additional no-root rows to make a two-coordinate deletion. The selected singleton then lies in an untouched root block of a five-row `D=2,k=2,p=3` shadow.

The sharp five-row theorem forbids this: every selected incomplete row in such a shadow must be one of three singleton blocks with `E_b not subset P`, whereas an untouched block has `E_b=0`.

Hence

`|S| >= 3`

for each singleton root block.

Equivalently, a nonempty touch support survives every two-coordinate deletion exactly when it has size at least three. The companion checker verifies this finite support statement directly for all subsets of seven coordinates.

### 4.3 Pair-puncturing obstruction

Let `P <= Q^7` be the rank-three seven-row coefficient space. For a pair `J` of deleted coordinates, let `pi_J` be puncturing to the remaining five coordinates and put

`P_J = pi_J(P)`.

Depth-two synchronization gives `rank P_J=3` for every pair `J`.

For each of the three singleton blocks `b`, the sharp five-row theorem gives

`pi_J(E_b) not subset P_J`

for every one of the 21 pairs `J`.

Equivalently, if `K_J` is the coordinate subspace supported on the deleted pair,

`E_b not subset P + K_J`

for every `|J|=2`.

Because `(E_b+P)/P` is one-dimensional, choose any `w_b in E_b` whose class generates that quotient line. The preceding condition says

`w_b notin P + K_J`

for every pair `J`.

Thus the coset `w_b+P` has Hamming distance at least three from `P`:

`min_{p in P} |supp(w_b-p)| >= 3`.

The remaining seven-row branch therefore has three distinguished nonzero quotient cosets of distance at least three, one for each selected singleton block.

## 5. Combined seven-row filters

A hypothetical `D=-2,k=4,d=0,p=3` state must now satisfy all of the following simultaneously.

- `P <= Q^7` has rank three.
- Its generalized weights satisfy `(d_1,d_2,d_3) >= (3,4,6)`.
- The root state has exactly three selected singleton blocks and no selected pair block.
- Each singleton block is touched by at least three no-root cycles.
- For each singleton block, its local singleton constraint lies in `P`.
- For each singleton block, its empty constraint is not contained in `P + K_J` for any two-coordinate subspace `K_J`.
- Equivalently, each singleton block supplies a nonzero quotient coset of distance at least three from `P`.
- The complete-block count still satisfies `c<=11`.

These tests are all available before any final 15-dimensional `T`-space reranking.

The useful implementation change is that a seven-row verifier no longer needs to enumerate arbitrary `p=3` local states or repeatedly reconstruct all 21 five-row shadows. It can enumerate triples of singleton blocks directly, reject any triple containing a block touched fewer than three times, and test the 21 containment failures `E_b not subset P+K_J` directly in the seven-coordinate coefficient space.

## 6. Verification and remaining bottleneck

The companion checker verifies the equality arithmetic in the low-singleton-generated case, the only possible `p=3` incomplete-row cost patterns, the two-support deletion lemma for arbitrary pairs of nonempty block-touch supports, and the equivalence between surviving every pair deletion and touch multiplicity at least three. It passes locally.

A direct exhaustive five-row `p=3` census was also attempted, but the naive rank-space enumeration is too slow to be a useful proof vehicle and no census result from that attempt is claimed here. The structural reduction above avoids depending on it.

The branch is not closed. The next exact computation should extend only rank-three seven-row coefficient spaces satisfying the projective-system bounds and the three-singleton/coset-distance filters above.

A cheap rejection order is:

1. enforce generalized weights `(3,4,6)` from the generator-column matroid;
2. require exactly three singleton blocks, each touched at least three times;
3. require each singleton local line to lie in `P`;
4. require `E_b not subset P+K_J` for all three singleton blocks and all 21 coordinate pairs;
5. reject `c>11`;
6. only then construct and rerank the exact `T`-relation system.

The direct C-II endpoint remains unchanged:

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.

No theorem-state authority file is changed by this note.
