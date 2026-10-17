> Generated reading edition · [exact source](../../../docs/audits/target_c_section149_atomic_orbit_hostile_audit_2026-09-12.md) · source SHA-256 `41378ee0062650e2e348d6a807dd346de9c490f11abd552cfbc24a17f2de58af`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DB1700803BBE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C Section 149 atomic phase-orbit step

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_section149_quantitative_atomic_detour_stability.md`  
**Base state:** `2026-09-12.audit.46`  
**Disposition:** **PARTIAL PASS; the all-regime theorem is not established as written.**  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Claims that pass

The outer-walk measure and Fourier calculation in §§149.1--149.2 are valid at the
stated subsequential scope. If `nu` is the weak limit of the occurrence-counted
projective outer measure and

$$
g(\alpha)=\int|\cos(\theta-\alpha)|\,d\nu(\theta)-2\ge0,
$$

then its mean is `2 delta/pi`. The Fourier coefficient of `g` at frequency `n` has
modulus

$$
\frac{2}{\pi(4n^2-1)}|\widehat\nu(n)|,
$$

so positivity gives

$$
|\widehat\nu(n)|\le \delta(4n^2-1).
$$

Pushing forward by `theta -> 6 theta` and applying the nonnegative Fejer kernel also
validly gives (149.9)--(149.10), an upper bound for the squared masses of **outer
atomic phase-orbit atoms**.

The arithmetic in §§149.5 and the displayed scalar implications is correct if the
unproved endpoint-capacity theorem in §149.4 is granted.

## 2. The unsupported step is (149.11)

Section 149.3 defines `S_j` only from the atoms of the weak limiting stopped-train
direction measure after quotienting directions modulo `pi/3`. It then asserts

$$
\sum_j S_j^2\ge \frac{4\Delta_2}{x^2}. \tag{A149.1}
$$

The cited §142 saturation input, as recorded in the current proof-only source, says
only that all but `o(D^2)` rhombus crossings have projective direction separation
tending to `pi/3`. This is a statement about the limiting **pair measure** of
crossing directions. It does not by itself say that the marginal train measure on
the quotient is purely atomic, nor that positive crossing mass is confined to its
atomic fibers.

A non-atomic coupling can be supported on the relation

$$
\eta=\xi+\pi/3
$$

while its marginal on the quotient parameter `xi mod (pi/3)` is non-atomic. In that
measure-level situation every `S_j` is zero although the crossing pair measure can
have positive mass. The finite train graph being simple and triangle-free does not
turn a support statement for a pair measure into a purely atomic marginal statement.
Weighted Mantel applies to a finite set of trains in one already identified phase
class; it does not justify summing over only the atoms of a weak limit when the phase
class itself varies with `D`.

This is not a claim that such a coupling has already been realized by a global
triangle-free minimizer. It is an exact missing implication in the proof: no theorem
in the cited dependency list supplies the required atomization or uniform phase-bin
estimate.

## 3. The required repair

To recover (149.11), the source needs a new finite-to-limit lemma of the following
kind. Let `G_D` be the stopped-train crossing graph, let `xi_tau` be the quotient
phase of train `tau`, and let `E_D^{far}(epsilon)` count crossing edges whose quotient
phase separation exceeds `epsilon`. One would need to prove, from the actual
geometric crossing rules and triangle-free graph alone, that

$$
E_D^{far}(\epsilon)=o(D^2)\quad(\epsilon>0\text{ fixed})
$$

and `|E_D|/D^2 -> Delta_2` imply

$$
\limsup_D\frac{|E_D|}{D^2}
\le \frac{x^2}{4}\sum_j S_j^2. \tag{A149.2}
$$

The factor `1/4` would require a localized Mantel argument after isolating the
atomic quotient neighborhoods; the ordinary degree-neighborhood estimate gives only
the weaker factor `1/2` and does not by itself identify the atoms. The necessary
order of limits, treatment of atom neighborhoods, and cross-neighborhood edges must
all be written explicitly.

Until (A149.2) is proved, the endpoint-capacity inequality (149.12), the tradeoff
(149.13), and the exclusion window (149.22) remain conditional. They cannot be
promoted or used as an all-regime C-II closure bridge.

## 4. Additional scope checks

- The Fourier part retains occurrence multiplicity and does not drop bridges.
- No contact-isolated source point is removed, and no full-source affine-kernel claim
  is used.
- The §149 source itself correctly states that it does not close C-II; this audit
  narrows that statement by identifying the missing atomization theorem.
- The Type-I macroscopic-container branch is untouched.

**Final verdict:** the outer Fourier/Fejer estimate is a valid proof-only lemma, but
the phase-orbit crossing lower bound is an unproved bridge. Section 149 as a whole is
not an audited all-regime theorem; C-II remains open.
