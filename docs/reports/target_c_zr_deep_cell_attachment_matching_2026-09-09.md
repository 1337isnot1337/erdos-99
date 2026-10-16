<!-- theorem-state: {"artifact_id":"ART-0924D4F2B17A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHA: a deep harmonic cell has linearly many attachments and short response pairs

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** closing-proof continuation / bridge-tree and response synthesis  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** revised ZHC, C20, C26, C33, C41, C43  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

Revised ZHC localizes the bridge-dominant near-zero phase into one unloaded harmonic component `I_*` with attachment set `A_*`. It contains an actual diameter pair `a,b in A_*` whose global contact bridge-tree route has

\[
L:=\ell(ab)\ge\eta D/2.
\tag{1}
\]

Every physical bridge on that route belongs to the closure of the same cell.

The first version of this report used C33 plus Eppstein to prove `|A_*|>=(L+3)/2`. The bridge-tree structure gives a stronger exact result. C26 says every reaction-free bridge block has degree at least three and every leaf block is loaded. Along the `a--b` route, each internal block therefore either contains a loaded terminal itself or has a disjoint off-route branch leading to one. Because the complete `a--b` path through `I_*` avoids all loaded terminals except its endpoints, the first loaded terminal reached in each such block/branch is a distinct attachment of `I_*`.

Thus

\[
\boxed{|A_*|\ge L+1.}
\]

C43 then makes the uniformly-short graph on `A_*` have independence number at most two, yielding an almost-perfect matching of uniformly-short pairs. C41 makes every such pair a strictly positive component-response pair.

---

## 1. The route inside the cell

Let `T` be the global contact bridge-block tree. Write the bridge-tree route between the blocks containing `a` and `b` as

\[
X_0,X_1,\ldots,X_L,
\tag{1.1}
\]

so the `L` tree edges between consecutive nodes are exactly the physical contact bridges separating `a` from `b`.

Revised ZHC proves all these bridges belong to the component closure

\[
K_*:=I_*\cup A_*
\tag{1.2}
\]

with its component and attachment contact edges. Since `a,b in A_*`, connectedness of `I_*` supplies an `a--b` contact path `P` whose internal vertices all lie in `I_*`.

Every global bridge on the route separates `a` from `b`; hence `P` crosses the route nodes in the order `X_0,...,X_L`.

---

## 2. Every internal route block supplies a new attachment

Fix an internal route node `X_i`, `1<=i<=L-1`.

### Case 1: `X_i` is loaded

Then `X_i` contains at least one terminal of `B`. Because `P` passes through `X_i` but has no internal loaded terminal, it also contains a vertex

\[
x_i\in I_*\cap X_i.
\]

The bridge block `X_i` is connected. Take a contact path inside `X_i` from `x_i` to any loaded terminal of the block, and let `t_i` be the **first** loaded terminal on that path.

Every vertex before `t_i` is nonloaded and is connected to `x_i` without passing through `B`. Hence those vertices lie in the same component `I_*` of `C[V\setminus B]`. The last edge of the prefix is therefore an attachment contact from `I_*` to `t_i`, so

\[
\boxed{t_i\in A_*.}
\tag{2.1}
\]

Moreover `t_i` belongs to the route block `X_i`.

### Case 2: `X_i` is reaction-free

The route already uses two bridge-tree incidences at `X_i`. C26 excludes reaction-free degree-two bridge blocks, so

\[
\deg_T(X_i)\ge3.
\tag{2.2}
\]

Choose an incident bridge leading into an off-route component `U_i` of `T-X_i`.

C20 says both sides of every positive contact bridge contain loaded terminals. Hence `U_i` contains a loaded terminal. Start at a nonloaded vertex of `X_i` lying on `P`, enter `U_i`, and follow any contact path until the first loaded terminal `t_i` is reached.

Before `t_i`, the path contains no loaded vertex, so the entire prefix remains connected to `I_*` in `C[V\setminus B]`. Thus again the last edge is an attachment contact and

\[
\boxed{t_i\in A_*.}
\tag{2.3}
\]

This `t_i` lies in the off-route subtree `U_i`.

### Distinctness

Off-route tree components attached at different route nodes are pairwise disjoint. They are also disjoint from every route block. Distinct route blocks are distinct components after the contact bridges are deleted.

Therefore the terminals `t_i` assigned to different internal route nodes are all distinct. None is `a` or `b`, whose blocks are `X_0` and `X_L`.

We have produced one distinct attachment for every one of the `L-1` internal route nodes, plus the two endpoint attachments `a,b`.

### Theorem ZHA.1 — exact attachment injection

\[
\boxed{|A_*|\ge L+1.}
\tag{ZHA1}
\]

For the revised ZHC route,

\[
\boxed{|A_*|\ge\frac{\eta D}{2}+1.}
\tag{ZHA2}
\]

This is stronger by a factor approaching two than the earlier Eppstein-only estimate.

---

## 3. Independent Eppstein audit

The earlier argument remains a useful independent check.

Let `m=|I_*|` and let `G_*` be the actual induced unit-contact graph on `I_* union A_*`. C33 gives at least

\[
|E_*|\ge2m+1
\tag{3.1}
\]

component contact rows. Every `a--b` path in `G_*` crosses the `L` global bridges, so its graph diameter `delta_*` is at least `L`.

Eppstein gives

\[
|E(G_*)|\le2(m+|A_*|)-\delta_*-2.
\tag{3.2}
\]

Combining with `|E(G_*)|>=|E_*|>=2m+1` recovers

\[
|A_*|\ge\frac{L+3}{2}.
\tag{3.3}
\]

It is weaker than ZHA1 but uses a logically different route and catches bookkeeping errors in the bridge-tree injection.

---

## 4. C43 gives an almost-perfect uniformly-short matching

Let `rho_0<1` be the canonical uniform anti-Reuleaux constant. Define the graph `S_*` on `A_*` by

\[
st\in E(S_*)
\iff
|s-t|\le\rho_0D.
\tag{4.1}
\]

C43 says every triple of source points contains a uniformly-short pair. Thus no three vertices of `A_*` are independent in `S_*`:

\[
\boxed{\alpha(S_*)\le2.}
\tag{4.2}
\]

Take a maximum matching `J_*` in `S_*`. It is maximal, so its unmatched vertices form an independent set. At most two remain unmatched. Therefore

\[
\boxed{|J_*|\ge\frac{|A_*|-2}{2}.}
\tag{ZHA3}
\]

Using ZHA1,

\[
\boxed{|J_*|\ge\frac{L-1}{2}.}
\tag{ZHA4}
\]

For the revised ZHC cell,

\[
\boxed{|J_*|\ge\frac{\eta D}{4}-\frac12.}
\tag{ZHA5}
\]

with integer rounding understood.

Every `st in J_*` lies in the same attachment set `A_*`, so C41 strict component response gives

\[
\boxed{c_{st}^{(*)}>0,}
\tag{ZHA6}
\]

and by construction

\[
\boxed{|s-t|\le\rho_0D.}
\tag{ZHA7}
\]

The matching is terminal-disjoint.

---

## 5. Response-defect consequence

C41's normalized defect identity is

\[
\varepsilon
=
\sum_{u<v}c_{uv}
\left(1-\frac{|u-v|^2}{D^2}\right).
\tag{5.1}
\]

Put

\[
\gamma_0=1-\rho_0^2>0.
\tag{5.2}
\]

For `st in J_*`, total response satisfies `c_st>=c_st^(*)` and the squared-distance deficit is at least `gamma_0`. Hence

\[
\boxed{
\varepsilon
\ge
\gamma_0\sum_{st\in J_*}c_{st}^{(*)}.
}
\tag{ZHA8}
\]

In the near-zero phase `D epsilon->0`,

\[
\boxed{
\sum_{st\in J_*}c_{st}^{(*)}=o(1/D).
}
\tag{ZHA9}
\]

Since `|J_*|=Omega_eta(D)`, the average component response on this terminal-disjoint uniformly-short matching is

\[
\boxed{o(1/D^2).}
\tag{ZHA10}
\]

Thus the same mechanically macroscopic cell simultaneously carries fixed exact-diameter response and an almost-perfect linear matching of uniformly-short channels whose conductances collapse quadratically on average.

---

## 6. Heavy-chain specialization

For the ZHH macroscopic chain,

\[
L\ge\frac{\eta^2}{16\pi}D.
\tag{6.1}
\]

ZHA1 and ZHA4 improve the corresponding attachment and short-matching bounds to

\[
\boxed{|A_*|\ge\frac{\eta^2}{16\pi}D+1,}
\tag{ZHA11}
\]

and

\[
\boxed{|J_*|\ge\frac{\eta^2}{32\pi}D-rac12.}
\tag{ZHA12}
\]

The ZHH cell therefore contains a linear attachment population and a linear uniformly-short matching at twice the coefficient supplied by the first Eppstein-only version.

---

## 7. Exact target implication

Under bridge dominance and `D epsilon->0`, one captured harmonic cell now has:

- `Omega_eta(D^2)` contact stress;
- an actual diameter transport route containing `Omega_eta(D)` global contact bridges;
- `Omega_eta(D)` distinct loaded attachments forced by the route itself;
- an almost-perfect `Omega_eta(D)` uniformly-short positive component-response matching;
- total conductance on that matching `o(1/D)` and average conductance `o(1/D^2)`.

For the ZHH cell, the same route bridges are individually macroscopic, `alpha_e=Omega_eta(D)`, and carry `Omega_eta(D^2)` stress in aggregate.

The remaining within-cell regression is now sharper:

> A triangle-free unit-contact cell with quadratic mechanical stress and a linearly deep, possibly macroscopic articulation route has a linearly large loaded boundary, yet almost every uniformly-short boundary pairing can become electrically negligible while fixed exact-diameter response survives through the same cell.

A closing theorem must rule out that anisotropic cell using unit geometry/global minimum information, or derive the exact face inequality, a strict sub-`D` competitor, or `epsilon=Omega(1/D)`.

---

## 8. Regressions and limits

- Abstract star-like resistor networks with many tiny side branches still model the response degeneration qualitatively.
- ZHA does not infer a conductance floor from support cardinality.
- The bridge-tree injection uses C26's no-reaction-free-degree-two theorem; it does not assume attachment sets are intervals.
- The Eppstein argument remains as an independent weaker audit.
- Contact-isolated source points remain untouched.

---

## 9. Dependencies

- revised ZHC / ZHH;
- C20 bridge-side loadedness;
- C26 loaded-leaf and reaction-free-degree-at-least-three bridge-block structure;
- C33 pinned component row surplus for the independent audit;
- C41 strict component response and defect identity;
- C43 uniform anti-Reuleaux gap;
- Eppstein only for the independent audit.

No new external literature is imported.

---

## 10. Promotion recommendation

**Hold as report.** It is downstream of report-level ZR/ZF and stacked PR #108/#111.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZHA exact attachment injection:
Let X_0,...,X_L be the bridge-block route of a response-visible diameter pair a,b whose
entire bridge route lies in one harmonic cell I_*. For each internal route block X_i:
- if loaded, the first loaded vertex reached inside the block from the I_* path is an
  attachment of I_*;
- if reaction-free, C26 gives an off-route branch, and the first loaded vertex reached
  in that branch is an attachment of I_*.
The assigned branches/blocks are disjoint. With endpoints a,b,
    |A_*| >= L+1.
For ZHC, L>=eta D/2, hence |A_*|>=eta D/2+1.

C43 makes the uniformly-short graph on A_* have independence number <=2. A maximum
matching leaves at most two vertices unmatched:
    |J_*| >= (L-1)/2 >= eta D/4-1/2.
Every matching pair has c_st^(*)>0 and |s-t|<=rho_0D.
The defect identity gives
    epsilon >= gamma_0 sum_{J_*} c_st^(*).
Thus D epsilon->0 forces total matching conductance o(1/D), average o(1/D^2), inside
the same mechanically macroscopic cell.

For the ZHH heavy chain, |A_*|>=eta^2 D/(16pi)+1 and
|J_*|>=eta^2 D/(32pi)-1/2.
```
