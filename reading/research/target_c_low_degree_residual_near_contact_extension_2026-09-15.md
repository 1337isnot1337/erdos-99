> Generated reading edition · [exact source](../../research/target_c_low_degree_residual_near_contact_extension_2026-09-15.md) · source SHA-256 `e5bab10a8dbc6e3ddb9891b4e7e20018f7dc6965514e6293eeef13e17600767f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e8a5b4c7236b243b8f6588a6feb30c8f6895ffe4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_low_degree_residual_near_contact_extension_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "fff38374c0d65f3c33bfad18457b1cf1bccd32b0c43e30ecd828cae729ddfb2e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — degree-5/6 face sea extends the residual/near-contact fork through `t<=2.1854`

**Date:** 2026-09-15
**Status:** proof-only source-level structural strengthening
**Scope:** canonical full-core Type-II branch at any fixed endpoint below the certified degree-6 staircase threshold
**Dependencies:** low-degree exceptional-face staircase; degree-`>=7` isolate-host theorem; exact inactive-chamber residual conservation; Wegner/Groemer stability for equilateral 5- and 6-faces; canonical contact-degree bound `deg_C<=5`
**Certificate:** `research/verify_target_c_low_degree_residual_near_contact_extension.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The pentagon residual theorem stops when the pentagon-only floor vanishes near `t=2.02157`. The modern low-degree staircase shows that this is not the end of the low-degree geometry: a linear population of bounded pentagon-or-hexagon contact faces persists to

```math
 t<X_6,
 \qquad
 X_6={6C_{707}+4\pi\over11}>2.1854,
```

where

```math
 C_{707}=2\sqrt{\pi/(2\sqrt3)}+0.007707.
```

Both degrees five and six are exactly the degrees for which the audited Wegner theorem classifies Oler equality, and the isolate-host theorem says both face types contain no assigned inactive source points. Consequently the exact residual argument extends without a new packing theorem.

Let

```math
F_{56}:=f_5+f_6.
```

For every fixed endpoint `t<=T<X_6`, the staircase gives

```math
\boxed{
 {F_{56}\over D}
 \ge L_6(T)-o(1),
 \qquad
 L_6(T):={3C_{707}/2+\pi-11T/4\over2}.
}
\tag{LR.1}
```

The conclusion is the following high-`t` fork.

### Theorem LR — residual or endpoint-disjoint hidden near contacts

Along every unbounded survivor sequence in the stated scope, either

```math
\limsup {R_F\over D}>0,
\tag{LR.2}
```

or `R_F=o(D)` and there is a matching `M_D` of inactive source pairs with

```math
\boxed{
 |M_D|
 \ge\left({L_6(T)\over9}-o(1)\right)D,
 \qquad
 \max_{xy\in M_D}(|x-y|-1)\to0.
}
\tag{LR.3}
```

Thus the sublinear-residual branch carries linearly many endpoint-disjoint almost-active unit constraints through the safe endpoint `t<=2.1854`, not merely through the pentagon cutoff.

## 1. The chamber residual equals normalized Oler slack for both degrees

Let `P` be a bounded exceptional contact face of degree `d in {5,6}`. The hostile-audited isolate-host theorem gives

```math
z_P=0.
```

Its fixed chamber boundary consists of exactly its `d` unit contact sides, so

```math
k_P=d,
\qquad
P_P=d.
```

With `a_0=sqrt(3)/2`, exact chamber residual conservation defines

```math
r_P={A_P\over a_0}+{d\over2}+1-d.
```

The equilateral-face Oler minimum is

```math
A_{min}(d)={\sqrt3\over4}(d-2)={a_0\over2}(d-2).
```

Therefore, exactly,

```math
\boxed{
 r_P={A_P-A_{min}(d)\over a_0}.
}
\tag{LR.4}
```

In particular `r_P>=0`, and residual conservation gives

```math
\boxed{
 \sum_{P:\deg P\in\{5,6\}}r_P\le R_F.
}
\tag{LR.5}
```

## 2. Wegner stability is uniform at each fixed hidden-distance margin

For `d=5,6`, the audited scaled Wegner equality theorem says that zero Oler slack is exactly a finite Groemer/Wegner packing and therefore contains a nonboundary unit pair.

For every fixed `eta>0`, compactness consequently gives positive constants

