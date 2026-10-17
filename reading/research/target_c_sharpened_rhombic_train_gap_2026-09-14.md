> Generated reading edition · [exact source](../../research/target_c_sharpened_rhombic_train_gap_2026-09-14.md) · source SHA-256 `ec63df24b67afde6e608bcde3da45706b2db561bb4f9dfe66a56143298b844a4`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "501ddc59cec974e7f5f8841474ab118d80f9e7d7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_sharpened_rhombic_train_gap_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d4ba2ee33a1cafd89ebc9798ad75f4f4f5faf80f1fbca6790b8dcc3395b3f615"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - sharpened explicit rhombic train gap

**Date:** 2026-09-14
**Repository base:** active `research/c2-closure-sol-20260914-r5` branch
**State version:** `2026-09-14.audit.51`
**Run type:** quantitative closing-proof reduction / rhombic train stability
**Target:** Target C-II, canonical full-core Type-II branch
**Claim class:** proved candidate awaiting independent audit
**External literature:** no new import
**Computation:** dependency-free outward constant regression only

## LEVEL I STATUS

`STILL OPEN`

The current explicit rhombic-train theorem gives

```math
\liminf {\sigma_R\over D}\ge0.00084,
\qquad
\sigma_R:=2T_R-4\sqrt{R_4},
```

where `T_R=B_4/2` is the number of non-singleton trains in the strict-rhombus
complex. That bound is obtained by doubling the AG42 atomic-mass gap. The atomic
argument contains more information when the **total rhombic train count itself** is
assumed close to Mantel equality.

Retaining the total majority mass across the two Mantel shores, rather than applying
the same worst-case minority loss separately to both shores, gives the stronger safe
bound

```math
\boxed{
\liminf_{D\to\infty}{\sigma_R\over D}\ge0.00119.
}
\tag{SG.1}
```

This is about a 41.7 percent increase over `0.00084`. The numerical root of the same
scalar certificate is about `0.00119968`, but no endpoint claim is needed here; the
round value `0.00119` leaves a comfortable strict diameter margin.

The proof uses only ingredients already audited for Sections 163, 166, and 168 and
already transferred to the rhombic-only crossing graph in
`target_c_explicit_rhombic_train_gap_2026-09-14.md`.

## 1. Normalize a hypothetical small-slack subsequence

Put

```math
\Delta_2={\pi\over2\sqrt3},
\qquad r:=\sqrt{\Delta_2},
\qquad s_0:=0.00119.
```

Assume for contradiction that a canonical full-core Type-II subsequence has

```math
{\sigma_R\over D}\to s<s_0.
\tag{SG.2}
```

Since `R_4/D^2 -> Delta_2` and

```math
\sigma_R=2T_R-4\sqrt{R_4},
```

we have

```math
x_R:={T_R\over D}\to 2r+{s\over2}
< x_0:=2r+{s_0\over2}.
\tag{SG.3}
```

Let `A_R` be the absolute `D`-normalized atomic train-direction mass from the
rhombic-only measure theorem. The transferred Sections 166/168 inputs give

```math
2r\le A_R\le x_R
\tag{SG.4}
```

and, after grouping atoms into `pi/3` projective orbits,

```math
E_j\le {M_j^2\over4},
\qquad
\sum_jE_j=\Delta_2,
\qquad
\sum_jM_j=A_R.
\tag{SG.5}
```

Let `M` be the largest orbit mass. Exactly as in Section 166,

```math
M\ge {4\Delta_2\over A_R}
>{4\Delta_2\over x_0}
=:M_0.
\tag{SG.6}
```

The total orbit/Mantel gap is

```math
G:={A_R^2\over4}-\Delta_2,
```

and the dominant-orbit Mantel deficit `delta` satisfies `delta<=G`. By (SG.3)--(SG.4),

```math
\delta
< d_0:={x_0^2\over4}-\Delta_2
={s_0r\over2}+{s_0^2\over16}.
\tag{SG.7}
```

Thus a small value of `sigma_R` controls both the **entire** rhombic-train population
and the dominant-orbit crossing deficit. This is stronger than assuming only an upper
bound on atomic mass.

## 2. Reuse finite Mantel stability, but keep total majority mass

Freeze shrinking continuity windows around the at most three atom directions in the
dominant orbit, exactly as in the audited finite-diagonal argument. On a sufficiently
far finite source, suppressing `o(D)` and `o(D^2)` terms, the selected orbit graph has

- total train mass at least `M_0 D`;
- Mantel deficit at most `d_0 D^2`.

The maximum-degree Mantel partition from Sections 166/168 gives shores `X,Y` with

```math
|X|,|Y|
\ge\left({M_0\over2}-\sqrt{d_0}-o(1)\right)D
\tag{SG.8}
```

and at most

```math
(2d_0+o(1))D^2
\tag{SG.9}
```

missing cross-shore pairs.

Write `x_i,y_i` for the normalized populations of the three atom windows on the two
shores. Same-window pairs cannot cross, so

```math
\sum_i x_i y_i\le2d_0+o(1).
\tag{SG.10}
```

Assign each atom window to its majority shore and discard the minority. If

```math
u_0:=\sqrt{6d_0},
```

then Cauchy--Schwarz gives

```math
\sum_i\min(x_i,y_i)\le u_0+o(1).
\tag{SG.11}
```

The standard Section-168 estimate applies separately to each shore, giving retained
mass at least

