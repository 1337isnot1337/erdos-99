> Generated reading edition · [exact source](../../research/target_c_g0050_physical_boundary_propagation_2026-09-14.md) · source SHA-256 `3a9b80bc3444bf010521eba0ed5475487ecd73f2be2b1237ae6743a891181867`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Erdős Problem #99 — matched `g=0.0050` physical boundary propagation

**Preservation provenance (2026-10-15):** the archived original-worktree06 README
attributes this report to `research/c2-g0050-physical-sol-20260914` at
`a81de9a0515076eb49bed6da8f555593a5d651c1`. The full report and its verifier
already matched current-main bytes; this addition preserves the missing index
attribution. The existing proof remains an unreviewed candidate under its stated
matched hypotheses. Its verifier checks displayed decimal inequalities and
constants, and supplies no positive KKT weights, stress floor or finite descent.
The [worktree reconciliation](../docs/audits/original_dirty_worktree_reconciliation_2026-10-15.md)
records the exact source comparison; it performs no new proof promotion.

**Date:** 2026-09-14  
**Target:** C-II, canonical full-core Type-II branch  
**Dependencies:** matched iterative-pruning atomic gap `g=0.0050`; Section-171 `epsilon=0.0023374`; exact outer-tooth/long-side dichotomy; shallow-tooth apex injectivity; outer-route directional-energy identity  
**Claim class:** proof-only source-level propagation awaiting independent audit  
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The matched iterative-pruning theorem raises the all-train and rhombic atomic gap to

```math
 g=0.0050
```

and the safe Section-171 floor to

```math
 t={q-k\over D}
 \ge t_{50}:=C_{146}+0.0023374,
 \qquad
 C_{146}={4\over9}(\pi+\sqrt{\Delta_2}),
 \quad
 \Delta_2={\pi\over2\sqrt3}.
```

The most useful propagation is source-level rather than another scalar floor.  The
low-`t` topology budget makes outer detour tiny while the exact outer-walk identity
forces a large tooth/long-side burden.  The two branches therefore yield robust
linear families of actual unit contacts with quantitative directions.

Put

```math
 s:=\sqrt{\Delta_2},
 \qquad C_{50}:=2s+0.0050.
```

At `t=t_50`, the exact low-`t` remainder is

```math
 R_{50}:={9t_{50}\over2}-2\pi-C_{50}
 =4.5(0.0023374)-0.0050
 =0.00551830.
\tag{PB.1}
```

Hence

```math
 \boxed{
 {d_{out}\over D}\le\delta_{50}:={R_{50}\over2}
 =0.00275915+o(1),
 }
\tag{PB.2}
```

and `k/D<=2R_50+o(1)=0.01103660+o(1)`.

The exact tooth/long-side theorem gives

```math
 {N_2+2L_{>2}\over D}
 \ge M_{50}-o(1),
 \qquad
 M_{50}:=5\pi+2C_{50}-10t_{50},
\tag{PB.3}
```

so every survivor lies in one of

```math
 \boxed{{N_2\over D}\ge B_{50}-o(1)}
 \qquad\text{or}\qquad
 \boxed{{L_{>2}\over D}\ge B_{50}-o(1)},
\tag{PB.4}
```

where

```math
 \boxed{
 B_{50}:={M_{50}\over3}
 =0.4362350385367828\ldots .
 }
\tag{PB.5}
```

The raw boundary burden remains close to the older one.  The gain is that the detour
payment in both physical conversions is now smaller.

---

## 1. Tooth branch: almost-optimal shallow penetration

Fix any

```math
 0<\eta<2(1-\cos(\pi/12)).
```

The exact tooth detour identity and apex-injectivity theorem give

```math
 {N_{sh}(\eta)\over D}
 \ge B_{50}-{\delta_{50}\over\eta}-o(1),
\tag{PB.6}
```

and the shallow apices are distinct.  Choosing one extra contact per apex and
remembering that one undirected contact may be selected from at most two endpoints,

```math
 \boxed{
 {E_{pen}(\eta)\over D}
 \ge {1\over2}\left(B_{50}-{\delta_{50}\over\eta}\right)-o(1).
 }
\tag{PB.7}
```

Every selected edge has inward normal component larger than

```math
 Y_\eta
 ={\sqrt3\over2}(1-\eta/2)
 -{1\over2}\sqrt{\eta-\eta^2/4}.
\tag{PB.8}
```

The count-maximizing endpoint `eta=1/15` gives

```math
 \boxed{
 {E_{pen}(1/15)\over D}
 \ge0.1974238942683914\ldots-o(1)
 }
\tag{PB.9}
```

