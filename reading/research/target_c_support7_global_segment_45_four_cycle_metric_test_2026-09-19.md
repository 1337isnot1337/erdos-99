> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_45_four_cycle_metric_test_2026-09-19.md) · source SHA-256 `6ef63f67d1169d4323b998f93b5433ac9487a0c6bcbbb610702d09a795466bb0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5ac6b27c4f6271944c52ab1cbb8dec020fa82ff8", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_45_four_cycle_metric_test_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e5b80363bb117a735c4c672330e4fa8cd5bfbe41a9039bd28ba3721ba8e42bfa"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C support-seven: 45 cross-root four-cycles suffice for complete metric closure

Date: 2026-09-19

Status: exact structural refinement of the generic reciprocal metric layer. The theorem-state authority is unchanged. C-II remains open.

## Result

The previous line-graph basis note gave 85 canonical cross-root four-cycles which, together with the 56 automatic triangle-side cycles, span the full cycle space of `L(K8)`. For complete reciprocal metric compatibility on the complete generic angular system, only 45 specific cross-root four-cycles are needed.

Fix reciprocal points `0` and `1`. For every pair

$$
2\le i<j\le7,
$$

use the three simple `K8` four-cycles

$$
C^{(1)}_{ij}=(0,1,i,j,0),
$$

$$
C^{(2)}_{ij}=(0,1,j,i,0),
$$

and

$$
C^{(3)}_{ij}=(0,i,1,j,0).
$$

There are

$$
3\binom62=\boxed{45}
$$

such cross-root four-cycles.

Let `H` be the reciprocal log-sine cochain on `L(K8)`. On every genuine reciprocal triangle, the triangle-side cycle sum of `H` vanishes identically. Then

$$
\boxed{
\text{common reciprocal metric}
\iff
\text{all 45 displayed four-cycle sums of }H\text{ vanish.}
}
$$

The forward direction is immediate from exactness of `H`. The reverse direction reduces exactly to the existing fifteen ground-root metric equations.

## The local K4 identity

For each `2 <= i < j <= 7`, let

$$
S_{ij}=S_0(1,i,j)
$$

be the root-`0` star triangle on the three segment vertices `01,0i,0j`. Let `T_{abc}` denote the triangle-side cycle on segments `ab,bc,ac`, with the orientations fixed in the verifier. Then the following identity holds as an integer 1-chain on `L(K8)`:

$$
\boxed{
2S_{ij}
=
-T_{01i}+T_{01j}-T_{0ij}-T_{1ij}
+C^{(1)}_{ij}-C^{(2)}_{ij}-C^{(3)}_{ij}.
}
\tag{1}
$$

This is not a trigonometric approximation. It is a coefficientwise identity of the 168 oriented line-graph edges.

The four `T` terms vanish identically for a Euclidean reciprocal angular system. If the three four-cycle sums on the right of (1) vanish, then the `S_ij` sum vanishes. Doing this for all fifteen pairs gives all fifteen root-fan equations

$$
S_0(1,i,j)=0,
\qquad 2\le i<j\le7.
$$

Those fifteen equations form the complete ground-root metric basis already proved in `target_c_support7_global_segment_order_2026-09-19.md` and `target_c_support7_h6_metric_coordinate_reduction_2026-09-19.md`. Hence a common reciprocal metric follows.

## Exact rank audit

The companion verifier independently checks:

```text
rank(56 triangle-side cycles)                         = 56
rank(15 ground-root star cycles)                     = 15
rank(side + ground)                                  = 71
rank(side + 45 selected cross-root four-cycles)     = 101
rank(side + 45 four-cycles + 15 ground cycles)      = 101
```

All ranks are certified by elimination modulo the prime `1,000,000,007`. Full row rank modulo a prime implies a nonzero integer minor and therefore exact independence over `Q`.

The last equality is also implied constructively by the fifteen instances of (1); it is kept as an independent guard.

The 45 selected four-cycles are linearly independent modulo the automatic side-cycle space. This does **not** prove that 45 is the globally smallest possible family of four-cycle equations sufficient for metric closure. No such minimality claim is made.

Certificate:

`research/verify_target_c_support7_global_segment_45_four_cycle_metric_test_2026_09_19.py`

## Computational consequence

This gives a direct short-cycle replacement for the fifteen ground-root nonlinear equations when cross-root geometry gives tighter interval bounds.

For a surviving H6 branch, it is now enough to target these 45 products:

1. form the four angle-dependent sine ratios around `C^(1)_ij`, `C^(2)_ij`, or `C^(3)_ij`;
2. use the exact rational sine-interval engine to bound that product;
3. exclude the branch whenever the certified interval misses `1`;
4. if every one of the 45 products is certified equal to `1`, metric compatibility follows on the complete generic angular system.

The 210 total four-cycles and longer chordless cycles remain useful as redundant discovery certificates. They are not required as an independent completion layer once these 45 equations are enforced.

As before, this statement concerns additive/log-sine metric exactness. It does not replace the longer chordless directed cycles needed for the strict segment-order acyclicity test.

## Scope

This is a structural reduction, not a new H6 cell exclusion. The explicit exact generic-H6 endpoint remains 4,704 cells, with the separate reflection-closed upper bound 4,582. Reciprocal-collinearity walls remain separate.