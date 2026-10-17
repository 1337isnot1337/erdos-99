> Generated reading edition · [exact source](../../../docs/reports/target_c_bridge_outer_walk_currency_2026-09-09.md) · source SHA-256 `737cd4ac05e91bfd064f1bd9448353a43240f13bbc84f036bcd71ba493cc846f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-607916E5E6D3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZOB: bridge stress forces exact outer-walk surplus

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** exact topological/stress coupling  
**Target:** Target C, post-ZF C-II / Level I  
**Depends on:** C23/C51 and the exact ZT terminal ledger  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The post-ZF ledger treats

```math
x_B:=b-q
```

as the outer-face boundary-walk excess beyond the `q` loaded convex-hull vertices. The bridge branch had previously treated total contact-bridge stress `S_br` as a separate mechanical currency.

They are directly coupled.

C51 proves every positive contact bridge is incident only with the outer face. In a connected plane graph the unique-edge outer-face subgraph is connected and contains every loaded hull vertex. The outer boundary walk counts each nonbridge outer edge once and every bridge twice. Therefore each contact bridge contributes, up to one tree baseline edge, one exact unit of `x_B`.

Combining this with the universal bridge bound `alpha_e<=D` gives the particularly simple consequence

```math
\boxed{
S_{br}\ge\eta D^2
\Longrightarrow
x_B\ge\eta D-1.
}
```

This holds before any C66 small-response assumption.

---

## 1. Outer-face edge accounting

Let `G=C` be the connected positive contact core. Write

- `b` for the length of the outer-face boundary walk, with multiplicity;
- `q=|B|` for the number of loaded convex-hull vertices;
- `B_br` for the number of contact bridges of `G`;
- `E_out` for the set of **distinct** contact edges incident with the outer face;
- `V_out` for the vertices incident with the outer face.

C51 proves that no contact bridge occurs on a bounded face boundary. Hence every contact bridge belongs to `E_out` and is incident with the outer face on both sides.

Every nonbridge edge in `E_out` has the outer face on exactly one side and is traversed once by the outer boundary walk. Every bridge has the same outer face on both sides and is traversed twice. Consequently

```math
\boxed{
 b=|E_{out}|+B_{br}.
}
\tag{ZOB1}
```

The outer-face boundary of a connected plane graph is one closed walk, so the subgraph `(V_out,E_out)` is connected. Therefore

```math
|E_{out}|\ge |V_{out}|-1.
\tag{1.1}
```

Every loaded force-hull vertex lies on the outer face, so

```math
|V_{out}|\ge q.
\tag{1.2}
```

Insert (1.1)-(1.2) into ZOB1:

```math
 b\ge q-1+B_{br}.
```

Thus:

### Theorem ZOB.1 — bridge count is outer-walk currency

```math
\boxed{
 x_B=b-q\ge B_{br}-1.
}
\tag{ZOB2}
```

Equivalently,

```math
\boxed{B_{br}\le x_B+1.}
\tag{ZOB3}
```

The additive `1` is sharp at the graph-theoretic level: for a tree whose outer-face vertex set is its full vertex set, `b=2|E|`, `q=|V|=|E|+1`, so `x_B=B_br-1`.

---

## 2. Mechanical bridge stress gives a linear bridge count

For a contact bridge `e`, C23 gives

```math
\alpha_e\le D w_e,
\tag{2.1}
```

where `w_e` is the total normalized diameter beta mass crossing the bridge cut.

Because

```math
\sum_{h\in H}\beta_h=1,
```

we have

```math
0<w_e\le1.
```

Hence every contact bridge satisfies the absolute bound

```math
\boxed{\alpha_e\le D.}
\tag{ZOB4}
```

Summing over the `B_br` bridges,

```math
S_{br}:=\sum_{e\text{ bridge}}\alpha_e
\le DB_{br}.
\tag{2.2}
```

Therefore

```math
\boxed{
B_{br}\ge\frac{S_{br}}D.
}
\tag{ZOB5}
```

Combine with ZOB2:

### Theorem ZOB.2 — exact stress-to-outer-surplus transfer

```math
\boxed{
 x_B
\ge
\frac{S_{br}}D-1.
}
\tag{ZOB6}
```

In particular, if for fixed `eta>0`

```math
S_{br}\ge\eta D^2,
```

then

```math
\boxed{
 x_B\ge\eta D-1.
}
\tag{ZOB7}
```

No response-defect, stress-star, or asymptotic radialization hypothesis is used.

---

## 3. Exact interaction with the post-ZF terminal ledger

Current main proves the exact partition

```math
\boxed{
q=x_B+f+g_F+2d_H+2s_Z.
}
\tag{3.1}
```

Hence ZOB gives

```math
\boxed{
 f+g_F+2d_H+2s_Z
\le
q+1-\frac{S_{br}}D.
}
\tag{ZOB8}
```

In the bridge-dominant phase,

```math
\boxed{
 f+g_F+2d_H+2s_Z
\le q-\eta D+1.
}
\tag{ZOB9}
```

Thus bridge dominance is not an additional uncharged phase: it spends a linear amount of the same finite terminal budget that must also pay for exceptional faces, diameter tree components, and extra mixed stress dependencies.

Since `q<=pi D`, one also gets the coarse finite ceiling

```math
\boxed{
S_{br}\le D(x_B+1)\le D(q+1)\le\pi D^2+D.
}
\tag{ZOB10}
```

The first inequality is exact route information; the latter perimeter bound is only a coarse global check.

---

## 4. Interaction with NB

Current main's NB theorem gives

```math
 r_H:=2h-q=x_B+Q+2s_Z
