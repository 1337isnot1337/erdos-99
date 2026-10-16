<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "869a0809b608a07d09e8c29c1339bc78eb820732", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_nearfloor_pentagon_rank_normal_form_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "94fd72701af6ecfb83e423abe225831f238a1309e58671edb16d07f5e71fbeea"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — direct-energy near-floor pentagon/rank normal form

**Date:** 2026-09-15<br>
**Reviewed:**
- `research/target_c_nearfloor_pentagon_rank_normal_form_2026-09-15.md`
- `research/verify_target_c_nearfloor_pentagon_rank_normal_form.py`

**Disposition:** **PASS at proof-only full-core Type-II scope.**<br>
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The first version of this note was based on the older `1.82890` complement-energy
floor.  Current main now contains the stronger hostile-audited direct
`dominant/complement` energy theorem with safe floor `t>=1.83236`.  The candidate has
therefore been rebased conceptually onto that theorem and now treats the nonempty band

\[
1.83236\le t\le1.8325.
\]

This audit attacks the revised load-bearing steps: margin stability for the *minimized*
direct energy functional, the face-ledger identification of unused network slack,
closure-rank conversion, extension of the older complement-pair lower bound to the
slightly wider detour range, and the strengthened correlated train split.  All pass.

---

## 1. The direct minimized margin has the required monotonicities

Current main defines

\[
G(t,\delta,\kappa)
=\min_K\{F(K-\delta)+J(\pi-K-N_*)\}-\delta.
\]

Its hostile audit proves the minimizing split is unique and interior on the relevant
region, so the envelope theorem applies.  It gives

\[
\partial_\kappa G>0
\]

and

\[
\partial_\delta G
=-F'(z)+2\left(1+{4\Delta_2\over U^2}\right)J'(p)-1.
\]

The parent verifier uses `p<0.72`, `U>=C0` to show this is `<-0.76`.  The present
independent certificate recomputes the coarser expression obtained by dropping the
nonpositive `-F'(z)` term and obtains

\[
2\left(1+{4\Delta_2\over C_0^2}\right)J'(0.72)-1
=-0.77130338\ldots<-0.76.
\]

Thus the round slope `0.76` used by the candidate is conservative.

**Verdict:** PASS.

---

## 2. The stability inequality has the correct sign

For fixed `t` put

\[
\delta_{max}=R(t)/2
\]

and let

\[
G_0(t)=G(t,\delta_{max},0).
\]

Since `G` increases with `kappa`, every survivor satisfies

\[
G(t,\delta,0)
\le G(t,\delta,\kappa)
\le0.
\]

Since `partial_delta G<-0.76`, for `delta<delta_max`,

\[
G(t,\delta,0)
>G_0(t)+0.76(\delta_{max}-\delta).
\]

The parent theorem proves `G_0(t)` strictly decreases with `t`.  The independent
certificate evaluates

\[
G_0(1.8325)
=-0.0003109891582858596\ldots .
\]

Hence any survivor with `t<=1.8325` obeys

\[
\boxed{
\delta_{max}-\delta
<{-G_0(1.8325)\over0.76}
=0.000409196260902447\ldots .
}
\]

The direction is correct: reducing detour makes the contradiction margin more
positive, so a survivor must remain close to maximum detour.

**Verdict:** PASS.

---

## 3. The same slack bounds `kappa` and exceptional degree

The network simplex is

\[
2\delta+\kappa/2\le R(t),
\]

or

\[
\delta+\kappa/4\le\delta_{max}.
\]

Thus

\[
\kappa/4\le\delta_{max}-\delta,
\]

which yields

\[
\boxed{
\kappa<0.00163678504360979\ldots .
}
\]

The face ledger gives

\[
Q/D=2t-\pi-\delta+o(1)
\]

and

\[
f/D\ge C_0/2-t/4+\kappa/4-o(1).
\]

Subtracting,

\[
{Q-f\over D}
\le
{9t\over4}-\pi-{C_0\over2}-\delta-\kappa/4+o(1).
\]

The first three terms equal `delta_max`, so

\[
{Q-f\over D}
\le\delta_{max}-\delta-\kappa/4+o(1).
\]

Therefore

\[
\boxed{(Q-f)/D<0.000409196260902447+o(1).}
\]

This is an exact algebraic coupling of the two ledgers, not a heuristic
identification.

**Verdict:** PASS.

---

## 4. The pentagon count is occurrence-safe and loses one degree-excess unit per high-degree face

Every bounded exceptional face has degree at least five, and

