# Target C-II — continuous optimization sharpens the FREE square-root fork

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; strengthens the square-root FREE face/superbraid tradeoff  
**Scope:** all-inactive non-anchored FREE reflection ancestry  
**Dependencies:** two-sided inactive gate absorption; two-sided outer-face localization; exact upper-event identity from the square-root tradeoff; sharp superdiameter-thrackle theorem; FREE superbraid forest transversal  
**Certificate:** `research/verify_target_c_tooth_reflection_optimized_sqrt_tradeoff_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing square-root theorem split the upper gates into a `3/4` thin-dominant case and a `1/4` thick-dominant case. That split throws away information twice. The exact upper-event identity already gives a quadratic backtracking term from the number of thick gates, while every thin gate contributes directly to the superdiameter braid. Keeping both counts simultaneously gives a one-variable quadratic optimization and a larger common constant.

Put

\[
h_*={\sqrt{303}\over52}=0.334747984337100\ldots
\]

and define

\[
\boxed{
 c_{\rm opt}
 :=\left(2+{h_*\over2}\right)^{-1/2}
 =0.679255355387642\ldots .
}
\tag{OS.1}

Then every all-inactive non-anchored FREE ancestry has at least one of the following outcomes.

### OPT-SQRT-FACE

One consecutive all-lower run in the original outer contact face has support span

\[
\boxed{
 \operatorname{span}_N(R)
 \ge (c_{\rm opt}-o(1))\sqrt D.
}
\tag{OS.2}

For every fixed `Lambda>1`, that run contains a vertex-disjoint matching of old fully inactive outer-face source pairs of size

\[
\boxed{
 \left({\Lambda-1\over2\Lambda}c_{\rm opt}-o(1)\right)\sqrt D
}
\tag{OS.3}

whose edges satisfy

\[
\boxed{
 1<|x-y|
 \le
 1+\left({\Lambda h_*\over c_{\rm opt}}+o(1)\right)D^{-1/2}.
}
\tag{OS.4}

In particular, with `Lambda=2`, the matching size is

\[
\boxed{
 (0.169813838846910\ldots-o(1))\sqrt D
}
\tag{OS.5}

and every retained edge has excess at most

\[
\boxed{
 (0.985632227061542\ldots+o(1))D^{-1/2}.
}
\tag{OS.6}

One may instead take any `Lambda_D -> infinity` with `Lambda_D=o(sqrt(D))`; then the matching size approaches

\[
\left({c_{\rm opt}\over2}-o(1)\right)\sqrt D
= (0.339627677693821\ldots-o(1))\sqrt D
\]

while its edge excess is still `o(1)`.

### OPT-SQRT-SUPER-BRAID

There is a vertex-disjoint matching of old fully inactive source pairs of size

\[
\boxed{
 (c_{\rm opt}-o(1))\sqrt D
}
\tag{OS.7}

such that every edge `xy` satisfies the exact sharp superdiameter inequality

\[
\boxed{
 |x-y|>\sqrt{D^2-1}.
}
\tag{OS.8}

Hence all those chords cross properly pairwise and every endpoint is a vertex of the full source hull. The existing superbraid forest-transversal theorem then applies without any change: every braid chord is external to the force hull, every braid chord crosses every actual diameter edge, the actual diameter graph is a caterpillar forest, and every diameter-tree bipartition is trapped in one complementary pair of braid boundary cells.

The previous common lower constant was `0.604935...`; the previous braid constant was `0.612372...`. The same ancestry now yields one of two square-root objects with the single common constant `0.679255...`.

---

## 1. Split at the exact superdiameter threshold

For an upper gate, use the notation of the square-root theorem:

- `Delta>0` is its activation-time increment;
- its original length is `D-rho`, with `0<rho<=Delta`;
- `b>0` is its support-direction backtracking.

The exact first-hit identity is

\[
2\Delta b=2D\rho-\rho^2+\Delta^2,
\]

and therefore

\[
\boxed{
 b\ge {\rho\over\Delta}\left(D-{\rho\over2}\right).
}
\tag{OS.9}

Use the exact threshold

\[
\tau_D:=D-\sqrt{D^2-1}
={1\over D+\sqrt{D^2-1}}.
\tag{OS.10}

Call an upper gate **thin** when `rho<tau_D`, and **thick** otherwise. If it is thin, then

\[
D-\rho>\sqrt{D^2-1},
\]

so the sharp superdiameter theorem applies exactly, with no `0.49/D` surrogate.

Let

\[
s:=\#\{\text{thin upper gates}\},
\qquad
m:=\#\{\text{thick upper gates}\},
\qquad
U=s+m.
\]

Same-parity ancestry edges are vertex-disjoint. Therefore the thin upper gates contain a pairwise-properly-crossing matching of size at least

\[
{s\over2}-O(1).
\tag{OS.11}

---

## 2. Thick gates give a quadratic backtracking term with the sharp coefficient

The clearing-time budget satisfies

\[
\sum_j\Delta_j\le t_D,
\qquad
t_D<h_*+D^{-1/3}.
\]

For a thick upper gate, `rho>=tau_D` and `rho<=Delta<=t_D`. From (OS.9),

\[
\begin{aligned}
b
&\ge
{\tau_D\over\Delta}\left(D-{t_D\over2}\right)\\
&={D\tau_D\over\Delta}
\left(1-{t_D\over2D}\right).
\end{aligned}
\tag{OS.12}

For a uniform finite lower bound set

\[
\bar t_D:=h_*+D^{-1/3},
\]

\[
A_D:=D\tau_D\left(1-{\bar t_D\over2D}\right),
\qquad
k_D:={A_D\over\bar t_D}.
\tag{OS.13}

Since `t_D<=bar t_D`, Cauchy gives

\[
\boxed{
 B_{\rm upper}
 \ge k_Dm^2.
}
\tag{OS.14}

Indeed

\[
\sum_{\rm thick}{1\over\Delta_j}
\ge {m^2\over\sum_{\rm thick}\Delta_j}
\ge {m^2\over\bar t_D}.
\]

Moreover

\[
D\tau_D={D\over D+\sqrt{D^2-1}}\longrightarrow{1\over2},
\]

so

\[
\boxed{
 k_D\longrightarrow k_\infty:={1\over2h_*}.
}
\tag{OS.15}

The support ledger from the two-sided theorem now yields

\[
\boxed{
 G_{\rm low}
 \ge D+k_Dm^2-O(\sqrt D),
}
\tag{OS.16}

where `G_low` is total positive support progress along lower gates.

Deleting all `U` upper edges leaves at most `U+1` consecutive lower runs.

---

## 3. Do not split into thin-dominant and thick-dominant cases

Define the finite balancing constant

\[
c_D:=\left(2+{1\over4k_D}\right)^{-1/2}.
\tag{OS.17}

Then `c_D -> c_opt`, because (OS.15) gives

\[
{1\over4k_\infty}={h_*\over2}.
\]

If

\[
{s\over2}\ge(c_D-o(1))\sqrt D,
\]

then (OS.11) gives OPT-SQRT-SUPER-BRAID. It remains to consider the complementary case

\[
s\le 2c_D\sqrt D+o(\sqrt D).
\tag{OS.18}

The choice (OS.17) is exactly the value for which the following quadratic is nonnegative for every `m>=0`:

\[
\begin{aligned}
&D+k_Dm^2-c_D\sqrt D\,(2c_D\sqrt D+m)\\
&\qquad=
 k_D\left(m-{c_D\sqrt D\over2k_D}\right)^2
 \ge0.
\end{aligned}
\tag{OS.19}

To check the identity, (OS.17) is equivalent to

\[
1-2c_D^2={c_D^2\over4k_D}.
\]

Combining (OS.18) and (OS.19) gives

\[
D+k_Dm^2
\ge
c_D\sqrt D\,(s+m)-o(D).
\tag{OS.20}

Now average (OS.16) over at most `s+m+1` lower runs. The `O(sqrt(D))` numerator error is harmless uniformly:

- if `U<=D^(1/4)`, the `D/(U+1)` term is `Omega(D^(3/4))`, already much larger than `sqrt(D)`;
- if `U>D^(1/4)`, dividing the `O(sqrt(D))` error by `U+1` gives only `O(D^(1/4))=o(sqrt(D))`.

Therefore one all-lower run satisfies

\[
\boxed{
\operatorname{span}_N(R)
\ge(c_D-o(1))\sqrt D
=(c_{\rm opt}-o(1))\sqrt D.
}
\tag{OS.21}

This proves the optimized fork.

The improvement comes from using `s` and `m` together. The old proof first required `s>=3U/4` or `m>U/4`, then optimized inside the chosen case. Equation (OS.19) is the continuous minimax calculation that those fixed fractions approximate.

---

## 4. Near-unit matching inside OPT-SQRT-FACE

Let `R` be the run from (OS.21), with `r=|E(R)|`. Lower-edge slack is

\[
\sigma_e:=|e|-1>0.
\]

The common activation-time ledger gives

\[
\sum_{e\in R}\sigma_e\le t_D<h_*+D^{-1/3}.
\tag{OS.22}

Since support progress on an edge is at most `1+sigma_e`,

\[
r\ge(c_{\rm opt}-o(1))\sqrt D.
\tag{OS.23}

Fix `Lambda>1`. By Markov, all but at most `r/Lambda` run edges satisfy

\[
\sigma_e
\le {\Lambda t_D\over r}
\le
\left({\Lambda h_*\over c_{\rm opt}}+o(1)\right)D^{-1/2}.
\tag{OS.24}

A set of `g` edges in a path contains a matching of size at least `g/2-O(1)`. Therefore the good edges contain a vertex-disjoint matching of size

\[
\left({\Lambda-1\over2\Lambda}c_{\rm opt}-o(1)\right)\sqrt D.
\]

Every endpoint remains an old fully inactive source point in the original outer contact face. This proves (OS.3)--(OS.4).

---

## 5. Diameter-topology consequences

The braid branch consists of source chords strictly longer than `sqrt(D^2-1)`, so the previous forest-transversal theorem applies verbatim. In particular:

1. every braid endpoint lies outside the force hull `F`;
2. every braid chord crosses every actual diameter chord;
3. the actual diameter graph cannot be in the cyclic Woodall case;
4. it is a caterpillar forest;
5. every connected diameter component has its two bipartition classes in one complementary pair of braid boundary cells.

Thus the cyclic Woodall topology forces OPT-SQRT-FACE with the improved constant `c_opt`.

If the canonical lower bound `h>=(1/4-o(1))D` for the number of actual diameter edges is also inserted, the braid branch now gives at least

\[
\boxed{
\left({c_{\rm opt}\over4}-o(1)\right)D^{3/2}
=(0.169813838846910\ldots-o(1))D^{3/2}
}
\tag{OS.25}

proper braid/actual-diameter crossing incidences.

---

## 6. What remains open

This strengthens the normal form but does not close C-II.

- In the cyclic Woodall topology, the surviving FREE object is now an outer-face all-lower run with support span `0.679255... sqrt(D)` and a correspondingly denser inverse-square-root near-unit matching.
- In the forest topology, the alternative is a larger exact-threshold superdiameter transversal, still localized against the diameter caterpillars by complementary braid cells.

The next closure step must spend one of those objects against existing outer-walk, force-hull, or source-preserving motion currency. Merely improving the square-root constant again will not by itself close the branch.

**Disposition:** replaced the fixed `3/4`/`1/4` thin-thick split by the exact continuous quadratic balance. The common square-root coefficient rises to `0.679255355387642...`; the superbraid uses the exact `sqrt(D^2-1)` threshold; and the face branch inherits a parameterized near-unit matching bound.
