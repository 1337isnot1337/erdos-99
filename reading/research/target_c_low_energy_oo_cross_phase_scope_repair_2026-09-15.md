> Generated reading edition · [exact source](../../research/target_c_low_energy_oo_cross_phase_scope_repair_2026-09-15.md) · source SHA-256 `8b9bfe10556597f476a7b5aa109466d1aca09b34ea711057884ef63ddd801b49`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 10 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8aa8551c0f048881c0656936e78f8cc9b150cab1", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_low_energy_oo_cross_phase_scope_repair_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "22b162022d3c9b7485cf42f5c6f65386814a093fd575dc340b84dbc66c98a121"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — scope repair for low-energy cross-phase O--O forcing

**Date:** 2026-09-15  
**Status:** hostile proof repair / dependency audit  
**Reviewed:** `research/target_c_low_energy_oo_cross_phase_forcing_2026-09-15.md` and downstream use in `research/target_c_two_leaf_outer_energy_exclusion_t18436_2026-09-15.md`  
**Disposition:** **PASS AFTER REPAIR** at the stated full-core Type-II near-disk scope  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The cross-phase O--O theorem is used downstream in the form

```math
\boxed{
\tau,\sigma\text{ noncrossing, phases separated by }\pi/3
\Longrightarrow
 e_\tau+e_\sigma\ge2-\sqrt3-o(1).
}
\tag{SR.1}
```

The original note proves the correct endpoint-energy formula and the correct
nonalternation cost, but its Section 3 only establishes the antipodal-branch
normalization under the individual threshold

```math
e_\tau\le{2-\sqrt3\over2}.
```

That is too narrow to justify asymmetric thresholds in its displayed theorem or the
unconditional implication (SR.1) as written.  In addition, the Section-3 comparison
between rhombus-count path length and a small endpoint separation is not by itself a
contradiction: a polygonal path may be much longer than the distance between its
endpoints.

Neither issue damages the theorem.  The already-proved terminal formula itself gives a
shorter and stronger branch-selection argument.  This note records that repair and
then rechecks the downstream `t<=1.8436` use.

---

## 1. Inputs retained from the parent theorem

Take one retained outer-to-outer complete train `tau` with projective phase `phi`.
Let its two outer terminal normal positions have smaller angular separation

```math
0\le w\le\pi,
```

and orient the interval as `[0,w]` with one representative of the train phase at
`phi in [0,w]`.  The hostile-audited Section-157/near-disk argument gives

```math
\boxed{
 e_\tau
 \ge [1-\sin\phi]+[1-\sin(w-\phi)]-o(1).
}
\tag{SR.2}
```

Define

```math
\alpha=\left|\phi-{\pi\over2}\right|,
\qquad
\beta=\left|w-\phi-{\pi\over2}\right|.
```

Then

```math
\boxed{
 e_\tau
 \ge (1-\cos\alpha)+(1-\cos\beta)-o(1).
}
\tag{SR.3}
```

The error is uniform after freezing the phase windows and then taking the Type-II
near-disk limit.

Also, using

```math
\sin\phi+\sin(w-\phi)
=2\sin(w/2)\cos(\phi-w/2)
\le2\sin(w/2),
```

(SR.2) gives the already-used terminal-separation estimate

```math
\boxed{
 e_\tau\ge2-2\sin(w/2)-o(1).
}
\tag{SR.4}
```

No rhombus-count path-length comparison is needed below.

---

## 2. Total energy below `2-sqrt(3)` selects the antipodal branches

Put

```math
c_*=2-\sqrt3.
```

Fix `eta>0` and suppose

```math
e_\tau\le c_*-\eta.
\tag{SR.5}
```

From (SR.3) and Jensen convexity of `1-cos x` on the relevant interval,

```math
2\left[1-\cos\left({\alpha+\beta\over2}\right)\right]
\le c_*-\eta+o(1).
```

Since

```math
c_*=2\left(1-\cos{\pi\over6}\right),
```

there is a number `rho(eta)>0` such that for all sufficiently large sources

```math
\boxed{
\alpha+\beta\le{\pi\over3}-\rho(\eta).
}
\tag{SR.6}
```

There is also a direct physical separation check.  Equation (SR.4) gives

```math
\sin(w/2)
\ge1-{e_\tau\over2}-o(1)
>{\sqrt3\over2}+{\eta\over3}
```

for all sufficiently large sources, after decreasing the harmless numerical margin.
Because `0<=w/2<=pi/2`,

```math
\boxed{
w>{2\pi\over3}+\rho'(\eta)}
\tag{SR.7}
```

for some `rho'(eta)>0`.

Thus the actual two outer terminals are separated by more than `120` degrees in the
round-limit normal coordinate.  The two endpoint deviations in (SR.3) therefore refer
to the two opposite ideal normals

