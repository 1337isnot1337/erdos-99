> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_shell_local_optimality_2026-09-09.md) · source SHA-256 `f462e80ad6b3208fa13e3adcfe34cf25467b17df20765d3fa95cde28c19fcf3e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AD769136F935","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic force hull is a locally diameter-minimal equilateral polygon

**Date:** 2026-09-09  
**Repository branch:** PR #118 after UFB/ID  
**Run type:** exact local-variational transfer from the full source to its shell  
**Target:** complete cyclic primitive endpoint, all `d_H=0,1,2`  
**Depends on:** UFB `F=conv A`, CY/C-I actual contact graph `C_q`, C65 contact-then-diameter lexicographic normalization  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

UFB closes the population-location gap in the cyclic endpoint: the force hull is the complete source hull. CY and C-I restoration say the only actual unit contacts are the `q` consecutive shell edges, while C65 says no contact-isolated interior point is an actual diameter endpoint.

These finite strict inequalities let any sufficiently small side-preserving deformation of the shell be performed while the `n-q` interior source points are held fixed. Thus full-source global optimality transfers to an exact local optimization property of the equilateral shell itself.

### Theorem SL — shell local diameter minimality

Let

$$
P=(p_0,\ldots,p_{q-1})
$$

be the cyclically ordered force-hull vertices of a sufficiently large cyclic C65 survivor. Then `P` is a local minimizer of diameter among convex equilateral `q`-gons of side length one.

More precisely, there is a neighborhood `U` of `P` in the space of labeled vertex tuples such that every convex equilateral tuple

$$
P'=(p'_0,\ldots,p'_{q-1})\in U,
\qquad |p'_{i+1}-p'_i|=1,
$$

satisfies

$$
\boxed{\operatorname{diam}\{p'_0,\ldots,p'_{q-1}\}\ge D.}
\tag{SL.1}
$$

Since the original shell has diameter `D`, equality holds at `P`.

### Theorem SL+ — lexicographic active-diameter rigidity

In the same neighborhood, suppose `P'` is convex and equilateral, its shell diameter is at most `D`, and no shell pair which was shorter than `D` at `P` becomes a diameter pair at `P'`.

Then no original actual diameter pair may become strictly shorter than `D`.

Equivalently, if

$$
H=\{ij:|p_i-p_j|=D\}
$$

is the full shell diameter graph, there is no sufficiently small admissible shell deformation satisfying

$$
|p'_i-p'_j|\le D\quad(ij\in H),
$$

with strict inequality for at least one `ij in H`, while every non-H shell pair remains `<D`.

Thus C65's diameter-pair minimality transfers to the shell as a local **active-set minimality** condition, not only a first-order KKT statement.

---

## 1. Finite slack to the interior population

Write

$$
Z:=A\setminus V(F).
$$

UFB gives

$$
F=\operatorname{conv}A,
$$

and CY/C-I gives the complete actual unit-contact graph

$$
C(A)=C_q
$$

on the shell vertices. Therefore for every `z in Z` and every distinct source point `a in A`,

$$
|z-a|>1.
\tag{1.1}
$$

C65 also says a contact-isolated point is not an actual diameter endpoint. Hence for every `z in Z` and every `a in A`,

$$
|z-a|<D.
\tag{1.2}
$$

The set of such pairs is finite. Therefore there is a source-dependent positive margin

$$
\boxed{
\eta_Z>0
}
\tag{1.3}
$$

such that simultaneously

$$
|z-a|\ge1+\eta_Z
$$

for every relevant distinct pair involving `z`, and

$$
|z-a|\le D-\eta_Z
$$

for every pair involving an interior point.

No uniform-in-`D` lower bound on `eta_Z` is claimed or needed.

---

## 2. Finite slack among nonadjacent shell pairs

The only shell unit contacts are consecutive cycle edges. Thus every nonadjacent shell pair satisfies

$$
|p_i-p_j|>1.
\tag{2.1}
$$

Among non-diameter shell pairs one also has

$$
|p_i-p_j|<D.
\tag{2.2}
$$

Again finiteness gives a positive source-dependent margin `eta_S` from both inactive constraint levels.

Choose a labeled neighborhood `U` of the shell tuple so small that whenever `P' in U`:

