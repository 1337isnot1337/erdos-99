> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_p1_endpoint_regular_cell_2026-09-09.md) · source SHA-256 `a724c1c9565b07da14902f566a2e7697ba6acb5b6778be2fe973ffe0aa5ce999`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E53BA7A83275","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — corrected P1 endpoint regular-cell theorem

**Date:** 2026-09-09  
**Repository branch:** PR #118 after CC/MG/PR  
**Run type:** exact difference-body incidence / singleton-block correction  
**Target:** cyclic primitive phase `d_H=1`, P1  
**Depends on:** P1 all-circular difference body, PR twin antipodal completions, CC moving-corner localization, MG moving-corner gap  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

> **Correction.** The first version of this report implicitly assumed that the two color blocks incident to the endpoints of a KKT-zero chord were non-singletons. If, for example, `B_0={b}`, the second shell neighbor of the `B_0` corner is across the fixed transition `ab`, not inside `B_0`. Therefore one cannot always assert that the two support events at the zeroed chord are specifically the two moving transitions `f,h`. That overclaim is withdrawn below.

The valid statement is slightly more invariant and remains strong: both support events at the endpoint-zero diameter must occur across **some** two cut-transition sides, one at each endpoint. Those two unit transition sides and the zeroed diameter form an exact diameter-lens equality cell. For an endpoint-zero edge lying away from the ends of the common path `J`, the two transition sides are indeed the moving sides `f,h`, recovering the original displayed cell.

### Theorem RC — corrected endpoint regular cell

Let `e=sp` be a P1 KKT-endpoint zeroed diameter edge. Let `H-e=A\sqcup B` be its two full-tree components, with `s in A` and `p in B`. Then:

1. the oriented diameter vector `s-p` is a strict circular vertex of `K=F-F`;
2. its two incident ordinary unit Minkowski edges change opposite endpoints of `sp` because `e` lies on the common odd-cycle core of both P1 antipodal refinements;
3. if the `p`-event changes `p` to its shell neighbor `p'`, then `p' in A`; if the `s`-event changes `s` to its shell neighbor `s'`, then `s' in B`;
4. consequently the shell sides `pp'` and `ss'` are two of the four contact-cycle transitions of the cut, and
   $$
   |p's|=|ps'|=D;
   \tag{RC.1}
   $$
5. the two neighboring diameter directions are exactly one minimum gap
   $$
   \delta=2\arcsin\frac1{2D}
   $$
   on either side of `e` in projective direction order;
6. the four points `p,p',s',s` form, after choosing the common side of the diameter line, the exact isosceles diameter-lens cell
   $$
   |pp'|=|ss'|=1,
   \qquad
   |sp|=|p's|=|ps'|=D,
   $$
   and
   $$
   |p's'|=D-\frac1D,
   \qquad
   p's'\parallel sp.
   \tag{RC.2}
   $$

If the relevant `B`-block at `p` and `A`-block at `s` are non-singletons, the only transition choices are the moving sides `f=pq` and `h=rs`; then `p'=q`, `s'=r`, and the original formulas

$$
|qs|=|pr|=D,
\qquad
|qr|=D-\frac1D,
\qquad
qr\parallel sp
\tag{RC.3}
$$

are valid. At an end edge of the common path `J`, one of the selected transition sides may instead be a fixed rectangle side `ab` or `cd`.

---

## 1. `e` is a strict circular difference-body vertex

P1 has one pair of parallel primal hull sides, namely the rectangle sides `ab,cd`. The resulting merged length-two edges of `K=F-F` have endpoints at the rectangle diameter directions `ac,bd` and their antipodes.

AE proves that neither `ac` nor `bd` can be KKT-zero. Hence the difference-body vertex corresponding to `e=sp` is not an endpoint of the merged edge. Both incident K-edges are ordinary unit Minkowski edges.

P1 has no off-circle K-vertices. Therefore the two neighboring K-vertices are also radius-`D` vertices and represent actual full-H diameter pairs.

---

## 2. Common-cycle status forces opposite endpoint events

PR gives two refined maximal antipodal thrackles `H+ad` and `H+bc`. Every KKT-face edge lies on the common path `J`, hence on the unique odd cycle of both refinements.

For a strict antipodal state, the two incident support events change opposite endpoints exactly when the corresponding antipodal chord lies on the odd cycle; if both events changed the same endpoint, the other endpoint would be a leaf and the chord would be pendant.

Thus one K-edge incident to `s-p` changes `p`, and the other changes `s`.

---

## 3. Each support event must cross the component boundary

