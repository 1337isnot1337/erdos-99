<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cb76a4485b592763e74f46d9ef76435feb7df65c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_chamber_surplus_repacking_barrier_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "27a4d64170aa27781e74cc999645d71e0d754401fbcd5065f809236f22209e94"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact barrier: high-`t` chamber surplus is mandatory boundary credit, not safe-repacking residual

**Date:** 2026-09-15  
**Status:** proof-only exact accounting identity / route barrier  
**Scope:** canonical Section-77 inactive chambers inside the force hull; applied to every remaining full-core Type-II survivor  
**Dependencies:** inactive-chamber residual conservation; canonical Section-85 interface currency; aggregate safe-lattice repacking theorem  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The modern high-`t` theorem proves

\[
A_{ch}-a_0Z_{ch}\ge(0.586223-o(1))D,
\qquad
a_0={\sqrt3\over2}.
\]

It is tempting to treat this linear Oler surplus as packing spare and compare it with the vertex-cover cost `tau(H)`.  That inference is false.  The exact chamber ledger shows that the Section-85 lower bound is precisely the mandatory boundary-credit term; the genuine force-hull residual `R_F` is the excess **above** that term.

With

\[
H_D=(b-P_F)+(Q+2f)
=2[(q-k)+f]-P_F,
\tag{RB.1}
\]

and

\[
R_F={A_F\over a_0}+{P_F\over2}+1-N_F-{E_4\over a_0},
\tag{RB.2}
\]

one has the finite exact identity

\[
\boxed{
{A_{ch}\over a_0}-Z_{ch}
=R_F+{H_D\over2}.
}
\tag{RB.3}
\]

Equivalently,

\[
\boxed{
A_{ch}-a_0Z_{ch}
=a_0R_F+{\sqrt3\over4}H_D.
}
\tag{RB.4}
\]

Therefore canonical Section 85,

\[
A_{ch}-a_0Z_{ch}\ge {\sqrt3\over4}H_D,
\]

is exactly the statement

\[
R_F\ge0.
\]

The new high-`t` lower bound `H_D/D>=1.353825-o(1)` consequently forces the advertised `0.586223D` chamber surplus even when `R_F=o(D)` or identically zero at first order.  It supplies no positive lower bound on the residual used by aggregate safe-lattice repacking.

The safe-lattice theorem instead requires

\[
\Xi=R_F
-\kappa_*L_c
-\lambda_*L_{add}
-C_*f
-\eta_*a
\ge\tau(H)
\]

for a strict-diameter competitor.  Since every erosion term is nonnegative, the high-`t` Section-85 surplus alone cannot prove even `Xi>0`, much less `Xi>=tau(H)`.

This rules out the direct composition

```text
high-t chamber surplus > 0.586223 D
+ diameter vertex-cover upper bound
=> aggregate safe-lattice repacking.
```

Any successful repacking route must obtain new positive information on `R_F` itself (and then overcome the wall-loss terms), or use a replacement geometry whose safe area does not pay those boundary erosions.

---

## 1. Derivation of the exact identity

Canonical chamber bookkeeping gives

\[
A_{ch}=A_F-A_4,
\qquad
A_4=a_0R_4+E_4,
\tag{RB.5}
\]

\[
Z_{ch}=N_F-m,
\tag{RB.6}
\]

and

\[
m=R_4+f+q-k+1.
\tag{RB.7}
\]

Hence

\[
\begin{aligned}
{A_{ch}\over a_0}-Z_{ch}
&={A_F\over a_0}-R_4-{E_4\over a_0}-N_F+m\\
&={A_F\over a_0}-N_F-{E_4\over a_0}+f+q-k+1.
\end{aligned}
\tag{RB.8}
\]

Subtract (RB.2):

\[
\begin{aligned}
\left({A_{ch}\over a_0}-Z_{ch}\right)-R_F
&=f+q-k-{P_F\over2}\\
&={1\over2}\left(2[(q-k)+f]-P_F\right)\\
&={H_D\over2}.
\end{aligned}
\]

This proves (RB.3).  Multiplication by `a_0=sqrt(3)/2` gives (RB.4).

No asymptotic statement is used.

---

## 2. Numerical consequence for the current high-`t` theorem

The modern high-`t` theorem proves

\[
{H_D\over D}\ge1.353825-o(1).
\]

The mandatory boundary-credit part in (RB.4) is therefore

\[
{\sqrt3\over4}H_D
\ge(0.586223-o(1))D,
\]

which is exactly the published high-`t` chamber-surplus floor up to the outward rounding in its certificate.

Thus the full numerical gain is already accounted for by `H_D`.  There is no hidden leftover linear term that can be assigned to `R_F`.

---

## 3. Interaction with the aggregate repacking theorem

The audited aggregate safe-lattice theorem first realizes a safe-region surplus bounded below by

\[
\Xi=R_F
-\kappa_*L_c
-\lambda_*L_{add}
-C_*f
-\eta_*a.
\tag{RB.9}
\]

It then closes if

\[
\Xi\ge\tau(H).
\tag{RB.10}
\]

Equation (RB.3) shows why replacing `R_F` in (RB.9) by the raw Oler surplus is invalid: doing so adds `H_D/2` a second time even though that amount is exactly the chamber-boundary credit already required by Oler.

In fact (RB.9) immediately gives

\[
\Xi\le R_F.
\tag{RB.11}
\]

So a necessary first step for this repacking architecture is a positive lower bound on `R_F` of at least vertex-cover scale.  The current high-`t` theorem gives only the canonical nonnegativity `R_F>=0`.

---

## 4. Frontier effect

The new high-`t` structural inputs remain useful, but not through a direct Section-85-to-lattice composition.  The viable directions are now separated cleanly:

1. **Residual route:** derive a genuinely new lower bound on `R_F`, then quantify the wall-loss terms in `Xi`.
2. **Low-erosion replacement:** build a source-level replacement whose protected region pays less than the contact-wall erosion in (RB.9).
3. **Variational route:** use the live low-energy O--O path, common diameter-routing hub, and one-sided `<=341` strip to obtain a strict-diameter deformation without deleting a global diameter vertex cover.
4. **Corridor route:** use the forced high-`t` interface/chamber currency to constrain the Section-84 doubled near-geodesic corridors rather than interpreting it as free packing area.

The third route currently has the sharpest local normal form; the first route now has an explicit missing scalar, `R_F`, rather than the misleading raw chamber surplus.

**Disposition:** exact route barrier proved.  The `0.586223D` high-`t` chamber surplus cannot by itself fund aggregate safe-lattice repacking. C-II and Level I remain open.
