<!-- theorem-state: {"artifact_id":"ART-867FE41BF630","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: Reuleaux trapping and diameter-cycle girth

**Date:** 2026-08-31  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / global diameter-graph reduction  
**Target:** Level I candidate route C  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This note turns the Reuleaux-container idea into a theorem about the full diameter graph of every global minimizer.

If the diameter graph contains an odd cycle of length `q`, then the cycle vertices are exactly the vertices of a Reuleaux `q`-gon of width `D`, and the **entire source configuration** lies in that Reuleaux polygon.  Firey--Sallee maximal-area theory for Reuleaux polygons then combines with the global minimum-diameter packing inequalities to force an explicit lower bound on `q`:

\[
\boxed{
q>
\frac{\pi D}{\sqrt{12(2D+1)}}
\sim
\frac{\pi}{\sqrt{24}}\sqrt D.
}
\tag{C17.1}
\]

Since `D(n)\asymp\sqrt n`, any diameter cycle in a global minimizer has length `\Omega(n^{1/4})`.  In particular no fixed odd diameter cycle can occur for arbitrarily large `n`.

No triangle-free hypothesis is used.

---

## 1. A diameter cycle has no diameter chord

Let `A` be a finite planar set of diameter `D`, and suppose its diameter graph contains a cycle

\[
\Gamma=(v_1,v_2,\ldots,v_q,v_1).
\tag{C17.2}
\]

The classical planar diameter-graph theorem says every cycle in a planar diameter graph is odd.  Hence `q` is odd.

### Lemma C17.1

The diameter graph induced by `V(\Gamma)` is exactly the cycle `\Gamma`.

#### Proof

Suppose an additional diameter edge `v_i v_j` joined two nonconsecutive cycle vertices.  That chord splits the odd cycle into two cycles whose lengths sum to `q+2`, which is odd.  Hence one of the two new cycles has even length.  This contradicts the theorem that every planar diameter-graph cycle is odd. `\square`

After scaling by `D`, the set `V(\Gamma)` therefore has diameter one and diameter graph exactly a `q`-cycle.

---

## 2. The cycle uniquely determines a Reuleaux polygon containing the whole source

Kupitz--Martini--Wegner, *A Linear-Time Construction of Reuleaux Polygons*, Theorem 0.1 / Theorem 1.7, prove the following exact planar fact: if a finite diameter-one set has Hamiltonian diameter graph, then it is the vertex set of a unique Reuleaux polygon of width one; equivalently its diameter graph is exactly an odd cycle.  Their proof also uses the classical completion theorem that every planar diameter-one set is contained in some convex body of constant width one.

Apply this after scaling `V(\Gamma)` by `D`.  There is a unique Reuleaux `q`-gon `R_\Gamma` of width `D` containing the cycle vertices.

### Theorem C17.2 (cycle trapping)

\[
\boxed{
A\subseteq R_\Gamma.
}
\tag{C17.3}
\]

#### Proof

The planar constant-width completion theorem gives a convex body `K` of constant width `D` containing the whole diameter-`D` set `A`.  In particular `K` contains `V(\Gamma)`.  But the Kupitz--Martini--Wegner uniqueness theorem says there is only one constant-width `D` body containing those cycle vertices, namely `R_\Gamma`.  Thus `K=R_\Gamma`, and therefore `A\subseteq R_\Gamma`. `\square`

This is stronger than merely saying that the cycle vertices themselves sit on a Reuleaux polygon.  Every KKT-invisible point, rattler, contact component, and hull point of the source is trapped in the same constant-width body.

---

## 3. Maximal area of a Reuleaux q-gon

For odd `q\ge3`, Firey and Sallee prove that among all Reuleaux `q`-gons of fixed width, the regular Reuleaux `q`-gon has maximum area.

For width one its area is

\[
\boxed{
A_q
=
\frac12\left(\pi-q\tan\frac{\pi}{2q}\right).
}
\tag{C17.4}
\]

Thus for width `D`,

\[
\operatorname{area}(R_\Gamma)
\le
A_qD^2.
\tag{C17.5}
\]

Every body of constant width `D` has perimeter `\pi D` by Barbier's theorem.  Steiner's formula therefore gives

\[
\boxed{
\operatorname{area}(R_\Gamma+B(0,1/2))
\le
A_qD^2+\frac\pi2D+\frac\pi4.
}
\tag{C17.6}
\]

Since `conv A\subseteq R_\Gamma`, the same expression is an upper bound for the source parallel body.

Define the regular-Reuleaux area deficit from the disk of width one:

\[
\delta_q
:=
\frac\pi4-A_q
=
\frac q2\left(\tan\frac{\pi}{2q}-\frac{\pi}{2q}\right)>0.
\tag{C17.7}
\]

For `x\ge0`,

\[
\tan x-x\ge\frac{x^3}{3}.
\tag{C17.8}
\]

Indeed, the difference has derivative `\tan^2x-x^2\ge0` and vanishes at zero.  Consequently

\[
\boxed{
\delta_q
\ge
\frac{\pi^3}{48q^2}.
}
\tag{C17.9}
\]

---

## 4. Global optimality forces long diameter cycles

Now let `A` be a global `n`-point minimizer and put `D=D(n)`.

The canonical Fejes Toth finite-packing inequality gives

\[
\operatorname{area}(\operatorname{conv}A+B(0,1/2))
\ge
\frac{\sqrt3}{2}n.
\tag{C17.10}
\]

The canonical strict upper bound

\[
D^2<\frac n{\Delta_2},
\qquad
\Delta_2=\frac\pi{2\sqrt3},
\tag{C17.11}
\]

implies

\[
\boxed{
\operatorname{area}(\operatorname{conv}A+B(0,1/2))
>
\frac\pi4D^2.
}
\tag{C17.12}
\]

If the diameter graph contains a `q`-cycle, combine (C17.6) and (C17.12):

\[
\frac\pi4D^2
<
A_qD^2+\frac\pi2D+\frac\pi4.
\]

Equivalently,

\[
\delta_qD^2
<
\frac\pi2D+\frac\pi4.
\tag{C17.13}
\]

Using (C17.9),

\[
\frac{\pi^3D^2}{48q^2}
<
\frac\pi2D+\frac\pi4.
\]

After simplification,

\[
\pi^2D^2<12q^2(2D+1),
\]

so

\[
\boxed{
q>
\frac{\pi D}{\sqrt{12(2D+1)}}.
}
\tag{C17.14}
\]

This proves the announced bound. `\square`

As `D\to\infty`,

\[
q>
\left(\frac\pi{\sqrt{24}}+o(1)\right)\sqrt D
=
(0.64127\ldots+o(1))\sqrt D.
\tag{C17.15}
\]

Since the canonical diameter estimates give `D(n)=\Theta(\sqrt n)`, any diameter cycle in global minimizers has length `\Omega(n^{1/4})`.

---

## 5. Consequences for Target C

### Corollary C17.3 (no bounded diameter-cycle phase)

For every fixed odd integer `q_0`, there is `n_0(q_0)` such that no global minimizer with `n\ge n_0(q_0)` has a diameter cycle of length at most `q_0`.

Thus the equilateral diameter triangle excluded in C15 is only the first member of a general phenomenon.

### Corollary C17.4 (positive KKT diameter cycles are long)

If the positive KKT diameter graph `H_+` of a normalized KKT stress contains a cycle of length `q`, then the same bound (C17.14) holds, because that cycle is also a cycle in the full diameter graph.

Hence a KKT boundary-shear obstruction cannot be supported on a fixed-size cyclic diameter gadget in large global minimizers.

### Corollary C17.5 (uniform local angular gap)

There exist absolute constants `\eta>0` and `n_1` such that for every global minimizer with `n\ge n_1`, whenever

\[
|b-y|=|b-z|=D(n),
\qquad y\ne z,
\]

the angle at `b` satisfies

\[
\boxed{
\angle ybz\le\frac\pi3-\eta.
}
\tag{C17.16}
\]

#### Proof sketch

If not, there would be global minimizers with `n_m\to\infty` and two diameter chords at one endpoint whose angle tends to `\pi/3`.  Their three endpoints, after scaling by `D(n_m)`, converge to an equilateral diameter triple.  The three corresponding unit-disk intersections converge to the unit Reuleaux triangle, so the normalized source parallel-body area has limsup at most `(\pi-\sqrt3)/2<\pi/4`.  But (C17.12) forces it to be strictly larger than `\pi/4` for every source.  This is exactly the compactness argument of Target C Theorem C16, now stated without KKT weights. `\square`

Therefore, in every sufficiently large minimizer, all diameter partners of a fixed point lie in an angular arc of width uniformly **strictly** below `60` degrees.

---

## 6. Why this matters for the shear obstruction

Target C6--C9 reduce weak-contact survival to differential angular motion of KKT-supported diameter chords.  C17 imposes a new global restriction on that boundary system:

- any cyclic part has at least order `\sqrt D` edges;
- no fixed odd-cycle gadget can carry the obstruction;
- all incident diameter directions at one endpoint lie in a uniformly acute cone of width `<60` degrees for large sources.

Thus the shear obstruction is forced into one of two regimes:

1. a large tree/matching-like diameter network; or
2. an odd cycle whose length itself diverges at least as `\Omega(\sqrt D)`.

This is a genuinely global restriction derived from packing area.  It is not a rigidity count and does not use Target A's scaffold or Target B's rhombic shell.

The next useful theorem is to combine this long-cycle/tree dichotomy with the angular variance inequality C13.3.  In particular, one should seek a Poincare inequality for the diameter angular-rate field on a geometric thrackle whose only cycle has length `\Omega(\sqrt D)` and whose incident edge directions have the strict angular gap (C17.16).

---

## 7. Literature imports

The following external facts are used exactly:

1. **Kupitz--Martini--Wegner**, *A Linear-Time Construction of Reuleaux Polygons*: for a finite diameter-one planar set, a Hamiltonian diameter graph is equivalent to being the vertex set of a Reuleaux polygon; the containing constant-width body is unique.
2. The standard planar **constant-width completion theorem**: every planar set of diameter `D` is contained in a convex body of constant width `D`.
3. **Firey--Sallee**: among Reuleaux `q`-gons of fixed width and fixed odd `q`, the regular one has maximum area; formula (C17.4).
4. **Barbier**: every planar convex body of constant width `D` has perimeter `\pi D`.
5. The classical planar diameter-graph fact that every cycle is odd.

The Kupitz--Martini--Wegner theorem and its uniqueness statement were checked directly at theorem level before use.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C17:
If a global minimizer of diameter D has a diameter-graph cycle of length q, then

    q > pi D / sqrt(12(2D+1))
      = (pi/sqrt(24)+o(1)) sqrt(D).

Proof:
- every planar diameter cycle is odd;
- an extra diameter chord of the cycle vertices would create an even cycle, so their induced diameter graph is exactly the q-cycle;
- Kupitz-Martini-Wegner => those vertices determine a unique Reuleaux q-gon R of width D;
- every diameter-D source has a constant-width D completion, and uniqueness forces the entire source A inside R;
- Firey-Sallee gives area(R)<=A_q D^2 with
      A_q=1/2(pi-q tan(pi/(2q)));
- Barbier + Steiner gives
      area(R+B_1/2)<=A_qD^2+(pi/2)D+pi/4;
- Fejes Toth + global D(n)^2<n/Delta_2 gives
      area(convA+B_1/2)>pi D^2/4;
- the area deficit satisfies
      pi/4-A_q = q/2(tan x-x) >= pi^3/(48q^2),
  yielding the stated q bound.

Consequences:
- no fixed diameter odd-cycle can occur for arbitrarily large n;
- any H_+ cycle in a KKT stress is Omega(sqrt D)=Omega(n^1/4);
- independently of KKT weights, large minimizers have a uniform angular gap below 60 degrees between any two diameter chords sharing an endpoint.

New Target C boundary regime:
the diameter-shear obstruction must live either on a large tree/matching-like system or on an odd cycle whose length diverges at least as sqrt(D).  Combine this next with C13's angular-variance inequality.
```
