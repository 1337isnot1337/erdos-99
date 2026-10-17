> Generated reading edition · [exact source](../../../docs/reports/target_c_tb1_swap_grid_local_immunity_2026-10-01.md) · source SHA-256 `81ca701f65c67b7d025e2efb0acb3e3daa1265aa51dc6b861f4f3db75290f267`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A32CCD49E2C5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- the exact TB1 swap preserves the complete-grid rhombus metric locally

Date: 2026-10-01  
Base branch dependency: 1d12f24de2c377edd420e6a5376dee8b7211ee02  
Status: proof-only; C-II remains open.

## 1. Statement

Work in the fixed-star complete global O--O rectangle on current main and in the
phase-changing TB1 situation of the exact-swap theorem. Let the adjacent trains on
one shore be

$$
\tau_i,\tau_{i+1}
$$

with coherent unit directions $u_i,u_{i+1}$, and let every train
$\sigma$ on the opposite retained shore cross both trains in actual strict rhombi.

Translate the physical middle strip by the exact swap vector

$$
\Delta=u_{i+1}-u_i.
\tag{1}
$$

Then:

1. every contact edge of $\tau_i$ changes from direction $u_i$ to direction
   $u_{i+1}$;
2. every contact edge of $\tau_{i+1}$ changes from direction $u_{i+1}$ to
   direction $u_i$, up to the harmless reversal of edge orientation;
3. every contact edge belonging to a transverse train $\sigma$ is unchanged;
4. for every retained transverse train $\sigma$, the rhombus
   $(\tau_i,\sigma)$ after the swap is congruent to an old rhombus
   $(\tau_{i+1},\sigma)$, and conversely.

In particular, the unordered pair of diagonal lengths of each boundary rhombus is
permuted inside the old complete grid. Therefore

$$
\boxed{
\text{no diagonal of a retained boundary-grid rhombus can be the inactive
near-active witness forced by the ONE-SIGN swap.}
}
\tag{2}
$$

For a pairwise nonadjacent family of $r$ TB1 interfaces inside a complete rectangle
with opposite shore $B$, the $2r|B|$ boundary rhombi are distinct. Thus if
$r=\Theta(D)$ and $|B|=\Theta(D)$, the exact swaps automatically protect a
quadratic family

$$
\boxed{\Theta(D^2)}
\tag{3}
$$

of the most obvious local inactive pairs. Any ONE-SIGN near-active obstruction must
be nonlocal to these retained crossing cells.

No inactive-gap estimate is used.

## 2. One boundary rhombus

Fix a transverse retained train $\sigma$. Let $v$ be either orientation of its
unit contact direction in the rhombus where it crosses $\tau_i$.

Use coordinates for that rhombus

$$
0,\quad u_i,\quad v,\quad u_i+v.
\tag{4}
$$

The proper train cut for $\tau_i$ joins the midpoints of the two opposite
$\tau_i$-edges. Hence the exact middle-strip translation moves the endpoints

$$
u_i,\quad u_i+v
$$

by the same vector $\Delta$, while $0,v$ remain fixed. The transformed vertices
are therefore

$$
0,\quad u_i+\Delta,\quad v,\quad u_i+v+\Delta.
\tag{5}
$$

By (1),

$$
u_i+\Delta=u_{i+1}.
$$

Thus (5) is exactly the unit parallelogram with side directions

$$
u_{i+1},\quad v.
\tag{6}
$$

All transverse $\sigma$-edges remain unchanged because a contact edge belonging to
a different complete stopped train has both endpoints on the same shore of the
$\tau_i$ cut.

The identical argument on the other boundary, using the outside-to-middle vector
$-u_{i+1}$, gives

$$
-u_{i+1}+\Delta=-u_i.
\tag{7}
$$

So the two adjacent train directions are exchanged exactly.

## 3. Congruence with an old crossing cell

Because the retained rectangle is complete, the same transverse train $\sigma$
also crosses $\tau_{i+1}$ in an old actual strict rhombus.

A unit rhombus is determined up to Euclidean congruence by the two projective side
directions. Equivalently, if representatives are $u,v$, its two diagonal lengths
are the unordered pair

$$
\{|u+v|,\ |u-v|\}.
\tag{8}
$$

The transformed $(\tau_i,\sigma)$ cell has projective side directions
$[u_{i+1}],[v]$, exactly those of the old $(\tau_{i+1},\sigma)$ cell.
Consequently their diagonal-length multisets coincide.

Likewise the transformed $(\tau_{i+1},\sigma)$ cell is congruent to the old
$(\tau_i,\sigma)$ cell.

This argument is insensitive to the orientation chosen for $v$: replacing $v$
by $-v$ only exchanges the two numbers in (8).

## 4. The local inactive diagonals remain admissible

Every retained crossing cell is an actual strict rhombus in the original
triangle-free source. Its four sides are unit contacts. Therefore neither diagonal
can have length below one; if the shorter diagonal had length exactly one, it and
two adjacent unit sides would form a forbidden unit equilateral triangle. Hence

$$
\min\{|u+v|,|u-v|\}>1.
\tag{9}
$$

The longer diagonal is $<2$, so for the asymptotic Target-C regime it is far below
the global diameter $D$.

By Section 3, after the exact swap the two diagonal lengths of every retained
boundary rhombus are old diagonal lengths of the neighboring retained rhombus.
Therefore they still satisfy the same strict lower-distance inequality and cannot
become a new diameter pair.

This proves (2).

## 5. Quadratic protected population on a linear TB1 family

Now take a pairwise nonadjacent family of $r$ adjacent interfaces on the same
retained shore. Nonadjacency makes their two boundary-train sets disjoint.

Every one of the $|B|$ trains on the complete transverse shore crosses both
boundary trains of each interface. Hence each selected interface contributes

$$
2|B|
$$

distinct retained strict-rhombus cells, and different selected interfaces contribute
disjoint cells. The exact swap at its tagged interface permutes the two local
rhombus shapes for every transverse train.

Thus the total number of retained boundary cells whose local diagonal constraints
are automatically safe is exactly

$$
2r|B|.
\tag{10}
$$

When the current complete rectangle has $r\ge cD-o(D)$ selected TB1 interfaces and
$|B|\ge c'D-o(D)$,

$$
2r|B|\ge (2cc'-o(1))D^2.
\tag{11}
$$

The ONE-SIGN obstruction supplied by the exact-swap theorem must therefore use a
source pair which is not a diagonal of any of these retained boundary rhombi.

## 6. Frontier effect

The exact-swap fork cannot be dismissed as merely rediscovering the already-dense
population of almost-equilateral rhombus diagonals. The swap exchanges the two
boundary row phases, so the entire complete transverse family sees old strict
rhombus geometry again.

The remaining ONE-SIGN witness is genuinely nonlocal to the protected complete-grid
cells. The next useful step is to classify such near-unit or near-diameter pairs by
their selected-cut support. The TWO-SIGN alternative remains an active-diameter
order problem.

This is analytic proof work only. No computation, verifier, numerical experiment, or
CI result is used.
