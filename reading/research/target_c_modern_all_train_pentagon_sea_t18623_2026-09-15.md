> Generated reading edition · [exact source](../../research/target_c_modern_all_train_pentagon_sea_t18623_2026-09-15.md) · source SHA-256 `c05b9f9596a8e29f02af899b95335e65cd326fd1297a994e329acef6bb6f0e9f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "18a4548f42332f1304331097920e34905bc361b8", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_modern_all_train_pentagon_sea_t18623_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1d980066af6ca1e856f1adb8a1c95a1b32f4a00909b2d427f81d355e5e0643b7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the modern all-train gap forces a pentagon sea through `t<=1.8623`

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II train-measure branch with `t=(q-k)/D<=1.8623`  
**Dependencies:** hostile-audited scope-safe matched all-train gap `g=0.007707`; canonical stopped-train/face ledger; canonical loaded-hull identity; Type-II force-hull disk limit  
**Certificate:** `research/verify_target_c_modern_all_train_pentagon_sea_t18623.py`  
**Supersedes numerically:** `target_c_high_t_pentagon_face_floor_2026-09-15.md` on every common endpoint  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The hostile-audited modern all-train theorem proves throughout the full-core train-measure
branch

$$
\boxed{
\liminf {T-q/2\over D}
\ge C_{707}:=2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3}.
}
\tag{MPS.1}
$$

The earlier modern pentagon note first converted this to the weaker train-slack floor
`tau/D>=rho+0.007707`, losing the direct `T-q/2` information.  That loss is unnecessary
when the goal is to count bounded exceptional faces.

Use the exact stopped-train ledger

$$
T-q=2f-k
\tag{MPS.2}
$$

and put

$$
t={q-k\over D},
\qquad
\kappa={k\over D}.
$$

Then

$$
{T-q/2\over D}
={t\over2}+2{f\over D}-{\kappa\over2}.
\tag{MPS.3}
$$

Consequently every survivor with `t<=1.8623` has

$$
\boxed{
{f\over D}>0.490D-o(1),
}
\tag{MPS.4}
$$

and degree arithmetic forces

$$
\boxed{
{P_5\over D}>0.398D-o(1),
}
\tag{MPS.5}
$$

where `P_5` is the number of bounded pentagonal contact faces.  More than `81%` of the
bounded nonquadrilateral faces are pentagons.

Every pentagon contributes five terminal face-side occurrences to the complete stopped-
train decomposition.  Since one stopped train has only two terminal occurrences,

$$
\boxed{
{N_5\over D}>0.99-o(1),
}
\tag{MPS.6}
$$

where `N_5` is the number of distinct complete stopped trains touching at least one
pentagon.

The bounded exceptional faces alone also satisfy

$$
\boxed{
{A_{exc}-a_0Z_{def}\over D}>0.637-o(1),
\qquad a_0={\sqrt3\over2}.
}
\tag{MPS.7}
$$

This is stronger, on the `t<=1.8623` window, than the previously advertised total
Section-85 chamber-surplus floor `0.586223D`: the exceptional bounded faces alone already
pay more.  This does not contradict the exact repacking-barrier identity; the payment is
mandatory boundary credit, not positive safe-repacking residual.

The pentagon conclusion is independent of the high-`t` O--O path extraction.  The
former path claims through `t<=1.8623` were later retracted because their oriented
terminal-branch step was incomplete.  The corrected opposite-branch theorem currently
gives a live path only through `t<=1.8593`; none of (MPS.1)--(MPS.7) uses that path.
Thus the `t<=1.8623` pentagon-sea endpoint remains valid even where no live O--O path is
currently proved.

---

## 1. Direct exceptional-face floor from the all-train gap

From (MPS.1)--(MPS.3),

$$
2{f\over D}
\ge C_{707}-{t\over2}+{\kappa\over2}-o(1).
$$

Since `kappa>=0`, for every fixed upper endpoint `t<=T`,

$$
\boxed{
\liminf {f\over D}
\ge f_0(T):={C_{707}\over2}-{T\over4}.
}
\tag{MPS.8}
$$

The exact outward certificate gives

$$
\begin{array}{c|c}
T & f_0(T)\\ \hline
1.8500 & >0.4936663\\
1.8550 & >0.4924163\\
1.8600 & >0.4911663\\
1.8623 & >0.4905913.
\end{array}
\tag{MPS.9}

The key point is that this uses the modern `0.007707` all-train theorem directly.  No
Dottie-number lower bound and no residual/low-`t` localization are required.

---

## 2. Total exceptional degree remains capped by `t`

Canonical loaded-hull algebra gives

\[
\boxed{b+Q=2(q-k),}
\tag{MPS.10}
$$

where `b` is the occurrence-counted old outer contact-face walk and

$$
Q=\sum_P(\deg P-4)
$$

over bounded nonquadrilateral faces.

The closed outer walk contains every force-hull extreme vertex, so

$$
b\ge\operatorname{per}(F).
\tag{MPS.11}
$$

Canonical Type II gives

$$
{\operatorname{per}(F)\over D}\to\pi.
\tag{MPS.12}
$$

Thus, for `t<=T`,

$$
\boxed{
\limsup {Q\over D}
\le Q_0(T):=2T-\pi.
}
\tag{MPS.13}
$$

At `T=1.8623` the exact certificate gives

$$
Q/D<0.583008+o(1).
\tag{MPS.14}
$$

No assumption that `b/D` itself converges to `pi` is used.

---

## 3. More than `0.398D` actual pentagons

Let `P_5` count degree-five bounded exceptional faces.  Every other bounded exceptional
face has degree at least six, so

$$
Q\ge P_5+2(f-P_5)=2f-P_5.
$$

Hence

$$
\boxed{P_5\ge2f-Q.}
\tag{MPS.15}
$$

Using (MPS.8) and (MPS.13),

$$
\boxed{
\liminf {P_5\over D}
\ge p_5(T):=2f_0(T)-Q_0(T)
=\pi+C_{707}-{5T\over2}.
}
\tag{MPS.16}
$$

The exact staircase is

$$
\begin{array}{c|c}
T & p_5(T)\\ \hline
1.8500 & >0.4289252\\
1.8550 & >0.4164252\\
1.8600 & >0.4039252\\
1.8623 & >0.3981752.
\end{array}
\tag{MPS.17}

At the widest endpoint,

\[
\liminf {P_5\over f}
\ge2-{Q_0(1.8623)\over f_0(1.8623)}
>0.8116.
\tag{MPS.18}
$$

Thus the high-`t` exceptional-face population is already overwhelmingly pentagonal at
the widest certified pentagon-sea endpoint.

---

## 4. Nearly one train per unit diameter touches a pentagon

Every contact edge belongs to one complete stopped train.  A boundary edge occurrence
of a bounded nonquadrilateral face is a terminal occurrence of that train; the train
cannot continue through the nonquadrilateral face as a strict-rhombus train segment.
Therefore each pentagon supplies exactly five stopped-train terminal face-side
occurrences.

A complete stopped train has only two terminal occurrences in total.  If `N_5` counts
trains with at least one pentagon terminal, then

$$
\boxed{N_5\ge{5P_5\over2}.}
\tag{MPS.19}
$$

Combining with (MPS.17),

$$
\begin{array}{c|c}
T & N_5/D\\ \hline
1.8500 & >1.0723\\
1.8550 & >1.0410\\
1.8600 & >1.0098\\
1.8623 & >0.9954.
\end{array}
\tag{MPS.20}

This count includes singleton stopped trains when the complete-train convention does;
it is an all-stopped-train endpoint statement, not a strict-rhombus-boundary statement.

---

## 5. Exceptional bounded faces alone pay `>0.637D` Oler surplus

Canonical Section 67 proves

\[
A_{exc}\ge a_0(Z_{def}+f)+c_0Q,
\qquad
c_0={\sqrt3\over4}.
\tag{MPS.21}
$$

Since `Q>=f`,

$$
A_{exc}-a_0Z_{def}
\ge(a_0+c_0)f
={3\sqrt3\over4}f.
\tag{MPS.22}
$$

Using (MPS.9), the exact certificate gives

\[
\begin{array}{c|c}
T & (A_{exc}-a_0Z_{def})/D\\ \hline
1.8500 & >0.641\\
1.8550 & >0.639\\
1.8600 & >0.638\\
1.8623 & >0.637.
\end{array}
\tag{MPS.23}

This does not create a new safe-packing residual.  The exact high-`t` repacking barrier
shows that chamber Oler surplus includes mandatory internal-boundary credit.  Equation
(MPS.23) identifies where much of that mandatory credit is physically located.

---

## 6. Relation to earlier pentagon artifacts

The September-14 proof-only pentagon-sea note derived the same algebra from the older
AG42 constant `2sqrt(Delta_2)+0.00042` and obtained `P_5>0.4003D` only through
`t<=1.8585`.  The present theorem uses the hostile-audited modern all-train gap
`0.007707` and extends the direct pentagon sea through `t<=1.8623`, independently of
the later-retracted path claim at that endpoint.

The earlier same-day note `target_c_high_t_pentagon_face_floor_2026-09-15.md` used only
the weaker consequence `tau/D>=rho+0.007707`; its bounds remain valid but are
numerically superseded by (MPS.17).

---

## 7. Binding regression and next step

The exact pentagon-lattice regression remains binding.  A convex unit-edge pentagon can
approach the three triangular-lattice projective directions while all relevant extra
diagonals approach length one.  Therefore no uniform positive angular or area excess
per pentagon follows from pentagon existence alone.

The new information is global network occupancy:

```text
~0.4 D actual pentagons
+ ~1.0 D stopped trains terminating on pentagons
+ modern train-slack singleton/rhombic-Mantel dichotomy
+ (only for t<=1.8593) the separately repaired opposite-branch O-O hub path.
```

A closing theorem should use train **routing**, not local pentagon nondegeneracy.  In
the overlap band `t<=1.8593`, one concrete target is to couple the pentagon-terminal
train population to the corrected common-hub O--O path.  On the full `t<=1.8623`
pentagon range, the recipient-waste/singleton versus rhombic-Mantel split remains
available without any path hypothesis.

**Disposition:** proved proof-only modern pentagon-sea and pentagon-terminal train
population through `t<=1.8623`.  C-II and Level I remain open.
