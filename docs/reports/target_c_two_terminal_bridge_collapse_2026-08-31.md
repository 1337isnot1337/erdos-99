<!-- theorem-state: {"artifact_id":"ART-6331540B52A9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: two-terminal bridge collapse and reaction budget

**Date:** 2026-08-31  
**Repository base:** `188a2b81fbc292db6d6873fe2c86b6924a5115ea`  
**Run type:** proof / structural reduction  
**Target:** C-II  
**Depends on:** Target C force-hull equilibrium, support connectivity, bridge/reciprocal theorem C20, and straight-chain theorem C21  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This note removes a residual loophole in the bridge side of Target C-II.

C21 proved that an unloaded positive-contact vertex of degree two lies on an exact
straight constant-stress unit chain.  A priori, however, a deep bridge corridor could
pass through a larger reaction-free two-dimensional block with exactly two bridge
terminals.  That possibility does not occur.

The new theorem is a finite maximum principle:

> Any connected positive-contact region with no positive diameter reaction and exactly
> two positive-contact edges leaving it is an exact straight constant-stress unit
> chain, regardless of how complicated the region was assumed to be.

Consequently, after deleting all positive-contact bridges, every nontrivial
reaction-free block has bridge-tree degree at least three.  Suppressing the remaining
single-vertex neutral degree-two blocks leaves at most `2|B_+|-2` structural block
nodes and at most `2|B_+|-3` bridge corridors.  Since the loaded vertices `B_+` are
unit-separated vertices of a convex set of diameter `D`, `|B_+| <= pi D`.

Thus a deep C-II bridge corridor can no longer use a reaction-free two-terminal
2-edge-connected block as a hidden two-dimensional event.  Every genuine event must
consume a positive diameter-reaction block or branch toward another loaded subtree.

---

## 1. Setup

Fix a normalized KKT stress `(alpha,beta)`.  Let

\[
C_+=\{xy:\alpha_{xy}>0\},
\qquad
H_+=\{bk:\beta_{bk}>0\},
\tag{C22.1}
\]

let `B_+=V(H_+)`, and let `F=conv B_+=conv V(C_+)`.  By the promoted Target C
support-connectivity theorem, `C_+` has one nontrivial connected component and that
component has Euclidean diameter `D`.

For `b in B_+`, write

\[
g_b
=\sum_{bk\in H_+}\beta_{bk}(b-k)
=\sum_{bc\in C_+}\alpha_{bc}(b-c).
\tag{C22.2}
\]

At a positive-contact vertex `x notin B_+`, put `g_x=0`.  Then the contact equilibrium
at every positive-contact vertex is

\[
\boxed{
 g_x=\sum_{xy\in C_+}\alpha_{xy}(x-y).
}
\tag{C22.3}
\]

All positive contacts have length one.

Let `uv` be a positive-contact bridge.  Removing it gives components `S,T`, with
`u in S` and `v in T`.  Put `B_S=B_+ cap S` and `B_T=B_+ cap T`.  C20 gives

\[
\sum_{b\in B_S}g_b=\alpha_{uv}(u-v).
\tag{C22.4}
\]

Both `B_S` and `B_T` are nonempty cyclic intervals of the loaded boundary order.

---

## 2. The bridge force is exactly a diameter-cut flow

The reaction sum in C22.4 can be expanded directly in the positive diameter graph.

### Lemma C22.1 (diameter-cut flow)

Orient every positive diameter edge crossing the partition `(B_S,B_T)` from its
endpoint `b in B_S` to its endpoint `k in B_T`.  Then

\[
\boxed{
\alpha_{uv}(u-v)
=
\sum_{\substack{bk\in H_+\\b\in B_S,\ k\in B_T}}
\beta_{bk}(b-k).
}
\tag{C22.5}
\]

In particular every positive-contact bridge separates the endpoints of at least one
positive diameter edge.

#### Proof

Expand the left side of C22.4 using the diameter formula in C22.2.  A positive
diameter edge with both endpoints in `B_S` contributes opposite vectors at its two
endpoints and cancels.  An edge with both endpoints in `B_T` contributes nothing to
the `B_S` sum.  The surviving terms are exactly the crossing edges, with the stated
orientation.  The bridge force is nonzero, so at least one crossing diameter edge is
present. `\square`

Thus the bridge tree is not supported by abstract boundary loads: every bridge cut is
crossed by the actual positive diameter graph.

---

## 3. A partial virial identity for every bridge side

The bridge cut also has an exact internal-stress identity.

For the side `S`, define

\[
W(S):=
\sum_{xy\in C_+[S]}\alpha_{xy},
\tag{C22.6}
\]

the total positive contact stress on edges with both endpoints in `S`.

### Lemma C22.2 (bridge-side virial)

\[
\boxed{
W(S)
=
\sum_{b\in B_S}(b-u)\cdot g_b.
}
\tag{C22.7}
\]

If

\[
s_b:=\sum_{bk\in H_+}\beta_{bk},
\tag{C22.8}
\]

then also

\[
\boxed{
W(S)
\ge
\frac12
\sum_{b\in B_S}s_b|b-u|^2.
}
\tag{C22.9}
\]

#### Proof

Dot C22.3 with the position vector `x` and sum over `x in S`.  Every internal
positive contact `xy` contributes

\[
\alpha_{xy}
\bigl[x\cdot(x-y)+y\cdot(y-x)\bigr]
=
\alpha_{xy}|x-y|^2
=
\alpha_{xy}.
\tag{C22.10}
\]

The only positive contact leaving `S` is `uv`, so its contribution is

\[
\alpha_{uv}u\cdot(u-v).
\tag{C22.11}
\]

Hence

\[
\sum_{b\in B_S}b\cdot g_b
=W(S)+u\cdot\alpha_{uv}(u-v).
\tag{C22.12}
\]

Use C22.4 to replace the bridge vector by `sum_{b in B_S}g_b` and rearrange.  This is
C22.7.

For C22.9, every `u in V(C_+)` lies in the force hull `F`.  Target C Lemma C5 gives,
for every positive diameter edge `bk` incident to `b`,

\[
(b-k)\cdot(b-u)
\ge\frac{|b-u|^2}{2}.
\tag{C22.13}
\]

Multiply by `beta_{bk}`, sum over the positive diameter edges incident to `b`, and use
C22.2:

\[
g_b\cdot(b-u)
\ge\frac{s_b}{2}|b-u|^2.
\tag{C22.14}
\]

Summing over `b in B_S` and applying C22.7 proves C22.9. `\square`

The identity is translation invariant.  It says that the internal contact stress of a
bridge side is exactly the work of its loaded-boundary reactions relative to the
bridge endpoint.  The lower bound shows that positive diameter mass far from the
bridge endpoint has a quadratic stress cost.

---

## 4. Two-terminal reaction-free regions collapse to one dimension

The next theorem is the main new reduction.

Let `K` be a nonempty vertex set in the positive contact component.  Assume:

1. the induced positive-contact graph `C_+[K]` is connected;
2. exactly two positive-contact edges leave `K`, say
   \[
   aa',\qquad bb',
   \tag{C22.15}
   \]
   with `a,b in K` and `a',b' notin K`; and
3. `K cap B_+` is empty.

No assumption is made about the number of vertices, cycles, degrees, or faces inside
`K`.

### Theorem C22.3 (two-terminal collapse)

Under the three assumptions above, the entire region and its two terminal contacts lie
on one straight line.  More precisely, for one unit vector `d` and one integer
`L>=0`, after orienting the terminals appropriately,

\[
\boxed{
 a'=a-d,
 \qquad
 b=a+Ld,
 \qquad
 b'=b+d,
}
\tag{C22.16}
\]

and

\[
\boxed{
V(C_+[K])
=\{a,a+d,\ldots,a+Ld\}.
}
\tag{C22.17}
\]

The positive-contact graph on `K` is exactly the unit path through these points, and
every edge of the extended path from `a'` to `b'` has one common stress value.

#### Proof

Because `K cap B_+=emptyset`, every vertex of `K` has zero external diameter reaction.
Sum the vector equilibrium C22.3 over all vertices of `K`.  Internal contact forces
cancel in opposite pairs.  Only the two leaving contacts remain, giving

\[
\alpha_{aa'}(a-a')
+
\alpha_{bb'}(b-b')
=0.
\tag{C22.18}
\]

Both contact vectors have length one and both coefficients are positive.  Therefore
there is a unit vector `d` and a number `tau>0` such that

\[
\alpha_{aa'}=\alpha_{bb'}=\tau,
\qquad
a-a'=d,
\qquad
b-b'=-d.
\tag{C22.19}
\]

Now take scalar moments of the equilibrium equations about an arbitrary origin and
sum over `K`.  Every internal central-force edge has zero total moment:

\[
\alpha_{xy}
\bigl[x\times(x-y)+y\times(y-x)\bigr]=0.
\tag{C22.20}
\]

The two terminal contributions therefore satisfy

\[
\tau a\times d-	au b\times d=0,
\]
so

\[
\boxed{(a-b)\times d=0.}
\tag{C22.21}
\]

Thus the two terminal forces have the same line of action.

Let `n=Jd` and put

\[
y_x=n\cdot x
\qquad(x\in K).
\tag{C22.22}
\]

Project the vertex equilibrium at every `x in K` onto `n`.  The two terminal forces
have zero `n`-component by C22.19.  Hence the scalar coordinates satisfy the weighted
Laplacian equations

\[
\sum_{xy\in C_+[K]}
\alpha_{xy}(y_x-y_y)=0
\qquad(x\in K).
\tag{C22.23}
\]

Multiply C22.23 by `y_x` and sum over `x in K`.  Symmetrizing over internal edges gives

\[
\sum_{xy\in C_+[K]}
\alpha_{xy}(y_x-y_y)^2=0.
\tag{C22.24}
\]

Every coefficient is positive, and `C_+[K]` is connected.  Therefore

\[
y_x=y_y
\qquad(x,y\in K).
\tag{C22.25}
\]

All vertices of `K` lie on one line parallel to `d`.  Together with C22.21 and
C22.19, the two external neighbors `a',b'` lie on the same line.

Order the vertices of `K` along that line.  Unit separation makes every gap between
consecutive vertices at least one.  If some consecutive gap were larger than one, no
unit contact could cross it, contradicting connectedness of `C_+[K]`.  Thus every
consecutive gap is exactly one.  Nonconsecutive vertices are at distance at least two,
so the only internal unit contacts are the consecutive ones.  Hence `C_+[K]` is the
exact unit path C22.17.

The external point `a'=a-d` cannot coincide with a vertex of `K`, so `a` is the end of
the path on the `-d` side.  Similarly `b'=b+d` makes `b` the end on the `+d` side.
This gives C22.16 after choosing the orientation of `d`.

Finally, one-dimensional equilibrium at each vertex of the extended path forces the
two incident positive axial stresses to agree.  Starting from the terminal value
`tau`, induction gives the same stress on every internal edge and on the opposite
terminal edge. `\square`

The theorem is stronger than the degree-two statement C21.2.  The region was allowed
to contain arbitrary branching or cycles; positivity plus the absence of transverse
external reaction collapses all of it.

---

## 5. The bridge-block tree has only loaded or branching events

Delete every bridge of `C_+`.  Contract each resulting connected component to one
node.  The positive-contact component is connected, so the resulting graph `T_br` is
a tree.  Call its nodes **bridge blocks**.  A bridge block is **loaded** if it contains
at least one vertex of `B_+`.

### Corollary C22.4 (reaction-free degree-two blocks are trivial)

Assume `T_br` has at least one edge.

1. Every leaf bridge block is loaded.
2. Every reaction-free bridge block of degree two consists of a single unloaded
   contact vertex.  Its two incident bridges are collinear and have equal stress.
3. Consequently every nontrivial reaction-free bridge block has degree at least three
   in `T_br`.

#### Proof

For a leaf block, orient its unique incident bridge toward the rest of the graph.  The
leaf side of that bridge is exactly the block.  C20.1 says every bridge side contains a
positive diameter-reaction vertex, so the leaf block is loaded.

Now let `K` be a reaction-free degree-two bridge block.  Exactly its two incident
bridges leave `K`, so Theorem C22.3 applies and makes `C_+[K]` a straight unit path.
If this path contained an internal edge, that edge would disconnect `K`, and because
`T_br` is a tree there is no route through the rest of the contact graph joining the
two sides without passing through `K`.  The internal edge would therefore be a bridge
of `C_+`, contradicting the definition of a component obtained after all bridges were
deleted.  Hence `K` is one vertex.  The final statement is immediate. `\square`

Thus a nontrivial two-edge-connected block cannot act as a reaction-free two-terminal
turning event.  If such a block has bridge-tree degree two, it must contain positive
diameter reaction.  If it contains no positive diameter reaction, it must branch to
at least three bridge-tree directions.

---

## 6. Linear bound on all structural bridge events

Suppress every reaction-free degree-two singleton block from `T_br`.  By C22.4 and C21,
each suppressed run is an exact straight constant-stress unit bridge chain.  Let the
resulting tree be `T_str`.

Let

- `R` be the number of loaded nodes of `T_str`;
- `L` be the number of leaves of `T_str`; and
- `I_0` be the number of reaction-free nodes of `T_str`.

Every leaf is loaded, so `L<=R`.  Every reaction-free node has degree at least three.
For every finite tree with at least two vertices,

\[
L
=2+
\sum_{x:\deg(x)\ge3}(\deg(x)-2).
\tag{C22.26}
\]

Therefore

\[
I_0\le L-2\le R-2.
\tag{C22.27}
\]

Each loaded block contains at least one distinct vertex of `B_+`, hence

\[
R\le |B_+|.
\tag{C22.28}
\]

We obtain the exact complexity bound

\[
\boxed{
|V(T_{str})|
=R+I_0
\le2|B_+|-2,
}
\tag{C22.29}
\]

and hence

\[
\boxed{
|E(T_{str})|
\le2|B_+|-3.
}
\tag{C22.30}
\]

Every edge of `T_str` represents one maximal exact straight constant-stress bridge
corridor.

Finally `B_+` is the vertex set of the convex force hull `F`.  Consecutive force-hull
vertices are source points and therefore are at distance at least one, so

\[
|B_+|\le\operatorname{per}(F).
\tag{C22.31}
\]

Cauchy's perimeter formula gives, for every planar convex body of diameter `D`,

\[
\operatorname{per}(F)
=\int_0^\pi w_F(\theta)\,d\theta
\le\pi D.
\tag{C22.32}
\]

Consequently

\[
\boxed{
|V(T_{str})|\le2\pi D-2,
\qquad
|E(T_{str})|\le2\pi D-3.
}
\tag{C22.33}
\]

The integer quantities can of course be replaced by the corresponding floor bounds.

---

## 7. Exact C-II effect

In the fully force-visible branch choose a relative-interior normalized KKT stress, so
`C_+=C`.  C20-C21 already give the following alternative if a positive fraction
`eta D^2` of contact stress lies on bridges:

\[
\text{bridge-tree depth}\ge\frac{\eta D}{2}.
\tag{C22.34}
\]

C22 sharpens the geometry of that deep tree.

A deep path is no longer allowed to alternate arbitrarily among

- straight neutral chains;
- reaction vertices;
- branching vertices; and
- reaction-free nontrivial two-edge-connected blocks.

The fourth category disappears as an independent event.  After maximal suppression,
**every** genuine event is either

1. a block containing at least one positive diameter-reaction vertex; or
2. a reaction-free branching block of bridge-tree degree at least three.

There are at most `2|B_+|-2 <= 2 pi D-2` such structural blocks in the entire bridge
tree, and the bridge portions between them are exact straight constant-stress unit
chains.

This does not yet contradict C22.34: both the depth lower bound and the event budget are
of order `D`.  It does, however, remove the possibility that `Omega(D)` depth is hidden
inside a succession of unloaded two-terminal two-dimensional gadgets.

The shortest remaining bridge-side lemma is now quantitative:

> **Loaded-event cost theorem.**  Show that along an `Omega(D)`-deep fully
> force-visible bridge path, the loaded/branching structural events from C22 cannot
> occur at linear frequency without violating the explicit diameter-angle/cycle
> restrictions or a global finite-packing inequality.
>
> Equivalently, prove a sublinear event bound on such a path, or prove a positive
> global capacity cost per event.  C22 would then force an `omega(1)`-long straight
> corridor; a sufficiently strong sublinear bound would force an `Omega(D)` straight
> corridor and expose the one-dimensional/packing contradiction directly.

The complementary branch, in which almost all stress lies in bridgeless contact
blocks, remains a separate C-II problem.

---

## 8. Regression audit

- **Straight chain:** C22.3 recovers it exactly.  A whole-source straight chain is still
  excluded only by the promoted one-dimensional force-hull theorem C19.
- **Y-shaped positive tree:** allowed.  Its central reaction-free region has three
  terminals, not two.
- **Unit square / regular pentagon:** bridge-free, so C22 does not apply.
- **Reaction-bearing two-edge-connected block:** allowed.  The transverse maximum
  principle has a source term there.
- **Reaction-free branching block:** allowed only with bridge-tree degree at least
  three, exactly as C22.4 states.
- **KKT-invisible points:** untouched; the theorem concerns the positive contact
  component for the chosen normalized stress.
- **Small individual stresses:** allowed.  No lower bound on any `alpha_e`, `beta_h`,
  or `|g_b|` is assumed.

The proof uses only exact KKT equilibrium, positivity, bridge topology, unit separation,
and elementary convex perimeter geometry.  No generic rigidity, PSD/Loewner claim,
lattice scaffold, or rhombic shell hypothesis is used.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New Target C theorem C22:
Let K be a connected region of the positive unit-contact graph with exactly two
positive-contact edges leaving K and with K cap B_+ empty.  Summed equilibrium makes
the two terminal forces equal and opposite; summed torque makes them collinear.
Projecting every vertex equilibrium perpendicular to that line gives a positive
weighted graph Laplacian with zero boundary source.  Hence the perpendicular coordinate
is constant on K.  Unit separation + connectedness then force K, together with its two
terminal contacts, to be one exact straight constant-stress unit chain.

Bridge-tree consequences:
- every leaf bridge block contains a positive diameter-reaction vertex;
- every reaction-free degree-2 bridge block is only one neutral degree-2 vertex;
- every nontrivial reaction-free bridge block has bridge-tree degree >=3.
After suppressing neutral degree-2 blocks, if q=|B_+| then the structural bridge tree
has at most 2q-2 nodes and 2q-3 straight bridge corridors.  Since q<=per(F)<=pi D,
there are at most 2pi D-2 structural events globally.

Additional exact cut identities:
  alpha_uv(u-v)
    = sum_{positive diameter edges crossing the bridge cut} beta_h(b-k),
and for the bridge side S containing u,
  sum_{xy in C_+[S]} alpha_xy
    = sum_{b in B_S}(b-u).g_b
    >= (1/2) sum_{b in B_S} s_b |b-u|^2.

C-II improvement:
A deep bridge corridor cannot hide 2D behavior in reaction-free two-terminal blocks.
Every genuine event is reaction-bearing or branches toward another loaded subtree.
The remaining bridge lemma is to make the resulting O(D) event budget sublinear, or
charge each event a global packing/diameter cost that forbids linear frequency.
```
