> Generated reading edition · [exact source](../../research/target_b_fourbar_211_phase_group_reduction_2026-10-03.md) · source SHA-256 `8b49656382be010d326ed1ffe942013434c1c722911164637b374fc2d7b0078c`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b39cdde780f91f6558b39bffecda55565cb3f93d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_b_fourbar_211_phase_group_reduction_2026-10-03.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "359153e23fd03eb2b7dff20531adf6d19b39db9153bf6f4c1a5627f427b91b3f"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target B: four-bar (2,1,1) reduction

Date: 2026-10-03
Base main: 60a08ff369c56d8fc604f7e3d1d40e61aeefa7ed
Status: proof-only candidate, noncanonical. Target B and Level I remain open.

This treats the residual fully supported four-persistent-bar case left by
`target_b_tangent_cubic_capacity_2026-09-21.md`: rotation-functional
multiplicities (2,1,1). It uses that report's candidate AP, PG, and CG theorems.

Let h1,h2 share rotation functional sA, and let h3,h4 have singleton functionals
sB,sC. Assume a persistent-gradient balance positive on all four bars.

If some phase-group row is nonzero, AP implies sA,sB,sC are affinely dependent.
Since they are distinct, write s_i=s_*+t_i delta for one nonzero delta in K*. The
integer affine-relation space is one-dimensional, so there is a primitive
c=(cA,cB,cC) in Z^3 with sum c_i=sum c_i t_i=0, and every phase row has form

    B_h = n_h c,  n_h in Z.                                (1)

All c_i are nonzero. Normalizing tA=0,tB=p,tC=q gives q/p rational; rescale to
distinct nonzero coprime integers p,q and c=(p-q,q,-p), up to sign.

Put S2=sum c_i t_i^2 and S3=sum c_i t_i^3. Then

    S2=pq(p-q) != 0.                                       (2)

For an active bar h in class i,

    F_h(v)=n_h Q_i delta(v)^3,
    Q_i=S3-3 t_i S2,                                      (3)

so Q_i-Q_j=-3S2(t_i-t_j) is nonzero for different classes. Also
sum c_j(t_j-t_i)^2=S2, so n_h!=0 is genuinely nonflat.

A tangent transfer from an active bar h to a singleton-class bar k has exactly two
persistent gradient incidences. Coordinatewise positive stress balance gives
mu_h |g_h,tau|=mu_k |g_k,tau|. The tangent magnitude is 2D and the nontangent
magnitude is strictly smaller, hence

    h -> singleton k  implies  mu_h < mu_k.                 (4)

Thus h3 and h4 cannot both be active, since each nonzero row transfers to every
other class and would force mu3<mu4<mu3.

Now suppose h1,h2 are both active. Their transfers to both singleton classes give a
connected K_{2,2} system of two-incidence gradient columns, fixing all positive stress
ratios. Hence the normalized stress polytope is a singleton {mu}. PG reduces to

    mu1 n1+mu2 n2+mu3 n3+mu4 n4=0.                         (5)

At most one of n3,n4 is nonzero. If, say, n3!=0, the unique weighted cubic equals

    mu3 n3 (Q_B-Q_A) delta^3,                              (6)

which is nonzero by (3), contradicting singleton-stress CG. Therefore

    n1,n2 != 0  implies  n3=n4=0,                           (7)

and mu1/mu2=-n2/n1 is a positive rational number.

Finally suppose exactly one singleton is active, say n3!=0. Then n4=0. PG and the
given positive stress require at least one of n1,n2 nonzero; (7) forbids both. After
relabeling, n1,n3!=0 and n2=n4=0. For every stress mu,

    mu1 n1+mu3 n3=0.                                       (8)

At any stress-polytope vertex the weighted cubic is
mu3 n3(Q_B-Q_A)delta^3. If every vertex had mu3>0, all coefficients would have the
same nonzero sign; choose the sign of delta(v) to make every vertex-weighted cubic
negative and invoke CG for a strict diameter descent. Hence some stress vertex has
mu3=0, and then (8) gives mu1=0. That vertex is supported entirely on the two flat
bars h2,h4.

Therefore the fully supported (2,1,1) case has only three possibilities:

1. all four rows vanish, hence all four bars are exactly flat;
2. exactly the two repeated-class bars are nonflat, both singleton bars are flat,
   stress is unique, and the entire nonflat response factors through one rational
   relative-rotation coordinate delta;
3. exactly one repeated-class bar and one singleton bar are nonflat, while the
   stress polytope has a vertex supported entirely on the other two, exactly flat,
   bars.

This removes arbitrary four-row repeated-class phase networks. The remaining
bottleneck is the exact one-coordinate two-bar core in case 2 or the flat-bar stress
face in case 3. No numerical search, verifier, or CI claim is used.
