<!-- theorem-state: {"artifact_id":"ART-A367F8F44DF0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e6f881a1276f3e2196b3ef6d807b1c31add508c5", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/campaign_boundary_defect_matching_2026-09-09.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2667ff491b48b847cc633833a74c629894fffca1a153b75b149514c03d3e868d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — boundary defect rank and non-diameter response matching

**Date:** 2026-09-09  
**Repository state:** `4bc7c9baddb38d12cbadde8394992c0e9f708104`  
**Run type:** closing-proof continuation / dependency audit  
**Target:** Target C Gate C-II / Level I  
**Active prompt:** user-supplied Target C–Z settlement prompt, 2026-09-09  
**External web search:** used only to inspect Gorbounov–Kazakov 2026; not used in the proof  
**Computation:** not used in the proof

## LEVEL I STATUS

`STILL OPEN`

The Z -> ZC -> ZR -> ZF route survives the dependency audit already recorded in the September 9 campaign reports. The exact face inequality

\[
b+\sum_{F\text{ bounded}}(\deg F-4)>2|H|
\]

is still not proved.

This run proves a new exact response consequence of ZR. The Schur-reduced boundary defect

\[
M=\Lambda-L_H
\]

has **exact** kernel equal to the three affine boundary modes and exact rank `q-3`. In particular every terminal has positive diagonal defect and every terminal row of `M` contains both signs off the diagonal. Combining this with the geometric-thrackle bound on the full diameter graph and the C41 harmonic-response decomposition gives a terminal-disjoint matching of at least `q/16` strictly non-diameter response pairs. Since C33 gives `q >= (ceil(D)+2)/2`, this supplies linearly many terminal-disjoint subdiameter response channels.

The result removes the combinatorial-extraction part of the small-trace response problem. It does **not** lower-bound the aggregate conductance of those channels. That quantitative mass bound is now the shortest response-side obstruction exposed by this run.

## 1. Starting endpoint

Under the audited report-level Z route, a sufficiently large lexicographically normalized triangle-free global minimizer in C-II has:

- the full positive contact core `C` on `v` nonisolated vertices;
- the full diameter graph `H` on the loaded terminal set `B`, `q=|B|`;
- a relative-interior normalized KKT stress `(alpha,beta)` with every contact and diameter row positive in support;
- scalar stress matrix

\[
\Omega=L_C(\alpha)-L_H(\beta)\succeq0;
\]

- ZR:

\[
\ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\},
\qquad
\operatorname{rank}\Omega=v-3;
\]

- ZF:

\[
e+|H|\ge2v-2.
\]

The exact scalar closure remains

\[
\boxed{b+\sum_F(\deg F-4)>2|H|,}
\]

which is equivalent by Euler to `e+|H|<2v-2` and would contradict ZF.

The response-side alternative remained less sharp. C64 gives only

\[
M=\Lambda-L_H\succeq0,
\qquad
M\mathbf1=MP_B=0,
\]

and its transport inequality for any matching `J` of non-diameter response pairs:

\[
\sum_{ij\in J}c_{ij}\le\frac12\operatorname{tr}M.
\]

The missing combinatorial question was whether the actual source necessarily supplies a large terminal-disjoint family to which this inequality can be applied.

The implication established here is

```text
ZR maximal scalar-stress rank
    -> exact boundary-defect rank q-3
    -> every terminal has strict defect and mixed row signs
    -> every diameter-degree <=2 terminal sees non-diameter response
    -> at least q/2 terminals see non-diameter response
    -> C41 atom decomposition + C15
    -> a non-diameter response matching of size >=q/16
    -> C64 matching transport applies on Omega(D) disjoint channels.
```

## 2. Strongest genuinely new audited theorem

### Theorem ZM — full boundary-defect rank and a linear non-diameter response matching

Assume the audited C-II/ZR hypotheses for a sufficiently large lexicographically normalized triangle-free global minimizer. Let

