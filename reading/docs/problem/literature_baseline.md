> Generated reading edition · [exact source](../../../docs/problem/literature_baseline.md) · source SHA-256 `21bac2fde1a2d5f012f843de2d7bc8ed13a24c07081e9d3dc3541c7bba4e7784`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Supplied-literature baseline and argument audit

> This modular audit was recovered from the homelab working tree on 2026-08-30. It
> records the supplied-paper baseline and dispositions of imported arguments. See the
> [current documentation map](../README.md) and [literature review](../literature_review.md)
> for the complete v1.7 source layout and expanded external audit.

## 2. What the supplied literature proves

### 2.1 Exact small cases

Bateman and Erdős [2](../BIBLIOGRAPHY.md#ref-2) establish

```math
D(2)=D(3)=1,\qquad D(4)=\sqrt2,
```

```math
D(5)=\frac{1+\sqrt5}{2},\qquad D(6)=2\sin72^\circ,
```

and prove

```math
D(7)=2,
```

with the unique $`n=7`$ minimizer equal to a regular unit hexagon together with its center.

Bezdek and Fodor [3, Theorem 1.1](../BIBLIOGRAPHY.md#ref-3) prove

```math
D(8)=\frac1{2\sin(\pi/14)},
```

and show that every minimizer has a regular unit heptagon as its convex hull; the eighth point is not uniquely determined.

The exact contact structures show nonmonotonicity:

- $`n=4`$: the unit square is triangle-free.
- $`n=5`$: the regular unit pentagon is triangle-free.
- $`n=6`$: the regular pentagon has circumradius $`1`$, so the center-to-vertex contacts form $`K_{1,5}`$; the configuration is triangle-free.
- $`n=7`$: the center and every pair of adjacent hexagon vertices form a unit equilateral triangle.
- $`n=8`$: taking the eighth point at the heptagon center gives contact graph $`C_7`$ plus an isolated vertex, hence a triangle-free minimizer.

These cases disprove every naive monotonicity principle.

### 2.2 Diameter bounds and normalization

Bondarenko, Hardin, and Saff [5](../BIBLIOGRAPHY.md#ref-5) define

```math
D_2(n)=\min
\frac{\max_{i\ne j}|p_i-p_j|}{\min_{i\ne j}|p_i-p_j|},
```

which is exactly the present $`D(n)`$ after normalizing the minimum distance to $`1`$. With

```math
\Delta_2=\frac{\pi}{\sqrt{12}}=\frac{\pi}{2\sqrt3},
```

their general Theorem 2 yields

```math
\sqrt{\frac n{\Delta_2}}-2\le D(n)\le\sqrt{\frac n{\Delta_2}}.
\tag{2.1}
```

For the plane, however, Bezdek and Fodor give the sharper lower estimate in the introduction to [3](../BIBLIOGRAPHY.md#ref-3):

```math
\boxed{
\sqrt{\frac n{\Delta_2}}-1\le D(n)<\sqrt{\frac n{\Delta_2}}.
}
\tag{2.2}
```

Indeed, Fejes Tóth's finite packing inequality gives

```math
\operatorname{area}\bigl(\operatorname{conv}A+B(0,1/2)\bigr)
\ge \frac{\sqrt3}{2}n.
```

The parallel body has diameter $`D(n)+1`$, and the isodiametric inequality gives the lower half of (2.2). For the strict upper half, average the number of points of the unit triangular lattice in an open disk of radius $`\frac12\sqrt{n/\Delta_2}`$. The average over lattice translations is exactly $`n`$, so some translate contains at least $`n`$ lattice points; any finite subset of that open disk has diameter strictly smaller than its diameter. The same argument is recorded in Theorem 10.9.

This correction matters: several imported drafts used the weaker (-2) bound even when working specifically in the plane.

### 2.3 Nonlattice optimality

Schürmann [4, Theorem 9](../BIBLIOGRAPHY.md#ref-4) includes the minimum-diameter packing function and proves that, for all sufficiently large $`n`$, extremal packings are nonlattice. His proof uses loose boundary edges and sequential movements of disks in a lattice packing.

This rules out an eventual classification by finite triangular-lattice patches. It does **not** imply that large minimizers are triangle-free, nor does it exclude a nonlattice configuration with a large triangular contact core.

### 2.4 Triangle-free penny graphs

Eppstein [6](../BIBLIOGRAPHY.md#ref-6) proves:

1. Every triangle-free penny graph is (2)-degenerate [6, Theorem 1](../BIBLIOGRAPHY.md#ref-6).
2. Every connected triangle-free penny graph containing a cycle has at least four non-articulation vertices of degree at most (2) [6, Lemma 2](../BIBLIOGRAPHY.md#ref-6).
3. If $`G`$ is connected with graph diameter $`d_G`$, then

   ```math
   |E(G)|\le2|V(G)|-d_G-2
   \tag{2.3}
   
   ```

   [6, Theorem 2](../BIBLIOGRAPHY.md#ref-6).
4. For arbitrary $`n`$-vertex triangle-free penny graphs,

   ```math
   |E(G)|
   \le
   2n-\frac12\sqrt{2\pi\sqrt3\,n}+O(1)
   \tag{2.4}
   
   ```

   [6, Theorem 4](../BIBLIOGRAPHY.md#ref-6).

These results are exact graph-theoretic restrictions, but they do not alone imply geometric flexibility of a cable-strut framework.

### 2.5 Rigidity terminology

Bezdek, Bezdek, and Connelly [7](../BIBLIOGRAPHY.md#ref-7) define tensegrity stresses with nonnegative coefficients on cables and nonpositive coefficients on struts. Their paper develops stability and infinitesimal-rigidity ideas for sphere packings.

One imported argument relied on an all-strut characterization quoted in Section 4 of [7](../BIBLIOGRAPHY.md#ref-7) from another paper. Because the present project permits results actually proved in the supplied sources, the consolidated arguments below do not rely on that quotation. The needed pinned result is instead proved directly by elementary finite-dimensional cone duality.

---

## 3. Audit of the imported GPT arguments

The imported work contains several valuable results, but also some statements that require repair.

| Imported claim | Audit result | Treatment here |
|---|---|---|
| Regular unit $`p`$-gons are triangle-free strict local diameter minima for odd primes $`p`$ | Correct, modulo Euclidean congruence | Included as Proposition 13.1 |
| Pinned rigidity provides a stress strictly positive on every contact | The cited justification was unsafe for pinned frameworks and relied on a theorem merely quoted in [7](../BIBLIOGRAPHY.md#ref-7) | Reproved directly from the zero expansive cone using cone duality |
| In the jammed branch every hull vertex is diametral | Correct; there is also a direct outward-flex proof | Included as Lemma 7.2 and Theorem 8.2 |
| A rigid triangle-free minimizer with forest contact graph has $`n\le43`$ | Correct after replacing “rigid” by the precisely defined zero-cone branch | Included as Corollary 9.2 |
| BHS gives the operative planar lower bound with (-2) | True but not sharp | Replaced by Bezdek-Fodor's planar (-1) bound |
| Every minimizer has an ordinary KKT stress | Correct; MFCQ has an explicit strict direction | Included with full proof |
| Positive contact-stress components must be boundary loaded | Correct | Included in Section 5 |
| A contact-minimal triangle-free minimizer has all non-diameter nonisolated vertices trapped by (3)-(5) contacts | Correct | Included in Section 6 |
| In the pinned zero-cone branch almost all faces are near-equilateral unit rhombi | Correct after direct rank proof | Included in Section 10 |
| One fixed KKT multiplier is nonnegative on the whole second-order critical cone | Not justified by MFCQ | Replaced by a direction-dependent multiplier theorem |
| An affine shear produces a negative second-order stress energy | False | The tensor identity makes the quadratic energy exactly zero |
| The pinned rank count may omit contacts joining two fixed vertices | Correct | Strengthened to $`e^\circ\ge2(n-q)`$ in Theorem 7.1 |
| The total rhombus angular excess is $`O(\sqrt n)`$ | Correct by the concavity chord bound | Included as Corollary 10.4 |
| The midpoint, quartic, annular-mass, and high-moment stress identities | Correct after direct algebraic verification | Included as Theorems 11.3--11.5 |
| A maximal-contact representative has every contact component diameter-anchored | Correct after handling coincident boundary circles | Included as Theorem 12.3 |
| The minimum- and maximum-contact normal forms can be partly combined | Correct only after freezing the original core and all original diameter endpoints | Included as Theorems 12.4--12.5; the remaining bridge forest is not silently declared jammed |
| Rhombus tracks are pseudolines and satisfy $`R\le B^2/16`$ | Correct after replacing an informal crossing-sign argument by the strict displacement-cone proof | Included as Theorem 10.6 |
| A two-direction rhombic core needs $`\Omega(\sqrt R)`$ non-hull supports | Correct with explicit simple-boundary and no-pinch hypotheses | Included as Theorem 10.12, with the one-rhombus and five-rhombus-cross classification at zero support |
| Boundary-pinned almost-equilateral rhombus meshes must contain a $`60^\circ`$ face | False | Proposition 10.10 gives total positive defect $`8/s\to0`$ with zero boundary-pinned cone |
| A triangle-free packing has a uniform density gap | False as a proposed principle | Explicit near-triangular perturbations and shell fillings disprove such a gap |
| Schürmann implies an eventual triangular or rhombic lattice structure | False | His theorem only excludes lattice extremizers |

The imported reports were therefore used as sources of candidate lemmas, not as authorities. Every theorem retained below is either quoted with its exact hypotheses from a supplied paper or reproved in this document.

### 3.1 Disposition of the latest strengthening

The outward hull-vertex flex, the degree-$`\le2`$ local motions, the effective row count $`e^\circ`$, the $`n-O(\sqrt n)`$ cyclomatic bound, the component estimates, and the angular-defect conversion are correct as stated after replacing the informal word “rigid” by the exact condition $`\mathcal E_Q(A)=\{0\}`$.

The virtual-work, midpoint, quartic, dispersion, annular-mass, and high-moment radius formulas are also correct; their constants were recomputed directly. Two proof repairs were made:

1. Full pinned rank follows directly from the zero expansive cone, so no rigidity theorem merely quoted in [7](../BIBLIOGRAPHY.md#ref-7) is invoked.
2. A regular boundary translation can activate several coincident constraints. They need not be unique, but the corresponding new unit edges form a matching and therefore cannot create a triangle. This is the form proved in Theorem 12.3.

### 3.2 Audit of the bridge-forest and train-track strengthening

The later imported investigation was also treated as candidate mathematics rather than authority. Its main claims were checked against the definitions and retained in the following precise forms.

1. The proposed representative combination is valid after freezing the contact-minimal core and every original diameter endpoint throughout the construction. New unit contacts can be made one at a time and always join distinct current components, so they remain bridges. This gives Theorem 12.4, not the stronger and still unproved assertion that the entire final representative is pinned-jammed.
2. Contracting the frozen core leaves a forest. A direct row count, allowing several fixed roots in one component, gives the lower bound $`u-r+c`$ in Theorem 12.5. Thus the residual obstruction is quantitatively high-dimensional whenever more than boundary-order many vertices lie outside the core.
3. The train-track monotonicity, at-most-one-crossing theorem, triangle-free crossing graph, width inequality, and Cartesian determinant inequality all survive without a disk assumption; the disk hypothesis is used only for the Euler relation in Theorem 10.8 and related boundary classifications.
4. The fixed-two-direction support theorem is valid with the regularity hypotheses stated in Theorem 10.12. In particular, hole-boundary incidences and pinched boundaries cannot be silently ignored.
5. The apparent five-direction escape is geometrically real. Proposition 10.10 realizes the balanced $`C_5`$ blow-up by a unit-separated rhombic disk, so no large Cartesian block follows merely from a dense triangle-free track-crossing graph.

These audits narrow the two branches but do not close either one. The five-sector construction is not certified globally optimal. The 11-point sun following Proposition 10.10 is stronger as a local regression test but is proved not globally optimal by an explicit smaller-diameter lattice competitor.

---