```math
\phi-{\pi\over2},
\qquad
\phi+{\pi\over2},
```

rather than to two copies of one oriented projective branch.  This is exactly the
branch normalization needed in the cross-phase endpoint argument.

The conclusion is stronger than the original Section-3 threshold: every train with
energy strictly below `c_*`, not merely below `c_*/2`, has the required antipodal
orientation.

---

## 3. A noncrossing cross-phase pair costs `2-sqrt(3)`

Let `tau,sigma` be O--O trains from distinct atoms of one exact projective `pi/3`
orbit.  Suppose their midpoint crosscuts are noncrossing.

If, contrary to (SR.1), there were a fixed `eta>0` and an unbounded source sequence
with

```math
e_\tau+e_\sigma\le c_*-\eta,
\tag{SR.8}
```

then each individual energy is `<c_*-eta`.  Section 2 therefore gives the antipodal
branch normalization for both trains.

The ideal normal endpoints of two diameters whose projective axes differ by `pi/3`
alternate around the circle.  Noncrossing O--O Jordan crosscuts cannot have alternating
boundary endpoints, so at least one ideal `pi/3` boundary gap must close.  Therefore
one endpoint deviation from `tau` and one from `sigma`, say `a,b`, satisfy

```math
a+b\ge{\pi\over3}-o(1).
```

Their costs are included in `e_tau+e_sigma`, and convexity gives

```math
\begin{aligned}
e_\tau+e_\sigma
&\ge(1-\cos a)+(1-\cos b)-o(1)\\
&\ge2\left(1-\cos{a+b\over2}\right)-o(1)\\
&\ge2-\sqrt3-o(1),
\end{aligned}
```

contradicting (SR.8).  Hence uniformly in the frozen-window limit,

```math
\boxed{
\text{noncrossing}\Longrightarrow
 e_\tau+e_\sigma\ge2-\sqrt3-o(1).
}
\tag{SR.9}
```

This proves the downstream implication (SR.1).

---

## 4. The general asymmetric-threshold theorem is also repaired

Take positive thresholds `lambda_i,lambda_j` with

```math
\lambda_i+\lambda_j<2-\sqrt3.
```

Every selected pair with

```math
e_\tau\le\lambda_i,
\qquad
e_\sigma\le\lambda_j
```

has total energy strictly below `c_*`.  By Section 3, such a pair cannot be
noncrossing.  Therefore its endpoints alternate and the audited Jordan-arc argument
forces a strict-rhombus crossing.

Weighted Markov extraction now gives exactly the parent theorem

```math
\boxed{
X_{ij}
\ge
\left(P_i-{E_i\over\lambda_i}\right)_+
\left(P_j-{E_j\over\lambda_j}\right)_+.
}
\tag{SR.10}
```

Letting both thresholds tend upward to `c_*/2` gives the symmetric displayed
corollary.  Thus the theorem statement survives; only its Section-3 justification
needed replacement.

---

## 5. Audit of the `t<=1.8436` dependency

The two-leaf outer-energy exclusion uses the stronger pairwise form (SR.9) on two
high-center-degree leaf O--O families.  Every `U`-family train and every `V`-family
train share a center neighbor.  Triangle-freeness therefore makes each cross-leaf pair
noncrossing.  Equation (SR.9) applies to every pair in the complete weighted product,
so

```math
G_VE_U^g+G_UE_V^g
\ge(2-\sqrt3)G_UG_V-o(1).
```

Hence

```math
E_U+E_V
\ge(2-\sqrt3)\min(G_U,G_V)-o(1),
```

which is precisely the load-bearing step TE.26--TE.29.

The downstream certificate has

```math
G_U,G_V>0.17085-o(1)
```

and consequently a safe leaf-energy payment above `0.045770715D`.  Adding the
disjoint center-phase one-well payment above `0.0153173048D` gives more than
`0.061088D`, while the complete detour budget is below `0.05034454D`.  The final
margin exceeds `0.0107D`, so the repaired `o(1)` branch-selection argument has ample
room.

---

## 6. Disposition

- The original low-energy cross-phase theorem's displayed inequalities LE.1--LE.2 are
  **valid after this repair**.
- The old Section-3 rhombus-count/path-length comparison is **not used** in the repaired
  proof and should not be treated as the load-bearing branch-selection argument.
- The unconditional noncrossing cost used by the two-leaf common-center and
  `t<=1.8436` exclusion theorems is now proved at the required scope.
- The numerical certificates in those downstream theorems are unchanged.

**Final verdict:** PASS AFTER REPAIR.  The proof-only exclusion through
`t=1.8436` survives this dependency audit.  C-II and Level I remain open.
