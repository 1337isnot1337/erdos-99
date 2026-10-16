# Target C-II — disjoint force-block packing yields a growing fully loaded corridor with vanishing total KKT mass

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the no-positive-density-TB1 branch of the selected one-sided high-`t` shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** near-full-shore growing exact-force diagonal; global one-sided KKT reaction budget; exact antipodal force-pair compression; coupled host transverse-margin theorem  
**Certificate:** `research/verify_target_c_high_t_vanishing_mass_force_corridor_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The near-full-shore diagonal gives positive linear density of centers whose entire growing radius neighborhood is exact-antipodal and force-loaded at every interface. The global reaction budget has so far been used pointwise, by deleting centers with large individual switching mass. There is a stronger block consequence.

Pack many of those growing neighborhoods disjointly. Their switching sets are then disjoint interface by interface, so all packed neighborhoods together still consume at most the normalized total diameter KKT mass `1`. One packed neighborhood must therefore have total switching mass tending to zero.

This gives one consecutive growing corridor in which **every** separator carries a resolved bilateral exact positive force pair with a fixed transverse first-order slope, while the sum of the original KKT mass on **all** switching diameters in the whole corridor tends to zero. Its normalized cut-resultant path collapses to a point. After a harmless refinement of the diagonal source thresholds, even the sum of all coefficients in the compressed two-ray force certificates tends to zero.

Thus the surviving local obstruction is not supported by a hidden positive amount of KKT mass. A closing argument must use the ordered geometry or persistent diameter core, rather than an absolute force-scale floor.

---

## 1. Parent growing-force diagonal

Put

\[
c={113\over5{,}000{,}000}.
\tag{VM.1}
\]

Use the concrete diagonal from the near-full-shore growing-force theorem. For integer `n>=1`, set

\[
r_n=n,
\qquad
m_n=2n+1,
\tag{VM.2}
\]

\[
\rho_n={c\over80n(2n+1)},
\tag{VM.3}
\]

and

\[
\lambda_n
={c\over2}-{3c\over40n}.
\tag{VM.4}
\]

After choosing a sufficiently large retained source `D_n`, there is a one-sided center family `Q_n` with

\[
\boxed{
|Q_n|>(\lambda_n-o(1))D_n,
\qquad
\lambda_n\longrightarrow {c\over2}=1.13\times10^{-5}.
}
\tag{VM.5}
\]

For every `i in Q_n`, all interfaces

\[
W_i:=[i-r_n,i+r_n]
\tag{VM.6}
\]

are exact-antipodal, have one common oriented row phase, and carry an exact positive two-ray force pair

\[
G_j
=D_n(\lambda_j^-d_j^-+\lambda_j^+d_j^+),
\qquad
\lambda_j^\pm>0.
\tag{VM.7}
\]

Every selected pair has projective gap at least `rho_n`, bilateral birth, and fixed host transverse margin

\[
|d_j^\pm\cdot Jv_i|
\ge c_H-o(1),
\qquad
c_H=0.453819885927\ldots .
\tag{VM.8}
\]

Hence its elementary dipole slopes satisfy

\[
|\ell_{h_j^\pm}(s d^{(j)})|
\ge(2c_H-o(1))D_n|s|,
\tag{VM.9}
\]

with

\[
2c_H=0.907639771854\ldots .
\]

The diagonal also has

\[
r_n\to\infty,
\qquad
{r_n\over D_n}\to0,
\qquad
\rho_nD_n^{1/4}\to\infty.
\tag{VM.10}
\]

Thus every pair remains geometrically resolved well above the canonical `O(D_n^(3/4))` midpoint-error scale.

---

## 2. Residue classes pack linearly many disjoint growing neighborhoods

Partition the center indices in `Q_n` by their residue modulo

\[
m_n=2r_n+1.
\]

One residue class contains at least

\[
\boxed{
M_n\ge {|Q_n|\over m_n}
}
\tag{VM.11}
\]

centers. If two distinct centers in this class are `i<i'`, then

\[
i'-i\ge m_n=2r_n+1,
\]

so their interface windows are disjoint:

\[
[i-r_n,i+r_n]
\cap
[i'-r_n,i'+r_n]
=\varnothing.
\tag{VM.12}
\]

Since `|Q_n|=Theta(D_n)` and `r_n=o(D_n)`, (VM.11) gives

