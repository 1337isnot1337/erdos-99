> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_spine_fan_chain_decomposition_2026-10-01.md) · source SHA-256 `88087a2e05705717d1e2afc3b907378b6704cf1a2a16025a2dc30133226ccf62`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-305068368C13","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — diameter-spine order and fan-chain decomposition

**Date:** 2026-10-01
**Base main:** c00bb08090cf3a7a89fc195cbe3ab450983a5de0
**Status:** proof-only; C-II remains open.

Let H=(B,E_H) be the loaded diameter graph, q=|B|, h=|E_H| and d_H=q-h.
Current main gives the Woodall dichotomy and global contiguity of every diameter star
in cyclic projective-direction order.

Call uv a core edge if deg_H(u),deg_H(v)>=2, and let s_D be the number of core
edges.

## Theorem 1: direction order reconstructs the Woodall core

A diameter edge is a core edge iff its predecessor and successor in projective
direction order share opposite endpoints with it.

In the Woodall forest branch, nonleaf diameter vertices occur in direction order
exactly in caterpillar-spine order, up to reversal, and all leaf edges at one spine
vertex form one consecutive bundle. If n_2 is the number of diameter vertices of
degree at least two, then

    n_2 = s_D + c_* <= s_D + d_H,

where c_* is the number of caterpillar components with a nonempty nonleaf core.

In the cyclic Woodall branch, nonleaf vertices occur in the order of the unique odd
cycle, pendant diameter leaves at each cycle vertex form one consecutive bundle, and

    n_2 = s_D.

Proof. For a diameter vertex v let I_v be its contiguous interval of direction
positions. For distinct u,v, I_u intersect I_v is empty unless uv is an edge, and then
the intersection is the singleton position uv. If uv is a core edge, both intervals
have at least two positions. The common position cannot be interior to either interval,
or the other interval would share a neighboring position as well. Thus uv is an
endpoint of both intervals. They extend from uv in opposite cyclic directions, since
extension to the same side would again create a second common position. The converse
is immediate.

In a caterpillar the nonleaf vertices induce a path, so the singleton interval
intersections force the star intervals to occur in spine order. A component with r>0
nonleaf vertices has r-1 core edges, giving the count above after summing. In the
cyclic Woodall branch the nonleaf core is exactly the odd cycle, so its vertex and
core-edge counts agree. QED.

## Theorem 2: quantitative V-cover becomes fan chains

Work in the rooted wrapping branch. Put

    A(lambda)=lambda+4 lambda sqrt(1-lambda^2),
    Delta(lambda)=pi/2-A(lambda),
    a_D=asin(1/(2D)).

Fix 0<eta<1. At least

    q-(2+1/eta) Delta(lambda) D-o(D)

distinct loaded-hull sides split into at most

    s_D+(1+1/eta) Delta(lambda) D+o(D)

edge-disjoint contiguous hull chains. Every chain has one common loaded apex v,
every chain vertex x has |v-x|=D, and every chain side has length in [1,1+eta].

Proof. Current main gives exactly d_H disjoint consecutive diameter-direction pairs
and q-2d_H shared pairs. Relative to the minimum gap 2a_D for a shared pair and 4a_D
for a disjoint pair, the exact total nonnegative excess is

    E_D = pi-2 a_D q.

The rooted ledger gives E_D<=Delta+o(1) and d_H<=Delta D+o(D). Therefore the number
B_eta of shared gaps with excess greater than eta/D is at most

    B_eta <= (Delta/eta+o(1))D.

For one star v, order its edges as vx_0,...,vx_t inside its ordinary aperture-pi/3
cone. A good shared gap g_i gives

    |x_i-x_{i+1}|=2D sin(g_i/2)<=1+eta,

while unit separation gives the lower bound one. Since eta<1, the current-main
short-arc V-cover argument makes x_i x_{i+1} an actual hull side, and the current-main
V-to-side map is injective.

A maximal run of good gaps at one star gives consecutive hull sides
x_a x_{a+1},...,x_b x_{b+1}, hence one contiguous hull chain on the exact circle
S(v,D). If b_v bad gaps occur in a star, its good gaps split into at most b_v+1
runs. Thus the number of chains is at most n_2+B_eta. Theorem 1 and
d_H<=Delta D+o(D) give the claimed bound. QED.

## Exact fan curvature

For one fan chain write the ray angles theta_0<...<theta_m and
g_i=theta_{i+1}-theta_i. Convexity makes the outward normal of side
x_i x_{i+1} parallel to

    (x_i-v)+(x_{i+1}-v).

Hence its angle is exactly

    nu_i=(theta_i+theta_{i+1})/2,

and at an internal fan vertex

    nu_{i+1}-nu_i=(g_i+g_{i+1})/2.

Thus the fan-interior hull turning is tied exactly to the diameter-direction gaps.

## Endpoint refinement

At the exact rooted endpoint A(lambda_1)=pi/2, current main gives

    q=pi D+o(D), d_H=o(D), E_D=o(1).

Set

    epsilon_D=max(D^(-1/4),sqrt(E_D)).

Then epsilon_D->0 and the number B_D of shared gaps with excess greater than
epsilon_D/D obeys

    B_D/D <= E_D/epsilon_D <= sqrt(E_D) -> 0.

All remaining shared gaps are eventually covered by the fixed eta=1/2 V-cover
argument and their hull sides have length at most 1+epsilon_D. Hence

    pi D-o(D)

near-unit hull sides split into at most

    s_D+o(D)

same-apex exact radius-D fan chains.

Therefore every endpoint sequence satisfies the alternative:

1. limsup s_D/D>0, so a positive density of exact star-center switches survives; or
2. s_D=o(D), and almost the entire near-unit hull boundary lies in o(D) same-apex fan
   chains. In this second case the maximum fan-chain length tends to infinity.

This is the new narrowing. It replaces the scattered V-cover by an exact ordered
fan decomposition controlled by one diameter-topology statistic s_D. A closing
continuation can now attack the Section-90 inverse-phase train families separately
against linear center switching and against the long single-apex fan regime.

No computation, verifier, CI result, Euler-path inference, source deletion, or
near-disk convergence rate is used. The macroscopic inactive-container branch is
untouched.

## Salvage provenance and lifecycle

Copied from `proof/target-c-spine-fan-chain-decomposition-20261001` at tip
`021442c23f2f4cef39e4bc1f977b384553714217`. This is proof-only structural work on
current-main loaded diameter-graph hypotheses. It does not close C-II or Level I, and
remains unreviewed pending independent audit.
