> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_db_surplus_2026-09-11.md) · source SHA-256 `2bc0161a7ae14df71a0c10fcba9e2ab7eea0ddf2e21a377c8cff91c57a2cac66`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-82F1C6E7CD9E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — diameter-density surcharge in the zero-transfer branch

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact branch synthesis / quantitative consequence  
**Target:** Target C, C-II  
**Status:** STILL OPEN; hold as report

This report records a conditional strengthening of the zero-transfer forest
branch. It combines the bounded-star conclusion of the zero-transfer response
argument with the defect-dependent diameter-edge density bound. It does not
promote any report-level ZF/ZE/ZK/PC input and does not close C-II.

## 1. Theorem

Let

```math
S_D=e_{BB}+2s_C,
\qquad
\nu_D=\frac{S_D-3d_H}{D}.
```

Assume the report-level post-ZF stack used by the zero-transfer report,
including the general-surplus estimate

```math
\liminf\nu_D\ge0.597+\varepsilon_{597}
\tag{1.1}
```

for some fixed $`\varepsilon_{597}>0`$, the zero-transfer alternative
$`\min_{e\ne f}K_{ef}=0`$, and the diameter-density theorem

```math
\liminf\frac hD\ge2\rho,
\qquad \rho=\cos\rho=0.7390851332\ldots.
\tag{1.2}
```

Then

```math
\boxed{
\liminf\frac{d_H}{D}\ge\frac\rho2
}
\tag{1.3}
```

and consequently

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge 0.597+\frac{3\rho}{2}+\varepsilon_{597}
=1.7056276998\ldots+\varepsilon_{597}.
}
\tag{1.4}
```

The same conclusion holds with any positive report-level gap in place of
$`\varepsilon_{597}`$; only the displayed numerical baseline uses the explicit
$`0.597`$ ledger.

## 2. Proof

The zero-transfer response theorem gives three facts. First, $`H`$ is a forest.
Second, every connected component of $`H`$ is a star. Third, every such star
has at most four edges. If $`d_H`$ is the number of forest components and
$`h=|H|`$, summing the component edge bounds gives

```math
h\le4d_H.
\tag{2.1}
```

Therefore

```math
\frac{d_H}{D}\ge\frac14\frac hD.
```

Taking lower limits and using (1.2) proves (1.3). The exact definition of
$`\nu_D`$ gives

```math
\frac{S_D}{D}=\nu_D+3\frac{d_H}{D}.
\tag{2.2}
```

Combine (1.1), (1.3), and (2.2):

```math
\liminf\frac{S_D}{D}
\ge0.597+\varepsilon_{597}+\frac{3\rho}{2}.
```

The decimal is the evaluation of
$`0.597+3(0.7390851332\ldots)/2`$. This proves (1.4). $`\square`$

## 3. Exact effect on the branch ledger

The earlier zero-transfer report only used $`h\ge D`$, yielding
$`d_H\ge D/4`$ and an ordinary-surplus lower bound above (1.347D). The
diameter-density input changes this to

```math
d_H\ge(0.3695425666-o(1))D
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
and the stronger ordinary-surplus threshold (1.4). Thus a zero-transfer
survivor is forced into a genuinely high-surplus regime. This is a branch
restriction, not an upper bound: the present theorem does not contradict a
configuration with $`S_D/D`$ above (1.7056\).
```



The strict-negative alternative

```math
\min_{e\ne f}K_{ef}<0
```

is unaffected. It may have $`d_H=o(D)`$, and no response surcharge of the
form (1.4) follows from the current identities.

## 4. Audit and regressions

- **Contact-isolated sources:** not used in the response or density inequalities;
  they remain retained in the report-level full-source inputs.
- **Regular odd shells:** not excluded by the numerical lower bound; they are
  high-surplus examples of the type the theorem permits.
- **Common contact block:** the proof uses only the zero-transfer star theorem;
  it does not extend bridge positivity to a 2-edge-connected block.
- **Strict-negative transfer:** no claim is made that it is impossible or that it
  pays the same component charge.
- **Global optimality:** the inputs are conditional report-level consequences of
  the lexicographic global-minimizer setup; the theorem does not replace them
  with density or local-jamming reasoning.

## 5. Remaining obstruction

To close the zero-transfer branch one still needs an opposing global upper bound
below (1.7056D+o(D)), or a direct competitor. No such bound is available in
the promoted theorem stack. The full remaining C-II ledger is therefore:

1. cyclic topology, with (s_Z=0) or (s_Z>0), including the high-surplus
   cyclic branch;
2. forest topology with strict-negative transfer;
3. forest topology with zero transfer but ordinary surplus at least the value in
   (1.4); and
4. positive $`s_Z`$ outside the report-level ZF stack.

The report remains unpromoted.
