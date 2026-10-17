> Generated reading edition · [exact source](../../research/target_c_near_mantel_atomic_endpoint_exclusion.md) · source SHA-256 `55a81e1dca5ca16c5560c61aeaf217c3728377da764a811fa5f8a69be8e70211`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8888f63de3cbda07a28d4033d825ae02f326ff4d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_near_mantel_atomic_endpoint_exclusion.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4a04178ba3382774d6d5ba10b4571c9001a3b2cd0c11e36aa2831f2a7cf4c620"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — near-Mantel atomic endpoint exclusion

**Date:** 2026-09-12  
**Lifecycle:** proof-only research candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note stacks on the audited-working Target C structural omnibus §§142–146. It
excludes the exact lower endpoint of §146 by combining the equality case of the
phase-atom/Mantel argument with a new **near-complete signed-monotone train theorem**.
No exact biclique extraction is required.

Put

$$
\Delta_2={\pi\over2\sqrt3},
\qquad s_0:=\sqrt{\Delta_2},
\qquad
C_{146}:={4\over9}(\pi+s_0)
=1.8195135379794445\ldots .
$$

For the post-ZF positive-contact core use the audited-working notation
`q,h,d_H,s_Z,k=d_H+s_Z,f,Q,T`, where `T` is the complete stopped-train count.
Define the §146 normalized quantity

$$
\Xi_D:={1\over D}\left(h-{d_H\over9}-{10s_Z\over9}\right)
={1\over D}\left(q-{10k\over9}\right).
\tag{NM.1}
$$

Audited-working §146 gives

$$
\liminf \Xi_D\ge C_{146}.
\tag{NM.2}
$$

The new theorem is:

$$
\boxed{
\text{No Type-II sequence can satisfy }\Xi_D\to C_{146}.
}
\tag{NM.3}
$$

Consequently, by the usual diagonal argument, there is an absolute
`epsilon_NM>0` such that every sufficiently large Type-II survivor in the scope of
§§142–146 satisfies

$$
\boxed{
\Xi_D\ge C_{146}+\epsilon_{NM}.
}
\tag{NM.4}
$$

The constant is not made explicit here. The proof has a fixed geometric margin, but a
numerical `epsilon_NM` would also require quantitative versions of the phase-measure
and Mantel-stability compactness steps.

---

## 1. Equality in §146 forces equality in the phase-atom chain

Assume for contradiction that a Type-II sequence satisfies

$$
\Xi_D\to C_{146}.
\tag{NM.5}
$$

Pass to a subsequence on which

$$
{k\over D}\to\kappa.
$$

Write

$$
t_D={q-k\over D}.
$$

Since `Xi_D=t_D-k/(9D)`, (NM.5) gives

$$
t_D\to C_{146}+{\kappa\over9},
\qquad
{q\over D}\to C_{146}+{10\kappa\over9}.
\tag{NM.6}
$$

Audited-working §146.2, rewritten with `t=(q-k)/D`, gives

$$
\liminf {f\over D}
\ge
s_0-{t\over4}+{\kappa\over4}.
\tag{NM.7}
$$

The exact outer-walk ledger used in §146 gives

$$
\limsup {Q\over D}\le2t-\pi.
\tag{NM.8}
$$

Define

$$
F_0:=s_0-{C_{146}\over4}=2C_{146}-\pi
=0.497434422369096\ldots .
$$

Substitution of (NM.6) into (NM.7)–(NM.8) yields

$$
\liminf {f\over D}\ge F_0+{2\kappa\over9},
\qquad
\limsup {Q\over D}\le F_0+{2\kappa\over9}.
$$

Because every bounded nonquadrilateral face contributes at least one unit to `Q`,
`f<=Q`. Hence both inequalities are equalities:

$$
{f\over D},{Q\over D}
\to F_0+{2\kappa\over9}.
\tag{NM.9}
$$

In particular `Q-f=o(D)`, so all but `o(D)` bounded nonquadrilateral faces are
pentagons. This pentagon conclusion is not needed for the contradiction below, but it
is a useful endpoint diagnostic.

Audited-working §142.4 gives the exact train ledger

$$
T=q+2f-k.
\tag{NM.10}
$$

Combining (NM.6), (NM.9), and (NM.10),

$$
{T-q/2\over D}\to2s_0.
\tag{NM.11}
$$

