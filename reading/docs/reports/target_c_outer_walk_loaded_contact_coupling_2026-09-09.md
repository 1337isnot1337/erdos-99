> Generated reading edition · [exact source](../../../docs/reports/target_c_outer_walk_loaded_contact_coupling_2026-09-09.md) · source SHA-256 `e406e0afde29dc2cc7487e92ef9fa24b235e044cf5a970b36d1789fcb02f3816`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-721004770081","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — outer-walk excess versus loaded-loaded contact coupling

**Date:** 2026-09-09  
**Run type:** exact planar-boundary coupling / post-ZF branch reduction  
**Target:** Target C C-II after ZF  
**Depends on:** C35 loaded-boundary interpretation, NM outer-walk interval decomposition, ZT exact terminal partition, DB diameter-edge density  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The post-ZF ledgers have treated

- `x_B=b-q`, the excess length of the outer contact-face walk beyond one step per loaded force-hull vertex; and
- `e_BB`, the number of unit contacts joining two loaded terminals,

as separate currencies. They are in fact coupled by a direct boundary argument.

Let the loaded force-hull vertices be `b_1,...,b_q` in cyclic order. Split one distinguished pass of the outer contact-face walk into the `q` subwalks `W_i` from `b_i` to `b_{i+1}`. NM already uses this decomposition and proves

```math
\sum_i(\ell_i-1)=x_B,
```

where `ell_i>=1` is the number of contact-edge occurrences in `W_i`.

Every interval with `ell_i=1` is literally the unit convex-hull side contact `b_i b_{i+1}`. Therefore only the outer-walk excess can destroy loaded-loaded hull-side contacts.

---

## 1. Exact hull-side contact theorem

Call `W_i` good when `ell_i=1` and bad when `ell_i>=2`. Let `m_bad` be the number of bad intervals. Since every bad interval contributes at least one unit to `ell_i-1`,

```math
\boxed{m_{bad}\le x_B.}
\tag{HB.1}
```

There are therefore at least

```math
q-m_{bad}\ge q-x_B
```

good intervals.

For a good interval the unique outer-walk edge has endpoints `b_i,b_{i+1}`. These are distinct loaded terminals and the edge is a unit contact. For `q>=3` the `q` cyclic hull sides are distinct unordered edges. Hence all good intervals give distinct edges counted by `e_BB`.

### Theorem HB.1 — hull-side loaded-contact coupling

Every sufficiently large fully force-visible C-II source satisfies

```math
\boxed{e_{BB}\ge q-x_B.}
\tag{HB.2}
```

Equivalently,

```math
\boxed{x_B+e_{BB}\ge q.}
\tag{HB.3}
```

No KKT weight is used. HB.2 is a statement about the actual contact graph of the same post-ZF source.

---

## 2. Convert to the exact post-ZF defect currencies

ZT gives

```math
\boxed{q=x_B+Q+2d_H+2s_Z.}
\tag{HB.4}
```

Substitute HB.4 into HB.2:

### Corollary HB.2 — direct contacts dominate face and mixed defects

```math
\boxed{
e_{BB}
\ge
Q+2d_H+2s_Z.
}
\tag{HB.5}
```

Thus each unit of bounded face defect must be matched by at least one loaded-loaded contact, while each diameter-tree-component defect or extra mixed row dependency costs at least two such contacts, unless that cost has already been paid as outer-walk excess before HB.5 is formed through the exact terminal partition.

In particular,

```math
\boxed{e_{BB}\ge Q+2s_Z,}
\tag{HB.6}
```

and

```math
\boxed{e_{BB}\ge2d_H.}
\tag{HB.7}
```

This is substantially stronger than treating `Q,d_H,s_Z` as independent of the loaded boundary contact graph.

---

## 3. Consequence for the pinned-contact ledger

ZU gives

```math
\boxed{c_I+e_{BB}+s_C=q-2+d_H+s_Z.}
\tag{HB.8}
```

Using HB.2,

```math
\begin{aligned}
c_I+s_C
&=q-2+d_H+s_Z-e_{BB}\\
&\le x_B+d_H+s_Z-2.
\end{aligned}
```

Hence

```math
\boxed{
c_I+s_C\le x_B+d_H+s_Z-2.
}
\tag{HB.9}
```

So a source with a short outer walk and small `d_H+s_Z` cannot hide a large number of unloaded components or pinned-contact stress dimensions: most of its boundary budget is already consumed by the mandatory loaded hull-side contacts.

The inequality is exact up to the integer constant `2`; no asymptotic estimate is used.

---

## 4. DB turns HB into a sharp two-way linear branch

DB proves

```math
\liminf\frac hD\ge2\rho,
\qquad
\rho=\cos\rho=0.7390851332\ldots .
\tag{HB.10}
```

