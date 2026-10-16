# Target C: corrected five-row status for the eight-no-root `k=6, D=-1, p=9` residual

Date: 2026-09-22

Status: correction of the previous version of this note. The five-row functional exclusions formerly stated here were invalid because they imported audits for a rank-one coefficient-constraint space into punctures whose coefficient-constraint space has rank two. No Profile A or Profile B closure follows from those rank-one audits.

The correction is certified by

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_five_row_functional_reduction_2026_09_22.py`,

which records the rank mismatch, and by

`research/verify_target_c_support7_global_segment_relative_five_noroot_k3_d2_mixed_fullrank_witness_2026_09_22.py`,

which gives an exact rank-two five-row `d=2` witness with four singleton replacements plus one pair of full functional extra rank five. That witness directly falsifies the obstruction that the earlier version of this note tried to import from the five-row `k=4` audits.

## 1. The coefficient rank after puncturing

The eight-no-root `k=6` branch has

```text
rank(P)=8-k=2.
```

The three-clean punctures used in the valid preceding reduction preserve this coefficient rank. Consequently a five-row shadow still has

```text
rank(P_5)=2,
k_5=5-2=3.
```

The earlier five-row functional audits used in the superseded argument enumerate `k=4` states. Their coefficient-constraint space has rank one. Their singleton- and pair-functional rank bounds therefore do not apply to these rank-two `k=3` shadows.

In particular, the following claims from the superseded version are withdrawn:

- that Profile A forces exactly four singleton replacements plus the pair at five rows because of the rank-one `d=2` functional bound;
- that a five-row `d=2` child of Profile B is impossible for the same reason;
- that Profile B can consequently be restricted to the old rank-one `d=3` full-span census.

The new rank-two mixed witness shows that a five-row `d=2` state can in fact have four singleton replacement classes plus a pair spanning the full five-dimensional quotient.

## 2. Valid residual restored from the six-row reduction

The preceding valid puncture reduction still leaves exactly two global profiles.

### Profile A

```text
global:
    d_v=2,
    q=8,
    7 singleton replacements + 1 pair replacement,
    functional rank 8;

three-clean seven-row shadow:
    rank(P_7)=2,
    d_7=2,
    functional rank 7;

synchronized six-row child:
    rank(P_6)=2,
    d_6=2,
    singleton capacity exactly 5,
    the pair survives,
    five actual singleton replacements + the pair span rank 6;

all one-coordinate punctures of that six-row child:
    rank(P_5)=2,
    d_5=2.
```

The five-singleton classes in the six-row child must themselves have rank five. A single pair class can increase rank by at most one, so rank six for the six actual replacement classes is impossible unless the five singleton classes are independent and the pair class lies outside their span.

Moreover, puncture functoriality maps the six-dimensional six-row functional quotient onto each five-dimensional five-row quotient. Each actual replacement functional maps to its punctured replacement functional when its block remains virtual-complete, and to zero otherwise. Therefore every five-row puncture must retain at least five of the six actual replacement blocks as virtual-complete. This is a necessary condition before any five-row rerank.

### Profile B

```text
global:
    d_v=3,
    q=9,
    9 singleton replacements,
    functional rank 9;

three-clean seven-row shadow:
    rank(P_7)=2,
    d_7=3,
    singleton-functional rank 8;

synchronized six-row child:
    rank(P_6)=2,
    d_6=3,
    singleton-functional rank 7;

five-row puncture:
    rank(P_5)=2,
    d_5 in {2,3},
    full punctured singleton-functional rank 5 or 6 respectively.
```

The `d_5=2` alternative is open again. Any further finite census for Profile B must enumerate rank-two five-row `k=3` states, not reuse rank-one `k=4` data.

## 3. A second coverage correction for Profile A

The old synchronized six-row `d=2` singleton-shadow audit reports 156 covered six-row states of singleton capacity five. It is not, by itself, an exhaustive list for Profile A.

That audit starts only from five-row `d=2` parents having singleton capacity at least five. This threshold was sufficient for the older six-singleton target: after puncturing, at least five of the six designated singleton blocks had to remain.

Profile A has five singleton replacements and one pair. A five-row puncture can retain the pair while losing one singleton. Such a child has only four guaranteed singleton-compatible blocks even though five of the six total actual replacement blocks remain. Therefore a Profile A cover must seed from every repaired five-row rank-two `d=2` parent of singleton capacity at least four.

The correct necessary six-row search is thus:

1. enumerate every five-row rank-two `d=2` parent with singleton capacity at least four;
2. extend by every sixth no-root row and enumerate every realizable rank-two six-row plane projecting to that parent;
3. require all six coefficient projections to retain rank two;
4. require six-row virtual deficiency two and singleton capacity exactly five;
5. require all six projected five-row virtual deficiencies to equal two;
6. take the five singleton-compatible complete blocks as the five actual singleton replacement blocks;
7. enumerate a distinct compatible pair replacement block;
8. require every five-row puncture to retain at least five of those six actual replacement blocks;
9. require the five singleton functional classes to have extra rank five and the pair to raise the mixed extra rank to six.

The companion verifier for this corrected cover is

`research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_capacity5_singleton_pair_functional_2026_09_22.py`.

It deliberately overapproximates actual realizations: it tests compatible replacement states without requiring those six displayed states alone to generate the coefficient plane. Hence a zero-survivor full cover would rigorously close Profile A; a survivor would only identify the next finite candidate.

## 4. Current bottleneck

No closure is claimed here. The immediate target is the corrected synchronized six-row Profile A audit above. Profile B remains the rank-two synchronized six-row `d=3`, full-singleton-rank-seven endpoint, with rank-two five-row `d=2/3` punctures.