```math
L_0:={M_0\over2}-\sqrt{d_0}-u_0
\tag{SG.12}
```

on each shore.

Here is the additional bookkeeping. The **total** retained mass on both shores loses
the minority population only once, hence is at least

```math
M_0-u_0-o(1).
\tag{SG.13}
```

There are at most three assigned atom windows and both shores have positive retained
mass. Therefore one shore consists of one assigned window; call its population `a`.
The other shore contains at most two windows, so its largest window has population
`b` at least half that shore's retained mass. Consequently

```math
\begin{aligned}
a+b
&\ge {1\over2}(M_0-u_0)+{1\over2}L_0-o(1)\\
&= {3M_0\over4}-{\sqrt{d_0}\over2}-u_0-o(1).
\end{aligned}
\tag{SG.14}
```

This is strictly stronger than the previous `3L_0/2` lower bound. The old bound
charges the worst possible total minority loss once to each shore, even though each
minority train is discarded only once.

For later common-neighbor use we retain the individual bounds

```math
a\ge L_0-o(1),
\qquad
b\ge {L_0\over2}-o(1).
\tag{SG.15}
```

The chosen opposite-window pair inherits the global missing-pair budget (SG.9).

## 3. Quantitative phase and degree pruning

Put

```math
p_0:=\sqrt{2d_0}.
\tag{SG.16}
```

The tie-safe phase-separation argument can be run with the absolute threshold `p_0D`.
Since the inversion count is at most `(p_0^2+o(1))D^2`, it removes at most
`p_0D+o(D)` trains from each selected family and leaves strict phase order.

Then delete every retained train missing more than `p_0D+o(D)` opposite trains.
Again the total missing-pair budget removes at most `p_0D+o(D)` trains per shore.
Thus the two families after both prunings have total size at least

```math
\left(
{3M_0\over4}-{\sqrt{d_0}\over2}-u_0-4p_0-o(1)
\right)D,
\tag{SG.17}
```

and every surviving train misses at most `p_0D+o(D)` opposite trains.

The individual lower bounds are

```math
|A'|/D\ge L_0-2p_0-o(1),
\qquad
|B'|/D\ge L_0/2-2p_0-o(1).
\tag{SG.18}
```

The companion certificate checks

```math
L_0/2-2p_0>3p_0,
\tag{SG.19}
```

so every two and every three trains on one shore have a common neighbor on the other.
The audited Section-163 `K_{2,2}` consistency and triple-neighbor transitivity therefore
give global crossing orders.

## 4. Opposite-corner diameter contradiction

Use the Section-163 opposite-corner path. Its two endpoint trains each miss at most
`p_0D+o(D)` selected opposite trains. Combining this additional `2p_0D` degree loss
with (SG.17), the selected degree sum is at least

```math
\boxed{
E_0D-o(D),
\qquad
E_0:={3M_0\over4}-{\sqrt{d_0}\over2}-\sqrt{6d_0}-6\sqrt{2d_0}.
}
\tag{SG.20}
```

The atom windows shrink, so every selected unit train vector has common projection
`sqrt(3)/2-o(1)`. The actual source diameter must satisfy

```math
1\ge {\sqrt3\over2}E_0-o(1).
\tag{SG.21}
```

For `s_0=0.00119`, the outward arithmetic certificate proves

```math
E_0>{2\over\sqrt3}+0.00110,
\tag{SG.22}
```

and hence the right side of (SG.21) exceeds `1` by more than `9.5e-4` for all
sufficiently large sources. This is impossible.

Therefore (SG.2) cannot occur, proving (SG.1).

## 5. Immediate numerical consequences

The exact rationalization

```math
M_R={\sigma_R\over8}
\left(4\sqrt{R_4}+{\sigma_R\over2}\right)
```

now gives

```math
\boxed{
\liminf {M_R\over D^2}
\ge {0.00119\over8}
\left(4\sqrt{\Delta_2}+{0.00119\over2}\right)
>0.000566.
}
\tag{SG.23}
```

The previous `0.00084` train-slack floor implied about `0.0004000 D^2`; thus the
certified quadratic missing-crossing floor also rises by roughly 42 percent.

Any downstream theorem that uses only a universal lower bound on `sigma_R` or `M_R`
may now substitute (SG.1)/(SG.23). This does not by itself close C-II: a larger
rhombic Mantel deficit remains a payment currency rather than a source-level diameter
descent.

## 6. Scope audit

- `T_R`, not the complete train count `T`, is used throughout. Singleton stopped
  trains are not inserted into the rhombic crossing graph.
- The atomic relation support and finite-diagonal extraction are exactly the
  rhombic-only transfer already justified in
  `target_c_explicit_rhombic_train_gap_2026-09-14.md`.
- Atomic-mass semicontinuity is not used. Windows are frozen in a fixed subsequential
  limit before finite sources are selected.
- The improvement is only the majority-mass bookkeeping in (SG.13)--(SG.14); phase
  pruning, degree pruning, crossing-order globalization, and the source-diameter path
  are the already-audited Sections 163/168 mechanisms.
- Contact-isolated source points remain in the full source.
- The AG42 `0.00042` theorem is not needed as an input to (SG.1); this is an
  independent sharpening of the rhombic-only stability route.
- No claim is made about the macroscopic inactive-container branch.
- No exact unit triangle and no same-cardinality strict sub-`D` competitor is produced.

**Disposition:** new proof-only candidate. C-II and Level I remain open.
