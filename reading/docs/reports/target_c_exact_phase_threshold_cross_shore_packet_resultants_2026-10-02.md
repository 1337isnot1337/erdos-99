> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_threshold_cross_shore_packet_resultants_2026-10-02.md) · source SHA-256 `ea206df909c07c2dcaf72c91f836e7f3ac6dd6c743ddd79f44449d57c55b50c1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-438E91F5408A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- cross-shore KKT load of internal threshold packets

Date: 2026-10-02
Base main: fbeae9b3fa18a63e07573676b4e2e512a91ca4d5
Status: proof-only; C-II remains open.

Let A={tau_1,...,tau_m} and B={sigma_1,...,sigma_n} be the retained shores of the
fixed-star complete O--O rectangle, with A in the threshold exact-phase branch and
common oriented train vector u. Let T be the paired-staircase simple gap tree on
A-layers 0,...,m.

For a simple edge e={a,b}, let H_e be all transversely active actual-diameter rows
with A-support (a,b]. Orient h from lower to higher A-layer, put
c_h=r_h dot Ju, and let beta_h>0 be a relative-interior KKT multiplier.

The positive gap circulation on current main has collapsed simple graph T. Deleting
e and summing node balance over either component of T-e therefore gives the exact
edgewise balance
$$
\boxed{\sum_{h\in H_e}\beta_h c_h=0.}
\tag{1}
$$
Both signs occur.

Now take an internal edge 1<=a<b<=m-1. The four-host argument used in the current
transverse-rail theorem applies to every row in H_e: each endpoint is in an internal
A-layer, the diameter-thrackle property puts the endpoints on opposite hull arcs,
and those two internal A-host arcs have B-layers 0 and n. Hence every h in H_e has
full B-support.

Reorient h from B-layer 0 to B-layer n and call the vector $\widehat r_h$. The
paired-staircase sign rule gives
$$
\widehat r_h=\operatorname{sgn}(c_h)r_h,\qquad
\widehat r_h\cdot Ju=|c_h|.
\tag{2}
$$
Thus the packet resultant
$$
P_e=\sum_{h\in H_e}\beta_h\widehat r_h
$$
satisfies
$$
\boxed{P_e\cdot Ju=\sum_{h\in H_e}\beta_h|c_h|>0.}
\tag{3}
$$
So the packet cancels in the A-shear equation but not as a physical vector load
when viewed across B.

Let I be the internal tree edges and
$$
P_{\rm int}=\sum_{e\in I}P_e.
$$
If I is nonempty, then
$$
\boxed{P_{\rm int}\cdot Ju>0.}
\tag{4}
$$

For B-train sigma_j orient its shore cut from B-layer 0 to n, let v_j be its unit
contact direction, and let C_j>0 be its total contact KKT mass. The exact cut
resultant identity gives
$$
\boxed{C_jv_j=P_{\rm int}+R_j,}
\tag{5}
$$
where R_j contains only actual diameter rows outside the internal A-packets. Indeed,
each internal row has full B-support and signed incidence +1 on every B-cut in its
B-orientation, so its contribution is independent of j.

Dotting (5) with Jv_j gives
$$
\boxed{R_j\cdot Jv_j=-P_{\rm int}\cdot Jv_j.}
\tag{6}
$$
Thus every B-direction not parallel to P_int requires a transverse correction from
an outside diameter row.

Subtracting (5) for adjacent B-cuts gives
$$
C_{j+1}v_{j+1}-C_jv_j=R_{j+1}-R_j.
$$
If no outside row changes B-incidence at that interface, then R_{j+1}=R_j, so
C_{j+1}v_{j+1}=C_jv_j. Positivity of the contact masses and unit length of the
coherently oriented train vectors force v_{j+1}=v_j. Therefore every adjacent
projective phase change on B is charged to a B-switch of a diameter row outside the
internal A-packets.

Writing H_int=union_{e in I} H_e and s_B^ph for the number of adjacent B phase
changes,
$$
\boxed{
s_B^{\rm ph}\le
\sum_{h\notin H_{\rm int}}t_B(h)
\le
\sum_{h\notin H_{\rm int}}(2-t_A(h)).
}
\tag{7}
$$
The second inequality is the current joint per-edge switch theorem.

Every h in H_int has two internal A-support endpoints, so t_A(h)=2. Its full
B-support gives t_B(h)=0. Parallel-diameter uniqueness leaves only the threshold
full-support reference diameter with c_h=0; hence every other diameter with two
distinct internal A-endpoint layers is transversely active and belongs to H_int.
All rows outside H_int are therefore A-boundary-touching or A-layer-local.

If the staircase is internal-heavy, e_int>=m/2, current main gives at least
2e_int>=m distinct rows in H_int. A linear diameter family is therefore
B-switch-inert while contributing to one common exported KKT load.

The remaining bottleneck is quantitative. Relative-interior positivity proves
P_e dot Ju>0 packet by packet, but current main gives no uniform lower bound on
those loads. Closure now requires either a lower bound on enough packet resultants,
or a proof that the A-boundary/layer-local rows cannot realize the correction family
R_j across a linear opposite shore. In the double-exact-phase case the same
decomposition can be applied in both directions.

No C-II closure is claimed. No computation, numerical evidence, verifier execution,
CI result, or unexecuted verifier code is used.