\ge(c_*-o(1))D,
\qquad
c_*=0.6099043189\ldots.
\tag{4.1}
```

ZOB identifies a concrete portion of this mandatory diameter-branching currency in the bridge-dominant branch:

```math
\boxed{x_B\ge\eta D-o(D).}
\tag{ZOB11}
```

Therefore, once a bridge-stress fraction `eta` is fixed, NB's remaining required amount beyond the bridge topology is only

```math
Q+2s_Z
\ge
(c_*-\eta-o(1))D
\tag{4.2}
```

when `eta<c_*`; for `eta>=c_*`, the outer-walk currency alone can satisfy NB.

This is a phase localization, not a contradiction. It prevents future proofs from treating `S_br`, `x_B`, and NB's branching defect as independent linear costs.

---

## 5. Interaction with ZHT/ZHL

Under the stronger bridge-dominant small-defect hypotheses, ZHT gives a consecutive macroscopic bridge trunk of length

```math
H\ge\frac{\eta^2}{16\pi}D.
```

ZOB implies the stronger global bridge-count floor

```math
B_{br}\ge\eta D,
```

and hence

```math
x_B\ge\eta D-1.
```

The gap between `eta D` total bridges and the smaller guaranteed ZHT trunk length means a bridge-dominant source may still distribute many bridges outside the captured trunk. ZHT remains essential because it localizes a linear **consecutive high-stress** subfamily into one harmonic cell; ZOB supplies the global exact topological currency.

ZHL independently gives

```math
e_{BB}+2s_C\ge\frac{\eta^2}{16\pi}D-O(1)
```

in the small-defect trunk phase. Thus that phase simultaneously pays two distinct post-ZF currencies:

```math
\boxed{
 x_B\ge\eta D-O(1),
\qquad
 e_{BB}+2s_C\ge\frac{\eta^2}{16\pi}D-O(1).
}
\tag{ZOB12}
```

Current identities do not yet make those two costs contradictory with the boundary degree or area budgets, but any future currency-coupling theorem can now use explicit lower bounds on both axes.

---

## 6. Regression checks

### Pure tree

For a tree with all outer vertices counted as `q`, every edge is a bridge and

```math
b=2B_{br},
\qquad q=B_{br}+1,
```

so ZOB2 is equality.

### Cycle with attached bridge trees

Every tree edge is traversed twice by the outer walk. The cyclic outer edges provide the connected baseline `|E_out|>=|V_out|-1`; each bridge adds one extra walk traversal beyond that baseline, exactly as ZOB2 records.

### Bounded dangling branch

Excluded in C-II by C51: any articulation branch contains a loaded hull vertex, so no bridge is trapped on a bounded face.

### Large bridge count with tiny stresses

Allowed. ZOB2 is unweighted. ZOB7 needs bridge-dominant total stress to force a linear count, but does not lower-bound individual stresses.

---

## 7. Exact remaining use

ZOB does not close Level I. The exact closing defect remains

```math
(b+Q)-2h=-2s_Z.
```

The useful consequence is that the bridge-dominant branch can no longer be analyzed as a separate mechanical phenomenon. It must satisfy simultaneously

```math
x_B=\Omega(D),
```

NB's exact diameter-branching constraints, and, in the small-defect trunk phase,

```math
e_{BB}+2s_C=\Omega(D).
```

The next high-value target is an exact boundary/area coupling theorem that upper-bounds the simultaneous pair `(x_B,e_BB+2s_C)` for a globally diameter-minimal triangle-free source, or else uses the ZHT/ZHN radial trunk geometry to force additional `Q` or `s_Z` currency.

---

## 8. Classification

**Status:** proved report-level exact theorem.  
**Level I:** still open.  
**External literature:** none newly imported.  
**Computation:** none.  
**Dependencies:** C23, C51, current-main ZT/NB for the stated corollaries.
