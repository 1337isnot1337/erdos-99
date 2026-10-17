> Generated reading edition · [exact source](../../research/target_c_open_cell_host_cap_attachment_depth_2026-10-04.md) · source SHA-256 `5193d8f6e0bef5d1edf05831b57a62d29c65fc9d96ed2e184e1fdcb9952e4065`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C: host-cap overlap forces a deep same-host harmonic attachment

Date: 2026-10-04
Base main: 0e01bddd51357e2278e78eac8e356da90d68dcd1
Status: proof-only Target C-II candidate; theorem-state authority unchanged.
LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.

This note stays inside the strong nonconstant open-witness-cell route.

Current main gives, in the Type-II branch, one host interval X_*, a set Q_* of
actual diameter endpoints on that host, the cap C_* = conv(Q_*), and one coherent
strict-rhombus component G_cap such that

    G_cap is contained in int(C_*) intersect P_cap,
    P_cap = conv(A_cap),

where A_cap is the loaded attachment set of the unloaded positive-contact component
I_cap carrying G_cap. Moreover

    A_G := area(G_cap) = Omega_epsilon(D^2).                         (1)

The previous host-cap localization theorem did not force any attachment of I_cap
back onto the physical host arc that generated C_*.

## 1. Cap chord and signed height

The loaded set B is the vertex set of the convex force hull F. The points of Q_*
are loaded extreme vertices. Order B by its convex-boundary order. Let q_0 and q_1
be the first and last points of Q_* in the X_*-order, and let Gamma_* be the
corresponding boundary arc of F following X_*.

Convex cyclic order is inherited from the source hull after non-B vertices are
deleted, so

    Q_* is contained in Gamma_*, and Gamma_* is contained in X_*.    (2)

Let L be the line through q_0 q_1. Let eta be signed perpendicular distance from L,
chosen positive on Gamma_*. A chord of a convex polygon separates its two boundary
arcs into opposite closed half-planes. Therefore

    eta(b) >= 0 for b in B intersect Gamma_*,
    eta(b) <= 0 for b in B outside Gamma_*.                           (3)

Every vertex of C_* belongs to Gamma_*, hence

    C_* is contained in {eta >= 0}.                                  (4)

The already-proved quadratic area of C_* ensures that this cap side is
two-dimensional.

## 2. Deep same-host attachment theorem

Define

    H_* := max eta(a), over a in A_cap intersect Gamma_*.

Then A_cap intersect Gamma_* is nonempty and

    H_* >= A_G / D.                                                   (5)

Proof. Every attachment belongs to B. By (3), every attachment outside Gamma_*
has nonpositive signed height.

First suppose A_cap intersect Gamma_* were empty. Then every attachment has
eta <= 0, so convexity gives P_cap contained in {eta <= 0}. But G_cap is contained
in P_cap intersect C_*, while C_* is contained in {eta >= 0}. Hence G_cap would
be contained in L and would have zero area, contradicting (1). Thus the maximum
defining H_* exists.

Every attachment has eta <= H_*. Convexity gives the same bound throughout
P_cap. Therefore

    G_cap is contained in P_cap intersect {0 <= eta <= H_*}.          (6)

Every line parallel to L cuts P_cap in a segment of length at most D, because
P_cap lies in the diameter-D source hull. Integrating these parallel slices gives

    A_G <= D H_*.

This proves (5).

Choose a_* in A_cap intersect Gamma_* attaining H_*. Then

    dist(a_*, L) >= A_G / D = Omega_epsilon(D).                       (7)

Because Gamma_* is contained in X_*, a_* is an actual loaded attachment on the
same host interval as the staircase endpoint cap.

## 3. Actual positive-contact port

By definition of the attachment set, a_* has a unit-contact neighbor x_* in I_cap:

    |a_* - x_*| = 1.

Signed distance from a fixed line is 1-Lipschitz. Hence

    eta(x_*) >= A_G / D - 1 = Omega_epsilon(D).                       (8)

Thus one physical port simultaneously consists of:

- a same-host loaded vertex a_*;
- an actual diameter endpoint a_*;
- an actual positive unit contact a_* x_* entering the exact unloaded component
  that contains the quadratic rhombus grain.

This is stronger than the previous geometric statement that G_cap lies in
C_* intersect P_cap. It forces an actual contact attachment onto the same physical
host cap.

No bound on the contact-path distance from x_* to a chosen rhombus of G_cap is
claimed.

## 4. The same host arc has linear chord detour

Put

    ell := |q_0 - q_1|,

and let Len(Gamma_*) denote the polygonal boundary length of Gamma_*. Since a_*
lies on the arc from q_0 to q_1,

    Len(Gamma_*) >= |q_0-a_*| + |a_*-q_1|.

For fixed perpendicular height H_* above a line through a segment of length ell,
the right side is minimized when the longitudinal coordinate is the midpoint.
Therefore

    Len(Gamma_*) >= sqrt(ell^2 + 4 H_*^2),

so

    Len(Gamma_*) - ell >= sqrt(ell^2 + 4 H_*^2) - ell.                (9)

The right side decreases as ell increases. Since ell <= D and H_* >= A_G/D,

    Len(Gamma_*) - |q_0-q_1|
      >= D * ( sqrt(1 + 4 (A_G/D^2)^2) - 1 )
      = Omega_epsilon(D).                                             (10)

Equation (10) is a loaded-force-hull host-arc detour. It is not identified here
with the occurrence-counted harmonic outer walk and is not automatically a payment
in the Section-122 signed-return ledger.

## 5. Counterexample pressure and exact remaining target

The theorem uses only convexity, the current host-cap localization, and the actual
harmonic attachment definition. The older threshold-rail depth theorem does not
supply this conclusion: its depth is relative to an assigned affine marker row,
whereas (5) forces an attachment of the particular harmonic cell onto the same
convex host arc as the staircase cap.

The strong Type-II open-cell survivor can therefore no longer attach the
macroscopic cap-local harmonic cell entirely through the complementary loaded-hull
arc. It has an actual diameter-loaded attachment on the staircase host at linear
perpendicular depth, an actual positive contact from that attachment into the
component carrying G_cap, and a linear host-arc chord detour.

This does not close C-II. The exact remaining strong Type-II obligation is now to
control the positive-contact route from this deep port into the cap-local complete
grid, or to charge any long such route to the canonical attachment/exceptional-face
ledger. Without that route control, (10) alone is not a contradiction.

The Type-I macroscopic-container branch and the non-strong inverse-D inactive
near-unit/near-diameter branch remain separate.

No computation, verifier, numerical experiment, or CI result is a proof premise.

Disposition: proof-only Target C candidate. C-II and Level I remain open.