Now pass to the phase-measure subsequence used in §142.3–142.4. Write

$$
{T\over D}\to x,
\qquad
{q\over T}\to y,
$$

and let `rho` be the total atomic mass of the limiting projective train-phase measure.
Audited-working §142 proves

$$
2s_0\le x\rho,
\tag{NM.12}
$$

and

$$
y\le2(1-\rho).
\tag{NM.13}
$$

Equation (NM.13) gives

$$
x\rho\le x\left(1-{y\over2}\right)
={T-q/2\over D}+o(1).
$$

Together with (NM.11)–(NM.12),

$$
\boxed{x\rho=2s_0.}
\tag{NM.14}
$$

Thus the weighted-Mantel bound in §142.5 is also saturated:

$$
{\Delta_2\over x^2}={\rho^2\over4}.
\tag{NM.15}
$$

The endpoint therefore contains

$$
\boxed{(2s_0+o(1))D}
$$

phase-atomic trains carrying

$$
\boxed{(\Delta_2-o(1))D^2}
$$

actual strict-rhombus crossings.

The last sentence is the equality extraction from the proof of §142.5. For
completeness: the normalized crossing measures there are supported, in the limit, on
projective phase separation `pi/3`; they are dominated by the product phase measure;
and the product measure charges that exact relation only through atoms. Exhaust the
atomic measure by finitely many atoms and then shrink disjoint neighborhoods of those
atoms. If a fixed positive normalized crossing mass remained outside every such
exhaustion, the final weighted-Mantel inequality would be strict. Hence a diagonal
choice of shrinking atomic neighborhoods gives an induced train graph `G_D` with

$$
n_D=(2s_0+o(1))D,
\qquad
e(G_D)=(\Delta_2-o(1))D^2
={n_D^2\over4}-o(D^2).
\tag{NM.16}
$$

`G_D` is simple and triangle-free by audited-working §142.2.

---

## 2. Self-contained near-Mantel stability

We need only the elementary stability form of Mantel.

### Lemma NM.1 — near-Mantel triangle-free graphs are nearly complete bipartite

If a triangle-free graph has `n` vertices and

$$
e={n^2\over4}-o(n^2),
$$

then there are disjoint independent sets `U,V` such that

$$
|U|=|V|={n\over2}+o(n),
\qquad
|V(G)\setminus(U\cup V)|=o(n),
$$

and only `o(n^2)` pairs in `U x V` are nonedges.

#### Proof

For every edge `uv`, triangle-freeness gives

$$
d(u)+d(v)\le n.
$$

Summing over edges,

$$
\sum_wd(w)^2\le ne.
$$

Cauchy gives

$$
\sum_wd(w)^2\ge{(2e)^2\over n}.
$$

Since `e=n^2/4-o(n^2)`, the edge-weighted average of `d(u)+d(v)` is
`n-o(n)`. Hence some edge `uv` satisfies

$$
d(u)+d(v)=n-o(n).
$$

Put

$$
U=N(u),\qquad V=N(v).
$$

The two sets are disjoint and each is independent. They cover `n-o(n)` vertices. All
edges not between `U,V` are incident with the `o(n)` uncovered vertices, hence number
`o(n^2)`. Therefore

$$
e(U,V)={n^2\over4}-o(n^2).
$$

Since `|U|+|V|=n-o(n)`, the product bound
`e(U,V)<=|U||V|` forces

$$
|U|=|V|={n\over2}+o(n),
$$

and then

$$
|U||V|-e(U,V)=o(n^2).
$$

This proves the lemma. `square`

Apply the lemma to (NM.16). After discarding `o(D)` trains we have two independent
train shores `U_D,V_D`, each of size

$$
(s_0+o(1))D,
\tag{NM.17}
$$

with only `o(D^2)` missing cross-shore crossings.

---

## 3. Near completeness collapses the atomic support to one phase star

Pass to limiting phase measures on the two stability shores. A positive-mass phase
atom cannot occur on both shores: two trains in sufficiently small neighborhoods of
the same projective direction cannot cross, whereas the `U_D x V_D` graph is missing
only `o(D^2)` pairs.

Likewise, if an atom `phi` on one shore and an atom `psi` on the other shore have
projective circular separation different from `pi/3`, they cannot form a positive
quadratic near-complete block. If the separation is below `pi/3`, strict-rhombus
geometry forbids crossings. If it is above `pi/3` by a fixed amount, a quadratic block
of such crossings would contradict the `o(D^2)` population of fixed-positive angular
rhombus defect used in §142.3. Thus every positive-mass cross-shore atom pair satisfies