- `B` be the loaded terminal set, `q=|B|`;
- `H` be the full active diameter graph on `B`;
- `Lambda` be the C11 Dirichlet-to-Neumann response of the positive contact core on `B`;
- `L_H` be the relative-interior `beta`-weighted diameter Laplacian;
- `M=Lambda-L_H`;
- `c_{ij}=-Lambda_{ij}` for `i!=j`;
- `G_0` be the graph on `B` whose edges are the pairs `ij` with `c_{ij}>0` and `ij notin H`.

Then:

1. **Exact boundary rank**

\[
\boxed{
\ker M=\operatorname{span}\{\mathbf1,P_{B,x},P_{B,y}\},
\qquad
\operatorname{rank}M=q-3.
}
\tag{ZM.1}
\]

2. **Strict terminal defect**. For every `b in B`,

\[
\boxed{d_b:=M_{bb}>0.}
\tag{ZM.2}
\]

3. **Mixed terminal signs**. Every terminal row has at least one positive and one negative off-diagonal entry. Since `M_{bk}=-c_{bk}<=0` off the diameter support, every `b` is incident to a diameter edge `bk` satisfying

\[
\boxed{\beta_{bk}>c_{bk}.}
\tag{ZM.3}
\]

4. **Low diameter degree forces non-diameter response**. If `deg_H(b)<=2`, then `b` is nonisolated in `G_0`.

5. **Linear terminal-disjoint response matching**. The graph `G_0` has a matching `J` with

\[
\boxed{|J|\ge\frac q{16}.}
\tag{ZM.4}
\]

Every edge of `J` is a strictly subdiameter terminal pair with strictly positive response conductance. Consequently, using C33,

\[
\boxed{|J|\ge\frac{\lceil D\rceil+2}{32}.}
\tag{ZM.5}
\]

up to the harmless integer rounding implicit in the displayed real lower bounds.

Finally C64 applies to this matching:

\[
\boxed{
0<\sum_{ij\in J}c_{ij}
\le\frac12\operatorname{tr}(\Lambda-L_H).
}
\tag{ZM.6}
\]

### Scope

ZM concerns the actual contact response and full diameter graph of the same sufficiently large lexicographically normalized global minimizer used by ZR. It does not replace the source by an electrically equivalent network or a different hull. It excludes contact-isolated source points from `v`, exactly as ZR does, but the terminal set `B` is the actual loaded boundary of that core.

ZM is exact. No asymptotic lower bound on any conductance is claimed.

### Proof

#### Step 1. Schur congruence gives the exact boundary nullity

Order the positive contact core by `B,I`, where `I=V(C)\setminus B`. Write the positive contact Laplacian as

\[
L_C=
\begin{pmatrix}
A_{BB}&A_{BI}\\
A_{IB}&A_{II}
\end{pmatrix}.
\]

C64 proves `A_{II}` is positive definite. Since the diameter Laplacian is supported only on `B`,

\[
\Omega=
\begin{pmatrix}
A_{BB}-L_H&A_{BI}\\
A_{IB}&A_{II}
\end{pmatrix}.
\]

The Schur complement of `A_{II}` is

\[
M=A_{BB}-L_H-A_{BI}A_{II}^{-1}A_{IB}
=\Lambda-L_H.
\]

Standard block congruence gives

\[
\Omega\sim
\begin{pmatrix}
M&0\\0&A_{II}
\end{pmatrix}.
\tag{ZM.7}
\]

Because `A_{II}` is nonsingular,

\[
\operatorname{nullity}M=\operatorname{nullity}\Omega.
\]

ZR gives `nullity Omega=3`. C11 gives

\[
M\mathbf1=MP_{B,x}=MP_{B,y}=0.
\]

The terminals are vertices of a strictly convex force hull, so the three affine boundary columns are independent. Hence they already span the whole kernel. This proves ZM.1.

#### Step 2. Every diagonal defect is strictly positive

C64 gives `M succeq 0`. For a PSD matrix,

