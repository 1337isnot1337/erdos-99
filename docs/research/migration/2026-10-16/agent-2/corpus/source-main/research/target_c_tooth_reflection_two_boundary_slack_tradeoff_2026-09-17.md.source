# Target C-II — two-sided FREE ancestry has one bounded boundary-slack budget

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of two-sided inactive gate absorption  
**Scope:** non-anchored FREE reflection modules at `eta=3/26`, in the all-inactive ancestry branch  
**Dependencies:** two-sided inactive gate absorption; FREE blocker-cap root-depth bound; contact-minimal normalization  
**Certificate:** `research/verify_target_c_tooth_reflection_two_boundary_slack_tradeoff_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The two-sided activation theorem records an `O(1)` total slack only for the lower-gate edges. The same activation-time telescope controls the diameter slack of the upper-gate edges as well.

This gives one common ledger for both metric boundaries. It also gives a scale tradeoff: along one all-inactive ancestry reaching support depth `D-1-o(1)`, either there are many original source pairs extremely close to the diameter boundary, or there is one long consecutive run of original source pairs extremely close to the unit boundary.

Use the notation of the two-sided absorption theorem. Thus

\[
0=s_0<s_1<\cdots<s_m\le t_D,
\qquad
\Delta_j=s_{j+1}-s_j,
\]

with

\[
t_D=\delta+D^{-1/3},
\qquad
0<\delta<h_*:=\frac{\sqrt{303}}{52}.
\]

For the ancestry edge `z_j z_{j+1}`, put

\[
d_j=z_j-\Delta_jN-z_{j+1}.
\]

Every ancestry edge is either a lower gate, with `|d_j|=1`, or an upper gate, with `|d_j|=D`. All ancestry vertices are fully inactive in the original source in the branch considered here.

The new global ledger is

\[
\boxed{
\sum_{j\in E_{\rm low}}
\bigl(|z_j-z_{j+1}|-1\bigr)
+
\sum_{j\in E_{\rm up}}
\bigl(D-|z_j-z_{j+1}|\bigr)
\le t_D
<h_*+D^{-1/3}.
}
\tag{BS.1}
\]

Thus the lower and upper near-boundary defects compete for the same bounded activation-time budget.

---

## 1. Upper-gate diameter slack is at most its activation-time increment

For a lower edge, the earlier theorem already gives

\[
1<|z_j-z_{j+1}|
\le1+\Delta_j,
\]

and hence

\[
0<\sigma_j:=|z_j-z_{j+1}|-1\le\Delta_j.
\tag{BS.2}
\]

Now take an upper edge. At its activation event,

\[
|d_j|=D,
\qquad
z_j-z_{j+1}=d_j+\Delta_jN.
\tag{BS.3}
\]

Because both endpoints were fully inactive in the original source, the original pair is not an actual diameter pair, so

\[
|z_j-z_{j+1}|<D.
\tag{BS.4}
\]

The reverse triangle inequality applied to (BS.3) gives

\[
|z_j-z_{j+1}|
\ge D-\Delta_j.
\tag{BS.5}
\]

Therefore its original diameter deficit satisfies

\[
\boxed{
0<\rho_j:=D-|z_j-z_{j+1}|\le\Delta_j.
}
\tag{BS.6}
\]

The activation increments telescope:

\[
\sum_{j=0}^{m-1}\Delta_j=s_m\le t_D.
\tag{BS.7}
\]

Summing (BS.2) and (BS.6) over their disjoint edge classes proves (BS.1).

The point is finite and exact: no averaging over different modules and no asymptotic geometric estimate is used after the two-sided activation theorem has produced the ancestry.

---

## 2. Exact support-direction/backtracking identity

There is a second ledger on the same ancestry.

Let

\[
a_v=H-N\cdot v,
\qquad
A:=a_{z_m}-a_{z_0},
\qquad
S:=\sum_j\Delta_j=s_m.
\]

For a lower edge put

\[
c_j:=N\cdot d_j\in[0,1],
\qquad
\epsilon_j:=1-c_j\in[0,1].
\]

For an upper edge, the first-hit sign theorem gives `N dot d_j<0`; put

\[
b_j:=-N\cdot d_j>0.
\]

Let `L` be the number of lower edges. Since

\[
a_{z_{j+1}}-a_{z_j}=N\cdot d_j+\Delta_j,
\]

summing gives the exact identity

\[
\boxed{
\sum_{j\in E_{\rm low}}\epsilon_j
+
\sum_{j\in E_{\rm up}}b_j
=L-A+S.
}
\tag{BS.8}
\]

The left side is nonnegative. It records two distinct inefficiencies:

- a lower event pays `epsilon_j` when its exact unit event vector fails to point fully inward along `N`;
- an upper event pays `b_j` for support backtracking.

The existing near-opposite theorem gives

\[
A>D-O(\sqrt D),
\qquad
L\ge D-O(\sqrt D),
\tag{BS.9}
\]

but does not give a useful source-wide upper bound on `L`. Accordingly, (BS.8) is recorded as an exact ledger, not as an unconditional small-angle theorem. In any subcase where `L=D+o(D)`, it immediately implies that the total lower directional defect plus total upper backtracking is `o(D)`.

---

## 3. A scale tradeoff between upper near-diameters and a consecutive lower run

Let

\[
U:=|E_{\rm up}|,
\qquad
L:=|E_{\rm low}|.
\]

The near-opposite theorem gives

\[
L\ge D-O(\sqrt D).
\tag{BS.10}
\]

Fix an integer scale `M=M_D` with

\[
1\ll M\ll D.
\tag{BS.11}
\]

There are two cases.

### Case A: `U >= M`

By (BS.1), the sum of all upper deficits is at most `t_D`. Hence at least `U/2` upper edges satisfy

\[
\rho_j\le\frac{2t_D}{U}
\le\frac{2t_D}{M}.
\tag{BS.12}
\]

The ancestry edges split by index parity into two matchings. Therefore one parity contains at least `U/4-O(1)` of these good upper edges. In the original source this yields a vertex-disjoint matching of fully inactive pairs satisfying

\[
\boxed{
D-\frac{2t_D}{M}
\le |x-y|<D,
}
\tag{BS.13}
\]

with size at least

\[
\boxed{
\frac{M}{4}-O(1).
}
\tag{BS.14}
\]

At the activation terminal configuration, before strictification, every corresponding ancestry edge is an exact diameter edge because both endpoints move with the same velocity after the child activates.

### Case B: `U < M`

Deleting the upper edges partitions the `L` lower edges into at most

\[
U+1\le M
\]

consecutive all-lower runs. Hence one run has length

\[
R\ge\frac{L}{M}
\ge\frac{D-O(\sqrt D)}{M}.
\tag{BS.15}
\]

The lower slacks on this run sum to at most `t_D`. At least `R/2` of its edges therefore satisfy

\[
\sigma_j\le\frac{2t_D}{R}
\le
\frac{2t_DM}{D-O(\sqrt D)}.
\tag{BS.16}
\]

Parity thinning inside this consecutive run gives a vertex-disjoint matching of size at least

\[
\boxed{
\frac{D-O(\sqrt D)}{4M}-O(1)
}
\tag{BS.17}
\]

whose original source pairs satisfy

\[
\boxed{
1<|x-y|
\le
1+
\frac{2t_DM}{D-O(\sqrt D)}.
}
\tag{BS.18}
\]

Unlike the source-wide lower matching from the previous theorem, these pairs lie inside one consecutive all-lower ancestry run. At the activation terminal configuration that whole run is an exact unit-contact chain. No upper-gate jump occurs inside it.

Equations (BS.13)--(BS.18) are the scale tradeoff.

---

## 4. Balanced square-root form

Take

\[
M=\lfloor\sqrt D\rfloor.
\]

Since

\[
2h_*=rac{\sqrt{303}}{26}
=0.6694959686742\ldots,
\]

one non-anchored FREE module in the all-inactive branch forces at least one of:

\[
\boxed{
\left(\frac14-o(1)\right)\sqrt D
\text{ vertex-disjoint fully inactive pairs with }
D-|x-y|
\le
(0.6694959687\ldots+o(1))D^{-1/2};
}
\tag{BS.19}
\]

or

\[
\boxed{
\left(\frac14-o(1)\right)\sqrt D
\text{ vertex-disjoint fully inactive pairs in one consecutive lower run with }
|x-y|-1
\le
(0.6694959687\ldots+o(1))D^{-1/2}.
}
\tag{BS.20}
\]

Thus one FREE module alone contains a square-root matching at one of the two metric boundaries, with inverse-square-root additive slack.

---

## 5. Reflection-matched quarter-power scale

The shallow-tooth reflection extraction naturally has a `D^{1/4}` scale. Taking

\[
M=\lfloor D^{1/4}\rfloor
\]

in the same dichotomy gives either

\[
\boxed{
\left(\frac14-o(1)\right)D^{1/4}
\text{ vertex-disjoint fully inactive pairs with }
D-|x-y|
\le
(2h_*+o(1))D^{-1/4},
}
\tag{BS.21}
\]

or one consecutive all-lower run containing a vertex-disjoint matching of size

\[
\boxed{
\left(\frac14-o(1)\right)D^{3/4}
}
\tag{BS.22}

with

\[
\boxed{
|x-y|-1
\le
(2h_*+o(1))D^{-3/4}.
}
\tag{BS.23}

The first alternative is on the same additive `D^{-1/4}` diameter-slack scale as the earlier pre-center tangent-gate theorem, but it is obtained after allowing arbitrary inactive upper gates to be absorbed. The second alternative is much denser and much closer to the unit boundary than the earlier fixed-`K/D` source-wide matching, at the price of localizing to one consecutive lower run.

These are still original-source inequalities. The exact unit/diameter equalities occur only in the finite activation deformation.

---

## 6. What this does and does not close

The theorem does not identify the lower pairs with the one-row Horn `LOWER` blockers from the separate strong-TB1 branch. It also does not identify the upper pairs with actual source-diameter edges. Those imports would require additional hypotheses not present in the FREE reflection ancestry.

What is new is that inactive upper gates no longer merely disappear into the absorption procedure. Their original diameter deficits are charged to the same telescoping budget as the lower unit excesses. Consequently a long all-inactive ancestry cannot simultaneously have many substantially subdiametral upper jumps and many substantially superunit lower steps.

The next finite-exchange seam is now scale-specific:

1. in the upper-rich case, exploit a large matching of old fully inactive `D-o(1)` pairs whose corresponding deformed gate edges are exact diameters;
2. in the upper-poor case, exploit one very long consecutive exact-unit gate chain whose original positions differ from those exact contacts by total activation time `O(1)`.

A closure still requires a source-preserving argument or a rigorous bridge from one of these two structures to the active force hull / canonical train system.

**Disposition:** proved a common `O(1)` lower-plus-upper boundary-slack ledger for every all-inactive two-sided FREE ancestry, an exact support/backtracking identity, and a tunable matching dichotomy. C-II and Level I remain open.
