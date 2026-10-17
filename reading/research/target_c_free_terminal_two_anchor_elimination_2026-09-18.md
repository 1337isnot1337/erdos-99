> Generated reading edition · [exact source](../../research/target_c_free_terminal_two_anchor_elimination_2026-09-18.md) · source SHA-256 `2d23cc935b031b60230fd716cfb8601e102988f3108ea08136564a08b6681d4b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C-II — two-anchor elimination either integrates the full train flex or leaves an internal 3-core

**Date:** 2026-09-18  
**Status:** proof-only structural reduction; theorem-state authority unchanged  
**Scope:** canonical full-core stopped-train system; terminal FREE application stated at the end  
**Depends on:** complete stopped-train decomposition; strict convexity of bounded nonquadrilateral contact faces; exact train-angle closure representation; bounded-face endpoint-pair simplicity; canonical mixed rigidity for the diameter-locking consequence  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The outer-star theorem uses only trains which terminate on the actual outer face. There
is a stronger exact mechanism when those outer anchors can be propagated through the
bounded-face transport graph.

A bounded exceptional face can be solved for two train-angle variables whenever those
two terminal train directions are nonparallel. If the two pivot trains go to the outer
face or to faces solved earlier, the resulting global pivot Jacobian is block upper
triangular. Hence a complete elimination order integrates **all** remaining train
angles into a finite exact contact-flex manifold.

This gives an exact dichotomy:

1. the elimination reaches every bounded exceptional face, in which case the contact
   realization space contains a smooth train-angle manifold of dimension `T-2f`, and
   its non-Euclidean dimension is exactly
   ```math
   T-2f-1=(q-k)-1=h-s_Z-1;
   
   ```
2. or the process stalls on a nonempty induced set `U` of bounded exceptional faces in
   which every face has at least three B--B transport neighbors inside `U`, while all
   trains from that face to the outer/solved side lie in at most one projective
   direction.

Thus failure to integrate essentially the entire contact-flex space now has a concrete
finite witness: an internally 3-valent exceptional-face transport core shielded from
the outer anchors by locally collinear boundary trains.

---

## 1. The endpoint transport graph with direction labels

Let `O` denote the actual outer face. Let

```math
\mathcal F=\{F_1,\ldots,F_f\}
```

be the bounded nonquadrilateral contact faces. Every complete stopped train is one
edge of the endpoint transport multigraph on

```math
\{O\}\cup\mathcal F.
```

A train terminating on a bounded face `F` uses one side of that strictly convex unit
polygon. Label the corresponding transport incidence by the projective direction of
that side.

Bounded transport vertices have no loops. The hostile-audited bounded-face endpoint
fan theorem also excludes repeated transport edges between the same pair of bounded
faces. Thus the B--B part is a simple graph, although this simplicity is needed only
for the final `|U|>=4` observation.

The total train count is

```math
\boxed{
T={b+Q\over2}+2f=h-s_Z+2f.
}
\tag{1.1}
```

---

## 2. Two-anchor activation process

Start with no bounded face active. Repeatedly activate a currently inactive bounded
face `F` if it has two incident transport edges

```math
\tau_1,\tau_2
```

such that

1. the other endpoint of each `tau_i` is either `O` or an already active bounded
   face; and
2. the two side directions of `tau_1,\tau_2` at `F` are nonparallel.

When `F` is activated, record those two train-angle variables as its two **pivot
variables**.

A pivot train is never recorded twice. If it joins `F` to an earlier active face, it
was not eligible as a pivot for that earlier face at the time the earlier face was
activated, because its other endpoint `F` was then inactive. A P--O pivot has only one
bounded endpoint.

Suppose the process activates all bounded faces, in the order

```math
F_1,F_2,\ldots,F_f.
\tag{2.1}
```

For each `F_i`, write its two chosen pivot angles as

```math
\theta_{i,1},\theta_{i,2}.
```

---

## 3. The pivot Jacobian is block upper triangular

Let

```math
\Psi:(\mathbb R/2\pi\mathbb Z)^T\longrightarrow\mathbb R^{2f}
```

be the exact bounded-exceptional-face closure map in train-angle coordinates. The
`F_i` block is the oriented vector sum of the unit side vectors of `F_i` after each
train direction is rotated by its angle. Strict-rhombus closure equations are omitted
because they vanish identically in train-angle coordinates.

At the canonical placement, the derivative of the `F_i` block with respect to its two
pivot variables is, up to occurrence signs,

```math
B_i=
\begin{bmatrix}
Ju_{i,1}&Ju_{i,2}
\end{bmatrix},
\tag{3.1}
```

where the two unit directions are nonparallel. Hence

```math
\det B_i\ne0.
\tag{3.2}
```

Order the `2f` closure rows by `F_1,...,F_f` and the `2f` pivot columns in the same
activation order. A pivot train assigned to `F_i` either goes to `O`, in which case
its column occurs only in the `F_i` closure block, or joins `F_i` to some `F_j` with
`j<i`, in which case its column occurs only in the `F_i` and `F_j` blocks.

Therefore the derivative submatrix on the pivot columns is block upper triangular:
all entries below the diagonal `2x2` block `B_i` vanish. Its determinant is

```math
\prod_{i=1}^f\det B_i\ne0.
\tag{3.3}
```

Consequently

```math
\boxed{
\operatorname{rank}D\Psi=2f.
}
\tag{3.4}
```

In particular the exact closure-corank identity forces

```math
\boxed{\sigma_C=0}
\tag{3.5}
```

whenever a complete two-anchor activation order exists.

---

## 4. Full nonlinear integration by the implicit-function theorem

Treat the `2f` pivot angles as dependent variables and the other `T-2f` train angles
as free variables. By (3.3), the implicit-function theorem solves all pivot angles
smoothly as functions of the free angles in a neighborhood of the canonical
placement. Therefore

```math
\Psi^{-1}(0)
```

contains a smooth local manifold of train-angle dimension exactly

```math
\boxed{T-2f.}
\tag{4.1}
```

Every strict rhombus closes identically under arbitrary train angles. Exact closure of
all bounded exceptional faces therefore gives closure of every graph cycle. Fixing one
core vertex integrates the resulting unit edge vectors to an exact finite
contact-preserving realization. Finite strict noncontact slack, including pairs to
contact-isolated source points held fixed, preserves the unit-separation inequalities
in a sufficiently small neighborhood.

The train-angle manifold contains the one-dimensional global-rotation direction.
After quotienting that direction, its non-Euclidean dimension is

```math
\boxed{
 m_{\rm full}=T-2f-1=h-s_Z-1=(q-k)-1.
}
\tag{4.2}
```

This agrees with the exact contact-flex dimension formula because (3.5) gives
`sigma_C=0`.

Applying the existing diameter-locking theorem to this manifold gives a matching to
`m_full` pairwise distinct actual diameter bars and at least `m_full` positive and
`m_full` negative derivative incidences. Since

```math
h=(q-k)+s_Z,
```

the matching misses at most `s_Z+1` actual diameter bars.

---

## 5. If activation stalls, the residual face set is an internal 3-core

Now suppose the activation process is run to maximality and leaves a nonempty set

```math
U\subset\mathcal F
```

of inactive bounded exceptional faces.

Fix `F in U`. By maximality, the train directions at `F` of all transport edges from
`F` to

```math
O\cup(\mathcal F\setminus U)
```

span at most one projective direction. Otherwise two nonparallel such edges would
activate `F`.

Because `F` is a strictly convex polygon, at most two of its sides can lie in one
projective direction. Therefore

```math
\boxed{
\deg_{\rm out}(F;U)\le2.
}
\tag{5.1}
```

Every bounded nonquadrilateral contact face has contact degree at least five, and its
transport degree equals that contact degree. Hence

```math
\boxed{
\deg_U(F)\ge3.
}
\tag{5.2}
```

Thus the B--B transport graph induced by `U` has minimum degree at least three. Since
the B--B graph is simple,

```math
\boxed{|U|\ge4}
\tag{5.3}
```

and

```math
\boxed{|E(U)|\ge{3\over2}|U|.}
\tag{5.4}
```

More importantly, every residual face is shielded from the already solved/outer side
by at most two terminal trains, and if there are two then they are projectively
parallel at that face.

This is an exact obstruction, not a density statement.

---

## 6. Terminal FREE application

On a terminal full-core FREE sequence the new correlated theorem gives

```math
\liminf {q-k\over D}
\ge1.960302849540479\ldots .
\tag{6.1}
```

Therefore a complete two-anchor activation order would produce an exact
contact-preserving manifold with

```math
\boxed{
\liminf {m_{\rm full}\over D}
\ge1.960302849540479\ldots .
}
\tag{6.2}
```

The remaining active-diameter system would have to positively lock essentially this
entire manifold, with a matching to the same linear number of distinct actual diameter
bars.

If the activation does not complete, the terminal survivor contains the residual
3-core from Section 5. That residual object is now the concrete next target: use its
minimum B--B degree three together with the locally collinear outer/solved boundary
trains to obtain either a new train-angle elimination step, a pure-contact stress
payment, or a source-preserving diameter descent.

The `0.791663...D` outer-star theorem remains unconditional in the live
`epsilon=0.00710` window. The present theorem is a sharper conditional route that
identifies exactly what must prevent the much larger `~1.9603D` manifold from
integrating.

No theorem-state file is changed.

**Disposition:** proved two-anchor block elimination, full nonlinear integration when
the activation reaches all bounded faces, and the exact internal-3-core obstruction
when it stalls. C-II remains open.
