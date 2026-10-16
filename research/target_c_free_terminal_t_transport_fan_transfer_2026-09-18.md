<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a073a663dae54ea194127db4075cfe066ccf542e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_t_transport_fan_transfer_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "bf70bac9f0c348b311be35768a3593471778e4391c11011b681fd59d1664b5a5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact `t` cancellation transfers the transport/fan ladder

**Date:** 2026-09-18  
**Status:** proof-only correction/strengthening of the terminal transport/fan scope; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE subsequences with `pi D-q=o(D)`  
**Depends on:** exact terminal `t` decomposition; matched all-train gap `g=0.007707`; terminal train ledger; `target_c_free_terminal_transport_fan_ladder_2026-09-18.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The transport/fan ladder was originally written with an upper hypothesis on the older all-phase surplus variable `mu_D`. The later exact cancellation theorem shows that its two scalar stability inputs hold directly under an upper hypothesis on

\[
t_D={q-k\over D}.
\]

This matters after the correlated `0.00704` theorem: the old `mu_D` may contain an additional nonunit-hull-side term, so an upper bound on `t_D` does not by itself upper-bound the old `mu_D`. The fan ladder therefore needs an explicit `t`-based transfer rather than a silent variable substitution.

The transfer is exact. No new geometric hypothesis is required.

---

## 1. Exact `t` defect constraint

Put

\[
s_2:=\sqrt{\frac\pi{2\sqrt3}},
\qquad
g:=0.007707,
\qquad
\tau_*:={\pi\over2}+g,
\]

and

\[
M_*:=4s_2+2g,
\qquad
p_*:={M_*\over5}.
\tag{1.1}
\]

The exact terminal identity is

\[
q-k
=
{2P_F+2\sqrt{R_4}\over5}
+{2\over5}(Q-f)
+{2\over5}(b-P_F)
+{1\over5}\tau_D,
\tag{1.2}
\]

where

\[
\tau_D:=T-2\sqrt{R_4}.
\]

Along a terminal subsequence define the nonnegative normalized defects

\[
r:=\lim {Q-f\over D},
\qquad
\delta:=\lim {b-P_F\over D},
\qquad
 a:=\lim\left({\tau_D\over D}-{\pi\over2}-g\right).
\tag{1.3}
\]

Terminality gives

\[
{P_F\over D}\to\pi,
\qquad
{\sqrt{R_4}\over D}\to s_2,
\]

and the matched all-train theorem gives `a>=0`.

Therefore

\[
\boxed{
\lim(t_D-\mu_*)
={2\over5}(r+\delta)+{1\over5}a,
}
\tag{1.4}
\]

where

\[
\mu_*
={\pi\over2}+{2\over5}s_2+{g\over5}
=1.953262849540479\ldots .
\]

Hence an upper hypothesis

\[
\limsup t_D\le\mu_*+\varepsilon
\tag{1.5}
\]

implies the exact stability constraint

\[
\boxed{
a+2(r+\delta)\le5\varepsilon.}
\tag{1.6}
\]

This is the first scalar input used by the transport/fan ladder.

---

## 2. The face-count formula also follows from `t` data alone

The second scalar input in the fan ladder is the normalized exceptional-face count. It does not depend on `mu_D` either.

Use the exact train ledger

\[
2T=b+Q+4f
\tag{2.1}
\]

and

\[
T=2\sqrt{R_4}+\tau_D.
\tag{2.2}
\]

Write

\[
x:=\lim {f\over D}.
\]

Since

\[
{b\over D}\to\pi+\delta,
\qquad
{Q\over D}\to x+r,
\]

while

\[
{2T\over D}
\to4s_2+\pi+2g+2a
=\pi+M_*+2a,
\]

equating the two sides of (2.1) gives

\[
\pi+M_*+2a
=\pi+\delta+r+5x.
\]

Thus

\[
\boxed{
{f\over D}
={M_*+2a-\delta-r\over5}+o(1).
}
\tag{2.3}
\]

This is exactly the second stability formula used in the transport/fan ladder.

---

## 3. Every fan-ladder count transfers verbatim

The remainder of the transport/fan proof uses only:

1. the endpoint multigraph identities
   \[
   2E_{BB}+E_{BO}=4f+Q,
   \qquad
   E_{BO}+2L_O=b;
   \]
2. the superpentagon bound
   \[
   n_+\le Q-f;
   \]
3. the full-flower incidence inequality
   \[
   P_5-F_5^{full}\le2S;
   \]
4. terminality `b/D=pi+delta+o(1)`;
5. the two scalar formulas (1.6) and (2.3).

No later step uses the old surplus variable itself. Therefore equations (2.1)--(4.8) of the transport/fan ladder re-run unchanged under (1.5).

For `1<=k<=4`, if `F^{full}_{5,>=kO}` counts fully rhombic pentagons with at least `k` pentagon-to-outer stopped trains, then

\[
\boxed{
\max\left\{
{S\over D},
{L_O\over D},
{F^{full}_{5,\ge kO}\over D}
\right\}
\ge C_k^{(t)}(\varepsilon)-o(1),
}
\tag{3.1}
\]

where

\[
\boxed{
C_k^{(t)}(\varepsilon)
=
{\pi-(k-1)p_*-3(6-k)\varepsilon\over20-3k}.
}
\tag{3.2}
\]

Thus the transport/fan ladder is now a theorem about actual terminal feasibility `t_D`, not merely the older all-phase surplus.

---

## 4. Concrete live constants above the `0.00704` floor

Take

\[
\varepsilon_0=0.00710.
\]

The correlated theorem excludes all terminal survivor limits at or below `0.00704` above `mu_*`, so this is a concrete narrow window immediately above the certified floor.

Equation (3.2) gives

| `k` | `C_k^(t)(0.00710)` | guaranteed outer spokes `k C_k` |
|---:|---:|---:|
| 1 | `0.178534861975870...` | `0.178534861975870...` |
| 2 | `0.163675686292759...` | `0.327351372585518...` |
| 3 | `0.140711505691587...` | `0.422134517074762...` |
| 4 | `0.100524189639537...` | `0.402096758558148...` |

The `k=3` row again maximizes the guaranteed number of localized outer-reaching spokes. In particular, every terminal subsequence satisfying

\[
\limsup t_D\le1.960362849540479\ldots
\]

obeys

\[
\boxed{
\max\left\{
S/D,\ L_O/D,\ F^{full}_{5,\ge3O}/D
\right\}
\ge0.140711505691587\ldots-o(1).
}
\tag{4.1}
\]

This is the `t`-based input used by `target_c_free_terminal_live_flex_diameter_locking_2026-09-18.md`.

---

## 5. Scope

- The transfer uses the exact `m_B` cancellation in the terminal `t` identity. It does not assume `m_B=o(D)`.
- No upper bound on the old all-phase `mu_D` is inferred from an upper bound on `t_D`.
- The geometric endpoint multigraph, fan, and full-flower arguments are unchanged.
- The statement is proof-only because it inherits the matched-gap and terminal transport dependencies.
- No theorem-state file is changed.

**Disposition:** repaired the transport/fan scope so that the live fan ladder is controlled directly by `t_D`; C-II remains open.
