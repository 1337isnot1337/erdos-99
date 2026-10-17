> Generated reading edition · [exact source](../../../docs/reports/target_c_branch_ledger_common_hub_sparse_stress_2026-09-11.md) · source SHA-256 `109cdeec4cd3655a6d82972af3a1882ea033f893010d51ccb6bc043955dcce5f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-614BE5156FFC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — common hub and sparse-stress branch audit

**Date:** 2026-09-11  
**Repository state:** `8a78616` (`research/integrator-ambient-force-shell-2026-09-09`)  
**Run type:** closing proof / branch audit  
**Target:** Target C, C-II / Level I  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

This run audits two reductions against the current C-II endpoint:

1. a positive contact bridge cannot lie in every positive diameter route, so the
   common bridge-block intersection is one 2-edge-connected block; and
2. conditional on the report-level ZR/ZF mixed-rigidity chain, `s_Z` is the affine
   dimension of the normalized KKT stress polytope, and an extreme stress omits at
   least `s_Z` actual contact/diameter rows.

Neither reduction supplies the missing global packing contradiction. In particular,
the `s_Z>0` branch remains live, and the `s_Z=0` cyclic branch remains possible above
the nonexplicit threshold `0.9955405...D`.

## 1. Starting endpoint

After the promoted C-I restoration, a hypothetical counterexample is chosen to
minimize contacts and then diameter pairs, with all contact-isolated source points
retained. The exact C-II endpoint is to exclude this fully force-visible,
triangle-free global minimizer or construct a strict sub-`D` competitor.

The route-level face contradiction would require the actual mixed-row inequality

$$
e+h\le 2v-3,
$$

equivalently, by Euler for the contact core,

$$
b+Q\ge 2h+2,
$$

where `b` is the outer contact-face walk and `Q` is the bounded-face degree excess.
The exact ZF slack is

$$
s_Z=e+h-(2v-2)\ge0.
$$

Thus the circuit identity `b+Q=2h` belongs only to `s_Z=0`; it cannot be extended to
the `s_Z>0` branch.

## 2. Strongest genuinely audited theorem

### Theorem A — no universal positive contact bridge

Assume the promoted C-II force-support hypotheses, at least two selected diameter
edges, and the C24 common-route theorem. Let `I_*` be the intersection of the
bridge-block-tree paths joining the endpoints of all selected diameter edges. Then

$$
\boxed{I_*\text{ contains no positive contact bridge}.}
$$

Since C24 says `I_*` is a nonempty tree path, it follows that

$$
\boxed{I_*\text{ is a single 2-edge-connected contact block}.}
$$

This applies to both diameter-topology branches and does not assume `s_Z=0`.

#### Proof

Suppose a positive contact bridge `uv` belongs to `I_*`. Removing it separates the
positive contact graph into sides `L` and `R`, with nonempty loaded sets

$$
B_L=B\cap L,
\qquad B_R=B\cap R.
$$

C20/C22 identify these as complementary cyclic intervals of the strictly convex
loaded boundary, and the definition of `I_*` says every selected diameter pair has
one endpoint on each side.

The two complementary boundary intervals are strictly linearly separable. Indeed,
the line through interior points of the two transition edges of the intervals cuts a
strictly convex polygon into the two open boundary arcs containing `B_L` and `B_R`.
Choose a normal `ell` with

$$
\ell(p_r-p_l)>0
\quad(l\in B_L,\ r\in B_R).
$$

Orient every selected diameter edge from `B_L` to `B_R`. All oriented diameter
vectors then lie in one open half-plane, so this is one legal C53 projective cut and
orientation.

Let `Lambda` be the positive contact Dirichlet response and

$$
K=Q^{\mathsf T}\Lambda^+Q
$$

the transfer kernel on the selected diameter edges. For a unit current demand along
any cross-bridge pair `f=(r',l')`, cut conservation sends exactly one unit through
`uv`. If `alpha` is its conductance and `u in L, v in R`, then

$$
V(v)-V(u)=1/\alpha.
$$

On the `R` side, the maximum principle gives `V(r)-V(v)>=0` for every loaded
`r in B_R`; on the `L` side it gives `V(u)-V(l)>=0` for every `l in B_L`. Therefore
for every other cross-bridge pair `e=(r,l)`,

$$
K_{ef}=V(r)-V(l)\ge1/\alpha>0. \tag{A.1}
$$

It remains to compare this with the promoted C53 response identities. Write the
oriented diameter vectors in the legal projective order as

$$
u_i=a_i(1,t_i),\qquad a_i>0,
$$

and let `beta_i` be the diameter weights. Put

$$
\gamma_i=a_i\beta_i,
\quad \Gamma=\operatorname{diag}(\gamma_i),
\quad G=\sum_i\gamma_i.
$$

C53 gives

$$
M:=\Gamma(B^{-1}-K)\Gamma\succeq0,
\qquad M\mathbf1=0,
\qquad Mt=0,
$$

where `B=diag(beta_i)`. If

$$
c=\min_{i\ne j}K_{ij}>0,
$$

define `A_ij=K_ij-c>=0` for `i ne j` and let `L_A` be the weighted Laplacian

$$
(L_A)_{ij}=-\gamma_i\gamma_jA_{ij},
\qquad L_A\mathbf1=0.
$$

Then `L_A` is positive semidefinite and direct comparison of off-diagonal and
diagonal entries gives

$$
L_A=M-c(G\Gamma-\gamma\gamma^{\mathsf T}). \tag{A.2}
$$

Set

$$
t^0=t-\frac{\gamma^{\mathsf T}t}{G}\mathbf1.
$$

Because the slopes are not all equal, `t^0 ne 0`; also
`gamma^T t^0=0`. From (A.2) and `M t^0=0`,

$$
(t^0)^{\mathsf T}L_A t^0
=-cG(t^0)^{\mathsf T}\Gamma t^0<0,
$$

contradicting `L_A succeq 0`. Hence

$$
\min_{i\ne j}K_{ij}\le0. \tag{A.3}
$$

Equations (A.1) and (A.3) contradict each other. No universal common positive
contact bridge exists. Since C24 makes `I_*` a path in a bridge-block tree, removing
all possible bridge edges leaves only one block node. `square`

### Theorem B — exact sparse-stress consequence of `s_Z>0`

This theorem is conditional on the report-level ZF rank conclusion
`rank R=2v-3` and on the promoted universal selected-stress PSD theorem. Let `v,e,h`
be the nonisolated contact-core vertex, contact-edge, and actual diameter-edge counts,
and set

$$
s_Z=e+h-(2v-2)\ge0.
$$

Let `P` be the normalized nonnegative KKT stress polytope on the actual rows
`C cup H`, normalized by `sum_H beta=1`. Then

$$
\boxed{\dim_{aff}P=s_Z.}
$$

If `x^*` is any vertex of `P`, then at least `s_Z` actual mixed rows have zero
multiplier:

$$
\boxed{|supp(x^*)|\le2v-2.}
$$

In particular, if `z_C,z_H` count zero contact and zero diameter multipliers in an
extreme stress, then `z_C+z_H>=s_Z`, so one of them is at least `s_Z/2`.

#### Proof

Let `W` be the signed planar equilibrium/self-stress space on `C cup H`, after
reversing the sign of the diameter rows. ZF gives `rank R=2v-3`, so

$$
\dim W=(e+h)-(2v-3)=s_Z+1. \tag{B.1}
$$

Let `L(alpha,beta)=sum_H beta`. If a nonzero nonnegative equilibrium stress had
`L=0`, then `beta=0`; taking the scalar virial identity for the contact equilibrium
would give `sum_C alpha=0`, hence the stress would vanish. Thus `L` is positive on
the nonnegative stress cone, and the normalized slice is compact.

C65 supplies a normalized stress with every actual row positive. Consequently the
nonnegative cone has full relative dimension in `W`, and slicing by `L=1` gives

$$
\dim_{aff}P=\dim W-1=s_Z. \tag{B.2}
$$

Now let `x^*` be a vertex and let `Z` be its zero-coordinate set. If
`|Z|<s_Z`, the `s_Z`-dimensional tangent space of `aff P` contains a nonzero vector
vanishing on every coordinate in `Z`. For sufficiently small positive `t`, both
`x^*+tw` and `x^*-tw` remain normalized, nonnegative equilibrium stresses, because
all coordinates outside `Z` are strictly positive. This gives a nontrivial convex
decomposition of `x^*`, contradicting extremality. Therefore `|Z|>=s_Z`, proving
the support bound and the `z_C+z_H` dichotomy. `square`

## 3. Exact target implication

Theorem A removes the universal-bridge/caterpillar corridor from the C24 route in
both diameter-topology branches. The surviving common contact geometry is a single
2-edge-connected hub block.

Theorem B makes the unresolved `s_Z>0` phase a sparse-support problem, but does not
make it a weak-constraint problem: a row with zero multiplier in one extreme stress
can still be supported by the relative-interior stress and can remain geometrically
strong. This is the precise obstruction to turning sparsity into a finite release.

Conditional on the report-level ZR/ZF chain, the exact ledger is:

| Branch | Proved reduction | Remaining obstruction |
|---|---|---|
| `s_Z=0`, cyclic `d_H=0` | Woodall gives one odd unicyclic diameter graph; cyclic Reuleaux/cap and stopped-train arguments give `L/D >= lambda_A + epsilon_A`, with `lambda_A=0.9955405845...`, and exclude equality | No quantitative gap is known that crosses `1`; no upper bound `L< D` is proved |
| `s_Z=0`, forest `d_H>0` | Woodall gives a caterpillar forest with exactly `d_H` components; `L/D >= 0.597+epsilon_597+3d_H/D`; all routes meet one bridgeless hub block | No global upper tradeoff couples the hub block to the `3d_H` charge |
| `s_Z>0` | Theorem B gives an extreme PSD stress omitting at least `s_Z` rows; `b+Q=2(h-s_Z)` so the circuit face argument is unavailable | No theorem converts omitted support rows into a simultaneous feasible release, strict competitor, or population contradiction |

Here `L=e_{BB}+2s_C`. The cyclic and forest numerical statements are report-level
consequences of the September 10 unpromoted reports; they are not silently promoted
by this audit. Contact-isolated source points remain in all full-source population
accounts and are not assumed diametral.

## 4. Exact remaining lemma

One of the following is still required:

$$
\boxed{
\begin{array}{l}
\text{(i) a global packing/response theorem giving }L/D<1-o(1)\text{ in the cyclic branch;}\\
\text{(ii) a hub-block/bypass inequality giving }L/D<0.597+3d_H/D\text{ in the forest branch;}\\
\text{(iii) a support-to-motion theorem for the }s_Z>0\text{ extreme stress;}\\
\text{or (iv) a strict sub-}D\text{ competitor accounting for every isolate.}
\end{array}}
$$

The shortest unresolved statement is not a generic PSD or planarity claim. It must
couple the actual full source population to the actual contact/diameter response with
the common hub block and all contact-isolated points retained.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
|---|---|---|
| C-I finite integration / universal selected-stress PSD | promoted proved | Controlled by the September 9 orientation/dependency audit |
| Theorem A | proved in this report from promoted C53 plus C20/C22/C24 | Maximum principle plus a direct C53 sign lemma |
| Theorem B | proved conditional | Requires unpromoted report-level ZF rank and C65 full-support stress |
| Woodall diameter-topology dichotomy | literature import / proved application | Exact straight-line-thrackle hypotheses match the actual diameter graph |
| `s_Z=0` cyclic `lambda_A` floor and endpoint exclusion | computationally independent report-level theorem | Exact arguments are in the named September 10 reports; no promotion is assumed here |
| `s_Z=0` forest `0.597` floor | report-level conditional theorem | Depends on the same unpromoted ZR/ZF/RSJ chain |
| zero multiplier implies weak geometric constraint | rejected | A coordinate can vanish in one stress while another stress supports the row |
| linear strict-minor count implies a trace gap | rejected | Circular-planar networks can have arbitrarily small strict minors |
| density gap for all triangle-free packings | rejected | Near-triangular rhombic perturbations and shell fillings are binding |

## 6. Regression tests

| Regression | Result | Exact reason |
|---|---|---|
| order-reversing diameter matching | survives | The bridge proof uses one separating half-plane, not a star or same-side order |
| incompatible projective orientations | excluded | The C53 orientation is chosen once from the bridge-side separation |
| regular odd shells | survives as a local/global-small-`n` regression | Their contact graph has `s_Z=2`; the circuit identities do not apply, and no global certificate for large shells is supplied |
| contact-isolated source points | retained | The response proof uses only loaded endpoints; population statements keep isolates in the source |
| shared diameter endpoints | survives | C53 and the bridge transfer estimate allow shared endpoints |
| exceptional faces and whole-circuit attachment exception | survives | They are retained in the cyclic reports; Theorem B does not use a proper-subset circuit count |
| high pinned surplus | survives | The lower floors are not treated as upper bounds |
| sublinear forest-component count | survives | The `3d_H` charge is retained, but no hub-block upper bound is known |

## 7. Failed routes and no-go results

### 7.1 Sparse extreme stress implies a release

This fails at the exact implication “zero multiplier implies weak row.” The relative
interior stress can be positive on every actual row while an extreme stress deletes a
linear number of rows. A deleted row may still be frozen on the fixed-diameter
critical cone. Theorem B therefore gives support sparsity, not a geometric motion.

### 7.2 Common hub block implies a response contradiction

The bridge transfer argument only eliminates a bridge common to every route. A
2-edge-connected hub block can carry all routes without a single forced voltage drop;
the maximum-principle inequality (A.1) then has no analogue. Extending it to arbitrary
multi-edge cuts would incorrectly assume a uniform transfer resistance, which is not
proved and is contradicted by near-star circular-planar response regressions.

### 7.3 Cyclic endpoint exclusion implies a threshold above one

The endpoint argument is qualitative compactness. It proves some `epsilon_A>0` but
does not quantify it, and the known difference `1-lambda_A` is about `0.0044594`.
No claim that the cyclic branch is closed is justified.

## 8. Canonical promotion recommendation

**Hold as report.**

The bridge proof is auditable, but Theorem A is already represented by the newer
unpromoted common-bridge report on `origin/main`; Theorem B is already represented by
the unpromoted extreme-stress report. This run does not justify route-map promotion
because no C-II endpoint is closed.

## 9. Next run

The highest-value next theorem is a quantitative common-2-connected-hub response
inequality that couples the hub block to the actual `3d_H` forest charge and remains
valid for multi-edge cuts without assuming a conductance floor. In parallel, the
cyclic branch needs a quantitative stability version of the atomic endpoint exclusion
strong enough to prove `e_{BB}+2s_C<D` or another exact global contradiction.

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem A: a positive contact bridge cannot lie in every positive diameter route.
C24 therefore reduces the common route to one 2-edge-connected contact block.
Proof: orient every cross-bridge diameter pair using the separating line of the two
loaded boundary intervals; a bridge current gives K_ef >= 1/alpha for every pair,
while the promoted C53 affine/PSD identities force min_{e!=f} K_ef <= 0.

Theorem B (conditional on report-level ZF): s_Z is the affine dimension of the
normalized KKT stress polytope. An extreme stress omits at least s_Z actual rows,
but this is not a release theorem.

Branch ledger: s_Z=0 cyclic survives above lambda_A+epsilon_A with lambda_A=0.99554...;
s_Z=0 forest survives above 0.597+epsilon+3d_H/D; s_Z>0 survives as a sparse-support
stress branch. Isolates remain accounted for. No global theorem closes any branch.

Next decisive lemma: a quantitative common-2-connected-hub response/bypass inequality,
or a quantified cyclic stability gap crossing 1.
```
