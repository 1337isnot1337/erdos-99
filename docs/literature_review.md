# Literature review for Erdős Problem #99

**Audit date:** 2026-08-30

**Scope:** minimum-diameter configurations of `n` unit-separated points in the
plane, with emphasis on the question whether every sufficiently large minimizer
contains a unit equilateral triangle.

## Executive assessment

The direct literature remains thin, but the surrounding finite-packing literature is
substantial and useful. The most valuable additions fall into four connected paths:

1. **Problem history and direct diameter data.** Erdős's 1995 survey gives the
   original wording of the problem, including the triangular-lattice heuristic and
   the unit-equilateral-triangle conjecture. Daróczy-Kiss is the closest later
   finite-diameter follow-up found in this audit: it improves an upper bound for
   `D(9)`, but does not determine `D(9)` or address the eventual equilateral
   triangle question.
2. **Finite-packing inequalities.** Oler's finite-packing paper, the
   Folkman--Graham proof, and the Graham--Witsenhausen--Zassenhaus Minkowski-plane
   paper give the geometric context for the boundary-order estimates and
   "Oler-slack" bookkeeping used by the current research report.
3. **Finite shape and boundary theory.** Wegner, Böröczky--Ruzsa,
   Böröczky--Schnell, and Schürmann study convex hulls, Groemer-type finite
   packings, exceptional cardinalities, and parametric density. These results explain
   why triangular/hexagonal bulk behavior is a powerful guide while still leaving a
   finite boundary problem.
4. **Saturation and computational analogies.** The Kuperberg papers, Fejes
   Tóth--Kuperberg--Kuperberg, Gensane, Graham--Lubachevsky, and the modern survey by
   Henk--Wills are relevant to gap defects, saturation, generation, and finite
   packing transitions. They provide mechanisms and warnings, not a proof of
   Erdős Problem #99.