\[
|M_{ij}|^2\le M_{ii}M_{jj}.
\]

Suppose `M_{bb}=0`. Then the entire `b`-row and `b`-column vanish, so the coordinate vector `e_b` belongs to `ker M`.

By ZM.1 this would mean that there is an affine function

\[
f(x,y)=a+ux+vy
\]

whose values on the terminal polygon are `1` at `b` and `0` at every other terminal. Since `q>=6` in the ZC regime, at least five distinct vertices of the strictly convex polygon would lie on the zero line of `f`. A line contains at most two vertices of a strictly convex polygon unless `f` is identically zero. Either alternative contradicts `f(b)=1`.

Therefore `M_{bb}>0` for every `b`, proving ZM.2.

#### Step 3. Every terminal row contains both signs

The affine kernel identity gives, row by row,

\[
\sum_{k\ne b}M_{bk}(p_k-p_b)=0.
\tag{ZM.8}
\]

Because `b` is a vertex of a strictly convex polygon, there is a strict supporting functional `n_b` such that

\[
n_b\cdot(p_k-p_b)>0
\qquad(k\ne b)
\]

after choosing the inward sign of `n_b`.

If every off-diagonal `M_{bk}` were nonpositive, dotting ZM.8 with `n_b` would give a strictly negative sum unless the entire row vanished. The row cannot vanish by ZM.2. Hence some off-diagonal entry is positive.

On the other hand `M\mathbf1=0` and `M_{bb}>0`, so

\[
\sum_{k\ne b}M_{bk}=-M_{bb}<0.
\]

Thus some off-diagonal entry is negative as well.

For `bk notin H`,

\[
M_{bk}=\Lambda_{bk}=-c_{bk}\le0.
\]

Therefore every positive off-diagonal entry lies on `H`, and there is an incident diameter edge with

\[
M_{bk}=\beta_{bk}-c_{bk}>0.
\]

This proves ZM.3.

#### Step 4. Diameter degree at most two forces a non-diameter response neighbor

Fix `b` with `deg_H(b)<=2`. Suppose for contradiction that `b` is isolated in `G_0`. Then every non-diameter pair `bk` has `c_{bk}=0`, so every nonzero off-diagonal entry in row `b` of `M` is supported on the at most two diameter neighbors of `b`.

By Step 3 the row has both a positive and a negative off-diagonal entry. Thus `deg_H(b)=2`, with distinct diameter neighbors `k,l`, and ZM.8 becomes a nontrivial linear relation between the two vectors

\[
p_k-p_b,\qquad p_l-p_b.
\]

Those two vectors are linearly independent. Indeed both have length `D`. If they were collinear, equal orientation would force `k=l`, while opposite orientation would give `|p_k-p_l|=2D>D`, impossible in a source of diameter `D`.

This contradicts ZM.8. Hence every terminal of diameter degree at most two is nonisolated in `G_0`.

#### Step 5. At least half the terminals have diameter degree at most two

The full diameter graph is a straight-line geometric thrackle on the convex terminal set, so the Hopf-Pannwitz bound gives

\[
|E(H)|\le q.
\tag{ZM.9}
\]

There are no isolated vertices of `H` by the definition of `B`. Let `r` be the number of terminals with diameter degree at least three. Then

\[
2|E(H)|
=\sum_b\deg_H(b)
\ge3r+(q-r)
=q+2r.
\]

Using ZM.9,

\[
q+2r\le2q,
\]

so `r<=q/2`. Therefore at least `q/2` terminals have diameter degree at most two. By Step 4,

\[
N_0:=|\{b:\deg_{G_0}(b)>0\}|\ge q/2.
\tag{ZM.10}
\]

#### Step 6. The C41 response decomposition forces a large matching in `G_0`

Use the C41 decomposition. Let `I_1,...,I_s` be the connected components of the unloaded contact graph. Each component has a loaded attachment set `A_r`, and C41 proves

