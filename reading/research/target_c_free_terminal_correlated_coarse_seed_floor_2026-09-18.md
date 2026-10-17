> Generated reading edition · [exact source](../../research/target_c_free_terminal_correlated_coarse_seed_floor_2026-09-18.md) · source SHA-256 `62371eb692ac3a4c5e988709ac16c30a66b606b41afdd9f7f8732855b7676759`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d51a1d163bcdcd5445f8126f6ec0fa36dbf1f355", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_correlated_coarse_seed_floor_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c22c296dc3915cca704b5dda1f6117565a9968ae2b098c448c7c8f1dda8247a5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — correlate the coarse pentagon-seed cap with the terminal defect ledger

**Date:** 2026-09-18  
**Status:** proof-only quantitative strengthening; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE subsequences with `limsup t_D <= mu_*+0.00710`  
**Depends on:** coarse pentagon-bootstrap corank theorem; exact terminal `t` decomposition; exact terminal face ledger; live detour pinching `delta>0.017609`; exact defect partition `k=d_H+p_D+sigma_C`  
**Certificate:** `research/verify_target_c_free_terminal_correlated_coarse_seed_floor_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The coarse pentagon-bootstrap theorem proves

$$
\sigma_C\le {2\over3}f+{4\over3}(Q-f).
\tag{1}
$$

Its first live consequence combined independent upper bounds for `f/D` and `(Q-f)/D` with an independent lower bound for `k/D`, giving

$$
{d_H+p_D\over D}>0.6733591-o(1).
$$

Those three extrema cannot occur simultaneously. Keeping the exact terminal correlation raises the unconditional unconverted-defect floor to

$$
\boxed{
{d_H+p_D\over D}>0.6734530-o(1).
}
\tag{2}
$$

The numerical gain is about `9.4e-5 D`. No new geometry is used.

---

## 1. Exact correlated formulas

Along a terminal subsequence write

$$
r={Q-f\over D},
\qquad
\delta={b-P_F\over D},
\qquad
a={\tau_D\over D}-{\pi\over2}-0.007707.
$$

The exact terminal `t` decomposition gives

$$
{q-k\over D}
=\mu_*+{a+2r+2\delta\over5}+o(1),
\tag{3}
$$

where

$$
\mu_*={\pi\over2}
+{2\over5}\sqrt{\frac\pi{2\sqrt3}}
+{0.007707\over5}.
$$

Hence, putting

$$
K_*:=\pi-\mu_*
={\pi\over2}-{2\over5}\sqrt{\frac\pi{2\sqrt3}}-{0.007707\over5},
$$

we have

$$
{k\over D}
=K_*-{a+2r+2\delta\over5}+o(1).
\tag{4}
$$

The exact face ledger is

$$
{f\over D}
={M_*+2a-\delta-r\over5}+o(1),
\qquad
M_*=4\sqrt{\frac\pi{2\sqrt3}}+2(0.007707).
\tag{5}
$$

The live assumptions give

$$
a+2(r+\delta)\le5\varepsilon_0,
\qquad
\varepsilon_0=0.00710,
\tag{6}
$$

and the certified detour pinching

$$
\delta>\delta_0:=0.017609.
\tag{7}
$$

---

## 2. Eliminate the correlated defects before rounding

Let

$$
x_D={d_H+p_D\over D}.
$$

Since `k=d_H+p_D+sigma_C`, equations (1), (4), and (5) give

$$
\begin{aligned}
x_D
&\ge {k\over D}-{2f\over3D}-{4r\over3}+o(1)\\
&\ge K_*-{2M_*\over15}
-{7a\over15}-{8r\over5}-{4\delta\over15}+o(1).
\end{aligned}
\tag{8}
$$

The defect penalty is

$$
{7a+24r+4\delta\over15}.
$$

Use the exact identity

$$
7a+24r+4\delta
=7\bigl(a+2r+2\delta\bigr)+10(r-\delta).
\tag{9}
$$

By (6),

$$
7\bigl(a+2r+2\delta\bigr)\le35\varepsilon_0.
$$

Also (6) with `a>=0` gives

$$
r+\delta\le{5\varepsilon_0\over2}=0.01775,
$$

and therefore, using (7),

$$
r-\delta
\le0.01775-2\delta
<0.01775-2(0.017609).
\tag{10}
$$

Substitute (9)--(10) into (8):

$$
\boxed{
 x_D
>
K_*-{2M_*\over15}
-{1\over15}\left[
35\varepsilon_0
+10\left({5\varepsilon_0\over2}-2\delta_0\right)
\right]
-o(1).
}
\tag{11}
$$

The exact-rational certificate evaluates the right-hand side with outward enclosures for `pi`, `sqrt(3)`, and `sqrt(pi/(2sqrt(3)))` and proves

$$
\boxed{x_D>0.6734530-o(1).}
\tag{12}
$$

This proves (2).

The optimization in (9) is transparent: after the mandatory detour `delta_0` is paid, residual degree excess `r` is the most expensive remaining use of the correlated `t` budget. The extremal relaxation is `a=0`, `delta=delta_0`, `r=0.01775-delta_0=0.000141`.

---

## 3. Updated live frontier

The correlated degree-weighted seed theorem gives

$$
{d_H+p_D\over D}+{8\over15}{m_D\over D}>1.5158692-o(1),
\tag{13}
$$

while the sealed-component line gives

$$
{d_H+p_D\over D}>5.9765850-4{m_D\over D}-o(1).
\tag{14}
$$

Replacing the old coarse floor by (12), the current certified piecewise envelope is

$$
\boxed{
{d_H+p_D\over D}
>
\max\left\{
5.9765850-4{m_D\over D},
\ 1.5158692-{8\over15}{m_D\over D},
\ 0.6734530
\right\}-o(1).
}
\tag{15}
$$

The safe rounded middle line meets the new coarse floor at

$$
{m_D\over D}=1.579530375.
$$

Using the unrounded certified constants moves this only in the seventh decimal place. The lower-flex crossing with the sealed-component line is unchanged at about `1.2867449`.

---

## 4. Remaining bottleneck

This is another correlation recovery, not a new geometric mechanism. It makes the high-flex end of the live feasible region slightly smaller and removes an inconsistent simultaneous worst case from the coarse pentagon-seed consequence.

The unresolved obstruction remains the same: the actual diameter thrackle must coexist with a large exact contact-flex manifold while carrying

$$
d_H+p_D>0.6734530D-o(D)
$$

unconditionally, with substantially larger lower bounds at smaller flex density. Closing C-II now requires a geometric upper bound on this unconverted defect or a finite deformation/reinsertion argument that turns its size into a diameter contradiction.

No theorem-state file is changed.

**Disposition:** retained exact terminal correlation in the coarse pentagon-bootstrap corank cap and raised the unconditional live `d_H+p_D` floor from `0.6733591D` to `0.6734530D`. C-II remains open.