Suppose the `p`-event changes `p` to a shell neighbor `p'` that remains in component `B`. The neighboring K-vertex represents the pair `p's`. It is circular by Section 1, hence

$$
|p's|=D.
$$

Then `p's` is a second full-H diameter edge crossing the `A|B` cut of `H-e`, impossible because a tree edge `e` is the unique original edge joining the two components of `H-e`.

Therefore

$$
p'\in A.
$$

So `pp'` is a transition side of the component coloring. The same argument at `s` gives

$$
s'\in B,
$$

and `ss'` is another transition side. The neighboring circular K-vertices yield RC.1.

This is the precise replacement for the invalid same-block-neighbor argument in the first version. It remains valid when a color block is a singleton.

---

## 4. Exact metric cell

Normalize

$$
p=(0,0),
\qquad
s=(D,0).
$$

Because `pp'=1` and `p's=D`, subtracting the two squared-distance equations gives

$$
p'_x=\frac1{2D}.
$$

Hence

$$
p'=\left(\frac1{2D},\ \sigma\sqrt{1-\frac1{4D^2}}\right)
$$
for some sign `sigma`.

Likewise `ss'=1` and `ps'=D` give

$$
s'=\left(D-\frac1{2D},\ \sigma'\sqrt{1-\frac1{4D^2}}\right).
$$

The two neighboring projective diameter directions lie on opposite sides of the direction of `sp`. With a common half-plane orientation, this forces `sigma=sigma'`. Therefore `p',s'` lie on the same side of the diameter line and

$$
|p's'|=D-\frac1D,
\qquad
p's'\parallel sp.
$$

This proves RC.2.

The angle between `sp` and either neighboring diameter is determined by

$$
\cos\delta=1-\frac1{2D^2},
$$
so it is exactly

$$
\delta=2\arcsin\frac1{2D}.
$$

---

## 5. When the original moving-side formulas are valid

In the CC notation for `e=sp`, the endpoint `p` is the `B_0` corner adjacent to `A_1`, across the moving transition `f=pq`. If `B_0` contains another vertex, the other shell neighbor of `p` remains in `B_0`, so Section 3 excludes that event and forces `p'=q`.

If `B_0` is a singleton, then `p=b` and both shell sides incident to `p` are cut transitions: the moving side `f` and the fixed rectangle side `ab`. Section 3 alone does not choose between them.

The same statement holds at `s`: if its incident `A_0` block is non-singleton then `s'=r` across `h=rs`; if the block is a singleton, a fixed rectangle transition may be selected instead.

Therefore RC.3 is valid for interior common-path edges, but it is not asserted for a path-end edge with a singleton adjacent color block.

---

## 6. Regression audit

- **Singleton blocks:** explicitly allowed and are the reason for this correction.
- **P1 all-circularity:** still guarantees that both neighboring strict K-states are actual diameter pairs.
- **Additional endpoint beta zeros:** irrelevant; the argument uses the full tree `H`.
- **Projective adjacency:** only the two K-neighbor diameter directions are claimed to be one `delta` from `e`; no graph-path adjacency is inferred beyond the shared endpoint forced by the support event.

---

## 7. Next theorem

The corrected invariant form suggests a stronger path theorem. First identify the exact endpoints of the PR common path `J` from the unique leaf endpoints of the rectangle diagonals `ac,bd`. Then apply Sections 1-4 to **every** edge of `J`, not only KKT-zero edges. Interior edges have the original moving-side cell; the two path-end edges are the only places where a fixed rectangle transition can participate.

That would turn P1 into a chain of exact diameter-lens cells with all exceptional behavior confined to two path ends.

---

## 8. Compact handoff

```text
CORRECTION: the first RC version assumed the relevant color blocks were non-singletons.
For a singleton block, an endpoint of e has two transition-side neighbors, so the K-event
need not be specifically the moving side f or h.

Valid theorem for any KKT-zero e=sp:
- e is a strict circular K-vertex away from the P1 merged edge;
- common-cycle status makes its two K-events change opposite endpoints;
- each event must cross the H-e component cut, else the neighboring circular K-state
  would create a second diameter crossing that tree cut;
- hence the two event sides are two cut-transition unit sides pp',ss';
- neighboring states give |p's|=|ps'|=D;
- exact lens geometry then gives |p's'|=D-1/D and p's' parallel sp;
- their projective directions are exactly delta on either side of e.

If the adjacent color blocks are non-singletons, pp'=f and ss'=h, recovering the old
moving-side formulas. Only common-path end edges can use a fixed rectangle transition.
```
