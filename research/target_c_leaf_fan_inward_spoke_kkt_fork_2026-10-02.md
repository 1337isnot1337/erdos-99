# Target C: inward-spoke / stress-flat fork inside an exact diameter-leaf fan

Date: 2026-10-02
Base main: abdbe1f5cd53806ab63f581df61e561273a03141
Status: proof-only reduction. Level I and C-II remain open.

Let p_0,...,p_g be one good same-carrier fan run from the current-main leaf-fan
theorem, with carrier a:

    |p_i-a|=D,     |p_i-p_{i+1}|=1.                               (1)

Every fan edge is a positive loaded-hull contact. An internal p_i has full diameter
degree one, with unique diameter edge p_i a. Canonical loaded-terminal geometry gives
contact degree at most three. Hence p_i has either exactly the two fan contacts or one
additional positive unit contact.

This note proves that the third-contact case is forced into an exact inward cone,
third neighbors cannot be reused along one fan, and KKT equilibrium makes the fan
contact multipliers a bounded-variation sequence with exact equality transport
through every degree-two vertex.

## 1. Exact third-contact cone

Fix p=p_i and put

    u=(p-a)/D,     eps=1/(2D),     tau=sqrt(1-eps^2).

Choose the unit tangent t so that

    w_- := p-p_{i-1} = eps u + tau t,
    w_+ := p-p_{i+1} = eps u - tau t.                              (2)

This is the exact decomposition of a unit chord of the radius-D circle.

Suppose p has a third contact neighbor z. Put

    v=p-z,     |v|=1,     r=u.v,     s=t.v.

Because the whole source has diameter D,

    |z-a|^2 = D^2+1-2Dr <= D^2,

so

    r >= eps.                                                       (3)

Unit separation from the two fan neighbors gives

    |w_+-v| >= 1,     |w_--v| >= 1,

hence, because all three vectors are unit,

    v.w_+ <= 1/2,     v.w_- <= 1/2.                               (4)

Let psi=acos(eps). The vectors w_+,w_- make angles -psi,+psi with u. Equation
(3) keeps v in the sector |angle(v,u)|<=psi, while (4) requires angular distance
at least pi/3 from both fan vectors. Therefore

    |angle(v,u)| <= psi-pi/3.                                      (5)

Equivalently,

    r >= c_D := (eps+sqrt(3) tau)/2,                               (6)

    |s| <= s_D := (tau-sqrt(3) eps)/2.                             (7)

Thus the third edge points through a 30-degree-plus-lower-order inward cone.

If R=|z-a|, then

    D^2-R^2 = 2Dr-1 >= 2D c_D-1.

Since R<=D,

    D-R >= c_D-eps
        =: delta_D
        = (sqrt(3) tau-eps)/2
        -> sqrt(3)/2.                                               (8)

So every degree-three internal fan leaf has a third neighbor a fixed positive depth
inside the carrier's diameter circle.

## 2. Third neighbors are injective along one fan

Let z_i be the third neighbor of a degree-three internal fan vertex p_i.

Lemma 2.1. For D>1, the map p_i -> z_i is injective along one same-carrier fan run.

Proof. All fan vertices lie on the radius-D circle centered at a. Every source pair
has distance at most D, so the minor central angle between any two fan vertices is at
most pi/3. Thus this same-carrier block lies on one short arc, and its convex order
agrees with angular order.

Write

    x=asin(1/(2D)).

Each fan step has central angle 2x. If j-i=k, then

    |p_i-p_j| = 2D sin(kx).                                        (9)

Suppose one source vertex z were the third neighbor of two distinct fan vertices
p_i,p_j. Since |p_i-z|=|p_j-z|=1, triangle inequality gives |p_i-p_j|<=2.

If k>=3, then kx<=pi/6 and sine is increasing, so

    |p_i-p_j| >= 2D sin(3x) = 3-1/D^2 > 2,

a contradiction.

If k=1, p_i,p_{i+1},z form a unit equilateral contact triangle, forbidden in the
canonical triangle-free contact graph.

