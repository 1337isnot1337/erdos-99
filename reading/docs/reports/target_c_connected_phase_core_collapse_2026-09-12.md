> Generated reading edition · [exact source](../../../docs/reports/target_c_connected_phase_core_collapse_2026-09-12.md) · source SHA-256 `7c834829fa09a0ed7661aee270f0bbb2125d3690159f84e565eb722d489477b8`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7736068EFFC4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — connected phase-core collapse

**Date:** 2026-09-12  
**Repository commit:** `87fcd1c` at the start of this subrun  
**State version:** `2026-09-12.audit.44`  
**Run type:** closing proof  
**Target:** C-II  
**Dependencies:** canonical Section 90, proof-only Section 118, and proof-only Theorem PC in
[`target_c_phase_component_endpoint_closure_2026-09-12.md`](target_c_phase_component_endpoint_closure_2026-09-12.md)

## STATUS

`PROVED CANDIDATE AWAITING PROMOTION`

This note proves a graph-to-phase-collapse lemma and composes it with Theorem PC.
It does not promote theorem state and does not claim C-II closure. The missing premise
is now a quantitative connected-core extraction with enough rhombus mass, not merely
the existence of a dense inverse-phase graph.

## 1. The graph lemma

Let (G_D=(V_D,E_D)) be a train graph with

```math
 |V_D|\le (C+o(1))D.
```

Suppose a connected component (K_D) has minimum degree at least

```math
 \delta_D\ge(\eta-o(1))D,
 \qquad \eta>0,
```

and every edge (uv) is (K_0/D)-good for a common lifted reduced-phase coordinate
(s):

```math
 |s(u)-s(v)|\le K_0/D.
\tag{CP.1}
```

The coordinate is allowed to include the fixed label offsets used to compare the
finite train direction families. The hypothesis is deliberately stated with a
common lift; an unproved identification of unrelated projective phases is not
being smuggled into the lemma.

### Lemma CP — connected near-phase components collapse

The phase diameter of (K_D) satisfies

```math
 \operatorname{diam}_s(K_D)
 \le
 \frac{K_0}{D}\left(\frac{3C}{\eta}+2+o(1)\right).
\tag{CP.2}
```

In particular, every such component lies in one reduced-phase window whose width is
(O(D^{-1})), hence in a window of width tending to zero.

### Proof

Take a shortest graph path

```math
 v_0,v_1,\ldots,v_m
```

inside (K_D). The closed neighborhoods of (v_0,v_3,v_6,\ldots) are pairwise
disjoint: if two of them shared a vertex, the corresponding path vertices would be
at graph distance at most two, contradicting shortestness at separation at least
three. Therefore

```math
 \left(\left\lfloor\frac m3\right\rfloor+1\right)
 \bigl((\eta-o(1))D+1\bigr)
 \le |K_D|\le(C+o(1))D.
```

Thus (m\le 3C/\eta+2+o(1)). Summing (CP.1) along the path gives

```math
 |s(v_0)-s(v_m)|
 \le mK_0/D,
```

which is (CP.2). Since the endpoints were arbitrary, the whole component has the
claimed phase diameter. $`\square`$

The only graph fact used here is the disjointness of neighborhoods at distance at
least three. In particular, this is not the rejected incident-diameter Euler-path
inference, and it does not require the train graph to be a path.

## 2. Composition with the endpoint contradiction

Let (R_D^{\mathrm{core}}) be the number of strict-rhombus crossings whose train
segments lie in one connected component satisfying Lemma CP, and suppose

```math
 \frac{R_D^{\mathrm{core}}}{D^2}\ge r_{\mathrm{core}}-o(1).
```

Mantel's inequality on the same simple triangle-free crossing graph gives

```math
 T_D^{\mathrm{core}}
 \ge 2\sqrt{R_D^{\mathrm{core}}}.
\tag{CP.3}
```

