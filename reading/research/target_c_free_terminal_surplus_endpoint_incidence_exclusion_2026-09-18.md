> Generated reading edition · [exact source](../../research/target_c_free_terminal_surplus_endpoint_incidence_exclusion_2026-09-18.md) · source SHA-256 `56aaf97151c3d7babb002d261f39c9cc7a5e11737039970c9214654a267e8fe0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "16ff663cc248db7092705513ea51452714e907af", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_surplus_endpoint_incidence_exclusion_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3be8ff4464a18d0c9ca43ea1b10e74e632f0454919fcf0138b736e04f58b611b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — terminal FREE surplus endpoint is incompatible with O--O rhombus incidence

**Date:** 2026-09-18  
**Status:** proof-only endpoint exclusion; theorem-state authority unchanged  
**Scope:** terminal full-core FREE branch at the exact matched surplus endpoint  
**Depends on:** terminal FREE surplus-endpoint stability; terminal FREE transport/phase separation; audited complement O--O train length/terminal-energy tradeoff; audited complement-rhombus orbit separation  
**Certificate:** `research/verify_target_c_free_terminal_surplus_endpoint_incidence_exclusion_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current terminal FREE package has an exact scalar lower endpoint

$$
\mu_*=
\frac\pi2+\frac25\sqrt{\frac\pi{2\sqrt3}}+\frac g5,
\qquad g=0.007707.
$$

The endpoint-stability theorem had treated equality as a possible rigid survivor. The new transport theorem then showed that such a survivor would contain about `1.56D` direction-diffuse O--O trains while essentially all quadratic strict-rhombus crossing mass is carried by one bounded-to-bounded atomic orbit.

Those two conclusions are incompatible with the already audited O--O train-length theorem. At surplus equality the outer walk has vanishing normalized detour, so almost every O--O train must have midpoint-path length asymptotic to `D`. Hence the O--O population demands a positive `Theta(D^2)` supply of strict rhombi. But the transport theorem leaves only about `1.5e-5 D^2` non-dominant rhombi available to touch those trains.

The numerical gap is not close:

$$
\boxed{
\frac\pi2-g
=1.563089326794897\ldots
>
2.98197119664\times10^{-5}
=\frac{r(0)^2}{2}.
}
\tag{EX.1}
$$

Therefore no terminal full-core FREE sequence can attain the matched surplus endpoint `mu_*`.

---

## 1. Endpoint equality forces zero normalized outer detour

Assume for contradiction that a terminal full-core FREE sequence satisfies

$$
\mu_D\to\mu_*.
\tag{1.1}
$$

The surplus-endpoint stability decomposition gives

$$
\delta_D:=\frac{b-P_F}{D}\to0.
\tag{1.2}
$$

This is exactly the normalized outer-route detour `d_out/D` used by the audited complement-incidence theorem.

The same endpoint has

$$
\frac{R_4}{D^2}\to
\Delta_2:=\frac\pi{2\sqrt3},
\qquad
s_2:=\sqrt{\Delta_2}.
\tag{1.3}
$$

Put

$$
M_*:=4s_2+2g.
\tag{1.4}
$$

---

## 2. Transport separation leaves a linear O--O population

Pass to the transport subsequence and write

$$
e:=\lim\frac{E_{BO}}D.
$$

The terminal transport theorem gives

$$
0\le e\le2g
\tag{2.1}
$$

and

$$
\frac{L_O}{D}	o p(e):=\frac{\pi-e}{2}.
\tag{2.2}
$$

Consequently

$$
\boxed{
p(e)\ge p_*:=\frac\pi2-g
=1.563089326794897\ldots .}
\tag{2.3}
$$

The same theorem shows that all atomic train mass is asymptotically bounded-to-bounded. Thus the O--O direction measure is nonatomic in the atomic decomposition. After freezing small disjoint phase windows around the dominant bounded-to-bounded orbit and then shrinking those windows, only `o(D)` O--O trains are lost.

Let `C_D` be the retained O--O trains outside those dominant windows. Then

$$
\frac{|C_D|}{D}\to p(e).
\tag{2.4}
$$

---

## 3. Every retained O--O train is asymptotically long

For `tau in C_D`, let

- `r_tau` be the number of strict rhombi in its stopped-train midpoint path;
- `e_tau` be the exact sum of the directional energies of its two outer terminal occurrences.

The hostile-audited complement-incidence geometry gives the uniform train-length/terminal-energy inequality