$$
\operatorname{dist}_{\mathbb R/\pi\mathbb Z}(\phi,\psi)={\pi\over3}.
\tag{NM.18}
$$

The graph on the projective direction circle joining points at distance `pi/3` is a
disjoint union of 3-cycles: the orbit of `phi` is

$$
\{\phi,\phi+\pi/3,\phi+2\pi/3\}\pmod\pi.
$$

It contains no `K_{2,2}`. Since every positive-mass atom on one stability shore must be
related by (NM.18) to every positive-mass atom on the other shore, one of the two
supports is therefore a singleton and the other contains at most its two phase
neighbors.

Relabel the shores so the singleton is the **central** atom. From (NM.17), its train
population is

$$
\boxed{(s_0+o(1))D.}
\tag{NM.19}
$$

The opposite shore has total population `(s_0+o(1))D` on at most two neighboring
phase atoms. One neighbor therefore carries at least

$$
\boxed{(s_0/2-o(1))D.}
\tag{NM.20}
$$

Choose that neighbor. By a diagonal shrinking-neighborhood choice, we obtain two
physical train families `A_D,B_D` such that

$$
|A_D|=(s_0+o(1))D,
\qquad
|B_D|\ge(s_0/2-o(1))D,
\tag{NM.21}
$$

all projective directions in each family lie in an `o(1)` neighborhood of one fixed
phase direction, the two limiting directions differ by `pi/3`, and

$$
\boxed{
|A_D||B_D|-e(A_D,B_D)=o(D^2).
}
\tag{NM.22}
$$

Same-family trains are pairwise disjoint for large `D`, because their projective
direction spread is less than `pi/3` while every strict-rhombus crossing has angle
strictly greater than `pi/3`.

---

## 4. Near-complete signed monotone train pairs already force large diameter

The following lemma is the geometric step that removes the need for an exact biclique.

### Lemma NM.2 — near-complete coherent train pair diameter bound

Let `A_D,B_D` be two train families in one source of diameter `D`, with

$$
|A_D|,|B_D|=\Theta(D),
$$

such that

1. trains are pairwise disjoint inside each family;
2. every two trains cross at most once;
3. family directions lie in `rho_D`-neighborhoods of projective directions separated
   by `pi/3`, where `rho_D->0`;
4. all actual cross-family crossings have the corresponding common orientation; and
5. the number of missing `A_D x B_D` crossing pairs is `o(D^2)`.

Then

$$
\boxed{
D\ge\left({\sqrt3\over2}-o(1)\right)
\bigl(|A_D|+|B_D|\bigr).
}
\tag{NM.23}
$$

#### Proof

Choose consistent lifts of the two contact-direction families near `alpha_0` and
`alpha_0+pi/3`. The canonical train orientation puts the elementary midpoint-path
displacements of the first family in the open cones

$$
(\alpha+\pi/3,\alpha+2\pi/3),
$$

and those of the second family, in its canonical orientation, in the adjacent cones

$$
(\beta+\pi/3,\beta+2\pi/3).
$$

Because the combined reduced-phase width is `o(1)<pi/3`, exactly the common-cone
argument used in audited-working §145 gives one linear coordinate `X` that is strictly
increasing along every canonically oriented selected train. At an actual cross-family
rhombus the strict angle is `pi/3+o(1)` and has one common sign. Thus, in `(X,Y)`
coordinates, every crossing has the same signed graph crossing.

Let

$$
\epsilon_D
={|A_D||B_D|-e(A_D,B_D)\over |A_D||B_D|}
\to0.
$$

Delete every `A` train missing more than `sqrt(epsilon_D)|B_D|` opposite trains and
every `B` train missing more than `sqrt(epsilon_D)|A_D|` opposite trains. Markov's
inequality deletes only `o(D)` trains. In the retained families every train misses
`o(D)` opposite trains.

For two retained `B` trains there is a common retained `A` neighbor. The pairwise
argument in canonical Lemma 76.1 applies verbatim to those three `X`-monotone curves:
the order in which the common `A` train meets the two `B` trains depends only on the
pair of `B` trains, not on the chosen common neighbor. For any three retained `B`
trains there is a common retained `A` neighbor once `D` is large, because each misses
`o(D)` of a linear-size shore. Their three pairwise orders are therefore transitive.
Hence the retained `B` family has one global total order, and every retained `A` sees
its neighbors in the restriction of that order. By symmetry the retained `A` family
has one global total order with the analogous property.

