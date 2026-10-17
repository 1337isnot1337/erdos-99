> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_bridgeless_two_star_normal_form_2026-09-11.md) · source SHA-256 `e87e515fda1c6d2df1fba6f3777c3a06146de0d296a92a264404e453e6fdf524`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F6C40DD96939","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — zero transfer forces a bridgeless contact core and two-edge stars

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact response/topology branch reduction  
**Target:** Target C, C-II  
**Status:** STILL OPEN; hold as report

## 1. Theorem

Assume the zero-transfer alternative

$$
K=Q^{\mathsf T}\Lambda^+Q=\operatorname{diag}(\beta_e^{-1}).
\tag{1.1}
$$

Assume the report-level mixed-support 3-connectivity and bridge bypass statement
that every contact bridge is crossed by at least two actual diameter edges. Assume
also the fully force-visible degree bounds

$$
\deg_C(b)\le3\quad(b\in B_+),
\qquad
\deg_C(v)\le5\quad(v\notin B_+),
\tag{1.2}
$$

and the source-preserving additive-response separator theorem SEPq. Then, for
sufficiently large C-II sources:

1. the contact graph has no bridge;
2. every component of $H$ is a star with at most two edges; and
3. after the independently certified perfect-matching branch is removed, any
   surviving zero-transfer source has at least one two-edge diameter star.

The strict-negative-transfer branch is not covered.

## 2. A contact bridge contradicts zero transfer

The report-level zero-transfer bridge-collapse theorem says every contact bridge
has a singleton side. Let that side be $\{p\}$, with the bridge joining $p$
to the other side. Mixed 3-connectivity supplies two distinct diameter edges

$$
e=pa,\qquad f=pb
\tag{2.1}
$$

crossing this bridge. Thus $p$ is a loaded force-hull vertex and $a,b$ are
loaded vertices on the other side.

The rays $a-p$ and $b-p$ lie in the open interior wedge at the strict convex
hull vertex $p$, whose width is less than $\pi$. Choose a projective C53 cut
whose open half-plane contains both rays and orient every diameter chord into that
half-plane. This is a legal C53 orientation, and both selected incidence columns
point from $p$ into the other side:

$$
q_e=\mathbf e_p-\mathbf e_a,
\qquad q_f=\mathbf e_p-\mathbf e_b.
\tag{2.2}
$$

Let $V$ be the harmonic potential for unit current demand $q_f$. The bridge
carries one unit, so

$$
V(p)-V(u)=1/\alpha_{pu}.
\tag{2.3}
$$

On the other side, after the bridge is removed, the source is at $u$, the sink
is at $b$, and there is no other injection. The discrete maximum principle gives
$V(u)\ge V(a)$. Hence

$$
K_{ef}=q_e^{\mathsf T}\Lambda^+q_f
=V(p)-V(a)\ge1/\alpha_{pu}>0.
\tag{2.4}
$$

Changing the legal projective cut only conjugates $K$ by a diagonal sign matrix:
if $Q'=QS$, then $K'=SKS$. A diagonal $K=\operatorname{diag}(\beta^{-1})$
stays diagonal. Thus (2.4) contradicts zero transfer. Therefore

$$
\boxed{C\text{ is bridgeless}.}
\tag{2.5}
$$

The orientation point matters: this uses a cut containing the two rays at the
singleton hull vertex, not a bridge positivity assertion for an arbitrary common
2-edge-connected block.

## 3. Larger diameter stars are impossible

Zero transfer gives that every component of $H$ is a star. Suppose one has
$k\ge3$ edges, with terminal set $T$ of size $k+1\ge4$. SEPq supplies a
contact vertex $z$ such that every component of $C-z$ contains at most one
terminal of $T$.

Since $C$ is bridgeless, every component of $C-z$ has at least two contact
edges to $z$. Otherwise its unique edge to $z$ would be a contact bridge.

If $z\notin T$, the $k+1$ terminals occupy distinct components, so
$\deg_C(z)\ge2(k+1)\ge8$, contradicting (1.2). If $z\in T$, the other
$k$ terminals occupy distinct components, so $\deg_C(z)\ge2k\ge6$, while
the loaded degree bound is three. Therefore

$$
\boxed{\text{every zero-transfer diameter star has at most two edges}.}
\tag{3.1}
$$

## 4. Quantitative consequence

Writing $h=|H|$ and $d_H=q-h$, (3.1) gives

$$
h\le2d_H.
\tag{4.1}
$$

The report-level diameter-density theorem gives

$$
\liminf h/D\ge2\rho,
\qquad \rho=\cos\rho=0.7390851332\ldots,
$$

so $\liminf d_H/D\ge\rho$. Combining this with the report-level general
surplus estimate

$$
\liminf\frac{e_{BB}+2s_C-3d_H}{D}
\ge0.597+\varepsilon_{597}
$$

gives

$$
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.597+3\rho+\varepsilon_{597}
=2.8142553996\ldots+\varepsilon_{597}.}
\tag{4.2}
$$

## 5. Exact remaining obstruction

The full matching subcase is excluded by the independent force-hull area gap. A
surviving zero-transfer sequence would therefore need two-edge stars as well as
matching components. SEPq does not apply to a three-terminal two-edge star, and
the current degree bounds permit a degree-four separator for that case. No global
upper bound below the surplus in (4.2) is known.

Contact-isolated source points are outside $C$ and are not charged. The
strict-negative-transfer alternative $\min K_{ef}<0$ is untouched.

## 6. Classification

| Claim | Status |
|---|---|
| zero transfer plus a contact bridge is impossible | proved conditional on bridge bypass and C53 |
| zero-transfer contact graph is bridgeless | proved conditional on bridge-collapse |
| zero-transfer stars have at most two edges | proved conditional on SEPq and degree caps |
| surplus floor (4.2) | proved conditional on report-level inputs |
| Level I settlement | not proved |

**Promotion recommendation:** hold as an unpromoted addendum pending independent
orientation and bridge-transfer audit.
