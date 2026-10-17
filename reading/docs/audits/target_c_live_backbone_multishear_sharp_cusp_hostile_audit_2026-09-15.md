> Generated reading edition · [exact source](../../../docs/audits/target_c_live_backbone_multishear_sharp_cusp_hostile_audit_2026-09-15.md) · source SHA-256 `15c036008e9d698d3b117605e48280d46e3cdf54032c2a0a58e7a027d7f46a30`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9A82C3694B7C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — sharp-cusp no-go for the live exact O--O multishear

**Date:** 2026-09-15
**Reviewed:** `research/target_c_live_backbone_multishear_sharp_cusp_nogo_2026-09-15.md`
**Disposition:** **PASS at the stated proof-only live-backbone scope.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate combines three recently merged facts:

1. the arbitrary O--O multishear is an exact finite contact-preserving deformation;
2. the live O--O backbone diameter-derivative matrix has full column rank; and
3. the canonical C-II lexicographic representative admits a relative-interior KKT
   stress positive on **all actual active diameter rows**.

The conclusion is a no-go result: on that full-rank backbone, every sufficiently small
nonzero exact multishear strictly increases the source diameter.  The audit concentrates
on support compatibility, the passage from weighted stationarity to a strict sign, and
uniform control of the finite Taylor remainder.

---

## 1. The KKT vector and the rank matrix use the same diameter-row set

A potential failure would be to take full column rank using all actual diameter rows
but use a KKT vector positive only on a smaller selected support.  Then a vector in the
kernel of the positive rows could still be detected by zero-weight rows, and the sign
argument would fail.

Canonical C-I restoration rules this out.  The C53/C63 dependency audit selects the
contact-minimal / diameter-pair-minimal representative for which the relative-interior
KKT stress sees every actual active contact and diameter row.  This is the same
representative used by the current C-II finite-shear and mixed-rigidity stack.  Thus

```math
\beta_h>0
```

for every actual diameter row appearing in the live-backbone derivative matrix `M`.

The live-backbone theorem proves

```math
\operatorname{rank}M=m
```

on those actual rows, not merely on an auxiliary selected subset.

**Verdict:** PASS.

---

## 2. KKT stationarity annihilates every selected shear column

For backbone cut `i`, the audited Section-157 resultant is

```math
A_i u_i=\sum_h\beta_h\varepsilon_{hi}r_h.
```

Dotting with `Ju_i` gives

```math
\sum_h\beta_h\varepsilon_{hi}(r_h\cdot Ju_i)=0.
```

The bracketed coefficient is exactly the live-backbone matrix entry

```math
M_{hi}=\varepsilon_{hi}(r_h\cdot Ju_i).
```

Therefore

```math
\beta^T M=0.
```

No factor of two from squared-distance differentiation matters to the kernel or sign.

**Verdict:** PASS.

---

## 3. Full rank plus positive weights forces both signs for every nonzero direction

Take `c!=0`.  Full column rank gives `Mc!=0`.  If every component of `Mc` were
nonpositive, then

```math
0=\beta^TMc
```

with every `beta_h>0` would force every component of `Mc` to vanish, contradiction.
The same argument for `-c` excludes every component being nonnegative.  Hence

```math
\max_h(Mc)_h>0,
\qquad
\min_h(Mc)_h<0.
```

This is stronger than coordinatewise two-sided bracing: it applies to every linear
combination of the selected train shears.

**Verdict:** PASS.

---

## 4. Compactness gives a source-specific quantitative cusp constant

The function

```math
g(c)=\max_h(Mc)_h
```

is continuous and strictly positive on the Euclidean unit sphere in the finite
`m`-dimensional shear space.  Therefore

```math
\gamma_0=\min_{\|c\|=1}g(c)>0.
```

The theorem does **not** claim a lower bound on `gamma_0` uniform in `D`.  Such a bound
would require singular-value information not supplied by the rank theorem.  The finite
source-specific positivity is sufficient for a local no-go statement.

**Verdict:** PASS.

---

## 5. The exact finite shear has a uniform quadratic remainder on the finite row set

For one row,

```math
r_h(\theta)=r_h+
\sum_i\varepsilon_{hi}(R_{\theta_i}u_i-u_i).
```

Every planar rotation has expansion

```math
R_su-u=sJu+O(s^2)
```

with an absolute local remainder bound.  The selected family and actual diameter-row
set are finite, so after summing at most `m` selected terms there is one finite constant
`C` and one neighborhood of the origin such that simultaneously for every actual
active diameter row

```math
|r_h(\theta)|^2-D^2
\ge2(M\theta)_h-C\|\theta\|^2.
```

No asymptotic-in-`D` uniformity is used.

Choose a row with `(M theta)_h>=gamma_0||theta||`.  For

```math
0<\|\theta\|<\gamma_0/C
```

one gets

```math
|r_h(\theta)|^2>D^2.
```

Therefore the full source diameter is strictly larger than `D`.

**Verdict:** PASS.

---

## 6. Contact feasibility is not needed to prove the diameter increase

The exact multishear theorem separately proves that all old unit contacts are preserved
and all strict old noncontacts stay longer than one in a sufficiently small parameter
neighborhood.  The sharp-cusp proof can intersect its radius with that feasibility
radius.

Even without doing so, the no-go statement about diameter is already valid because an
old actual diameter pair becomes longer than `D`.  Thus there is no hidden dependence
on inactive near-contact clearance in the sign proof.

**Verdict:** PASS.

---

## 7. Higher-order reparametrization does not evade the obstruction

Suppose a parameter path has first nonzero jet

```math
\theta(t)=t^k c+o(t^k),
\qquad c\ne0.
```

The same finite expansion gives

```math
\max_h(|r_h(\theta(t))|^2-D^2)
\ge2\gamma_0|t|^k\|c\|+o(|t|^k)>0.
```

Thus replacing a linear shear by `t^2c`, or any finite-order flat
reparametrization, cannot make the KKT-weighted second-curvature form load-bearing.
A genuinely different coordinate family is required to create a first-order critical
kernel.

The theorem does not address pathological parameter paths flat to all orders; the
local norm inequality in Section 5 is stronger anyway and excludes every sufficiently
small nonzero parameter vector directly.

**Verdict:** PASS.

---

## 8. Scope and frontier consequence

The conclusion applies to any selected O--O shear family with full-column-rank actual
diameter derivative matrix under the canonical full-support stress.  In particular it
applies to the current live `>0.017104D-o(D)` backbone.

It does not say that every conceivable contact-preserving deformation is cusp-locked.
The promising escape routes are exactly those outside the selected O--O coordinate
space: bounded-face flex coordinates, weak/inactive-contact activation coordinates, or
a structural contradiction showing that the full-rank interval-brace pattern itself
cannot exist in the near-disk geometry.

A negative value of the KKT weighted curvature matrix on the same full-rank O--O block
is therefore insufficient for C-II closure.  The first-order max cusp wins before the
quadratic term can affect diameter.

**Final verdict:** PASS.  The exact O--O multishear is a useful coordinate system but,
on the live full-rank backbone, is not a standalone descent mechanism.  C-II and Level
I remain open.
