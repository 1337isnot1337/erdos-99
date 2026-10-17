> Generated reading edition · [exact source](../../research/target_c_qk_bootstrap_exceptional_chambers_2026-09-14.md) · source SHA-256 `2f7d83bc25aba2050329ad30304792bfd7cbe5f158fec9668139f687b3d31309`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "90b855337d237aa892d340be05b55efeab9085ed", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_qk_bootstrap_exceptional_chambers_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f0b26cf1cc41ddec878ebeb5632daecb7f3222aca6e9cf375cfa264c647557e7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — q-k bootstrap and forced exceptional chambers

**Date:** 2026-09-14
**Repository base:** `9d7998d8c3f5e60f0cd47b844ae30e141e78bcaa`
**State version:** `2026-09-14.audit.51`
**Run type:** closing-proof reduction / bootstrap across audited-working Type-II ledgers
**Target:** Target C-II, canonical full-core Type-II branch
**Claim class:** proof-only consequence awaiting independent audit
**External literature:** no new import
**Computation:** dependency-free constant regression only

## LEVEL I STATUS

`STILL OPEN`

Two recent proof-only inputs can be composed more strongly than in the current notes:

1. AG42 gives
   
   ```math
   {T-q/2\over D}\ge C_* -o(1),
   \qquad
   C_*:=2\sqrt{\Delta_2}+0.00042;
   \tag{QB.1}
   ```

2. the §171 AG42 refinement gives
   
   ```math
   {q-k\over D}\ge t_* -o(1),
   \qquad
   t_*:=C_{146}+0.0013751,
   \quad
   C_{146}={4\over9}(\pi+\sqrt{\Delta_2}).
   \tag{QB.2}
   ```


The first input by itself already forces linearly many bounded nonquadrilateral contact
faces. The second replaces the much weaker difference-body lower bound on `q` when the
all-train endpoint/interface currency is estimated. The result is a stronger chamber
package than the previous correlated-surplus propagation.

No source-preserving deformation or exact unit triangle is proved.

## 1. AG42 forces linearly many bounded exceptional faces

The exact all-train ledger is

```math
T=q+2f-k.
\tag{QB.3}
```

Therefore

```math
T-{q\over2}={q\over2}+2f-k.
\tag{QB.4}
```

Every force-hull side joins distinct unit-separated source points, so each side has
length at least one and hence

```math
q\le P_F.
\tag{QB.5}
```

Since `k>=0`, (QB.4) gives the finite upper bound

```math
T-{q\over2}\le {P_F\over2}+2f.
\tag{QB.6}
```

In the full-core Type-II branch `P_F/D->pi`. Combining with (QB.1),

```math
\boxed{
\liminf {f\over D}
\ge f_*:=\sqrt{\Delta_2}-{\pi\over4}+0.00021
=0.167124643466509\ldots .
}
\tag{QB.7}
```

Thus a full-core survivor contains at least `0.1671D-o(D)` actual bounded
nonquadrilateral contact faces. This is a geometric face count, not a train-graph or
local induced-cell count.

Because every such face has degree at least five,

```math
Q\ge f,
\qquad
P_{exc}^{global}:=4f+Q\ge5f,
```

so also

```math
\boxed{
\liminf {Q\over D}\ge f_*,
\qquad
\liminf {P_{exc}^{global}\over D}\ge5f_*
=0.835623217332545\ldots .
}
\tag{QB.8}
```

This does not identify `P_exc^global` with the Section-123 local induced-cell sum.

## 2. Bootstrap the all-train endpoint/interface floor with §171

Define as before

```math
J_D:=(b-P_F)+(Q+4f).
\tag{QB.9}
```

The outer/train handshakes give the exact finite identity

```math
J_D=2T-P_F.
\tag{QB.10}
```

Also

```math
2T=q+2\left(T-{q\over2}\right).
```

Since `q=(q-k)+k>=q-k`, (QB.1)--(QB.2) and `P_F/D->pi` imply

```math
\boxed{
\liminf {J_D\over D}
\ge j_{171}:=t_*+2C_* -\pi
=2.489387211845480\ldots .
}
\tag{QB.11}
```

This strictly improves the previous correlated-hull value
`2.146668840296357...`, which used only the difference-body lower bound
`q/D>=2rho-o(1)`.

The improvement is structural rather than decimal: it feeds the independent §171
`q-k` pressure back into the all-train endpoint ledger.

## 3. Propagation through Section 85

Put

```math
H_D:=(b-P_F)+(Q+2f).
\tag{QB.12}
```

As in canonical Section 85,

```math
5H_D-3J_D=2[(b-P_F)+(Q-f)]\ge0,
```

hence

```math
\boxed{H_D\ge {3\over5}J_D.}
\tag{QB.13}
```

Thus

```math
\boxed{
\liminf {H_D\over D}
\ge {3\over5}j_{171}
=1.493632327107288\ldots .
}
\tag{QB.14}
```

The exact face count and outer ledger give

```math
m-R_4={P_F+H_D\over2}+1,
\tag{QB.15}
```

where here `m` is the positive-contact-core population. Therefore

```math
\boxed{
\liminf {m-R_4\over D}
\ge c_{171}:={\pi\over2}+{3j_{171}\over10}
=2.317612490348541\ldots .
}
\tag{QB.16}
```

Canonical Section 85 also gives