\[
c^{(r)}_{uv}>0
\qquad(u\ne v\in A_r).
\tag{ZM.11}
\]

The remaining response atoms are direct loaded-loaded contact edges. Such an edge has length one, so for `D>1` it is automatically a non-diameter edge and belongs to `G_0`.

A terminal `b` is incident to at most three response atoms in the following sense. Each component `A_r` containing `b` requires at least one actual contact from `b` into `I_r`; each direct loaded-loaded response atom is itself one actual contact at `b`. Distinct atoms consume distinct actual contact edges. C35 gives

\[
\deg_C(b)\le3.
\tag{ZM.12}
\]

Hence `b` belongs to at most three such atoms.

Now take a maximum matching `J` in `G_0`, write `m=|J|`, and let `U` be the set of nonisolated vertices of `G_0` left unmatched by `J`. Since a maximum matching is maximal, `U` is independent in `G_0`.

For every harmonic attachment set `A_r`,

\[
|U\cap A_r|\le2.
\tag{ZM.13}
\]

Indeed, if three unmatched vertices `u,v,w` lay in one `A_r`, C41.11 would give positive response conductance on all three pairs. Since `U` is independent in `G_0`, each of `uv,uw,vw` would then have to be a diameter edge. That would be a three-vertex diameter clique, excluded for sufficiently large global minimizers by C15 (and a fortiori by C43).

A direct loaded-loaded contact atom contains at most one vertex of `U`, because that contact edge itself lies in `G_0`.

Fix one matched endpoint `x`. Every unmatched neighbor `u` of `x` in `G_0` is supported by at least one response atom containing both `x,u`. By ZM.13 a harmonic atom contributes at most two such unmatched neighbors; a direct-contact atom contributes at most one. Since `x` belongs to at most three atoms, it has at most six unmatched neighbors:

\[
|N_{G_0}(x)\cap U|\le6.
\tag{ZM.14}
\]

There is a standard extra saving for a **maximum** matching. If `xy in J` and there were distinct unmatched vertices

\[
u\in N(x)\cap U,
\qquad
v\in N(y)\cap U,
\qquad u\ne v,
\]

then

\[
u-x-y-v
\]

would be an augmenting path, contradicting maximal cardinality of `J`. Therefore the two endpoint neighborhoods of one matched edge cannot contain distinct unmatched vertices on opposite sides. Together with ZM.14,

\[
|(N(x)\cup N(y))\cap U|\le6
\qquad(xy\in J).
\tag{ZM.15}
\]

Every `u in U` has a neighbor because `U` contains only nonisolated vertices. Every such neighbor is matched, again by maximality. Charge `u` to one matched edge incident to one of its matched neighbors. Equation ZM.15 allows at most six charges per matched edge. Thus

\[
|U|\le6m.
\tag{ZM.16}
\]

The nonisolated vertices of `G_0` are exactly the `2m` matched endpoints together with `U`, so

\[
N_0=2m+|U|\le8m.
\]

Using ZM.10 gives

\[
m\ge\frac{N_0}{8}\ge\frac q{16}.
\]

This proves ZM.4. C33 gives `2q>=ceil(D)+2`, proving ZM.5.

Every matching edge lies outside `H` and has positive response conductance by definition. C64.19 therefore yields ZM.6. `square`

### Dependencies

The proof uses only the following existing inputs.

- `docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md`: ZC and ZR, after the dependency review in the consolidated September 9 campaign.
- `docs/reports/target_c_fully_visible_response_psd_transport_2026-08-31.md`: C64, especially `M=Lambda-L_H succeq0`, the Schur setup, and matching transport.
- `docs/reports/target_c_response_diameter_defect_trace_2026-08-31.md`: C41 response decomposition and strict response clique on every harmonic attachment set.
- `docs/reports/target_c_pinned_self_stress_boundary_surplus_2026-08-31.md`: C33 boundary lower bound.
- `docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md`: C35 loaded contact degree at most three.
- canonical C15/C43: no three pairwise diametral source points for sufficiently large global minimizers.
- canonical Hopf-Pannwitz / geometric-thrackle bound `|E(H)|<=|V(H)|` for the diameter graph.

