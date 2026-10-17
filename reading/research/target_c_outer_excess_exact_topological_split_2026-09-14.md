> Generated reading edition · [exact source](../../research/target_c_outer_excess_exact_topological_split_2026-09-14.md) · source SHA-256 `eecfe3bc6c32beef3825488350bbcbdc57711456e65443b3feaf3713f07bed27`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 10 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b06d2cd491b6a2f092f0434020e7aa622946e8b4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_outer_excess_exact_topological_split_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "40073e06a9b0ed781993718c3fbd0af780e1d64f963681700ee9329398d3e9ea"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — exact topological split of outer-walk excess

**Date:** 2026-09-14  
**Target:** Target C-II canonical full-core branch  
**Claim class:** exact graph-theoretic refinement of the outer-walk ledger  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`

Let `G=C` be the connected positive-contact core. Write

- `b` for the occurrence-counted outer-face boundary-walk length;
- `q` for the loaded force-hull vertex count;
- `x_B=b-q`;
- `E_out` for the distinct contact edges incident with the outer face;
- `V_out` for the distinct source vertices incident with the outer face;
- `B_br` for the number of contact bridges;
- `U_out:=|V_out|-q` for the distinct **nonloaded** outer-face vertices; and
- `r_out:=|E_out|-|V_out|+1` for the cycle rank of the connected outer-edge subgraph.

Canonical C51 says every contact bridge is incident only with the outer face. Hence the exact outer-walk count is

```math
b=|E_{out}|+B_{br}.
```

Since `(V_out,E_out)` is connected,

```math
|E_{out}|=|V_{out}|-1+r_{out}.
```

Therefore

```math
\boxed{
 x_B+1=B_{br}+U_{out}+r_{out}.
}
\tag{OE.1}
```

This strengthens the older one-sided bridge charge `B_br<=x_B+1` by identifying the full complementary currency.

---

## 1. Proof

Every nonbridge outer edge is traversed once by the outer-face boundary walk, while every bridge is traversed twice. Thus

```math
 b=|E_{out}|+B_{br}.
\tag{1.1}
```

The subgraph containing all outer-face vertices and all distinct outer-face edges is connected because the outer boundary is one closed walk whose edge set is exactly `E_out`. Its cyclomatic number is

```math
r_{out}=|E_{out}|-|V_{out}|+1\ge0,
```

so

```math
|E_{out}|=|V_{out}|-1+r_{out}.
\tag{1.2}
```

Every loaded force-hull vertex lies on the outer face, so

```math
|V_{out}|=q+U_{out}.
\tag{1.3}
```

Insert (1.2)--(1.3) into (1.1):

```math
 b=q+U_{out}-1+r_{out}+B_{br}.
```

Subtract `q` and rearrange to obtain (OE.1). `square`

---

## 2. Immediate trichotomy

Equation (OE.1) gives the finite bound

```math
\boxed{
\max\{B_{br},U_{out},r_{out}\}
\ge{x_B+1\over3}.
}
\tag{2.1}
```

Thus a linear outer-walk excess must be stored in at least one of three concrete objects:

1. contact bridges;
2. distinct nonloaded vertices exposed to the outer face; or
3. independent cycles in the subgraph of outer-face contact edges.

Repeated articulation traversal is not a fourth currency; it is already represented by bridges and/or the cycle structure of the connected outer subgraph.

---

## 3. AG58 low-`t` specialization

At the AG58 safe low-`t` endpoint write

```math
t={q-k\over D}=t_{58}=1.820922037979444\ldots,
```

```math
\delta={b-P_F\over D},
\qquad
\kappa={k\over D}.
```

Section 171 gives

```math
2\delta+{\kappa\over2}\le R_{58}=0.00575825.
\tag{3.1}
```

Type II gives `P_F/D->pi`, and hence

```math
{x_B\over D}
=\pi+\delta-t-\kappa+o(1).
\tag{3.2}
```

The smallest possible right side under (3.1) occurs at `delta=0`, `kappa=2R58`, giving

```math
\boxed{
\liminf{x_B\over D}
\ge1.30915411561035\ldots .
}
\tag{3.3}
```

Consequently every near-floor survivor has at least one of

```math
\boxed{
{B_{br}\over D},\quad {U_{out}\over D},\quad {r_{out}\over D}
}
```

with limsup at least

```math
\boxed{0.436384705203450\ldots .}
\tag{3.4}
```

The additive `1` in (OE.1) vanishes after normalization.

---

## 4. Composition with the forward-shadow theorem

The independent projection theorem gives

```math
2s_B+10E_{sh}
\ge x_B-2(b-P_F).
\tag{4.1}
```

Thus the same low-`t` outer boundary simultaneously carries

```math
x_B/D\ge1.3091541\ldots
```

units of exact topological excess and

```math
(2s_B+10E_{sh})/D\ge1.3091541\ldots
```

units of degree-slack/blocker obligation at the worst endpoint.

These are not independent inequalities, but they give two orthogonal descriptions of the same macroscopic boundary layer:

```text
outer topology:
    bridges + distinct unloaded outer vertices + outer cycle rank;

outer mechanics:
    loaded degree slack + extra blocker contacts.
```

A closing theorem should correlate the two rather than assigning separate budgets.

---

## 5. Scope

- `r_out` is the ordinary graph cycle rank of the **distinct-edge** outer-face subgraph; it is not the number of bounded faces of the full contact graph.
- `U_out` counts distinct nonloaded positive-core vertices, not occurrences.
- Contact-isolated source points are absent from the positive-contact core and do not enter the outer walk.
- No simplicity of the outer boundary walk is assumed.
- No stress weights are used.

**Disposition:** exact finite graph identity. C-II remains open.
