<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b3f6fb4a0703dfdd97deacdd821984d1e70f3584", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_exact_swap_slack_ratio_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0d17e24dc84b37efc8bd60dff84e4a381657dcd3688c52f412840ffc744fc228"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — contact minimality already obstructs the exact TB1 swap, with a slack-ratio sign law

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the one-sign side of the strong-TB1 exact contact-swap branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** TB1 cone collapse; exact contact-swap algebra; contact-minimal canonical normalization; coupled host transverse margin; disjoint physical path layers  
**Certificate:** `research/verify_target_c_high_t_tb1_exact_swap_slack_ratio_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The contact-swap branch previously used a tiny overswap to avoid the diameter-pair-minimality issue at the exact second contact intersection. A limiting argument shows that this extra displacement is unnecessary even if only **contact minimality** is used.

At every one-sign strong-TB1 interface, the exact swap itself is already blocked by a previously strict pair. Thus the inactive witness window is governed by the actual local swap length

\[
q_i=|a_i+b_i|=2\sin{\epsilon_i\over2},
\qquad
\epsilon_i:=\pi-\angle(a_i,b_i),
\]

rather than by the slightly longer overswap. Since

\[
q_i\le\epsilon_i
<{31.4\times10^6\over D}+o(D^{-1}),
\]

the old asymptotic window remains valid, but each witness now carries a sharper **local scale** `q_i`.

The exact swap also gives a useful sign law. Orient a witness vector `r` from its fixed endpoint toward its endpoint in the translated layer, and write the swap as

\[
r\longmapsto r-q_iw_i.
\]

If an exact-swap witness is near the diameter and

\[
\xi_i:=D-|r|,
\]

then

\[
{r\cdot w_i\over D}
\le
- {\xi_i\over q_i}
+ {1+(\xi_i/q_i)^2\over2}{q_i\over D}.
\]

Because `q_i=O(D^-1)`, a witness whose diameter slack is a fixed fraction of its local swap length has a fixed **negative** transverse projection. For every fixed `0<tau<1`,

\[
\xi_i\ge\tau q_i
\quad\Longrightarrow\quad
r\cdot w_i\le-(\tau-o(1))D.
\]

Therefore the near-diameter inactive branch has a new internal fork:

```text
substantial relative slack:
    an inactive almost-diameter points macroscopically opposite the strong TB1 blocker;

or

ultra-small relative slack:
    D-|r| < tau q_i,
    hence an arbitrarily smaller inverse-D diameter-slack window after tau is chosen.
```

This does not turn the inactive almost-diameter into an actual diameter edge, and no thrackle conclusion is inferred from it. It does, however, replace an unstructured `O(D^-1)` witness by either a signed almost-diameter or a strictly thinner inactive shell.

---

## 1. Exact swap and the one-sign diameter margin

At a one-sign strong-TB1 interface `i`, let the rooted unit boundary-contact vectors be `a_i,b_i`, and put

\[
q_i:=|a_i+b_i|>0,
\qquad
w_i:={a_i+b_i\over q_i}.
\tag{ES.1}
\]

For `lambda>=0`, translate the physical layer `R_i` by

\[
v_i(\lambda)=-\lambda q_iw_i=-\lambda(a_i+b_i).
\tag{ES.2}
\]

Direct expansion gives

\[
\boxed{
|a_i+v_i(\lambda)|^2
=|b_i+v_i(\lambda)|^2
=1+q_i^2\lambda(\lambda-1).
}
\tag{ES.3}
\]

At `lambda=1`, the two boundary contacts are swapped exactly:

\[
a_i+v_i(1)=-b_i,
\qquad
b_i+v_i(1)=-a_i.
\tag{ES.4}

For `lambda>1`, both boundary-contact families are strictly opened.

Let `h` be any moving old actual diameter. Orient its inward vector `n_h` so that the layer translation contributes `n_h\cdot v`. On a one-sign interface the audited host theorem gives

\[
\boxed{
n_h\cdot w_i\ge(c_H-o(1))D,
\qquad c_H=0.453819885927\ldots .}
\tag{ES.5}

Hence

\[
|r_h(v_i(\lambda))|^2-D^2
=-2\lambda q_i(n_h\cdot w_i)+\lambda^2q_i^2.
\tag{ES.6}

Since

\[
q_i=O(D^{-1}),
\tag{ES.7}

for all sufficiently large sources (ES.6) is strictly negative uniformly for `1<=lambda<=2`, say. Thus every moving old diameter is shortened not only at the exact swap but throughout a fixed one-sided neighborhood past it.

Every nonswitching pair is invariant exactly under the layer translation.

---

## 2. Contact minimality forces a previously strict pair at the exact swap

Fix one finite source and one one-sign interface `i` after the large-`D` threshold from Section 1.

For every sufficiently small `epsilon>0`, consider the overswap endpoint

\[
lambda=1+\epsilon.
\]

Suppose every pair that was previously strict still had distance strictly between `1` and `D` at that endpoint. Then:

- all old contacts away from the two boundary trains are unchanged;
- by (ES.3), both boundary train contact families are strictly opened;
- every moving old actual diameter is strictly shortened by (ES.6);
- every nonswitching old diameter is unchanged;
- no previously strict pair creates a new unit contact or reaches diameter `D`.

If a nonswitching old diameter exists, the new source still has diameter exactly `D` but has fewer unit contacts, contradicting contact minimality among global diameter minimizers. If no nonswitching old diameter exists, every old diameter has shortened and every old nondiameter remains below `D`, so the new source has diameter below `D`, contradicting global diameter minimality.

Therefore for every sufficiently small `epsilon>0` some previously strict pair violates one of the two distance inequalities at `lambda=1+epsilon`.

There are only finitely many source pairs. Choose a sequence

\[
epsilon_n\downarrow0.
\]

By finite pigeonhole, one previously strict pair `xy` is a violating pair for infinitely many `n`; after taking a further subsequence, it violates the same boundary (`1` or `D`) each time. Pair distances depend continuously on `lambda`. Hence at the exact swap itself,

\[
\boxed{
|x(1)-y(1)|\le1
\quad\text{or}\quad
|x(1)-y(1)|\ge D.
}
\tag{ES.8}

The pair must straddle `R_i`; otherwise it is invariant and cannot violate a constraint that was strict initially.

This proves the exact-swap obstruction using contact minimality alone. No diameter-pair-minimal tie-break is needed.

---

## 3. The exact local witness windows

Orient the exact-swap witness from its fixed endpoint to its endpoint inside `R_i`. Its initial relative vector is `r`, and at the exact swap

\[
r'=r-q_iw_i.
\tag{ES.9}

Let

\[
ell:=|r|.
\]

Because the pair was previously strict,

\[
1<\ell<D.
\tag{ES.10}

If the lower constraint is violated at the exact swap, then `|r'|<=1`. The triangle inequality gives

