# Target C-II — sub-square-root external population forces two FREE modules onto common lower runs

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only multi-module refinement in the small-external branch  
**Scope:** full-order residual all-inactive FREE family with `Z_D=|A\setminus F|=o(sqrt(D))`  
**Dependencies:** ordered two-normal shared skeleton; two-sided outer-face localization; external-population upper-gate injection; slow-scale module extraction  
**Certificate:** `research/verify_target_c_tooth_reflection_small_external_common_lower_runs_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The joint terminal/external theorem already shows that `Z_D=o(sqrt(D))` forces one very long lower run. The multi-module reuse results give a different conclusion: after tuning the slow reflection scale to `Z_D`, either the source contains a superlinear inverse-`D` matching, or two distinct FREE modules share a growing family of the same near-unit gates **inside one all-lower run of each ancestry**.

Write

\[
Z_D:=|A\setminus F|,
\qquad
F=\operatorname{conv}B,
\]

and assume

\[
\boxed{Z_D=o(\sqrt D).}
\tag{CR.1}
\]

In the residual branch, suppose a full-order family of all-inactive non-anchored FREE modules survives after the exact-anchor alternatives are removed.

Choose the slow reflection scale

\[
\boxed{
\kappa_D:=\max\{\log\log D,\sqrt{Z_D+1}\}.
}
\tag{CR.2}
\]

Then

\[
\kappa_D\to\infty,
\qquad
\kappa_D=o(D^{1/4}),
\tag{CR.3}
\]

so the slow-scale extraction is available. Retain a full-order residual family of size

\[
\boxed{
m=\Theta(D^{1/4}/\kappa_D).}
\tag{CR.4}
\]

In particular `m->infinity`, and consecutive retained normals have gap

\[
\gamma_D=\Theta(\kappa_DD^{-1/4}),
\qquad
m\gamma_D=\Theta(1).
\tag{CR.5}
\]

Apply the two-normal theorem with

\[
\omega_D:=\sqrt m.
\tag{CR.6}
\]

Then at least one of the following holds.

### EXTERNAL-MATCHING

There is a vertex-disjoint matching of old fully inactive outer-face source pairs of size

\[
\boxed{\Omega(D\sqrt m)}
\tag{CR.7}
\]

with

\[
1<|x-y|\le1+{K\over D}
\tag{CR.8}
\]

for any fixed `K>h_*` used in the extraction. Since `m->infinity`, this is superlinear in `D`.

### COMMON-LOWER-RUNS

There are two fixed selected modules `i,j` and one maximal all-lower run `R_i` in ancestry `i` and one maximal all-lower run `R_j` in ancestry `j` such that the two runs contain the same vertex-disjoint family `Q^*_{ij}` of original inverse-`D` near-unit edges, with

\[
\boxed{
|Q^*_{ij}|
\ge
\left(\sqrt{\alpha_K/44}-o(1)\right)
{\sqrt D\over m(2Z_D+3)}.
}
\tag{CR.9}

The family is order coherent: along the two lower runs the shared edges occur either in the same order or in reverse order, and all have the same relative traversal orientation inherited from the ordered-skeleton theorem.

Using (CR.4),

\[
|Q^*_{ij}|
=\Omega\left({\kappa_DD^{1/4}\over Z_D+1}\right).
\tag{CR.10}
\]

The choice (CR.2) makes this diverge. Indeed,

\[
{\kappa_DD^{1/4}\over Z_D+1}
\ge
{D^{1/4}\over\sqrt{Z_D+1}}
\longrightarrow\infty
\tag{CR.11}
\]

under (CR.1). Therefore

\[
\boxed{|Q^*_{ij}|\to\infty.}
\tag{CR.12}

Every shared edge still satisfies

\[
1<|e|\le1+{K\over D},
\tag{CR.13}
\]

and the two module repairs turn that same edge into an exact unit gate. The low-activation refinement from the two-normal theorem may be retained before the run-pair pigeonhole, so the selected shared gates also inherit the corresponding `O(m^2/D)` activation-time bound after an additional constant-factor thinning if required.

The normal separation of the two modules is at least

\[
\Omega(m^{-1/2}),
\tag{CR.14}
\]

because `omega_D=sqrt(m)` and `m gamma_D=Theta(1)`.

This removes another escape in the small-external regime. The common two-normal skeleton cannot be dispersed among `Z_D+1` different lower runs forever: because every upper gate consumes a distinct external source point, the number of run changes is too small. A hard survivor has two genuinely all-lower plane paths carrying a growing common set of inverse-`D` gates.

The next obstruction is now purely planar/topological: classify two simple paths in the common sub-`sqrt(2)` source-pair graph which share an unbounded ordered matching of near-unit edges while arising from two separated support directions. No upper-gate jump remains between the first and last selected shared gates on either path.

---

## 1. The `Z_D`-adapted slow scale is admissible

Equation (CR.1) implies

\[
\sqrt{Z_D+1}=o(D^{1/4}).
\]

Also `log log D=o(D^(1/4))`. Hence (CR.2) gives (CR.3).

Moreover,

\[
{D^{1/4}\over\kappa_D}\to\infty.
\]

If the maximum in (CR.2) is `sqrt(Z_D+1)`, this follows from `Z_D=o(sqrt(D))`; if it is `log log D`, it is immediate. Thus the retained module count in (CR.4) diverges.

The slow-scale normal gap is `Theta(kappa_D D^(-1/4))`, so multiplying by (CR.4) proves (CR.5).

---

## 2. There are at most `Z_D+1` lower runs per all-inactive ancestry

On an all-inactive two-sided FREE ancestry, every upper-gate child is an old source point outside the force hull `F`. A source vertex activates only once along one ancestry, so distinct upper gates have distinct child vertices. Therefore

\[
\boxed{U_i\le Z_D}
\tag{CR.15}
\]

for each selected module ancestry.

Deleting the `U_i` upper edges partitions the lower edges into at most

\[
\boxed{U_i+1\le Z_D+1}
\tag{CR.16}
\]

maximal all-lower runs.

---

## 3. Order coherence makes the run-pair sequence change only `O(Z_D)` times

In the TWO-NORMAL-SKELETON branch, the ordered-skeleton theorem supplies

\[
Q_{ij}
\]

with

\[
|Q_{ij}|
\ge
\left(\sqrt{\alpha_K/44}-o(1)\right){\sqrt D\over m}.
\tag{CR.17}
\]

List `Q_ij` in its occurrence order along ancestry `i`. For an edge `e`, let

\[
r_i(e),\qquad r_j(e)
\]

be the indices of the maximal lower runs containing `e` in the two ancestries.

Along the chosen order, `r_i(e)` is nondecreasing. By order coherence, `r_j(e)` is either nondecreasing for the entire sequence or nonincreasing for the entire sequence. The first coordinate changes at most `Z_D` times by (CR.16), and the second coordinate changes at most `Z_D` times. Hence the pair

\[
(r_i(e),r_j(e))
\]

changes at most `2Z_D` times.

Thus `Q_ij` splits into at most

\[
2Z_D+1
\]

contiguous blocks with a constant lower-run pair. Using `2Z_D+3` in the denominator absorbs endpoints and integer rounding uniformly. One block therefore has size at least (CR.9). Call it `Q^*_ij`, and denote its two fixed runs by `R_i,R_j`.

Because both selected edges of every interval lie in the same maximal lower run, the complete ancestry segment between them contains no upper gate. Hence between the first and last edges of `Q^*_ij`, both selected module ancestries are entirely lower-gate paths in the common plane short-edge graph.

---

## 4. The shared run-pair population diverges

Combining (CR.9) with (CR.4) gives (CR.10). By (CR.2),

\[
\kappa_D\ge\sqrt{Z_D+1},
\]

and therefore

\[
{\kappa_DD^{1/4}\over Z_D+1}
\ge
{D^{1/4}\over\sqrt{Z_D+1}}.
\]

The right side tends to infinity exactly because `Z_D=o(sqrt(D))`. This proves (CR.11)--(CR.12).

No claim is made that the two lower runs are distinct as geometric paths. If they coincide on a long trunk, that is already a strong shared-corridor outcome. If they repeatedly diverge and rejoin, the union contains a correspondingly nontrivial planar near-unit routing structure. Distinguishing those two cases is the next finite graph-geometric seam.

C-II remains open. No theorem-state authority is changed.

**Disposition:** in the `Z_D=o(sqrt(D))` residual FREE branch, tuned the slow reflection scale so that the heavy-reuse alternative yields two fixed all-lower plane runs sharing an unbounded ordered matching of the same inverse-`D` source pairs; otherwise a superlinear inverse-`D` matching is already present.