\[
Q-f=\sum_F(\deg F-5).
\]

Thus each face of degree at least six spends at least one unit of `Q-f`, so

\[
f_{>=6}\le Q-f.
\]

For `t<=1.8325`, `kappa>=0` gives

\[
f/D\ge C_0/2-1.8325/4-o(1)
=0.4966878068639573\ldots-o(1).
\]

Therefore

\[
\boxed{p_5/D>0.4962786106030549\ldots-o(1).}
\]

The high-degree fraction among the guaranteed exceptional-face population is below
`0.000824`, so the `99.9176%` purity statement is conservative.

**Verdict:** PASS.

---

## 5. The closure-rank floor uses the right defect parameter

Canonical notation is

\[
k=d_H+s_Z,
\qquad d_H,s_Z\ge0,
\]

so `s_Z<=k`.  The exact closure-corank identity is

\[
2f-\operatorname{rank}C_{face}
=\sigma_C\le s_Z.
\]

Using the certified `f` floor and `kappa=k/D` cap gives

\[
\boxed{
\operatorname{rank}C_{face}/D
>0.9917388286843049\ldots-o(1).
}
\]

The theorem correctly makes no smallest-singular-value claim.  Nearly flat pentagon
blocks can remain badly conditioned while the exact row rank is almost maximal.

**Verdict:** PASS.

---

## 6. The complement outer-to-outer train lower bound is not taken from the optimized split

A potentially invalid shortcut would be to identify the direct theorem's optimizing
value

\[
p_{opt}\approx0.57104
\]

with a universal complement-train population.  The candidate explicitly does not do
this.

Instead it reuses the independently audited complement-capacity lower bound

\[
p_c
\ge
\pi-Q_\Phi(\delta)-U-(t+\kappa)/2+4\Delta_2/U.
\]

The older certificate only needed `Q_Phi<1.62`; the present band extends beyond that.
The new verifier checks instead

\[
Q_\Phi(\delta)<1.81,
\]

and

\[
\Phi'(1.81)=0.04383765\ldots<0.044,
\qquad
1/\Phi'(1.81)>22.7.
\]

Meanwhile the magnitude of the complement-count derivative with respect to `delta` is
less than `4`.  Hence

\[
\partial_\delta p_c<-18.7<0
\]

throughout the band.  The original algebra still gives `partial_kappa p_c>0`, and on
the maximum-detour boundary `p_c` decreases with `t`.

Thus the worst point is `t=1.8325`, `kappa=0`, `delta=delta_max`, where the certificate
gives

\[
\boxed{p_c=0.4081989620519120\ldots .}
\]

Since retained weight on one train is at most one, this implies at least the same
normalized count of actual complement outer-to-outer trains.  Section 157 supplies
actual diameter bracing of both transverse signs for each.

**Verdict:** PASS.

---

## 7. The correlated stopped-train update uses the current main floor

Exact train bookkeeping gives

\[
\rho_{rec}+\sigma_R=2T-4\sqrt{R_4}.
\]

The hostile-audited `g=0.0050` theorem and rhombic saturation imply

\[
(\rho_{rec}+\sigma_R-q)/D\ge0.0100-o(1).
\]

Current main now proves

\[
t=(q-k)/D\ge1.83236-o(1),
\]

and `k>=0`, hence

\[
q/D\ge1.83236-o(1).
\]

Therefore

\[
\boxed{(\rho_{rec}+\sigma_R)/D\ge1.84236-o(1).}
\]

The branch split is then

\[
S/D\ge0.46059-o(1)
\]

or

\[
\sigma_R/D\ge0.92118-o(1).
\]

The exact Mantel rationalization gives

\[
\boxed{M_R/D^2>0.4916615427-o(1)}
\]

in the rhombic branch.  The post-endpoint surplus identity gives

\[
\boxed{\liminf\mu_D\ge1.8217981841815002\ldots .}
\]

There remains no universal upper bound on `mu_D` below this value.

**Verdict:** PASS.

---

## 8. Scope and remaining obstruction

The result is nonvacuous because the current safe theorem floor is `1.83236`, while the
candidate treats all survivors through `1.8325`.  It does not assume the unclaimed
numerical root `1.8323676...` as theorem authority.

It proves no local pentagon nondegeneracy, no quantitative singular-value gap, no
injective diameter-edge assignment to the outer-to-outer trains, and no simultaneous
source-preserving train shear.  Those are exactly the remaining compatibility routes.

**Final disposition:** **PASS at proof-only full-core Type-II scope. C-II and Level I
remain open.**