\[
\boxed{1<\ell\le1+q_i.}
\tag{ES.11}

If the upper constraint is violated, `|r'|>=D`, and the reverse triangle inequality gives

\[
\boxed{D-q_i\le\ell<D.}
\tag{ES.12}

Thus every one-sign strong-TB1 interface carries a previously strict witness in a local exact-swap window of width `q_i`, with

\[
\boxed{
q_i
=2\sin{\epsilon_i\over2}
\le\epsilon_i
<{31.4\times10^6\over D}+o(D^{-1}).
}
\tag{ES.13}

The former global `31.4e6/D` window remains a valid corollary, but (ES.11)--(ES.13) preserve the actual non-antipodality scale of the individual interface.

---

## 4. Exact directional law for a near-unit witness

Assume first that the exact swap reaches the unit lower boundary. From

\[
|r-q_iw_i|^2\le1
\]

we obtain

\[
\boxed{
r\cdot w_i
\ge{\ell^2-1+q_i^2\over2q_i}.}
\tag{ES.14}

Write

\[
\zeta_i:=\ell-1,
\qquad
x_i:={\zeta_i\over q_i}\in(0,1].
\tag{ES.15}

Substituting `ell=1+x_iq_i` gives the exact identity

\[
{\ell^2-1+q_i^2\over2q_i}
=x_i+{x_i^2+1\over2}q_i.
\tag{ES.16}

Hence

\[
\boxed{r\cdot w_i\ge x_i={\ell-1\over q_i}.}
\tag{ES.17}

In particular, if `ell-1>=tau q_i` for a fixed `tau in (0,1)`, then

\[
\boxed{r\cdot w_i\ge\tau.}
\tag{ES.18}

This is an exact signed statement, although its scale is only order one because the witness itself is a near-unit pair.

---

## 5. Exact directional law for a near-diameter witness

Now assume the exact swap reaches the diameter upper boundary. From

\[
|r-q_iw_i|^2\ge D^2
\]

we get

\[
\boxed{
r\cdot w_i
\le{\ell^2-D^2+q_i^2\over2q_i}.}
\tag{ES.19}

Let

\[
\xi_i:=D-\ell,
\qquad
x_i:={\xi_i\over q_i}\in(0,1].
\tag{ES.20}

Then `ell=D-x_iq_i`, and (ES.19) becomes

\[
\boxed{
{r\cdot w_i\over D}
\le
-x_i+{x_i^2+1\over2}{q_i\over D}.}
\tag{ES.21}

Since `0<x_i<=1`,

\[
0\le{x_i^2+1\over2}{q_i\over D}
\le{q_i\over D}
=O(D^{-2}).
\tag{ES.22}

Therefore for every fixed `0<tau<1`,

\[
\boxed{
D-\ell\ge\tau q_i
\quad\Longrightarrow\quad
r\cdot w_i\le-(\tau-o(1))D.}
\tag{ES.23}

The sign is opposite the selected strong-TB1 blocker, whose inward diameter vector obeys

\[
n_i\cdot w_i\ge(c_H-o(1))D.
\tag{ES.24}

Again, `r` is not asserted to be an actual diameter vector. Equation (ES.23) is a metric sign law for an inactive pair that is within `q_i` of diameter.

---

## 6. Parameterized thin-shell fork inside the near-diameter branch

Fix any constant

\[
0<\tau<1.
\tag{ES.25}

Every exact-swap near-diameter witness satisfies exactly one of

\[
\boxed{
\text{SIGNED:}
\quad
r\cdot w_i\le-(\tau-o(1))D,
}
\tag{ES.26}

or

\[
\boxed{
\text{THIN:}
\quad
0<D-|r|<\tau q_i.
}
\tag{ES.27}

Using (ES.13), the second case lies in the narrower global shell

\[
\boxed{
0<D-|r|
< {31.4\times10^6\tau\over D}+o(D^{-1}).}
\tag{ES.28}

A useful concrete choice is

\[
\tau_0:={c_H\over2}
=0.2269099429635\ldots .
\tag{ES.29}

Then SIGNED gives

\[
r\cdot w_i
\le-(0.2269099429635\ldots-o(1))D,
\tag{ES.30}

while THIN gives

\[
\boxed{
0<D-|r|
<{7.12497221\times10^6\over D}+o(D^{-1}).}
\tag{ES.31}

Thus a substantial-relative-slack almost-diameter is transversely opposed to the strong blocker by a fixed macroscopic amount; avoiding that sign forces the inactive diameter shell to shrink by the factor `c_H/2`.

The theorem is parameterized in `tau`, so the shell factor can be made arbitrarily small at the price of a smaller fixed negative projection in the SIGNED alternative.

---

## 7. Global density consequence

Suppose the one-sign half of the strong-TB1 contact-swap fork occurs. Its interface population has size

\[
>{s_0\over2}D-o(D),
\qquad
s_0={791\over320{,}000{,}000}.
\tag{ES.32}

A fixed source pair straddles at most two disjoint physical path layers. Therefore exact-swap witnesses selected at these interfaces contain more than

\[
\boxed{
{s_0\over4}D-o(D)
=(6.1796875\times10^{-7})D-o(D)
}
\tag{ES.33}

**distinct** previously strict pairs, each retaining one representative interface tag `i` and its local scale `q_i`.

Split these distinct witnesses into near-unit and near-diameter types. One type has size

\[
\boxed{
>{s_0\over8}D-o(D)
=(3.08984375\times10^{-7})D-o(D).}
\tag{ES.34}

If the near-diameter type is the larger type, split once more according to SIGNED/THIN at any fixed `tau`. One subclass then has size

\[
\boxed{
>{s_0\over16}D-o(D)
=(1.544921875\times10^{-7})D-o(D).}
\tag{ES.35}

For `tau=tau_0=c_H/2`, that final subfamily therefore consists either of linearly many tagged inactive almost-diameters with transverse projection at most `-(c_H/2-o(1))D`, or linearly many tagged inactive pairs lying within `7.125e6/D+o(D^-1)` of the diameter.

The multiplicity-two argument is unchanged by passing from overswap witnesses to exact-swap witnesses: a pair changes under layer `R_i` exactly when one endpoint belongs to `R_i`, and each endpoint belongs to at most one physical path layer.

---

## 8. Scope and next target

This result does **not** prove that a near-diameter witness is an active diameter edge. Consequently it does not invoke the convex diameter-thrackle property, C67 diameter-direction spacing, or KKT stress on that inactive pair.

What it removes is weaker but exact:

1. the one-sign branch no longer needs diameter-pair minimality to obtain its inactive witness;
2. the witness scale is the actual local non-antipodality `q_i`, not only a global `O(D^-1)` envelope;
3. an inactive near-diameter with non-negligible relative slack already points macroscopically against the local TB1 blocker.

The remaining layer-tag problem can now be attacked in two distinct regimes. The SIGNED regime supplies a virtual opposite transverse ray at the same tagged layer, but with length just below `D`; the THIN regime supplies a much narrower inactive shell, and `tau` can be chosen before the global density split. A useful next step is to combine either regime with the common ordered near-equilateral train ladder, rather than treating all inactive `O(D^-1)` witnesses identically.

**Disposition:** strengthened the one-sign TB1 contact-swap branch to exact-swap obstruction under contact minimality alone and derived a parameterized directional/thin-shell fork for inactive near-diameter witnesses. C-II and Level I remain open.
