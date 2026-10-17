> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_p1_rectangle_twin_completion_2026-09-09.md) · source SHA-256 `6bdd00bab62914a9dc0eccc09d35d1189934d96fbdbb57ae53f4a536c47d5bde`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-9088814006A1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — P1 is a unit-width rectangle tie with a twin-completion KKT core

**Date:** 2026-09-09  
**Repository branch:** PR #118 after D1/SC/LF  
**Run type:** exact parallel-tie / maximal-thrackle refinement  
**Target:** cyclic primitive phase `d_H=1`, parallel-side endpoint P1  
**Depends on:** D1 exact P1 difference body, DC spanning diameter tree, LF leaf-edge forcing, maximal convex-thrackle structure  
**External literature:** none used in the proof; rotating-calipers monotonicity is reproved in the needed tie form  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

D1 identifies P1 as the endpoint where the unique S1 short difference-body vertex collapses and the two adjacent unit Minkowski edges become one edge of length two. In primal geometry this is much more rigid than merely saying that one pair of hull sides is parallel.

The four endpoints of that parallel side pair form an exact rectangle. Its two diagonals are actual diameter edges, while its other two sides are equal short antipodal chords of length `sqrt(D^2-1)`. Either short chord can be inserted into the diameter tree to produce a maximal convex thrackle.

The two maximal completions need not have the same odd cycle. Using both at once confines every KKT-face diameter edge to the common path where those two odd cycles overlap.

### Theorem PR — P1 rectangle and twin completion

Let the unique pair of parallel hull sides be

```math
ab,\qquad cd
```

in cyclic shell order, oriented counterclockwise so that

```math
b-a=t,
\qquad
d-c=-t,
\qquad |t|=1.
\tag{PR.1}
```

Then:

1. `a,b,c,d` form a rectangle;
2. its diagonals are actual diameter pairs
   
   ```math
   |a-c|=|b-d|=D;
   \tag{PR.2}
   ```

3. its other two sides are equal short antipodal pairs
   
   ```math
   a-d=b-c,
   \qquad
   |a-d|=|b-c|=\sqrt{D^2-1};
   \tag{PR.3}
   ```

4. the projective diameter directions have exactly one gap
   
   ```math
   \Delta_2=2\arcsin(1/D)
   ```

   and all remaining `q-2` gaps equal
   
   ```math
   \delta=2\arcsin(1/(2D));
   ```

5. both graphs
   
   ```math
   T_{ad}:=H+ad,
   \qquad
   T_{bc}:=H+bc
   \tag{PR.4}
   ```

   are maximal `q`-edge convex thrackles and hence each consists of one odd cycle plus direct leaves;
6. if `C_ad,C_bc` are their unique odd cycles and
   
   ```math
   J:=(C_{ad}\cap H)\cap(C_{bc}\cap H),
   \tag{PR.5}
   ```

   then `J` is a path in the diameter tree and every KKT boundary coordinate lies on `J`;
7. because the `d_H=1` KKT interval has two distinct coordinate facets,
   
   ```math
   \boxed{|E(J)|\ge2.}
   \tag{PR.6}
   ```


Equivalently, every diameter edge outside the common twin-cycle path `J` is a full-`H` leaf edge and is beta-positive throughout the complete KKT segment.

---

## 1. The merged difference-body edge gives two diameter diagonals

The Minkowski edge merge for

```math
K=F+(-F)
```
combines the primal side `ab`, whose vector is `t`, with the corresponding side of `-F` coming from `cd`, whose vector is also `t` because `d-c=-t`.

Thus the unique length-two edge of `K` is

```math
[a-c,\ b-d]
```
with vector

```math
(b-d)-(a-c)=2t.
\tag{1.1}
```

P1 has no off-circle difference-body vertices. Therefore both endpoints of this merged edge lie on the radius-`D` circle:

```math
|a-c|=|b-d|=D.
```

These are the two actual diameter edges adjacent to the unique large projective direction gap.

---

## 2. The four primal vertices form a rectangle

From PR.1,

```math
b=a+t,
\qquad
d=c-t.
```

Hence

```math
a+c=b+d.
\tag{2.1}
```

So the quadrilateral with vertices `a,b,c,d` in shell order is a parallelogram: its diagonals `ac` and `bd` have the same midpoint.

But Section 1 gives

```math
|a-c|=|b-d|=D.
```

A parallelogram has equal diagonals if and only if it is a rectangle. Thus `a,b,c,d` form a rectangle.

One pair of rectangle sides has length one by construction. The Pythagorean theorem with diagonal `D` gives the other side length

