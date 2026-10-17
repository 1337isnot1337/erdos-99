> Generated reading edition · [exact source](../../../docs/problem/literature_archit_das_stress_rhombic_audit_2026-10-08.md) · source SHA-256 `554b1ec5a0aa25342eb319a0879d2fb2c4fb25046cbc13eeb4dabf9a64c362c7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Independent audit of new literature: Das, stress and rhombic reductions (2026)

**Literature entry:** Archit Das, *Stress, rigidity and rhombic reductions for an Erdos minimum-diameter problem (Problem #99)*. Zenodo preprint, version 1, published September 15, 2026. [Record](https://zenodo.org/records/22768362); [DOI](https://doi.org/10.5281/zenodo.22768362).

**Source identity:** Zenodo record 22768362, file erdos99_stress_rhombic_reductions_dcg_final.pdf. The PDF reviewed on October 8 had SHA-256 ad57a6668f6882315ba4b422fb247f4fde6ce4ff515824eab52e0a3f82e82c3a.

**Review date:** October 8, 2026. **Run type:** independent literature and mathematical proof audit. **Repository starting point:** main at d32a55f224e484609b1557bf5b8d531869b20558, theorem state 2026-10-08.audit.148.

**Audit status:** **AUDITED, WITH EXPLICIT SCOPE LIMITS.** This is a completed independent audit of the manuscript's stated arguments and their compatibility with the repository. It is *not* peer review, a reproof of every externally cited theorem, or a theorem-state promotion. Specific results below have different dispositions. No claim in this entry becomes canonical from its presence in the literature ledger.

**Global state:** Erdős Problem #99 and Level I remain open. Target A and Target B remain open. Target C-I is closed; C-II remains open. This entry does not alter these statuses.

## Problem and notation

For each $`n\ge2`$, let $`D(n)`$ be the minimum diameter of any unit-separated $`n`$-point planar set. A Level I proof must force a unit equilateral triangle in **every** sufficiently large global minimizer.

The paper uses $`m=|E_1|`$ for the number of unit contacts and $`k=|E_D|`$ for the number of diametral pairs. Its adapted KKT contact-stress support has vertex set $`S`$ of size $`s`$. Its ordinary active bar framework consists of $`E_1\cup E_D`$.

Do not identify these objects with the canonical C-II **nonisolated positive-contact core** $`V`$, its selected active diameter set $`H`$, or the full source containing contact-isolated points. Such identifications need their own theorem.

## Audited claim dispositions

| Paper item | Audit | Exact scope and dependency |
| --- | --- | --- |
| Lemma 2.1 and Corollary 2.2 | Audited-working; valid | Translated triangular-lattice averaging gives $`D(n)^2\le(2\sqrt3/\pi)n`$; the planar isodiametric inequality gives $`\operatorname{area}(\operatorname{conv}A)\le\sqrt3n/2`$. |
| Lemmas 2.3–2.4 and equation (6) | Audited-working, external dependency | Straight unit-contact edges do not properly cross. Hull vertices number at most $`\pi D`$. The bound $`k\le h(A)`$ uses the classical planar diameter-pair theorem. |
| Lemma 3.1, equations (10)–(12) | Audited-working; valid; duplicate | MFCQ follows from $`v_i=p_i,\ \tau=3D^2`$. KKT gives normalized nonnegative contact/diameter equilibrium and $`\sum\lambda=D^2`$. Canonical repo Theorem 4.1 already proves this and a stronger tensor identity. |
| Lemma 3.2 (adapted stress) | Audited-working; valid | There exists a normalized KKT stress supported only on contact edges that every flex in $`F(A)`$ freezes **pointwise in relative velocity**. Uses a generic flex, finite inactive margins, and compact multipliers. |
| Lemma 3.3 and Theorem 1.2 (spine count) | Audited-working; valid | $`m\ge2s-6k`$. The result does not assert that $`s=n-O(\sqrt n)`$, that all vertices are stressed, or that the full source is infinitesimally rigid. |
| Theorem 1.3 | Audited-working; valid conditional implication | If $`s=n-O(\sqrt n)`$, then $`m=2n-O(\sqrt n)`$; the contact graph has $`n-O(\sqrt n)`$ rhombus faces and angular excess $`O(\sqrt n)`$. The co-large-spine premise is not proved. |
| Proposition 1.4 and Proposition 4.1 | Audited-working; external dependency | If the ordinary active bar framework is infinitesimally rigid, $`m+k\ge2n-3`$. Eppstein's triangle-free penny-graph bound forces $`k=\Omega(\sqrt n)`$. Ordinary bar rigidity is a substantive additional hypothesis. |
| Lemma 5.1 | Audited-working; valid | Euler's face-defect identity correctly counts components, bridges, and repeated outer-face incidences. |
| Propositions 5.2–5.3 | Audited-working; valid | Near-maximal contacts imply almost all bounded faces are strict unit rhombi. Their total angular excess is $`O(\sqrt n)`$ by face area and concavity of sine. |
| Lemma 6.1 | Audited-working; valid | For unit lattice generators with angle strictly between $`\pi/3`$ and $`2\pi/3`$, unit contacts use only the two grid axes. Hence $`m\le2n-2\sqrt n`$. |
| Lemma 6.2 | Audited-working; external dependency | The Jarník convex lattice-polygon bound, under a uniformly conditioned affine transformation, yields $`h(A),k=O(D^{2/3})`$. For minimizers this is $`O(n^{1/3})`$. |
| Theorem 1.5 | Audited-working; valid under rigidity | $`m\ge2n-3-O(n^{1/3})`$ contradicts $`m\le2n-2\sqrt n`$. It excludes sufficiently large **fully lattice-supported, ordinarily active-rigid** minimizers. |
| Lemma 7.1 | Dependency-qualified | The claimed pairwise crossing of track direction classes in a convex rhombus tiling needs an explicit zonotopal train-track theorem or a complete proof. Conditional on that standard fact, at most two projective edge directions occur in a triangle-free tiling. |
| Theorem 1.6 | Audited-working, conditional on Lemma 7.1 | A global minimizer whose complete convex hull is tiled edge-to-edge by unit rhombi cannot be triangle-free for sufficiently large $`n`$. This does not cover nonconvex, incomplete, holed, or multigrain rhombic complexes. |
| Section 8, equations (22)–(26) | Audited-working under the disk hypotheses | Train counts, the $`T`$-track displacement representation, and its derivative are correct for the stated simple rhombus disk. |
| Section 8, equation (27) | Audited necessary condition | Zero belongs to the convex hull of active diameter gradients at an interior train-angle **local minimum**. This is not a sufficient condition for finite pinning or strict local optimality. |
| Section 8, Question 8.1, “equivalently” | **Unproved implication; do not import** | Convex-gradient stationarity and geometric pinning of all train rotations are not equivalent from the stated hypotheses. A finite exact regression appears below. |
| Section 8, $`T-1=\Theta(\sqrt n)`$ | Needs scope qualifier | $`q=n-T-1\le T^2/4`$ yields only $`T\ge2\sqrt n-2`$. An upper bound requires a boundary-size or near-maximal-contact hypothesis. |
| Section 9.1, equation (28) | Audited-working; valid | Triangle-free unit-separated configurations can approximate the global minimum diameter arbitrarily closely without attaining it. There is no fixed positive triangle-free diameter gap. |
| Section 9.2, Proposition 9.1 | Audited-working; valid restricted regression | Explicit two-direction finite patches have a strict cusp minimum under *uniform shear* at $`\theta=\pi/3+\Theta(1/n)`$. They are not certified against general deformations or globally optimal. |
| Section 9.3 | Audited-working as a limitation | A unit chain with one diameter cable supports concentrated KKT stress. This prevents deducing a large stress spine from normalization alone. The chain is not asserted globally optimal. |

“**Audited-working**” here identifies the result of this **external-source proof audit**, not a manifest promotion. The standard outside inputs (Eppstein, Jarník, planar diameter-pair bound, zonotopal track fact) were checked for their stated role but were not independently reproved from the original publications.

## 1. Adapted stress-spine argument: exact transferable statement

The strongest useful presentation difference is Lemma 3.2's choice of stress.

Define the linear flex space
```math
F(A)=\{v:(p_i-p_j)\cdot(v_i-v_j)=0\ (ij\in E_1),\quad v_i=v_j\ (ij\in E_D)\}.
```
Call a contact $`ij`$ frozen when $`v_i=v_j`$ for **every** $`v\in F(A)`$. The latter is stronger than a first-order zero length derivative.

Choose one $`v\in F(A)`$ with $`v_i\ne v_j`$ on every nonfrozen contact. Such a vector exists because a finite union of proper linear subspaces cannot cover $`F(A)`$. Under $`p_i(\varepsilon)=p_i+\varepsilon v_i`$, each nonfrozen contact satisfies
```math
|p_i(\varepsilon)-p_j(\varepsilon)|^2=1+\varepsilon^2|v_i-v_j|^2>1.
```
Frozen contacts and all originally diametral pairs retain their exact lengths. Originally inactive pairs retain positive margins for small $`\varepsilon`$.

The perturbed source is therefore a global minimizer of the same cardinality and diameter. Compactness of its normalized nonnegative KKT multipliers yields a limiting KKT stress at the original source. Every nonfrozen contact multiplier is zero.

If its positive contact graph has $`c`$ components and $`s`$ incident vertices, each component meets a positive diameter-stress endpoint. Consequently $`c\le2k`$. Contact bar rows and two coordinate rows for each diameter edge yield
```math
2(s-c)\le\operatorname{rank}M\le m+2k,\qquad
\boxed{m\ge2s-6k}.
```

**Novelty disposition:** An independently audited *external formulation and proof* useful for comparison. Do not call it a new canonical theorem or infer that its stress support is the selected canonical C-II support. The missing bridge is a quantitative bound on $`n-s`$ for every relevant global-minimizer representative.

## 2. The exact two-direction lattice result adds no C-II closure

Theorem 1.5 makes an elegant restricted contradiction. Its hypotheses require the *whole source* inside one lattice and the *whole active bar framework* to be infinitesimally rigid.

The existing [2026-10-02 affine-core report](../reports/target_c_affine_core_diameter_shell_exclusion_2026-10-02.md) has a stronger candidate for the selected C-II representative. It only requires its loaded positive-contact core to lie in one exact unit oblique lattice. It uses the selected $`H`$ diameter-edge floor instead of full-source ordinary rigidity. **That report is unreviewed and noncanonical unless separately promoted.**

Neither result handles drifting train directions, approximate affine charts, multiple coherent grains, or source-preserving finite diameter shortening. The new source is useful as independent support and a clean proof model, not as a replacement for the current C-II frontier.

## 3. Convex rhombus tilings: an independently useful restricted obstruction

Under the convex zonotopal track-intersection fact of Lemma 7.1, three projective edge directions force one crossing angle at most $`\pi/3`$. A triangle-free unit-separated rhombus tiling therefore uses at most two directions.

A convex two-direction tiling has a parallelogram hull. For $`q`$ rhombi and $`b`$ unit boundary edges,
```math
q=n-b/2-1=n-O(\sqrt n).
```
Every strict triangle-free unit rhombus has area greater than $`\sqrt3/2`$. Therefore
```math
\operatorname{area}(K)>\frac{\sqrt3}{2}n-O(\sqrt n).
```
But a parallelogram of diameter $`D(n)`$ has
```math
\operatorname{area}(K)\le D(n)^2/2\le\frac{\sqrt3}{\pi}n,
```
a contradiction for large $`n`$.

**Dependency:** Verify or prove the required pairwise-crossing statement for distinct direction classes of a convex edge-to-edge rhombus tiling. Do not apply the theorem to a nonconvex or only near-rhombic core. There is no new unconditional Target B or C-II exclusion.

## 4. Exact regression: train-gradient stationarity is not finite pinning

The paper's equation (27) is a *necessary* first-order condition:
```math
0\in\operatorname{conv}\{\nabla_\phi |p-q|^2:|p-q|=D\}.
```
It does not assert a strict local minimum and cannot exclude a second-order diameter decrease.

Here is an explicit, exact **nine-point** rhombus-disk regression. It illustrates the missing implication and is not a Level I counterexample.

At the initial position, take the $`3\times3`$ square grid
```math
p_{ij}(0)=(i,j),\qquad i,j\in\{0,1,2\}.
```
Its only active diameter pairs are the two opposite corner diagonals. The squared diameter is $`8`$. Use train-angle coordinates for two horizontal tracks and two vertical tracks. Their active squared-diameter gradients at the square embedding are
```math
g_+=(4,4,-4,-4),\qquad g_-=-g_+.
```
Thus $`0=(g_++g_-)/2`$ satisfies equation (27).

Now put
```math
u_1=(c,s),\quad u_2=(c,-s),\quad v_1=v_2=(0,1),\quad
c^2+s^2=1,\quad c<1,
```
and set
```math
p_{ij}=\sum_{a=1}^{i}u_a+j(0,1).
```
For small positive $`s`$, every former unit contact stays exactly unit length. Every former noncontact remains strictly longer than one by continuity. All four cells remain nondegenerate strict unit rhombi.

Both old diameter pairs shorten to
```math
4c^2+4=8-4s^2<8.
```
All other pairs had squared distance at most $`5`$ at $`s=0`$; hence they remain shorter than the old and new diameter for sufficiently small $`s>0`$. This is an actual same-cardinality finite descent in the entire rhombus disk.

An explicit rational certificate is
```math
(c,s)=\left(\frac{220}{221},\frac{21}{221}\right).
```
Exact enumeration of all $`\binom92=36`$ pairs yields minimum squared separation $`1`$, exactly 12 unit contacts, and
```math
\operatorname{diam}^2=\frac{388964}{48841}
=8-\frac{1764}{48841}<8.
```
The two opposite corner pairs remain the unique diametral pairs. The certificate uses only rational coordinates and squared distances.

**Regression conclusion:** The implication “equation (27) implies finite boundary pinning” is false, even for a complete strict unit-rhombus disk. The paper only proves the necessary condition. Its Question 8.1 does not establish equivalence between the condition and pinning. The finite example does **not** decide the paper's separate question about *asymptotically diameter-optimal sequences*.

The repository already gives the more relevant source-specific finite-motion tests in [Target B, Section 40 onward](../targets/target-b/01-jammed-rhombic-branch.md). Any future argument needs second-order or finite feasibility, plus all contacts and inactive-pair margins.

## 5. Uniform-shear regression

For the paper's centrally symmetric two-direction patch, the two competing squared radii are
```math
2m^2+2+2(m^2-1)c,\qquad 5m^2-4m^2c,
```
where $`c=\cos\theta`$. They cross at
```math
c_m=\frac{3m^2-2}{2(3m^2-1)}
=\frac12-\frac1{2(3m^2-1)}.
```
The resulting shear angle obeys
```math
\theta_m-\pi/3=\frac1{3\sqrt3m^2}+O(m^{-4}).
```
The maximum of the two competing radii has a strict cusp minimum at that angle. The example rules out a universal *uniform-shear* descent claim. It does not satisfy a global-minimizer certificate and does not obstruct a different train-angle motion.

## 6. Crosswalk to established repository work

| External paper | Existing repository work | Import decision |
| --- | --- | --- |
| KKT / MFCQ / total stress | [Shared theory, Theorem 4.1](../theory/01-local-structure.md) | Existing canonical theorem is stronger. Use the paper as supporting literature. |
| Rhombic face defect / angular excess | [Shared theory, Section 10](../theory/01-local-structure.md) | Existing canonical scope already covers the basic result. |
| Train tracks and $`R\le T^2/4`$ | [Shared theory, Theorem 10.6](../theory/01-local-structure.md) | Existing theorem handles holes and disconnected complexes. |
| Boundary stationarity | [Target B, Section 40](../targets/target-b/01-jammed-rhombic-branch.md) | Already present. Do not promote equation (27) as new. |
| Fixed-direction structural obstructions | [Shared theory, Theorem 10.12](../theory/01-local-structure.md), [affine-core candidate](../reports/target_c_affine_core_diameter_shell_exclusion_2026-10-02.md) | Different hypotheses. Preserve distinctions and candidate status. |
| Boundary-pinned false positives | [Shared theory, Proposition 10.10](../theory/01-local-structure.md), [nonlinear regressions](../theory/02-nonlinear-and-regressions.md) | The exact $`3\times3`$ example is a small illustrative additional regression, not a new closure. |

## 7. Final ledger decision and exact missing bridges

**New literature import:** Yes. This is an audited direct preprint with precise theorem-level qualifications.

**Canonical theorem promotion:** None. No state manifest, target route map, or active prompt changes follow from this source alone.

**Use as premises:** The directly audited elementary results are externally supported research inputs. Check any noncanonical application against the source's complete hypotheses. The convex zonotopal track theorem remains an external dependency. Neither source-wide peer review nor independent reproduction of all outside references is claimed.

**Target B's unresolved step:** Prove the canonical multi-grain/global shell-stability inequality with topology and boundary corrections, or construct a full-source finite strict-$`D`$ competitor.

**Target C-II's unresolved step:** Build a finite source-preserving motion or payment theorem that incorporates actual loaded endpoints, all active and inactive pairs, and contact-isolated points.

**Level I:** Still open. A literature audit or a stationary rhombus model cannot settle its universal global-minimizer quantifier.