If k=2, then |p_i-p_{i+2}|=2 tau. The two intersections of the unit circles centered
at p_i,p_{i+2} are p_{i+1} and the only possible distinct shared neighbor. Their
mutual separation is

    2 sqrt(1-tau^2) = 2 eps = 1/D < 1.

Thus the second intersection violates unit separation from p_{i+1}, while p_{i+1}
itself is already a fan neighbor and cannot be the third neighbor. QED.

Therefore T degree-three internal fan vertices force T distinct actual source vertices
satisfying the inward-depth bound (8).

## 3. Exact KKT transport

Let lambda_{i-1},lambda_i>0 be the contact multipliers on the two fan edges through
p_i. Let beta_i>0 be the multiplier on p_i a. If p_i has a third contact, give it
multiplier gamma_i>0; otherwise put gamma_i=0.

Equilibrium at p_i is

    lambda_{i-1} w_- + lambda_i w_+ + gamma_i v
      = beta_i (p_i-a).                                            (10)

Radial and tangential components give exactly

    eps(lambda_{i-1}+lambda_i) + gamma_i r_i = D beta_i,           (11)

    tau(lambda_{i-1}-lambda_i) + gamma_i s_i = 0.                  (12)

If p_i has contact degree two, gamma_i=0, so

    lambda_{i-1}=lambda_i,                                         (13)

    beta_i=lambda_i/D^2.                                           (14)

Thus a block of m consecutive degree-two internal fan vertices carries one common
contact multiplier on all m+1 fan edges, and all m pendant diameter multipliers are
exactly that common value divided by D^2.

For a degree-three vertex, (6), (7), (11), and (12) give

    c_D gamma_i <= D beta_i,                                       (15)

and

    |lambda_i-lambda_{i-1}| <= kappa_D gamma_i,                    (16)

where

    kappa_D := s_D/tau
             = 1/2 - sqrt(3) eps/(2 tau)
             < 1/2.

Hence

    |lambda_i-lambda_{i-1}|
      <= (kappa_D D/c_D) beta_i.                                   (17)

Summing over the run and using the normalized diameter mass sum_h beta_h=1 gives

    sum_{i=1}^{g-1} |lambda_i-lambda_{i-1}|
      <= (kappa_D/c_D) D
      = (1/sqrt(3)+o(1)) D.                                        (18)

All fan-stress variation is concentrated at degree-three vertices; degree-two vertices
transmit it exactly unchanged.

## 4. Square-root-of-run fork

Let N=g-1 be the number of internal fan vertices and T the number having contact
degree three.

If T>=sqrt(N), Lemma 2.1 and (8) give at least sqrt(N) distinct constant-depth inward
spokes.

If T<sqrt(N), the N-T degree-two vertices are split into at most T+1 consecutive
blocks. Hence one block has length

    m >= (N-T)/(T+1) > sqrt(N)-2.                                  (19)

Therefore every good fan run satisfies

    at least sqrt(g-1) distinct inward spokes,

or

    a stress-flat degree-two subrun of length > sqrt(g-1)-2.       (20)

The preceding current-main theorem gives g=Omega(sqrt(D)) in the
x_B=O(sqrt(D)), nu=O(sqrt(D)) branch. Thus this branch contains either

    Omega(D^(1/4))

distinct inward spokes on one carrier circle, or an Omega(D^(1/4))-long exact
stress-flat fan segment.

## 5. Remaining bottleneck

This does not close C-II.

The low-x_B fan branch is now split into two concrete source-level structures:

1. many distinct third-contact spokes, each entering the exact cone (5) and reaching
   carrier-radius deficit at least delta_D -> sqrt(3)/2;
2. a long degree-two fan segment with exactly constant contact stress and exactly
   equal pendant diameter weights lambda/D^2.

Equation (18) controls the mixed case by bounding total fan-stress variation using
only normalized diameter mass.

The next target is to charge the spoke-rich branch to loaded/interface or ball-hull
currency, or to propagate the exact common multiplier in the stress-flat branch through
the common positive-contact block. No contradiction is claimed here.

Disposition: theorem/proof only. No numerical search, verifier execution, CI output,
or unexecuted certificate code is used.