```math
L=\sqrt{D^2-1}.
```

Algebraically,

```math
a-d=a-(c-t)=a-c+t=b-c,
```
so the two long rectangle sides are equal directed chords. This proves PR.3.

Because `ab` and `cd` lie on opposite parallel support lines of `F`, every endpoint choice across those two support faces is an antipodal vertex pair. In particular both short rectangle sides `ad` and `bc` are vertex-vertex antipodal pairs, although their length is strictly below `D`.

---

## 3. Exact projective diameter-gap code

The merged K-edge has chord length two in the radius-`D` circle. Therefore the central/projective angle between its endpoints `a-c` and `b-d` is

```math
\boxed{\Delta_2=2\arcsin\frac1D.}
\tag{3.1}
```

Every other K-edge is a unit chord joining two radius-`D` vertices, hence subtends

```math
\boxed{\delta=2\arcsin\frac1{2D}.}
\tag{3.2}
```

There are `q-2` such ordinary projective gaps. Thus the complete diameter-direction circle is

```text
q-1 actual diameter directions,
q-2 gaps of size delta,
one gap of size Delta_2.
```

and closure of the projective circle is exactly the D1 P1 equation

```math
(q-2)\delta+\Delta_2=\pi.
\tag{3.3}
```

The two diameter edges at the ends of the exceptional gap are the crossing rectangle diagonals `ac` and `bd`.

---

## 4. The tie has two canonical antipodal refinements

The length-two K-edge can be viewed as the sum of two collinear unit Minkowski steps. There are exactly two orders in which the two summand support vertices can change.

Starting at the diameter state `a-c` and ending at `b-d`, the two refined state sequences are

```math
a-c\longrightarrow b-c\longrightarrow b-d,
\tag{4.1}
```

or

```math
a-c\longrightarrow a-d\longrightarrow b-d.
\tag{4.2}
```

Thus the two possible intermediate antipodal chords are precisely the two short rectangle sides

```math
bc,\qquad ad.
```

For either refinement, the maximizing and minimizing support indices move monotonically around the two shell copies exactly as in the strict rotating-calipers argument. Consequently any two distinct chords in that refined antipodal list either share an endpoint or have alternating endpoints and cross properly.

All original states other than the inserted one are actual diameter pairs, i.e. the edges of `H`. Therefore

```math
H+bc
```
and
```math
H+ad
```
are both convex straight-line thrackles.

Each has

```math
(q-1)+1=q
```
edges on `q` vertices. The convex-thrackle edge bound is `q`, so both are maximal. The standard maximal structure gives one odd cycle plus direct leaves in each completion. This proves PR.4.

---

## 5. Intersect the two odd cycles

Because `H` is a tree, adding one edge creates exactly one cycle. Hence

```math
C_{ad}-ad=P_H(a,d),
\qquad
C_{bc}-bc=P_H(b,c),
\tag{5.1}
```

where `P_H(x,y)` denotes the unique tree path in `H` joining `x` to `y`.

The intersection of two simple paths in a tree is empty, a single vertex, or another simple path. Define

```math
J:=P_H(a,d)\cap P_H(b,c).
\tag{5.2}
```

This is exactly PR.5 after the added short edges are removed.

---

## 6. Every KKT-face edge lies on the common path

Take an actual diameter edge

```math
h\in E(H)
```
that does not lie on `C_ad`.

In the maximal convex thrackle `T_ad`, every edge outside the unique odd cycle is a direct pendant edge incident to a degree-one vertex. Since the added edge `ad` itself lies on the cycle, that pendant leaf vertex is not created by the added edge and remains degree one after `ad` is removed. Thus `h` is a full-`H` leaf edge.

LF then gives

```math
\beta_h(s)>0
\qquad\text{for every }s\in\mathcal S.
\tag{6.1}
```

The same argument with `T_bc` applies to every edge outside `C_bc`.

Therefore an edge whose beta coordinate can vanish at a KKT boundary stress must lie on **both** odd cycles:

```math
\boxed{
\{h\in H:\exists s\in\partial\mathcal S,\ \beta_h(s)=0\}
\subseteq E(J).
}
\tag{6.2}
```

This is stronger than the general LF core localization because P1 supplies two canonical maximal completions rather than one.

Since `dim S=1`, LF requires at least two distinct diameter-coordinate facets. Hence at least two distinct edges of `J` can vanish, and in particular

```math
|E(J)|\ge2.
```

This proves PR.6. `square`

---

## 7. Resulting full-tree shape

Every edge of `H` outside `J` is absent from at least one of `C_ad,C_bc`. Section 6 therefore shows that every such edge is incident to a full-`H` leaf.