```math
A_{ch}-a_0Z_{ch}\ge c_0H_D,
\qquad
a_0={\sqrt3\over2},
\quad c_0={\sqrt3\over4}.
```

Hence

```math
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge \beta_{171}:={3c_0\over5}j_{171}
=0.646761769594289\ldots .
}
\tag{QB.17}
```

In particular `A_ch>=0.6467617695...D-o(D)`.

## 4. Chamber perimeter and chamber count

Canonical Section 77 decomposes total inactive-chamber perimeter as

```math
P_{ch}=P_{exc}^{global}+P_{out},
```

with

```math
P_{out}=b+P_F-2q+2a,
```

where `a>=0` is the number of outer pockets. Since `P_F>=q`,

```math
P_{out}\ge b-P_F.
```

Therefore

```math
\boxed{P_{ch}\ge J_D,}
\tag{QB.18}
```

and

```math
\boxed{
\liminf {P_{ch}\over D}\ge j_{171}
=2.489387211845480\ldots .
}
\tag{QB.19}
```

The total number `s_ch` of inactive chambers is `f+a`, so (QB.7) gives

```math
\boxed{
\liminf {s_{ch}\over D}\ge f_*
=0.167124643466509\ldots .
}
\tag{QB.20}
```

Thus the inactive region is not merely forced to have boundary-order area and
perimeter: it has linearly many actual convex chambers.

## 5. Chamber Oler-slack floor above `2.1586 D`

Canonical Section 77 defines

```math
\Sigma_{ch}
={A_{ch}-a_0Z_{ch}\over a_0}+{P_{ch}\over2}+s_{ch}.
\tag{QB.21}
```

Since `c_0/a_0=1/2`, (QB.13), (QB.17), (QB.18), and (QB.20) give

```math
\Sigma_{ch}
\ge {H_D\over2}+{J_D\over2}+s_{ch}
\ge {4\over5}J_D+s_{ch}.
\tag{QB.22}
```

Consequently

```math
\boxed{
\liminf {\Sigma_{ch}\over D}
\ge \sigma_{171}:={4\over5}j_{171}+f_*
=2.158634412942893\ldots .
}
\tag{QB.23}
```

This is substantially larger than the previous `1.717335...D` floor.

Again, it is not legitimate to compare this local chamber-slack sum directly with the
single Oler slack of the full source hull: internal chamber perimeter contributes
`P_ch/2` to (QB.21). A closure theorem must cancel or pay that internal perimeter.

## 6. Absolute rhombus-count deficit

The full-source Oler upper bound is

```math
n\le\Delta_2D^2+{\pi\over2}D+1.
```

Since `m<=n`, (QB.16) implies

```math
\boxed{
\liminf {\Delta_2D^2-R_4\over D}
\ge \gamma_{171}:={3j_{171}\over10}
=0.746816163553644\ldots .
}
\tag{QB.24}
```

Equivalently,

```math
\boxed{
\liminf {\pi D^2/4-a_0R_4\over D}
\ge a_0\gamma_{171}
=\beta_{171}
=0.646761769594289\ldots .
}
\tag{QB.25}
```

The matching numerical coefficient in (QB.17) is not accidental: both arise from the
same Section-85 currency `H_D`.

## 7. Why this still does not close C-II

The new package forces all of the following simultaneously:

```text
f/D >= 0.1671246434... - o(1),
P_exc^global/D >= 0.8356232173... - o(1),
J_D/D >= 2.4893872118... - o(1),
H_D/D >= 1.4936323271... - o(1),
(m-R_4)/D >= 2.3176124903... - o(1),
(A_ch-a_0 Z_ch)/D >= 0.6467617695... - o(1),
P_ch/D >= 2.4893872118... - o(1),
s_ch/D >= 0.1671246434... - o(1),
Sigma_ch/D >= 2.1586344129... - o(1).
```

These are first-order constraints. The full-core branch permits linearly many thin
inactive chambers, and Section 77 gives only an `O(D)` upper bound on their total Oler
slack. No current theorem gives an upper coefficient below `2.1586`.

The best next target is therefore more specific than another scalar floor:

> prove an additive Oler-slack gluing inequality in which the internal boundaries of
> the inactive chambers are cancelled against the positive-contact core, leaving only
> the outer source-hull boundary plus already-controlled rhombic angular defect.

If such a gluing inequality bounded the left side of (QB.23) by a coefficient below
`2.1586`, the full-core branch would close. Without internal-boundary cancellation,
local chamber Oler inequalities cannot be summed sharply enough.

A second live target is the face count (QB.7): linearly many actual bounded exceptional
faces must coexist with the near-disk rhombic phase system. A geometric theorem forcing
positive width/area cost per defect face after phase conditioning would also close the
thin-corridor escape.

The macroscopic-container branch is untouched.

## 8. Scope audit

- `T` is the all-stopped-train count from the canonical train ledger, including
  singleton stopped trains.
- `R_4` counts bounded strict unit-rhombus faces.
- `f,Q` are the global contact-graph exceptional-face currencies, not Section-123 local
  induced-cell quantities.
- `m` in (QB.15)--(QB.16) is the positive-core population, not the nonunit-hull-side
  count denoted `m` in the older five-currency note.
- The §171 value `t_*` and AG42 value `0.00042` are proof-only pending theorem-state
  promotion; all consequences here inherit that status.
- Every source point is retained. No full-source affine-kernel statement is used.