\[
\boxed{M_n\to\infty.}
\tag{VM.13}
\]

This is the key extra packing step: the near-full-shore theorem supplies not only many overlapping deep centers, but an unbounded collection of pairwise interface-disjoint fully loaded growing blocks.

---

## 3. One whole growing block has vanishing original switching KKT mass

For an interface `j`, let

\[
B_j:=\sum_{h\in X_j}\beta_h
\tag{VM.14}
\]

be the original normalized KKT mass of its switching set. On one side of the common hub the switching sets at distinct interfaces are pairwise edge-disjoint, and the C65 normalization is

\[
\sum_h\beta_h=1.
\]

Therefore, over all interfaces belonging to all `M_n` disjoint packed windows,

\[
\sum B_j\le1.
\tag{VM.15}
\]

By pigeonhole there is one packed window, call it

\[
J_n=[a_n,b_n],
\qquad
|J_n|=m_n=2r_n+1,
\tag{VM.16}
\]

such that

\[
\mathcal B_n
:=\sum_{j\in J_n}B_j
\le {1\over M_n}
\le {m_n\over |Q_n|}.
\tag{VM.17}
\]

Using (VM.5),

\[
\boxed{
\mathcal B_n
\le
{2r_n+1\over(\lambda_n-o(1))D_n}
\longrightarrow0.
}
\tag{VM.18}
\]

At leading order,

\[
\mathcal B_n
\le
\left({4\over c}+o(1)\right){r_n\over D_n},
\tag{VM.19}
\]

where

\[
\boxed{
{4\over c}={20{,}000{,}000\over113}
=176991.150442\ldots .
}
\tag{VM.20}
\]

Equation (VM.18) is stronger than a pointwise `B_j=o(1)` statement. It says that the **entire growing corridor**, despite being force-loaded at every interface, uses asymptotically zero total original diameter KKT mass on all of its switching sets.

---

## 4. The normalized reaction path collapses through the whole corridor

The exact strip reaction satisfies

\[
G_j
=D_n\sum_{h\in X_j}\beta_hd_h,
\qquad |d_h|=1,
\]

so

\[
|G_j|\le D_nB_j.
\tag{VM.21}
\]

Summing over `J_n` gives

\[
\boxed{
{1\over D_n}
\sum_{j\in J_n}|G_j|
\le\mathcal B_n
\longrightarrow0.
}
\tag{VM.22}
\]

All rows in `J_n` have one exact oriented phase. Write the cut resultants as

\[
F_j=A_jv_n,
\]

with the `A_j` strictly monotone. Since

\[
G_j=F_j-F_{j+1},
\]

we obtain

\[
\boxed{
{1\over D_n}
\operatorname{diam}
\{F_{a_n},F_{a_n+1},\ldots,F_{b_n+1}\}
\le\mathcal B_n
\longrightarrow0.
}
\tag{VM.23}
\]

Thus a growing sequence of distinct exact cut resultants is squeezed into a normalized interval of vanishing diameter, even though every step remains nonzero and every separator carries a bilateral exact force pair with the fixed geometric slope (VM.9).

There is also a useful average absolute bound. From (VM.17),

\[
{1\over m_n}
\sum_{j\in J_n}|G_j|
\le {D_n\over |Q_n|}
\le {1\over\lambda_n-o(1)}.
\tag{VM.24}
\]

Hence the mean absolute reaction scale in the selected growing corridor stays bounded, asymptotically by

\[
\boxed{
{2\over c}={10{,}000{,}000\over113}
=88495.575221\ldots .
}
\tag{VM.25}
\]

This is an absolute, not merely normalized, average bound.

---

## 5. The compressed two-ray coefficient mass may also be made to vanish

At every interface the exact two-ray formula and pair-gap lower bound give

\[
\lambda_j^-+\lambda_j^+
\le {2|G_j|\over D_n\sin\rho_n}
\le {2B_j\over\sin\rho_n}.
\tag{VM.26}
\]

Therefore

\[
\sum_{j\in J_n}(\lambda_j^-+\lambda_j^+)
\le {2\mathcal B_n\over\sin\rho_n}
\le
{2m_n\over |Q_n|\sin\rho_n}.
\tag{VM.27}
\]

