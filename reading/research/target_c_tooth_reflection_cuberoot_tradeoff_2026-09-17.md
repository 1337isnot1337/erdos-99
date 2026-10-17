> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_cuberoot_tradeoff_2026-09-17.md) · source SHA-256 `75c078e7efb02363df0be6ecbb3b6a3409057ae84cff5a3f46e3474ca183c0dc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ca08dd0e061916c7940225d6b26d32aca838b065", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_cuberoot_tradeoff_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e5a60cdcacc8ed1f1058e21e4a99d97e4b71e814b893e5356cda7f75598eee57"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every all-inactive FREE ancestry has a cube-root face run or cube-root crossing braid

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; combines the two-boundary slack ledger with long-matching crossing extraction  
**Scope:** non-anchored FREE reflection modules, all-inactive ancestry branch  
**Dependencies:** two-sided inactive gate absorption; two-boundary slack tradeoff; two-sided outer-face localization; upper-poor deep-face run; long-matching crossing extraction  
**Certificate:** `research/verify_target_c_tooth_reflection_cuberoot_tradeoff_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current all-inactive FREE ancestry contains `D-O(sqrt D)` lower gates and an arbitrary number `U` of upper gates. The lower and upper boundary defects share one total budget

```math
\sum_{\rm lower}(|e|-1)
+
\sum_{\rm upper}(D-|e|)
\le t_D,
\qquad
 t_D<h_*+D^{-1/3},
```

where

```math
h_*={\sqrt{303}\over52}=0.334747984337100\ldots .
```

The upper-poor theorem already converts small `U` into one long near-unit run, and the two-sided outer-face theorem localizes every ancestry vertex and every lower run to the original outer contact face. The long-matching crossing theorem now handles large `U`. Balancing the two scales at

```math
\boxed{U\asymp D^{2/3}}
```

forces an unconditional `D^(1/3)` structure from every all-inactive FREE ancestry.

---

## 1. The dichotomy

Let `U` be the number of upper-gate edges on an all-inactive ancestry reaching the near-opposite threshold.

### Case A: `U < D^(2/3)`

Take

```math
M=\lceil D^{2/3}\rceil
```

in the upper-poor deep-face theorem. Since `U<M`, one consecutive all-lower run `R` lies in the original outer contact face and satisfies

```math
\boxed{
\operatorname{span}_N(R)
\ge
(1-o(1))D^{1/3}.
}
\tag{CR.1}
```

Its edge count obeys the same lower bound, up to `O(1)`, and it contains a vertex-disjoint matching of

```math
\boxed{
\left({1\over4}-o(1)\right)D^{1/3}
}
\tag{CR.2}
```

fully inactive original outer-face source pairs with

```math
\boxed{
1<|x-y|
\le
1+(2h_*+o(1))D^{-1/3}.
}
\tag{CR.3}
```

At terminal activation, the complete run is an exact weakly support-monotone unit chain.

Call this outcome `CUBEROOT-FACE`.

### Case B: `U >= D^(2/3)`

Let the original upper-gate deficits be

```math
\rho_j=D-|e_j|>0.
```

The two-boundary ledger gives

```math
\sum_{j\in E_{\rm up}}\rho_j\le t_D.
\tag{CR.4}
```

Therefore at least `U/2` upper edges satisfy

```math
\rho_j\le {2t_D\over U}.
\tag{CR.5}
```

Split these good upper edges by ancestry-index parity. One parity is a source matching `E_good` with

```math
\boxed{|E_{\rm good}|\ge U/4-O(1).}
\tag{CR.6}
```

Every endpoint in this matching is an old fully inactive outer-face source point, by two-sided outer-face localization. Every edge has

```math
|e|
\ge
D-\delta_U,
\qquad
\delta_U:={2t_D\over U}.
\tag{CR.7}
```

Apply Theorem LC.2 with

```math
L=D-\delta_U.
```

Its conflict radius satisfies

```math
\begin{aligned}
R_U^2
&=D^2-(D-\delta_U)^2\\
&=2D\delta_U-\delta_U^2\\
&\le {4t_DD\over U}.
\end{aligned}
\tag{CR.8}
```