Every one of these complete train segments has two physical endpoint occurrences.
Lemma CP places the component in one narrow window per direction label. If at most
(q) labels occur, Theorem PC's endpoint accounting therefore gives

```math
 4\sqrt{r_{\mathrm{core}}}
 \le
 U(\sigma)+2qB_*(\sigma),
 \qquad
 U(\sigma):=M(\theta)+\frac{16}{3}\sigma.
\tag{CP.4}
```

The use of (CP.4) is legitimate for a subcomponent: its principal-route endpoints
are charged to the same three physical routes, while each off-route endpoint is
charged to the Section-118 capacity of the window containing its train. No endpoint
is charged twice because the component and its label windows are assigned before the
count. The argument retains all source points; it only counts a selected set of
complete carrier trains.

Consequently a connected phase core is impossible whenever

```math
 r_{\mathrm{core}}
 > \left(\frac{U(\sigma)+2qB_*(\sigma)}4\right)^2.
\tag{CP.5}
```

At the safe Section-118 endpoint used in Theorem PC,

```math
 U=1.8692857318002269\ldots,
 \qquad B_*=0.1162704799276074\ldots.
```

The resulting forbidden core-mass thresholds are

```math
\begin{array}{c|c}
 q & \left((U+2qB_*)/4\right)^2\\
 \hline
 1 & 0.2761047151097038\ldots\\
 2 & 0.3405795207762111\ldots\\
 3 & 0.4118137386940167\ldots
\end{array}
\tag{CP.6}
```

Thus, for example, a connected two-label (K_0/D)-good core carrying more than
(0.34058D^2+o(D^2)) strict-rhombus crossings is already incompatible with the
safe endpoint. A connected three-label core carrying more than
(0.41182D^2+o(D^2)) crossings is also impossible. The full carrier lower bound
(R_D/D^2\ge0.4703752868\ldots-o(1)) would trigger the latter conclusion if the
entire carrier could be placed in one such connected phase core.

## 3. What this closes and what it does not

This result eliminates the following explicit subbranch:

```text
safe Section-118 full-core carrier
+ a connected common-lift K/D-good train component
+ minimum degree eta D
+ more than the CP.5 rhombus mass in that component
-> endpoint contradiction.
```

It also turns the vague multi-grain issue into a falsifiable extraction target:

```math
\boxed{
 \text{extract one connected near-phase component with enough crossing mass,}
 }
```

or prove a multi-component version whose total endpoint capacity is below the
principal-route budget.

The canonical/proof-only stack does not supply that extraction. Section 90 produces a
large inverse-phase graph after pruning, but its certified minimum-degree and retained
crossing constants are not currently known to exceed the thresholds in (CP.6).
The graph may also split into many components, and the existing (O(D)) interface
ledger does not bound their number by three. Hence CP is a genuine structural
reduction, not a C-II closure.

The inactive-container branch is untouched. In particular, no contact-isolated source
point has been removed, no affine-kernel statement has been extended to those points,
and no first-contact motion has been promoted to a finite source-preserving competitor.

## 4. Hostile audit

* The neighborhood packing proves a graph-distance bound, not a geometric crossing
  order. It cannot be used to infer an Euler trail or path.
* The common lifted phase coordinate is an explicit hypothesis. Pairwise near-phase
  edges with incompatible label offsets do not automatically provide it.
* A high average degree is not enough: the minimum-degree hypothesis must follow from
  a certified pruning theorem, and pruning may lose too much (R_D).
* (CP.4) uses Theorem PC as a proof-only dependency. It inherits its directional
  leakage and route-capacity hypotheses and therefore cannot be promoted from this
  note alone.
* The argument is carrier-local. It does not turn the full-source ZR/ZF core theorem
  into a statement about contact-isolated points and does not establish global
  diameter optimality of a replacement.

The companion certificate checks only the finite graph-distance estimate and the three
endpoint thresholds. It is not a substitute for the missing connected-core
extraction.