The diameter-thrackle bound gives `q>=h`. Therefore

```math
\boxed{
\liminf\frac qD\ge2\rho
=1.4781702664\ldots .
}
\tag{HB.11}
```

Divide HB.3 by `D`:

```math
\liminf\frac{x_B+e_{BB}}D\ge2\rho.
\tag{HB.12}
```

Consequently every unbounded post-ZF survivor satisfies the two-way alternative

```math
\boxed{
 x_B\ge(\rho-o(1))D
}
\tag{HB.13}
```

or

```math
\boxed{
 e_{BB}\ge(\rho-o(1))D.
}
\tag{HB.14}
```

Numerically,

```math
\rho=0.7390851332\ldots .
```

This is much stronger than the crude three-way consequence of NB, whose individual threshold was only `0.2033 D`. NB remains stronger in a different sense because it lower-bounds diameter branching `2h-q`; HB instead says that the post-ZF source must pay a large amount directly on its outer walk and/or in loaded-loaded unit contacts.

---

## 5. Interaction with the GU threshold

GU uses

```math
\lambda_2
:=\limsup\frac{e_{BB}+2s_C}{D}
```

and forces a quadratic attachment-cell gap whenever

```math
\lambda_2<\lambda_*
:=\sqrt{\frac{\sqrt3}{\pi}}
=0.7425152492\ldots .
\tag{HB.15}
```

The HB contact threshold

```math
\rho=0.7390851332\ldots
```

lies only

```math
\lambda_* - \rho
=0.0034301160\ldots
```

below the GU transition.

More concretely, along any subsequence with

```math
\frac{e_{BB}+2s_C}{D}<\lambda_*-o(1),
```

we also have `e_BB/D<lambda_*+o(1)`. HB.3 and HB.11 then force

```math
\boxed{
\liminf\frac{x_B}{D}
\ge2\rho-\lambda_*
=0.7356550172\ldots .
}
\tag{HB.16}
```

Thus the GU low-surplus/macroscopic-gap branch necessarily carries an enormous outer-walk excess at the same time. A future cavity theorem can therefore assume both:

1. the GU quadratic attachment-cell gap; and
2. at least `0.73565 D-o(D)` extra outer-face contact-edge occurrences.

This is a narrower target than the previous generic macroscopic-gap branch.

---

## 6. Regressions

### Regular odd shell

For a regular unit odd shell, `x_B=0` and every hull side is a loaded-loaded contact, so `e_BB=q`. HB.2 is equality. ZT gives `Q=q-4`, `d_H=0`, `s_Z=2`, and HB.5 again gives equality:

```math
e_{BB}=q=Q+2s_Z.
```

Thus HB retains the main local/non-global shell regression.

### Unit square

Here `x_B=0`, `e_BB=q=4`, `Q=s_Z=0`, and `d_H=2`. Again HB.5 is equality:

```math
4=2d_H.
```

### Bridge/excursion-heavy outer face

A bad interval may contain arbitrarily complicated bridge excursions. HB does not attempt to convert its excess length to area. It charges that entire possibility honestly to `x_B`.

### Non-hull loaded-loaded chords

They only increase `e_BB`; HB counts only the guaranteed good hull-side contacts and does not assume every loaded-loaded contact lies on the hull boundary.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| at most `x_B` bad hull intervals | proved | `sum(ell_i-1)=x_B` |
| `e_BB>=q-x_B` | proved | every good interval is a distinct loaded-loaded unit hull side |
| `e_BB>=Q+2d_H+2s_Z` | proved | HB.2 + exact ZT partition |
| `c_I+s_C<=x_B+d_H+s_Z-2` | proved | HB.2 + ZU |
| `x_B+e_BB>=2rho D-o(D)` | proved post-DB | `q>=h` + DB |
| GU low-surplus branch has `x_B>=0.735655 D-o(D)` | proved | HB + GU threshold |
| large `x_B` itself forces an area contradiction | not proved | long thin outer excursions remain possible |
| large `e_BB` itself forces a triangle | not proved | convex shell regressions retain many hull contacts |

---

## 8. Next theorem

HB reduces the post-ZF topology to two concrete geometric targets:

1. **outer-excess branch:** `x_B>=rho D-o(D)`, meaning a linear amount of the outer contact-face walk lies beyond the one-edge convex loaded cycle;
2. **loaded-shell branch:** `e_BB>=rho D-o(D)`, meaning a linear family of actual unit contacts joins loaded force-hull vertices.

The GU low-surplus branch lies deep inside the first case, with the stronger bound HB.16 and an independent quadratic attachment-cell gap. The highest-value next step is therefore an outer-excursion area/capacity theorem that uses both pieces simultaneously.

The direct Level I face inequality remains open.