1. every originally nonadjacent shell pair remains farther than one;
2. every originally non-diameter shell pair remains shorter than `D` unless explicitly allowed otherwise;
3. for every fixed interior point `z in Z`, every distance `|z-p'_i|` remains in `(1,D)`.

Such a neighborhood exists by continuity and the finite margins above.

---

## 3. Proof of shell local diameter minimality

Suppose for contradiction that there is a convex equilateral shell tuple

$$
P'\in U
$$

with

$$
\operatorname{diam}P'<D.
\tag{3.1}
$$

Construct a new `n`-point source

$$
A':=Z\cup\{p'_0,\ldots,p'_{q-1}\},
$$

holding every interior point fixed.

By the definition of `U`:

- adjacent shell distances remain exactly one;
- nonadjacent shell distances remain greater than one;
- all distances involving an interior point remain greater than one.

Hence `A'` is unit-separated.

Its pair distances satisfy:

- shell-shell distances are `<D` by (3.1);
- shell-interior distances are `<D` by the neighborhood choice;
- interior-interior distances were already `<D` and are unchanged.

Therefore

$$
\operatorname{diam}A'<D.
$$

But the original source has global minimum diameter

$$
D=D(n).
$$

Contradiction.

Thus every sufficiently small convex equilateral shell deformation has shell diameter at least `D`. This proves SL. `square`

---

## 4. Proof of active-diameter minimality

Now suppose `P' in U` is convex and equilateral and satisfies:

1. every original diameter pair has length at most `D`;
2. at least one original diameter pair has length strictly below `D`;
3. every originally inactive shell pair stays strictly below `D`.

As above form

$$
A'=Z\cup P'.
$$

The neighborhood construction preserves the complete actual contact graph:

