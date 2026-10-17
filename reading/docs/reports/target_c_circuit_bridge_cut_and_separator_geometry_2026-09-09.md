> Generated reading edition · [exact source](../../../docs/reports/target_c_circuit_bridge_cut_and_separator_geometry_2026-09-09.md) · source SHA-256 `24c5e1e271948f8c3dd196bc9262431377804816d33b7f76bd1bcbe49cc2f29c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EEE27731BABC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — circuit bridge-cut ledger and noncollinear separator theorem

**Date:** 2026-09-09  
**Repository base:** current PR #143 branch after MC/TF/BM  
**Run type:** exact structural sharpening  
**Target:** Target C C-II / `s_Z=0` circuit phase and mixed separators  
**Depends on:** MC, ZF, U1  
**LEVEL I STATUS:** STILL OPEN

MC proves that the post-ZF mixed equality support

```math
G_M=C\cup H
```

is 3-vertex-connected.  The same reflection argument actually gives a broader geometric statement: **no vertex separator of `G_M` can lie on one line**, regardless of its cardinality.

In the exact `s_Z=0` phase, MC also proves that `G_M` is a circuit of the actual planar rigidity matroid.  Applying circuit sparsity across a contact-bridge cut gives an exact bypass ledger.  If both bridge sides contain at least two vertices and `t` actual diameter edges cross the cut, then

```math
\boxed{
t=3+\delta_A+\delta_B,
}
\tag{CS.1}
```

where `delta_A,delta_B` are the ordinary `(2,3)` sparsity deficits of the two induced mixed subframeworks.  Thus three diameter bypasses is the absolute circuit minimum; equality means both sides are Laman-tight.

---

## 1. No collinear vertex separator

Let `S subset V(G_M)` be a vertex separator: `G_M-S` has at least two nonempty connected components.  Assume `|S|>=2` and that all points

```math
\{p_s:s\in S\}
```

lie on one line `ell`.

### Theorem CS.1 — separator noncollinearity

No such `S` exists. Equivalently, every vertex separator of `G_M` with at least two vertices affinely spans the plane.

### Proof

Let the components of `G_M-S` be `K_1,...,K_m`, with `m>=2`.

Suppose first that two distinct components, say `K_1,K_2`, each contain a point off `ell`. Reflect only the vertices of `K_1` across `ell`, fixing every other vertex.

Every mixed bar length is preserved:

- edges internal to `K_1` are reflected rigidly;
- any edge from `K_1` to the rest ends in `S`, whose points lie on and are fixed by `ell`;
- there are no edges from `K_1` to another component of `G_M-S`;
- every other vertex is fixed.

Thus the new realization has exactly the same `C union H` bar lengths. U1 universal rigidity says it must be congruent to the original.

But the two realizations agree pointwise on two distinct separator vertices and on an off-line vertex of `K_2`. Those three fixed points are noncollinear, so the only Euclidean isometry fixing them is the identity. An off-line point of `K_1` moved under the partial reflection. Contradiction.

Therefore at most one component of `G_M-S` contains an off-line point.

The full post-ZF framework spans the plane, so at least one component contains an off-line point. Since `m>=2`, some other component `K_j` lies entirely on `ell`.

Give the vertices of `K_j` arbitrary nonzero velocities perpendicular to `ell`, and give every other vertex velocity zero. More explicitly, choose a unit normal `n` to `ell` and scalars `eta_x`, not all zero, and put

```math
v_x=\eta_x n\quad(x\in K_j),
\qquad v_x=0\quad(x\notin K_j).
```

Every mixed edge incident to `K_j` has both geometric endpoints on `ell`: internal edges do by collinearity, and every edge leaving the component ends in `S`. Hence every such bar vector is parallel to `ell`, while its velocity difference is perpendicular to `ell`. All first variations vanish. Edges disjoint from `K_j` have zero endpoint velocities.

This is a nonzero infinitesimal flex. It is not a global Euclidean infinitesimal motion because at least two distinct separator points are fixed; a planar infinitesimal rigid motion fixing two distinct points is zero. This contradicts ZF.

Hence no collinear separator exists. `square`

For `|S|=2` this contains MC's two-separator contradiction. The new content begins at three- and higher-vertex separators.

---

## 2. Geometry of minimal mixed boundaries of contact regions

Let `A` be a proper nonempty vertex set and suppose every mixed edge from `A` to `V\A` is incident, on the `A` side, to a set

```math
\partial_M A\subseteq A.
```

If `A\setminus\partial_M A` is nonempty, then deleting `partial_M A` disconnects a surviving vertex of `A` from the complement. Therefore `partial_M A` is a vertex separator.

CS.1 gives:

### Corollary CS.2

If `A\setminus\partial_M A` is nonempty and `|partial_M A|>=2`, then the points of `partial_M A` are not collinear.

In particular, in BM's bridge-side setting, if a bridge side with at least four vertices has the minimum possible three mixed boundary vertices, those three boundary points form a nondegenerate triangle.

No uniform area lower bound for that triangle follows: the separator can be arbitrarily close to collinear without violating CS.1.

---

## 3. Enter the exact `s_Z=0` circuit phase

Now assume

```math
\boxed{s_Z=0.}
\tag{CS.2}
```

ZF gives

```math
\operatorname{rank}R(G_M,p)=2v-3,
```

while

```math
|E(G_M)|=e+h=2v-2.
```

The row-dependence space is therefore one-dimensional. The relative-interior KKT dependence has nonzero coefficient on every actual mixed edge. As proved in MC, every proper edge subset is independent.

Thus for every proper vertex subset `W` with `|W|>=2`,

```math
\boxed{|E(G_M[W])|\le2|W|-3.}
\tag{CS.3}
```

---

## 4. Exact contact-bridge bypass ledger in a rigidity circuit

Let `uv` be a contact bridge. Removing it partitions the full vertex set as

```math
V=A\sqcup B,
\qquad u\in A,
\qquad v\in B.
\tag{CS.4}
```

Let

```math
t:=|E_H(A,B)|
\tag{CS.5}
```

be the number of actual diameter edges crossing the same cut. The unique crossing contact edge is `uv`.

Assume first

```math
|A|\ge2,
\qquad |B|\ge2.
\tag{CS.6}
```

Define the induced mixed-edge counts

```math
m_A:=|E(G_M[A])|,
\qquad
m_B:=|E(G_M[B])|,
```

and their nonnegative circuit-sparsity deficits

```math
\boxed{
\delta_A:=2|A|-3-m_A\ge0,
\qquad
\delta_B:=2|B|-3-m_B\ge0.
}
\tag{CS.7}
```

The total edge count is

```math
2v-2
=m_A+m_B+1+t.
\tag{CS.8}
```

Insert CS.7 and use `v=|A|+|B|`:

```math
\begin{aligned}
2v-2
&=(2|A|-3-\delta_A)+(2|B|-3-\delta_B)+1+t\\
&=2v-5-\delta_A-\delta_B+t.
\end{aligned}
```

Therefore:

### Theorem CS.3 — exact circuit bridge-cut ledger

```math
\boxed{
t=3+\delta_A+\delta_B.}
\tag{CS.9}
```

Consequences:

```math
\boxed{t\ge3.}
\tag{CS.10}
```

Moreover

```math
t=3
```

if and only if both induced mixed subframeworks are Laman-tight:

```math
m_A=2|A|-3,
\qquad
m_B=2|B|-3.
\tag{CS.11}
```

Thus BM's two vertex-disjoint diameter bypasses are only part of the `s_Z=0` picture: every nonsingleton circuit bridge cut has at least **three** diameter edges in total, and every additional crossing diameter edge is paid exactly by one unit of internal sparsity deficit on one of the two sides.

---

## 5. Singleton bridge side

If `A={u}` is a singleton, then `m_A=0`. Assume `|B|>=2` and define

```math
\delta_B:=2|B|-3-m_B\ge0.
```

Now `v=|B|+1`, and CS.8 becomes

```math
2|B|
=m_B+1+t
=2|B|-3-\delta_B+1+t.
```

Hence

```math
\boxed{t=2+\delta_B.}
\tag{CS.12}
```

In particular a singleton contact leaf has diameter degree at least two, recovering BM/MC. Equality `t=2` occurs exactly when the complementary induced mixed framework is Laman-tight.

The symmetric statement holds when `B` is the singleton side.

---

## 6. Three-separator count in the circuit phase

The same sparsity calculation is useful for a genuine three-vertex separator.

Let

```math
S=\{a,b,c\}
```

separate the remaining vertices into two nonempty sets `A,B`, with no edges between `A` and `B`. Put

```math
V_1=A\cup S,
\qquad
V_2=B\cup S,
```

and let

```math
e_S:=|E(G_M[S])|.
```

Define

```math
\delta_i:=2|V_i|-3-|E(G_M[V_i])|\ge0.
```

Because edges inside `S` are counted in both induced subgraphs,

```math
2v-2
=|E(G_M[V_1])|+|E(G_M[V_2])|-e_S.
```

Since

```math
|V_1|+|V_2|=v+3,
```

substitution gives

```math
\boxed{
\delta_1+\delta_2+e_S=2.
}
\tag{CS.13}
```

Therefore

```math
\boxed{e_S\le2.}
\tag{CS.14}
```

So an `s_Z=0` circuit can never have a three-vertex separator whose three vertices span a mixed triangle. Combined with CS.1, every three-separator is a noncollinear triple spanning at most two mixed edges, and the missing internal edges are paid exactly by the two side deficits in CS.13.

This is a narrow exact 3-sum structure, but it is not empty in abstract rigidity circuits.

---

## 7. Relation to geometric edge types

For `D>2`, a mixed triangle has severe length restrictions:

- one diameter edge plus two unit contacts is impossible by the triangle inequality;
- two diameter edges plus one unit contact are possible only as an isosceles triangle with sides `(D,D,1)`;
- three diameter edges form an equilateral triangle of side `D`.

CS.14 says no three-separator in the `s_Z=0` circuit may realize any of those complete mixed triangles. This does not rule out the circuit phase itself, because a separator can be noncollinear while spanning zero, one, or two mixed edges.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| no collinear vertex separator of any size | proved | U1 partial reflection + ZF transverse flex |
| bridge-side minimum boundary triple is noncollinear | proved | separator corollary |
| circuit bridge ledger `t=3+delta_A+delta_B` | proved | exact edge count + actual row sparsity |
| singleton formula `t=2+delta_B` | proved | same count |
| circuit three-separator ledger `delta_1+delta_2+e_S=2` | proved | inclusion-exclusion + sparsity |
| every three-separator has at most two mixed edges | proved | preceding identity |
| `s_Z=0` circuit phase impossible | not proved | abstract 3-connected circuits with valid 3-separations exist |
| Level I | still open | need geometric use of the exact separator/cut structure |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

U1+ZF imply more than 3-connectivity:
no vertex separator S with |S|>=2 can be collinear. Partial reflection excludes two
off-line separator components; if only one is off-line, any other collinear component
has a transverse infinitesimal flex.

In the exact s_Z=0 phase, G_M is an actual planar-rigidity circuit.
For a contact bridge cut A|B with |A|,|B|>=2, let t be the number of crossing H edges
and
    delta_A=2|A|-3-|E_M(A)|,
    delta_B=2|B|-3-|E_M(B)|.
Then exactly
    t=3+delta_A+delta_B.
So t>=3; equality iff both sides are Laman-tight.
For a singleton side, t=2+delta_other.

For any 3-separator S splitting the circuit into two sides,
    delta_1+delta_2+|E_M(S)|=2,
so S spans at most two mixed edges. Together with separator noncollinearity this gives
a narrow exact 3-sum normal form for the s_Z=0 branch.
```