Thus the entire nonleaf-nonleaf core of the P1 diameter tree is contained in the one common path `J`. The full diameter tree has the form

```text
common path J
+ direct diameter leaves attached to vertices of J
+ possibly leaf edges attached at the two path ends.
```

No branch of length two can leave `J`: its first edge would not itself be a full-H leaf.

So P1 is not an arbitrary convex-thrackle tree. It is a double-completion caterpillar with a single common path carrying all KKT support degeneration.

---

## 8. Relation to SC and the P1 Littlewood equation

SC obtains the same P1 geometry from the sign side. Splitting the merged length-two K-edge into the two collinear unit summand steps gives opposite signs, so those two primal side vectors cancel. The remaining `q-2` side vectors must close and produce the Littlewood equation

```math
P(e^{i\delta})=0,
\qquad
\deg P=q-3.
```

PR identifies the geometric meaning of that cancellation: the canceled primal vectors are the two unit sides of the exact rectangle, while the two possible intermediate support states are its two long sides of length `sqrt(D^2-1)`.

Thus the arithmetic SC obstruction and the mechanical LF/TC obstruction now describe the same parallel-tie rectangle.

---

## 9. Regression audit

### Two short antipodal pairs

P1 has no off-circle **vertices of `F-F`**, but it does have the two short vertex-vertex antipodal pairs `ad,bc`. They map to the same interior point of the merged K-edge rather than to K vertices. This is consistent with AD's count.

### Both completions at once

`ad` and `bc` are disjoint and do not belong to one common thrackle. The theorem does not add both simultaneously. It constructs two separate maximal completions `H+ad` and `H+bc`.

### Common cycle intersection

The two cycles need not coincide. Their tree-path intersection `J` may be a proper subpath. PR uses only that every zeroable edge must be on both cycles.

### Rectangle vertices need not be consecutive as four vertices

Only `ab` and `cd` are hull sides. The boundary arcs from `b` to `c` and from `d` to `a` may contain many other shell vertices. The rectangle is formed by four selected hull vertices, not asserted to be a four-edge face of `F`.

---

## 10. Next theorem

P1 now has two independent finite descriptions:

1. **arithmetic:** the SC Littlewood root at the fixed P1 angle;
2. **mechanical:** a unit-width rectangle whose diameter tree is a caterpillar with all KKT-face coordinates confined to a common twin-cycle path `J` of length at least two.

The next high-value attack is to combine the two.

The sign-change states corresponding to edges of `J` are the only possible endpoint-zero diameter rows. TC/IB/WM applied to two distinct such edges give two four-block body-bar cuts of the same common path. Their transition contact lines are drawn from the two long boundary arcs of the P1 rectangle. The P1 reflection geometry should make the two WM cofactor systems explicitly comparable.

A second route is arithmetic: P1 geometry gives, with `m=q-2`,

```math
T_m(\cos\delta)+4\cos\delta-3=0.
```

SC would force `cos delta` to have algebraic degree at most `(m-1)/2`. Exact factorization experiments suggest the physical root has degree `m` except for a removable linear factor when `6|m`, but that pattern is not yet used as a theorem.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P1 parallel sides ab and cd have vectors t and -t, |t|=1. The merged length-2 edge
of K=F-F is [a-c,b-d]. P1 has all K vertices on the radius-D circle, so
  |a-c|=|b-d|=D.
Since b=a+t and d=c-t, a+c=b+d: a,b,c,d form a parallelogram. Equal diagonals make
it a rectangle. Hence
  |a-d|=|b-c|=sqrt(D^2-1),
with ad=b-c as directed chords.

The exceptional diameter-direction gap is Delta_2=2asin(1/D); all q-2 other gaps
are delta=2asin(1/(2D)), giving (q-2)delta+Delta_2=pi.

Split the merged Minkowski edge in either summand order:
  a-c -> b-c -> b-d,
or
  a-c -> a-d -> b-d.
Each refined antipodal list is a q-edge convex thrackle, so both H+bc and H+ad are
maximal odd-cycle-plus-leaves completions.

Let J=P_H(a,d) intersect P_H(b,c). Any H-edge outside either completion cycle is a
full-H leaf edge, hence LF freezes its beta coefficient. Therefore every KKT-face edge
lies in J. The 1D KKT polytope needs two distinct coordinate facets, so |E(J)|>=2.
Thus the entire zeroable diameter core of P1 is one common twin-completion path.

Next: combine two TC/WM endpoint cuts on J with the rectangle/reflection geometry, or
prove the SC fixed-angle Littlewood root impossible arithmetically.
```