For each fixed `n`, the parent theorem holds beyond a finite source threshold, while `m_n`, `lambda_n`, and `rho_n` are fixed. In the diagonal construction we are free to enlarge `D_n` further. Add the requirement

\[
{2m_n\over(\lambda_n-o(1))D_n\sin\rho_n}< {1\over n}.
\tag{VM.28}
\]

This does not change any earlier conclusion. Along that refined diagonal,

\[
\boxed{
\sum_{j\in J_n}(\lambda_j^-+\lambda_j^+)
\longrightarrow0.
}
\tag{VM.29}
\]

In particular every compressed coefficient tends to zero uniformly on the selected growing corridor.

This is not a new global KKT stress: the `lambda_j^\pm` are the exact local two-ray compression coefficients. The point is that both the original switching KKT mass and the compressed local force-certificate mass can vanish collectively, while the force-pair geometry remains uniformly transverse and centrally resolved.

---

## 6. A growing consecutive subcorridor can have an arbitrarily slow absolute reaction ceiling

The total-mass estimate also improves the fully loaded corridor pointwise after a second elementary extraction.

Let `K_n` be any sequence with

\[
K_n\to\infty,
\qquad
K_n=o(m_n).
\tag{VM.30}
\]

Call `j in J_n` bad if

\[
B_j>{K_n\over D_n}.
\tag{VM.31}
\]

If there are `q_n` bad interfaces, then (VM.17) gives

\[
q_n{K_n\over D_n}
<\mathcal B_n
\le {m_n\over |Q_n|},
\]

hence

\[
q_n
< {m_n\over(\lambda_n-o(1))K_n}.
\tag{VM.32}
\]

The good interfaces form at most `q_n+1` consecutive runs. Therefore one good run has length at least

\[
{m_n-q_n\over q_n+1}
\ge(\lambda_n-o(1))K_n.
\tag{VM.33}
\]

Here the last inequality is asymptotic, using `K_n->infinity` and `K_n=o(m_n)`.

Consequently there is a consecutive subcorridor of length tending to infinity on which **every** interface satisfies

\[
\boxed{
B_j\le {K_n\over D_n},
\qquad
0<|G_j|\le K_n.
}
\tag{VM.34}
\]

All exact-force, bilateral, transverse-margin, central-diamond, and exact-phase conclusions are inherited on this subcorridor.

For example, taking

\[
K_n=\sqrt{m_n}
\]

gives a consecutive force-loaded run of length

\[
>(c/2-o(1))\sqrt{m_n}
\]

on which every absolute strip reaction is at most `sqrt(m_n)` and every original switching mass is at most `sqrt(m_n)/D_n`.

More generally the reaction ceiling may be chosen to diverge arbitrarily slowly, at the price of a correspondingly slowly growing guaranteed consecutive run.

---

## 7. Frontier effect

On the no-positive-density-TB1 branch, the high-`t` survivor now contains a consecutive growing exact-force corridor with the simultaneous package

```text
2r_n+1 -> infinity exact-antipodal interfaces;
every interface carries a bilateral exact positive diameter-force pair;
pair gap rho_n -> 0 but rho_n D_n^(1/4) -> infinity;
every selected force ray has transverse component >=0.453819...-o(1);
every elementary dipole slope has magnitude >=(0.907639...-o(1))D_n;
total ORIGINAL switching KKT mass across the whole corridor -> 0;
sum |G_j|/D_n -> 0;
normalized cut-resultant diameter -> 0;
a refined diagonal has total compressed two-ray coefficient mass -> 0.
```

So an absolute KKT-force floor cannot close this branch. Even a growing corridor force-loaded at every separator can be supported by asymptotically zero total switching multiplier mass.

The remaining obstruction is sharper: explain why one exact-phase ordered strip stack with a nearly constant normalized cut resultant cannot carry a geometrically resolved, uniformly transverse central diameter dipole at every separator, despite the total local KKT mass tending to zero. Any closure must use the persistent diameter core, endpoint/thrackle order, the common train geometry, or a genuinely nonlocal argument. The already-closed exact laminar multishear family cannot supply a local escape.

**Disposition:** packed the near-full-shore growing exact-force neighborhoods disjointly and used the global one-sided KKT budget to force one fully loaded growing corridor with vanishing total original switching mass, vanishing normalized reaction variation, and, after refining the diagonal, vanishing total compressed two-ray force mass. C-II and Level I remain open.
