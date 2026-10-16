# Target C-II — fixed accuracy can be traded for a genuinely linear tagged common ladder

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** corrected one-sided high-`t` obstruction shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** repaired rail-partition dense-ladder theorem; interval-reaction normal form  
**Certificate:** `research/verify_target_c_high_t_linear_accuracy_tradeoff_tagged_ladder_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The rail-partition argument has a second useful regime besides `k_D=D/log D`. If one permits a prescribed fixed angular error `epsilon>0`, then the rail group itself may have **linear** size in `D` while the whole interval still shares a positive-density transverse train family.

Let

\[
M:=9{,}000{,}000,
\qquad
r_0:=0.6536,
\qquad
q_0:=r_0-{1.02\over\sqrt3}
=0.0647027254265\ldots .
\tag{LA.1}

Fix

\[
0<\varepsilon<0.06
\tag{LA.2}
\]

and set

\[
\boxed{
\alpha_\varepsilon:={\varepsilon^2\over M}.
}
\tag{LA.3}

Then, for all sufficiently large `D`, there is one contiguous hub-free path interval containing at least

\[
\boxed{
(\alpha_\varepsilon-o(1))D
}
\tag{LA.4}

positions of the same fixed-host exact-normal tagged nested rail, with total full local cost

\[
\boxed{
\sum_i(N_i+L_i+DB_i+F_i+F_{i+1})
<(\varepsilon^2+o(1))D.
}
\tag{LA.5}

After deleting at most `epsilon D` common transverse columns, the **entire interval** has one common column family of density

\[
\boxed{
(r_0-\varepsilon-\varepsilon^2-o(1))D
}
\tag{LA.6}

and every retained crossing has angular defect at most

\[
\boxed{\varepsilon+o(1).}
\tag{LA.7}

At metric margin `mu=.01`, the same ordered family has two common circumcenter flanks, simultaneous on every row, each of density

\[
\boxed{
(q_0-\varepsilon-\varepsilon^2-o(1))D.
}
\tag{LA.8}

The whole interval also has total switching KKT mass at most

\[
\boxed{\varepsilon^2+o(1),}
\tag{LA.9}

and every pair of row phases differs by at most

\[
\boxed{
{\varepsilon^2\over r_0-\varepsilon^2}+o(1).
}
\tag{LA.10}

Thus every contiguous slab inside the interval has aggregate opening width `O(epsilon^2)`, even though the individual retained rhombi are only required to have defect `O(epsilon)`.

For the concrete choice `epsilon=.01`:

\[
\boxed{\alpha_{.01}=1.1111111\times10^{-11},}
\tag{LA.11}

\[
\boxed{|P|>(0.6435-o(1))D,}
\tag{LA.12}

\[
\boxed{|P^-|,|P^+|>(0.0546027254-o(1))D,}
\tag{LA.13}

and the all-row phase spread is below

\[
\boxed{1.53023\times10^{-4}+o(1)\text{ radians}.}
\tag{LA.14}

After fixing one mechanism tag and one physical destination, at least

\[
\boxed{
\left({\alpha_\varepsilon\over4}-o(1)\right)D
}
\tag{LA.15}

rail positions remain inside the same linear common ladder.

---

## 1. Use a linear-size rail group

The fixed-host tagged rail has more than

\[
\gamma D-o(D),
\qquad
\gamma=2.825\times10^{-6},
\]

positions on one hub side. The repaired partition theorem proves that a consecutive group of `k` rail positions has some enclosing path interval with cost

\[
<(M+o(1))k
\tag{LA.16}

provided `k` is below the total rail population.

Take

\[
k=\lfloor\alpha_\varepsilon D\rfloor.
\]

For `epsilon<0.06`, `alpha_epsilon<4e-10`, far below `gamma`, so many such rail groups exist. Equation (LA.16) gives

\[
(M+o(1))k
=(\varepsilon^2+o(1))D,
\]

which is (LA.5).

The selected interval contains the full group, proving (LA.4).

---

## 2. A positive-density common column family survives

Every row has more than `r_0D-o(D)` complete crossing trains. The terminal-topology part of (LA.5) gives

\[
\sum_iL_i<(\varepsilon^2+o(1))D.
\]

Therefore the trains common to every row of the interval have size

\[
>(r_0-\varepsilon^2-o(1))D.
\tag{LA.17}

The row-defect part gives

\[
\sum_jF_j<(\varepsilon^2+o(1))D.
\tag{LA.18}

For each common column `b`, let `Delta_b` be its total defect through the interval. Delete columns with

\[
\Delta_b>\varepsilon.
\]

By (LA.18), fewer than `(epsilon+o(1))D` columns are deleted. Thus the retained common family has size (LA.6), and every crossing defect is bounded by its column total, proving (LA.7).

Since `epsilon<0.06`,

\[
q_0-\varepsilon-\varepsilon^2>0,
\]

so the exact train-step/circumdisk argument yields the two common flank blocks (LA.8).

---

## 3. The full interval has small KKT mass and much smaller row-phase spread

The `DB_i` part of (LA.5) immediately gives

\[
\sum_iB_i<\varepsilon^2+o(1),
\]

which is (LA.9).

Before the final `epsilon D` column deletion, let `C` be the common family from (LA.17). For any two rows `tau_a,tau_b`, common orientation gives

\[
|\alpha_a-\alpha_b|
=|\delta_{ac}-\delta_{bc}|
\le\delta_{ac}+\delta_{bc}
\]

for every `c in C`. Sum over `C` and use (LA.18):

\[
|C|\,|\alpha_a-\alpha_b|
\le F_a+F_b
\le\sum_jF_j
<(\varepsilon^2+o(1))D.
\]

Together with (LA.17),

\[
|\alpha_a-\alpha_b|
\le{\varepsilon^2\over r_0-\varepsilon^2}+o(1),
\]

proving (LA.10).

The rooted-shore sign theorem identifies this with the opening-width bound for every slab between two rows of the interval.

---

## 4. The entire global rail normal form survives

The `alpha_epsilon D` selected rail positions are consecutive positions in the global fixed-host tagged rail. They retain:

- strict selected-cut support nesting;
- strict exact diameter-normal order;
- exact antipodal normal transport to their partners;
- partner destination on opposite host or `T_m`;
- one `EA` or `TB1` mechanism tag per position.

Pigeonholing the two tags and two destinations leaves at least one quarter of the group, proving (LA.15).

The interval-reaction theorem applies simultaneously: every contiguous slab has an exact nonzero reaction generated by at most two actual switching diameter bars, and the full switching stress available to the entire interval is only `epsilon^2+o(1)`.

---

## 5. Frontier effect

There are now two complementary scales available from the same rail-partition mechanism.

- Letting `epsilon=epsilon_D->0` gives almost-linear tagged groups such as `D/log D` with phase error tending to zero.
- Fixing any sufficiently small `epsilon>0` gives a **genuinely linear** tagged group and a linear-by-linear common train ladder with prescribed uniform angular accuracy.

For example, `epsilon=.01` gives a common grid with at least `0.6435D` columns and at least `1.11e-11D` tagged rail positions, while every retained rhombus has angular defect at most `.01+o(1)` and every row phase lies in a window of width only `1.54e-4+o(1)`.

C-II remains open. The remaining obstruction is not scarcity: even at any fixed requested small accuracy one can force a positive linear number of exact-normal tagged diameter bars into one common positive-density train ladder with small total switching stress.

**Disposition:** converted the rail-partition estimate into a fixed-accuracy/positive-density tradeoff, giving genuinely linear tagged common ladders at arbitrarily small prescribed angular error.