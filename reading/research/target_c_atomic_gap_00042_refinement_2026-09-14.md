> Generated reading edition · [exact source](../../research/target_c_atomic_gap_00042_refinement_2026-09-14.md) · source SHA-256 `a963f5de11c314b82f02450fe77e2431167ddc859e0f8c2628d307a546dbb1d2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e9858af8cb61fc8b5d3f3254a1284032cb13bb3c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_atomic_gap_00042_refinement_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "26774cb30629defce0fbc1add83e03794427b1e71d658eba428d2e6b3c006472"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — safe 0.00042 atomic-grid refinement

**Date:** 2026-09-14
**Repository base:** `602040915703d313a13db78749a181186b827d40`
**State version:** `2026-09-14.audit.51`
**Run type:** quantitative closing-proof refinement
**Target:** Target C-II, Type-II/full-core train route
**Claim class:** proved candidate awaiting independent audit; theorem-state authority unchanged
**External literature:** none
**Computation:** exact rational sign certificate plus high-precision regression

## LEVEL I STATUS

`STILL OPEN`

This note sharpens the audited-working §168 robust-grid constant from `0.0004` to the
safe round value

```math
\boxed{\eta_{grid}=0.00042.}
```

No geometric lemma is changed.  The only new step is to rerun the quantitative
bookkeeping in §§168.1--168.4 at the larger value and certify every strict numerical
inequality needed by the inherited §163 crossing-order argument.

The displayed §168 bookkeeping loses its final opposite-corner contradiction at
approximately

```math
\eta_*=0.0004206068955666769\ldots,
```

so `0.00042` is close to, but safely below, the limit of this particular proof.

## 1. Candidate chain

```text
eta_grid = 0.00042 in the audited §168 bookkeeping
  -> retained phase-pure shores still have triple common neighbors
  -> global signed crossing orders still follow from §163
  -> opposite-corner effective path mass > 2/sqrt(3)
  -> source diameter > D, contradiction
  -> x*sigma >= 2*sqrt(Delta_2)+0.00042
  -> stronger all-train and rhombic-train floors.
