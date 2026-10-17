> Generated reading edition · [exact source](../../../docs/reports/target_c_minimal_interface_internal_train_defect_2026-09-09.md) · source SHA-256 `fae4f0b1d0b69106009a2ccf2f0d0a19d0bfa04041c1fe7b1bd1caa66163af22`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 13 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-0CD060F4C5CC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_minimal_interface_internal_train_defect_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=92b06e60085267bbd46a0e42db2eb99ba0841516; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — minimal loaded-interface equality forces linear internal carrier defect

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** exact stopped-train consequence in corrected FS equality branch  
**Target:** full-core near-circle endpoint with `Q_B/D->2`  
**Depends on:** corrected FS, AS/CF, DT/DS finite stopped-train inequality  
**Computation:** displayed constants only

## LEVEL I STATUS

`STILL OPEN`

The first version of FS incorrectly tried to import DS.3, whose semicircle-carrier form assumes the additional cap-minimal graph-metric fact `delta_i/D->1`. That overclaim has been corrected.

However the **finite** DS.1 inequality itself does not use graph diameter at all. In the minimal-interface equality branch, AS/CF supplies exactly the population and outer-walk inputs needed to apply it directly.

For each of the two dominant half-disk harmonic components `I_i`,

```math
\boxed{
\frac{Q_i+4f_i}{D}
\ge
2\left(
\sqrt{\frac\pi{\sqrt3}}
-\frac\pi4-\frac12
\right)-o(1)
=0.1227510474\ldots-o(1).
}
\tag{IT.1}
```

Since every exceptional face contributes at least one unit to `Q_i`, so `f_i<=Q_i`, this implies

```math
\boxed{
\frac{Q_i}{D}
\ge
\frac25\left(
\sqrt{\frac\pi{\sqrt3}}
-\frac\pi4-\frac12
\right)-o(1)
=0.02455020948\ldots-o(1).
}
\tag{IT.2}
```

Therefore

```math
\boxed{
Q_{\rm int}:=Q_1+Q_2+Q_{\rm minor}
\ge
0.0491004189\ldots D-o(D).
}
\tag{IT.3}
```

This is a valid internal-defect consequence of `Q_B/D->2` and does **not** assume `S/D->2` or `delta_i/D->1`.

Thus the sharp interface equality model cannot have squaregraph-like half-disk interiors. Even when the interface itself is at its minimum coefficient two, both positive-density carriers must contain a linear number/degree budget of internal stopped-train faults.

---

## 1. Inputs at minimal interface defect

Assume

```math
Q_B=(2+o(1))D.
```

Corrected FS proves two dominant components `I_1,I_2` with

```math
n_i:=|I_i|
=\left(\frac\Delta2+o(1)\right)D^2,
\qquad
\Delta=\frac\pi{2\sqrt3}.
\tag{1.1}
```

AS/CF proves their component outer-face walk lengths satisfy

```math
\boxed{
k_i=\left(1+\frac\pi2+o(1)\right)D.}
\tag{1.2}
```

No assertion about `delta_i/D` beyond the lower bound `>=1-o(1)` is needed below.

Let

- `f_i` be the number of bounded nonquadrilateral faces of `C[I_i]`;
- `Q_i=sum_F(deg F-4)` over those faces.

Post-ZF face budgets give `f_i,Q_i=O(D)`, but only `f_i<=Q_i` is used for IT.2.

---

## 2. Apply the finite stopped-train inequality

DS.1 is the finite theorem

```math
k+Q+4f\ge4\sqrt{n+f}-4
\tag{2.1}
```

for every connected triangle-free unit-contact graph.

Apply it to `C[I_i]`:

```math
Q_i+4f_i
\ge
4\sqrt{n_i+f_i}-4-k_i.
\tag{2.2}
```

Since `f_i=O(D)` while `n_i=Theta(D^2)`, (1.1) gives

```math
\frac{4\sqrt{n_i+f_i}}D
\to4\sqrt{\frac\Delta2}
=2\sqrt{\frac\pi{\sqrt3}}.
\tag{2.3}
```

Equation (1.2) gives

```math
\frac{k_i}{D}\to1+\frac\pi2.
\tag{2.4}
```

Divide (2.2) by `D` and use (2.3)--(2.4):

```math
\liminf\frac{Q_i+4f_i}{D}
\ge
2\sqrt{\frac\pi{\sqrt3}}-1-\frac\pi2.
```

