# Target C: k=6 p=5 triple-deletion synchronization

Date: 2026-10-04
Base: d432d18a14cfeccbb7e47c51960847ecc33351f2
Status: proof-only finite Target C reduction; C-II remains open.

Assume nine no-root rows with k=6, D=-1, d_root=1, p=5 and rank-three coefficient space P<=Q^9. The established deletion identity gives D(B-S)=-1+2|S|-3q_S>=0, so (d1,d2,d3)(P)>=(2,4,5). Root accounting gives p_S+3d_S=8, hence p-p_S is a nonnegative multiple of 3.

Every one-coordinate deletion preserves rank. Its p-value is 5 or 2; p=2 is impossible by the committed eight-row rank-three low-p theorem D>=11-2p. Thus all nine one-coordinate shadows retain p=5.

For a pair S={i,j}, q_S is 0 or 1. If q_S=0 but p_S=2, lost cost 3 lies in blocks with exact touch support S. This needs at least two blocks and includes a singleton. The two cycles jointly touch two distinct root blocks, so committed local four-cycle geometry makes their directions at the singleton distinct. Its singleton constraint is then a nonzero word of P supported on S, contradicting q_S=0. Hence every rank-preserving pair retains p. Any p-losing pair supports a weight-two word. Distinct p-losing pairs use disjoint exact-support cost-three packets, so p=5 permits at most one.

For a triple T, q_T is 0 or 1 and p_T is 5 or 2. If there is no p-losing pair, any p-losing triple uses its own exact-support-T cost-three packet, so at most one of 84 triples loses p. If a unique p-losing pair S exists, exactly the seven triples containing S can lose p; every triple avoiding S retains p, since another disjoint cost-three packet would exceed p=5. Therefore at least 77 of 84 triples retain p.

Finally dim(Q^9/P)=6. Choose six coordinate classes forming a quotient basis. All 20 triples among them have q_T=0. If a bad pair exists, its two quotient classes are dependent and cannot both be in this basis, so all 20 basis triples retain p. Otherwise at most one triple globally loses p, so at least 19 do. Each such shadow has q_T=0, p_T=5, d_T=1, D=5, rank(P_T)=3 on six coordinates, hence k=3.

Therefore every survivor has at least nineteen exact six-no-root shadows of type (k,D,d_root,p)=(3,5,1,5), and twenty in the exceptional-pair case. The next finite target is to classify this six-row class and test simultaneous extension multiplicity at least nineteen.

No computation is used.