with inward component

```math
 Y_{1/15}=0.7091387945271472\ldots .
```

For a directional-mass statement, the exact convenient choice

```math
 \eta={3\over50}=0.06
```

is nearly optimal for the guaranteed product `Y_eta E_pen(eta)`.  It gives

```math
 \boxed{
 {E_{pen}(3/50)\over D}
 \ge0.1951246026017247\ldots-o(1),
 }
\tag{PB.10}
```

```math
 \boxed{Y_{3/50}>0.7184921838594731,}
\tag{PB.11}
```

and therefore the sum of the inward normal components over the selected distinct
penetration contacts satisfies

```math
 \boxed{
 {1\over D}\sum_{e\in E_{pen}(3/50)}
 \operatorname{proj}_{in}(e)
 >0.14019550-o(1).
 }
\tag{PB.12}
```

This is an unweighted geometric sum over actual unit contacts; no KKT multiplier is
inserted.

---

## 2. Long-side branch: near-tangent physical contacts

For one distinguished outer route let `theta` be the angle between a unit route-edge
occurrence and the corresponding loaded-hull chord direction.  The exact directional
energy identity is

```math
 d_{out}
 =\sum_{i,j}(1-\cos\theta_{i,j}).
\tag{PB.13}
```

Thus for every fixed `beta`, the number of occurrences with `|theta|>=beta` is at most

```math
 {d_{out}\over1-\cos\beta}.
```

In the long-side branch, taking `beta=pi/6` and passing from occurrences to distinct
undirected contacts loses at most a factor two.  Therefore

```math
 \boxed{
 {E_{tan}(\pi/6)\over D}
 \ge{1\over2}\left(
 B_{50}-{\delta_{50}\over1-\sqrt3/2}
 \right)-o(1)
 }
\tag{PB.14}
```

and the right side equals

```math
 \boxed{0.2078202312826877\ldots .}
\tag{PB.15}
```

Every such contact has absolute projection on its local loaded-side direction larger
than `cos(pi/6)=sqrt3/2`, so

```math
 \boxed{
 {1\over D}\sum_{e\in E_{tan}(\pi/6)}
 |\operatorname{proj}_{tan}(e)|
 >0.1799-o(1).
 }
\tag{PB.16}
```

Again this is a weight-free sum over distinct physical contact edges.

---

## 3. Unified physical endpoint

Every `g=0.0050`, `t=t_50`, small-residual Type-II survivor therefore satisfies

```math
 \boxed{
 \begin{array}{ll}
 \text{either}&
 E_{pen}\ge0.1974238942D-o(D)
 \quad\text{(strongly inward contacts)},\\[1mm]
 \text{or}&
 E_{tan}\ge0.2078202312D-o(D)
 \quad\text{(near-tangent outer contacts)}.
 \end{array}
 }
\tag{PB.17}
```

In particular at least

```math
 \boxed{0.1974238942D-o(D)}
```

distinct unit contacts belong to one of two explicit robust directional families.
The tooth side also has the stronger aggregate inward-direction certificate (PB.12),
while the long-side side has the stronger tangent-direction certificate (PB.16).

The matched atomic improvement therefore has a direct source-level consequence; it is
not confined to train-measure constants.

---

## 4. What remains

This theorem still does not close C-II.  The contacts are counted without KKT weights,
and the known near-chain regressions show that a weighted stress summation can hide
large unweighted populations behind tiny coefficients.

The next closing target is now narrow: prove a **weight-free capacity or deformation
theorem** for one of the two robust contact families.  Plausible mechanisms are:

1. charge the inward family to attachment/phase-boundary incidence;
2. charge the near-tangent family to the nearly extremal diameter-thrackle circular
   order; or
3. construct a simultaneous boundary motion for a linear independent subfamily.

Further tuning of the atomic decimal is lower value than one of these source-level
bridges.

## 5. Scope audit

- The theorem inherits the `R_F=o(D)` / low-`t` scope of the current structural
  endpoint.
- `g=0.0050` and the Section-171 `0.0023374` floor are independently audited.
- The tooth/long-side inequality is finite and exact before normalization.
- Apex injectivity uses only convexity, contact separation, and
  `eta<2(1-cos(pi/12))`.
- Direction concentration is the exact identity `d_out=sum(1-cos theta)` plus a
  deterministic tail bound.
- Counts are of distinct actual unit-contact edges.  No positive stress-weight floor
  is asserted.
- Contact-isolated source points remain in the source.
- C-II and Level I remain open.