$$
C(A')=C_q=C(A).
\tag{4.1}
$$

In particular `A'` remains triangle-free and has the same number `q` of contacts as the contact-minimal C65 source. Hence it is still contact-minimal among global minimizers if its diameter is `D`.

All pair distances in `A'` are at most `D`: inactive shell pairs are `<D`; all interior-involving pairs are `<D`; the old active shell pairs are `<=D`.

Thus

$$
\operatorname{diam}A'\le D.
$$

Global optimality of `D(n)` rules out strict inequality, so

$$
\operatorname{diam}A'=D.
\tag{4.2}
$$

By hypothesis no new shell pair becomes diametral, and no interior point is diametral in the neighborhood. At least one old diameter pair has been lost. Therefore the number of actual diameter pairs of `A'` is strictly smaller than for `A`.

Equation (4.1) says the contact count is unchanged at its lexicographically minimal value. Equation (4.2) says `A'` is another global minimizer. This contradicts C65's secondary choice minimizing the number of actual diameter pairs among the contact-minimal triangle-free global minimizers.

This proves SL+. `square`

---

## 5. Infinitesimal consequence

Let

$$
u=(u_0,\ldots,u_{q-1})
$$

be the velocity of a differentiable convex equilateral shell path through `P`, so each cycle edge has zero first length variation.

For a shell pair `ij` put

$$
\dot\ell_{ij}:=
\frac{(p_i-p_j)\cdot(u_i-u_j)}{|p_i-p_j|}.
$$

SL implies that no integrable equilateral velocity can satisfy

$$
\dot\ell_{ij}<0
\qquad\text{for every }ij\in H,
\tag{5.1}
$$

because the shell diameter would decrease for small positive time.

SL+ is stronger at finite order: even if the first-order maximum is zero, a sufficiently small exact equilateral motion cannot weakly preserve all H-lengths, strictly decrease one, and create no new diameter pair.

The existing KKT stress certifies the first-order obstruction. SL+ records the additional nonlinear active-set obstruction inherited from C65.

---

## 6. Relation to classical equilateral-polygon diameter problems

The cyclic force shell is therefore not merely near Reinhardt's perimeter-diameter scale. It is an actual local minimizer of the classical problem:

> minimize diameter among convex equilateral `q`-gons of fixed side length one.

Vincze's classical necessary condition for such extrema says every polygon vertex must have an opposite vertex at the diameter. Target C already has the stronger property that every shell vertex is an actual diameter endpoint.

The literature on small equilateral polygons, especially `q=2^s`, contains highly nonregular locally or near-globally optimal diameter skeletons. Therefore SL by itself does not imply Reinhardt equality or an odd unicyclic diameter graph. It is a transfer theorem that permits such polygon results to be imported without a source-population gap.

---

## 7. Regression audit

### Power-of-two near-extremal equilateral polygons

Allowed. Modern constructions show that connected/highly branched diameter skeletons can approach the formal Reinhardt scale extremely closely. SL does not falsely claim shell local optimality forces the `d_H=0` Reinhardt family.

### Arbitrarily small interior slack

Allowed. The proof uses only a source-dependent positive neighborhood obtained from finiteness; no uniform quantitative clearance is claimed.

### Additional endpoint beta zeros

Irrelevant. SL is a primal source theorem and uses the full actual diameter set, not a selected stress support.

### Contact-preserving hull saturation

Not used. The argument works directly on the UFB/C65 representative and therefore respects the canonical warning against combining C1 saturation with diameter-pair minimization.

---

## 8. What this changes

The complete cyclic endpoint now simultaneously has:

$$
F=\operatorname{conv}A,
$$

$$
C(A)|_{V(F)}=C_q,
$$

$$
q=\pi D-\frac\pi{24D}+O(D^{-2}),
$$

$$
D(n-q)<D(n)-\sqrt3,
$$

and

$$
F\text{ is a local diameter minimizer among convex equilateral }q\text{-gons}.
$$

Moreover the C65 diameter active set is locally inclusion-minimal among side-preserving same-diameter shell motions that create no new active pair.

This links the source-wide packing problem and the finite equilateral-polygon problem on the same representative.

---

## 9. Next theorem

Two directions are now sharply separated.

1. **Classical-polygon import:** find a theorem stronger than Vincze's endpoint condition that applies to local diameter minima with the Target C extra hypotheses `d_H<=2`, near-Reinhardt scale, and convex-thrackle diameter graph.
2. **Interior stability:** use the fact that the shell cannot move inward even infinitesimally without running into the dense contact-isolated population. A useful quantitative theorem would turn the source-dependent slack in Section 1 into many near-unit shell-interior constraints, which could contradict C-I actual-contact minimality or feed a second-order packing estimate.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

SL/SL+ are elementary finite consequences of UFB/CY/C65. They introduce no new external proof dependency.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

UFB gives F=conv(A). CY/C-I says the only actual unit contacts are the q consecutive
shell edges. C65 says each interior rattler is not a diameter endpoint. Since A is
finite, all interior-shell distances have positive slack from both 1 and D, all
nonadjacent shell pairs have positive slack from 1, and all inactive shell pairs have
positive slack from D.

Therefore fix all n-q interior points and make any sufficiently small convex equilateral
deformation of the q shell vertices. All inactive source constraints remain inactive.
If the shell diameter dropped below D, the full n-point source diameter would drop
below D(n): impossible. Thus F is a local diameter minimizer among convex equilateral
q-gons.

Stronger C65 transfer: a sufficiently small side-preserving deformation cannot keep all
old diameter pairs <=D, make at least one strictly <D, and create no new diameter pair.
Otherwise the full source stays contact-minimal with diameter D but has fewer actual
diameter pairs, contradicting C65's secondary lexicographic choice.

Next: import a stronger local equilateral-polygon theorem, or use dense interior points
to force quantitative near-active shell/interior constraints.
```
