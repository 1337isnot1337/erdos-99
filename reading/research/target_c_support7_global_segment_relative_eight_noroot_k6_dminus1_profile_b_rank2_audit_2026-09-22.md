> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_rank2_audit_2026-09-22.md) · source SHA-256 `8cb6f1c83c861dde4b0444bb77239a7a6dc61f89afa07d5cb09bd1b8bd204249`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "26ae2c3a14f3ff28cb01b66e96a3e138348bb621", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_rank2_audit_2026-09-22.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c3486757d6830c5dc9b1e97318d3db564353313ef86d8add29311db514fd4576"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: corrected rank-two audit for the remaining `k=6, D=-1` Profile B

Date: 2026-09-22

Status: rigorous reduction to a coverage-correct finite necessary-condition audit. No closure is claimed until the full audit executes.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d3_profile_b_singleton_functional_2026_09_22.py`

Workflow:

`.github/workflows/target-c-k6-dminus1-profile-b-rank2.yml`

## 1. Input profile

After the corrected coefficient-rank bookkeeping, the all-singleton residual is

```text
global eight-row profile:
    rank(P_8)=2,
    d_8=3,
    9 singleton replacements,
    replacement-functional rank 9;

three-clean seven-row shadow:
    rank(P_7)=2,
    d_7=3,
    singleton-functional rank 8;

synchronized six-row child:
    rank(P_6)=2,
    d_6=3,
    singleton-functional rank 7;

five-row puncture of that child:
    rank(P_5)=2,
    d_5 in {2,3},
    full punctured singleton-functional rank 5 or 6.
```

The five-row coefficient rank is two. Rank-one `k=4` functional censuses are therefore not used anywhere in this audit.

## 2. Quotient dimensions force full compatible-singleton spans

For a rank-two coefficient plane on `t` no-root rows, a virtual-canonical state of deficiency `d` has replacement-functional quotient dimension

```text
s_t = t - 2 + d.
```

Hence the six-row `d_6=3` quotient has dimension seven. Every actual Profile B six-row child has seven independent descended singleton replacement classes.

After deleting one more no-root row, the coefficient rank remains two. If `d_5=2`, the punctured quotient has dimension five; if `d_5=3`, it has dimension six. Puncture functoriality sends each actual singleton replacement class either to the corresponding punctured singleton class or to zero, and the descended actual classes span the punctured quotient.

Therefore every actual five-row shadow satisfies the following necessary condition:

```text
d_5=2  => compatible singleton capacity >=5
           and the span of all compatible singleton classes has rank 5;

d_5=3  => compatible singleton capacity >=6
           and the span of all compatible singleton classes has rank 6.
```

Using *all* compatible singleton states is an overapproximation of the actual nine globally chosen singleton blocks. Failure of this enlarged span condition is therefore a rigorous exclusion.

The same argument at six rows gives the necessary condition

```text
compatible singleton capacity >=7,
span of all compatible singleton classes = 7.
```

## 3. Puncture-kernel basis lemma

There is a further common-block constraint that does not require knowing the actual singleton states.

Let `V_6` be the seven-dimensional six-row replacement-functional quotient. The actual singleton replacement classes span `V_6`, so choose seven of them, on seven distinct actual replacement blocks, that form a basis `B`.

For puncture `i`, functoriality induces a surjection

```text
pi_i : V_6 -> V_{5,i}
```

because the descended actual replacement classes span the punctured quotient. Its target has dimension `3+d_i`, hence

```text
dim ker(pi_i) = 7-(3+d_i) = 4-d_i.
```

If a basis block is no longer virtual-canonical complete after puncture `i`, its replacement class maps to zero. The lost basis classes are still linearly independent, so they form an independent subset of `ker(pi_i)`. Therefore

```text
number of blocks of B lost under puncture i <= 4-d_i.
```

Concretely:

```text
d_i=2 => at most two of the seven basis blocks can disappear;
d_i=3 => at most one of the seven basis blocks can disappear.
```

Thus every genuine Profile B six-row state must admit one common seven-block subset of its singleton-compatible complete blocks satisfying those six simultaneous puncture bounds.

The verifier now checks this condition before the six-row functional rerank. It still does not demand that the selected seven blocks admit a particular independent choice of singleton states, so this is a necessary overapproximation and cannot remove an actual Profile B state.

## 4. Exact finite cover

The established five-row orbit engine gives the exact 20,451 `S_7` orbit representatives of five no-root subsets. For each representative the verifier enumerates every realizable rank-two coefficient plane using the repaired five-row `k=3` candidate-space generator.

It keeps only parents with `d_5 in {2,3}` that already satisfy the corresponding full compatible-singleton span condition above. This parent filter is exhaustive for Profile B because every actual six-row child has all six five-row punctures of exactly those forms.

For every retained parent the established six-row extension engine enumerates every realizable rank-two six-row plane projecting to it. The verifier then requires:

1. all six one-coordinate projections retain coefficient rank two;
2. six-row virtual deficiency is exactly three;
3. at least seven canonical-complete blocks admit a compatible singleton state;
4. every five-row projection has virtual deficiency two or three;
5. every five-row projection fills its entire compatible-singleton quotient, rank five or six as appropriate;
6. there is a common seven-block candidate basis satisfying the six puncture-kernel bounds above;
7. the six-row compatible-singleton span fills the seven-dimensional quotient.

The verifier intentionally does not require a single globally consistent choice of nine singleton blocks. It also allows every compatible singleton state on every complete block. Thus it searches a superset of actual Profile B realizations.

Consequently:

> if the full 20,451-orbit cover returns zero six-row survivors, Profile B is impossible.

If survivors occur, they are only finite candidates; they must still pass the common-nine-block consistency conditions and a distinct-block functional-basis check.

## 5. Exactness of the rank tests

Coefficient-space row reduction and the extension cover are exact rational computations inherited from the repaired five-row and six-row engines.

Relation and replacement-functional ranks are computed modulo the Mersenne prime `2^127-1`. The verifier runs the Lucas-Lehmer check and records the maximum squared row norms and matrix widths. It asserts the corresponding Hadamard inequalities before accepting a zero-survivor result, so the modular rank decisions are exact over `Q` rather than probabilistic finite-field evidence.

The committed verifier blob after the puncture-kernel upgrade is `eab77c4a0754b100590fe426c2ecbebcc8ab0b42`; those exact bytes were syntax-compiled locally before push.

## 6. Execution status

The GitHub Actions workflow shards the exact 20,451-orbit cover into 32 disjoint intervals. The first workflow attempt failed before any runner executed a step: all jobs had an empty step list and runner id zero. The repository execution infrastructure therefore produced no mathematical result from that attempt.

The immediate bottleneck is execution of the Profile A and Profile B rank-two full-cover audits. The mathematical reduction no longer depends on the invalid rank-one five-row functional bounds.
