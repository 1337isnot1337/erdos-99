> Generated reading edition · [exact source](../../research/target_c_open_cell_cut_divergence_condensation_2026-10-03.md) · source SHA-256 `1107f74e245baa872595cd8c8ac6860ec55d22e72796d36108229b261a66cf05`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C: open-cell cut divergence

Date: 2026-10-03
Base main: 4eb09a14d4a1f7fb764bb1f7cb19094ec2533414
Status: proof-only candidate, noncanonical. C-II and Level I remain open.
Arbitrary-ideal extension sourced from `worker-c/target-c-open-cell-arbitrary-ideal-flux-2026-10-03-v2` at `a6a1ab70937458e3ee5bc5dabc7aecbd918236dc`.

Let P_i={0,...,i-1}. Orient each actual diameter r_h from lower layer a_h
to higher layer b_h. For e=u(mu) in the common open witness cell put v=Je,
and direct the gap edge by the sign of r_h dot v. This direction is independent
of mu because the cell contains no actual diameter direction. Give h flow
f_h=beta_h |r_h dot v|.

The KKT cut identity is
A_i u_i = sum_{a_h<i<=b_h} beta_h r_h.
Therefore, exactly,
Phi(P_i;mu):=F_out(P_i)-F_in(P_i)=A_i sin(theta_i-mu).        (1)

For S_{p,q}={p,...,q-1}=P_q\P_p,
Phi(S_{p,q};mu)
 = A_q sin(theta_q-mu)-A_p sin(theta_p-mu).                 (2)
At the midpoint mu=(theta_p+theta_q)/2 this recovers the phase-flux law on
current main.

Set mu=theta_i in (1). The net flow across cut i is zero. At least one actual
diameter crosses the cut because A_i>0, and every crossing transverse component
is nonzero because u_i is in an open diameter-direction cell. Hence every
selected cut has at least one directed diameter edge each way. No proper prefix
or suffix is a source or sink ideal.

Now let S_{p,q} be a proper interior interval. If it is a source ideal with an
outgoing edge, (2) at mu=theta_p gives
0 < A_q sin(theta_q-theta_p), hence theta_q>theta_p.
With F_in=0, the current block-transposition theorem is ONE-SIGN and canonical
minimality forces a previously strict pair xy with
1<|xy|<=1+|u_q-u_p| or D-|u_q-u_p|<=|xy|<D.                 (3)
A sink ideal with an incoming edge similarly gives theta_q<theta_p and the
reversed ONE-SIGN case, hence the same witness (3). In the Section-90 window
|u_q-u_p|<=4K/D.

Thus every nonisolated contiguous source or sink ideal forces inverse-D inactive
near-activity; the previous phase-compatible interval-ideal escape disappears.

If S_{p,q} has no incoming or outgoing edge, (2) vanishes for every mu in an
open interval, so A_q u_q=A_p u_p. Positivity and coherent lifts give
u_q=u_p and A_q=A_p. This is necessary, not sufficient.

Consequently, after excluding (3), every source and sink SCC in any nontrivial
condensation weak component must be noninterval/interleaved in layer order.
The remaining open-cell task is to combine that interleaving with the opposite
complete shore, four-host geometry, and convex-diameter-thrackle order.

No computation, verifier execution, or CI result is used.


## Arbitrary interleaved-set divergence

For an arbitrary layer set `S subset {0,...,m}`, let `x_j=1_S(j)` and define
`Phi(S;mu)=F_out(S)-F_in(S)`. The prefix identity (1) implies

```math
\Phi(S;\mu)=\sum_{i=1}^m(x_{i-1}-x_i)A_i\sin(\theta_i-\mu)
=C_S\cdot Ju(\mu),
```
where
```math
C_S=\sum_{i=1}^m(x_{i-1}-x_i)A_i u_i.
```
This is a finite telescoping identity and applies to interleaved as well as
contiguous layer sets.

If `S` is a source ideal with an outgoing edge, every crossing edge contributes
positively, so `Phi(S;mu)>0` throughout the open phase cell. For
`theta_- = min_i theta_i` and `theta_+ = max_i theta_i`, this forces
```math
\arg C_S\in(\theta_+,\theta_-+\pi).
```
For a sink ideal with an incoming edge, the same interval condition holds for
`arg(-C_S)`. In particular, no nontrivial source or sink ideal can have all its
layer-boundary transitions at one common phase.

Writing `R={i:x_{i-1}=1,x_i=0}` and `L={i:x_{i-1}=0,x_i=1}`, source ideals
also satisfy the two endpoint moment reversals
```math
\sum_{i\in R}A_i\sin(\theta_i-\theta_-)>
\sum_{i\in L}A_i\sin(\theta_i-\theta_-),
```
```math
\sum_{i\in L}A_i\sin(\theta_+-\theta_i)>
\sum_{i\in R}A_i\sin(\theta_+-\theta_i).
```
Both inequalities reverse for sink ideals. This constrains every interleaved
extremal SCC in the remaining condensation branch, but supplies no contradiction
with four-host geometry or the opposite complete shore. C-II and Level I remain
open. No verifier is claimed.
