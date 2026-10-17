> Generated reading edition · [exact source](../../research/target_c_high_t_linear_strong_tb1_density_t18687_2026-09-17.md) · source SHA-256 `78f84f0460d04be188249677aab0b48ded8bd1fb12972b4744feda43d707957c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6806b753fc9a1a6890906acca30d1e4600f8b88c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_linear_strong_tb1_density_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "63b019273dbfd406c8585a95289ceef4afbe26b581d19bee2bb7a1584071210d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a linear high-`t` shore has either exact-antipodal reactions or uniformly interior one-bar blockers

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; corrected antipodal split  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** corrected linear obstruction fork; shrinking common row-phase window; one-bar tangent dual-cone characterization; exact-antipodal second-order blocker theorem; canonical C67/DB.3 separation of distinct actual diameter directions  
**Certificate:** `research/verify_target_c_high_t_linear_strong_tb1_density_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The corrected linear-shore theorem gives

$$
|E_D|+|U_D|>c_0D-o(D),
\qquad
c_0:=0.00000565={113\over20{,}000{,}000},
\tag{SB.1}
$$

where `E_D` consists of exact-antipodal good interfaces and `U_D` consists of non-antipodal interfaces possessing a one-bar tangent certificate. The non-antipodal genuine two-bar remainder is already `o(D)`.

The one-bar branch can be sharpened further. All rectangle boundary rays project to one shrinking row-phase window, while distinct actual diameter directions have inverse-`D` separation. Therefore only a fixed small fraction of the chosen TB1 bars can lie near that common boundary phase. The rest lie a fixed absolute angle inside both rays of their local dual cone and block every local opening tangent direction with an order-`D` positive first derivative.

Combining this with the exact-antipodal set gives the unconditional quantitative fork

$$
\boxed{
|E_D|+|S_D|>0.00000494375D-o(D),
}
\tag{SB.2}

where `S_D` is a family of strong non-antipodal TB1 interfaces. In particular at least one of the two mechanisms occurs with density greater than

