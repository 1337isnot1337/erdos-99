> Generated reading edition · [exact source](../../../docs/audits/target_c_paired_bathtub_exclusion_t18436_hostile_audit_2026-09-15.md) · source SHA-256 `cac43ec6d473a2bfb8aca50832bec64242a6adc94812d129d4933cea384b73d4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A71CCE9C278C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — paired-bathtub exclusion of `t<=1.8436`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_paired_bathtub_exclusion_t18436_2026-09-15.md`
- `research/verify_target_c_paired_bathtub_excludes_t18436.py`
- parent phase-resolved retained-mass theorem
- parent two-leaf common-center terminal-energy theorem

**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate combines two already-proved near-frontier facts that were previously
kept separate: a large retained outer-occurrence measure in each exact phase, and a
fixed amount of directional energy carried specifically by paired O--O terminal
weights in the two leaf phases.  The main audit risk is double counting the paired
energy when a bathtub bound is applied to the same occurrence measure.  The candidate
avoids that by subtracting the paired terminal submeasure before applying the second
bathtub bound.

---

## 1. Parent constants are inherited in the correct scope

The phase-resolved theorem applies for every full-core Type-II survivor with
`t<=1.844`, hence on the smaller band `t<=1.8436`.  It gives

```math
z_C+z_U+z_V>2.2069-o(1)
```

and

```math
\delta<0.051295+o(1).
```

The two-leaf common-center theorem applies directly on `t<=1.8436`.  It gives good
retained O--O pair weight in both leaves exceeding `0.06895-o(1)` and a complete
cross-leaf noncrossing relation after the common-center pruning.

No theorem is used outside its stated `t` range.

**Verdict:** PASS.

---

## 2. Fractional trimming preserves every needed property

Let the two good-family pair weights be `G_U,G_V`.  Since

```math
G_U,G_V>0.06895-o(1),
```

we may pass to the limit and reduce individual retained weights so that the selected
total pair weight in each leaf tends to

```math
g_0=0.06895.
```

Reducing a train weight cannot destroy:

- membership in the good family;
- the fact that every selected `U` train and every selected `V` train share a center
  neighbor;
- cross-leaf noncrossing; or
- the pairwise terminal-energy inequality.

Because retained pair weights are real weights, not integer train counts, a final train
may be fractionally trimmed.  This does not invoke a new combinatorial selection
lemma.

**Verdict:** PASS.

---

## 3. The paired terminal measure is genuinely dominated by the retained phase measure

For one selected O--O train with retained terminal weights `a_tau,b_tau`, the pair
weight is

```math
w_\tau=\min(a_\tau,b_\tau).
```

After trimming, put the selected weight `\widetilde w_tau<=w_tau` on **each** terminal
occurrence.  The resulting paired terminal measure `mu_i` satisfies

```math
\mu_i\le\nu_i
```

occurrence by occurrence, because

```math
\widetilde w_\tau\le a_\tau,
\qquad
\widetilde w_\tau\le b_\tau.
```

Each selected train contributes twice its pair weight to `mu_i`, so

```math
|\mu_U|=|\mu_V|\to2g_0=0.1379.
```

Thus the remainder measures

```math
\eta_i=\nu_i-\mu_i
```

are nonnegative and remain dominated by the same unit-density round measure used by
the parent bathtub theorem.

**Verdict:** PASS.

---

## 4. The paired energy and the remainder bathtub are disjoint currencies

The two-leaf theorem defines `E_i^{good}` by weighting the exact two-terminal
outer-directional energy of each O--O train by its pair weight.  That energy is part of
the already selected dominant outer directional-energy budget; the parent theorem
explicitly does not introduce a second energy currency.

After trimming, the phase occurrence weights split as

```text
paired terminal weight mu_i
+
remaining retained terminal weight eta_i.
```

The actual phase energy therefore splits additively between those two weight
submeasures.  On the paired part we retain the already-proved lower bound
`E_i^{trim}`.  On the remainder, the one-well cost lower bound gives

```math
\operatorname{energy}(\eta_i)
\ge f(z_i-0.1379).
```

Hence

```math
D_i\ge E_i^{trim}+f(z_i-0.1379)-o(1).
```

This is not

```math
D_i\ge E_i^{trim}+f(z_i),
```

which would indeed double count the paired mass.  The subtraction of `0.1379` is the
binding repair.

**Verdict:** PASS.

---

## 5. The trimmed cross-leaf energy remains above `0.01847`

Every selected cross-leaf pair is noncrossing and the two exact phases differ by
`pi/3`, so

```math
e_\tau+e_\sigma\ge2-\sqrt3-o(1).
```

Multiply by the two trimmed pair weights and sum over the complete product.  Since the
total trimmed weight is `g_0` on both shores,

```math
E_U^{trim}+E_V^{trim}
\ge(2-\sqrt3)g_0-o(1).
```

The exact rational enclosure

```math
\sqrt3<1.7321
```

gives

```math
(2-\sqrt3)(0.06895)>0.018471705>0.01847.
```

The inequality direction is correct: replacing the exact pair-energy constant by
`0.01847` weakens the lower bound.

**Verdict:** PASS.

---

## 6. Jensen is applied to the correct three residual masses

The center phase contributes a bathtub term `f(z_C)`.  The two leaves contribute
remainder terms

```math
f(z_U-0.1379),
\qquad
f(z_V-0.1379).
```

Their arguments have total

```math
\begin{aligned}
z_C+(z_U-0.1379)+(z_V-0.1379)
&>2.2069-0.2758-o(1)\\
&=1.9311-o(1).
\end{aligned}
```

The parent theorem separately gives `z_U,z_V>0.616-o(1)`, so the leaf arguments are
positive.  All three arguments remain below `pi`.  On this interval

```math
f'(s)=1-\cos(s/2)\ge0,
\qquad
f''(s)=\tfrac12\sin(s/2)\ge0.
```

Thus monotonicity and Jensen give

```math
f(z_C)+f(z_U-0.1379)+f(z_V-0.1379)
\ge3f(0.6437)-o(1).
```

No equal-phase-mass assumption is made; equality is only the convex relaxation.

**Verdict:** PASS.

---

## 7. Exact arithmetic has a large contradiction margin

The verifier bounds

```math
\sin x
< x-{x^3\over6}+{x^5\over120}
```

at

```math
x=0.6437/2=0.32185.
```

The alternating-series conditions are immediate at this positive `x`, and the next
term is negative.  Therefore it obtains the rigorous lower bound

```math
f(0.6437)>0.0110556445694\ldots .
```

Consequently

```math
3f(0.6437)+0.01847
>0.0516369337082\ldots .
```

Subtracting the parent ceiling `0.051295` leaves more than

```math
0.0003419>0.00034.
```

This is far larger than all omitted `o(1)` terms after passing to the limiting survivor
subsequence.

**Verdict:** PASS.

---

## 8. Scope and conclusion

The proof excludes only the full-core Type-II branch on which both parent theorems
apply.  It does not address the Type-I/inactive-container branch and does not prove an
exact equilateral triangle directly.

Within the stated scope, however, every limiting survivor with

```math
t\le1.8436
```

would simultaneously satisfy an outer-energy lower bound above `0.0516369` and an
upper bound below `0.051295`, which is impossible.

Thus the proof-only full-core Type-II floor is safely promoted to

```math
\boxed{\liminf (q-k)/D\ge1.8436.}
```

**Final verdict:** PASS.  This is a genuine band exclusion, not a decimal retuning of
the atomic gap.  C-II and Level I remain open.
