> Generated reading edition · [exact source](../../../docs/reports/target_c_complete_grid_joint_stress_light_cusps_2026-10-01.md) · source SHA-256 `e589bcfe64d90784c9a2b3be17b8bca943415e3a8edbdb56f93c002335270318`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2F39B32F95AA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- joint stress-light cusp extraction

Date: 2026-10-01
Authoritative main before write: 91be6776e6748b0f449ccfff69bca1e352d1b75d
Dependency: 4abd2eb3cbdeb122f8ca787cb9cdbd7522e9c978
Status: proof-only; C-II remains open.

## Theorem

Use the fixed-star complete O-O rectangle after the current witness-cell extraction. Write

$$
|A|,|B|\ge(c_*-o(1))D,\qquad
c_*={\kappa^4\over16\pi^3 C_KM_K},
$$

with $C_K=\lfloor4K\rfloor+2$ and $M_K=2\lfloor4K\rfloor+3$.
For an adjacent selected interface $i$ on either shore let $H_i$ be the actual
diameter edges whose signed cut incidence changes there, and set

$$
N_i=|H_i|,\qquad
\mu_i=\sum_{h\in H_i}\beta_h,
$$

using the canonical positive normalization $\sum_h\beta_h=1$.

The joint two-shore switch theorem gives for every actual diameter edge

$$
t_A(h)+t_B(h)\le2.
\tag{1}
$$

Consequently

$$
\boxed{\sum_{i\in A}\mu_i+\sum_{j\in B}\mu_j\le2.}
\tag{2}
$$

Put

$$
H_*=\left\lceil{4\pi\over c_*}\right\rceil+1.
$$

For every fixed $L>4/c_*$, one shore contains at least

$$
\boxed{\left({c_*\over4}-{1\over L}-o(1)\right)D}
\tag{3}
$$

adjacent interfaces satisfying simultaneously

$$
\boxed{1\le N_i\le H_*,\qquad \mu_i\le {L\over D}.}
\tag{4}
$$

Moreover one can retain at least

$$
\boxed{\left(
{c_*/4-1/L\over H_*+3}-o(1)
\right)D}
\tag{5}
$$

of these interfaces so that their adjacent train pairs are pairwise disjoint and
their complete switching packets $H_i$ are pairwise edge-disjoint.

Taking $L=8/c_*$ gives

$$
\boxed{\left({c_*\over8}-o(1)\right)D}
$$

stress-light bounded interfaces on one shore and

$$
\boxed{\left({c_*\over8(H_*+3)}-o(1)\right)D}
\tag{6}
$$

pairwise-disjoint stress-light bounded cusps.

For every retained cusp the audited adjacent-strip KKT identity gives

$$
G_i=W_i u_i-W_{i+1}u_{i+1}
=\sum_{h\in H_i}\beta_hn_h,\qquad |n_h|=D.
\tag{7}
$$

Reaction nondegeneracy gives $G_i\ne0$, while (4) gives

$$
\boxed{0<|G_i|\le D\mu_i\le L.}
\tag{8}
$$

Planar conic Caratheodory therefore expresses each $G_i$ exactly as a positive
combination of one or two actual switching diameter bars. Because the retained
packets are edge-disjoint, these one/two-bar reaction supports are edge-disjoint
between cusps. Also

$$
|G_i|^2=(W_i-W_{i+1})^2+
2W_iW_{i+1}(1-u_i\cdot u_{i+1}),
$$

so

$$
\boxed{|W_i-W_{i+1}|\le L.}
\tag{9}
$$

No uniform positive lower bound for $|G_i|$ is claimed.

## Proof of the joint mass bound

Double counting gives

$$
\sum_i\mu_i^A+\sum_j\mu_j^B
=\sum_h\beta_h(t_A(h)+t_B(h)).
$$

Apply (1) and $\sum_h\beta_h=1$ to obtain (2).

## Bounded plus stress-light averaging

Current main gives

$$
s_A+s_B\ge(c_*-o(1))D
$$

active adjacent interfaces. The joint count theorem gives

$$
\sum_iN_i^A+\sum_jN_j^B\le2h=(2\pi+o(1))D.
$$

By the definition of $H_*$, fewer than $(c_*/2+o(1))D$ active interfaces have
$N_i>H_*$. Hence at least

$$
(c_*/2-o(1))D
\tag{10}
$$

interfaces across both shores have $1\le N_i\le H_*$.

By (2), fewer than $2D/L$ interfaces can satisfy $\mu_i>L/D$. Subtracting from
(10) leaves at least

$$
\left({c_*\over2}-{2\over L}-o(1)\right)D
$$

bounded stress-light interfaces across both shores. One shore contains half, proving
(3).

## Disjoint-packet extraction

On the shore supplied by (3), form a conflict graph on its retained interfaces.
Two interfaces conflict if their adjacent train pairs overlap or if their switching
packets share a diameter edge.

A selected adjacent train pair overlaps at most its two neighboring pairs. Exact
interval support says one diameter row starts at most once and stops at most once on
this shore, so a diameter edge occurring in one switching packet can occur in at most
one other packet. Since every retained packet has at most $H_*$ edges, the conflict
graph has maximum degree at most

$$
H_*+2.
$$

A greedy independent set therefore retains at least a $1/(H_*+3)$ fraction. This
proves (5).

## Reaction consequence

For a retained adjacent strip, the established switching-order theorem and the
adjacent-strip reaction theorem apply without any phase-gap hypothesis. Equation (7)
is exact and $G_i\ne0$. The triangle inequality gives

$$
|G_i|\le\sum_{h\in H_i}\beta_h|n_h|=D\mu_i\le L,
$$

which proves (8). The one/two-bar conclusion is the planar conic Caratheodory
sparsification already audited for the same exact strip reaction. Packet disjointness
makes those sparse supports distinct between retained cusps. Equation (9) follows
from the displayed norm identity.

## Remaining target

The fixed-star branch now contains a linear family of pairwise-disjoint adjacent O-O
strips on one shore with all of the following simultaneously:

- at most $H_*=O_{K,\kappa}(1)$ moving diameter rows per strip;
- total normalized switching stress at most $8/(c_*D)$ per strip;
- an exact nonzero reaction bounded above by $8/c_*$;
- an exact one/two-bar reaction certificate, edge-disjoint between retained strips;
- the full opposite linear shore crossing every retained train;
- the current fixed full-span witness pair, which is not a switching row.

Thus KKT stress concentration is not an escape from the bounded-cusp reduction.
The next target is local: classify the one-bar and two-bar reaction chord patterns
inside the one-arc prefix / optional-hub / suffix switching order and combine that
classification with the complete transverse train order and fixed witness cell.

The split-star O-O branch and inactive-interface branch remain open.

No computation, verifier, numerical experiment, or CI output is used.
