> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_heavy_bridge_chain_2026-09-09.md) · source SHA-256 `5e3665298f59a866e98025e5e446cf17db8a11c5a658b3af50872bb5548219cc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F724A8F6378B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — bridge-dominant stress forces a long heavy chain

**Date:** 2026-09-09  
**Repository state:** branch `sol/2026-09-09-zr-kernel-consequences`, after ZBL and reconciled against main `a8efd00fa7fca0c4a20911e86efd46cb0aadeb9c`  
**Run type:** closing-proof continuation / laminar bridge reduction  
**Target:** Target C, Gate C-II bridge-dominant near-zero phase  
**External web search:** no theorem imported  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The preceding ZBL report proves that bridge-dominant contact stress contains linearly many macroscopic bridges, and in the C66 near-zero phase their supporting lines are all macroscopically localized at the stress-star center while almost all make near-unit radial progress.

This note uses the older C20 antichain stress budget to show that those heavy bridges cannot be distributed across a wide bridge tree. They contain a **single nested chain of linear length**. Once the C66 non-star `beta` mass is smaller than the heavy cut mass, every heavy bridge is crossed by an actual diameter edge incident to the stress-star center. A star edge crossing the deepest bridge of the chain crosses every bridge above it.

Thus one actual diameter pair has a contact bridge-tree route containing `Omega_eta(D)` macroscopic, asymptotically radial bridge edges.

This is a substantially narrower geometric endpoint than either C27's one macroscopic bridge or ZBL's unstructured linear family. It still does not prove that the intervening 2-edge-connected blocks form a narrow contact path, so Theorem P/C98 cannot yet be applied as an exact chain theorem.

## 1. Inputs

Assume

```math
S_{\rm br}:=\sum_{e\text{ contact bridge}}\alpha_e
\ge\eta D^2
\tag{1.1}
```

for fixed `eta in (0,1]`.

Following ZBL, put

```math
c_\eta:=\frac{\eta}{4\pi}
\tag{1.2}
```

and call a contact bridge **eta-heavy** if

```math
\alpha_e\ge c_\eta D.
\tag{1.3}
```

ZBL proves that the number `N_eta` of eta-heavy bridges satisfies

```math
N_\eta\ge\frac\eta2 D.
\tag{1.4}
```

C20 proves the antichain bridge-stress budget: if oriented bridge-side components are pairwise disjoint, then

```math
\sum\alpha_e\le2D.
\tag{1.5}
```

In a rooted bridge tree, descendant sides of pairwise incomparable edges are pairwise disjoint, so (1.5) applies to every edge antichain.

In the C66 near-zero phase let `z` be the stress-star center and

```math
\tau_z:=\sum_{h\not\ni z}\beta_h.
\tag{1.6}
```

C66 gives

```math
\tau_z\le C_0D\varepsilon.
\tag{1.7}
```

Finally every eta-heavy bridge satisfies, by C20/ZBR,

```math
w_e\ge\frac{\alpha_e}{D}\ge c_\eta,
\tag{1.8}
```

where `w_e` is the total active diameter weight crossing the bridge cut.

## 2. Strongest genuinely new audited theorem

### Theorem ZBC — linear heavy bridge chain

Under (1.1):

1. **Bounded heavy-antichain width.** Every antichain of eta-heavy bridge edges has cardinality at most
   ```math
   \boxed{
   W_\eta:=\left\lfloor\frac{2}{c_\eta}\right\rfloor
   =\left\lfloor\frac{8\pi}{\eta}\right\rfloor.
   }
   \tag{ZBC1}
   
   ```

2. **Linear nested chain.** The eta-heavy bridge edges contain a single chain in the bridge-tree ancestor order of length `L_eta` satisfying
   ```math
   \boxed{
   L_\eta
   \ge
   \frac{N_\eta}{W_\eta}
   \ge
   \frac{\eta^2}{16\pi}D.
   }
   \tag{ZBC2}
   
   ```
   The last displayed lower bound is understood as a real lower bound; the integer chain length is at least its ceiling when necessary.

Now also assume the C66 near-zero phase and `D epsilon -> 0`. Root the bridge tree at the contact block containing `z`. Then for all sufficiently large `D`:

3. **Every eta-heavy cut is crossed by the stress star.** Every eta-heavy bridge is crossed by at least one active diameter edge incident to `z`.

4. **One diameter edge crosses the entire heavy chain.** If
   ```math
   e_1<e_2<\cdots<e_{L_\eta}
   \tag{2.1}
   
   ```
   is a deepest-oriented eta-heavy chain, there exists an actual diameter edge `zk in H` such that the bridge-tree path from the block of `z` to the block of `k` contains all `e_1,...,e_{L_eta}`.

5. **Near-zero geometric refinement.** Combining with ZBL, the chain can be chosen so that every chain bridge has
   ```math
   \operatorname{dist}(z,\ell_{e_j})=o(D),
   \tag{2.2}
   
   ```
   and for every fixed `xi>0`, all but `o(D)` of its bridges satisfy
   ```math
   \bigl||u_j-z|-|v_j-z|\bigr|>1-\xi.
   \tag{2.3}
   
   ```

Thus one actual diameter pair has a contact bridge-tree route containing a linear number of `Theta_eta(D)`-stress, macroscopically radial bridge edges.

### Proof of ZBC1

Root the contact bridge-block tree at an arbitrary block. Let `A` be an antichain of eta-heavy bridge edges. Choose for each edge its descendant-side contact component. Incomparable tree edges have disjoint descendant components, so C20's antichain budget gives

```math
\sum_{e\in A}\alpha_e\le2D.
\tag{2.4}
```

Each edge in `A` is eta-heavy, hence contributes at least `c_eta D`. Therefore

```math
|A|c_\eta D\le2D,
```

so

```math
|A|\le\frac2{c_\eta}.
```

Integrality gives ZBC1. QED.

### Proof of ZBC2

For every eta-heavy edge `e`, define its **heavy rank** `r(e)` to be the number of eta-heavy edges on the root-to-`e` tree path, including `e` itself.

Two eta-heavy edges with the same heavy rank are incomparable. Indeed, if `e<f`, the root-to-`f` path contains all heavy edges on the root-to-`e` path plus `f`, so `r(f)>r(e)`.

Thus each heavy-rank level is an antichain and contains at most `W_eta` edges by ZBC1. If the largest heavy rank is `L_eta`, then

```math
N_\eta\le W_\eta L_\eta.
\tag{2.5}
```

Hence

```math
L_\eta\ge\frac{N_\eta}{W_\eta}.
\tag{2.6}
```

Using `N_eta>=eta D/2` from ZBL and

```math
W_\eta\le\frac{8\pi}{\eta}
```

gives

```math
L_\eta
\ge
\frac{\eta D}{2}\frac{\eta}{8\pi}
=
\frac{\eta^2}{16\pi}D.
```

This proves ZBC2 without importing Dilworth or any external poset theorem. QED.

### Proof that every heavy cut is crossed by the stress star

Root now at the bridge block containing the C66 star center `z`. Since `D epsilon->0`, equation (1.7) gives

```math
\tau_z=o(1).
\tag{2.7}
```

For all sufficiently large `D`,

```math
\tau_z<c_\eta.
\tag{2.8}
```

Let `e` be eta-heavy. Its crossing diameter mass satisfies `w_e>=c_eta` by (1.8). If no crossing active diameter edge were incident to `z`, then all crossing diameter mass would belong to the global non-star tail, giving

```math
w_e\le\tau_z<c_\eta,
```

contradiction. Therefore some active star edge `zk` crosses `e`.

Because the tree is rooted at the block containing `z`, the descendant side of `e` is the side not containing `z`; the partner `k` of every crossing star edge lies in that descendant side. QED.

### Proof that one diameter edge crosses the entire chain

Take a heavy chain

```math
e_1<e_2<\cdots<e_L
```

ordered from the root outward. The descendant components satisfy

```math
S_{e_L}\subset S_{e_{L-1}}\subset\cdots\subset S_{e_1}.
\tag{2.9}
```

By the preceding result, the deepest bridge `e_L` is crossed by some star edge `zk`. Thus `z` lies outside `S_{e_L}` and `k` lies inside it.

Since `S_{e_L}` is contained in every ancestor descendant component `S_{e_j}`, the same partner `k` lies inside every `S_{e_j}`, while `z` lies on the root side of every `e_j`. Therefore the unique bridge-tree path from the block of `z` to the block of `k` crosses every edge `e_1,...,e_L`. QED.

### Proof of the near-zero geometric refinement

ZBL3 applies to every eta-heavy bridge and gives

```math
\frac{\operatorname{dist}(z,\ell_e)}D
\le
\frac{4\pi C_0}{\eta}D\varepsilon=o(1).
\tag{2.10}
```

Hence every bridge in the heavy chain satisfies (2.2).

For fixed `xi>0`, ZBL4 says the total number of eta-heavy bridges in the entire source violating (2.3) is `o(D)`. The chosen heavy chain is a subset of the heavy bridges, so it also contains at most `o(D)` such bad edges. Since its length is `Omega_eta(D)` by ZBC2, all but `o(D)` chain bridges satisfy (2.3). QED.

## 3. Exact Target C implication

Assume bridge dominance and near-zero response defect:

```math
S_{\rm br}\ge\eta D^2,
\qquad
D\varepsilon\to0.
\tag{3.1}
```

Then there is an actual diameter pair `z,k` with `|z-k|=D` such that **every** contact path from the block of `z` to the block of `k` must cross a nested sequence of at least

```math
\frac{\eta^2}{16\pi}D
\tag{3.2}
```

eta-heavy contact bridges. Every one of those bridges has

```math
\alpha_e\ge\frac{\eta}{4\pi}D,
\tag{3.3}
```

its supporting line passes `o(D)` from `z`, and all but `o(D)` have near-unit radial progress from `z`.

This converts the bridge-dominant near-zero phase into a **single deep diameter route** rather than a collection of unrelated macroscopic cuts.

The route is not yet a contact chain: between successive bridge edges lie 2-edge-connected contact blocks that may have nontrivial internal diameter and two-dimensional geometry. C29/C39 bound their total complexity but do not make each block small. It is therefore invalid to apply Theorem P directly to the sequence of bridge edges.

## 4. Interaction with loaded-block accounting

The C29 proof already shows that root-to-loaded bridge depth consumes distinct loaded blocks. ZBC identifies one root-to-diameter-partner route with linear heavy depth. Thus the route passes through `Omega_eta(D)` distinct bridge blocks, and C26 excludes reaction-free degree-two transport.

Consequently, a linear number of positions along the route must be paid for by either

- a loaded block; or
- an off-route subtree terminating in a loaded block.

This is the exact place where the low-weight transverse geometry must enter. In the C66 phase the non-star `beta` mass is `o(1)`, but the deep route still requires linearly many loaded/branching events.

No theorem currently turns those linearly many events into an `Omega(D^2)` C68 radial defect or an `Omega(1/D)` response defect. Local stress weights can become arbitrarily small.

## 5. Exact remaining lemma

The global face endpoint remains

```math
\boxed{
 b+\sum_F(\deg F-4)>2h.
}
\tag{5.1}
```

For the bridge-dominant near-zero branch, ZBC sharpens the geometric substitute to:

> **BC — deep radial diameter-route exclusion.** For every fixed `eta>0`, no sufficiently large lexicographically normalized triangle-free global minimizer can have an actual diameter pair `z,k` whose bridge-tree route contains `Omega_eta(D)` contact bridges satisfying
> 

```math
> \alpha_e=\Omega_\eta(D),
> \qquad
> \operatorname{dist}(z,\ell_e)=o(D),
> \qquad
> \bigl||u-z|-|v-z|\bigr|=1-o(1)
> 
```
> for all but `o(D)` of them, while the intervening loaded/transverse structure carries only `o(1)` total non-star diameter weight.
>
> It is enough to derive an `Omega(1/D)` response defect, a strict sub-`D` competitor, or the face inequality (5.1).

A proof must control the 2-edge-connected blocks between bridges; merely concatenating the bridge edges into a geometric path is not justified.

## 6. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| Heavy antichain width is `O_eta(1)` | proved | C20 antichain stress budget plus `alpha_e>=c_eta D`. |
| Linear heavy chain | proved | Heavy-rank levels are antichains; ZBL supplies `Omega_eta(D)` heavy edges. |
| Every heavy cut is crossed by a z-star edge in near-zero phase | proved | `w_e>=c_eta` but total non-star beta is `o(1)`. |
| One actual diameter edge crosses the whole heavy chain | proved | Nested descendant components; choose a star edge crossing the deepest cut. |
| Heavy chain is macroscopically localized/radial | proved under `D epsilon->0` | ZBL3/ZBL4. |
| Intervening blocks form a narrow contact chain | not proved | Blocks may be two-dimensional and have nontrivial internal diameter. |
| Deep radial route is impossible | still open | This is BC. |

## 7. Regression tests and failed implications

### Path of loaded blocks

C29 explicitly allows a bridge-tree path consisting entirely of loaded blocks. ZBC strengthens the stress and geometry of many bridge edges on such a path but does not remove the loaded-block regression.

### Large 2-edge-connected blocks between radial bridges

A root-to-leaf bridge route may pass through blocks that move angularly or radially by a large amount before the next bridge. Therefore near-unit radial progress on the bridge edges does not telescope to the diameter `D` without an additional block-diameter estimate on the same route.

### Tiny transverse KKT weights

Each loaded or branching event may be structurally necessary while carrying arbitrarily small positive `beta` or contact stress. The linear number of events does not by itself give a linear or quadratic weighted defect.

### Direct use of Theorem P

Invalid. Theorem P applies to an actual contact path with a uniform angular/narrowness hypothesis. ZBC produces a sequence of bridge edges separated by blocks; it does not prove that the contact subpaths inside those blocks remain in the same narrow tube.

## 8. Literature imported

No new literature theorem is imported. The chain theorem is an internal consequence of C20, ZBL, C66, and elementary rooted-tree ordering.

## 9. Computation and reproducibility

No computation is used.

## 10. Canonical promotion recommendation

**Hold as report.**

ZBC depends on report-level ZR/ZF/ZK/ZBR/ZBL. If those dependencies are promoted, update the bridge frontier so the bridge-dominant near-zero endpoint reads:

```text
S_bridge >= eta D^2
+ D epsilon -> 0
  -> Omega_eta(D) eta-heavy bridges
  -> heavy antichain width O_eta(1)
  -> one root-to-leaf heavy chain of length Omega_eta(D)
  -> one actual z-diameter edge crosses the whole chain
  -> all chain bridge lines pass o(D) from z
  -> all but o(D) chain bridges make near-unit radial progress.
