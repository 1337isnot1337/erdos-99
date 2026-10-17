# Target B: (2,1,1) singleton stress endpoint

Date: 2026-10-03
Base main: 19cf8ad1d5959d295181c43a87286a9cfbbc567a
Status: proof-only candidate, noncanonical. Target B and Level I remain open.

This sharpens case 3 of `research/target_b_fourbar_211_phase_group_reduction_2026-10-03.md`.
Keep its notation: h1,h2 are in rotation class A, h3 is the singleton class B,
h4 is singleton class C, a positive gradient balance exists on all four bars, and

    n1,n3 != 0,  n2=n4=0.

The primitive phase relation is c=(p-q,q,-p), with p,q,p-q nonzero. Current main
also proves that the normalized persistent-gradient stress polytope P has a vertex
with mu3=0 and hence mu1=0.

## Singleton-transfer lemma

If a persistent bar h has a nonzero phase transfer count to a singleton rotation
class {k}, some tangent train tau of h is assigned to k. The tau gradient coordinate
has exactly two nonzero persistent-bar entries, those of h and k.

The h entry is nonzero because tau is tangent to h, and the k entry is nonzero by
the destination-class definition. A third bar l cannot occur. If tau were tangent
to l, h and l would be parallel diameter bars, impossible for distinct active
diameters. If tau were nontangent to l, persistent equality would identify the
tau coordinate on K with s_l; assignment to k identifies it with s_k, so l must
be in k's rotation class. That class is a singleton.

Thus every mu in P obeys

    mu_h g_h,tau + mu_k g_k,tau = 0.

The known full-support positive stress shows the two entries have opposite signs.
Hence a fixed kappa_hk>0 satisfies mu_k=kappa_hk mu_h for every mu in P.

## Case-3 consequence

Because n1 != 0 and both singleton coordinates of c are nonzero,

    N_1B=n1 q != 0,   N_1C=-n1 p != 0.

Applying the lemma twice gives fixed k3,k4>0 such that every mu in P satisfies

    mu3=k3 mu1,   mu4=k4 mu1.                              (1)

Take the current-main stress vertex with mu3=0. Equation (1) forces
mu1=mu4=0, so normalization gives

    mu^0=(0,1,0,0).                                        (2)

Therefore g2=0 exactly. The flat-bar stress face from the preceding reduction is
actually a singleton coordinate stress.

Moreover P is exactly one segment. Since (2) is a stress and a full-support
positive stress exists, dividing the latter balance by mu1 gives

    g1+k3 g3+k4 g4=0.

Hence

    mu^*=(1,0,k3,k4)/(1+k3+k4)

is also a stress. Conversely (1), nonnegativity, and normalization leave no other
points. Therefore

    P=conv{(0,1,0,0),mu^*}.                                (3)

At mu^*, phase-group balance gives mu1^* n1+mu3^* n3=0. Thus its weighted
cubic is

    sum_h mu_h^* F_h
      =mu3^* n3 (Q_B-Q_A) delta^3,

which is nonzero. The only CG-degenerate endpoint of (3) is therefore the
zero-gradient bar h2.

## Integer-diameter consequence

In pure-disk train coordinates,

    r_2=sum_tau d_2tau u_tau,   d_2tau in {-1,0,1},

and (g_2)_tau=2 r_2 dot J(d_2tau u_tau). Since g2=0, every nonzero separating
contribution d_2tau u_tau is parallel to r_2, hence equals +e_2 or -e_2 for
e_2=r_2/D. If P_2,N_2 count the two signs, then

    r_2=(P_2-N_2)e_2,   D=P_2-N_2 in Z.                    (4)

Thus every case-3 survivor has integer diameter and a persistent active diameter
bar with identically zero full train-angle gradient.

The remaining case-3 bottleneck is now exact: combine a negative quadratic
direction for this zero-gradient bar with the nonzero cubic at mu^*, or derive
an ordered-shell contradiction from the collinear separator structure in (4).
Case 2 remains the separate one-coordinate rational-stress core.

No numerical search, verifier execution, CI result, or unexecuted verifier is used.