No external theorem beyond the already canonical diameter-graph edge bound is imported by the new proof.

### Why it is new

C64 records only positive semidefiniteness and an upper conductance bound **if** a terminal-disjoint non-diameter family has already been found. ZR records exact rank on the full core but does not transfer that rank to the boundary defect. The active route maps do not state `rank M=q-3`, do not state `M_bb>0` at every terminal, and do not extract a linear non-diameter response matching.

The new step is the combination of:

1. ZR with the C64 Schur congruence;
2. strict convexity to force mixed signs row by row;
3. the `|H|<=q` degree budget;
4. C41's response-atom decomposition plus C35's three-atom terminal cap; and
5. C15 to bound unmatched vertices inside one response clique.

## 3. Exact target implication

ZM does not prove the global face inequality and therefore does not contradict ZF.

It does sharpen the response endpoint. Before ZM, C64's proposed `C65-B` route required two logically separate steps:

1. find `Omega(D)` terminal-disjoint non-diameter response channels;
2. prove that such channels carry enough aggregate conductance to force a trace defect.

Step 1 is now exact. There is always a matching `J` of size at least `q/16=Omega(D)`.

Thus the small-trace response obstruction is reduced to **weight only**:

\[
\boxed{
\text{prove a source-specific lower bound on }
\sum_{ij\in J}c_{ij}
\text{ for some ZM matching }J.
}
\]

C64 would immediately turn any absolute lower bound `mu>0` into

\[
\operatorname{tr}M\ge2\mu.
\]

Even a bound of order `1/D` would be new quantitative information at the current large-defect/near-zero boundary.

The face/rank endpoint remains unchanged:

\[
\boxed{b+\sum_F(\deg F-4)>2|H|.}
\]

## 4. Exact remaining lemma

The shortest new response-side lemma is:

> **ZM mass lemma.** There is a function `mu(D)` strong enough for the C44/C64 phase split, ideally `mu(D)>=c/D` and preferably `mu(D)>=c>0`, such that every sufficiently large C-II survivor has a ZM matching `J` of non-diameter response pairs satisfying
> \[
> \sum_{ij\in J}c_{ij}\ge\mu(D).
> \]

The theorem must use the actual unit-contact embedding/global-minimum hypothesis. Positivity of the response support alone cannot supply such a bound because individual positive conductances may tend to zero.

For direct Level I closure, the shortest scalar lemma is still the stronger global statement

\[
\boxed{b+\sum_F(\deg F-4)>2|H|.}
\]

## 5. Audit of Z, ZC, ZR, ZF, and ZB

| Claim | Classification | Audit result |
| --- | --- | --- |
| Theorem Z | proved and promotable after dependency audit | The circular split representation, interval signs, projective orientation, all-gap argument, split-support exclusion, and terminal-cover upgrade survive the September 9 review. The two-edge crossing-square regression remains outside the `m>=3` hypothesis. |
| ZC | proved conditional on the stated C-II relative-interior source | For `D>=9`, `q>=6` and at least three selected diameter edges; Z plus SEPq gives an actual contact-network separator, contradicted by C26/C35 degree caps. |
| ZR | proved conditional on C56-G and ZC | The edge-defect nullity, singular-value transfer, Schur congruence, affine independence, and exclusion of contact-isolated points survive audit. ZM uses this theorem. |
| ZF | proved conditional on ZR plus the promoted C63/C65 finite active-face integration | Every critical velocity integrates in the same active face; ZR makes it affine; three diameter directions kill symmetric affine strain; row rank plus a nonzero KKT dependence gives `e+h>=2v-2`. |
| ZB | proved only for the pure simply connected strict-rhombic disk class | ZF gives `h>=T`, while the audited Target B exposed-hull theorem gives `T>q>=h` with a positive linear margin. It is not a general-topology theorem. |
| ZM | proved conditional on ZR and the same C-II source | New in this report. |

