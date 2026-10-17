> Generated reading edition · [exact source](../../research/target_c_pentagon_three_gap_inequality_hostile_audit_2026-09-19.md) · source SHA-256 `42ab583341769fa61553f65650d8c41cf8e067de623ef89443ae975304b1f273`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bc7eee0be5db4d209da8ac33dbb2593329d5ab9b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_pentagon_three_gap_inequality_hostile_audit_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c13c36cf37c7b6475f1c59a204657910b5ace9c410121876ae8a2ed5cffa2d06"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — pentagon three-gap inequality

**Date:** 2026-09-19  
**Audited source:** `target_c_pentagon_three_gap_inequality_2026-09-19.md`  
**Verdict:** passes with the stated scope; no support-seven closure follows from this lemma alone.

## 1. Indexing and closure identity

The proof uses

```math
u_i+u_{i+1}+u_{i+2}=-(u_{i+3}+u_{i+4}).
```

The squared norm of the left side is

```math
3+2\cos\delta_i+2\cos\delta_{i+1}
+2\cos(\delta_i+\delta_{i+1}),
```

while the squared norm of the right side is

```math
2+2\cos\delta_{i+3}.
```

Thus the index `i+3` in the conclusion is correct; there is no hidden `i+2`/`i+4` shift.

## 2. The strict product bound is valid

Set `s=a+b`. The only delicate step is

```math
|a-b|<\frac{4\pi}{3}-s.
```

If `a>=b`, then `a-b=2a-s<4pi/3-s` because `a<2pi/3`; the other case is symmetric. Since `2pi/3<s<pi`, both `|a-b|/2` and `2pi/3-s/2` lie in `[0,pi]`, so the use of strict cosine monotonicity is legitimate.

The algebra

```math
\frac12\left(\cos\frac s2+
\cos\left(\frac{2\pi}{3}-\frac s2\right)\right)
=
\frac12\cos\left(\frac s2-\frac\pi3\right)
```

is correct: `cos A+cos B=2cos((A+B)/2)cos((A-B)/2)` and `(A+B)/2=pi/3`.

## 3. Final cosine comparison has the correct domain

The proof obtains

```math
\cos c>\cos(s-\pi/3).
```

The old bounds give

```math
0<c<2\pi/3,
\qquad
\pi/3<s-\pi/3<2\pi/3.
```

Both are in `(0,pi)`, so strict decrease of cosine gives `c<s-pi/3`. No inverse-cosine branch ambiguity is present.

## 4. Strictness is not lost at a boundary

The new inequality is strict because `a,b<2pi/3` is strict. Equality could only be approached when one of `a,b` approaches `2pi/3`; that boundary is excluded for a physical strict pentagon. The proof does not silently replace an open physical constraint by a closed one.

## 5. Reciprocal raw-gap corollary

For raw order `alpha_1<...<alpha_5` and minority positions `2,4`, the force cycle `(2,4,1,3,5)` gives the five gaps listed in the source. Direct coefficient cancellation gives

```math
x_2+x_3-x_0
=
\frac{(\alpha_2-\alpha_1)+(\alpha_5-\alpha_4)}{\pi}.
```

Global sign reversal changes `(2,4,1,3,5)` to the cyclic rotation `(1,3,5,2,4)`, so the cyclic family of inequalities is unchanged.

## 6. Scope check

The lemma is local. It does not prove that any of the twelve current convex support-seven `H8` orbits is empty, and it says nothing by itself about the nonconvex `H6/H7` branches. Any later use must still derive a contradiction or a resource payment from the stronger inequalities.

**Disposition:** the proof and raw-gap corollary are sound. The new information is exactly the five strict inequalities `x_i+x_{i+1}-x_{i+3}>1/3`; no stronger endpoint claim is licensed.