Let `B^+` be the maximal retained `B` train. Among its neighbors choose `A^+` maximal
in the global `A` order. Since `B^+` misses only `o(D)` trains, `A^+` is within `o(D)`
of the top of the `A` order. Since `A^+` itself misses only `o(D)` `B` trains and
`B^+` is the global maximum, `B^+` is the last crossing of `A^+` among all its retained
`B` neighbors. Likewise `A^+` is the last crossing of `B^+` among all its retained `A`
neighbors in the canonical orientation.

Follow `A^+` canonically from its first retained `B` crossing to its crossing with
`B^+`. Then follow `B^+` **opposite** to its canonical orientation from `A^+` to its
first retained `A` crossing. The two endpoints are centers of actual source rhombi and
lie in the source convex hull, so their distance is at most `D`.

The first leg contains every retained `B` neighbor of `A^+`; the second contains every
retained `A` neighbor of `B^+`. At selected crossings the corresponding unit contact
vectors project onto the direction halfway between the two limiting contact directions
by

$$
{\sqrt3\over2}-o(1).
$$

Intervening rhombi cannot create a macroscopic negative error. Along an `A` train their
midpoint displacements lie in the canonical `(pi/3,2pi/3)` cone relative to its
contact direction; along the reversed `B` train they lie in the opposite corresponding
cone. Against the midpoint projection direction every such displacement has projection
at least `-O(rho_D)`. A complete train crosses at most `2D/sqrt3` strict rhombi,
because each rhombus increases its transverse coordinate by at least `sqrt3/2` and the
total transverse span is at most `D`. Thus both legs together contribute at worst
`o(D)` negative projection outside the selected crossings.

As in §76, the two path endpoints cost at most two half-vectors. Therefore

$$
D
\ge
\left({\sqrt3\over2}-o(1)\right)
\left(
\deg_{B}(A^+)+\deg_A(B^+)
\right)-o(D).
$$

Both degrees equal the corresponding shore size minus `o(D)`, proving (NM.23).
`square`

---

## 5. The §146 endpoint violates the diameter bound

Apply Lemma NM.2 to the families in (NM.21)–(NM.22). Then

$$
D
\ge
\left({\sqrt3\over2}-o(1)\right)
\left({3s_0\over2}-o(1)\right)D.
$$

But

$$
{3\sqrt3\over4}s_0
={3\sqrt3\over4}
\sqrt{\frac\pi{2\sqrt3}}
=1.237090624640176\ldots>1.
\tag{NM.24}
$$

For sufficiently large `D` this says `D>(1+c)D` for a fixed `c>0`, a contradiction.
This proves (NM.3).

If no uniform positive gap in (NM.4) existed, one could choose a sequence of
sufficiently large Type-II survivors with

$$
C_{146}\le\Xi_D<C_{146}+1/j
$$

at the `j`-th term. That sequence would satisfy (NM.5), already excluded. Hence
(NM.4) follows.

---

## 6. Scope and frontier effect

- The theorem is **proof-only** and depends on audited-working §§142–146; it does not
  promote theorem authority beyond canonical audit.46 / Section 123.
- Every source point is retained. Contact-isolated points never enter the Section-57
  affine-kernel statement.
- No pure-disk hypothesis is used. Defect faces, holes, bridges, and stopped-train
  endpoints are allowed. The new Lemma NM.2 needs only the actual train arcs and the
  full source diameter.
- No exact complete grid is extracted. This is important: the endpoint is killed by
  near-completeness plus signed train order, so the historical sliding-interval
  regression does not apply.
- The argument excludes the **sharp scalar endpoint** of the audited §146 chain. It
  does not give an explicit numerical improvement because the stability steps are
  compactness-based.
- The macroscopic inactive-container branch is untouched.

The full-core Type-II frontier is therefore strictly above the audited §146 lower
surface:

$$
h-{d_H\over9}-{10s_Z\over9}
\ge(C_{146}+\epsilon_{NM})D
$$

for some absolute `epsilon_NM>0`, once this proof-only theorem is independently audited.
C-II remains open.
