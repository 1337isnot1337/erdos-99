<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cb135653fb24b393e5f16238de237cced6e2ff8e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_seven_spaced_horn_propagation_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d3cb536a636e3062ffc0abc03b72c472e9cc6e1d133ff31b24fd1a299b38414c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the six-row bound upgrades the Horn subsystem to seven-spacing

**Date:** 2026-09-17  
**Status:** proof-only quantitative strengthening of the exact-swap Horn chain; no canonical promotion claimed  
**Scope:** one-sign strong-TB1 exact swaps through `t=(q-k)/D<=1.8687`  
**Dependencies:** six-row Oler short-blocker theorem; simultaneous exact-swap active-constraint decoupling; genuine-upper binary shell bound; Horn reduction; poison-forest theorem; lower local-ladder theorem; upper dense-grid localization theorem  
**Certificate:** `research/verify_target_c_high_t_tb1_seven_spaced_horn_propagation_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The historical Horn reduction retained one residue class modulo fifteen because the available short-pair theorem only gave LOWER path bandwidth at most fourteen. The new Oler-center argument gives bandwidth at most six. Nothing else in the finite-swap decoupling needs spacing fifteen: the retained layers only need to be nonadjacent, and a LOWER blocker must not be able to contain two retained endpoints.

Therefore the same construction can retain one residue class modulo seven.

Let

\[
s_0={791\over320{,}000{,}000}.
\]

The one-sign strong-TB1 population has size

\[
|M_D|>{s_0\over2}D-o(D).
\]

Keeping a largest residue class modulo seven and deleting the `O(1)` coordinates incident to genuine upper binary exceptions gives a retained exact-swap system `P_D^{(7)}` with

\[
\boxed{
|P_D^{(7)}|>
(\gamma_7-o(1))D,
\qquad
\gamma_7={s_0\over14}
={113\over640{,}000{,}000}
=1.765625\times10^{-7}.
}
\tag{SP.1}
\]

This is larger than the previous Horn density by the exact factor

\[
\boxed{{\gamma_7\over\gamma_{15}}={15\over7}.}
\tag{SP.2}
\]

Every two retained coordinates differ by at least seven, while every inverse-`D` near-unit blocker has path bandwidth at most six. Hence all LOWER singleton blockers are again permanent one-coordinate constraints, and the no-new-two-coordinate-obstruction argument is unchanged.

The entire Horn poisoning theorem therefore reruns with `gamma_7`. It forces one of:

\[
\boxed{
N_{\rm permanent\ lower}>
\left({\gamma_7\over4}-o(1)\right)D
=(4.4140625\times10^{-8}-o(1))D,
}
\tag{SP.3}
\]

\[
\boxed{
N_{\rm permanent\ upper}>
\left({\gamma_7\over8}-o(1)\right)D
=(2.20703125\times10^{-8}-o(1))D,
}
\tag{SP.4}
\]

or

\[
\boxed{
N_{\rm implication\ forest}>
\left({\gamma_7\over2}-o(1)\right)D
=(8.828125\times10^{-8}-o(1))D.
}
\tag{SP.5}
\]

The local-ladder and upper-localization steps also improve without any structural change. In the LOWER branch, after the orientation and low-cost extractions there are

\[
\boxed{
\left({\gamma_7\over16}-o(1)\right)D
=(1.103515625\times10^{-8}-o(1))D
}
\tag{SP.6}
\]

pairwise-disjoint support windows, now of depth at most six. One fixed complete stopped train belongs to the pure common-column family of more than

\[
\boxed{
\left(
{\gamma_7\over16}{0.6436\over3.0605}-o(1)
\right)D
=
(2.32060988809\ldots\times10^{-9}-o(1))D
}
\tag{SP.7}
\]

such windows.

In either UPPER branch, the common owned upper family may be taken with density `gamma_7/8`. Repeating the long-support/common-cut versus short-support/local-window localization gives a same-type SIGNED or THIN population of more than

\[
\boxed{
(c_{*,7}-o(1)){D\over\log D},
\qquad
c_{*,7}
={\gamma_7\over48T_*}
={113\over94{,}018{,}560{,}000}
=1.20189035016\ldots\times10^{-9},
}
\tag{SP.8}
\]

where

\[
T_*=3.0605={6121\over2000}.
\]

All later SIGNED/THIN geometric reductions inherit this larger input coefficient. Their polynomial exponents and normal forms do not change.

---

## 1. Seven-spacing is sufficient for the finite-swap reduction

Partition the one-sign coordinate indices into their seven residue classes. A largest class `P_D^0` satisfies

\[
|P_D^0|\ge{|M_D|\over7}
>{s_0\over14}D-o(D).
\tag{SP.9}
\]

If `i,j in P_D^0` are distinct, then

\[
\boxed{|i-j|\ge7.}
\tag{SP.10}
\]

In particular the layers are nonadjacent, so the simultaneous exact-swap active-contact/old-diameter decoupling theorem still applies.

Now let `xy` be a LOWER blocker of the singleton swap at retained coordinate `i`. The exact local window gives

\[
1<|xy|\le1+O(D^{-1}).
\]

The Oler short-pair theorem gives

\[
|\operatorname{reg}(x)-\operatorname{reg}(y)|\le6.
\tag{SP.11}
\]

Thus the other endpoint cannot lie in another retained layer. Relative to `P_D^0`, every LOWER blocker depends on one Boolean coordinate only and is unaffected by all other retained swaps.

The source-wide genuine-upper binary theorem still removes only `O(1)` exceptional source pairs. Delete their incident retained coordinates and call the result `P_D^{(7)}`. Equations (SP.9)--(SP.10) survive up to `O(1)`, proving (SP.1).

The exact two-coordinate implication/Horn argument used no further numerical property of the old spacing `15`. Hence it applies verbatim on `P_D^{(7)}`.

---

## 2. Poison-forest constants with `gamma_7`

Let `F_D` be the forbidden set and `I_D` the Horn implication digraph on `P_D^{(7)}`. As before, canonical minimality implies every sink SCC of `I_D` meets `F_D`, hence every retained coordinate has a directed implication path to `F_D`.

If

\[
|F_D|<{|P_D^{(7)}|\over2},
\]

shortest paths to `F_D` select an acyclic implication forest with

\[
|E_{forest}|=|P_D^{(7)}|-|F_D|
>{|P_D^{(7)}|\over2},
\]

which yields (SP.5).

If instead

\[
|F_D|\ge{|P_D^{(7)}|\over2},
\]

at least half of the chosen forbidden incidences have one common metric type.

For LOWER, (SP.11) plus seven-spacing means one lower source pair poisons at most one retained coordinate. Therefore a LOWER winner gives at least

\[
{|P_D^{(7)}|\over4}
\]

distinct blockers, proving (SP.3).

For UPPER, one source pair has at most two retained endpoint coordinates, so an UPPER winner gives at least

\[
{|P_D^{(7)}|\over8}
\]

distinct blockers, proving (SP.4).

The proof is identical to the existing poison-forest theorem after substituting `gamma_7` for the old retained density.

---

## 3. LOWER local ladders become six-deep

Assume the permanent LOWER branch (SP.3). Split blockers according to whether the nonowner endpoint lies path-left or path-right of the owner and keep the larger class. Its density is more than `gamma_7/8`.

The owners are seven-spaced and every support interval has length at most six. For a right-oriented blocker owned at `i`, its support ends by cut `i+6`. If the next owner is `i'>=i+7`, its support begins at cut `i'+1`. Hence the intervals are disjoint. The left-oriented case is symmetric.

The global train-defect and terminal-variation budgets may therefore be spent independently on these windows exactly as in the previous local-ladder theorem. Keeping the low-cost half gives (SP.6).

Each good six-deep window retains a common pure column family of

\[
(0.6436-o(1))D
\]

trains with uniform inverse-`D` angular error on every support row. Counting blocker-window/train incidences against the global complete-train count

\[
T_D<(T_*+o(1))D
\]

gives (SP.7).

The exact coefficient is

\[
{\gamma_7\over16}{0.6436\over T_*}
={181817\over78{,}348{,}800{,}000{,}000}
=2.32060988809\ldots\times10^{-9}.
\tag{SP.12}
\]

---

## 4. UPPER localization coefficient

Both UPPER poison outcomes contain an injectively owned upper family of density at least

\[
\delta_{0,7}:={\gamma_7\over8}.
\tag{SP.13}
\]

The upper dense-grid localization proof uses only:

- injective ownership;
- exact interval support;
- the global row/train defect budgets;
- `m<=T_*D+o(D)`;
- and the linear input density `delta_0`.

Its rich-cut threshold is `delta_0/(3T_*)`, followed by one factor `1/2` for the SIGNED/THIN type split. Therefore the localized same-type coefficient is

\[
{\delta_{0,7}\over6T_*}
={\gamma_7\over48T_*}
=c_{*,7},
\]

which is (SP.8).

This is again exactly `15/7` times the historical 15-spaced coefficient.

---

## 5. Downstream effect and remaining bottleneck

The seven-spaced theorem improves constants but does not remove any of the three live Horn geometries. Their current structural normal forms remain:

```text
LOWER:
    linear permanent near-unit blockers;
    now support depth <= 6;
    pairwise-disjoint oriented local ladders;
    one fixed train threads a linear subfamily.

UPPER / THIN:
    superdiameter thrackle / growing braid and train-fence normal forms.

UPPER / SIGNED:
    D/log D localization;
    D^(1/4-o(1)) crossing braid;
    COMMON-CUT row/column uniqueness or LOCAL-WINDOW column-cell remainder.
```

The main qualitative gain is on LOWER: every surviving local obstruction now lives in at most six co-phased rows rather than fourteen, while the exact-swap Horn subsystem itself is more than twice as dense.

The next useful LOWER target is therefore a finite local classification of a strict near-unit pair crossing at most six rows of an inverse-`D` near-equilateral ladder. Any reduction of those blockers to actual missing rhombus diagonals, or any exclusion of support depth at least two, would immediately sharpen the permanent-LOWER normal form further.

**Disposition:** replaced modulo-fifteen thinning by modulo-seven thinning, propagated the resulting `15/7` density gain through the poison forest, LOWER local ladders, and UPPER dense-grid localization, and reduced every good permanent-LOWER support window from depth fourteen to depth six. C-II and Level I remain open.
