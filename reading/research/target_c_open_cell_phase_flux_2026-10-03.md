> Generated reading edition · [exact source](../../research/target_c_open_cell_phase_flux_2026-10-03.md) · source SHA-256 `82bcf72417a4e622cc72a2b52f7d4ae30b169a8970343d2a8ed7a9713f21ad1a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C: exact open-cell phase-flux law

Date: 2026-10-03
Base main: d1d0047bdf870aa0f2878784a1e034ca16a485e0
Status: proof-only candidate, noncanonical. C-II and Level I remain open.

This note stays off the current high-t collar route and the Target B cross-grain
phase-polytope route. It attacks the nonconstant open-witness-cell branch.

Let tau_1,...,tau_m be one retained ordered O-O shore in one open global
diameter-direction cell J. Write the coherently lifted unit train directions as
u_i=u(theta_i), all in one real interval of width less than pi/2. Let A_i>0 be
the positive KKT contact mass on cut i.

For an actual diameter h whose endpoints have different layers a_h<b_h, orient
r_h from a_h to b_h. For e=u(mu) in J put v=J e. Since J contains no actual
diameter direction, sign(r_h dot v) is nonzero and cannot change as e moves
inside J. Thus the rule

    a_h -> b_h if r_h dot v > 0,
    b_h -> a_h if r_h dot v < 0

defines one directed gap multigraph G_J.

Fix p<q with theta_p != theta_q. Put

    delta = theta_q-theta_p,
    e = u((theta_p+theta_q)/2),
    v = J e,
    t = sin(delta/2),
    S = {p,...,q-1}.

The exact block transposition between cuts p and q is the slab translation

    Delta = u_q-u_p = 2 t v.                              (1)

Give every directed diameter edge positive flow

    f_h = beta_h |r_h dot v|,

and let F_in(S), F_out(S) be the total flow entering and leaving S.

## Theorem: exact phase-flux identity

For every distinct-phase pair p<q,

    F_out(S)-F_in(S) = (A_p+A_q) sin((theta_q-theta_p)/2).  (2)

Proof. The two-cut subset reflection has layer potential x=2t on S and x=0
outside. Therefore

    sum_h beta_h r_h dot Delta_h
      = 2t (F_in(S)-F_out(S)).                             (3)

The exact KKT subset-reflection work identity gives, because
u_p dot v=-t and u_q dot v=t,

    sum_h beta_h r_h dot Delta_h
      = -2(A_p+A_q)t^2.                                   (4)

Equating (3) and (4) and dividing by 2t proves (2). QED.

This is a finite identity with no asymptotic error and no lower bound on an
individual KKT multiplier.

## Exact classification of the old-diameter obstruction

The existing two-cut non-grazing theorem applies for D>=1, so every moving old
diameter has the same strict finite length-change sign as its work sign.

If theta_p<theta_q, then t>0. Entering edges have positive work and leaving
edges have negative work. Equation (2) forces F_out>F_in, hence at least one
strictly shortening old diameter. Therefore

    TWO-SIGN iff F_in(S)>0,
    ONE-SIGN iff F_in(S)=0.                               (5)

If theta_p>theta_q, the signs reverse and (2) forces F_in>F_out. Hence

    TWO-SIGN iff F_out(S)>0,
    ONE-SIGN iff F_out(S)=0.                              (6)

Thus the active obstruction to an arbitrary block transposition is exactly a
directed gap edge crossing the slab against the KKT-enforced net flux.

In the ONE-SIGN case canonical minimality invokes the existing endpoint
argument. Since

    |u_q-u_p| <= 4K/D,

there is a previously strict source pair xy with either

    1 < |xy| <= 1+|u_q-u_p|

or

    D-|u_q-u_p| <= |xy| < D.                              (7)

So every distinct-phase interval has the exact fork

    wrong-way active diameter flux
    OR
    inverse-D inactive near-activity.                     (8)

## Condensation consequence

Call a set of gap vertices a source ideal if no directed edge enters it and a
sink ideal if no directed edge leaves it. Assume the inactive witness (7) has
been excluded for the pair p,q.

For the contiguous slab S={p,...,q-1},

    S source ideal  => theta_p >= theta_q,                 (9)
    S sink ideal    => theta_p <= theta_q.                (10)

Indeed, a source ideal with theta_p<theta_q has F_in=0 and is ONE-SIGN by (5);
a sink ideal with theta_p>theta_q has F_out=0 and is ONE-SIGN by (6).

Hence the non-strongly-connected branch is no longer an arbitrary condensation
DAG. Any contiguous source component must sit across a phase drop or plateau,
and any contiguous sink component across a phase rise or plateau. The remaining
escape is interleaved/noninterval SCC structure or a phase-compatible interval
ideal.

For q=p+1 this also localizes the blocker. In the no-inactive-witness branch,
a strict phase ascent at interface p forces an actual directed diameter edge
into gap vertex p; a strict phase descent forces one out of p. Ascents can be
assigned distinct witnesses by distinct heads, descents by distinct tails, so
if U and Dn are the ascent/descent interface sets, there are at least

    max(|U|,|Dn|) >= (|U|+|Dn|)/2                         (11)

distinct actual diameter rows with signed endpoint-layer localization.

## Scope

The pair-dependent magnitudes f_h change with the midpoint direction e, so (2)
for different pairs is not one common conserved weighted network. No summation
of those weights is asserted. Positive wrong-way flow proves existence, not a
cardinality bound proportional to its value. Strong connectivity is not inferred
from nonconstant phase; the existing five-point regression remains valid and is
explained by (5)-(6). No two-axis or within-layer motion is covered.

The remaining open-cell task is to combine (8)-(10) with the complete opposite
shore/four-host geometry: either rule out the surviving interleaved SCC pattern
or charge its forced wrong-way diameter rows to a bounded source currency. No
computation, verifier execution, or CI result is used.