\[
\boxed{0.000002471875D-o(D).}
\tag{SB.3}

---

## 1. Starting fork and distinct chosen TB1 bars

For every `i in U_D`, choose one TB1 switching diameter bar `h_i`. Its orientation-independent inward vector `n_i` satisfies

\[
|n_i|=D,
\qquad
n_i\in\operatorname{cone}\{a_i,b_i\},
\tag{SB.4}
$$

where `a_i,b_i` are the rooted unit boundary-contact vectors of the strip and, because this is the non-antipodal branch,

$$
\theta_i:=\angle(a_i,b_i)\in(0,\pi).
\tag{SB.5}
$$

All selected interfaces lie on one side of the common diameter-routing hub. The one-sided switching theorem therefore makes their switching supports disjoint, so

$$
\boxed{h_i\ne h_j\qquad(i\ne j).}
\tag{SB.6}
$$

The rectangle rows lie in one shrinking projective phase window. Thus there is a projective direction `phi_D` and

$$
\omega_D=o(1)
\tag{SB.7}
$$

such that

$$
d_{\mathbb{RP}^1}([a_i],\phi_D)\le\omega_D,
\qquad
d_{\mathbb{RP}^1}([b_i],\phi_D)\le\omega_D
\tag{SB.8}
$$

for every selected interface.

---

## 2. A fixed boundary neighborhood has subcritical capacity

Put

$$
\boxed{
\gamma:={c_0\over32}
={113\over640{,}000{,}000}
=1.765625\times10^{-7}.}
\tag{SB.9}
$$

Call the chosen TB1 bar `h_i` **boundary-near** when

$$
d_{\mathbb{RP}^1}([n_i],\phi_D)<2\gamma.
\tag{SB.10}
$$

Canonical C67/DB.3 says distinct actual diameter edges have distinct projective directions separated by

$$
\delta_D=2\arcsin{1\over2D}\ge {1\over D}.
\tag{SB.11}
$$

The projective ball in (SB.10) is an arc of length `4 gamma`. Hence, using (SB.6), the number `R_D` of boundary-near chosen TB1 bars is at most

$$
R_D\le1+{4\gamma\over\delta_D}
\le1+4\gamma D.
\tag{SB.12}
$$

Since

$$
4\gamma={c_0\over8}
={113\over160{,}000{,}000}
=0.00000070625,
\tag{SB.13}
$$

we obtain

$$
\boxed{
R_D\le {c_0\over8}D+1.}
\tag{SB.14}
$$

Let

$$
S_D:=U_D\setminus\{\text{boundary-near chosen TB1 interfaces}\}.
\tag{SB.15}
$$

Then

$$
|S_D|\ge |U_D|-{c_0\over8}D-O(1).
\tag{SB.16}
$$

---

## 3. Strong TB1 bars are uniformly inside both dual-cone rays

Because `omega_D=o(1)`, for all sufficiently large sources

$$
\omega_D<\gamma.
\tag{SB.17}
$$

Take `i in S_D`. By definition

$$
d_{\mathbb{RP}^1}([n_i],\phi_D)\ge2\gamma.
$$

Together with (SB.8) and the reverse triangle inequality on the projective circle,

$$
\boxed{
d_{\mathbb{RP}^1}([n_i],[a_i])\ge\gamma,
\qquad
d_{\mathbb{RP}^1}([n_i],[b_i])\ge\gamma.}
\tag{SB.18}
$$

Now use the actual TB1 orientation. Rotate coordinates so

$$
a_i=(1,0),
\qquad
b_i=(\cos\theta_i,\sin\theta_i),
\qquad0<\theta_i<\pi.
$$

Since `n_i` belongs to the positive cone generated by `a_i,b_i`, write its unit direction at angle

$$
t_i\in[0,\theta_i].
$$

The projective lower bounds (SB.18) imply the ordinary interior margins

$$
\boxed{
\gamma\le t_i\le\theta_i-\gamma.}
\tag{SB.19}
$$

Thus every member of `S_D` is separated from both local dual-cone rays by one fixed absolute angle independent of `D`.

---

## 4. Uniform first-order blocking margin

The unit tangent directions opening both boundary contact families form

$$
\Omega_i
=\{w\in S^1:a_i\cdot w\ge0,\ b_i\cdot w\ge0\}.
$$

In the coordinates above their angles satisfy

$$
s\in[\theta_i-\pi/2,\ \pi/2].
\tag{SB.20}
$$

For `t_i` in (SB.19) and every `s` in (SB.20),

$$
|t_i-s|\le{\pi\over2}-\gamma.
\tag{SB.21}
$$

Therefore

$$
{n_i\over D}\cdot w
=\cos(t_i-s)
\ge\sin\gamma.
$$

Equivalently

$$
\boxed{
 n_i\cdot w\ge D\sin\gamma
\quad\text{for every unit }w\in\Omega_i,
\qquad i\in S_D.}
\tag{SB.22}
$$

So a strong TB1 bar is not a barely tangent blocker. It has a uniform order-`D` positive first derivative against the entire local opening cone.

---

## 5. Unconditional exact-antipodal / strong-TB1 density fork

The corrected parent theorem gives

$$
|E_D|+|U_D|>c_0D-o(D).
\tag{SB.23}
$$

Subtract the boundary-near capacity (SB.14):

$$
\begin{aligned}
|E_D|+|S_D|
&\ge |E_D|+|U_D|-{c_0\over8}D-O(1)\\
&>{7c_0\over8}D-o(D).
\end{aligned}
$$

Since

$$
{7c_0\over8}
={791\over160{,}000{,}000}
=0.00000494375,
$$

we have

$$
\boxed{
|E_D|+|S_D|>0.00000494375D-o(D).}
\tag{SB.24}
$$

Consequently

$$
\boxed{
\max\{|E_D|,|S_D|\}
> {7c_0\over16}D-o(D)
=0.000002471875D-o(D).}
\tag{SB.25}
$$

This is an unconditional two-mechanism fork.

### EA mechanism

Every `i in E_D` has

$$
b_i=-a_i,
\qquad
G_i=(A_i-B_i^{ct})a_i\ne0,
\qquad
|G_i|<4{,}436{,}000,
\tag{SB.26}
$$

and the exact-antipodal second-order blocker theorem supplies two switching diameter edges with opposite transverse signs. All switching is one-sided toward the same global hub and supports are disjoint across interfaces.

### Strong-TB1 mechanism

Every `i in S_D` has one distinct switching actual diameter bar whose inward direction is at least `gamma` from both local dual-cone rays and satisfies the robust inequality (SB.22). These interfaces also occur at distinct ordered positions on the same hub side.

Thus the high-`t` survivor contains a linear-density family of either exact axial strip reactions or robust single-bar tangent blockers; arbitrary near-degenerate local obstructions no longer suffice.

---

## 6. What remains

The two remaining closure routes are now concrete.

1. **Exact-antipodal route:** show that a linear ordered family of one-sided exact-antipodal interfaces with nonzero bounded axial reactions and opposite-transverse switching pairs is incompatible with the diameter-thrackle endpoint order, cut-resultant variation, or the common transverse ladder.
2. **Strong-TB1 route:** combine the fixed interior angle `gamma`, distinct ordered switch positions, convex diameter-thrackle order, and the linear near-triangular transverse scaffold to force a forbidden endpoint order, an exact unit triangle, or a finite strict-diameter descent.

No individual KKT multiplier floor is available in either route; the next step must use geometry/order or a global weighted identity.

---

## 7. Scope audit

- This note no longer assumes that all linear-good interfaces are non-antipodal. Exact antipodality is one side of the final fork.
- `S_D` uses one chosen TB1 bar per non-antipodal TB1 interface. It does not claim every TB1 bar at that interface is strong.
- The boundary-near capacity estimate uses only chosen-bar distinctness and canonical C67 direction separation.
- The projective-to-oriented step uses the positive-cone characterization of a non-antipodal TB1 inward vector.
- The robust estimate (SB.22) is local to each strip's opening cone. It does not provide one common translation direction for all interfaces.
- No individual KKT multiplier lower bound is inferred from strong geometric transversality.
- No C-II or Level-I closure is claimed.

**Disposition:** sharpened the corrected linear obstruction fork to an unconditional positive-density alternative between exact-antipodal strip reactions and uniformly interior one-bar tangent blockers. C-II and Level I remain open.