```math
\sigma_5(\eta)>0,
\qquad
\sigma_6(\eta)>0
```

such that a convex equilateral unit-separated `d`-face all of whose nonconsecutive pairs have distance at least `1+eta` satisfies

```math
A_P\ge A_{min}(d)+\sigma_d(\eta).
```

Set

```math
c(\eta):={\min\{\sigma_5(\eta),\sigma_6(\eta)\}\over a_0}>0.
```

If

```math
h(P):=\min_{xy\text{ nonconsecutive in }P}(|x-y|-1),
```

then (LR.4)--(LR.5) imply the finite estimate

```math
\boxed{
 \#\{P:\deg P\in\{5,6\},\ h(P)\ge\eta\}
 \le {R_F\over c(\eta)}.
}
\tag{LR.6}
```

Hence if `R_F=o(D)`, then for every fixed `eta>0` all but `o(D)` of the linearly many faces counted by (LR.1) have a hidden nonedge shorter than `1+eta`.

A diagonal choice `eta_D downarrow 0` gives a family `G_D` with

```math
|G_D|\ge(L_6(T)-o(1))D,
\qquad
\max_{P\in G_D}h(P)\to0.
\tag{LR.7}
```

Choose one minimizing hidden pair `e_P` from each such face.

## 3. Endpoint matching costs only a factor nine

The previous pentagon residual theorem extracted vertex-disjoint *faces*, which costs a factor 21. For the activation problem only the selected hidden-pair endpoints need to be disjoint.

A source vertex belongs to at most `deg_C(v)<=5` distinct bounded face boundaries. Therefore, after selecting one hidden pair from each face in `G_D`, any source vertex is an endpoint of at most five selected pair occurrences.

Regard the chosen pairs as a multigraph on source vertices. Its maximum degree is at most five. A chosen pair `xy` conflicts with at most

```math
(5-1)+(5-1)=8
```

other chosen pair occurrences. Greedy edge selection therefore gives a matching of at least one ninth of all chosen pairs:

```math
\boxed{|M_D|\ge{|G_D|\over9}.}
\tag{LR.8}
```

Combining (LR.7)--(LR.8) proves (LR.3). Repeated candidate pairs from different faces cause no problem: they share both endpoints and are simply mutually conflicting occurrences in the same greedy extraction.

## 4. Certified representative rows

The exact companion certificate gives the following deliberately rounded-down matching densities in the sublinear-residual branch:

```math
\begin{array}{c|c|c}
T & F_{56}/D\text{ lower} & |M_D|/D\text{ lower}\\ \hline
2.00 & 0.2550 & 0.0283\\
2.05 & 0.1862 & 0.0206\\
2.10 & 0.1175 & 0.0130\\
2.15 & 0.0487 & 0.0053\\
2.18 & 0.0075 & 0.0008\\
2.1854 & 0.00012 & 0.00001
\end{array}
\tag{LR.9}
```

The exact positivity threshold satisfies `X_6>2.1854`.

## 5. Relation to the pentagon sensor theorem

The factor-nine matching is an endpoint-disjoint source matching. It does **not** replace the vertex-disjoint pentagon family used by the hidden-diagonal train-sensor theorem: that theorem needs distinct pentagons not to reuse terminal face occurrences when proving sensor-graph degree at most two.

For pentagons one may therefore retain both extractions:

- factor `9` for the strongest source-pair activation matching;
- factor `21` for the stronger vertex-disjoint-face hypothesis needed by the current train-sensor rank theorem.

For hexagons a Wegner-forced hidden unit pair can also span three boundary edges, so no two-train sensor identity is asserted here.

## 6. Updated high-t frontier

The residual route now has a natural low-degree endpoint:

```text
fixed t < 2.1854:
  either R_F is linear along a subsequence,
  or there are linearly many endpoint-disjoint inactive pairs at distance 1+o(1).
```

This is materially wider than the O-O path frontier `1.86177` and the pentagon-only residual frontier `2.0215`.

A further extension above `2.1854` would require either a Wegner/Oler stability theorem for degree at least seven or a different use of the low-degree staircase, because degree-7 faces may also store contact-isolated source points.

No simultaneous activation, diameter decrease, or exact unit diagonal is claimed.

**Disposition:** proved proof-only degree-5/6 residual/near-contact extension through the certified `t<=2.1854` frontier. C-II and Level I remain open.