No step above upgrades report-level Z mathematics to canonical status merely by being recorded here.

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Two-edge crossing square | yes | ZM is downstream of ZC/ZR in the `D>=9`, `q>=6` regime. It does not enlarge Theorem Z to two selected edges. |
| Regular heptagon plus isolated center | yes | ZM works only on the nonisolated contact core and does not declare isolated source points diametral. |
| C43 near-Reuleaux approximants | yes | ZM says its matching pairs are strictly subdiameter, not uniformly separated from `D`. C43 does not make every such pair uniformly short. |
| Tiny-conductance / near-star response | yes | ZM proves support cardinality only. It explicitly does not infer an aggregate conductance lower bound from positivity. |
| Pure rhombic disks | yes | They are already excluded by ZB under the audited dependencies; ZM is not used to re-prove that branch. |

### Exact matrix regression against over-strengthening ZM

The rank/sign part alone cannot force more than an edge-cover-type positive support.

Take the regular hexagon

\[
p_j=(\cos(j\pi/3),\sin(j\pi/3)),\qquad j=0,\ldots,5,
\]

and let `P_aff` be the orthogonal projector onto the three-dimensional span of the sampled affine functions `1,x,y`. Put

\[
M=I-P_{aff}.
\]

Then `M succeq0`, `rank M=3=6-3`, and its kernel is exactly the affine span. Orthogonality of the Fourier modes gives

\[
M_{jj}=\frac12,
\]

and for cyclic separation `s`,

\[
M_{j,j+s}=-\frac{1+2\cos(s\pi/3)}6.
\]

Hence

- adjacent entries are `-1/3`;
- distance-two entries are `0`;
- opposite entries are `+1/6`.

Thus the positive off-diagonal support is exactly the three opposite diagonals, a perfect matching and a convex geometric thrackle. This is an algebraic regression against claims such as “maximal PSD affine-kernel rank forces positive support degree at least two” or “forces more than `q/2` positive support edges.” It is **not** asserted to realize the full unit-contact/global-minimizer response hypotheses.

## 7. Failed implications and decisive obstructions

### ZM matching count -> absolute trace gap

**Failure:** C64 gives an upper bound

\[
\sum_{J}c_{ij}\le\operatorname{tr}M/2,
\]

but ZM provides only `c_{ij}>0`, not a uniform lower bound. A linear number of positive response channels can carry arbitrarily small total mass absent an additional source-specific conductance theorem.

**Disposition:** live only with a new quantitative hypothesis. Do not infer mass from support count.

### Strictly subdiameter -> uniformly short

**Failure:** a non-diameter terminal pair can approach distance `D` arbitrarily closely. C43 guarantees a uniformly short pair in every triple, not that every non-diameter pair is uniformly short.

**Disposition:** rejected as a universal implication.

### Maximal boundary rank -> purely matrix-theoretic contradiction with a thrackle

**Failure:** the regular-hexagon projector above has exact affine kernel, maximal PSD rank, and positive support equal to a crossing diameter matching.

**Disposition:** any further contradiction must use the circular-planar response realization, actual unit-contact geometry, global optimality, or quantitative weights.

### Replacing the face inequality by the ZM response theorem

**Failure:** ZM does not bound `e+h` from above and does not control exceptional-face loss. The exact Euler currency remains

\[
\frac12\left(b+\sum_F(\deg F-4)\right).
\]

**Disposition:** ZM is a parallel response reduction, not a substitute for the face theorem.

## 8. Literature imported

### Gorbounov–Kazakov, *Metric properties of electrical networks and the graph reconstruction problems*, arXiv:2601.08465 (2026)

