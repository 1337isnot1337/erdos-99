<!-- theorem-state: {"artifact_id":"ART-589251BA4A08","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Target B: exclude the singleton zero-gradient four-bar endpoint

**Date:** 2026-10-03.
**Research base:** `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`.
**State version:** `2026-09-14.audit.51`.
**Branch:** `research/full-settlement-20261003`.
**Classification:** proved candidates awaiting promotion; artifact lifecycle unreviewed.
**Level I / Target B:** STILL OPEN.
**Literature:** none imported.
**Certificate:** `research/verify_target_b_zero_gradient_cubic_corrector_2026_10_03.py`.

## 1. Endpoint and exact scope

The October 3 four-bar reduction and singleton-endpoint report leave case 3:
rotation classes `(A,A,B,C)`, phase rows `n_1,n_3!=0`, `n_2=n_4=0`, and a
persistent-gradient stress polytope

\[
\mathcal P=\operatorname{conv}\{(0,1,0,0),\mu^*\},\qquad
\mu^*={ (1,0,k_3,k_4)\over1+k_3+k_4},\quad k_3,k_4>0. \tag{1}
\]

In particular `g_2=0`, and the weighted cubic at `mu^*` is nonzero. We close
this endpoint by two independent finite arguments. The first is an exact
gradient-transfer contradiction without a large-diameter hypothesis. The second
constructs a complete contact-preserving strict source descent for `D>3` from
the endpoint data alone, without phase-transfer extraction.

```text
case-3 endpoint -> reciprocal singleton gradient transfers -> contradiction;
or endpoint data + D>3 -> negative zero-bar corrector + strict residual cubic
-> every old active diameter shortens -> all inactive pairs retain slack
-> same-cardinality full source with diameter < D.
```

These statements concern an actual finite pure simply connected strict-rhombic
source chart. They do not assert that an arbitrary B or C source admits that
chart, that selection of a diameter-pair-minimal source preserves purity, or
that the remaining four-bar case 2 or full backward-rank case is closed.

## 2. Precise chart hypotheses

Use the canonical pure-disk train coordinates of Target B §§37,40--43:

\[
p_x(\theta)=p_0+\sum_\tau\epsilon_\tau(x)u(\theta_\tau),\qquad
r_h(\theta)=\sum_\tau d_{h\tau}u(\theta_\tau),
\quad d_{h\tau}\in\{-1,0,1\}.
\]

Every contact remains exactly unit in a sufficiently small neighborhood of the
initial angles. All source points are retained. Put `f_h=|r_h|^2-D^2`, use its
**full** gradient `g_h` and Hessian `H_h`, and let `K` be a nonzero real train
velocity space with:

1. `g_h v=0` for every old active diameter and `v in K`;
2. `H_h[v,v]<=0` for every active bar;
3. its persistent set is exactly `J={1,2,3,4}`;
4. for `h in J`, every separating nontangent contribution has speed `s_h(v)`,
   and the tangent signed first moment vanishes.

These are the canonical backward-kernel equality conditions, not a PSD claim
about the full source. For a zero-gradient persistent bar every separating
contribution has the same speed. Write `F_h(v)` for its tangent cubic moment;
the straight-path cubic coefficient of `f_h` is `C_h(v)=D F_h(v)/3`.

For the phase application also use the actual persistent phase assignment of
the unpromoted AP/PG reduction, with distinct `s_A,s_B,s_C`. A tangent train
assigned to class `A`, `B`, or `C` has that functional on `K`. A separating
nontangent incidence at another persistent bar forces the same functional as
that bar. These hypotheses are explicitly conditional on that unpromoted
reduction when applying the result to its case 3. The arguments below rederive
the needed new bridge; they do not promote the AP/PG reduction by reference.

## 3. Zero-gradient recipients cannot compensate a tangent transfer

**Lemma ZT.** Suppose `g_2=0` and a positive gradient balance exists on bars
`1,2,3,4`. Under the phase hypotheses above, if both `N_1B!=0` and
`N_3A!=0`, no such balance can exist.

**Proof.** A nonzero signed transfer count contains at least one contributing
tangent train. Choose a tangent train of bar 1 assigned to singleton class `B`.
It cannot be tangent to any other distinct diameter bar: two distinct diameter
bars are not parallel. A nonzero nontangent gradient incidence at bar 4 would
identify its velocity with `s_C`, contradicting assignment to `s_B`; an incidence
at bar 2 has zero gradient. Thus positive coordinatewise balance forces a nonzero
incidence at bar 3 and

\[
\mu_1\,2D=\mu_3\,|(g_3)_\tau|<\mu_3\,2D,
\quad\text{hence}\quad\mu_1<\mu_3. \tag{2}
\]

Here `(g_h)_tau=2 r_h dot J(d_h,tau u_tau)`, the tangent magnitude is `2D`,
and the magnitude at a nontangent bar is strictly smaller. If the train missed
bar 3, balance would already be impossible.

Now choose a tangent train of bar 3 assigned to class `A`. Bar 4 cannot have a
nonzero nontangent incidence because `s_C!=s_A`; it cannot be tangent because
distinct diameter bars are not parallel. Bar 2 has identically zero gradient.
Therefore balance forces a nonzero nontangent incidence at bar 1, giving

\[
\mu_3\,2D=\mu_1\,|(g_1)_\sigma|<\mu_1\,2D,
\quad\text{hence}\quad\mu_3<\mu_1. \tag{3}
\]

Equations (2)--(3) contradict each other. Zero **full gradient**, rather than
merely zero signed transfer sum or zero stress at one point, is essential. QED.

For completeness, parallel distinct diameters are impossible for any finite
diameter-`D` source: if their equally oriented displacements are `r` and their
starting points differ by `w!=0`, the two cross distances include `r+w,r-w`;
one has squared length at least `D^2+|w|^2>D^2`.

In case 3 the primitive relation is `c=(p-q,q,-p)` with all entries nonzero.
Hence `N_1B=n_1 q!=0` and `N_3A=n_3(p-q)!=0`. The October singleton endpoint
gives `g_2=0`, so ZT excludes that case.

This identifies the exact missing use of the endpoint: the second member of the
double rotation class has zero gradient and cannot carry any of the recipient
weight. The old combined-recipient escape reduces to an impossible reciprocal
strict weight ordering.

## 4. A general zero-bar correction theorem

The following theorem does not assume phase-transfer labels or integer counts.
It supplies the requested finite source mechanism if only the endpoint data have
been established.

**Theorem ZC.** In the chart of Section 2, suppose `g_2=0`, `D>3`, (1) holds
with `mu^*` positive on `{1,3,4}`, and `sum_h mu_h^* F_h` is a nonzero cubic on
`K`. Then the full source has a same-cardinality unit-separated configuration of
diameter strictly less than `D`.

### 4.1 A correction invisible to all other persistent gradients

Zero full gradient makes every separating contribution of bar 2 equal `+e_2`
or `-e_2`, where `e_2=r_2/D`. If their counts are `P,N`,

\[
D=P-N\in\mathbb Z,\qquad P\ge D\ge4. \tag{4}
\]

The positive balance `mu^*` makes the rank of `{g_1,g_3,g_4}` at most two.
Restrict corrections `a` to the `P` forward coordinates of bar 2 and impose

\[
g_1a=g_3a=g_4a=0,\qquad\sum_{\tau\text{ forward for }2}a_\tau=0. \tag{5}
\]

There are at most three independent linear conditions on at least four variables,
so a nonzero `a` exists. Its full zero-bar Hessian is exactly

\[
\boxed{H_2[a,a]=-2D\sum a_\tau^2<0.} \tag{6}
\]

This is a simultaneous correction: it annihilates **all** other persistent
gradients. It is not a collection of separately feasible bar corrections.

### 4.2 Persistent equality annihilates the full mixed Hessian

For any persistent `h`, let `a_h,tau=d_h,tau u_tau` and
`lambda_h,tau=r_h dot a_h,tau`. Its equality conditions give

\[
\sum_\tau a_{h\tau}v_\tau=s_h(v)r_h,
\quad
\lambda_{h\tau}(v_\tau-s_h(v))=0.
\]

For an **arbitrary** full train correction `z`, differentiating the chart gives

\[
H_h[v,z]
=2\Big(\sum a_{h\tau}v_\tau\Big)\cdot
     \Big(\sum a_{h\tau}z_\tau\Big)
 -2\sum\lambda_{h\tau}v_\tau z_\tau=0. \tag{7}
\]

Thus vanishing on `K x K` is not being silently extended to all columns: (7)
is proved from the exact equality conditions. It is the reason a second-order
correction does not create an uncontrolled cubic term.

### 4.3 Residual strict cubic correction

Choose `v in K` so `sum mu_h^* C_h(v)<0`. This defines a nonempty open set,
since the weighted cubic is nonzero and odd. Choose `v` there avoiding the proper
quadratic kernels of all nonpersistent old active bars. Their quadratic terms are
then strictly negative.

Because `g_2=0`, (1) implies that the normalized nonnegative gradient-balance
polytope on `{1,3,4}` is exactly `{mu^*}`. The strict finite linear alternative
therefore supplies a full correction `b` such that

\[
g_hb+C_h(v)<0\qquad(h=1,3,4). \tag{8}
\]

Equivalently, infeasibility of (8) would give a nonzero nonnegative gradient
balance whose pairing with `C(v)` is nonnegative, contradicting the unique
balance `mu^*`. This is the same finite strict alternative used in canonical
Target B's higher-order correction.

### 4.4 Complete source path

Use the exact train-angle path

\[
\boxed{\theta(t)=\theta(0)+tv+\varepsilon t^2a+t^3b,\quad t>0.} \tag{9}
\]

Choose fixed `epsilon>0` sufficiently small. For bars `1,3,4`, (5), (7), and
(8) make the leading change the strictly negative cubic
`[g_h b+C_h(v)]t^3`.

For bar 2, every separating coordinate of `v` has the common speed `s_2(v)`.
Factor that common rotation out of its **exact** bar formula. The remaining
angle increments are `epsilon t^2 a+t^3 b`, and `g_2=0`, so

\[
f_2(\theta(t))
=\tfrac12\varepsilon^2t^4 H_2[a,a]+O(t^5)<0 \tag{10}
\]

for sufficiently small positive `t`. Every nonpersistent active bar has leading
coefficient `H_h[v,v]/2+epsilon g_h a` at order `t^2`, negative after the stated
choice of `epsilon`.

Every contact is preserved exactly by the same chart. Every other lower pair
inequality initially has positive slack; every inactive upper pair has distance
strictly below `D`. Finiteness and continuity retain all these inequalities for
sufficiently small `t`. Every old active diameter now has distance strictly below
`D`; thus the maximum over **all** source pairs is strictly below `D`.
No point is dropped or replaced, and cardinality is unchanged. QED.

## 5. Immediate consequence and surviving four-bar case

The singleton report's weighted cubic is

\[
\sum\mu_h^*F_h
=\mu_3^*n_3(Q_B-Q_A)\delta^3\ne0.
\]

Thus ZC independently resolves its advertised negative-quadratic/nonzero-cubic
bottleneck for every sufficiently large diameter. ZT gives the stronger exact
phase-transfer contradiction even before that large-diameter restriction.

Composed with the stated unpromoted `(2,1,1)` reduction, only these alternatives
remain: all phase rows vanish (exact flat family), or

\[
n_1n_2\ne0,\quad n_3=n_4=0,\quad
\mathcal P=\{\mu\},\quad
\mu_1/\mu_2=-n_2/n_1\in\mathbb Q_{>0},
\quad\sum\mu_hF_h=0. \tag{11}
\]

Equation (11) is the separate one-coordinate repeated-class two-bar core.
The proof above does not eliminate it: it has no singled-out zero-gradient bar
and its stress-weighted cubic cancels exactly. A formal opposite-cubic cusp is a
binding regression against declaring that cancellation a strict descent.

## 6. Audit, computation, and disposition

Canonical dependencies: actual pure-disk train chart and signed Hessian, Target B
§§37,41--43; finite slack preservation; the strict finite linear alternative.
The phase application is conditional on the explicitly stated unpromoted AP/PG
and October case-3 endpoint hypotheses. The new ZT and ZC bridges are proved
completely above; the baseline reduction is not silently made canonical.

ZT uses **full gradient zero**, not zero KKT multiplier, so it does not integrate
a universally zero source multiplier. ZC handles every pair in the same source
and does not infer feasibility from negative weighted curvature alone. Curvature
terms caused by the correction are checked in (7) and (10). No contact-core-only
motion is transferred to ignored isolated coordinates.

The exact verifier checks rational correction kernels, strict negativity of (6),
the zero-bar expansion of (9), and a concrete rational stress/cubic correction
instance. It does not certify the phase chart's extraction, actual bar geometry,
local/global optimality, or Level I. The arbitrary-size implication is analytic.

An exact algebraic regression delimits the dimension step: on three forward
coordinates take residual gradients `(1,-1,0)`, `(0,1,-1)`, `(-1,0,1)`.
They have a positive equal-weight balance, but their common kernel consists only
of common rotation. Its intersection with the zero-sum plane is zero. This does
not refute ZT or assert a three-diameter source; it shows why ZC's dimension
argument needs the fourth forward coordinate.

**Promotion recommendation:** unreviewed, pending independent audit. No canonical
state, prompt, or state version is changed.

**Next exact lemma:** eliminate (11) by a valid quartic/finite source argument that
also handles its two exactly flat singleton bars. The common strict cubic test
fails identically on its unique stress, so it cannot simply be reused.

## Slot 2 recovery provenance — 2026-10-05

Recovered from `research/full-settlement-20261003` at exact source tip `c044a07f59dbe0993d69c801f73a21f1927838b0`; no original PR was associated with the source branch. This artifact is preserved as a unreviewed proof-only candidate. It does not change theorem state. Any conditional source hypotheses and limits remain as stated above; C-II and Level I remain open.
