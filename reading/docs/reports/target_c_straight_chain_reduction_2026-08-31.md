> Generated reading edition · [exact source](../../../docs/reports/target_c_straight_chain_reduction_2026-08-31.md) · source SHA-256 `977dc985094875e1bfebb61880be4bf1b010ac5a9463ffd28978a1049608ec6c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7AD749371862","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: exact straight-chain reduction

**Date:** 2026-08-31  
**Repository state:** `research/target-c-bridge-reciprocal-2026-08-31`  
**Run type:** proof / structural reduction  
**Target:** C-II  
**Depends on:** Target C KKT equilibrium and the bridge/reciprocal addendum C20  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The positive KKT contact network has a rigid local form at every unloaded degree-two
vertex.  Such a vertex is the midpoint of its two contact neighbors, and the two
contact stresses are equal.  Therefore every maximal run of unloaded degree-two
vertices is an exact straight unit chain carrying constant axial stress.

Suppressing those vertices turns the fully force-visible contact graph into a plane
weighted skeleton with positive-integer edge lengths.  The normalized KKT virial
identity becomes an exact stress-length identity on that skeleton:

```math
\boxed{\sum_{E\in E(\mathscr S)} L_E\alpha_E=D^2.}
```

This identifies the precise loophole left by the bridge/reciprocal theorem C20.  A
large amount of bridge stress can evade the `O(D)` reciprocal-frontier budget only by
being transported repeatedly along long straight chains between genuine reaction,
branching, or two-edge-connected events.

---

## 1. Local equilibrium at an unloaded low-degree vertex

Fix a normalized KKT stress.  Let `C_+` be its positive unit-contact graph and `B_+`
the positive diameter-reaction vertices.  At every vertex `x notin B_+`, KKT
equilibrium is

```math
\boxed{
\sum_{xy\in C_+}\alpha_{xy}(x-y)=0,
\qquad \alpha_{xy}>0.
}
\tag{C21.1}
```

Every positive contact has length one.

### Lemma C21.1 (no unloaded leaf)

If `x notin B_+`, then
```math
\boxed{\deg_{C_+}(x)\ne1.}
\tag{C21.2}
```

#### Proof

A single nonzero vector with a positive coefficient cannot sum to zero in (C21.1).
`\square`

### Theorem C21.2 (unloaded degree two is exactly straight)

Suppose `x notin B_+` has exactly two positive-contact neighbors `y,z`.  Then

```math
\boxed{
y,x,z\text{ are collinear},
\qquad |y-x|=|x-z|=1,
\qquad x=\frac{y+z}{2},}
\tag{C21.3}
```

and

```math
\boxed{\alpha_{xy}=\alpha_{xz}.}
\tag{C21.4}
```

#### Proof

Put
```math
u=x-y,\qquad v=x-z.
```
Both are unit vectors.  Equation (C21.1) becomes
```math
\alpha_{xy}u+\alpha_{xz}v=0.
\tag{C21.5}
```
A positive linear combination of two nonzero vectors can vanish only when the vectors
are antiparallel.  Since they have the same norm,
```math
v=-u
```
and equality of coefficients follows from (C21.5).  The geometric statements in
(C21.3) are immediate. `\square`

This uses neither genericity nor triangle-freeness.

---

## 2. Maximal neutral chains

Call a contact vertex **structural** when it belongs to `B_+` or its positive-contact
degree is not two.  A **neutral chain** is a simple contact path
```math
P=(x_0,x_1,\ldots,x_L)
\tag{C21.6}
```
whose internal vertices `x_1,...,x_{L-1}` are nonreaction degree-two vertices.

### Corollary C21.3 (straight constant-stress chain)

Every neutral chain satisfies
```math
\boxed{
x_i=x_0+i u
\qquad(0\le i\le L)}
\tag{C21.7}
```
for one unit vector `u`, and all its contact edges have one common stress value
```math
\boxed{\alpha_{x_{i-1}x_i}=\alpha_P>0.}
\tag{C21.8}
```
Consequently
```math
\boxed{|x_0-x_L|=L.}
\tag{C21.9}
```

#### Proof

Apply Theorem C21.2 at each internal vertex.  Consecutive edge directions continue
straight and consecutive stress coefficients agree.  Induction gives (C21.7)--(C21.8),
and (C21.9) follows. `\square`

In particular `L<=D` because the whole source has diameter `D`.

A connected positive-contact component cannot be a cycle consisting entirely of
nonreaction degree-two vertices.  Equation (C21.1) would then make every vertex a
strict barycenter of its two neighbors; equivalently Corollary C21.3 would force the
cycle to lie on one line.  Also the canonical support-connectivity theorem says the
positive component contains positive diameter endpoints.  Therefore every maximal
neutral chain terminates at structural vertices.

---

## 3. The weighted structural skeleton

Suppress every internal vertex of every maximal neutral chain.  Let
```math
\mathscr S
\tag{C21.10}
```
be the resulting graph.  Its vertices are the structural vertices.  For each skeleton
edge `E=ab`, let

```math
L_E\in\mathbb Z_{\ge1}
\tag{C21.11}
```
be the number of unit contacts in the corresponding neutral chain and let
`alpha_E` be the common stress on that chain.

### Theorem C21.4 (plane integer-length stress skeleton)

The skeleton has the following exact properties.

1. Every skeleton edge is realized by the straight segment `[a,b]` and
   ```math
   \boxed{|a-b|=L_E\in\mathbb Z_{\ge1}.}
   \tag{C21.12}
   
   ```
2. The straight-line skeleton is plane.  Distinct edge interiors are disjoint.
3. At every nonreaction skeleton vertex `a`,
   ```math
   \boxed{
   \sum_{E=ab}\alpha_E\frac{a-b}{L_E}=0.
   }
   \tag{C21.13}
   
   ```
   At a reaction vertex `b in B_+`, the same left side equals the canonical diameter
   reaction `g_b`.
4. The normalized contact virial becomes
   ```math
   \boxed{
   
   \sum_{E\in E(\mathscr S)}L_E\alpha_E=D^2.
   }
   \tag{C21.14}
   
   ```

#### Proof

Item 1 is Corollary C21.3.  If two skeleton segments crossed properly, some two unit
contact edges in their underlying chains would cross properly, impossible for a penny
graph.  A nontrivial collinear overlap would give two different unit-spaced contact
chains on the same segment; the ordered unit positions are unique, so the chains would
share suppressed vertices and would not be distinct maximal chains.  This proves item
2.

At a structural endpoint `a`, the contact force contributed by the first edge of the
chain to `b` is
```math
\alpha_E\frac{a-b}{|a-b|}
=
\alpha_E\frac{a-b}{L_E}.
```
All suppressed internal forces cancel by equilibrium.  Summing over incident chains
gives (C21.13) and its reaction version.

Finally each skeleton edge represents exactly `L_E` unit contacts, each with stress
`alpha_E`.  Summing their contributions to
`sum_{e in C_+}alpha_e=D^2` gives (C21.14). `\square`

The skeleton may be a multigraph only if two distinct contact routes have the same
structural endpoints.  But two straight neutral chains between the same endpoints
would both have length `|a-b|` and therefore the same uniquely determined unit-spaced
vertices; they are the same chain.  Thus neutral-chain suppression itself does not
create parallel edges.

---

## 4. Exact interaction with contact bridges

A maximal neutral chain is either wholly contained in one two-edge-connected contact
block or every one of its unit edges is a contact bridge.  Indeed an edge on the chain
lies on a cycle if and only if there is an alternate path between the chain endpoints;
then every edge of the straight series path lies on the corresponding cycle.

Suppose a skeleton edge `E` is a bridge edge.  Every one of its `L_E` underlying unit
contacts is then a positive contact bridge with the same stress `alpha_E`.
Moving a bridge cut across one suppressed internal vertex changes no positive diameter
reaction vertex on either side.  Therefore Theorem C20.2 assigns the **same**
reciprocal-polygon diagonal to every unit bridge in the chain:

```math
\boxed{
\Delta z_E
=\alpha_E J\frac{a-b}{L_E},
\qquad
|\Delta z_E|=\alpha_E.
}
\tag{C21.15}
```

Thus repeated identical reciprocal diagonals have an exact primal meaning: they are
precisely straight unloaded series transport until a reaction, branch, or
2-edge-connected event changes the cut data.

---

## 5. C-II bridge-depth refinement

Now assume the fully force-visible branch and choose a relative-interior normalized
KKT stress, so `C_+=C`.

Let
```math
S_{\rm br}
=
\sum_{e\text{ bridge of }C}\alpha_e
\tag{C21.16}
```
be the total contact-stress mass on bridges.  C20 gives, for every bridge-tree depth
frontier, total stress at most `2D`.  Hence if
```math
S_{\rm br}\ge\eta D^2
\tag{C21.17}
```
for some `eta>0`, then the bridge tree has unit-edge depth at least
```math
\boxed{\frac{\eta D}{2}.}
\tag{C21.18}
```

Along any bridge-tree path, every maximal subrun with no reaction vertex, no branching
vertex, and no nontrivial two-edge-connected block is a neutral chain and is therefore
an exact straight unit segment carrying constant stress by Corollary C21.3.

This gives the sharpened C-II articulation alternative:

- either almost all normalized stress lies in two-edge-connected contact blocks;
- or a positive fraction lies on bridges, forcing an `Omega(D)`-deep bridge corridor;
- along that corridor every interval between genuinely two-dimensional events is an
  exact straight constant-stress chain, represented by one repeated reciprocal
  diagonal.

No contradiction is claimed.  A long straight chain is a binding local regression.
The new reduction identifies exactly what additional event must interrupt it.

---

## 6. Regression audit

- **Straight chain:** satisfies C21.2--C21.15 exactly; it is not a global C-II
  counterexample because the one-dimensional force-hull phase is excluded by C19.
- **Unit square:** every contact vertex is a reaction vertex in the standard symmetric
  stress, so no vertex is suppressed; the skeleton is the square itself.
- **Rhombic grid:** degree-four unloaded vertices survive as structural vertices.  The
  theorem does not incorrectly collapse a genuinely two-dimensional rhombic bulk.
- **Long obtuse source runs:** permitted.  The theorem uses positive KKT contact
  equilibrium, not an unweighted Schuermann-type loose-edge claim.
- **KKT-invisible points:** irrelevant to the skeleton and not assumed absent.

---

## 7. Exact next lemma

The bridge side of C-II is now reduced to a quantitative event-frequency problem.
One sufficient theorem is:

> **No deep sparse-event bridge corridor.**  In a sufficiently large global
> minimizer, an `Omega(D)` bridge-tree path in the fully force-visible positive contact
> graph must contain `Omega(D)` reaction/branching/nontrivial-block events, and those
> events force either a forbidden diameter configuration or a contact-density/area
> cost incompatible with global minimum diameter.

The complementary two-edge-connected branch remains open and should be attacked via
the circular-planar response and second-order angular-variance identities rather than
bridge combinatorics.