- Relevant statements inspected: Theorems 3.2--3.4 in the arXiv version.
- Exact useful external fact: boundary effective resistances of connected circular electrical networks are Kalmanson; Theorem 3.4 characterizes electrical Kalmanson metrics by identifying the circular split-coefficient matrix with the negative response matrix of the dual network.
- Applicability: yes to the existing circular-planar/Kalmanson layer behind Theorem Z.
- Use in ZM proof: none.
- Route effect: no new quantitative lower bound on response conductance, no face inequality, and no direct bridge from maximal defect rank to Level I. The source strengthens provenance for the Kalmanson input but does not close the remaining endpoint.

No other external literature was needed.

## 9. Computation and reproducibility

No computation is logically used.

The regular-hexagon regression is an exact Fourier/projector calculation displayed above; no numerical certificate is required.

## 10. Canonical promotion recommendation

**Hold as report pending an independent dependency review.**

The ZM proof is complete given ZR, C64, C41, C35, C15/C43, and the diameter-thrackle edge bound. It materially sharpens the response frontier, but ZR itself remains report-level in the current authority hierarchy.

Do not edit the canonical Target C route map solely from this report. If ZR is promoted after independent review, the natural promotion targets are:

- `docs/targets/target-c/README.md`;
- `docs/targets/target-c/04-near-minimal-response-frontier.md`;
- the active Target C continuation prompt;
- the campaign ledger, with ZM classified as a downstream exact response theorem.

## 11. Next run

Attack the **ZM mass lemma**, not the matching count again.

Two concrete routes survive the regressions:

1. Use C44 Branch B's macroscopic harmonic component together with ZM's terminal-disjoint matching and the component's actual unit-contact cut structure to lower-bound aggregate effective conductance at scale `1/D` or better.
2. In the small-trace phase, combine ZM with C64.17 on diameter matchings and the circular-planar split/dual representation to prove that concentrating almost all response mass on the diameter thrackle forces the additive/zero-transfer structure already excluded by ZC.

The direct face route remains the other highest-value target: prove

\[
b+\sum_F(\deg F-4)>2|H|
\]

with the full `2f_exc` exceptional-face loss retained.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem (ZM):
Under the audited ZR C-II hypotheses, M=Lambda-L_H has
  ker M = span{1,Px,Py}, rank M=q-3.
Hence every terminal diagonal defect M_bb is strictly positive and every terminal row
has both off-diagonal signs. Every diameter-degree <=2 terminal has a positive-response
non-diameter partner. Since |H|<=q, at least q/2 terminals have degree <=2.
Using the C41 response-atom decomposition, C35 loaded degree <=3, and C15 exclusion of
a diameter triangle, the non-diameter response graph contains a matching J with
  |J|>=q/16 >= (ceil D+2)/32.
C64 then gives
  0 < sum_(ij in J)c_ij <= tr(Lambda-L_H)/2.

Exact endpoint advanced:
The existence of Omega(D) terminal-disjoint non-diameter response channels is no longer
missing. Only their aggregate conductance mass remains uncontrolled.

Shortest remaining response lemma:
Prove for some ZM matching J that sum_J c_ij >= c/D (preferably >=c>0) from the actual
unit-contact/global-minimum geometry.

Shortest direct Level I lemma remains:
  b + sum_F(deg F-4) > 2|H|.

Audit:
Z, ZC, ZR, ZF survive the September 9 campaign audit under their stated dependencies;
ZB survives only in the pure simply connected strict-rhombic disk class.

Binding regressions:
No support-count-to-mass implication; no non-diameter-to-uniform-short implication;
regular-hexagon affine projector shows maximal PSD affine-kernel rank can have positive
support equal to a perfect crossing matching.

Authoritative files:
  docs/targets/target-c/56-ci-restored-frontier.md
  docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md
  docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md
  docs/reports/target_c_fully_visible_response_psd_transport_2026-08-31.md
  docs/reports/target_c_response_diameter_defect_trace_2026-08-31.md
  docs/reports/campaign_boundary_defect_matching_2026-09-09.md
```
