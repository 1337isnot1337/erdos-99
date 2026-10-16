# Target B: case-2 sign-frustration lemma

Date: 2026-10-03
Base main: 6c45398dcfe69e3b3bb322920a2911468dfe0573
Status: proof-only candidate, noncanonical. Target B and Level I remain open.

Continue case 2 of `research/target_b_fourbar_211_phase_group_reduction_2026-10-03.md`.
Bars h1,h2 are the nonflat repeated-class bars and h3,h4 are the flat singleton
classes. The persistent stress mu is unique and positive, all four transfers
h_i -> h_j (i=1,2 and j=3,4) occur, and each has exactly two persistent
gradient incidences.

For an oriented diameter bar hi write e_i for its unit direction and v_i=mu_i e_i.
The coordinatewise balance used in Theorem FF gives, for each transfer hi -> hj,

    |v_i dot v_j| = |v_i|^2 = mu_i^2.                    (1)

Distinct diameter bars are nonparallel. If two length-D diameter vectors were
parallel, both positive endpoints would lie on one extreme support face and both
negative endpoints on the opposite face; each such face is a singleton, so the
pairs would coincide.

Put eps_ij=sgn(v_i dot v_j). The cross-Gram matrix is

    C = [[eps_13 mu_1^2, eps_14 mu_1^2],
         [eps_23 mu_2^2, eps_24 mu_2^2]].

Since both pairs v1,v2 and v3,v4 are linearly independent,

    0 != det C = det[v1 v2] det[v3 v4].

Therefore

    eps_13 eps_14 eps_23 eps_24 = -1.                    (2)

So the residual K_2,2 transfer square is necessarily sign-frustrated: no choice
of bar orientations makes all four transfer projections positive.

Taking absolute determinants yields

    mu_3 mu_4 |sin(theta_12) sin(theta_34)| = 2 mu_1 mu_2, (3)

and in particular

    mu_3 mu_4 >= 2 mu_1 mu_2.                            (4)

After orientation flips take eps_13=eps_14=eps_23=+1 and eps_24=-1. Write

    v1=(a,0),  v2=(b cos(theta), b sin(theta)),

with a=mu_1, b=mu_2 and sin(theta)!=0. Equations (1) force

    v3=(a,(b-a cos(theta))/sin(theta)),
    v4=(a,-(b+a cos(theta))/sin(theta)).                  (5)

Hence

    mu_3^2=(a^2+b^2-2ab cos(theta))/sin(theta)^2,
    mu_4^2=(a^2+b^2+2ab cos(theta))/sin(theta)^2,         (6)

and

    v3 dot v4=(a^2-b^2)/sin(theta)^2.                     (7)

Case-2 phase balance gives mu_1 n_1+mu_2 n_2=0, so
mu_1/mu_2=|n_2|/|n_1| is rational. The surviving geometry is therefore reduced
to one angle, one positive rational repeated-stress ratio, and the forced odd
sign cycle (2). If |n_1|=|n_2|, then (7) forces the singleton diameter directions
to be perpendicular.

This does not exclude case 2. The next target is to combine (2)-(7) with planar
diameter-thrackle endpoint topology. No verifier or CI result is a proof premise.


## Diameter-thrackle sharpness regression

Generic planar diameter topology alone does not exclude the balanced subcase.
At diameter 1 take

    A=(-sqrt(3)/2,0),
    B=(1-sqrt(3)/2,0),
    C=(0,-1/2),
    D=(0,1/2).

Then

    AB=CD=AC=AD=1,
    BC=BD=sqrt(2-sqrt(3))<1.

So the actual diameter graph has exactly the four edges AB, CD, AC, AD; it is
a valid planar diameter thrackle (the triangle ACD with the leaf AB).

Assign

    h1=AC, h2=AD, h3=AB, h4=CD

and orient

    e1=(sqrt(3)/2,-1/2),
    e2=(sqrt(3)/2, 1/2),
    e3=(1,0),
    e4=(0,1).

With positive weights

    mu1=mu2=1,  mu3=2/sqrt(3),  mu4=2,

the four cross projections are exactly

    v1 dot v3 = 1,
    v2 dot v3 = 1,
    v1 dot v4 = -1,
    v2 dot v4 = 1.

Thus (1)-(7), including the odd sign cycle and the balanced rational ratio, are
realizable by an actual four-edge planar diameter graph. Any closure of case 2
must therefore use additional rhombic/train structure (or stronger source
constraints), not the diameter-thrackle property by itself.