```

Do not promote BC; it is the open route theorem.

## 11. Next run

The next attack should be route-local rather than global:

1. take the `z-k` diameter route supplied by ZBC;
2. use C39's summed internal block-diameter budget to show that either many intervening blocks are small or a bounded number consume a macroscopic fraction of the route complexity;
3. in the many-small-block case, try to concatenate the near-radial bridge edges into a C98/Theorem-P-type narrow path;
4. in the macroscopic-block case, use the existing harmonic-cell / two-edge-connected response machinery inside that block.

This gives an exact dichotomy that matches the existing bridge-vs-block C-II architecture without assuming a uniform KKT weight floor.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem ZBC:
If S_bridge >= eta D^2, eta-heavy bridges (alpha >= eta D/(4pi)) have antichain
width at most floor(8pi/eta). ZBL gives at least eta D/2 heavy bridges, so one
nested bridge-tree chain has length at least eta^2 D/(16pi).

In the C66 phase D epsilon->0, total non-z-star beta=o(1), whereas every heavy cut
has w_e>=eta/(4pi). Hence every heavy cut is crossed by a z-star diameter edge.
Choose a star edge crossing the deepest heavy cut; nestedness makes that same actual
diameter edge cross the entire heavy chain.

By ZBL, all chain bridge lines pass o(D) from z, and for every fixed xi>0 all but
o(D) chain bridges have radial progress >1-xi.

Remaining bridge lemma BC:
control the 2-edge-connected blocks between these bridges strongly enough to turn
the deep radial diameter route into a contradiction / response gap / face inequality.
```
