> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_seven_noroot_k6_C_d5q12_d5_codim1_kernel_reduction_2026-09-22.md) · source SHA-256 `51b3fb28562f449c51167d2acec559d648a6b4d74b4ad2af0ea56229572172d5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "708955304d168dd8a0cd17429e0c76f5287719f0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_seven_noroot_k6_C_d5q12_d5_codim1_kernel_reduction_2026-09-22.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9afcd4c19895ff92fa0482e85a873b49dc812688b55c13346114ac124f48d100"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: codimension-one kernel reduction for the remaining `C:(5,12,12)`, `d_6=5` lift branch

Date: 2026-09-22

Status: proved structural strengthening of the sole remaining six-row-shadow branch in the current eight-no-root `k=7` finite split. It reduces the seven-row rank-11 test to one residual direction and shows that only singleton-compatible blocks which become canonical-complete during the lift can supply that direction. This note does not claim the finite census has been completed.

## 1. Setup

Fix a six-row synchronized state in the remaining profile with

```text
D_6=3,  p_6=12,  d_6=5,
```

and coefficient line `P_6`. The committed six-row functional reduction says that a surviving shadow must have singleton-functional extra rank exactly ten. Restore one member of the good deletion pair and let `P_7` be a compatible seven-row coefficient line projecting to `P_6`.

The deficiency-monotonicity lemma and the established seven-row alternatives force

```text
D_7=1,  p_7=12,  d_7=5,
```

with singleton capacity at least eleven. The seven-row replacement-functional inequality then forces singleton-functional extra rank eleven.

Write `C_t` for the virtual-canonical complete block set at `t` external rows, and write `H_b` for the fixed complete-block `T`-relation row of block `b`. For a coefficient line `P_t`, put

```text
N_t = P_t^perp.
```

The canonical relation matrix has one row `H_b` for every `b in C_t` and one external relation row for every basis vector of `N_t`.

## 2. Singleton compatibility is unique on a canonical-complete block

For one block, write its two quotient component rows as `x` and `y`. With the fixed local directions

```text
u0=(1,0),  u1=(0,1),  u2=(1,-1),
```

the three singleton constraints are, up to nonzero scalar,

```text
y,  x,  x+y.
```

Suppose two distinct singleton states were both compatible with the same coefficient line `P_t`. Any two of `x`, `y`, and `x+y` lying in `P_t` imply the third relevant component row also lies in `P_t`. In every case this gives

```text
span{x,y} subset P_t.
```

But that is exactly the canonical-empty condition. Therefore:

> A virtual-canonical complete block admits at most one compatible singleton state.

This holds at every row count. In particular, the seven-row audit never needs to treat multiple singleton choices on one canonical-complete block.

## 3. An old complete block cannot acquire a new singleton state

Let `pi: Q^7 -> Q^6` delete the restored coordinate. Compatibility of the line lift means

```text
pi(P_7)=P_6.
```

For every fixed singleton state `s`, its seven-row local constraint projects to its six-row local constraint. Hence

```text
W_7(b,s) subset P_7  =>  W_6(b,s) subset P_6.
```

Consequently, if `b in C_6` has a singleton state compatible at seven rows, that state was already compatible at six rows. By the uniqueness lemma it is exactly the old six-row compatible state.

Thus every seven-row compatible singleton on an old complete block is one of the retained old singleton functionals. Any genuinely new singleton functional must belong to a block in

```text
J = C_7 \ C_6.
```

## 4. The six-row canonical kernel embeds in the seven-row kernel

The previously proved persistence lemma gives

```text
C_6 subset C_7.
```

Since both deficiencies equal five,

```text
rank H(C_6) = |C_6|-5,
rank H(C_7) = |C_7|-5.
```

If `m=|C_7\C_6|`, then adjoining the `m` new complete-block rows increases `rank H` by exactly `m`. Equivalently, those new rows are independent modulo `H(C_6)`.

Now embed

```text
N_6 -> N_7,   alpha |-> (alpha,0).
```

This is valid because `P_7` projects to `P_6`. Choose a basis of `N_7` whose first five vectors are these embedded six-row null vectors and whose sixth vector completes them.

For an embedded `(alpha,0)`:

1. the restored external cycle contributes zero to the external `T` term;
2. an old complete block has exactly its six-row quotient contraction;
3. a newly complete block was six-row canonical-empty (or untouched), so both of its six-row quotient component rows lie in `P_6`; therefore `alpha` annihilates both components and the local complete-state correction on that block is zero.

Hence the seven-row canonical relation row associated to `(alpha,0)` is exactly the six-row canonical relation row associated to `alpha`, after inserting zero coordinates for the new complete-block rows.

Let `K_t` be the left kernel of the canonical relation matrix, equivalently the dependency space among its canonical relation rows. Extending a six-row dependency by zero on `J` and on the sixth seven-row null vector therefore gives an injection

```text
K_6 -> K_7.
```

The dimensions are explicit. At six rows the canonical matrix has `|C_6|+5` rows and rank `|C_6|-5`, so

```text
dim K_6 = 10.
```

At seven rows it has `|C_7|+6` rows and rank `|C_7|-5`, so

```text
dim K_7 = 11.
```

Therefore the embedded `K_6` is a codimension-one subspace of `K_7`.

## 5. Ten retained old singleton functionals already fill the embedded kernel

For the six-row witness, choose ten compatible singleton replacement functionals whose classes are independent modulo the canonical relation-column span. Their restrictions to `K_6` form a basis of `K_6^*`.

Suppose these ten singleton states remain compatible in a qualifying seven-row lift. Build their seven-row functionals using the adapted nullspace basis above. On the embedded copy of `K_6`, each seven-row functional restricts exactly to its six-row functional: the block coordinate is unchanged and the sixth null-coordinate of the embedded dependency is zero.

Therefore the ten retained functionals remain linearly independent modulo the seven-row canonical relation-column span. They contribute exactly ten functional dimensions at seven rows. Their common kernel inside the eleven-dimensional `K_7` is one-dimensional.

So the remaining rank question has only one degree of freedom:

> Seven-row extra rank reaches the required value eleven if and only if some other compatible singleton functional is nonzero on this one-dimensional common kernel.

By Section 3, an old complete block cannot supply such an additional functional. It is enough to test compatible singleton functionals on `J=C_7\C_6`.

## 6. Finite consequence

The existing seven-row verifier reranks all compatible singleton functionals on all complete blocks. The reduction above permits a smaller exact audit for every qualifying lift:

1. select ten retained old singleton functionals forming a six-row basis;
2. use a seven-row nullspace basis extending `N_6 x {0}`;
3. form the seven-row canonical relation columns plus those ten retained functionals;
4. test only the unique compatible singleton, if any, on each newly complete block `b in C_7\C_6` for one additional rank.

Because the base already has canonical rank plus ten, any nonzero increment is exactly the forbidden/required eleventh functional direction. If no newly complete singleton produces an increment over the full 325,955-representative cover, the remaining `d_6=5` branch is impossible.

All modular membership decisions can use the existing `P=2^127-1` certificate. Recording the same functional-width and row-norm Hadamard bounds makes the finite result exact over `Q`.

This reduction is independent of the older two-cycle full-span multiplicity route. It does not change the theorem-state declaration until the finite residual audit is actually completed.
