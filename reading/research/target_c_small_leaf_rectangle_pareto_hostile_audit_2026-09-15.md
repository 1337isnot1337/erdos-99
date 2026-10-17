> Generated reading edition · [exact source](../../research/target_c_small_leaf_rectangle_pareto_hostile_audit_2026-09-15.md) · source SHA-256 `441f1ee7ab8b4758438a90d677bc80063aad0feb45d79dac5d14235b2a54fa18`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2e94cfb795099dafecccaa9ad4e906a1e90bdc95", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_small_leaf_rectangle_pareto_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6fd5bd6596d49032b61838910f0af0a57dd6d43177758f9f3a5d7a9627004c8d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — small-leaf complete-rectangle Pareto profile

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_small_leaf_rectangle_pareto_2026-09-15.md`
- `research/verify_target_c_small_leaf_rectangle_pareto.py`
- corrected dual-tree-backbone parent theorem `target_c_small_leaf_complete_rectangle_t1844_2026-09-15.md`

**Disposition:** **PASS at proof-only `t<=1.844` full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate does not introduce new topology. It keeps the parent theorem's consecutive block length symbolic and optimizes the resulting affine tradeoff. This audit checks that the actual backbone length may be replaced by its certified lower bound in the stated direction, that the `o(D)` terms remain harmless under division, and that the balanced/product corollaries are exact.

---

## 1. Parent inputs are used without strengthening

The corrected parent theorem gives a dual-tree backbone of `s=s_D` smallest-leaf outer-to-outer trains with

```math
s>s_0D-o(D),
\qquad
s_0={627\over42520},
```

each crossed by more than `d_0D-o(D)` center trains, where

```math
d_0={57\over100}.
```

The total center family satisfies

```math
N_C<n_0D+o(D),
\qquad
n_0={1063\over1000}.
```

For every center train, the backbone intersection is a consecutive interval because it is the intersection of two paths in the same tree. These are exactly the already-audited parent inputs; no global linear ordering of all leaf cuts is reintroduced.

**Verdict:** PASS.

---

## 2. Symbolic consecutive-block averaging has the correct normalization

For fixed `rho>0`, put `r=floor(rho D)`. The parent block-counting argument gives

```math
\sum_B \#\{\gamma:B\subset N(\gamma)\cap P_0\}
\ge I_0-(r-1)N_C,
```

with

```math
I_0>d_0sD-o(D^2).
```

There are `s-r+1<=s` blocks. Hence some block has common center neighborhood

```math
>{d_0sD-rN_C\over s}-o(D).
```

Because `s=Theta(D)` uniformly (`s/D` has positive lower limit `s_0`) and `r=rho D+O(1)`, division does not magnify the error beyond `o(D)`. Therefore

```math
|N(B)|>
\left(d_0-{\rho n_0\over s/D}\right)D-o(D).
```

This is the correct normalization.

**Verdict:** PASS.

---

## 3. Replacing the actual backbone density by `s_0` has the correct inequality direction

The penalty is

```math
{\rho n_0\over s/D}.
```

For positive `rho,n_0` this is decreasing in `s/D`. Since

```math
{s\over D}\ge s_0-o(1),
```

the worst asymptotic penalty occurs at the smallest allowed backbone density. Thus

```math
d_0-{\rho n_0\over s/D}
\ge d_0-{\rho n_0\over s_0}-o(1).
```

The candidate therefore weakens the actual block bound when it substitutes `s_0`; it does not reverse an inequality.

With

```math
\alpha={n_0\over s_0}={1129969\over15675},
```

the claimed profile

```math
|C_\rho|>(d_0-\alpha\rho)D-o(D)
```

is valid.

**Verdict:** PASS.

---

## 4. Parameter range is safe

The displayed center lower bound is positive exactly for

```math
0<\rho<{d_0\over\alpha}
={35739\over4519876}
=0.0079070753\ldots .
```

This upper endpoint is strictly smaller than

```math
s_0=0.0147460\ldots,
```

so `r<s` automatically for every fixed `rho` in the advertised range and all sufficiently large `D`. No separate block-existence condition is missing.

The theorem correctly notes that the topological extraction itself can be run farther, up to `rho<s_0`; only the stated quantitative center lower bound ceases to be useful after `rho_max`.

**Verdict:** PASS.

---

## 5. Balanced square arithmetic

Solving

```math
\rho=d_0-\alpha\rho
```

gives

```math
\rho_{bal}={35739\over4582576}
=0.00779888866\ldots .
```

The theorem uses the smaller rational value

```math
\rho={779\over100000}=0.00779.
```

The exact certificate gives

```math
d_0-\alpha\rho
={696271\over82500000}
=0.00843964848\ldots>0.00779.
```

Thus both shores are at least `0.00779D-o(D)`. The rounding has a substantial margin and is not sensitive to hidden decimal error.

**Verdict:** PASS.

---

## 6. Product optimum arithmetic

The guaranteed product profile is

```math
P(\rho)=\rho(d_0-\alpha\rho).
```

Since `alpha>0`, this is strictly concave and has unique critical point

```math
\rho_*={d_0\over2\alpha}
={35739\over9039752}
=0.0039535376634\ldots .
```

At this point

```math
d_0-\alpha\rho_*={d_0\over2}={57\over200}=0.285.
```

The exact product is `0.001126758234...`, as certified independently in Pyroam. The nearby simple value `rho=.00395` also has center lower bound `0.2852550207...`.

**Verdict:** PASS.

---

## 7. Scope

The result is a quantitative repackaging of one corrected structural theorem. It does not claim that large complete train rectangles themselves contradict global minimality, does not import the rejected global-stack shortcut, and does not claim distinct diameter bracing edges across leaf cuts.

Its value is downstream flexibility: strip-reuse arguments can use the wider `0.00779D` leaf block, while grid/shear arguments can use the product-optimal aspect ratio.

**Final disposition:** **PASS at proof-only scope. C-II and Level I remain open.**