```

The final contradiction is the same source-diameter contradiction as audited §168;
no source points are deleted.

## 2. Recompute the §168 constants

Put

```math
\Delta_2={\pi\over2\sqrt3},\qquad
s_2=\sqrt{\Delta_2},\qquad
\eta=0.00042,
```

and assume for contradiction that the absolute atomic stopped-train mass satisfies

```math
A\le\bar A:=2s_2+\eta.
```

Exactly as in §168.1, define

```math
M_0={4s_2^2\over\bar A},\qquad
R_0=\bar A-M_0,
```

```math
d_0={\bar A^2\over4}-s_2^2+{R_0^2\over4},
\qquad
p_0=\sqrt{2d_0},
```

and

```math
S_0={M_0\over2}-\sqrt{d_0}-\sqrt{6d_0}.
```

High-precision evaluation gives

```math
\begin{aligned}
s_2&=0.9523128068639573458\ldots,\\
M_0&=1.9042057063241227450\ldots,\\
d_0&=0.0004001918399945982\ldots,\\
p_0&=0.0282910530024811277\ldots,\\
S_0&=0.8830965165371775833\ldots .
\end{aligned}
\tag{AG42.1}
```

After the distinct phase-order and degree-pruning payments from §168.3, the smaller
shore has normalized size at least

```math
{S_0\over2}-2p_0
=0.3849661522636265\ldots,
\tag{AG42.2}
```

whereas three missing-neighbor allowances cost only

```math
3p_0=0.0848731590074433\ldots .
\tag{AG42.3}
```

Thus the inherited `K_{2,2}` consistency and triple-common-neighbor transitivity step
has very large slack.  In particular, the quantitative change from `0.0004` to
`0.00042` does not approach this combinatorial threshold.

## 3. Opposite-corner contradiction still closes

The retained opposite-corner degree sum is bounded below exactly as in §168.4 by

```math
E(\eta):={3S_0\over2}-6p_0.
```

At `eta=0.00042`,

```math
E(0.00042)
=1.1548984567908796\ldots .
\tag{AG42.4}
```

The common projection of the unit train vectors tends to `sqrt(3)/2`, so the source
diameter would satisfy

```math
1\ge {\sqrt3\over2}E(0.00042)-o(1).
```

But

```math
{\sqrt3\over2}E(0.00042)
=1.0001714023723465\ldots>1.
\tag{AG42.5}
```

This is the required contradiction.

The exact-Fraction certificate deliberately uses much coarser outward bounds:

```math
S_0>0.8830948529981,
\qquad
p_0<0.028292,
```

which still imply

```math
E(0.00042)>1.1548902794972
>{2\over\sqrt3}.
\tag{AG42.6}
```

Therefore the strict inequality does not depend on floating-point rounding.

### Theorem AG42.1 — sharpened atomic grid gap

Every Type-II §142 train-measure subsequential limit in the audited §168 scope obeys

```math
\boxed{x\sigma\ge2\sqrt{\Delta_2}+0.00042.}
\tag{AG42.7}
```

This is a proof-only refinement of audited §168.1 pending independent audit.

## 4. Immediate all-train propagation

The exposed-hull argument used in audited §§142/164 is unchanged, hence

```math
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.00042.
}
\tag{AG42.8}
```

Using `T-q=2f-k`,

```math
\boxed{
\liminf {2f-k\over D}
\ge2\sqrt{\Delta_2}-\frac\pi2+0.00042.
}
\tag{AG42.9}
```

The §146 elimination gain becomes

```math
{2\over9}(0.00042)=0.000093333333\ldots,
```

instead of `1/11250 = 0.000088888...`.

## 5. Rhombic-only propagation

The independent audit of
`target_c_explicit_rhombic_train_gap_2026-09-14.md` verified that §§168.1--168.4
restrict to the non-singleton rhombic train graph `G_R`; the exposed-hull propagation
is not needed for the atomic gain itself.  Therefore (AG42.7) also gives

```math
\boxed{
\liminf {T_R\over D}
\ge2\sqrt{\Delta_2}+0.00042.
}
\tag{AG42.10}
```

For

```math
\sigma_R=2T_R-4\sqrt{R_4},
```

this yields

```math
\boxed{
\liminf {\sigma_R\over D}\ge0.00084.
}
\tag{AG42.11}
```

With `M_R=T_R^2/4-R_4` and

```math
M_R={\sigma_R(T_R+2\sqrt{R_4})\over8},
```

one obtains

```math
\boxed{
\liminf {M_R\over D^2}
\ge {0.00084\over8}
\left(4\sqrt{\Delta_2}+0.00042\right)
=0.00040001547888\ldots>0.0004.
}
\tag{AG42.12}
```

The proof-only post-endpoint identity then improves its guaranteed rhombic-train
contribution from `0.00008` to

```math
\boxed{0.000084}
\tag{AG42.13}
```

in the lower bound for `mu_D-mu_TC`.

Similarly the extra chamber Oler-slack contribution becomes exactly

```math
\boxed{0.000252D-o(D)}
\tag{AG42.14}
```

beyond the old train-floor baseline.

## 6. Why 0.00042, not a larger displayed constant

For the unchanged §168 bookkeeping define `E(eta)` by the same formulas above.  The
high-precision scalar root of

```math
E(\eta)={2\over\sqrt3}
```

is

```math
\eta_*=0.0004206068955666769669\ldots .
```

For example, `eta=0.0004206` leaves only about `1.95e-6` in the final projected
diameter coefficient, while `eta=0.0004207` makes that coefficient less than one.
Thus `0.00042` is a reasonable safe round endpoint for the existing proof.  Improving
past `eta_*` requires a better stability/pruning estimate, not more numerical precision.

## 7. Scope audit

- This does not alter the canonical theorem state.
- It assumes exactly the geometric inputs already audited in §§163 and 168.
- The only new proof obligation is the quantitative sign check at the larger `eta`.
- The all-train propagation uses the existing exposed-hull argument; the rhombic-only
  propagation stops before that step, exactly as in the independent audit of the
  previous `0.0004` rhombic gap.
- Contact-isolated source points remain outside the positive-contact train ledger and
  remain in the full source.
- C-II remains open: the result strengthens lower floors but gives no matching global
  upper bound or source-preserving descent.

## 8. Reproducibility

Run

```bash
python3 research/verify_target_c_atomic_gap_00042_exact.py
python3 research/verify_target_c_atomic_gap_00042.py
```

The first script checks the decisive inequalities using `fractions.Fraction` and
outward rational bounds.  The second reports the high-precision constants and locates
the bookkeeping root.

## 9. Next obligation

Propagate `g=0.00042` through the audited §171 orbit/detour scalar envelope, then combine
the resulting stronger `q-k` floor with the exact post-endpoint defect decomposition
and aggregate-detour identity.  A numerical improvement is useful only if it narrows an
actual structural branch; the target remains a source-level contradiction or strict
same-cardinality sub-`D` competitor.