Equivalently,

```math
\boxed{
\liminf\frac{Q_i+4f_i}{D}
\ge
2\left(
\sqrt{\frac\pi{\sqrt3}}-\frac\pi4-\frac12
\right).
}
```

This is IT.1.

Numerically,

```math
\sqrt{\frac\pi{\sqrt3}}-\frac\pi4-\frac12
=0.06137552369\ldots,
```

so the right side is

```math
0.12275104738\ldots .
```

---

## 3. Convert train endpoint defect to face degree defect

Every bounded nonquadrilateral face has degree at least five, so

```math
Q_i\ge f_i.
\tag{3.1}
```

Therefore

```math
Q_i+4f_i\le5Q_i.
```

Combine with IT.1:

```math
\boxed{
\liminf\frac{Q_i}{D}
\ge
\frac25\left(
\sqrt{\frac\pi{\sqrt3}}-\frac\pi4-\frac12
\right)
=0.02455020948\ldots .
}
```

This proves IT.2.

Summing `i=1,2` and using nonnegativity of every minor-component defect gives IT.3.

---

## 4. Equality structure of the internal defect bound

IT.2 itself has a clear extremal pattern. To make `Q_i` approach its minimum coefficient, both inequalities must nearly saturate:

1. `f_i<=Q_i` must satisfy
   
   ```math
   Q_i-f_i=o(D),
   ```

   so almost every unit of internal face defect is carried by pentagons (`deg=5`);
2. DS.1 must nearly saturate its Mantel step, so the stopped-train crossing graph of `I_i` must be asymptotically extremal triangle-free at its leading `Theta(D^2)` crossing scale.

Thus the least expensive internal fault model is not arbitrary. It consists of a near-bipartite stopped-train system broken by a linear family of asymptotically pentagonal faults.

No stability theorem for the Mantel equality is imported here; this paragraph only identifies the equalities that a sharp sequence would need to approach.

---

## 5. Interaction with the exact terminal budget

HBd gives throughout the near-circle branch

```math
Q+2s_C=(\pi+o(1))D.
\tag{5.1}
```

In the present equality branch

```math
Q=Q_B+Q_{\rm int}
```

with `Q_B=(2+o(1))D`. IT.3 therefore gives

```math
\boxed{
Q\ge2.0491004189\ldots D-o(D).
}
\tag{5.2}
```

Consequently

```math
\boxed{
s_C
\le
\frac{\pi-2.0491004189\ldots}{2}D+o(D)
=0.5462461173\ldots D+o(D).
}
\tag{5.3}
```

This is not contradictory, but it removes another `0.02455D` per carrier from the pinned-stress side of the exact terminal budget.

---

## 6. What remains

Minimal loaded-interface defect now forces **both** kinds of boundary-order fault:

```text
loaded interface:
    one central exceptional face with Q_F*=(2+o(1))D

inside each half-disk carrier:
    Q_i >=0.02455020948... D-o(D)
    and Q_i+4f_i >=0.12275104738... D-o(D).
```

A closing theorem can therefore target their compatibility rather than trying to eliminate either fault class separately.

The most promising next step is to combine the explicit C43/C44 harmonic-response theorem with the two carrier geometry. Both dominant attachment sets have diameter `(1-o(1))D`, so they lie in the long-response branch of the quantitative anti-Reuleaux dichotomy. This supplies a fixed response-mass and contact-stress obligation for **each** half-disk carrier. The question is whether two disjoint semicircle carriers can satisfy those response obligations while the terminal defect matrix has only the remaining trace/stress budget in (5.3).

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| IT.1 | proved | finite DS.1 + corrected FS population + AS outer-walk length |
| IT.2 | proved | `f_i<=Q_i` |
| IT.3 | proved | sum two dominant components |
| uses `delta_i/D->1` | no | graph diameter absent from DS.1 |
| near-Mantel/pentagon equality description | necessary equality conditions only | no stability conclusion claimed |
| Level I | still open | `Q_int≈0.0491D` fits global terminal budget |

---

## 8. Next target

Insert PR #132's explicit anti-Reuleaux/C44 Branch-B constants separately for the two dominant components. If their response matrices contribute additively to a terminal trace or stress quantity with a sharp global upper bound, IT's loss of pinned-stress budget may produce the first direct contradiction in the minimum-interface equality branch. If additivity fails because the two response atoms can share the same terminal modes, that overlap should be characterized explicitly.