The official problem record still labels Problem #99 open: [Erdős Problems,
#99](https://www.erdosproblems.com/99). The companion question about the number of
inequivalent minimizers is [Problem #103](https://www.erdosproblems.com/103). No
source located in this audit closes either question.

## How the audit was conducted

The search started from the seven PDFs already in `papers/primary/` and the
references named in the canonical report. It then followed the terms *minimal
diameter*, *finite packing*, *Oler inequality*, *parametric density*, *Groemer
packing*, *saturation*, *gap defect*, *plane-width*, and *equilateral-triangle
packing* through original journal pages, arXiv, EJC, EMS, MathDoc, institutional
repositories, and author manuscripts. Sources were selected when they supplied at
least one of the following:

- the original problem statement or a direct `D(n)` result;
- a theorem used to understand finite-packing boundary terms or hulls;
- a rigorous finite-to-infinite/asymptotic shape bridge;
- a precise saturation or defect phenomenon relevant to the current obstruction; or
- an exact reformulation or computational comparison that makes the problem easier
  to test.

Broad packing surveys with no finite-diameter or boundary connection were not
bundled. Papers for which a stable, legally appropriate open copy was not found are
listed as citation-only leads below.

## Bundled sources

The labels indicate how a source should be used in the repository:

- **A — direct:** problem statement, direct minimum-diameter result, or exact
  reformulation;
- **B — structural:** finite-packing geometry that can constrain a proof;
- **C — context:** saturation, computation, or analogy; useful for hypotheses and
  counterexample checks, but not itself a theorem about Problem #99.

| Label | Source | What it adds | Local copy |
| --- | --- | --- | --- |
| A | Paul Erdős, “Some of my Favourite Problems in Number Theory, Combinatorics, and Geometry,” *Resenhas IME-USP* 2(2) (1995), 165–186. [Record](https://revistas.usp.br/resenhasimeusp/en/article/view/74798), [DOI](https://doi.org/10.11606/resimeusp.v2i2.74798) | The original published wording of Problem #99: unit separation, minimum diameter, triangular-lattice asymptotics, and the conjectured unit equilateral triangle. The article is marked CC BY-NC-SA 4.0 by the journal. | [PDF](https://revistas.usp.br/resenhasimeusp/en/article/view/74798) |
| A | E. Daróczy-Kiss, “A New Bound for the Minimal Diameter of Nine Coplanar Congruent Disks,” *Annales Univ. Sci. Budapest., Sect. Comp.* 25 (2005), 25–35. [PDF](https://ac.inf.elte.hu/Vol_025_2005/doi/025_25.pdf) | Improves the known upper bound to `d(9) ≤ 2.5693` using computer-assisted construction. It confirms that the `n=9` finite problem was still not exact; it does not bear directly on the eventual large-`n` conjecture. | [PDF](https://ac.inf.elte.hu/Vol_025_2005/doi/025_25.pdf) |
| A | M. Kamiński, P. Medvedev, and M. Milanič, “The Plane-Width of Graphs,” [arXiv:0812.4346](https://arxiv.org/abs/0812.4346) (2008). | Gives an exact graph-embedding language: the plane-width of a complete graph is the minimum diameter of a unit-separated point set. This provides a clean independent formulation of the `D_2(n)` objective and a route to graph-theoretic comparisons. | [PDF](https://arxiv.org/abs/0812.4346) |
| B | Norman Oler, “A Finite Packing Problem,” *Canadian Mathematical Bulletin* 4 (1961), 153–155. [Record/DOI](https://geodesic.mathdoc.fr/articles/10.4153/CMB-1961-018-7/) | The short source behind the finite packing inequality used in many planar estimates; it applies the inequality to unit-separated points in an equilateral triangle and relates the result to triangular-number bounds. | [PDF](https://geodesic.mathdoc.fr/articles/10.4153/CMB-1961-018-7/) |
| B | J. H. Folkman and R. L. Graham, “A Packing Inequality for Compact Convex Subsets of the Plane,” *Canadian Mathematical Bulletin* 12 (1969), 745–752. [Record/DOI](https://geodesic.mathdoc.fr/articles/10.4153/CMB-1969-096-7/) | Supplies an elementary planar proof of the Oler-type area-plus-perimeter bound for unit-separated points in a compact convex set. This is the cleanest companion to the report's finite boundary accounting. | [PDF](https://geodesic.mathdoc.fr/articles/10.4153/CMB-1969-096-7/) |
| B | R. L. Graham, H. S. Witsenhausen, and H. J. Zassenhaus, “On Tightest Packings in the Minkowski Plane,” *Pacific Journal of Mathematics* 41 (1972), 699–715. [Journal PDF](https://msp.org/pjm/1972/41-3/pjm-v41-n3-p10-s.pdf) | Extends finite-packing/tightness ideas from the Euclidean plane to arbitrary Minkowski norms and develops a slackness viewpoint. It is useful for distinguishing metric packing facts from specifically triangular-lattice facts. | [PDF](https://msp.org/pjm/1972/41-3/pjm-v41-n3-p10-s.pdf) |
| B | N. Oler, “An Inequality in the Geometry of Numbers,” *Acta Mathematica* 105 (1961), 19–48. [DOI](https://doi.org/10.1007/BF02559533), [open scan](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5914-11511_2007_Article_BF02559533.pdf) | The longer foundational source for the convex-domain finite-packing inequality. It is worth having beside the three-page application because it exposes the geometric-number-theoretic machinery rather than only the final estimate. | [PDF](https://doi.org/10.1007/BF02559533) |
| B | Stephen Vincze, “On a Geometrical Extremum Problem,” *Acta Scientiarum Mathematicarum (Szeged)* 12A (1950), 136–142. [Record/PDF](https://acta.bibl.u-szeged.hu/13598/) | An early convex-polygon diameter problem cited by Bateman--Erdős and by the later `D(9)` discussion. It supplies historical context for the polygonal extremum branch, but its objective is not identical to Problem #99. | [PDF](https://acta.bibl.u-szeged.hu/13598/) |
| B | Károly Böröczky Jr. and Uwe Schnell, “Asymptotic Shape of Finite Packings,” *Canadian Journal of Mathematics* 50 (1998), 16–28. [Record/DOI](https://geodesic.mathdoc.fr/articles/10.4153/CJM-1998-002-5/) | Bridges finite packings and infinite packing density through parametric density and proves asymptotic shape statements. It supports a bulk-versus-boundary reading of the triangular-lattice heuristic, not a claim that every finite minimizer is lattice-supported. | [PDF](https://geodesic.mathdoc.fr/articles/10.4153/CJM-1998-002-5/) |
| B | Gerd Wegner, “Über endliche Kreispackungen in der Ebene,” *Studia Scientiarum Mathematicarum Hungarica* 21 (1986), 1–28. [Full volume](https://real-j.mtak.hu/5463/1/StudScientMath_21.pdf) | Introduces the `P`-hull and proves hexagonal-lattice optimality for broad classes of finite cardinalities, with 121 as the first exceptional integer in the representation condition discussed there. It is a central finite-hull analogue, but the paper is in German and optimizes a disk-hull objective. | [Article-only PDF](https://real-j.mtak.hu/5463/1/StudScientMath_21.pdf) |
| B | Károly J. Böröczky and Imre Z. Ruzsa, “Note on an Inequality of Wegner,” *Discrete & Computational Geometry* 37 (2007), 245–249. [DBLP record](https://dblp.org/rec/journals/dcg/BoroczkyR07), [author PDF](https://users.renyi.hu/~carlos/wegner.pdf) | Gives a number-theoretic characterization of the cardinalities for which Wegner/Groemer finite packings exist and identifies 121 as the smallest exceptional value. This sharpens the finite-lattice analogy without resolving arbitrary minimum-diameter point sets. | [PDF](https://dblp.org/rec/journals/dcg/BoroczkyR07) |
| B | Achill Schürmann, “On Parametric Density of Finite Circle Packings,” *Beiträge zur Algebra und Geometrie* 41 (2000), 329–334. [Journal page](https://www.maths.tcd.ie/EMIS/journals/BAG/vol.41/no.2/3.html) | Complements the supplied *On Extremal Finite Packings* paper with a parametric-density formulation, including critical-lattice and Groemer-packing regimes. It is useful for testing which finite packing conclusions need a parameter or a hull hypothesis. | [PDF](https://www.maths.tcd.ie/EMIS/journals/BAG/vol.41/no.2/3.html) |
| B | Orgil-Erdene Erdenebaatar and Uuganbaatar Ninjbat, “The Smallest Convex `k`-gon Containing `n` Congruent Disks,” *Elemente der Mathematik* 77 (2022), 122–137. [EMS record/DOI](https://ems.press/journals/em/articles/1121827), [DOI](https://doi.org/10.4171/EM/451) | A modern open-access finite-packing treatment using Wegner-type inequalities and tight cases. It is a useful comparison for converting between center packings, convex containers, and boundary shape. The objective is containment area, not minimum diameter. | [PDF](https://ems.press/journals/em/articles/1121827) |
| C | Gábor Fejes Tóth, Greg Kuperberg, and Włodzimierz Kuperberg, “Highly Saturated Packings and Reduced Coverings,” *Monatshefte für Mathematik* 125 (1998), 127–145. [arXiv](https://arxiv.org/abs/math/9511225), [DOI](https://doi.org/10.1007/BF01332823) | Defines and studies `n`-saturation and reduced coverings. It is the most direct source for the report's warning that local saturation language must be separated from finite global diameter optimality. | [PDF](https://arxiv.org/abs/math/9511225) |
| C | Greg Kuperberg, Krystyna Kuperberg, and Włodzimierz Kuperberg, “Lattice Packings with Gap Defects Are Not Completely Saturated,” *Beiträge zur Algebra und Geometrie* 45 (2004), 267–273. [arXiv](https://arxiv.org/abs/math/0303366), [journal page](https://ftp.gwdg.de/pub/misc/EMIS/journals/BAG/vol.45/no.1/22.html) | Proves that a honeycomb packing with a narrow linear gap defect need not be completely saturated. This is a concrete warning against turning a locally plausible near-lattice scaffold into a global perturbation theorem. | [PDF](https://arxiv.org/abs/math/0303366) |
| C | A. V. Bondarenko, D. P. Hardin, and E. B. Saff, “Mesh Ratios for Best-Packing and Limits of Minimal Energy Configurations,” [arXiv:1212.6211](https://arxiv.org/abs/1212.6211) (2012). | Bounds the mesh/separation ratio for best-packing configurations and discusses limits of minimal-energy configurations. It is relevant to the canonical report's mesh-ratio citation, with an important caveat: statements about selected energy-limit representatives do not automatically apply to every best-packing minimizer. | [PDF](https://arxiv.org/abs/1212.6211) |
| C | Thierry Gensane, “Generation of Optimal Packings from Optimal Packings,” *Electronic Journal of Combinatorics* 16(1) (2009), R24. [Record/DOI](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r24) | Studies weak/strong generation through contact graphs, including the equilateral-triangle sequence of hexagonal packings and computations through `n=34`. It is useful for conjecture generation and contact-graph experiments, not as a theorem about all diameter minimizers. | [PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r24) |
| C | R. L. Graham and B. D. Lubachevsky, “Dense Packings of Equal Disks in an Equilateral Triangle: From 22 to 34 and Beyond,” *Electronic Journal of Combinatorics* 2(1) (1995), A1. [Record/DOI](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1a1), [arXiv](https://arxiv.org/abs/math/0406252) | A computationally intensive equilateral-triangle packing study with conjectured infinite families and exact algebraic configurations. It is a valuable experimental analogue for boundary transitions, while its numerical/conjectural parts should not be imported as proof. | [PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1a1) |
| C | Martin Henk and Jörg M. Wills, “Packings, Sausages and Catastrophes,” *Beiträge zur Algebra und Geometrie* 62 (2021), 265–280. [Springer article](https://link.springer.com/article/10.1007/s13366-020-00502-x), [arXiv](https://arxiv.org/abs/2005.04267) | An open survey organizing parametric density, finite/free packings, and transitions between packing regimes. Best used as a map into the older literature and as terminology support. | [PDF](https://link.springer.com/article/10.1007/s13366-020-00502-x) |

## Suggested reading paths

### Path 1: the direct Erdős Problem #99 thread

Read the supplied Erdős 1994 paper in `papers/primary/`, then [Erdős's 1995
survey](https://revistas.usp.br/resenhasimeusp/en/article/view/74798), followed by the supplied
Bateman--Erdős and Bezdek--Fodor papers. Add Daróczy-Kiss for the `n=9` update and
the plane-width paper for an exact graph-theoretic restatement. This path is the
shortest route to understanding what is known about small `n`, what the original
conjecture actually says, and why the large-(n) question is still separate.

### Path 2: finite-packing inequalities and boundary terms

Read Oler's three-page application first, then Folkman--Graham for the planar proof,
Graham--Witsenhausen--Zassenhaus for the Minkowski generalization, and the longer
Oler geometry-of-numbers paper for the foundational context. Follow with
Böröczky--Schnell, Wegner, Böröczky--Ruzsa, and Schürmann. This path is the best
background for the canonical report's use of area-plus-perimeter estimates,
finite-packing slack, and the expectation that the unresolved information is
boundary-scale.

### Path 3: saturation, defects, and stress-testing the obstruction

Read Henk--Wills as a map, then Fejes Tóth--Kuperberg--Kuperberg and the Kuperberg
gap-defect paper. Add Gensane and Graham--Lubachevsky for contact-graph and numerical
examples. The key methodological takeaway is negative but important: local
saturation, a near-hexagonal bulk, or a small defect does not by itself imply finite
global diameter optimality.

## Citation-only leads

These are worth retaining in the bibliography and following when a future proof
needs a narrower result, but they were not bundled as PDFs because a stable open copy
was not found or because the paper is more peripheral than the curated collection.

- Daniel A. Klain, “An Error Estimate for the Isoperimetric Deficit,” *Illinois
  Journal of Mathematics* 49 (2005), 981–992,
  [author PDF](https://faculty.uml.edu/dklain/Klain-Isoperimetric.pdf),
  [DOI](https://doi.org/10.1215/ijm/1258138231). Section 4, equation (6), records the
  classical Bonnesen inequality
  \(P^2-4\pi A\ge\pi^2(R-r)^2\) for compact convex planar sets, with \(R\) and
  \(r\) the circumradius and inradius. Section 155 uses exactly this statement to
  turn the canonical isoperimetric deficit into an \(O(\sqrt D)\) annular-thickness
  bound.
- Charles Payan, “Packing of Equal Disks in an Equilateral Triangle: On a Conjecture
  of Erdős–Oler,” *Discrete Mathematics* 165–166 (1997), 555–565,
  [DOI](https://doi.org/10.1016/S0012-365X(96)00201-4). This is a direct finite
  equilateral-triangle analogue and should be checked if the container comparison
  becomes central.
- B. D. Melissen, “Densest Packings of Congruent Circles in an Equilateral
  Triangle,” *The American Mathematical Monthly* 100 (1993), 916–925,
  [DOI](https://doi.org/10.1080/00029890.1993.11990512), and B. D. Melissen and
  H. Schuur, “Packing 16, 17 or 18 circles in an equilateral triangle,” *Discrete
  Mathematics* 145 (1995), 333–342, [DOI](https://doi.org/10.1016/0012-365X(95)90139-C).
  These are useful for the finite-triangle computational lineage.
- G. Joós, “Packing 13 circles in an equilateral triangle,” *Aequationes
  Mathematicae* 95 (2020), 35–65, [DOI](https://doi.org/10.1007/s00010-020-00753-y).
  This is a modern exact finite-container result, but it does not target the
  unconstrained minimum-diameter problem.
- Matthew Tedeschi, “On Packing Thirteen Points in an Equilateral Triangle,”
  *American Journal of Undergraduate Research* 18(2) (2021), [PDF](https://ajuronline.org/uploads/Volume_18_2/AJUR_Vol_18_2_Sept_2021p3.pdf),
  [DOI](https://doi.org/10.33697/ajur.2021.042). This is a readable pedagogical
  treatment of the finite-triangle analogue.
- “Kernelization for Spreading Points,” *ESA 2023*, [arXiv](https://arxiv.org/abs/2308.07099),
  [Dagstuhl record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2023.48).
  This is algorithmic relocation/spreading literature, not the same optimization
  objective, but it may become useful for finite certificates.
- B. D. Lubachevsky, R. L. Graham, and J. D. Stillinger, “Spontaneous Patterns in
  Disk Packings,” [project page](https://www.mi.sanu.ac.rs/vismath/lub/index.html).
  The simulations are useful exploratory material, but they are not a substitute
  for exact finite-diameter certificates.

## What this audit does—and does not—support

The new sources support the following safe statements:

- triangular/hexagonal structure is a robust bulk heuristic and appears in many
  finite-packing equality or asymptotic regimes;
- Oler-type inequalities naturally leave a perimeter/boundary-scale remainder;
- finite hull objectives have exceptional cardinalities and nontrivial boundary
  behavior; and
- local saturation and near-lattice structure can coexist with defects or with
  insufficient information about global optimality.

They do **not** support any of the following stronger claims without a new argument:

- every large minimum-diameter configuration is a subset of the triangular lattice;
- every strict rattler or triangle-free local cell pays a fixed positive geometric
  cost;
- a finite optimum remains an optimum after deleting points or contracting a local
  structure; or
- an asymptotic mesh-ratio or saturation theorem automatically applies to every
  representative of every finite optimum.

Accordingly, the canonical report remains unchanged as a theorem-state document. The
new PDFs are a research library and a set of precise comparison points for the
remaining boundary-to-bulk first-variation obstruction.

## 2026-09-09 update: circular-planar Kalmanson metrics

V. G. Gorbounov and A. A. Kazakov, *Metric properties of electrical networks and the
graph reconstruction problems*, arXiv:2601.08465 (submitted January 13, 2026),
<https://arxiv.org/abs/2601.08465>, proves that effective resistances between
boundary nodes of circular electrical networks satisfy the Kalmanson property and
gives a full characterization of planar electrical Kalmanson metrics. The paper also
derives its network embedding via the generalized Temperley trick and totally
non-negative Grassmannians.

This is directly relevant to the circular-planar response machinery used in Target
C. It provides a newer independent source for the Kalmanson structure that the
repository has primarily cited through Stefan Forcey's arXiv:2108.00550. It should
therefore be treated as supporting provenance for the imported electrical-network
input, not as an Erdős #99 theorem.

In particular, Gorbounov–Kazakov does **not** by itself establish the repository's
diameter-thrackle interval-sign lemma, signed-stress PSD argument, Newton–Hoffman
finite integration, zero-transfer theorem Z, scalar-kernel theorem ZR, or
mixed-framework rigidity theorem ZF. Those remain additional repository arguments.
No theorem authority or Level I status changes from this literature update.

See the dated assessment
[`reports/literature_update_gorbounov_kazakov_2026-09-09.md`](reports/literature_update_gorbounov_kazakov_2026-09-09.md)
for the explicit novelty and dependency split.

## 2026-10-08 update: audited new direct literature (Das, Zenodo 22768362)

**Newly identified source, independently audited October 8, 2026.** Archit Das,
*Stress, rigidity and rhombic reductions for an Erdos minimum-diameter problem
(Problem #99)*, Zenodo preprint, **version 1, September 15, 2026**.
[Record](https://zenodo.org/records/22768362);
[DOI](https://doi.org/10.5281/zenodo.22768362).
**Category A: direct Erdős #99 research.** The preprint has a completed,
scope-qualified **independent mathematical audit** in
[the dated theorem-by-theorem literature entry](problem/literature_archit_das_stress_rhombic_audit_2026-10-08.md).
This is an external preprint, not a peer-reviewed or canonical repository theorem.

The audited manuscript establishes these **scoped** results:

- Every global diameter minimizer has a normalized nonnegative KKT equilibrium
  stress. An adapted stress can put positive weight only on contacts frozen by
  every infinitesimal contact flex that fixes all diametral-pair relative
  displacements. With \(s\) stressed vertices, \(m\) unit contacts, and \(k\)
  diameter edges, its rank argument gives \(m\ge2s-6k\). This does **not**
  prove that the stress spine covers all but \(O(\sqrt n)\) source vertices.
- If the spine covers \(n-O(\sqrt n)\) vertices, the contact graph has
  \(n-O(\sqrt n)\) strict unit-rhombus faces with total angular excess
  \(O(\sqrt n)\). The co-large-spine premise remains open.
- A sufficiently large source wholly contained in a two-direction unit
  lattice cannot be a triangle-free global minimizer **with an ordinarily
  infinitesimally rigid active bar framework**. A separate exact convex-hull
  unit-rhombus tiling obstruction does not need that rigidity premise, but its
  proof relies on a standard convex zonotopal train-track intersection fact.
- The paper gives a valid train-angle stationarity condition and an explicit
  regression against universal **uniform-shear** descent.

**Audit corrections and boundaries:** Its equation (27) is necessary
first-order stationarity, not a finite boundary-pinning certificate.
Question 8.1's claimed equivalence between stationarity and pinning is not
proved. The audited entry supplies an exact nine-point strict-rhombus disk
with \(0\) in the convex hull of its diameter gradients and a finite,
contact-preserving strict diameter decrease. The paper's \(T=\Theta(\sqrt n)\)
description needs an upper-bound hypothesis beyond its general lower bound
\(T\ge2\sqrt n-2\).

The paper's KKT theorem, near-rhombic reductions, and train-angle equilibrium
overlap substantially with existing canonical work in
[shared theory](theory/01-local-structure.md) and
[Target B Section 40](targets/target-b/01-jammed-rhombic-branch.md).
An [unreviewed October 2 C-II affine-core report](reports/target_c_affine_core_diameter_shell_exclusion_2026-10-02.md)
has a different, stronger candidate at its precise canonical-source scope.
This literature import **does not promote** that report, change theorem state,
or close Target B, Target C-II, or Level I.

The independent audit directly checks the manuscript's proof steps. External
classical references and the convex zonotopal crossing result were not all
reproved from their original sources. **Audited** describes that bounded
review, not full formal verification or peer review. No copy of the preprint
PDF is redistributed by this change.
