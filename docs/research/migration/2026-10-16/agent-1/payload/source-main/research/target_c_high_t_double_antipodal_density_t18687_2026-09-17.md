# Target C-II — retuned high-`t` density forces strong one-bar blockers or consecutive exact-antipodal double cells

**Date:** 2026-09-17
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed
**Scope:** the consecutive one-sided row shore of the high-`t` rectangle, through `t=(q-k)/D<=1.8687`
**Dependencies:** linear one-bar/exact-antipodal obstruction proof; non-antipodal TB2 direction packing; common one-sided switch half-plane; exact force-carrying antipodal pairs; robust narrow-pair capacity; wide-dipole central-diamond theorem
**Certificate:** `research/verify_target_c_high_t_double_antipodal_density_t18687.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous density fork used the convenient local threshold `J_i<4C`.  That threshold leaves enough globally bad interfaces to separate every exact-antipodal good interface from the next one.  Re-running the same budget with the still-fixed threshold `16C` reduces the bad-interface density enough to force a stronger ordered alternative.

Put

\[
c={113\over5{,}000{,}000}=0.0000226,
\qquad
C=1{,}109{,}000.
\tag{DA.1}
\]

There is a consecutive one-sided interface shore `I_D` with

\[
|I_D|>{c\over2}D-o(D).
\tag{DA.2}
\]

Call `i in I_D` **16-good** when

\[
J_i<16C=17{,}744{,}000.
\tag{DA.3}
\]

Let:

- `E_D` be the 16-good exact-antipodal interfaces;
- `S_D` be the 16-good non-antipodal TB1 interfaces whose chosen blocker is at least
  \[
  \gamma={c\over512}={113\over2{,}560{,}000{,}000}
  \tag{DA.4}
  \]
  from both local dual-cone rays;
- `P_D` be the set of positions `i` for which **both** `i` and `i+1` belong to `E_D`.

Then

\[
\boxed{
|P_D|+2|S_D|
>{23c\over64}D-o(D)
={2599\over320{,}000{,}000}D-o(D).
}
\tag{DA.5}

Consequently

\[
\boxed{
\max\{|P_D|,|S_D|\}
>{23c\over192}D-o(D)
={2599\over960{,}000{,}000}D-o(D).
}
\tag{DA.6}

Numerically, the guaranteed density in (DA.6) is

\[
2.707291666\times10^{-6}D-o(D).
\tag{DA.7}

This replaces the old final alternative “strong TB1 or isolated exact-antipodal interface” by

```text
linear strong-TB1 population
OR
linear population of two consecutive exact-antipodal interfaces.
```

Every `i in P_D` gives three consecutive rows with one exact real direction

\[
u_i=u_{i+1}=u_{i+2}=:v_i.
\tag{DA.8}
\]

The two exact reactions are nonzero, point in the **same ordinary direction**, and have bounded magnitude:

\[
\boxed{
G_i=\rho_i e_i,
\qquad
G_{i+1}=\rho_{i+1}e_i,
\qquad
0<\rho_i,\rho_{i+1}<16C,
}
\tag{DA.9}
\]

for one unit vector `e_i=+/-v_i`.  Each reaction has an exact positive two-bar force compression by opposite-transverse switching diameters.

The double-antipodal alternative can be made robust as well.  Define

\[
p_0:={2599\over960{,}000{,}000},
\qquad
\rho_*:={p_0\over8}
={2599\over7{,}680{,}000{,}000}
\approx3.384114583\times10^{-7}.
\tag{DA.10}
\]

If the `P_D` side of (DA.6) occurs, then after discarding only a linear minority there remain more than

\[
\boxed{
{p_0\over2}D-o(D)
={2599\over1{,}920{,}000{,}000}D-o(D)
}
\tag{DA.11}

consecutive double-antipodal cells in which **both** exact force pairs have projective angle at least `rho_*`.  Thus each of the two consecutive interfaces carries a force-generating central macroscopic diameter diamond, and both exact reactions point along the same ordinary axis.

This is a new finite local object at positive linear density: a three-row exact phase plateau with two ordered, force-carrying, fixed-angle antipodal dipoles.

---

## 1. Retune the good-interface threshold

The linear-shore proof uses the nonnegative joint cost

\[
J_i=N_i+L_i+DB_i+S_i+S_{i+1}.
\tag{DA.12}
\]

Its audited global budget is

\[
\sum_iJ_i<KD+o(D),
\qquad
K<Cc.
\tag{DA.13}
\]

If `B_D` is the set of interfaces in `I_D` failing (DA.3), then

\[
16C|B_D|
\le\sum_iJ_i
<CcD+o(D),
\]

so

\[
\boxed{
|B_D|<{c\over16}D+o(D).
}
\tag{DA.14}
\]

Therefore the 16-good set `Q_D=I_D\setminus B_D` satisfies

\[
\boxed{
|Q_D|>{7c\over16}D-o(D)
={791\over80{,}000{,}000}D-o(D).
}
\tag{DA.15}

Every 16-good interface has

\[
N_i,L_i<16C,
\qquad
B_i<{16C\over D},
\qquad
S_i+S_{i+1}<16C.
\tag{DA.16}

The only cost is a larger but still absolute local-complexity constant.

---

## 2. Non-antipodal genuine TB2 interfaces remain sublinear

The common oriented column family still has

\[
|B_+|>0.1567D-o(D).
\tag{DA.17}
\]

For a 16-good non-antipodal interface, the same row-phase estimate gives opening width

\[
\varepsilon_i
\le {16C\over0.1567D-o(D)}
<{1.133\times10^8\over D}+o(D^{-1}).
\tag{DA.18}
\]

A genuine minimal TB2 certificate therefore has both actual diameter directions within `epsilon_i` of the projective normal to the row direction.  All row directions lie in one shrinking projective phase window `omega_D=o(1)`.  Consequently every diameter direction chosen from a 16-good TB2 certificate lies in one projective interval of width

\[
o(1)+O(D^{-1})=o(1).
\tag{DA.19}
\]

Different interfaces have disjoint switching supports, so all chosen certificate edges are distinct.  Canonical C67 separates distinct actual diameter directions by at least `1/D`.  Hence the total number of chosen directions in (DA.19) is `o(D)`, and therefore

\[
\boxed{|T_D|=o(D)}
\tag{DA.20}
\]

for the 16-good genuine TB2 class.

Thus, up to `o(D)`, every 16-good interface is exact-antipodal or TB1.

---

## 3. Only `cD/128+O(1)` chosen TB1 bars are boundary-near

For each 16-good TB1 interface choose one TB1 switching diameter bar.  All row boundary rays lie in the shrinking projective window around `phi_D`.

Use the fixed margin (DA.4).  Call a chosen TB1 direction boundary-near when its projective distance from `phi_D` is less than `2gamma`.  That projective ball has length `4gamma`, and C67 gives

\[
\#\{\text{boundary-near chosen TB1 bars}\}
\le1+4\gamma D.
\tag{DA.21}
\]

Since

\[
4\gamma={c\over128},
\]

write this boundary-near class as `R_D`; then

\[
\boxed{
|R_D|\le {c\over128}D+O(1).
}
\tag{DA.22}

For sufficiently large `D`, `omega_D<gamma`.  Every chosen TB1 bar outside `R_D` is therefore at least `gamma` from each local dual-cone ray.  These are the strong interfaces `S_D`, and every unit local opening direction `w` satisfies

\[
\boxed{
n_i\cdot w\ge D\sin\gamma.}
\tag{DA.23}
\]

Partitioning the 16-good set as

\[
Q_D=E_D\sqcup R_D\sqcup S_D\sqcup T_D
\tag{DA.24}
\]

and using (DA.15), (DA.20), and (DA.22) gives

\[
\boxed{
|E_D|+|S_D|
>{55c\over128}D-o(D)
={1243\over128{,}000{,}000}D-o(D).
}
\tag{DA.25}

---

## 4. A path-counting identity forces adjacent exact-antipodal pairs

The interfaces of `I_D` occur consecutively along one side of the row chain.  Mark the positions belonging to `E_D`.  Let `r_D` be the number of maximal `E_D` runs.  Every two distinct `E_D` runs require at least one non-`E_D` separator, so

\[
r_D\le |I_D\setminus E_D|+1.
\tag{DA.26}
\]

Inside a run of `ell` marked interfaces there are exactly `ell-1` adjacent marked pairs.  Therefore

\[
|P_D|=|E_D|-r_D
\ge |E_D|-|I_D\setminus E_D|-1.
\tag{DA.27}
\]

By (DA.24),

\[
I_D\setminus E_D
=B_D\sqcup R_D\sqcup S_D\sqcup T_D.
\tag{DA.28}
\]

Use (DA.14), (DA.20), (DA.22), and

\[
|E_D|>{55c\over128}D-|S_D|-o(D)
\tag{DA.29}
\]

from (DA.25).  Then

\[
\begin{aligned}
|P_D|
&>{55c\over128}D-|S_D|
-{c\over16}D-{c\over128}D-|S_D|-o(D)\\
&={23c\over64}D-2|S_D|-o(D).
\end{aligned}
\tag{DA.30}
\]

This is exactly (DA.5).

Since

\[
|P_D|+2|S_D|
\le3\max\{|P_D|,|S_D|\},
\]

(DA.6) follows.

This step uses only the actual linear order of the row interfaces.  It makes no Euler-trail inference about the diameter graph.

---

## 5. A double-antipodal position is an exact three-row force cell

Take `i in P_D`.  Exact antipodality at interfaces `i` and `i+1` means

\[
u_i=u_{i+1}=u_{i+2}=v_i.
\tag{DA.31}
\]

Write the cut resultants

\[
F_j=A_jv_i
\qquad(j=i,i+1,i+2).
\tag{DA.32}
\]

The global one-sided separation functional gives

\[
\phi(F_i-F_{i+1})>0,
\qquad
\phi(F_{i+1}-F_{i+2})>0.
\tag{DA.33}
\]

Therefore

\[
(A_i-A_{i+1})\phi(v_i)>0,
\qquad
(A_{i+1}-A_{i+2})\phi(v_i)>0.
\tag{DA.34}
\]

The two scalar differences have the same strict sign.  Hence the three force magnitudes are strictly monotone and the two exact reactions point in one common ordinary direction

\[
e_i=\operatorname{sgn}(\phi(v_i))v_i.
\tag{DA.35}
\]

Each interface is 16-good, so

\[
|G_i|,|G_{i+1}|<DB_i,DB_{i+1}<16C.
\tag{DA.36}
\]

The exact-force-pair theorem supplies two distinct switching diameter bars at each interface with positive coefficients:

\[
G_i=D(\lambda_i^-d_i^-+\lambda_i^+d_i^+),
\]

\[
G_{i+1}=D(\lambda_{i+1}^-d_{i+1}^-+\lambda_{i+1}^+d_{i+1}^+),
\tag{DA.37}
\]

where every `lambda` is positive and each pair strictly brackets the same axis `e_i`.  The two switching supports are edge-disjoint by one-sided interval support.

Thus a double-antipodal position is a two-step exact KKT force cell, not merely three parallel rows.

---

## 6. In the double-antipodal branch, linearly many cells have two wide force pairs

Let

\[
p_0={23c\over192}
={2599\over960{,}000{,}000}
\tag{DA.38}
\]

be the common density in (DA.6), and fix

\[
\rho_*={p_0\over8}.
\tag{DA.39}
\]

The exact-force robust packing theorem gives, for any fixed `rho`,

\[
\#\{\text{exact-antipodal force pairs of gap}<\rho\}
\le2\rho D+o(D).
\tag{DA.40}
\]

At `rho=rho_*`, at most

\[
{p_0\over4}D+o(D)
\tag{DA.41}
\]

exact-antipodal interfaces have a narrow exact force pair.

One narrow interface can spoil at most two adjacent positions in `P_D`, once as the left interface and once as the right interface.  Therefore at most

\[
{p_0\over2}D+o(D)
\tag{DA.42}

double-antipodal cells contain a narrow constituent pair.

If the `P_D` side of (DA.6) occurs, then

\[
|P_D|>p_0D-o(D).
\]

Subtracting (DA.42) leaves more than

\[
{p_0\over2}D-o(D)
\]

cells in which both exact force pairs have projective gap at least `rho_*`.  This proves (DA.11).

For each of the two pairs, the wide-force central-diamond theorem now gives:

- two vertex-disjoint crossing actual diameter bars;
- exact positive generation of its tagged axial reaction;
- a four-endpoint hull containing
  \[
  B\!\left(o,{D\over2}\sin{\rho_*\over2}-L_D\right);
  \]
- a diagonal intersection within `O_{rho_*}(D^{3/4})` of the common circumcenter;
- exact area at least `(D^2/2)sin rho_*`.

Both diamonds in one cell are tagged by consecutive interfaces, and both exact reactions point along the same ordinary direction `e_i`.

If desired, greedily taking every other surviving cell leaves at least `p_0D/4-o(D)` three-row cells with disjoint **interface tags**.  This thinning is not needed for (DA.11).

---

## 7. Frontier effect

The high-`t` final fork can now be stated at a more rigid resolution:

```text
either
  > 2.707291666e-6 D strong non-antipodal TB1 interfaces,
  each with a fixed local opening margin,

or
  > 2.707291666e-6 D adjacent exact-antipodal interface pairs,
  hence linearly many exact three-row phase plateaus.

In the second case, after a fixed-angle thinning,
  > 1.353645833e-6 D cells remain
  with TWO consecutive wide exact-force antipodal diamonds,
  both reactions pointing along the same ordinary axis.
```

This removes the isolated-antipodal regression from the dense branch.  If the strong one-bar mechanism does not occur at the stated density, exact antipodality must persist across two successive interfaces at positive linear density.

The resulting double cell is compatible with the older local multishear cusp isolation, so it is not by itself a diameter descent.  The remaining useful target is geometric/order-theoretic: combine two consecutive force-carrying central diamonds with the common ordered near-triangular transverse ladder crossing the same three rows.  That is substantially more rigid than a single unweighted antipodal dipole.

No C-II or Level-I closure is claimed.

**Disposition:** retuned the global interface budget to force a positive-density alternative between strong TB1 blockers and consecutive exact-antipodal double cells; in the latter branch linearly many cells carry two consecutive fixed-angle exact-force central diamonds with a common reaction direction. C-II and Level I remain open.
