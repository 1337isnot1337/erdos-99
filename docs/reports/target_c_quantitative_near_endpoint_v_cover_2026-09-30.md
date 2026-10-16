<!-- theorem-state: {"artifact_id":"ART-CB9918235D30","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — quantitative near-endpoint diameter-V cover

Proof-only; C-II remains open.

Let A(lambda)=lambda+4 lambda sqrt(1-lambda^2) and Delta(lambda)=pi/2-A(lambda). In the rooted wrapping branch current main gives

    (pi D-P_F)+(P_F-q)+k <= Delta(lambda) D+o(D),
    k=d_H+s_Z.

Global diameter-star contiguity gives R_D=0, m_D=d_H and h=q-d_H. Fix any constant 0<eta<1. Then at least

    q-(2+1/eta) Delta(lambda) D-o(D)

distinct loaded-hull sides xy have a unique loaded vertex v with |v-x|=|v-y|=D, satisfy |x-y|<=1+eta+o(1), and have width deficit D-w_F(n_xy)=O_eta(1/D).

Proof. Let a_D=asin(1/(2D)). The exact angular excess is

    E_D=pi-2 a_D q.

Since pi/(2a_D)<pi D and pi D-q<=Delta D+o(D),

    E_D<=Delta+o(1).

Call a shared consecutive diameter-direction pair bad if its excess over 2a_D is >eta/D. The number of bad shared pairs is at most (Delta/eta+o(1))D. The exact number of shared pairs is h-m_D=q-2d_H, while d_H<=k<=Delta D+o(D). Hence the number of good shared pairs is at least

    q-(2+1/eta)Delta D-o(D).

For a good pair vx,vy with projective gap g, the diameter-neighbor cone has aperture at most pi/3, so g is the ordinary angle at v and

    |x-y|=2D sin(g/2)<=2D sin(a_D+eta/(2D))=1+eta+o(1).

Because eta<1, this stays a fixed amount below 2. Canonical near-disk convergence gives the same short-arc argument as the endpoint V-cover theorem: if a loaded hull vertex lay strictly between x and y, the short boundary chain would contain at least two unit-separated sides with directions in one o(1) tangent cone, forcing |x-y|>=2-o(1), contradiction. Thus xy is a hull side.

The V-to-side map is injective. If one side xy had two distinct common diameter partners v,w and s=|x-y|=O_eta(1), then

    |v-w|=2 sqrt(D^2-s^2/4)>D,

contradicting the source diameter. Finally the common partner lies at altitude H=sqrt(D^2-s^2/4) from the support line through xy, so

    0<=D-w_F(n_xy)<=D-H=s^2/[4(D+H)]=O_eta(1/D).

Taking eta=1/2 gives N_V>=q-(4Delta+o(1))D. Since q>=(pi-Delta)D-o(D), also N_V>=(pi-5Delta-o(1))D.

This is theorem/proof work; no computation or verifier is load-bearing. A regular odd shell remains a local regression. The next target is to couple the two Section-90 inverse-phase families to this quantitative short V-cover, charging train/fan transitions to the rooted scalar defect Delta D.
