<!-- theorem-state: {"artifact_id":"ART-B6D087CA84A7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHN: almost every macroscopic trunk block is a bounded near-neutral high-stress corridor

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** closing-proof continuation / route-block localization  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** ZHT, C23, C39, C35 degree bounds  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZHT produces, under bridge dominance and `D epsilon->0`, one harmonic cell whose bridge-block tree contains a consecutive trunk of

\[
H\ge c_H D,
\qquad
c_H:=\frac{\eta^2}{16\pi},
\tag{1}
\]

physical bridges, every one satisfying

\[
\alpha_e\ge c_BD,
\qquad
c_B:=\frac{\eta}{32\pi}.
\tag{2}
\]

The unresolved objects are the two-edge-connected bridge blocks between those trunk edges.

This report shows that almost all of those blocks are finite-complexity, asymptotically two-terminal mechanical corridors. C39 gives only `O(D)` total block graph diameter, while C23 endpoint mass gives only total mass two across all route layers. Therefore, for every fixed `rho>0`, at least `(1-rho)H-o(D)` trunk blocks have:

- graph diameter bounded by a constant depending only on `eta,rho`;
- a bounded number of vertices and edges;
- total nontrunk external force `o(D)`;
- two trunk forces of size at least `c_BD`.

A cut-capacity argument then forces a bounded-length contact path across each such block on which every contact stress is `Omega_{eta,rho}(D)`.

Thus almost the entire ZHT trunk is locally a macroscopic-force corridor. The remaining escape is concentrated in a small fraction of large/side-loaded blocks or in geometrically essential contacts whose stresses are small compared with `D`.

---

## 1. Trunk blocks and the C39 diameter budget

Write the consecutive ZHT bridge trunk as

\[
f_1,\ldots,f_H.
\tag{1.1}
\]

Let

\[
X_0,X_1,\ldots,X_H
\tag{1.2}
\]

be its successive bridge blocks, so internal route block `X_i` is incident to trunk bridges `f_i` and `f_{i+1}` for `1<=i<=H-1`.

Let `delta_X` be the internal contact-graph diameter used by C39, with singleton blocks assigned diameter zero.

C39 proves globally

\[
\sum_X\delta_X
\le2|B|-2
\le2\pi D.
\tag{1.3}
\]

Fix `rho in (0,1)`. Set

\[
K_{\eta,\rho}
:=\frac{4\pi}{\rho c_H}
=\frac{64\pi^2}{\rho\eta^2}.
\tag{1.4}
\]

The number of route blocks with

\[
\delta_{X_i}>K_{\eta,\rho}
\]

is at most

\[
\frac{2\pi D}{K_{\eta,\rho}}
=\frac{\rho c_H}{2}D
\le\frac{\rho H}{2}.
\tag{1.5}
\]

Therefore at least

\[
(1-\rho/2)H-O(1)
\tag{1.6}
\]

internal trunk blocks have graph diameter at most `K_{eta,rho}`.

---

## 2. Bounded graph diameter gives bounded combinatorial complexity

Every vertex of a triangle-free unit-contact graph has contact degree at most five: distinct unit neighbors subtend angles strictly greater than `pi/3`.

A connected graph of maximum degree five and graph diameter at most `K` has at most

\[
M(K):=1+5\sum_{j=0}^{K-1}4^j
\tag{2.1}
\]

vertices. Hence every block counted in (1.6) has at most

\[
M_{\eta,\rho}:=M(K_{\eta,\rho})
\tag{2.2}
\]

vertices and at most

\[
E_{\eta,\rho}:=\frac52M_{\eta,\rho}
\tag{2.3}
\]

internal contact edges.

These constants may be enormous; only finiteness independent of `D` matters.

---

## 3. Endpoint mass assigned to trunk layers has total two

For each loaded terminal `b in B`, let `tau(b)` be its global bridge-tree block. Project `tau(b)` to the unique nearest node of the trunk path `X_0,...,X_H`; call that path node `pi(b)`.

Let

\[
s_b=\sum_{bk\in H}\beta_{bk}
\tag{3.1}
\]

be the total diameter endpoint mass at `b`. Define the mass assigned to route layer `X_i` by

\[
\mu_i:=\sum_{b:\pi(b)=X_i}s_b.
\tag{3.2}
\]

The projection classes partition the loaded terminals, and

\[
\sum_{b\in B}s_b=2.
\]

Therefore

\[
\boxed{
\sum_{i=0}^H\mu_i=2.
}
\tag{ZHN1}
\]

In particular, for any sequence `lambda_D>0`, the number of route layers with `mu_i>lambda_D` is at most `2/lambda_D`.

Choose

\[
\lambda_D=D^{-1/2}.
\tag{3.3}
\]

Then only `O(sqrt D)=o(D)` trunk blocks have `mu_i>D^{-1/2}`.

Intersecting with (1.6), for every fixed `rho>0` at least

\[
\boxed{
(1-\rho/2)H-o(D)
}
\tag{ZHN2}
\]

internal route blocks have simultaneously

\[
\delta_{X_i}\le K_{\eta,\rho},
\qquad
\mu_i\le D^{-1/2}.
\tag{3.4}
\]

Call these **regular trunk blocks**.

---

## 4. Side forces on a regular block are `o(D)`

Fix a regular internal block `X=X_i`.

Its two trunk bridges are the parent and child route edges. Treat every other force incident to `X` as a side force. There are two sources.

### Loaded diameter reactions in `X`

The total norm of the positive diameter reaction at a loaded vertex `b` is at most `Ds_b`. All loaded vertices lying in `X` project to `X`, so

\[
\sum_{b\in B\cap X}|g_b|
\le D\mu_i.
\tag{4.1}
\]

### Off-trunk contact bridges

Every off-trunk bridge at `X` leads into a bridge-tree subtree whose loaded terminal blocks project to `X`. For such a bridge `e`, its crossing beta mass is at most the sum of endpoint masses in that subtree. C20/C23 gives

\[
\alpha_e\le D\,w_e.
\tag{4.2}
\]

The off-trunk subtrees at `X` are disjoint, so summing over them gives

\[
\sum_{e\text{ off trunk at }X}\alpha_e
\le D\mu_i.
\tag{4.3}
\]

Therefore the total magnitude of all nontrunk external forces on the block is at most

\[
\boxed{F_{side}(X)\le2D\mu_i\le2\sqrt D=o(D).}
\tag{ZHN3}
\]

By ZHT, both trunk bridge forces have magnitudes at least `c_BD`.

---

## 5. Every separating contact cut has macroscopic scalar capacity

Let `p^-` and `p^+` be the vertices of `X` incident to its parent and child trunk bridges. If `X` is a singleton, set the internal corridor length to zero and skip this section.

Otherwise take any partition

\[
V(X)=S\sqcup(V(X)\setminus S)
\tag{5.1}
\]

with `p^- in S` and `p^+ notin S`.

Sum mechanical equilibrium over the vertices of `S`. Internal forces cancel except the contact forces on edges crossing the cut. The parent trunk force contributes a vector of magnitude at least `c_BD`. The child trunk force is outside `S`. Every other external force incident to vertices of `S` is part of the side-force budget, whose total norm is at most `F_side(X)`.

Hence the resultant carried by internal contact edges crossing the cut has norm at least

\[
c_BD-F_{side}(X).
\tag{5.2}
\]

For regular blocks and sufficiently large `D`, ZHN3 makes this at least

\[
\frac{c_B}{2}D.
\tag{5.3}
\]

The norm of a vector sum is at most the sum of its positive contact-force magnitudes. Thus every `p^---p^+` edge cut in the internal block graph has scalar alpha-capacity at least

\[
\boxed{
\sum_{e\in\partial S}\alpha_e
\ge\frac{c_B}{2}D.
}
\tag{ZHN4}
\]

---

## 6. Max-flow/min-cut produces a bounded macroscopic-stress contact path

Regard the internal contact graph of `X` as an undirected capacitated graph with edge capacity `alpha_e`.

By ZHN4, every cut separating the two trunk ports has capacity at least `c_BD/2`. Max-flow/min-cut gives a scalar port-to-port flow of value at least

\[
\frac{c_B}{2}D.
\tag{6.1}
\]

Delete flow cycles and decompose the remaining flow into simple `p^---p^+` paths. With at most `E_{eta,rho}` internal edges, at most that many path terms are needed. Hence one path carries at least

\[
\frac{c_B}{2E_{\eta,\rho}}D.
\tag{6.2}
\]

Every edge on that path has capacity at least its path-flow value. Therefore:

### Theorem ZHN.1 — regular blocks contain a bounded macroscopic corridor

Every non-singleton regular trunk block contains a contact path between its two trunk ports of length at most `M_{eta,rho}-1` such that every path edge satisfies

\[
\boxed{
\alpha_e
\ge
c_{\eta,\rho}^{path}D,
\qquad
c_{\eta,\rho}^{path}
:=\frac{c_B}{2E_{\eta,\rho}}>0.
}
\tag{ZHN5}
\]

The constant is extremely small but depends only on fixed `eta,rho`, never on `D`.

Together with ZHN2, this holds in a `(1-rho/2)-o(1)` fraction of all ZHT trunk blocks.

---

## 7. Internal contact stresses are uniformly `O(D)` on regular blocks

This is useful for compactness.

Translate one vertex of `X` to the origin. Because the block graph diameter is at most `K_{eta,rho}` and every contact has length one, every block vertex lies in a Euclidean disk of radius `K_{eta,rho}`.

Sum vertex equilibrium over `X` after dotting each equation with its position. Internal contact edges contribute exactly `alpha_e|x-y|^2=alpha_e`. The only remaining terms are the two trunk bridge forces and the side external forces.

Each trunk force has magnitude at most `D` because every bridge satisfies `alpha_e<=Dw_e<=D`. Therefore

\[
\sum_{e\in E(X)}\alpha_e
\le
K_{\eta,\rho}
\left(2D+F_{side}(X)\right).
\tag{7.1}
\]

For regular blocks,

\[
\boxed{
\sum_{e\in E(X)}\frac{\alpha_e}{D}
\le
2K_{\eta,\rho}+o(1).
}
\tag{ZHN6}
\]

Thus normalized internal stresses on every regular block lie in a compact bounded set.

---

## 8. Finite local-limit normal form

Fix `eta,rho`. There are only finitely many abstract contact graphs with at most `M_{eta,rho}` vertices and two distinguished trunk ports.

Along any unbounded hypothetical sequence, ZHN2 supplies `Omega(D)` regular blocks. By finite pigeonhole and compactness, one can choose a subsequence of regular blocks with:

- one fixed combinatorial block type;
- convergent unit-contact coordinates after Euclidean normalization;
- convergent normalized stresses `alpha_e/D` by ZHN6;
- convergent normalized parent/child trunk forces, each of magnitude at least `c_B`;
- normalized side-force vector tending to zero by ZHN3.

In the limit, all positive normalized contact stress belongs to the mechanical component transmitting the two nonzero trunk forces. The two limiting trunk forces must be equal and opposite. Any positive-stress component not meeting a trunk port would be a pure positive contact self-stress, impossible by the scalar virial identity.

Therefore the positive normalized support joining the two ports is an exact reaction-free two-terminal positive-contact region. C21/C22 classify such a region as a straight constant-stress unit chain.

### Corollary ZHN.2 — local normalized stress collapse

A linear population of regular trunk blocks has subsequential local limits in which

\[
\boxed{
\text{all }\Theta(D)\text{-scale force is transmitted by a straight two-terminal chain.}
}
\tag{ZHN7}
\]

Every contact/branch needed to keep the finite block genuinely two-dimensional or to satisfy C26 carries only `o(D)` stress along that local limiting subsequence.

This is **not yet a contradiction**: actual finite blocks may retain geometrically essential contacts whose stresses are positive but `o(D)`.

---

## 9. Interaction with C68 radialization

For every fixed `xi>0`, a contact edge with

\[
1-(|r_u-r_v|)^2\ge\xi
\tag{9.1}
\]

and stress at least `c D` contributes at least `c xi D` to C68's radial defect `Q_z`.

C68 gives

\[
Q_z=o(D^2)
\tag{9.2}
\]

under `D epsilon->0`.

ZHN supplies `Omega(D)` macroscopic corridor edges across the regular blocks. Hence only `o(D)` of those selected corridor edges can have a fixed radial inefficiency. Almost every selected high-stress corridor edge satisfies

\[
\bigl||r_u-r_v|\bigr|=1-o(1)
\tag{9.3}
\]

in the usual threshold sense.

Thus the local C21/C22 limit chain is also asymptotically radial about the C66 center.

---

## 10. Exact target implication

The ZHT block-corridor obstruction is now finite and local:

```text
for every fixed rho>0,
a (1-rho)-fraction of Omega(D) consecutive trunk blocks has bounded size,
side load o(D),
two trunk forces Omega(D),
a bounded port-to-port contact path with every alpha=Omega(D),
and a local normalized-stress limit equal to a straight two-terminal chain.
```

The unresolved escape is precise:

> bounded-size nontrivial contact blocks can approach a neutral straight two-terminal force chain while the contacts/branches that preserve two-dimensional geometry and contact minimality carry only `o(D)` stress.

A closing local theorem would show that such a sequence of bounded triangle-free unit-contact blocks is incompatible with lexicographic global minimality, ZK redundant rigidity, or the exact unit geometry. Any uniform exclusion for one fixed `rho<1` would eliminate the bridge-dominant `D epsilon->0` branch.

---

## 11. Regressions and limits

- A finite truss can approach an axial mechanism while brace stresses tend to zero; ZHN does not assume otherwise.
- Relative-interior positivity is qualitative and permits `alpha_e/D->0` on braces.
- The local limit may retain zero-normalized-stress unit contacts that make the actual finite graph 2-connected.
- No claim is made that the entire global contact path is uniformly narrow.
- Fully inactive rattlers remain untouched.

---

## 12. Dependencies

- ZHT consecutive macroscopic trunk;
- C23/C20 bridge cut force and endpoint mass;
- C39 total block graph-diameter budget;
- contact degree at most five from unit-angle geometry;
- C21/C22 exact two-terminal positive-support collapse;
- C68 only for Section 9.

No new external literature is imported.

---

## 13. Promotion recommendation

**Hold as report.** It is downstream of report-level ZR/ZF and stacked PR #108/#111.

---

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZHN:
ZHT gives H>=eta^2 D/(16pi) consecutive trunk bridges, each alpha>=eta D/(32pi).
C39 gives sum block graph diameters <=2piD. For every fixed rho>0, all but rho H/2
route blocks have diameter <=K_{eta,rho}=64pi^2/(rho eta^2), hence bounded vertex/edge
count.

Project every loaded terminal block to the trunk and let mu_i be the sum of endpoint
masses s_b assigned to layer i. Sum_i mu_i=2. Thus only o(D) layers have
mu_i>D^{-1/2}. On every remaining bounded block, total nontrunk external force is
<=2D mu_i=o(D), while both trunk forces are Omega(D).

Every cut separating the two trunk ports must therefore carry alpha-capacity Omega(D).
Max-flow/min-cut gives a bounded-length port-to-port contact path all of whose edges
have alpha=Omega(D). Internal alpha/D is uniformly bounded by a local virial estimate.

Consequently a linear population of bounded trunk blocks has local subsequential limits
where side load vanishes and the positive normalized support is an exact reaction-free
two-terminal system; C21/C22 makes it a straight constant-stress unit chain.

Remaining local obstruction:
actual finite blocks can retain 2D geometry only through contacts/branches whose
normalized stresses alpha/D tend to zero. Excluding that bounded-size axial-degeneration
under lexicographic global minimality would close the bridge-dominant small-defect branch.
```