$$
\boxed{
\frac{r_\tau}{D}
\ge
1-\delta_D-\frac{e_\tau}{2}-o(1).
}
\tag{3.1}
$$

The exact outer-route energy identity pays every terminal occurrence from the same nonnegative detour budget. Therefore

$$
\frac1D\sum_{\tau\in C_D}e_\tau
\le
\delta_D+o(1)
=o(1).
\tag{3.2}
$$

Sum (3.1) over `C_D`. Since `|C_D|=O(D)` and the geometric error is uniform,

$$
\frac1{D^2}
\sum_{\tau\in C_D}r_\tau
\ge
p(e)(1-\delta_D)
-
\frac1{2D}\sum_{\tau\in C_D}e_\tau
-o(1).
$$

Using (1.2) and (3.2),

$$
\boxed{
\liminf
\frac1{D^2}
\sum_{\tau\in C_D}r_\tau
\ge p(e)\ge p_*.
}
\tag{3.3}
$$

Thus the retained O--O trains demand at least

$$
(1.563089326794897\ldots-o(1))D^2
$$

train-rhombus incidences.

---

## 4. The dominant atomic orbit leaves essentially no rhombi for them

For the transport subsequence set

$$
B(e):=\frac{M_*-e}{2}
$$

and

$$
w(e):=
\frac{B(e)+\sqrt{8\Delta_2-B(e)^2}}2,
\qquad
r(e):=B(e)-w(e).
\tag{4.1}
$$

The sharp dominant-orbit frontier gives total non-dominant atomic train mass at most

$$
r(e)+o(1).
\tag{4.2}
$$

Moreover

$$
0\le r(e)\le r(0)
=0.007722656533397\ldots .
\tag{4.3}
$$

The audited complement-rhombus separation applies after the same frozen-window limit: every strict rhombus incident to a retained train in `C_D` lies outside the dominant/dominant orbit, apart from `o(D^2)` leakage. Non-dominant exact-orbit crossing mass is bounded by the square of its total mass, so if `R_comp` is the number of distinct strict rhombi incident to at least one train in `C_D`,

$$
\boxed{
\frac{R_{comp}}{D^2}
\le
\frac{r(e)^2}{4}+o(1)
\le
\frac{r(0)^2}{4}+o(1).
}
\tag{4.4}
$$

Every strict rhombus belongs to exactly two complete stopped trains. Hence it contributes at most two incidences to the sum in (3.3), and

$$
\frac1{D^2}\sum_{\tau\in C_D}r_\tau
\le
2\frac{R_{comp}}{D^2}
\le
\frac{r(0)^2}{2}+o(1).
\tag{4.5}
$$

Numerically,

$$
\boxed{
\frac{r(0)^2}{2}
=0.0000298197119664\ldots .}
\tag{4.6}
$$

---

## 5. Contradiction

Equations (3.3) and (4.5) require

$$
p_*\le\frac{r(0)^2}{2}.
\tag{5.1}
$$

But

$$
\frac\pi2-g
-
\frac{r(0)^2}{2}
=
1.563059507082930\ldots>0.
\tag{5.2}
$$

This contradiction proves:

$$
\boxed{
\text{No terminal full-core FREE sequence satisfies }\mu_D\to\mu_*.
}
\tag{5.3}
$$

Equivalently, the exact matched surplus endpoint is not an attainable terminal FREE asymptotic state.

This is an endpoint exclusion, not a full proof of C-II. It does not yet provide an explicit uniform numerical improvement above `mu_*`; doing so requires quantitative stability versions of the transport-phase separation estimates rather than only their equality-limit form. But any hypothetical sequence with surplus tending to `mu_*` is now ruled out.

---

## 6. What remains

The next target should quantify the exclusion. Surplus stability already gives

$$
\delta_D\le\frac52\varepsilon+o(1)
$$

under `mu_D<=mu_*+epsilon`. A quantitative version of the transport theorem controlling

1. the O--O population retained outside dominant windows, and
2. the non-dominant rhombus capacity,

as explicit functions of `epsilon` would insert directly into the same incidence inequality

$$
p(1-\delta)-\frac{e_c}{2}
\le
2\frac{R_{comp}}{D^2}.
$$

Because the equality-case gap in (5.2) is larger than `1.56`, substantial perturbation room is available. This should produce a positive explicit surplus gap without requiring a new local geometric theorem.

No theorem-state file is changed.