Hence the good upper matching contains a pairwise-properly-crossing submatching of size at least

```math
\boxed{
{U/4-O(1)
\over
2\left(4\sqrt{t_DD/U}+1\right)^2+1}.
}
\tag{CR.9}
```

The right side is increasing with `U`. Its smallest value in this branch is attained asymptotically at `U=D^(2/3)`. Therefore

```math
\boxed{
|E_{\rm braid}|
\ge
\left({1\over128h_*}-o(1)\right)D^{1/3}.
}
\tag{CR.10}
```

Numerically,

```math
\boxed{
{1\over128h_*}
=0.0233384527033704\ldots .
}
\tag{CR.11}
```

Every braid edge is an **original-source**, vertex-disjoint pair of old fully inactive outer-face endpoints and satisfies

```math
\boxed{
D-(2h_*+o(1))D^{-2/3}
\le |x-y|<D.
}
\tag{CR.12}
```

All braid segments cross properly pairwise in the original source. No terminal-deformation equality is needed for that crossing claim.

Call this outcome `CUBEROOT-UPPER-BRAID`.

---

## 2. Why the exponent is `1/3`

For an upper-gate count `U`, the two mechanisms have natural sizes

```math
\text{same-face lower-run span}
\asymp {D\over U+1},
\tag{CR.13}
```

and, after the boundary-slack and bounded-conflict extraction,

```math
\text{upper crossing-braid size}
\asymp {U^2\over D}
\tag{CR.14}
```

through the range where `U=o(D)` and both asymptotics are informative.

Balancing

```math
{D\over U}
\asymp
{U^2\over D}
```

gives

```math
U\asymp D^{2/3},
\qquad
{D\over U}\asymp{U^2\over D}\asymp D^{1/3}.
```

Thus the cube-root scale is not an arbitrary choice of `M`; it is the balance point between the lower-face and upper-braid currencies.

---

## 3. Stronger variable-`U` statement

The proof gives more than the balanced dichotomy.

For every ancestry with `U` upper gates:

1. the lower gains contain one outer-face all-lower run with support span at least
   ```math
   {D-O(\sqrt D)\over U+1};
   
   ```
2. the upper gates contain a matching of at least `U/4-O(1)` edges of deficit at most `2t_D/U`;
3. that matching has a pairwise-crossing submatching of size bounded below by (CR.9).

When `U=o(D)`, (CR.9) has the scale

```math
\boxed{
\Omega\!\left({U^2\over D}\right).
}
\tag{CR.15}
```

Hence the all-inactive ancestry cannot simultaneously avoid a long single-face near-unit run and a large original-source near-diameter crossing braid.

---

## 4. Relation to the sharp superdiameter threshold

If the upper deficit drops below

```math
D-\sqrt{D^2-1}\sim {1\over2D},
```

the long-matching conflict radius is below one and every pair of matching edges crosses automatically. CR.9 is the quantitative continuation beyond that threshold.

This is needed here because at the balanced cube-root scale

```math
D-|e|=O(D^{-2/3}),
```

which is much larger than `1/D`. The bounded-conflict theorem loses only `O(D^(1/3))` neighbors per edge at that scale, leaving a `D^(1/3)` crossing subfamily.

---

## 5. Hostile checks and limitations

- `CUBEROOT-UPPER-BRAID` is entirely in the original source. The terminal exact-diameter gate graph is not used to infer crossings.
- No hull-vertex claim is made for the braid endpoints. At deficit `D^(-2/3)` the sharp superdiameter hull lemma does not apply.
- The braid endpoints are fully inactive only because this theorem is restricted to the all-inactive ancestry branch.
- `CUBEROOT-FACE` lies in the original outer contact face; the newer two-sided localization theorem removes the bounded-exceptional-face escape.
- The two outcomes are structural reductions, not contradictions. C-II remains open.

**Disposition:** every all-inactive FREE reflection ancestry now has a polynomial source-level normal form: either the original outer contact face contains a `D^(1/3)` support-deep near-unit run, or the original source contains a `D^(1/3)` pairwise-crossing braid of fully inactive outer-face endpoint pairs of length `D-O(D^(-2/3))`.
